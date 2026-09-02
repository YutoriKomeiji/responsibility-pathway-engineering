#!/usr/bin/env python3
"""Deterministic checks for experimental M3 configuration/relationship integrity."""

from __future__ import annotations

from rpe_kernel.integrity import compare_integrity_binding, integrity_result_to_risk_condition
from rpe_kernel.risk_conditions import evaluate_risk_conditions


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

    print("M3 integrity comparison checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
