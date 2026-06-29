# Responsibility Pathway Engineering

Author: Akihisa Ono (小野昭久)

Affiliation for this repository: Independent

Responsibility Pathway Engineering is a design framework for preserving where judgment, authority, evidence, stop authority, human return, and repair remain reachable when humans and AI systems act together.

It is not a blame assignment mechanism.

## Why this matters

AI systems do not only produce outputs. They participate in decisions, recommendations, classifications, tool use, evidence production, and sometimes action preparation.

When that happens, the important question is not only whether the output was correct. The important question is whether the path of responsibility remained visible and returnable:

- where judgment arose
- who or what participated
- where approval was required
- where the action could stop
- where the case returned to humans
- what evidence remained
- who could repair or reconnect the path

Responsibility Pathway Engineering treats these as design objects.

## Current status

Early public specification.

This repository is intentionally specification-first. It prioritizes definitions, examples, lifecycle boundaries, checker boundaries, provenance, and excluded claims before larger implementation layers.

## Try this first

To quickly inspect the practical shape of the project, start with the first copyable template:

- [templates/ai-assisted-work-responsibility-path.yaml](templates/ai-assisted-work-responsibility-path.yaml) - under-construction template for recording AI-assisted work responsibility paths
- [templates/README.md](templates/README.md) - template directory guide and non-claim boundary

Use the template when AI assistance was involved and you need to preserve source references, human or institutional review, evidence, uncertainty, responsibility return points, and repair or reopening paths.

The template is a lightweight starting point. It is not certification, conformance evidence, production approval, legal review, safety review, compliance review, fairness review, social acceptance proof, or AI final-responsibility transfer.

## Provenance

According to the author's development record, Akihisa Ono began thinking about and using the concept of **責任経路 / Responsibility Pathway** from the public note article published on 2026-01-18:

- [AI事故は「責任設計」だけでは防げない――最後の砦は「責任経路設計」である](https://note.com/dantarg/n/nb7f28afa6882)

A fuller provenance record is available at [docs/provenance.md](docs/provenance.md).

This provenance statement is for attribution and traceability. It is not a legal claim, ownership adjudication, plagiarism accusation, certification, or production approval.

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
- [docs/external-review-package-note.md](docs/external-review-package-note.md) - compact external-review reader package
- [docs/external-review-readiness-checklist.md](docs/external-review-readiness-checklist.md) - non-certifying review-readiness checklist
- [docs/progress-map.md](docs/progress-map.md) - rough planning-only progress and gate map
- [docs/zenn-publication-readiness-plan.md](docs/zenn-publication-readiness-plan.md) - non-certifying public-publication readiness gates
- [docs/api-future-shape.md](docs/api-future-shape.md) - future API design preview, not implementation
- [docs/external-product-connection-survey.md](docs/external-product-connection-survey.md) - external connection-surface survey note
- [docs/connector-target-matrix.md](docs/connector-target-matrix.md) - future connector target matrix, synthetic-first and non-implementation
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
