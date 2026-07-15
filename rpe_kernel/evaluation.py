"""Deterministic evaluation of applicable requirement packs."""

from __future__ import annotations

from typing import Any

DECISION_ORDER = {"allow": 0, "hold": 1, "human_gate": 2, "deny": 3}


def evaluate_pack(pack: dict[str, Any], request: dict[str, Any]) -> dict[str, Any]:
    context = request.get("context", {})
    if not isinstance(context, dict):
        context = {}
    requirements = pack.get("requirements", [])
    missing = [name for name in requirements if context.get(name) is not True]
    decision = str(pack.get("decision_on_missing_requirement", "human_gate")) if missing else "allow"
    prefix = str(pack.get("reason_code_prefix", "RPE"))
    result: dict[str, Any] = {
        "pack_id": str(pack.get("pack_id", "unknown-pack")),
        "applicable": True,
        "decision": decision,
        "reason_codes": [f"{prefix}-MISSING-{name.replace('_', '-').upper()}" for name in missing],
        "missing_requirements": missing,
    }
    if decision != "allow":
        result["human_return"] = pack.get("human_return", {})
    return result


def combine_decisions(results: list[dict[str, Any]]) -> str:
    return max(
        (str(item["decision"]) for item in results),
        key=lambda value: DECISION_ORDER.get(value, 2),
        default="allow",
    )
