# Example Index

This index lists the current example files and explains how they should be read during Phase 1.6 - Lightweight Validation and Lifecycle Coverage.

Examples are illustrative reference instances. They are not schema validation results, certifications, compliance determinations, safety guarantees, fairness guarantees, legal assessments, moral accountability judgments, or production-ready patterns.

## Current examples

### `examples/minimal-pathway.yaml`

Purpose:

- show the smallest readable Responsibility Pathway instance
- model AI-assisted support without final responsibility transfer
- preserve a return path from an AI support node to a human decision owner
- demonstrate evidence logging and a Human Return Point in a minimal structure

Key boundary:

The AI support node may generate, recommend, classify, explain, escalate, or return, but it does not assume final responsibility.

Use this example when introducing:

- Responsibility Node
- AI participation boundary
- decision owner
- evidence log
- Human Return Point
- formalization-scope exclusions

### `examples/record-review-minimal.yaml`

Purpose:

- show a small Responsibility Pathway record with review metadata
- demonstrate how a record can be reviewed or rechecked without becoming certified
- preserve AI support as support only, with responsibility returning to a human reviewer
- connect record version, lifecycle state, node roles, evidence records, excluded claims, and review result

Key boundary:

Record review checks structure only. It does not certify legal validity, safety, compliance, fairness, moral accountability resolution, institutional approval, or production readiness.

Use this example when introducing:

- Responsibility Pathway record review
- review metadata
- review result boundaries
- evidence records for recheckability
- excluded claims in review outputs
- human review after AI support

### `examples/repair-flow.yaml`

Purpose:

- show a minimal pathway that enters repair
- model ambiguity, uncertainty, or incomplete evidence as a repair trigger
- connect the human decision owner, AI support node, repair owner, evidence log, return point, and repair record
- show that repair is a pathway-restoration mechanism, not a claim that harm disappeared or responsibility was fully resolved

Key boundary:

Repair may support explanation, documentation, continuation, suspension, closure, or later corrective action, but it does not by itself resolve legal liability, moral blame, safety, fairness, or real-world accountability.

Use this example when introducing:

- repair owner
- evidence incompleteness
- return to authority
- repair records
- repair-state vocabulary
- excluded claims for harm elimination and real-world accountability resolution

### `examples/suspended-pathway.yaml`

Purpose:

- show a minimal pathway that enters suspension rather than continuation, repair completion, or closure
- model uncertainty, authority ambiguity, or insufficient review conditions as reasons to preserve the pathway in a suspended state
- connect the human decision owner, AI support node, stop authority, evidence log, return point, and suspension record
- show that suspension preserves responsibility-return conditions instead of erasing, resolving, appropriating, or closing responsibility

Key boundary:

Suspension is not closure, repair completion, certification, compliance, safety, fairness, legal validity, moral resolution, production readiness, or AI decision authority. It is a responsibility-preserving pause until human or institutional authority can review, continue, repair, return, or close the pathway.

Use this example when introducing:

- lifecycle state `suspended`
- stop authority
- suspension owner
- uncertainty-triggered pause
- continuation conditions
- distinction between suspension, repair, and closure
- excluded claims for certification, safety, legal validity, moral resolution, and production readiness

### `examples/returning-pathway.yaml`

Purpose:

- show a minimal pathway that returns from a suspended lifecycle state to an authorized human decision owner
- model returning as a review state rather than automatic continuation, repair completion, or closure
- connect stop authority, AI support, human decision owner, evidence log, return point, and return-condition record
- show that returning restores the pathway to human review while keeping next-state choice explicit

Key boundary:

Returning is not automatic continuation, repair completion, closure, certification, compliance, safety, fairness, legal validity, moral resolution, production readiness, or AI decision authority. It makes the pathway available for human or institutional review and next-state decision.

Use this example when introducing:

- lifecycle state `returning`
- return from suspension
- return-condition review
- distinction between returning, continuation, repair, suspension, and closure
- human decision owner review after return
- excluded claims for automatic continuation, repair completion, closure, certification, and production readiness

### `examples/closed-pathway.yaml`

Purpose:

- show a minimal pathway that reaches a recorded closed lifecycle state
- model closure as an explicit human-reviewed end state within the example scope
- connect human decision owner, AI support, closure reviewer, evidence log, return point, and closure record
- show that closure records boundaries and evidence rather than erasing responsibility history

Key boundary:

Closure is not erasure, immunity, certification, compliance, safety, fairness, legal validity, moral resolution, production readiness, or AI decision authority. It records a declared end state within the example scope while preserving evidence, reopening conditions, and excluded claims.

Use this example when introducing:

- lifecycle state `closed`
- closure owner
- closure reviewer
- closure basis
- residual obligations
- reopening conditions
- distinction between closure, repair completion, certification, and responsibility erasure

## Reading order for examples

Recommended reading order:

1. `docs/schema-cross-reference.md`
2. `docs/validation-checklist.md`
3. `docs/validator-boundary.md`
4. `docs/responsibility-pathway-record-review.md`
5. `examples/minimal-pathway.yaml`
6. `examples/record-review-minimal.yaml`
7. `examples/repair-flow.yaml`
8. `examples/suspended-pathway.yaml`
9. `examples/returning-pathway.yaml`
10. `examples/closed-pathway.yaml`
11. `docs/example-review-notes.md`

## Naming convention

Current examples use descriptive filenames:

- `minimal-pathway.yaml`
- `record-review-minimal.yaml`
- `repair-flow.yaml`
- `suspended-pathway.yaml`
- `returning-pathway.yaml`
- `closed-pathway.yaml`

Future examples should prefer short names that describe the responsibility-pathway pattern rather than implementation details.

Possible future names:

- `approval-gate-flow.yaml`
- `high-impact-action-flow.yaml`
- `evidence-redaction-flow.yaml`

## Example design rules

New examples should:

- keep human or institutional responsibility visible
- keep AI final responsibility explicitly disallowed
- include evidence logging when reconstruction is relevant
- include a return point when human review or authority return is relevant
- state assumptions and excluded claims
- avoid implying certification, compliance, safety, fairness, legal resolution, or moral resolution
- distinguish suspension, return, repair, continuation, closure, and reopening conditions when lifecycle state matters
- remain small enough to be read without tooling

## Future work

Low-risk next steps:

- refine lightweight checker rules after lifecycle examples exist
- add diagrams only after example structures stabilize
- add machine-readable fixtures only after schema validation rules are explicit
- add higher-impact flow examples only after lifecycle boundaries remain stable
