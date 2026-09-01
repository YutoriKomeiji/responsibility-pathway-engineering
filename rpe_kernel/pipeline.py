"""Composable Python API for applicability resolution and evaluation."""

from __future__ import annotations

from datetime import date
from typing import Any, Mapping, Sequence

from .applicability import resolve_pack
from .compatibility import (
    check_contract_version,
    governance_contract_version,
    pack_contract_version,
    request_contract_version,
)
from .evaluation import combine_decisions, evaluate_pack
from .governance import governance_decision

GATE_DECISION_CONTRACT_VERSION = "1.0.0"
GOVERNED_RESULT_CONTRACT_VERSION = "1.2.0"


def _human_gate(
    request: dict[str, Any],
    *,
    stage: str,
    reason_codes: list[str],
    human_return: dict[str, Any] | None,
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


def _pack_ref(binding_id: str, pack: dict[str, Any], governance: dict[str, Any]) -> dict[str, Any]:
    return {
        "binding_id": binding_id,
        "pack_id": str(pack.get("pack_id", "unknown-pack")),
        "pack_version": str(pack.get("version", "unknown-version")),
        "governance_contract_version": str(governance.get("contract_version", "unknown-version")),
    }


def _normalize_transport_provenance(value: Any) -> tuple[dict[str, Any] | None, list[str]]:
    if value is None:
        return None, []
    if not isinstance(value, dict):
        return None, ["RPE-GOVERNED-ADMISSION-INVALID-TRANSPORT-PROVENANCE"]

    source_kind = value.get("source_kind")
    content_sha256 = value.get("content_sha256")
    byte_length = value.get("byte_length")
    observation_scope = value.get("observation_scope")
    valid_digest = (
        isinstance(content_sha256, str)
        and len(content_sha256) == 64
        and all(character in "0123456789abcdef" for character in content_sha256)
    )
    valid_length = isinstance(byte_length, int) and not isinstance(byte_length, bool) and byte_length >= 0
    if (
        source_kind not in {"caller_content", "local_file"}
        or not valid_digest
        or not valid_length
        or observation_scope != "transport_bytes_only"
    ):
        return None, ["RPE-GOVERNED-ADMISSION-INVALID-TRANSPORT-PROVENANCE"]

    return {
        "source_kind": source_kind,
        "content_sha256": content_sha256,
        "byte_length": byte_length,
        "observation_scope": "transport_bytes_only",
    }, []


def _responsibility_handoff(
    request: dict[str, Any],
    *,
    decision: str,
    reason_codes: list[str],
    selected_pack_refs: list[dict[str, Any]],
    rejected_pack_refs: list[dict[str, Any]],
    human_return: dict[str, Any] | None,
    transport_provenance: dict[str, Any] | None,
) -> dict[str, Any]:
    evidence_scope = request.get("evidence_scope")
    if not isinstance(evidence_scope, dict):
        evidence_scope = {"available": [], "missing": []}
    residual_owner_role = "downstream_execution_owner"
    if isinstance(human_return, dict):
        role = human_return.get("role")
        if isinstance(role, str) and role:
            residual_owner_role = role
    return {
        "authority_effect": "none",
        "decision_scope": "evaluation_only",
        "evaluation_decision": decision,
        "evaluation_reason_codes": sorted(set(reason_codes)),
        "selected_pack_refs": selected_pack_refs,
        "rejected_pack_refs": rejected_pack_refs,
        "evaluation_evidence_scope": {
            "available": list(evidence_scope.get("available", [])) if isinstance(evidence_scope.get("available", []), list) else [],
            "missing": list(evidence_scope.get("missing", [])) if isinstance(evidence_scope.get("missing", []), list) else [],
        },
        "transport_provenance": dict(transport_provenance) if transport_provenance is not None else None,
        "human_return": human_return,
        "downstream_obligations": {
            "dispatch_authority_required": True,
            "effect_verification_required_for_effect_claim": True,
            "receipt_sufficient_for_effect_claim": False,
            "reauthorization_required_for": ["retry", "repair", "resume"],
            "authority_owner": "downstream_runtime_or_institution",
            "residual_owner_role": residual_owner_role,
        },
    }


def _governed_result(
    request: dict[str, Any],
    *,
    decision: str,
    stage: str,
    reason_codes: list[str],
    human_return: dict[str, Any] | None,
    next_step: str,
    selected_pack_refs: list[dict[str, Any]],
    rejected_pack_refs: list[dict[str, Any]],
    applicability: list[dict[str, Any]] | None = None,
    pack_decisions: list[dict[str, Any]] | None = None,
    governance: list[dict[str, Any]] | None = None,
    transport_provenance: dict[str, Any] | None = None,
) -> dict[str, Any]:
    normalized_reason_codes = sorted(set(reason_codes))
    return {
        "contract_version": GOVERNED_RESULT_CONTRACT_VERSION,
        "request_id": request.get("request_id"),
        "decision": decision,
        "stage": stage,
        "reason_codes": normalized_reason_codes,
        "applicability": applicability or [],
        "pack_decisions": pack_decisions or [],
        "governance": governance or [],
        "human_return": human_return,
        "next_step": next_step,
        "responsibility_handoff": _responsibility_handoff(
            request,
            decision=decision,
            reason_codes=normalized_reason_codes,
            selected_pack_refs=selected_pack_refs,
            rejected_pack_refs=rejected_pack_refs,
            human_return=human_return,
            transport_provenance=transport_provenance,
        ),
    }


def _evaluate_core(
    request: dict[str, Any],
    packs: Sequence[dict[str, Any]],
    *,
    governance_results: list[dict[str, Any]] | None = None,
    governed_refs: list[dict[str, Any]] | None = None,
    transport_provenance: dict[str, Any] | None = None,
) -> dict[str, Any]:
    governance_results = governance_results or []
    resolutions = [resolve_pack(pack, request, str(pack.get("pack_id", index))) for index, pack in enumerate(packs)]
    unknown_ids = [item["pack_id"] for item in resolutions if item["status"] == "unknown"]
    applicable_indexes = [index for index, item in enumerate(resolutions) if item["status"] == "applicable"]

    if governed_refs is not None:
        if unknown_ids:
            return _governed_result(
                request,
                decision="human_gate",
                stage="applicability",
                reason_codes=["RPE-APPLICABILITY-UNKNOWN"],
                applicability=resolutions,
                governance=governance_results,
                human_return={"role": "applicability_review_owner"},
                next_step="review_unknown_applicability",
                selected_pack_refs=[],
                rejected_pack_refs=governed_refs,
                transport_provenance=transport_provenance,
            )
        if not applicable_indexes:
            return _governed_result(
                request,
                decision="human_gate",
                stage="applicability",
                reason_codes=["RPE-APPLICABILITY-NO-APPLICABLE-PACKS"],
                applicability=resolutions,
                governance=governance_results,
                human_return={"role": "applicability_review_owner"},
                next_step="select_or_review_requirement_packs",
                selected_pack_refs=[],
                rejected_pack_refs=governed_refs,
                transport_provenance=transport_provenance,
            )
    else:
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
    human_return = human_returns[0] if human_returns else None

    if governed_refs is not None:
        selected = [governed_refs[index] for index in applicable_indexes]
        rejected = [ref for index, ref in enumerate(governed_refs) if index not in applicable_indexes]
        return _governed_result(
            request,
            decision=combined,
            stage="evaluation",
            reason_codes=[code for item in decisions for code in item["reason_codes"]],
            applicability=resolutions,
            pack_decisions=decisions,
            governance=governance_results,
            human_return=human_return,
            next_step="continue_action" if combined == "allow" else "return_to_human",
            selected_pack_refs=selected,
            rejected_pack_refs=rejected,
            transport_provenance=transport_provenance,
        )

    return {
        "contract_version": GATE_DECISION_CONTRACT_VERSION,
        "request_id": request.get("request_id"),
        "decision": combined,
        "stage": "evaluation",
        "reason_codes": [code for item in decisions for code in item["reason_codes"]],
        "applicability": resolutions,
        "pack_decisions": decisions,
        "governance": governance_results,
        "human_return": human_return,
        "next_step": "continue_action" if combined == "allow" else "return_to_human",
    }


def evaluate_action(
    request: dict[str, Any],
    packs: Sequence[dict[str, Any]],
    *,
    governance_records: Mapping[str, dict[str, Any]] | None = None,
    today: date | None = None,
    enforce_contract_versions: bool = False,
) -> dict[str, Any]:
    """Legacy/M1-compatible evaluation entry.

    The historical optional M2 gates remain available for migration, but callers
    that require strict governed semantics should use ``evaluate_governed_action``.
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
                governance_results.append({
                    "pack_id": pack_id,
                    "eligible": False,
                    "decision": "human_gate",
                    "reason_codes": ["RPE-PACK-GOV-MISSING-RECORD"],
                    "human_return": {"role": "requirement_pack_governance_owner"},
                })
            else:
                governance_results.append(governance_decision(record, today=today, strict=False))
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

    return _evaluate_core(request, packs, governance_results=governance_results)


def evaluate_governed_action(
    envelope: dict[str, Any],
    *,
    today: date | None = None,
) -> dict[str, Any]:
    """Strict fail-closed governed M2 evaluation entry.

    The JSON envelope structurally binds each Requirement Pack to its governance
    record. Loader-observed transport provenance, when present as non-JSON Python
    metadata, is preserved into the result without changing the request payload.
    """
    if not isinstance(envelope, dict):
        return _governed_result(
            {}, decision="human_gate", stage="admission",
            reason_codes=["RPE-GOVERNED-ADMISSION-INVALID-ENVELOPE"],
            human_return={"role": "contract_compatibility_owner"},
            next_step="repair_governed_evaluation_request",
            selected_pack_refs=[], rejected_pack_refs=[],
        )

    unknown_top_level = sorted(set(envelope) - {"contract_version", "request", "governed_packs"})
    if unknown_top_level:
        request_value = envelope.get("request")
        return _governed_result(
            request_value if isinstance(request_value, dict) else {},
            decision="human_gate", stage="admission",
            reason_codes=["RPE-GOVERNED-ADMISSION-UNKNOWN-TOP-LEVEL-FIELD"],
            human_return={"role": "contract_compatibility_owner"},
            next_step="repair_governed_evaluation_request",
            selected_pack_refs=[], rejected_pack_refs=[],
        )

    transport_provenance, provenance_reasons = _normalize_transport_provenance(
        getattr(envelope, "transport_provenance", None)
    )
    request = envelope.get("request")
    bindings = envelope.get("governed_packs")
    if provenance_reasons:
        return _governed_result(
            request if isinstance(request, dict) else {},
            decision="human_gate", stage="admission",
            reason_codes=provenance_reasons,
            human_return={"role": "contract_compatibility_owner"},
            next_step="repair_transport_provenance",
            selected_pack_refs=[], rejected_pack_refs=[],
        )
    if not isinstance(request, dict) or not isinstance(bindings, list) or not bindings:
        return _governed_result(
            request if isinstance(request, dict) else {},
            decision="human_gate", stage="admission",
            reason_codes=["RPE-GOVERNED-ADMISSION-INVALID-STRUCTURE"],
            human_return={"role": "contract_compatibility_owner"},
            next_step="repair_governed_evaluation_request",
            selected_pack_refs=[], rejected_pack_refs=[],
            transport_provenance=transport_provenance,
        )

    compatibility_reasons = check_contract_version("governed_evaluation_request", envelope.get("contract_version"))
    compatibility_reasons.extend(check_contract_version("action_request", request_contract_version(request)))
    if compatibility_reasons:
        return _governed_result(
            request, decision="human_gate", stage="compatibility",
            reason_codes=compatibility_reasons,
            human_return={"role": "contract_compatibility_owner"},
            next_step="migrate_or_review_governed_contracts",
            selected_pack_refs=[], rejected_pack_refs=[],
            transport_provenance=transport_provenance,
        )

    packs: list[dict[str, Any]] = []
    governance_results: list[dict[str, Any]] = []
    refs: list[dict[str, Any]] = []
    admission_reasons: list[str] = []
    compatibility_reasons = []
    seen_pack_versions: set[tuple[str, str]] = set()

    for index, binding in enumerate(bindings):
        if not isinstance(binding, dict):
            admission_reasons.append("RPE-GOVERNED-ADMISSION-INVALID-BINDING")
            continue
        binding_id = binding.get("binding_id")
        pack = binding.get("pack")
        governance = binding.get("governance")
        if not isinstance(binding_id, str) or not binding_id or not isinstance(pack, dict) or not isinstance(governance, dict):
            admission_reasons.append("RPE-GOVERNED-ADMISSION-INVALID-BINDING")
            continue

        compatibility_reasons.extend(check_contract_version("governed_pack_binding", binding.get("contract_version")))
        compatibility_reasons.extend(check_contract_version("requirement_pack", pack_contract_version(pack)))
        compatibility_reasons.extend(check_contract_version("requirement_pack_governance", governance_contract_version(governance)))

        pack_id = pack.get("pack_id")
        pack_version = pack.get("version")
        if not isinstance(pack_id, str) or not pack_id or not isinstance(pack_version, str) or not pack_version:
            admission_reasons.append("RPE-GOVERNED-ADMISSION-MISSING-PACK-IDENTITY")
            continue
        identity = (pack_id, pack_version)
        if identity in seen_pack_versions:
            admission_reasons.append("RPE-GOVERNED-ADMISSION-DUPLICATE-PACK")
        seen_pack_versions.add(identity)

        if governance.get("pack_id") != pack_id:
            admission_reasons.append("RPE-GOVERNED-BINDING-PACK-ID-MISMATCH")
        if governance.get("pack_version") != pack_version:
            admission_reasons.append("RPE-GOVERNED-BINDING-PACK-VERSION-MISMATCH")

        source_metadata = pack.get("source_metadata")
        if not isinstance(source_metadata, dict):
            admission_reasons.append("RPE-GOVERNED-ADMISSION-MISSING-SOURCE-METADATA")
        else:
            comparisons = (
                (source_metadata.get("authority_name"), governance.get("source_authority"), "RPE-GOVERNED-BINDING-SOURCE-AUTHORITY-MISMATCH"),
                (source_metadata.get("source_version"), governance.get("source_version"), "RPE-GOVERNED-BINDING-SOURCE-VERSION-MISMATCH"),
                (source_metadata.get("jurisdiction"), governance.get("jurisdiction"), "RPE-GOVERNED-BINDING-JURISDICTION-MISMATCH"),
            )
            for left, right, code in comparisons:
                if left != right:
                    admission_reasons.append(code)

        packs.append(pack)
        refs.append(_pack_ref(binding_id, pack, governance))
        governance_results.append(governance_decision(governance, today=today, strict=True))

    if compatibility_reasons:
        return _governed_result(
            request, decision="human_gate", stage="compatibility",
            reason_codes=compatibility_reasons,
            human_return={"role": "contract_compatibility_owner"},
            next_step="migrate_or_review_governed_contracts",
            selected_pack_refs=[], rejected_pack_refs=refs,
            governance=governance_results,
            transport_provenance=transport_provenance,
        )

    if admission_reasons or len(packs) != len(bindings):
        return _governed_result(
            request, decision="human_gate", stage="admission",
            reason_codes=admission_reasons or ["RPE-GOVERNED-ADMISSION-INVALID-BINDING"],
            human_return={"role": "requirement_pack_governance_owner"},
            next_step="repair_governed_pack_binding",
            selected_pack_refs=[], rejected_pack_refs=refs,
            governance=governance_results,
            transport_provenance=transport_provenance,
        )

    governance_failures = [item for item in governance_results if not item["eligible"]]
    if governance_failures:
        return _governed_result(
            request, decision="human_gate", stage="governance",
            reason_codes=[code for item in governance_failures for code in item["reason_codes"]],
            human_return=governance_failures[0].get("human_return") or {"role": "requirement_pack_governance_owner"},
            next_step="review_requirement_pack_governance",
            selected_pack_refs=[], rejected_pack_refs=refs,
            governance=governance_results,
            transport_provenance=transport_provenance,
        )

    return _evaluate_core(
        request,
        packs,
        governance_results=governance_results,
        governed_refs=refs,
        transport_provenance=transport_provenance,
    )
