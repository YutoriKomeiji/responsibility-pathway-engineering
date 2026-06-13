# Adapter Boundary

This document defines the boundary for future Responsibility Pathway Engineering adapters.

Adapters are the planned bridge between external logs, API events, workflow results, runtime observations, and Responsibility Pathway records.

This document is documentation-only. It does not add a connector, production runtime, verification engine, compliance system, safety certification tool, legal decision system, or AI final-responsibility transfer mechanism.

## Purpose

The purpose of an adapter is to help transform external event data into a Responsibility Pathway record that can be reviewed by a human or institution.

An adapter may support:

- extracting source event fields
- normalizing event timestamps, actors, actions, and targets
- preserving source references
- classifying candidate action classes
- identifying possible Decision Owner, Approval Gate, Execution Actor, Stop Authority, Evidence Log, Repair Owner, and Human Return Point signals
- recording uncertainty and missing context
- producing a draft Responsibility Pathway record for review

An adapter must not turn an external event into an approved, certified, safe, compliant, legally valid, morally resolved, production-ready, or final-responsibility-complete record.

## What an adapter may do

An adapter may:

- parse external event data
- map event fields to Responsibility Pathway fields
- generate a draft pathway record
- attach source references to evidence records
- flag missing context
- flag uncertainty
- suggest an action class
- suggest whether human or institutional review is required
- suggest whether a stop, approval, repair, correction, or rollback path may be relevant

These operations are support operations only.

They do not decide responsibility.

## What an adapter must not claim

An adapter must not claim that:

- a generated record is certified
- a generated record is legally valid
- a generated record is safe
- a generated record is compliant
- a generated record is fair
- a generated record resolves moral responsibility
- a generated record is production ready
- an AI system has accepted final responsibility
- a human or institution has approved an action unless that approval is present in the source evidence
- external impact has been erased merely because a correction or rollback path exists

A successful adapter run means only that the adapter produced a draft record according to its implemented mapping rules.

## Input event assumptions

A future runtime event schema should remain small at first.

A minimal input event should preserve:

- event identifier
- source system
- event timestamp
- observed actor or system
- observed action
- observed target or affected object
- source reference or evidence pointer when available
- uncertainty or missing-context notes when available
- whether human or institutional review appears required

The first runtime event schema should not assume any specific vendor, cloud provider, AI provider, ticketing system, or enterprise platform.

Service-specific connectors should come later.

## Output pathway record assumptions

A generated Responsibility Pathway record should preserve:

- source event reference
- lifecycle state
- participating nodes
- candidate roles
- evidence records
- human or institutional return point
- responsibility boundary fields
- excluded claims
- uncertainty notes
- missing-context notes
- review requirement

The generated record should be treated as a draft until reviewed by the appropriate human or institutional authority.

## Human review requirement

Adapters do not replace human or institutional review.

When a generated record concerns a Class C, Class D, Class E, or Class F action, the record should preserve explicit review, approval, stop, repair, correction, rollback, or restart conditions where relevant.

If the adapter cannot identify a responsible human or institution, it should record the missing context rather than inventing an authority.

If the adapter cannot determine whether the action is safe, legal, compliant, fair, reversible, or complete, it should record that uncertainty rather than treating the record as approved.

## Evidence log requirement

Adapters should preserve enough evidence for later reconstruction.

Evidence records may include:

- source event identifier
- source system name
- source timestamp
- source actor or system
- raw event pointer when available
- transformation timestamp
- adapter version when available
- mapping notes
- uncertainty notes
- missing-context notes
- human review status when available

Evidence logging is for reconstruction and review.

It is not certification.

## Failure and missing-context handling

Adapters should fail conservatively.

When required information is absent, ambiguous, contradictory, stale, or outside the adapter's scope, the adapter should preserve that fact in the generated record.

An adapter should prefer:

- `review_required`
- `missing_context`
- `uncertainty_notes`
- `stop_or_escalate`
- `human_return_point_required`

rather than silently completing or approving a record.

Missing context is not a defect to hide. It is evidence for review.

## Relationship to Action Class Matrix

Adapters may suggest an action class.

A suggested action class is not a certification.

Class-specific expectations include:

- Class A Observe-Only: preserve source and context
- Class B Suggest-Only: distinguish AI proposal from human adoption
- Class C Approval-Required: preserve approval gate, execution actor, and evidence log signals
- Class D Reversible External Action: preserve affected-party visibility and rollback or correction path signals
- Class E Irreversible or High-Impact Action: remain negative or boundary-only until explicit future modeling exists
- Class F Emergency Stop: preserve stop trigger, Stop Authority, pending responsibility owner, Human Return Point, and restart or closure boundary

Adapters must not autonomously upgrade a draft record into an approved action.

## Relationship to future connectors

Future connectors may be introduced only after this boundary, runtime event schema, and minimal event-to-pathway examples are stable.

Possible future connector documentation may include:

- GitHub Actions to Responsibility Pathway records
- OpenAI API logs to Responsibility Pathway records
- FastAPI request logs to Responsibility Pathway records
- AWS CloudTrail events to Responsibility Pathway records
- ticketing or approval workflow events to Responsibility Pathway records

The first connector should be small, synthetic where possible, and bounded to repository-maintenance or review examples before any production-like workflow is introduced.

## Non-certifying interpretation

Adapter outputs are draft records.

A generated draft record does not mean:

- the underlying action was correct
- the underlying action was approved
- the underlying action was safe
- the underlying action was legal
- the underlying action was compliant
- the underlying action was fair
- the underlying action was morally resolved
- the underlying action was production ready
- an AI system assumed final responsibility

The human author, maintainer, reviewer, or responsible institution remains responsible for deciding how the generated record should be interpreted, reviewed, changed, accepted, rejected, repaired, escalated, or closed.

## Next low-risk work

After this document is stable, the next small steps are:

1. add `spec/runtime-event.schema.yaml`
2. add `examples/adapter-input-event-minimal.json`
3. add `examples/runtime-event-to-pathway-minimal.yaml`
4. only then consider a local, non-production conversion script

Do not add service-specific connectors before the minimal runtime event bridge is readable and reviewable.
