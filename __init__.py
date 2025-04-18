"""chemname – zero‑dependency IUPAC helper library (core graph model)."""

from importlib.metadata import version as _v

# Public API re‑exports
from .core.structures import Atom, Bond, Molecule
from .core.exceptions import (
    DuplicateAtomError,
    DuplicateBondError,
    UnknownAtomError,
)

__all__ = [
    "Atom",
    "Bond",
    "Molecule",
    "DuplicateAtomError",
    "DuplicateBondError",
    "UnknownAtomError",
]

__version__: str = "0.1.0"

# Ensure package metadata is available even when installed editable
try:  # pragma: no cover
    __pkg_version = _v(__name__)  # noqa: SLF001
except Exception:  # noqa: BLE001
    __pkg_version = __version__

