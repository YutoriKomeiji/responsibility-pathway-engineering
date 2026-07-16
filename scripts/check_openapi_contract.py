#!/usr/bin/env python3
"""Check the bounded OpenAPI contract and runtime exposure."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "spec" / "openapi" / "rpe-kernel.openapi.json"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> int:
    document = json.loads(SPEC_PATH.read_text(encoding="utf-8"))

    if document.get("openapi") != "3.1.0":
        fail("OpenAPI version must be 3.1.0")

    paths = document.get("paths")
    if not isinstance(paths, dict):
        fail("paths must be an object")

    required_operations = {
        "/health": "get",
        "/openapi.json": "get",
        "/v1/evaluate": "post",
    }
    for path, method in required_operations.items():
        if not isinstance(paths.get(path), dict) or method not in paths[path]:
            fail(f"missing operation: {method.upper()} {path}")

    schemas = document.get("components", {}).get("schemas", {})
    for name in ("HealthResponse", "EvaluateRequest", "EvaluateResponse", "ErrorResponse"):
        if name not in schemas:
            fail(f"missing component schema: {name}")

    decisions = schemas["EvaluateResponse"]["properties"]["decision"].get("enum")
    if decisions != ["allow", "hold", "human_gate", "deny"]:
        fail("decision enum must preserve kernel precedence vocabulary")

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
