from pathlib import Path

from setuptools import find_packages, setup

NAME = "chemname"
VERSION = "0.2.0"

README = Path(__file__).with_name("README.md").read_text(encoding="utf‑8")

setup(
    name=NAME,
    version=VERSION,
    description="Zero‑dependency IUPAC naming engine (core graph model)",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Katherine Eyal",
    url="https://github.com/your‑org/chemname",
    python_requires=">=3.9",
    packages=find_packages(include=[NAME, f"{NAME}.*"]),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
    zip_safe=False,
)
