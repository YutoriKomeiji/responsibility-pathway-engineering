# Example Index

This index lists the current example and fixture files and explains how they should be read during Phase 1.6, Phase 3 reference-example work, and Phase 3.1 runtime-event bridge work.

Examples and fixtures are illustrative reference instances. They are not schema validation results, certifications, compliance determinations, safety guarantees, fairness guarantees, legal assessments, moral accountability judgments, or production-ready patterns.

## Current examples and fixtures

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

### `examples/action-class-matrix-minimal.yaml`

Purpose:

- show a minimal classification-only Action Class Matrix fixture
- list the source-aligned Class A-F action classes in a readable example form
- preserve AI support as classification support only, without execution or approval authority
- connect action classification to Decision Owner, Stop Authority, Evidence Log, and Human Return Point signals

Key boundary:

This fixture classifies example action types only. It does not execute any action, approve any action, certify any action class, or prove safety, compliance, legality, fairness, moral resolution, or production readiness.

Use this example when introducing:

- Action Class Matrix
- Class A-F action classification
- classification-only AI support
- proposal/adoption separation
- action-class-specific future example design
- non-certifying action classification boundaries

### `examples/internal-document-update.yaml`

Purpose:

- show a minimal Class C Approval-Required internal document update example
- model AI-assisted drafting without AI approval, execution, or final responsibility
- require human approval before internal document update execution
- connect Decision Owner, Approval Gate, Execution Actor, Stop Authority, Evidence Log, Repair Owner, and Human Return Point signals

Key boundary:

This example models an internal document update only. It does not publish externally, certify the update, validate the content, approve real-world use, or prove legal, safety, compliance, fairness, moral, or production readiness.

Use this example when introducing:

- Class C Approval-Required actions
- internal state change or internal document update
- approval gate before execution
- proposal/adoption separation
- execution actor without final responsibility
- repair owner and correction path for internal updates

### `examples/missed-support-boundary-minimal.yaml`

Purpose:

- show a small boundary-only missed-support example in repository maintenance
- model an AI support node preparing a public-facing documentation or navigation update without requesting required human review
- record the missed support signal as a return condition, not as automatic continuation or certification
- connect support-call policy, Decision Owner, Approval Gate, Stop Authority, Evidence Log, Repair Owner, and Human Return Point signals

Key boundary:

This example is synthetic, local, boundary-only, and non-production. The `support_call_policy` block is example-only and is not currently schema-enforced. The example does not certify the update, validate runtime behavior, validate connector behavior, approve automatic execution, or prove legal, safety, compliance, fairness, moral, or production readiness.

Current checker boundary:

This example is checked only by the existing bounded structural example checker as a pathway example with `lifecycle_state: returning`. The checker does not currently enforce the semantics of `support_call_policy`.

Use this example when introducing:

- support-call policy as a concept-level mapping
- missed support as a structural review signal
- Class C Approval-Required public-facing repository documentation changes
- returning lifecycle boundary after missed human review
- stop-and-return before publication
- repair owner review after missed support

### `examples/reversible-external-action.yaml`

Purpose:

- show a minimal Class D Reversible External Action example
- model a human-approved external notification with rollback or correction path
- preserve AI support as drafting or recommendation support only, without AI approval, execution, stop authority, repair authority, or final responsibility
- connect Decision Owner, Approval Gate, Execution Actor, Stop Authority, Evidence Log, Repair Owner, affected-party visibility, rollback/correction path, and Human Return Point signals

Key boundary:

This example models a correctable external notification only. Reversibility means a correction or retraction path exists; it does not mean the external impact is harmless, erased, legally approved, safe, compliant, or production ready.

Use this example when introducing:

- Class D Reversible External Action
- external impact scope
- affected-party visibility
- explicit approval before external action
- rollback or correction path before action
- distinction between reversible external impact and internal document update

### `examples/emergency-stop-flow.yaml`

Purpose:

- show a minimal Class F Emergency Stop / stop-and-await example
- model abnormal uncertainty or authority gap as a reason to suspend rather than continue
- preserve pending responsibility after stop instead of treating stop as approval, repair, or closure
- connect Stop Authority, Evidence Log, Human Return Point, pending responsibility owner, repair owner, and restart boundary signals

Key boundary:

This example models emergency stop and suspension only. It does not prove safety, complete repair, approve continuation, resolve legal or moral responsibility, certify compliance, or authorize production use.

Use this example when introducing:

- Class F Emergency Stop actions
- stop trigger and stop reason
- stop authority separate from execution authority
- stop-and-await lifecycle boundary
- restart approval boundary
- pending responsibility preservation after stop

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

### `examples/human-ai-review-workflow-minimal.yaml`

Purpose:

- show the first small Phase 3 reference example
- model a human-led review workflow supported by an AI summary assistant
- preserve a return path from AI support back to a human reviewer
- record evidence, uncertainty notes, missing-context notes, checked items, unchecked items, and excluded claims

Key boundary:

The AI node may summarize evidence and explain uncertainty, but it does not decide, approve, execute, close, or assume final responsibility. The human reviewer remains the decision owner, approval gate, stop authority, and responsibility owner.

Use this example when introducing:

- Phase 3 reference examples
- human-led AI-supported review workflows
- AI summary support without final responsibility transfer
- evidence records for human acceptance or rejection
- review-result boundaries in a reference workflow
- reference implementation boundaries

### `examples/adapter-input-event-minimal.json`

Purpose:

- show the first selected synthetic runtime-event JSON fixture
- provide a small vendor-neutral runtime-event input for the adapter boundary
- preserve event identity, source system, observed actor, observed action, observed target, evidence, review requirement, adapter context, and excluded claims
- keep the event as an observation input, not approval, execution, certification, or production connector output

Key boundary:

This fixture is synthetic and vendor-neutral. It is not a production runtime event, service-specific connector payload, approval record, execution record, legal validation, safety certification, compliance certification, fairness certification, moral resolution, production-readiness proof, or AI final-responsibility transfer.

Current checker boundary:

This JSON fixture is checked by `scripts/check_runtime_events.py` for bounded structural runtime-event signals only. It is not checked by `scripts/check_examples.py` because it is not a pathway YAML example.

Use this fixture when introducing:

- Phase 3.1 adapter boundary and runtime event bridge
- synthetic runtime-event input shape
- source-system and observed-actor boundaries
- missing-context and uncertainty preservation
- adapter suggestion versus human review
- review-required event interpretation

### `examples/runtime-event-to-pathway-minimal.yaml`

Purpose:

- show the first small Phase 3.1 runtime-event-to-pathway draft example
- model a synthetic runtime event being represented as a draft Responsibility Pathway record
- preserve source event reference, missing context, uncertainty notes, evidence log, and Human Return Point signals
- keep adapter output as review-required draft record, not approval, execution, certification, or production connector output

Key boundary:

This example models a synthetic, vendor-neutral runtime-event bridge only. It does not provide a service-specific connector, production runtime, automatic responsibility decision, automatic approval, legal validation, safety certification, compliance certification, fairness certification, moral resolution, production readiness, or AI final-responsibility transfer.

Current checker boundary:

This example is currently checked only as a pathway example under the existing structural and originating-lifecycle checker rules. `docs/runtime-event-schema-fixture-alignment.md` describes the current structural alignment between the draft runtime-event schema, selected JSON fixtures, and bounded runtime-event checker. `docs/event-to-pathway-relation-checker-plan.md` describes a possible future local structural relation checker plan between selected runtime-event JSON fixtures and pathway YAML examples, but it is not current checker behavior and does not authorize implementation by itself. `docs/runtime-event-checking-plan.md` describes future checks and boundaries. A checker pass must not be interpreted as schema validation, JSON semantic correctness proof, adapter mapping correctness proof, event-to-pathway relation correctness proof, runtime correctness proof, production readiness, certification, conformance evidence, or AI final-responsibility transfer.

Use this example when introducing:

- Phase 3.1 adapter boundary and runtime event bridge
- synthetic runtime event input mapping
- draft pathway records generated from observed events
- missing-context and uncertainty preservation
- adapter suggestion versus human review
- generated record review requirements
- difference between pathway-example checks, JSON fixture checks, and planned relation-checker work

### `examples/minimal-synthetic-runtime-fixture.json`

Purpose:

- show the first minimal synthetic runtime observation fixture
- provide a small runtime-like observation point before production runtime integration
- wrap a draft proposal observation while preserving review-required and non-production boundaries
- reference `examples/adapter-input-event-minimal.json` without adding a service-specific connector

Key boundary:

This fixture is synthetic, local, vendor-neutral, non-production, review-required, and non-certifying. It does not implement a production runtime, service-specific connector, adapter mapping correctness proof, automatic approval, automatic execution, legal validation, safety certification, compliance certification, fairness certification, moral resolution, production readiness, runtime correctness, conformance evidence, or AI final-responsibility transfer.

Current checker boundary:

This JSON fixture is checked by `scripts/check_runtime_events.py` for bounded structural runtime-boundary signals only. It is not checked by `scripts/check_examples.py` because it is not a pathway YAML example. It remains a minimal synthetic runtime observation fixture for reading and review, not a production runtime or runtime correctness proof.

Use this fixture when introducing:

- minimal runtime candidate planning
- synthetic runtime observation boundaries
- non-production runtime-like fixtures
- missing approval evidence and missing execution evidence preservation
- separation between runtime fixture, checker stub, workflow, connector, and production runtime
- open review of runtime boundaries before implementation

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

## Reading order for examples and fixtures

Recommended reading order:

1. `docs/schema-cross-reference.md`
2. `docs/validation-checklist.md`
3. `docs/validator-boundary.md`
4. `docs/responsibility-pathway-record-review.md`
5. `docs/reference-implementation-boundary.md`
6. `docs/action-class-matrix.md`
7. `examples/action-class-matrix-minimal.yaml`
8. `examples/minimal-pathway.yaml`
9. `examples/internal-document-update.yaml`
10. `examples/missed-support-boundary-minimal.yaml`
11. `examples/emergency-stop-flow.yaml`
12. `examples/reversible-external-action.yaml`
13. `examples/record-review-minimal.yaml`
14. `examples/human-ai-review-workflow-minimal.yaml`
15. `docs/adapter-boundary.md`
16. `spec/runtime-event.schema.yaml`
17. `docs/runtime-event-schema-fixture-alignment.md`
18. `docs/event-to-pathway-relation-checker-plan.md`
19. `docs/runtime-event-checking-plan.md`
20. `docs/minimal-runtime-candidate-design.md`
21. `examples/adapter-input-event-minimal.json`
22. `examples/runtime-event-to-pathway-minimal.yaml`
23. `examples/minimal-synthetic-runtime-fixture.json`
24. `examples/repair-flow.yaml`
25. `examples/suspended-pathway.yaml`
26. `examples/returning-pathway.yaml`
27. `examples/closed-pathway.yaml`
28. `docs/example-review-notes.md`

## Relationship to Action Class Matrix

`docs/action-class-matrix.md` is the design aid for classifying future AI-agent actions before example design.

Current examples do not need to be retroactively reclassified unless they are updated.

Future examples should state their intended action class before claiming pathway sufficiency.

For example:

- Class A Observe-Only examples should preserve source/context and adoption boundaries.
- Class B Suggest-Only examples should distinguish AI proposal from human adoption.
- Class C Approval-Required examples should include Approval Gate, Execution Actor, and Evidence Log signals.
- Class D Reversible External Action examples should include rollback or repair path signals.
- Class E Irreversible or High-Impact examples should remain synthetic, bounded, non-production, and explicitly non-autonomous unless future institutional/legal layers are modeled.
- Class F Emergency Stop examples should include stop trigger, Stop Authority, pending responsibility owner, Human Return Point, and restart/closure boundary.

Action Class Matrix classification is not a certification, compliance determination, safety review, legal review, or production-readiness review.

## Naming convention

Current examples use descriptive filenames:

- `minimal-pathway.yaml`
- `action-class-matrix-minimal.yaml`
- `internal-document-update.yaml`
- `missed-support-boundary-minimal.yaml`
- `emergency-stop-flow.yaml`
- `reversible-external-action.yaml`
- `record-review-minimal.yaml`
- `human-ai-review-workflow-minimal.yaml`
- `adapter-input-event-minimal.json`
- `runtime-event-to-pathway-minimal.yaml`
- `minimal-synthetic-runtime-fixture.json`
- `repair-flow.yaml`
- `suspended-pathway.yaml`
- `returning-pathway.yaml`
- `closed-pathway.yaml`

Future examples should prefer short names that describe the responsibility-pathway pattern rather than implementation details.
