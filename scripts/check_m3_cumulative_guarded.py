#!/usr/bin/env python3
"""Check cumulative exposure composition through the guarded 0.2 adapter."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from rpe_kernel.guarded_adapter import evaluate_guarded_adapter_request

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "examples/external-kernel/minimal-governed-evaluation-request.json"


def main() -> int:
    governed = json.loads(FIXTURE.read_text(encoding="utf-8"))

    exceeded = evaluate_guarded_adapter_request({
        "contract_version": "0.2.0-exp",
        "governed_evaluation": governed,
        "cumulative_exposure_checks": [{
            "check": {
                "exposure_id": "bounded-autonomy",
                "dimensions": [{"name": "external_actions", "current": 5, "proposed_increment": 1, "budget": 5, "unit": "actions"}],
                "evidence_refs": ["caller-trajectory-state"],
            },
            "required_controls": ["require_authority"],
        }],
    }, today=date(2026, 9, 1))
    observation = exceeded["guard_observations"]["cumulative_exposure_results"][0]
    assert observation["status"] == "triggered", exceeded
    assert observation["threshold_origin"] == "caller_or_policy_supplied", exceeded
    assert observation["persistent_state_effect"] == "none", exceeded
    assert observation["trajectory_safety_claim"] is False, exceeded
    assert exceeded["transition_result"]["control_action"] == "require_authority", exceeded

    at_limit = evaluate_guarded_adapter_request({
        "contract_version": "0.2.0-exp",
        "governed_evaluation": governed,
        "cumulative_exposure_checks": [{
            "check": {"exposure_id": "bounded-autonomy", "dimensions": [{"name": "external_actions", "current": 4, "proposed_increment": 1, "budget": 5, "unit": "actions"}]},
            "required_controls": ["require_authority"],
        }],
    }, today=date(2026, 9, 1))
    assert at_limit["guard_observations"]["cumulative_exposure_results"][0]["status"] == "clear", at_limit
    assert at_limit["transition_result"]["control_action"] == "allow", at_limit

    unknown = evaluate_guarded_adapter_request({
        "contract_version": "0.2.0-exp",
        "governed_evaluation": governed,
        "cumulative_exposure_checks": [{
            "check": {"exposure_id": "bounded-autonomy", "dimensions": [{"name": "external_actions", "current": None, "proposed_increment": 1, "budget": 5, "unit": "actions"}]},
            "required_controls": ["hold"],
        }],
    }, today=date(2026, 9, 1))
    assert unknown["guard_observations"]["cumulative_exposure_results"][0]["status"] == "unknown", unknown
    assert unknown["transition_result"]["control_action"] == "hold", unknown

    competing = evaluate_guarded_adapter_request({
        "contract_version": "0.2.0-exp",
        "governed_evaluation": governed,
        "integrity_checks": [{
            "check": {"check_id": "config", "kind": "configuration", "expected": {"configuration_id": "a"}, "observed": {"configuration_id": "b"}},
            "required_controls": ["require_evidence"],
        }],
        "cumulative_exposure_checks": [{
            "check": {"exposure_id": "bounded-autonomy", "dimensions": [{"name": "external_actions", "current": 5, "proposed_increment": 1, "budget": 5, "unit": "actions"}]},
            "required_controls": ["require_authority"],
        }],
    }, today=date(2026, 9, 1))
    assert competing["transition_result"]["control_action"] == "hold", competing
    assert "RPE-M3-CONTROL-SELECTION-REQUIRED" in competing["risk_condition_result"]["reason_codes"], competing

    print("M3 cumulative exposure guarded-adapter checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
