# Ændringslog

Alle bemærkelsesværdige ændringer til Generative AI for Beginners pensum er dokumenteret i denne fil.

Formatet er baseret på [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Da dette er et
læringspensum fremfor en versionsstyret softwarepakke, er indtastninger grupperet efter dato.

## [2026-07-06] — Indholdsmodernisering Opdatering

En bred opdatering for at holde pensum nøjagtigt for 2026: moderne API'er, aktuelle produktnavne og
modelnavne, opdateret leverandørvejledning og nye udvikleroplevelsesværktøjer.

### Tilføjet

- **Microsoft Agent Framework** sektion i lektion `17-ai-agents`, der dækker enkelt chatagenter,
  værktøjer/funktionsopkald, Azure OpenAI (Microsoft Foundry) konfiguration og multi-agent
  workflow orkestrering (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** dokumenteret som en offline / på-enheden leverandør (sammen med Ollama) i
  `00-course-setup/03-providers.md` og lektion `19-slm`.
- **Continuous integration workflows**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (håndhævet på den vedligeholdte `shared/`
    modul, vejledende på resten af pensum), et rådgivende ESLint-kørsel og en pytest-job.
  - `.github/workflows/security.yml` — CodeQL-analyse (Python + JavaScript/TypeScript) og
    afhængighedsgennemgang ved pull requests.
- **Test suite** under `tests/` — 41 pytest tests, der dækker den delte hjælpefunktion modul.
- **Azure OpenAI → Responses API migrationsskill** under
  `.github/skills/azure-openai-to-responses/` brugt til at vejlede API-migrationen.

### Ændret

- **Chat Completions API → Responses API** i alle Python- og TypeScript-chat-eksempler
  (`client.responses.create(...)` → `response.output_text`), inklusive lektionerne 04, 06, 07, 11,
  15 og 18, plus deres README-filer.
- **GitHub Models → Microsoft Foundry Models** gennemgående i tekst, links og eksempler. GitHub Models
  udfases ved slutningen af juli 2026; eksempler peger nu på Microsoft Foundry-modelkataloget og anvender
  miljøvariablerne `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` og leverandørdokumentation** opdateret for at afspejle, at Azure OpenAI nu er en del
  af Microsoft Foundry, og den standard API-version er rykket til `2024-10-21`.
- **TypeScript-eksempler** (lektionerne 06, 07, 08, 11) migreret fra den udgåede `@azure/openai`
  beta SDK til `openai`-pakken (chatapps bruger Responses API; søgeappen bruger
  embeddings-klienten).
- **.NET notebooks** (`dotnet/*.dib`) standardiseret på `Azure.AI.OpenAI` **2.1.0**: lektionerne 06 og 07
  bruger `ChatClient` API, lektion 08 bruger `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), og
  lektion 09 bruger `ImageClient` (`GenerateImage`) med `gpt-image-1`, hvilket erstatter den gamle
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` fra `1.0.0-beta.9`.
- **Produktnavn modernisering**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lektionerne 14, 16, 17) og "Bing" → **Microsoft Copilot** (lektion 12), hvor disse refererede til
  de aktuelle produkter.
- **DevContainer** (`.devcontainer/`) indeholder nu Pylance, Black, Ruff, ESLint, Prettier og Copilot
  udvidelser, aktiverer formatering-ved-gem, og installerer `ruff`, `black`, `mypy` og `pytest`, så CI
  tjek kan genskabes lokalt.
- **Billedgenerering** (lektion 09) anbefaler `gpt-image-1` for Azure (Azure-kataloget droppede
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** opdateret for at afspejle færdigt arbejde (API-migration, CI,
  DevContainer, tests) og aktuelle fakta (oversættelser produceres automatisk af
  Azure Co-op Translator; Assistants API er erstattet af Responses API).

### Rettet

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` returnerer nu en
  tom streng for input med kun whitespace i stedet for at rejse en "for kort" fejl (konsistent med
  `None`-tilfældet). Fundet og dækket af den nye testsuite.
- **Lektion 09 billedeksempler** — rettede reelle fejl: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  og en variabel, der skjulte `openai` modulet.
- **Lektion 15 RAG notebook** — reparerede klientopsætningen, udskiftede den fjernede `DataFrame.append`
  med `pd.concat`, og moderniserede den gamle SDK-brug.
- Udgåede / udfasede modelnavne (`gpt-3.5-turbo`, `gpt-35-turbo`) erstattet med `gpt-4o-mini`
  i aktive eksempler; historiske fine-tuning output i lektion 18 blev bevaret og annoteret
  i stedet for omskrevet.

### Udgået / Noter

- **Microsoft Foundry Models eksempler**, der bruger `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — `githubmodels-*` og `js-githubmodels` eksempler og lektioner 19, 20,
  og 21 — forbliver på Model Inference API, som **ikke** understøtter Responses API. Disse er
  bevidst efterladt på den SDK.
- `AzureOpenAI()` bevares bevidst, hvor det stadig er relevant (embeddings og billedgenerering),
  da disse workflows ikke er en del af Responses API migrationen.
- Referencer til `text-embedding-ada-002` beholdes, hvor et precomputret embedding-indeks er afhængigt af dem.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->