"""Composable Python API for applicability resolution and evaluation."""

from __future__ import annotations

from datetime import date
from typing import Any, Mapping, Sequence

from .applicability import resolve_pack
from .compatibility import check_contract_version, pack_contract_version, request_contract_version
from .evaluation import combine_decisions, evaluate_pack
from .governance import governance_decision

GATE_DECISION_CONTRACT_VERSION = "1.0.0"


def _human_gate(
    request: dict[str, Any],
    *,
    stage: str,
    reason_codes: list[str],
    human_return: dict[str, Any],
    next_step: str,
    applicability: list[dict[str, Any]] | None = None,
    pack_decisions: list[dict[str, Any]] | None = None,
    governance: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    return {
        "contract_version": GATE_DECISION_CONTRACT_VERSION,
        "request_id": request.get("request_id"),
        "decision": "human_gate",
        "stage": stage,
        "reason_codes": reason_codes,
        "applicability": applicability or [],
        "pack_decisions": pack_decisions or [],
        "governance": governance or [],
        "human_return": human_return,
        "next_step": next_step,
    }


def evaluate_action(
    request: dict[str, Any],
    packs: Sequence[dict[str, Any]],
    *,
    governance_records: Mapping[str, dict[str, Any]] | None = None,
    today: date | None = None,
    enforce_contract_versions: bool = False,
) -> dict[str, Any]:
    """Resolve applicability, enforce optional M2 entry gates, and evaluate packs.

    The two-argument M1 call remains supported. M2 callers should supply
    governance_records and enable contract-version enforcement. A governance or
    compatibility failure returns ``human_gate`` before requirement evaluation.
    """
    if enforce_contract_versions:
        request_reasons = check_contract_version("action_request", request_contract_version(request))
        if request_reasons:
            return _human_gate(
                request,
                stage="compatibility",
                reason_codes=request_reasons,
                human_return={"role": "contract_compatibility_owner"},
                next_step="migrate_or_review_action_request_contract",
            )

        pack_version_reasons: list[str] = []
        for pack in packs:
            pack_version_reasons.extend(check_contract_version("requirement_pack", pack_contract_version(pack)))
        if pack_version_reasons:
            return _human_gate(
                request,
                stage="compatibility",
                reason_codes=sorted(set(pack_version_reasons)),
                human_return={"role": "contract_compatibility_owner"},
                next_step="migrate_or_review_requirement_pack_contract",
            )

    governance_results: list[dict[str, Any]] = []
    if governance_records is not None:
        for pack in packs:
            pack_id = str(pack.get("pack_id", "unknown-pack"))
            record = governance_records.get(pack_id)
            if record is None:
                governance_results.append(
                    {
                        "pack_id": pack_id,
                        "eligible": False,
                        "decision": "human_gate",
                        "reason_codes": ["RPE-PACK-GOV-MISSING-RECORD"],
                        "human_return": {"role": "requirement_pack_governance_owner"},
                    }
                )
            else:
                governance_results.append(governance_decision(record, today=today))

        governance_failures = [item for item in governance_results if not item["eligible"]]
        if governance_failures:
            return _human_gate(
                request,
                stage="governance",
                reason_codes=sorted({code for item in governance_failures for code in item["reason_codes"]}),
                human_return=governance_failures[0].get("human_return") or {"role": "requirement_pack_governance_owner"},
                next_step="review_requirement_pack_governance",
                governance=governance_results,
            )

    resolutions = [resolve_pack(pack, request, str(pack.get("pack_id", index))) for index, pack in enumerate(packs)]
    unknown_ids = [item["pack_id"] for item in resolutions if item["status"] == "unknown"]
    applicable_indexes = [index for index, item in enumerate(resolutions) if item["status"] == "applicable"]

    if unknown_ids:
        return _human_gate(
            request,
            stage="applicability",
            reason_codes=["RPE-APPLICABILITY-UNKNOWN"],
            applicability=resolutions,
            governance=governance_results,
            human_return={"role": "applicability_review_owner"},
            next_step="review_unknown_applicability",
        )

    if not applicable_indexes:
        return _human_gate(
            request,
            stage="applicability",
            reason_codes=["RPE-APPLICABILITY-NO-APPLICABLE-PACKS"],
            applicability=resolutions,
            governance=governance_results,
            human_return={"role": "applicability_review_owner"},
            next_step="select_or_review_requirement_packs",
        )

    decisions = [evaluate_pack(packs[index], request) for index in applicable_indexes]
    combined = combine_decisions(decisions)
    human_returns = [item.get("human_return") for item in decisions if item.get("human_return")]
    return {
        "contract_version": GATE_DECISION_CONTRACT_VERSION,
        "request_id": request.get("request_id"),
        "decision": combined,
        "stage": "evaluation",
        "reason_codes": [code for item in decisions for code in item["reason_codes"]],
        "applicability": resolutions,
        "pack_decisions": decisions,
        "governance": governance_results,
        "human_return": human_returns[0] if human_returns else None,
        "next_step": "continue_action" if combined == "allow" else "return_to_human",
    }
