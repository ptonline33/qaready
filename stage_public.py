#!/usr/bin/env python3
"""Stage the static PWA into public/ for Vercel's static builder.

GitHub Pages serves the repository root directly, but Vercel's static builder
expects a build output directory (default: `public`). Rather than duplicate every
asset in git, this script generates `public/` from the same source files at
build time. `public/` is gitignored - it is a build artefact, not source.

Run automatically by `npm run build` (see package.json).
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "public"

FILES = ["index.html", "styles.css", "manifest.webmanifest", "sw.js", ".nojekyll"]
DIRS = ["js", "data", "fonts", "icons", "vendor"]


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    for name in FILES:
        src = ROOT / name
        if src.exists():
            shutil.copy2(src, OUT / name)

    for name in DIRS:
        src = ROOT / name
        if src.exists():
            shutil.copytree(src, OUT / name,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    count = sum(1 for p in OUT.rglob("*") if p.is_file())
    print(f"Staged {count} files into public/ (Vercel output directory)")
    for name in ["index.html", "data/content.js", "js/app.js", "sw.js", "manifest.webmanifest"]:
        if not (OUT / name).exists():
            raise SystemExit(f"ERROR: {name} was not staged")
    print("All required PWA assets present.")


if __name__ == "__main__":
    main()
