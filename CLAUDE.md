# Hebrew-AI-Models

Public catalogue of Hebrew AI models (README.md). Updating it from Hugging Face is the repo skill
`.claude/skills/hebrew-model-sweep/SKILL.md`; follow it for any "update the list" or "sweep" request.

- Saved Hub searches: `hfsearches.json`. Snapshot runner: `uv run scripts/snapshot.py` (stdlib only).
- Dated raw snapshots: `snapshots/YYYY-MM-DD/`, committed unedited.
- Verdicts (specialist / multilingual-notable / multilingual-skip / not-relevant): `data/verdicts.json`; rules and maintainer guidance in `docs/classification.md`.
- Curated HF collections: `collections.json`, imported by skill `import-collections`; README table between `collections:start/end` markers is generated (`scripts/render_collections.py`).
- Hugging Face Space (static, generated from README): `space.json`, `scripts/build_space.py`, skill `build-hf-space`; `space/` is build output.
- Companion repo `danielrosehill/Hebrew-Datasets` shares `scripts/*.py` byte-identical; copy changes across.
- Hebrew specialist models and multilingual-with-Hebrew models never share a table.
