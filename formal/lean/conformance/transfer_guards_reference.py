"""Pure Python reference for the bounded Lean TransferGuards decision.
NOT the RPE gateway; it consumes host-asserted Boolean facts, not credentials.
"""
from __future__ import annotations

from itertools import product

FIELDS = ("authority_verified", "delegation_verified", "receiver_eligible",
          "evidence_accessible", "evidence_current", "effect_unknown")


def transfer_permitted(facts: dict[str, bool]) -> bool:
    if set(facts) != set(FIELDS) or any(type(v) is not bool for v in facts.values()):
        raise ValueError("exactly six Boolean facts required")
    return all(facts[k] for k in FIELDS[:5]) and not facts["effect_unknown"]


def exhaustive_cases():
    for values in product((False, True), repeat=6):
        facts = dict(zip(FIELDS, values))
        yield facts, transfer_permitted(facts)
