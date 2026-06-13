# Schema Cross-Reference

This note explains how the current Responsibility Pathway Engineering schema files relate to each other during Phase 1.5 - Specification Binding, Phase 1.6 - lightweight validation, Phase 2.5 - record-review alignment, and Phase 3.1 - runtime-event bridge work.

It is explanatory only. It does not claim complete validation, legal liability, production readiness, compliance, safety, fairness, moral accountability, connector correctness, adapter correctness, or runtime readiness.

## Core vocabulary map

`spec/responsibility-pathway-core.yaml` is the conceptual vocabulary map for the repository.

It defines the broad Responsibility Pathway concept, including:

- supported entity types
- responsibility node capabilities
- pathway roles
- responsibility-related elements
- lifecycle states
- action classes
- pathway requirements
- returnability conditions
- non-goals
- AI participation boundaries
- formalization boundaries

The core file should be read as the conceptual anchor. The split schema files below provide more focused, machine-readable structures for specific parts of that vocabulary.

## Split schema files

### `spec/node.schema.yaml`

Defines the minimum structure for a Responsibility Node.

Use this schema for pathway participants such as humans, AI agents, organizations, business processes, information systems, artifacts, documents, interfaces, database records, model outputs, and audit artifacts.

Key concerns:

- node identity
- node type
- capabilities
- authority scope
- evidence binding
- human responsibility capacity
- AI participation limits

Important boundary:

AI may participate as a pathway node or implementation-support layer, but AI participation does not establish final responsibility authorship.

### `spec/action-class.schema.yaml`

Defines the minimum structure for classifying actions by responsibility impact.

Use this schema to describe the expected responsibility weight of an action before composing or validating a pathway.

Current status:

- `spec/action-class.schema.yaml` is currently v0.2.0.
- The current source-aligned structure uses Class A-F.
- Earlier Class 0-4 values are retained only as historical mapping references.
- New examples should prefer `source_aligned_class` over legacy `level`.

Current source-aligned classes:

| Class | Name | Main distinction |
| --- | --- | --- |
| A | Observe-Only | Observation without execution. |
| B | Suggest-Only | Proposal, summary, classification, or draft without execution. |
| C | Approval-Required | Internal change or controlled state change requiring approval design. |
| D | Reversible External Action | External effect with rollback or correction path. |
| E | Irreversible or High-Impact Action | Irreversible, safety-relevant, legal, financial, production, permission, customer, or other high-impact effect. |
| F | Emergency Stop | Stop, isolate, suspend, downgrade, or return to human confirmation. |

Key concerns:

- action class identity
- `source_aligned_class`
- optional legacy mapping
- responsibility requirements
- reversibility
- external impact
- execution effect
- automation boundary
- excluded interpretations

The action class helps determine when stronger requirements are expected, such as human authorization, approval gate, evidence logging, stop authority, return points, rollback/correction paths, or repair ownership.

Important boundary:

The schema classifies actions for Responsibility Pathway design. It does not determine legal classification, safety, compliance, fairness, moral responsibility, production readiness, or final responsibility by itself.

Related documents and examples:

- `docs/action-class-matrix.md`
- `examples/action-class-matrix-minimal.yaml`

### `spec/return-point.schema.yaml`

Defines the minimum structure for Return Points, including Human Return Points.

Use this schema when responsibility-related state must be returnable to an authorized human, organization, institution, or process.

Key concerns:

- source and target node
- returnability conditions
- supported actions
- evidence requirements
- human conditions

A Human Return Point is not valid merely because a human is present. Returnability depends on visible meaning, authority, time, information quality, calibrated trust, reversibility or compensation, value, cost, and repair capacity.

### `spec/evidence-log.schema.yaml`

Defines the minimum structure for evidence records that support reconstruction, explanation, stopping, return, and repair.

Use this schema when a pathway needs reconstructable records for authority, context, uncertainty, tool use, execution, stop conditions, affected parties, repair actions, or post-event explanation.

Key concerns:

- pathway binding
- evidence categories
- integrity state
- ordering
- reconstruction support
- quality
- access boundary

Evidence logs support responsibility return and repair, but they are not complete truth records by default.

### `spec/repair.schema.yaml`

Defines the minimum structure for restoring a broken, unclear, suspended, or damaged Responsibility Pathway to an actionable state.

Use this schema when a pathway requires detection, preservation, return to authority, corrective action, documentation, closure, or unresolved-state preservation.

Key concerns:

- repair trigger
- repair owner
- repair state
- evidence reference
- affected parties
- corrective action
- outcome

Repair does not mean harm disappears, and it does not resolve blame by itself. It restores the pathway enough for action, explanation, correction, compensation, redesign, closure, or explicit unresolved preservation.

### `spec/runtime-event.schema.yaml`

Defines a minimal vendor-neutral input event shape for future adapters.

Use this schema when describing an observed runtime event before it is transformed into a draft Responsibility Pathway record.

Key concerns:

- event identity
- schema version
- source system
- observation timestamp
- observed actor
- observed action
- observed target
- evidence and missing-context notes
- review requirement
- excluded claims
- adapter context when available

Important boundary:

A runtime event is an observation input, not approval, execution authority, certification, legal or moral resolution, connector correctness, adapter correctness, or production readiness.

Related documents and examples:

- `docs/adapter-boundary.md`
- `docs/phase-3-1-current-snapshot.md`
- `docs/phase-3-1-sync-log.md`
- `examples/adapter-input-event-minimal.json`
- `examples/runtime-event-to-pathway-minimal.yaml`

### `spec/pathway.schema.yaml`

Defines the minimum structure for a composed Responsibility Pathway instance.

Use this schema to bind the split schema parts into one pathway-level structure.

Key concerns:

- pathway identity and version
- lifecycle state
- nodes
- edges
- roles
- action class
- evidence logs
- return points
- repairs
- responsibility boundary
- formalization scope
- review metadata where applicable

This file composes the split schema files:

| Pathway field | Referenced schema or concept |
| --- | --- |
| `nodes` | `spec/node.schema.yaml` |
| `action_class` | `spec/action-class.schema.yaml` |
| `evidence_logs` | `spec/evidence-log.schema.yaml` |
| `return_points` | `spec/return-point.schema.yaml` |
| `repairs` | `spec/repair.schema.yaml` |
| `source_runtime_event` | optional Phase 3.1 runtime-event bridge input |
| `input_event_mapping` | optional adapter mapping notes |
| `runtime_adapter_boundary` | optional adapter-boundary fields |
| `review_metadata` | optional bounded record-review metadata |
| `responsibility_boundary` | AI and human/institutional responsibility boundary from the core vocabulary |
| `formalization_scope` | bounded assumptions, modeled entities, excluded claims, and theorem status |

### `spec/review-result.schema.yaml`

Defines the minimum structure for a bounded Responsibility Pathway review result.

Use this schema to record the output of a structural record review.

Key concerns:

- review result identity
- reviewed pathway identifier
- review scope
- review status
- schema and review tool versions
- checked items
- warnings and failures
- not-checked items
- not-claimed boundaries
- plain-language summary
- responsibility boundary flags

A review result records what was checked, what was not checked, and what is not claimed. It is not a legal decision, safety decision, compliance decision, fairness decision, moral-resolution decision, institutional certification, or production approval.

Related fixture:

- `fixtures/review-results/record-review-result-minimal.yaml`

## Reading order

Recommended reading order:

1. `spec/responsibility-pathway-core.yaml`
2. `spec/node.schema.yaml`
3. `spec/action-class.schema.yaml`
4. `spec/return-point.schema.yaml`
5. `spec/evidence-log.schema.yaml`
6. `spec/repair.schema.yaml`
7. `spec/runtime-event.schema.yaml`
8. `spec/pathway.schema.yaml`
9. `spec/review-result.schema.yaml`

This order moves from concept vocabulary to specialized schema files, runtime-event inputs, composed pathway instances, and then bounded review-result outputs.

## Validation boundary

These schema files currently define minimum structure and design expectations. They do not yet constitute a complete validator, certification scheme, compliance framework, connector framework, adapter correctness proof, or formal proof system.

`spec/runtime-event.schema.yaml` is not yet validated by the current lightweight checker. `examples/adapter-input-event-minimal.json` is not yet checked by `scripts/check_examples.py`.

Action-class-specific checker enforcement is not yet active. Future checker work may inspect bounded structural signals from `spec/action-class.schema.yaml`, but such checks must remain non-certifying and must not be interpreted as legal validity, safety, compliance, fairness, moral resolution, institutional approval, production readiness, or AI final-responsibility transfer.

Formal claims must remain limited to explicitly stated definitions, assumptions, modeled entities, and transitions.

Real-world claims about safety, legality, fairness, compliance, connector behavior, adapter correctness, production readiness, or moral accountability require additional human, institutional, legal, domain, and operational review outside these schema files.
