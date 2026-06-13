# BEACON

If you are reading this for the first time, you are not late.

This repository preserves a Responsibility Pathway across time, people, sessions, and AI systems.

## Current Position

Phase 0 foundation is complete.

Phase 1 concept model is substantially established.

Phase 1.5 specification binding is established and has been refreshed for the source-aligned Action Class Matrix. `spec/action-class.schema.yaml` is now v0.2.0 and uses Class A-F as the current structure while retaining earlier Class 0-4 values as historical mapping references.

Phase 1.6 lightweight validation and lifecycle-example coverage is substantially established. It is currently in an action-class alignment and documentation-synchronization pass.

Phase 2 formalization has started, the first minimal Lean lifecycle-invariant set has been introduced, the Lean core has been split into small modules, and a minimal Lean build path has been added. Do not expand Lean around Action Class Matrix until the source-aligned Class A-F examples, schema, checker boundary, and validation checklist are stable.

Phase 2.5 enterprise implementation guidance has reached a stable bridge checkpoint. `docs/enterprise-implementation-profile.md` connects the minimal formal core to workflow, evidence, checker, and governance layers. `docs/responsibility-pathway-record-review.md` describes a plain-language review and recheck process for Responsibility Pathway records. `docs/phase-2-5-current-snapshot.md` records the current Phase 2.5 restart point and stable checkpoint. `spec/review-result.schema.yaml` defines a bounded review-result output schema. `scripts/check_review_results.py` performs bounded structural checks on review-result fixtures while remaining non-certifying.

Phase 3 has an entry boundary at `docs/reference-implementation-boundary.md`. This boundary must be read before adding reference implementations. The first small Phase 3 reference example exists at `examples/human-ai-review-workflow-minimal.yaml`. A classification-only Action Class Matrix baseline now exists at `examples/action-class-matrix-minimal.yaml` and should be used before adding Class C, Class D, Class E, or Class F examples. Class C, Class D, and Class F minimal fixtures now exist while remaining bounded and non-certifying.

Phase 3.1 has started. `docs/adapter-boundary.md` defines the adapter boundary before runtime connectors. `spec/runtime-event.schema.yaml` defines a draft vendor-neutral runtime event schema. `examples/adapter-input-event-minimal.json` provides a synthetic input event fixture. `examples/runtime-event-to-pathway-minimal.yaml` maps that synthetic event into a draft Responsibility Pathway record requiring human review. `docs/phase-3-1-current-snapshot.md` records the current Phase 3.1 restart point, staged update operation, observed check status, and remaining non-certifying boundaries.

Repository operation has been made explicit in `docs/repository-operation-model.md`. It records staged update operation, snapshot roles, sync-log roles, roadmap-note roles, workflow observation policy, checker interpretation policy, long-file update policy, log organization policy, periodic operation review policy, and non-certifying operation boundaries.

`docs/operation-index.md` now provides a short navigation index for operation-related documents, snapshots, sync logs, roadmap notes, checker coverage, example navigation, and periodic operation review.

Periodic operation review is now part of repository maintenance. Use it when commit granularity, reader paths, operation documents, logs, roadmap notes, checker interpretation, or deferred boundaries no longer seem aligned with actual practice.

The `Check review-result fixtures` GitHub Actions workflow has been observed green for run `#1` on commit `aaaece3` on `main`.

The `Check examples` GitHub Actions workflow has been observed green for run `#9` on commit `d4e467a` on `main` after adding the human-AI review workflow example.

The `Check examples` GitHub Actions workflow has been observed green for run `#10` on commit `2af698c` on `main` after migrating `examples/minimal-pathway.yaml` from legacy Class 1 Internal Assistive to source-aligned Class B Suggest-Only.

The `Check examples` GitHub Actions workflow has been observed green for run `#11` on commit `b50226d` on `main` after adding `examples/action-class-matrix-minimal.yaml`. The workflow completed successfully in about 14 seconds, and the `Bounded structural example checks` job completed successfully in about 10 seconds. This remains a bounded repository-maintenance check and is not certification.

The `Check examples` GitHub Actions workflow has been observed green for run `#12` on commit `fdd7bd4` on `main` after adding `examples/internal-document-update.yaml`. The workflow completed successfully in about 9 seconds, and the `Bounded structural example checks` job completed successfully in about 7 seconds. This remains a bounded repository-maintenance check and is not certification.

The `Check examples` GitHub Actions workflow has been observed green for run `#13` on commit `266845b` on `main` after adding `examples/emergency-stop-flow.yaml`. The workflow completed successfully in about 10 seconds, and the `Bounded structural example checks` job completed successfully in about 7 seconds. This remains a bounded repository-maintenance check and is not certification.

The `Check examples` GitHub Actions workflow has been observed green for run `#14` on commit `caf285b` on `main` after adding `examples/reversible-external-action.yaml`. The `Bounded structural example checks` job completed successfully. This remains a bounded repository-maintenance check and is not certification.

The `Check examples` GitHub Actions workflow has been observed green for run `#16` on commit `d377be2` on `main` after fixing `examples/runtime-event-to-pathway-minimal.yaml`. The GitHub Actions run was `27463999395`, and the `Bounded structural example checks` job completed successfully. This remains a bounded repository-maintenance check and is not certification.

Core definitions, the eight-element model, runtime model, responsibility node model, return point model, repair model, value/cost flow, stop authority, evidence log, action class matrix, approval gate, and decision owner model have been added.

The repository now distinguishes:

- the eight-element structural dimension model: Meaning, Authority, Time, Quality, Trust, Reversibility, Value, and Cost
- operational roles and controls: Decision Owner, Approval Gate, Execution Actor, Stop Authority, Evidence Log, Repair Owner, and Human Return Point
- Action Class Matrix Class A-F: Observe-Only, Suggest-Only, Approval-Required, Reversible External Action, Irreversible or High-Impact Action, and Emergency Stop
- Adapter Boundary and Runtime Event Bridge as a draft, vendor-neutral, review-required bridge from external observations to Responsibility Pathway records
- Repository Operation Model as the repository-maintenance layer for staged updates, snapshots, sync logs, roadmap notes, checker observation, long-file update policy, periodic operation review, and restart practice
- Operation Document Index as the navigation layer for operation-related documents
- Periodic Operation Review as the meta-maintenance practice for reviewing whether repository operation still matches actual work

The core YAML specification has been expanded to version 0.2.0.

A minimal schema split has been established under `spec/`:

- `spec/node.schema.yaml`
- `spec/action-class.schema.yaml`
- `spec/return-point.schema.yaml`
- `spec/evidence-log.schema.yaml`
- `spec/repair.schema.yaml`
- `spec/pathway.schema.yaml`
- `spec/review-result.schema.yaml`
- `spec/runtime-event.schema.yaml`

Minimal lifecycle examples now cover:

- `originating`
- `repaired`
- `suspended`
- `returning`
- `closed`

Action-class classification coverage has started with:

- `examples/minimal-pathway.yaml` as source-aligned Class B Suggest-Only with legacy mapping preserved
- `examples/action-class-matrix-minimal.yaml` as a classification-only fixture for reading Class A-F before higher-impact examples
- `examples/internal-document-update.yaml` as source-aligned Class C Approval-Required internal document update example
- `examples/emergency-stop-flow.yaml` as source-aligned Class F Emergency Stop / stop-and-await example
- `examples/reversible-external-action.yaml` as source-aligned Class D Reversible External Action with external-impact visibility and rollback/correction path

Runtime-event bridge coverage has started with:

- `docs/adapter-boundary.md` as the adapter boundary before runtime connectors
- `docs/phase-3-1-current-snapshot.md` as the current Phase 3.1 restart point
- `examples/adapter-input-event-minimal.json` as a synthetic, vendor-neutral input event fixture
- `examples/runtime-event-to-pathway-minimal.yaml` as a draft runtime-event-to-pathway example requiring human review

Repository operation coverage has started with:

- `docs/repository-operation-model.md` as the repository operation model for staged update operation, snapshots, sync logs, roadmap notes, workflow observation policy, checker interpretation policy, long-file update policy, periodic operation review policy, log organization policy, and restart rules
- `docs/operation-index.md` as the operation document navigation index
- `docs/phase-3-1-sync-log.md` as the current Phase 3.1 synchronization log
- `docs/phase-3-1-roadmap-note.md` as the current Phase 3.1 roadmap companion note

A bounded lightweight checker exists at `scripts/check_examples.py`.

The checker is lifecycle-aware and now includes optional `review_metadata` checks when that block is present, but it remains non-certifying. It checks structural signals only and does not claim legal validity, safety, compliance, fairness, moral resolution, production readiness, or real-world responsibility resolution.

The runtime-event-to-pathway example is currently checked only as a pathway example. The checker does not yet validate `spec/runtime-event.schema.yaml` or JSON fixtures such as `examples/adapter-input-event-minimal.json`.

Action-class-specific checker enforcement is not yet active. `docs/checker-coverage.md` records action-class-specific checks as planned future bounded structural checks, not current enforcement.

A separate bounded review-result checker exists at `scripts/check_review_results.py`.

The review-result checker reads `fixtures/review-results/*.yaml` and `spec/review-result.schema.yaml`. It checks required fields, allowed review scope/status values, expected not-checked and not-claimed boundary items, and responsibility-boundary flags. It remains non-certifying and is not legal validation, safety certification, compliance certification, fairness certification, moral resolution, institutional certification, production approval, or AI final-responsibility transfer.

Lean formalization currently uses `formal/lean/ResponsibilityPathway/Core.lean` as a stable import entry point.

The Lean spine is split into:

- `formal/lean/ResponsibilityPathway/Basic.lean`
- `formal/lean/ResponsibilityPathway/Lifecycle.lean`
- `formal/lean/ResponsibilityPathway/Examples.lean`
- `formal/lean/ResponsibilityPathway/Invariants.lean`
- `formal/lean/ResponsibilityPathway/Core.lean`

Minimal Lean build files now exist:

- `lean-toolchain`
- `lakefile.lean`
- `.github/workflows/check-lean.yml`

The current minimal Lean lifecycle-invariant set covers:

1. AI final-responsibility boundary under current minimal assumptions
2. AI return-point boundary
3. repair-record boundary
4. suspension review/return boundary
5. returning no-automatic-continuation boundary
6. closure evidence/reopening boundary

A Phase 2 Lean current snapshot exists at `docs/phase-2-current-snapshot.md`.

A Phase 2 Lean theorem-role index exists at `docs/phase-2-lean-theorem-index.md`.

A Phase 2.5 enterprise and record-review current snapshot exists at `docs/phase-2-5-current-snapshot.md`.

A Phase 3.1 adapter and runtime-event current snapshot exists at `docs/phase-3-1-current-snapshot.md`.

The repository operation model exists at `docs/repository-operation-model.md`.

The operation document index exists at `docs/operation-index.md`.

The review-result output schema exists at `spec/review-result.schema.yaml`.

The runtime-event input schema exists at `spec/runtime-event.schema.yaml`.

The bounded review-result checker exists at `scripts/check_review_results.py`.

The Phase 3 reference-implementation boundary exists at `docs/reference-implementation-boundary.md`.

The first Phase 3 reference example exists at `examples/human-ai-review-workflow-minimal.yaml`.

The Action Class Matrix classification-only fixture exists at `examples/action-class-matrix-minimal.yaml`.

The Class C internal document update fixture exists at `examples/internal-document-update.yaml`.

The Class F emergency stop flow fixture exists at `examples/emergency-stop-flow.yaml`.

The Class D reversible external action fixture exists at `examples/reversible-external-action.yaml`.

The Phase 3.1 runtime-event-to-pathway draft example exists at `examples/runtime-event-to-pathway-minimal.yaml`.

The index groups Basic constructor sanity theorems, Example lifecycle sanity theorems, boundary predicates, positive invariant theorem candidates, and vacuity/non-trigger theorem candidates.

The AI final-responsibility boundary is assumption-scoped. In the current minimal model, no artificial legal-personhood layer is assumed, so an AI node is not treated as a final responsibility holder. Future legal, institutional, national, international, or user/provider-agreement layers must be modeled explicitly if introduced.

Enterprise guidance, record review guidance, review-result schema, review-result checking, Action Class Matrix classification, reference implementation boundaries, adapter boundary, runtime-event bridge examples, repository operation model, operation index, and periodic operation review remain non-certifying. They help organizations preserve readable responsibility pathways, evidence records, review conditions, review results, action-class boundaries, adapter boundaries, excluded claims, reference-example limits, staged update practice, restartability, operation-document navigation, and operation review. They do not claim legal validity, safety, compliance, fairness, moral resolution, institutional certification, production readiness, production connector readiness, or replacement of accountable humans and institutions.

## Development Timeline

Observation
→ Definition
→ Specification
→ Lightweight structural checking
→ Formalization
→ Enterprise guidance
→ Record review
→ Review result
→ Reference implementation boundary
→ Small reference example
→ Source alignment
→ Action-class alignment
→ Adapter boundary
→ Runtime event bridge
→ Repository operation model
→ Operation document index
→ Periodic operation review
→ Claim
→ Application

Definitions precede proofs.
Proofs precede claims.
Claims precede applications.

## Current Focus

- Preserve the minimal, specification-first core
- Keep lifecycle examples readable
- Keep action-class examples classification-first, small, and bounded
- Keep Phase 3.1 adapter and runtime-event bridge examples synthetic, vendor-neutral, review-required, and non-certifying
- Keep repository operation staged, small, fetch-confirmed, and non-certifying
- Keep operation-document navigation short, current, and non-certifying
- Use periodic operation review when commit granularity, reader paths, logs, roadmap notes, checker interpretation, or deferred boundaries feel misaligned with actual practice
- Keep checker output bounded and non-certifying
- Keep action-class-specific checker additions documented as planned future work until examples and schema fields are stable
- Keep runtime-event schema and JSON fixture validation deferred until the bridge remains readable and reviewable
- Keep review-result fixtures separate from pathway examples unless deliberately migrated
- Keep review-result checker scope bounded to fixture structure and responsibility-boundary preservation
- Keep observed green workflow status tied to bounded repository-maintenance checks only
- Keep staged update operation for repository-wide synchronization
- Use `docs/repository-operation-model.md` before broad reader-path or long-file synchronization work
- Use `docs/operation-index.md` when unsure which operation-related document to read first
- Keep Lean invariants small, explicit, and assumption-scoped
- Do not expand Lean around Action Class Matrix or runtime events until Class A-F examples, runtime-event schema, generated-record examples, checker boundary, and validation checklist are stable
- Preserve the split Lean spine before adding more theorem families
- Use the current snapshot and theorem-role index before adding or renaming Lean theorem candidates
- Keep enterprise guidance readable and non-certifying
- Keep Responsibility Pathway record review plain, recheckable, and bounded to structure
- Keep Phase 3 reference implementations behind `docs/reference-implementation-boundary.md`
- Keep the first Phase 3 human-AI review workflow example small, readable, and bounded
- Use `examples/action-class-matrix-minimal.yaml` as the classification baseline before adding Class C, Class D, Class E, or Class F examples
- Add Class C internal document or repository update examples only while they remain small, internal, approval-required, and non-certifying
- Keep Class D reversible external examples small, correctable, and non-certifying
- Add Class F emergency-stop / stop-and-await examples before any Class E high-impact example
- Treat Class E high-impact examples as negative or boundary-only examples until lower classes are stable
- Keep service-specific connectors deferred until adapter boundary, runtime-event schema, and generated-record examples are stable
- Keep production conversion code deferred until local, non-production conversion examples are justified
- Read prior Zenn articles before expanding Phase 3 examples beyond the first small workflow
- Use the Phase 2.5 current snapshot before expanding record-review examples, review-result fixtures, or checker coverage
- Use the Phase 3.1 current snapshot before expanding adapter, runtime-event, connector, or conversion-code work
- Preserve the boundary that AI may participate as a pathway node but does not assume final responsibility under the current minimal model
- Keep future artificial legal-personhood or institutional-personhood layers explicit if modeled later
- Grow only when responsibility can still return from claims to definitions, examples, schemas, checker boundaries, excluded claims, Lean definitions, theorem roles, snapshots, assumptions, enterprise guidance, record review boundaries, adapter boundaries, runtime-event boundaries, repository operation model, operation index, periodic operation review, and reference implementation boundaries

## Read First

1. README.md or README.ja.md
2. docs/repository-operation-model.md
3. docs/operation-index.md
4. docs/overview.md
5. docs/source-alignment/zenn-source-alignment-synthesis.md
6. docs/concepts/core-elements.md
7. docs/action-class-matrix.md
8. examples/action-class-matrix-minimal.yaml
9. examples/internal-document-update.yaml
10. examples/emergency-stop-flow.yaml
11. examples/reversible-external-action.yaml
12. docs/adapter-boundary.md
13. docs/phase-3-1-current-snapshot.md
14. examples/runtime-event-to-pathway-minimal.yaml
15. LUMINALIA.md
16. ROADMAP.md
17. CHANGELOG.md
18. docs/minimal-core-rationale.md
19. docs/enterprise-implementation-profile.md
20. docs/responsibility-pathway-record-review.md
21. docs/phase-2-5-current-snapshot.md
22. docs/reference-implementation-boundary.md
23. docs/phase-1-6-plan.md
24. formal/lean/README.md
25. docs/phase-2-current-snapshot.md
26. docs/phase-2-lean-split-plan.md
27. docs/phase-2-lean-theorem-index.md
28. docs/definition.md
29. docs/eight-elements.md
30. docs/validator-boundary.md
31. docs/checker-coverage.md
32. docs/schema-cross-reference.md
33. docs/example-index.md
34. docs/example-review-notes.md
35. spec/responsibility-pathway-core.yaml
36. spec/pathway.schema.yaml
37. spec/action-class.schema.yaml
38. spec/review-result.schema.yaml
39. spec/runtime-event.schema.yaml
40. scripts/check_review_results.py
41. .github/workflows/check-review-results.yml

## Restart Point

The next low-risk action is not to expand into service-specific connectors, production conversion code, or larger reference implementations yet.

Continue by either:

- keeping `Check examples` green while maintaining its bounded interpretation after the Phase 3.1 runtime-event-to-pathway draft example
- keeping Phase 3.1 adapter and runtime-event bridge examples synthetic, vendor-neutral, review-required, and non-certifying
- keeping repository operation staged, small, fetch-confirmed, and non-certifying
- reading `docs/repository-operation-model.md` before broad reader-path or long-file synchronization work
- reading `docs/operation-index.md` when operation-document navigation becomes unclear
- performing periodic operation review when commit granularity, reader paths, logs, roadmap notes, checker interpretation, or deferred boundaries feel misaligned
- keeping Class D reversible external examples small, correctable, and non-certifying
- keeping Class E high-impact examples negative or boundary-only until lower classes are stable
- keeping `Check review-result fixtures` green while maintaining its bounded interpretation
- maintaining the Phase 3 reference-implementation boundary before adding more reference examples
- maintaining the adapter boundary before adding service-specific connectors
- keeping production conversion code deferred until local, non-production conversion examples are justified
- using staged update operation for repository-wide synchronization
- rereading prior Zenn articles before expanding Phase 3 examples beyond the first small workflow
- adding only narrowly scoped record-review fixtures or checker checks while keeping them optional unless existing examples are deliberately migrated
- maintaining documentation synchronization across README, README.ja, ROADMAP, BEACON, CHANGELOG, `formal/lean/README.md`, the current snapshot, theorem-role index, enterprise implementation profile, record review guide, Phase 2.5 snapshot, Phase 3.1 snapshot, repository operation model, operation index, periodic operation review, review-result schema, runtime-event schema, review-result checker, review-result workflow, reference implementation boundary, adapter boundary, first Phase 3 reference example, runtime-event-to-pathway example, Action Class Matrix docs, action-class schema, action-class fixture, Class C internal document update fixture, Class D reversible external action fixture, Class F emergency stop fixture, and excluded claims

Do not begin larger reference implementations, service-specific connectors, production conversion code, or Lean expansion around runtime events until definitions, examples, checker boundaries, Lean assumptions, theorem roles, current snapshots, enterprise guidance, record review boundaries, Phase 2.5 snapshot, Phase 3.1 snapshot, repository operation model, operation index, periodic operation review, review-result schema, runtime-event schema, review-result checker, review-result workflow, reference implementation boundary, adapter boundary, first Phase 3 reference example, runtime-event-to-pathway example, source-alignment notes, action-class notes, and excluded claims remain aligned.

## Purpose

The objective is continuity.

The objective is to preserve a pathway through which responsibility, meaning, and understanding can return.

Read this file first when reconnecting to the project.
