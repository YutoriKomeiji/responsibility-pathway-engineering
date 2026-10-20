"""Minimal dependency-free HTTP boundary for the RPE kernel."""

from __future__ import annotations

import argparse
import json
import socket
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Callable

from .gateway import evaluate_gateway_request
from .guarded_adapter import evaluate_guarded_adapter_request
from .pipeline import evaluate_action, evaluate_governed_action

JsonObject = dict[str, Any]
Evaluator = Callable[[JsonObject, list[JsonObject]], JsonObject]
GovernedEvaluator = Callable[[JsonObject], JsonObject]
GatewayEvaluator = Callable[[JsonObject], JsonObject]
OPENAPI_PATH = Path(__file__).with_name("rpe-kernel.openapi.json")
GUARDED_OPENAPI_PATH = Path(__file__).with_name("rpe-kernel-guarded.openapi.json")
# This reference server is local-only by default. A reverse proxy must enforce
# authentication, transport security, and request limits in production.
MAX_REQUEST_BYTES = 1_048_576
REQUEST_READ_TIMEOUT_SECONDS = 10.0


def _unique_json_fields(pairs: list[tuple[str, Any]]) -> JsonObject:
    """Reject ambiguous objects before policy/authority fields are evaluated."""
    result: JsonObject = {}
    for name, value in pairs:
        if name in result:
            raise ValueError("duplicate JSON object field")
        result[name] = value
    return result


def _finite_json_constant(value: str) -> Any:
    raise ValueError(f"non-finite JSON constant: {value}")



def load_openapi_document() -> JsonObject:
    return json.loads(OPENAPI_PATH.read_text(encoding="utf-8"))


def load_guarded_openapi_document() -> JsonObject:
    return json.loads(GUARDED_OPENAPI_PATH.read_text(encoding="utf-8"))


def create_handler(
    evaluator: Evaluator = evaluate_action,
    governed_evaluator: GovernedEvaluator = evaluate_governed_action,
    gateway_evaluator: GatewayEvaluator = evaluate_gateway_request,
    guarded_evaluator: GatewayEvaluator = evaluate_guarded_adapter_request,
) -> type[BaseHTTPRequestHandler]:
    class RPERequestHandler(BaseHTTPRequestHandler):
        server_version = "rpe-kernel/0.1"

        def _write_json(self, status: int, payload: JsonObject) -> None:
            body = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self) -> None:  # noqa: N802
            if self.path == "/health":
                self._write_json(200, {"status": "ok", "service": "rpe-kernel"})
                return
            if self.path == "/openapi.json":
                self._write_json(200, load_openapi_document())
                return
            if self.path == "/openapi-guarded.json":
                self._write_json(200, load_guarded_openapi_document())
                return
            self._write_json(404, {"error": "not_found"})

        def do_POST(self) -> None:  # noqa: N802
            supported = {
                "/v1/evaluate",
                "/v1/evaluate/governed",
                "/v1/evaluate/transition",
                "/v1/evaluate/transition/guarded",
            }
            if self.path not in supported:
                self._write_json(404, {"error": "not_found"})
                return
            if self.headers.get("Transfer-Encoding") is not None:
                self._write_json(400, {"error": "unsupported_transfer_encoding"})
                return
            lengths = self.headers.get_all("Content-Length", [])
            if len(lengths) != 1 or not lengths[0].isascii() or not lengths[0].isdecimal():
                self._write_json(400, {"error": "invalid_content_length"})
                return
            length = int(lengths[0])
            if length > MAX_REQUEST_BYTES:
                self._write_json(413, {"error": "request_too_large"})
                return
            if self.headers.get("Content-Type", "").split(";", 1)[0].strip().lower() != "application/json":
                self._write_json(415, {"error": "unsupported_media_type"})
                return
            try:
                self.connection.settimeout(REQUEST_READ_TIMEOUT_SECONDS)
                body = self.rfile.read(length)
                if len(body) != length:
                    self._write_json(400, {"error": "incomplete_body"})
                    return
                payload = json.loads(
                    body.decode("utf-8"),
                    object_pairs_hook=_unique_json_fields,
                    parse_constant=_finite_json_constant,
                )
            except (ValueError, UnicodeDecodeError, json.JSONDecodeError):
                self._write_json(400, {"error": "invalid_json"})
                return
            except (socket.timeout, TimeoutError):
                self._write_json(408, {"error": "request_timeout"})
                return
            if not isinstance(payload, dict):
                self._write_json(400, {"error": "invalid_request", "detail": "body must be an object"})
                return
            if self.path == "/v1/evaluate/governed":
                self._write_json(200, governed_evaluator(payload))
                return
            if self.path == "/v1/evaluate/transition":
                self._write_json(200, gateway_evaluator(payload))
                return
            if self.path == "/v1/evaluate/transition/guarded":
                self._write_json(200, guarded_evaluator(payload))
                return
            request = payload.get("request")
            packs = payload.get("packs")
            if not isinstance(request, dict) or not isinstance(packs, list) or not all(isinstance(pack, dict) for pack in packs):
                self._write_json(400, {"error": "invalid_request", "detail": "request must be an object and packs must be an array of objects"})
                return
            self._write_json(200, evaluator(request, packs))

        def log_message(self, format: str, *args: Any) -> None:
            pass

    return RPERequestHandler


def serve(host: str = "127.0.0.1", port: int = 8080) -> None:
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
