"""Helper builder extended for multiple unsaturations and multi‑atom substituents."""
from typing import List, Union

from chemname.core.structures import Molecule


def build_molecule(
    length: int,
    *,
    unsat: str | None = None,
    unsat_locs: Union[int, List[int]] | None = None,
    substituents: list[tuple[int, Union[str, List[str]]]] | None = None,
) -> Molecule:
    """
    Build a straight‑chain molecule of given length with:
      - unsaturations of one type ('ene' or 'yne') at the given locants,
      - substituents where each is specified by (backbone_position, element or list of elements).
    Positions are 1‑based.
    """
    substituents = substituents or []
    # normalize unsat_locs into a list
    if isinstance(unsat_locs, int):
        unsats = [unsat_locs]
    else:
        unsats = list(unsat_locs) if unsat_locs is not None else []

    m = Molecule()
    # add backbone carbons
    for i in range(length):
        m.add_atom("C", i)
    # add backbone bonds (with unsaturation where specified)
    for i in range(length - 1):
        order = 1
        if unsat and (i + 1) in unsats:
            order = 2 if unsat == "ene" else 3
        m.add_bond(i, i + 1, order)

    # add substituents
    idx = length
    for pos, elem in substituents:
        # determine sequence of atoms for this substituent
        seq = [elem] if isinstance(elem, str) else list(elem)
        prev = pos - 1  # attach to backbone atom at pos‑1
        for symbol in seq:
            m.add_atom(symbol, idx)
            m.add_bond(prev, idx)
            prev = idx
            idx += 1

    return m
