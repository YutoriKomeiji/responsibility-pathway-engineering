# Agent security competitive landscape and RP* falsification — 2026-10

**Status:** exploratory research note on RPE M3 Draft only. **Not a canonical market verdict, security certificate, legal determination, feature implementation, M4 definition, publication permission or evidence of RP* superiority.**

## Research question

If established vendors already provide identity, policy enforcement, sandboxing, telemetry and agent governance, does RPE/RPR/RPOS create distinct and adoptable value? Compare **specific operational obligations**, not names, architectures or marketing. An overlapping product does not invalidate the project; neither does an unproven feature list establish the need for RP*.

Review evidence is **vendor documentation / repositories**, not independent product testing. Status must be rechecked by version/date before decisions.

## Competitive reference scan (vendor claims unless independently demonstrated)

| Product or category | What documentation actually covers | Important boundary / challenge to RP* |
| --- | --- | --- |
| **NVIDIA OpenShell** | Sandboxed AI agent execution, network egress policy, filesystem and process restrictions, isolated model-provider credential routing; uses **OPA policy engine** for network rules; separate audit vs enforce modes. NVIDIA Sentry extends external hardware-based monitoring. | RPE should **not** reinvent sandboxing, generic runtime deny-by-default or OPA policy checks. OpenShell's documented operator approvals and policy-revision lifecycle must be compared with any proposed RP* responsibility transition. Its docs caution about alpha maturity and audit mode not blocking actions. |
| **AWS Bedrock AgentCore Gateway / Policy** | Identity and gateway-bound Cedar/Dogwood authorization of agent tool calls by principal/action/resource; explicit LOG_ONLY vs ENFORCE; tool-level policy metrics/traces and temporal policy capabilities. | Generic MCP pre-tool authorization, typed policy decisions and observability are **already occupied**. Must inspect how policy approval, session authority, partial/external effect, durable human obligations and cross-vendor result translation are handled before claiming a gap. |
| **Microsoft Agent 365 / Entra** | Distinct agent identities, sponsor/accountable business owners, assigned permissions, agent activity attribution and audit/security controls; identity and sponsor lifecycle. | Merely naming an agent and responsible owner is **not a differentiator**. Need evidence for responsibilities that **persist through state change, uncertainty and multi-system handoff** instead of asserting Microsoft lacks them. |
| **Palo Alto Prisma AIRS Agent Security** | Broad agent lifecycle posture, identity/privilege, runtime control, tool call visibility, supply-chain scanning and red-team capabilities. | Enterprise agent monitoring and generic AI security are heavily commoditized. Claims need version/edition/licensing scope; product marketing is not independent operational test evidence. |
| **Invariant Guardrails** | Declarative constraints over tool-call order, counts, and data flows; MCP/LLM integration with intervention. | Cross-tool trajectories, policy-driven dataflow and attack chains **already exist** in open source. RP* cannot claim uniqueness for 'checking combinations of tool calls' without narrower, demonstrable obligations. |
| **OPA / Cedar policy-as-code** | Deterministic policy decisions, scoped authorization and schema/typed identity evaluation. | RPE should not compete on generic rule evaluation. Its reason/control outputs must be assessed against policy-as-code plus conventional workflow integration. |
| **Existing workflow/runtime ecosystems (e.g. durable orchestrators)** | Persisted history, retries, observability, approvals and compensation may already cover parts of RPR/RPOS. | Do not claim unique 'durable state / approval / retry' until concrete product behavior, APIs, and test evidence are compared. |

### Primary/public source anchors, read 2026-10-20

- NVIDIA OpenShell: https://docs.nvidia.com/openshell/latest/security/best-practices.html
- NVIDIA OpenShell repo: https://github.com/NVIDIA/OpenShell
- NVIDIA September 28 2026 announcement: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Launches-Open-Agent-Safety-Platform-to-Secure-Agents-From-Testing-to-Deployment/
- AWS AgentCore Policy scope: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-scope.html
- AWS AgentCore policy engine and tool authorization: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-create-engine.html
- AWS AgentCore observability: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-policy-metrics.html
- Microsoft Agent 365 identity and sponsor: https://learn.microsoft.com/en-us/microsoft-agent-365/developer/identity
- Microsoft Agent 365 governance: https://learn.microsoft.com/en-us/microsoft-agent-365/guidance/agent-identity
- Palo Alto Prisma AIRS agent security: https://www.paloaltonetworks.com/ai-security/agent-security
- Invariant Guardrails: https://github.com/invariantlabs-ai/invariant
- OPA/Amazon Verified Permissions comparison: https://aws.amazon.com/blogs/security/migrating-from-open-policy-agent-to-amazon-verified-permissions/

## Capability status: no blank 'absent' claims

The following gaps are **research hypotheses**, not substantiated deficits in competitors.

| Cross-system question | Existing products to interrogate | What RPE/RPR/RPOS would have to **prove** |
| --- | --- | --- |
| External evidence is present, but is it sufficiently reliable for **this proposal, scope, time and institution**? | AWS Cedar, Microsoft Agent 365, customer policy engines | Exact source/authority boundary and invalid-evidence consequence; tested no implicit elevation of source claims |
| A tool was allowed, but the **policy, requested target or authorizing state changed** before dispatch. | OpenShell policy revision, AWS per-tool policies, Entra token lifecycle | Material-change re-evaluation, expiry and non-bypass in an integrating host, not merely a response field |
| Component A returned success but component B cannot verify a **real external effect**. | Gateway telemetry, durable runtime/event stores | Honest unknown/ambiguous state, no unsafe retry, residual owner and bounded Human Return consistent across RPE→RPR→RPOS |
| One component has logs and another has auth records, but no common **evidence lineage** survives across systems. | Agent 365 audit, AgentCore traces, vendor-independent OTel | Versioned provenance-safe, privacy-aware adapter/handoff record with absent/unknown fields preserved and no invented correlation |
| Legitimate workflow is held too often by safety policy. | OpenShell audit/enforce workflow, AWS LOG_ONLY/ENFORCE, Invariant guardrails | Benchmark both **false allows and false holds**, legitimate recovery and measured integration/operational overhead |

## RP* falsifiable positioning hypotheses

**H1 — Cross-vendor responsibility/evidence handoff:** For an independently defined scenario crossing at least two real products, RP* can retain a stable mapping among actor, proposed action, required authority, evidence origin, decision, downstream effect state and residual owner **without** fabricating truth or authority.  
*Disconfirm if*: existing products / open standards preserve equal or better semantics with less integration work or equivalent output can be obtained using a small documented configuration plus conventional event logs.

**H2 — Ambiguous external effect with bounded responsibility return:** A tool timeout, partial write, duplicate retry or unverified receipt is represented as **effect unknown**, routed to a named residual owner and reconciled before retry.  
*Disconfirm if*: an incumbent provides the same safety and accountability at a lower operational burden, or RP* fails to prevent erroneous 'no effect' / unsafe retry in bounded tests.

**H3 — Material-change reauthorization with compositional trace:** If a policy, actor entitlement, evidence source, target or tool capability changes between approval and dispatch, a trusted enforcing host invalidates or re-evaluates the relevant permission **without converting RPE evaluation into Authority**.  
*Disconfirm if*: RP* cannot close host bypasses, or standard platform policy checks already provide identical guarantees with fewer moving parts.

**H4 — Adoption value for non-specialists:** A clean-project implementer can connect RP* to a real framework with clear I/O, errors, and an enforceable boundary while accurately understanding 'allow ≠ authorization'.  
*Disconfirm if*: installation/integration burden or false-hold rate is worse than a comparably scoped standard policy engine, or the adoption experience requires RP* domain experts.

## Experiment design, not executed

1. Freeze one **benign** and one **adversarial** workflow (e.g. supplier-bank-detail change, permission drift, unknown post-dispatch effect).
2. Reproduce baseline using AWS/OPA/invariant/runtime-native integration from public documented APIs; collect actual outputs and adverse cases. No live financial, credential, personal or external irreversible action.
3. Integrate RPE's current governed/guarded evaluate-only contract and separately enforce host-owned authority. Include RPR/RPOS when testing effects and recovery; do not attribute their behavior to RPE alone.
4. Score: false-allow, false-hold, preserved source/pack/version binding, truthful unknown effects, proper residual owner, externally observed enforcement, integration code changes, dependencies, p50/p95/p99, reviewer workload, robustness against replay and stale decisions.
5. Permit a **negative outcome**: if incumbent products or simple composition already do the job better, retire the overlapping RP* feature and keep only a real gap; if no meaningful gap survives, revisit product positioning candidly.

## Avoid reinventing these capabilities

Do not prioritize a bespoke agent sandbox, generic permission policy language, vendor-specific agent identity provider, standard trace exporter, broad malware scanner or another agent runtime for their own sake. Those fields are already actively served. Prefer a versioned **responsibility/evidence translation and verification contract** built around existing enforcement, identity and runtime systems *if* tests show material missing semantics.

## Evidence grades and next owners

- **A: independently reproduced behavior**, code/source with exact version and runnable tests.
- **B: vendor docs/code review**, version/source anchored but not independently executed.
- **C: product positioning statements/press**, no proof of actual behavior.
- **D: RP* hypothesis/unverified gap**.

Current competitor evidence is mostly **B/C**; RP* differential claims remain **D**. No conclusion about actual comparative performance, financial value, defensible IP, adoption market size or product superiority is reached.

**Owner routing:** RPE M3/DAN-65 for proposed evaluation and adapter semantics; RP* cross-product DAN-50 and DAN-117 for security/market overlap; RPR/RPOS owning teams for real effect / recovery. Do not merge, release or publish this research note as canonical proof without owner review. No authority/Identity/User Data canon change.

**Decision point:** preserve the most narrowly falsifiable differentiator that survives baseline comparison, even if it means deleting or repurposing substantial RP* scope. The objective is needed functionality, not maintaining the original architecture at all costs.
