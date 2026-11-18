#!/usr/bin/env python3
"""Regenerate the curated-collections cards in README.md from collections.json.

Shared, byte-identical, by Hebrew-AI-Models and Hebrew-Datasets. Replaces everything between
<!-- collections:start --> and <!-- collections:end --> in README.md. Stdlib only.

  uv run scripts/render_collections.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
START, END = "<!-- collections:start -->", "<!-- collections:end -->"

cfg = json.loads((ROOT / "collections.json").read_text())
BADGE = "[![Collection](https://img.shields.io/badge/Hugging_Face-Collection-FFD21E?style=flat&logo=huggingface)]({url})"
cards = "\n\n---\n\n".join(
    f"### {c['title']}\n\n{c['why'].rstrip('.')}.\n\n" + BADGE.format(url=c["url"])
    for c in sorted(cfg["collections"], key=lambda c: c["title"].lower()))
block = (f"{START}\n<!-- Generated from collections.json by scripts/render_collections.py; edit that file, not these cards. -->\n\n"
         f"{cards}\n\n---\n\nAll collections: [{cfg['owner_collections_url']}]({cfg['owner_collections_url']})\n{END}")
readme = (ROOT / "README.md").read_text()
if START not in readme:
    raise SystemExit(f"README.md has no {START} marker; add the markers where the table belongs")
head, rest = readme.split(START, 1)
(ROOT / "README.md").write_text(head + block + rest.split(END, 1)[1])
print(f"{len(cfg['collections'])} collections -> README.md")
