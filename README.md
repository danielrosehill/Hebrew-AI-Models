[![Master Index](https://img.shields.io/badge/Master_Index-GitHub-blue?style=for-the-badge&logo=github)](https://github.com/danielrosehill/Start-Here) [![Index of Indexes](https://img.shields.io/badge/Index_of_Indexes-Subindices-FF6B6B?style=for-the-badge&logo=github)](https://github.com/danielrosehill/Subindices) [![Hugging Face Space](https://img.shields.io/badge/Search_it-Hugging_Face_Space-FFD21E?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/danielrosehill/Hebrew-AI-Models)

# Hebrew AI Models

A catalog of AI models for the Hebrew language — LLMs, speech-to-text, text-to-speech, NLP, embeddings, translation, and more.

Part of the [Hebrew AI](https://github.com/danielrosehill/Hebrew-AI) index. Datasets are catalogued in [Hebrew-Datasets](https://github.com/danielrosehill/Hebrew-Datasets); people and organisations in [Hebrew-AI-Community](https://github.com/danielrosehill/Hebrew-AI-Community), benchmarks in [Hebrew-AI-Benchmarks](https://github.com/danielrosehill/Hebrew-AI-Benchmarks). Scope: [SCOPE.md](SCOPE.md).

This is a community resource. Contributions welcome via pull request.

**Last updated:** November 18, 2026

---

## Contents

- [Embeddings](#embeddings)
- [Large Language Models (LLMs)](#large-language-models-llms)
- [NLP Models](#nlp-models)
- [Notable Projects & Resources](#notable-projects--resources)
- [OCR / Vision](#ocr--vision)
- [Speech Foundation Models](#speech-foundation-models)
- [Speech-to-Text / ASR](#speech-to-text--asr)
- [Summarization](#summarization)
- [Text-to-Speech (TTS)](#text-to-speech-tts)
- [Translation](#translation)

---

## Embeddings

Sentence and text embedding models for Hebrew retrieval and similarity.

### neodictabert-bilingual-embed

Bilingual Hebrew-English embeddings.

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/neodictabert-bilingual-embed)

---

### sentence-transformers-alephbert

Hebrew sentence embeddings (4.9K downloads)

*Author: imvladikon*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/imvladikon/sentence-transformers-alephbert)

---

### sentence_transformers_alephbertgimmel_small

Smaller Hebrew sentence embeddings.

*Author: imvladikon*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/imvladikon/sentence_transformers_alephbertgimmel_small)

---

## Large Language Models (LLMs)

Hebrew-adapted and Hebrew-trained LLMs, base and instruction-tuned, with quantised builds.

### dicta-il (Israel Center for Text Analysis)

#### BEREL

BERT for Early/Rabbinic Hebrew.

*Type: Base*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/BEREL)

---

#### BEREL_3.0

Biblical/Rabbinic Hebrew language model.

*Type: Base*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/BEREL_3.0)

---

#### DictaLM-3.0-1.7B-Base

Compact Hebrew LLM.

*Size: 1.7B · Type: Base*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/DictaLM-3.0-1.7B-Base)

---

#### DictaLM-3.0-1.7B-Instruct

Instruction-tuned compact model.

*Size: 1.7B · Type: Instruct*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/DictaLM-3.0-1.7B-Instruct)

---

#### DictaLM-3.0-1.7B-Thinking

Thinking variant of compact model.

*Size: 1.7B · Type: Reasoning*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/DictaLM-3.0-1.7B-Thinking)

---

#### DictaLM-3.0-24B-Base

Latest generation Hebrew LLM, large variant.

*Size: 24B · Type: Base*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/DictaLM-3.0-24B-Base)

---

#### DictaLM-3.0-24B-Thinking

Thinking/reasoning variant.

*Size: 24B · Type: Reasoning*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/DictaLM-3.0-24B-Thinking)

---

#### DictaLM-3.0-Nemotron-12B-Base

Nemotron-based Hebrew LLM.

*Size: 12B · Type: Base*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/DictaLM-3.0-Nemotron-12B-Base)

---

#### DictaLM-3.0-Nemotron-12B-Instruct

Instruction-tuned Nemotron.

*Size: 12B · Type: Instruct*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/DictaLM-3.0-Nemotron-12B-Instruct)

---

#### dictalm2.0

Previous-gen Hebrew LLM (Mistral-based)

*Size: 7B · Type: Base*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/dictalm2.0)

---

#### dictalm2.0-instruct

Instruction-tuned DictaLM 2.0.

*Size: 7B · Type: Instruct*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/dictalm2.0-instruct)

### Other Hebrew LLMs

#### dictalm2.0-instruct-fine-tuned-alpaca-gpt4-hebrew

DictaLM 2.0 fine-tuned on Alpaca GPT-4 Hebrew.

*Author: ronigold · Size: 7B · Type: Instruct*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/ronigold/dictalm2.0-instruct-fine-tuned-alpaca-gpt4-hebrew)

---

#### gemma-3_4b_hebrew-lyrics-finetune

Gemma 3 fine-tuned for Hebrew lyrics.

*Author: Norod78 · Size: 4B · Type: Fine-tune*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/Norod78/gemma-3_4b_hebrew-lyrics-finetune)

---

#### Hebrew-GPT

Hebrew fine-tune of Llama 3.2 1B.

*Author: XythicK · Size: 1B · Type: Instruct*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/XythicK/Hebrew-GPT)

---

#### Hebrew-GPT2-345M-Stage

Hebrew GPT-2.

*Author: Norod78 · Size: 345M · Type: Base*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/Norod78/Hebrew-GPT2-345M-Stage)

---

#### hebrew-gpt_neo-small

Hebrew GPT-Neo small.

*Author: Norod78 · Size: ~125M · Type: Base*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/Norod78/hebrew-gpt_neo-small)

---

#### hebrew-math-tutor-v1

Hebrew math tutoring model.

*Author: Intel · Size: 4B · Type: Instruct*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/Intel/hebrew-math-tutor-v1)

---

#### Hebrew-Mistral-7B-Instruct-v0.1

Hebrew instruction-tuned Mistral.

*Author: ronmasas · Size: 7B · Type: Instruct*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/ronmasas/Hebrew-Mistral-7B-Instruct-v0.1)

---

#### hebrew_bible_ai

gpt2-xl fine-tuned on the Hebrew Bible; generates Bible-style verses.

*Author: tombenj · Type: Base*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/tombenj/hebrew_bible_ai)

---

#### Hebrew_Nemo

Hebrew fine-tune of Mistral Nemo.

*Author: SicariusSicariiStuff · Size: 12B · Type: Instruct*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/SicariusSicariiStuff/Hebrew_Nemo)

---

#### Hebrew_Nemo-i1-GGUF

imatrix GGUF quants of Hebrew_Nemo.

*Author: mradermacher · Size: 12B · Type: GGUF*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/mradermacher/Hebrew_Nemo-i1-GGUF)

---

#### HebrewGPT-1B

Hebrew-native GPT trained from scratch.

*Author: Slasky · Size: 1B · Type: Base*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/Slasky/HebrewGPT-1B)

---

#### HebrewGPT-296M

Smaller Hebrew-native GPT.

*Author: Slasky · Size: 296M · Type: Base*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/Slasky/HebrewGPT-296M)

---

#### Llama-3.2-3B-Hebrew-Master

Hebrew fine-tune of Llama 3.2.

*Author: yonioz123 · Size: 3B · Type: Chat*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/yonioz123/Llama-3.2-3B-Hebrew-Master)

---

#### Llama-3.2-3B-Instruct-Aya-Hebrew-Lora

Hebrew LoRA on Llama 3.2 3B Instruct (thin card)

*Author: itayl · Size: 3B · Type: LoRA*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/itayl/Llama-3.2-3B-Instruct-Aya-Hebrew-Lora)

---

#### Qwen2.5-1.5B-Instruct-bnb-4bit-Hebrew

Hebrew fine-tune of Qwen2.5 1.5B Instruct, 4-bit (thin card)

*Author: itayl · Size: 1.5B · Type: Instruct*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/itayl/Qwen2.5-1.5B-Instruct-bnb-4bit-Hebrew)

---

#### qwen2.5-3b_Hebrew

Hebrew fine-tune of Qwen2.5 3B (thin card)

*Author: itayl · Size: 3B · Type: Instruct*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/itayl/qwen2.5-3b_Hebrew)

---

#### qwen2.5-3b_Hebrew-Q5_K_M-GGUF

Q5_K_M GGUF of qwen2.5-3b_Hebrew.

*Author: itayl · Size: 3B · Type: GGUF*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/itayl/qwen2.5-3b_Hebrew-Q5_K_M-GGUF)

---

#### SmolLM-135M-FakyPedia-EngHeb

Bilingual English-Hebrew small LM.

*Author: Norod78 · Size: 135M · Type: Base*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/Norod78/SmolLM-135M-FakyPedia-EngHeb)

### yam-peleg

#### Hebrew-Gemma-11B

Base Hebrew Gemma.

*Size: 11B · Type: Base*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/yam-peleg/Hebrew-Gemma-11B)

---

#### Hebrew-Gemma-11B-i1-GGUF

imatrix GGUF quants of Hebrew-Gemma-11B (mradermacher)

*Size: 11B · Type: GGUF*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/mradermacher/Hebrew-Gemma-11B-i1-GGUF)

---

#### Hebrew-Gemma-11B-Instruct

Instruction-tuned Hebrew Gemma.

*Size: 11B · Type: Instruct*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/yam-peleg/Hebrew-Gemma-11B-Instruct)

---

#### Hebrew-Gemma-11B-V2

Hebrew-adapted Gemma, v2.

*Size: 11B · Type: Chat*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/yam-peleg/Hebrew-Gemma-11B-V2)

---

#### Hebrew-Mistral-7B

Hebrew-adapted Mistral 7B.

*Size: 7B · Type: Base*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/yam-peleg/Hebrew-Mistral-7B)

---

#### Hebrew-Mistral-7B-200K

Extended context (200K) Hebrew Mistral.

*Size: 7B · Type: Base*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/yam-peleg/Hebrew-Mistral-7B-200K)

---

#### Hebrew-Mistral-7B-GGUF

GGUF quants of Hebrew-Mistral-7B (mradermacher)

*Size: 7B · Type: GGUF*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/mradermacher/Hebrew-Mistral-7B-GGUF)

---

#### Hebrew-Mistral-7B-GGUF

GGUF quants of Hebrew-Mistral-7B (tensorblock)

*Size: 7B · Type: GGUF*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/tensorblock/Hebrew-Mistral-7B-GGUF)

---

#### Hebrew-Mistral-7B-Q4_K_M-GGUF

Q4_K_M GGUF of Hebrew-Mistral-7B.

*Size: 7B · Type: GGUF*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/rony-shtamler/Hebrew-Mistral-7B-Q4_K_M-GGUF)

---

#### Hebrew-Mixtral-8x22B

Mixtral 8x22B continued-pretrained on English and Hebrew.

*Size: 141B · Type: Base*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/yam-peleg/Hebrew-Mixtral-8x22B)

---

## NLP Models

Task models for Hebrew text: foundation encoders, NER, sentiment, morphology, nikud and more.

### BERT-based Foundation Models

#### AlephBERT-base

Foundational Hebrew BERT (29.6K downloads)

*Author: onlplab (BIU)*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/onlplab/alephbert-base)

---

#### AlephBertGimmel-base

Third-generation Hebrew BERT.

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/alephbertgimmel-base)

---

#### bert-mini-hebrew

Small Hebrew BERT.

*Author: yosefw*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/yosefw/bert-mini-hebrew)

---

#### DictaBERT

Hebrew BERT from Dicta.

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/dictabert)

---

#### DictaBERT-large

Large Hebrew BERT.

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/dictabert-large)

---

#### heBERT

Hebrew BERT.

*Author: avichr*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/avichr/heBERT)

---

#### HeRo

Hebrew RoBERTa.

*Author: HeNLP*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/HeNLP/HeRo)

---

#### Knesset-DictaBERT

DictaBERT fine-tuned on the Knesset corpus (parliamentary Hebrew)

*Author: GiliGold*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/GiliGold/Knesset-DictaBERT)

---

#### Legal-heBERT

Hebrew BERT for legal domain.

*Author: avichr*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/avichr/Legal-heBERT)

---

#### LongHeRo

Long-context Hebrew RoBERTa.

*Author: HeNLP*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/HeNLP/LongHeRo)

---

#### MsBERT

Hebrew BERT variant.

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/MsBERT)

---

#### NeoDictaBERT

Next-gen DictaBERT.

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/neodictabert)

---

#### NeoDictaBERT-bilingual

Bilingual Hebrew-English BERT.

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/neodictabert-bilingual)

### Diacritization (Nikud)

#### dictabert-char

Character-level Hebrew model.

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/dictabert-char)

---

#### dictabert-large-char-menaked

Hebrew diacritization / nikud restoration (4.5K downloads)

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/dictabert-large-char-menaked)

### Morphology & Parsing

#### dictabert-joint

Joint morphological analysis.

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/dictabert-joint)

---

#### dictabert-large-parse

Hebrew syntactic parsing.

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/dictabert-large-parse)

---

#### dictabert-lex

Hebrew lexical analysis.

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/dictabert-lex)

---

#### dictabert-morph

Hebrew morphological analysis.

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/dictabert-morph)

---

#### dictabert-parse

Standard Hebrew parser.

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/dictabert-parse)

---

#### dictabert-seg

Hebrew word segmentation.

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/dictabert-seg)

---

#### dictabert-syntax

Hebrew syntax analysis.

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/dictabert-syntax)

### Named Entity Recognition (NER)

#### dictabert-large-ner

Large Hebrew NER.

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/dictabert-large-ner)

---

#### dictabert-ner

Standard Hebrew NER.

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/dictabert-ner)

---

#### heBERT_NER

Hebrew NER (39K downloads)

*Author: avichr*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/avichr/heBERT_NER)

### Other NLP

#### dictabert-heq

Hebrew extractive question answering.

*Author: dicta-il · Type: QA*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/dictabert-heq)

---

#### hebert-finetuned-hebrew-metaphor

Hebrew metaphor detection.

*Author: tdklab · Type: Classification*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/tdklab/hebert-finetuned-hebrew-metaphor)

---

#### hebert_parashoot

Hebrew reading comprehension.

*Author: imvladikon · Type: QA*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/imvladikon/hebert_parashoot)

---

#### hebrew-intent-classifier

BERT intent classifier for Hebrew customer-service text (4 classes)

*Author: humy65 · Type: Classification*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/humy65/hebrew-intent-classifier)

---

#### hebrew-latin-token-classifier

Finds Hebrew words written in Latin letters; moved to Hebrish/Hebrew-Latin-Token-Classifier.

*Author: danielrosehill · Type: Token classification*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/danielrosehill/hebrew-latin-token-classifier)

---

#### hebrew-offensive-detection

Hebrew offensive language detection.

*Author: KevynKrancenblum · Type: Classification*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/KevynKrancenblum/hebrew-offensive-detection)

---

#### hebrew_punctuation

Hebrew punctuation restoration.

*Author: Verbit · Type: Punctuation*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/verbit/hebrew_punctuation)

---

#### punctuation-restoration-deberta-alepgbert-hebrew

Hebrew punctuation restoration (no model card)

*Author: baravninaor · Type: Punctuation*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/baravninaor/punctuation-restoration-deberta-alepgbert-hebrew)

### Sentiment Analysis

#### dictabert-sentiment

Hebrew sentiment classifier.

*Author: dicta-il*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dicta-il/dictabert-sentiment)

---

#### hebEMO

Hebrew emotion detection (8 emotions: anger, fear, joy, surprise, sadness, disgust, anticipation, trust)

*Author: avichr*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/avichr/hebEMO_anger)

---

#### heBERT_sentiment_analysis

Hebrew sentiment analysis.

*Author: avichr*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/avichr/heBERT_sentiment_analysis)

---

#### xlm-r_hebrew_sentiment

XLM-R fine-tuned for Hebrew sentiment (accuracy 0.92)

*Author: DGurgurov*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/DGurgurov/xlm-r_hebrew_sentiment)

---

## Notable Projects & Resources

Code, lists and projects around Hebrew AI that aren't models themselves.

### AvrahamRaviv/Deep-Learning-in-Hebrew

Deep learning educational resources in Hebrew.

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/AvrahamRaviv/Deep-Learning-in-Hebrew)

---

### danielrosehill/Hebrew-Datasets

Companion list: Hebrew audio, sentence and text datasets.

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/danielrosehill/Hebrew-Datasets)

---

### danielrosehill/Hebrew-Image-Generation-Eval

Evaluation of image generation models for Hebrew text.

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/danielrosehill/Hebrew-Image-Generation-Eval)

---

### danielrosehill/Hebrew-LLMs

Resource list of Hebrew large language models.

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/danielrosehill/Hebrew-LLMs)

---

### danielrosehill/Hebrew-TTS-Providers

Directory of Hebrew TTS providers and services.

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/danielrosehill/Hebrew-TTS-Providers)

---

### HebrewNLP/HebrewNLP4J

Java library for HebrewNLP API.

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/HebrewNLP/HebrewNLP4J)

---

### iddoberger/awesome-hebrew-nlp

Curated list of Hebrew NLP resources.

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/iddoberger/awesome-hebrew-nlp)

---

### ivrit-ai/asr-training

ASR training recipes for Hebrew.

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/ivrit-ai/asr-training)

---

### ivrit-ai/eliezer

ivrit.ai's Hebrew bot.

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/ivrit-ai/eliezer)

---

### ivrit-ai/ivrit.ai

Main ivrit.ai codebase for Hebrew ASR.

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/ivrit-ai/ivrit.ai)

---

### NNLP-IL/Hebrew-Resources

Comprehensive list of Hebrew NLP resources.

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/NNLP-IL/Hebrew-Resources)

---

### ShmuelRonen/hebrew_whisper

Hebrew Whisper ASR project.

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/ShmuelRonen/hebrew_whisper)

---

### slp-rl/HebTTS

Diacritic-free Hebrew TTS research.

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/slp-rl/HebTTS)

---

### thewh1teagle/israwave

Hebrew TTS project.

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/thewh1teagle/israwave)

---

## OCR / Vision

Models that read printed or handwritten Hebrew from images.

### hebrew-Hand-Writen

Hebrew handwriting image-to-text (no model card)

*Author: makies*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/makies/hebrew-Hand-Writen)

---

### paleo-hebrew-mt5-post-ocr-processing

Post-OCR correction for paleo-Hebrew.

*Author: mr3vial*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/mr3vial/paleo-hebrew-mt5-post-ocr-processing)

---

### paleo-hebrew-qwen3-vl-lora-post-ocr-processing

Vision-language post-OCR for paleo-Hebrew.

*Author: mr3vial*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/mr3vial/paleo-hebrew-qwen3-vl-lora-post-ocr-processing)

---

### testing-trOCR-hebrew-handwritten

TrOCR for Hebrew handwritten text.

*Author: sivan22*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/sivan22/testing-trOCR-hebrew-handwritten)

---

## Speech Foundation Models

Speech encoders and speech-language models used as a base for Hebrew speech work.

### mhubert-base-25hz

mHuBERT speech features at 25Hz.

*Author: slprl (Hebrew University)*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/slprl/mhubert-base-25hz)

---

### PAST

Prosody-aware speech model.

*Author: slprl*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/slprl/PAST)

---

### slam / slam_scaled / slam_large

Speech-language alignment models.

*Author: slprl*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/slprl/slam_scaled)

---

### StresSLM

Hebrew stress-aware speech-language model.

*Author: slprl*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/slprl/StresSLM)

---

## Speech-to-Text / ASR

Hebrew speech recognition models, including English-Hebrew code-switching.

### Hebrish (English-Hebrew code-switching)

Maintainer's own ASR models for English speech with Hebrew words mixed in.

#### Jachnun-GGUF

GGUF of Jachnun (Parakeet TDT 0.6B code-switching); superseded by Sabich-Rolling per its card (gated)

*Author: Hebrish*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/Hebrish/Jachnun-GGUF)

---

#### Jachnun-ONNX

ONNX of Jachnun; superseded by Sabich-Rolling per its card (gated)

*Author: Hebrish*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/Hebrish/Jachnun-ONNX)

---

#### Jachnun-sherpa-onnx-int8

sherpa-onnx int8 of Jachnun; superseded by Sabich-Rolling per its card (gated)

*Author: Hebrish*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/Hebrish/Jachnun-sherpa-onnx-int8)

---

#### Whisper-Hebrish

Whisper large-v3-turbo fine-tuned on English-Hebrew code-switching sentences (POC)

*Author: danielrosehill*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/danielrosehill/Whisper-Hebrish)

---

#### Whisper-Hebrish-Small-ACFT

Whisper small.en ACFT build for code-switching (gated)

*Author: Hebrish*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/Hebrish/Whisper-Hebrish-Small-ACFT)

### imvladikon

#### wav2vec2-large-xlsr-53-hebrew

Hebrew fine-tuned XLSR-53.

*Size: 300M · Type: ASR*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/imvladikon/wav2vec2-large-xlsr-53-hebrew)

---

#### wav2vec2-xls-r-1b-hebrew

Hebrew fine-tuned XLS-R 1B.

*Size: 1B · Type: ASR*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/imvladikon/wav2vec2-xls-r-1b-hebrew)

---

#### wav2vec2-xls-r-300m-hebrew

Most downloaded Hebrew model (144K downloads)

*Size: 300M · Type: ASR*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/imvladikon/wav2vec2-xls-r-300m-hebrew)

---

#### wav2vec2-xls-r-300m-lm-hebrew

With language model decoding.

*Size: 300M · Type: ASR+LM*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/imvladikon/wav2vec2-xls-r-300m-lm-hebrew)

---

#### whisper-medium-he

Hebrew Whisper medium.

*Size: Medium · Type: ASR*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/imvladikon/whisper-medium-he)

### ivrit-ai

The leading Hebrew ASR project. Community-driven.
GitHub: [ivrit-ai/ivrit.ai](https://github.com/ivrit-ai/ivrit.ai) | [ivrit-ai/asr-training](https://github.com/ivrit-ai/asr-training)

#### faster-whisper-v2-d4

Faster-Whisper format.

*Size: Large-v2 · Type: Faster-Whisper*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/ivrit-ai/faster-whisper-v2-d4)

---

#### pyannote-segmentation-3.0

Hebrew audio segmentation.

*Type: Segmentation*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/ivrit-ai/pyannote-segmentation-3.0)

---

#### pyannote-speaker-diarization-3.1

Hebrew speaker diarization.

*Type: Diarization*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/ivrit-ai/pyannote-speaker-diarization-3.1)

---

#### whisper-large-v3

Hebrew fine-tuned Whisper large-v3.

*Size: Large-v3 · Type: Fine-tuned*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/ivrit-ai/whisper-large-v3)

---

#### whisper-large-v3-ct2

CT2 format of Hebrew Whisper.

*Size: Large-v3 · Type: CTranslate2*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/ivrit-ai/whisper-large-v3-ct2)

---

#### whisper-large-v3-turbo

Hebrew fine-tuned Whisper turbo.

*Size: Large-v3 · Type: Fine-tuned*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/ivrit-ai/whisper-large-v3-turbo)

---

#### whisper-large-v3-turbo-ct2

Top Hebrew ASR model, CT2 optimized (22K+ downloads)

*Size: Large · Type: CTranslate2*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/ivrit-ai/whisper-large-v3-turbo-ct2)

---

#### whisper-v2-d4

Earlier Hebrew Whisper fine-tune.

*Size: Large-v2 · Type: Fine-tuned*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/ivrit-ai/whisper-v2-d4)

### Other ASR

#### embeddinggemma-2-asr-hebrew-english-streaming

Streaming Hebrew + English ASR on the EmbeddingGemma 2 audio encoder, 351M.

*Author: MaorB*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/MaorB/embeddinggemma-2-asr-hebrew-english-streaming)

---

#### fast-hebrew-asr

GigaAM-He: 220M CTC Hebrew ASR built for real-time calls; faster but less accurate than ivrit.ai turbo.

*Author: asfberlin*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/asfberlin/fast-hebrew-asr)

---

#### hebrew_whisper

Hebrew Whisper ASR project.

*Author: ShmuelRonen*

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/ShmuelRonen/hebrew_whisper)

---

#### nemotron-3.5-asr-streaming-0.6b-hebrew

Nemotron 3.5 ASR streaming 0.6B fine-tuned on ivrit.ai data.

*Author: mralexivy*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/mralexivy/nemotron-3.5-asr-streaming-0.6b-hebrew)

---

#### qwen3-asr-hebrew

Qwen3-ASR Hebrew (no model card)

*Author: guychuk*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/guychuk/qwen3-asr-hebrew)

---

#### wav2vec2-large-xls-r-300m-hebrew-colab

wav2vec2 XLS-R 300M Hebrew fine-tune (no model card)

*Author: Mizurodp*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/Mizurodp/wav2vec2-large-xls-r-300m-hebrew-colab)

---

#### whisper-heb-ipa

Hebrew Whisper with IPA phoneme output.

*Author: thewh1teagle*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/thewh1teagle/whisper-heb-ipa)

---

#### whisper-large-v3-hebrew

Whisper large-v3 fine-tuned for Hebrew.

*Author: adarcook*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/adarcook/whisper-large-v3-hebrew)

---

#### WhiStress

Hebrew stress/prosody-aware ASR.

*Author: slprl*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/slprl/WhiStress)

---

## Summarization

Models that summarise Hebrew text.

### cross_summarization_he_en

Cross-lingual Hebrew-English summarization.

*Author: imvladikon*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/imvladikon/cross_summarization_he_en)

---

### hebrew-summarization-llm

DictaLM 2.0 fine-tuned for Hebrew summarization; author says not evaluated.

*Author: maayanorner*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/maayanorner/hebrew-summarization-llm)

---

### het5_small_summarization

Smaller Hebrew T5 summarization.

*Author: imvladikon*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/imvladikon/het5_small_summarization)

---

### het5_summarization

Hebrew T5 for summarization.

*Author: imvladikon*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/imvladikon/het5_summarization)

---

## Text-to-Speech (TTS)

An emerging area for Hebrew — no production-grade standalone model yet, but active research.

### f5tts-hebrew-v2

F5-TTS fine-tuned on ~158h of Hebrew speech, 58 built-in voices.

*Author: Yzamari*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/Yzamari/f5tts-hebrew-v2)

---

### hebrew-orpheus-tts

Hebrew Orpheus TTS variant.

*Author: rotem1121*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/rotem1121/hebrew-orpheus-tts)

---

### hebrewTTS-orpheus3b

Hebrew Orpheus TTS 3B.

*Author: Trojanssafsdg*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/Trojanssafsdg/hebrewTTS-orpheus3b)

---

### HebTTS

Diacritic-free Hebrew TTS research.

*Author: slp-rl (Hebrew University)*

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/slp-rl/HebTTS)

---

### israwave

Hebrew TTS project.

*Author: thewh1teagle*

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/thewh1teagle/israwave)

---

### kokoro-hebrew-nc

Kokoro Hebrew ONNX export, non-commercial licence (from avris/kokoro-hebrew-saspeech)

*Author: thewh1teagle*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/thewh1teagle/kokoro-hebrew-nc)

---

### mms-tts-heb

Hebrew MMS TTS.

*Author: thewh1teagle*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/thewh1teagle/mms-tts-heb)

---

### MOSS-TTS-Realtime-Hebrew

Hebrew MOSS-TTS Realtime (no model card)

*Author: dm15*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/dm15/MOSS-TTS-Realtime-Hebrew)

---

### phonikud

Hebrew diacritization/phonemization for TTS pipelines.

*Author: thewh1teagle*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/thewh1teagle/phonikud)

---

### SIMS-7B

Larger speech-language model.

*Author: slprl*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/slprl/SIMS-7B)

---

### SIMS-Llama3.2-3B

Speech-language model, 3B.

*Author: slprl*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/slprl/SIMS-Llama3.2-3B)

---

### Zonos-Hebrew

Hebrew variant of Zonos TTS.

*Author: notmax123*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/notmax123/Zonos-Hebrew)

---

## Translation

Models translating between Hebrew and other languages.

### english-hebrew

t5-small fine-tuned on opus100 en-he.

*Author: SoyGema · Direction: EN-HE*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/SoyGema/english-hebrew)

---

### english-hebrew-translation

T5-based English-Hebrew translation.

*Author: ashercn97 · Direction: EN ↔ HE*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/ashercn97/english-hebrew-translation)

---

### opus-mt-en-he

English to Hebrew translation.

*Author: Helsinki-NLP · Direction: EN → HE*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/Helsinki-NLP/opus-mt-en-he)

---

### opus-mt-tc-big-he-en

Hebrew to English, large model.

*Author: Helsinki-NLP · Direction: HE → EN*

[![Model](https://img.shields.io/badge/Hugging_Face-Model-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/Helsinki-NLP/opus-mt-tc-big-he-en)

---

## Curated HF Collections

Curated Hugging Face collections (by danielrosehill) grouping Hebrew models, datasets and spaces:

<!-- collections:start -->
<!-- Generated from collections.json by scripts/render_collections.py; edit that file, not these cards. -->

### Code Switching (English And Hebrew) - All Resources

English-Hebrew code-switching models and datasets.

[![Collection](https://img.shields.io/badge/Hugging_Face-Collection-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/collections/danielrosehill/code-switching-english-and-hebrew-all-resources-6acfdcb1e11911797af4c3b3)

---

### Hebrew

General Hebrew collection: models and datasets across tasks.

[![Collection](https://img.shields.io/badge/Hugging_Face-Collection-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/collections/danielrosehill/hebrew-6ad68f42575d0b5073d19e86)

---

### Hebrew AI Spaces

Hugging Face Spaces for Hebrew AI (spaces are listed, not imported).

[![Collection](https://img.shields.io/badge/Hugging_Face-Collection-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/collections/danielrosehill/hebrew-ai-spaces-68042a7ab079f5df1cdf9264)

---

### Hebrew ASR (And Audio To Text)

Hebrew ASR and audio-to-text models.

[![Collection](https://img.shields.io/badge/Hugging_Face-Collection-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/collections/danielrosehill/hebrew-asr-and-audio-to-text-69cbb72271b4fe75732a465a)

---

### Hebrew LLMs + Text Prediction

Hebrew LLMs and text prediction models.

[![Collection](https://img.shields.io/badge/Hugging_Face-Collection-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/collections/danielrosehill/hebrew-llms-text-prediction-675f3e982858d6e9652e7bac)

---

### Hebrew TTS

Hebrew text-to-speech models.

[![Collection](https://img.shields.io/badge/Hugging_Face-Collection-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/collections/danielrosehill/hebrew-tts-69cbb6f343675b83becaeae1)

---

### Parakeet V2 - English-Hebrew Codeswitching Finetune

Parakeet TDT 0.6B v2 English-Hebrew code-switching fine-tunes.

[![Collection](https://img.shields.io/badge/Hugging_Face-Collection-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/collections/danielrosehill/parakeet-v2-english-hebrew-codeswitching-finetune-6ad26d79c70d28a49ed71c78)

---

All collections: [https://huggingface.co/danielrosehill/collections](https://huggingface.co/danielrosehill/collections)
<!-- collections:end -->

---

## How this list is maintained

Models are swept from Hugging Face with saved searches ([`hfsearches.json`](hfsearches.json)): the Hebrew language tag plus a task (text generation, ASR, TTS and others), sorted by trending or downloads, plus name searches for "heb". Each sweep keeps a dated raw snapshot in [`snapshots/`](snapshots/) and every model gets a recorded verdict in [`data/verdicts.json`](data/verdicts.json).

Most models tagged Hebrew on the Hub are multilingual models that list Hebrew among many languages. They are not Hebrew models, so this list keeps them apart: **Hebrew specialist** models (trained or fine-tuned for Hebrew) fill the main sections, and notable multilingual models with Hebrew support go in a separate *Multilingual models with Hebrew support* subsection. Criteria: [`docs/classification.md`](docs/classification.md).

## Contributing

Maintained on a best-effort basis by [Daniel Rosehill](https://github.com/danielrosehill). To be included, or to send a correction, open a pull request or email public@danielrosehill.com.

## License

[![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This work is licensed under a Creative Commons Attribution 4.0 International License.
