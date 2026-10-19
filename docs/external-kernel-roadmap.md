# External Kernel Roadmap — technical stages K0–K10

This tracks RPE's portable, responsibility-preserving **evaluation** kernel.
K0–K10 are *technical scope stages*, **not** numbered product milestones:
K4 ≠ M4. For actual milestone gates, see [ROADMAP.md](../ROADMAP.md).

## Current position and authority boundaries

**M1:** compatibility reference kernel complete. **M2:** bounded
governed-integration baseline closed on merged `main`; consult
[the M2 closure evidence](m2-r5-adversarial-closure-evidence.md) and
[the current M2 contract](m2-governed-integration-current.md).
**M3:** adaptive responsibility gateway implementation in **unmerged Draft
PR #127**; no public-release/production-effect claim. **M4+:** not yet
formally defined, and no stage automatically grants milestone authority.

RPE evaluates proposals, scoped Requirement Packs, evidence declarations,
risk observations and responsibility transitions. It returns machine-readable
decisions and obligations, **not** execution Authority or proof of an external
effect. Authority and real-world verification belong to separately secured
downstream systems/institutions.

## Stage inventory and accurate maturity labels

| Stage | Scope | Current state |
| --- | --- | --- |
| **K0** Foundation | bounded actions, packs, results, reasons and Human Return | Implemented synthetic/reference baseline |
| **K1** Contracts and compatibility | versioned JSON Schemas, snapshots and drift checks | Implemented M1/M2; migration cases when an actual breaking change is proposed |
| **K2** Applicability/mapping | explicit scoped requirements; uncertainty/exception boundary | Bounded deterministic resolver; no automatic full legal reasoning |
| **K3** Pack governance | ownership/review/expiry, binding and eligibility | Strict M2 implemented; independent source trust still external |
| **K4** Runtime kernel package | legacy and strict governed evaluation; no-authority handoff | Bounded M2 closed; kernel remains separate from execution |
| **K5** Reference adapters and SDKs | Python, REST/OpenAPI, MCP stdio, experimental guarded routes | M2 merged; M3 enhanced interfaces and three-surface parity on Draft branch |
| **K6** Bounded loading | local/caller UTF-8 bytes and digest observation | M2 implemented; remote registry and author trust not established |
| **K7** Reviewed mappings | owner-reviewed real-world requirement sets | Synthetic by default; human maintenance/review needed before real claims |
| **K8** Handoff/uncertainty/recovery boundary | preserved residual owner, effect-vs-evaluation, retry/repair obligations | M2 handoff contract closed; durable effect/recovery owned by RPR/RPOS |
| **K9** Production architecture research | authentication, authorization, TLS, tenancy, quotas, observability, incident response | Threat work and bounded reference-adapter hardening; **not** production deployment |
| **K10** Formalization/interoperability | bounded invariants, other frameworks and client conformance | Experimental; formal acceptance alone does not verify runtime or live outcome |

The historical plan's “remaining M2” language for K8 is superseded by the
actual bounded M2 closure. The remaining durable post-execution work is an
explicit **downstream responsibility**, not silently incomplete M2.

## Integration I/O to provide before widening claims

```text
Agent / host proposal + scoped governance + caller-observed evidence
       ↓
M2 governed entry + optional experimental M3 risk/guard input
       ↓
RPE evaluation → control + reason codes + unmet conditions
                 + route metadata + residual owner
                 + authority_effect:none + execution_effect:none
       ↓
Host's separately authenticated, authorized PRE-DISPATCH decision
       ↓
Host executor / RPR / RPOS handles effect, audit, reconciliation, recovery
```

M3 experimental complete-response parity is executable via
`python scripts/demo_m3_cross_surface.py` or
`python scripts/demo_m3_cross_surface.py --json`.
See [M3 adoption profiles](m3-adoption-profiles.md) for precise I/O,
positive/missing-evidence/conflict examples and trust limitations. All three
surfaces must preserve the **same kernel semantics**; an adapter is not a new
authority provider. An RPE `allow` does not bypass the host's own checks.

## Front-load the dependency graph

1. **Now / K1, K5:** test request/framing/schema failures and exact
   Python/REST/MCP parity; preserve currently valid M2 success cases.
2. **Now / K5:** runnable starter paths, clear successful and adverse I/O,
   integration diagram, host responsibility and error handling.
3. **Now / K9 research:** bounded negative security/timeout/resource and
   performance tests; log assumptions, observed metrics and regressions.
4. **Now / K7 example:** synthetic business-specific policies with labelled
   caller-supplied signals, not invented domain-approved Authority.
5. **Separately / K8:** effect execution, retries, reconciliation,
   reauthorization and durability to RPR/RPOS owners.
6. **Later with evidence / K7/K9/K10:** real domain governance, production
   authentication/tenancy/operations, broad interop and formal assurance.

Integration-ready OSS does not require proof of third-party production use.
It *does* require precise API I/O, reproducible bounded tests, installable
examples, clear host-side enforcement obligations and truthful release
maturity. Claims of measured safety, operational SLO or ROI require their
own observations; do not invent them.

## Review/promotion conditions

Preserve closed M2 regressions; test M3 edge cases at exact PR head; measure
integration/latency where feasible; reconcile overlapping M3 Draft PRs;
decide M3 merge/release by existing maintainer/Human Gates. Do not create
M4+, production-security certification, legal compliance or real-world
impact claims merely by completing a roadmap entry.
