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

## Phase 1.5 - Specification Binding (Current)

- Core YAML specification expanded to v0.2.0
- Align concept documents with machine-readable specification
- Split core YAML into focused schema files
- Define validation-oriented fields for nodes, roles, lifecycle, action classes, evidence, return points, and repair
- Add minimal examples only after definitions and specifications are stable

Candidate schema files:

- spec/node.schema.yaml
- spec/action-class.schema.yaml
- spec/return-point.schema.yaml
- spec/evidence-log.schema.yaml
- spec/repair.schema.yaml
- spec/pathway.schema.yaml

## Phase 2 - Formalization

- Lean invariants
- State transitions
- Path semantics
- Returnability invariants
- Stop authority invariants
- Evidence sufficiency boundaries
- Repair preconditions

Formalization rule:

Formal proofs must remain bounded to explicit definitions, assumptions, and modeled scope.

## Phase 3 - Reference Implementations

- YAML extensions
- Example workflows
- Multi-agent examples
- Human Return Point example
- Evidence Log example
- Approval Gate example
- Repair flow example

## Guiding Principle

Small commits.
Verified definitions.
Incremental formalization.

Definitions precede proofs.
Proofs precede claims.
Claims precede applications.
