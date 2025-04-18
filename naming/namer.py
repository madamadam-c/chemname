"""Public naming façade (v0.3)."""

from itertools import chain as it_chain
from typing import Dict, List, Tuple

from ..core.structures import Molecule
from .assembler import assemble_name
from .chain_finder import find_chain
from .substituents import get_all_substituents


def _alphabetic_key(s: str) -> str:
    """Ignore multiplier prefixes when sorting."""
    for p in ("di", "tri", "tetra"):
        if s.startswith(p):
            return s[len(p) :]
    return s


def _convert_locs(locs: List[int], length: int, forward: bool) -> List[int]:
    return locs if forward else [length + 1 - l for l in locs]


def _orientation_score(
    length: int,
    unsat_locs: List[int],
    subs: Dict[str, List[int]],
    forward: bool,
) -> Tuple:
    convert = (lambda ls: _convert_locs(ls, length, forward))

    uns_conv = convert(unsat_locs) or [999]
    sub_locs = sorted(convert(list(it_chain.from_iterable(subs.values())))) or [999]
    return (*uns_conv, *sub_locs)


def name(mol: Molecule) -> str:  # noqa: C901
    chain = find_chain(mol)
    if not chain:
        raise ValueError("No carbon chain found")

    # collect unsaturations
    unsat_type = None
    unsat_pos: List[int] = []
    for i in range(len(chain) - 1):
        bond = mol._bonds[frozenset({chain[i], chain[i + 1]})]  # type: ignore[attr-defined]
        if bond.order in {2, 3}:
            typ = "ene" if bond.order == 2 else "yne"
            if unsat_type and typ != unsat_type:
                raise ValueError("Mixed double/triple bonds not yet supported")
            unsat_type = typ
            unsat_pos.append(i + 1)

    subs = get_all_substituents(chain, mol)
    length = len(chain)

    # choose orientation with full lowest‑set + alphabetical tie‑break
    fwd_score = _orientation_score(length, unsat_pos, subs, True)
    rev_score = _orientation_score(length, unsat_pos, subs, False)

    if fwd_score < rev_score:
        forward = True
    elif rev_score < fwd_score:
        forward = False
    else:
        # tie‑break: find alphabetically first substituent (ignoring di/tri)
        keys = sorted(subs.keys(), key=lambda s: _alphabetic_key(s))
        if keys:
            first = keys[0]
            # compare locant for that substituent
            loc_fwd = subs[first][0]
            loc_rev = length + 1 - loc_fwd
            forward = loc_fwd < loc_rev
        else:
            forward = True

    if not forward:
        chain.reverse()
        unsat_pos = _convert_locs(unsat_pos, length, False)
        subs = {k: sorted(_convert_locs(v, length, False)) for k, v in subs.items()}

    # α‑order substituents (ignoring di/tri)
    subs_list = sorted(
        subs.items(),
        key=lambda kv: _alphabetic_key(kv[0]),
    )

    return assemble_name(length, unsat_type, sorted(unsat_pos), subs_list)
