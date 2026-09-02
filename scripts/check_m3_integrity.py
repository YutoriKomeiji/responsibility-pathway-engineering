#!/usr/bin/env python3
"""Deterministic checks for experimental M3 configuration/relationship integrity."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from rpe_kernel import evaluate_gateway_request
from rpe_kernel.integrity import compare_integrity_binding, integrity_result_to_risk_condition
from rpe_kernel.risk_conditions import evaluate_risk_conditions

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "examples/external-kernel/minimal-governed-evaluation-request.json"


def main() -> int:
    config_match = compare_integrity_binding(
        {
            "check_id": "execution-config",
            "kind": "configuration",
            "expected": {
                "model": "model-a",
                "policy_pack": "pack-v3",
                "tool_manifest": "tools-sha256:1111",
            },
            "observed": {
                "tool_manifest": "tools-sha256:1111",
                "policy_pack": "pack-v3",
                "model": "model-a",
            },
            "evidence_refs": ["config-snapshot"],
        }
    )
    assert config_match["status"] == "clear", config_match
    assert config_match["independent_authentication_claim"] is False, config_match
    assert config_match["authority_effect"] == "none", config_match

    config_changed = compare_integrity_binding(
        {
            "check_id": "execution-config",
            "kind": "configuration",
            "expected": {
                "model": "model-a",
                "policy_pack": "pack-v3",
                "tool_manifest": "tools-sha256:1111",
            },
            "observed": {
                "model": "model-b",
                "policy_pack": "pack-v3",
                "tool_manifest": "tools-sha256:1111",
            },
            "evidence_refs": ["config-snapshot"],
        }
    )
    assert config_changed["status"] == "triggered", config_changed
    assert config_changed["reason_codes"] == ["RPE-M3-INTEGRITY-IDENTITY-MISMATCH"], config_changed

    relationship_misbound = compare_integrity_binding(
        {
            "check_id": "approval-request-binding",
            "kind": "relationship",
            "expected": {
                "approval_id": "approval-42",
                "request_id": "request-42",
            },
            "observed": {
                "approval_id": "approval-42",
                "request_id": "request-99",
            },
            "evidence_refs": ["approval-binding-record"],
        }
    )
    assert relationship_misbound["status"] == "triggered", relationship_misbound

    unknown_observation = compare_integrity_binding(
        {
            "check_id": "tool-server-binding",
            "kind": "relationship",
            "expected": {"server_id": "approved-server"},
            "observed": None,
        }
    )
    assert unknown_observation["status"] == "unknown", unknown_observation
    assert "RPE-M3-INTEGRITY-OBSERVED-IDENTITY-UNKNOWN" in unknown_observation["reason_codes"], unknown_observation

    condition = integrity_result_to_risk_condition(
        relationship_misbound,
        required_controls=["require_authority"],
    )
    graph = evaluate_risk_conditions({"conditions": [condition]})
    assert graph["graph_status"] == "triggered", graph
    assert graph["required_controls"] == ["require_authority"], graph

    unknown_condition = integrity_result_to_risk_condition(
        unknown_observation,
        required_controls=["isolate"],
    )
    unresolved = evaluate_risk_conditions({"conditions": [unknown_condition]})
    assert unresolved["graph_status"] == "unresolved", unresolved
    assert "RPE-M3-RISK-CONDITION-UNKNOWN" in unresolved["reason_codes"], unresolved

    invalid = compare_integrity_binding(
        {
            "check_id": "bad-kind",
            "kind": "trust-me-bro",
            "expected": {"id": "x"},
            "observed": {"id": "x"},
        }
    )
    assert invalid["status"] == "invalid", invalid
    assert "RPE-M3-INTEGRITY-CHECK-UNSUPPORTED-KIND" in invalid["reason_codes"], invalid

    # One-call gateway integration: the comparator reports identity state while
    # the caller/policy explicitly supplies the required control.
    base = json.loads(FIXTURE.read_text(encoding="utf-8"))
    integrated = evaluate_gateway_request(
        {
            "contract_version": "0.1.0-exp",
            "governed_evaluation": base,
            "integrity_checks": [
                {
                    "check": {
                        "check_id": "approval-request-binding",
                        "kind": "relationship",
                        "expected": {"approval_id": "a-1", "request_id": "r-1"},
                        "observed": {"approval_id": "a-1", "request_id": "r-2"},
                        "evidence_refs": ["binding-readback"],
                    },
                    "required_controls": ["require_authority"],
                }
            ],
        },
        today=date(2026, 9, 1),
    )
    assert integrated["evaluation_result"]["decision"] == "allow", integrated
    assert integrated["integrity_results"][0]["status"] == "triggered", integrated
    assert integrated["integrity_results"][0]["independent_authentication_claim"] is False, integrated
    assert integrated["risk_condition_result"]["required_controls"] == ["require_authority"], integrated
    assert integrated["transition_result"]["control_action"] == "require_authority", integrated
    assert integrated["authority_effect"] == "none", integrated
    assert integrated["execution_effect"] == "none", integrated

    integrated_unknown = evaluate_gateway_request(
        {
            "contract_version": "0.1.0-exp",
            "governed_evaluation": base,
            "integrity_checks": [
                {
                    "check": {
                        "check_id": "configuration-readback",
                        "kind": "configuration",
                        "expected": {"configuration_id": "cfg-7"},
                        "observed": None,
                    },
                    "required_controls": ["isolate"],
                }
            ],
        },
        today=date(2026, 9, 1),
    )
    assert integrated_unknown["integrity_results"][0]["status"] == "unknown", integrated_unknown
    assert integrated_unknown["risk_condition_result"]["graph_status"] == "unresolved", integrated_unknown
    assert integrated_unknown["transition_result"]["control_action"] == "hold", integrated_unknown

    # Caller risk and integrity-derived controls are combined without hidden
    # precedence. Different triggered controls must force explicit selection.
    competing = evaluate_gateway_request(
        {
            "contract_version": "0.1.0-exp",
            "governed_evaluation": base,
            "risk_graph": {
                "conditions": [
                    {
                        "condition_id": "external-evidence-missing",
                        "status": "triggered",
                        "required_controls": ["require_evidence"],
                    }
                ]
            },
            "integrity_checks": [
                {
                    "check": {
                        "check_id": "execution-config",
                        "kind": "configuration",
                        "expected": {"configuration_id": "cfg-a"},
                        "observed": {"configuration_id": "cfg-b"},
                    },
                    "required_controls": ["require_authority"],
                }
            ],
        },
        today=date(2026, 9, 1),
    )
    assert competing["risk_condition_result"]["required_controls"] == ["require_authority", "require_evidence"], competing
    assert "RPE-M3-CONTROL-SELECTION-REQUIRED" in competing["risk_condition_result"]["reason_codes"], competing
    assert competing["transition_result"]["control_action"] == "hold", competing

    # No implicit policy: a one-call integrity entry without an explicit control
    # is invalid rather than silently inventing a consequence.
    missing_control = evaluate_gateway_request(
        {
            "contract_version": "0.1.0-exp",
            "governed_evaluation": base,
            "integrity_checks": [
                {
                    "check": {
                        "check_id": "execution-config",
                        "kind": "configuration",
                        "expected": {"configuration_id": "cfg-a"},
                        "observed": {"configuration_id": "cfg-b"},
                    },
                    "required_controls": [],
                }
            ],
        },
        today=date(2026, 9, 1),
    )
    assert missing_control["evaluation_result"] is None, missing_control
    assert missing_control["transition_result"]["control_action"] == "hold", missing_control
    assert "RPE-M3-INTEGRITY-CHECK-CONTROL-REQUIRED" in missing_control["transition_result"]["reason_codes"], missing_control

    print("M3 integrity comparison and gateway integration checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
