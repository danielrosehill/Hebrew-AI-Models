---
name: import-collections
description: Import the maintainer's curated Hugging Face collections (listed in collections.json) into this list. Fetch the items of this repo's kind (models or datasets), triage each new one, file it in the README, and refresh the collections table. Use on "import my collections", "sync from my HF collections", "add what's in my Hebrew collection", or after adding a collection to collections.json.
---

# Import curated collections

Shared by Hebrew-AI-Models (imports models) and Hebrew-Datasets (imports datasets). The kind comes from `hfsearches.json` → `kind`. This repo's sweep skill (`hebrew-model-sweep` or `hebrew-dataset-sweep`) owns the triage and README rules; this skill only changes the source.

## Steps

1. **Refresh the collection list if asked.** The maintainer's collections are at https://huggingface.co/danielrosehill/collections. To find new Hebrew-relevant ones: `curl -s "https://huggingface.co/api/collections?owner=danielrosehill&q=hebrew&limit=100"` (also try `q=sentence`, `q=audio`, `q=code-switching`). The list endpoint returns at most 100 and only the first 4 items of each, so search by `q` and fetch each collection on its own. Add new ones to `collections.json` with a short `key`, the full `slug` (it ends in a hash; links without it 404), `title`, `url` and a one-line `why`. A collection that holds both models and datasets goes in both repos' `collections.json`.
2. **Snapshot.** `uv run scripts/snapshot.py --collections`. This writes `snapshots/YYYY-MM-DD/collection-<key>.json` and merges into that day's `candidates.json`; items from collections have `curated: true`.
3. **Triage** the candidates with no `prior_verdict`, following steps 3 to 5 of the sweep skill and `docs/classification.md`. Curated means the maintainer thought the item was worth saving, not that it's a Hebrew specialist: a multilingual item from a collection is usually `multilingual-notable` rather than `multilingual-skip`.
4. **File** new items in the README following step 6 of the sweep skill. Items already in the README (`in_readme: true`) still get a verdict entry.
5. **Regenerate the collections table:** `uv run scripts/render_collections.py`. It rewrites the block between the `collections:start/end` markers; never hand-edit that block.
6. **Report and ship** following steps 7 and 8 of the sweep skill. If the Space exists, offer to rebuild it (skill `build-hf-space`).
