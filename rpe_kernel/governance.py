"""Runtime governance eligibility checks for requirement packs.

This module is intentionally bounded. It checks whether a human-maintained
pack governance record is eligible to enter evaluation; it does not validate
the underlying interpretation, legality, safety, or operational suitability.
"""

from __future__ import annotations

from datetime import date
from typing import Any

ACTIVE_STATE = "active"
STRICT_ELIGIBLE_INTERPRETATION_STATES = {"reviewed_mapping", "not_applicable"}
LEGACY_ELIGIBLE_INTERPRETATION_STATES = STRICT_ELIGIBLE_INTERPRETATION_STATES | {"reviewed"}
REQUIRED_TEXT_FIELDS = (
    "pack_id",
    "pack_version",
    "maintenance_owner",
    "reviewer",
    "approver",
    "source_authority",
    "source_version",
    "jurisdiction",
    "effective_scope",
)


def _parse_date(value: Any) -> date | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def check_governance(
    record: dict[str, Any],
    *,
    today: date | None = None,
    strict: bool = False,
) -> list[str]:
    """Return stable reason codes for governance ineligibility.

    ``strict=True`` is reserved for the explicit governed M2 entry. The legacy
    checker keeps bounded migration compatibility for historical records.
    """
    effective_today = today or date.today()
    reasons: list[str] = []

    state = record.get("lifecycle_state")
    if state != ACTIVE_STATE:
        reasons.append("RPE-PACK-GOV-NOT-ACTIVE")

    field_codes = {
        "maintenance_owner": "RPE-PACK-GOV-MISSING-MAINTENANCE-OWNER",
        "reviewer": "RPE-PACK-GOV-MISSING-REVIEWER",
        "approver": "RPE-PACK-GOV-MISSING-APPROVER",
    }
    for field in REQUIRED_TEXT_FIELDS:
        value = record.get(field)
        if not isinstance(value, str) or not value.strip():
            reasons.append(field_codes.get(field, f"RPE-PACK-GOV-MISSING-{field.replace('_', '-').upper()}"))

    interpretation_status = record.get("interpretation_status")
    eligible_states = STRICT_ELIGIBLE_INTERPRETATION_STATES if strict else LEGACY_ELIGIBLE_INTERPRETATION_STATES
    if interpretation_status not in eligible_states:
        reasons.append("RPE-PACK-GOV-INTERPRETATION-NOT-ELIGIBLE")

    ambiguity = record.get("unresolved_ambiguity")
    if not isinstance(ambiguity, list) or not all(isinstance(item, str) for item in ambiguity):
        reasons.append("RPE-PACK-GOV-INVALID-AMBIGUITY-RECORD")
    elif strict and ambiguity:
        reasons.append("RPE-PACK-GOV-UNRESOLVED-AMBIGUITY")

    last_reviewed_raw = record.get("last_reviewed")
    last_reviewed = _parse_date(last_reviewed_raw)
    if not isinstance(last_reviewed_raw, str) or not last_reviewed_raw:
        reasons.append("RPE-PACK-GOV-MISSING-REVIEW-DATE")
    elif last_reviewed is None:
        reasons.append("RPE-PACK-GOV-INVALID-REVIEW-DATE")
    elif strict and last_reviewed > effective_today:
        reasons.append("RPE-PACK-GOV-REVIEW-DATE-IN-FUTURE")

    next_review_due_raw = record.get("next_review_due")
    next_review_due = _parse_date(next_review_due_raw)
    if not isinstance(next_review_due_raw, str) or not next_review_due_raw:
        reasons.append("RPE-PACK-GOV-MISSING-NEXT-REVIEW-DUE")
    elif next_review_due is None:
        reasons.append("RPE-PACK-GOV-INVALID-NEXT-REVIEW-DUE")
    else:
        if next_review_due < effective_today:
            reasons.append("RPE-PACK-GOV-REVIEW-EXPIRED")
        if strict and last_reviewed is not None and next_review_due < last_reviewed:
            reasons.append("RPE-PACK-GOV-INVALID-REVIEW-DATE-ORDER")

    effective_date_raw = record.get("effective_date")
    if strict and effective_date_raw is not None:
        effective_date = _parse_date(effective_date_raw)
        if effective_date is None:
            reasons.append("RPE-PACK-GOV-INVALID-EFFECTIVE-DATE")
        elif effective_date > effective_today:
            reasons.append("RPE-PACK-GOV-NOT-YET-EFFECTIVE")

    human_return = record.get("human_return")
    role = human_return.get("role") if isinstance(human_return, dict) else None
    if not isinstance(role, str) or not role.strip():
        reasons.append("RPE-PACK-GOV-MISSING-HUMAN-RETURN")

    if state == "superseded" and not record.get("superseded_by"):
        reasons.append("RPE-PACK-GOV-SUPERSEDED-WITHOUT-REPLACEMENT")

    return sorted(set(reasons))


def governance_decision(
    record: dict[str, Any],
    *,
    today: date | None = None,
    strict: bool = False,
) -> dict[str, Any]:
    """Return the bounded runtime decision for a governance record."""
    reasons = check_governance(record, today=today, strict=strict)
    return {
        "pack_id": record.get("pack_id", "unknown-pack"),
        "pack_version": record.get("pack_version"),
        "eligible": not reasons,
        "decision": "allow" if not reasons else "human_gate",
        "reason_codes": reasons,
        "human_return": record.get("human_return", {}),
    }
