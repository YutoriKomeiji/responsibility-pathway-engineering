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

## Phase 1.6 - Lightweight Validation and Lifecycle Examples (Substantially Established; action-class alignment in progress)

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
- `docs/example-index.md` connected future examples to Action Class Matrix design rules
- `docs/checker-coverage.md` documented action-class-specific checks as planned future bounded checks, not current enforcement
- `Check examples #10` observed green on commit `2af698c` on `main` after minimal-pathway action-class migration

Phase 1.6 rule:

Lifecycle-aware and action-class-aware checks remain bounded structural maintenance checks. They do not certify examples, systems, legal validity, safety, compliance, fairness, moral resolution, production readiness, or real-world responsibility resolution.

Remaining Phase 1.6 maintenance tasks:

- observe the next `Check examples` workflow result after adding `examples/action-class-matrix-minimal.yaml`
- maintain bounded checker stability
- keep examples small and manually readable
- keep action-class-specific checker additions optional until examples are deliberately migrated
- avoid adding higher-impact examples until lifecycle and action-class boundaries remain stable

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
- `formal/lean/README.md` records the formalization boundary, current invariant set, module layout, build path, and theorem summaries
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
- observe the next Lean workflow result and adjust only if the minimal build path fails
- use the current snapshot and theorem-role index before adding or renaming Lean theorem candidates
- keep formalization incremental and assumption-explicit
- maintain traceability among examples, schemas, checker boundaries, Lean definitions, theorem roles, current snapshot, and excluded claims

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

Implementation rule:

Reference implementations must not outrun definitions, examples, checker boundaries, formalization assumptions, enterprise governance boundaries, Responsibility Pathway record review boundaries, validator boundaries, review-result boundaries, action-class boundaries, or excluded claims.

First recommended Phase 3 step:

- keep the first human-AI review workflow example small, readable, bounded, and non-certifying before adding additional reference examples
- use `examples/action-class-matrix-minimal.yaml` as a classification baseline before adding Class C, Class D, Class E, or Class F examples

Next low-risk Phase 3 work:

- observe the next `Check examples` workflow after the Action Class Matrix fixture addition
- add a Class C internal document or repository update example only after the classification-only fixture remains green
- add a Class F emergency-stop / stop-and-await example before any Class E high-impact example
- delay Class D reversible external examples until Class C and Class F boundaries are clear
- treat Class E high-impact examples as negative or boundary-only examples until lower classes are stable
- record source-alignment checkpoints before expanding reference examples
- reread prior Zenn articles for definition, claim, and boundary alignment
- add only one small reference example at a time
- avoid production-service, legal-decision, certification, compliance, fairness, moral-resolution, or AI-final-responsibility interpretations

## Guiding Principle

Small commits.
Verified definitions.
Incremental formalization.

Definitions precede proofs.
Proofs precede claims.
Claims precede applications.
