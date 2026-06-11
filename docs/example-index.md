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

## Reading order for examples

Recommended reading order:

1. `docs/schema-cross-reference.md`
2. `docs/validation-checklist.md`
3. `docs/validator-boundary.md`
4. `examples/minimal-pathway.yaml`
5. `examples/repair-flow.yaml`
6. `examples/suspended-pathway.yaml`
7. `docs/example-review-notes.md`

## Naming convention

Current examples use descriptive filenames:

- `minimal-pathway.yaml`
- `repair-flow.yaml`
- `suspended-pathway.yaml`

Future examples should prefer short names that describe the responsibility-pathway pattern rather than implementation details.

Possible future names:

- `returning-pathway.yaml`
- `closed-pathway.yaml`
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
- distinguish suspension, repair, return, and closure when lifecycle state matters
- remain small enough to be read without tooling

## Future work

Low-risk next steps:

- add examples for `returning` and `closed` lifecycle states
- refine lightweight checker rules after more lifecycle examples exist
- add diagrams only after example structures stabilize
- add machine-readable fixtures only after schema validation rules are explicit
