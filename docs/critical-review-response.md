# Critical Review Response

This note records an internal adversarial review of the current RPE kernel surface. It separates implementation facts, accepted weaknesses, and required follow-up work.

## SDK reuse and reference adapters

The dependency-free Python evaluator remains the small canonical core. The current REST and MCP modules are local reference adapters that demonstrate delegation to `rpe_kernel.evaluate_action()`.

For operational adapters, RPE should evaluate established SDKs and maintained protocol libraries before extending custom protocol code. SDK integrations must remain thin and must not duplicate applicability, requirement evaluation, decision precedence, or human-return semantics.

## Condition logic and real-world requirements

The current resolver uses a small fixed set of applicability fields and equality checks. Requirement evaluation checks named Boolean context values. This is not a general legal or policy reasoning engine.

The bounded claim is:

> RPE evaluates a human-scoped and human-approved operational requirement mapping against a structured action request.

Complex source interpretation, exceptions, conflicts, timing, jurisdiction, uncertainty, and authority remain outside the runtime kernel. Unknown applicability should return to a human rather than being hidden by increasingly complex condition syntax.

## Requirement-pack maintenance

A pack can become misleading when its source, interpretation, owner, version, or review status is stale. Metadata fields alone do not create maintenance responsibility.

Pack governance is therefore a prerequisite for external pack loading and reviewed real-world packs. The lifecycle should distinguish at least:

```text
draft → reviewed → approved → active → suspended / superseded / retired
```

A governed pack needs explicit owner, reviewer, source version, jurisdiction, effective scope, interpretation status, unresolved ambiguity, review dates, and supersession relationships. Expired, ownerless, ambiguous, or unreviewed packs must not silently produce an operational `allow` result.

## Lean scope and presentation

The current Lean files express selected structural properties under a minimal model. They do not verify the Python runtime, source interpretation, organizational operation, or real-world outcomes.

Lean remains an experimental formalization surface. Current results should be described as model-scoped structural invariants, not as proof that RPE is legally correct, safe, compliant, operationally correct, or production ready. Runtime and formalization claims must remain visibly separate unless an explicit checked correspondence is later established.

## Revised product position

The current kernel is:

> A small deterministic responsibility-gate kernel for evaluating explicitly scoped requirement packs and returning structured allow, hold, human-gate, or deny outcomes.

It is not currently a general legal reasoning engine, complete policy engine, production service, self-maintaining regulatory knowledge base, or formally verified runtime.

## Priority changes

Before broadening integrations or loading reviewed real-world packs:

1. define pack lifecycle, ownership, expiry, supersession, and review-validity rules;
2. define request, result, reason-code, and pack-version compatibility policy;
3. classify reference adapters separately from SDK-based operational adapters;
4. narrow source-mapping and formalization claims at reader-facing surfaces;
5. add external pack loading only after governance failure modes are explicit.

This review follows [`internal-critical-review.md`](internal-critical-review.md). Final prioritization, merge, publication, and responsibility remain with the human maintainer.