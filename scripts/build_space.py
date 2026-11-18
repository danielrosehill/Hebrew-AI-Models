#!/usr/bin/env python3
"""Build the Hugging Face Space (static SDK) for this list from README.md.

Shared, byte-identical, by Hebrew-AI-Models and Hebrew-Datasets. Settings come from space.json.
README.md is the source: every `## Section` / `### Subsection` and every markdown table under it
becomes a searchable, filterable page. Stdlib only.

  uv run scripts/build_space.py            # writes space/ (README.md with Space front matter, index.html, data.json)

Publish (see the build-hf-space skill):
  hf upload <space_id> space/ . --repo-type space --commit-message "..."
"""
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
SKIP_SECTIONS = {"Table of Contents", "Contributing", "License", "How this list is maintained"}


def md_inline(text):
    text = html.escape(text, quote=False)
    text = LINK.sub(lambda m: f'<a href="{html.escape(m[2])}" target="_blank" rel="noopener">{m[1]}</a>', text)
    return re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)


def parse(readme):
    sections, sec, sub, header, intro = [], None, None, None, []
    for line in readme.splitlines():
        if line.startswith("## "):
            name = line[3:].strip()
            sec = None if name in SKIP_SECTIONS else {"name": name, "tables": []}
            if sec:
                sections.append(sec)
            sub, header = None, None
        elif line.startswith("### ") and sec:
            sub, header = line[4:].strip(), None
        elif line.startswith("|") and sec:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                continue
            if header is None:
                header = cells
                sec["tables"].append({"subsection": sub, "columns": header, "rows": []})
            else:
                sec["tables"][-1]["rows"].append(cells)
        else:
            header = None
    return [s for s in sections if any(t["rows"] for t in s["tables"])]


PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<style>
body{{font-family:system-ui,sans-serif;margin:0;color:#1d1d1f;background:#fafafa}}
header{{padding:24px 32px;background:#fff;border-bottom:1px solid #e5e5e5}}
h1{{margin:0 0 6px;font-size:1.6rem}} header p{{margin:4px 0;color:#555}}
.bar{{position:sticky;top:0;background:#fafafa;padding:12px 32px;border-bottom:1px solid #e5e5e5;display:flex;gap:8px;flex-wrap:wrap;align-items:center}}
input{{padding:8px 12px;font-size:1rem;border:1px solid #ccc;border-radius:8px;min-width:260px}}
button{{padding:6px 12px;border:1px solid #ccc;border-radius:16px;background:#fff;cursor:pointer;font-size:.85rem}}
button.on{{background:#1d1d1f;color:#fff;border-color:#1d1d1f}}
main{{padding:8px 32px 48px}} h2{{margin-top:32px}} h3{{color:#444;font-size:1rem;margin:18px 0 6px}}
table{{border-collapse:collapse;width:100%;background:#fff;font-size:.9rem}}
th,td{{text-align:left;padding:6px 10px;border-bottom:1px solid #eee;vertical-align:top}} th{{background:#f3f3f3}}
a{{color:#0b57d0;text-decoration:none}} a:hover{{text-decoration:underline}} .hidden{{display:none}}
footer{{padding:24px 32px;color:#777;font-size:.85rem}}
</style></head><body>
<header><h1>{title}</h1><p>{subtitle}</p><p><a href="{repo}" target="_blank">Source list on GitHub</a>{links}</p></header>
<div class="bar"><input id="q" placeholder="Search names, authors, descriptions..." autofocus><span id="chips"></span></div>
<main id="main"></main>
<footer>Generated from README.md of <a href="{repo}">{repo_name}</a> on {built}.</footer>
<script>
const DATA={data};
const main=document.getElementById('main'),chips=document.getElementById('chips'),q=document.getElementById('q');
let active=null;
DATA.forEach((s,i)=>{{const b=document.createElement('button');b.textContent=s.name;b.onclick=()=>{{active=active===i?null:i;render()}};chips.appendChild(b)}});
function render(){{
 const term=q.value.toLowerCase();main.innerHTML='';
 [...chips.children].forEach((b,i)=>b.className=active===i?'on':'');
 DATA.forEach((s,i)=>{{
  if(active!==null&&active!==i)return;
  let out='';
  s.tables.forEach(t=>{{
   const rows=t.rows.filter(r=>!term||r.text.includes(term));
   if(!rows.length)return;
   out+=(t.subsection?`<h3>${{t.subsection}}</h3>`:'')+'<table><tr>'+t.columns.map(c=>`<th>${{c}}</th>`).join('')+'</tr>'+
     rows.map(r=>'<tr>'+r.cells.map(c=>`<td>${{c}}</td>`).join('')+'</tr>').join('')+'</table>';
  }});
  if(out)main.innerHTML+=`<h2>${{s.name}}</h2>`+out;
 }});
 if(!main.innerHTML)main.innerHTML='<p>No matches.</p>';
}}
q.oninput=render;render();
</script></body></html>
"""


def main():
    cfg = json.loads((ROOT / "space.json").read_text())
    sections = parse((ROOT / "README.md").read_text())
    import datetime as dt
    built = dt.date.today().isoformat()
    data = [{"name": s["name"], "tables": [
        {"subsection": t["subsection"], "columns": [md_inline(c) for c in t["columns"]],
         "rows": [{"cells": [md_inline(c) for c in r], "text": " ".join(r).lower()} for r in t["rows"]]}
        for t in s["tables"] if t["rows"]]} for s in sections]
    out = ROOT / "space"
    out.mkdir(exist_ok=True)
    links = "".join(f' · <a href="{u}" target="_blank">{html.escape(n)}</a>' for n, u in cfg.get("links", {}).items())
    (out / "index.html").write_text(PAGE.format(
        title=html.escape(cfg["title"]), subtitle=html.escape(cfg["subtitle"]), repo=cfg["github_repo"],
        repo_name=cfg["github_repo"].split("github.com/")[-1], links=links, built=built,
        data=json.dumps(data, ensure_ascii=False)))
    (out / "data.json").write_text(json.dumps(sections, ensure_ascii=False, indent=1) + "\n")
    fm = cfg["front_matter"]
    (out / "README.md").write_text(
        "---\n" + "".join(f"{k}: {v}\n" for k, v in fm.items()) + "---\n\n"
        f"# {cfg['title']}\n\n{cfg['subtitle']}\n\nGenerated from [{cfg['github_repo']}]({cfg['github_repo']}); "
        "edit the list there, not here.\n")
    n = sum(len(t["rows"]) for s in sections for t in s["tables"])
    print(f"{len(sections)} sections, {n} rows -> space/ (target {cfg['space_id']})")


if __name__ == "__main__":
    main()
