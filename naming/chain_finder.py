"""Detect the (unique) longest carbon chain in an unbranched molecule."""

from collections import deque
from typing import List

from ..core.structures import Molecule


def _distance(n: int, parents: dict[int, int | None]) -> int:
    d = 0
    while parents[n] is not None:
        n = parents[n]  # type: ignore[assignment]
        d += 1
    return d


def find_chain(mol: Molecule) -> List[int]:
    """Return carbon indices in order along the chain (0‑based)."""
    carbons = [a.index for a in mol if a.symbol == "C"]
    if not carbons:  # pragma: no cover – invalid input
        return []

    # adjacency limited to carbon–carbon bonds
    adj: dict[int, list[int]] = {c: [] for c in carbons}
    for bond in mol._bonds.values():  # type: ignore[attr-defined]
        i, j = tuple(bond.atoms)
        if i in adj and j in adj:
            adj[i].append(j)
            adj[j].append(i)

    # pick an endpoint (degree 1) or the first carbon
    start = next((c for c in carbons if len(adj[c]) == 1), carbons[0])

    # BFS tree
    parent = {start: None}
    q = deque([start])
    while q:
        v = q.popleft()
        for nb in adj[v]:
            if nb not in parent:
                parent[nb] = v
                q.append(nb)

    # farthest node from start
    end = max(parent, key=lambda n: _distance(n, parent))

    # reconstruct path
    path: list[int] = []
    cur: int | None = end
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path
