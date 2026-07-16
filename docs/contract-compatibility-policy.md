# Contract Compatibility Policy

This policy defines how the bounded external-kernel contracts may evolve without silently changing runtime meaning.

It applies to:

- action requests;
- gate decisions;
- requirement packs;
- requirement-pack governance records;
- reason codes;
- reference adapter representations.

It does not establish production compatibility, certification, legal validity, or interoperability with third-party systems.

## Version model

Each contract family has an independent semantic version in `schemas/external-kernel/contract-versions.json`.

```text
MAJOR.MINOR.PATCH
```

- **MAJOR**: a consumer may need code or data migration.
- **MINOR**: additive compatible capability.
- **PATCH**: clarification or correction that does not change accepted or produced meaning.

Repository releases and contract-family versions are separate. A repository commit may update one contract without changing the others.

## Compatibility rules

### Additive compatible changes

A MINOR change may:

- add an optional field;
- add a new document or example;
- add a reason code without changing existing code meaning;
- add a lifecycle state only when older consumers fail closed or treat it as unknown;
- widen documentation without changing runtime behavior.

### Breaking changes

A MAJOR change is required when a change:

- removes or renames a field;
- changes a required field to a different type or meaning;
- changes decision precedence;
- changes applicability semantics;
- changes an existing reason code meaning;
- changes an existing lifecycle state's operational eligibility;
- changes a default or failure mode in a way that can alter `allow`, `hold`, `deny`, or `human_gate` outcomes;
- requires consumers to accept previously invalid input.

### Patch changes

A PATCH change may correct spelling, examples, links, or non-normative wording only when accepted input and produced meaning remain unchanged.

## Reason-code stability

Reason codes are stable identifiers, not display strings.

- Existing codes must not be reused for a different condition.
- Display text may improve without changing the code meaning.
- Deprecated codes remain documented through the migration window.
- Replacement codes must name the replaced code.
- Unknown reason codes must be preserved by adapters rather than discarded.

## Unknown-version behavior

A consumer must not silently guess compatibility.

- Unknown MAJOR version: reject or return `human_gate` before evaluation.
- Newer MINOR version under a known MAJOR: accept only when the consumer explicitly declares forward-compatible handling; otherwise return `human_gate`.
- Newer PATCH version under a known MAJOR and MINOR: may be accepted when schema validation succeeds.
- Missing version metadata: treat as legacy input and require an explicit migration path; do not silently label it current.

## Deprecation and migration

A breaking transition requires:

1. a migration note;
2. old and new version identifiers;
3. affected fields and reason codes;
4. a deterministic compatibility failure;
5. at least one migration fixture;
6. a human-maintainer decision before removal.

The repository does not promise a time-based support window yet. Until release policy is defined, deprecated contract versions remain supported only as explicitly documented repository fixtures.

## Requirement-pack governance interaction

Contract compatibility and pack governance are separate gates.

A structurally compatible pack may still be ineligible because it is expired, ownerless, suspended, superseded, retired, ambiguous, or insufficiently reviewed.

A well-governed pack may still be structurally incompatible with the current kernel.

Both checks must pass before future external loading can proceed to applicability and requirement evaluation.

## Reference adapters

REST, OpenAPI, and MCP reference adapters must expose or preserve contract version information when versioned runtime fields are introduced.

Adapters must not translate an unsupported version into a supported version without an explicit migration function and visible trace.

## Current bounded status

The manifest introduced with this policy records version `1.0.0` for the current action-request, gate-decision, requirement-pack, and pack-governance contract families.

This records the current repository contract baseline. It does not claim ecosystem stability or production support.
