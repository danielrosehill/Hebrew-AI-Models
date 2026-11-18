# Hebrew-AI-Models

Public catalogue of Hebrew AI models (README.md). Updating it from Hugging Face is the repo skill
`.claude/skills/hebrew-model-sweep/SKILL.md`; follow it for any "update the list" or "sweep" request.

- Saved Hub searches: `hfsearches.json`. Snapshot runner: `uv run scripts/snapshot.py` (stdlib only).
- Dated raw snapshots: `snapshots/YYYY-MM-DD/`, committed unedited.
- Verdicts (specialist / multilingual-notable / multilingual-skip / not-relevant): `data/verdicts.json`; rules and maintainer guidance in `docs/classification.md`.
- Hebrew specialist models and multilingual-with-Hebrew models never share a table.
