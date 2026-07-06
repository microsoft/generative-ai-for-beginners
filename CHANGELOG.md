# Changelog

All notable changes to the Generative AI for Beginners curriculum are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Because this is a
learning curriculum rather than a versioned software package, entries are grouped by date.

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
