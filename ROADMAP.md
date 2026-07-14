# ROADMAP

## Phase 0 - Foundation (Completed)

- README
- README.ja
- BEACON
- LUMINALIA
- CHANGELOG
- Repository governance
- Development process
- ADR structure
- Lessons structure
- Definition
- Eight Elements
- Core YAML
- Lean scaffold

## Phase 1 - Concept Models (Substantially Established)

- Runtime Model
- Responsibility Node
- Return Point
- Human Return Point boundary
- Value Flow
- Cost Flow
- Repair Model
- Stop Authority
- Evidence Log
- Action Class Matrix
- Approval Gate
- Decision Owner
- Source Mapping from public articles to canonical repository definitions

## Phase 1.5 - Specification Binding (Established; action-class schema refreshed)

- Core YAML specification expanded to v0.2.0
- Concept documents aligned with initial machine-readable specification
- Minimal schema split established under `spec/`
- Validation-oriented fields defined for nodes, roles, lifecycle, action classes, evidence, return points, repair, and pathway composition
- Schema cross-reference notes added
- Validation checklist documentation added
- Initial minimal examples added
- README, README.ja, CHANGELOG, and BEACON maintained at milestones
- `spec/action-class.schema.yaml` updated to v0.2.0 with source-aligned Class A-F structure while retaining earlier Class 0-4 values as historical mapping references

Established schema files:

- spec/node.schema.yaml
- spec/action-class.schema.yaml
- spec/return-point.schema.yaml
- spec/evidence-log.schema.yaml
- spec/repair.schema.yaml
- spec/pathway.schema.yaml

## Phase 1.6 - Lightweight Validation and Lifecycle Examples (Substantially Established; action-class and missed-support alignment in progress)

- Lightweight checker added at `scripts/check_examples.py`
- GitHub Actions workflow added for bounded example checks
- Validator boundary documented in `docs/validator-boundary.md`
- Checker coverage documented in `docs/checker-coverage.md`
- Minimal core rationale documented in `docs/minimal-core-rationale.md`
- Lifecycle example coverage established for:
  - `originating`
  - `repaired`
  - `suspended`
  - `returning`
  - `closed`
- Example index updated
- Example review notes updated
- README and README.ja reader paths updated
- CHANGELOG milestones recorded
- Action Class Matrix source-aligned from earlier Class 0-4 form to Class A-F form in `docs/action-class-matrix.md`
- `docs/concepts/core-elements.md` clarified as operational roles and controls connected to the eight-element model, not a replacement for the eight-element model
- `examples/minimal-pathway.yaml` migrated from legacy Class 1 Internal Assistive to source-aligned Class B Suggest-Only with legacy mapping preserved
- `examples/action-class-matrix-minimal.yaml` added as a classification-only fixture for Class A-F reading before higher-impact examples
- `examples/internal-document-update.yaml` added as a Class C Approval-Required internal document update example
- `examples/emergency-stop-flow.yaml` added as a Class F Emergency Stop / stop-and-await example
- `examples/reversible-external-action.yaml` added as a Class D Reversible External Action example with external-impact visibility and rollback/correction path
- `docs/concepts/support-call-policy.md` added as a concept-level mapping from support-call policy to Decision Owner, Human Return Point, Approval Gate, Stop Authority, Evidence Log, and Repair Owner
- `docs/concepts/missed-support-review-signal.md` added to define missed support as a structural review signal, not automatic fault determination or certification
- `examples/missed-support-boundary-minimal.yaml` added as a boundary-only repository-maintenance example with `lifecycle_state: returning`
- `docs/examples/missed-support-workflow-observation.md` records the observed failed-then-passing example-check sequence for the missed-support example
- `docs/examples/missed-support-current-status.md` records the current missed-support reader path, checker boundary, and still-deferred schema/checker/runtime/Lean work
- `docs/concepts/index.md` added as a concept reader-path index
- `docs/example-index.md` connected future examples to Action Class Matrix design rules and includes the missed-support boundary example
- `docs/checker-coverage.md` documented action-class-specific checks and support-call/missed-support checks as planned future bounded checks, not current semantic enforcement
- `Check examples #10` observed green on commit `2af698c` on `main` after minimal-pathway action-class migration
- `Check examples #11` observed green on commit `b50226d` on `main` after adding `examples/action-class-matrix-minimal.yaml`; the workflow completed successfully in about 14 seconds, and the `Bounded structural example checks` job completed successfully in about 10 seconds
- `Check examples #12` observed green on commit `fdd7bd4` on `main` after adding `examples/internal-document-update.yaml`; the workflow completed successfully in about 9 seconds, and the `Bounded structural example checks` job completed successfully in about 7 seconds
- `Check examples #13` observed green on commit `266845b` on `main` after adding `examples/emergency-stop-flow.yaml`; the workflow completed successfully in about 10 seconds, and the `Bounded structural example checks` job completed successfully in about 7 seconds
- `Check examples #14` observed green on commit `caf285b` on `main` for the Class D reversible external action fixture
- `Check examples #17` observed failed on commit `57445b1` because the missed-support example declared `lifecycle_state: returning` without a top-level `returning` block
- `Check examples #18` observed green on commit `f63678c` after adding the top-level `returning` block to the missed-support example

Phase 1.6 rule:

Lifecycle-aware, action-class-aware, and support-call-related checks remain bounded structural maintenance checks unless deliberately expanded later. They do not certify examples, systems, legal validity, safety, compliance, fairness, moral resolution, production readiness, support-call correctness, missed-support correctness, or real-world responsibility resolution.

Remaining Phase 1.6 maintenance tasks:

- maintain bounded checker stability after the Class D reversible external action fixture and missed-support boundary example
- keep examples small and manually readable
- keep support-call and missed-support fields concept-level or example-level unless schema work is explicitly reopened
- keep action-class-specific checker additions optional until examples are deliberately migrated
- avoid adding higher-impact examples until lifecycle, action-class, and missed-support boundaries remain stable

## Phase 2 - Formalization (Started; minimal lifecycle invariant set reached; Lean core split, build path, theorem index, and current snapshot added)

- Lean invariants
- State transitions
- Path semantics
- Returnability invariants
- Stop authority invariants
- Evidence sufficiency boundaries
- Repair preconditions
- Suspension boundary invariants
- Returning boundary invariants
- Closure and reopening-condition invariants

Current Phase 2 status:

- `formal/lean/ResponsibilityPathway/Core.lean` is now a stable import entry point
- the Lean spine has been split into `Basic.lean`, `Lifecycle.lean`, `Examples.lean`, and `Invariants.lean`
- six scoped lifecycle-invariant candidates have been preserved after the split
- constructor-level sanity theorems now cover basic node definitions and lifecycle examples
- `docs/phase-2-current-snapshot.md` records the current stable Phase 2 Lean snapshot and restart point
- `docs/phase-2-lean-theorem-index.md` groups current theorem roles before further theorem expansion
- `lean-toolchain` pins the minimal Lean toolchain
- `lakefile.lean` defines a minimal Lake package using `formal/lean` as the source directory
- `.github/workflows/check-lean.yml` defines a minimal Lean build workflow using `lake build`
- `formal/lean/README.md` records the formalization boundary, current invariant set, module layout, build path, theorem summaries, and evidence / approval structural-completeness planning route
- `docs/lean-evidence-approval-formalization-plan.md` records the planning boundary for possible future Evidence Log completeness, approval-skip, approval-transfer, correction-record, and later-return-path theorem work
- `docs/phase-2-lean-split-plan.md` records the split rationale, order, stop conditions, and non-goals
- README, README.ja, and BEACON summarize the current Phase 2 Lean status

Formalization rule:

Formal proofs must remain bounded to explicit definitions, assumptions, and modeled scope.

Current invariant candidates:

- AI final-responsibility boundary under current minimal assumptions
- AI-assisted pathway preserves a human or institutional return point
- repaired pathway references a repair record
- suspended pathway preserves review or return conditions
- returning pathway does not imply automatic continuation
- closed pathway preserves evidence and reopening-condition records

AI final-responsibility boundary note:

The current AI final-responsibility invariant is assumption-scoped. In the current minimal RPE model, no artificial legal-personhood layer is assumed, so an AI node is not treated as a final responsibility holder. Future legal, institutional, national, international, or user/provider-agreement layers must be modeled explicitly if introduced.

Next low-risk Phase 2 work:

- do not expand Lean around Action Class Matrix until the source-aligned Class A-F examples, schema, checker boundary, and validation checklist are stable
- do not expand Lean around support-call policy or missed-support signals until examples, schema conventions, checker boundaries, and review-signal semantics are stable
- do not expand Lean around Evidence Log completeness, approval skip, approval transfer, correction records, or later return paths without first using `docs/lean-evidence-approval-formalization-plan.md`
- observe the next Lean workflow result and adjust only if the minimal build path fails
- use the current snapshot, theorem-role index, and evidence / approval formalization plan before adding or renaming theorem candidates
- keep formalization incremental and assumption-explicit
- maintain traceability among examples, schemas, checker boundaries, Lean definitions, theorem roles, current snapshot, planning notes, and excluded claims

## Phase 2.5 - Enterprise Implementation Profile (Stable bridge checkpoint reached)

- Enterprise implementation profile added at `docs/enterprise-implementation-profile.md`
- Responsibility Pathway record review guide added at `docs/responsibility-pathway-record-review.md`
- Phase 2.5 current snapshot added at `docs/phase-2-5-current-snapshot.md`
- Phase 2.5 stable checkpoint recorded in `docs/phase-2-5-current-snapshot.md`
- Minimal record-review example added at `examples/record-review-minimal.yaml`
- Minimal review-result fixture added at `fixtures/review-results/record-review-result-minimal.yaml`
- Review-result schema added at `spec/review-result.schema.yaml`
- Review-result schema/fixture alignment note added at `docs/review-result-schema-fixture-alignment.md`
- Bounded review-result checker added at `scripts/check_review_results.py`
- GitHub Actions workflow added at `.github/workflows/check-review-results.yml`
- `Check review-result fixtures` workflow observed green for run `#1` on commit `aaaece3` on `main`
- Validator boundary updated to include both pathway-example checks and review-result fixture checks
- Optional review metadata checks added to `scripts/check_examples.py`
- Layer separation documented for formal core, specification layer, checker layer, workflow layer, evidence layer, and governance layer
- Plain-language review and recheck process documented for Responsibility Pathway records
- Minimal enterprise adoption path documented before larger reference implementations
- Initial enterprise implementation candidates identified without claiming certification, legal validity, compliance, fairness, safety, moral resolution, or production readiness
- Action-class-specific checker additions remain optional and bounded unless deliberately integrated with pathway examples and review-result fixtures

Phase 2.5 rule:

Enterprise adoption guidance, record review guidance, review-result schema, review-result fixtures, bounded checkers, and observed green workflow status must remain structural and non-certifying. They must not treat RPE as a production verifier, legal decision system, compliance engine, safety certification tool, fairness certification tool, moral-resolution engine, or replacement for accountable humans and institutions.

Next low-risk Phase 2.5 work:

- maintain the stable checkpoint without expanding claims
- keep review-result fixture checks separate from pathway example checks unless deliberately integrated
- keep checker additions optional unless existing examples are deliberately migrated
- keep review-result schema validation and fixture checking bounded to structural responsibility-boundary preservation
- keep review results structural and non-certifying
- keep action-class-specific coverage documented as planned future work until examples and schema fields are stable

## Phase 3 - Reference Implementations (First bounded example reached; action-class classification baseline added)

- Reference implementation boundary added at `docs/reference-implementation-boundary.md`
- First small Phase 3 reference example added at `examples/human-ai-review-workflow-minimal.yaml`
- `Check examples #9` observed green on commit `d4e467a` on `main` for the bounded structural example checks
- YAML extensions
- Example workflows
- Multi-agent examples
- Human Return Point example
- Evidence Log example
- Approval Gate example
- Repair flow example
- Suspension flow example
- Returning flow example
- Closure and reopening flow example
- Action Class Matrix classification-only baseline added at `examples/action-class-matrix-minimal.yaml`
- `Check examples #11` observed green on commit `b50226d` on `main` for the Action Class Matrix classification-only fixture
- Class C internal document update example added at `examples/internal-document-update.yaml`
- `Check examples #12` observed green on commit `fdd7bd4` on `main` for the Class C internal document update fixture
- Class F emergency stop flow example added at `examples/emergency-stop-flow.yaml`
- `Check examples #13` observed green on commit `266845b` on `main` for the Class F emergency stop flow fixture
- Class D reversible external action example added at `examples/reversible-external-action.yaml`
- `Check examples #14` observed green on commit `caf285b` on `main` for the Class D reversible external action fixture
- Missed-support boundary example added at `examples/missed-support-boundary-minimal.yaml` as a repository-maintenance boundary-only example
- `Check examples #18` observed green on commit `f63678c` on `main` for the missed-support boundary example after adding a `returning` block

Implementation rule:

Reference implementations must not outrun definitions, examples, checker boundaries, formalization assumptions, enterprise governance boundaries, Responsibility Pathway record review boundaries, validator boundaries, review-result boundaries, action-class boundaries, support-call boundaries, missed-support review-signal boundaries, or excluded claims.

First recommended Phase 3 step:

- keep the first human-AI review workflow example small, readable, bounded, and non-certifying before adding additional reference examples
- use `examples/action-class-matrix-minimal.yaml` as a classification baseline before adding Class C, Class D, Class E, or Class F examples

Next low-risk Phase 3 work:

- keep Class D reversible external examples small, correctable, and non-certifying
- treat Class E high-impact examples as negative or boundary-only examples until lower classes are stable
- keep support-call and missed-support examples boundary-only until semantics and checker boundaries are stable
- record source-alignment checkpoints before expanding reference examples
- reread prior Zenn articles for definition, claim, and boundary alignment
- add only one small reference example at a time
- avoid production-service, legal-decision, certification, compliance, fairness, moral-resolution, or AI-final-responsibility interpretations

## Phase 3.1 - Adapter Boundary and Runtime Event Bridge (Bounded bridge checkpoint reached; checker and workflow observed)

Purpose:

Define the bridge from external logs, API events, workflow results, and runtime observations into Responsibility Pathway records without treating that bridge as a production connector, verifier, certification tool, legal decision system, or AI final-responsibility transfer mechanism.

Current artifacts and companion notes:

- `docs/adapter-boundary.md` defines what adapters may do, what they must not claim, human review requirements, evidence logging requirements, missing-context handling, and relationship to the Action Class Matrix
- `spec/runtime-event.schema.yaml` defines a minimal input event shape before service-specific connectors exist
- `examples/adapter-input-event-minimal.json` provides a small synthetic runtime event input
- `examples/minimal-synthetic-runtime-fixture.json` provides a selected minimal synthetic runtime observation fixture for reading and review
- `examples/runtime-event-to-pathway-minimal.yaml` shows how a runtime event can be represented as a Responsibility Pathway record pending human or institutional review
- `scripts/check_runtime_events.py` provides bounded structural checks for selected synthetic JSON fixtures
- `.github/workflows/check-runtime-events.yml` runs the bounded runtime-event checker for selected fixture and checker changes
- `docs/runtime-event-checking-plan.md` defines current checks, future checks, preconditions, exclusions, and non-certifying boundaries
- `docs/runtime-event-schema-fixture-alignment.md` records the current structural alignment between draft schema, selected JSON fixtures, and bounded checker without treating alignment as validation
- `docs/event-to-pathway-relation-checker-plan.md` records planned future local structural relation-checker boundaries between selected runtime-event JSON fixtures and pathway YAML examples before any implementation
- `docs/social-connection-review-navigation.md` records the focused reader path for social-connection review when approval skip, responsibility transfer, Evidence Log, explanation paths, affected-party visibility, or later return paths matter
- `docs/repository-pathway-gap-inventory.md` records reader-path gaps, structure-break risks, deferred connection return rules, and safe next connection points
- `docs/evidence-approval-transfer-alignment.md` records the relation between approval skip, evidence logging, responsibility transfer, social-connection exceptions, and later return paths
- `docs/lean-evidence-approval-formalization-plan.md` records the planning route before any Lean evidence / approval theorem work
- `docs/zenn-publication-readiness-connection.md` records the repo-side public reader path for Zenn readiness while article titles and article routes remain separate
- `docs/runtime-event-workflow-current-status.md` records observed runtime-event workflow status
- `docs/minimal-runtime-fixture-checker-workflow-observation.md` records the focused observation for run `27607798655`
- `docs/phase-3-1-minimal-runtime-fixture-checker-connection.md` records the reader path for the minimal runtime fixture checker expansion and workflow observation
- `docs/phase-3-1-minimal-runtime-fixture-checker-sync-note.md` supplements the long sync log for the minimal runtime fixture checker workflow observation responsibility unit
- `docs/phase-3-1-current-snapshot.md` records the current Phase 3.1 restart point
- `docs/phase-3-1-sync-log.md` records the staged synchronization work for Phase 3.1
- `docs/phase-3-1-roadmap-note.md` records the short roadmap companion for this phase
- `docs/phase-3-1-repository-alignment-audit.md` records the current repository alignment audit and remaining cleanup candidates
- `docs/repository-operation-model.md` records the repository-wide staged update operation, document roles, commit granularity policy, periodic operation review policy, workflow observation policy, checker interpretation policy, long-file update policy, log organization policy, non-certifying operation boundaries, and restart rules
- `docs/operation-index.md` records which operation-related document to read for each maintenance situation
- `docs/operation-tool-selection-guard.md` records a guard for choosing the correct GitHub read/write tool during AI-assisted maintenance
- `docs/readme-expanded.md` preserves the previous expanded README after root README lightweight recovery
- `docs/concepts/index.md` records the concept-level reader path, including support-call and missed-support notes
- [Published RPE Artifact Catalog](https://yutorikomeiji.github.io/responsibility-pathway-engineering/) provides the browser-friendly first-reader orientation path.

Observed status:

- `Check examples #16` observed green on commit `d377be2` on `main` after fixing `examples/runtime-event-to-pathway-minimal.yaml`
- the GitHub Actions run was `27463999395`
- `Check runtime events` observed green on run `27501847137` for the first minimal runtime-event workflow
- `Check runtime events` observed green on run `27607798655` after `examples/minimal-synthetic-runtime-fixture.json` was added to bounded runtime-event checker coverage
- all observed green statuses remain bounded repository-maintenance checks and are not certification
- root `README.md` was shortened and then strengthened after GitHub mobile app rendering appeared blank while the file remained readable through GitHub API

Adapter rule:

Adapters may extract, normalize, summarize, classify, or transform external event data into Responsibility Pathway records. They must not decide responsibility, approve actions, certify records, prove safety, prove compliance, resolve legal or moral responsibility, or transfer final responsibility to AI.

Runtime-event bridge rule:

A generated pathway record must remain reviewable. It should preserve source event references, uncertainty, missing context, evidence records, human or institutional return points, approval requirements, stop conditions, and repair or correction paths where relevant.

Repository operation rule:

Broad reader-path synchronization, long-file updates, snapshot updates, operation-index updates, changelog or roadmap synchronization, and periodic operation review should follow `docs/repository-operation-model.md`.

Runtime-event checking rule:

The current runtime-event checker and workflow may be maintained as bounded repository-maintenance tools for selected synthetic JSON fixtures only.

Any passing runtime-event check must remain a bounded repository-maintenance signal only.

A passing runtime-event check must not be interpreted as certification, legal review, safety review, compliance review, fairness review, production approval, connector correctness proof, adapter correctness proof, schema correctness proof, JSON fixture correctness proof, semantic mapping correctness proof, responsibility assignment proof, conformance evidence, or AI final-responsibility transfer.

Event-to-pathway relation checker planning rule:

`docs/event-to-pathway-relation-checker-plan.md` may be maintained as a future local structural checker plan for selected runtime-event JSON fixtures and pathway YAML examples.

It is not current checker behavior and does not authorize implementation by itself.

Any future relation checker must remain local, structural, selected-fixture-only, non-certifying, and preconditioned by the plan before implementation.

Social-connection and publication-readiness rule:

Social-connection review, evidence / approval-transfer alignment, gap inventory, Zenn readiness connection, and published Pages reader paths are reader-path and planning layers only.

They do not authorize schema, checker, workflow, runtime, connector, conformance, Lean implementation, certification, legal review, safety review, compliance review, fairness review, social acceptance claim, production approval, or AI final-responsibility transfer.

Next low-risk Phase 3.1 work:

- keep service-specific connectors deferred
- keep production conversion code deferred
- keep production runtime integration deferred
- keep runtime-event schema checking deferred until the schema and examples remain stable
- keep broader JSON schema-fixture checking deferred until the current event-to-pathway bridge remains readable and reviewable
- keep event-to-pathway relation checker implementation deferred until `docs/event-to-pathway-relation-checker-plan.md` preconditions are deliberately reviewed
- keep event-to-pathway semantic checking deferred
- keep `docs/runtime-event-schema-fixture-alignment.md`, `docs/event-to-pathway-relation-checker-plan.md`, `docs/checker-coverage.md`, `docs/example-index.md`, current snapshot, current task inventory, and operation index aligned when fixture, checker, or relation-checker planning interpretation changes
- keep `docs/social-connection-review-navigation.md`, `docs/repository-pathway-gap-inventory.md`, `docs/evidence-approval-transfer-alignment.md`, `docs/lean-evidence-approval-formalization-plan.md`, and `docs/zenn-publication-readiness-connection.md` aligned when review-navigation, deferred-gap, formalization-planning, or repo-side publication-readiness paths change
- use `docs/runtime-event-checking-plan.md` before considering runtime-event checker expansion or runtime-event workflow expansion
- use `docs/event-to-pathway-relation-checker-plan.md` before considering any future relation checker between selected runtime-event JSON fixtures and pathway YAML examples
- use `docs/repository-pathway-gap-inventory.md` before retrying deferred direct reader-path connections
- keep article drafting and title routes separate from repo-side Zenn readiness unless deliberately reopened
- keep published Pages reader paths aligned if Example browser or Template helper pages are added
- keep Class E positive examples deferred
- keep support-call and missed-support runtime-event fields deferred until concept notes, examples, schema conventions, and checker boundaries are stable
- keep Lean expansion around adapter, runtime events, support-call policy, missed-support signals, Evidence Log completeness, approval skip, approval transfer, correction records, or later return paths deferred until the relevant boundary notes and formalization plans are stable
- maintain `docs/operation-index.md` when operation documents, snapshots, sync logs, roadmap notes, checker plans, alignment notes, social-connection review paths, gap inventories, formalization plans, publication-readiness connections, or concept navigation change
- use periodic operation review when commit granularity, reader paths, logs, roadmap notes, checker interpretation, social-connection boundaries, or deferred boundaries feel misaligned with actual practice
- add only short ROADMAP or CHANGELOG references after the detailed state has a stable snapshot, sync log, roadmap note, checker plan, alignment note, or operation document to point to

## Guiding Principle

Small commits.
Verified definitions.
Incremental formalization.

Definitions precede proofs.
Proofs precede claims.
Claims precede applications.
