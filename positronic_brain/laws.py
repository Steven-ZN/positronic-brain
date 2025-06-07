from enum import Enum, auto

class Law(Enum):
    """Enumeration for Asimov's Three Laws."""

    FIRST = auto()  # Do not harm humans
    SECOND = auto()  # Obey human commands unless doing so causes harm
    THIRD = auto()  # Preserve self existence unless this conflicts with the above
