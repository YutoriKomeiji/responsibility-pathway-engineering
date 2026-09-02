"""Integration check for the dependency-free RPE REST boundary."""

from __future__ import annotations

import json
import threading
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

from rpe_kernel.http_api import create_handler

ROOT = Path(__file__).resolve().parents[1]
GOVERNED_FIXTURE = ROOT / "examples/external-kernel/minimal-governed-evaluation-request.json"


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

        status, openapi = request_json(f"{base_url}/openapi.json")
        assert status == 200
        assert "/v1/evaluate" in openapi["paths"]
        assert "/v1/evaluate/governed" in openapi["paths"]
        assert "/v1/evaluate/transition" in openapi["paths"]

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

        governed_payload = json.loads(GOVERNED_FIXTURE.read_text(encoding="utf-8"))
        status, governed = request_json(f"{base_url}/v1/evaluate/governed", "POST", governed_payload)
        assert status == 200
        assert governed["decision"] == "allow"
        assert governed["stage"] == "evaluation"
        assert governed["responsibility_handoff"]["authority_effect"] == "none"
        assert governed["responsibility_handoff"]["decision_scope"] == "evaluation_only"

        gateway_payload = {
            "contract_version": "0.1.0-exp",
            "governed_evaluation": governed_payload,
            "risk_graph": {
                "conditions": [
                    {
                        "condition_id": "authority_scope_mismatch",
                        "status": "triggered",
                        "required_controls": ["require_authority"],
                        "evidence_refs": ["authority-binding"],
                    }
                ]
            },
            "constraints": ["no_delegation"],
        }
        status, transition = request_json(f"{base_url}/v1/evaluate/transition", "POST", gateway_payload)
        assert status == 200
        assert transition["evaluation_result"]["decision"] == "allow"
        assert transition["transition_result"]["control_action"] == "require_authority"
        assert transition["transition_result"]["authority_effect"] == "none"
        assert transition["transition_result"]["execution_effect"] == "none"
        assert transition["transition_result"]["downstream_executor_required"] is True

        status, invalid_transition = request_json(
            f"{base_url}/v1/evaluate/transition",
            "POST",
            {"contract_version": "9.9.9", "governed_evaluation": governed_payload},
        )
        assert status == 200
        assert invalid_transition["evaluation_result"] is None
        assert invalid_transition["transition_result"]["control_action"] == "hold"
        assert "RPE-M3-GATEWAY-REQUEST-INCOMPATIBLE-VERSION" in invalid_transition["transition_result"]["reason_codes"]

        status, held = request_json(f"{base_url}/v1/evaluate/governed", "POST", {"request": {}})
        assert status == 200
        assert held["decision"] == "human_gate"
        assert held["stage"] == "admission"

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
