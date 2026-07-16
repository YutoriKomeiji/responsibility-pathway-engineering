# Internal Critical Review Protocol

RPE uses an internal adversarial review pass before major implementation or claim-expansion work.

The review is defined only by functional roles. Internal identity names, persona labels, private workflow names, or other non-public identity information must not be written into this repository.

## Purpose

The adversarial review role challenges proposals from the opposite direction before they reach the human maintainer gate.

The review asks:

- Is this rebuilding a protocol, SDK, policy engine, validator, or lifecycle system that should instead reuse an established implementation?
- Does the implementation claim more semantic power than the code actually has?
- Who owns and maintains the data, mappings, schemas, adapters, and review decisions over time?
- Are formal methods, mathematical language, standards language, or security language being used beyond their demonstrated scope?
- What fails when requirements conflict, age, become ambiguous, or lose a responsible owner?
- Which parts are reference examples, and which parts are suitable for long-term operational use?

## Review flow

```text
proposal or implementation
        ↓
adversarial review
        ↓
factual and repository verification
        ↓
integration and scope alignment
        ↓
human maintainer decision
```

These are functional review roles only. They do not approve merges, interpret law, establish compliance, or transfer responsibility from the human maintainer.

## Required output

A critical review should separate:

1. observed implementation facts;
2. valid criticism;
3. criticism that applies only to production or a broader claimed scope;
4. changes required now;
5. deferred changes with explicit restart conditions;
6. claims that must be narrowed or removed.

## Trigger conditions

Run this review before:

- adding a new runtime adapter;
- adding a new policy or legal mapping;
- presenting Lean results as product evidence;
- adding production-oriented security or deployment language;
- adding an external requirement-pack loader;
- changing decision semantics;
- publishing a maturity, compliance, safety, or interoperability claim.

## Boundary

Internal critical review improves design discipline. It is not independent external review, legal review, security certification, compliance assessment, formal verification of the runtime, production approval, or evidence that the resulting design is correct.
