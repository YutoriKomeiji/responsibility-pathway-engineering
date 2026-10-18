#!/usr/bin/env python3
"""Repository-wide RPE file-consistency inventory (not a safety or product certification).

Traverse every Git-tracked file. Separate active public/current sources from
historical/context records, review local Markdown links, and enforce a small
set of current-contract invariants. Report findings rather than silently
rewriting historical evidence.
"""
from __future__ import annotations

import ast
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
ACTIVE = {
    "README.md", "README.ja.md", "READMEforAI.md", "BEACON.md",
    "ROADMAP.md", "AGENTS.md", "LUMINALIA.md",
    "docs/external-kernel-roadmap.md",
    "docs/m2-governed-integration-current.md",
    "docs/claim-boundary-promotion.md",
    "docs/repository-principles.md",
    "docs/repository-governance.md",
    "docs/development-process.md",
    "docs/responsibility-routing-contract-v0.1.md",
    "docs/quickstart-review-one-path.md",
}
HISTORY_PREFIXES = (
    "docs/changelog/", "docs/source-alignment/", "docs/phase-",
    "docs/2026-", "docs/roadmap-history",
)
HISTORY_TERMS = (
    "snapshot", "sync-note", "audit-", "research", "review-findings",
    "migration", "historical", "log", "connection",
)
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
POTENTIAL_STALE_RE = re.compile(
    r"(?:M2[^\n]{0,90}(?:in progress|not yet closed|next focus|remaining work|implementation pending))"
    r"|(?:(?:next|remaining) M2 (?:slice|task|work))",
    re.IGNORECASE,
)
STALE = (
    "Status: implementation in progress; governed-integration baseline reached.",
    "Full M2 closure not yet claimed.",
    "Status: next M2 focus.",
    "Merge/read back the M2 documentation synchronization slice.",
)


def tracked() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True
    )
    return sorted(p.decode("utf-8") for p in result.stdout.split(b"\0") if p)


def kind(path: str) -> str:
    if path in ACTIVE:
        return "active-current"
    if path.startswith(HISTORY_PREFIXES) or (
        path.startswith("docs/") and any(token in Path(path).name for token in HISTORY_TERMS)
    ):
        return "history-or-context"
    if path.startswith(("rpe_kernel/", "schemas/", "spec/", "scripts/", "runtime/")):
        return "implementation-contract-test"
    if path.startswith(".github/"):
        return "automation"
    return "supporting"


def link_target(path: str, raw: str) -> str | None:
    target = raw.strip().split(" ", 1)[0].strip("<>").split("#", 1)[0]
    if not target or target.startswith(("/", "http:", "https:", "mailto:", "data:", "//")):
        return None
    target = unquote(target).split("?", 1)[0]
    import posixpath
    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(path), target))
    if resolved.startswith("../") or resolved == "..":
        return None
    return resolved


def main() -> int:
    paths = tracked()
    present = set(paths)
    counts: Counter[str] = Counter()
    found: Counter[str] = Counter()
    problems: list[str] = []
    broken_links: list[str] = []
    historical_stale: list[str] = []
    malformed_negative_json: list[str] = []
    semantic_review_candidates: list[str] = []
    for path in paths:
        counts[kind(path)] += 1
        p = ROOT / path
        try:
            text = p.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            found["non-utf8-or-unreadable"] += 1
            continue
        found["readable"] += 1
        if path.endswith(".py"):
            found["python"] += 1
            try:
                ast.parse(text, filename=path)
            except SyntaxError as exc:
                problems.append(f"INVALID_PYTHON_SYNTAX: {path}:{exc.lineno}: {exc.msg}")
        if path.endswith(".json"):
            found["json"] += 1
            try:
                json.loads(text)
            except json.JSONDecodeError as exc:
                if path.startswith(("schemas/", "spec/", "rpe_kernel/")):
                    problems.append(f"INVALID_CONTRACT_JSON: {path}:{exc.lineno}: {exc.msg}")
                else:
                    malformed_negative_json.append(f"{path}:{exc.lineno}: {exc.msg}")
        if path.startswith(".github/workflows/") and path.endswith((".yaml", ".yml")):
            found["workflow"] += 1
            for reference in re.findall(r"\bpython(?:3)?\s+(scripts/[a-zA-Z0-9_./-]+\.py)\b", text):
                found["workflow-python-ref"] += 1
                if reference not in present:
                    problems.append(f"WORKFLOW_MISSING_SCRIPT: {path} -> {reference}")
        if path.endswith(".md"):
            found["markdown"] += 1
            for n, line in enumerate(text.splitlines(), 1):
                if POTENTIAL_STALE_RE.search(line):
                    semantic_review_candidates.append(f"{path}:{n}: {line.strip()[:160]}")
            for match in LINK_RE.finditer(text):
                dest = link_target(path, match.group(1))
                if dest is None:
                    continue
                found["local-link"] += 1
                candidates = (dest, dest + "/index.md", dest + "/index.html")
                if dest.endswith(".html"):
                    candidates += (dest[:-5] + ".md",)
                if not any(c in present for c in candidates):
                    note = f"{path} -> {dest}"
                    broken_links.append(note)
                    if path in ACTIVE:
                        problems.append("ACTIVE_BROKEN_LINK: " + note)
            for phrase in STALE:
                if phrase in text:
                    if path in ACTIVE:
                        problems.append(f"ACTIVE_STALE_STATUS: {path}: {phrase}")
                    else:
                        historical_stale.append(path)
    def requires(path: str, *markers: str) -> None:
        if path not in present:
            problems.append("MISSING_CURRENT_SOURCE: " + path)
            return
        text = (ROOT / path).read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                problems.append(f"MISSING_CURRENT_MARKER: {path}: {marker}")
    requires("ROADMAP.md", "bounded M2 governed-integration closure", "M3 draft PR #127")
    requires("docs/external-kernel-roadmap.md",
             "bounded M2 governed-integration closure completed", "M3 draft PR #127")
    requires("docs/m2-governed-integration-current.md",
             "bounded M2 governed-integration closure complete")
    requires("docs/claim-boundary-promotion.md", "bounded M2 governed-integration closure at repository level")
    requires("docs/repository-principles.md", "From principle to executable evidence")
    report = {
        "tracked_files": len(paths),
        "categorized": dict(counts),
        "readable_files": found["readable"],
        "markdown_files": found["markdown"],
        "python_files_parsed": found["python"],
        "json_files_checked": found["json"],
        "workflow_files_checked": found["workflow"],
        "workflow_python_references": found["workflow-python-ref"],
        "noncontract_invalid_json": malformed_negative_json[:18],
        "local_markdown_links": found["local-link"],
        "broken_links_all": len(broken_links),
        "broken_link_samples": broken_links[:25],
        "semantic_status_review_candidates": len(semantic_review_candidates),
        "semantic_status_samples": semantic_review_candidates[:65],
        "historical_status_matches": len(set(historical_stale)),
        "historical_status_samples": sorted(set(historical_stale))[:12],
        "current_failures": problems[:40],
        "current_failures_total": len(problems),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
