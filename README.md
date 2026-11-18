[![Master Index](https://img.shields.io/badge/Master_Index-GitHub-blue?style=for-the-badge&logo=github)](https://github.com/danielrosehill/Start-Here)

# Hebrew AI Models

A catalog of AI models for the Hebrew language — LLMs, speech-to-text, text-to-speech, NLP, embeddings, translation, and more.

Part of the [Hebrew AI](https://github.com/danielrosehill/Hebrew-AI) index. Datasets are catalogued in [Hebrew-Datasets](https://github.com/danielrosehill/Hebrew-Datasets); people and organisations in [Hebrew-AI-Community](https://github.com/danielrosehill/Hebrew-AI-Community). Scope: [SCOPE.md](SCOPE.md).

This is a community resource. Contributions welcome via pull request.

**Last updated:** November 18, 2026

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
- [Curated HF Collections](#curated-hf-collections)
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
| [Hebrew-Gemma-11B-i1-GGUF](https://huggingface.co/mradermacher/Hebrew-Gemma-11B-i1-GGUF) | 11B | GGUF | imatrix GGUF quants of Hebrew-Gemma-11B (mradermacher) |
| [Hebrew-Mistral-7B](https://huggingface.co/yam-peleg/Hebrew-Mistral-7B) | 7B | Base | Hebrew-adapted Mistral 7B |
| [Hebrew-Mistral-7B-GGUF](https://huggingface.co/mradermacher/Hebrew-Mistral-7B-GGUF) | 7B | GGUF | GGUF quants of Hebrew-Mistral-7B (mradermacher) |
| [Hebrew-Mistral-7B-GGUF](https://huggingface.co/tensorblock/Hebrew-Mistral-7B-GGUF) | 7B | GGUF | GGUF quants of Hebrew-Mistral-7B (tensorblock) |
| [Hebrew-Mistral-7B-Q4_K_M-GGUF](https://huggingface.co/rony-shtamler/Hebrew-Mistral-7B-Q4_K_M-GGUF) | 7B | GGUF | Q4_K_M GGUF of Hebrew-Mistral-7B |
| [Hebrew-Mistral-7B-200K](https://huggingface.co/yam-peleg/Hebrew-Mistral-7B-200K) | 7B | Base | Extended context (200K) Hebrew Mistral |
| [Hebrew-Mixtral-8x22B](https://huggingface.co/yam-peleg/Hebrew-Mixtral-8x22B) | 141B | Base | Mixtral 8x22B continued-pretrained on English and Hebrew |

### Other Hebrew LLMs

| Model | Author | Size | Type | Description |
|-------|--------|------|------|-------------|
| [Hebrew_Nemo](https://huggingface.co/SicariusSicariiStuff/Hebrew_Nemo) | SicariusSicariiStuff | 12B | Instruct | Hebrew fine-tune of Mistral Nemo |
| [Hebrew_Nemo-i1-GGUF](https://huggingface.co/mradermacher/Hebrew_Nemo-i1-GGUF) | mradermacher | 12B | GGUF | imatrix GGUF quants of Hebrew_Nemo |
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
| [qwen2.5-3b_Hebrew](https://huggingface.co/itayl/qwen2.5-3b_Hebrew) | itayl | 3B | Instruct | Hebrew fine-tune of Qwen2.5 3B (thin card) |
| [qwen2.5-3b_Hebrew-Q5_K_M-GGUF](https://huggingface.co/itayl/qwen2.5-3b_Hebrew-Q5_K_M-GGUF) | itayl | 3B | GGUF | Q5_K_M GGUF of qwen2.5-3b_Hebrew |
| [Qwen2.5-1.5B-Instruct-bnb-4bit-Hebrew](https://huggingface.co/itayl/Qwen2.5-1.5B-Instruct-bnb-4bit-Hebrew) | itayl | 1.5B | Instruct | Hebrew fine-tune of Qwen2.5 1.5B Instruct, 4-bit (thin card) |
| [Llama-3.2-3B-Instruct-Aya-Hebrew-Lora](https://huggingface.co/itayl/Llama-3.2-3B-Instruct-Aya-Hebrew-Lora) | itayl | 3B | LoRA | Hebrew LoRA on Llama 3.2 3B Instruct (thin card) |
| [hebrew_bible_ai](https://huggingface.co/tombenj/hebrew_bible_ai) | tombenj | — | Base | gpt2-xl fine-tuned on the Hebrew Bible; generates Bible-style verses |

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
| [hebrew_whisper](https://github.com/ShmuelRonen/hebrew_whisper) | ShmuelRonen | Hebrew Whisper ASR project |
| [nemotron-3.5-asr-streaming-0.6b-hebrew](https://huggingface.co/mralexivy/nemotron-3.5-asr-streaming-0.6b-hebrew) | mralexivy | Nemotron 3.5 ASR streaming 0.6B fine-tuned on ivrit.ai data |
| [embeddinggemma-2-asr-hebrew-english-streaming](https://huggingface.co/MaorB/embeddinggemma-2-asr-hebrew-english-streaming) | MaorB | Streaming Hebrew + English ASR on the EmbeddingGemma 2 audio encoder, 351M |
| [fast-hebrew-asr](https://huggingface.co/asfberlin/fast-hebrew-asr) | asfberlin | GigaAM-He: 220M CTC Hebrew ASR built for real-time calls; faster but less accurate than ivrit.ai turbo |
| [whisper-large-v3-hebrew](https://huggingface.co/adarcook/whisper-large-v3-hebrew) | adarcook | Whisper large-v3 fine-tuned for Hebrew |
| [wav2vec2-large-xls-r-300m-hebrew-colab](https://huggingface.co/Mizurodp/wav2vec2-large-xls-r-300m-hebrew-colab) | Mizurodp | wav2vec2 XLS-R 300M Hebrew fine-tune (no model card) |
| [qwen3-asr-hebrew](https://huggingface.co/guychuk/qwen3-asr-hebrew) | guychuk | Qwen3-ASR Hebrew (no model card) |

### Hebrish (English-Hebrew code-switching)

Maintainer's own ASR models for English speech with Hebrew words mixed in.

| Model | Author | Description |
|-------|--------|-------------|
| [Whisper-Hebrish](https://huggingface.co/danielrosehill/Whisper-Hebrish) | danielrosehill | Whisper large-v3-turbo fine-tuned on English-Hebrew code-switching sentences (POC) |
| [Whisper-Hebrish-Small-ACFT](https://huggingface.co/Hebrish/Whisper-Hebrish-Small-ACFT) | Hebrish | Whisper small.en ACFT build for code-switching (gated) |
| [Jachnun-GGUF](https://huggingface.co/Hebrish/Jachnun-GGUF) | Hebrish | GGUF of Jachnun (Parakeet TDT 0.6B code-switching); superseded by Sabich-Rolling per its card (gated) |
| [Jachnun-ONNX](https://huggingface.co/Hebrish/Jachnun-ONNX) | Hebrish | ONNX of Jachnun; superseded by Sabich-Rolling per its card (gated) |
| [Jachnun-sherpa-onnx-int8](https://huggingface.co/Hebrish/Jachnun-sherpa-onnx-int8) | Hebrish | sherpa-onnx int8 of Jachnun; superseded by Sabich-Rolling per its card (gated) |

---

## Text-to-Speech (TTS)

An emerging area for Hebrew — no production-grade standalone model yet, but active research.

| Model / Project | Author | Description |
|-----------------|--------|-------------|
| [HebTTS](https://github.com/slp-rl/HebTTS) | slp-rl (Hebrew University) | Diacritic-free Hebrew TTS research |
| [SIMS-Llama3.2-3B](https://huggingface.co/slprl/SIMS-Llama3.2-3B) | slprl | Speech-language model, 3B |
| [SIMS-7B](https://huggingface.co/slprl/SIMS-7B) | slprl | Larger speech-language model |
| [israwave](https://github.com/thewh1teagle/israwave) | thewh1teagle | Hebrew TTS project |
| [Zonos-Hebrew](https://huggingface.co/notmax123/Zonos-Hebrew) | notmax123 | Hebrew variant of Zonos TTS |
| [hebrewTTS-orpheus3b](https://huggingface.co/Trojanssafsdg/hebrewTTS-orpheus3b) | Trojanssafsdg | Hebrew Orpheus TTS 3B |
| [hebrew-orpheus-tts](https://huggingface.co/rotem1121/hebrew-orpheus-tts) | rotem1121 | Hebrew Orpheus TTS variant |
| [phonikud](https://huggingface.co/thewh1teagle/phonikud) | thewh1teagle | Hebrew diacritization/phonemization for TTS pipelines |
| [mms-tts-heb](https://huggingface.co/thewh1teagle/mms-tts-heb) | thewh1teagle | Hebrew MMS TTS |
| [f5tts-hebrew-v2](https://huggingface.co/Yzamari/f5tts-hebrew-v2) | Yzamari | F5-TTS fine-tuned on ~158h of Hebrew speech, 58 built-in voices |
| [kokoro-hebrew-nc](https://huggingface.co/thewh1teagle/kokoro-hebrew-nc) | thewh1teagle | Kokoro Hebrew ONNX export, non-commercial licence (from avris/kokoro-hebrew-saspeech) |
| [MOSS-TTS-Realtime-Hebrew](https://huggingface.co/dm15/MOSS-TTS-Realtime-Hebrew) | dm15 | Hebrew MOSS-TTS Realtime (no model card) |

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
| [Knesset-DictaBERT](https://huggingface.co/GiliGold/Knesset-DictaBERT) | GiliGold | DictaBERT fine-tuned on the Knesset corpus (parliamentary Hebrew) |
| [bert-mini-hebrew](https://huggingface.co/yosefw/bert-mini-hebrew) | yosefw | Small Hebrew BERT |
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
| [xlm-r_hebrew_sentiment](https://huggingface.co/DGurgurov/xlm-r_hebrew_sentiment) | DGurgurov | XLM-R fine-tuned for Hebrew sentiment (accuracy 0.92) |
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
| [hebrew-intent-classifier](https://huggingface.co/humy65/hebrew-intent-classifier) | humy65 | Classification | BERT intent classifier for Hebrew customer-service text (4 classes) |
| [hebrew-latin-token-classifier](https://huggingface.co/danielrosehill/hebrew-latin-token-classifier) | danielrosehill | Token classification | Finds Hebrew words written in Latin letters; moved to Hebrish/Hebrew-Latin-Token-Classifier |
| [punctuation-restoration-deberta-alepgbert-hebrew](https://huggingface.co/baravninaor/punctuation-restoration-deberta-alepgbert-hebrew) | baravninaor | Punctuation | Hebrew punctuation restoration (no model card) |

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
| [english-hebrew](https://huggingface.co/SoyGema/english-hebrew) | SoyGema | EN-HE | t5-small fine-tuned on opus100 en-he |

---

## Summarization

| Model | Author | Description |
|-------|--------|-------------|
| [het5_summarization](https://huggingface.co/imvladikon/het5_summarization) | imvladikon | Hebrew T5 for summarization |
| [het5_small_summarization](https://huggingface.co/imvladikon/het5_small_summarization) | imvladikon | Smaller Hebrew T5 summarization |
| [cross_summarization_he_en](https://huggingface.co/imvladikon/cross_summarization_he_en) | imvladikon | Cross-lingual Hebrew-English summarization |
| [hebrew-summarization-llm](https://huggingface.co/maayanorner/hebrew-summarization-llm) | maayanorner | DictaLM 2.0 fine-tuned for Hebrew summarization; author says not evaluated |

---

## OCR / Vision

| Model | Author | Description |
|-------|--------|-------------|
| [testing-trOCR-hebrew-handwritten](https://huggingface.co/sivan22/testing-trOCR-hebrew-handwritten) | sivan22 | TrOCR for Hebrew handwritten text |
| [paleo-hebrew-mt5-post-ocr-processing](https://huggingface.co/mr3vial/paleo-hebrew-mt5-post-ocr-processing) | mr3vial | Post-OCR correction for paleo-Hebrew |
| [paleo-hebrew-qwen3-vl-lora-post-ocr-processing](https://huggingface.co/mr3vial/paleo-hebrew-qwen3-vl-lora-post-ocr-processing) | mr3vial | Vision-language post-OCR for paleo-Hebrew |
| [hebrew-Hand-Writen](https://huggingface.co/makies/hebrew-Hand-Writen) | makies | Hebrew handwriting image-to-text (no model card) |

---

## Speech Foundation Models

| Model | Author | Description |
|-------|--------|-------------|
| [mhubert-base-25hz](https://huggingface.co/slprl/mhubert-base-25hz) | slprl (Hebrew University) | mHuBERT speech features at 25Hz |
| [slam / slam_scaled / slam_large](https://huggingface.co/slprl/slam_scaled) | slprl | Speech-language alignment models |
| [StresSLM](https://huggingface.co/slprl/StresSLM) | slprl | Hebrew stress-aware speech-language model |
| [PAST](https://huggingface.co/slprl/PAST) | slprl | Prosody-aware speech model |

---

## Curated HF Collections

Curated Hugging Face collections (by danielrosehill) grouping Hebrew models, datasets and spaces:

<!-- collections:start -->
<!-- Generated from collections.json by scripts/render_collections.py; edit that file, not this table. -->
| Collection | Contents |
|------------|----------|
| [Hebrew ASR (And Audio To Text)](https://huggingface.co/collections/danielrosehill/hebrew-asr-and-audio-to-text-69cbb72271b4fe75732a465a) | Hebrew ASR and audio-to-text models |
| [Hebrew TTS](https://huggingface.co/collections/danielrosehill/hebrew-tts-69cbb6f343675b83becaeae1) | Hebrew text-to-speech models |
| [Hebrew LLMs + Text Prediction](https://huggingface.co/collections/danielrosehill/hebrew-llms-text-prediction-675f3e982858d6e9652e7bac) | Hebrew LLMs and text prediction models |
| [Hebrew](https://huggingface.co/collections/danielrosehill/hebrew-6ad68f42575d0b5073d19e86) | General Hebrew collection: models and datasets across tasks |
| [Code Switching (English And Hebrew) - All Resources](https://huggingface.co/collections/danielrosehill/code-switching-english-and-hebrew-all-resources-6acfdcb1e11911797af4c3b3) | English-Hebrew code-switching models and datasets |
| [Parakeet V2 - English-Hebrew Codeswitching Finetune](https://huggingface.co/collections/danielrosehill/parakeet-v2-english-hebrew-codeswitching-finetune-6ad26d79c70d28a49ed71c78) | Parakeet TDT 0.6B v2 English-Hebrew code-switching fine-tunes |
| [Hebrew AI Spaces](https://huggingface.co/collections/danielrosehill/hebrew-ai-spaces-68042a7ab079f5df1cdf9264) | Hugging Face Spaces for Hebrew AI (spaces are listed, not imported) |

All collections: [https://huggingface.co/danielrosehill/collections](https://huggingface.co/danielrosehill/collections)
<!-- collections:end -->

---

## Notable Projects & Resources

| Project | Description |
|---------|-------------|
| [danielrosehill/Hebrew-Datasets](https://github.com/danielrosehill/Hebrew-Datasets) | Companion list: Hebrew audio, sentence and text datasets |
| [NNLP-IL/Hebrew-Resources](https://github.com/NNLP-IL/Hebrew-Resources) | Comprehensive list of Hebrew NLP resources |
| [iddoberger/awesome-hebrew-nlp](https://github.com/iddoberger/awesome-hebrew-nlp) | Curated list of Hebrew NLP resources |
| [ivrit-ai/ivrit.ai](https://github.com/ivrit-ai/ivrit.ai) | Main ivrit.ai codebase for Hebrew ASR |
| [ivrit-ai/asr-training](https://github.com/ivrit-ai/asr-training) | ASR training recipes for Hebrew |
| [ivrit-ai/eliezer](https://github.com/ivrit-ai/eliezer) | ivrit.ai's Hebrew bot |
| [slp-rl/HebTTS](https://github.com/slp-rl/HebTTS) | Diacritic-free Hebrew TTS research |
| [thewh1teagle/israwave](https://github.com/thewh1teagle/israwave) | Hebrew TTS project |
| [HebrewNLP/HebrewNLP4J](https://github.com/HebrewNLP/HebrewNLP4J) | Java library for HebrewNLP API |
| [danielrosehill/Hebrew-TTS-Providers](https://github.com/danielrosehill/Hebrew-TTS-Providers) | Directory of Hebrew TTS providers and services |
| [danielrosehill/Hebrew-Image-Generation-Eval](https://github.com/danielrosehill/Hebrew-Image-Generation-Eval) | Evaluation of image generation models for Hebrew text |
| [danielrosehill/Hebrew-LLMs](https://github.com/danielrosehill/Hebrew-LLMs) | Resource list of Hebrew large language models |
| [AvrahamRaviv/Deep-Learning-in-Hebrew](https://github.com/AvrahamRaviv/Deep-Learning-in-Hebrew) | Deep learning educational resources in Hebrew |
| [ShmuelRonen/hebrew_whisper](https://github.com/ShmuelRonen/hebrew_whisper) | Hebrew Whisper ASR project |

---

## Key Organizations

| Organization | Focus | Notes |
|-------------|-------|-------|
| [dicta-il](https://huggingface.co/dicta-il) | LLMs, BERT, NLP | Israel Center for Text Analysis. Most comprehensive Hebrew NLP toolkit |
| [ivrit-ai](https://huggingface.co/ivrit-ai) | ASR / STT | Leading Hebrew speech recognition project. Community-driven. Website: [ivrit.ai](https://www.ivrit.ai/) |
| [yam-peleg](https://huggingface.co/yam-peleg) | LLMs | Hebrew Gemma and Mistral adaptations |
| [avichr](https://huggingface.co/avichr) | NLP | heBERT family — widely used Hebrew NER and sentiment |
| [onlplab](https://huggingface.co/onlplab) | Foundation BERT | AlephBERT — foundational Hebrew BERT from Bar-Ilan University |
| [imvladikon](https://huggingface.co/imvladikon) | ASR, embeddings | wav2vec2 Hebrew (144K downloads), sentence transformers |
| [slprl](https://huggingface.co/slprl) | TTS, speech | SLP-RL, Hebrew University speech and language processing lab |
| [HeNLP](https://huggingface.co/HeNLP) | Foundation models | HeRo (Hebrew RoBERTa) |
| [Helsinki-NLP](https://huggingface.co/Helsinki-NLP) | Translation | OPUS-MT Hebrew translation models |
| [Norod78](https://huggingface.co/Norod78) | Small LLMs | Hebrew GPT-2, GPT-Neo, creative fine-tunes |
| [Slasky](https://huggingface.co/Slasky) | LLMs | Hebrew-native GPTs trained from scratch |
| [thewh1teagle](https://huggingface.co/thewh1teagle) | TTS, phonemization | israwave TTS, phonikud diacritization |
| [Intel](https://huggingface.co/Intel) | Education LLMs | Hebrew math tutoring model |

---

## How this list is maintained

Models are swept from Hugging Face with saved searches ([`hfsearches.json`](hfsearches.json)): the Hebrew language tag plus a task (text generation, ASR, TTS and others), sorted by trending or downloads, plus name searches for "heb". Each sweep keeps a dated raw snapshot in [`snapshots/`](snapshots/) and every model gets a recorded verdict in [`data/verdicts.json`](data/verdicts.json).

Most models tagged Hebrew on the Hub are multilingual models that list Hebrew among many languages. They are not Hebrew models, so this list keeps them apart: **Hebrew specialist** models (trained or fine-tuned for Hebrew) fill the main tables, and notable multilingual models with Hebrew support go in a separate *Multilingual models with Hebrew support* subsection. Criteria: [`docs/classification.md`](docs/classification.md).

## Contributing

Maintained on a best-effort basis by [Daniel Rosehill](https://github.com/danielrosehill). To be included, or to send a correction, open a pull request or email public@danielrosehill.com.

## License

[![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This work is licensed under a Creative Commons Attribution 4.0 International License.
