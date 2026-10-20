# RPE M3 — Integration and Operator Guide (experimental)

**Status:** implementation on unmerged Draft PR #127, guarded contract `0.2.0-exp`. The merged `main` baseline is bounded M2. This guide is **not** a public release, production certification, or assignment of operational Authority.

## Purpose and connection boundary

RPE evaluates an AI agent's proposed action against an explicitly governed Requirement Pack, caller-declared evidence and optional risk/guard observations. It returns a machine-readable *evaluation and responsibility transition*, so an integrating host can distinguish continuation, evidence/authority requests, escalation, holding and denial. RPE **does not** authenticate the caller's claims, authorize actual dispatch, execute tools, maintain durable retry state or certify external effects.

```text
AI/tool proposal (untrusted) + institution-supplied governance/evidence
      ↓ trusted host selects exact actor, target, policy and evidence context
RPE guarded evaluation (NO dispatch or new Authority)
      ↓ structured M2 evaluation, M3 control, reason codes, unmet conditions
trusted host verifies its own independent authorization and enforces control
      ↓ allowed only if RPE and host independently permit the exact action
separate executor / RPR / RPOS owns external effect, audit, reconciliation
```

The *trusted host* and RPE are separate components; a model-produced claim about identity, out-of-band approval, source trust, budget or evidence must never become verified merely by appearing in a request.

## Reproduce from the M3 Draft

Requires Python 3.11+, from the repository root:

```bash
git clone https://github.com/YutoriKomeiji/responsibility-pathway-engineering.git
cd responsibility-pathway-engineering
git checkout akihisaono0118/dan-65-rpe-m3-adaptive-responsibility-gateway-architecture-reform
python -m pip install .
python scripts/demo_m3_cross_surface.py
python scripts/demo_m3_cross_surface.py --json
python scripts/demo_m3_host_enforcement.py
python examples/business-controls/vendor_bank_change_preflight.py --self-test
```

The cross-surface demo starts a **loopback** REST server and exercises the MCP JSON-RPC stdio handler; it compares **complete JSON results** against direct Python results for four synthetic requests. The host demo records a **simulated** effect in an in-memory list, not an ERP/bank/network write. They are reproducibility evidence under declared conditions, not an end-to-end deployment trial.

## First five minutes: one command, then details

After installing the M3 Draft as above, run `python scripts/try_m3.py` (or `python scripts/try_m3.py --json`). It calls the existing **real** cross-surface parity demo and **synthetic** host-enforcement demo; it does not invent expected outputs. The summary shows which inputs receive `allow`, `hold`, `require_authority`, or non-allow, confirms six bad/unauthorized paths did not reach the simulated executor, and reports **zero real external effects**. A green local check establishes only that the selected reference scenarios pass, not a secure deployment. If a check fails, the script exits nonzero and does not claim success.

A first-time adopter can then examine `--json` and the two underlying scripts for full I/O and the trusted-host responsibility boundary. Reusable copy-and-paste starter packaging for other systems remains with DAN-83 rather than this reference command.

## Exact input and output contracts

All three guarded surfaces accept the same JSON-compatible payload with `contract_version: "0.2.0-exp"` and a **complete governed M2 envelope** in `governed_evaluation`. Optional `risk_graph`, `integrity_checks`, `human_return_checks`, `cumulative_exposure_checks`, `requested_route` and `constraints` have strict schemas. The caller/policy layer supplies the control requirements; the adapter cannot invent normative policy.

| Surface | Invocation | Result representation |
| --- | --- | --- |
| Python | `rpe_kernel.guarded_adapter.evaluate_guarded_adapter_request(payload)` | Python dict |
| REST (loopback reference) | `POST /v1/evaluate/transition/guarded` with JSON body | JSON object; HTTP 200 may still contain `hold` |
| MCP stdio (reference) | JSON-RPC `tools/call`, name `rpe_evaluate_guarded_responsibility_transition`, `arguments: payload` | `result.structuredContent` and equivalent JSON text |

A useful top-level *shape*, **not a complete valid governed request**, is:

```json
{"contract_version":"0.2.0-exp","governed_evaluation":{},"risk_graph":{"conditions":[]}}
```

For an executable **complete** request, run `python scripts/demo_m3_cross_surface.py --json`: it emits each actual governed fixture input and the observed output. Do not copy the empty placeholder into production.

Input schema: [guarded-adapter-request](../schemas/m3/guarded-adapter-request.schema.json). Output schema: [guarded-adapter-response](../schemas/m3/guarded-adapter-response.schema.json). Semantics and invariant ceilings: [versioned guarded contract](m3-versioned-guarded-adapter-contract-v0.1.md).

Output inspection:

| Output | Host interpretation |
| --- | --- |
| `evaluation_result` | Strict M2 admission/governance/applicability decision, possibly null on invalid outer request |
| `guard_observations` | Caller-observed integrity, return readiness and exposure results; not identity or evidence truth |
| `risk_condition_result` | Bounded conditional-risk evaluation; can be null |
| `transition_result.control_action` | Evaluation's next control, **not a dispatch permission** |
| `transition_result.reason_codes`, `unmet_conditions` | Explanation and outstanding requirements |
| `transition_result.responsibility_transition.residual_owner_role` | Residual owner role descriptor; does not prove reviewer capacity |
| `authority_effect`, `execution_effect` | `none`, regardless of an `allow` evaluation |

Version incompatibility, malformed or missing fields, conflicting controls, transport errors, untrusted provenance and timeouts must never be converted to `allow` by a host. A successful HTTP status or MCP tool response is **not** proof of operational authorization.

## Adverse cases and enforcing results

Run `python scripts/demo_m3_cross_surface.py --json` for observed request/response values rather than inventing a static expected JSON payload.

| Synthetic scenario | Expected M3 state | Required host continuation |
| --- | --- | --- |
| Valid approval evidence and no risk flags | `allow` | Separate actor/target/action authorization before dispatch |
| Missing approval evidence | Not `allow` | Obtain/verify required evidence; no dispatch |
| Caller-observed account mismatch | `require_authority` | Independent authority verification, not agent self-approval |
| Unknown field in risk graph | `hold` | Stop and correct the envelope; never silently discard unknown fields |

The host enforcement demo separately rejects missing host grant, wrong actor/target, missing RPE evidence, caller-flagged mismatch and a forged `authority_effect`. Its positive case is a local **synthetic dispatch**, not a real-world effect. For a business-specific example, see [vendor bank-detail preflight](../examples/business-controls/vendor_bank_change_preflight.py); out-of-band and dual-control booleans are explicitly **synthetic caller-provided observations**.

## Trust, security, error and recovery contract

- Host owns identity authentication, credentials, authorization for exact operation/target, independent evidence collection, approved Pack governance, prevention of alternative bypass paths, secrets and logs.
- RPE reference REST binds `127.0.0.1` by default. It has a 1 MiB request cap, explicit JSON/Content-Length framing, duplicate-field rejection and a 10-second body-read timeout; it has **no production TLS, authentication, tenancy isolation, public-network rate limiting or comprehensive resource quotas**. Never expose it directly on a public interface.
- MCP stdio input uses a 1 MiB line limit and rejects duplicate keys/non-finite constants. The MCP host must still isolate the process, tool privileges, memory and resource budgets and must not treat tool descriptions as policy Authority.
- Host checks both the M2 decision and M3 `control_action`, contracts and required conditions; `allow` alone is **necessary but not sufficient**. If any check fails or the result cannot be trusted, there is **no dispatch**.
- A re-evaluation is not permission to retry a previously dispatched action. RPR/RPOS or the execution-owning institution must separately handle effect verification, uncertain outcomes, idempotency, reauthorization, reconciliation, repair and resume.

See the [REST adapter boundary](integrations/rest-api.md), [MCP reference](integrations/mcp-stdio.md), and [OpenAPI contract](integrations/openapi.md). The [M3 adoption profiles](m3-adoption-profiles.md) distinguish Thin, Governed and not-yet-complete Assured.

## What AI agents may gain — expected, not yet observed in production

The interface can make missing evidence, control requirements, residual owners and explanations machine-readable; its **expected** benefit is less ambiguous continuation and more auditable handoffs *when* the host actually enforces the result. Do not invent incident-reduction rates, performance SLOs or ROI.

| Proposed measure | Required evidence method |
| --- | --- |
| Adapter coherence | Frozen same-payload comparisons across Python, REST, MCP; count mismatches |
| False permit vs false hold | Human-labeled benign and adversarial fixtures with expected outcomes |
| Integration burden | Actual code-change size, clean-install steps and developer time |
| Latency p50/p95/p99 | Sample size, environment, warmed/cold workload, raw observations and overhead baseline |
| Reviewer workload | Count and time human returns, quality of missing-evidence explanation |
| External impact | Separately observed executor effects, verified incidents and deployment conditions |

No third-party production pilot is a **universal prerequisite** for a truthfully scoped experimental OSS release. Production safety, compliance, independent security assurance and operational effectiveness remain separate claims needing separate evidence and review.

## Owners and promotion

RPE / DAN-65 owns evaluation contracts, adapter parity and Draft M3 evidence; DAN-117 tracks cross-RP* security hardening; DAN-83 owns reusable starter packaging; DAN-91 and DAN-50 own reader and release-surface coordination. RPR/RPOS and the adopting institution own execution/effect/recovery. Companion Draft PRs #130/#131/#132 must be reconciled without duplicating their owner work. M4+ is not formally defined. **No merge, publication, certification or deployment is authorized by this document.**
