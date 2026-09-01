# Python Package API

The RPE external kernel can be imported as a dependency-free Python package.

## Install locally

```bash
python -m pip install .
```

## Legacy / M1-compatible evaluation

```python
from rpe_kernel import evaluate_action

result = evaluate_action(action_request, requirement_packs)
```

`evaluate_action()` remains the compatibility entry for the historical M1-style request + pack interface.

## Strict governed evaluation

```python
from rpe_kernel import evaluate_governed_action

result = evaluate_governed_action(governed_envelope)
```

The strict governed path performs bounded admission, contract compatibility, pack/governance binding, governance eligibility, applicability, requirement evaluation, and responsibility-preserving handoff.

Governed results preserve:

- `authority_effect = none`;
- `decision_scope = evaluation_only`.

An `allow` result is not an execution authorization token.

## Bounded loading

```python
from rpe_kernel import load_governed_envelope_content, load_governed_envelope_file
```

The first loader accepts caller-provided UTF-8 JSON content or an explicitly supplied local file. It does not fetch URLs, discover registries, install packages, or establish source trust.

Loader success means only that bounded bytes were decoded as a JSON object. It does not establish interpretation correctness, governance eligibility, legal validity, or source authority.

## Integration role

Adapters should delegate to the appropriate package entry rather than reimplementing compatibility, governance, applicability, requirement evaluation, decision precedence, or Human Return behavior.

Legacy adapter surfaces delegate to `evaluate_action()`. Strict governed adapter surfaces delegate to `evaluate_governed_action()`.

The package evaluates proposals only. Dispatch, execution, effect verification, repair/resume authority, deployment approval, and final responsibility remain outside the package boundary.
