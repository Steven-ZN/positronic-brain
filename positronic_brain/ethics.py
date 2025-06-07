"""Simple evaluation functions for Asimov's laws."""

from .action import Action

class EthicsEvaluator:
    """Evaluates actions for compliance with the laws."""

    def evaluate(self, action: Action) -> bool:
        """Return True if the action is permissible."""
        if action.harms_human:
            return False
        if action.commanded_by_human:
            return True
        if action.jeopardizes_self:
            return False
        return True
