# Roadmap Alignment Plan: Provenance and Support-Call Policy

This plan aligns two recent work streams with the repository roadmap:

1. Responsibility Pathway provenance preservation
2. Strategic decision support / support-call policy as related work

It is a planning note only. It does not modify schemas, examples, checkers, workflows, runtime connectors, production runtime, or Lean formalization.

## Why this plan exists

The repository recently added stronger provenance statements to `README.md` and `README.ja.md` for the public source lineage of **責任経路 / Responsibility Pathway**.

The repository also added `docs/related-work/strategic-decision-support.md`, which connects the paper "Strategic Decision Support for AI Agents" to RPE as a support-call policy and missed-support signal.

Both additions are useful, but they belong at different roadmap layers.

This plan prevents provenance preservation, related-work mapping, schema design, checker implementation, runtime integration, and Lean formalization from being mixed too early.

## Roadmap placement

### Phase 0: Foundation

Relevant role:

- README and README.ja are foundational public entry points.
- Authorship, citation, notice, and source traceability are foundation-level concerns.

Current alignment:

- `README.md` now records the author's own development record for **責任経路 / Responsibility Pathway**.
- `README.ja.md` records the same provenance in Japanese.

Planned low-risk work:

- Add or update `docs/provenance.md` as a detailed provenance record.
- Connect `AUTHORSHIP.md` to the provenance record.
- Connect `NOTICE.md` to the provenance record.
- Consider whether `CITATION.cff` should include related public-source references without overloading citation metadata.

Do not use Phase 0 provenance work to make legal accusations, ownership adjudications, certification claims, or production-readiness claims.

### Phase 1: Concept Models

Relevant role:

- Phase 1 contains responsibility node, return point, value flow, cost flow, repair model, stop authority, evidence log, action class matrix, approval gate, decision owner, and source mapping.

Current alignment:

- Provenance supports the concept model by preserving the public source lineage for the term and concept.
- Strategic decision support contributes a related concept: when an AI agent should seek support instead of acting alone.

Planned low-risk work:

- Treat support-call policy as a concept-level relation, not a schema field yet.
- Map support-call policy to existing concepts:
  - Human Return Point
  - Approval Gate
  - Stop Authority
  - Evidence Log
  - Repair Owner
  - Decision Owner
- Treat missed-support error as a non-certifying structural signal.

Do not introduce new canonical concepts until the mapping to existing Phase 1 concepts is clear.

### Phase 1.5: Specification Binding

Relevant role:

- Phase 1.5 binds concept documents to minimal machine-readable specifications.

Current alignment:

- No schema change has been introduced by the provenance work or the strategic decision support related-work note.

Planned low-risk work:

- Keep support-call policy out of schema until examples and concept mapping are stable.
- If future schema work is considered, first write a design note that explains whether support-call policy belongs in a node, action class, pathway, evidence log, or review-result layer.

Deferred work:

- support-call policy schema fields
- missed-support schema fields
- runtime-event schema changes
- JSON fixture checking for support-call policies

### Phase 1.6: Lightweight Validation and Lifecycle Examples

Relevant role:

- Phase 1.6 contains bounded structural checks, lifecycle examples, action-class examples, checker coverage, example index, and validation boundaries.

Current alignment:

- Strategic decision support suggests a future review signal: missed support.
- Current checkers do not check support-call policies or missed-support signals.

Planned low-risk work:

- Record support-call policy and missed-support as future example-review concepts only.
- Update example-index or checker-coverage only after at least one small, readable example exists.
- Keep Class E positive examples deferred.

Deferred work:

- action-class-specific enforcement for support-call policy
- checker enforcement of missed-support signals
- high-impact positive support-call examples

### Phase 2: Formalization

Relevant role:

- Phase 2 formalizes small, assumption-scoped invariants.

Current alignment:

- No Lean change has been introduced by the provenance work or strategic decision support note.

Planned low-risk work:

- Do not formalize strategic decision support yet.
- If future formalization is considered, first stabilize examples, schema boundaries, checker boundaries, and concept mapping.

Deferred work:

- Lean support-call policy theorem
- Lean missed-support invariant
- Lean runtime-event support-seeking formalization

### Phase 2.5: Enterprise Implementation Profile

Relevant role:

- Phase 2.5 covers enterprise adoption, record review, review-result schema, bounded review-result checker, and non-certifying review processes.

Current alignment:

- Missed-support can be useful as a future review-result observation, but it is not currently part of review-result schema or checker behavior.
- Provenance can support authorship and traceability for public-facing enterprise readers.

Planned low-risk work:

- Keep missed-support as a possible future review note or review-result extension.
- Keep provenance language visible but non-accusatory.
- Do not present strategic decision support as enterprise compliance, safety certification, legal review, or production approval.

Deferred work:

- review-result schema extension for missed support
- checker extension for support-call review results
- enterprise deployment guidance that treats support-call optimization as compliance evidence

### Phase 3: Reference Implementations

Relevant role:

- Phase 3 adds small bounded reference examples while avoiding production or certification claims.

Current alignment:

- Strategic decision support can eventually inform a small reference example where an AI support node must choose whether to ask for human, tool, or evidence support.

Planned low-risk work:

- Add only a boundary-oriented or negative example first if support-call examples are introduced.
- Prefer an example showing missed-support risk over a high-impact positive deployment claim.
- Keep examples manually readable and non-certifying.

Deferred work:

- production-service support-call examples
- medical, legal, financial, or other high-impact positive support-call examples
- automated support-call execution without human review

### Phase 3.1: Adapter Boundary and Runtime Event Bridge

Relevant role:

- Phase 3.1 defines the bridge from external logs, API events, workflow results, and runtime observations into Responsibility Pathway records.

Current alignment:

- Strategic decision support is closely related to Phase 3.1 because support-call decisions may appear in runtime observations.
- However, the current runtime bridge remains synthetic, vendor-neutral, review-required, and non-production.
- Current runtime-event checking remains deferred.

Planned low-risk work:

- Treat support-call policy as a possible future runtime observation concept.
- Treat missed-support as a possible future review signal in runtime-event-to-pathway records.
- Keep support-call policy separate from service-specific connectors.
- Keep runtime-event checker work gated by `docs/runtime-event-checking-plan.md`.

Deferred work:

- support-call runtime fixture
- runtime-event schema changes for support-call decisions
- runtime-event checker support for missed-support signals
- workflow checks for support-call policies
- service-specific connector behavior
- production runtime integration

## Recommended execution order

Use this order unless a checker failure or serious inconsistency appears.

1. Create `docs/provenance.md` for detailed public source lineage.
2. Connect `AUTHORSHIP.md` to `docs/provenance.md` with a short reference.
3. Connect `NOTICE.md` to `docs/provenance.md` with a short non-accusatory attribution boundary.
4. Add a small related-work index if more related-work notes are added.
5. Connect `docs/related-work/strategic-decision-support.md` to `docs/example-index.md` or `docs/checker-coverage.md` only after a concrete support-call example or review note exists.
6. Consider a small boundary-only example for missed-support risk.
7. Only after examples remain stable, consider whether schema design is needed.
8. Only after schema and examples remain stable, consider bounded checker planning.
9. Only after checker planning remains stable, consider workflow integration.
10. Keep Lean support-call formalization deferred until the concept, examples, schemas, and checker boundary are stable.

## Current next task

The next roadmap-aligned task is:

- create `docs/provenance.md`

Reason:

- README and README.ja now contain concise provenance statements.
- A standalone provenance document can preserve detailed source lineage without overloading README.
- This is a Phase 0 / Phase 1 alignment task and does not unlock schema, checker, runtime, or Lean work.

## Non-goals

This plan does not authorize:

- legal claims
- plagiarism accusations
- ownership adjudication
- certification claims
- safety claims
- compliance claims
- fairness claims
- moral-resolution claims
- production readiness claims
- connector correctness claims
- adapter correctness claims
- runtime correctness claims
- AI final-responsibility transfer

## Stop conditions

Stop and preserve state if:

- a planned update starts implying legal accusation or ownership adjudication
- support-call policy starts being treated as production approval
- missed-support starts being treated as legal, safety, compliance, or fairness proof
- schema work begins before examples and concept mapping are stable
- checker work begins before schema and examples are stable
- runtime workflow work begins before checker behavior exists
- Lean work begins before the modeling boundary is clear
