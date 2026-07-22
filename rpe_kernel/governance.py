"""Runtime governance eligibility checks for requirement packs.

This module is intentionally bounded. It checks whether a human-maintained
pack governance record is eligible to enter evaluation; it does not validate
the underlying interpretation, legality, safety, or operational suitability.
"""

from __future__ import annotations

from datetime import date
from typing import Any

ACTIVE_STATE = "active"
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


def check_governance(record: dict[str, Any], *, today: date | None = None) -> list[str]:
    """Return stable reason codes for governance ineligibility."""
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

    last_reviewed = record.get("last_reviewed")
    if not isinstance(last_reviewed, str) or not last_reviewed:
        reasons.append("RPE-PACK-GOV-MISSING-REVIEW-DATE")

    next_review_due = record.get("next_review_due")
    if not isinstance(next_review_due, str) or not next_review_due:
        reasons.append("RPE-PACK-GOV-MISSING-NEXT-REVIEW-DUE")
    else:
        try:
            due = date.fromisoformat(next_review_due)
        except ValueError:
            reasons.append("RPE-PACK-GOV-INVALID-NEXT-REVIEW-DUE")
        else:
            if due < effective_today:
                reasons.append("RPE-PACK-GOV-REVIEW-EXPIRED")

    if record.get("interpretation_status") == "unreviewed":
        reasons.append("RPE-PACK-GOV-INTERPRETATION-UNREVIEWED")

    ambiguity = record.get("unresolved_ambiguity")
    if not isinstance(ambiguity, list) or not all(isinstance(item, str) for item in ambiguity):
        reasons.append("RPE-PACK-GOV-INVALID-AMBIGUITY-RECORD")

    human_return = record.get("human_return")
    role = human_return.get("role") if isinstance(human_return, dict) else None
    if not isinstance(role, str) or not role.strip():
        reasons.append("RPE-PACK-GOV-MISSING-HUMAN-RETURN")

    if state == "superseded" and not record.get("superseded_by"):
        reasons.append("RPE-PACK-GOV-SUPERSEDED-WITHOUT-REPLACEMENT")

    return sorted(set(reasons))


def governance_decision(record: dict[str, Any], *, today: date | None = None) -> dict[str, Any]:
    """Return the bounded runtime decision for a governance record."""
    reasons = check_governance(record, today=today)
    return {
        "pack_id": record.get("pack_id", "unknown-pack"),
        "eligible": not reasons,
        "decision": "allow" if not reasons else "human_gate",
        "reason_codes": reasons,
        "human_return": record.get("human_return", {}),
    }
