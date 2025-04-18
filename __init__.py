"""chemname – zero‑dependency IUPAC helper library (v0.3)."""

from importlib.metadata import version as _v

from .core.exceptions import DuplicateAtomError, DuplicateBondError, UnknownAtomError
from .core.structures import Atom, Bond, Molecule
from .naming.namer import name

__all__ = [
    "Atom",
    "Bond",
    "Molecule",
    "DuplicateAtomError",
    "DuplicateBondError",
    "UnknownAtomError",
    "name",
]

__version__ = "0.3.0"

try:  # pragma: no cover
    __pkg_version = _v(__name__)
except Exception:  # noqa: BLE001
    __pkg_version = __version__
