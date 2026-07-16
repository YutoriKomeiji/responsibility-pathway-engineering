#!/usr/bin/env python3
"""Bounded structural checks for requirement-pack governance records."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any

ACTIVE_STATE = "active"
INELIGIBLE_STATES = {"draft", "reviewed", "approved", "suspended", "superseded", "retired"}
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


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("governance record must be a JSON object")
    return value


def check_record(record: dict[str, Any], *, today: date) -> list[str]:
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
            if due < today:
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--today", type=date.fromisoformat, default=date.today())
    args = parser.parse_args()

    try:
        record = load_json(args.path)
        reasons = check_record(record, today=args.today)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"eligible": False, "decision": "human_gate", "errors": [str(exc)]}, indent=2))
        return 1

    result = {
        "pack_id": record.get("pack_id", "unknown-pack"),
        "eligible": not reasons,
        "decision": "allow" if not reasons else "human_gate",
        "reason_codes": reasons,
        "human_return": record.get("human_return", {}),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not reasons else 1


if __name__ == "__main__":
    raise SystemExit(main())
