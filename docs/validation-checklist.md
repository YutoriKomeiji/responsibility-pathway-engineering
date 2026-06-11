# Validation Checklist

This checklist provides a bounded review guide for Responsibility Pathway Engineering schema instances during Phase 1.5 - Specification Binding.

It is not a certification process, legal assessment, compliance determination, production-readiness review, safety guarantee, fairness guarantee, or moral accountability judgment.

Use it to check whether a pathway instance preserves the minimum structure needed for responsibility-related state to originate, propagate, suspend, return, repair, and close under explicitly modeled boundaries.

## 1. Pathway identity and lifecycle

Check that the pathway instance has:

- `id`
- `version`
- `lifecycle_state`
- `nodes`
- `edges`
- `roles`
- `evidence_logs`
- `responsibility_boundary`

Lifecycle review:

- If `lifecycle_state` is `originating`, the initial authority and intended action class should be visible.
- If `lifecycle_state` is `propagating`, node-to-node transitions should be reconstructable.
- If `lifecycle_state` is `suspended`, a stop authority or return point should be present.
- If `lifecycle_state` is `returning`, the target authorized entity should be visible.
- If `lifecycle_state` is `repaired`, at least one repair record should be present.
- If `lifecycle_state` is `closed`, the reason for closure should be preserved through evidence or boundary documentation.

## 2. Node review

For each node, check:

- stable `id`
- allowed `type`
- declared `capabilities`
- `authority_scope`
- `evidence_binding`

Authority review:

- Nodes that decide should have decision authority.
- Nodes that approve should have approval authority.
- Nodes that execute should have execution authority.
- Nodes that stop should have stop authority or an explicit justification.
- Nodes that repair should have repair authority and evidence access.
- Nodes that close should have closure authority or an explicit boundary reason.

AI participation review:

- If a node is an AI agent, it may generate, recommend, classify, or execute only within modeled authority.
- If a node is an AI agent, `assumes_final_responsibility` should be false.
- AI participation should not remove the need for human or institutional responsibility where applicable.

## 3. Action class review

Check that the pathway has an action class or a documented reason why action classification is not yet available.

For the action class, review:

- `id`
- `name`
- `level`
- `responsibility_requirements`
- `reversibility`
- `external_impact`
- `automation_boundary`

Escalation expectations:

- Level 0 actions may be informational and usually reversible.
- Level 1 actions may be internally assistive and should remain within internal support boundaries.
- Level 2 actions may involve controlled execution and should have a decision owner.
- Level 3 actions may create external impact and should have human authorization and evidence logging.
- Level 4 actions may be irreversible or high risk and should have strong human authorization, stop authority, evidence logging, return points, and repair ownership.

## 4. Role binding review

Check whether the following roles are present or explicitly out of scope:

- `decision_owner`
- `approval_gate`
- `execution_actor`
- `stop_authority`
- `evidence_log`
- `repair_owner`
- `return_point`
- `human_return_point`
- `affected_party`

Role expectations:

- A controlled or higher-impact action should identify a decision owner.
- Authority threshold crossings should identify an approval gate.
- Actions that may increase irreversibility or harm should identify stop authority.
- Pathways needing reconstruction or repair should bind evidence logs.
- Pathways needing responsibility return should bind return points.
- Failure, ambiguity, or damage conditions should identify a repair owner.

## 5. Evidence review

For each evidence log, check:

- `id`
- `pathway_id`
- `evidence_categories`
- `integrity_state`
- `access_boundary`

Evidence sufficiency review:

- External impact actions should include actor identity or role and authority state.
- Tool use or system execution should preserve tool call and execution result where applicable.
- Stopped or suspended pathways should preserve stop condition or refusal/override evidence.
- Repair pathways should include repair action or post-event explanation evidence.
- Evidence quality should be reviewed for completeness, readability, availability, scope clarity, retention period, privacy constraints, and safety constraints.

Boundary reminder:

Evidence supports reconstruction, explanation, stopping, return, and repair. It should not be treated as complete truth by default.

## 6. Return point review

For each return point, check:

- `id`
- `type`
- `target_node`
- `returnability_conditions`
- `supported_actions`

Returnability conditions:

- meaning is visible
- authority is visible
- time is available
- information quality is sufficient
- trust is calibrated
- reversibility or compensation is visible
- value is visible
- cost is visible

Human Return Point review:

If the return point is a Human Return Point, check that human conditions are present, including:

- understandable information
- meaningful choice
- refusal availability
- stop authority availability
- repair path availability
- adequate review time
- no coercive pressure

A human being present is not sufficient for Human Return Point validity.

## 7. Repair review

If repair is present or required, check:

- `id`
- `pathway_id`
- `trigger`
- `repair_owner`
- `repair_state`
- `evidence_reference`

Repair process review:

- A repair owner should be present before corrective action is applied.
- Available and missing evidence should be identified.
- Affected parties should be visible when compensation is considered.
- Unresolved repair states should preserve a reason.
- Repair outcomes should be documented before closure.

Repair boundary:

Repair does not mean harm disappears. Repair does not resolve blame by itself. Repair restores the pathway enough for action, explanation, correction, compensation, redesign, closure, or explicit unresolved preservation.

## 8. Responsibility boundary review

Check that `responsibility_boundary` preserves the following expectations:

- human author or institutionally authorized responsibility is required where applicable
- AI final responsibility is not allowed
- institutional authority is required when applicable
- legal or moral claims are out of scope unless separately established by qualified review

Boundary expectations:

- The schema may model participation.
- The schema may model authority and evidence requirements.
- The schema may support reconstruction and repair.
- The schema does not itself establish legal liability, moral blame, compliance, fairness, safety, or production readiness.

## 9. Formalization scope review

If formalization fields are present, check:

- assumptions are explicit
- modeled entities are identified
- excluded claims are identified
- theorem status is clear

Formalization boundary:

Formal claims must refer only to explicitly stated definitions, assumptions, modeled entities, and bounded transitions.

A formal proof over a modeled structure does not by itself establish real-world safety, legality, fairness, compliance, or moral accountability.

## 10. Minimum pass condition

A pathway instance is ready for further review when:

- required pathway fields are present
- nodes have authority and evidence bindings
- action class expectations are documented
- roles are bound or explicitly out of scope
- evidence supports reconstruction
- return points are available when responsibility must return
- repair ownership exists when failure or ambiguity may need restoration
- AI participation boundaries are explicit
- formal claims are bounded
- non-goals and excluded claims are preserved

This checklist is intentionally conservative. When in doubt, preserve uncertainty, document the boundary, and return responsibility to an authorized human or institutional review point.
