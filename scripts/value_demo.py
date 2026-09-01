#!/usr/bin/env python3
"""Show one concrete adoption value of RPE without executing any external action.

The comparison is intentionally small: a naive agent-style workflow treats a
model-produced proposal as ready to continue, while the same proposal is passed
through RPE's strict governed evaluation path before continuation.

This demo measures repository-observable behavior only. It does not prove real-
world safety, compliance, effect prevention, or production risk reduction.
"""

from __future__ import annotations

import copy
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from rpe_kernel import evaluate_governed_action  # noqa: E402

FIXTURE = ROOT / "examples/external-kernel/minimal-governed-evaluation-request.json"


def _load_fixture() -> dict[str, Any]:
    value = json.loads(FIXTURE.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("governed fixture must be an object")
    return value


def _naive_agent(proposal: dict[str, Any]) -> dict[str, Any]:
    """Minimal comparison baseline: proposal presence means continue."""
    return {
        "decision": "continue",
        "reason": "proposal_generated",
        "human_return": None,
        "executed": False,
    }


def _guarded_agent(envelope: dict[str, Any]) -> dict[str, Any]:
    result = evaluate_governed_action(envelope, today=date(2026, 9, 1))
    handoff = result["responsibility_handoff"]
    return {
        "decision": result["decision"],
        "stage": result["stage"],
        "reason_codes": result["reason_codes"],
        "human_return": result["human_return"],
        "authority_effect": handoff["authority_effect"],
        "decision_scope": handoff["decision_scope"],
        "residual_owner_role": handoff["downstream_obligations"]["residual_owner_role"],
        "executed": False,
    }


def main() -> int:
    envelope = _load_fixture()
    envelope = copy.deepcopy(envelope)
    envelope["request"]["request_id"] = "value-demo-missing-approval"
    envelope["request"]["context"]["human_approval_present"] = False
    envelope["request"]["evidence_scope"] = {
        "available": [],
        "missing": ["approval-record"],
    }

    proposal = {
        "action": envelope["request"]["action"],
        "target": envelope["request"]["target"],
    }

    naive = _naive_agent(proposal)
    guarded = _guarded_agent(envelope)

    assert naive["decision"] == "continue", naive
    assert guarded["decision"] == "human_gate", guarded
    assert guarded["stage"] == "evaluation", guarded
    assert guarded["reason_codes"] == ["RPE-DEMO-MISSING-HUMAN-APPROVAL-PRESENT"], guarded
    assert guarded["human_return"] == {"role": "demo-owner"}, guarded
    assert guarded["residual_owner_role"] == "demo-owner", guarded
    assert guarded["authority_effect"] == "none", guarded
    assert guarded["decision_scope"] == "evaluation_only", guarded
    assert naive["executed"] is False and guarded["executed"] is False

    print("RPE VALUE DEMO — SAME PROPOSAL, DIFFERENT CONTINUATION")
    print("Synthetic scenario: an AI agent proposes an external send, but required human approval is missing.")
    print("No external action is executed by this demo.\n")

    print("WITHOUT RPE")
    print(f"  continuation : {naive['decision'].upper()}")
    print(f"  reason       : {naive['reason']}")
    print("  owner return : none")
    print()

    print("WITH RPE GOVERNED EVALUATION")
    print(f"  decision     : {guarded['decision'].upper()}")
    print(f"  reason code  : {guarded['reason_codes'][0]}")
    print(f"  return to    : {guarded['human_return']['role']}")
    print(f"  residual     : {guarded['residual_owner_role']}")
    print(f"  authority    : {guarded['authority_effect']} ({guarded['decision_scope']})")
    print()

    print("OBSERVED VALUE IN THIS TEST")
    print("  1. A missing approval changes continuation from implicit CONTINUE to HUMAN_GATE.")
    print("  2. The stop has a stable machine-readable reason code.")
    print("  3. The authorized return/residual-owner role remains explicit.")
    print("  4. RPE still grants no execution authority; it only evaluates the proposal.")
    print()
    print("Boundary: this is a synthetic repository-level comparison, not proof of real-world risk reduction.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
