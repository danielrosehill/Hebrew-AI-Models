#!/usr/bin/env python3
"""Take a dated firehose snapshot of the Hugging Face searches in hfsearches.json.

Stdlib only; run with `uv run scripts/snapshot.py` (or plain python3) from the repo root.

  uv run scripts/snapshot.py                  # core: llm/asr/tts x (trending, downloads, name)
  uv run scripts/snapshot.py --all            # core + extra
  uv run scripts/snapshot.py --search tts-trending --search asr-downloads
  uv run scripts/snapshot.py --limit 20       # override per-search limit (small test runs)

Writes snapshots/YYYY-MM-DD/:
  <search-id>.json   raw results, one model per line, with the query that produced them
  candidates.json    unique models across those searches, with pre-triage signals and any
                     verdict already in data/verdicts.json; the agent triages from this file
"""
import argparse
import datetime as dt
import json
import pathlib
import re
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
HEBREW_NAME = re.compile(r"hebrew|ivrit|hebrish|(^|[-_/.])(he|heb)([-_/.]|$)", re.I)
# Short tags that look like language codes but are not.
NOT_LANG = {"asr", "tdt", "jax", "mlx", "tts", "stt", "gpt", "llm", "ctc", "vad", "sft", "dpo",
            "orpo", "onnx", "pt", "art", "ocr", "lid", "nlp", "ner", "moe", "rl", "us", "eu"}


def languages(tags):
    return [t for t in tags if re.fullmatch(r"[a-z]{2,3}", t) and t not in NOT_LANG]


def fetch(cfg, search, limit):
    params = {"pipeline_tag": search["task"], "sort": cfg["sorts"][search["sort"]]["api"],
              "direction": "-1", "limit": str(limit)}
    if search["mode"] == "name":
        params["search"] = search["search"]
    else:  # exact tag; the API's language= parameter is much looser (see api_notes)
        params["filter"] = cfg["language"]
    url = cfg["api_base"] + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "hebrew-ai-models-snapshot"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return url, json.load(r)


def hint(m, langs, known):
    author = m["id"].split("/")[0]
    if HEBREW_NAME.search(m["id"]) or author in known:
        return "likely-specialist"
    if "he" not in langs:
        # The Hub's language=he filter also returns models whose tags never mention Hebrew.
        return "no-hebrew-tag"
    if len(langs) >= 5:
        return "likely-multilingual"
    return "unclear"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--search", action="append", default=[])
    ap.add_argument("--limit", type=int)
    ap.add_argument("--date", default=dt.date.today().isoformat())
    a = ap.parse_args()

    cfg = json.loads((ROOT / "hfsearches.json").read_text())
    verdicts = json.loads((ROOT / "data/verdicts.json").read_text())["models"]
    readme = (ROOT / "README.md").read_text()
    known = set(cfg["known_hebrew_authors"])
    chosen = [s for s in cfg["searches"]
              if (s["id"] in a.search if a.search else (a.all or s["tier"] == "core"))]
    missing = set(a.search) - {s["id"] for s in chosen}
    if missing:
        raise SystemExit(f"unknown search id(s): {sorted(missing)}")

    out = ROOT / "snapshots" / a.date
    out.mkdir(parents=True, exist_ok=True)
    cands = {}
    for s in chosen:
        url, models = fetch(cfg, s, a.limit or s["limit"])
        body = ",\n".join(json.dumps(m, ensure_ascii=False) for m in models)
        head = json.dumps({"search": s["id"], "query": url, "web_url": s["web_url"],
                           "fetched": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                           "count": len(models)}, ensure_ascii=False)
        (out / f"{s['id']}.json").write_text(f'{{"meta": {head},\n"models": [\n{body}\n]}}\n')
        for rank, m in enumerate(models, 1):
            tags = m.get("tags", [])
            langs = languages(tags)
            c = cands.setdefault(m["id"], {
                "id": m["id"], "url": f"https://huggingface.co/{m['id']}",
                "pipeline_tag": m.get("pipeline_tag"), "downloads": m.get("downloads"),
                "likes": m.get("likes"), "created": (m.get("createdAt") or "")[:10],
                "n_languages": len(langs), "he_tagged": "he" in langs,
                "base_model": next((t.split(":", 1)[1] for t in tags if t.startswith("base_model:")
                                    and t.count(":") == 1), None),
                "hint": hint(m, langs, known),
                "in_readme": m["id"] in readme,
                "prior_verdict": verdicts.get(m["id"], {}).get("verdict"),
                "seen_in": {}})
            c["seen_in"][s["id"]] = rank
        print(f"{s['id']}: {len(models)}")

    rows = sorted(cands.values(), key=lambda c: (c["prior_verdict"] is not None, c["hint"] != "likely-specialist", -(c["downloads"] or 0)))
    body = ",\n".join(json.dumps(c, ensure_ascii=False) for c in rows)
    (out / "candidates.json").write_text(f"[\n{body}\n]\n")
    new = sum(1 for c in rows if c["prior_verdict"] is None)
    print(f"{len(rows)} unique models, {new} without a verdict -> {out.relative_to(ROOT)}/candidates.json")


if __name__ == "__main__":
    main()
