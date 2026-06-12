# Reference Implementation Boundary

This document defines the boundary for future reference implementations in Phase 3.

It is not a reference implementation. It is a gate before reference implementations are added.

## Purpose

Reference implementations should show how Responsibility Pathway Engineering can be represented in small, readable, reusable implementation examples.

They should help readers move from definitions, schemas, examples, checkers, and record-review guidance toward practical patterns without turning the repository into a production product, certification system, legal decision system, compliance engine, safety tool, fairness tool, or moral-resolution system.

## Phase 3 entry rule

Phase 3 should begin with boundary-preserving reference examples, not large systems.

A reference implementation must not outrun:

- core definitions
- the eight-element model
- current schemas
- example boundaries
- checker boundaries
- review-result boundaries
- Lean assumptions
- theorem-role notes
- enterprise implementation guidance
- Responsibility Pathway record review guidance
- validator-boundary documentation
- excluded claims

If an implementation cannot clearly point back to those materials, it should not be added yet.

## Allowed first reference implementation types

The first Phase 3 reference implementations may include small examples such as:

- a simple human-AI review workflow
- a small evidence-record flow
- a small repair-record flow
- a small suspension/return flow
- a small closure/reopening flow
- a minimal command-line or script example that reads an existing fixture and explains its boundary

Each example should remain small enough to review manually.

## Not allowed yet

Phase 3 should not begin with:

- production services
- hosted applications
- legal decision tools
- safety certification systems
- compliance certification systems
- fairness certification systems
- moral-resolution engines
- automated governance replacement tools
- AI final-responsibility assignment tools
- large multi-agent demonstrations that cannot be traced back to the current definitions and boundaries

## Required boundary language

Every reference implementation should state:

- what it demonstrates
- what files, schemas, examples, or checkers it depends on
- what it does not demonstrate
- what claims are excluded
- where responsibility returns to a human or institution

A reference implementation may say that a bounded structural check passed.

It must not say that a workflow, system, organization, decision, deployment, or AI output is legally valid, safe, compliant, fair, morally resolved, institutionally certified, production ready, or approved for real-world use.

## Relationship to checkers

Reference implementations may call bounded repository-maintenance checkers such as:

- `scripts/check_examples.py`
- `scripts/check_review_results.py`

A passing checker result means only that the implementation or fixture satisfied the limited structural rules implemented by that checker version.

It does not certify real-world correctness, safety, legality, fairness, compliance, morality, production readiness, or final responsibility.

## Relationship to GitHub Actions

Reference implementations may rely on existing GitHub Actions workflows as maintenance signals.

Observed green workflow status means only that the relevant bounded checker completed successfully for the files in that run.

It is not certification.

## Recommended first step

The recommended first Phase 3 implementation step is a small human-AI review workflow example that:

- uses a human or institutional return point
- includes an AI support node only as support
- records evidence
- records what was checked
- records what was not checked
- records what is not claimed
- preserves the responsibility boundary
- remains readable without running a service

This should be introduced only after this boundary document is linked from ROADMAP, BEACON, README, and README.ja.

## Stop conditions

Pause Phase 3 expansion if a reference implementation:

- looks like a product launch instead of a reference example
- implies certification
- implies legal validity
- implies safety, compliance, or fairness certification
- implies moral resolution
- implies production readiness
- assigns final responsibility to an AI support node
- cannot point back to the current definitions, schemas, examples, checkers, Lean assumptions, enterprise guidance, record-review guide, validator boundary, and excluded claims

## Restart point

Before adding a Phase 3 reference implementation, read:

1. `docs/phase-2-5-current-snapshot.md`
2. `docs/validator-boundary.md`
3. `docs/checker-coverage.md`
4. `docs/responsibility-pathway-record-review.md`
5. `docs/enterprise-implementation-profile.md`
6. `spec/pathway.schema.yaml`
7. `spec/review-result.schema.yaml`
8. `examples/record-review-minimal.yaml`
9. `fixtures/review-results/record-review-result-minimal.yaml`
10. this document
