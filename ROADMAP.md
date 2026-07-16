# ROADMAP

This is the compact current planning map for Responsibility Pathway Engineering.

It is a planning aid only. It is not certification, conformance evidence, legal review, safety review, compliance review, fairness review, production approval, runtime correctness proof, or transfer of final responsibility to AI.

## Current position

RPE now has a shared deterministic external-kernel implementation with multiple bounded interfaces.

Implemented now:

- applicability resolution for requirement packs;
- deterministic multi-pack evaluation;
- importable Python package API;
- local REST reference adapter;
- OpenAPI 3.1 contract served by the REST adapter;
- bounded MCP stdio reference adapter;
- source metadata and human-return routes;
- CI checks for package, REST, OpenAPI, MCP, repository security hygiene, and single-source kernel delegation.

Canonical runtime path:

```text
Python / REST / MCP
        ↓
rpe_kernel.evaluate_action()
        ↓
applicability resolution
        ↓
pack evaluation and decision combination
```

The current kernel evaluates explicitly scoped operational mappings. It is not a general legal reasoning engine, complete policy engine, production service, self-maintaining regulatory knowledge base, or formally verified runtime.

## Internal critical-review gate

Major implementation and claim-expansion work should pass the internal adversarial review described in [`docs/internal-critical-review.md`](docs/internal-critical-review.md).

The first recorded response is [`docs/critical-review-response.md`](docs/critical-review-response.md).

This internal review improves design discipline but is not independent external review or approval.

## Active gates

### Gate 1: keep documentation aligned with implementation

Active.

Keep these synchronized when package, adapter, or claim surfaces change:

- `README.md`;
- `README.ja.md`;
- `READMEforAI.md`;
- `ROADMAP.md`;
- `docs/external-kernel-roadmap.md`;
- package and integration documentation;
- formalization scope statements.

Reference adapters must not be presented as production services. Lean must not be presented as verification of the runtime or real-world outcomes.

### Gate 2: preserve one decision kernel

Active.

All runtime interfaces must delegate to `rpe_kernel.evaluate_action()`.

Adapters must not independently redefine applicability resolution, requirement evaluation, decision precedence, or human-return semantics.

The single-source guard is an implementation-drift check, not proof of semantic correctness or production safety.

### Gate 3: define pack governance before external loading

Next.

Define a requirement-pack lifecycle with at least:

```text
draft → reviewed → approved → active → suspended / superseded / retired
```

Define required ownership and maintenance fields:

- owner and reviewer;
- source authority and source version;
- jurisdiction and effective scope;
- interpretation status and unresolved ambiguity;
- effective date, last review, and next review due;
- supersession and retirement relationships;
- failure behavior when ownership or review validity is missing.

Expired, ownerless, ambiguous, or unreviewed packs must not silently produce an operational `allow` result.

### Gate 4: stabilize request, result, reason-code, and pack contracts

Next after the governance model.

Define explicit compatibility policy for:

- request schema version;
- result schema version;
- pack schema and lifecycle version;
- reason-code stability;
- additive versus breaking changes;
- deprecation and migration windows.

### Gate 5: separate reference adapters from operational SDK integrations

Candidate.

Keep the dependency-free adapters as bounded reference implementations. Before adding an operational adapter, evaluate established SDKs and maintained protocol libraries.

Any SDK-based adapter must remain thin and must document dependency, protocol-version, security, and maintenance ownership.

### Gate 6: add bounded external pack loading

Blocked until Gates 3 and 4 are sufficiently defined.

External loading must preserve governance metadata and deterministic validation failures. Loading a pack must not imply that its source interpretation is correct or current.

### Gate 7: improve trace, repair, and resume

Candidate.

Extend result handling with explicit trace identifiers, evidence references, repair inputs, resume conditions, and return-to-human ownership. Avoid automatic execution or silent reopening.

### Gate 8: research production boundaries before production claims

Deferred until deliberately scoped.

Production adoption requires separate design and review for authentication, authorization, TLS, rate limiting, persistence, retention, tenancy, secrets, observability, deployment, rollback, operational ownership, and incident response.

## Recommended next sequence

1. Complete pack lifecycle and maintenance-ownership design.
2. Define compatibility policy for packs, requests, results, and reason codes.
3. Reclassify and document reference adapters versus SDK-based operational adapters.
4. Add external pack loading only after governance and version failure modes are explicit.
5. Improve trace, repair, resume, and evidence structures.
6. Add reviewed real-world mappings only with named human interpretation and maintenance ownership.
7. Revisit production architecture after local contracts and governance have implementation experience.

## Deferred work

Deferred unless reopened through a scoped design note and human maintainer decision:

- production deployment;
- automatic approval or action execution;
- service-specific adapters that bypass the common kernel;
- legal or regulatory correctness claims;
- certification or conformance claims;
- automatic responsibility assignment;
- silent policy compilation without review diffs;
- real-world mappings without identified interpretation and maintenance ownership;
- claims that Lean verifies the Python runtime or real-world validity;
- public standardization claims.

## Stop conditions

Stop and preserve state if a proposed change:

- makes RPE sound like a finished standard or certified product;
- implies legal validity, safety, compliance, fairness, or production readiness;
- presents simple condition checks as complete real-world reasoning;
- lets an adapter redefine kernel semantics;
- adds an operational protocol implementation without considering maintained SDKs;
- hides pack age, ownership, review validity, or applicability uncertainty;
- treats Lean or a checker pass as runtime or deployment proof;
- executes an external action without a separate authority boundary;
- transfers final responsibility to AI.

## Detailed sources

- [`docs/critical-review-response.md`](docs/critical-review-response.md)
- [`docs/internal-critical-review.md`](docs/internal-critical-review.md)
- [`docs/external-kernel-roadmap.md`](docs/external-kernel-roadmap.md)
- [`docs/architecture/external-responsibility-kernel.md`](docs/architecture/external-responsibility-kernel.md)
- [`docs/single-source-kernel.md`](docs/single-source-kernel.md)
- [`CHANGELOG.md`](CHANGELOG.md)

## Guiding principle

Small commits. Shared semantics. Named maintenance ownership. Visible evidence. Human-return routes.

Human-scoped requirements precede controls. Controls precede claims. Claims precede deployment.