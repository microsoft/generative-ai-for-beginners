# Muutosloki

Kaikki Generative AI for Beginners -oppimateriaalin merkittävät muutokset on dokumentoitu tässä tiedostossa.

Muoto perustuu [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Koska kyseessä on
oppimateriaali eikä versioitu ohjelmistopaketti, merkinnät on ryhmitelty päivämäärän mukaan.

## [2026-07-06] — Sisällön modernisointipäivitys

Laaja päivitys, jolla kurssi pidetään ajan tasalla vuodelle 2026: nykyaikaiset API:t, nykyiset tuotemerkit ja
mallinimet, päivitetyt tarjoajaohjeet ja uudet kehittäjäkokemustyökalut.

### Lisätty

- **Microsoft Agent Framework** -osio oppitunnissa `17-ai-agents` kattaa yksittäiset chat-agentit,
  työkalut/funktiokutsut, Azure OpenAI (Microsoft Foundry) -konfiguraation sekä monen agentin
  työnkulun orkestroinnin (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** dokumentoitu offline- / laitteella suoritettavana tarjoajana (Ollaman ohella) tiedostoissa
  `00-course-setup/03-providers.md` ja oppitunnissa `19-slm`.
- **Jatkuvat integraatiotyönkulut**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (pakollinen ylläpidetyssä `shared/`
    moduulissa, suositus muualla materiaalissa), suositteleva ESLint-käynti ja pytest-tehtävä.
  - `.github/workflows/security.yml` — CodeQL-analyysi (Python + JavaScript/TypeScript) ja
    riippuvuustarkistus pull requesteissa.
- **Testipaketti** hakemistossa `tests/` — 41 pytest-testiä kattavat yhteistä apumoduulia.
- **Azure OpenAI → Responses API -migrointitaito** kansiossa
  `.github/skills/azure-openai-to-responses/`, jota käytetään API-siirtymän ohjaamiseen.

### Muutettu

- **Chat Completions API → Responses API** kaikissa Python- ja TypeScript-chat-esimerkeissä
  (`client.responses.create(...)` → `response.output_text`), mukaan lukien oppitunnit 04, 06, 07, 11,
  15 ja 18 sekä niiden README-tiedostot.
- **GitHub Models → Microsoft Foundry Models** kauttaaltaan tekstissä, linkeissä ja esimerkeissä. GitHub Models
  poistuu käytöstä heinäkuun 2026 lopussa; esimerkit osoittavat nyt Microsoft Foundryn malliluetteloon ja
  käyttävät ympäristömuuttujia `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` ja tarjoajien dokumentaatio** päivitetty vastaamaan, että Azure OpenAI on nyt osa
  Microsoft Foundrya, ja oletus API-versio nostettu versioon `2024-10-21`.
- **TypeScript-esimerkit** (oppitunnit 06, 07, 08, 11) siirretty pois vanhentuneesta `@azure/openai`
  beta SDK:sta `openai`-pakettiin (chat-sovellukset käyttävät Responses APIa; hakusovellus käyttää
  embeddings-asiakasta).
- **.NET-muistikirjat** (`dotnet/*.dib`) standardoitu `Azure.AI.OpenAI` versioon **2.1.0**: oppitunnit 06 ja 07
  käyttävät `ChatClient` APIa, oppitunti 08 käyttää `EmbeddingClient`ia (`GenerateEmbedding` / `ToFloats`),
  ja oppitunti 09 käyttää `ImageClient`ia (`GenerateImage`) mallilla `gpt-image-1`, korvaten vanhan
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` version `1.0.0-beta.9`.
- **Tuotemerkkien modernisointi**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (oppitunnit 14, 16, 17) ja "Bing" → **Microsoft Copilot** (oppitunti 12), missä nämä viitsivät
  nykyisiin tuotteisiin.
- **DevContainer** (`.devcontainer/`) sisältää nyt Pylance-, Black-, Ruff-, ESLint-, Prettier- ja Copilot-
  laajennukset, sallii automaattisen tallennuksen yhteydessä suoritettavan muotoilun ja asentaa `ruff`-, `black`-,
  `mypy`- ja `pytest`-työkalut, jotta CI-tarkistukset voidaan toistaa paikallisesti.
- **Kuvageneraattorin käyttö** (oppitunti 09) suosittelee Azurelle mallia `gpt-image-1` (Azure-katalogista
  on poistettu `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** päivitetty heijastamaan tehdyt työt (API-siirtymä, CI,
  DevContainer, testit) ja nykyiset tosiasiat (käännökset tuotetaan automaattisesti Azure Co-op Translatorilla;
  Assistants API on korvattu Responses APIlla).

### Korjattu

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` palauttaa nyt
  tyhjän merkkijonon pelkkää välilyöntiä sisältävän syötteen kohdalla sen sijaan, että heittäisi "liian lyhyt" virheen
  (yhdenmukainen `None`-tapauksen kanssa). Löytyi ja testattiin uudella testipaketilla.
- **Oppitunti 09 kuvasamplet** — korjattiin todelliset virheet: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  sekä muuttuja, joka varjosti `openai`-moduulia.
- **Oppitunti 15 RAG-muistikirja** — korjattiin asiakasasetukset, korvattiin poistettu `DataFrame.append`
  komento `pd.concat`illa ja modernisoitiin vanhaa SDK:n käyttöä.
- Vanhenneet / poistuneet mallinimet (`gpt-3.5-turbo`, `gpt-35-turbo`) korvattu mallilla `gpt-4o-mini`
  aktiivisissa esimerkeissä; oppitunnin 18 historialliset hienosäätöjen tulokset säilytettiin ja merkittiin
  sen sijaan, että kirjoitettiin uudelleen.

### Vanhentuneet / Huomautukset

- **Microsoft Foundry Models -esimerkit**, jotka käyttävät `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK:ta (`client.complete()`) — `githubmodels-*` ja `js-githubmodels` esimerkit sekä oppitunnit 19, 20,
  ja 21 — pysyvät Model Inference API:ssa, joka **ei** tue Responses API:a. Nämä on
  tarkoituksella jätetty kyseiselle SDK:lle.
- `AzureOpenAI()` pidetään tarkoituksella käytössä siellä, missä se on vielä sopiva (embeddings ja kuvagenerointi),
  koska nämä työnkulut eivät kuulu Responses API:n siirtymään.
- `text-embedding-ada-002` viittaukset säilytetään siellä, missä niihin perustuu valmiiksi laskettu embedding-indeksi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->