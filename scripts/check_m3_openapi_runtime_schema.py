#!/usr/bin/env python3
"""Validate representative M3 runtime output against the published OpenAPI schema."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from jsonschema import Draft202012Validator

from rpe_kernel import evaluate_gateway_request

ROOT = Path(__file__).resolve().parents[1]
OPENAPI = ROOT / "spec" / "openapi" / "rpe-kernel.openapi.json"
FIXTURE = ROOT / "examples" / "external-kernel" / "minimal-governed-evaluation-request.json"


def validator_for(document: dict, component: str) -> Draft202012Validator:
    wrapper = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$ref": f"#/components/schemas/{component}",
        "components": document["components"],
    }
    return Draft202012Validator(wrapper)


def main() -> int:
    document = json.loads(OPENAPI.read_text(encoding="utf-8"))
    governed = json.loads(FIXTURE.read_text(encoding="utf-8"))
    result = evaluate_gateway_request(
        {
            "contract_version": "0.1.0-exp",
            "governed_evaluation": governed,
            "requested_route": {
                "kind": "verifier",
                "target_id": "independent-verifier",
                "purpose": "second_check",
            },
        },
        today=date(2026, 9, 1),
    )
    assert result["transition_result"]["control_action"] == "route", result
    validator_for(document, "GatewayEvaluateResponse").validate(result)
    print("PASS: representative M3 runtime output matches OpenAPI schema")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
