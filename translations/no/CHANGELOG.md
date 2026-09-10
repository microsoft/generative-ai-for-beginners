# Endringslogg

Alle merkbare endringer i Generative AI for nybegynnere pensum dokumenteres i denne filen.

Formatet er basert på [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Fordi dette er en
læringspensum snarere enn en versjonert programvarepakke, er oppføringer gruppert etter dato.

## [2026-07-16] — Validering av innhold + Bildeelementer for leksjon 09

### Endret

- **Leksjon 10 (lavkode AI-apper):** oppdaterte to pensjonerte `docs.microsoft.com/powerapps/...` Dataverse
  linker til den nåværende `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (verifisert live).
- **Leksjon 17 (AI-agenter):** moderniserte et utdatert modeleksempel (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, og Llama 3.3`) og et plassholder-distribusjonsnavn i Agent Framework-eksemplet
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Rot `README.md`:** la til den manglende `?WT.mc_id=academic-105485-koreyst` sporings-ID til
  *Microsoft for Startups* lenken.
- **Leksjon 09 bildeelementer** ble generert på nytt med `gpt-image`-modellen: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, og
  `images/startup.png` (før/etter-eksempelet på redigering ble produsert via en ekte
  `client.images.edit` kall med en generert maske).

### Validert

- Revidert README-filene for leksjonene 01, 03, 05, 12, 14, og 16 — alle oppdaterte (korrekt Microsoft Foundry
  navngivning og lenker); ingen endringer nødvendig.
- Kjørte full markdown-validering på alle 41 markdown filer i repoet (unntatt oversettelser) for
  utdaterte dokumentbaner, `/en-us/` Microsoft lokaler, utdaterte produkt-/modelnavn, manglende sporings-
  IDer, og ødelagte relative lenker/bilder. Kun det enkeltstående *Microsoft for Startups* sporings-ID-gapet var
  relevant; alle andre varsler ble bekreftet som falske positive (automatisk genererte oversettelseslenker,
  utkommenterte plassholdere, og tredjeparts `/en/` strukturelle URLer).

## [2026-07-15] — Omskriving av Leksjon 09 (Bildeapplikasjoner) for GPT Bildemodeller

### Endret

- **Omskrev leksjon 09 "Bygge bildegenereringsapplikasjoner"** rundt den nåværende **`gpt-image`**
  modelfamilien (standard **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` også GA), og erstattet
  det utdaterte DALL·E 2/3-innholdet. Viktige korreksjoner:
  - `gpt-image` modeller returnerer bildet som **base64 (`b64_json`)**, ikke en URL. Oppdatert alle eksemplene til
    `base64.b64decode(...)` i stedet for å laste ned en `url` med `requests`.
  - Oppgradert bilde-API-versjonen til `2025-04-01-preview`.
  - Erstattet det fabrikkerte "temperature"-avsnittet (bildemodeller bruker ikke `temperature`) og
    DALL·E-2-spesifikke bilde **variasjoner**-innhold med et **bilde-redigerings** (maske/inpainting) avsnitt.
  - Oppdatert `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, begge
    oppgaveskript (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), og .NET `.dib` notatblokk.

### Fjernet

- Slettet utdatert `python/aoai-app-variation.py` og `python/oai-app-variation.py` eksempler
  (`images.create_variation` er kun for DALL·E-2 og støttes ikke av `gpt-image`).
- Slettet 4 foreldreløse bildeelementer knyttet til den fjernede temperatur-sammenligningsseksjonen
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Fjernet den unødvendige `requests`-avhengigheten fra leksjonens Python-eksempler og krav.

### Validert

- Kjørte `aoai-app.py` ende-til-ende mot en distribuert `gpt-image-1.5` modell og bekreftet at base64
  dekoder/- lagringsflyten produserer en PNG. Notatblokkene ble bekreftet som gyldig JSON.

## [2026-07-14] — Oppdatering av standardmodell + Veiledning for resonneringsmodell

### Endret

- **Standard chatmodell `gpt-4o-mini` → `gpt-5-mini`** i alle kjørbare eksempler,
  dokumenter og konfigurasjoner i pensum. Dette ble drevet av modellens livssyklusstatus: på Microsoft Foundry,
  `gpt-4o-mini` (pensioneres 2026-10-01) og hele `gpt-4.1` familien (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, pensioneres 2026-10-14) er **på vei til utfasing**, mens **GPT-5 familien
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) er generelt tilgjengelig** (pensioneres 2027-02-06). Oppdaterte:
  - `.env.copy`, `00-course-setup/03-providers.md` (anbefalt distribusjon og `az cognitiveservices`
    deploy-kommandolinjer), og README-filer for leksjonene 04, 06, 07, og 15.
  - Python-eksempler i leksjon 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) og leksjon 08 skript.
  - TypeScript / JavaScript-eksempler i leksjonene 06, 07, og 11, og `.dib` .NET-notatblokker for
    leksjon 06 og 07.
  - Oppgaveskript i leksjonene 04, 06, 07, og 11 (kodeceller), pluss `shared/python/api_utils.py`
    docstring-eksempler.
- **Veiledning for resonneringsmodellparameter (ny).** `gpt-5-mini` er en *resonnerings*modell: den støtter **ikke**
  `temperature`/`top_p`, og bruker `max_completion_tokens` (chat-completions) /
  `max_output_tokens` (Responses API) i stedet for `max_tokens`. Følgelig:
  - Fjernet `temperature`/`top_p`/`max_tokens` fra eksempler som nå bruker `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, leksjon 15 RAG README).
  - La til en **"Resonneringsmodeller bruker ikke `temperature`"** merknad i leksjon 06, som forklarer at
    resonneringsmodeller styres med **prompt-teknikk + resonneringskontroller** fremfor
    sampling-parametere, mens `temperature`/`top_p` fortsatt er gyldige for ikke-resonneringsmodeller
    (GPT-4.x, Mistral, Llama, Phi, åpne modeller).
- **`gpt-5-mini` brukes ikke i finjusteringsveiledningen (leksjon 18).** GPT-5 støtter kun
  forsterkningsfinjustering (RFT); veiledningen for veiledet finjustering (SFT) i leksjon 18 beholder
  `gpt-4.1-mini`, som støtter SFT/DPO.
- **Temperatur-demoer bruker en Llama-modell.** For å fortsette undervisning i `temperature` (som resonneringsmodeller
  ikke støtter), brukes en `Llama-3.3-70B-Instruct` modell via Foundry Models-endepunktet. La til en ny
  `AZURE_INFERENCE_CHAT_MODEL` variabel i `.env.copy`; leksjon 04/06 `githubmodels` notatblokker og
  `06` `js-githubmodels` eksempler leser denne (tilbakefall til `Llama-3.3-70B-Instruct`) og beholder sine
  `temperature`/`top_p`/`max_tokens` demoer.
- **JS / .NET-eksempler oppdatert for GPT-5.** Fjernet `temperature`/`top_p`/`max_tokens` fra GPT-5
  eksemplene (`06` `recipe-app` TypeScript, `06` `.dib` .NET - som også hever `MaxOutputTokenCount`
  slik at resonneringsutdata ikke trunkeres). `06` `js-githubmodels` eksemplet bruker nå Llama for å beholde sin
  temperatur-demo. `.dib` noterer at `Azure.AI.Inference` + en Llama-modell er måten å
  demonstrere `Temperature` i .NET.
- Beholdt `gpt-4o-mini` / `gpt-5-mini` der de fortsatt er nøyaktige: `tiktoken` token-kodings-
  referanser, liste over modellkatalog tilgjengelighet, og leksjon 02 tale modeller (`gpt-4o-transcribe`).
- Leksjon 20 (Mistral) og 21 (Meta) eksempler beholder `temperature`/`max_tokens` fordi de målretter
  Mistral/Llama modeller, som støtter disse parameterne.

## [2026-07-06] — Oppfriskning av innholdsmodernisering

En bred oppdatering for å holde pensum nøyaktig for 2026: moderne API-er, nåværende produktnavn og
modelnavn, oppdatert veiledning for leverandører, og nye verktøy for utvikleropplevelse.

### Lagt til

- **Microsoft Agent Framework** seksjon i leksjon `17-ai-agents` om enkelt-chatagenter,
  verktøy/funksjonskall, Azure OpenAI (Microsoft Foundry) konfigurasjon, og multi-agent
  arbeidsflyt-orchestrering (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** dokumentert som en offline/fjernleverandør (sammen med Ollama) i
  `00-course-setup/03-providers.md` og leksjon `19-slm`.
- **Kontinuerlige integrasjons-arbeidsflyter**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (påtvunget i `shared/`
    modulen, veiledende i resten av pensumet), en rådgivende ESLint gjennomgang, og et pytest-jobb.
  - `.github/workflows/security.yml` — CodeQL analyse (Python + JavaScript/TypeScript) og
    avhengighetsgjennomgang på pull requests.
- **Testsuite** under `tests/` — 41 pytest tester som dekker den delte verktøymodulen.
- **Azure OpenAI → Responses API migreringsferdighet** under
  `.github/skills/azure-openai-to-responses/` som brukes til å veilede API-migrasjonen.

### Endret

- **Chat Completions API → Responses API** i alle Python og TypeScript chat-eksempler
  (`client.responses.create(...)` → `response.output_text`), inkludert leksjoner 04, 06, 07, 11,
  15, og 18, pluss deres README-filer.
- **GitHub Models → Microsoft Foundry Models** i all tekst, lenker og eksempler. GitHub Models
  pensjoneres ved slutten av juli 2026; eksempler viser nå til Microsoft Foundry modellkatalog og bruker
  miljøvariablene `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md`, og leverandørdokumentasjon** oppdatert for å gjenspeile at Azure OpenAI nå er en del
  av Microsoft Foundry, og standard API-versjon oppgradert til `2024-10-21`.
- **TypeScript-eksempler** (leksjoner 06, 07, 08, 11) migrert bort fra utgått `@azure/openai`
  beta SDK til `openai`-pakken (chat-apper bruker Responses API; søke-appen bruker
  embeddings-klienten).
- **.NET-notatblokker** (`dotnet/*.dib`) standardisert på `Azure.AI.OpenAI` **2.1.0**: leksjon 06 og 07
  bruker `ChatClient` API, leksjon 08 bruker `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), og
  leksjon 09 bruker `ImageClient` (`GenerateImage`) med `gpt-image-1`, og erstatter den utdaterte
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` fra `1.0.0-beta.9`.
- **Modernisering av produktnavn**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (leksjoner 14, 16, 17) og "Bing" → **Microsoft Copilot** (leksjon 12), der disse refererte til
  nåværende produkter.
- **DevContainer** (`.devcontainer/`) inkluderer nå Pylance, Black, Ruff, ESLint, Prettier, og Copilot
  utvidelser, aktiverer formatering ved lagring, og installerer `ruff`, `black`, `mypy`, og `pytest` slik at CI
  tester kan reproduseres lokalt.
- **Bildgenerering** (leksjon 09) anbefaler `gpt-image-1` for Azure (Azure katalogen har fjernet
  `dall-e-3`).

- **`docs/ENHANCED_FEATURES_ROADMAP.md`** oppdatert for å gjenspeile fullført arbeid (API-migrasjon, CI,
  DevContainer, tester) og nåværende fakta (oversettelser produseres automatisk av
  Azure Co-op Translator; Assistants API er erstattet av Responses API).

### Fikset

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` returnerer nå en
  tom streng for inndata med kun mellomrom i stedet for å kaste en "for kort"-feil (konsekvent med
  `None`-tilfellet). Funnet og dekket av den nye testsuiten.
- **Lesson 09 bildeeksempler** — korrigerte reelle feil: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  og en variabel som skjulte `openai`-modulen.
- **Lesson 15 RAG-notatbok** — reparerte klientoppsettet, erstattet fjernet `DataFrame.append`
  med `pd.concat`, og moderniserte den gamle SDK-bruken.
- Utdaterte / pensjonerte modellnavn (`gpt-3.5-turbo`, `gpt-35-turbo`) erstattet med `gpt-4o-mini`
  i aktive eksempler; historiske finjusteringsutdata i lesson 18 ble bevart og merket
  i stedet for omskrevet.

### Utdatert / Merknader

- **Microsoft Foundry Models-eksempler** som bruker `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — `githubmodels-*` og `js-githubmodels` eksempler og lekser 19, 20,
  og 21 — forblir på Model Inference API, som **ikke** støtter Responses API. Disse er
  med vilje beholdt på den SDK-en.
- `AzureOpenAI()` beholdes bevisst der det fortsatt er passende (embedding og bildegenerering),
  ettersom disse arbeidsflytene ikke er en del av Responses API-migrasjonen.
- Referanser til `text-embedding-ada-002` beholdes der en forhåndsberegnet embedding-indeks er avhengig av dem.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->