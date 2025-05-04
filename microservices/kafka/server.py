import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
from uuid import uuid4

from kafka import KafkaConsumer, KafkaProducer  # type: ignore
from opentelemetry import trace
from opentelemetry.context import attach
from opentelemetry.exporter.otlp.proto.http.trace_exporter import (
    OTLPSpanExporter,
)
from opentelemetry.propagate import extract, inject
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({SERVICE_NAME: "kafka-chain-server"})
    )
)
tracer = trace.get_tracer(__name__)

otlp_exporter = OTLPSpanExporter(
    endpoint="http://jaeger-collector.default.svc.cluster.local:4318/v1/traces"
)
trace.get_tracer_provider().add_span_processor(  # type: ignore
    BatchSpanProcessor(otlp_exporter)
)

KAFKA_BROKER = "kafka.kafka.svc.cluster.local:9092"
TOPIC = "trace-chain"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode(),
)
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    value_deserializer=lambda m: json.loads(m.decode()),
    group_id="chain-consumer",
)

HOST = "0.0.0.0"
PORT = 3000


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        request_id = str(uuid4())

        if self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return

        with tracer.start_as_current_span("incoming_request") as span:
            span.set_attribute("request.id", request_id)
            span.add_event("Enqueuing first event")

            headers: dict[str, str] = {}
            inject(headers)

            event = {
                "request_id": request_id,
                "hop": 1,
                "trace_context": headers,
            }
            producer.send(TOPIC, event)

            response = json.dumps(
                {"status": "queued", "request_id": request_id}
            ).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)


def process_messages() -> None:
    for msg in consumer:
        payload = msg.value
        hop = payload.get("hop", 0)
        request_id = payload.get("request_id")
        headers = payload.get("trace_context", {})

        ctx = extract(headers)
        attach(ctx)

        with tracer.start_as_current_span("process_hop") as span:
            span.set_attribute("request.id", request_id)
            span.set_attribute("hop", hop)
            span.add_event(f"Processing hop {hop}")
            time.sleep(0.2)

            if hop < 5:
                inject(headers)
                next_event = {
                    "request_id": request_id,
                    "hop": hop + 1,
                    "trace_context": headers,
                }
                producer.send(TOPIC, next_event)
                span.add_event(f"Forwarded to hop {hop + 1}")


if __name__ == "__main__":
    Thread(target=process_messages, daemon=True).start()
    print(f"🚀 Server running at http://{HOST}:{PORT}")
    server = HTTPServer((HOST, PORT), SimpleHandler)
    server.serve_forever()
