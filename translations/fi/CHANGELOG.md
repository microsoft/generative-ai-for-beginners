# Muutosloki

Kaikki merkittävät muutokset Generative AI for Beginners -oppimateriaaliin on dokumentoitu tässä tiedostossa.

Muoto perustuu [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Koska kyseessä on
oppimateriaali, ei versioitu ohjelmistopaketti, merkinnät on ryhmitelty päivämäärän mukaan.

## [2026-07-16] — Sisällön tarkistus + Oppitunti 09 Kuvavarasto

### Muutettu

- **Oppitunti 10 (low-code AI sovellukset):** päivitettiin kaksi vanhentunutta `docs.microsoft.com/powerapps/...` Dataverse
  linkkiä nykyiseen `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (varmistettu toimivaksi).
- **Oppitunti 17 (AI agentit):** uudistettiin vanhentunut malliesimerkki (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) ja paikanvarausnimi Agent Framework -näytteessä
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Juuri `README.md`:** lisättiin puuttuva `?WT.mc_id=academic-105485-koreyst` seurantatunnus
  *Microsoft for Startups* -linkkiin.
- **Oppitunti 09 kuvavarastot** luotiin uudelleen `gpt-image` mallilla: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, ja
  `images/startup.png` (muokkausesimerkin ennen/jälkeen pari tuotettiin oikealla
  `client.images.edit` -kutsulla ja generoidulla maskilla).

### Vahvistettu

- Tarkistettiin oppituntien 01, 03, 05, 12, 14 ja 16 README-tiedostot — kaikki ajan tasalla (oikeat Microsoft Foundryn
  nimet ja linkit); muutoksia ei tarvittu.
- Suoritettiin täydellinen markdownin tarkistus kaikissa 41 repossa olevassa markdown-tiedostossa (käännökset pois lukien)
  vanhentuneiden dokumenttipolkujen, `/en-us/` Microsoft paikallisten, vanhentuneiden tuote-/mallinimien,
  puuttuvien seurantatunnusten ja rikkinäisten suhteellisten linkkien/kuvien varalta. Ainoastaan *Microsoft for Startups* seurantatunnuksen puutos oli
  korjattava; muut havainnot olivat virheellisiä (automaattisesti luodut käännöslinkit,
  kommentoidut paikanvaraukset ja kolmannen osapuolen `/en/` rakenteelliset URLit).

## [2026-07-15] — Oppitunti 09 (Kuvakäyttöliittymät) Uudelleen kirjoitus GPT Image -malleille

### Muutettu

- **Kirjoitettiin oppitunti 09 "Kuvageneraattorisovellusten rakentaminen" uudelleen** nykyisen **`gpt-image`**
  malliperheen ympärille (oletus **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` myös yleisesti saatavilla), korvaten
  vanhan DALL·E 2/3 sisällön. Keskeiset korjaukset:
  - `gpt-image` mallit palauttavat kuvan **base64 (`b64_json`)** muodossa, eivät URL-osoitteena. Kaikki esimerkit päivitettiin
    käyttämään `base64.b64decode(...)` lataamisen sijaan `url` kanssa `requests`-kirjastolla.
  - Kuvan API versio nostettiin `2025-04-01-preview`.
  - Poistettiin keksitty "lämpötila" osio (kuvamallit eivät käytä `temperature`) ja korvattiin vain DALL·E-2 kuvien **muunnelmat** osio
    **kuvamuokkauksella** (maski/maalaus).
  - Päivitettiin `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, molemmat
    tehtävämuistikirjat (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`) ja .NET `.dib` muistikirja.

### Poistettu

- Poistettu vanhentuneet `python/aoai-app-variation.py` ja `python/oai-app-variation.py` esimerkit
  (`images.create_variation` toimii vain DALL·E-2:ssa ja ei ole `gpt-image` mallien tukema).
- Poistettu 4 irtonaista kuvavaraistoa, jotka liittyivät poistettuun lämpötilan vertailuosioon
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Poistettu tarpeeton `requests` riippuvuus Python-esimerkeistä ja vaatimuksista.

### Vahvistettu

- Ajettiin `aoai-app.py` päältä loppuun käyttämällä käyttöön otettua `gpt-image-1.5` mallia ja
  varmennettiin base64 purku/talletus tuottaa PNG:n. Muistikirjat vahvistettiin kelvollisiksi JSON-tiedostoiksi.

## [2026-07-14] — Oletusmallin päivitys + Päättelymallin ohjeistus

### Muutettu

- **Oletuskeskustelumalli `gpt-4o-mini` → `gpt-5-mini`** kaikissa kurssin ajettavissa esimerkeissä,
  dokumentaatiossa ja konfiguraatiossa. Muutos johtui mallin elinkaaren tilasta: Microsoft Foundryssa,
  `gpt-4o-mini` (eläköityy 2026-10-01) ja koko `gpt-4.1` perhe (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, eläköityy 2026-10-14) ovat **Eläkkeelle siirtymässä**, kun taas **GPT-5 perhe
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) on Yleisesti saatavilla** (eläköityy 2027-02-06). Päivitettiin:
  - `.env.copy`, `00-course-setup/03-providers.md` (suositellut käyttöönotot ja `az cognitiveservices`
    deploy-komennot), sekä oppituntien 04, 06, 07 ja 15 README:t.
  - Python-esimerkit oppitunnilla 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) ja oppitunnin 08 skriptit.
  - TypeScript / JavaScript-esimerkit oppitunneilla 06, 07 ja 11, sekä `.dib` .NET muistikirjat
    oppitunneilla 06 ja 07.
  - Tehtävämuistikirjat oppitunneilla 04, 06, 07 ja 11 (koodisolut), sekä `shared/python/api_utils.py`
    dokumentaation esimerkit.
- **Päättelymallin parametriohjeistus (uusi).** `gpt-5-mini` on *päättely*-malli: se EI tue
  `temperature`/`top_p` ja käyttää `max_completion_tokens` (chat-kompletiot) /
  `max_output_tokens` (Responses API) sijasta `max_tokens`. Tämän mukaisesti:
  - Poistettiin `temperature`/`top_p`/`max_tokens` esimerkeistä, jotka nyt käyttävät `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, oppitunti 15 RAG README).
  - Lisättiin **"Päättelymallit eivät käytä `temperature`-parametria"** huomautus oppitunnille 06, jossa
    selitetään, että päättelymalleja ohjataan **kehotteen suunnittelulla + päättelyn ohjauksilla** eikä
    otannankytkimillä, kun taas `temperature`/`top_p` ovat edelleen voimassa ei-päättelymalleilla
    (GPT-4.x, Mistral, Llama, Phi, avoimet mallit).
- **`gpt-5-mini` ei ole käytössä hienosäätöoppaassa (oppitunti 18).** GPT-5 tukee vain
  vahvistettua hienosäätöä (RFT); oppitunnin 18 valvottu hienosäätö (SFT) käyttää edelleen
  `gpt-4.1-mini`:ä, joka tukee SFT/DPO:ta.
- **Lämpötilademot käyttävät Llama-mallia.** Opetuksen ylläpitämiseksi `temperature`-parametrin käyttö (jota päättelymallit
  hylkäävät), käytetään `Llama-3.3-70B-Instruct` mallia Foundry Models -rajapinnan kautta. Lisättiin uusi
  `AZURE_INFERENCE_CHAT_MODEL` muuttuja `.env.copy` tiedostoon; opetuksen 04/06 `githubmodels` muistikirjat ja
  `06` `js-githubmodels` esimerkki lukevat sitä (palautuen `Llama-3.3-70B-Instruct`:iin) ja säilyttävät
  `temperature`/`top_p`/`max_tokens` demonsa.
- **JS / .NET esimerkit päivitettiin GPT-5:lle.** Poistettiin `temperature`/`top_p`/`max_tokens` GPT-5:
  sta esimerkeistä (`06` `recipe-app` TypeScript, `06` `.dib` .NET - joka nostaa myös `MaxOutputTokenCount`
  rajoittaakseen päättelyn katkeamisen). `06` `js-githubmodels` esimerkki käyttää nyt Llamaa säilyttääkseen
  lämpötilademonsa. `.dib`-muistikirjassa todetaan, että `Azure.AI.Inference` + Llama-malli on tapa
  demonstroida `Temperature` käytön .NET ympäristössä.
- Jätettiin `gpt-4o-mini` / `gpt-5-mini` paikoilleen paikoissa, joissa ne ovat yhä ajantasaisia: `tiktoken` token-koodausta
  koskevat viitteet, malliluettelon saatavuuslistat ja oppitunti 02 puhemallit (`gpt-4o-transcribe`).
- Oppituntien 20 (Mistral) ja 21 (Meta) esimerkit säilyttävät `temperature`/`max_tokens`, koska ne kohdistuvat
  Mistral/Llama malleihin, jotka tukevat näitä parametreja.

## [2026-07-06] — Sisällön modernisointipäivitys

Laaja päivitys kurssin ajantasaisuuden ylläpitämiseksi vuodelle 2026: modernit rajapinnat, ajantasaiset tuote- ja
mallinimet, päivitetyt tarjoajaohjeet ja uudet kehittäjäkokemuksen työkalut.

### Lisätty

- **Microsoft Agent Framework** osio oppitunnille `17-ai-agentit`, kattaa yksittäiset chat-agentit,
  työkalujen/funktioiden kutsun, Azure OpenAI (Microsoft Foundry) konfiguraation ja moniagenttien
  työnkulkujen orkestroinnin (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** dokumentoitu offline / paikallisena tarjoajana (Ollaman rinnalla) tiedostossa
  `00-course-setup/03-providers.md` ja oppitunnilla `19-slm`.
- **Jatkuvan integraation työnkulut**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (pakollinen ylläpidetylle `shared/`
    moduulille, muille kurssin osille on neuvova ESLint-tarkistus sekä pytest-tehtävä).
  - `.github/workflows/security.yml` — CodeQL analyysi (Python + JavaScript/TypeScript) ja
    riippuvuuskatselmointi vedä-pyyntöihin.
- **Testisalkku** hakemistossa `tests/` — 41 pytest-testiä, jotka kattavat jaetun apumoduulin.
- **Azure OpenAI → Responses API siirtotaito** hakemistossa
  `.github/skills/azure-openai-to-responses/`, joka ohjaa API-migraatiota.

### Muutettu

- **Chat Completions API → Responses API** kaikissa Python- ja TypeScript-chat-esimerkeissä
  (`client.responses.create(...)` → `response.output_text`), mukaan lukien oppitunnit 04, 06, 07, 11,
  15 ja 18, sekä niiden README:t.
- **GitHub Models → Microsoft Foundry Models** kaikessa tekstissä, linkeissä ja esimerkeissä. GitHub Models
  eläköityy heinäkuun 2026 lopussa; esimerkit osoittavat nyt Microsoft Foundryn malliluetteloon ja käyttävät
  ympäristömuuttujia `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` ja tarjoajadokumentaatio** päivitettiin heijastamaan, että Azure OpenAI on nyt osa
  Microsoft Foundrya, ja oletus API-versio nostettiin `2024-10-21`.
- **TypeScript esimerkit** (oppitunnit 06, 07, 08, 11) siirrettiin pois vanhentuneesta `@azure/openai`
  beta SDK:sta `openai` pakettiin (chat-sovellukset käyttävät Responses API:a; hakusovellus käyttää
  embeddings-kirjastoa).
- **.NET muistikirjat** (`dotnet/*.dib`) yhdenmukaistettiin käyttämään `Azure.AI.OpenAI` **2.1.0**: oppitunnit 06 ja 07
  käyttävät `ChatClient` API:a, oppitunti 08 käyttää `EmbeddingClient`-luokkaa (`GenerateEmbedding` / `ToFloats`), ja
  oppitunti 09 käyttää `ImageClient` -luokkaa (`GenerateImage`) mallilla `gpt-image-1`, korvaten vanhan
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` version `1.0.0-beta.9`.
- **Tuotenimien modernisointi:** "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (oppitunnit 14, 16, 17) ja "Bing" → **Microsoft Copilot** (oppitunti 12), kun ne viittasivat
  nykyisiin tuotteisiin.
- **DevContainer** (`.devcontainer/`) sisältää nyt Pylance, Black, Ruff, ESLint, Prettier ja Copilot
  laajennukset, sallii tallennettaessa muotoilun ja asentaa `ruff`, `black`, `mypy` ja `pytest` jotta CI
  tarkistukset voi toistaa paikallisesti.
- **Kuvagenerointi** (oppitunti 09) suosittelee `gpt-image-1`:ä Azurelle (Azure luettelo poisti
  `dall-e-3`).

- **`docs/ENHANCED_FEATURES_ROADMAP.md`** päivitetty heijastamaan valmistuneita töitä (API-migraatio, CI,
  DevContainer, testit) ja nykyisiä faktoja (käännökset tuotetaan automaattisesti Azure Co-op Translatorin
  toimesta; Assistants API on korvattu Responses API:lla).

### Korjattu

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` palauttaa nyt
  tyhjän merkkijonon pelkkiä välilyöntejä sisältävälle syötteelle sen sijaan, että antaisi "liian lyhyt" -virheen
  (yhteneväinen `None`-tapauksen kanssa). Löydetty ja katettu uudella testikattavuudella.
- **Lesson 09 kuvanäytteet** — korjattiin oikeat virheet: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  ja muuttuja, joka varjosti `openai`-moduulia.
- **Lesson 15 RAG -muistikirja** — korjattiin clientin asetukset, korvattiin poistettu `DataFrame.append`
  `pd.concat`illa ja modernisoitiin vanhaa SDK:n käyttöä.
- Vanhentuneet / luopuneet mallinimet (`gpt-3.5-turbo`, `gpt-35-turbo`) korvattiin `gpt-4o-mini`
  aktiivisissa näytteissä; historian hienosäätötulokset opetus 18:lla säilytettiin ja niihin lisättiin
  kommentteja uudelleenkirjoituksen sijaan.

### Vanhentuneet / Huomautuksia

- **Microsoft Foundry Models -näytteet**, jotka käyttävät `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK:ta (`client.complete()`) — `githubmodels-*` ja `js-githubmodels` näytteet sekä opetus 19, 20,
  ja 21 — pysyvät Model Inference API:ssa, joka **ei** tue Responses API:ta. Nämä on
  tarkoituksella jätetty tälle SDK:lle.
- `AzureOpenAI()` on tarkoituksella säilytetty siellä, missä se on edelleen sopiva (upotukset ja kuvanluonti),
  koska nämä työnkulut eivät kuulu Responses API -migraatioon.
- `text-embedding-ada-002` viittaukset pidetään siellä, missä esilaskettu upotusindeksi riippuu niistä.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->