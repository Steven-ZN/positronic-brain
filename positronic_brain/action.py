from dataclasses import dataclass

@dataclass
class Action:
    """Representation of a potential agent action."""
    description: str
    harms_human: bool = False
    commanded_by_human: bool = False
    jeopardizes_self: bool = False
