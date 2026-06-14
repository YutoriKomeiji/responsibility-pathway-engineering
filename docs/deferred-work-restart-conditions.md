# Deferred Work Restart Conditions

This document collects restart conditions for work that has been deliberately deferred.

A deferred item is not abandoned. It is paused until its restart conditions are satisfied.

## General rule

Do not restart a deferred item merely because it is interesting, adjacent, or easy to implement.

Restart only when:

1. the relevant concept is documented,
2. the reader path is clear,
3. the boundary and non-goals are explicit,
4. examples or fixtures are stable enough to review,
5. the change can be made in a small, auditable commit,
6. the result remains non-certifying unless a later document explicitly changes that scope.

## Provenance reader-path synchronization

Deferred item:

- direct short references from long navigation files such as `BEACON.md` and `docs/operation-index.md`

Current reason for deferral:

- those files are long and broad synchronization edits can be hard to review.

Restart conditions:

- `docs/provenance.md` exists and has been connected from authorship, notice, citation, and authorship files.
- `docs/provenance-reader-path.md` exists as a short navigation target.
- the proposed edit is limited to one short reference or one small list item.
- the edit does not repeat detailed provenance content inside the long file.

Allowed restart action:

- add a compact reference to `docs/provenance.md` or `docs/provenance-reader-path.md`.

Do not restart as:

- a full rewrite of `BEACON.md`
- a full rewrite of `docs/operation-index.md`
- a new broad source-lineage argument inside a navigation file

## Support-call policy schema fields

Deferred item:

- adding support-call policy or missed-support fields to schemas.

Current reason for deferral:

- support-call policy is currently a related-work and concept-level mapping, not a stable schema element.

Restart conditions:

- `docs/related-work/strategic-decision-support.md` remains stable.
- a small concept note maps support-call policy to existing RPE concepts.
- at least one small, manually readable example or review note exists.
- the target layer is decided: node, action class, pathway, evidence log, runtime event, or review-result.
- checker behavior is still explicitly out of scope or separately planned.

Allowed restart action:

- write a schema-design note before changing any schema.

Do not restart as:

- direct schema field addition
- runtime-event schema expansion
- review-result schema expansion
- checker implementation

## Missed-support review signal

Deferred item:

- treating missed support as a review signal in examples or review results.

Current reason for deferral:

- missed-support is useful but not yet represented by a stable RPE example.

Restart conditions:

- support-call policy has been mapped to Human Return Point, Approval Gate, Stop Authority, Evidence Log, Repair Owner, and Decision Owner.
- at least one boundary-only or negative example is drafted.
- the example remains non-production and non-certifying.
- the example does not involve real medical, legal, financial, or other high-impact deployment.

Allowed restart action:

- add a small boundary-only example or review note.

Do not restart as:

- a high-impact positive example
- an automatic approval example
- a production support-routing claim

## Runtime-event checking

Deferred item:

- `scripts/check_runtime_events.py`
- runtime-event workflow
- runtime-event schema checking
- JSON fixture checking
- runtime fixture checking

Current reason for deferral:

- runtime-event bridge and fixtures are still reading and review artifacts.

Restart conditions:

- `docs/runtime-event-checking-plan.md` preconditions are satisfied.
- runtime-event examples remain readable and reviewable.
- JSON fixtures remain stable.
- checker scope is limited to structural signals.
- passing status is documented as bounded repository-maintenance only.

Allowed restart action:

- write or update a checker-design note before implementation.

Do not restart as:

- production runtime validation
- connector behavior validation
- adapter correctness validation
- legal, safety, compliance, fairness, or production certification

## Service-specific connectors

Deferred item:

- service-specific connectors
- production conversion code
- production runtime integration

Current reason for deferral:

- adapter boundary and runtime-event bridge are still vendor-neutral and non-production.

Restart conditions:

- adapter boundary remains stable.
- runtime-event schema remains stable.
- generated-record examples remain stable.
- minimal synthetic runtime fixture remains stable.
- checker boundaries and validation checklist are updated first.
- a local, non-production conversion example is justified before any service connector.

Allowed restart action:

- write a connector-boundary design note.

Do not restart as:

- direct integration with external services
- production connector
- production runtime
- automatic execution or approval

## Lean expansion around runtime or support-call policy

Deferred item:

- Lean theorem families for adapter events, runtime events, support-call policy, or missed-support signals.

Current reason for deferral:

- modeling boundary is not stable enough for formalization.

Restart conditions:

- concepts are stable.
- examples are stable.
- schema boundaries are stable or explicitly out of scope.
- checker boundaries are stable or explicitly out of scope.
- theorem roles are named before theorem implementation.
- assumptions are explicit.

Allowed restart action:

- write a theorem-role note first.

Do not restart as:

- direct Lean theorem expansion
- proof of production safety
- proof of legal validity
- proof of AI final responsibility

## Class E high-impact examples

Deferred item:

- positive Class E examples.

Current reason for deferral:

- lower-impact examples and boundaries should remain stable first.

Restart conditions:

- Class A-F examples remain stable.
- checker coverage remains bounded and non-certifying.
- Class D and Class F examples remain readable and correctable.
- the example is negative or boundary-only unless a later roadmap note explicitly permits otherwise.

Allowed restart action:

- add a negative or boundary-only Class E example.

Do not restart as:

- a positive deployment example
- a medical, legal, financial, or other high-impact production claim

## Provenance maintenance

Deferred item:

- adding new public source references to provenance.

Current reason for deferral:

- provenance should remain source-lineage focused, not become a general changelog.

Restart conditions:

- the new item clarifies authorship, source lineage, or public concept development.
- the item is relevant to **責任経路 / Responsibility Pathway** or Responsibility Pathway Engineering.
- the wording remains attribution and traceability focused.

Allowed restart action:

- add a short dated entry or public-source reference to `docs/provenance.md`.

Do not restart as:

- a dispute log
- a general update log
- a certification record

## Restart audit checklist

Before restarting any deferred item, record:

- which deferred item is being restarted
- which restart conditions are satisfied
- which files prove those conditions
- what remains out of scope
- why the change is small enough for post-hoc audit

If those five points cannot be stated, keep the item deferred.
