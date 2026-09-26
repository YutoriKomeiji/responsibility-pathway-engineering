"""Experimental M3 identity-integrity comparisons.

These helpers compare caller-supplied expected and observed identities. They do
not authenticate either side, create authority, or infer trust from content.
Their output is evidence for a bounded comparison only and can be translated
into Risk Condition Graph nodes by an explicit caller/policy layer.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

INTEGRITY_CONTRACT_VERSION = "0.1.0-exp"
INTEGRITY_KINDS = frozenset({"configuration", "relationship"})
INTEGRITY_STATUSES = frozenset({"clear", "triggered", "unknown", "invalid"})


def _strings(value: Any) -> list[str]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        return []
    return [item for item in value if isinstance(item, str) and item]


def _identity(value: Any) -> dict[str, str] | None:
    """Normalize a bounded identity mapping or return None when unavailable."""
    if value is None:
        return None
    if not isinstance(value, Mapping) or not value:
        return None
    normalized: dict[str, str] = {}
    for key, item in value.items():
        if not isinstance(key, str) or not key or not isinstance(item, str) or not item:
            return None
        normalized[key] = item
    return dict(sorted(normalized.items()))


def compare_integrity_binding(check: Mapping[str, Any]) -> dict[str, Any]:
    """Compare one expected/observed configuration or relationship identity.

    `expected` and `observed` are both caller-supplied claims. Equality therefore
    establishes only comparison consistency, not independent authentication.
    """
    if not isinstance(check, Mapping):
        return {
            "contract_version": INTEGRITY_CONTRACT_VERSION,
            "status": "invalid",
            "reason_codes": ["RPE-M3-INTEGRITY-CHECK-INVALID"],
            "comparison_scope": "caller_supplied_identity_comparison_only",
            "authority_effect": "none",
        }

    check_id = check.get("check_id")
    kind = check.get("kind")
    expected = _identity(check.get("expected"))
    observed_raw = check.get("observed")
    observed = _identity(observed_raw)
    evidence_refs = sorted(set(_strings(check.get("evidence_refs"))))

    reasons: list[str] = []
    if not isinstance(check_id, str) or not check_id:
        reasons.append("RPE-M3-INTEGRITY-CHECK-MISSING-ID")
    if kind not in INTEGRITY_KINDS:
        reasons.append("RPE-M3-INTEGRITY-CHECK-UNSUPPORTED-KIND")
    if expected is None:
        reasons.append("RPE-M3-INTEGRITY-CHECK-MISSING-EXPECTED-IDENTITY")

    if reasons:
        status = "invalid"
    elif observed_raw is None:
        status = "unknown"
        reasons.append("RPE-M3-INTEGRITY-OBSERVED-IDENTITY-UNKNOWN")
    elif observed is None:
        status = "invalid"
        reasons.append("RPE-M3-INTEGRITY-OBSERVED-IDENTITY-INVALID")
    elif observed != expected:
        status = "triggered"
        reasons.append("RPE-M3-INTEGRITY-IDENTITY-MISMATCH")
    else:
        status = "clear"

    return {
        "contract_version": INTEGRITY_CONTRACT_VERSION,
        "check_id": check_id if isinstance(check_id, str) else None,
        "kind": kind if isinstance(kind, str) else None,
        "status": status,
        "expected": expected,
        "observed": observed,
        "evidence_refs": evidence_refs,
        "reason_codes": sorted(set(reasons)),
        "comparison_scope": "caller_supplied_identity_comparison_only",
        "independent_authentication_claim": False,
        "authority_effect": "none",
    }


def integrity_result_to_risk_condition(
    result: Mapping[str, Any],
    *,
    required_controls: Sequence[str],
) -> dict[str, Any]:
    """Translate a bounded integrity comparison into a declarative risk node.

    Control selection is supplied explicitly by the caller/policy layer rather
    than invented by the integrity comparator.
    """
    check_id = result.get("check_id") if isinstance(result, Mapping) else None
    status = result.get("status") if isinstance(result, Mapping) else None
    risk_status = "clear" if status == "clear" else ("triggered" if status == "triggered" else "unknown")
    controls = sorted(set(_strings(required_controls)))
    evidence_refs = _strings(result.get("evidence_refs")) if isinstance(result, Mapping) else []
    return {
        "condition_id": f"integrity:{check_id}" if isinstance(check_id, str) and check_id else "integrity:unknown",
        "status": risk_status,
        "required_controls": controls,
        "depends_on": [],
        "evidence_refs": sorted(set(evidence_refs)),
    }
