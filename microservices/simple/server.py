import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from uuid import uuid4

HOST = "0.0.0.0"
PORT = 3000
persistent_id = str(uuid4())


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        response = json.dumps({"id": persistent_id}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)


if __name__ == "__main__":
    print(f"🚀 Server running at http://{HOST}:{PORT}")
    server = HTTPServer((HOST, PORT), SimpleHandler)
    server.serve_forever()
