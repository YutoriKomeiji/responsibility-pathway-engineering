#!/usr/bin/env python3
"""Check the bounded OpenAPI contract and runtime exposure."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "spec" / "openapi" / "rpe-kernel.openapi.json"
PACKAGED_SPEC_PATH = ROOT / "rpe_kernel" / "rpe-kernel.openapi.json"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> int:
    document = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    packaged = json.loads(PACKAGED_SPEC_PATH.read_text(encoding="utf-8"))

    if document != packaged:
        fail("repository and packaged OpenAPI contracts must match exactly")

    if document.get("openapi") != "3.1.0":
        fail("OpenAPI version must be 3.1.0")

    paths = document.get("paths")
    if not isinstance(paths, dict):
        fail("paths must be an object")

    required_operations = {
        "/health": "get",
        "/openapi.json": "get",
        "/v1/evaluate": "post",
        "/v1/evaluate/governed": "post",
    }
    for path, method in required_operations.items():
        if not isinstance(paths.get(path), dict) or method not in paths[path]:
            fail(f"missing operation: {method.upper()} {path}")

    schemas = document.get("components", {}).get("schemas", {})
    for name in (
        "HealthResponse",
        "EvaluateRequest",
        "EvaluateResponse",
        "GovernedEvaluateRequest",
        "GovernedEvaluateResponse",
        "ErrorResponse",
    ):
        if name not in schemas:
            fail(f"missing component schema: {name}")

    decisions = schemas["EvaluateResponse"]["properties"]["decision"].get("enum")
    if decisions != ["allow", "hold", "human_gate", "deny"]:
        fail("decision enum must preserve kernel precedence vocabulary")

    governed_stages = schemas["GovernedEvaluateResponse"]["properties"]["stage"].get("enum")
    if governed_stages != ["admission", "compatibility", "governance", "applicability", "evaluation"]:
        fail("governed stage enum must preserve strict pipeline stages")

    handoff = schemas["GovernedEvaluateResponse"]["properties"].get("responsibility_handoff", {})
    handoff_props = handoff.get("properties", {}) if isinstance(handoff, dict) else {}
    if handoff_props.get("authority_effect", {}).get("const") != "none":
        fail("governed OpenAPI must preserve authority_effect=none")
    if handoff_props.get("decision_scope", {}).get("const") != "evaluation_only":
        fail("governed OpenAPI must preserve decision_scope=evaluation_only")

    description = document.get("info", {}).get("description", "").lower()
    if "does not imply production readiness" not in description:
        fail("OpenAPI description must preserve the production boundary")

    sys.path.insert(0, str(ROOT))
    from rpe_kernel.http_api import load_openapi_document

    if load_openapi_document() != document:
        fail("runtime OpenAPI document differs from repository contract")

    print("PASS: OpenAPI contract and runtime exposure are consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
