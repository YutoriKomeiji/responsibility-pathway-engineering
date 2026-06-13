# Current Task Inventory

This document records the current task inventory across active and near-active phases.

It is a planning and prioritization note only. It is not a certification record, production approval record, legal review, safety review, compliance review, fairness review, connector correctness proof, adapter correctness proof, runtime correctness proof, Lean completeness proof, or AI final-responsibility transfer mechanism.

## Priority classes

Use the following priority classes when choosing the next task.

| Priority | Meaning | Rule |
| --- | --- | --- |
| P0 | Preserve restartability and boundaries | Do before broad implementation or public-claim expansion. |
| P1 | Low-risk consolidation | Safe documentation, reader-path, index, coverage, or snapshot work. |
| P2 | Bounded artifact preparation | Small examples, fixtures, or design notes that remain synthetic, local, review-required, and non-certifying. |
| P3 | Conditional checker or workflow work | Only after documented preconditions remain satisfied. |
| P4 | Deferred expansion | Do not start until lower-risk layers are stable and explicitly reopened. |

## Cross-phase P0 tasks

These tasks preserve the repository's current operating ability.

- Keep `BEACON.md` short enough to remain a reconnection entrance.
- Keep `docs/phase-3-1-current-snapshot.md` as the detailed current-state record for Phase 3.1.
- Keep `docs/operation-index.md` aligned when operation documents, snapshots, sync logs, roadmap notes, checker plans, runtime candidate planning, or document-role rules change.
- Keep `docs/phase-3-1-sync-log.md` as the detailed synchronization record, not a phase plan.
- Keep `docs/phase-3-1-roadmap-note.md` as the short planning companion, not a second changelog.
- Keep `CHANGELOG.md` archival and investigative rather than the active construction restart path.
- Preserve open-source review intent without implying certification or production approval.

## Phase 1.6 task inventory

Current status: substantially established; action-class alignment remains in maintenance mode.

### P1: low-risk consolidation

- Maintain bounded checker stability after existing Class C, Class D, and Class F examples.
- Keep examples small and manually readable.
- Keep `docs/example-index.md` and `docs/checker-coverage.md` aligned when examples change.
- Keep action-class-specific checker additions documented as planned future bounded work.

### P3: conditional checker work

- Add action-class-specific structural checks only after examples and schema fields remain stable.
- Keep any such checks optional or narrowly scoped until existing examples are deliberately migrated.

### P4: deferred expansion

- Do not add Class E positive examples yet.
- Do not treat current action-class examples as certification, safety review, legal review, or production-readiness evidence.

## Phase 2 task inventory

Current status: formalization started; minimal Lean lifecycle invariant set reached; Lean core split, build path, theorem index, and current snapshot exist.

### P1: low-risk consolidation

- Keep the Lean spine small and readable.
- Maintain `formal/lean/ResponsibilityPathway/Core.lean` as the stable import entry point.
- Use `docs/phase-2-current-snapshot.md` and `docs/phase-2-lean-theorem-index.md` before adding or renaming theorem candidates.
- Keep formal claims assumption-scoped and traceable to examples, schemas, checker boundaries, and excluded claims.

### P3: conditional Lean work

- Expand Lean only after relevant examples, schema fields, checker boundaries, and validation checklists are stable.
- Observe Lean workflow results before treating build behavior as current.

### P4: deferred expansion

- Do not expand Lean around Action Class Matrix or runtime events yet.
- Do not formalize production connectors, runtime correctness, adapter correctness, legal responsibility, safety, compliance, fairness, or moral resolution.

## Phase 2.5 task inventory

Current status: stable bridge checkpoint reached for enterprise implementation profile and record-review layer.

### P1: low-risk consolidation

- Maintain the stable checkpoint without expanding claims.
- Keep review-result fixture checks separate from pathway example checks unless deliberately integrated.
- Keep review-result schema validation and fixture checking bounded to structural responsibility-boundary preservation.
- Keep `docs/phase-2-5-current-snapshot.md` current if record-review or review-result boundaries change.

### P3: conditional checker work

- Add review-result checker coverage only if the review-result schema grows and the new check remains structural.
- Integrate review-result and pathway example checking only with an explicit migration plan.

### P4: deferred expansion

- Do not treat enterprise guidance, review-result outputs, observed green workflows, or review processes as certification, legal validity, safety, compliance, fairness, moral resolution, institutional approval, or production readiness.

## Phase 3 task inventory

Current status: first bounded reference example reached; action-class classification baseline exists.

### P1: low-risk consolidation

- Keep the first human-AI review workflow example small, readable, bounded, and non-certifying.
- Keep `docs/reference-implementation-boundary.md` as the gate before larger reference implementations.
- Keep source-alignment checkpoints before expanding reference examples.
- Keep Class D reversible external examples small, correctable, and non-certifying.

### P2: bounded artifact preparation

- Add only one small reference example at a time.
- Prefer negative or boundary-only examples before any high-impact positive example.

### P4: deferred expansion

- Keep Class E positive examples deferred.
- Avoid production-service, legal-decision, certification, compliance, fairness, moral-resolution, or AI-final-responsibility interpretations.

## Phase 3.1 task inventory

Current status: adapter boundary, runtime-event bridge, runtime-event checking plan, minimal runtime candidate design, and minimal synthetic runtime fixture exist.

### P1: low-risk consolidation

- Keep `docs/phase-3-1-current-snapshot.md` aligned with runtime fixture, checker boundary, open-source review intent, and deferred work.
- Keep `docs/phase-3-1-sync-log.md` as the detailed synchronization record for runtime-event and runtime-fixture work.
- Keep `docs/phase-3-1-roadmap-note.md` as the short planning companion for near-term runtime candidate decisions.
- Keep `docs/phase-3-1-roadmap-runtime-reference.md` as a short note for ROADMAP reference until a safe short ROADMAP edit is possible.
- Keep `docs/example-index.md` and `docs/checker-coverage.md` explicit that the JSON runtime fixture is for reading and review only.

### P2: bounded artifact preparation

- Review `examples/minimal-synthetic-runtime-fixture.json` for clarity, smallness, and boundary preservation.
- If a second runtime fixture is ever needed, design it only through `docs/minimal-runtime-candidate-design.md`.
- Keep any runtime fixture synthetic, local, vendor-neutral, non-production, review-required, and non-certifying.

### P3: conditional checker or workflow work

- Add runtime fixture checking only after `docs/minimal-runtime-candidate-design.md` and `docs/runtime-event-checking-plan.md` preconditions remain satisfied after review.
- Add `scripts/check_runtime_events.py` only after runtime-event checking preconditions are explicitly satisfied.
- Add a runtime-event workflow only after local runtime-event checker behavior exists and has been observed.

### P4: deferred expansion

- Keep service-specific connectors deferred.
- Keep production conversion code deferred.
- Keep production runtime integration deferred.
- Keep runtime-event schema checking deferred until the schema and examples remain stable.
- Keep JSON fixture checking deferred until the bridge remains readable and reviewable.
- Keep Lean expansion around adapter or runtime-event concepts deferred.
- Keep Class E positive examples deferred.

## Open-source review tasks

Open-source review is intended to invite inspection of boundaries, responsibility paths, examples, schemas, checker limits, runtime fixture limits, operation documents, and deferred implementation choices.

### P1: low-risk review preparation

- Make reader paths clear enough that an external reviewer can find current boundaries without reading the whole repository.
- Keep non-certifying boundaries repeated where misunderstanding would be likely.
- Keep `BEACON.md`, `docs/operation-index.md`, current snapshots, checker coverage, and example index aligned.

### P2: bounded review artifacts

- Prepare short review notes only when they help reviewers inspect a specific boundary.
- Prefer boundary-focused notes over broad claims.

### P4: deferred public claims

- Do not claim the project proves legal validity, safety, compliance, fairness, moral resolution, production readiness, connector correctness, adapter correctness, runtime correctness, or AI final-responsibility transfer.

## Recommended next sequence

Use this sequence unless a checker failure or serious inconsistency appears.

1. P0: preserve restartability and boundary clarity.
2. P1: connect this task inventory through `docs/operation-index.md` and the current Phase 3.1 snapshot.
3. P1: decide whether `ROADMAP.md` should receive only a short reference to `docs/phase-3-1-roadmap-runtime-reference.md` in a later small edit.
4. P2: review the minimal synthetic runtime fixture for readability and boundary preservation.
5. P2: prepare external-review notes only if they improve reviewability.
6. P3: consider runtime fixture checking only after documented preconditions remain satisfied.
7. P4: keep connectors, production runtime, production conversion, Class E positive examples, and runtime Lean expansion deferred.

## Stop conditions

Stop and preserve state if:

- a long file update is blocked
- a checker failure appears
- a task starts implying production runtime integration
- a task starts depending on a service-specific connector
- a task implies automatic approval or execution
- a task implies certification, legal validation, safety certification, compliance certification, fairness certification, moral resolution, connector correctness, adapter correctness, runtime correctness, production readiness, or AI final-responsibility transfer
