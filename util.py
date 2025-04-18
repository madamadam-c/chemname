"""Shared constants."""
ROOT_NAMES = {
    1: "meth",
    2: "eth",
    3: "prop",
    4: "but",
    5: "pent",
    6: "hex",
    7: "hept",
    8: "oct",
    9: "non",
    10: "dec",
    11: "undec",
    12: "dodec",
}

YL_NAMES = {n: root + "yl" for n, root in ROOT_NAMES.items()}
MULTIPLIER_PREFIXES = {2: "di", 3: "tri", 4: "tetra"}
HALO_PREFIXES = {"F": "fluoro", "Cl": "chloro", "Br": "bromo", "I": "iodo"}
