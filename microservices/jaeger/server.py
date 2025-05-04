import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from uuid import uuid4

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import (
    OTLPSpanExporter,
)
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

trace.set_tracer_provider(
    TracerProvider(resource=Resource.create({SERVICE_NAME: "test-server"}))
)
tracer = trace.get_tracer(__name__)

otlp_exporter = OTLPSpanExporter(
    endpoint="http://jaeger-collector.default.svc.cluster.local:4318/v1/traces"
)
trace.get_tracer_provider().add_span_processor(  # type: ignore
    BatchSpanProcessor(otlp_exporter)
)

HOST = "0.0.0.0"
PORT = 3000


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        request_id = str(uuid4())
        with tracer.start_as_current_span("handle_request") as span:
            span.set_attribute("http.method", "GET")
            span.set_attribute("http.path", self.path)
            span.set_attribute("request.id", request_id)
            span.add_event("Handling request start")

            if self.path == "/favicon.ico":
                time.sleep(1)
                self.send_response(204)
                self.end_headers()
                return

            with tracer.start_as_current_span("fetch_from_db") as db_span:
                db_span.set_attribute("db.system", "mockdb")
                db_span.set_attribute("db.operation", "select")
                db_span.set_attribute(
                    "db.statement", "SELECT * FROM users WHERE id = ?"
                )
                time.sleep(0.1)
                user = {"id": request_id, "name": "Brayan"}

            with tracer.start_as_current_span("call_external_api") as api_span:
                api_span.set_attribute("http.method", "GET")
                api_span.set_attribute(
                    "http.url", "https://api.example.com/data"
                )
                time.sleep(0.2)
                external_data = {"external": True, "value": 42}

            with tracer.start_as_current_span("generate_response") as subspan:
                time.sleep(0.05)
                subspan.set_attribute("response.id", request_id)
                response = json.dumps(
                    {"id": request_id, "user": user, "external": external_data}
                ).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            try:
                self.wfile.write(response)
            except BrokenPipeError:
                trace.get_current_span().add_event(
                    "BrokenPipeError: client disconnected early"
                )

            span.add_event("Response sent")


if __name__ == "__main__":
    print(f"🚀 Server running at http://{HOST}:{PORT}")
    server = HTTPServer((HOST, PORT), SimpleHandler)
    server.serve_forever()
