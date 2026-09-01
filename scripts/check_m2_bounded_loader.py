#!/usr/bin/env python3
"""Deterministic checks for the bounded M2 governed-envelope loader."""

from __future__ import annotations

import json
import tempfile
from datetime import date
from pathlib import Path

from rpe_kernel import (
    LoaderError,
    evaluate_governed_action,
    load_governed_envelope_content,
    load_governed_envelope_file,
)

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "examples/external-kernel/minimal-governed-evaluation-request.json"


def require_loader_code(fn, code: str) -> None:
    try:
        fn()
    except LoaderError as error:
        assert error.code == code, (error.code, code)
    else:
        raise AssertionError(f"expected LoaderError {code}")


def main() -> int:
    fixture_text = FIXTURE.read_text(encoding="utf-8")

    loaded = load_governed_envelope_content(fixture_text)
    result = evaluate_governed_action(loaded, today=date(2026, 9, 1))
    assert result["decision"] == "allow", result
    assert result["responsibility_handoff"]["authority_effect"] == "none", result
    assert result["responsibility_handoff"]["decision_scope"] == "evaluation_only", result

    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "governed.json"
        path.write_text(fixture_text, encoding="utf-8")
        from_file = load_governed_envelope_file(path)
        assert from_file == loaded

        directory_path = Path(directory) / "not-a-file"
        directory_path.mkdir()
        require_loader_code(
            lambda: load_governed_envelope_file(directory_path),
            "RPE-LOADER-NOT-A-FILE",
        )

        missing = Path(directory) / "missing.json"
        require_loader_code(
            lambda: load_governed_envelope_file(missing),
            "RPE-LOADER-FILE-NOT-FOUND",
        )

    require_loader_code(
        lambda: load_governed_envelope_file("https://example.invalid/pack.json"),
        "RPE-LOADER-REMOTE-SOURCE-UNSUPPORTED",
    )
    require_loader_code(
        lambda: load_governed_envelope_content("not-json"),
        "RPE-LOADER-INVALID-JSON",
    )
    require_loader_code(
        lambda: load_governed_envelope_content(json.dumps([1, 2, 3])),
        "RPE-LOADER-TOP-LEVEL-NOT-OBJECT",
    )
    require_loader_code(
        lambda: load_governed_envelope_content(b"\xff"),
        "RPE-LOADER-NON-UTF8-CONTENT",
    )
    require_loader_code(
        lambda: load_governed_envelope_content(fixture_text, max_bytes=8),
        "RPE-LOADER-CONTENT-TOO-LARGE",
    )
    require_loader_code(
        lambda: load_governed_envelope_content(fixture_text, max_bytes=0),
        "RPE-LOADER-INVALID-SIZE-LIMIT",
    )

    print("M2 bounded loader checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
