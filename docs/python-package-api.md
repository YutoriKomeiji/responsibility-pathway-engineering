# Python Package API

The RPE external kernel can be imported as a dependency-free Python package.

## Install locally

```bash
python -m pip install .
```

## Evaluate an action

```python
from rpe_kernel import evaluate_action

result = evaluate_action(action_request, requirement_packs)
```

`action_request` is a dictionary matching the Action Request schema. `requirement_packs` is a sequence of dictionaries matching the Requirement Pack schema.

The result contains:

- `decision`: `allow`, `hold`, `human_gate`, or `deny`
- `stage`: `applicability` or `evaluation`
- per-pack applicability records
- per-pack evaluation decisions
- reason codes
- human-return information
- the next operational step

Unknown applicability and an empty applicable-pack set return `human_gate` rather than silently continuing.

## Integration role

This API is the framework-neutral boundary intended for future REST, MCP, LangGraph, LangChain, CI, and enterprise adapters. Adapters should call this API instead of reimplementing decision precedence or applicability behavior.
