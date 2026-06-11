# Action Class Matrix

## Purpose

The Action Class Matrix classifies actions by their responsibility impact so that approval, stopping, evidence, return, and repair requirements can be designed before execution.

Different actions require different responsibility pathways.

## Minimal Definition

An Action Class is a category of action defined by its potential impact, reversibility, authority requirement, evidence requirement, and repair burden.

The Action Class Matrix maps action classes to pathway requirements.

## Action Classes

### Class 0: Informational

The action only produces or transforms information without direct external effect.

Examples:

- summarize
- classify
- draft
- suggest
- search within accessible context

Typical requirements:

- source visibility
- uncertainty visibility
- no external execution

### Class 1: Internal Assistive

The action affects internal work but does not directly affect external parties or irreversible systems.

Examples:

- create draft document
- organize notes
- update internal checklist
- propose task plan

Typical requirements:

- human review
- change trace
- rollback or correction path

### Class 2: Controlled Execution

The action executes within a bounded system under known authority and reversible or reviewable conditions.

Examples:

- update repository file
- create ticket
- modify non-critical internal record
- send draft to review queue

Typical requirements:

- decision owner
- approval gate
- evidence log
- return point
- rollback or repair path

### Class 3: External Impact

The action affects external parties, customers, public communication, financial state, legal state, production systems, or organizational commitments.

Examples:

- send external communication
- execute customer-impacting workflow
- change production policy
- publish claim
- trigger payment or contract-related process

Typical requirements:

- explicit authority
- human return point
- stop authority
- high-quality evidence log
- repair owner
- affected-party visibility

### Class 4: Irreversible or High-Risk

The action may be irreversible, safety-relevant, legally significant, financially material, or socially harmful if wrong.

Examples:

- delete critical data
- deny access or benefit
- report to authority
- make binding legal or financial decision
- execute safety-critical operation

Typical requirements:

- strong human authorization
- independent review where appropriate
- explicit stop authority
- pre-execution evidence capture
- post-execution repair plan
- documented non-automation boundary where needed

## Matrix Fields

For each action class, specify:

- decision owner
- approval gate
- stop authority
- evidence log requirement
- return point
- repair owner
- reversibility level
- affected party visibility
- residual risk

## Boundary

The Action Class Matrix is a design aid.

It does not determine legal status, moral blame, or compliance by itself.
