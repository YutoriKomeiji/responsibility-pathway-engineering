# Repository Map Generator Design

## Purpose

This design introduces a small, dependency-free generator for an AI-readable repository inventory.

The generated map is intended to help AI/search readers discover exact repository file URLs without pretending that directory names or links prove file contents.

## Output

Default output path:

```text
docs/ai-readable/repository-map.generated.md
```

The generated document contains:

- repository and ref metadata
- total listed-file count
- files grouped by top-level repository area
- an exact GitHub browser URL for every listed file
- a reading rule requiring the exact URL to be fetched before summarization

## Usage

```bash
python scripts/generate_repository_map.py
```

To generate into a temporary location:

```bash
python scripts/generate_repository_map.py --output /tmp/repository-map.generated.md
```

To use another repository or ref:

```bash
python scripts/generate_repository_map.py \
  --repository-url https://github.com/example/project \
  --ref review-branch
```

## Boundary

The map is navigation metadata only.

A listed path does not establish that:

- the file was fetched or read
- its content was interpreted correctly
- the inventory is complete for another ref, fork, submodule, artifact, release, issue, pull request, Pages deployment, or external source
- the file is current, validated, approved, safe, compliant, fair, legally sufficient, or production-ready
- the repository or any component is certified

## Workflow direction

The first workflow is manual and artifact-only:

1. check out the requested ref
2. run the generator
3. upload the generated Markdown as a workflow artifact

It does not push commits, rewrite `READMEforAI.md`, publish Pages, merge a branch, or approve repository content.

A later maintainer-approved step may decide whether to track the generated file, add drift checking, or insert a bounded generated section into `READMEforAI.md`.
