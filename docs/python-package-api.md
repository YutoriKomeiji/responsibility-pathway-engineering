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
- `decision_scope = evaluation_only`;
- the evaluation decision and reason-code references;
- selected/rejected governed Pack references;
- evaluation evidence scope and Human Return;
- downstream obligations for dispatch authority, effect verification, and retry/repair/resume reauthorization.

An `allow` result is not an execution authorization token.

## Bounded loading

```python
from rpe_kernel import load_governed_envelope_content, load_governed_envelope_file
```

The first loader accepts caller-provided UTF-8 JSON content or an explicitly supplied local file. It does not fetch URLs, discover registries, install packages, or establish source trust.

The loader records SHA-256 and byte length for the exact bytes it observed. This transport provenance is retained as non-JSON Python metadata so loading does not mutate or silently migrate the governed request contract. When that loaded envelope is passed directly to `evaluate_governed_action()`, the observation is preserved in the responsibility handoff.

The transport observation contains only:

- `source_kind` (`caller_content` or `local_file`);
- `content_sha256`;
- `byte_length`;
- `observation_scope = transport_bytes_only`.

The local filesystem path is intentionally not carried into the governed payload or result. A normal JSON caller cannot self-assert this loader-observed provenance by adding a top-level field; the strict governed request remains closed to unknown top-level fields.

Loader success or a matching digest establishes only which bytes this loader observed. It does not establish authorship, source authority, interpretation correctness, governance eligibility, legal validity, current applicability, or external effect.

## Integration role

Adapters should delegate to the appropriate package entry rather than reimplementing compatibility, governance, applicability, requirement evaluation, decision precedence, or Human Return behavior.

Legacy adapter surfaces delegate to `evaluate_action()`. Strict governed adapter surfaces delegate to `evaluate_governed_action()`.

The package evaluates proposals only. Dispatch, execution, effect verification, repair/resume authority, deployment approval, and final responsibility remain outside the package boundary.
