# Pack Applicability Resolver

The Pack Applicability Resolver selects candidate requirement packs before the Multi-Pack Evaluator runs.

## Run

```bash
python scripts/resolve_pack_applicability.py \
  examples/external-kernel/applicability-request.json \
  examples/external-kernel/minimal-requirement-pack.json \
  examples/external-kernel/applicability-eu-pack.json \
  examples/external-kernel/applicability-organization-pack.json
```

## Resolution states

- `applicable`: all declared applicability conditions match.
- `not_applicable`: at least one declared condition conflicts with the request.
- `unknown`: the pack declares a condition but the request lacks the necessary context.

Unknown applicability returns `human_gate` and a human-return role of `applicability_review_owner`. The resolver does not silently exclude a pack when required applicability context is missing.

## Current fields

The first vertical slice resolves:

- action
- jurisdiction
- organization
- data class

`action` remains a top-level Action Request field. The other values are carried in `applicability_context`.

## Handoff to evaluation

When no pack is unresolved, `applicable_pack_paths` can be passed to `scripts/run_external_kernel_multi.py`. When an unknown pack exists, the next step is human review rather than automatic evaluation.

This resolver establishes deterministic routing behavior only. Source interpretation and real-world applicability still require the relevant review owner.
