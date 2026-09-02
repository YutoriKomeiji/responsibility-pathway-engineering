"""Experimental M3 caller-observed cumulative exposure evaluation.

This module does not persist trajectory history and does not define a universal
risk threshold. It compares caller-supplied current usage, proposed increments,
and explicit budgets. Results are bounded observations that may be translated
into Risk Condition nodes only with caller/policy-supplied controls.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

CUMULATIVE_EXPOSURE_CONTRACT_VERSION = "0.1.0-exp"


def _nonnegative_int(value: Any) -> int | None:
    return value if isinstance(value, int) and not isinstance(value, bool) and value >= 0 else None


def evaluate_cumulative_exposure(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Compare one caller-declared cumulative state with explicit budgets."""
    base = {
        "contract_version": CUMULATIVE_EXPOSURE_CONTRACT_VERSION,
        "authority_effect": "none",
        "execution_effect": "none",
        "persistent_state_effect": "none",
        "threshold_origin": "caller_or_policy_supplied",
        "universal_safety_claim": False,
        "trajectory_safety_claim": False,
    }
    if not isinstance(payload, Mapping):
        return {**base, "exposure_id": None, "status": "invalid", "dimensions": [], "reason_codes": ["RPE-M3-CUMULATIVE-EXPOSURE-INVALID"]}

    allowed = {"exposure_id", "dimensions", "evidence_refs"}
    if set(payload) - allowed:
        return {**base, "exposure_id": payload.get("exposure_id") if isinstance(payload.get("exposure_id"), str) else None, "status": "invalid", "dimensions": [], "reason_codes": ["RPE-M3-CUMULATIVE-EXPOSURE-UNKNOWN-FIELD"]}

    exposure_id = payload.get("exposure_id")
    raw_dimensions = payload.get("dimensions")
    reasons: list[str] = []
    if not isinstance(exposure_id, str) or not exposure_id:
        reasons.append("RPE-M3-CUMULATIVE-EXPOSURE-MISSING-ID")
        exposure_id = None
    if not isinstance(raw_dimensions, Sequence) or isinstance(raw_dimensions, (str, bytes, bytearray)) or not raw_dimensions:
        reasons.append("RPE-M3-CUMULATIVE-EXPOSURE-MISSING-DIMENSIONS")
        raw_dimensions = []

    dimensions: list[dict[str, Any]] = []
    names: set[str] = set()
    any_unknown = False
    any_exceeded = False
    for raw in raw_dimensions:
        if not isinstance(raw, Mapping) or set(raw) - {"name", "current", "proposed_increment", "budget", "unit"}:
            reasons.append("RPE-M3-CUMULATIVE-EXPOSURE-DIMENSION-INVALID")
            continue
        name = raw.get("name")
        if not isinstance(name, str) or not name or name in names:
            reasons.append("RPE-M3-CUMULATIVE-EXPOSURE-DIMENSION-ID-INVALID")
            continue
        names.add(name)
        unit = raw.get("unit")
        if not isinstance(unit, str) or not unit:
            reasons.append("RPE-M3-CUMULATIVE-EXPOSURE-UNIT-INVALID")
            continue
        current_raw = raw.get("current")
        increment_raw = raw.get("proposed_increment")
        budget_raw = raw.get("budget")
        current = _nonnegative_int(current_raw)
        increment = _nonnegative_int(increment_raw)
        budget = _nonnegative_int(budget_raw)

        if current_raw is None or increment_raw is None or budget_raw is None:
            status = "unknown"
            projected = None
            any_unknown = True
        elif current is None or increment is None or budget is None:
            reasons.append("RPE-M3-CUMULATIVE-EXPOSURE-VALUE-INVALID")
            continue
        else:
            projected = current + increment
            status = "exceeded" if projected > budget else ("at_limit" if projected == budget else "within_budget")
            any_exceeded = any_exceeded or status == "exceeded"
        dimensions.append({"name": name, "unit": unit, "current": current, "proposed_increment": increment, "budget": budget, "projected": projected, "status": status})

    if reasons:
        status = "invalid"
    elif any_unknown:
        status = "unknown"
    elif any_exceeded:
        status = "triggered"
    else:
        status = "clear"

    evidence_refs = []
    raw_refs = payload.get("evidence_refs")
    if isinstance(raw_refs, Sequence) and not isinstance(raw_refs, (str, bytes, bytearray)):
        evidence_refs = sorted({item for item in raw_refs if isinstance(item, str) and item})

    return {**base, "exposure_id": exposure_id, "status": status, "dimensions": dimensions, "evidence_refs": evidence_refs, "reason_codes": sorted(set(reasons))}


def cumulative_exposure_to_risk_condition(result: Mapping[str, Any], *, required_controls: Sequence[str]) -> dict[str, Any]:
    """Translate a cumulative observation into a policy-declared risk node."""
    exposure_id = result.get("exposure_id") if isinstance(result, Mapping) else None
    status = result.get("status") if isinstance(result, Mapping) else None
    risk_status = "clear" if status == "clear" else ("triggered" if status == "triggered" else "unknown")
    controls = sorted({item for item in required_controls if isinstance(item, str) and item})
    refs = result.get("evidence_refs", []) if isinstance(result, Mapping) else []
    return {
        "condition_id": f"cumulative:{exposure_id}" if isinstance(exposure_id, str) and exposure_id else "cumulative:unknown",
        "status": risk_status,
        "required_controls": controls,
        "depends_on": [],
        "evidence_refs": [item for item in refs if isinstance(item, str) and item],
    }
