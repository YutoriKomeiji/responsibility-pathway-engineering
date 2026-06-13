# Responsibility Pathway Engineering

Author: Akihisa Ono (小野昭久)

Affiliation for this repository: Independent

Responsibility Pathway Engineering is a design framework for preserving the pathways through which responsibility, meaning, authority, value, cost, and repair can return across humans, AI agents, organizations, and systems.

It is not a blame assignment mechanism.

## Provenance and first public source

The Japanese term and design concept **責任経路設計** was first publicly introduced by Akihisa Ono in the note article "AI事故は「責任設計」だけでは防げない――最後の砦は「責任経路設計」である", published on 2026-01-18.

First public source:

- https://note.com/dantarg/n/nb7f28afa6882

Major public source articles for the Responsibility Pathway Design / Responsibility Pathway Engineering lineage include:

- "AI事故は「責任設計」だけでは防げない――最後の砦は「責任経路設計」である" — https://note.com/dantarg/n/nb7f28afa6882
- "2026年、AI安全の争点は「ガバナンス」ではない" — https://note.com/dantarg/n/n7e55212b8ac4
- "責任経路設計とは何か" — https://note.com/dantarg/n/na7a65ee28906
- "責任あるAI（Responsible AI）が実装できない本当の理由" — https://note.com/dantarg/n/n77367658521c

These articles are treated as the public source lineage for the concept, terminology, motivation, and early framing of responsibility pathway design before and alongside this repository's specification work.

That article defines responsibility pathway design as designing responsibility not merely as a point of attribution, but as a flow or path that preserves where judgment arises, where it changes, where it can stop, where it returns to humans, and how those pathways remain structurally maintained during operation.

This repository develops that public source into an open specification, examples, schemas, bounded checkers, review notes, and formalization candidates. The repository records provenance to preserve traceability of the term, the concept, and the responsibility path of the project itself.

This provenance note is an attribution and traceability statement. It is not a legal claim, ownership adjudication, plagiarism accusation, certification, or production approval.

## Current orientation

Responsibility Pathway Engineering focuses on responsibility-flow design, not model performance alone.

It asks:

- where judgment arises
- who or what participates in the judgment
- who accepts the judgment as responsibility
- where approval is required
- who executes
- where the action can stop
- where the case returns to humans
- what evidence remains
- who repairs or reconnects the responsibility path

The current repository treats AI as a participant in proposals, classification, tool use, and evidence production, but not as a final responsibility holder under the current minimal assumptions.

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

## Status

Early public specification.

This repository is intentionally small and specification-first. See [docs/minimal-core-rationale.md](docs/minimal-core-rationale.md) for why the current core prioritizes definitions, examples, lifecycle boundaries, checker boundaries, and excluded claims before larger implementation layers.

A source-alignment pass over the currently inventoried Zenn article candidates has been completed. The synthesis is available at [docs/source-alignment/zenn-source-alignment-synthesis.md](docs/source-alignment/zenn-source-alignment-synthesis.md). The detailed inventory is available at [docs/source-alignment/zenn-article-inventory.md](docs/source-alignment/zenn-article-inventory.md).

A developer-facing explanatory note for the try/catch/finally analogy is available at [docs/explanations/try-catch-finally-responsibility-pathway.md](docs/explanations/try-catch-finally-responsibility-pathway.md). It is an explanatory analogy only, not formal semantics.

A repository overview after the source-alignment pass is available at [docs/overview.md](docs/overview.md).

Phase 2 has started. The current Lean formalization contains a minimal node/pathway model and a scoped lifecycle-invariant set in [formal/lean/ResponsibilityPathway/Core.lean](formal/lean/ResponsibilityPathway/Core.lean). These invariants are structural, assumption-bound, and non-certifying.

The Phase 2 Lean spine has now been split into small modules while preserving `Core.lean` as the stable entry point. See [formal/lean/README.md](formal/lean/README.md), [docs/phase-2-current-snapshot.md](docs/phase-2-current-snapshot.md), [docs/phase-2-lean-split-plan.md](docs/phase-2-lean-split-plan.md), and [docs/phase-2-lean-theorem-index.md](docs/phase-2-lean-theorem-index.md).

An initial enterprise adoption guide is available at [docs/enterprise-implementation-profile.md](docs/enterprise-implementation-profile.md). It describes how organizations can connect the minimal formal core to workflow, evidence, checker, and governance layers without treating RPE as a production verifier, compliance engine, safety certification tool, or legal decision system.

A plain-language record review guide is available at [docs/responsibility-pathway-record-review.md](docs/responsibility-pathway-record-review.md). It describes how a Responsibility Pathway record can be reviewed or rechecked after it is created without turning the review into legal, safety, compliance, fairness, moral, or production certification.

The current Phase 2.5 enterprise and record-review snapshot is available at [docs/phase-2-5-current-snapshot.md](docs/phase-2-5-current-snapshot.md).

A bounded review-result schema is available at [spec/review-result.schema.yaml](spec/review-result.schema.yaml). It defines a public structure for recording what a review checked, what it did not check, and what it does not claim.

A bounded review-result checker is available at [scripts/check_review_results.py](scripts/check_review_results.py). It checks review-result fixtures for required fields, allowed review scope/status values, expected not-checked and not-claimed boundaries, and responsibility-boundary flags. It remains structural and non-certifying.

The `Check review-result fixtures` GitHub Actions workflow has been observed green for run `#1` on commit `aaaece3` on `main`. This observed green status means only that the bounded review-result fixture checker passed for that repository state; it is not certification.

Phase 3 has an entry boundary at [docs/reference-implementation-boundary.md](docs/reference-implementation-boundary.md). Read it before adding reference implementations.

The source-aligned Action Class Matrix now has small examples for classification-only Class A-F reading, Class C Approval-Required internal document update, Class D Reversible External Action, and Class F Emergency Stop. These examples remain structural and non-certifying.

Phase 3.1 has started with an adapter boundary and runtime-event bridge. See [docs/adapter-boundary.md](docs/adapter-boundary.md) and [docs/phase-3-1-current-snapshot.md](docs/phase-3-1-current-snapshot.md). The first runtime-event-to-pathway example is [examples/runtime-event-to-pathway-minimal.yaml](examples/runtime-event-to-pathway-minimal.yaml). It remains a synthetic, vendor-neutral, review-required draft example, not a service-specific connector or production runtime.

The repository operation model is available at [docs/repository-operation-model.md](docs/repository-operation-model.md). It documents staged update operation, snapshots, sync logs, roadmap notes, checker observation policy, long-file update policy, and non-certifying operation boundaries.

The operation document index is available at [docs/operation-index.md](docs/operation-index.md). It explains which operation-related document to read for each maintenance situation.

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
2. [docs/repository-operation-model.md](docs/repository-operation-model.md) - repository operation model for staged updates, snapshots, sync logs, and long-file update policy
3. [docs/operation-index.md](docs/operation-index.md) - navigation index for operation-related documents
4. [docs/overview.md](docs/overview.md) - current repository overview after source alignment
5. [docs/source-alignment/zenn-source-alignment-synthesis.md](docs/source-alignment/zenn-source-alignment-synthesis.md) - source-alignment synthesis from reviewed Zenn materials
6. [docs/concepts/core-elements.md](docs/concepts/core-elements.md) - operational roles and controls aligned with the eight-element model
7. [docs/action-class-matrix.md](docs/action-class-matrix.md) - source-aligned Class A-F action classification design aid
8. [examples/action-class-matrix-minimal.yaml](examples/action-class-matrix-minimal.yaml) - classification-only Action Class Matrix fixture
9. [examples/internal-document-update.yaml](examples/internal-document-update.yaml) - Class C Approval-Required internal document update example
10. [examples/emergency-stop-flow.yaml](examples/emergency-stop-flow.yaml) - Class F Emergency Stop / stop-and-await example
11. [examples/reversible-external-action.yaml](examples/reversible-external-action.yaml) - Class D Reversible External Action example
12. [docs/adapter-boundary.md](docs/adapter-boundary.md) - adapter boundary before runtime connectors
13. [docs/phase-3-1-current-snapshot.md](docs/phase-3-1-current-snapshot.md) - current Phase 3.1 adapter and runtime-event snapshot
14. [examples/runtime-event-to-pathway-minimal.yaml](examples/runtime-event-to-pathway-minimal.yaml) - synthetic runtime-event-to-pathway draft example
15. [docs/explanations/try-catch-finally-responsibility-pathway.md](docs/explanations/try-catch-finally-responsibility-pathway.md) - developer-facing analogy, not formal semantics
16. [LUMINALIA.md](LUMINALIA.md) - design philosophy
17. [ROADMAP.md](ROADMAP.md) - current and future phases
18. [CHANGELOG.md](CHANGELOG.md) - conceptual milestones
19. [docs/minimal-core-rationale.md](docs/minimal-core-rationale.md) - why the current repository remains intentionally small
20. [docs/enterprise-implementation-profile.md](docs/enterprise-implementation-profile.md) - minimal enterprise adoption profile and layer separation
21. [docs/responsibility-pathway-record-review.md](docs/responsibility-pathway-record-review.md) - plain-language review process for responsibility pathway records
22. [docs/phase-2-5-current-snapshot.md](docs/phase-2-5-current-snapshot.md) - current Phase 2.5 enterprise and record-review snapshot
23. [docs/reference-implementation-boundary.md](docs/reference-implementation-boundary.md) - boundary before Phase 3 reference implementations
24. [docs/phase-1-6-plan.md](docs/phase-1-6-plan.md) - lightweight validation and lifecycle-example status
25. [formal/lean/README.md](formal/lean/README.md) - Lean formalization boundary and current invariant candidates
26. [docs/phase-2-current-snapshot.md](docs/phase-2-current-snapshot.md) - current Phase 2 Lean snapshot and restart point
27. [docs/phase-2-lean-split-plan.md](docs/phase-2-lean-split-plan.md) - current Phase 2 Lean split plan and non-goals
28. [docs/phase-2-lean-theorem-index.md](docs/phase-2-lean-theorem-index.md) - current Phase 2 Lean theorem role index
29. [docs/definition.md](docs/definition.md) - core definition
30. [docs/eight-elements.md](docs/eight-elements.md) - eight-element structural dimension model
31. [docs/repository-governance.md](docs/repository-governance.md) - repository governance
32. [docs/development-process.md](docs/development-process.md) - development process
33. [docs/schema-cross-reference.md](docs/schema-cross-reference.md) - cross-reference for schema files
34. [spec/review-result.schema.yaml](spec/review-result.schema.yaml) - bounded review-result output schema
35. [spec/runtime-event.schema.yaml](spec/runtime-event.schema.yaml) - draft vendor-neutral runtime event schema
36. [docs/validation-checklist.md](docs/validation-checklist.md) - bounded validation checklist
37. [docs/validator-boundary.md](docs/validator-boundary.md) - boundary for lightweight validation tools
38. [docs/checker-coverage.md](docs/checker-coverage.md) - current lifecycle-aware checker coverage
39. [docs/example-index.md](docs/example-index.md) - index and reading guide for examples
40. [docs/example-review-notes.md](docs/example-review-notes.md) - initial bounded review notes for examples

## Current source-aligned concepts

The repository now distinguishes two related layers:

- the eight-element structural dimension model: Meaning, Authority, Time, Quality, Trust, Reversibility, Value, and Cost
- operational roles and controls: Decision Owner, Approval Gate, Execution Actor, Stop Authority, Evidence Log, Repair Owner, and Human Return Point

The source-alignment pass supports these concepts as current repository-facing source material:

- Responsibility Pathway Design as responsibility-flow design
- Responsibility Pathway Layer as a minimal operational layer
- Action Class Matrix for classifying AI-agent actions
- Human Return Point as return to human understanding, authority, time, information, and responsibility capacity
- Evidence Log as pathway reconstruction support
- Stop Authority as a separate stop role, not merely technical abort
- Repair Owner as post-failure repair / rollback / reconnection ownership
- non-final AI responsibility under current minimal assumptions

## Examples

Minimal examples are available under `examples/`.

- [examples/minimal-pathway.yaml](examples/minimal-pathway.yaml) - a minimal pathway where an AI support node returns responsibility to a human decision owner
- [examples/action-class-matrix-minimal.yaml](examples/action-class-matrix-minimal.yaml) - a classification-only Action Class Matrix fixture for Class A-F reading
- [examples/internal-document-update.yaml](examples/internal-document-update.yaml) - a Class C Approval-Required internal document update example
- [examples/emergency-stop-flow.yaml](examples/emergency-stop-flow.yaml) - a Class F Emergency Stop / stop-and-await example
- [examples/reversible-external-action.yaml](examples/reversible-external-action.yaml) - a Class D Reversible External Action example with rollback or correction path
- [examples/runtime-event-to-pathway-minimal.yaml](examples/runtime-event-to-pathway-minimal.yaml) - a synthetic runtime-event-to-pathway draft example requiring human review
- [examples/record-review-minimal.yaml](examples/record-review-minimal.yaml) - a minimal record-review example with optional review metadata and non-certifying review-result boundaries
- [examples/repair-flow.yaml](examples/repair-flow.yaml) - a minimal repair flow after ambiguity or incomplete evidence is detected
- [examples/suspended-pathway.yaml](examples/suspended-pathway.yaml) - a minimal suspended lifecycle-state example
- [examples/returning-pathway.yaml](examples/returning-pathway.yaml) - a minimal returning lifecycle-state example
- [examples/closed-pathway.yaml](examples/closed-pathway.yaml) - a minimal closed lifecycle-state example

See [docs/example-index.md](docs/example-index.md) for example purposes, boundaries, and future example candidates.

These examples are illustrative only. They do not claim legal liability resolution, moral accountability, safety, fairness, compliance, or production readiness.

Review-result output fixtures are kept separate from pathway examples under `fixtures/review-results/`.

## Lightweight checks

A bounded structural checker is available at [scripts/check_examples.py](scripts/check_examples.py).

Install the minimal Python dependency and run:

```bash
python -m pip install -r requirements.txt
python scripts/check_examples.py
```

The same bounded structural check also runs in GitHub Actions via [.github/workflows/check-examples.yml](.github/workflows/check-examples.yml) when examples, the checker, requirements, or the workflow change.

It checks only limited structural signals and explicit responsibility-boundary fields. A passing result does not mean certified, safe, compliant, fair, legally valid, morally resolved, or production ready.

When an example includes `review_metadata`, the checker also performs optional bounded checks on review metadata structure and non-certifying review-result boundaries.

The runtime-event-to-pathway example is currently checked only as a pathway example. The checker does not yet validate `spec/runtime-event.schema.yaml` or JSON fixtures such as `examples/adapter-input-event-minimal.json`.

A separate bounded review-result checker is available at [scripts/check_review_results.py](scripts/check_review_results.py).

```bash
python scripts/check_review_results.py
```

It checks only review-result fixture structure and boundary-preservation signals. A passing result does not mean legal validation, safety certification, compliance certification, fairness certification, moral resolution, institutional certification, production approval, or AI final-responsibility transfer.

The review-result checker also runs in GitHub Actions via [.github/workflows/check-review-results.yml](.github/workflows/check-review-results.yml). The `Check review-result fixtures` workflow has been observed green for run `#1` on commit `aaaece3` on `main`; this means only that bounded repository-maintenance checks passed for that repository state.

See [docs/validator-boundary.md](docs/validator-boundary.md) for the checker boundary and [docs/checker-coverage.md](docs/checker-coverage.md) for the current checker coverage map.

## Lean formalization

The current Phase 2 Lean work is intentionally minimal.

The Lean spine is split into:

- `formal/lean/ResponsibilityPathway/Basic.lean`
- `formal/lean/ResponsibilityPathway/Lifecycle.lean`
- `formal/lean/ResponsibilityPathway/Examples.lean`
- `formal/lean/ResponsibilityPathway/Invariants.lean`
- `formal/lean/ResponsibilityPathway/Core.lean`

`Core.lean` remains the stable import entry point.

The current Phase 2 snapshot is available at [docs/phase-2-current-snapshot.md](docs/phase-2-current-snapshot.md).

The theorem-role index is available at [docs/phase-2-lean-theorem-index.md](docs/phase-2-lean-theorem-index.md).

It currently contains six scoped invariant candidates:

1. AI final-responsibility boundary under current minimal assumptions
2. AI return-point boundary
3. repair-record boundary
4. suspension review/return boundary
5. returning no-automatic-continuation boundary
6. closure evidence/reopening boundary

The AI final-responsibility boundary is not an absolute claim that AI can never hold responsibility under every possible future legal or institutional framework. In the current minimal RPE model, no artificial legal-personhood layer is assumed, so an AI node is not treated as a final responsibility holder. Future legal, institutional, national, international, or user/provider-agreement layers must be modeled explicitly if introduced.

The Lean formalization does not establish legal validity, safety, compliance, fairness, moral accountability resolution, institutional certification, or production readiness.

A minimal Lean toolchain, Lake package, and GitHub Actions workflow have been added:

```bash
lake build
```

The workflow is defined in [.github/workflows/check-lean.yml](.github/workflows/check-lean.yml). It is intended only to check the current Lean package build. A passing Lean build does not certify legal validity, safety, compliance, fairness, moral accountability resolution, institutional certification, or production readiness.

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
