#!/usr/bin/env python3
"""Regenerate the curated-collections table in README.md from collections.json.

Shared, byte-identical, by Hebrew-AI-Models and Hebrew-Datasets. Replaces everything between
<!-- collections:start --> and <!-- collections:end --> in README.md. Stdlib only.

  uv run scripts/render_collections.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
START, END = "<!-- collections:start -->", "<!-- collections:end -->"

cfg = json.loads((ROOT / "collections.json").read_text())
rows = "\n".join(f"| [{c['title']}]({c['url']}) | {c['why']} |" for c in cfg["collections"])
block = (f"{START}\n<!-- Generated from collections.json by scripts/render_collections.py; edit that file, not this table. -->\n"
         f"| Collection | Contents |\n|------------|----------|\n{rows}\n\n"
         f"All collections: [{cfg['owner_collections_url']}]({cfg['owner_collections_url']})\n{END}")
readme = (ROOT / "README.md").read_text()
if START not in readme:
    raise SystemExit(f"README.md has no {START} marker; add the markers where the table belongs")
head, rest = readme.split(START, 1)
(ROOT / "README.md").write_text(head + block + rest.split(END, 1)[1])
print(f"{len(cfg['collections'])} collections -> README.md")
