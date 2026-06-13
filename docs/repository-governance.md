# Repository Governance

This repository is itself operated as a Responsibility Pathway.

Its governance rules are designed to preserve return paths from claims to definitions, from definitions to specifications, from specifications to formalization, and from formalization back to stated assumptions.

For the current operational procedure used to apply these governance rules across growing documentation, examples, schemas, checkers, snapshots, and logs, see `docs/repository-operation-model.md`.

For the development work cycle, see `docs/development-process.md`.

## Core Rules

1. No silent knowledge.
2. Do not commit a claim before committing its definition.
3. One commit should express one coherent understanding.
4. Failures that are understood should become design knowledge.
5. AI assistance must remain visible as assistance, not authorship.
6. Formalization must state its scope before any claim is made from it.
7. Repository-wide synchronization should remain staged, small, fetch-confirmed, and non-certifying.

## Documentation Flow

New work should move through the following stages when applicable:

1. Observation
2. Discussion
3. Temporary practice
4. Operational validation
5. Repository rule
6. Specification
7. Formalization
8. Paper or public claim

When work spans multiple documents, use the staged update operation described in `docs/repository-operation-model.md`.

This includes using snapshots, sync logs, and roadmap notes when direct long-file updates would be risky or unclear.

## Responsibility Boundary

The human maintainer remains responsible for repository direction, definitions, claims, citations, publication, and licensing.

AI tools may assist with drafting, structuring, refactoring, checking, and implementation, but they are not responsible maintainers or authors.

Checker success, workflow success, generated drafts, adapter outputs, or Lean builds do not transfer final responsibility to AI tools.

## Review Principle

A change should be reviewable by asking:

- What definition does this depend on?
- What claim does this enable?
- What scope does this exclude?
- What return path allows future readers to understand why this exists?
- What snapshot, sync log, roadmap note, checker result, or operation-model rule should future maintainers consult before continuing?

## Non-certifying governance boundary

Repository governance preserves authorship clarity, traceability, maintainability, and returnability.

It does not certify legal validity, safety, compliance, fairness, moral resolution, institutional approval, production readiness, connector correctness, adapter correctness, Lean theorem completeness, or AI final-responsibility transfer.
