#!/usr/bin/env python3
"""Snapshot Hugging Face sources into a dated folder for triage.

Shared, byte-identical, by Hebrew-AI-Models (kind: models) and Hebrew-Datasets (kind: datasets);
the kind comes from hfsearches.json. Stdlib only; run from the repo root with uv run.

  uv run scripts/snapshot.py                      # core saved searches
  uv run scripts/snapshot.py --all                # core + extra searches
  uv run scripts/snapshot.py --search tts-trending --search asr-downloads
  uv run scripts/snapshot.py --collections        # only the curated collections in collections.json
  uv run scripts/snapshot.py --limit 20           # override per-search limit (small test runs)

Writes snapshots/YYYY-MM-DD/:
  <search-id>.json              raw search results, one item per line, with the query that produced them
  collection-<key>.json         raw collection items (same shape)
  candidates.json               unique items across everything fetched that day (merged if the file
                                already exists), with pre-triage signals and any verdict already in
                                data/verdicts.json; the agent triages from this file
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
UA = {"User-Agent": "hebrew-hf-snapshot"}


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return json.load(r)


def languages(tags):
    out = []
    for t in tags:
        t = t.removeprefix("language:")
        if re.fullmatch(r"[a-z]{2,3}", t) and t not in NOT_LANG:
            out.append(t)
    return out


def search_url(cfg, s, limit):
    params = [("sort", cfg["sorts"][s["sort"]]["api"]), ("direction", "-1"), ("limit", str(limit))]
    if s.get("task") and cfg["kind"] == "models":
        params.append(("pipeline_tag", s["task"]))
    elif s.get("task"):
        params.append(("filter", f"task_categories:{s['task']}"))
    if s["mode"] == "name":
        params.append(("search", s["search"]))
    else:  # exact tag; the API's language= parameter is much looser (see api_notes)
        params.append(("filter", cfg["language_tag"]))
    return cfg["api_base"] + "?" + urllib.parse.urlencode(params)


def hint(item_id, langs, known):
    if HEBREW_NAME.search(item_id) or item_id.split("/")[0] in known:
        return "likely-specialist"
    if "he" not in langs:
        # The Hub's language filters also return items whose tags never mention Hebrew.
        return "no-hebrew-tag"
    if len(langs) >= 5:
        return "likely-multilingual"
    return "unclear"


def write_raw(path, meta, items):
    body = ",\n".join(json.dumps(m, ensure_ascii=False) for m in items)
    path.write_text(f'{{"meta": {json.dumps(meta, ensure_ascii=False)},\n"items": [\n{body}\n]}}\n')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--search", action="append", default=[])
    ap.add_argument("--collections", action="store_true")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--date", default=dt.date.today().isoformat())
    a = ap.parse_args()

    cfg = json.loads((ROOT / "hfsearches.json").read_text())
    kind = cfg["kind"]
    verdicts = json.loads((ROOT / "data/verdicts.json").read_text())["models" if kind == "models" else "datasets"]
    readme = (ROOT / "README.md").read_text()
    known = set(cfg["known_hebrew_authors"])
    now = lambda: dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")

    out = ROOT / "snapshots" / a.date
    out.mkdir(parents=True, exist_ok=True)
    cpath = out / "candidates.json"
    cands = {c["id"]: c for c in json.loads(cpath.read_text())} if cpath.exists() else {}

    def add(m, source, rank, curated=False):
        tags = m.get("tags", [])
        langs = languages(tags)
        c = cands.setdefault(m["id"], {
            "id": m["id"],
            "url": f"https://huggingface.co/{'datasets/' if kind == 'datasets' else ''}{m['id']}",
            "task": m.get("pipeline_tag") or [t.split(":", 1)[1] for t in tags if t.startswith("task_categories:")],
            "downloads": m.get("downloads"), "likes": m.get("likes"),
            "created": (m.get("createdAt") or "")[:10],
            "n_languages": len(langs), "he_tagged": "he" in langs,
            "base_model": next((t.split(":", 1)[1] for t in tags
                                if t.startswith("base_model:") and t.count(":") == 1), None),
            "hint": hint(m["id"], langs, known),
            "curated": False,
            "in_readme": m["id"] in readme,
            "prior_verdict": verdicts.get(m["id"], {}).get("verdict"),
            "seen_in": {}})
        c["seen_in"][source] = rank
        c["curated"] = c["curated"] or curated

    if a.collections:
        coll = json.loads((ROOT / "collections.json").read_text())
        want = "model" if kind == "models" else "dataset"
        for col in coll["collections"]:
            data = get(f"https://huggingface.co/api/collections/{col['slug']}")
            ids = [i["id"] for i in data["items"] if i["type"] == want]
            # Collection items carry few fields; fetch each item for tags and counts.
            items = [get(f"{cfg['api_base']}/{i}") for i in ids]
            write_raw(out / f"collection-{col['key']}.json",
                      {"collection": col["slug"], "url": col["url"], "fetched": now(), "count": len(items)}, items)
            for rank, m in enumerate(items, 1):
                add(m, f"collection:{col['key']}", rank, curated=True)
            print(f"collection {col['key']}: {len(items)} {kind}")
    else:
        chosen = [s for s in cfg["searches"]
                  if (s["id"] in a.search if a.search else (a.all or s["tier"] == "core"))]
        missing = set(a.search) - {s["id"] for s in chosen}
        if missing:
            raise SystemExit(f"unknown search id(s): {sorted(missing)}")
        for s in chosen:
            url = search_url(cfg, s, a.limit or s["limit"])
            items = get(url)
            write_raw(out / f"{s['id']}.json",
                      {"search": s["id"], "query": url, "web_url": s["web_url"], "fetched": now(), "count": len(items)}, items)
            for rank, m in enumerate(items, 1):
                add(m, s["id"], rank)
            print(f"{s['id']}: {len(items)}")

    rows = sorted(cands.values(), key=lambda c: (c["prior_verdict"] is not None, not c["curated"],
                                                 c["hint"] != "likely-specialist", -(c["downloads"] or 0)))
    cpath.write_text("[\n" + ",\n".join(json.dumps(c, ensure_ascii=False) for c in rows) + "\n]\n")
    new = sum(1 for c in rows if c["prior_verdict"] is None)
    print(f"{len(rows)} unique {kind}, {new} without a verdict -> {cpath.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
