#!/usr/bin/env python3
"""Synthetic host-side M3 decision enforcement, before any real tool call.

This sample intentionally does NOT create Authority. The configured "grant"
is a test fixture standing for a separate institution's trusted authorization
system. All writes below are to an in-memory list.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from examples.business_controls.vendor_bank_change_preflight import evaluate_preflight  # noqa: E402


class SyntheticExecutor:
    """No I/O beyond this Python process; no bank/ERP connection."""

    def __init__(self) -> None:
        self.effects: list[str] = []

    def dispatch(self, case_id: str) -> None:
        self.effects.append(case_id)


def host_pre_dispatch(
    proposal: dict[str, Any],
    *,
    authenticated_actor: str,
    authorized_target: str | None,
    executor: SyntheticExecutor,
) -> dict[str, Any]:
    """Demonstrate enforcement, not proof of identity or a real authority grant.

    authenticated_actor and authorized_target MUST come from a separately
    trusted host system in reality, never an LLM/tool's free-text assertion.
    """
    if not isinstance(authenticated_actor, str) or authenticated_actor != "accounts_payable_operator":
        return {"status": "not_dispatched", "reason": "host_actor_not_authorized", "simulated": True}
    if authorized_target is None or authorized_target != proposal.get("vendor_ref"):
        return {"status": "not_dispatched", "reason": "host_target_not_authorized", "simulated": True}

    result = evaluate_preflight(proposal)
    # A successful RPE evaluation is necessary here, but not sufficient.
    if (
        result.get("evaluation_decision") != "allow"
        or result.get("control_action") != "allow"
        or result.get("authority_effect") != "none"
        or result.get("execution_effect") != "none"
        or result.get("external_action_executed") is not False
        or result.get("missing_evidence")
    ):
        return {
            "status": "not_dispatched",
            "reason": "rpe_evaluation_requires_other_action",
            "control_action": result.get("control_action"),
            "simulated": True,
        }

    executor.dispatch(proposal["case_id"])
    return {
        "status": "synthetic_dispatch_recorded",
        "reason": "host_fixture_authorized_and_rpe_evaluation_allowed",
        "control_action": result["control_action"],
        "simulated": True,
        "real_external_effect": False,
    }


def main() -> int:
    base = {
        "case_id": "synthetic-ready",
        "vendor_ref": "vendor-only-test",
        "out_of_band_verified": True,
        "dual_control_approved": True,
        "account_mismatch": False,
    }
    executor = SyntheticExecutor()
    cases = [
        ("valid_with_host_grant", base, "accounts_payable_operator", base["vendor_ref"], "synthetic_dispatch_recorded"),
        ("no_host_grant", base, "accounts_payable_operator", None, "not_dispatched"),
        ("different_target", base, "accounts_payable_operator", "another-vendor", "not_dispatched"),
        ("untrusted_actor", base, "unknown-agent", base["vendor_ref"], "not_dispatched"),
        ("missing_evidence", {**base, "case_id": "synthetic-missing", "dual_control_approved": False}, "accounts_payable_operator", base["vendor_ref"], "not_dispatched"),
        ("mismatch_observed", {**base, "case_id": "synthetic-mismatch", "account_mismatch": True}, "accounts_payable_operator", base["vendor_ref"], "not_dispatched"),
    ]
    observed: dict[str, dict] = {}
    for label, proposal, actor, target, expected in cases:
        count = len(executor.effects)
        result = host_pre_dispatch(proposal, authenticated_actor=actor, authorized_target=target, executor=executor)
        assert result["status"] == expected, (label, result)
        assert len(executor.effects) == count + (1 if expected == "synthetic_dispatch_recorded" else 0), label
        observed[label] = result

    original = evaluate_preflight(base)
    with patch(__name__ + ".evaluate_preflight", return_value={**original, "authority_effect": "granted"}):
        before = len(executor.effects)
        tampered = host_pre_dispatch(base, authenticated_actor="accounts_payable_operator", authorized_target=base["vendor_ref"], executor=executor)
        assert tampered["status"] == "not_dispatched"
        assert len(executor.effects) == before
        observed["forged_rpe_authority_effect"] = tampered

    assert executor.effects == ["synthetic-ready"], executor.effects
    print(json.dumps({
        "test": "synthetic_host_pre_dispatch_enforcement",
        "cases": observed,
        "simulated_dispatch_count": len(executor.effects),
        "real_external_effects": 0,
        "evidence_scope": "untrusted_synthetic_host_and_rpe_fixtures_only",
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
