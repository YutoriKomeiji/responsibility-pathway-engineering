# CHANGELOG

This changelog records conceptual milestones rather than individual code edits.

## 2026-06

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
- README and README.ja now link to the current snapshot in the Phase 2 reader path
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
