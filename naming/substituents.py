"""Merge halogen and alkyl substituents."""

from typing import Dict, List

from ..core.structures import Molecule
from .alkyl import get_alkyl_substituents
from ..util import HALO_PREFIXES


def get_all_substituents(chain: list[int], mol: Molecule) -> Dict[str, List[int]]:
    """Return merged substituent map."""
    loc_by_idx = {idx: pos for pos, idx in enumerate(chain, 1)}
    halo = {}
    # halogens
    for c in chain:
        for nb in mol.neighbours(c):
            atom = mol._atoms[nb]  # type: ignore[attr-defined]
            if atom.symbol in HALO_PREFIXES and nb not in loc_by_idx:
                name = HALO_PREFIXES[atom.symbol]
                halo.setdefault(name, []).append(loc_by_idx[c])

    for v in halo.values():
        v.sort()

    # alkyls
    alkyl = get_alkyl_substituents(chain, mol)

    merged: Dict[str, List[int]] = {}
    merged.update(halo)
    merged.update(alkyl)
    return merged
