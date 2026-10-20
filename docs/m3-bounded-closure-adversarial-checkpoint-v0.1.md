# RPE M3 bounded closure adversarial checkpoint v0.1

Status: branch-local review checkpoint / not a release / not a merge decision

## Purpose

Record the current bounded M3 engineering slice before adding further architecture. This checkpoint asks whether the implemented slice is internally coherent, externally bounded, and sufficiently defended against accidental scope expansion.

## Current implemented slice

The branch currently contains:

- additive Responsibility Gateway evaluation metadata;
- generalized responsibility-transition descriptors;
- declarative Risk Condition Graph evaluation;
- explicit fail-closed control-selection behavior;
- guarded adapter contract `0.2.0-exp` kept separate from the existing `0.1.0-exp` transition contract;
- guarded Python, REST, MCP, and OpenAPI surfaces;
- integrity, Human Return readiness, and cumulative-exposure guard observations;
- stateless cumulative-exposure evaluation with caller/policy supplied budgets and controls;
- runtime-output-to-OpenAPI validation;
- contract-documentation drift checking;
- bounded benchmark smoke and compatibility checks.

## Non-negotiable boundary

M3 remains an evaluation/control-selection metadata layer. It is not an executor, router, durable retry engine, recovery runtime, authorization service, or truth oracle.

The externally visible contract therefore preserves:

- `authority_effect = none`;
- `execution_effect = none`;
- `downstream_executor_required = true` where applicable;
- no external dispatch;
- no independent identity authentication;
- no certification that supplied authority, capability, evidence, or world-state claims are true;
- no durable trajectory-state ownership.

## Adversarial review findings

### 1. Version separation

The guarded `0.2.0-exp` surface is separate from the `0.1.0-exp` surface rather than silently mutating the original contract. This is a compatibility strength and should remain explicit.

### 2. Guard composition

Integrity, Human Return readiness, and cumulative exposure are represented as observations that may introduce caller/policy controls. They do not independently invent normative authority. Conflicting required controls remain an explicit selection problem rather than being silently resolved.

### 3. Cumulative exposure

The cumulative-exposure slice is intentionally stateless. The caller supplies current usage, proposed increment, budget, unit, and optional evidence references. The result describes whether the supplied proposed transition is within budget, at the limit, exceeded, unknown, or invalid.

This must not drift into a claim that RPE itself maintains durable long-horizon counters or proves trajectory safety. Durable trajectory state and long-horizon invariants remain separate owners.

### 4. Human Return

Human Return readiness is an evaluation input, not proof that a human or institution is willing, able, timely, competent, or authorized to intervene. Reviewer capacity and intervention effectiveness remain separate empirical/organizational questions.

### 5. Verification ceiling

Schema validation, CI success, runtime/OpenAPI parity, and bounded tests establish properties of the current artifact and its declared contract. They do not establish production effectiveness, legal adequacy, organizational authorization, universal safety, or real-world correctness.

`FORMAL OR TESTED PROPERTY OF ARTIFACT != PROPERTY OF WORLD`

## Closure candidate criteria

This bounded M3 slice may be treated as internally closed for the current checkpoint when all of the following remain true at the exact branch head:

1. guarded core, REST, MCP, OpenAPI, and schema checks are green;
2. existing 0.1 compatibility checks remain green;
3. documentation-drift check remains green;
4. cumulative exposure remains stateless and non-normative;
5. no public artifact contains claims larger than the tested/evidenced slice;
6. no new feature is being added merely because it is conceivable rather than because a defined M3 obligation remains open.

Closure here means `BOUNDED_ENGINEERING_SLICE_CLOSED`, not M3 complete, release-ready, production-ready, or merged.

## Remaining owners / not closed by this checkpoint

- autonomy-envelope semantics beyond explicit policy-supplied dimensions;
- durable long-horizon trajectory state;
- production NFR/SLO evidence;
- independent integration/adoption evidence;
- reviewer-capacity and Human Return effectiveness evidence;
- broader security threat families not represented by the current three guarded observation classes;
- any claim that a transition is substantively safe in the external world.

## Next decision

Prefer one of two paths after exact-head readback:

1. declare this slice a bounded closure checkpoint and move unresolved obligations to named owners/research items; or
2. add only a narrowly defined M3 feature whose obligation cannot be represented by the current contract.

Do not continue broad feature accumulation without a named unresolved obligation.