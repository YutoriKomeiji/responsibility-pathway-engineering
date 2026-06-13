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

Phase 3 has an entry boundary at `docs/reference-implementation-boundary.md`. This boundary must be read before adding reference implementations. The first small Phase 3 reference example exists at `examples/human-ai-review-workflow-minimal.yaml`. A classification-only Action Class Matrix baseline now exists at `examples/action-class-matrix-minimal.yaml` and should be used before adding Class C, Class D, Class E, or Class F examples.

The `Check review-result fixtures` GitHub Actions workflow has been observed green for run `#1` on commit `aaaece3` on `main`.

The `Check examples` GitHub Actions workflow has been observed green for run `#9` on commit `d4e467a` on `main` after adding the human-AI review workflow example.

The `Check examples` GitHub Actions workflow has been observed green for run `#10` on commit `2af698c` on `main` after migrating `examples/minimal-pathway.yaml` from legacy Class 1 Internal Assistive to source-aligned Class B Suggest-Only.

The `Check examples` GitHub Actions workflow has been observed green for run `#11` on commit `b50226d` on `main` after adding `examples/action-class-matrix-minimal.yaml`. The workflow completed successfully in about 14 seconds, and the `Bounded structural example checks` job completed successfully in about 10 seconds. This remains a bounded repository-maintenance check and is not certification.

The `Check examples` GitHub Actions workflow has been observed green for run `#12` on commit `fdd7bd4` on `main` after adding `examples/internal-document-update.yaml`. The workflow completed successfully in about 9 seconds, and the `Bounded structural example checks` job completed successfully in about 7 seconds. This remains a bounded repository-maintenance check and is not certification.

The `Check examples` GitHub Actions workflow has been observed green for run `#13` on commit `266845b` on `main` after adding `examples/emergency-stop-flow.yaml`. The workflow completed successfully in about 10 seconds, and the `Bounded structural example checks` job completed successfully in about 7 seconds. This remains a bounded repository-maintenance check and is not certification.

Core definitions, the eight-element model, runtime model, responsibility node model, return point model, repair model, value/cost flow, stop authority, evidence log, action class matrix, approval gate, and decision owner model have been added.

The repository now distinguishes:

- the eight-element structural dimension model: Meaning, Authority, Time, Quality, Trust, Reversibility, Value, and Cost
- operational roles and controls: Decision Owner, Approval Gate, Execution Actor, Stop Authority, Evidence Log, Repair Owner, and Human Return Point
- Action Class Matrix Class A-F: Observe-Only, Suggest-Only, Approval-Required, Reversible External Action, Irreversible or High-Impact Action, and Emergency Stop

The core YAML specification has been expanded to version 0.2.0.

A minimal schema split has been established under `spec/`:

- `spec/node.schema.yaml`
- `spec/action-class.schema.yaml`
- `spec/return-point.schema.yaml`
- `spec/evidence-log.schema.yaml`
- `spec/repair.schema.yaml`
- `spec/pathway.schema.yaml`
- `spec/review-result.schema.yaml`

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

A bounded lightweight checker exists at `scripts/check_examples.py`.

The checker is lifecycle-aware and now includes optional `review_metadata` checks when that block is present, but it remains non-certifying. It checks structural signals only and does not claim legal validity, safety, compliance, fairness, moral resolution, production readiness, or real-world responsibility resolution.

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

The review-result output schema exists at `spec/review-result.schema.yaml`.

The bounded review-result checker exists at `scripts/check_review_results.py`.

The Phase 3 reference-implementation boundary exists at `docs/reference-implementation-boundary.md`.

The first Phase 3 reference example exists at `examples/human-ai-review-workflow-minimal.yaml`.

The Action Class Matrix classification-only fixture exists at `examples/action-class-matrix-minimal.yaml`.

The Class C internal document update fixture exists at `examples/internal-document-update.yaml`.

The Class F emergency stop flow fixture exists at `examples/emergency-stop-flow.yaml`.

The index groups Basic constructor sanity theorems, Example lifecycle sanity theorems, boundary predicates, positive invariant theorem candidates, and vacuity/non-trigger theorem candidates.

The AI final-responsibility boundary is assumption-scoped. In the current minimal model, no artificial legal-personhood layer is assumed, so an AI node is not treated as a final responsibility holder. Future legal, institutional, national, international, or user/provider-agreement layers must be modeled explicitly if introduced.

Enterprise guidance, record review guidance, review-result schema, review-result checking, Action Class Matrix classification, and reference implementation boundaries remain non-certifying. They help organizations preserve readable responsibility pathways, evidence records, review conditions, review results, action-class boundaries, excluded claims, and reference-example limits. They do not claim legal validity, safety, compliance, fairness, moral resolution, institutional certification, production readiness, or replacement of accountable humans and institutions.

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
→ Claim
→ Application

Definitions precede proofs.
Proofs precede claims.
Claims precede applications.

## Current Focus

- Preserve the minimal, specification-first core
- Keep lifecycle examples readable
- Keep action-class examples classification-first and low impact
- Keep checker output bounded and non-certifying
- Keep action-class-specific checker additions documented as planned future work until examples and schema fields are stable
- Keep review-result fixtures separate from pathway examples unless deliberately migrated
- Keep review-result checker scope bounded to fixture structure and responsibility-boundary preservation
- Keep observed green workflow status tied to bounded repository-maintenance checks only
- Keep Lean invariants small, explicit, and assumption-scoped
- Do not expand Lean around Action Class Matrix until Class A-F examples, schema, checker boundary, and validation checklist are stable
- Preserve the split Lean spine before adding more theorem families
- Use the current snapshot and theorem-role index before adding or renaming Lean theorem candidates
- Keep enterprise guidance readable and non-certifying
- Keep Responsibility Pathway record review plain, recheckable, and bounded to structure
- Keep Phase 3 reference implementations behind `docs/reference-implementation-boundary.md`
- Keep the first Phase 3 human-AI review workflow example small, readable, and bounded
- Use `examples/action-class-matrix-minimal.yaml` as the classification baseline before adding Class C, Class D, Class E, or Class F examples
- Add Class C internal document or repository update examples only while they remain small, internal, approval-required, and non-certifying
- Add Class F emergency-stop / stop-and-await examples before any Class E high-impact example
- Delay Class D reversible external examples until Class C and Class F boundaries are clear
- Treat Class E high-impact examples as negative or boundary-only examples until lower classes are stable
- Read prior Zenn articles before expanding Phase 3 examples beyond the first small workflow
- Use the Phase 2.5 current snapshot before expanding record-review examples, review-result fixtures, or checker coverage
- Preserve the boundary that AI may participate as a pathway node but does not assume final responsibility under the current minimal model
- Keep future artificial legal-personhood or institutional-personhood layers explicit if modeled later
- Grow only when responsibility can still return from claims to definitions, examples, schemas, checker boundaries, excluded claims, Lean definitions, theorem roles, snapshots, assumptions, enterprise guidance, record review boundaries, and reference implementation boundaries

## Read First

1. README.md or README.ja.md
2. docs/overview.md
3. docs/source-alignment/zenn-source-alignment-synthesis.md
4. docs/concepts/core-elements.md
5. docs/action-class-matrix.md
6. examples/action-class-matrix-minimal.yaml
7. examples/internal-document-update.yaml
8. examples/emergency-stop-flow.yaml
9. LUMINALIA.md
10. ROADMAP.md
11. CHANGELOG.md
12. docs/minimal-core-rationale.md
13. docs/enterprise-implementation-profile.md
14. docs/responsibility-pathway-record-review.md
15. docs/phase-2-5-current-snapshot.md
16. docs/reference-implementation-boundary.md
17. docs/phase-1-6-plan.md
18. formal/lean/README.md
19. docs/phase-2-current-snapshot.md
20. docs/phase-2-lean-split-plan.md
21. docs/phase-2-lean-theorem-index.md
22. docs/definition.md
23. docs/eight-elements.md
24. docs/validator-boundary.md
25. docs/checker-coverage.md
26. docs/schema-cross-reference.md
27. docs/example-index.md
28. docs/example-review-notes.md
29. spec/responsibility-pathway-core.yaml
30. spec/pathway.schema.yaml
31. spec/action-class.schema.yaml
32. spec/review-result.schema.yaml
33. scripts/check_review_results.py
34. .github/workflows/check-review-results.yml

## Restart Point

The next low-risk action is not to expand into larger reference implementations yet.

Continue by either:

- updating ROADMAP and CHANGELOG with the `Check examples #13` observed green result
- delaying Class D reversible external action example until Class C and Class F boundaries remain green
- keeping Class E high-impact examples negative or boundary-only until lower classes are stable
- keeping `Check review-result fixtures` green while maintaining its bounded interpretation
- keeping `Check examples` green while maintaining its bounded interpretation after Class F emergency stop flow
- maintaining the Phase 3 reference-implementation boundary before adding more reference examples
- rereading prior Zenn articles before expanding Phase 3 reference examples beyond the first small workflow
- adding only narrowly scoped record-review fixtures or checker checks while keeping them optional unless existing examples are deliberately migrated
- maintaining documentation synchronization across README, README.ja, ROADMAP, BEACON, CHANGELOG, `formal/lean/README.md`, the current snapshot, theorem-role index, enterprise implementation profile, record review guide, Phase 2.5 snapshot, review-result schema, review-result checker, review-result workflow, reference implementation boundary, first Phase 3 reference example, Action Class Matrix docs, action-class schema, action-class fixture, Class C internal document update fixture, Class F emergency stop fixture, and excluded claims

Do not begin larger reference implementations until definitions, examples, checker boundaries, Lean assumptions, theorem roles, current snapshot, enterprise guidance, record review boundaries, Phase 2.5 snapshot, review-result schema, review-result checker, review-result workflow, reference implementation boundary, first Phase 3 reference example, source-alignment notes, action-class notes, and excluded claims remain aligned.

## Purpose

The objective is continuity.

The objective is to preserve a pathway through which responsibility, meaning, and understanding can return.

Read this file first when reconnecting to the project.
