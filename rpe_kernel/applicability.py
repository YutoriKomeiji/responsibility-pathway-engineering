"""Deterministic requirement-pack applicability resolution."""

from __future__ import annotations

from typing import Any

APPLICABILITY_FIELDS = ("action", "jurisdiction", "organization", "data_class")


def _request_value(request: dict[str, Any], field: str) -> Any:
    if field == "action":
        return request.get("action")
    context = request.get("applicability_context", {})
    return context.get(field) if isinstance(context, dict) else None


def resolve_pack(pack: dict[str, Any], request: dict[str, Any], pack_ref: str | None = None) -> dict[str, Any]:
    conditions = pack.get("applies_when", {})
    if not isinstance(conditions, dict):
        conditions = {}
    missing: list[str] = []
    mismatches: list[dict[str, Any]] = []
    matched: list[str] = []
    for field in APPLICABILITY_FIELDS:
        if field not in conditions:
            continue
        expected = conditions[field]
        observed = _request_value(request, field)
        if observed is None:
            missing.append(field)
        elif observed != expected:
            mismatches.append({"field": field, "expected": expected, "observed": observed})
        else:
            matched.append(field)
    if mismatches:
        status = "not_applicable"
        reasons = ["RPE-APPLICABILITY-CONDITION-MISMATCH"]
    elif missing:
        status = "unknown"
        reasons = [f"RPE-APPLICABILITY-MISSING-{field.replace('_', '-').upper()}" for field in missing]
    else:
        status = "applicable"
        reasons = ["RPE-APPLICABILITY-CONDITIONS-MATCHED"]
    return {
        "pack_id": str(pack.get("pack_id", "unknown-pack")),
        "pack_ref": pack_ref,
        "status": status,
        "matched_fields": matched,
        "missing_context": missing,
        "mismatches": mismatches,
        "reason_codes": reasons,
    }
