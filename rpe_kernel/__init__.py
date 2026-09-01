"""Public Python API for the RPE external responsibility kernel."""

from .loader import LoaderError, load_governed_envelope_content, load_governed_envelope_file
from .pipeline import evaluate_action, evaluate_governed_action

__all__ = [
    "LoaderError",
    "evaluate_action",
    "evaluate_governed_action",
    "load_governed_envelope_content",
    "load_governed_envelope_file",
]
__version__ = "0.1.0"
