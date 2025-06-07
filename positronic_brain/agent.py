"""Base agent implementation."""

from .action import Action
from .ethics import EthicsEvaluator

class AsimovAgent:
    """Simple agent that consults an ethics evaluator before acting."""

    def __init__(self, evaluator: EthicsEvaluator | None = None) -> None:
        self.evaluator = evaluator or EthicsEvaluator()

    def perform(self, action: Action) -> str:
        """Return a message describing whether the action was performed."""
        if self.evaluator.evaluate(action):
            return f"Performing: {action.description}"
        return f"Action blocked: {action.description}"
