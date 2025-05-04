import json
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from uuid import uuid4

from jaeger_client import Config, Tracer  # type: ignore


def init_tracer(service_name: str) -> Tracer:
    logging.getLogger("").handlers = []
    logging.basicConfig(format="%(message)s", level=logging.DEBUG)

    config = Config(
        config={
            "sampler": {"type": "const", "param": 1},
            "logging": True,
            "local_agent": {
                "reporting_host": "jaeger-agent.observability.svc.cluster.local",
                "reporting_port": 6831,
            },
        },
        service_name=service_name,
    )
    tracer = config.initialize_tracer()
    if tracer is None:
        raise RuntimeError("Failed to initialize tracer")
    return tracer


tracer = init_tracer("simple-http-server")

HOST = "0.0.0.0"
PORT = 3000
persistent_id = str(uuid4())


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        with tracer.start_span("http_request") as span:
            span.set_tag("http.method", "GET")
            span.set_tag("http.url", self.path)

            if self.path == "/favicon.ico":
                self.send_response(204)
                self.end_headers()
                return

            response = json.dumps({"id": persistent_id}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)

            span.log_kv({"event": "response_sent", "status_code": 200})


if __name__ == "__main__":
    print(f"🚀 Server running at http://{HOST}:{PORT}")
    server = HTTPServer((HOST, PORT), SimpleHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        tracer.close()
