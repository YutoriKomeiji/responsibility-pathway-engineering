# API Future Shape

This document is a placeholder for a future API design preview.

The future API material is not implemented yet.

This file will describe intended input, draft-output, review, and boundary concepts before any implementation work begins.

## Current status

Design preview placeholder.

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

## Boundary

This file does not define an implemented API, connector, runtime, certification process, conformance process, or final-responsibility transfer mechanism.

## Next note expansion

A later small commit may add:

- relation to current runtime-event fixtures
- restart conditions before implementation

The human author or maintainer remains responsible for deciding whether this placeholder should be expanded, revised, published, relied upon, reverted, repaired, or deferred.
