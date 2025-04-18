"""Immutable atoms, bonds and a mutable Molecule container (O(1) look‑ups)."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, FrozenSet, Iterator, List, Set

from .exceptions import DuplicateAtomError, DuplicateBondError, UnknownAtomError


@dataclass(frozen=True, slots=True)
class Atom:
    """An atom in a molecule graph."""

    symbol: str
    index: int
    isotope: int | None = None
    charge: int = 0

    def __post_init__(self) -> None:
        if self.index < 0:  # pragma: no cover – defensive
            raise ValueError("Atom index must be non‑negative")


@dataclass(frozen=True, slots=True)
class Bond:
    """An (unordered) bond between two atoms."""

    atoms: FrozenSet[int] = field(repr=False)
    order: int | str = 1  # 1, 2, 3 or 'ar'

    def __post_init__(self) -> None:
        if len(self.atoms) != 2:
            raise ValueError("Bond must connect exactly two distinct atoms")


class Molecule:
    """Graph container with O(1) neighbour access."""

    def __init__(self) -> None:
        self._atoms: Dict[int, Atom] = {}
        self._bonds: Dict[FrozenSet[int], Bond] = {}
        self._adj: Dict[int, Set[int]] = defaultdict(set)

    # --------------------------------------------------------------------- API
    def add_atom(self, symbol: str, index: int, /, *, isotope: int | None = None, charge: int = 0) -> Atom:
        if index in self._atoms:
            raise DuplicateAtomError(f"Atom index {index} already present")
        atom = Atom(symbol, index, isotope, charge)
        self._atoms[index] = atom
        return atom

    def add_bond(self, idx1: int, idx2: int, order: int | str = 1) -> Bond:
        if idx1 not in self._atoms or idx2 not in self._atoms:
            raise UnknownAtomError(f"Cannot create bond; unknown atom(s) {idx1}, {idx2}")
        key: FrozenSet[int] = frozenset({idx1, idx2})
        if key in self._bonds:
            raise DuplicateBondError(f"Bond between {idx1} and {idx2} already exists")
        bond = Bond(key, order)
        self._bonds[key] = bond
        self._adj[idx1].add(idx2)
        self._adj[idx2].add(idx1)
        return bond

    # ---------------------------------------------------------------- queries
    def neighbours(self, idx: int) -> List[int]:
        if idx not in self._atoms:
            raise UnknownAtomError(f"Atom {idx} not found")
        return list(self._adj[idx])

    def degree(self, idx: int) -> int:
        return len(self.neighbours(idx))

    # ----------------------------------------------------------- dunder sugar
    def __len__(self) -> int:
        return len(self._atoms)

    def __iter__(self) -> Iterator[Atom]:
        return iter(self._atoms.values())

    # ---------------------------------------------------- representation/debug
    def __repr__(self) -> str:  # pragma: no cover
        return f"<Molecule n_atoms={len(self)} n_bonds={len(self._bonds)}>"

