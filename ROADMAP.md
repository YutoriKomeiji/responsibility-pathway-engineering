# ROADMAP

This is the compact current planning map for Responsibility Pathway Engineering.

It is a planning aid only. It is not certification, conformance evidence, legal review, safety review, compliance review, fairness review, production approval, runtime correctness proof, or transfer of final responsibility to AI.

## Current position

RPE has completed the **bounded M2 governed-integration closure**. M3's adaptive responsibility gateway is being developed in an **unmerged Draft PR**; M3-only results are not yet the released public baseline. The closed M2 scope is the strict governed-evaluation and responsibility-preserving handoff surface described below; broader adaptive routing, security, trajectory, adoption, and production concerns remain post-M2 work rather than unfinished M2 implementation.

Public current-status detail: [`docs/m2-governed-integration-current.md`](docs/m2-governed-integration-current.md).

Implemented now:

- deterministic applicability resolution and multi-pack evaluation;
- legacy/M1-compatible Python entry via `evaluate_action()`;
- explicit strict governed Python entry via `evaluate_governed_action()`;
- governed contract families and runtime compatibility checks;
- exact pack/governance identity and version binding;
- strict governance eligibility for ownership, review state, ambiguity, effectivity, expiry, suspension, supersession, and related failure classes;
- explicit no-authority handoff semantics: `authority_effect = none`, `decision_scope = evaluation_only`;
- legacy and governed REST reference routes;
- legacy and governed MCP stdio tools;
- OpenAPI 3.1 coverage for governed admission/compatibility/governance/applicability/evaluation stages;
- packaged OpenAPI snapshot with repository/package drift checks;
- bounded caller-content and local-file governed-envelope loading;
- explicit rejection of network/registry loading in the first loader;
- schemas, synthetic fixtures, deterministic regression checks, and CI guards.

Current governed runtime path:

```text
Python / REST / MCP governed entry
        ↓
governed envelope admission
        ↓
contract compatibility
        ↓
pack ↔ governance binding
        ↓
governance eligibility
        ↓
applicability resolution
        ↓
pack evaluation and decision combination
        ↓
responsibility-preserving handoff
```

The legacy path remains available for compatibility. Governed evaluation is explicit rather than an optional gate that callers can accidentally omit.

The kernel evaluates explicitly scoped operational mappings. It is not a general legal reasoning engine, complete policy engine, production service, self-maintaining regulatory knowledge base, formally verified runtime, or execution-authority provider.

## Milestone checkpoint

### M1 — Governed Reference Kernel

Reached and retained as the compatibility baseline.

M1 established the shared deterministic kernel, bounded reference interfaces, pack-governance model, contract baselines, compatibility policy, reason-code stability rules, and explicit scope limits.

### M2 — Governed Pack Integration

**Closed within the declared bounded repository scope.**

M2 closure includes:

1. strict governed contracts and version coherence;
2. explicit governed admission, compatibility, binding, and normalized governance checks;
3. REST/MCP/OpenAPI governed adapter parity;
4. bounded caller-content/local-file loading with no network trust expansion;
5. responsibility-preserving handoff semantics;
6. adversarial checks for selected authority/evidence/governance/adapter/loader drift classes;
7. a bounded public value demonstration and exact closure evidence.

Closure evidence: [`docs/m2-r5-adversarial-closure-evidence.md`](docs/m2-r5-adversarial-closure-evidence.md).

This bounded closure does not absorb the post-execution state machine. Evaluation evidence is not effect evidence; repair readiness is not repair authority; resume authority belongs to the runtime/institution that owns execution. Broader adaptive routing and architecture reform are post-M2 concerns.

### M3 — Adaptive Responsibility Gateway

**Status: active experimental Draft PR #127, unmerged.** M1/M2 remain the
current merged implementation baseline.

The M3 working branch includes generalized responsibility-route descriptors,
adaptive controls, conditional risk graphs, caller-observed integrity, Human
Return readiness and cumulative-exposure guards; `0.2.0-exp` guarded Python,
REST/OpenAPI and MCP stdio interfaces; bounded malformed-input/error handling;
a reproducible cross-surface I/O parity demo; and a synthetic bank-detail change
preflight. All of these are **branch-scoped** until reviewed and promoted.

Remaining M3 acceptance work includes:
- independently review the end-to-end versioned I/O and current source/schema
  coherence, including unknown/ambiguous/hostile caller inputs;
- verify explicit downstream **pre-dispatch enforcement**, trust sources for
  Authority/Evidence and no bypass or effect/authority inflation;
- measure reproducible latency/resource/error behavior and onboarding burden;
- document realistic success, missing-evidence, conflict/hold and failure
  cases, with the exact host integration responsibilities;
- reconcile concurrent Draft documentation/value/quality PRs and run
  exact-final-head tests before considering merge/promotion.

External pilot/third-party production deployment is **not** a universal OSS
release requirement. It can support a later verified-effectiveness claim.
This planning status alone is not permission to merge, publish or deploy.

## Beyond M3 — candidate outcomes, not numbered milestones

**There is no formally defined M4 or later milestone yet.** The K0–K10
technical stages below and in the detailed technical roadmap are **not**
M4–M10 milestones. Candidates for future promotion are:

| Outcome lane | What can start before M3 closure | Evidence / owner boundary |
| --- | --- | --- |
| Integration-ready | machine-readable I/O, minimal starters, adapter parity, clear executor handoff | separate host enforcement, normal/error examples and measured integration effort |
| Secure-by-design | attack fixtures, payload and trust checks, configuration/authority preservation | identity, perimeter, secrets and network tenancy provided by host |
| Operational quality | bounded latency p50/p95/p99, failure modes, diagnostics, migration planning | production SLA, deployment, durability and recovery separately owned |
| Assured interoperability | frozen contracts, adversarial cases, formal assumptions, version consistency | third-party certification and real-effect claims require separate evidence |

Do not create new M numbers, adapters or governance sources merely because a
candidate lane is listed. Prioritize small, independently testable owner-local
slices; assign durable action execution and recovery to RPR/RPOS.

## Active gates

### Gate 1: keep documentation aligned with implementation

Active.

Keep these synchronized when package, adapter, governance, contract, loader, or claim surfaces change:

- `README.md`;
- `README.ja.md`;
- `READMEforAI.md`;
- `ROADMAP.md`;
- `docs/m2-governed-integration-current.md`;
- `docs/external-kernel-roadmap.md`;
- package and integration documentation;
- formalization and claim-boundary statements.

Reference adapters must not be presented as production services. Lean must not be presented as verification of the runtime or real-world outcomes.

### Gate 2: preserve one semantic kernel

Active.

Legacy interfaces delegate to `evaluate_action()` and governed interfaces delegate to `evaluate_governed_action()`. Adapters must not independently redefine applicability, governance, compatibility, requirement evaluation, decision precedence, or Human Return semantics.

The single-source guard is an implementation-drift check, not proof of semantic correctness or production safety.

### Gate 3: preserve strict governed admission

Implemented for the explicit governed entry.

Governed evaluation must fail visibly on incompatible contracts, invalid binding, ineligible governance, unresolved ambiguity, stale/invalid review state, and applicability uncertainty. A governed `allow` does not create execution authority.

### Gate 4: preserve contract/version source coherence

Implemented.

Runtime compatibility consumes the packaged version snapshot, while CI checks repository/package coherence. Version drift must fail visibly rather than silently changing semantics.

### Gate 5: keep loader trust bounded

Implemented for the first loader.

Caller-provided JSON and explicit local files are accepted within bounded limits. Network fetching, registry discovery, automatic updates, and remote trust establishment remain out of scope.

File existence is transport evidence only. It does not establish source authority, interpretation correctness, governance eligibility, or current validity.

### Gate 6: preserve evaluation/execution separation

Active as a permanent post-M2 architecture boundary.

RPE may state requirements for downstream effect evidence, repair, resume, and Human Return, but must not silently become the authority owner for dispatch, effect verification, retry/reconciliation, repair execution, or resume authorization.

### Gate 7: preserve M2 closure evidence

Completed for bounded M2 closure.

The closure matrix covers selected authority/evidence confusion, stale/binding/governance failures, adapter drift, loader boundary violations, runtime/schema alignment, and Human Return/residual-owner continuity. Future changes touching the closed surface must preserve or deliberately revise those checks.

### Gate 8: research production boundaries before production claims

Deferred until deliberately scoped.

Production adoption requires separate design and review for authentication, authorization, TLS, rate limiting, persistence, retention, tenancy, secrets, observability, deployment, rollback, operational ownership, and incident response.

## Front-loaded execution order

1. Preserve M2 as **closed** and fix mismatched current-state documentation.
2. Keep M3 work on its Draft branch; maintain Python/REST/MCP complete-result
   parity, malformed input cases, and explicit Authority/Evidence limits.
3. Test a minimal host-side pre-dispatch enforcement example that *consumes*
   RPE decisions but does not silently make RPE a runtime executor.
4. Measure bounded performance, integration cost and error handling with
   declared environment/inputs; present expected benefits as hypotheses until
   measured.
5. Consolidate overlapping M3 Draft PRs before exact-head integration review.
6. Review promotion/merge/release only under existing human maintainer gates.
7. Feed downstream execution/recovery and trajectory/legal-Authority research
   to their existing RP* owners.

## Recommended next sequence

1. Preserve the bounded M2 closure and its public/currentness checks.
2. Use DAN-65 / post-M2 architecture work for adaptive Responsibility Routing, conditional/trajectory risk, security, NFR, and adoption-profile redesign.
3. Keep production deployment concerns separately scoped and evidence-gated.
4. Feed material post-M2 findings upstream to RPD/RPM only through their own review/claim boundaries.
5. Add reviewed real-world mappings only with named human interpretation and maintenance ownership.

## Deferred work

Deferred unless reopened through a scoped design note and human maintainer decision:

- production deployment;
- automatic approval or action execution;
- network/registry Requirement Pack trust;
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
- hides pack age, ownership, review validity, compatibility, binding, or applicability uncertainty;
- changes an existing reason-code meaning without a compatible migration;
- treats file loading or schema validity as source trust;
- treats evaluation evidence as verified external effect;
- turns repair readiness into repair authority;
- resumes execution without a separate authority-bearing transition;
- executes an external action without a separate authority boundary;
- transfers final responsibility to AI.

## Detailed sources

- [`docs/m2-governed-integration-current.md`](docs/m2-governed-integration-current.md)
- [`docs/m2-governed-pack-integration-entry-plan.md`](docs/m2-governed-pack-integration-entry-plan.md)
- [`docs/contract-compatibility-policy.md`](docs/contract-compatibility-policy.md)
- [`docs/requirement-pack-governance.md`](docs/requirement-pack-governance.md)
- [`docs/claim-boundary-promotion.md`](docs/claim-boundary-promotion.md)
- [`docs/external-kernel-roadmap.md`](docs/external-kernel-roadmap.md)
- [`docs/architecture/external-responsibility-kernel.md`](docs/architecture/external-responsibility-kernel.md)
- [`docs/single-source-kernel.md`](docs/single-source-kernel.md)
- [`CHANGELOG.md`](CHANGELOG.md)

## Guiding principle

Small commits. Shared semantics. Named maintenance ownership. Explicit compatibility. Visible evidence. Human-return routes.

Human-scoped requirements precede controls. Controls precede claims. Claims precede deployment.
