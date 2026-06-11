# Repository Governance

This repository is itself operated as a Responsibility Pathway.

Its governance rules are designed to preserve return paths from claims to definitions, from definitions to specifications, from specifications to formalization, and from formalization back to stated assumptions.

## Core Rules

1. No silent knowledge.
2. Do not commit a claim before committing its definition.
3. One commit should express one coherent understanding.
4. Failures that are understood should become design knowledge.
5. AI assistance must remain visible as assistance, not authorship.
6. Formalization must state its scope before any claim is made from it.

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

## Responsibility Boundary

The human maintainer remains responsible for repository direction, definitions, claims, citations, publication, and licensing.

AI tools may assist with drafting, structuring, refactoring, checking, and implementation, but they are not responsible maintainers or authors.

## Review Principle

A change should be reviewable by asking:

- What definition does this depend on?
- What claim does this enable?
- What scope does this exclude?
- What return path allows future readers to understand why this exists?
