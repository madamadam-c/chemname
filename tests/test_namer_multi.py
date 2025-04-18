"""Behaviour tests for multi‑unsaturation + alkyl."""
from chemname.core.structures import Molecule
from chemname.naming.namer import name


def build(n, *, unsat=None, unsat_locs=None, subs=None):
    subs = subs or []
    m = Molecule()
    for i in range(n):
        m.add_atom("C", i)
    unsat_locs = ([] if unsat_locs is None else unsat_locs)
    for i in range(n - 1):
        order = 1
        if unsat and (i + 1) in unsat_locs:
            order = 2 if unsat == "ene" else 3
        m.add_bond(i, i + 1, order)
    idx = n
    for loc, elem in subs:
        m.add_atom(elem, idx)
        m.add_bond(loc - 1, idx)
        idx += 1
    return m


def test_buta_13_diene():
    mol = build(4, unsat="ene", unsat_locs=[1, 3])
    assert name(mol) == "buta-1,3-diene"


def test_hexa_1_3_diyne():
    mol = build(6, unsat="yne", unsat_locs=[1, 3])
    assert name(mol) == "hexa-1,3-diyne"


def test_dimethylbutane():
    mol = build(4, subs=[(2, "C"), (2, "C")])
    assert name(mol) == "2,2-dimethylbutane"
