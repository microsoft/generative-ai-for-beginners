# Ändringslogg

Alla anmärkningsvärda ändringar i Generative AI for Beginners-kursplanen dokumenteras i denna fil.

Formatet baseras på [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Eftersom detta är en
läroplan snarare än ett versionerat mjukvarupaket, grupperas poster efter datum.

## [2026-07-06] — Uppdatering av innehåll för modernisering

En bred uppdatering för att hålla kursplanen korrekt för 2026: moderna API:er, aktuella produktnamn och
modellnamn, uppdaterade leverantörsriktlinjer och nya verktyg för utvecklarupplevelsen.

### Tillagt

- **Microsoft Agent Framework** avsnitt i lektion `17-ai-agents` som täcker enskilda chattagenter,
  verktyg/funktionsanrop, Azure OpenAI (Microsoft Foundry) konfiguration och multi-agent
  arbetsflödesorkestrering (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** dokumenterat som offline- / enhetsleverantör (tillsammans med Ollama) i
  `00-course-setup/03-providers.md` och lektion `19-slm`.
- **Kontinuerliga integrationsarbetsflöden**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (tillämpas på den underhållna `shared/`
    modulen, rekommendation för resten av kursplanen), en rekommenderande ESLint-körning och ett pytest-jobb.
  - `.github/workflows/security.yml` — CodeQL-analys (Python + JavaScript/TypeScript) och
    beroenderevision på pull-begäranden.
- **Testsvit** under `tests/` — 41 pytest-tester som täcker den delade hjälpbiblioteksmodulen.
- **Azure OpenAI → Responses API migreringskompetens** under
  `.github/skills/azure-openai-to-responses/` används för att vägleda API-migreringen.

### Ändrat

- **Chat Completions API → Responses API** i alla Python- och TypeScript-chattprov
  (`client.responses.create(...)` → `response.output_text`), inklusive lektionerna 04, 06, 07, 11,
  15 och 18 samt deras README-filer.
- **GitHub Models → Microsoft Foundry Models** genomgående i text, länkar och prover. GitHub Models
  pensioneras i slutet av juli 2026; prover pekar nu på Microsoft Foundrys modellkatalog och använder
  miljövariablerna `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` och leverantörsdokumentation** uppdaterade för att återspegla att Azure OpenAI nu är en del av
  Microsoft Foundry, och standard-API-versionen höjdes till `2024-10-21`.
- **TypeScript-prov** (lektionerna 06, 07, 08, 11) migrerade från den föråldrade beta-SDK:n `@azure/openai`
  till `openai`-paketet (chattappar använder Responses API; sökappen använder
  embeddingsklienten).
- **.NET-notebookar** (`dotnet/*.dib`) standardiserade på `Azure.AI.OpenAI` **2.1.0**: lektionerna 06 och 07
  använder `ChatClient` API, lektion 08 använder `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), och
  lektion 09 använder `ImageClient` (`GenerateImage`) med `gpt-image-1`, vilket ersätter den äldre
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` från `1.0.0-beta.9`.
- **Modernisering av produktnamn**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lektionerna 14, 16, 17) och "Bing" → **Microsoft Copilot** (lektion 12), där dessa syftade på
  aktuella produkter.
- **DevContainer** (`.devcontainer/`) inkluderar nu Pylance, Black, Ruff, ESLint, Prettier och Copilot
  extensioner, aktiverar format-on-save och installerar `ruff`, `black`, `mypy` och `pytest` så att CI-
  kontroller kan reproduceras lokalt.
- **Bildgenerering** (lektion 09) rekommenderar `gpt-image-1` för Azure (Azure-katalogen tog bort
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** uppdaterad för att återspegla avslutat arbete (API-migrering, CI,
  DevContainer, tester) och aktuella fakta (översättningar produceras automatiskt av
  Azure Co-op Translator; Assistants API har ersatts av Responses API).

### Fixat

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` returnerar nu en
  tom sträng för indatatxt som bara innehåller mellanrum istället för att kasta ett "för kort"-fel (i enlighet med
  `None`-fallet). Upptäckt och täckt av den nya testsviten.
- **Bildexempel i lektion 09** — korrigerade verkliga buggar: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  och en variabel som skuggade `openai`-modulen.
- **RAG-notebook i lektion 15** — reparerade klientinställningen, ersatte den borttagna `DataFrame.append`
  med `pd.concat` och moderniserade den gamla SDK-användningen.
- Föråldrade / pensionerade modellnamn (`gpt-3.5-turbo`, `gpt-35-turbo`) ersatta med `gpt-4o-mini`
  i aktiva prover; historiska fine-tuning-resultat i lektion 18 bevarades och annoterades
  istället för att skrivas om.

### Föråldrade / Noteringar

- **Microsoft Foundry Models-prov** som använder `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — `githubmodels-*` och `js-githubmodels` prover samt lektionerna 19, 20
  och 21 — förblir på Model Inference API, som **inte** stöder Responses API. Dessa har
  medvetet lämnats på den SDK:n.
- `AzureOpenAI()` behålls medvetet där det fortfarande är lämpligt (embeddings och bildgenerering),
  eftersom dessa arbetsflöden inte omfattas av Responses API-migreringen.
- Referenser till `text-embedding-ada-002` behålls där en förberäknad embedding-index är beroende av dem.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->