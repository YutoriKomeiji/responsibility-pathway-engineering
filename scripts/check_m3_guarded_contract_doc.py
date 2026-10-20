#!/usr/bin/env python3
"""Detect obvious guarded-adapter documentation drift."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/m3-versioned-guarded-adapter-contract-v0.1.md"


def main() -> int:
    text = DOC.read_text(encoding="utf-8")
    required = [
        'POST /v1/evaluate/transition/guarded',
        'contract version `0.2.0-exp`',
        '`rpe_evaluate_guarded_responsibility_transition`',
        '"authority_reference": "authority-record"',
        '"capability_status": "available"',
        '"response_window_status": "available"',
        '"cumulative_exposure_checks"',
        '"cumulative_exposure_results"',
        'threshold_origin = caller_or_policy_supplied',
        'trajectory_safety_claim = false',
        '/openapi-guarded.json',
    ]
    missing = [item for item in required if item not in text]
    assert not missing, f"guarded contract doc missing current contract markers: {missing}"

    stale = [
        '"authority_ref":',
        '"capability_status": "observed_available"',
        '"response_window_status": "open"',
    ]
    present = [item for item in stale if item in text]
    assert not present, f"guarded contract doc contains stale vocabulary: {present}"

    print("M3 guarded contract documentation drift check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
