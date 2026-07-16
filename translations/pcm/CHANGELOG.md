# Changelog

All di important changes wey happen for di Generative AI for Beginners curriculum dey documented for dis file.

Di format base on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Becos na learning curriculum e be, no be versioned software package, di entries group by date.


## [2026-07-16] — Content Validation + Lesson 09 Image Assets

### Changed

- **Lesson 10 (low-code AI apps):** updated two retired `docs.microsoft.com/powerapps/...` Dataverse
  links to di current `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (verified live).
- **Lesson 17 (AI agents):** modernize one old model example (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) and change one placeholder deployment name for di Agent Framework sample
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Root `README.md`:** add the missing `?WT.mc_id=academic-105485-koreyst` tracking ID to di
  *Microsoft for Startups* link.
- **Lesson 09 image assets** regenerate with di `gpt-image` model: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, and
  `images/startup.png` (di editing example before/after pair na real
  `client.images.edit` call with one generated mask).

### Validated

- Check di READMEs for lessons 01, 03, 05, 12, 14, and 16 — all correct (Microsoft Foundry
  naming and links); no changes needed.
- Do one full markdown validation for all 41 in-repo markdown files (translation no count) to check
  deprecated doc paths, `/en-us/` Microsoft locales, old product/model names, missing tracking
  IDs, and broken relative links/images. Only one *Microsoft for Startups* tracking-ID gap show
  e be real; all other worries be false alarms (auto-generated translation links,
  commented-out placeholders, and third-party `/en/` structural URLs).

## [2026-07-15] — Lesson 09 (Image Applications) Rewrite for GPT Image Models

### Changed

- **Rewrite lesson 09 "Building Image Generation Applications"** around di current **`gpt-image`**
  model family (default **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` also GA), replace di
  old DALL·E 2/3 content. Important corrections:
  - `gpt-image` models dey return image as **base64 (`b64_json`)**, no be URL. Update all samples to
    use `base64.b64decode(...)` insteadof download `url` with `requests`.
  - Upgrade di image API version to `2025-04-01-preview`.
  - Remove di fake "temperature" section (image models no dey use `temperature`) and di
    DALL·E-2-only image **variations** content; replace am with **image editing** (mask/inpainting) section.
  - Update `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, both
    assignment notebooks (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), and di .NET `.dib` notebook.

### Removed

- Delete di old `python/aoai-app-variation.py` and `python/oai-app-variation.py` samples
  (`images.create_variation` na DALL·E-2-only and no support for `gpt-image`).
- Remove 4 orphaned image assets wey relate to di removed temperature-comparison section
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Drop di unneeded `requests` dependency from di lesson's Python samples and requirements.

### Validated

- Run `aoai-app.py` end-to-end against one deployed `gpt-image-1.5` model and confirm say di base64
  decode/save flow fit produce PNG. Notebooks confirm be valid JSON.

## [2026-07-14] — Default Model Update + Reasoning-Model Guidance

### Changed

- **Default chat model `gpt-4o-mini` → `gpt-5-mini`** for di whole curriculum runnable samples,
  docs, and config. Dis one na because model lifecycle status: for Microsoft Foundry,
  `gpt-4o-mini` (go retire 2026-10-01) and di entire `gpt-4.1` family (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, retire 2026-10-14) dey **Deprecating**, but di **GPT-5 family
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) dey Generally Available** (go retire 2027-02-06). Update:
  - `.env.copy`, `00-course-setup/03-providers.md` (recommended deployment and `az cognitiveservices`
    deploy commands), and di READMEs for lessons 04, 06, 07, and 15.
  - Python samples for lesson 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) and lesson 08 scripts.
  - TypeScript / JavaScript samples for lessons 06, 07, and 11, and di `.dib` .NET notebooks for
    lessons 06 and 07.
  - Assignment notebooks for lessons 04, 06, 07, and 11 (code cells), plus `shared/python/api_utils.py`
    docstring examples.
- **Reasoning-model parameter guidance (new).** `gpt-5-mini` na *reasoning* model: e no dey
  support `temperature`/`top_p`, e dey use `max_completion_tokens` (chat completions) /
  `max_output_tokens` (Responses API) instead of `max_tokens`. So:
  - Remove `temperature`/`top_p`/`max_tokens` from samples wey now default to `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, lesson 15 RAG README).
  - Add one **"Reasoning models no dey use `temperature`"** note to lesson 06, to explain say
    reasoning models dem dey controlled with **prompt engineering + reasoning controls** no be
    sampling knobs, but `temperature`/`top_p` still valid for non-reasoning models
    (GPT-4.x, Mistral, Llama, Phi, open models).
- **`gpt-5-mini` no dey use for fine-tuning tutorial (lesson 18).** GPT-5 only support
  reinforcement fine-tuning (RFT); di lesson 18 supervised fine-tuning (SFT) walkthrough still use
  `gpt-4.1-mini`, wey support SFT/DPO.
- **Temperature demos dey use Llama model.** To keep teach `temperature` (wey reasoning models
  no accept), dem use `Llama-3.3-70B-Instruct` model via di Foundry Models endpoint. Add new
  `AZURE_INFERENCE_CHAT_MODEL` variable to `.env.copy`; di lesson 04/06 `githubmodels` notebooks and
  di `06` `js-githubmodels` sample read am (fall back to `Llama-3.3-70B-Instruct`) and keep their
  `temperature`/`top_p`/`max_tokens` demos.
- **JS / .NET samples update for GPT-5.** Remove `temperature`/`top_p`/`max_tokens` from GPT-5
  samples (`06` `recipe-app` TypeScript, `06` `.dib` .NET - which also raise `MaxOutputTokenCount`
  so reasoning output no go cut off). Di `06` `js-githubmodels` sample now use Llama to keep
  im temperature demo. Di `.dib` show say `Azure.AI.Inference` + Llama model na correct way to
  demonstrate `Temperature` for .NET.
- Leave `gpt-4o-mini` / `gpt-5-mini` where dem still dey accurate: `tiktoken` token-encoding
  references, model-catalog lists, and lesson 02 speech models (`gpt-4o-transcribe`).
- Di lesson 20 (Mistral) and 21 (Meta) samples still keep `temperature`/`max_tokens` because dem target
  Mistral/Llama models, wey support those parameters.

## [2026-07-06] — Content Modernization Refresh

Big refresh to keep di curriculum correct for 2026: modern APIs, current product names and
model names, updated provider guidance, and new developer-experience tools.

### Added

- **Microsoft Agent Framework** section for lesson `17-ai-agents` wey cover single chat agents,
  tools/function calling, Azure OpenAI (Microsoft Foundry) config, and multi-agent
  workflow orchestration (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** document am as offline / on-device provider (side by side with Ollama) for
  `00-course-setup/03-providers.md` and lesson `19-slm`.
- **Continuous integration workflows**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (enforced on di maintained `shared/`
    module, advisory across di rest of di curriculum), advisory ESLint run, and pytest job.
  - `.github/workflows/security.yml` — CodeQL analysis (Python + JavaScript/TypeScript) and
    dependency review on pull requests.
- **Test suite** for `tests/` — 41 pytest tests wey cover shared utility module.
- **Azure OpenAI → Responses API migration skill** for
  `.github/skills/azure-openai-to-responses/` wey guide API migration.

### Changed

- **Chat Completions API → Responses API** for all Python and TypeScript chat samples
  (`client.responses.create(...)` → `response.output_text`), including lessons 04, 06, 07, 11,
  15, and 18, plus dia READMEs.
- **GitHub Models → Microsoft Foundry Models** inside prose, links, and samples. GitHub Models
  dey retire end of July 2026; samples now dey use Microsoft Foundry model catalog and use
  di `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL` environment variables.
- **`.env.copy`, `AGENTS.md`, and provider docs** update say Azure OpenAI na part of
  Microsoft Foundry, and the default API version upgrade to `2024-10-21`.
- **TypeScript samples** (lessons 06, 07, 08, 11) migrate off di old `@azure/openai`
  beta SDK to di `openai` package (chat apps dey use Responses API; search app dey use
  embeddings client).
- **.NET notebooks** (`dotnet/*.dib`) standardize on `Azure.AI.OpenAI` **2.1.0**: lessons 06 and 07
  use `ChatClient` API, lesson 08 use `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), and
  lesson 09 use `ImageClient` (`GenerateImage`) with `gpt-image-1`, to replace old
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` from `1.0.0-beta.9`.
- **Product-name modernization**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lessons 14, 16, 17) and "Bing" → **Microsoft Copilot** (lesson 12), for where dem mean
  current products.
- **DevContainer** (`.devcontainer/`) now come with Pylance, Black, Ruff, ESLint, Prettier, and Copilot
  extensions, enable format-on-save, and install `ruff`, `black`, `mypy`, and `pytest` so CI
  checks fit run locally.
- **Image generation** (lesson 09) recommend `gpt-image-1` for Azure (di Azure catalog drop
  `dall-e-3`).

- **`docs/ENHANCED_FEATURES_ROADMAP.md`** don update to show di work wey don finish (API migration, CI,
  DevContainer, tests) and wetin dey true now (translations dey automatically produced by di
  Azure Co-op Translator; di Assistants API don replace by di Responses API).

### Fix

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` now dey return
  empty string if input na only whitespace instead make e throw "too short" error (dis one
  consistent with di `None` case). E show for new test wey dem do.
- **Lesson 09 image samples** — true bugs don fix: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  plus one variable wey shadow di `openai` module.
- **Lesson 15 RAG notebook** — fix client setup, comot di old `DataFrame.append`
  put `pd.concat`, plus update di old SDK waka.
- Deprecated / retire model names (`gpt-3.5-turbo`, `gpt-35-turbo`) don change to `gpt-4o-mini`
  for active samples; historical fine-tuning output for lesson 18 still dey and e get note
  instead of rewrite am.

### Deprecated / Notes

- **Microsoft Foundry Models samples** wey use `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — di `githubmodels-*` and `js-githubmodels` samples plus lessons 19, 20,
  and 21 — still dey use Model Inference API, wey no dey support Responses API. Dem purposely
  leave am for dat SDK.
- `AzureOpenAI()` still dey for where e still make sense (embeddings and image generation),
  as those workflow no be part of Responses API migration.
- Reference to `text-embedding-ada-002` still dey where precomputed embedding index need am.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->