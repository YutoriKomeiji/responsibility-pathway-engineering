#!/usr/bin/env python3
"""One-command, synthetic first-use proof for the experimental RPE M3 gateway.

Reuses the actual cross-surface and host-enforcement demonstrations. This
script performs no external dispatch. It is NOT a deployment readiness check.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def run_json_demo(path: str) -> dict[str, Any]:
    command = [sys.executable, str(ROOT / path)]
    if path.endswith(("demo_m3_cross_surface.py", "value_demo.py")):
        command.append("--json")
    proc = subprocess.run(
        command, cwd=ROOT, capture_output=True, text=True, timeout=40,
        check=False,
    )
    if proc.returncode:
        # Do not print complete potentially sensitive requests or subprocess logs.
        raise RuntimeError(f"{path}: demo failed (exit {proc.returncode})")
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"{path}: not a single JSON result") from exc
    if not isinstance(payload, dict):
        raise RuntimeError(f"{path}: expected one JSON object")
    return payload


def inspect() -> dict[str, Any]:
    parity = run_json_demo("scripts/demo_m3_cross_surface.py")
    expected = {
        "approved": "allow",
        "caller_flagged_mismatch": "require_authority",
        "invalid_graph_envelope": "hold",
    }
    cases = parity.get("cases", {})
    if (
        parity.get("contract") != "0.2.0-exp"
        or parity.get("surfaces") != ["python", "rest_loopback", "mcp_stdio"]
        or parity.get("external_action_executed") is not False
        or set(cases) != {*expected, "missing_approval"}
    ):
        raise RuntimeError("M3 cross-surface contract or case coverage differs")
    actions = {}
    for name, item in cases.items():
        observation = item["observed"]
        action = observation["m3_control_action"]
        if item["all_surfaces_equal"] is not True:
            raise RuntimeError(f"{name}: adapter results differ")
        if observation["authority_effect"] != "none" or observation["execution_effect"] != "none":
            raise RuntimeError(f"{name}: unrecognized authority/execution effect")
        if observation["downstream_executor_required"] is not True:
            raise RuntimeError(f"{name}: executor boundary missing")
        if name in expected and action != expected[name]:
            raise RuntimeError(f"{name}: expected {expected[name]}, observed {action}")
        if name == "missing_approval" and action == "allow":
            raise RuntimeError("missing approval was allowed")
        actions[name] = action

    host = run_json_demo("scripts/demo_m3_host_enforcement.py")
    decisions = host.get("cases", {})
    required_blocked = (
        "no_host_grant", "different_target", "untrusted_actor",
        "missing_evidence", "mismatch_observed", "forged_rpe_authority_effect",
    )
    if (
        host.get("test") != "synthetic_host_pre_dispatch_enforcement"
        or host.get("real_external_effects") != 0
        or host.get("simulated_dispatch_count") != 1
        or decisions.get("valid_with_host_grant", {}).get("status")
        != "synthetic_dispatch_recorded"
        or any(decisions.get(name, {}).get("status") != "not_dispatched" for name in required_blocked)
    ):
        raise RuntimeError("M3 synthetic host enforcement deviates from its contract")
    # A separate, intentionally naive baseline makes the added decision
    # boundary visible; it is not a general population model of all agents.
    comparison = run_json_demo("scripts/value_demo.py")
    if (
        comparison.get("external_action_executed") is not False
        or comparison.get("without_rpe", {}).get("decision") != "continue"
        or comparison.get("with_rpe", {}).get("decision") != "human_gate"
        or comparison.get("with_rpe", {}).get("authority_effect") != "none"
        or comparison.get("approved_with_rpe", {}).get("decision") != "allow"
        or comparison.get("approved_with_rpe", {}).get("authority_effect") != "none"
    ):
        raise RuntimeError("governed-vs-naive synthetic comparison differs")
    return {
        "test": "m3_first_use_reference",
        "synthetic_before_after": {
            "naive_generated_proposal": comparison["without_rpe"]["decision"],
            "missing_approval_with_rpe": comparison["with_rpe"]["decision"],
            "approved_with_rpe": comparison["approved_with_rpe"]["decision"],
        },
        "contract_version": "0.2.0-exp",
        "adapter_surfaces_checked": parity["surfaces"],
        "observed_control_actions": actions,
        "host_adverse_cases_blocked": list(required_blocked),
        "simulated_dispatches": 1,
        "real_external_effects": 0,
        "trust_claim": "none; caller evidence and host grants are synthetic",
        "production_ready_claim": False,
        "status": "reference_checks_passed",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="machine-readable bounded observation")
    args = parser.parse_args()
    try:
        record = inspect()
    except (RuntimeError, OSError, ValueError, KeyError, TypeError, subprocess.TimeoutExpired) as exc:
        print(f"FAIL: RPE M3 first-use reference: {exc}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(record, sort_keys=True))
    else:
        print("RPE M3 first-use reference: PASS (synthetic only)")
        print("Naive generated proposal: continue -> RPE missing approval: human_gate")
        print("Python / loopback REST / MCP stdio: same full result")
        for name, value in record["observed_control_actions"].items():
            print(f"  {name}: {value}")
        print("Host: six adverse/unauthorized paths blocked; one simulated dispatch.")
        print("Real external effects: 0. RPE allow is NOT permission to execute.")
        print("Scope: experimental Draft only; host must authenticate evidence and enforce permission.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
