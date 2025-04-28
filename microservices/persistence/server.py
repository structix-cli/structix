import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any
from uuid import uuid4

import pymysql  # type: ignore[import]

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

HOST = "0.0.0.0"
PORT = 3000
persistent_id = str(uuid4())


def get_db_connection() -> Any:
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )


def initialize_db() -> None:
    connection = get_db_connection()  # type: ignore
    with connection.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS events (
                id INT AUTO_INCREMENT PRIMARY KEY,
                server_id VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
    connection.close()


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        connection = get_db_connection()  # type: ignore
        try:
            with connection.cursor() as cursor:
                # Insertar nuevo evento
                cursor.execute(
                    "INSERT INTO events (server_id) VALUES (%s)",
                    (persistent_id,),
                )
                cursor.execute("SELECT * FROM events")
                events = cursor.fetchall()

            response = json.dumps(events, default=str).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)
        finally:
            connection.close()


if __name__ == "__main__":
    print(f"🚀 Server running at http://{HOST}:{PORT}")
    initialize_db()
    server = HTTPServer((HOST, PORT), SimpleHandler)
    server.serve_forever()
