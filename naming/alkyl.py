"""Collect straight‑chain alkyl substituents."""

from collections import defaultdict
from typing import Dict, List

from ..core.structures import Molecule
from ..util import YL_NAMES


def get_alkyl_substituents(chain: list[int], mol: Molecule) -> Dict[str, List[int]]:
    """Return {alkyl_name: [locants]}."""
    backbone = set(chain)
    loc_by_idx = {idx: pos for pos, idx in enumerate(chain, 1)}
    subs = defaultdict(list)

    for c in chain:
        for nb in mol.neighbours(c):
            if nb in backbone:
                continue
            frag = []
            stack = [nb]
            seen = set(stack)
            while stack:
                a = stack.pop()
                atom = mol._atoms[a]  # type: ignore[attr-defined]
                if atom.symbol != "C":
                    frag = []  # hetero atom encountered – skip
                    break
                frag.append(a)
                for x in mol.neighbours(a):
                    if x not in seen and x not in backbone:
                        stack.append(x)
                        seen.add(x)
            if frag:
                length = len(frag)
                if 1 <= length <= 12:
                    subs[YL_NAMES[length]].append(loc_by_idx[c])

    for v in subs.values():
        v.sort()
    return dict(subs)
