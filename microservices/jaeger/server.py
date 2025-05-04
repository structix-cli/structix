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

otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces")
trace.get_tracer_provider().add_span_processor(  # type: ignore
    BatchSpanProcessor(otlp_exporter)
)

HOST = "0.0.0.0"
PORT = 3000
persistent_id = str(uuid4())


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        with tracer.start_as_current_span("handle_request") as span:
            span.set_attribute("http.method", "GET")
            span.set_attribute("http.path", self.path)
            span.add_event("Handling request start")

            if self.path == "/favicon.ico":
                self.send_response(204)
                self.end_headers()
                return

            with tracer.start_as_current_span("generate-response") as subspan:
                time.sleep(0.2)
                subspan.set_attribute("response.id", persistent_id)

                response = json.dumps({"id": persistent_id}).encode("utf-8")

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
