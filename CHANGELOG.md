# CHANGELOG

This changelog records conceptual milestones rather than individual code edits.

## 2026-06

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
- Non-AI pathway implication case added to show the AI-specific boundary is not over-applied
- `formal/lean/README.md` updated with the current return-point invariant candidate

### Phase 2 Lean formalization started

- `formal/lean/ResponsibilityPathway/Core.lean` added as the first Phase 2 Lean formalization file
- Minimal `NodeKind` and `Node` structures added for early structural invariants
- First invariant candidate added: a safely constructed AI node cannot hold final responsibility
- `formal/lean/README.md` updated with current files, invariant candidates, and formalization boundary
- `ROADMAP.md` updated to mark Phase 2 as started and to record the current Lean invariant candidate

### Phase 1.6 status alignment established

- `docs/phase-1-6-plan.md` updated from planned work to current status, established work items, completion condition, and restart point
- `ROADMAP.md` updated to mark Phase 1.5 as established and Phase 1.6 as substantially established
- `BEACON.md` updated with current Phase 1.6 position, lifecycle-example coverage, checker boundary, read-first order, and Phase 2 restart point

### Phase 1.6 minimal core rationale established

- `docs/minimal-core-rationale.md` added to explain why the repository is intentionally small and specification-first
- The rationale distinguishes a minimal responsibility-preserving core from production applications, governance automation platforms, legal decision systems, certification tools, and moral accountability engines
- The rationale states that growth should preserve returnability from claims to definitions, examples, schemas, checker boundaries, excluded claims, and assumptions
- `README.md` and `README.ja.md` updated with minimal-core rationale links in the status section and reader path

### Phase 1.6 checker coverage documentation established

- `docs/checker-coverage.md` added to summarize current `scripts/check_examples.py` coverage
- Coverage documentation lists general checks, lifecycle-aware checks, current example coverage map, and interpretation boundary
- `README.md` and `README.ja.md` updated to link to checker coverage from the reader path and lightweight-checks section

### Phase 1.6 full lifecycle checker coverage established

- `scripts/check_examples.py` updated with bounded lifecycle rules for `originating` and `repaired` examples
- Originating examples are checked for human decision-owner and stop-authority capacity, empty repair records, and human return-point signals
- Repaired examples are checked for repair-record presence, repair-owner responsibility capacity, repair trigger, repair state, and repair-boundary signals
- `docs/validator-boundary.md` updated to clarify that lifecycle-aware checks now cover `originating`, `repaired`, `suspended`, `returning`, and `closed` examples while remaining structural maintenance checks only

### Phase 1.6 lifecycle-aware checker established

- `scripts/check_examples.py` updated with lifecycle-aware bounded structural checks
- The checker now inspects declared lifecycle-specific blocks for `suspended`, `returning`, and `closed` examples
- Suspended examples are checked for suspension records, continuation and closure boundary signals, and disallowed-interpretation signals
- Returning examples are checked for returning records, prior lifecycle-state signal, automatic-continuation boundary signals, and disallowed-interpretation signals
- Closed examples are checked for closure records, closure basis, residual obligations, reopening conditions, automatic-closure boundary signals, and closure-specific excluded claims
- `docs/validator-boundary.md` updated to clarify that lifecycle-aware checks remain structural maintenance checks, not lifecycle correctness, legal, moral, safety, compliance, certification, or production-readiness judgments

### Phase 1.6 closed lifecycle example established

- `examples/closed-pathway.yaml` added as a minimal closed lifecycle-state example
- The closed example distinguishes closure from erasure, immunity, repair completion, certification, safety, compliance, legal validity, moral resolution, and production readiness
- Closure records evidence, closure basis, residual obligations, reopening conditions, and excluded claims rather than removing responsibility history
- `docs/example-index.md` updated with closed-pathway purpose, boundary, reading order, naming convention, and future lifecycle-example notes
- `docs/example-review-notes.md` updated with bounded review notes for the closed example
- `README.md` and `README.ja.md` updated with closed example links

### Phase 1.6 returning lifecycle example established

- `examples/returning-pathway.yaml` added as a minimal returning lifecycle-state example
- The returning example distinguishes return from automatic continuation, repair completion, closure, certification, safety, compliance, legal validity, moral resolution, and production readiness
- `docs/example-index.md` updated with returning-pathway purpose, boundary, reading order, naming convention, and future lifecycle-example notes
- `docs/example-review-notes.md` updated with bounded review notes for the returning example
- `README.md` and `README.ja.md` updated with returning example links

### Phase 1.6 suspended lifecycle example established

- `examples/suspended-pathway.yaml` added as a minimal suspended lifecycle-state example
- The suspended example distinguishes suspension from repair completion, closure, certification, safety, compliance, legal validity, and production readiness
- `docs/example-index.md` updated with suspended-pathway purpose, boundary, reading order, naming convention, and future lifecycle-example notes
- `docs/example-review-notes.md` updated with bounded review notes for the suspended example
- `README.md` and `README.ja.md` updated with suspended example links

### Phase 1.6 lightweight validation boundary established

- `scripts/check_examples.py` added as a bounded structural checker for example YAML files
- Checker output explicitly avoids certification, safety, compliance, fairness, legal, moral, and production-readiness claims
- `docs/validator-boundary.md` added to define what lightweight validation tools may and may not claim
- `requirements.txt` added with the minimal Python dependency for the example checker
- `.github/workflows/check-examples.yml` added to run bounded structural example checks on relevant changes
- `README.md` and `README.ja.md` updated with lightweight checker, setup command, run command, GitHub Actions workflow, and validator-boundary links

### Authorship clarification and Phase 1.6 entry established

- `AUTHORSHIP.md` added to clarify independent authorship, attribution, and repository-primary authorship information
- `AUTHORS.md` updated with independent affiliation signal and authorship clarification link
- `CITATION.cff` added as machine-readable citation metadata
- `README.md` and `README.ja.md` updated with author, independent repository affiliation, and authorship/citation links
- `docs/phase-1-6-plan.md` added as the next lightweight validation phase plan
- `README.md` and `README.ja.md` updated with Phase 1.6 plan links in the reader path

### Phase 1.5 examples, attribution, and reader path established

- `docs/schema-cross-reference.md` added to explain how the split schema files relate to each other
- `docs/validation-checklist.md` added as a bounded review guide for schema instances
- `examples/minimal-pathway.yaml` added as the first minimal Responsibility Pathway example
- `examples/repair-flow.yaml` added as the first minimal repair-flow example
- Japanese comments added to examples to support Japanese readers without changing schema keys
- `docs/example-index.md` added as an index and reading guide for current and future examples
- `docs/example-review-notes.md` added as initial bounded review notes for examples
- `README.md` and `README.ja.md` updated with schema-document, example, example-index, and example-review links
- `LICENSE` added under the MIT License
- Copyright notice standardized as `Akihisa Ono (小野昭久)`
- `NOTICE.md` added to clarify authorship, attribution, AI-assistance, derivative-use responsibility, and responsibility boundaries
- README license sections now link to `NOTICE.md`

### Phase 1.5 minimal schema split established

- Initial schema split completed under `spec/`
- `spec/node.schema.yaml` added
- `spec/action-class.schema.yaml` added
- `spec/return-point.schema.yaml` added
- `spec/evidence-log.schema.yaml` added
- `spec/repair.schema.yaml` added
- `spec/pathway.schema.yaml` added
- Responsibility Pathway can now be described as a composition of nodes, edges, roles, lifecycle state, evidence logs, return points, repairs, and responsibility boundaries
- Validation-oriented rules now exist for AI final responsibility boundary, stop/return references, repair records, evidence sufficiency, and high-impact action requirements

### v0.2.0 Concept model and specification binding

- Source mapping from public Zenn articles to canonical repository definitions added
- Runtime Model added
- Responsibility Node model added
- Return Point model added
- Repair Model added
- Value and Cost Flow model added
- Stop Authority model added
- Evidence Log model added
- Action Class Matrix added
- Approval Gate model added
- Decision Owner model added
- Core YAML specification expanded to version 0.2.0
- AI participation clarified as pathway-node participation, not final responsibility authorship
- Formalization boundary clarified: formal claims must remain bound to explicit definitions, assumptions, and model scope

### Foundation established

- Repository created
- README and README.ja added
- Responsibility Pathway definition published
- Eight-element model published
- Core YAML specification added
- Lean scaffold created
- BEACON established
- LUMINALIA philosophy established
- ROADMAP established
