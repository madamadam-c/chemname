"""Assemble parent name string."""

from typing import List, Sequence, Tuple

from ..util import MULTIPLIER_PREFIXES, ROOT_NAMES


def _subs_to_string(groups: Sequence[Tuple[str, List[int]]]) -> str:
    if not groups:
        return ""
    frags = []
    for name, locs in groups:
        locants = ",".join(map(str, locs))
        mult = MULTIPLIER_PREFIXES.get(len(locs), "")
        prefix = f"{mult}{name}" if mult else name
        frags.append(f"{locants}-{prefix}")
    return "-".join(frags)


def assemble_parent(
    chain_len: int,
    unsat_type: str | None,
    unsat_locs: List[int],
) -> str:
    root = ROOT_NAMES[chain_len]
    if not unsat_type:
        return f"{root}ane"

    if len(unsat_locs) == 1:
        loc = unsat_locs[0]
        if chain_len == 2 and loc == 1:
            return f"{root}{unsat_type}"
        return f"{root}-{loc}-{unsat_type}"

    # multiple unsaturations → use connecting vowel “a” and multiplicative prefix
    root = root + "a"
    locs = ",".join(map(str, unsat_locs))
    mult = MULTIPLIER_PREFIXES[len(unsat_locs)]
    return f"{root}-{locs}-{mult}{unsat_type}"


def assemble_name(
    chain_len: int,
    unsat_type: str | None,
    unsat_locs: List[int],
    substituents: List[Tuple[str, List[int]]],
) -> str:
    subs_part = _subs_to_string(substituents)
    parent = assemble_parent(chain_len, unsat_type, unsat_locs)
    name = f"{subs_part}{parent}" if subs_part else parent

    # drop redundant locant “1-” for monosubstituted methane/ethane
    if (
        subs_part
        and chain_len <= 2
        and len(substituents) == 1
        and substituents[0][1] == [1]
        and name.startswith("1-")
    ):
        return name[2:]
    return name
