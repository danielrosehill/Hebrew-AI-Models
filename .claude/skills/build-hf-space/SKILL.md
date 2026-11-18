---
name: build-hf-space
description: Build and publish (or update) this list's Hugging Face Space, a static searchable page generated from README.md. Use on "build the Space", "update the Space", "publish to Hugging Face", or after a sweep/import changed the README.
---

# Build / update the Hugging Face Space

Shared by Hebrew-AI-Models and Hebrew-Datasets. Settings live in `space.json` (`space_id`, title, links to the companion Space, Space front matter). The Space is a static-SDK Space generated entirely from `README.md`: every `##` section, `###` subsection and the cards under them become a filterable, searchable section. `space/` is generated output: never edit it by hand, change the README or `scripts/build_space.py`.

## Steps

1. **Build:** `uv run scripts/build_space.py`. It prints sections and row count; compare with the README (a section missing usually means its cards lost their badge line: an entry is a `###`/`####` heading followed by a description, an optional `*details*` line and a `[![...](...)](url)` badge line).
2. **Look at it before publishing.** Screenshot it headless: `google-chrome --headless=new --window-size=1280,900 --screenshot=/tmp/space.png file://$PWD/space/index.html`, then read the PNG. Also check that searching works if you changed the template.
3. **Publish.** The first time, confirm with the user (it creates a public page), then `hf repo create <space_id> --repo-type space --space-sdk static` if it does not exist yet (the public URL returns 401 for a Space that does not exist; `hf upload` on its own also creates it, as seen 2026-11-18). Upload: `hf upload <space_id> space/ . --repo-type space --commit-message "Rebuild from README <git short sha>"`. Updates after that need no confirmation.
4. **Verify the live thing**, not the upload exit code: fetch `https://huggingface.co/spaces/<space_id>/raw/main/index.html` (or the `*.static.hf.space` URL) and check the build date in the footer matches today.
5. **Commit** `space/` along with whatever README change triggered the rebuild, and push.

## Notes

- The template is inside `scripts/build_space.py` (`PAGE`). The script is byte-identical in both repos: copy a change to the other repo in the same session.
- Sections skipped from the Space: Contents, Table of Contents, Contributing, License, How this list is maintained (`SKIP_SECTIONS`).
