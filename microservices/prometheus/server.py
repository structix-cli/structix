import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from uuid import uuid4

from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest

HOST = "0.0.0.0"
PORT = 3000
persistent_id = str(uuid4())

REQUEST_COUNT = Counter(
    "root_requests_total", "Total number of requests to the root endpoint"
)


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return

        elif self.path == "/metrics":
            self.send_response(200)
            self.send_header("Content-Type", CONTENT_TYPE_LATEST)
            self.end_headers()
            self.wfile.write(generate_latest())
            return

        elif self.path == "/":
            REQUEST_COUNT.inc()
            response = json.dumps({"id": persistent_id}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)
            return

        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    print(f"🚀 Server running at http://{HOST}:{PORT}")
    server = HTTPServer((HOST, PORT), SimpleHandler)
    server.serve_forever()
