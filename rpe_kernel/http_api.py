"""Minimal dependency-free HTTP boundary for the RPE kernel."""

from __future__ import annotations

import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, Callable

from .pipeline import evaluate_action

JsonObject = dict[str, Any]
Evaluator = Callable[[JsonObject, list[JsonObject]], JsonObject]


def create_handler(evaluator: Evaluator = evaluate_action) -> type[BaseHTTPRequestHandler]:
    """Create an HTTP handler bound to an evaluator implementation."""

    class RPERequestHandler(BaseHTTPRequestHandler):
        server_version = "rpe-kernel/0.1"

        def _write_json(self, status: int, payload: JsonObject) -> None:
            body = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self) -> None:  # noqa: N802 - stdlib handler contract
            if self.path == "/health":
                self._write_json(200, {"status": "ok", "service": "rpe-kernel"})
                return
            self._write_json(404, {"error": "not_found"})

        def do_POST(self) -> None:  # noqa: N802 - stdlib handler contract
            if self.path != "/v1/evaluate":
                self._write_json(404, {"error": "not_found"})
                return

            try:
                length = int(self.headers.get("Content-Length", "0"))
                payload = json.loads(self.rfile.read(length).decode("utf-8"))
            except (ValueError, UnicodeDecodeError, json.JSONDecodeError):
                self._write_json(400, {"error": "invalid_json"})
                return

            if not isinstance(payload, dict):
                self._write_json(400, {"error": "invalid_request", "detail": "body must be an object"})
                return

            request = payload.get("request")
            packs = payload.get("packs")
            if not isinstance(request, dict) or not isinstance(packs, list) or not all(
                isinstance(pack, dict) for pack in packs
            ):
                self._write_json(
                    400,
                    {
                        "error": "invalid_request",
                        "detail": "request must be an object and packs must be an array of objects",
                    },
                )
                return

            result = evaluator(request, packs)
            self._write_json(200, result)

        def log_message(self, format: str, *args: Any) -> None:
            """Keep the reference server quiet by default."""

    return RPERequestHandler


def serve(host: str = "127.0.0.1", port: int = 8080) -> None:
    """Run the reference HTTP server until interrupted."""
    server = ThreadingHTTPServer((host, port), create_handler())
    print(f"RPE kernel REST API listening on http://{host}:{port}")
    server.serve_forever()


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the RPE kernel reference REST API")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()
    serve(args.host, args.port)


if __name__ == "__main__":
    main()
