#!/usr/bin/env python3
"""Exercise the repository-map generator against a temporary synthetic tree."""

from __future__ import annotations

import importlib.util
import tempfile
from pathlib import Path

GENERATOR_PATH = Path(__file__).with_name("generate_repository_map.py")


def load_generator_module():
    spec = importlib.util.spec_from_file_location("generate_repository_map", GENERATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load repository-map generator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    generator = load_generator_module()

    with tempfile.TemporaryDirectory() as temporary_directory:
        root = Path(temporary_directory)
        (root / "README.md").write_text("# Demo\n", encoding="utf-8")
        (root / "docs").mkdir()
        (root / "docs" / "guide.md").write_text("# Guide\n", encoding="utf-8")
        (root / ".git").mkdir()
        (root / ".git" / "ignored").write_text("ignore\n", encoding="utf-8")

        output = root / "docs" / "ai-readable" / "repository-map.generated.md"
        output.parent.mkdir(parents=True)
        rendered = generator.render_map(
            root,
            output,
            "https://github.com/example/project",
            "main",
        )

        required_fragments = [
            "Listed files: `2`",
            "README.md",
            "docs/guide.md",
            "https://github.com/example/project/blob/main/README.md",
            "Listed does not mean fetched, read, validated, approved, complete, or production-ready.",
        ]
        missing = [fragment for fragment in required_fragments if fragment not in rendered]
        if missing:
            raise AssertionError("missing expected output fragments: " + ", ".join(missing))
        if ".git/ignored" in rendered:
            raise AssertionError("excluded .git content appeared in generated output")
        if "repository-map.generated.md" in rendered:
            raise AssertionError("output file listed itself")

    print("repository map generator check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
