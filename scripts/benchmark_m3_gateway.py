#!/usr/bin/env python3
"""Measure repository-observable latency for the experimental M3 gateway.

This benchmark is descriptive evidence for the machine/environment where it is
run. It is not a production SLA and does not set a pass/fail latency threshold.
"""

from __future__ import annotations

import argparse
import json
import statistics
import time
from datetime import date
from pathlib import Path
from typing import Callable

from rpe_kernel import evaluate_gateway_request

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "examples" / "external-kernel" / "minimal-governed-evaluation-request.json"


def percentile(samples: list[float], p: float) -> float:
    """Return a linearly interpolated percentile for sorted millisecond samples."""
    if not samples:
        raise ValueError("samples must not be empty")
    ordered = sorted(samples)
    position = (len(ordered) - 1) * p
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    fraction = position - lower
    return ordered[lower] + (ordered[upper] - ordered[lower]) * fraction


def measure(call: Callable[[], object], iterations: int) -> list[float]:
    samples: list[float] = []
    for _ in range(iterations):
        started = time.perf_counter_ns()
        call()
        elapsed_ns = time.perf_counter_ns() - started
        samples.append(elapsed_ns / 1_000_000.0)
    return samples


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--iterations", type=int, default=500)
    parser.add_argument("--warmup", type=int, default=25)
    args = parser.parse_args()
    if args.iterations < 1 or args.warmup < 0:
        raise SystemExit("iterations must be >= 1 and warmup must be >= 0")

    governed = json.loads(FIXTURE.read_text(encoding="utf-8"))
    payload = {
        "contract_version": "0.1.0-exp",
        "governed_evaluation": governed,
        "risk_graph": {
            "conditions": [
                {
                    "condition_id": "authority_scope_mismatch",
                    "status": "triggered",
                    "required_controls": ["require_authority"],
                    "evidence_refs": ["authority-binding"],
                }
            ]
        },
        "constraints": ["no_delegation"],
    }

    def evaluate() -> object:
        return evaluate_gateway_request(payload, today=date(2026, 9, 1))

    for _ in range(args.warmup):
        evaluate()

    samples = measure(evaluate, args.iterations)
    result = {
        "benchmark": "m3_gateway_reference_path",
        "iterations": args.iterations,
        "warmup": args.warmup,
        "unit": "ms",
        "p50": percentile(samples, 0.50),
        "p95": percentile(samples, 0.95),
        "p99": percentile(samples, 0.99),
        "mean": statistics.fmean(samples),
        "min": min(samples),
        "max": max(samples),
        "evidence_scope": "repository_observable_local_process_only",
        "production_sla_claim": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
