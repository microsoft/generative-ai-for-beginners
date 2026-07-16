# Changelog

All notable changes to the Generative AI for Beginners curriculum are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Because this is a
learning curriculum rather than a versioned software package, entries are grouped by date.

## [2026-07-16] — Content Validation + Lesson 09 Image Assets

### Changed

- **Lesson 10 (low-code AI apps):** updated two retired `docs.microsoft.com/powerapps/...` Dataverse
  links to the current `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (verified live).
- **Lesson 17 (AI agents):** modernized a dated model example (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) and a placeholder deployment name in the Agent Framework sample
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Root `README.md`:** added the missing `?WT.mc_id=academic-105485-koreyst` tracking ID to the
  *Microsoft for Startups* link.
- **Lesson 09 image assets** regenerated with the `gpt-image` model: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, and
  `images/startup.png` (the editing example's before/after pair was produced via a real
  `client.images.edit` call with a generated mask).

### Validated

- Audited the READMEs for lessons 01, 03, 05, 12, 14, and 16 — all current (correct Microsoft Foundry
  naming and links); no changes required.
- Ran a full markdown validation across all 41 in-repo markdown files (translations excluded) for
  deprecated doc paths, `/en-us/` Microsoft locales, outdated product/model names, missing tracking
  IDs, and broken relative links/images. Only the single *Microsoft for Startups* tracking-ID gap was
  actionable; all other flags were confirmed false positives (auto-generated translation links,
  commented-out placeholders, and third-party `/en/` structural URLs).

## [2026-07-15] — Lesson 09 (Image Applications) Rewrite for GPT Image Models

### Changed

- **Rewrote lesson 09 "Building Image Generation Applications"** around the current **`gpt-image`**
  model family (default **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` also GA), replacing the
  legacy DALL·E 2/3 content. Key corrections:
  - `gpt-image` models return the image as **base64 (`b64_json`)**, not a URL. Updated all samples to
    `base64.b64decode(...)` instead of downloading a `url` with `requests`.
  - Bumped the image API version to `2025-04-01-preview`.
  - Replaced the fabricated "temperature" section (image models don't take `temperature`) and the
    DALL·E-2-only image **variations** content with an **image editing** (mask/inpainting) section.
  - Updated `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, both
    assignment notebooks (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), and the .NET `.dib` notebook.

### Removed

- Deleted the obsolete `python/aoai-app-variation.py` and `python/oai-app-variation.py` samples
  (`images.create_variation` is DALL·E-2-only and unsupported by `gpt-image`).
- Deleted 4 orphaned image assets tied to the removed temperature-comparison section
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Dropped the unnecessary `requests` dependency from the lesson's Python samples and requirements.

### Validated

- Ran `aoai-app.py` end-to-end against a deployed `gpt-image-1.5` model and confirmed the base64
  decode/save flow produces a PNG. Notebooks confirmed to be valid JSON.

## [2026-07-14] — Default Model Update + Reasoning-Model Guidance

### Changed

- **Default chat model `gpt-4o-mini` → `gpt-5-mini`** across the curriculum's runnable samples,
  docs, and configuration. This was driven by model lifecycle status: on Microsoft Foundry,
  `gpt-4o-mini` (retires 2026-10-01) and the entire `gpt-4.1` family (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, retire 2026-10-14) are **Deprecating**, whereas the **GPT-5 family
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) is Generally Available** (retires 2027-02-06). Updated:
  - `.env.copy`, `00-course-setup/03-providers.md` (recommended deployment and `az cognitiveservices`
    deploy commands), and the READMEs for lessons 04, 06, 07, and 15.
  - Python samples in lesson 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) and lesson 08 scripts.
  - TypeScript / JavaScript samples in lessons 06, 07, and 11, and the `.dib` .NET notebooks for
    lessons 06 and 07.
  - Assignment notebooks in lessons 04, 06, 07, and 11 (code cells), plus `shared/python/api_utils.py`
    docstring examples.
- **Reasoning-model parameter guidance (new).** `gpt-5-mini` is a *reasoning* model: it does **not**
  support `temperature`/`top_p`, and uses `max_completion_tokens` (chat completions) /
  `max_output_tokens` (Responses API) instead of `max_tokens`. Accordingly:
  - Removed `temperature`/`top_p`/`max_tokens` from samples that now default to `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, lesson 15 RAG README).
  - Added a **"Reasoning models don't use `temperature`"** note to lesson 06, explaining that
    reasoning models are steered with **prompt engineering + reasoning controls** rather than
    sampling knobs, while `temperature`/`top_p` remain valid on non-reasoning models
    (GPT-4.x, Mistral, Llama, Phi, open models).
- **`gpt-5-mini` is not used for the fine-tuning tutorial (lesson 18).** GPT-5 only supports
  reinforcement fine-tuning (RFT); the lesson 18 supervised fine-tuning (SFT) walkthrough keeps
  `gpt-4.1-mini`, which supports SFT/DPO.
- **Temperature demos use a Llama model.** To keep teaching `temperature` (which reasoning models
  reject), a `Llama-3.3-70B-Instruct` model is used via the Foundry Models endpoint. Added a new
  `AZURE_INFERENCE_CHAT_MODEL` variable to `.env.copy`; the lesson 04/06 `githubmodels` notebooks and
  the `06` `js-githubmodels` sample read it (falling back to `Llama-3.3-70B-Instruct`) and keep their
  `temperature`/`top_p`/`max_tokens` demos.
- **JS / .NET samples updated for GPT-5.** Removed `temperature`/`top_p`/`max_tokens` from the GPT-5
  samples (`06` `recipe-app` TypeScript, `06` `.dib` .NET - which also raises `MaxOutputTokenCount`
  so reasoning output isn't truncated). The `06` `js-githubmodels` sample now uses Llama to keep its
  temperature demo. The `.dib` notes that `Azure.AI.Inference` + a Llama model is the way to
  demonstrate `Temperature` in .NET.
- Left `gpt-4o-mini` / `gpt-5-mini` in place where they remain accurate: `tiktoken` token-encoding
  references, model-catalog availability lists, and lesson 02 speech models (`gpt-4o-transcribe`).
- The lesson 20 (Mistral) and 21 (Meta) samples keep `temperature`/`max_tokens` because they target
  Mistral/Llama models, which support those parameters.

## [2026-07-06] — Content Modernization Refresh

A broad refresh to keep the curriculum accurate for 2026: modern APIs, current product names and
model names, updated provider guidance, and new developer-experience tooling.

### Added

- **Microsoft Agent Framework** section in lesson `17-ai-agents` covering single chat agents,
  tools/function calling, Azure OpenAI (Microsoft Foundry) configuration, and multi-agent
  workflow orchestration (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** documented as an offline / on-device provider (alongside Ollama) in
  `00-course-setup/03-providers.md` and lesson `19-slm`.
- **Continuous integration workflows**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (enforced on the maintained `shared/`
    module, advisory across the rest of the curriculum), an advisory ESLint pass, and a pytest job.
  - `.github/workflows/security.yml` — CodeQL analysis (Python + JavaScript/TypeScript) and
    dependency review on pull requests.
- **Test suite** under `tests/` — 41 pytest tests covering the shared utility module.
- **Azure OpenAI → Responses API migration skill** under
  `.github/skills/azure-openai-to-responses/` used to guide the API migration.

### Changed

- **Chat Completions API → Responses API** across all Python and TypeScript chat samples
  (`client.responses.create(...)` → `response.output_text`), including lessons 04, 06, 07, 11,
  15, and 18, plus their READMEs.
- **GitHub Models → Microsoft Foundry Models** throughout prose, links, and samples. GitHub Models
  retires at the end of July 2026; samples now point to the Microsoft Foundry model catalog and use
  the `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL` environment variables.
- **`.env.copy`, `AGENTS.md`, and provider docs** updated to reflect that Azure OpenAI is now part
  of Microsoft Foundry, and the default API version bumped to `2024-10-21`.
- **TypeScript samples** (lessons 06, 07, 08, 11) migrated off the deprecated `@azure/openai`
  beta SDK to the `openai` package (chat apps use the Responses API; the search app uses the
  embeddings client).
- **.NET notebooks** (`dotnet/*.dib`) standardized on `Azure.AI.OpenAI` **2.1.0**: lessons 06 and 07
  use the `ChatClient` API, lesson 08 uses `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), and
  lesson 09 uses `ImageClient` (`GenerateImage`) with `gpt-image-1`, replacing the legacy
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` from `1.0.0-beta.9`.
- **Product-name modernization**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lessons 14, 16, 17) and "Bing" → **Microsoft Copilot** (lesson 12), where those referred to the
  current products.
- **DevContainer** (`.devcontainer/`) now ships Pylance, Black, Ruff, ESLint, Prettier, and Copilot
  extensions, enables format-on-save, and installs `ruff`, `black`, `mypy`, and `pytest` so the CI
  checks can be reproduced locally.
- **Image generation** (lesson 09) recommends `gpt-image-1` for Azure (the Azure catalog dropped
  `dall-e-3`).

- **`docs/ENHANCED_FEATURES_ROADMAP.md`** updated to reflect completed work (API migration, CI,
  DevContainer, tests) and current facts (translations are produced automatically by the
  Azure Co-op Translator; the Assistants API is superseded by the Responses API).

### Fixed

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` now returns an
  empty string for whitespace-only input instead of raising a "too short" error (consistent with the
  `None` case). Found and covered by the new test suite.
- **Lesson 09 image samples** — corrected real bugs: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  and a variable that shadowed the `openai` module.
- **Lesson 15 RAG notebook** — repaired the client setup, replaced the removed `DataFrame.append`
  with `pd.concat`, and modernized the legacy SDK usage.
- Deprecated / retired model names (`gpt-3.5-turbo`, `gpt-35-turbo`) replaced with `gpt-4o-mini`
  in active samples; historical fine-tuning outputs in lesson 18 were preserved and annotated
  rather than rewritten.

### Deprecated / Notes

- **Microsoft Foundry Models samples** that use the `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — the `githubmodels-*` and `js-githubmodels` samples and lessons 19, 20,
  and 21 — remain on the Model Inference API, which does **not** support the Responses API. These are
  intentionally left on that SDK.
- `AzureOpenAI()` is intentionally retained where still appropriate (embeddings and image generation),
  as those workflows are not part of the Responses API migration.
- `text-embedding-ada-002` references are kept where a precomputed embedding index depends on them.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->