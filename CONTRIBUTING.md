# Contributing

Contributions are welcome. RPE is Open Construction: real failures, counterexamples, integration pain, and adversarial cases are part of how the project improves.

## Valuable contributions

Useful contributions include:

- minimal bug reproductions;
- regression tests;
- adversarial scenarios;
- authority/evidence confusion cases;
- prompt, relationship, memory, trajectory, or supply-chain attack cases;
- performance and integration-cost measurements;
- framework/SaaS/legacy adapter proposals;
- documentation and quick-start improvements;
- Requirement Pack examples with clear source/governance boundaries;
- compatibility and migration improvements;
- patches that simplify integration without weakening responsibility boundaries.

## Before opening a PR

Where practical:

1. identify the behavior or problem being changed;
2. separate observed facts from broader claims;
3. add or update deterministic tests for behavior changes;
4. keep authority, evaluation evidence, execution, external effect, repair, and resume semantics distinct;
5. do not introduce real secrets, customer data, private operational topology, or unreviewed legal/compliance claims;
6. update relevant public docs when a supported surface or limitation changes.

## Bugs versus security reports

Ordinary bugs may be reported publicly.

If the finding exposes a practical vulnerability or sensitive exploit path, follow [`SECURITY.md`](SECURITY.md) instead of publishing exploit details in a public issue.

## Claim discipline

A successful test, integration, or deployment report is valuable evidence for the tested scope. It should not be generalized into universal safety, legal, compliance, production-readiness, or external-effect claims without additional evidence.

## AI-assisted contributions

AI assistance is welcome. Contributors remain responsible for reviewing what they submit, respecting licenses and confidentiality, and accurately representing test and provenance evidence.
