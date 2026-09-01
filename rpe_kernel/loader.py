"""Bounded local/caller-content loading for governed RPE envelopes.

This module intentionally does not fetch URLs, discover registries, install
packages, or infer source authority. Loading bytes is not trust establishment.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

MAX_GOVERNED_ENVELOPE_BYTES = 1_048_576


class LoaderError(ValueError):
    """Stable bounded loader failure."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code


def _looks_remote(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme.lower() in {"http", "https", "ftp", "ftps", "s3", "gs"}


def _decode_json_object(text: str) -> dict[str, Any]:
    try:
        value = json.loads(text)
    except json.JSONDecodeError as error:
        raise LoaderError("RPE-LOADER-INVALID-JSON", "governed envelope content must be valid JSON") from error
    if not isinstance(value, dict):
        raise LoaderError("RPE-LOADER-TOP-LEVEL-NOT-OBJECT", "governed envelope top level must be a JSON object")
    return value


def _attach_transport_provenance(value: dict[str, Any], raw: bytes, *, source_kind: str) -> dict[str, Any]:
    """Attach a bounded observation of the exact input bytes.

    The digest is transport provenance only. It does not establish who authored
    the content, whether the source is authoritative, or whether the semantics
    are correct. Existing caller-declared transport provenance is overwritten
    when these loader functions directly observe the bytes.
    """
    loaded = dict(value)
    loaded["transport_provenance"] = {
        "source_kind": source_kind,
        "content_sha256": hashlib.sha256(raw).hexdigest(),
        "byte_length": len(raw),
        "observation_scope": "transport_bytes_only",
    }
    return loaded


def _load_raw(raw: bytes, *, source_kind: str, max_bytes: int) -> dict[str, Any]:
    if max_bytes <= 0:
        raise LoaderError("RPE-LOADER-INVALID-SIZE-LIMIT", "max_bytes must be positive")
    if len(raw) > max_bytes:
        raise LoaderError("RPE-LOADER-CONTENT-TOO-LARGE", "governed envelope content exceeds the configured size limit")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise LoaderError("RPE-LOADER-NON-UTF8-CONTENT", "governed envelope content must be UTF-8") from error
    return _attach_transport_provenance(_decode_json_object(text), raw, source_kind=source_kind)


def load_governed_envelope_content(content: str | bytes, *, max_bytes: int = MAX_GOVERNED_ENVELOPE_BYTES) -> dict[str, Any]:
    """Load one governed envelope from caller-provided JSON content.

    The returned envelope records SHA-256 and byte length for the exact supplied
    UTF-8 bytes. This is a transport observation, not a trust assertion.
    """
    if isinstance(content, str):
        raw = content.encode("utf-8")
    elif isinstance(content, bytes):
        raw = content
    else:
        raise LoaderError("RPE-LOADER-INVALID-CONTENT-TYPE", "content must be str or bytes")
    return _load_raw(raw, source_kind="caller_content", max_bytes=max_bytes)


def load_governed_envelope_file(path: str | Path, *, max_bytes: int = MAX_GOVERNED_ENVELOPE_BYTES) -> dict[str, Any]:
    """Load one governed envelope from an explicitly supplied local JSON file.

    The function performs no network access and treats path existence only as a
    transport fact, not as evidence of source authority or semantic validity.
    It records a digest of the exact file bytes but intentionally does not place
    the local filesystem path into the governed envelope.
    """
    text_path = str(path)
    if _looks_remote(text_path):
        raise LoaderError("RPE-LOADER-REMOTE-SOURCE-UNSUPPORTED", "remote/network sources are not supported")

    candidate = Path(path)
    if not candidate.exists():
        raise LoaderError("RPE-LOADER-FILE-NOT-FOUND", "local governed envelope file was not found")
    if not candidate.is_file():
        raise LoaderError("RPE-LOADER-NOT-A-FILE", "local governed envelope source must be a regular file")
    try:
        size = candidate.stat().st_size
    except OSError as error:
        raise LoaderError("RPE-LOADER-FILE-STAT-FAILED", "unable to inspect local governed envelope file") from error
    if max_bytes <= 0:
        raise LoaderError("RPE-LOADER-INVALID-SIZE-LIMIT", "max_bytes must be positive")
    if size > max_bytes:
        raise LoaderError("RPE-LOADER-CONTENT-TOO-LARGE", "governed envelope file exceeds the configured size limit")
    try:
        raw = candidate.read_bytes()
    except OSError as error:
        raise LoaderError("RPE-LOADER-FILE-READ-FAILED", "unable to read local governed envelope file") from error
    return _load_raw(raw, source_kind="local_file", max_bytes=max_bytes)
