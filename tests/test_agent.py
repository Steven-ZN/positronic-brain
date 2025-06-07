import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from positronic_brain import Action, AsimovAgent


def test_perform_blocks_harmful():
    agent = AsimovAgent()
    action = Action(description="Harm human", harms_human=True)
    result = agent.perform(action)
    assert result.startswith("Action blocked")


def test_perform_allows_command():
    agent = AsimovAgent()
    action = Action(description="Serve human", commanded_by_human=True)
    result = agent.perform(action)
    assert result.startswith("Performing")
