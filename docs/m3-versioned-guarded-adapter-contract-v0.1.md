# M3 versioned guarded adapter contract — design v0.1

Status: branch-local experimental design; not a released adapter contract.

## Purpose

Define the next adapter-facing revision for guarded M3 observations without incrementally mutating the existing `/v1/evaluate/transition` contract.

The guarded contract composes three independent inputs:

1. the existing governed M2 evaluation envelope;
2. caller-observed configuration / relationship integrity comparisons;
3. caller-observed Human Return destination readiness.

The adapter must preserve the same core rule already enforced by the Python-only composition path: observations may narrow continuation, but they do not create authority, certify a person or institution, establish evidence truth, dispatch an action, or choose hidden policy precedence.

## Proposed version boundary

Keep the existing adapter unchanged:

- `POST /v1/evaluate/transition`
- contract version `0.1.0-exp`

Introduce a separate versioned candidate surface rather than adding optional fields piecemeal:

- candidate: `POST /v1/evaluate/transition/guarded`
- candidate contract version: `0.2.0-exp`

The version bump is semantic, not marketing. A caller using the guarded surface can supply additional observation classes whose results may change the permitted next action.

## Candidate request shape

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
        "authority_ref": "authority-record",
        "capability_status": "observed_available",
        "response_window_status": "open",
        "next_decision_scope": "bounded_review",
        "evidence_scope": {
          "available": ["decision-record"],
          "missing": []
        }
      },
      "required_controls": ["handoff"]
    }
  ],
  "requested_route": null,
  "constraints": []
}
```

## Candidate response shape

The response should expose observation results as evidence rather than force callers to reconstruct them from risk nodes:

```json
{
  "contract_version": "0.2.0-exp",
  "evaluation_result": {},
  "guard_observations": {
    "integrity_results": [],
    "human_return_results": []
  },
  "risk_condition_result": {},
  "transition_result": {},
  "authority_effect": "none",
  "execution_effect": "none"
}
```

Required claims that remain false:

- `independent_authentication_claim = false` for caller-supplied identity comparison;
- `authority_validity_claim = false` for Human Return readiness;
- `capability_validity_claim = false` beyond the caller-observed status;
- `evidence_truth_claim = false` for evidence references/content;
- no execution or dispatch effect.

## Policy non-invention

Every guard entry that can trigger a consequence must carry an explicit non-empty `required_controls` set supplied by the caller/policy layer.

The adapter must never derive normative policy from labels such as `configuration`, `relationship`, `human`, `institution`, or `ready`.

If two triggered guard observations require different controls, the existing M3 rule applies:

```text
multiple candidate controls
  -> explicit selection required
  -> hold
```

No ranking, weighted score, or hidden precedence is introduced by this contract.

## Human Return boundary

A named destination is not enough. The structural readiness observation may include:

- identified owner role;
- authority reference presence;
- evidence availability/missing state;
- next-decision scope;
- response-window state;
- caller-observed capability state.

These fields do not prove that the human or institution is competent, legitimate, available in reality, legally responsible, or capable of making a correct decision. They only preserve the observed structural preconditions instead of treating termination or routing as responsibility closure.

## Compatibility rule

The current `/v1/evaluate/transition` endpoint must continue validating against its existing `0.1.0-exp` OpenAPI request/response contract.

The guarded surface may be added only when all of the following move together in one deliberate slice:

- Python adapter implementation;
- request/response JSON Schema;
- packaged OpenAPI snapshot;
- source OpenAPI specification;
- REST checker;
- runtime-output-to-OpenAPI validator;
- MCP exposure decision or explicit MCP non-support statement;
- deterministic negative tests;
- compatibility/readback evidence.

## Initial negative cases

The guarded adapter should fail closed for at least:

- unknown request fields;
- missing or incompatible contract version;
- malformed guard entries;
- empty required-control set;
- unsupported control name;
- unknown observed identity;
- invalid observed identity;
- missing authority reference at a Human Return destination;
- expired/unknown response window;
- missing evidence for the returned decision;
- conflicting triggered controls;
- attempted authority/execution fields in caller input where prohibited.

## Adoption boundary

This document authorizes no release, merge, publication, remote routing, or downstream execution. It is the design basis for the next M3 adapter implementation slice.