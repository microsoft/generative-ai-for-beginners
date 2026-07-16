# Änderingslogg

Alla märkbara ändringar i Generative AI for Beginners-kursplanen dokumenteras i denna fil.

Formatet är baserat på [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Eftersom detta är en
utbildningsplan snarare än ett versionshanterat mjukvarupaket, är poster grupperade efter datum.

## [2026-07-16] — Innehållsvalidering + Bildresurser för Lektion 09

### Ändrat

- **Lektion 10 (low-code AI-appar):** uppdaterade två pensionerade `docs.microsoft.com/powerapps/...` Dataverse
  länkar till den aktuella `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (verifierat live).
- **Lektion 17 (AI-agenter):** moderniserade ett daterat modellexempel (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, och Llama 3.3`) och ett platshållarnamn för distribution i Agent Framework-exemplet
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Rot `README.md`:** lade till den saknade `?WT.mc_id=academic-105485-koreyst` spårnings-ID i
  *Microsoft for Startups*-länken.
- **Bildresurser för Lektion 09** genererades på nytt med `gpt-image` modellen: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png` och
  `images/startup.png` (exemplet för redigering före/efter producerades via ett verkligt
  `client.images.edit` anrop med en genererad mask).

### Validerat

- Granskade README-filerna för lektionerna 01, 03, 05, 12, 14 och 16 — alla aktuella (korrekta Microsoft Foundry
  namn och länkar); inga ändringar krävdes.
- Körde en fullständig markdown-validering över alla 41 markdown-filer i repo (exklusive översättningar) för
  utgångna dokumentsökvägar, `/en-us/` Microsoft-lokaler, föråldrade produkt-/modnamn, saknade spårnings-
  ID:n och brutna relativa länkar/bilder. Endast det enda *Microsoft for Startups* spårnings-ID-gapet
  var åtgärdbart; alla andra flaggor bekräftades som falska positiva (automatiskt genererade översättningslänkar,
  kommenterade platshållare och tredjeparts `/en/` strukturella URL:er).

## [2026-07-15] — Omskrivning av Lektion 09 (Bildapplikationer) för GPT Bildmodeller

### Ändrat

- **Omskrev lektion 09 "Bygga applikationer för bildgenerering"** kring den aktuella **`gpt-image`**
  modelfamiljen (standard **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` är också GA), och ersatte
  det föråldrade DALL·E 2/3-innehållet. Viktiga korrigeringar:
  - `gpt-image` modeller returnerar bilden som **base64 (`b64_json`)**, inte en URL. Uppdaterade alla exempel till
    `base64.b64decode(...)` istället för att ladda ner en `url` med `requests`.
  - Uppgraderade bild-API-versionen till `2025-04-01-preview`.
  - Ersatte det påhittade "temperature"-avsnittet (bildmodeller tar inte `temperature`) och DALL·E-2-endast bild
    **variationer** innehållet med ett **bildredigerings**-avsnitt (mask/inpainting).
  - Uppdaterade `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, båda
    assignmentsböckerna (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`) och .NET `.dib` notebook.

### Tagit bort

- Raderade de föråldrade exemplen `python/aoai-app-variation.py` och `python/oai-app-variation.py`
  (`images.create_variation` är DALL·E-2-endast och stöds inte av `gpt-image`).
- Raderade 4 kvarlämnade bildresurser kopplade till det borttagna temperatur-jämförelseavsnittet
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Tog bort den onödiga `requests`-beroendet från lektionens Python-exempel och krav.

### Validerat

- Körde `aoai-app.py` helt och hållet mot en distribuerad `gpt-image-1.5`-modell och bekräftade att base64
  dekodnings-/sparflödet producerar en PNG. Assignmentsböcker bekräftades vara giltig JSON.

## [2026-07-14] — Standardmodelluppdatering + Riktlinjer för resonemangsmodeller

### Ändrat

- **Standard chattmodell `gpt-4o-mini` → `gpt-5-mini`** i hela kursplanens körbara exempel,
  dokumentation och konfiguration. Detta drevs av modellens livscykelstatus: på Microsoft Foundry,
  `gpt-4o-mini` (pensioneras 2026-10-01) och hela `gpt-4.1` familjen (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, pensioneras 2026-10-14) är **under avveckling**, medan **GPT-5 familjen
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) är Allmänt Tillgänglig** (pensioneras 2027-02-06). Uppdaterad:
  - `.env.copy`, `00-course-setup/03-providers.md` (rekommenderade distributions- och `az cognitiveservices`
    kommandon), och README-filer för lektionerna 04, 06, 07 och 15.
  - Python-exempel i lektion 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) och lektion 08:s skript.
  - TypeScript / JavaScript-exempel i lektionerna 06, 07 och 11, och .NET `.dib` notebooks för
    lektionerna 06 och 07.
  - Assignmentsböcker i lektionerna 04, 06, 07 och 11 (kodceller), plus `shared/python/api_utils.py`
    docstringexempel.
- **Riktlinjer för parametrar för resonemangsmodellen (nytt).** `gpt-5-mini` är en *resonemangs*modell: den stöder
  **inte** `temperature`/`top_p`, och använder `max_completion_tokens` (chattkompletteringar) /
  `max_output_tokens` (Responses API) istället för `max_tokens`. Följaktligen:
  - Tog bort `temperature`/`top_p`/`max_tokens` från exempel som nu standardmässigt använder `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, lektion 15 RAG README).
  - Lade till en **"Resonemangsmodeller använder inte `temperature`"**-notis i lektion 06, som förklarar att
    resonemangsmodeller styrs med **prompt engineering + resonemangskontroller** snarare än
    sampelparametrar, medan `temperature`/`top_p` är giltiga på icke-resonemangsmodeller
    (GPT-4.x, Mistral, Llama, Phi, öppna modeller).
- **`gpt-5-mini` används inte för finjusteringshandledningen (lektion 18).** GPT-5 stödjer endast
  förstärkningsbaserad finjustering (RFT); lektion 18:s handledning för övervakad finjustering (SFT) använder
  `gpt-4.1-mini`, som stöder SFT/DPO.
- **Temperaturdemonstrationer använder en Llama-modell.** För att fortsätta lära ut `temperature` (som resonemangsmodeller
  avvisar), används en `Llama-3.3-70B-Instruct` modell via Foundry Models endpoint. En ny
  `AZURE_INFERENCE_CHAT_MODEL` variabel lades till i `.env.copy`; lektion 04/06 `githubmodels` notebooks och
  `06` `js-githubmodels` exemplet läser den (med fallback till `Llama-3.3-70B-Instruct`) och behåller sina
  `temperature`/`top_p`/`max_tokens` demonstrationer.
- **JS / .NET-exempel uppdaterade för GPT-5.** Tog bort `temperature`/`top_p`/`max_tokens` från GPT-5
  exemplen (`06` `recipe-app` TypeScript, `06` `.dib` .NET - som också höjer `MaxOutputTokenCount`
  så resonemangsoutput inte trunkeras). `06` `js-githubmodels` exemplet använder nu Llama för att behålla sin
  temperaturdemo. `.dib` noterar att `Azure.AI.Inference` + en Llama-modell är sättet att
  demonstrera `Temperature` i .NET.
- Lämnade `gpt-4o-mini` / `gpt-5-mini` på plats där de fortfarande är korrekta: `tiktoken` token-kodnings
  referenser, modellkatalogtillgänglighetslistor och lektion 02:s talmodeller (`gpt-4o-transcribe`).
- Lektion 20 (Mistral) och 21 (Meta) exemplen behåller `temperature`/`max_tokens` eftersom de riktar sig till
  Mistral/Llama modeller, som stödjer dessa parametrar.

## [2026-07-06] — Uppdatering och Förnyelse av Innehåll

En bred förnyelse för att hålla kursplanen korrekt för 2026: moderna API:er, aktuella produktnamn och
modellnamn, uppdaterade leverantörsriktlinjer och nytt utvecklarverktyg.

### Tillagt

- **Microsoft Agent Framework** avsnitt i lektion `17-ai-agents` som täcker enskilda chattagenter,
  verktyg/funktionsanrop, Azure OpenAI (Microsoft Foundry) konfiguration och multi-agent
  arbetsflödesorkestrering (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** dokumenterat som en offline-/på-enheten-leverantör (tillsammans med Ollama) i
  `00-course-setup/03-providers.md` och lektion `19-slm`.
- **Integrationsarbetsflöden:**
  - `.github/workflows/code-quality.yml` — Ruff + Black (tillämpas på det underhållna `shared/`
    modulen, rådgivande för resten av kursplanen), en rådgivande ESLint-pass och ett pytest-jobb.
  - `.github/workflows/security.yml` — CodeQL-analys (Python + JavaScript/TypeScript) och
    beroendegranskning vid pull-förfrågningar.
- **Testsvit** under `tests/` — 41 pytest-tester som täcker den delade hjälpfunktionmodulen.
- **Färdighet för migration Azure OpenAI → Responses API** under
  `.github/skills/azure-openai-to-responses/` som används för att vägleda API-migreringen.

### Ändrat

- **Chat Completions API → Responses API** i alla Python- och TypeScript-chatt-exempel
  (`client.responses.create(...)` → `response.output_text`), inkluderande lektionerna 04, 06, 07, 11,
  15 och 18, samt deras README-filer.
- **GitHub Models → Microsoft Foundry Models** genom hela texten, länkar och exempel. GitHub Models
  pensioneras i slutet av juli 2026; exemplen pekar nu till Microsoft Foundry:s modellkatalog och använder
  miljövariablerna `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md`, och leverantörsdokumentation** uppdaterades för att reflektera att Azure OpenAI nu är en del
  av Microsoft Foundry, och att standard-API-versionen höjts till `2024-10-21`.
- **TypeScript-exempel** (lektionerna 06, 07, 08, 11) migrerade från det föråldrade `@azure/openai`
  beta-SDK:t till `openai`-paketet (chattappar använder Responses API; sökappen använder
  embedding-klienten).
- **.NET-notebooks** (`dotnet/*.dib`) standardiserade på `Azure.AI.OpenAI` **2.1.0**: lektion 06 och 07
  använder `ChatClient` API:et, lektion 08 använder `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), och
  lektion 09 använder `ImageClient` (`GenerateImage`) med `gpt-image-1`, som ersätter det äldre
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` från `1.0.0-beta.9`.
- **Produktnamnsmodernisering:** "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lektionerna 14, 16, 17) och "Bing" → **Microsoft Copilot** (lektion 12), där dessa refererade till
  aktuella produkter.
- **DevContainer** (`.devcontainer/`) innehåller nu Pylance, Black, Ruff, ESLint, Prettier och Copilot
  tillägg, aktiverar format-on-save och installerar `ruff`, `black`, `mypy` och `pytest` så att CI-
  kontroller kan reproduceras lokalt.
- **Bildgenerering** (lektion 09) rekommenderar `gpt-image-1` för Azure (Azure-katalogen tog bort
  `dall-e-3`).

- **`docs/ENHANCED_FEATURES_ROADMAP.md`** uppdaterad för att återspegla genomfört arbete (API-migrering, CI,
  DevContainer, tester) och aktuella fakta (översättningar produceras automatiskt av
  Azure Co-op Translator; Assistants API har ersatts av Responses API).

### Fikserade

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` returnerar nu en
  tom sträng för inmatning som bara innehåller blanksteg istället för att kasta ett "för kort" fel (i enlighet med
  fallet `None`). Upptäckt och täckt av den nya testsviten.
- **Bildexempel från Lesson 09** — korrigerade verkliga buggar: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  och en variabel som skuggade `openai`-modulen.
- **Lesson 15 RAG notebook** — reparerade klientuppställningen, ersatte den borttagna `DataFrame.append`
  med `pd.concat`, och moderniserade den äldre SDK-användningen.
- Föråldrade / pensionerade modellnamn (`gpt-3.5-turbo`, `gpt-35-turbo`) ersatta med `gpt-4o-mini`
  i aktiva exempel; historiska fine-tuning-resultat i lesson 18 bevarades och annoterades
  istället för att skrivas om.

### Föråldrade / Anmärkningar

- **Microsoft Foundry Models-exempel** som använder `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK:n (`client.complete()`) — `githubmodels-*` och `js-githubmodels`-exemplen och lesson 19, 20,
  och 21 — ligger kvar på Model Inference API:n, som **inte** stödjer Responses API. Dessa är
  medvetet kvar på den SDK:n.
- `AzureOpenAI()` behålls medvetet där det fortfarande är lämpligt (embeddingar och bildgenerering),
  eftersom dessa arbetsflöden inte ingår i Responses API-migreringen.
- Referenser till `text-embedding-ada-002` behålls där en förberäknad embeddingindex är beroende av dem.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->