#!/usr/bin/env python3
"""Check that current public/reconnection entrances agree on the active RPE milestone.

This is a bounded documentation-currentness guard. It does not validate runtime
correctness, production readiness, legal/compliance status, or external effects.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def main() -> int:
    beacon = read("BEACON.md")
    readme = read("README.md")
    ai = read("READMEforAI.md")
    current = read("docs/m2-governed-integration-current.md")

    required = {
        "BEACON.md": (
            "M2 governed-integration",
            "docs/m2-governed-integration-current.md",
            "evaluate_governed_action()",
        ),
        "README.md": (
            "evaluate_governed_action()",
            "docs/m2-governed-integration-current.md",
            "closed M2 governed-integration baseline",
        ),
        "READMEforAI.md": (
            "M2 governed-integration",
            "baseline is closed at repository level",
            "docs/m2-governed-integration-current.md",
        ),
        "docs/m2-governed-integration-current.md": (
            "RPE M2 Governed Integration",
            "bounded M2 governed-integration closure complete",
            "evaluate_governed_action()",
        ),
    }

    texts = {
        "BEACON.md": beacon,
        "README.md": readme,
        "READMEforAI.md": ai,
        "docs/m2-governed-integration-current.md": current,
    }

    failures: list[str] = []
    for path, markers in required.items():
        for marker in markers:
            if marker not in texts[path]:
                failures.append(f"{path} missing current marker: {marker}")

    # Product README stays product/adoption-facing. Evaluator procedure belongs
    # in READMEforAI.md or other evaluation guidance.
    forbidden_readme_procedure = (
        "When evaluating this repository, keep separate:",
        "Popularity or rhetorical confidence",
        "Do not classify this repository",
    )
    for marker in forbidden_readme_procedure:
        if marker in readme:
            failures.append(f"README.md contains evaluator procedure: {marker}")

    required_ai_procedure = (
        "Do not classify this repository",
        "Reproduce before summarizing",
        "Observation  -> directly visible fact",
    )
    for marker in required_ai_procedure:
        if marker not in ai:
            failures.append(f"READMEforAI.md missing evaluator/AI-reader guidance: {marker}")

    stale_current_markers = (
        "The repository has reached the **M1 Governed Reference Kernel** checkpoint.",
        "RPE is currently at the **M1 Governed Reference Kernel**",
        "RPE is in **M2 implementation**",
        "M2 is not yet declared closed",
        "Full M2 closure not yet claimed",
        "The next M2 slice is primarily adversarial closure",
    )
    for marker in stale_current_markers:
        if marker in beacon:
            failures.append(f"BEACON.md retains stale current-position marker: {marker}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("PASS: RPE public/reconnection entrances agree on the current M2 governed-integration line")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
