# CHANGELOG

This changelog records conceptual milestones rather than individual code edits.

## 2026-06

### Periodic operation review policy added

- `docs/repository-operation-model.md` now includes a periodic operation review policy for reviewing repository operation while operating
- `docs/operation-index.md` now points readers to the periodic operation review policy when commit granularity, reader paths, logs, roadmap notes, checker interpretation, or deferred boundaries need review
- `BEACON.md` now records periodic operation review as part of the current repository-maintenance practice and restart guidance
- Periodic operation review may produce operation-model updates, operation-index updates, current snapshot updates, sync-log entries, roadmap notes, or short changelog milestones when the repository operating model changes how future work should be read or maintained
- Periodic operation review remains a repository-maintenance practice only; it is not production approval, connector correctness proof, adapter correctness proof, legal review, safety review, compliance review, fairness review, Lean completeness proof, or AI final-responsibility transfer

### Phase 3.1 repository operation model and synchronization notes added

- `docs/repository-operation-model.md` added to document staged update operation, snapshot roles, sync-log roles, roadmap-note roles, workflow observation policy, checker interpretation policy, long-file update policy, log organization policy, non-certifying operation boundaries, and restart rules
- `docs/phase-3-1-sync-log.md` records the staged synchronization work for the Phase 3.1 Adapter Boundary and Runtime Event Bridge
- `docs/phase-3-1-roadmap-note.md` records the short roadmap companion for Phase 3.1 so that large `ROADMAP.md` updates can remain small and reviewable
- README, README.ja, BEACON, ROADMAP, and the Phase 3.1 current snapshot now point to the repository operation model or the Phase 3.1 companion notes
- The operation model is a repository-maintenance guide only; it is not certification, legal review, safety review, compliance review, production approval, connector correctness proof, adapter correctness proof, or AI final-responsibility transfer

### Phase 3.1 runtime-event bridge synchronization checkpoint added

- `docs/adapter-boundary.md`, `spec/runtime-event.schema.yaml`, `examples/adapter-input-event-minimal.json`, and `examples/runtime-event-to-pathway-minimal.yaml` establish a draft, vendor-neutral, review-required bridge from runtime observations to Responsibility Pathway draft records
- `docs/phase-3-1-current-snapshot.md` records the current Phase 3.1 restart point, observed checker status, staged update operation, and non-certifying boundaries
- `docs/example-index.md`, `docs/checker-coverage.md`, `docs/schema-cross-reference.md`, README, README.ja, BEACON, and ROADMAP now include the Phase 3.1 runtime-event bridge reader path or coverage notes
- The current checker treats `examples/runtime-event-to-pathway-minimal.yaml` only as a pathway example; it does not yet validate `spec/runtime-event.schema.yaml`, `examples/adapter-input-event-minimal.json`, adapter mapping correctness, service-specific connector behavior, or production runtime behavior
- Service-specific connectors, production conversion code, runtime-event schema checking, JSON fixture checking, Class E positive examples, and Lean expansion around runtime events remain deferred

### Check examples #16 observed green for runtime-event-to-pathway draft example

- `Check examples #16` observed green on commit `d377be2` on `main` after fixing `examples/runtime-event-to-pathway-minimal.yaml`
- The GitHub Actions run was `27463999395`
- The `Bounded structural example checks` job completed successfully after the example was aligned with the existing checker-required top-level `return_points` key and `human_responsibility_capacity: true` on the human decision owner node
- The observed green status remains a bounded repository-maintenance check and is not certification

### Check examples #14 observed green for Class D reversible external action fixture

- `Check examples #14` observed green on commit `caf285b` on `main` after adding `examples/reversible-external-action.yaml`
- The `Bounded structural example checks` job completed successfully
- BEACON and ROADMAP now record the observed green workflow status
- The observed green status remains a bounded repository-maintenance check and is not certification

### Class D reversible external action fixture added

- `examples/reversible-external-action.yaml` added as a Class D Reversible External Action example
- The fixture models a human-approved external notification with affected-party visibility and a rollback or correction path
- AI participation remains drafting, recommendation, explanation, and classification support only; AI approval, execution, stop authority, repair authority, and final responsibility remain disallowed
- `docs/example-index.md` and `docs/checker-coverage.md` now include the Class D fixture while keeping action-class-specific checker enforcement as future bounded work
- The fixture remains structural and non-certifying, and does not claim harmless reversibility, legal validity, safety, compliance, fairness, moral resolution, production readiness, or AI final-responsibility transfer

### Action Class Matrix source-alignment checkpoint added

- `docs/action-class-matrix.md` updated from the earlier Class 0-4 form to the source-aligned Class A-F form
- Earlier Class 0-4 categories are retained as historical mapping references instead of being silently removed
- `spec/action-class.schema.yaml` updated to v0.2.0 with `source_aligned_class: A-F` as the current structure and legacy `level: 0-4` as optional historical mapping
- `examples/minimal-pathway.yaml` migrated from legacy Class 1 Internal Assistive to source-aligned Class B Suggest-Only with legacy mapping preserved
- `examples/action-class-matrix-minimal.yaml` added as a classification-only fixture for reading Class A-F before adding higher-impact examples
- `docs/example-index.md`, `docs/checker-coverage.md`, ROADMAP, and BEACON now connect examples, schema, and checker boundaries to Action Class Matrix work
- The checkpoint remains structural and non-certifying, and does not claim legal validity, safety, compliance, fairness, moral resolution, institutional certification, production readiness, or AI final-responsibility transfer

### Check examples #11 observed green for action-class classification fixture

- `Check examples #11` observed green on commit `b50226d` on `main` after adding `examples/action-class-matrix-minimal.yaml`
- The workflow completed successfully in about 14 seconds, and the `Bounded structural example checks` job completed successfully in about 10 seconds
- BEACON and ROADMAP now record the observed green workflow status
- The observed green status remains a bounded repository-maintenance check and is not certification

### Check examples #12 observed green for Class C internal document update fixture

- `Check examples #12` observed green on commit `fdd7bd4` on `main` after adding `examples/internal-document-update.yaml`
- The workflow completed successfully in about 9 seconds, and the `Bounded structural example checks` job completed successfully in about 7 seconds
- BEACON and ROADMAP now record the observed green workflow status
- The observed green status remains a bounded repository-maintenance check and is not certification

### Check examples #13 observed green for Class F emergency stop fixture

- `Check examples #13` observed green on commit `266845b` on `main` after adding `examples/emergency-stop-flow.yaml`
- The workflow completed successfully in about 10 seconds, and the `Bounded structural example checks` job completed successfully in about 7 seconds
- BEACON and ROADMAP now record the observed green workflow status
- The observed green status remains a bounded repository-maintenance check and is not certification

### Core operational roles aligned with eight-element model

- `docs/concepts/core-elements.md` now treats Decision Owner, Approval Gate, Execution Actor, Stop Authority, Evidence Log, Repair Owner, and Human Return Point as operational roles and controls
- The file explicitly states that these seven roles/controls do not replace the eight-element structural dimension model
- `docs/overview.md` and README now distinguish the eight-element model from operational roles and controls
- The alignment preserves Meaning, Authority, Time, Quality, Trust, Reversibility, Value, and Cost as the eight-element structural dimensions

### Action-class checker coverage documented as future bounded work

- `docs/checker-coverage.md` now states that action-class-specific checker enforcement is not yet active
- Planned future bounded checks may inspect declared `action_class`, Class C or higher approval design, Class D or higher rollback/repair design, Class E high-impact boundaries, and Class F stop/return boundaries
- Existing examples are not retroactively required to satisfy action-class-specific checker rules unless deliberately migrated
- Any future checker rule must remain structural and non-certifying

### BEACON and ROADMAP synchronized with action-class current position
