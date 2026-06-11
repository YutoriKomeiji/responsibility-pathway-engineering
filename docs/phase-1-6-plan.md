# Phase 1.6 Plan

Phase 1.6 prepares the repository for lightweight example checking and clearer transition toward executable validation.

This phase does not claim certification, compliance, legal validity, safety, fairness, moral accountability resolution, production readiness, or real-world responsibility resolution.

The goal is to make repository examples easier to inspect, maintain, and eventually validate against explicitly declared schema assumptions.

## Current status

Phase 1.6 is substantially established.

The repository now contains:

- bounded lightweight example checker
- validator-boundary documentation
- checker-coverage documentation
- minimal-core rationale documentation
- lifecycle examples for `originating`, `repaired`, `suspended`, `returning`, and `closed`
- example index and bounded review notes covering the lifecycle examples
- GitHub Actions workflow for bounded example checks
- README and README.ja reader paths for the checker, coverage map, and minimal-core rationale
- CHANGELOG entries for the Phase 1.6 milestones

Phase 1.6 remains non-certifying. It establishes structural maintainability and lifecycle-example coverage only.

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

Phase 1.6 did not expand claims. It made the existing structure easier to check, review, explain, and extend.

## Phase 1.6 goals

1. add lightweight structural checks for example files - established
2. keep validation language bounded and non-certifying - established
3. clarify lifecycle-state example coverage - established
4. prepare future Lean or machine-checkable invariants without overclaiming - established as a boundary and future direction
5. preserve human responsibility and AI non-responsibility boundaries - established across examples, checker, and documentation

## Non-goals

Phase 1.6 does not claim:

- complete schema validation
- legal compliance
- safety guarantees
- fairness guarantees
- production readiness
- moral accountability resolution
- real-world harm elimination
- institutional certification
- autonomous AI responsibility transfer

## Established work items

### 1. Lightweight required-key checker

`scripts/check_examples.py` now checks bounded structural signals in example YAML files.

It checks required top-level keys, node and edge structures, human return-point signals, AI final-responsibility boundary fields, excluded-claim signals, and lifecycle-specific structural signals.

Boundary:

This checker detects missing or weak structural signals. It does not prove semantic correctness, real-world safety, compliance, fairness, legal validity, moral resolution, or responsibility resolution.

### 2. Example lifecycle coverage

Current examples cover:

- `originating` via `examples/minimal-pathway.yaml`
- `repaired` via `examples/repair-flow.yaml`
- `suspended` via `examples/suspended-pathway.yaml`
- `returning` via `examples/returning-pathway.yaml`
- `closed` via `examples/closed-pathway.yaml`

Boundary:

Lifecycle examples remain minimal and readable. They are not operational governance templates unless that scope is explicitly added later.

### 3. Example index maintenance

`docs/example-index.md` now records:

- purpose
- key boundary
- concepts introduced
- excluded claims
- reading order
- future improvement notes

### 4. Review note maintenance

`docs/example-review-notes.md` now records bounded inspection notes for all current lifecycle examples.

Review notes record structural observations. They are not certification outcomes.

### 5. Validator boundary and checker coverage

`docs/validator-boundary.md` defines the checker boundary.

`docs/checker-coverage.md` summarizes current checker coverage and interpretation boundaries.

### 6. Minimal core rationale

`docs/minimal-core-rationale.md` explains why the repository is intentionally small and specification-first.

It frames the current repository as a minimal responsibility-preserving core rather than a production application, governance automation platform, legal decision system, certification tool, or moral accountability engine.

## Current validator behavior

The current validator can:

- scan `examples/*.yaml`
- parse YAML
- check required top-level keys
- check that AI participation does not set final responsibility to true
- check that a Human Return Point signal exists
- check that excluded claims include legal, moral, safety, fairness, compliance, and production-readiness boundaries
- check lifecycle-specific structural signals for `originating`, `repaired`, `suspended`, `returning`, and `closed`

It prints conservative results such as:

- `PASS: required key present`
- `PASS: lifecycle rule applied`
- `WARN: optional or weak signal missing`
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
- a suspended pathway must preserve return or review conditions
- a returning pathway must not imply automatic continuation
- a closed pathway must preserve evidence, residual boundaries, and reopening conditions
- evidence reconstruction claims must remain bounded to declared evidence logs

Boundary:

Lean formalization should remain limited to explicitly modeled definitions and assumptions. It should not claim real-world legal, ethical, safety, fairness, or institutional validity.

## Completion condition

Phase 1.6 may be treated as complete when:

- examples remain readable
- checker remains bounded and non-certifying
- lifecycle coverage remains explicit
- README reader paths point to boundary and coverage documents
- CHANGELOG records the milestones
- future work is shifted toward Phase 2 formalization or Phase 3 reference implementation without expanding claims prematurely

## Stop condition

Stop Phase 1.6 work if:

- validation wording starts implying certification
- examples become too large to read manually
- AI responsibility boundaries become ambiguous
- new examples introduce real-world legal, safety, fairness, or compliance claims
- formalization language exceeds the modeled assumptions

## Restart point

The next low-risk action is to either:

1. update `ROADMAP.md` and `BEACON.md` to reflect Phase 1.6 completion, or
2. begin Phase 2 by selecting a very small Lean invariant, such as `AI cannot be final responsibility holder`.
