# Single-source kernel boundary

RPE exposes several integration surfaces, but decision behavior has one implementation source.

```text
Python API
REST API
MCP stdio
    |
    v
rpe_kernel.pipeline.evaluate_action()
    |
    +-- applicability.resolve_pack()
    +-- evaluation.evaluate_pack()
    +-- evaluation.combine_decisions()
```

## Guarded invariants

The checker at `scripts/check_single_source_kernel.py` verifies that:

- `evaluate_action`, `resolve_pack`, `evaluate_pack`, and `combine_decisions` each have one canonical definition;
- REST and MCP adapters import and call `evaluate_action` instead of reimplementing applicability or decision precedence;
- the MCP structured and text results match the direct Python API result for the same fixture.

This is a bounded implementation-drift guard. It is not a complete semantic-equivalence proof, security audit, compliance certification, or production-readiness assessment.

## Adapter rule

New runtime adapters should validate and translate transport input, delegate to `rpe_kernel.evaluate_action()`, then serialize the returned structured result. They should not copy decision precedence, applicability resolution, or pack evaluation logic.
