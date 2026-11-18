# Classifying swept models: Hebrew specialist or multilingual

A Hugging Face search for Hebrew returns mostly models that **support** Hebrew among many languages
(Whisper, XTTS, OmniVoice, Qwen...). Those are not Hebrew models. The list keeps the two apart:
each README task section has Hebrew specialist subsections first, then a
`### Multilingual models with Hebrew support` subsection.

## Verdicts

Each model in `data/verdicts.json` gets exactly one:

| Verdict | Meaning | Goes in README |
|---|---|---|
| `specialist` | Built, trained or fine-tuned **for Hebrew**: Hebrew is the target language, or one side of a pair (English-Hebrew code-switching, he↔en translation). Includes quantisations and format conversions of a specialist (set `variant_of`). | Specialist tables of the task section |
| `multilingual-notable` | A general multilingual model that supports Hebrew and is worth a Hebrew user's attention: widely used, Hebrew quality reported or benchmarked, or an obvious base for Hebrew fine-tunes. | `Multilingual models with Hebrew support` subsection |
| `multilingual-skip` | Supports Hebrew, nothing Hebrew-specific to say. Recorded so later sweeps skip it. | No |
| `not-relevant` | Carries the Hebrew tag without real Hebrew support, or is not a model for the task (diarization, aligners, test repos, empty cards). | No |

Verdict entry shape (`data/verdicts.json` → `models`):

```json
"ivrit-ai/whisper-large-v3-turbo": {
  "verdict": "specialist",
  "task": "automatic-speech-recognition",
  "reason": "Whisper large-v3-turbo fine-tuned on ivrit.ai Hebrew corpora",
  "variant_of": null,
  "first_seen": "2026-11-18",
  "decided": "2026-11-18"
}
```

## How to tell them apart

Evidence, strongest first:

1. **Model card says so.** "Fine-tuned on Hebrew", Hebrew datasets (ivrit-ai, saspeech, HebDB, Knesset, CommonVoice he), Hebrew-only eval numbers → `specialist`.
2. **Base model plus a Hebrew name.** `base_model:` is a general model and the id contains hebrew/heb/he → probably a Hebrew fine-tune; confirm on the card. A merge or quant of a Hebrew model is a `specialist` variant.
3. **Language tags.** Five or more languages and no Hebrew in the name or card → multilingual. One to three languages including `he` → check the card; often specialist or bilingual.
4. **Author.** Known Hebrew orgs (`known_hebrew_authors` in `hfsearches.json`) publish specialists, but not exclusively (dicta-il also has multilingual work), so still read the card.

`snapshot.py` pre-labels a `hint` (`likely-specialist`, `likely-multilingual`, `unclear`, `no-hebrew-tag`) from these
signals. A hint is not a verdict. A Hebrew name with no card, or a "hebrew" fine-tune trained on 20 clips,
is still a specialist, but the README description should say it's thin.

## Maintainer guidance

Rules the maintainer has given for edge cases. Add new ones here, dated, and apply them before the
general criteria above.

- 2026-11-18: A multilingual model that lists Hebrew support is not a Hebrew specialist; when it is worth listing it goes in the separate multilingual subsection, never mixed into the specialist subsections.
