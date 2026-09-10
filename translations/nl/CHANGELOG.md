# Wijzigingslogboek

Alle opmerkelijke wijzigingen aan het Generative AI for Beginners curriculum zijn in dit bestand gedocumenteerd.

Het formaat is gebaseerd op [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Omdat dit een
leercurriculum is in plaats van een versioned softwarepakket, zijn de entries gegroepeerd op datum.

## [2026-07-16] — Inhoudsvalidatie + Les 09 afbeeldingsassets

### Gewijzigd

- **Les 10 (low-code AI apps):** bijgewerkt twee verouderde `docs.microsoft.com/powerapps/...` Dataverse
  links naar de huidige `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (live gecontroleerd).
- **Les 17 (AI-agenten):** gemoderniseerd een verouderd modelvoorbeeld (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, en Llama 3.3`) en een tijdelijke implementatienaam in het Agent Framework voorbeeld
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Root `README.md`:** toegevoegd de ontbrekende `?WT.mc_id=academic-105485-koreyst` tracking-ID aan de
  *Microsoft for Startups* link.
- **Les 09 afbeeldingsassets** opnieuw gegenereerd met het `gpt-image` model: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, en
  `images/startup.png` (het voor/na voorbeeld van de bewerking werd gemaakt via een echte
  `client.images.edit` oproep met een gegenereerde mask).

### Gevalideerd

- Gecontroleerd de README’s van lessen 01, 03, 05, 12, 14, en 16 — allen actueel (correcte Microsoft Foundry
  naamgevingen en links); geen wijzigingen nodig.
- Uitgevoerd een volledige markdownvalidatie door alle 41 in-repo markdownbestanden (vertalingen uitgezonderd) voor
  verouderde documentpaden, `/en-us/` Microsoft locale, verouderde product/modelnamen, ontbrekende tracking
  ID’s, en kapotte relatieve links/afbeeldingen. Alleen de enkele *Microsoft for Startups* tracking-ID lag toe
  actie; alle andere meldingen bleken false positives (automatisch gegenereerde vertalingslinks,
  uitge-commentarieerde tijdelijke aanduidingen, en derde partij `/en/` structurele URL’s).

## [2026-07-15] — Les 09 (Afbeeldingstoepassingen) herschreven voor GPT afbeeldingsmodellen

### Gewijzigd

- **Herschreven les 09 "Bouwen van afbeeldingsgeneratie toepassingen"** rond de huidige **`gpt-image`**
  model familie (standaard **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` ook GA), ter vervanging van de
  legacy DALL·E 2/3 inhoud. Belangrijke correcties:
  - `gpt-image` modellen geven de afbeelding terug als **base64 (`b64_json`)**, niet als een URL. Alle voorbeelden bijgewerkt naar
    `base64.b64decode(...)` in plaats van een `url` te downloaden met `requests`.
  - De API-versie voor afbeeldingen verhoogd naar `2025-04-01-preview`.
  - De gefabriceerde "temperatuur" sectie verwijderd (beeldmodellen gebruiken geen `temperature`) en de
    DALL·E-2-only image **variaties** inhoud vervangen door een **afbeeldingsbewerking** (masker/inpainting) sectie.
  - `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, beide
    opdrachtennotebooks (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), en de .NET `.dib` notebook bijgewerkt.

### Verwijderd

- Verwijderd de verouderde `python/aoai-app-variation.py` en `python/oai-app-variation.py` voorbeelden
  (`images.create_variation` is alleen DALL·E-2 en wordt niet ondersteund door `gpt-image`).
- Verwijderd 4 verweesde afbeeldingsassets die gekoppeld waren aan de verwijderde temperatuurvergelijkingssectie
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Verwijderd de onnodige `requests` afhankelijkheid uit de Python voorbeelden en requirements van de les.

### Gevalideerd

- `aoai-app.py` end-to-end uitgevoerd tegen een gedeployd `gpt-image-1.5` model en bevestigd dat de base64
  decodeer/save flow een PNG produceert. Notebooks bevestigd valide JSON.

## [2026-07-14] — Standaard Model Update + Redeneringsmodel Richtlijnen

### Gewijzigd

- **Standaard chatmodel `gpt-4o-mini` → `gpt-5-mini`** door het hele curriculum in uitvoerbare voorbeelden,
  documentatie en configuratie. Dit is gedreven door de modellenlevenscyclusstatus: op Microsoft Foundry,
  `gpt-4o-mini` (met pensioen per 2026-10-01) en de gehele `gpt-4.1` familie (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, pensioen per 2026-10-14) zijn **Verouderend**, terwijl de **GPT-5 familie
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) algemeen beschikbaar is** (pensioen per 2027-02-06). Bijgewerkt:
  - `.env.copy`, `00-course-setup/03-providers.md` (aanbevolen deployment en `az cognitiveservices`
    deploy commando’s), en de README’s voor lessen 04, 06, 07, en 15.
  - Python voorbeelden in les 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) en scripts van les 08.
  - TypeScript / JavaScript voorbeelden in lessen 06, 07, en 11, en de `.dib` .NET notebooks voor
    lessen 06 en 07.
  - Opdrachtennotebooks in lessen 04, 06, 07, en 11 (codecellen), plus `shared/python/api_utils.py`
    docstringvoorbeelden.
- **Richtlijnen voor reasoning-model parameters (nieuw).** `gpt-5-mini` is een *reasoning* model: het ondersteunt **geen**
  `temperature`/`top_p`, en gebruikt `max_completion_tokens` (chatcompletions) /
  `max_output_tokens` (Responses API) in plaats van `max_tokens`. Dienovereenkomstig:
  - Verwijderd `temperature`/`top_p`/`max_tokens` uit voorbeelden die nu standaard `gpt-5-mini` gebruiken
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, les 15 RAG README).
  - Toegevoegd een **"Reasoning modellen gebruiken geen `temperature`"** opmerking aan les 06, met uitleg dat
    reasoning modellen worden gestuurd met **prompt engineering + reasoning controls** in plaats van
    sampleknoppen, terwijl `temperature`/`top_p` geldig blijven op niet-reasoning modellen
    (GPT-4.x, Mistral, Llama, Phi, open modellen).
- **`gpt-5-mini` wordt niet gebruikt voor de fine-tuning tutorial (les 18).** GPT-5 ondersteunt alleen
  versterkte fine-tuning (RFT); de les 18 supervised fine-tuning (SFT) walkthrough gebruikt
  `gpt-4.1-mini`, dat SFT/DPO ondersteunt.
- **Temperatuur demos gebruiken een Llama model.** Om `temperature` te blijven onderwijzen (wat reasoning modellen
  weigeren), wordt een `Llama-3.3-70B-Instruct` model gebruikt via de Foundry Models endpoint. Toegevoegd een nieuwe
  `AZURE_INFERENCE_CHAT_MODEL` variabele aan `.env.copy`; de les 04/06 `githubmodels` notebooks en
  de `06` `js-githubmodels` voorbeeld lezen deze in (met fallback naar `Llama-3.3-70B-Instruct`) en behouden hun
  `temperature`/`top_p`/`max_tokens` demo’s.
- **JS / .NET voorbeelden bijgewerkt voor GPT-5.** Verwijderd `temperature`/`top_p`/`max_tokens` uit de GPT-5
  voorbeelden (`06` `recipe-app` TypeScript, `06` `.dib` .NET - dat ook `MaxOutputTokenCount` verhoogt
  zodat reasoning output niet wordt afgebroken). Het `06` `js-githubmodels` voorbeeld gebruikt nu Llama om zijn
  temperatuur demo te behouden. De `.dib` geeft aan dat `Azure.AI.Inference` + een Llama model de manier is om
  `Temperature` in .NET te demonstreren.
- `gpt-4o-mini` / `gpt-5-mini` op hun plek gelaten waar ze nog accuraat zijn: `tiktoken` token-encoding
  verwijzingen, modelcatalogus beschikbaarheidslijsten, en les 02 spraakmodellen (`gpt-4o-transcribe`).
- Les 20 (Mistral) en 21 (Meta) voorbeelden behouden `temperature`/`max_tokens` omdat zij gericht zijn
  op Mistral/Llama modellen, die deze parameters ondersteunen.

## [2026-07-06] — Inhoudsmodernisering Vernieuwing

Een brede vernieuwing om het curriculum accuraat te houden voor 2026: moderne API’s, actuele productnamen en
modelnamen, bijgewerkte providerrichtlijnen en nieuwe tooling voor ontwikkelaarservaring.

### Toegevoegd

- **Microsoft Agent Framework** sectie in les `17-ai-agents` die single chat agenten behandelt,
  tools/function calling, Azure OpenAI (Microsoft Foundry) configuratie, en multi-agent
  workflow orkestratie (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** gedocumenteerd als een offline / on-device provider (naast Ollama) in
  `00-course-setup/03-providers.md` en les `19-slm`.
- **Continuous integration workflows**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (afgedwongen op de onderhouden `shared/`
    module, advies over de rest van het curriculum), een adviserende ESLint run, en een pytest taak.
  - `.github/workflows/security.yml` — CodeQL analyse (Python + JavaScript/TypeScript) en
    dependency review bij pull requests.
- **Testsuite** onder `tests/` — 41 pytest tests die de gedeelde utiliteitsmodule dekken.
- **Azure OpenAI → Responses API migratievaardigheid** onder
  `.github/skills/azure-openai-to-responses/` gebruikt om de API migratie te begeleiden.

### Gewijzigd

- **Chat Completions API → Responses API** door alle Python en TypeScript chatvoorbeelden
  (`client.responses.create(...)` → `response.output_text`), inclusief lessen 04, 06, 07, 11,
  15, en 18, plus hun README’s.
- **GitHub Models → Microsoft Foundry Models** in gehele proza, links en voorbeelden. GitHub Models
  stopt eind juli 2026; voorbeelden verwijzen nu naar de Microsoft Foundry modelcatalogus en gebruiken
  de `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL` omgevingsvariabelen.
- **`.env.copy`, `AGENTS.md`, en provider docs** bijgewerkt om aan te geven dat Azure OpenAI nu onderdeel is
  van Microsoft Foundry, en de standaard API-versie verhoogd naar `2024-10-21`.
- **TypeScript voorbeelden** (lessen 06, 07, 08, 11) gemigreerd van het verouderde `@azure/openai`
  beta SDK naar het `openai` pakket (chatapps gebruiken de Responses API; de zoekapp gebruikt de
  embeddings client).
- **.NET notebooks** (`dotnet/*.dib`) gestandaardiseerd op `Azure.AI.OpenAI` **2.1.0**: lessen 06 en 07
  gebruiken de `ChatClient` API, les 08 gebruikt `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), en
  les 09 gebruikt `ImageClient` (`GenerateImage`) met `gpt-image-1`, ter vervanging van de legacy
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` van `1.0.0-beta.9`.
- **Productnaam modernisering**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lessen 14, 16, 17) en "Bing" → **Microsoft Copilot** (les 12), waar deze verwezen naar de
  huidige producten.
- **DevContainer** (`.devcontainer/`) levert nu Pylance, Black, Ruff, ESLint, Prettier, en Copilot
  extensies, schakelt format-on-save in, en installeert `ruff`, `black`, `mypy`, en `pytest` zodat de CI
  checks lokaal nagebootst kunnen worden.
- **Afbeeldingsgeneratie** (les 09) beveelt `gpt-image-1` aan voor Azure (de Azure catalogus heeft
  `dall-e-3` verwijderd).

- **`docs/ENHANCED_FEATURES_ROADMAP.md`** bijgewerkt om voltooid werk weer te geven (API-migratie, CI,
  DevContainer, tests) en huidige feiten (vertalingen worden automatisch geproduceerd door de
  Azure Co-op Translator; de Assistants API is vervangen door de Responses API).

### Gerepareerd

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` retourneert nu een
  lege string voor invoer die alleen uit witruimte bestaat in plaats van een "te kort" fout te geven (consitent met het
  `None` geval). Gevonden en gedekt door de nieuwe testsuite.
- **Afbeeldingsvoorbeelden les 09** — echte bugs gecorrigeerd: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  en een variabele die het `openai` module overschaduwde.
- **Les 15 RAG notebook** — client setup gerepareerd, de verwijderde `DataFrame.append` vervangen
  door `pd.concat`, en het oude SDK-gebruik gemoderniseerd.
- Verouderde / gepensioneerde modelnamen (`gpt-3.5-turbo`, `gpt-35-turbo`) vervangen door `gpt-4o-mini`
  in actieve voorbeelden; historische fine-tuning resultaten in les 18 zijn bewaard en
  geannoteerd in plaats van herschreven.

### Verouderd / Opmerkingen

- **Microsoft Foundry Models voorbeelden** die de `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) gebruiken — de `githubmodels-*` en `js-githubmodels` voorbeelden en lessen 19, 20,
  en 21 — blijven op de Model Inference API, welke **niet** de Responses API ondersteunt. Deze zijn
  opzettelijk op die SDK gelaten.
- `AzureOpenAI()` wordt opzettelijk behouden waar nog gepast (embeddings en beeldgeneratie),
  omdat die workflows geen deel uitmaken van de Responses API migratie.
- Verwijzingen naar `text-embedding-ada-002` worden behouden waar een voorgecalculeerde embedding index ervan afhangt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->