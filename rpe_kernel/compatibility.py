"""Bounded runtime contract-version compatibility checks."""

from __future__ import annotations

from typing import Any

SUPPORTED_CONTRACT_VERSIONS = {
    "action_request": "1.0.0",
    "gate_decision": "1.0.0",
    "requirement_pack": "1.0.0",
    "requirement_pack_governance": "1.0.0",
}


def _major(version: str) -> str:
    return version.split(".", 1)[0]


def check_contract_version(contract: str, supplied_version: Any) -> list[str]:
    """Return reason codes when a runtime contract version is unsupported."""
    supported = SUPPORTED_CONTRACT_VERSIONS.get(contract)
    if supported is None:
        return ["RPE-CONTRACT-UNKNOWN-FAMILY"]
    if not isinstance(supplied_version, str) or not supplied_version.strip():
        return [f"RPE-CONTRACT-MISSING-{contract.replace('_', '-').upper()}-VERSION"]
    if _major(supplied_version) != _major(supported):
        return [f"RPE-CONTRACT-UNSUPPORTED-{contract.replace('_', '-').upper()}-MAJOR"]
    return []


def request_contract_version(request: dict[str, Any]) -> str | None:
    """Read the action-request contract version from the runtime envelope."""
    value = request.get("contract_version")
    return value if isinstance(value, str) else None


def pack_contract_version(pack: dict[str, Any]) -> str | None:
    """Read the requirement-pack contract version from the runtime envelope."""
    value = pack.get("contract_version")
    return value if isinstance(value, str) else None
