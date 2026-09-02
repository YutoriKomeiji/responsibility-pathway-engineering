"""Experimental M3 Human Return readiness evaluation.

This module checks whether a declared Human Return destination carries enough
structured information to receive a bounded review. It does not establish that
the named person or institution has legitimate authority, sufficient competence,
or that supplied evidence is true.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

HUMAN_RETURN_CONTRACT_VERSION = "0.1.0-exp"
CAPABILITY_STATUSES = frozenset({"available", "limited", "unknown"})
WINDOW_STATUSES = frozenset({"available", "limited", "expired", "unknown"})


def _strings(value: Any) -> list[str]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        return []
    return sorted({item for item in value if isinstance(item, str) and item})


def _result(
    *,
    return_id: str | None,
    readiness: str,
    reasons: list[str],
    available_evidence: list[str] | None = None,
    missing_evidence: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "contract_version": HUMAN_RETURN_CONTRACT_VERSION,
        "return_id": return_id,
        "readiness": readiness,
        "reason_codes": sorted(set(reasons)),
        "available_evidence": available_evidence or [],
        "missing_evidence": missing_evidence or [],
        "authority_effect": "none",
        "human_decision_effect": "none",
        "authority_validity_claim": False,
        "capability_validity_claim": False,
        "evidence_truth_claim": False,
        "assessment_scope": "caller_supplied_return_readiness_only",
    }


def evaluate_human_return_readiness(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Evaluate structural readiness of a caller-declared Human Return target."""
    if not isinstance(payload, Mapping):
        return _result(
            return_id=None,
            readiness="invalid",
            reasons=["RPE-M3-HUMAN-RETURN-INVALID"],
        )

    allowed = {
        "return_id",
        "owner_role",
        "authority_reference",
        "capability_status",
        "response_window_status",
        "next_decision_scope",
        "evidence_scope",
    }
    if set(payload) - allowed:
        return _result(
            return_id=payload.get("return_id") if isinstance(payload.get("return_id"), str) else None,
            readiness="invalid",
            reasons=["RPE-M3-HUMAN-RETURN-UNKNOWN-FIELD"],
        )

    return_id = payload.get("return_id")
    owner_role = payload.get("owner_role")
    authority_reference = payload.get("authority_reference")
    capability_status = payload.get("capability_status")
    window_status = payload.get("response_window_status")
    decision_scope = payload.get("next_decision_scope")
    evidence_scope = payload.get("evidence_scope")

    structural_reasons: list[str] = []
    if not isinstance(return_id, str) or not return_id:
        structural_reasons.append("RPE-M3-HUMAN-RETURN-MISSING-ID")
        return_id = None
    if not isinstance(owner_role, str) or not owner_role:
        structural_reasons.append("RPE-M3-HUMAN-RETURN-MISSING-OWNER")
    if authority_reference is not None and (
        not isinstance(authority_reference, str) or not authority_reference
    ):
        structural_reasons.append("RPE-M3-HUMAN-RETURN-INVALID-AUTHORITY-REFERENCE")
    if capability_status not in CAPABILITY_STATUSES:
        structural_reasons.append("RPE-M3-HUMAN-RETURN-INVALID-CAPABILITY-STATUS")
    if window_status not in WINDOW_STATUSES:
        structural_reasons.append("RPE-M3-HUMAN-RETURN-INVALID-WINDOW-STATUS")
    if not isinstance(decision_scope, str) or not decision_scope:
        structural_reasons.append("RPE-M3-HUMAN-RETURN-MISSING-DECISION-SCOPE")
    if not isinstance(evidence_scope, Mapping):
        structural_reasons.append("RPE-M3-HUMAN-RETURN-INVALID-EVIDENCE-SCOPE")
        available: list[str] = []
        missing: list[str] = []
    else:
        available_raw = evidence_scope.get("available")
        missing_raw = evidence_scope.get("missing")
        if not isinstance(available_raw, Sequence) or isinstance(available_raw, (str, bytes, bytearray)):
            structural_reasons.append("RPE-M3-HUMAN-RETURN-INVALID-EVIDENCE-SCOPE")
        if not isinstance(missing_raw, Sequence) or isinstance(missing_raw, (str, bytes, bytearray)):
            structural_reasons.append("RPE-M3-HUMAN-RETURN-INVALID-EVIDENCE-SCOPE")
        available = _strings(available_raw)
        missing = _strings(missing_raw)

    if structural_reasons:
        return _result(
            return_id=return_id,
            readiness="invalid",
            reasons=structural_reasons,
            available_evidence=available,
            missing_evidence=missing,
        )

    reasons: list[str] = []
    if authority_reference is None:
        reasons.append("RPE-M3-HUMAN-RETURN-AUTHORITY-REFERENCE-UNKNOWN")
    if missing:
        reasons.append("RPE-M3-HUMAN-RETURN-EVIDENCE-INCOMPLETE")
    if capability_status == "limited":
        reasons.append("RPE-M3-HUMAN-RETURN-CAPABILITY-LIMITED")
    elif capability_status == "unknown":
        reasons.append("RPE-M3-HUMAN-RETURN-CAPABILITY-UNKNOWN")
    if window_status == "limited":
        reasons.append("RPE-M3-HUMAN-RETURN-WINDOW-LIMITED")
    elif window_status == "expired":
        reasons.append("RPE-M3-HUMAN-RETURN-WINDOW-EXPIRED")
    elif window_status == "unknown":
        reasons.append("RPE-M3-HUMAN-RETURN-WINDOW-UNKNOWN")

    hard_unresolved = (
        authority_reference is None
        or bool(missing)
        or capability_status == "unknown"
        or window_status in {"expired", "unknown"}
    )
    readiness = "unresolved" if hard_unresolved else ("conditional" if reasons else "ready_for_review")

    return _result(
        return_id=return_id,
        readiness=readiness,
        reasons=reasons,
        available_evidence=available,
        missing_evidence=missing,
    )


def human_return_result_to_risk_condition(
    result: Mapping[str, Any],
    *,
    required_controls: Sequence[str],
) -> dict[str, Any]:
    """Translate readiness into a declarative Risk Condition node.

    Required controls are caller/policy supplied. This function does not choose
    the operational response to an unresolved or conditional return target.
    """
    return_id = result.get("return_id")
    readiness = result.get("readiness")
    if readiness == "ready_for_review":
        status = "clear"
    elif readiness in {"conditional", "unresolved"}:
        status = "triggered" if readiness == "conditional" else "unknown"
    else:
        status = "unknown"
    return {
        "condition_id": f"human_return:{return_id or 'unknown'}",
        "status": status,
        "required_controls": [item for item in required_controls if isinstance(item, str) and item],
        "depends_on": [],
        "evidence_refs": [
            f"human-return-readiness:{return_id}"
        ] if isinstance(return_id, str) and return_id else [],
    }
