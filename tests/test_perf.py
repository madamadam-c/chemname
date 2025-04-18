"""Performance guard: 1 000 random molecules ≤ 0.5 s."""
import os
import random
import time

import pytest

from chemname.core.structures import Molecule
from chemname.naming.namer import name

SKIP = os.getenv("CI_SKIPPERF")

@pytest.mark.skipif(SKIP, reason="Perf test skipped by env var")
def test_perf_1000():
    random.seed(42)
    molecules = []
    for _ in range(1000):
        n = random.randint(1, 12)
        unsat = random.choice([None, "ene", "yne"])
        unsat_loc = None
        if unsat and n >= 2:
            unsat_loc = random.randint(1, n - 1)
        subs = []
        for _ in range(random.randint(0, 3)):
            loc = random.randint(1, n)
            elem = random.choice(["F", "Cl", "Br", "I"])
            subs.append((loc, elem))
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
        molecules.append(m)

    t0 = time.perf_counter()
    for m in molecules:
        name(m)
    duration = time.perf_counter() - t0
    assert duration < 0.5
