#!/usr/bin/env python3
"""Check the bounded OpenAPI contract and runtime exposure."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "spec" / "openapi" / "rpe-kernel.openapi.json"
PACKAGED_SPEC_PATH = ROOT / "rpe_kernel" / "rpe-kernel.openapi.json"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> int:
    document = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    packaged = json.loads(PACKAGED_SPEC_PATH.read_text(encoding="utf-8"))

    if document != packaged:
        fail("repository and packaged OpenAPI contracts must match exactly")

    if document.get("openapi") != "3.1.0":
        fail("OpenAPI version must be 3.1.0")

    paths = document.get("paths")
    if not isinstance(paths, dict):
        fail("paths must be an object")

    required_operations = {
        "/health": "get",
        "/openapi.json": "get",
        "/v1/evaluate": "post",
        "/v1/evaluate/governed": "post",
        "/v1/evaluate/transition": "post",
    }
    for path, method in required_operations.items():
        if not isinstance(paths.get(path), dict) or method not in paths[path]:
            fail(f"missing operation: {method.upper()} {path}")

    schemas = document.get("components", {}).get("schemas", {})
    for name in (
        "HealthResponse",
        "EvaluateRequest",
        "EvaluateResponse",
        "TransportProvenance",
        "DownstreamObligations",
        "ResponsibilityHandoff",
        "GovernedEvaluateRequest",
        "GovernedEvaluateResponse",
        "GatewayControlAction",
        "GatewayRouteTarget",
        "GatewayNormalizedRouteTarget",
        "GatewayRiskCondition",
        "GatewayRiskGraph",
        "GatewayEvaluateRequest",
        "GatewayResponsibilityTransition",
        "GatewayTransitionResult",
        "GatewayEvaluateResponse",
        "ErrorResponse",
    ):
        if name not in schemas:
            fail(f"missing component schema: {name}")

    decisions = schemas["EvaluateResponse"]["properties"]["decision"].get("enum")
    if decisions != ["allow", "hold", "human_gate", "deny"]:
        fail("decision enum must preserve kernel precedence vocabulary")

    governed = schemas["GovernedEvaluateResponse"]
    governed_stages = governed["properties"]["stage"].get("enum")
    if governed_stages != ["admission", "compatibility", "governance", "applicability", "evaluation"]:
        fail("governed stage enum must preserve strict pipeline stages")
    if "contract_version" not in governed.get("required", []):
        fail("governed response must require contract_version")

    governed_request = schemas["GovernedEvaluateRequest"]
    if "transport_provenance" in governed_request.get("properties", {}):
        fail("HTTP governed request must not accept caller-asserted transport provenance")

    handoff = schemas["ResponsibilityHandoff"]
    handoff_props = handoff.get("properties", {}) if isinstance(handoff, dict) else {}
    required_handoff = {
        "authority_effect",
        "decision_scope",
        "evaluation_decision",
        "evaluation_reason_codes",
        "selected_pack_refs",
        "rejected_pack_refs",
        "evaluation_evidence_scope",
        "transport_provenance",
        "human_return",
        "downstream_obligations",
    }
    if set(handoff.get("required", [])) != required_handoff:
        fail("governed handoff required fields drift from runtime contract")
    if handoff_props.get("authority_effect", {}).get("const") != "none":
        fail("governed OpenAPI must preserve authority_effect=none")
    if handoff_props.get("decision_scope", {}).get("const") != "evaluation_only":
        fail("governed OpenAPI must preserve decision_scope=evaluation_only")
    if handoff_props.get("downstream_obligations", {}).get("$ref") != "#/components/schemas/DownstreamObligations":
        fail("governed handoff must expose downstream obligations")

    obligations = schemas["DownstreamObligations"]["properties"]
    if obligations.get("dispatch_authority_required", {}).get("const") is not True:
        fail("dispatch must require separate downstream authority")
    if obligations.get("effect_verification_required_for_effect_claim", {}).get("const") is not True:
        fail("effect claims must require downstream verification")
    if obligations.get("receipt_sufficient_for_effect_claim", {}).get("const") is not False:
        fail("receipt must not be sufficient effect evidence")
    if obligations.get("authority_owner", {}).get("const") != "downstream_runtime_or_institution":
        fail("RPE must not become downstream authority owner")

    provenance = schemas["TransportProvenance"]
    provenance_props = provenance.get("properties", {})
    if provenance_props.get("observation_scope", {}).get("const") != "transport_bytes_only":
        fail("transport provenance must remain bounded to observed bytes")
    if "source_path" in provenance_props or "file_path" in provenance_props or "local_path" in provenance_props:
        fail("OpenAPI transport provenance must not expose local paths")

    gateway_request = schemas["GatewayEvaluateRequest"]
    if gateway_request.get("properties", {}).get("contract_version", {}).get("const") != "0.1.0-exp":
        fail("M3 gateway request contract version must remain explicitly experimental")
    if gateway_request.get("properties", {}).get("governed_evaluation", {}).get("$ref") != "#/components/schemas/GovernedEvaluateRequest":
        fail("M3 gateway must preserve the governed M2 evaluation envelope as its baseline")

    gateway_response = schemas["GatewayEvaluateResponse"]
    gateway_response_props = gateway_response.get("properties", {})
    if gateway_response_props.get("authority_effect", {}).get("const") != "none":
        fail("M3 gateway response must not create authority")
    if gateway_response_props.get("execution_effect", {}).get("const") != "none":
        fail("M3 gateway response must not claim execution")

    transition_result = schemas["GatewayTransitionResult"]
    transition_props = transition_result.get("properties", {})
    if transition_props.get("authority_effect", {}).get("const") != "none":
        fail("M3 transition must preserve authority_effect=none")
    if transition_props.get("execution_effect", {}).get("const") != "none":
        fail("M3 transition must preserve execution_effect=none")
    if transition_props.get("downstream_executor_required", {}).get("const") is not True:
        fail("M3 transition must keep downstream executor ownership explicit")

    transition_descriptor = schemas["GatewayResponsibilityTransition"].get("properties", {})
    if transition_descriptor.get("dispatch_effect", {}).get("const") != "none":
        fail("M3 transition descriptor must not dispatch")
    authority_props = transition_descriptor.get("authority", {}).get("properties", {})
    if authority_props.get("effect", {}).get("const") != "none":
        fail("M3 transition descriptor must not generate authority")
    if authority_props.get("downstream_authority_required", {}).get("const") is not True:
        fail("M3 transition descriptor must require downstream authority")

    description = document.get("info", {}).get("description", "").lower()
    if "does not imply production readiness" not in description:
        fail("OpenAPI description must preserve the production boundary")

    governed_description = paths["/v1/evaluate/governed"]["post"].get("description", "").lower()
    if "does not accept caller-asserted transport provenance" not in governed_description:
        fail("governed HTTP description must preserve loader-observed provenance boundary")

    gateway_description = paths["/v1/evaluate/transition"]["post"].get("description", "").lower()
    for phrase in ("does not dispatch", "execute an external action", "create authority", "retry/repair/resume"):
        if phrase not in gateway_description:
            fail(f"M3 gateway HTTP description missing boundary phrase: {phrase}")

    sys.path.insert(0, str(ROOT))
    from rpe_kernel.http_api import load_openapi_document

    if load_openapi_document() != document:
        fail("runtime OpenAPI document differs from repository contract")

    print("PASS: OpenAPI contract and runtime exposure are consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
