"""Behaviour tests (non‑golden) for v0.2."""
from chemname.core.structures import Molecule
from chemname.naming.namer import name


def _build_linear(n, *, unsat=None, unsat_loc=None, subs=None):
    """Quick builder for behaviour tests."""
    subs = subs or []
    m = Molecule()
    for i in range(n):
        m.add_atom("C", i)
    for i in range(n - 1):
        order = 1
        if unsat and unsat_loc == i + 1:
            order = 2 if unsat == "ene" else 3
        m.add_bond(i, i + 1, order)
    idx = n
    for loc, elem in subs:
        m.add_atom(elem, idx)
        m.add_bond(loc - 1, idx)
        idx += 1
    return m


def test_simple_root_names():
    exp = [
        (1, "methane"),
        (4, "butane"),
        (12, "dodecane"),
    ]
    for n, expected in exp:
        mol = _build_linear(n)
        assert name(mol) == expected


def test_lowest_substituent_locant():
    mol = _build_linear(4, subs=[(2, "Cl")])
    assert name(mol) == "2-chlorobutane"


def test_unsaturation_priority():
    mol = _build_linear(4, unsat="ene", unsat_loc=1)
    assert name(mol) == "but-1-ene"
    mol2 = _build_linear(4, unsat="ene", unsat_loc=2)
    assert name(mol2) == "but-2-ene"


def test_multiplicative_prefix():
    mol = _build_linear(2, subs=[(1, "Cl"), (2, "Cl")])
    assert name(mol) == "1,2-dichloroethane"


def test_substituent_alphabetical():
    mol = _build_linear(3, subs=[(1, "Br"), (2, "Cl")])
    assert name(mol) == "1-bromo-2-chloropropane"
