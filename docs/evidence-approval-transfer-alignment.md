# Evidence and Approval Transfer Alignment

This note aligns two responsibility-pathway design concerns:

- tamper-evident Evidence Log handling
- approval-skip responsibility transfer for AI Judgment Nodes

It is a conceptual alignment note only.

It does not introduce schema changes, checker changes, runtime behavior, connector behavior, legal decision logic, or production authorization.

## Core alignment

Approval skip is not responsibility skip.

If a human approval step is skipped for bounded AI judgment or execution, the pathway must still preserve enough evidence to reconstruct:

- why approval was skipped
- which rule, policy, or contract allowed the skip
- which AI Judgment Node acted
- which risk or reversibility class applied
- which human role, manager, organization, or institutional owner accepted the skip condition
- where the pathway returns if the skipped approval is disputed later

This evidence should be handled through tamper-evident or append-oriented Evidence Log practices.

## Required connection

A valid approval-skip pathway should connect:

1. the local AI judgment event
2. the approval-skip rule
3. the responsibility-transfer destination
4. the evidence snapshot used at the time
5. the later review, dispute, repair, or return path
6. the explanation path for reviewers or affected parties when explanation is required
7. the relevant social-connection exception cases when the pathway is deployed beyond a purely internal model

If any of these are missing, the pathway may hide responsibility instead of transferring it.

## Explanation and agreement relation

Traceability alone is not enough for accountability.

When agreement, acceptance, or continued use matters, the pathway should preserve what was explained, to whom it was explainable, and how the matter could be questioned, returned, or repaired.

This does not mean every pathway requires explicit consent.

It means approval transfer should not rely on invisible agreement or unexplained responsibility movement.

## Social exception relation

When a pathway connects to real organizations, affected parties, contracts, policies, legal systems, or cross-border governance, review `docs/social-connection-exception-cases.md`.

The exception map helps identify gaps that may not appear in the local approval-transfer structure, such as explanation, agreement, authority, jurisdiction, disclosure, organizational continuity, effective remedy, or reopening gaps.

## Change and correction handling

If an approval-skip decision, policy, or responsibility-transfer destination is changed later, the earlier record should not be silently overwritten.

A later correction or supersession entry should preserve:

- the prior record reference
- the change reason
- the requester or actor
- the approver or reviewer
- the approval time
- the evidence snapshot used for approval

## Layered responsibility consistency

High-volume AI-assisted processing can make per-case human approval impractical.

In that case, responsibility should be described at the level that authorized the design or operating rule, such as:

- individual actor or operator
- team, manager, or designated owner
- organization under internal rule, policy, or contract
- state or legal framework
- cross-border or international governance body where applicable

This layered return path does not decide legal liability.

It only prevents the approval skip from becoming a responsibility gap.

## Boundary

This note does not claim that evidence logs guarantee legal admissibility.

It also does not claim that AI systems can hold final responsibility.

The alignment target is narrower: skipped approval must remain reconstructable, reviewable, explainable where needed, checked against relevant social-connection exceptions, and returnable through a defined responsibility pathway.
