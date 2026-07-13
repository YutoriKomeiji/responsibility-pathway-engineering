#!/usr/bin/env python3
"""One-command RPE demo.

This demo prints a tiny responsibility-path review surface for AI-assisted work.
It is intentionally dependency-free and non-certifying.
"""

from __future__ import annotations


def main() -> int:
    checks = [
        ("decision owner", "human_reviewer"),
        ("AI final responsibility", "blocked"),
        ("approval gate", "human"),
        ("stop authority", "human"),
        ("evidence log", "present"),
        ("return point", "present"),
        ("repair owner", "human_reviewer"),
    ]

    print("RPE 15-second demo: AI-assisted work path")
    print()
    print("Human request -> AI assists -> evidence is recorded -> human approval remains reachable")
    print()

    for label, value in checks:
        print(f"[ok] {label}: {value}")

    print()
    print("Result: responsibility path is visible, reviewable, stoppable, and returnable.")
    print("Boundary: this demo is a review aid only; it is not certification, safety review,")
    print("legal review, compliance review, fairness review, production approval, or")
    print("AI final-responsibility transfer.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
