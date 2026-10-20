#!/usr/bin/env python3
"""Check guarded REST/OpenAPI adapter parity for M3 0.2.0-exp."""

from __future__ import annotations

import json
import threading
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

from jsonschema import Draft202012Validator

from rpe_kernel.http_api import create_handler

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "examples/external-kernel/minimal-governed-evaluation-request.json"
SOURCE_OPENAPI = ROOT / "spec/openapi/rpe-kernel-guarded.openapi.json"
PACKAGED_OPENAPI = ROOT / "rpe_kernel/rpe-kernel-guarded.openapi.json"


def request_json(url: str, method: str = "GET", payload: dict | None = None) -> tuple[int, dict]:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method=method)
    if data is not None:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=5) as response:
        return response.status, json.loads(response.read().decode("utf-8"))


def validator_for(document: dict, schema_name: str) -> Draft202012Validator:
    schema = document["components"]["schemas"][schema_name]
    return Draft202012Validator(schema, resolver=None if False else __import__("jsonschema").RefResolver.from_schema(document))


def main() -> int:
    source = json.loads(SOURCE_OPENAPI.read_text(encoding="utf-8"))
    packaged = json.loads(PACKAGED_OPENAPI.read_text(encoding="utf-8"))
    assert source == packaged, "guarded OpenAPI source/package drift"
    assert source["info"]["version"] == "0.2.0-exp"
    assert set(source["paths"]) == {"/v1/evaluate/transition/guarded"}

    governed = json.loads(FIXTURE.read_text(encoding="utf-8"))
    payload = {
        "contract_version": "0.2.0-exp",
        "governed_evaluation": governed,
        "integrity_checks": [
            {
                "check": {
                    "check_id": "config",
                    "kind": "configuration",
                    "expected": {"configuration_id": "cfg-a"},
                    "observed": {"configuration_id": "cfg-b"},
                },
                "required_controls": ["require_authority"],
            }
        ],
        "human_return_checks": [
            {
                "check": {
                    "return_id": "review",
                    "owner_role": "review_owner",
                    "authority_reference": "auth",
                    "capability_status": "available",
                    "response_window_status": "available",
                    "next_decision_scope": "bounded_review",
                    "evidence_scope": {"available": ["request"], "missing": []},
                },
                "required_controls": ["require_authority"],
            }
        ],
    }
    validator_for(source, "GuardedEvaluateRequest").validate(payload)

    server = ThreadingHTTPServer(("127.0.0.1", 0), create_handler())
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}"
    try:
        status, served_openapi = request_json(f"{base}/openapi-guarded.json")
        assert status == 200 and served_openapi == source
        status, result = request_json(f"{base}/v1/evaluate/transition/guarded", "POST", payload)
        assert status == 200
        validator_for(source, "GuardedEvaluateResponse").validate(result)
        assert result["contract_version"] == "0.2.0-exp"
        assert result["guard_observations"]["integrity_results"][0]["status"] == "triggered"
        assert result["guard_observations"]["integrity_results"][0]["independent_authentication_claim"] is False
        assert result["guard_observations"]["human_return_results"][0]["authority_validity_claim"] is False
        assert result["transition_result"]["control_action"] == "require_authority"
        assert result["authority_effect"] == "none" and result["execution_effect"] == "none"

        old_status, old_openapi = request_json(f"{base}/openapi.json")
        assert old_status == 200
        assert "/v1/evaluate/transition" in old_openapi["paths"]
        assert "/v1/evaluate/transition/guarded" not in old_openapi["paths"], "0.1 OpenAPI was silently expanded"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)

    print("M3 guarded REST/OpenAPI adapter parity checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
