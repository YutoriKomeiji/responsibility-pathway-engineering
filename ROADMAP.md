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

## Phase 1.5 - Specification Binding (Established)

- Core YAML specification expanded to v0.2.0
- Concept documents aligned with initial machine-readable specification
- Minimal schema split established under `spec/`
- Validation-oriented fields defined for nodes, roles, lifecycle, action classes, evidence, return points, repair, and pathway composition
- Schema cross-reference notes added
- Validation checklist documentation added
- Initial minimal examples added
- README, README.ja, CHANGELOG, and BEACON maintained at milestones

Established schema files:

- spec/node.schema.yaml
- spec/action-class.schema.yaml
- spec/return-point.schema.yaml
- spec/evidence-log.schema.yaml
- spec/repair.schema.yaml
- spec/pathway.schema.yaml

## Phase 1.6 - Lightweight Validation and Lifecycle Examples (Substantially Established)

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

Phase 1.6 rule:

Lifecycle-aware checks remain bounded structural maintenance checks. They do not certify examples, systems, legal validity, safety, compliance, fairness, moral resolution, production readiness, or real-world responsibility resolution.

Remaining Phase 1.6 tasks:

- run and stabilize checker output if execution environment is available
- keep examples small and manually readable
- avoid adding higher-impact examples until lifecycle boundaries remain stable

## Phase 2 - Formalization (Started)

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

Current Phase 2 start:

- `formal/lean/ResponsibilityPathway/Core.lean` added
- minimal `NodeKind` and `Node` model added
- first invariant candidate added: a safely constructed AI node cannot hold final responsibility
- Lean README updated with formalization boundary and current invariant candidate

Formalization rule:

Formal proofs must remain bounded to explicit definitions, assumptions, and modeled scope.

Current invariant candidates:

- an AI node cannot be final responsibility holder - started
- an AI-assisted pathway must preserve a human or institutional return point
- a repaired pathway must reference a repair record
- a suspended pathway must preserve review or return conditions
- a returning pathway must not imply automatic continuation
- a closed pathway must preserve evidence and reopening-condition records

## Phase 3 - Reference Implementations

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

Implementation rule:

Reference implementations must not outrun definitions, examples, checker boundaries, or formalization assumptions.

## Guiding Principle

Small commits.
Verified definitions.
Incremental formalization.

Definitions precede proofs.
Proofs precede claims.
Claims precede applications.
