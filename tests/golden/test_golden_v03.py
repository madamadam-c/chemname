"""Fifty canonical v0.3.0 cases exercising multi‑unsaturation, alkyl + halo substituents, and full locant rules."""
import pytest

from chemname.naming.namer import name
from .builders import build_molecule

CASES = [
    # 1–4: simple methyls on butane
    ("2-methylbutane", build_molecule(4, substituents=[(2, "C")])),
    ("2-methylbutane", build_molecule(4, substituents=[(3, "C")])),
    ("2,2-dimethylbutane", build_molecule(4, substituents=[(2, "C"), (2, "C")])),
    ("2,3-dimethylbutane", build_molecule(4, substituents=[(2, "C"), (3, "C")])),
    # 5–7: methyl on longer alkanes
    ("3-methylpentane", build_molecule(5, substituents=[(3, "C")])),
    ("2-methylpentane", build_molecule(5, substituents=[(4, "C")])),
    ("2-methylhexane", build_molecule(6, substituents=[(5, "C")])),
    # 8: ethyl substituent
    ("2-methylbutane", build_molecule(3, substituents=[(2, ["C", "C"])])),
    # 9–11: alkyl + single unsaturation
    ("3-methylpent-1-ene", build_molecule(5, unsat="ene", unsat_locs=[1], substituents=[(3, "C")])),
    ("3-methylpent-2-ene", build_molecule(5, unsat="ene", unsat_locs=[2], substituents=[(3, "C")])),
    ("3-methylhex-2-yne", build_molecule(6, unsat="yne", unsat_locs=[2], substituents=[(3, "C")])),
    # 12–13: mixed halogen + alkyl
    ("2-bromo-4-methylpentane", build_molecule(5, substituents=[(2, "Br"), (4, "C")])),
    ("1-bromo-3-methylbutane", build_molecule(4, substituents=[(1, "Br"), (3, "C")])),
    # 14–17: multiple unsaturations only
    ("buta-1,3-diene", build_molecule(4, unsat="ene", unsat_locs=[1, 3])),
    ("hexa-1,3-diyne", build_molecule(6, unsat="yne", unsat_locs=[1, 3])),
    ("hepta-1,4-diene", build_molecule(7, unsat="ene", unsat_locs=[1, 4])),
    ("octa-2,5-diyne", build_molecule(8, unsat="yne", unsat_locs=[2, 5])),
    # 18–19: multi‑unsat + methyl
    ("2,5-dimethylhexa-1,3-diene", build_molecule(6, unsat="ene", unsat_locs=[1, 3], substituents=[(2, "C"), (5, "C")])),
    ("3-bromohexa-1,5-diyne", build_molecule(6, unsat="yne", unsat_locs=[1, 5], substituents=[(3, "Br")])),
    # 20: multi‑unsat + alkyl multiplicative
    ("2-methylpent-1-yne", build_molecule(4, unsat="yne", unsat_locs=[1], substituents=[(2, "C"), (4, "C")])),
    # 21–22: multi‑unsat + halo
    ("3-chloropropa-1,2-diene", build_molecule(3, unsat="ene", unsat_locs=[1, 2], substituents=[(3, "Cl")])),
    ("2-bromobuta-1,3-diene", build_molecule(4, unsat="ene", unsat_locs=[1, 3], substituents=[(2, "Br")])),
    # 23: mixed halo + alkyl + multi‑unsat
    ("3-chloro-5-methylhexa-1,4-diene", build_molecule(6, unsat="ene", unsat_locs=[1, 4], substituents=[(3, "Cl"), (5, "C")])),
    # 24: three substituents, pure alkane
    ("2-bromo-3-chloro-4-methylhexane", build_molecule(6, substituents=[(2, "Br"), (3, "Cl"), (4, "C")])),
    # 25: same‑loc substituents different type
    ("2-chloro-2-methylpropane", build_molecule(3, substituents=[(2, "Cl"), (2, "C")])),
    # 26: two ethyls
    ("3,4-diethyloctane", build_molecule(8, substituents=[(3, ["C", "C"]), (4, ["C", "C"])])),
    # 27: ethyl + methyl
    ("2-ethyl-3-methylhexane", build_molecule(6, substituents=[(2, ["C", "C"]), (3, "C")])),
    # 28: diethyl
    ("3,3-diethylpentane", build_molecule(5, substituents=[(3, ["C", "C"]), (3, ["C", "C"])])),
    # 29: diethyl + methyl
    ("2,5-diethyl-5-methylheptane", build_molecule(7, substituents=[(2, ["C", "C"]), (5, ["C", "C"]), (5, "C")])),
    # 30: halo + multi‑unsat
    ("4-chlorohexa-1,4-diene", build_molecule(6, unsat="ene", unsat_locs=[1, 4], substituents=[(4, "Cl")])),
    # 31: halo + ethyl + single unsat
    ("2-bromo-3-methylpent-1-ene", build_molecule(4, unsat="ene", unsat_locs=[1], substituents=[(2, "Br"), (3, ["C", "C"])])),
    # 32: halo + diyne
    ("3-chlorohexa-2,4-diyne", build_molecule(6, unsat="yne", unsat_locs=[2, 4], substituents=[(3, "Cl")])),
    # 33: dichloro + diene
    ("2,3-dichlorohexa-1,4-diene", build_molecule(6, unsat="ene", unsat_locs=[1, 4], substituents=[(2, "Cl"), (3, "Cl")])),
    # 34: trimethyl + ene
    ("2,2,3-trimethylpent-1-ene", build_molecule(5, unsat="ene", unsat_locs=[1], substituents=[(2, "C"), (2, "C"), (3, "C")])),
    # 35–37: long‑chain edge cases
    # ("12-methyldodecane", build_molecule(12, substituents=[(12, "C")])),
    ("dodec-2-ene", build_molecule(12, unsat="ene", unsat_locs=[11])),
    ("dodeca-1,11-diene", build_molecule(12, unsat="ene", unsat_locs=[1, 11])),
    # 38–41: higher multiplicities of unsat
    ("hexa-1,2,3-triene", build_molecule(6, unsat="ene", unsat_locs=[1, 2, 3])),
    ("octa-1,3,5,7-tetraene", build_molecule(8, unsat="ene", unsat_locs=[1, 3, 5, 7])),
    ("hexa-1,3,5-triene", build_molecule(6, unsat="ene", unsat_locs=[1, 3, 5])),
    ("hexa-1,3,5-triyne", build_molecule(6, unsat="yne", unsat_locs=[1, 3, 5])),
    # 42: dimethyl + diyne
    ("2,4-dimethylhepta-1,3-diyne", build_molecule(7, unsat="yne", unsat_locs=[1, 3], substituents=[(2, "C"), (4, "C")])),
    # 43: chloro + dimethyl + diene
    ("3-chloro-2,4-dimethylhexa-1,5-diene", build_molecule(6, unsat="ene", unsat_locs=[1, 5], substituents=[(3, "Cl"), (2, "C"), (4, "C")])),
    # 44: chloro + diethyl + ene
    ("2-chloro-3,3-diethylpent-1-ene", build_molecule(5, unsat="ene", unsat_locs=[1], substituents=[(2, "Cl"), (3, ["C", "C"]), (3, ["C", "C"])])),
    # 45: bromo + trimethyl + ene
    ("3-bromo-2,2,3-trimethylbut-1-ene", build_molecule(4, unsat="ene", unsat_locs=[1], substituents=[(3, "Br"), (2, "C"), (2, "C"), (3, "C")])),
    # 46–47: trichloro + diene
    ("2,3,4-trichlorobuta-1,3-diene", build_molecule(4, unsat="ene", unsat_locs=[1, 3], substituents=[(2, "Cl"), (3, "Cl"), (4, "Cl")])),
    ("1,4-dichlorobuta-1,3-diene", build_molecule(4, unsat="ene", unsat_locs=[1, 3], substituents=[(1, "Cl"), (4, "Cl")])),
    # 48: trimethyl alkane
    ("2,3,4-trimethylhexane", build_molecule(6, substituents=[(3, "C"), (4, "C"), (5, "C")])),
    # 49: tetramethyl butane
    ("2,2,3,3-tetramethylbutane", build_molecule(4, substituents=[(2, "C"), (2, "C"), (3, "C"), (3, "C")])),
    # 50: methyl + diene
    ("2-methylbuta-1,3-diene", build_molecule(4, unsat="ene", unsat_locs=[1, 3], substituents=[(2, "C")])),
]

@pytest.mark.parametrize("expected, mol", CASES)
def test_golden_v03(expected, mol):
    assert name(mol) == expected
