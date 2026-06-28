# API Future Shape

This document records a future API design preview for Responsibility Pathway Engineering.

The future API material is not implemented yet.

This file describes intended input, draft-output, review, fixture relationship, and boundary concepts before any implementation work begins.

## Current status

Design preview only.

No public API route, service connector, production runtime, schema-validation service, conformance service, or adapter implementation is defined here.

## Expected API layers

The future API shape is expected to remain layered.

| Layer | Purpose | Current status |
| --- | --- | --- |
| Runtime event input | Receive structured observations from external systems. | Draft schema exists. |
| Adapter mapping | Map event fields to candidate pathway roles and evidence records. | Boundary documented; implementation deferred. |
| Draft pathway generation | Produce draft Responsibility Pathway records for review. | Minimal examples exist. |
| Review result capture | Record what a human or institution reviewed and did not review. | Bounded schema and checker exist. |
| Relation checking | Check selected structural preservation between event and pathway record. | Planning only. |
| Service connectors | Connect specific systems such as workflow logs, API logs, ticketing systems, or audit logs. | Deferred. |
| Production runtime | Continuous production integration. | Deferred. |

This layered view is a planning aid only. It does not change the current implementation state.

## Candidate route preview

The following route names are illustrative only.

They are not implemented routes and are not stable public API.

| Candidate route | Intended role | Current status |
| --- | --- | --- |
| `POST /runtime-events` | Receive a structured runtime-event object for bounded inspection. | Preview only. |
| `POST /pathway-drafts/from-runtime-event` | Produce a draft Responsibility Pathway record from a runtime-event object or reference. | Preview only. |
| `GET /pathway-drafts/{id}` | Retrieve a draft pathway record for review, correction, repair, or closure. | Preview only. |
| `POST /review-results` | Record a bounded human or institutional review result. | Preview only. |
| `POST /pathway-drafts/{id}/repair-note` | Attach a repair, rollback, correction, or reconnection note to a draft record. | Preview only. |

Any future route should preserve review requirement, missing context, uncertainty, evidence references, and excluded claims.

A future route must not silently turn a draft record into an approved or final record.

## Expected input concepts

A future API input should preserve enough structure for later human or institutional review.

Expected input concepts include:

- event identifier
- source system
- event timestamp
- observed actor or system
- observed action
- observed target or affected object
- source reference or evidence pointer
- uncertainty notes
- missing-context notes
- review requirement signal
- excluded claims

The input should preserve what is unknown instead of filling gaps silently.

## Expected draft output concepts

A future draft output should support review, correction, repair, or rejection.

Expected draft output concepts include:

- draft record identifier
- lifecycle state
- candidate Decision Owner
- candidate Approval Gate
- candidate Execution Actor
- candidate Stop Authority
- candidate Evidence Log entries
- candidate Repair Owner
- candidate Human Return Point
- missing-context notes
- uncertainty notes
- excluded claims
- review-required flag

The output should remain a draft until the responsible human or institution reviews it.

## Connector target relationship

Future API design should use `docs/connector-target-matrix.md` when deciding which external system category is being modeled.

The matrix helps distinguish:

- workflow automation events;
- agent tool protocol events;
- API request logs;
- local service logs;
- cloud audit logs;
- ticketing workflow events;
- AI governance surfaces;
- ERP document changes;
- incident and support workflow events.

The matrix is a design-preview aid only. It does not authorize connector implementation or production integration.

## Relation to current runtime-event fixtures

Current fixture-related artifacts include:

- `spec/runtime-event.schema.yaml`
- `examples/adapter-input-event-minimal.json`
- `examples/minimal-synthetic-runtime-fixture.json`
- `examples/runtime-event-to-pathway-minimal.yaml`
- `scripts/check_runtime_events.py`
- `docs/runtime-event-schema-fixture-alignment.md`
- `docs/event-to-pathway-relation-checker-plan.md`

These artifacts are useful for API design because they show the current draft boundary between observed runtime events, draft pathway records, and bounded structural checking.

They do not define a production API contract.

They also do not prove schema validity, semantic correctness, adapter correctness, runtime correctness, connector correctness, or responsibility assignment correctness.

## Restart conditions before implementation

Before implementing any API route, the maintainer should confirm that:

1. the relevant concept is documented;
2. the reader path is clear;
3. boundary and non-goals are explicit;
4. examples or fixtures are stable enough to review;
5. the change can be made in a small, auditable commit;
6. the result remains non-certifying;
7. service-specific connectors remain deferred unless explicitly reopened;
8. production runtime integration remains deferred unless explicitly reopened.

The preferred next action is still documentation alignment or a local synthetic design note, not service integration.

## Boundary

This file does not define an implemented API, connector, runtime, certification process, conformance process, or final-responsibility transfer mechanism.

The human author or maintainer remains responsible for deciding whether this file should be expanded, revised, published, relied upon, reverted, repaired, or deferred.
