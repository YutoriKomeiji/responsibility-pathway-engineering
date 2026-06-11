# Evidence Log

## Purpose

An Evidence Log preserves information needed to reconstruct, explain, review, stop, return, or repair a Responsibility Pathway.

An evidence log is not responsibility by itself.
It supports responsibility return by preserving traceable information.

## Minimal Definition

An Evidence Log is an artifact or record set that preserves pathway-relevant information across time so that a later entity can reconstruct what happened, what was known, what changed, and what could have been done.

## Evidence Categories

An evidence log may preserve:

- actor identity or role
- decision owner
- approval state
- input
- output
- model or system version
- prompt or instruction
- tool call
- execution result
- timestamp
- authority state
- stop condition
- refusal or override
- uncertainty
- affected party
- repair action
- post-event explanation

## Evidence Quality

Evidence should be evaluated by:

- completeness
- ordering
- integrity
- readability
- availability
- scope clarity
- retention period
- access boundary
- privacy and safety constraints

## Relationship to Responsibility Pathway

Evidence supports a pathway when it helps answer:

- what happened
- who or what acted
- under what authority
- with what information
- at what time
- with what uncertainty
- who could stop it
- where it could return
- how it was repaired

## Failure Modes

Evidence logging fails when:

- logs exist but cannot be understood
- logs omit the relevant authority or approval state
- logs show execution but not decision context
- logs record outputs but not assumptions
- logs are unavailable to the repair owner
- logs cannot distinguish human action from AI action
- logs preserve technical events but not affected-party visibility

## Boundary

An Evidence Log is not a complete truth record.

It records what was captured under a given design.

Responsibility Pathway Engineering treats logs as necessary but not sufficient for responsibility return.
