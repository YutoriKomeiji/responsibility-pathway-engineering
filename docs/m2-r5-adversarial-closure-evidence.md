# M2 R5 Adversarial Closure Evidence

Status: Draft closure evidence for DAN-60. This document does not claim production, legal, compliance, deployment-security, external-effect, exactly-once, or implementation-wide formal guarantees.

## Purpose

Record the adversarial closure surface for the bounded RPE M2 governed-integration implementation and distinguish:

- directly tested repository-observable behavior;
- cross-checks already enforced by focused CI;
- claim ceilings that remain permanent or evidence-limited boundaries.

## Current M2 closure question

M2 closure means the currently implemented governed-integration scope has a coherent, adversarially checked repository-level evidence bundle. It does **not** mean every future responsibility-routing, adaptive-risk, security, deployment, or organizational problem is solved.

## Coverage matrix

| DAN-60 adversarial concern | Current evidence | Closure status |
| --- | --- | --- |
| governance/version failure | `check_m2_governed_admission.py`, `check_contract_compatibility.py` | covered |
| pack ↔ governance pack-version misbinding | `check_m2_governed_admission.py` | covered |
| source-authority/source-version/jurisdiction misbinding | `check_m2_adversarial_closure.py` | added for closure |
| unresolved ambiguity / future effective date / future review date | `check_m2_governed_admission.py` | covered |
| inactive / suspended governance | `check_m2_adversarial_closure.py` | added for closure |
| superseded governance without replacement | `check_m2_adversarial_closure.py` | added for closure |
| unknown applicability | `check_m2_adversarial_closure.py`; existing applicability resolver | added for closure |
| no applicable governed pack | `check_m2_adversarial_closure.py`; existing applicability resolver | added for closure |
| accidental legacy/M1 replacement | explicit separate `evaluate_action()` and `evaluate_governed_action()` surfaces; REST and MCP checks exercise both | covered as interface separation, not a claim that legacy mode provides strict governed semantics |
| REST governed route drift | `check_rest_api.py` | covered |
| MCP governed tool drift | `check_mcp_stdio.py` | covered |
| OpenAPI repository/package/runtime drift | `check_openapi_contract.py` | covered |
| manifest/runtime contract-version drift | `check_contract_compatibility.py` | covered |
| governed JSON Schema ↔ runtime result mismatch | `check_m2_adversarial_closure.py` validates representative outputs across admission, compatibility, governance, applicability, and evaluation stages | added for closure |
| caller-asserted transport provenance | `check_m2_bounded_loader.py`, OpenAPI check | covered |
| local/private path leakage | `check_m2_bounded_loader.py`, `check_m2_responsibility_handoff.py`, OpenAPI check | covered |
| authority inflation | responsibility handoff invariants assert `authority_effect = none`, `decision_scope = evaluation_only`, downstream authority owner | covered |
| receipt/effect evidence-class collapse | downstream obligation invariant `receipt_sufficient_for_effect_claim = false` | covered |
| retry/repair/resume authority collapse | downstream obligation invariant requires reauthorization | covered |
| unintended RPR/RPOS operational-state duplication | forbidden operational keys plus downstream owner invariant | covered at RPE output boundary |
| concrete external-engineer adoption value | `scripts/value_demo.py`, `docs/why-rpe.md`, `check-rpe-value-demo.yml` | covered for one synthetic repository-level scenario |

## New closure checker

`python scripts/check_m2_adversarial_closure.py`

The checker adds only discriminating cases not already explicit in focused checkers:

1. source-authority misbinding;
2. source-version misbinding;
3. jurisdiction misbinding;
4. inactive/suspended governance;
5. superseded governance without replacement;
6. missing applicability context;
7. explicit applicability mismatch / no applicable packs;
8. runtime output validation against the governed-result JSON Schema across all major fail-closed stages;
9. evidence-scope and residual-owner preservation on evaluation failure.

It also reasserts the no-authority and downstream-obligation invariants on every tested failure stage.

## Value validation

The existing value demo compares the same synthetic external-send proposal in two bounded paths:

- a deliberately naive agent-style baseline continues when a proposal exists;
- the RPE strict governed path returns `human_gate` when required approval evidence is absent.

Observed repository-level value is limited to visible continuation change, stable machine-readable reason, explicit Human Return/residual owner, and absence of execution authority.

No real external action is executed and no real-world risk reduction is claimed.

## Claim boundary at closure

If the closure checker and existing focused checks pass at the exact PR head and merge/main readback, the supported M2 claim is bounded to the implemented repository surface:

> RPE provides a strict governed evaluation path with bounded admission, compatibility, pack/governance binding, governance eligibility, applicability resolution, requirement evaluation, responsibility-preserving handoff, bounded local/caller-content loading, and reference Python/REST/MCP/OpenAPI surfaces, with deterministic negative checks for selected failure and drift classes.

The following remain outside that closure claim:

- production readiness;
- legal interpretation or compliance determination;
- certification or conformity assessment;
- deployment security;
- external action execution;
- proof that a downstream effect occurred or was prevented;
- exactly-once semantics;
- dispatch/retry/reconciliation/repair/resume operational ownership;
- generalized adaptive responsibility routing planned for later work;
- implementation-wide formal verification.

## Closure procedure

1. run the new adversarial closure workflow at exact PR head;
2. require existing relevant CI to remain green;
3. inspect any failure with verifier/environment alternatives before classifying it as a code defect;
4. merge only after closure evidence is coherent;
5. read back exact merge commit, main CI, and public documentation;
6. return exact RPE M2 closure evidence to RPM v0.8 without inflating the claim class.
