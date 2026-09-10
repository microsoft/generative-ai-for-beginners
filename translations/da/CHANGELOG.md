# Änderingslog

Alle bemærkelsesværdige ændringer til Generative AI for Beginners-kurset er dokumenteret i denne fil.

Formatet er baseret på [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Da dette er et
læringskursus fremfor en versionsstyret softwarepakke, er posterne grupperet efter dato.

## [2026-07-16] — Indholdsvalidering + Lektion 09 billedmateriale

### Ændret

- **Lektion 10 (low-code AI apps):** opdaterede to pensionerede `docs.microsoft.com/powerapps/...` Dataverse
  links til den aktuelle `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (bekræftet live).
- **Lektion 17 (AI agenter):** moderniserede et forældet modeleksempel (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, og Llama 3.3`) og et pladsholder-udrulningsnavn i Agent Framework-eksemplet
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Rod `README.md`:** tilføjede det manglende `?WT.mc_id=academic-105485-koreyst` tracking-ID til
  *Microsoft for Startups*-linket.
- **Lektion 09 billedmateriale** genereret på ny med `gpt-image` modellen: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png` og
  `images/startup.png` (redigerings-eksemplets før/efter par blev produceret via et virkelig
  `client.images.edit` kald med en genereret maske).

### Valideret

- Reviderede README-filer til lektionerne 01, 03, 05, 12, 14 og 16 — alle er aktuelle (korrekte Microsoft Foundry
  navne og links); ingen ændringer krævet.
- Kørte en fuld markdown-validering på alle 41 markdown-filer i repoen (ekskl. oversættelser) for
  forældede dokumentsstier, `/en-us/` Microsoft lokaliteter, forældede produkt-/modelnavne, manglende tracking
  ID'er og ødelagte relative links/billeder. Kun den enkelte *Microsoft for Startups* tracking-ID var
  anvendelig; alle andre mærker blev bekræftet som falske positiver (automatisk genererede oversættelseslinks,
  kommenterede pladsholdere og tredjeparts `/en/` strukturelle URL'er).

## [2026-07-15] — Omskrivning af lektion 09 (Billedapplikationer) til GPT billedmodeller

### Ændret

- **Omskrev lektion 09 "Byg billedegenereringsapplikationer"** omkring den aktuelle **`gpt-image`**
  modelfamilie (standard **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` også GA), som erstattede
  det gamle DALL·E 2/3-indhold. Vigtige rettelser:
  - `gpt-image` modeller returnerer billedet som **base64 (`b64_json`)**, ikke en URL. Opdaterede alle eksempler til
    `base64.b64decode(...)` i stedet for at downloade en `url` med `requests`.
  - Forøgede billed-API-versionen til `2025-04-01-preview`.
  - Udskiftede den opdigtede "temperatur"-sektion (billedmodeller bruger ikke `temperature`) og
    DALL·E-2-specifikke billed **variationer** med en **billedredigering** (maske/inpainting) sektion.
  - Opdaterede `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, begge
    opgave-notebooks (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`) og .NET `.dib` notebooken.

### Fjernet

- Slettede de forældede `python/aoai-app-variation.py` og `python/oai-app-variation.py` eksempler
  (`images.create_variation` er kun for DALL·E-2 og understøttes ikke af `gpt-image`).
- Slettede 4 forladte billedressourcer tilknyttet den fjernede temperatur-sammenligningssektion
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Fjernede den unødvendige `requests`-afhængighed fra lektionens Python-eksempler og krav.

### Valideret

- Kørte `aoai-app.py` end-to-end mod en udrullet `gpt-image-1.5` model og bekræftede at base64
  afkodnings-/gemmeflowet producerer en PNG. Notebooks bekræftet som gyldig JSON.

## [2026-07-14] — Standard Modelopdatering + Vejledning til Reasoning-Model

### Ændret

- **Standard chatmodel `gpt-4o-mini` → `gpt-5-mini`** på tværs af kursussets kørbare eksempler,
  dokumenter og konfiguration. Dette er styret af modellens livscyklusstatus: på Microsoft Foundry,
  `gpt-4o-mini` (pensioneres 2026-10-01) og hele `gpt-4.1` familien (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, pensioneres 2026-10-14) er **udfasende**, mens **GPT-5 familien
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) er generelt tilgængelig** (pensioneres 2027-02-06). Opdateret:
  - `.env.copy`, `00-course-setup/03-providers.md` (anbefalet udrulning og `az cognitiveservices`
    deploy-kommandoer) og README-filerne til lektion 04, 06, 07 og 15.
  - Python-eksempler i lektion 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) og scripts i lektion 08.
  - TypeScript / JavaScript-eksempler i lektion 06, 07 og 11 samt `.dib` .NET notebooks til
    lektion 06 og 07.
  - Opgavenotebooks i lektion 04, 06, 07 og 11 (kodeceller), plus `shared/python/api_utils.py`
    docstring-eksempler.
- **Vejledning til reasoning-model-parameter (ny).** `gpt-5-mini` er en *reasoning*-model: den understøtter **ikke**
  `temperature`/`top_p`, og bruger `max_completion_tokens` (chat-kompletions) /
  `max_output_tokens` (Responses API) i stedet for `max_tokens`. Følgelig:
  - Fjernede `temperature`/`top_p`/`max_tokens` fra eksempler, der nu bruger `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, lektion 15 RAG README).
  - Tilføjede en **"Reasoning-modeller bruger ikke `temperature`"** note til lektion 06, der forklarer, at
    reasoning-modeller styres med **prompt engineering + reasoning-kontroller** snarere end
    sampling-indstillinger, mens `temperature`/`top_p` stadig er gyldige på ikke-reasoning modeller
    (GPT-4.x, Mistral, Llama, Phi, åbne modeller).
- **`gpt-5-mini` bruges ikke til finjusteringsvejledningen (lektion 18).** GPT-5 understøtter kun
  reinforcement finjustering (RFT); lektion 18's overvågede finjustering (SFT) gennemgang bruger
  `gpt-4.1-mini`, som understøtter SFT/DPO.
- **Temperatur-demos bruger en Llama-model.** For at fortsætte med at undervise `temperature` (som reasoning-modeller
  afviser), bruges en `Llama-3.3-70B-Instruct` model via Foundry Models-endpointet. Tilføjede en ny
  `AZURE_INFERENCE_CHAT_MODEL` variabel til `.env.copy`; lektion 04/06 `githubmodels` notebooks og
  `06` `js-githubmodels` eksemplet benytter den (med fallback til `Llama-3.3-70B-Instruct`) og beholder deres
  `temperature`/`top_p`/`max_tokens` demos.
- **JS / .NET eksempler opdateret til GPT-5.** Fjernede `temperature`/`top_p`/`max_tokens` fra GPT-5
  eksemplerne (`06` `recipe-app` TypeScript, `06` `.dib` .NET - som også forhøjer `MaxOutputTokenCount`
  så reasoning-output ikke afkortes). `06` `js-githubmodels` eksemplet bruger nu Llama for at bevare sin
  temperatur-demo. `.dib` noterer, at `Azure.AI.Inference` + en Llama-model er måden at
  vise `Temperature` i .NET.
- Beholdt `gpt-4o-mini` / `gpt-5-mini`, hvor de stadig er korrekte: `tiktoken` token-encoding
  referencer, modelkatalog-tilgængelighedslister og lektion 02 tale-modeller (`gpt-4o-transcribe`).
- Lektion 20 (Mistral) og 21 (Meta) prøver beholder `temperature`/`max_tokens`, da de målretter
  Mistral/Llama modeller, som understøtter disse parametre.

## [2026-07-06] — Opdatering og modernisering af indhold

En bred opdatering for at holde kurset ajour for 2026: moderne API’er, aktuelle produkt- og
modelnavne, opdateret udbydervejledning og nyt udvikleroplevelses-værktøj.

### Tilføjet

- **Microsoft Agent Framework** sektion i lektion `17-ai-agents` der dækker enkelt-chat-agenter,
  værktøjer/funktionskald, Azure OpenAI (Microsoft Foundry) konfiguration og multi-agent
  workflow orkestrering (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** dokumenteret som offline / enhedsbaseret udbyder (sammen med Ollama) i
  `00-course-setup/03-providers.md` og lektion `19-slm`.
- **Kontinuerlige integrations-workflows**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (håndhævet på den vedligeholdte `shared/`
    modul, rådgivende på resten af kursusindholdet), en rådgivende ESLint-kørsel og en pytest-job.
  - `.github/workflows/security.yml` — CodeQL-analyse (Python + JavaScript/TypeScript) og
    afhængighedsgennemgang ved pull requests.
- **Testpakke** under `tests/` — 41 pytest tests, der dækker det delte hjælpeværktøjsmodul.
- **Azure OpenAI → Responses API migrationskompetence** under
  `.github/skills/azure-openai-to-responses/` brugt til at vejlede API-migrationen.

### Ændret

- **Chat Completions API → Responses API** på tværs af alle Python- og TypeScript chat-eksempler
  (`client.responses.create(...)` → `response.output_text`), inkl. lektion 04, 06, 07, 11,
  15 og 18, samt deres README’er.
- **GitHub Models → Microsoft Foundry Models** gennem hele teksten, links og eksempler. GitHub Models
  pensioneres ved udgangen af juli 2026; eksempler peger nu på Microsoft Foundry modelkataloget og bruger
  miljøvariablerne `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` og udbyderdokumenter** opdateret til at afspejle, at Azure OpenAI nu er en del
  af Microsoft Foundry, og den standard API-version er opgraderet til `2024-10-21`.
- **TypeScript eksempler** (lektion 06, 07, 08, 11) migreret fra den forældede `@azure/openai`
  beta SDK til `openai` pakken (chat-apps bruger Responses API; søge-app bruger
  embeddings-klienten).
- **.NET notebooks** (`dotnet/*.dib`) standardiseret på `Azure.AI.OpenAI` **2.1.0**: lektion 06 og 07
  bruger `ChatClient` API, lektion 08 bruger `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`) og
  lektion 09 bruger `ImageClient` (`GenerateImage`) med `gpt-image-1`, der erstatter den gamle
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` fra `1.0.0-beta.9`.
- **Modernisering af produktnavne**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lektion 14, 16, 17) og "Bing" → **Microsoft Copilot** (lektion 12), hvor disse henviste til
  nuværende produkter.
- **DevContainer** (`.devcontainer/`) inkluderer nu Pylance, Black, Ruff, ESLint, Prettier og Copilot
  udvidelser, aktiverer formatering ved gem, og installerer `ruff`, `black`, `mypy` og `pytest`, så CI
  tjek kan reproduceres lokalt.
- **Billedgenerering** (lektion 09) anbefaler `gpt-image-1` til Azure (Azure-kataloget fjernede
  `dall-e-3`).

- **`docs/ENHANCED_FEATURES_ROADMAP.md`** opdateret for at afspejle færdigt arbejde (API-migration, CI,
  DevContainer, tests) og aktuelle fakta (oversættelser produceres automatisk af
  Azure Co-op Translator; Assistants API er blevet afløst af Responses API).

### Rettet

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` returnerer nu en
  tom streng for input med kun mellemrum i stedet for at kaste en "for kort" fejl (i overensstemmelse med
  `None`-tilfældet). Fundet og dækket af den nye testsuite.
- **Lesson 09 billedeksempler** — rettede reelle fejl: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  samt en variabel der overskyggede `openai` modulet.
- **Lesson 15 RAG-notebook** — reparerede klientopsætningen, erstattede det fjernede `DataFrame.append`
  med `pd.concat`, og moderniserede den gamle SDK-brug.
- Udfasede / pensionerede modelnavne (`gpt-3.5-turbo`, `gpt-35-turbo`) erstattet med `gpt-4o-mini`
  i aktive eksempler; historiske fine-tuning outputs i lektion 18 er bevaret og annoteret
  fremfor omskrevet.

### Udfaset / Noter

- **Microsoft Foundry Models eksempler** der bruger `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — `githubmodels-*` og `js-githubmodels` eksempler samt lektion 19, 20,
  og 21 — forbliver på Model Inference API, som **ikke** understøtter Responses API. Disse er
  med vilje efterladt på den SDK.
- `AzureOpenAI()` bevares med vilje der hvor det stadig er relevant (embeddings og billedgenerering),
  da disse workflows ikke er del af Responses API-migrationen.
- Referencer til `text-embedding-ada-002` beholdes hvor en prækalkuleret embedding indeks er afhængig af dem.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->