# RPE M2 Governed Pack Integration — Entry Plan

Status: Entry planning approved for repository work. Runtime integration and external loading remain bounded implementation work and do not authorize production deployment.

## Purpose

Define when and how RPE should move from the M1 Governed Reference Kernel into M2 Governed Pack Integration without collapsing governance eligibility, compatibility, applicability, requirement evaluation, execution authority, or final responsibility.

## M2 objective

M2 connects governed, versioned Requirement Packs to the canonical runtime decision path so that stale, ownerless, ambiguous, suspended, superseded, incompatible, or otherwise ineligible packs fail visibly and cannot silently produce `allow`.

M2 does not create:

- automatic legal or policy interpretation;
- self-updating regulation;
- production authorization;
- action execution authority;
- certification or compliance proof;
- transfer of final responsibility from the named human or institution.

## Entry assessment

### Already present from M1

- deterministic `evaluate_action()` entry point;
- applicability resolution;
- multi-pack evaluation;
- ordered outcomes: `allow < hold < human_gate < deny`;
- governance lifecycle model;
- governance checker and reason-code namespace;
- contract-family schemas and version manifest;
- Python, REST, OpenAPI, and MCP reference interfaces;
- synthetic fixtures and repository checks.

### Missing runtime links

- explicit contract-version fields in runtime request and decision payloads;
- governance eligibility enforcement inside the canonical kernel path;
- compatibility checks before pack evaluation;
- one canonical pack-selection and rejection trace;
- deterministic fixtures for stale, unsupported, suspended, superseded, ownerless, ambiguous, or expired packs;
- bounded external pack loader;
- trace, repair, resume, and evidence references.

## Start decision

RPE may begin **M2 Entry Phase** now.

RPE should not yet claim M2 completion, operational deployment readiness, or external governed-pack support.

The first implementation boundary is internal and fixture-driven. External file or network loading is blocked until governance and compatibility failures are connected to the canonical kernel and tested deterministically.

## Required implementation order

### M2-E1 — Runtime contract versioning

Add explicit version identifiers to:

- action request;
- requirement pack;
- governance record;
- gate decision;
- reason-code policy where carried by runtime metadata.

Unknown or unsupported versions must produce a visible non-allow outcome.

### M2-E2 — Canonical governance eligibility function

Move bounded governance eligibility logic from repository-only script use into an importable kernel module.

Requirements:

- one semantic source for governance eligibility;
- deterministic reason codes;
- explicit evaluation date or clock input;
- no silent fallback to eligible;
- configured human-return route;
- repository checker delegates to the same function.

### M2-E3 — Compatibility gate

Before applicability evaluation, verify:

- supported contract family and version;
- required migration state;
- deprecated-but-supported behavior;
- breaking incompatibility behavior.

Compatibility failure must not produce `allow`.

### M2-E4 — Governed evaluation pipeline

Canonical order:

```text
action request version check
→ pack version and compatibility check
→ governance eligibility
→ applicability resolution
→ requirement evaluation
→ strongest decision combination
→ trace and human return
```

Adapters must continue delegating to this single path.

### M2-E5 — Deterministic negative fixtures

Add fixtures and tests for:

- inactive lifecycle state;
- missing owner, reviewer, or approver;
- missing or expired review date;
- unreviewed interpretation;
- malformed ambiguity record;
- missing human return;
- superseded pack without valid replacement;
- unsupported contract version;
- ambiguous applicability;
- no applicable packs.

Each case must preserve visible reason codes and a non-allow result.

### M2-E6 — Bounded external pack loading

Only after E1–E5 pass:

- load local JSON by explicit path or supplied content;
- validate schema, version, compatibility, and governance before evaluation;
- reject stale or invalid records visibly;
- preserve source identity and content digest;
- do not add network fetching, remote registry trust, or automatic updates in the first loader.

### M2-E7 — Trace, repair, and resume references

Extend the decision envelope with:

- evaluation trace ID;
- selected and rejected pack references;
- evidence references;
- repair or missing-input route;
- resume condition;
- residual human owner;
- reopening triggers.

## Entry gates

### Gate A — repository implementation gate

Permits bounded code, schema, fixture, documentation, and test changes in the RPE repository.

Does not permit production deployment or connection to consequential live actions.

### Gate B — reviewed real-world mapping gate

Required before a non-synthetic public-guidance, law, standard, or organizational mapping is marked usable.

Requires named interpretation owner, reviewer, approver, source version, scope, ambiguity, maintenance schedule, expiry, and supersession route.

### Gate C — operational adapter gate

Required before connecting RPE to a live system that may produce externally observable or consequential effects.

Requires separate authentication, authorization, transport, persistence, incident response, observability, deployment binding, rollback, and operational ownership review.

## Completion criteria for M2

M2 may be described as reached only when:

1. runtime payload versions are explicit;
2. governance and compatibility checks run in the canonical kernel path;
3. all supported adapters delegate to that path;
4. invalid or stale packs fail visibly and deterministically;
5. a bounded external loader preserves source, version, governance, and digest;
6. positive and negative fixtures cover the main failure classes;
7. trace and human-return information is preserved;
8. documentation states the remaining non-production boundary;
9. no production, compliance, certification, or legal-validity claim is implied.

## Relationship to LuminaliaOS and LCA

- LCA supplies authority, effect, trust, replay, evidence, recovery, and Human Gate architecture.
- RPD supplies reviewed transformation from findings and authorized normative inputs into testable requirements.
- RPE M2 supplies governed runtime evaluation of approved machine-readable Requirement Packs.
- LuminaliaOS may later consume RPE as a bounded decision-support component, but RPE does not become the OS authority owner and does not execute actions by itself.

## Current decision

- M2 Entry Phase: ready to begin.
- M2 runtime integration: permitted as bounded repository implementation under current delegation.
- External pack loading: deferred until E1–E5 are complete and read back.
- Real-world mapping activation: separate Human Gate.
- Production or consequential live integration: separate Human Gate.
