# Current Task Inventory

This document records the current task inventory across active and near-active phases.

It is a planning and prioritization note only. It is not a certification record, production approval record, legal review, safety review, compliance review, fairness review, connector correctness proof, adapter correctness proof, runtime correctness proof, Lean completeness proof, standardization certification, progress certification, or AI final-responsibility transfer mechanism.

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
- Keep root `README.md` short, mobile-renderer friendly, and linked to `docs/readme-expanded.md` for the previous expanded content.
- Keep `docs/phase-3-1-current-snapshot.md` as the detailed current-state record for Phase 3.1.
- Keep `docs/phase-3-1-snapshot-reduction-note.md` available as a low-risk follow-up when the Phase 3.1 snapshot becomes too heavy.
- Keep `docs/phase-3-1-ai-judgment-node-reader-path-status.md` available as the current focused reader-path status for AI Judgment Node material.
- Keep `docs/phase-3-1-sync-log.md` as the detailed synchronization record, not a phase plan.
- Keep focused sync notes available when a narrow responsibility unit should not force broad long-file rewrites.
- Keep `docs/phase-3-1-roadmap-note.md` as the short planning companion, not a second changelog.
- Keep `docs/phase-3-1-roadmap-sync-after-readme-recovery.md` as the short companion note for the README recovery and missed-support synchronization unit.
- Keep `docs/progress-map.md` as the rough, planning-only progress and gate map before discussing progress percentage, next gates, or maturity.
- Keep `docs/phase-3-1-progress-map-connection.md` as the focused Phase 3.1 reader-path note for progress-map context without rewriting the full current snapshot.
- Keep `docs/ai-judgment-node-task-control.md` available when AI local judgment, task-control loops, stop conditions, evaluator separation, evidence visibility, or judgment-versus-execution boundaries matter.
- Keep `docs/phase-3-1-ai-judgment-node-connection.md` available as the focused Phase 3.1 connection note for AI local judgment and task-control boundaries.
- Keep `docs/phase-3-1-ai-judgment-node-sync-note.md` available as the focused synchronization record for the AI Judgment Node task-control boundary unit.
- Keep `docs/standardization-strategy.md` as the grounded, non-certifying standardization-preparation note before writing world-standard, conformance, or public-facing standardization claims.
- Keep `docs/external-review-readiness-checklist.md` available before preparing external-review package notes, conformance-model drafting, or public-facing review-readiness claims.
- Keep `docs/external-review-package-note.md` available when preparing a compact reviewer handoff path without treating it as an external review result, endorsement, certification package, conformance package, or deployment approval.
- Keep `docs/responsibility-pathway-availability.md` available when a responsibility pathway becomes narrowed, incomplete, noisy, or temporarily broken and the remaining evidence, missing evidence, uncertainty, or next judgment must be preserved.
- Keep `docs/operation-index.md` aligned when operation documents, snapshots, sync logs, roadmap notes, progress map, focused connection notes, checker plans, runtime candidate planning, review notes, external-review readiness, external-review package notes, standardization strategy, document-role rules, concept navigation, or AI local judgment task-control boundaries change.
- Keep `CHANGELOG.md` archival and investigative rather than the active construction restart path.
- Preserve open-source review intent without implying certification or production approval.
- Keep `docs/deferred-work-restart-conditions.md` as the restart-condition entry point for deferred schema, checker, workflow, connector, runtime, and Lean work.
- Keep `docs/ai-agent-operation-patterns.md` available as the AI-assisted maintenance operation pattern.

## Phase 1.6 task inventory

Current status: substantially established; action-class alignment remains in maintenance mode. A first missed-support boundary example now exists as a checked, non-certifying Class C-style returning example.

### P1: low-risk consolidation

- Maintain bounded checker stability after existing Class C, Class D, Class F, and missed-support boundary examples.
- Keep examples small and manually readable.
- Keep `docs/example-index.md` and `docs/checker-coverage.md` aligned when examples change.
- Keep action-class-specific checker additions documented as planned future bounded work.
- Keep `docs/examples/missed-support-current-status.md` as the focused current-state note for missed-support example work.
- Keep `docs/examples/missed-support-workflow-observation.md` as workflow-observation evidence, not certification.

### P2: bounded artifact preparation

- Use `docs/concepts/support-call-policy.md`, `docs/concepts/missed-support-review-signal.md`, and `docs/examples/missed-support-boundary-example-plan.md` before adding any further missed-support examples.
- Keep any missed-support example synthetic, local, boundary-only or negative, manually readable, and non-certifying.
- Keep support-call policy represented as concept-level and example-level material unless a later schema-design note explicitly reopens schema work.

### P3: conditional checker work

- Add action-class-specific structural checks only after examples and schema fields remain stable.
- Keep any such checks optional or narrowly scoped until existing examples are deliberately migrated.
- Do not add support-call or missed-support checker behavior until schema or example conventions are deliberately designed and restart conditions are satisfied.

### P4: deferred expansion

- Do not add Class E positive examples yet.
- Do not treat current action-class examples as certification, safety review, legal review, or production-readiness evidence.
- Do not add support-call schema fields, missed-support schema fields, support-call semantic checking, or missed-support correctness checking yet.

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

- Do not expand Lean around Action Class Matrix, runtime events, support-call policy, missed-support signals, or AI Judgment Node task-control concepts yet.
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

Current status: first bounded reference example reached; action-class classification baseline exists. AI-assisted maintenance operation notes and missed-support boundary notes now provide additional reviewable repository-maintenance patterns.

### P1: low-risk consolidation

- Keep the first human-AI review workflow example small, readable, bounded, and non-certifying.
- Keep `docs/reference-implementation-boundary.md` as the gate before larger reference implementations.
- Keep source-alignment checkpoints before expanding reference examples.
- Keep Class D reversible external examples small, correctable, and non-certifying.
- Keep `docs/ai-agent-operation-patterns.md` aligned with actual AI-assisted maintenance practice if operation practice changes.
- Keep `docs/ai-judgment-node-task-control.md` visible when AI-assisted maintenance includes local task-control judgment, evidence selection, stop conditions, or evaluator separation.

### P2: bounded artifact preparation

- Add only one small reference example at a time.
- Prefer negative or boundary-only examples before any high-impact positive example.
- Treat `examples/missed-support-boundary-minimal.yaml` as a boundary-only repository-maintenance example, not as production support-routing behavior.

### P4: deferred expansion

- Keep Class E positive examples deferred.
- Avoid production-service, legal-decision, certification, compliance, fairness, moral-resolution, AI-final-responsibility, or AI-local-judgment-as-final-responsibility interpretations.

## Phase 3.1 task inventory

Current status: adapter boundary, runtime-event bridge, runtime-event checking plan, first bounded runtime-event checker stub, first local runtime-event checker pass, first minimal runtime-event workflow, first observed runtime-event workflow success, minimal runtime candidate design, minimal synthetic runtime fixture, minimal synthetic runtime fixture checker coverage, observed minimal runtime fixture checker workflow success, runtime-event schema/fixture alignment note, event-to-pathway relation checker plan, external review readiness checklist, external review package note, README recovery, support-call / missed-support synchronization, operation-reader path recovery, runtime ROADMAP reference closure, grounded standardization strategy, progress map, responsibility pathway availability, focused Phase 3.1 progress-map connection note, AI Judgment Node task-control boundary note, focused Phase 3.1 AI Judgment Node connection note, focused AI Judgment Node synchronization note, Phase 3.1 snapshot reduction follow-up note, and AI Judgment Node reader-path status note are recorded.

### P1: low-risk consolidation

- Keep `docs/phase-3-1-current-snapshot.md` aligned with runtime fixture, first bounded runtime-event checker stub, first minimal runtime-event workflow, observed runtime-event workflow success, minimal runtime fixture checker coverage, runtime-event schema/fixture alignment, event-to-pathway relation checker plan, external review readiness, external review package note, checker boundary, open-source review intent, review notes, README recovery, support-call / missed-support notes, progress map, focused progress-map connection note, responsibility pathway availability, AI Judgment Node task-control boundary, focused AI Judgment Node connection note, standardization strategy, and deferred work.
- Keep `docs/phase-3-1-snapshot-reduction-note.md` as a follow-up for future low-risk snapshot reduction if the current snapshot becomes too heavy.
- Keep `docs/phase-3-1-ai-judgment-node-reader-path-status.md` as the focused current reader-path status for AI Judgment Node material.
- Keep `docs/phase-3-1-sync-log.md` as the detailed synchronization record for runtime-event, runtime-fixture, runtime-event checker stub, runtime-event workflow observation, minimal runtime fixture checker workflow observation, runtime-event schema/fixture alignment, event-to-pathway relation checker planning, external review readiness, external review package note, README recovery, missed-support synchronization, progress-map synchronization, focused connection-note synchronization, responsibility pathway availability synchronization, AI Judgment Node synchronization, and future standardization synchronization units.
- Keep `docs/ai-judgment-node-task-control.md` as the bounded concept and operation boundary note for AI Judgment Nodes, task-control loops, stop conditions, evaluator separation, evidence visibility, and judgment-versus-execution separation.
- Keep `docs/phase-3-1-ai-judgment-node-connection.md` as the focused reader-path note connecting Phase 3.1 to the AI Judgment Node boundary without forcing a broad current-snapshot rewrite.
- Keep `docs/phase-3-1-ai-judgment-node-sync-note.md` as the focused sync-log supplement for the AI Judgment Node task-control boundary responsibility unit.
- Keep `docs/runtime-event-workflow-current-status.md` as the focused workflow-status note for the first runtime-event workflow and observed run status.
- Keep `docs/minimal-runtime-fixture-checker-workflow-observation.md` as the focused observation note for the workflow success after `examples/minimal-synthetic-runtime-fixture.json` was added to bounded runtime-event checker coverage.
- Keep `docs/phase-3-1-minimal-runtime-fixture-checker-connection.md` as the focused reader-path note connecting the minimal runtime fixture checker expansion, workflow observation, and operation documents without forcing a broad current-snapshot or sync-log rewrite.
- Keep `docs/phase-3-1-minimal-runtime-fixture-checker-sync-note.md` as the focused sync-log supplement for the minimal runtime fixture checker workflow observation responsibility unit.
- Keep `docs/runtime-event-schema-fixture-alignment.md` as the focused alignment note connecting the draft runtime-event schema, selected JSON fixtures, and bounded runtime-event checker without treating the alignment as validation.
- Keep `docs/event-to-pathway-relation-checker-plan.md` as the focused plan for possible future structural relation checks between selected runtime-event JSON fixtures and pathway YAML examples, without treating it as implementation permission.
- Keep `docs/external-review-readiness-checklist.md` as the focused review-readiness aid for external inspection without treating readiness as certification, conformance evidence, correctness proof, production approval, or public standardization.
- Keep `docs/external-review-package-note.md` as the compact external-review reader package without treating it as external review findings, endorsement, certification package, conformance package, deployment approval, or public standardization claim.
- Keep `docs/phase-3-1-progress-map-connection.md` as the focused reader-path note connecting Phase 3.1 to `docs/progress-map.md` without forcing a broad current-snapshot rewrite.
- Keep `docs/phase-3-1-roadmap-note.md` as the short planning companion for near-term runtime candidate decisions.
- Keep `docs/phase-3-1-roadmap-sync-after-readme-recovery.md` as the short companion note for the README recovery and missed-support synchronization unit.
- Keep `docs/phase-3-1-roadmap-runtime-reference.md` as a historical reference note; the intended ROADMAP reference has already been absorbed unless the runtime candidate boundary changes again.
- Keep `docs/minimal-runtime-fixture-review-connection.md` as the reader-path note connecting the fixture review to operation documents.
- Keep `docs/progress-map.md` rough and planning-only: progress estimates are not maturity proof, conformance proof, external review findings, or certification.
- Keep `docs/responsibility-pathway-availability.md` reachable for degraded-pathway handling, minimum preservation, and judgment-return handling.
- Keep `docs/standardization-strategy.md` grounded: RPE may prepare for future standardization only by improving terminology, scope, non-scope, reviewability, traceability, compatibility, and anti-overclaim boundaries.
- Keep `docs/example-index.md` and `docs/checker-coverage.md` explicit that JSON runtime-event and minimal synthetic runtime fixture checking remains bounded structural checking and does not validate schema correctness, JSON semantic correctness, adapter mapping correctness, runtime correctness, production readiness, or certification.
- Keep root `README.md` short and point detailed content to `docs/readme-expanded.md`.
- Keep `BEACON.md` short; move detailed state into snapshots, sync logs, roadmap notes, progress map, focused connection notes, or focused status notes.

### P2: bounded artifact preparation

- `docs/minimal-runtime-fixture-review.md` records that `examples/minimal-synthetic-runtime-fixture.json` is acceptable as a first minimal synthetic runtime observation fixture for reading and review.
- No change to `examples/minimal-synthetic-runtime-fixture.json` was required by the first review.
- `scripts/check_runtime_events.py` now exists as the first bounded local runtime-event checker stub and checks both `examples/adapter-input-event-minimal.json` and `examples/minimal-synthetic-runtime-fixture.json` by default.
- `.github/workflows/check-runtime-events.yml` now exists as the first minimal runtime-event workflow and runs when either selected JSON fixture or the checker changes.
- `docs/runtime-event-schema-fixture-alignment.md` records the current structural alignment between `spec/runtime-event.schema.yaml`, selected JSON fixtures, and `scripts/check_runtime_events.py` without treating alignment as validation.
- `docs/event-to-pathway-relation-checker-plan.md` records planned future structurally checkable relation signals such as source-reference preservation, review requirement preservation, evidence and missing-context preservation, actor and responsibility-boundary preservation, excluded-claim preservation, and lifecycle compatibility.
- `docs/external-review-readiness-checklist.md` records the current review-readiness checklist for claim traceability, boundary clarity, checker readability, runtime-event bridge reviewability, operation readability, and non-readiness areas.
- `docs/external-review-package-note.md` records the compact external-review reader path, reviewer questions, inspection targets, non-readiness boundaries, and maintainer pre-send checklist without treating it as an external review result.
- `docs/ai-judgment-node-task-control.md` records the bounded concept for AI Judgment Nodes and task-control boundaries without introducing schema, checker, workflow, runtime, connector, conformance, or Lean work.
- `docs/phase-3-1-snapshot-reduction-note.md` records a maintainability follow-up after the snapshot was expanded with AI Judgment Node material.
- `docs/phase-3-1-ai-judgment-node-reader-path-status.md` records the current AI Judgment Node reader-path status without unlocking implementation.
- `docs/runtime-event-checker-local-observation.md` records the first local runtime-event checker pass.
- `docs/runtime-event-workflow-current-status.md` records the first observed runtime-event workflow success on run `27501847137` and the observed minimal runtime fixture checker workflow success on run `27607798655`.
- `docs/minimal-runtime-fixture-checker-workflow-observation.md` records the focused workflow observation for run `27607798655`.
- If a second runtime fixture is ever needed, design it only through `docs/minimal-runtime-candidate-design.md`.
- Keep any runtime fixture synthetic, local, vendor-neutral, non-production, review-required, and non-certifying.
- Prepare a future `docs/conformance-model-draft.md` only after terminology, scope, examples, schemas, checker boundaries, and review processes stabilize further.

### P3: conditional checker or workflow work

- Treat `scripts/check_runtime_events.py` as the first bounded local runtime-event checker stub, not as schema validation, semantic mapping validation, production runtime integration, or certification.
- Treat `docs/runtime-event-schema-fixture-alignment.md` as an alignment and reviewability note, not as validation, conformance evidence, or proof of semantic correctness.
- Treat `docs/event-to-pathway-relation-checker-plan.md` as a plan only. It does not authorize implementation, semantic correctness checking, adapter mapping checking, responsibility assignment checking, conformance evidence, or production runtime checking by itself.
- Treat `docs/external-review-readiness-checklist.md` as a review-readiness aid only, not as external review findings, certification readiness, conformance evidence, or public standardization evidence.
- Treat `docs/external-review-package-note.md` as a review-navigation package only, not as external review findings, endorsement, certification package, conformance package, deployment approval, or public standardization claim.
- Treat `docs/ai-judgment-node-task-control.md` as a boundary note only, not as autonomous task-control implementation, automatic approval, automatic execution, verification, safety proof, compliance proof, runtime correctness proof, conformance evidence, or AI final-responsibility transfer.
- Treat the observed runtime-event workflow successes as bounded workflow observations only, not as schema validation, JSON semantic correctness proof, runtime correctness proof, production readiness, or certification.
- Expand the runtime-event workflow only after the minimal push-triggered workflow remains stable and the expansion need is documented.
- Add further runtime fixture checking only after `docs/minimal-runtime-candidate-design.md` and `docs/runtime-event-checking-plan.md` preconditions remain satisfied after review.
- Expand runtime-event schema checking only after the schema, selected JSON fixtures, checker boundary, workflow boundary, and documentation path remain stable after the first checker stub and workflow observations.
- Do not implement an event-to-pathway relation checker until `docs/event-to-pathway-relation-checker-plan.md` preconditions are deliberately reviewed and the first implementation remains local, structural, and non-certifying.
- Do not add support-call or missed-support semantic checking until schema conventions, examples, checker boundaries, and review-signal semantics are deliberately stabilized.
- Do not create conformance claims or conformance checks until `docs/standardization-strategy.md` conditions are satisfied.

### P4: deferred expansion

- Keep service-specific connectors deferred.
- Keep production conversion code deferred.
- Keep production runtime integration deferred.
- Keep runtime-event workflow expansion deferred until a specific need is documented.
- Keep runtime-event schema checking deferred until the schema and examples remain stable after the first checker stub and workflow observations.
- Keep JSON schema-fixture checking beyond the selected synthetic runtime-event and minimal synthetic runtime observation fixtures deferred until the bridge remains readable and reviewable.
- Keep event-to-pathway semantic checking deferred.
- Keep AI Judgment Node schema, checker, workflow, runtime, connector, conformance, and Lean expansion deferred until a separate design note and restart-condition review exists.
- Keep further runtime fixture checking deferred unless a new fixture is deliberately designed.
- Keep Lean expansion around adapter or runtime-event concepts deferred.
- Keep Lean expansion around support-call policy or missed-support signals deferred.
- Keep support-call schema fields deferred.
- Keep missed-support schema fields deferred.
- Keep runtime-event support-call fields deferred.
- Keep Class E positive examples deferred.
- Keep finished-standard, certification, legal-validity, safety-proof, compliance-proof, production-readiness, connector-correctness, runtime-correctness, progress-certification, and AI-final-responsibility-transfer claims deferred.

## Open-source review tasks

Open-source review is intended to invite inspection of boundaries, responsibility paths, examples, schemas, checker limits, runtime fixture limits, first bounded runtime-event checker stub, first minimal runtime-event workflow, observed runtime-event workflow successes, minimal runtime fixture checker coverage, runtime-event schema/fixture alignment, event-to-pathway relation checker planning, external review readiness checklist, external review package note, operation documents, progress map, focused progress-map connection note, responsibility pathway availability, AI Judgment Node task-control boundary, standardization strategy, and deferred implementation choices.

### P1: low-risk review preparation

- Make reader paths clear enough that an external reviewer can find current boundaries without reading the whole repository.
- Keep non-certifying boundaries repeated where misunderstanding would be likely.
- Keep `BEACON.md`, `README.md`, `docs/operation-index.md`, current snapshots, sync logs, roadmap notes, progress map, focused connection notes, checker coverage, example index, standardization strategy, external review readiness checklist, external review package note, and focused review notes aligned.
- Keep `docs/ai-judgment-node-task-control.md` and `docs/phase-3-1-ai-judgment-node-connection.md` available when reviewers need to inspect AI local judgment, evaluator separation, loop-like task control, goal-like stop conditions, evidence visibility, and judgment-versus-execution boundaries.
- Keep `docs/external-review-package-note.md` available as the compact reader package for external reviewers before broader external-review handoff or public-facing review-readiness language.
- Keep `docs/external-review-readiness-checklist.md` available as the focused reader path for claim traceability, boundary clarity, checker readability, runtime-event bridge reviewability, operation readability, standardization/public-language readiness, and known non-readiness areas.
- Keep `docs/event-to-pathway-relation-checker-plan.md` available as the focused reader path for planned future structural relation-checker boundaries before any implementation.
- Keep `docs/examples/missed-support-current-status.md` available as the focused reader path for missed-support review.
- Keep `docs/phase-3-1-roadmap-sync-after-readme-recovery.md` available as the short companion note for README recovery and missed-support synchronization.
- Keep `docs/progress-map.md` available as the focused reader path for rough progress, active gates, next gates, and progress-related stop conditions.
- Keep `docs/phase-3-1-progress-map-connection.md` available when reviewers need the Phase 3.1-specific route to the progress map without reading the full current snapshot first.
- Keep `docs/responsibility-pathway-availability.md` available when reviewers need degraded-pathway handling, minimum-preservation, or judgment-return boundaries.
- Keep `docs/standardization-strategy.md` available as the focused reader path for world-standard preparation language, grounding discipline, anti-overclaim boundaries, and future conformance discussion.
- Keep `docs/checker-coverage.md` available as the focused reader path for current checker behavior, including the first bounded runtime-event checker stub and remaining unchecked boundaries.
- Keep `docs/runtime-event-schema-fixture-alignment.md` available as the focused reader path for draft runtime-event schema, selected JSON fixture, and bounded checker alignment without treating it as validation.
- Keep `docs/runtime-event-workflow-current-status.md` available as the focused reader path for the first minimal runtime-event workflow and observed workflow status.
- Keep `docs/minimal-runtime-fixture-checker-workflow-observation.md` available as the focused reader path for the first observed workflow success after the minimal synthetic runtime fixture was added to bounded checker coverage.
- Keep `docs/phase-3-1-minimal-runtime-fixture-checker-connection.md` available as the focused reader path connecting minimal runtime fixture checker expansion and workflow observation without forcing broad long-file rewrites.

### P2: bounded review artifacts

- Prepare short review notes only when they help reviewers inspect a specific boundary.
- Prefer boundary-focused notes over broad claims.
- Keep `docs/ai-judgment-node-task-control.md` as a boundary-focused note, not an autonomous task-control implementation, verification result, certification result, conformance package, production approval, or AI final-responsibility transfer claim.
- Keep `docs/external-review-package-note.md` as a compact external-review navigation aid, not an external review result, endorsement, certification package, conformance package, deployment approval, or public standardization claim.
- Keep `docs/external-review-readiness-checklist.md` as a review-readiness checklist, not certification, conformance evidence, external review findings, production approval, or public standardization evidence.
- Keep `docs/event-to-pathway-relation-checker-plan.md` as a future checker-planning note, not relation-checker implementation, semantic correctness proof, adapter mapping proof, responsibility assignment proof, or conformance evidence.
- Keep `docs/minimal-runtime-fixture-review.md` as a boundary-focused review note, not a checker result or certification record.
- Keep `docs/examples/missed-support-workflow-observation.md` as workflow-observation evidence, not as certification.
- Keep any future external-review note source-based, cautious, and non-accusatory when comparing RPE with existing standards or frameworks.

### P4: deferred public claims

- Do not claim the project proves legal validity, safety, compliance, fairness, moral resolution, production readiness, connector correctness, adapter correctness, runtime correctness, standardization certification, progress certification, AI final-responsibility transfer, or AI-local-judgment final responsibility.

## Recommended next sequence

Use this sequence unless a checker failure or serious inconsistency appears.

1. P0: preserve restartability and boundary clarity.
2. P1: keep BEACON short and ensure README / operation-index / current snapshot / sync log / roadmap note remain aligned.
3. P1: keep AI Judgment Node task-control boundary connected before discussing loop-like task control, goal-like stop conditions, evaluator separation, or local AI judgment as Phase 3.1 runtime-event design inputs.
4. P1: consider `docs/phase-3-1-snapshot-reduction-note.md` before adding more narrow detailed sections to `docs/phase-3-1-current-snapshot.md`.
5. P1: keep progress map rough, planning-only, and connected before using progress percentages in public-facing language.
6. P1: keep `docs/phase-3-1-progress-map-connection.md` available when Phase 3.1 progress visibility is needed without rewriting the full current snapshot.
7. P1: keep standardization strategy grounded and connected before any public-facing world-standard language is expanded.
8. P1: keep external review package note, external review readiness checklist, event-to-pathway relation checker plan, missed-support current status, example index, checker coverage, and focused reader paths aligned after review-readiness, package-note, or checker-planning changes.