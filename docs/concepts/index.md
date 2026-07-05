# Concepts Index

This index provides a short reader path for concept-level documents.

It is a navigation document only. It does not introduce schema fields, checker rules, workflow behavior, runtime connectors, production runtime, or Lean theorems.

## Core concept entry points

Start with:

- `docs/concepts/core-elements.md`

Then use the broader repository entry points:

- `docs/overview.md`
- `docs/source-mapping.md`
- `docs/source-scope-verification.md`
- `docs/example-index.md`
- `docs/checker-coverage.md`

## Source scope verification

Use `docs/source-scope-verification.md` when a claim, evidence source, workflow result, Lean file, AI summary, public article, citation, or non-claim boundary might be overread beyond its actual support.

It is a concept-level note for keeping claim, evidence, evidence type, source scope, validity owner, stop condition, and human return point connected.

Current boundary:

- concept-level only
- no schema enforcement
- no checker semantics
- no Lean theorem
- no external-review result
- no certification, conformance, production-readiness, legal, safety, compliance, or fairness determination
- no AI final-responsibility transfer

## Support-call and missed-support path

For support-call and missed-support concepts, read in this order:

1. `docs/related-work/strategic-decision-support.md`
2. `docs/concepts/support-call-policy.md`
3. `docs/concepts/missed-support-review-signal.md`
4. `docs/examples/missed-support-boundary-example-plan.md`
5. `docs/examples/missed-support-example-restart-audit.md`
6. `examples/missed-support-boundary-minimal.yaml`
7. `docs/examples/missed-support-workflow-observation.md`
8. `docs/examples/missed-support-current-status.md`
9. `docs/example-index.md`
10. `docs/checker-coverage.md`

## Support-call policy

`docs/concepts/support-call-policy.md` maps support-call policy to existing Responsibility Pathway Engineering concepts.

It treats support seeking as a responsibility-pathway question: when should an AI support node continue, and when should it return to a human, approval gate, stop authority, tool, evidence source, or repair owner?

Current boundary:

- concept-level only
- example-level only where explicitly marked
- no schema enforcement
- no checker semantics
- no production policy

## Missed-support review signal

`docs/concepts/missed-support-review-signal.md` defines missed support as a structural review signal.

It records that a pathway appears to have continued or nearly continued without support that should have been requested.

Current boundary:

- not legal liability determination
- not moral blame assignment
- not safety certification
- not compliance determination
- not fairness determination
- not production-readiness result
- not runtime correctness proof
- not connector correctness proof
- not AI final-responsibility transfer

## Concept to example connection

The current minimal example is:

- `examples/missed-support-boundary-minimal.yaml`

Its focused current status is recorded in:

- `docs/examples/missed-support-current-status.md`

The example is synthetic, local, boundary-only, non-production, and non-certifying.

## Future concept work

Future concept work should follow:

- `docs/deferred-work-restart-conditions.md`
- `docs/current-task-inventory.md`
- `docs/ai-agent-operation-patterns.md`
- `docs/operation-tool-selection-guard.md`

Do not move concept notes into schema, checker, runtime, connector, or Lean work without satisfying the relevant restart conditions.
