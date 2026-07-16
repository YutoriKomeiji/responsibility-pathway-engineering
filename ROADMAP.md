# ROADMAP

This is the compact current planning map for Responsibility Pathway Engineering.

It is a planning aid only. It is not certification, conformance evidence, legal review, safety review, compliance review, fairness review, production approval, runtime correctness proof, or transfer of final responsibility to AI.

## Current position

RPE has moved beyond the first small-program step and now has a shared external-kernel implementation with multiple bounded interfaces.

Implemented now:

- applicability resolution for requirement packs
- deterministic multi-pack evaluation
- importable Python package API
- local REST adapter
- OpenAPI 3.1 contract served by the REST adapter
- bounded MCP stdio adapter
- source metadata and human-return routes
- CI checks for package, REST, OpenAPI, MCP, repository security hygiene, and single-source kernel delegation

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

The adapters evaluate proposals only. They do not execute actions, approve deployments, merge code, publish releases, or transfer responsibility.

## Active gates

### Gate 1: keep documentation aligned with implementation

Active.

When the package or adapter surface changes, keep these synchronized:

- `README.md`
- `README.ja.md`
- `READMEforAI.md`
- `ROADMAP.md`
- `docs/external-kernel-roadmap.md`
- `docs/python-package-api.md`
- `docs/integrations/rest-api.md`
- `docs/integrations/openapi.md`
- `docs/integrations/mcp-stdio.md`
- `docs/single-source-kernel.md`

Implemented interfaces must not remain described as only planned work.

### Gate 2: preserve one decision kernel

Active.

All runtime interfaces must delegate to `rpe_kernel.evaluate_action()`.

Adapters must not independently redefine:

- applicability resolution
- requirement evaluation
- decision precedence
- human-return semantics

The single-source guard is a bounded implementation-drift check, not proof of semantic correctness or production safety.

### Gate 3: stabilize request and result contracts

Next.

Add an explicit compatibility policy for:

- request schema version
- result schema version
- reason-code stability
- additive versus breaking changes
- deprecation and migration windows

The OpenAPI contract should remain aligned with actual REST behavior and the package API.

### Gate 4: add bounded external pack loading

Candidate.

Design a small interface that can load external requirement packs while preserving:

- source metadata
- interpretation owner
- jurisdiction and version
- review status
- unresolved ambiguity
- deterministic validation errors

Loading a pack must not imply that its legal, regulatory, organizational, or social interpretation is correct.

### Gate 5: improve trace, repair, and resume

Candidate.

Extend result handling with explicit, reviewable support for:

- trace identifiers
- evidence references
- repair inputs
- resume conditions
- return-to-human ownership

Avoid automatic execution or silent reopening.

### Gate 6: research production boundaries before production claims

Deferred until deliberately scoped.

Production adoption would require separate design and review for at least:

- authentication and authorization
- TLS termination
- rate limiting
- persistence and retention
- tenancy isolation
- secrets handling
- observability
- deployment and rollback controls
- operational ownership
- incident response

The current local REST and MCP adapters are not production services.

## Recommended next sequence

1. Define request/result schema-version and compatibility policy.
2. Add a bounded external requirement-pack loader and checker.
3. Add one integration example at a time without duplicating kernel semantics.
4. Improve trace, repair, resume, and evidence structures.
5. Revisit production architecture only after the local contracts have implementation experience.
6. Develop reviewed real-world requirement packs only with source-specific human ownership.

## Deferred work

The following remain deferred unless reopened through a scoped design note and human maintainer decision:

- production deployment
- automatic approval or action execution
- service-specific connectors that bypass the common kernel
- legal or regulatory correctness claims
- certification or conformance claims
- automatic responsibility assignment
- silent policy compilation without review diffs
- real-world law mappings without identified interpretation ownership
- public standardization claims

## Stop conditions

Stop and preserve state if a proposed change:

- makes RPE sound like a finished standard or certified product
- implies legal validity, safety, compliance, fairness, or production readiness
- lets an adapter redefine kernel semantics
- hides applicability uncertainty
- drops reason codes, source metadata, or human-return routes
- treats a checker or workflow pass as deployment approval
- executes an external action from an evaluation result without a separate authority boundary
- transfers final responsibility to AI

## Detailed sources

- [`docs/external-kernel-roadmap.md`](docs/external-kernel-roadmap.md)
- [`docs/architecture/external-responsibility-kernel.md`](docs/architecture/external-responsibility-kernel.md)
- [`docs/single-source-kernel.md`](docs/single-source-kernel.md)
- [`docs/current-task-inventory.md`](docs/current-task-inventory.md)
- [`docs/progress-map.md`](docs/progress-map.md)
- [`docs/operation-index.md`](docs/operation-index.md)
- [`docs/roadmap-history.md`](docs/roadmap-history.md)
- [`CHANGELOG.md`](CHANGELOG.md)

## Maintenance rule

Keep this file compact. Put historical detail in focused notes, snapshots, `CHANGELOG.md`, and git history.

## Guiding principle

Small commits. Shared semantics. Visible evidence. Human-return routes.

Requirements precede controls. Controls precede claims. Claims precede deployment.
