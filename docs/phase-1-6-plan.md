# Phase 1.6 Plan

Phase 1.6 prepares the repository for lightweight example checking and clearer transition toward executable validation.

This phase does not claim certification, compliance, legal validity, safety, fairness, moral accountability resolution, production readiness, or real-world responsibility resolution.

The goal is to make repository examples easier to inspect, maintain, and eventually validate against explicitly declared schema assumptions.

## Position after Phase 1.5

Phase 1.5 established:

- split schema files under `spec/`
- schema cross-reference documentation
- bounded validation checklist
- initial examples under `examples/`
- example index and example review notes
- MIT License
- authorship and attribution notice
- README reader paths in English and Japanese

Phase 1.6 should not expand claims. It should make the existing structure easier to check and extend.

## Phase 1.6 goals

1. add lightweight structural checks for example files
2. keep validation language bounded and non-certifying
3. clarify lifecycle-state example coverage
4. prepare future Lean or machine-checkable invariants without overclaiming
5. preserve human responsibility and AI non-responsibility boundaries

## Non-goals

Phase 1.6 should not claim:

- complete schema validation
- legal compliance
- safety guarantees
- fairness guarantees
- production readiness
- moral accountability resolution
- real-world harm elimination
- institutional certification
- autonomous AI responsibility transfer

## Candidate work items

### 1. Lightweight required-key checker

A small script may check whether example YAML files include required top-level keys, such as:

- `id`
- `version`
- `lifecycle_state`
- `nodes`
- `edges`
- `roles`
- `evidence_logs`
- `return_points`
- `responsibility_boundary`
- `formalization_scope`

Boundary:

This checker would only detect missing or malformed structure. It would not prove semantic correctness, real-world safety, compliance, fairness, legal validity, or responsibility resolution.

### 2. Example lifecycle coverage

Current examples cover:

- `originating` via `examples/minimal-pathway.yaml`
- `repaired` via `examples/repair-flow.yaml`

Possible future lifecycle examples:

- `suspended-pathway.yaml`
- `returning-pathway.yaml`
- `closed-pathway.yaml`

Boundary:

Lifecycle examples should remain minimal and readable. They should not become operational governance templates unless that scope is explicitly added later.

### 3. Example index maintenance

`docs/example-index.md` should be updated whenever a new example is added.

Each new example should include:

- purpose
- key boundary
- concepts introduced
- excluded claims
- future improvement notes if needed

### 4. Review note maintenance

`docs/example-review-notes.md` should be updated after adding or changing examples.

Review notes should remain bounded. They should record inspection results, not certification outcomes.

### 5. Future machine-readable validation

Later phases may introduce stricter validators using:

- YAML parsing
- JSON Schema
- custom rule checks
- CI checks
- Lean invariants

Boundary:

Machine checks should always state what they check and what they do not check.

## Candidate minimal validator behavior

A first validator may:

- scan `examples/*.yaml`
- parse YAML
- check required top-level keys
- check that AI participation does not set final responsibility to true
- check that a Human Return Point exists when required by the example type
- check that excluded claims include legal, moral, safety, fairness, compliance, and production-readiness boundaries

It should print conservative results such as:

- `PASS: required keys present`
- `WARN: optional key missing`
- `FAIL: required boundary missing`

It should not print:

- `certified`
- `safe`
- `compliant`
- `fair`
- `legally valid`
- `morally resolved`
- `production ready`

## Candidate Lean direction

Future Lean work may focus on small structural invariants such as:

- an AI node cannot be final responsibility holder
- a pathway with AI assistance must have a human or institutional return point
- a repaired pathway must reference a repair record
- evidence reconstruction claims must remain bounded to declared evidence logs

Boundary:

Lean formalization should remain limited to explicitly modeled definitions and assumptions. It should not claim real-world legal, ethical, safety, fairness, or institutional validity.

## Suggested Phase 1.6 order

Recommended order:

1. add `scripts/check_examples.py` or equivalent lightweight checker
2. add `docs/validator-boundary.md`
3. add one lifecycle example, preferably `suspended-pathway.yaml`
4. update `docs/example-index.md`
5. update `docs/example-review-notes.md`
6. record milestone in `CHANGELOG.md`

## Stop condition

Stop Phase 1.6 work if:

- validation wording starts implying certification
- examples become too large to read manually
- AI responsibility boundaries become ambiguous
- new examples introduce real-world legal, safety, fairness, or compliance claims
- formalization language exceeds the modeled assumptions

## Restart point

The next low-risk action is to add a lightweight example checker that only verifies required structural keys and explicit responsibility-boundary fields.
