# Endringslogg

Alle merkbare endringer i Generative AI for nybegynnere-læreplanen dokumenteres i denne filen.

Formatet er basert på [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Siden dette er en
læringsplan og ikke en versjonert programvarepakke, grupperes oppføringene etter dato.

## [2026-07-06] — Innholdsmodernisering Oppfriskning

En bred oppfriskning for å holde læreplanen nøyaktig for 2026: moderne APIer, nåværende produktnavn og
modellenavn, oppdatert veiledning for leverandører og nytt verktøy for utvikleropplevelse.

### Lagt til

- **Microsoft Agent Framework** seksjon i leksjon `17-ai-agents` omhandler enkeltchat-agenter,
  verktøy/funksjonskall, Azure OpenAI (Microsoft Foundry) konfigurasjon, og multi-agent
  arbeidsflytorkestrering (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** dokumentert som en offline / enhetsbasert leverandør (ved siden av Ollama) i
  `00-course-setup/03-providers.md` og leksjon `19-slm`.
- **Kontinuerlige integreringsarbeidsflyter**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (håndhevet på den vedlikeholdte `shared/`
    modulen, veiledende på resten av læreplanen), en veiledende ESLint-gjennomgang, og en pytest-jobb.
  - `.github/workflows/security.yml` — CodeQL-analyse (Python + JavaScript/TypeScript) og
    avhengighetsgjennomgang på pull requests.
- **Testsuite** under `tests/` — 41 pytest-tester som dekker den delte hjelpebibliotekmodulen.
- **Azure OpenAI → Responses API migreringsferdighet** under
  `.github/skills/azure-openai-to-responses/` brukt for å veilede API-migreringen.

### Endret

- **Chat Completions API → Responses API** i alle Python- og TypeScript-chat-eksempler
  (`client.responses.create(...)` → `response.output_text`), inkludert leksjonene 04, 06, 07, 11,
  15, og 18, pluss deres README-filer.
- **GitHub Models → Microsoft Foundry Models** gjennomgående i tekst, lenker og eksempler. GitHub Models
  fases ut ved slutten av juli 2026; eksempler peker nå til Microsoft Foundry modellkatalog og bruker
  miljøvariablene `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` og leverandørdokumentasjon** oppdatert for å reflektere at Azure OpenAI nå er en del
  av Microsoft Foundry, og standard API-versjon oppjustert til `2024-10-21`.
- **TypeScript-eksempler** (leksjoner 06, 07, 08, 11) migrert bort fra den utdaterte `@azure/openai`
  beta SDK til `openai`-pakken (chat-applikasjoner bruker Responses API; søkeapplikasjonen bruker
  embeddings-klienten).
- **.NET-notatbøker** (`dotnet/*.dib`) standardisert på `Azure.AI.OpenAI` **2.1.0**: leksjonene 06 og 07
  bruker `ChatClient` API, leksjon 08 bruker `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), og
  leksjon 09 bruker `ImageClient` (`GenerateImage`) med `gpt-image-1`, som erstatter den gamle
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` fra `1.0.0-beta.9`.
- **Produktnavnmodernisering**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (leksjoner 14, 16, 17) og "Bing" → **Microsoft Copilot** (leksjon 12), der disse refererte til
  nåværende produkter.
- **DevContainer** (`.devcontainer/`) leverer nå Pylance, Black, Ruff, ESLint, Prettier og Copilot
  utvidelser, aktiverer formatering ved lagring, og installerer `ruff`, `black`, `mypy` og `pytest` så CI-
  kontroller kan gjenskapes lokalt.
- **Bildegenerering** (leksjon 09) anbefaler `gpt-image-1` for Azure (Azure-katalogen fjernet
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** oppdatert for å reflektere fullført arbeid (API-migrering, CI,
  DevContainer, tester) og nåværende fakta (oversettelser produseres automatisk av
  Azure Co-op Translator; Assistants API er erstattet av Responses API).

### Fikset

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` returnerer nå en
  tom streng for inndata med bare mellomrom i stedet for å kaste en "for kort" feil (i samsvar med
  `None`-tilfellet). Funnet og dekket av den nye testsuiten.
- **Bildeeksempler i leksjon 09** — korrigerte ekte feil: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  og en variabel som overskygget `openai`-modulen.
- **Leksjon 15 RAG notatbok** — reparerte klientoppsett, erstattet den fjernede `DataFrame.append`
  med `pd.concat`, og moderniserte gammel SDK-bruk.
- Utdaterte / pensjonerte modellenavn (`gpt-3.5-turbo`, `gpt-35-turbo`) erstattet med `gpt-4o-mini`
  i aktive eksempler; historiske finjusteringsutdata i leksjon 18 ble bevart og annotert
  i stedet for omskrevet.

### Utdaterte / Notater

- **Microsoft Foundry Models eksempler** som bruker `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) – `githubmodels-*` og `js-githubmodels` eksempler og leksjonene 19, 20,
  og 21 – forblir på Model Inference API, som **ikke** støtter Responses API. Disse er
  med vilje beholdt på denne SDK-en.
- `AzureOpenAI()` beholdes med hensikt der det fortsatt er passende (embedding og bildegenerering),
  siden disse arbeidsflytene ikke er en del av Responses API-migreringen.
- Referanser til `text-embedding-ada-002` beholdes der en forhåndsberegnet embedding-indeks avhenger av dem.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->