# RPE M3 post-closure owner map v0.1

Status: branch-local planning record / not a release / not a merge decision

## Purpose

Prevent a boundedly closed M3 engineering slice from reopening through undifferentiated feature accumulation. Remaining obligations are routed to named owners or explicit future work rather than being implicitly absorbed into the current gateway slice.

## Closed slice

The current bounded slice is closed as `BOUNDED_ENGINEERING_SLICE_CLOSED` at exact-head CI evidence recorded under DAN-65. Closure applies to the implemented gateway, guarded adapter `0.2.0-exp`, REST/MCP/OpenAPI parity, current three guard-observation families, schema/runtime parity checks, documentation-drift checks, and stateless cumulative-exposure evaluation.

This does not imply release, merge, production readiness, complete security coverage, or completion of all M3 research scope.

## Remaining obligations and owners

### Durable trajectory state and long-horizon invariants

Owner: DAN-28 or a successor trajectory-assurance owner.

RPE may evaluate caller-supplied cumulative state but does not become the durable counter/history owner.

### Policy semantics and authority basis

Owner: DAN-9 or the current Policy / Authority Engine owner.

RPE may report missing/conflicting authority/control requirements but does not manufacture authority or certify supplied authority as true.

### Formalization

Owner: DAN-14 / current Lean assurance owner where a proposition is narrow enough to formalize.

Formal results remain properties of specified artifacts/models, not the external world.

### Production NFR / SLO evidence

Owner: future deployment/operations evidence track.

Latency smoke, schema parity, and CI do not establish production availability, p95/p99, capacity, incident response, or deployment fitness.

### Independent integration and adoption evidence

Owner: DAN-63 / future external adoption track as applicable.

Repository-local examples and tests are constructive evidence, not independent adoption or effectiveness evidence.

### Human Return effectiveness / reviewer capacity

Owner: RPM/DAN-64 research feedback and any future empirical Human Return study.

A named destination or readiness descriptor does not prove willingness, expertise, attention, response time, institutional capability, or effective intervention.

### Broader security families

Owner: security research/prototype tasks opened only for concrete threat obligations.

Current integrity/readiness/exposure observations are not exhaustive coverage of injection, supply chain, path shaping, resource abuse, cross-agent escalation, recovery-path attacks, or other threat families.

### Memory/provenance hardening

Owner: DAN-21 and the external-mechanism assimilation queue where applicable.

Provenance, memory verification, and lifecycle findings may feed future RPE requirements, but provenance must not be collapsed into truth, Evidence Sufficiency, or Authority.

## Reopen rule

The bounded M3 slice should reopen only when at least one of the following is true:

1. a current contract or implementation defect is observed;
2. a current documented claim exceeds exact tested behavior;
3. an upstream/downstream integration exposes a concrete missing obligation that belongs specifically to the gateway layer;
4. a security or evidence failure demonstrates that the existing boundary is insufficient and the responsibility cannot be assigned to another owner;
5. a Human Gate explicitly requests a new bounded M3 deliverable.

`Interesting`, `possible`, or `adjacent research exists` is not by itself a reopen trigger.

## Control rule

For every proposed M3 addition after this checkpoint, record:

`observed obligation -> why current contract cannot represent it -> why RPE is the correct owner -> minimum bounded change -> verification -> residual owner`.
