"""Public Python API for the RPE external responsibility kernel."""

from .gateway import evaluate_gateway_request, evaluate_transition
from .loader import LoaderError, load_governed_envelope_content, load_governed_envelope_file
from .pipeline import evaluate_action, evaluate_governed_action
from .risk_conditions import evaluate_risk_conditions

__all__ = [
    "LoaderError",
    "evaluate_action",
    "evaluate_gateway_request",
    "evaluate_governed_action",
    "evaluate_risk_conditions",
    "evaluate_transition",
    "load_governed_envelope_content",
    "load_governed_envelope_file",
]
__version__ = "0.1.0"
