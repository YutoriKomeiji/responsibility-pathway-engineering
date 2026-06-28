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

## Boundary

This file does not define an implemented API, connector, runtime, certification process, conformance process, or final-responsibility transfer mechanism.

## Next note expansion

A later small commit may add:

- expected input concepts
- expected draft output concepts
- candidate route names
- relation to current runtime-event fixtures
- restart conditions before implementation

The human author or maintainer remains responsible for deciding whether this placeholder should be expanded, revised, published, relied upon, reverted, repaired, or deferred.
