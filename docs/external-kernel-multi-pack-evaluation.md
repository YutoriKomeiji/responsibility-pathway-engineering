# External Kernel Multi-Pack Evaluation

## Purpose

This reference step evaluates one AI action request against multiple Responsible AI requirement packs and preserves each pack's result before producing a combined gate decision.

It demonstrates how RPE components can compose organizational, data-handling, publication, safety, or other requirement layers without collapsing their reasons or human-return destinations into one opaque score.

## Reference command

```bash
python scripts/run_external_kernel_multi.py \
  examples/external-kernel/minimal-action-request.json \
  examples/external-kernel/minimal-requirement-pack.json \
  examples/external-kernel/minimal-data-handling-pack.json
```

## Combination rule

The current reference precedence is:

```text
allow < hold < human_gate < deny
```

The most restrictive applicable pack decision becomes `combined_decision`.

Each pack still retains:

- applicability
- its own decision
- missing requirements
- reason codes
- human-return role

## Why per-pack results remain visible

A combined decision alone cannot explain which requirement source caused a stop or where responsibility should return. RPE therefore preserves the route from each requirement pack to its own result.

## Current boundary

This is a deterministic reference evaluator for synthetic packs. It does not determine whether a law, standard, policy, jurisdiction, or organizational rule actually applies. It does not establish legal validity, compliance, safety, fairness, certification, or production approval.

Future work may add explicit pack priority, conflict handling, source metadata, version selection, jurisdiction matching, expiry, and adapter-facing APIs.
