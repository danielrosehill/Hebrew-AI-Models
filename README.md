[![Master Index](https://img.shields.io/badge/Master_Index-GitHub-blue?style=for-the-badge&logo=github)](https://github.com/danielrosehill/Index)

# Hebrew AI Models

A catalog of AI models for the Hebrew language — LLMs, speech-to-text, text-to-speech, NLP, embeddings, translation, and more.

This is a community resource. Contributions welcome via pull request.

**Last updated:** April 1, 2026

---

## Table of Contents

- [Large Language Models (LLMs)](#large-language-models-llms)
- [Speech-to-Text / ASR](#speech-to-text--asr)
- [Text-to-Speech (TTS)](#text-to-speech-tts)
- [NLP Models](#nlp-models)
- [Embeddings](#embeddings)
- [Translation](#translation)
- [Summarization](#summarization)
- [OCR / Vision](#ocr--vision)
- [Speech Foundation Models](#speech-foundation-models)
- [Notable Projects & Resources](#notable-projects--resources)
- [Key Organizations](#key-organizations)

---

## Large Language Models (LLMs)

### dicta-il (Israel Center for Text Analysis)

| Model | Size | Type | Description |
|-------|------|------|-------------|
| [DictaLM-3.0-24B-Base](https://huggingface.co/dicta-il/DictaLM-3.0-24B-Base) | 24B | Base | Latest generation Hebrew LLM, large variant |
| [DictaLM-3.0-24B-Thinking](https://huggingface.co/dicta-il/DictaLM-3.0-24B-Thinking) | 24B | Reasoning | Thinking/reasoning variant |
| [DictaLM-3.0-Nemotron-12B-Base](https://huggingface.co/dicta-il/DictaLM-3.0-Nemotron-12B-Base) | 12B | Base | Nemotron-based Hebrew LLM |
| [DictaLM-3.0-Nemotron-12B-Instruct](https://huggingface.co/dicta-il/DictaLM-3.0-Nemotron-12B-Instruct) | 12B | Instruct | Instruction-tuned Nemotron |
| [DictaLM-3.0-1.7B-Base](https://huggingface.co/dicta-il/DictaLM-3.0-1.7B-Base) | 1.7B | Base | Compact Hebrew LLM |
| [DictaLM-3.0-1.7B-Instruct](https://huggingface.co/dicta-il/DictaLM-3.0-1.7B-Instruct) | 1.7B | Instruct | Instruction-tuned compact model |
| [DictaLM-3.0-1.7B-Thinking](https://huggingface.co/dicta-il/DictaLM-3.0-1.7B-Thinking) | 1.7B | Reasoning | Thinking variant of compact model |
| [dictalm2.0](https://huggingface.co/dicta-il/dictalm2.0) | 7B | Base | Previous-gen Hebrew LLM (Mistral-based) |
| [dictalm2.0-instruct](https://huggingface.co/dicta-il/dictalm2.0-instruct) | 7B | Instruct | Instruction-tuned DictaLM 2.0 |
| [BEREL_3.0](https://huggingface.co/dicta-il/BEREL_3.0) | — | Base | Biblical/Rabbinic Hebrew language model |
| [BEREL](https://huggingface.co/dicta-il/BEREL) | — | Base | BERT for Early/Rabbinic Hebrew |

### yam-peleg

| Model | Size | Type | Description |
|-------|------|------|-------------|
| [Hebrew-Gemma-11B-V2](https://huggingface.co/yam-peleg/Hebrew-Gemma-11B-V2) | 11B | Chat | Hebrew-adapted Gemma, v2 |
| [Hebrew-Gemma-11B-Instruct](https://huggingface.co/yam-peleg/Hebrew-Gemma-11B-Instruct) | 11B | Instruct | Instruction-tuned Hebrew Gemma |
| [Hebrew-Gemma-11B](https://huggingface.co/yam-peleg/Hebrew-Gemma-11B) | 11B | Base | Base Hebrew Gemma |
| [Hebrew-Mistral-7B](https://huggingface.co/yam-peleg/Hebrew-Mistral-7B) | 7B | Base | Hebrew-adapted Mistral 7B |
| [Hebrew-Mistral-7B-200K](https://huggingface.co/yam-peleg/Hebrew-Mistral-7B-200K) | 7B | Base | Extended context (200K) Hebrew Mistral |

### Other Hebrew LLMs

| Model | Author | Size | Type | Description |
|-------|--------|------|------|-------------|
| [Hebrew_Nemo](https://huggingface.co/SicariusSicariiStuff/Hebrew_Nemo) | SicariusSicariiStuff | 12B | Instruct | Hebrew fine-tune of Mistral Nemo |
| [Hebrew-GPT](https://huggingface.co/XythicK/Hebrew-GPT) | XythicK | 1B | Instruct | Hebrew fine-tune of Llama 3.2 1B |
| [HebrewGPT-1B](https://huggingface.co/Slasky/HebrewGPT-1B) | Slasky | 1B | Base | Hebrew-native GPT trained from scratch |
| [HebrewGPT-296M](https://huggingface.co/Slasky/HebrewGPT-296M) | Slasky | 296M | Base | Smaller Hebrew-native GPT |
| [Hebrew-GPT2-345M-Stage](https://huggingface.co/Norod78/Hebrew-GPT2-345M-Stage) | Norod78 | 345M | Base | Hebrew GPT-2 |
| [hebrew-gpt_neo-small](https://huggingface.co/Norod78/hebrew-gpt_neo-small) | Norod78 | ~125M | Base | Hebrew GPT-Neo small |
| [Llama-3.2-3B-Hebrew-Master](https://huggingface.co/yonioz123/Llama-3.2-3B-Hebrew-Master) | yonioz123 | 3B | Chat | Hebrew fine-tune of Llama 3.2 |
| [hebrew-math-tutor-v1](https://huggingface.co/Intel/hebrew-math-tutor-v1) | Intel | 4B | Instruct | Hebrew math tutoring model |
| [Hebrew-Mistral-7B-Instruct-v0.1](https://huggingface.co/ronmasas/Hebrew-Mistral-7B-Instruct-v0.1) | ronmasas | 7B | Instruct | Hebrew instruction-tuned Mistral |
| [dictalm2.0-instruct-fine-tuned-alpaca-gpt4-hebrew](https://huggingface.co/ronigold/dictalm2.0-instruct-fine-tuned-alpaca-gpt4-hebrew) | ronigold | 7B | Instruct | DictaLM 2.0 fine-tuned on Alpaca GPT-4 Hebrew |
| [SmolLM-135M-FakyPedia-EngHeb](https://huggingface.co/Norod78/SmolLM-135M-FakyPedia-EngHeb) | Norod78 | 135M | Base | Bilingual English-Hebrew small LM |
| [gemma-3_4b_hebrew-lyrics-finetune](https://huggingface.co/Norod78/gemma-3_4b_hebrew-lyrics-finetune) | Norod78 | 4B | Fine-tune | Gemma 3 fine-tuned for Hebrew lyrics |

---

## Speech-to-Text / ASR

### ivrit-ai

The leading Hebrew ASR project. Community-driven.

| Model | Size | Type | Description |
|-------|------|------|-------------|
| [whisper-large-v3-turbo-ct2](https://huggingface.co/ivrit-ai/whisper-large-v3-turbo-ct2) | Large | CTranslate2 | Top Hebrew ASR model, CT2 optimized (22K+ downloads) |
| [whisper-large-v3](https://huggingface.co/ivrit-ai/whisper-large-v3) | Large-v3 | Fine-tuned | Hebrew fine-tuned Whisper large-v3 |
| [whisper-large-v3-turbo](https://huggingface.co/ivrit-ai/whisper-large-v3-turbo) | Large-v3 | Fine-tuned | Hebrew fine-tuned Whisper turbo |
| [whisper-large-v3-ct2](https://huggingface.co/ivrit-ai/whisper-large-v3-ct2) | Large-v3 | CTranslate2 | CT2 format of Hebrew Whisper |
| [whisper-v2-d4](https://huggingface.co/ivrit-ai/whisper-v2-d4) | Large-v2 | Fine-tuned | Earlier Hebrew Whisper fine-tune |
| [faster-whisper-v2-d4](https://huggingface.co/ivrit-ai/faster-whisper-v2-d4) | Large-v2 | Faster-Whisper | Faster-Whisper format |
| [pyannote-speaker-diarization-3.1](https://huggingface.co/ivrit-ai/pyannote-speaker-diarization-3.1) | — | Diarization | Hebrew speaker diarization |
| [pyannote-segmentation-3.0](https://huggingface.co/ivrit-ai/pyannote-segmentation-3.0) | — | Segmentation | Hebrew audio segmentation |

GitHub: [ivrit-ai/ivrit.ai](https://github.com/ivrit-ai/ivrit.ai) | [ivrit-ai/asr-training](https://github.com/ivrit-ai/asr-training)

### imvladikon

| Model | Size | Type | Description |
|-------|------|------|-------------|
| [wav2vec2-xls-r-300m-hebrew](https://huggingface.co/imvladikon/wav2vec2-xls-r-300m-hebrew) | 300M | ASR | Most downloaded Hebrew model (144K downloads) |
| [wav2vec2-large-xlsr-53-hebrew](https://huggingface.co/imvladikon/wav2vec2-large-xlsr-53-hebrew) | 300M | ASR | Hebrew fine-tuned XLSR-53 |
| [wav2vec2-xls-r-1b-hebrew](https://huggingface.co/imvladikon/wav2vec2-xls-r-1b-hebrew) | 1B | ASR | Hebrew fine-tuned XLS-R 1B |
| [wav2vec2-xls-r-300m-lm-hebrew](https://huggingface.co/imvladikon/wav2vec2-xls-r-300m-lm-hebrew) | 300M | ASR+LM | With language model decoding |
| [whisper-medium-he](https://huggingface.co/imvladikon/whisper-medium-he) | Medium | ASR | Hebrew Whisper medium |

### Other ASR

| Model | Author | Description |
|-------|--------|-------------|
| [whisper-heb-ipa](https://huggingface.co/thewh1teagle/whisper-heb-ipa) | thewh1teagle | Hebrew Whisper with IPA phoneme output |
| [WhiStress](https://huggingface.co/slprl/WhiStress) | slprl | Hebrew stress/prosody-aware ASR |

---

## Text-to-Speech (TTS)

An emerging area for Hebrew — no production-grade standalone model yet, but active research.

| Model / Project | Author | Description |
|-----------------|--------|-------------|
| [HebTTS](https://github.com/slp-rl/HebTTS) | slp-rl (Technion) | Diacritic-free Hebrew TTS research |
| [SIMS-Llama3.2-3B](https://huggingface.co/slprl/SIMS-Llama3.2-3B) | slprl | Speech-language model, 3B |
| [SIMS-7B](https://huggingface.co/slprl/SIMS-7B) | slprl | Larger speech-language model |
| [israwave](https://github.com/thewh1teagle/israwave) | thewh1teagle | Hebrew TTS project |
| [Zonos-Hebrew](https://huggingface.co/notmax123/Zonos-Hebrew) | notmax123 | Hebrew variant of Zonos TTS |
| [hebrewTTS-orpheus3b](https://huggingface.co/Trojanssafsdg/hebrewTTS-orpheus3b) | Trojanssafsdg | Hebrew Orpheus TTS 3B |
| [hebrew-orpheus-tts](https://huggingface.co/rotem1121/hebrew-orpheus-tts) | rotem1121 | Hebrew Orpheus TTS variant |
| [phonikud](https://huggingface.co/thewh1teagle/phonikud) | thewh1teagle | Hebrew diacritization/phonemization for TTS pipelines |
| [mms-tts-heb](https://huggingface.co/thewh1teagle/mms-tts-heb) | thewh1teagle | Hebrew MMS TTS |

---

## NLP Models

### BERT-based Foundation Models

| Model | Author | Description |
|-------|--------|-------------|
| [AlephBERT-base](https://huggingface.co/onlplab/alephbert-base) | onlplab (BIU) | Foundational Hebrew BERT (29.6K downloads) |
| [heBERT](https://huggingface.co/avichr/heBERT) | avichr | Hebrew BERT |
| [Legal-heBERT](https://huggingface.co/avichr/Legal-heBERT) | avichr | Hebrew BERT for legal domain |
| [DictaBERT](https://huggingface.co/dicta-il/dictabert) | dicta-il | Hebrew BERT from Dicta |
| [DictaBERT-large](https://huggingface.co/dicta-il/dictabert-large) | dicta-il | Large Hebrew BERT |
| [NeoDictaBERT](https://huggingface.co/dicta-il/neodictabert) | dicta-il | Next-gen DictaBERT |
| [NeoDictaBERT-bilingual](https://huggingface.co/dicta-il/neodictabert-bilingual) | dicta-il | Bilingual Hebrew-English BERT |
| [AlephBertGimmel-base](https://huggingface.co/dicta-il/alephbertgimmel-base) | dicta-il | Third-generation Hebrew BERT |
| [MsBERT](https://huggingface.co/dicta-il/MsBERT) | dicta-il | Hebrew BERT variant |
| [HeRo](https://huggingface.co/HeNLP/HeRo) | HeNLP | Hebrew RoBERTa |
| [LongHeRo](https://huggingface.co/HeNLP/LongHeRo) | HeNLP | Long-context Hebrew RoBERTa |

### Named Entity Recognition (NER)

| Model | Author | Description |
|-------|--------|-------------|
| [heBERT_NER](https://huggingface.co/avichr/heBERT_NER) | avichr | Hebrew NER (39K downloads) |
| [dictabert-large-ner](https://huggingface.co/dicta-il/dictabert-large-ner) | dicta-il | Large Hebrew NER |
| [dictabert-ner](https://huggingface.co/dicta-il/dictabert-ner) | dicta-il | Standard Hebrew NER |

### Sentiment Analysis

| Model | Author | Description |
|-------|--------|-------------|
| [heBERT_sentiment_analysis](https://huggingface.co/avichr/heBERT_sentiment_analysis) | avichr | Hebrew sentiment analysis |
| [dictabert-sentiment](https://huggingface.co/dicta-il/dictabert-sentiment) | dicta-il | Hebrew sentiment classifier |
| [hebEMO](https://huggingface.co/avichr/hebEMO_anger) | avichr | Hebrew emotion detection (8 emotions: anger, fear, joy, surprise, sadness, disgust, anticipation, trust) |

### Morphology & Parsing

| Model | Author | Description |
|-------|--------|-------------|
| [dictabert-morph](https://huggingface.co/dicta-il/dictabert-morph) | dicta-il | Hebrew morphological analysis |
| [dictabert-joint](https://huggingface.co/dicta-il/dictabert-joint) | dicta-il | Joint morphological analysis |
| [dictabert-large-parse](https://huggingface.co/dicta-il/dictabert-large-parse) | dicta-il | Hebrew syntactic parsing |
| [dictabert-parse](https://huggingface.co/dicta-il/dictabert-parse) | dicta-il | Standard Hebrew parser |
| [dictabert-seg](https://huggingface.co/dicta-il/dictabert-seg) | dicta-il | Hebrew word segmentation |
| [dictabert-lex](https://huggingface.co/dicta-il/dictabert-lex) | dicta-il | Hebrew lexical analysis |
| [dictabert-syntax](https://huggingface.co/dicta-il/dictabert-syntax) | dicta-il | Hebrew syntax analysis |

### Diacritization (Nikud)

| Model | Author | Description |
|-------|--------|-------------|
| [dictabert-large-char-menaked](https://huggingface.co/dicta-il/dictabert-large-char-menaked) | dicta-il | Hebrew diacritization / nikud restoration (4.5K downloads) |
| [dictabert-char](https://huggingface.co/dicta-il/dictabert-char) | dicta-il | Character-level Hebrew model |

### Other NLP

| Model | Author | Type | Description |
|-------|--------|------|-------------|
| [hebrew_punctuation](https://huggingface.co/verbit/hebrew_punctuation) | Verbit | Punctuation | Hebrew punctuation restoration |
| [dictabert-heq](https://huggingface.co/dicta-il/dictabert-heq) | dicta-il | QA | Hebrew extractive question answering |
| [hebert_parashoot](https://huggingface.co/imvladikon/hebert_parashoot) | imvladikon | QA | Hebrew reading comprehension |
| [hebrew-offensive-detection](https://huggingface.co/KevynKrancenblum/hebrew-offensive-detection) | KevynKrancenblum | Classification | Hebrew offensive language detection |
| [hebert-finetuned-hebrew-metaphor](https://huggingface.co/tdklab/hebert-finetuned-hebrew-metaphor) | tdklab | Classification | Hebrew metaphor detection |

---

## Embeddings

| Model | Author | Description |
|-------|--------|-------------|
| [neodictabert-bilingual-embed](https://huggingface.co/dicta-il/neodictabert-bilingual-embed) | dicta-il | Bilingual Hebrew-English embeddings |
| [sentence-transformers-alephbert](https://huggingface.co/imvladikon/sentence-transformers-alephbert) | imvladikon | Hebrew sentence embeddings (4.9K downloads) |
| [sentence_transformers_alephbertgimmel_small](https://huggingface.co/imvladikon/sentence_transformers_alephbertgimmel_small) | imvladikon | Smaller Hebrew sentence embeddings |

---

## Translation

| Model | Author | Direction | Description |
|-------|--------|-----------|-------------|
| [opus-mt-en-he](https://huggingface.co/Helsinki-NLP/opus-mt-en-he) | Helsinki-NLP | EN → HE | English to Hebrew translation |
| [opus-mt-tc-big-he-en](https://huggingface.co/Helsinki-NLP/opus-mt-tc-big-he-en) | Helsinki-NLP | HE → EN | Hebrew to English, large model |
| [english-hebrew-translation](https://huggingface.co/ashercn97/english-hebrew-translation) | ashercn97 | EN ↔ HE | T5-based English-Hebrew translation |

---

## Summarization

| Model | Author | Description |
|-------|--------|-------------|
| [het5_summarization](https://huggingface.co/imvladikon/het5_summarization) | imvladikon | Hebrew T5 for summarization |
| [het5_small_summarization](https://huggingface.co/imvladikon/het5_small_summarization) | imvladikon | Smaller Hebrew T5 summarization |
| [cross_summarization_he_en](https://huggingface.co/imvladikon/cross_summarization_he_en) | imvladikon | Cross-lingual Hebrew-English summarization |

---

## OCR / Vision

| Model | Author | Description |
|-------|--------|-------------|
| [testing-trOCR-hebrew-handwritten](https://huggingface.co/sivan22/testing-trOCR-hebrew-handwritten) | sivan22 | TrOCR for Hebrew handwritten text |
| [paleo-hebrew-mt5-post-ocr-processing](https://huggingface.co/mr3vial/paleo-hebrew-mt5-post-ocr-processing) | mr3vial | Post-OCR correction for paleo-Hebrew |
| [paleo-hebrew-qwen3-vl-lora-post-ocr-processing](https://huggingface.co/mr3vial/paleo-hebrew-qwen3-vl-lora-post-ocr-processing) | mr3vial | Vision-language post-OCR for paleo-Hebrew |

---

## Speech Foundation Models

| Model | Author | Description |
|-------|--------|-------------|
| [mhubert-base-25hz](https://huggingface.co/slprl/mhubert-base-25hz) | slprl (Technion) | mHuBERT speech features at 25Hz |
| [slam / slam_scaled / slam_large](https://huggingface.co/slprl/slam_scaled) | slprl | Speech-language alignment models |
| [StresSLM](https://huggingface.co/slprl/StresSLM) | slprl | Hebrew stress-aware speech-language model |
| [PAST](https://huggingface.co/slprl/PAST) | slprl | Prosody-aware speech model |

---

## Notable Projects & Resources

| Project | Description |
|---------|-------------|
| [NNLP-IL/Hebrew-Resources](https://github.com/NNLP-IL/Hebrew-Resources) | Comprehensive list of Hebrew NLP resources |
| [iddoberger/awesome-hebrew-nlp](https://github.com/iddoberger/awesome-hebrew-nlp) | Curated list of Hebrew NLP resources |
| [ivrit-ai/ivrit.ai](https://github.com/ivrit-ai/ivrit.ai) | Main ivrit.ai codebase for Hebrew ASR |
| [ivrit-ai/asr-training](https://github.com/ivrit-ai/asr-training) | ASR training recipes for Hebrew |
| [ivrit-ai/eliezer](https://github.com/ivrit-ai/eliezer) | ivrit.ai's Hebrew bot |
| [slp-rl/HebTTS](https://github.com/slp-rl/HebTTS) | Diacritic-free Hebrew TTS research |
| [thewh1teagle/israwave](https://github.com/thewh1teagle/israwave) | Hebrew TTS project |
| [HebrewNLP/HebrewNLP4J](https://github.com/HebrewNLP/HebrewNLP4J) | Java library for HebrewNLP API |

---

## Key Organizations

| Organization | Focus | Notes |
|-------------|-------|-------|
| [dicta-il](https://huggingface.co/dicta-il) | LLMs, BERT, NLP | Israel Center for Text Analysis. Most comprehensive Hebrew NLP toolkit |
| [ivrit-ai](https://huggingface.co/ivrit-ai) | ASR / STT | Leading Hebrew speech recognition project. Community-driven |
| [yam-peleg](https://huggingface.co/yam-peleg) | LLMs | Hebrew Gemma and Mistral adaptations |
| [avichr](https://huggingface.co/avichr) | NLP | heBERT family — widely used Hebrew NER and sentiment |
| [onlplab](https://huggingface.co/onlplab) | Foundation BERT | AlephBERT — foundational Hebrew BERT from Bar-Ilan University |
| [imvladikon](https://huggingface.co/imvladikon) | ASR, embeddings | wav2vec2 Hebrew (144K downloads), sentence transformers |
| [slprl](https://huggingface.co/slprl) | TTS, speech | Technion Speech Processing Lab |
| [HeNLP](https://huggingface.co/HeNLP) | Foundation models | HeRo (Hebrew RoBERTa) |
| [Helsinki-NLP](https://huggingface.co/Helsinki-NLP) | Translation | OPUS-MT Hebrew translation models |
| [Norod78](https://huggingface.co/Norod78) | Small LLMs | Hebrew GPT-2, GPT-Neo, creative fine-tunes |
| [Slasky](https://huggingface.co/Slasky) | LLMs | Hebrew-native GPTs trained from scratch |
| [thewh1teagle](https://huggingface.co/thewh1teagle) | TTS, phonemization | israwave TTS, phonikud diacritization |
| [Intel](https://huggingface.co/Intel) | Education LLMs | Hebrew math tutoring model |

---

## Contributing

Know of a Hebrew AI model not listed here? Open a pull request or file an issue.

## License

[![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This work is licensed under a Creative Commons Attribution 4.0 International License.
