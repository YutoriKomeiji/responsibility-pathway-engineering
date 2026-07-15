# External Kernel Pipeline

The external-kernel pipeline runs pack applicability resolution and multi-pack evaluation through one command.

```bash
python scripts/run_external_kernel_pipeline.py \
  examples/external-kernel/applicability-request-resolved.json \
  examples/external-kernel/minimal-requirement-pack.json \
  examples/external-kernel/applicability-eu-pack.json \
  examples/external-kernel/applicability-organization-pack.json
```

## Behavior

1. Resolve every pack as `applicable`, `not_applicable`, or `unknown`.
2. Stop at `human_gate` when any pack has unknown applicability.
3. Stop at `human_gate` when no pack is applicable.
4. Evaluate only applicable packs when routing is resolved.
5. Return one structured result containing applicability records and pack decisions.

An applicability stop uses `stage: applicability`. A completed evaluation uses `stage: evaluation`.

The pipeline does not infer undeclared jurisdiction, organization, or data class. Missing routing context is returned to `applicability_review_owner`.
