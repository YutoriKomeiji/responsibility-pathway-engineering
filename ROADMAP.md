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
- requirement-pack governance lifecycle, ownership, review validity, expiry, and supersession checks;
- contract-family version manifest and compatibility policy;
- CI checks for package, REST, OpenAPI, MCP, governance, compatibility, repository security hygiene, and single-source kernel delegation.

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

## Milestone checkpoint

### M1 — Governed Reference Kernel

Reached as a bounded repository baseline after the compatibility-policy change is merged.

M1 means the repository has one shared kernel, bounded reference interfaces, pack-governance rules, contract baselines, compatibility rules, reason-code stability rules, and explicit scope limits.

M1 does not include external pack loading, runtime binding of governance eligibility, production services, or correctness claims for real-world source interpretation.

The next publication checkpoint is after M1 documentation is synchronized.

## Internal critical-review gate

Major implementation and claim-expansion work should pass the internal adversarial review described in [`docs/internal-critical-review.md`](docs/internal-critical-review.md).

The first recorded response is [`docs/critical-review-response.md`](docs/critical-review-response.md).

This internal review improves design discipline but is not independent external review or approval.

## Active gates

### Gate 1: keep documentation aligned with implementation

Active.

Keep these synchronized when package, adapter, governance, contract, or claim surfaces change:

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

### Gate 3: preserve pack governance

Implemented as a separate bounded governance layer.

The current governance checker covers lifecycle, owner, reviewer, approver, source version, scope, ambiguity, review dates, expiry, suspension, supersession, retirement, and human-return behavior.

Governance eligibility is not yet bound into `evaluate_action()`.

### Gate 4: preserve contract compatibility policy

Implemented as a documented baseline and checked manifest.

Current policy covers:

- independent contract-family versions;
- semantic version meaning;
- additive versus breaking changes;
- reason-code stability;
- unknown-version behavior;
- deprecation and migration requirements.

Runtime payloads do not yet carry explicit contract-version fields. Adding those fields requires a separate compatibility-reviewed change.

### Gate 5: separate reference adapters from operational SDK integrations

Next documentation task before adding another adapter.

Keep dependency-free adapters as bounded reference implementations. Before adding an operational adapter, evaluate established SDKs and maintained protocol libraries.

Any SDK-based adapter must remain thin and document dependency, protocol-version, security, and maintenance ownership.

### Gate 6: add bounded external pack loading

Blocked until governance and compatibility checks are intentionally connected.

External loading must preserve governance metadata and deterministic validation failures. Loading a pack must not imply that its source interpretation is correct or current.

### Gate 7: improve trace, repair, and resume

Candidate.

Extend result handling with explicit trace identifiers, evidence references, repair inputs, resume conditions, and return-to-human ownership. Avoid automatic execution or silent reopening.

### Gate 8: research production boundaries before production claims

Deferred until deliberately scoped.

Production adoption requires separate design and review for authentication, authorization, TLS, rate limiting, persistence, retention, tenancy, secrets, observability, deployment, rollback, operational ownership, and incident response.

## Recommended next sequence

1. Merge the contract compatibility baseline and mark M1.
2. Synchronize README and integration documentation for the M1 publication checkpoint.
3. Prepare the project progress article from the synchronized repository state.
4. Document reference adapters versus future SDK-based operational adapters.
5. Design the explicit governance-plus-compatibility gate before external pack loading.
6. Add external pack loading only after failure modes are testable.
7. Improve trace, repair, resume, and evidence structures.
8. Add reviewed real-world mappings only with named human interpretation and maintenance ownership.

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
- hides pack age, ownership, review validity, compatibility, or applicability uncertainty;
- changes an existing reason code meaning without a major-version migration;
- treats Lean or a checker pass as runtime or deployment proof;
- executes an external action without a separate authority boundary;
- transfers final responsibility to AI.

## Detailed sources

- [`docs/contract-compatibility-policy.md`](docs/contract-compatibility-policy.md)
- [`docs/requirement-pack-governance.md`](docs/requirement-pack-governance.md)
- [`docs/critical-review-response.md`](docs/critical-review-response.md)
- [`docs/internal-critical-review.md`](docs/internal-critical-review.md)
- [`docs/external-kernel-roadmap.md`](docs/external-kernel-roadmap.md)
- [`docs/architecture/external-responsibility-kernel.md`](docs/architecture/external-responsibility-kernel.md)
- [`docs/single-source-kernel.md`](docs/single-source-kernel.md)
- [`CHANGELOG.md`](CHANGELOG.md)

## Guiding principle

Small commits. Shared semantics. Named maintenance ownership. Explicit compatibility. Visible evidence. Human-return routes.

Human-scoped requirements precede controls. Controls precede claims. Claims precede deployment.
