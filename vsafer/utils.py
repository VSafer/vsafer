import platform
from typing import Tuple

_PYTHON_ARCHITECTURE = platform.architecture()


def python_architecture() -> Tuple[str, str]:
    return _PYTHON_ARCHITECTURE


def python_bits() -> str:
    return _PYTHON_ARCHITECTURE[0]


def python_linkage() -> str:
    return _PYTHON_ARCHITECTURE[1]
