"""Integration check for the dependency-free RPE REST boundary."""

from __future__ import annotations

import json
import threading
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer

from rpe_kernel.http_api import create_handler


def request_json(url: str, method: str = "GET", payload: dict | None = None) -> tuple[int, dict]:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=data, method=method)
    if data is not None:
        request.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            return response.status, json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        return error.code, json.loads(error.read().decode("utf-8"))


def main() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", 0), create_handler())
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base_url = f"http://127.0.0.1:{server.server_port}"

    try:
        status, health = request_json(f"{base_url}/health")
        assert status == 200
        assert health == {"service": "rpe-kernel", "status": "ok"}

        payload = {
            "request": {"request_id": "rest-check-1", "action": "publish"},
            "packs": [
                {
                    "pack_id": "publication-pack",
                    "applicability": {"action": ["publish"]},
                    "requirements": [],
                }
            ],
        }
        status, result = request_json(f"{base_url}/v1/evaluate", "POST", payload)
        assert status == 200
        assert result["request_id"] == "rest-check-1"
        assert result["stage"] == "evaluation"
        assert result["decision"] == "allow"

        status, error = request_json(f"{base_url}/v1/evaluate", "POST", {"request": {}})
        assert status == 400
        assert error["error"] == "invalid_request"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)

    print("REST API check passed")


if __name__ == "__main__":
    main()
