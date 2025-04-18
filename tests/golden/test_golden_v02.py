"""Fifty canonical v0.2.0 cases."""
import pytest

from chemname.naming.namer import name
from .builders import build_molecule

CASES = [
    # 1‑12 alkanes
    ("methane", build_molecule(1)),
    ("ethane", build_molecule(2)),
    ("propane", build_molecule(3)),
    ("butane", build_molecule(4)),
    ("pentane", build_molecule(5)),
    ("hexane", build_molecule(6)),
    ("heptane", build_molecule(7)),
    ("octane", build_molecule(8)),
    ("nonane", build_molecule(9)),
    ("decane", build_molecule(10)),
    ("undecane", build_molecule(11)),
    ("dodecane", build_molecule(12)),
    # enes & ynes
    ("ethene", build_molecule(2, unsat="ene", unsat_locs=[1])),
    ("but-1-ene", build_molecule(4, unsat="ene", unsat_locs=[1])),
    ("but-2-ene", build_molecule(4, unsat="ene", unsat_locs=[2])),
    ("pent-1-yne", build_molecule(5, unsat="yne", unsat_locs=[1])),
    ("pent-2-yne", build_molecule(5, unsat="yne", unsat_locs=[2])),
    ("but-2-ene", build_molecule(4, unsat="ene", unsat_locs=[2])),
    # single halogen
    ("1-fluorohexane", build_molecule(6, substituents=[(1, "F")])),
    ("2-fluorohexane", build_molecule(6, substituents=[(5, "F")])),
    ("1-chloropropane", build_molecule(3, substituents=[(1, "Cl")])),
    ("2-chloropropane", build_molecule(3, substituents=[(2, "Cl")])),
    ("1-bromobutane", build_molecule(4, substituents=[(1, "Br")])),
    ("2-bromobutane", build_molecule(4, substituents=[(2, "Br")])),
    ("1-iodopentane", build_molecule(5, substituents=[(1, "I")])),
    ("2-iodopentane", build_molecule(5, substituents=[(4, "I")])),
    ("1-bromopropane", build_molecule(3, substituents=[(1, "Br")])),
    ("1-bromopropane", build_molecule(3, substituents=[(3, "Br")])),
    ("1,2-dichloroethane", build_molecule(2, substituents=[(1, "Cl"), (2, "Cl")])),
    ("2,3-dichlorobutane", build_molecule(4, substituents=[(2, "Cl"), (3, "Cl")])),
    ("1-chlorobutane", build_molecule(4, substituents=[(4, "Cl")])),
    ("1,4-dibromobutane", build_molecule(4, substituents=[(1, "Br"), (4, "Br")])),
    ("1-chloropentane", build_molecule(5, substituents=[(1, "Cl")])),
    ("1-chloropentane", build_molecule(5, substituents=[(5, "Cl")])),
    ("1-fluorobutane", build_molecule(4, substituents=[(1, "F")])),
    ("2-fluorobutane", build_molecule(4, substituents=[(2, "F")])),
    ("2-fluorobutane", build_molecule(4, substituents=[(3, "F")])),
    # halo + unsaturation
    ("3-chloroprop-1-ene", build_molecule(3, unsat="ene", unsat_locs=[1], substituents=[(3, "Cl")])),
    ("1-chloroprop-2-ene", build_molecule(3, unsat="ene", unsat_locs=[2], substituents=[(1, "Cl")])),
    ("1-chloroprop-2-yne", build_molecule(3, unsat="yne", unsat_locs=[2], substituents=[(1, "Cl")])),
    ("3-chloroprop-1-yne", build_molecule(3, unsat="yne", unsat_locs=[1], substituents=[(3, "Cl")])),
    ("1-bromohexane", build_molecule(6, substituents=[(6, "Br")])),
    ("1-bromopentane", build_molecule(5, substituents=[(5, "Br")])),
    ("1-bromobutane", build_molecule(4, substituents=[(4, "Br")])),
    ("1-bromopropane", build_molecule(3, substituents=[(3, "Br")])),
    ("bromoethane", build_molecule(2, substituents=[(2, "Br")])),
    ("bromomethane", build_molecule(1, substituents=[(1, "Br")])),
    ("1-chloropropane", build_molecule(3, substituents=[(3, "Cl")])),
    ("chloroethane", build_molecule(2, substituents=[(2, "Cl")])),
    ("chloromethane", build_molecule(1, substituents=[(1, "Cl")])),
]

@pytest.mark.parametrize("expected, mol", CASES)
def test_golden_v02(expected, mol):
    assert name(mol) == expected
