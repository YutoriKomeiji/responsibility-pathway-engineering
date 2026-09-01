"""Public Python API for the RPE external responsibility kernel."""

from .pipeline import evaluate_action, evaluate_governed_action

__all__ = ["evaluate_action", "evaluate_governed_action"]
__version__ = "0.1.0"
