"""Unit tests for the v0.1.0 core graph model."""
import pytest

from chemname import (
    Atom,
    Bond,
    Molecule,
    DuplicateAtomError,
    DuplicateBondError,
    UnknownAtomError,
)


def test_add_atoms() -> None:
    mol = Molecule()
    mol.add_atom("C", 0)
    mol.add_atom("O", 1)
    mol.add_atom("H", 2)
    assert len(mol) == 3
    indices = {atom.index for atom in mol}
    assert indices == {0, 1, 2}


def test_add_bond_and_neighbours() -> None:
    mol = Molecule()
    mol.add_atom("C", 0)
    mol.add_atom("O", 1)
    mol.add_bond(0, 1, 2)
    assert mol.neighbours(0) == [1]
    assert mol.neighbours(1) == [0]
    assert mol.degree(0) == 1
    assert mol.degree(1) == 1


def test_duplicate_atom_error() -> None:
    mol = Molecule()
    mol.add_atom("C", 0)
    with pytest.raises(DuplicateAtomError):
        mol.add_atom("O", 0)


def test_duplicate_bond_error() -> None:
    mol = Molecule()
    mol.add_atom("C", 0)
    mol.add_atom("C", 1)
    mol.add_bond(0, 1)
    with pytest.raises(DuplicateBondError):
        mol.add_bond(1, 0)


def test_unknown_atom_error() -> None:
    mol = Molecule()
    mol.add_atom("C", 0)
    with pytest.raises(UnknownAtomError):
        mol.add_bond(0, 99)

