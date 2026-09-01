# Why use RPE?

RPE is useful when an AI or automation can propose a consequential action, but the system should not treat proposal generation as sufficient authority to continue.

The practical role is small on purpose:

```text
agent proposes action
→ RPE evaluates explicit requirements / evidence / governance
→ machine-readable decision
→ continue only when the caller's separate execution authority permits it
```

RPE is not another agent framework and does not execute the action. It is an integration boundary between **"the model wants to do this"** and **"the surrounding system has enough evidence and authority to let this continue."**

## Concrete value

A useful RPE integration should make at least these differences observable.

### 1. Unsupported continuation becomes a visible stop

Without a separate decision boundary, a simple agent implementation can collapse:

```text
proposal generated → continue
```

into one step.

With governed RPE evaluation, missing required approval/evidence can become:

```text
proposal generated
→ HUMAN_GATE
→ stable reason code
→ explicit Human Return / residual owner
```

The repository demonstrates this with:

```bash
python scripts/value_demo.py
```

The demo uses a synthetic external-send proposal with missing human approval. It does not send anything.

### 2. Stops are machine-readable rather than opaque

RPE returns structured fields such as:

- decision;
- pipeline stage;
- stable reason codes;
- Human Return;
- residual-owner role;
- selected/rejected Requirement Pack references;
- evaluation evidence scope.

This lets an existing orchestrator decide whether to show a review screen, create a ticket, ask for evidence, or stop the workflow without parsing prose from an LLM.

### 3. Evaluation evidence stays distinct from effect evidence

RPE deliberately preserves the boundary that:

- approval/evaluation evidence is not proof of external effect;
- a receipt alone is not verified effect;
- retry, repair, and resume require reauthorization by the downstream system that owns execution.

This helps prevent an integration from turning "RPE allowed the proposal" into "the action definitely happened" or "RPE authorized the retry."

### 4. It can be added as a boundary instead of replacing the agent stack

The reference package exposes a Python API plus REST and MCP adapters. A caller can keep its existing planning/model/tool stack and insert RPE before a consequential continuation point.

The strict governed path is explicit:

```python
from rpe_kernel import evaluate_governed_action

result = evaluate_governed_action(governed_envelope)
```

RPE does not require the downstream application to become an RPE-specific runtime.

## Where this can fit

Potential integration points include agent workflows that propose:

- external email/message sending;
- publishing or submitting content;
- internal approval-dependent requests;
- file or record changes;
- payment/refund/order actions;
- infrastructure or deployment changes.

These are examples of placement, not claims that the current repository is production-ready for those domains. Real deployments still need domain-specific Requirement Packs, authentication/authorization, security controls, effect verification, persistence, audit retention, and operational ownership.

## What the value demo proves — and does not prove

The current value demo proves only repository-observable behavior for one synthetic scenario:

1. the naive comparison path would continue when a proposal exists;
2. the governed RPE path returns `human_gate` when required approval is missing;
3. the stop contains a stable reason and explicit return owner;
4. RPE grants no execution authority.

It does **not** prove production safety, legal compliance, general risk reduction, correct domain interpretation, successful action prevention in an external system, or economic ROI.

Those claims require evidence from real integrations.
