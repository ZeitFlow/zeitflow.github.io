#!/usr/bin/env python3
"""Prepare the static site without publishing repository files or documentation."""

from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist"
FILES = (
    "index.html",
    "legal.css",
    "impressum/index.html",
    "privacy/index.html",
)


def build():
    for name in FILES:
        if not (ROOT / name).is_file():
            raise FileNotFoundError(f"Missing website asset: {name}")
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    for name in FILES:
        destination = OUTPUT / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, destination)
    print(f"Prepared {len(FILES)} static assets in {OUTPUT.name}/")


if __name__ == "__main__":
    build()
