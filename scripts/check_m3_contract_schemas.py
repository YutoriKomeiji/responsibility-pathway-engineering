#!/usr/bin/env python3
"""Validate the experimental M3 risk and transition contracts against runtime outputs."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from jsonschema import Draft202012Validator

from rpe_kernel import evaluate_governed_action, evaluate_risk_conditions, evaluate_transition

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas" / "m3"
FIXTURE = ROOT / "examples" / "external-kernel" / "minimal-governed-evaluation-request.json"


def _validator(name: str) -> Draft202012Validator:
    schema = json.loads((SCHEMA_DIR / name).read_text(encoding="utf-8"))
    return Draft202012Validator(schema)


def main() -> int:
    risk_input_validator = _validator("risk-condition-graph.schema.json")
    transition_validator = _validator("responsibility-transition-result.schema.json")

    graph = {
        "conditions": [
            {
                "condition_id": "authority_scope_mismatch",
                "status": "triggered",
                "required_controls": ["require_authority"],
                "depends_on": [],
                "evidence_refs": ["authority-binding"],
            }
        ]
    }
    risk_input_validator.validate(graph)
    risk_result = evaluate_risk_conditions(graph)
    assert risk_result["scalar_score"] is None, risk_result

    envelope = json.loads(FIXTURE.read_text(encoding="utf-8"))
    evaluation = evaluate_governed_action(envelope, today=date(2026, 9, 1))
    result = evaluate_transition(evaluation, risk_result=risk_result)
    assert result["control_action"] == "require_authority", result
    transition_validator.validate(result)

    routed = evaluate_transition(
        evaluation,
        requested_route={
            "kind": "verifier",
            "target_id": "independent-verifier",
            "purpose": "second_check",
        },
    )
    transition_validator.validate(routed)

    held = evaluate_transition(
        evaluation,
        risk_result=evaluate_risk_conditions(
            {
                "conditions": [
                    {
                        "condition_id": "relationship_integrity",
                        "status": "unknown",
                        "required_controls": ["isolate"],
                    }
                ]
            }
        ),
    )
    assert held["control_action"] == "hold", held
    transition_validator.validate(held)

    print("M3 contract schema checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
