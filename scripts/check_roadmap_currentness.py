#!/usr/bin/env python3
"""Bounded milestone/stage currentness check on the experimental M3 branch."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def main() -> int:
    road = read("ROADMAP.md")
    kernel = read("docs/external-kernel-roadmap.md")
    m2 = read("docs/m2-governed-integration-current.md")
    m3 = read("docs/m3-classification-and-first-slice.md")
    beacon = read("BEACON.md")
    assert "bounded M2 governed-integration closure" in road
    assert "bounded M2 governed-integration closure complete" in m2
    assert "M3 — Adaptive Responsibility Gateway" in road
    assert "PR #127" in road and "PR #127" in kernel
    assert "unmerged Draft PR #127" in beacon
    assert "M4 or later milestone" in road
    assert "M3 Draft PR #127" in m3
    for n in range(11):
        assert f"K{n}" in kernel, f"missing technical stage K{n}"
    stale = (
        "RPE is in **M2 implementation**",
        "Full M2 closure not yet claimed",
        "**M1 Governed Reference Kernel** checkpoint",
        "Status: **implementation in progress",
    )
    for name, content in (
        ("ROADMAP.md", road),
        ("docs/external-kernel-roadmap.md", kernel),
        ("docs/m2-governed-integration-current.md", m2),
        ("BEACON.md", beacon),
    ):
        for phrase in stale:
            assert phrase not in content, (name, phrase)
    print("PASS: M2 closure / M3 Draft / K0-K10 roadmap currentness")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
