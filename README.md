# chemname v0.1.0

Core graph data structures (Atom, Bond, Molecule) for a zero‑dependency IUPAC
naming engine.  Future versions will add naming logic incrementally.

## Quickstart

```bash
python -m pip install -e .
pytest -q

## Changelog

### v0.2.0 — Straight‑chain naming
- Add naming of straight‑chain alkanes, alkenes, alkynes, and haloalkanes  
- Enforce lowest‑set locants and drop redundant “1‑” for monosubstituted methane/ethane and ethene  
- 50 golden regression tests locked in `tests/golden`  
- Performance guard: ≤ 0.5 s naming 1 000 random C₁₂ molecules  

### v0.3.0 — Multi‑unsaturation & alkyl substituents
- Detect and name multiple double/triple bonds (diene, triene, diyne, …) with correct multiplicative prefixes  
- recognise straight‑chain alkyl substituents (methyl → dodecyl) alongside halogens  
- apply full lowest‑set locant rule including alphabetical tie‑break for substituents  
- 50 new golden regression tests covering all new features  
