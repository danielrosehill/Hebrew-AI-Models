---
name: hebrew-model-sweep
description: Sweep Hugging Face for Hebrew models (LLM, ASR, TTS and more) with the saved searches in hfsearches.json, keep a dated firehose snapshot, triage each new model as Hebrew specialist vs multilingual-with-Hebrew, and update the README. Use on "sweep Hugging Face", "update the Hebrew models list", "check trending Hebrew TTS", "new Hebrew ASR models".
---

# Hebrew model sweep

Repo root: the `Hebrew-AI-Models` checkout. Files:

- `hfsearches.json`: saved searches. Each one is the Hebrew filter plus a task plus a sort; `mode: name` searches match model ids containing `heb`. `web_url` opens the same search in a browser.
- `scripts/snapshot.py`: runs the searches and writes `snapshots/YYYY-MM-DD/` (raw `<search-id>.json` files plus `candidates.json`).
- `docs/classification.md`: verdicts, evidence rules and **Maintainer guidance**. Read it before triaging, every time.
- `data/verdicts.json`: one verdict per model id, cumulative across sweeps.

## Steps

1. **Pick searches.** Default is core: LLM, ASR and TTS × trending, downloads and name. If the user names a task or sort ("trending TTS", "most downloaded ASR"), use `--search <id>`. A task or sort with no entry yet: add an entry to `hfsearches.json` first (copy an existing one, set `task` (the Hub pipeline_tag), `sort`, `mode` and `web_url`), then run it. Use `--all` for the extra tasks (translation, embeddings, NER, OCR...).
2. **Snapshot.** `uv run scripts/snapshot.py [--search id ...] [--all]`. The snapshot files are the firehose record; commit them unedited.
3. **Auto-close tag noise.** Candidates with `hint: no-hebrew-tag` and no prior verdict get `not-relevant` with reason "no he tag; Hub filter noise", without reading the card.
4. **Triage the rest.** Only candidates whose `prior_verdict` is null. Go through `likely-specialist` first, then `unclear`, then `likely-multilingual`. For anything not obvious from id, tags and `base_model`, read the card (`https://huggingface.co/<id>/raw/main/README.md`). Apply Maintainer guidance first, then the general criteria. For `likely-multilingual`, judge by id/tags in bulk and open a card only for well-known or high-download models that might be `multilingual-notable`. Write each verdict to `data/verdicts.json` with `reason`, `first_seen` and `decided` (the snapshot date).
5. **Ask when unsure.** If a model really sits on the line (a bilingual model, or a multilingual model with a Hebrew-specific checkpoint), list those few to the user with your lean and the evidence. Their answer becomes a dated line under Maintainer guidance, so the same question isn't asked twice.
6. **Update the README.** Add new `specialist` models to the task section's specialist tables (by org where an org table exists, else "Other ..."), with a one-line description taken from the card; put quant/format variants on the parent's row or right below it. Add new `multilingual-notable` models to that section's `### Multilingual models with Hebrew support` subsection, creating it at the end of the section if it's missing. Never mix the two. Bump **Last updated**.
7. **Report** to the user: per task, how many new specialists and notable multilinguals were added (named), how many were auto-closed or skipped, and any open questions from step 5.
8. **Commit and push** the snapshot, verdicts, README and any guidance changes in one commit.

## Notes

- The Hub API's `language=he` parameter is loose: on 2026-11-18 it returned 1000 TTS models of which 54 had the `he` tag. The script uses `filter=he` (exact tag) instead; see `api_notes` in `hfsearches.json`. The website's `language=he` URL is fine for browsing.
- Trending and downloads top-100 lists are dominated by multilingual models. Specialists mostly come in through the `*-name` searches.
- Keep snapshot dates ISO (`YYYY-MM-DD`). For a second sweep on the same day, pass `--date YYYY-MM-DD-2`.
