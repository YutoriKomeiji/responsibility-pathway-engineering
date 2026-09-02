#!/usr/bin/env python3
"""Deterministic checks for bounded M3 cumulative exposure evaluation."""

from __future__ import annotations

from rpe_kernel.cumulative_exposure import cumulative_exposure_to_risk_condition, evaluate_cumulative_exposure
from rpe_kernel.risk_conditions import evaluate_risk_conditions


def main() -> int:
    clear = evaluate_cumulative_exposure({
        "exposure_id": "bounded-autonomy",
        "dimensions": [
            {"name": "external_actions", "current": 2, "proposed_increment": 1, "budget": 5, "unit": "actions"},
            {"name": "targets", "current": 1, "proposed_increment": 0, "budget": 1, "unit": "targets"},
        ],
        "evidence_refs": ["caller-trajectory-state"],
    })
    assert clear["status"] == "clear", clear
    assert clear["dimensions"][0]["projected"] == 3, clear
    assert clear["universal_safety_claim"] is False, clear
    assert clear["trajectory_safety_claim"] is False, clear
    assert clear["persistent_state_effect"] == "none", clear

    exceeded = evaluate_cumulative_exposure({
        "exposure_id": "bounded-autonomy",
        "dimensions": [{"name": "external_actions", "current": 5, "proposed_increment": 1, "budget": 5, "unit": "actions"}],
    })
    assert exceeded["status"] == "triggered", exceeded
    assert exceeded["dimensions"][0]["status"] == "exceeded", exceeded
    condition = cumulative_exposure_to_risk_condition(exceeded, required_controls=["require_authority"])
    graph = evaluate_risk_conditions({"conditions": [condition]})
    assert graph["graph_status"] == "triggered", graph
    assert graph["required_controls"] == ["require_authority"], graph

    at_limit = evaluate_cumulative_exposure({
        "exposure_id": "bounded-autonomy",
        "dimensions": [{"name": "external_actions", "current": 4, "proposed_increment": 1, "budget": 5, "unit": "actions"}],
    })
    assert at_limit["status"] == "clear", at_limit
    assert at_limit["dimensions"][0]["status"] == "at_limit", at_limit

    unknown = evaluate_cumulative_exposure({
        "exposure_id": "bounded-autonomy",
        "dimensions": [{"name": "external_actions", "current": None, "proposed_increment": 1, "budget": 5, "unit": "actions"}],
    })
    assert unknown["status"] == "unknown", unknown
    unknown_condition = cumulative_exposure_to_risk_condition(unknown, required_controls=["hold"])
    unresolved = evaluate_risk_conditions({"conditions": [unknown_condition]})
    assert unresolved["graph_status"] == "unresolved", unresolved

    invalid = evaluate_cumulative_exposure({
        "exposure_id": "bounded-autonomy",
        "dimensions": [{"name": "external_actions", "current": -1, "proposed_increment": 1, "budget": 5, "unit": "actions"}],
    })
    assert invalid["status"] == "invalid", invalid
    assert "RPE-M3-CUMULATIVE-EXPOSURE-VALUE-INVALID" in invalid["reason_codes"], invalid

    print("M3 cumulative exposure checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
