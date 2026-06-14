# Responsibility Pathway Engineering

Author: Akihisa Ono (小野昭久)

Affiliation for this repository: Independent

Responsibility Pathway Engineering is a design framework for preserving the pathways through which responsibility, meaning, authority, value, cost, and repair can return across humans, AI agents, organizations, and systems.

It is not a blame assignment mechanism.

## Current status

Early public specification.

This repository is intentionally specification-first. It prioritizes definitions, examples, lifecycle boundaries, checker boundaries, provenance, and excluded claims before larger implementation layers.

## What this repository is not

This repository does not claim to provide:

- legal responsibility determination
- safety certification
- compliance certification
- fairness certification
- moral accountability resolution
- institutional approval
- production readiness
- an agent runtime
- a replacement for RACI, HITL, Guardrails, ISO/IEC 42001, or human oversight frameworks
- a transfer of final responsibility to AI

All schemas, examples, checkers, and Lean files in this repository remain structural, assumption-bound, and non-certifying.

## Start here

For first-time readers, future maintainers, or AI-assisted continuation, read in this order:

1. [BEACON.md](BEACON.md) - current position and reconnection point
2. [docs/operation-index.md](docs/operation-index.md) - operation and maintenance navigation
3. [docs/overview.md](docs/overview.md) - current repository overview
4. [docs/concepts/index.md](docs/concepts/index.md) - concept-level reader path
5. [docs/example-index.md](docs/example-index.md) - examples and boundaries
6. [docs/checker-coverage.md](docs/checker-coverage.md) - current checker boundary and coverage
7. [LUMINALIA.md](LUMINALIA.md) - public Luminalia design philosophy boundary
8. [ROADMAP.md](ROADMAP.md) - current and future phases
9. [CHANGELOG.md](CHANGELOG.md) - conceptual milestones

The previous expanded root README content has been moved to [docs/readme-expanded.md](docs/readme-expanded.md) to keep the root README mobile-renderer friendly.

## Key documents

- [docs/provenance.md](docs/provenance.md) - provenance and public source lineage
- [AUTHORSHIP.md](AUTHORSHIP.md) - authorship and responsibility boundary
- [NOTICE.md](NOTICE.md) - notice, attribution, and AI-assistance boundary
- [CITATION.cff](CITATION.cff) - citation metadata
- [docs/deferred-work-restart-conditions.md](docs/deferred-work-restart-conditions.md) - restart conditions for deferred work
- [docs/current-task-inventory.md](docs/current-task-inventory.md) - current task inventory
- [formal/lean/README.md](formal/lean/README.md) - Lean formalization boundary

## Examples

Minimal examples are available under `examples/`.

See [docs/example-index.md](docs/example-index.md) for purposes, boundaries, and reading order.

These examples are illustrative only. They do not claim legal liability resolution, moral accountability, safety, fairness, compliance, or production readiness.

## Lightweight checks

A bounded structural checker is available at [scripts/check_examples.py](scripts/check_examples.py).

```bash
python -m pip install -r requirements.txt
python scripts/check_examples.py
```

A separate bounded review-result checker is available at [scripts/check_review_results.py](scripts/check_review_results.py).

```bash
python scripts/check_review_results.py
```

A passing checker or workflow result does not mean certified, safe, compliant, fair, legally valid, morally resolved, institutionally approved, production ready, or AI-final-responsibility transferred.

## Repository principle

This repository is itself operated as a Responsibility Pathway.

Readers should be able to return from claims to definitions, from definitions to specifications, from specifications to formalization, and from formalization back to assumptions.

## Boundary

The human author remains responsible for all definitions and claims. AI tools assist drafting and implementation but do not assume responsibility.

## License and notice

This repository is released under the [MIT License](LICENSE).

Copyright (c) 2026 Akihisa Ono (小野昭久).

Reuse, modification, distribution, and sublicensing are permitted under the license terms, provided that the copyright notice and license notice are preserved.

See [NOTICE.md](NOTICE.md) for authorship, attribution, AI-assistance, and responsibility-boundary notes.
