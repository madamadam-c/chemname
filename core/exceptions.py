"""Custom exceptions isolating user‑facing errors."""


class ChemnameError(Exception):
    """Base class for all chemname‑specific exceptions."""


class DuplicateAtomError(ChemnameError):
    """Raised when an atom index already exists in the molecule."""


class DuplicateBondError(ChemnameError):
    """Raised when a bond between two atoms already exists."""


class UnknownAtomError(ChemnameError):
    """Raised when a referenced atom index is not present."""

