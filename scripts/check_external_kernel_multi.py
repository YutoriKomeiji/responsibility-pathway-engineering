#!/usr/bin/env python3
"""Check the multi-pack evaluator against the committed synthetic fixtures."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    with tempfile.TemporaryDirectory() as temporary_directory:
        output = Path(temporary_directory) / "decision.json"
        command = [
            sys.executable,
            str(ROOT / "scripts" / "run_external_kernel_multi.py"),
            str(ROOT / "examples" / "external-kernel" / "minimal-action-request.json"),
            str(ROOT / "examples" / "external-kernel" / "minimal-requirement-pack.json"),
            str(ROOT / "examples" / "external-kernel" / "minimal-data-handling-pack.json"),
            "--output",
            str(output),
        ]
        subprocess.run(command, check=True)
        actual = load(output)
        expected = load(ROOT / "examples" / "external-kernel" / "expected-multi-pack-decision.json")
        if actual != expected:
            raise AssertionError("multi-pack evaluator output did not match expected fixture")
    print("external kernel multi-pack check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
