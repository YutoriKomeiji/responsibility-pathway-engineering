"""Installed-package snapshot of RPE external-kernel contract support.

This file mirrors the human-maintained repository manifest at
schemas/external-kernel/contract-versions.json. CI must fail if the two drift.
Runtime code may import this module without depending on repository-root data.
"""

MANIFEST_VERSION = "1.4.0"

CONTRACTS = {
    "action_request": {"version": "1.1.0", "unknown_major_behavior": "reject"},
    "gate_decision": {"version": "1.0.0", "unknown_major_behavior": "human_gate"},
    "runtime_evaluation_result": {"version": "1.0.0", "unknown_major_behavior": "human_gate"},
    "requirement_pack": {"version": "1.1.0", "unknown_major_behavior": "human_gate"},
    "requirement_pack_governance": {"version": "1.1.0", "unknown_major_behavior": "human_gate"},
    "governed_pack_binding": {"version": "1.0.0", "unknown_major_behavior": "human_gate"},
    "governed_evaluation_request": {"version": "1.0.0", "unknown_major_behavior": "human_gate"},
    "governed_evaluation_result": {"version": "1.2.0", "unknown_major_behavior": "human_gate"},
}

REASON_CODE_POLICY = {
    "version": "1.0.0",
    "unknown_code_behavior": "preserve",
    "reuse_forbidden": True,
}
