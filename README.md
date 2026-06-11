# Responsibility Pathway Engineering

Author: Akihisa Ono (小野昭久)

Affiliation for this repository: Independent

Responsibility Pathway Engineering is a design framework for preserving the pathways through which responsibility, meaning, authority, value, cost, and repair can return across humans, AI agents, organizations, and systems.

It is not a blame assignment mechanism.

## Status

Early public specification.

## Authorship and citation

This repository is authored and maintained by Akihisa Ono (小野昭久) as an independent public specification and design framework.

For authorship, attribution, affiliation clarification, and citation metadata, see:

- [AUTHORSHIP.md](AUTHORSHIP.md)
- [AUTHORS.md](AUTHORS.md)
- [CITATION.cff](CITATION.cff)
- [NOTICE.md](NOTICE.md)

## Start here

For first-time readers, future maintainers, or AI-assisted continuation, read in this order:

1. [BEACON.md](BEACON.md) - current position and reconnection point
2. [LUMINALIA.md](LUMINALIA.md) - design philosophy
3. [ROADMAP.md](ROADMAP.md) - current and future phases
4. [docs/phase-1-6-plan.md](docs/phase-1-6-plan.md) - next lightweight validation phase plan
5. [CHANGELOG.md](CHANGELOG.md) - conceptual milestones
6. [docs/definition.md](docs/definition.md) - core definition
7. [docs/eight-elements.md](docs/eight-elements.md) - eight-element model
8. [docs/repository-governance.md](docs/repository-governance.md) - repository governance
9. [docs/development-process.md](docs/development-process.md) - development process
10. [docs/schema-cross-reference.md](docs/schema-cross-reference.md) - cross-reference for schema files
11. [docs/validation-checklist.md](docs/validation-checklist.md) - bounded validation checklist
12. [docs/validator-boundary.md](docs/validator-boundary.md) - boundary for lightweight validation tools
13. [docs/example-index.md](docs/example-index.md) - index and reading guide for examples
14. [docs/example-review-notes.md](docs/example-review-notes.md) - initial bounded review notes for examples

## Examples

Minimal examples are available under `examples/`.

- [examples/minimal-pathway.yaml](examples/minimal-pathway.yaml) - a minimal pathway where an AI support node returns responsibility to a human decision owner
- [examples/repair-flow.yaml](examples/repair-flow.yaml) - a minimal repair flow after ambiguity or incomplete evidence is detected
- [examples/suspended-pathway.yaml](examples/suspended-pathway.yaml) - a minimal suspended lifecycle-state example
- [examples/returning-pathway.yaml](examples/returning-pathway.yaml) - a minimal returning lifecycle-state example
- [examples/closed-pathway.yaml](examples/closed-pathway.yaml) - a minimal closed lifecycle-state example

See [docs/example-index.md](docs/example-index.md) for example purposes, boundaries, and future example candidates.

These examples are illustrative only. They do not claim legal liability resolution, moral accountability, safety, fairness, compliance, or production readiness.

## Lightweight checks

A bounded structural checker is available at [scripts/check_examples.py](scripts/check_examples.py).

Install the minimal Python dependency and run:

```bash
python -m pip install -r requirements.txt
python scripts/check_examples.py
```

The same bounded structural check also runs in GitHub Actions via [.github/workflows/check-examples.yml](.github/workflows/check-examples.yml) when examples, the checker, requirements, or the workflow change.

It checks only limited structural signals and explicit responsibility-boundary fields. A passing result does not mean certified, safe, compliant, fair, legally valid, morally resolved, or production ready.

See [docs/validator-boundary.md](docs/validator-boundary.md) for the checker boundary.

## Initial scope

- Definitions
- Eight-element model
- Runtime responsibility pathways
- Return point model
- Formalization candidates (Lean)
- Reference specifications
- Examples

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
