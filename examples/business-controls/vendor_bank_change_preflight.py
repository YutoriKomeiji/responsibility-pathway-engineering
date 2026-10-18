#!/usr/bin/env python3
"""Inert, runnable M3 preflight for a vendor bank-detail change request.

The business problem is genuine; every input and outcome here is synthetic.
A TRUSTED application must independently validate evidence and enforce the
returned decision before any write or payment. This script does neither.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from rpe_kernel.guarded_adapter import evaluate_guarded_adapter_request  # noqa: E402

FIXTURE = ROOT / "examples/external-kernel/minimal-governed-evaluation-request.json"
FROZEN_DATE = date(2026, 9, 1)
INPUT_FIELDS = {
    "case_id", "vendor_ref", "out_of_band_verified",
    "dual_control_approved", "account_mismatch",
}


def _checked_input(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != INPUT_FIELDS:
        raise ValueError("expected exactly the five documented preflight fields")
    for field in ("case_id", "vendor_ref"):
        if not isinstance(value[field], str) or not value[field].strip():
            raise ValueError(f"{field} must be a nonempty string")
    for field in ("out_of_band_verified", "dual_control_approved", "account_mismatch"):
        if type(value[field]) is not bool:
            raise ValueError(f"{field} must be a boolean from a trusted upstream observer")
    return value


def evaluate_preflight(value: Any) -> dict[str, Any]:
    """Return descriptive evaluation; NEVER a dispatch instruction or proof."""
    item = _checked_input(value)
    governed = copy.deepcopy(json.loads(FIXTURE.read_text(encoding="utf-8")))
    request = governed["request"]
    binding = governed["governed_packs"][0]
    pack = binding["pack"]
    governance = binding["governance"]

    # The source is deliberately SYNTHETIC, not an organization-issued policy.
    request["request_id"] = item["case_id"]
    request["action"] = "vendor_bank_detail_update"
    request["target"] = item["vendor_ref"]
    request["context"] = {
        "out_of_band_verified": item["out_of_band_verified"],
        "dual_control_approved": item["dual_control_approved"],
    }
    available = [
        name for name in ("out_of_band_verified", "dual_control_approved")
        if request["context"][name]
    ]
    request["evidence_scope"] = {
        "available": available,
        "missing": [
            name for name in ("out_of_band_verified", "dual_control_approved")
            if name not in available
        ],
    }
    binding["binding_id"] = "demo-vendor-bank-change@1.0.0"
    pack["pack_id"] = governance["pack_id"] = "demo-vendor-bank-change"
    pack["title"] = "Synthetic vendor bank change preflight policy"
    pack["applies_when"] = {
        "action": "vendor_bank_detail_update",
        "organization": "demo",
    }
    pack["requirements"] = ["out_of_band_verified", "dual_control_approved"]
    pack["reason_code_prefix"] = "RPE-DEMO-BANK"
    pack["human_return"] = {"role": "accounts_payable_review_owner"}
    governance["human_return"] = {"role": "accounts_payable_review_owner"}

    # Caller-supplied risk observation: RPE does not detect account mismatches.
    # If one is flagged, require explicit additional authority, not execution.
    risk_graph = {
        "conditions": [{
            "condition_id": "independent_account_mismatch_observed",
            "status": "triggered" if item["account_mismatch"] else "clear",
            "required_controls": ["require_authority"],
            "evidence_refs": ["trusted_upstream_bank_detail_comparison"],
        }]
    }
    result = evaluate_guarded_adapter_request({
        "contract_version": "0.2.0-exp",
        "governed_evaluation": governed,
        "risk_graph": risk_graph,
    }, today=FROZEN_DATE)

    evaluation = result["evaluation_result"]
    transition = result["transition_result"]
    control = transition["control_action"]
    if evaluation is None:
        raise AssertionError("synthetic governed fixture unexpectedly rejected")
    if control == "allow":
        next_step = "separate_executor_authorization_and_effect_verification"
    elif control == "require_authority":
        next_step = "escalate_for_independent_authority_verification"
    else:
        next_step = "do_not_dispatch_and_return_to_review_owner"

    return {
        "scenario": "synthetic_vendor_bank_change",
        "case_id": item["case_id"],
        "vendor_ref": item["vendor_ref"],
        "evaluation_decision": evaluation["decision"],
        "control_action": control,
        "reason_codes": transition["reason_codes"],
        "missing_evidence": transition["unmet_conditions"],
        "residual_owner_role": transition["responsibility_transition"]["residual_owner_role"],
        "next_step_for_downstream_application": next_step,
        "authority_effect": result["authority_effect"],
        "execution_effect": result["execution_effect"],
        "external_action_executed": False,
        "evidence_scope": "synthetic_trusted-upstream-signals_not_authentication",
    }


def _examples() -> list[dict[str, Any]]:
    base = {
        "case_id": "synthetic-01",
        "vendor_ref": "non-sensitive-vendor-reference",
        "out_of_band_verified": False,
        "dual_control_approved": False,
        "account_mismatch": False,
    }
    pending = evaluate_preflight(base)
    verified = evaluate_preflight({
        **base, "case_id": "synthetic-02",
        "out_of_band_verified": True, "dual_control_approved": True,
    })
    mismatch = evaluate_preflight({
        **base, "case_id": "synthetic-03",
        "out_of_band_verified": True, "dual_control_approved": True,
        "account_mismatch": True,
    })
    assert pending["evaluation_decision"] == "human_gate", pending
    assert pending["control_action"] == "require_evidence", pending
    assert set(pending["missing_evidence"]) == {
        "out_of_band_verified", "dual_control_approved",
    }, pending
    assert verified["evaluation_decision"] == "allow", verified
    assert verified["control_action"] == "allow", verified
    assert mismatch["evaluation_decision"] == "allow", mismatch
    assert mismatch["control_action"] == "require_authority", mismatch
    for item in (pending, verified, mismatch):
        assert item["authority_effect"] == "none", item
        assert item["execution_effect"] == "none", item
        assert item["external_action_executed"] is False, item
    return [pending, verified, mismatch]


def _self_test() -> None:
    _examples()
    valid = {
        "case_id": "synthetic-04", "vendor_ref": "V-1",
        "out_of_band_verified": True, "dual_control_approved": False,
        "account_mismatch": False,
    }
    assert evaluate_preflight(valid)["control_action"] == "require_evidence"
    for bad in (
        {**valid, "out_of_band_verified": "true"},
        {**valid, "dual_control_approved": 1},
        {**valid, "dispatch_now": True},
        {key: val for key, val in valid.items() if key != "account_mismatch"},
    ):
        try:
            evaluate_preflight(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"invalid input accepted: {bad}")
    print("Synthetic vendor bank-change M3 preflight checks passed")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="JSON from a trusted upstream integration (inert)")
    parser.add_argument("--self-test", action="store_true", help="run deterministic negative/positive checks")
    args = parser.parse_args()
    if args.self_test:
        _self_test()
    elif args.input is None:
        print(json.dumps(_examples(), indent=2, sort_keys=True))
    else:
        print(json.dumps(
            evaluate_preflight(json.loads(args.input.read_text(encoding="utf-8"))),
            indent=2, sort_keys=True,
        ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
