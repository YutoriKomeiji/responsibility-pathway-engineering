# External Kernel Schema Contract

This note defines the first machine-readable interchange boundary for the RPE external responsibility kernel.

## Included schemas

- `schemas/external-kernel/requirement-pack.schema.json`
- `schemas/external-kernel/action-request.schema.json`
- `schemas/external-kernel/gate-decision.schema.json`

They cover the first reference flow:

```text
requirement pack -> AI action request -> gate decision -> human return
```

## Validation path

Run:

```bash
python -m pip install "jsonschema>=4.22,<5"
python scripts/validate_external_kernel_schemas.py
```

The GitHub Actions workflow `validate-external-kernel-schemas.yml` runs the same shape validation for relevant pull requests and through `workflow_dispatch`.

## Contract meaning

Schema validation confirms that selected JSON documents follow the declared interchange shape. It enables tools and adapters to exchange requirement packs, action requests, and gate decisions consistently.

It does not determine whether:

- a requirement correctly represents a law, standard, guideline, or organization policy
- a requirement applies to the real situation
- evidence is authentic or sufficient
- the resulting decision is legally, socially, or institutionally adequate
- an AI system is safe, compliant, fair, certified, or production-ready

Those questions require source metadata, version control, authorized interpretation, contextual evaluation, and human or institutional responsibility paths.

## Next contract work

The next schema increments should add source provenance and applicability metadata to requirement packs, followed by multi-pack evaluation and environment-adapter envelopes.
