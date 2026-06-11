# Validator Boundary

This document defines the boundary for lightweight validation tools in this repository.

The current checker is:

- `scripts/check_examples.py`

## Purpose

The checker is intended to help maintain example files during Phase 1.6 by detecting missing structural fields and responsibility-boundary signals.

It supports repository maintenance. It does not certify examples or systems.

## What the checker may check

The checker may inspect whether example YAML files contain:

- required top-level keys
- non-empty node lists
- edge lists
- human return-point signals
- AI final responsibility boundary fields
- formalization-scope exclusion signals

## What the checker does not check

The checker does not determine:

- legal validity
- regulatory compliance
- safety
- fairness
- moral accountability
- production readiness
- institutional certification
- real-world responsibility resolution
- real-world harm elimination
- semantic completeness
- operational correctness

## Output language

Checker output should remain conservative.

Allowed terms include:

- `PASS: required key present`
- `WARN: optional or weak signal missing`
- `FAIL: required boundary missing`
- `bounded structural checks`

Avoid terms such as:

- `certified`
- `safe`
- `compliant`
- `fair`
- `legally valid`
- `morally resolved`
- `production ready`
- `approved for use`

## Interpretation

A passing checker result only means that the checked file satisfied the limited structural rules implemented by that checker version.

A passing result does not mean that the example is complete, correct in all contexts, ethically valid, legally valid, safe, fair, compliant, or ready for production use.

## Responsibility boundary

The checker is a maintenance aid.

The human author or maintainer remains responsible for deciding whether an example, schema, document, or public claim should be changed, published, or relied upon.

AI tools may assist with checker implementation and review, but they are not authors, responsibility holders, legal actors, moral agents, or final decision-makers.

## Future validators

Future validators may become stricter, but each validator should continue to state:

- what it checks
- what it does not check
- what assumptions it uses
- what claims are excluded

No validator in this repository should imply legal, moral, safety, fairness, compliance, or production-readiness conclusions unless that scope is explicitly defined and justified in a future phase.
