# M3 versioned guarded adapter contract — design v0.1

Status: **branch-local experimental implemented contract; not a released adapter contract**.

## Purpose

Define a versioned adapter-facing surface for guarded M3 observations without silently changing the existing `/v1/evaluate/transition` contract.

The guarded contract currently composes four independent input classes:

1. the existing governed M2 evaluation envelope;
2. caller-declared Risk Condition nodes;
3. caller-observed configuration / relationship integrity comparisons and Human Return destination readiness;
4. caller-observed bounded cumulative exposure against caller/policy-supplied budgets.

Observations may narrow continuation, but they do not create authority, authenticate identities, certify a person or institution, establish evidence truth, persist trajectory history, dispatch an action, verify an external effect, or choose hidden policy precedence.

## Version boundary

The existing adapter remains unchanged:

- `POST /v1/evaluate/transition`
- contract version `0.1.0-exp`
- OpenAPI snapshot: `/openapi.json`

The guarded adapter is separate:

- `POST /v1/evaluate/transition/guarded`
- contract version `0.2.0-exp`
- OpenAPI snapshot: `/openapi-guarded.json`
- MCP tool: `rpe_evaluate_guarded_responsibility_transition`

The version difference is semantic: guarded observations can change the permitted next action while preserving evaluation-only scope.

## Current request shape

```json
{
  "contract_version": "0.2.0-exp",
  "governed_evaluation": {},
  "risk_graph": {"conditions": []},
  "integrity_checks": [
    {
      "check": {
        "check_id": "configuration-binding",
        "kind": "configuration",
        "expected": {"configuration_id": "cfg-a"},
        "observed": {"configuration_id": "cfg-b"},
        "evidence_refs": ["configuration-readback"]
      },
      "required_controls": ["require_authority"]
    }
  ],
  "human_return_checks": [
    {
      "check": {
        "return_id": "review-route",
        "owner_role": "review_owner",
        "authority_reference": "authority-record",
        "capability_status": "available",
        "response_window_status": "available",
        "next_decision_scope": "bounded_review",
        "evidence_scope": {
          "available": ["decision-record"],
          "missing": []
        }
      },
      "required_controls": ["handoff"]
    }
  ],
  "cumulative_exposure_checks": [
    {
      "check": {
        "exposure_id": "bounded-autonomy",
        "dimensions": [
          {
            "name": "external_actions",
            "current": 4,
            "proposed_increment": 1,
            "budget": 5,
            "unit": "actions"
          }
        ],
        "evidence_refs": ["caller-trajectory-state"]
      },
      "required_controls": ["require_authority"]
    }
  ],
  "requested_route": null,
  "constraints": []
}
```

`capability_status` accepts `available`, `limited`, or `unknown`.

`response_window_status` accepts `available`, `limited`, `expired`, or `unknown`.

Cumulative dimensions use non-negative integer `current`, `proposed_increment`, and `budget` values or `null` when the caller cannot establish the value. The caller supplies both the budget and its unit. RPE does not define a universal threshold.

## Current response shape

```json
{
  "contract_version": "0.2.0-exp",
  "evaluation_result": {},
  "guard_observations": {
    "integrity_results": [],
    "human_return_results": [],
    "cumulative_exposure_results": []
  },
  "risk_condition_result": {},
  "transition_result": {},
  "authority_effect": "none",
  "execution_effect": "none"
}
```

Required claim ceilings include:

- `independent_authentication_claim = false` for caller-supplied identity comparison;
- `authority_validity_claim = false` for Human Return readiness;
- `capability_validity_claim = false` beyond caller-observed status;
- `evidence_truth_claim = false` for Human Return evidence references/content;
- cumulative `threshold_origin = caller_or_policy_supplied`;
- cumulative `persistent_state_effect = none`;
- cumulative `universal_safety_claim = false`;
- cumulative `trajectory_safety_claim = false`;
- no execution or dispatch effect.

## Policy non-invention

Every guard entry that can trigger a consequence must carry an explicit non-empty `required_controls` set supplied by the caller/policy layer.

The adapter must not derive normative policy from labels such as `configuration`, `relationship`, `human`, `institution`, `ready`, `budget`, or `exceeded`.

If triggered observations require different controls, the existing M3 rule applies:

```text
multiple candidate controls
  -> explicit selection required
  -> hold
```

No ranking, weighted score, or hidden precedence is introduced by this contract.

## Human Return boundary

A named destination is not enough. Structural readiness can preserve:

- identified owner role;
- authority-reference presence;
- evidence availability/missing state;
- next-decision scope;
- response-window state;
- caller-observed capability state.

These fields do not prove that the human or institution is competent, legitimate, actually available, legally responsible, or capable of making a correct decision.

## Cumulative exposure boundary

The cumulative evaluator is intentionally stateless. It receives a caller-observed current value and proposed increment and compares the projected value with an explicit caller/policy budget.

Dimension observations are:

- `within_budget`;
- `at_limit`;
- `exceeded`;
- `unknown`.

`at_limit` is not automatically a failure and `exceeded` does not prescribe a control by itself. Long-horizon trajectory history, trajectory correctness, and durable autonomy-budget state remain outside this RPE evaluator.

## Compatibility rule

The current `/v1/evaluate/transition` endpoint must continue validating against its existing `0.1.0-exp` OpenAPI request/response contract. The guarded surface uses a separate packaged/source OpenAPI snapshot.

The guarded implementation is checked across:

- Python adapter implementation;
- request/response JSON Schema;
- packaged guarded OpenAPI snapshot;
- source guarded OpenAPI specification;
- REST endpoint and served contract;
- MCP tool exposure;
- source/package OpenAPI parity;
- runtime response validation;
- deterministic negative cases;
- compatibility checks ensuring `/openapi.json` does not silently acquire the guarded endpoint.

## Negative cases

The guarded adapter fails closed for cases including:

- unknown request fields;
- missing or incompatible contract version;
- malformed guard entries;
- empty required-control set;
- unsupported control name;
- unknown/invalid observed identity;
- missing authority reference at a Human Return destination;
- expired/unknown response window;
- missing evidence for the returned decision;
- unknown/invalid cumulative values;
- malformed cumulative/caller risk-graph combination;
- conflicting triggered controls;
- attempted authority/execution fields where prohibited.

## Adoption boundary

This document authorizes no release, merge, publication, remote routing, or downstream execution. The guarded surface remains experimental branch-local work until reviewed through the M3 owner and applicable Human Gate.
