#!/usr/bin/env python3
"""Bounded repository security hygiene checker.

This checker inspects a small set of repository-maintenance security signals.
It is not a security audit, vulnerability scanner, certification process,
production-readiness assessment, compliance review, or proof of repository safety.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DIR = ROOT / ".github" / "workflows"

REQUIRED_FILES = [
    ROOT / "SECURITY.md",
    ROOT / ".github" / "CODEOWNERS",
    ROOT / ".github" / "dependabot.yml",
]

EXPECTED_BOUNDARY_TEXT = [
    "not certification",
    "AI final-responsibility transfer",
]

DANGEROUS_WORKFLOW_PATTERNS = [
    "pull_request_target",
    "secrets.",
    "curl | bash",
    "wget | bash",
    "curl | sh",
    "wget | sh",
]

# This workflow currently installs Elan through a reviewed Lean bootstrap command.
# Keep it explicit so the checker records the exception instead of silently allowing
# arbitrary pipe-to-shell usage elsewhere.
ALLOWED_PIPE_TO_SHELL_LINES = {
    "curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh -s -- -y --no-modify-path",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def warn(message: str) -> None:
    print(f"WARN: {message}")


def check_required_files() -> None:
    for path in REQUIRED_FILES:
        if not path.exists():
            fail(f"required repository security file is missing: {path.relative_to(ROOT)}")


def check_security_policy_boundaries() -> None:
    text = read(ROOT / "SECURITY.md")
    lower_text = text.lower()
    if "reporting" not in lower_text:
        fail("SECURITY.md must include a reporting section")
    if "scope" not in lower_text:
        fail("SECURITY.md must include a scope section")
    for phrase in EXPECTED_BOUNDARY_TEXT:
        if phrase.lower() not in lower_text:
            fail(f"SECURITY.md must preserve boundary phrase: {phrase}")


def check_codeowners_sensitive_paths() -> None:
    text = read(ROOT / ".github" / "CODEOWNERS")
    required_paths = [
        ".github/",
        ".github/workflows/",
        ".github/dependabot.yml",
        "SECURITY.md",
        "scripts/",
        "spec/",
        "examples/",
        "formal/",
        "README.md",
        "BEACON.md",
        "ROADMAP.md",
    ]
    for entry in required_paths:
        if entry not in text:
            fail(f"CODEOWNERS must include sensitive path: {entry}")


def check_dependabot_config() -> None:
    text = read(ROOT / ".github" / "dependabot.yml")
    if "package-ecosystem: \"github-actions\"" not in text:
        fail("dependabot.yml must include GitHub Actions updates")
    if "package-ecosystem: \"pip\"" not in text:
        fail("dependabot.yml must include pip updates")
    if "interval: \"weekly\"" not in text:
        fail("dependabot.yml should include an explicit weekly schedule")


def workflow_files() -> list[Path]:
    if not WORKFLOW_DIR.exists():
        fail(".github/workflows directory is missing")
    files = sorted(WORKFLOW_DIR.glob("*.yml")) + sorted(WORKFLOW_DIR.glob("*.yaml"))
    if not files:
        fail("no GitHub Actions workflow files found")
    return files


def check_workflow_permissions(path: Path, text: str) -> None:
    # Bounded text-level check: top-level read-only token permission should be explicit.
    if not re.search(r"(?m)^permissions:\n(?:  .+\n)*  contents: read\s*$", text):
        fail(f"workflow must declare top-level permissions.contents read: {path.relative_to(ROOT)}")


def check_workflow_risky_patterns(path: Path, text: str) -> None:
    for pattern in DANGEROUS_WORKFLOW_PATTERNS:
        if pattern not in text:
            continue
        if pattern in {"curl | sh", "curl | bash", "wget | sh", "wget | bash"}:
            offending = [line.strip() for line in text.splitlines() if pattern in line]
            unapproved = [line for line in offending if line not in ALLOWED_PIPE_TO_SHELL_LINES]
            if unapproved:
                fail(f"workflow contains unapproved pipe-to-shell command in {path.relative_to(ROOT)}: {unapproved[0]}")
            warn(f"workflow contains approved Lean bootstrap pipe-to-shell exception: {path.relative_to(ROOT)}")
            continue
        fail(f"workflow contains risky pattern '{pattern}': {path.relative_to(ROOT)}")


def check_workflow_action_pinning(path: Path, text: str) -> None:
    # Bounded warning only. Full SHA pinning is desirable but not yet required here.
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("uses:"):
            continue
        if "@" not in stripped:
            fail(f"workflow action reference lacks version/ref: {path.relative_to(ROOT)}: {stripped}")
        ref = stripped.split("@", 1)[1]
        if not re.fullmatch(r"[0-9a-f]{40}", ref):
            warn(f"workflow action is not pinned to a full commit SHA: {path.relative_to(ROOT)}: {stripped}")


def check_workflows() -> None:
    for path in workflow_files():
        text = read(path)
        check_workflow_permissions(path, text)
        check_workflow_risky_patterns(path, text)
        check_workflow_action_pinning(path, text)


def main() -> int:
    check_required_files()
    check_security_policy_boundaries()
    check_codeowners_sensitive_paths()
    check_dependabot_config()
    check_workflows()
    print("PASS: bounded repository security hygiene checks completed without failures")
    return 0


if __name__ == "__main__":
    sys.exit(main())
