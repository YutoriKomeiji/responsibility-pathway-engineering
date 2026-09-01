"""Bounded runtime contract-version compatibility checks."""

from __future__ import annotations

from typing import Any

from .contract_versions import CONTRACTS


def _parse_semver(version: Any) -> tuple[int, int, int] | None:
    if not isinstance(version, str):
        return None
    parts = version.split(".")
    if len(parts) != 3 or not all(part.isdigit() for part in parts):
        return None
    return tuple(int(part) for part in parts)  # type: ignore[return-value]


def check_contract_version(contract: str, supplied_version: Any) -> list[str]:
    """Return stable reason codes when a governed runtime contract is unsupported.

    Current M2 support is intentionally conservative: exact supported versions are
    accepted; older/newer MINOR versions require an explicit future compatibility
    declaration rather than being accepted by major-version coincidence.
    """
    entry = CONTRACTS.get(contract)
    if entry is None:
        return ["RPE-CONTRACT-UNKNOWN-FAMILY"]

    supplied = _parse_semver(supplied_version)
    if supplied is None:
        if not isinstance(supplied_version, str) or not supplied_version.strip():
            return [f"RPE-CONTRACT-MISSING-{contract.replace('_', '-').upper()}-VERSION"]
        return [f"RPE-CONTRACT-INVALID-{contract.replace('_', '-').upper()}-VERSION"]

    supported = _parse_semver(entry["version"])
    assert supported is not None
    if supplied[0] != supported[0]:
        return [f"RPE-CONTRACT-UNSUPPORTED-{contract.replace('_', '-').upper()}-MAJOR"]
    if supplied[1] != supported[1]:
        return [f"RPE-CONTRACT-UNSUPPORTED-{contract.replace('_', '-').upper()}-MINOR"]
    if supplied[2] > supported[2]:
        return [f"RPE-CONTRACT-UNSUPPORTED-{contract.replace('_', '-').upper()}-PATCH"]
    return []


def request_contract_version(request: dict[str, Any]) -> str | None:
    value = request.get("contract_version")
    return value if isinstance(value, str) else None


def pack_contract_version(pack: dict[str, Any]) -> str | None:
    value = pack.get("contract_version")
    return value if isinstance(value, str) else None


def governance_contract_version(record: dict[str, Any]) -> str | None:
    value = record.get("contract_version")
    return value if isinstance(value, str) else None
