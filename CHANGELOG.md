# CHANGELOG

This changelog records conceptual milestones rather than individual code edits.

## 2026-06

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

- ROADMAP now records Phase 1.6 as an action-class alignment and documentation-synchronization pass
- ROADMAP now records `examples/action-class-matrix-minimal.yaml` as a classification-only baseline before Class C, Class D, Class E, or Class F examples
- BEACON now records the current action-class alignment position, read-first path, current focus, and restart point
- BEACON and ROADMAP both state that Lean should not be expanded around Action Class Matrix until Class A-F examples, schema, checker boundary, and validation checklist are stable

### Phase 2.5 stable checkpoint added

- `docs/phase-2-5-current-snapshot.md` now records a stable checkpoint for the enterprise implementation and record-review bridge
- The checkpoint lists the enterprise profile, record-review guide, minimal example, review-result fixture, review-result schema, alignment note, bounded checker, GitHub Actions workflow, observed green run, validator boundary, and synchronized reader files
- The checkpoint remains structural and non-certifying, and does not claim legal validity, safety, compliance, fairness, moral resolution, institutional certification, production readiness, or real-world responsibility resolution

### README files updated with review-result workflow status

- README and README.ja now record that the `Check review-result fixtures` GitHub Actions workflow was observed green for run `#1` on commit `aaaece3` on `main`
- README and README.ja keep the observed green workflow status bounded to repository-maintenance checks and non-certifying interpretation

### ROADMAP updated with review-result workflow status

- ROADMAP now records the review-result schema/fixture alignment note, bounded review-result checker, review-result workflow, observed green workflow status, and validator-boundary update in Phase 2.5
- ROADMAP now removes the outdated note that review-result fixtures are not yet checked
- ROADMAP keeps the observed green workflow status structural and non-certifying

### Validator boundary updated for review-result checker

- `docs/validator-boundary.md` now records both `scripts/check_examples.py` and `scripts/check_review_results.py` as bounded repository-maintenance checkers
- The validator boundary now documents what the review-result checker may check and what it must not claim
- The validator boundary now records that observed green GitHub Actions status is a bounded repository-maintenance signal, not certification
- The update keeps checker and workflow interpretation structural and non-certifying

### Review-result fixture workflow observed green

- `Check review-result fixtures` GitHub Actions workflow observed green for run `#1` on commit `aaaece3` on `main`
- The workflow completed successfully in about 12 seconds, and the `Check review-result fixtures` job completed successfully in about 8 seconds
- `docs/phase-2-5-current-snapshot.md` and BEACON now record the observed green workflow status
- The observed green status remains a bounded repository-maintenance check and is not certification

### Review-result fixture workflow added

- `.github/workflows/check-review-results.yml` added to run `scripts/check_review_results.py` on review-result fixture, review-result schema, checker, requirements, or workflow changes
- The workflow installs the minimal Python dependencies and runs the bounded review-result checker
- The workflow remains structural and non-certifying

### Reader path synchronized for bounded review-result checker

- README.ja now documents manual execution of `scripts/check_review_results.py`
- BEACON now records the bounded review-result checker in the current position, read-first path, current focus, and restart point
- The synchronization keeps review-result checking structural and non-certifying

### Bounded review-result checker added

- `scripts/check_review_results.py` added as a bounded structural checker for review-result fixtures under `fixtures/review-results/*.yaml`
- The checker reads `spec/review-result.schema.yaml` and checks required fields, allowed review scope/status values, expected `not_checked` and `not_claimed` boundary items, and responsibility-boundary flags
- README now documents manual execution of the checker
- `docs/checker-coverage.md` now records the checker separately from `scripts/check_examples.py`
- `docs/phase-2-5-current-snapshot.md` now records the checker and keeps CI wiring as a later low-risk step
- The checker remains structural and non-certifying

### Review-result schema fixture alignment note added

- `docs/review-result-schema-fixture-alignment.md` added as a documentation-only alignment note for the current review-result schema and minimal review-result fixture
- `docs/phase-2-5-current-snapshot.md` now records the alignment note as part of the current Phase 2.5 set
- `docs/checker-coverage.md` now links the alignment note and clarifies that it is not an automated checker result
- The alignment note records that the fixture includes the current schema's required fields, not-checked list, not-claimed list, and responsibility-boundary flags
- The update remains structural and non-certifying

### Reader path updated for review-result schema

- README and README.ja now link to `spec/review-result.schema.yaml` in the reader path
- README and README.ja clarify that review-result fixtures are not currently validated by `scripts/check_examples.py`
- BEACON now records the review-result schema in the current position, schema list, read-first path, current focus, and restart point
- The update keeps review-result schema work structural and non-certifying

### Review-result checker coverage boundary documented

- `docs/checker-coverage.md` now records that `fixtures/review-results/*.yaml` are not currently read by `scripts/check_examples.py`
- `docs/checker-coverage.md` now records that `spec/review-result.schema.yaml` is not currently validated by the checker
- ROADMAP now notes the review-result schema and the current unchecked status of review-result fixtures
- This keeps pathway example checks separate from review-result fixture validation until a future deliberate checker is added
- The update remains structural and non-certifying

### Review result schema added

- `spec/review-result.schema.yaml` added as the bounded public schema for Responsibility Pathway review-result outputs
- `docs/schema-cross-reference.md` now includes the review-result schema and places it after composed pathway instances in the reading order
- `docs/phase-2-5-current-snapshot.md` now records the review-result schema as part of the current Phase 2.5 set
- The schema records checked items, not-checked items, not-claimed boundaries, review status, review scope, tool version, and responsibility-boundary flags
- The schema remains structural and non-certifying, and adds no legal, safety, compliance, fairness, moral-resolution, certification, production-approval, or AI-final-responsibility-transfer claims

### ROADMAP Phase 2.5 status synchronized

- ROADMAP now records the Phase 2.5 current snapshot, minimal record-review example, minimal review-result fixture, and optional review metadata checks
- ROADMAP now includes short next low-risk Phase 2.5 work items
- This resolves the earlier deferred ROADMAP synchronization with a smaller update
- The update remains structural and non-certifying

### Minimal review result fixture added

- `fixtures/review-results/record-review-result-minimal.yaml` added as a small output fixture for a bounded Responsibility Pathway review result
- `docs/responsibility-pathway-record-review.md` now links to the fixture and clarifies that it is an output example only
- `docs/phase-2-5-current-snapshot.md` now records the review-result fixture as part of the current Phase 2.5 set
- The fixture is not a pathway example and is not currently part of the bounded example checker workflow
- The fixture remains structural and non-certifying, and adds no legal, safety, compliance, fairness, moral-resolution, certification, or production-readiness claims

### Phase 2.5 current snapshot added

- `docs/phase-2-5-current-snapshot.md` added as a reconnection note for enterprise implementation guidance and Responsibility Pathway record review
- README, README.ja, and BEACON now link to the Phase 2.5 current snapshot
- The snapshot records current Phase 2.5 files, schema alignment, the minimal record-review example, optional review metadata checker support, current green check status, boundaries, next low-risk work, stop conditions, and restart point
- The snapshot remains structural and non-certifying
- ROADMAP synchronization is now completed with a smaller follow-up update

### Optional review metadata checks added

- `scripts/check_examples.py` now checks optional `review_metadata` structure when it is present
- The checker requires `review_tool_version`, non-empty `checked_items`, non-empty `unchecked_items`, `review_result`, and non-empty `review_result.not_claimed` only for examples that include `review_metadata`
- `docs/checker-coverage.md` now documents the optional review metadata checks and keeps their interpretation bounded and non-certifying
- Existing examples without `review_metadata` are not required to add it
- This remains a bounded structural check and adds no legal, safety, compliance, fairness, moral-resolution, certification, or production-readiness claims

### Minimal record review example added

- `examples/record-review-minimal.yaml` added as a small readable example for Responsibility Pathway record review
- `docs/example-index.md` now describes the record-review example and places it in the recommended example reading order
- `docs/checker-coverage.md` now lists the record-review example in the current example coverage map
- The example follows the existing originating lifecycle checker path and does not expand checker semantics
- The example remains structural and non-certifying, and adds no legal, safety, compliance, fairness, moral-resolution, certification, or production-readiness claims

### Pathway schema aligned with record review concepts

- `spec/pathway.schema.yaml` now includes review aliases, review metadata, record-review alignment notes, and additional lifecycle review concepts
- `docs/checker-coverage.md` now records that the schema and record-review guide are aligned, while the checker has not yet been expanded to validate every record-review field
- The alignment remains structural and non-certifying, and does not add legal, safety, compliance, fairness, moral-resolution, certification, or production-readiness claims

### Japanese README and BEACON synchronized with enterprise review guides

- README.ja now links to the enterprise implementation profile and Responsibility Pathway record review guide
- BEACON now records Phase 2.5 enterprise guidance and the plain-language record review guide in the current position, read-first path, current focus, and restart point
- The synchronization keeps enterprise guidance and record review bounded, structural, and non-certifying

### Responsibility Pathway record review added

- `docs/responsibility-pathway-record-review.md` added as a plain-language review and recheck guide for Responsibility Pathway records
- The guide uses accessible terms such as record, review, recheck, review result, review tool, evidence record, repair record, and reopening condition
- The guide defines what can be structurally checked and what must not be claimed from a successful review
- README, ROADMAP, and the enterprise implementation profile now link to the record review guide
- The guide adds no legal, safety, compliance, fairness, moral-resolution, certification, or production-readiness claims

### Enterprise implementation profile added

- `docs/enterprise-implementation-profile.md` added as a minimal enterprise adoption bridge
- The profile distinguishes the minimal formal core from production verifiers, legal certification systems, compliance engines, fairness certification tools, and safety certification tools
- The profile documents layer separation across formal core, specification layer, checker layer, workflow layer, evidence layer, and governance layer
- ROADMAP now includes Phase 2.5 as an enterprise implementation bridge before larger reference implementations
- README now links to the enterprise implementation profile in the reader path

### ROADMAP phase status wording aligned

- Phase 1.6 remaining tasks were updated to maintenance wording for bounded checker stability and small readable examples
- Phase 2 heading now reflects the current snapshot and theorem index alongside the Lean core split and build path
- This is a documentation alignment only and adds no new formal claims

### Lean README synchronized with Phase 2 current snapshot

- `formal/lean/README.md` now links to `docs/phase-2-current-snapshot.md`
- The Lean README now points to the current snapshot, split plan, and theorem-role index together
- This completes the current snapshot reader path across README, README.ja, BEACON, ROADMAP, CHANGELOG, and `formal/lean/README.md`

### ROADMAP synchronized with Phase 2 current snapshot

- ROADMAP now references `docs/phase-2-current-snapshot.md` in the current Phase 2 status
- Next low-risk Phase 2 work now says to use the current snapshot and theorem-role index before adding or renaming Lean theorem candidates
- Traceability wording now includes the current snapshot alongside examples, schemas, checker boundaries, Lean definitions, theorem roles, and excluded claims

### Phase 2 current snapshot added

- `docs/phase-2-current-snapshot.md` added as a stable reconnection document for the current Phase 2 Lean position
- README and README.ja now link to the current snapshot in the Phase 2 Lean reader path
- BEACON now records the current snapshot as part of the Phase 2 Lean reconnection path
- The snapshot records module layout, build path, theorem categories, current invariant candidates, non-certifying boundaries, next allowed work, and stop conditions

### Invariants Lean file aligned with theorem-role index

- `formal/lean/ResponsibilityPathway/Invariants.lean` now includes section comments for boundary predicates, positive invariant theorem candidates, and vacuity/non-trigger theorem candidates
- The comments align the file layout with `docs/phase-2-lean-theorem-index.md`
- No theorem statements or formal claims were expanded by this documentation-only Lean update

### ROADMAP synchronized with Lean theorem index

- ROADMAP now records constructor-level sanity theorem coverage for Basic and Examples modules
- ROADMAP now references `docs/phase-2-lean-theorem-index.md` as the theorem-role guide before further theorem expansion
- Next low-risk Phase 2 work now includes using the theorem-role index before adding or renaming Lean theorem candidates

### BEACON synchronized with Lean theorem index

- BEACON now records `docs/phase-2-lean-theorem-index.md` as part of the Phase 2 Lean reconnection path
- Current Focus now says to use the theorem-role index before adding or renaming Lean theorem candidates
- Restart Point now includes theorem-role stability as a condition before adding further theorem candidates

### Lean theorem index linked from README files

- README and README.ja now include `docs/phase-2-lean-theorem-index.md` in the Phase 2 Lean reader path
- `formal/lean/README.md` now links to the theorem-role index near the split-plan link
- This completes the previously deferred README synchronization for the theorem index

### Phase 2 Lean theorem index added

- `docs/phase-2-lean-theorem-index.md` added as a navigation aid for current Lean theorem roles
- The index groups Basic constructor sanity theorems, Example lifecycle sanity theorems, boundary predicates, positive invariant theorem candidates, and vacuity/non-trigger theorem candidates
- The index adds no new formal claims and remains non-certifying

### Phase 2 example lifecycle sanity theorems added

- `formal/lean/ResponsibilityPathway/Examples.lean` updated with constructor-level sanity theorems for lifecycle examples
- Added checks for AI participation and return-point fields in the safe AI-assisted example
- Added checks for non-AI participation, repaired/record, suspended/review-or-return, returning/no-automatic-continuation, and closed/evidence/reopening constructor examples
- These are structural model facts only; they do not certify legal validity, safety, compliance, fairness, moral accountability resolution, institutional certification, or production readiness

### Phase 2 basic node sanity theorems added

- `formal/lean/ResponsibilityPathway/Basic.lean` updated with constructor-level sanity theorems for basic node definitions
- Added theorem candidates showing that a safe AI node is an AI node and cannot hold final responsibility by construction
- Added theorem candidates showing that human and institutional responsibility nodes can hold final responsibility by construction
- These are structural model facts only; they do not certify legal validity, safety, compliance, fairness, moral accountability resolution, institutional certification, or production readiness

### Lean workflow generates Lake manifest before build

- `.github/workflows/check-lean.yml` updated after the first workflow attempt reported `No lake-manifest.json found`
- The workflow now installs Elan directly, prints Lean/Lake versions, runs `lake update`, and then runs `lake build`
- This avoids requiring a precommitted `lake-manifest.json` for the current dependency-free minimal Lean package

### Lean workflow inputs made explicit

- `.github/workflows/check-lean.yml` updated to use explicit `leanprover/lean-action@v1` inputs
- `auto-config` is set to `false`
- `build`, `test`, `lint`, and `use-mathlib-cache` are set explicitly as string inputs
- This keeps the minimal Lean CI focused on `lake build` only

### Phase 2 minimal Lean build path added

- `lean-toolchain` added and pinned to `leanprover/lean4:v4.30.0`
- `lakefile.lean` added as a minimal Lake package using `formal/lean` as the Lean source directory
- `.github/workflows/check-lean.yml` added as a minimal Lean build workflow using `leanprover/lean-action@v1`
- README, README.ja, ROADMAP, BEACON, and `formal/lean/README.md` updated to reflect the minimal Lean build path
- The workflow checks only the Lean package build; it does not certify legal validity, safety, compliance, fairness, moral accountability resolution, institutional certification, or production readiness

### Phase 2 Lean core split documented across entry files

- README and README.ja now state that the Phase 2 Lean spine is split into small modules while `Core.lean` remains the stable entry point
- ROADMAP now records the Lean core split as completed and lists minimal Lean toolchain/build verification as the next low-risk Phase 2 work
- BEACON now records the split module layout, the current restart point, and the fact that Lean build verification is not yet established
- Current GitHub Actions automation remains limited to the bounded Python example checker

### Phase 2 Lean core split into small modules

- `formal/lean/ResponsibilityPathway/Core.lean` reduced to a stable import entry point
- New split modules added: `Basic.lean`, `Lifecycle.lean`, `Examples.lean`, and `Invariants.lean`
- The existing six Phase 2 invariant candidates were preserved while separating model primitives, lifecycle predicates, constructor examples, and theorem candidates
- `docs/phase-2-lean-split-plan.md` records the split rationale, order, stop conditions, and non-goals
- `formal/lean/README.md` updated to describe the split module layout
- No new legal, safety, compliance, fairness, moral accountability, certification, or production-readiness claims were introduced

### Phase 2 minimal Lean lifecycle invariant set introduced

- `formal/lean/ResponsibilityPathway/Core.lean` now contains a minimal node/pathway model and six scoped lifecycle-invariant candidates
- The current invariant set covers AI final-responsibility boundary, AI return-point boundary, repair-record boundary, suspension review/return boundary, returning no-automatic-continuation boundary, and closure evidence/reopening boundary
- The AI final-responsibility boundary is explicitly assumption-scoped to the current minimal model where no artificial legal-personhood layer is assumed
- Future legal, institutional, national, international, or user/provider-agreement personhood layers remain open for explicit modeling rather than silent assumption
- README, README.ja, ROADMAP, and BEACON updated to reflect the current Phase 2 Lean status
- The formalization remains structural, assumption-bound, and non-certifying; it does not claim legal validity, safety, compliance, fairness, moral accountability resolution, institutional certification, or production readiness

### Phase 2 closure evidence-reopening invariant established

- `formal/lean/ResponsibilityPathway/Core.lean` updated with closed-pathway structural fields
- `IsClosedPathway`, `HasEvidenceRecord`, `HasReopeningCondition`, and `ClosureEvidenceReopeningBoundary` predicates added
- Sixth invariant candidate added: a safely constructed closed pathway preserves evidence and reopening-condition records
- Non-closed pathway implication case added to show the closure-specific boundary is not over-applied
- `formal/lean/README.md` updated with the current closure evidence/reopening invariant candidate and boundary note

### Phase 2 returning no-automatic-continuation invariant established

- `formal/lean/ResponsibilityPathway/Core.lean` updated with returning-pathway structural fields
- `IsReturningPathway`, `AllowsAutomaticContinuation`, and `ReturningNoAutomaticContinuationBoundary` predicates added
- Fifth invariant candidate added: a safely constructed returning pathway does not allow automatic continuation
- Non-returning pathway implication case added to show the returning-specific boundary is not over-applied
- `formal/lean/README.md` updated with the current returning no-automatic-continuation invariant candidate and boundary note

### Phase 2 suspension review-return invariant established

- `formal/lean/ResponsibilityPathway/Core.lean` updated with suspended-pathway structural fields
- `IsSuspendedPathway`, `HasReviewOrReturnCondition`, and `SuspensionReviewReturnBoundary` predicates added
- Fourth invariant candidate added: a safely constructed suspended pathway preserves review or return conditions
- Non-suspended pathway implication case added to show the suspension-specific boundary is not over-applied
- `formal/lean/README.md` updated with the current suspension review/return invariant candidate and boundary note

### Phase 2 repair-record invariant established

- `formal/lean/ResponsibilityPathway/Core.lean` updated with repaired-pathway structural fields
- `IsRepairedPathway`, `HasRepairRecord`, and `RepairRecordBoundary` predicates added
- Third invariant candidate added: a safely constructed repaired pathway has a repair record
- Non-repaired pathway implication case added to show the repair-specific boundary is not over-applied
- `formal/lean/README.md` updated with the current repair-record invariant candidate and boundary note

### Phase 2 AI responsibility invariant assumption boundary clarified

- `formal/lean/ResponsibilityPathway/Core.lean` updated with `ModelAssumptions` and `NoArtificialLegalPersonhood`
- The AI final-responsibility invariant is now scoped to the current minimal model where no artificial legal-personhood layer is assumed
- The theorem name was updated to `safe_ai_node_cannot_hold_final_responsibility_under_current_assumptions`
- The formalization now explicitly leaves room for future legal, institutional, national, international, or user/provider-agreement models that may introduce artificial legal-personhood layers
- `formal/lean/README.md` updated to clarify that the invariant is not a universal claim about all possible future legal or institutional regimes

### Phase 2 AI return-point invariant established

- `formal/lean/ResponsibilityPathway/Core.lean` updated with a minimal `Pathway` model
- `HasAIParticipation`, `HasHumanOrInstitutionalReturnPoint`, and `AIReturnPointBoundary` predicates added
- Second invariant candidate added: a safely constructed AI-assisted pathway has a human or institutional return point
