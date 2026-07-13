# Parannettujen ominaisuuksien ja kehityssuunnitelman tiekartta

Tämä asiakirja kuvaa suositeltuja parannuksia ja kehitysehdotuksia Generative AI for Beginners -opetussuunnitelmaan, perustuen kattavaan koodin tarkastukseen ja alan parhaiden käytäntöjen analyysiin.

## Tiivistelmä

Koodikanta on analysoitu turvallisuuden, koodin laadun ja opetuksellisen tehokkuuden näkökulmasta. Tämä asiakirja tarjoaa suosituksia välittömistä korjauksista, lähiajan parannuksista ja tulevista kehityksistä.

---

## 1. Turvallisuuden parannukset (Prioriteetti: Kriittinen)

### 1.1 Välittömät korjaukset (Valmiit)

| Ongelma | Vaikuttavat tiedostot | Tila |
|-------|----------------|--------|
| Koodiin kirjoitettu SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Korjattu |
| Puuttuva ympäristömuuttujien validointi | Useita JS/TS-tiedostoja | Korjattu |
| Turvattomat funktiokutsut | `11-integrating-with-function-calling/js-githubmodels/app.js` | Korjattu |
| Tiedostokahvojen vuoto | `08-building-search-applications/scripts/` | Korjattu |
| Puuttuvat pyynnön aikakatkaisut | `09-building-image-applications/python/` | Korjattu |

### 1.2 Suositellut lisäturvallisuusominaisuudet

1. **Rajoitusesimerkit**
   - Lisää esimerkkikoodi, joka näyttää kuinka toteuttaa rajoitus API-kutsuissa
   - Havainnollista eksponentiaalinen palautuskäyttäytyminen

2. **API-avaimen kierto**
   - Lisää dokumentaatio parhaista käytännöistä API-avainten kiertoon
   - Sisällytä esimerkkejä Azure Key Vaultin tai vastaavien palveluiden käytöstä

3. **Sisällön turvallisuuden integrointi**
   - Lisää esimerkkejä Azure Content Safety API:sta
   - Havainnollista syötteen ja tuloksen moderointimalleja

---

## 2. Koodin laadun parannukset

### 2.1 Konfiguraatiotiedostot lisätty

| Tiedosto | Tarkoitus |
|------|---------|
| `.eslintrc.json` | JavaScript/TypeScript-linttausasetukset |
| `.prettierrc` | Koodin muotoilun standardit |
| `pyproject.toml` | Python-työkalujen konfiguraatio (Black, Ruff, mypy) |

### 2.2 Jaetut apuohjelmat luotu

Uusi `shared/python/` -moduuli sisältää:
- `env_utils.py` - Ympäristömuuttujien käsittely
- `input_validation.py` - Syötteiden validointi ja puhdistus
- `api_utils.py` - Turvalliset API-pyyntöjen rullaukset

### 2.3 Suositellut koodin parannukset

1. **Tyyppivihjeiden kattavuus**
   - Lisää tyyppivihjeet kaikkiin Python-tiedostoihin
   - Ota käyttöön tiukka TypeScript-tila kaikissa TS-projekteissa

2. **Dokumentointistandardit**
   - Lisää docstringit kaikkiin Python-funktioihin
   - Lisää JSDoc-kommentit kaikkiin JavaScript/TypeScript-funktioihin

3. **Testauskehys**
   - Lisää pytest-asetukset ja esimerkkitestit _(valmiina: pytest-asetus `pyproject.toml`-tiedostossa; esimerkkitestit jaetuille apuohjelmille [`tests/`](../../../tests) -hakemistossa, joita ajaa CI)_
   - Lisää Jest-konfiguraatio JavaScript/TypeScriptille

---

## 3. Opetukselliset parannukset

### 3.1 Uudet oppituntien aiheet

1. **Turvallisuus tekoälysovelluksissa** (Ehdotettu oppitunti 22)
   - Kehoteinjektiohyökkäykset ja suojaukset
   - API-avainten hallinta
   - Sisällön moderointi
   - Rajoitus ja väärinkäytön ehkäisy

2. **Tuotantoon käyttöönotto** (Ehdotettu oppitunti 23)
   - Kontitus Dockerilla
   - CI/CD-putket
   - Monitorointi ja lokitus
   - Kustannusten hallinta

3. **Edistyneet RAG-tekniikat** (Ehdotettu oppitunti 24)
   - Hybridihaku (avainsanat + semanttinen)
   - Uudelleenjärjestelystrategiat
   - Monimodaalinen RAG
   - Arviointimittarit

### 3.2 Nykyisten oppituntien parannukset

| Oppitunti | Suositeltu parannus |
|--------|------------------------|
| 06 - Tekstintuotanto | Lisää suoravirtauksen esimerkit |
| 07 - Chat-sovellukset | Lisää keskustelumuistin mallit |
| 08 - Hakusovellukset | Lisää vektoripohjaisten tietokantojen vertailu |
| 09 - Kuvantuotanto | Lisää kuvan muokkaus/variaatioesimerkit |
| 11 - Funktiokutsut | Lisää rinnakkaiset funktiokutsut |
| 15 - RAG | Lisää pilkkomisstrategian vertailu |
| 17 - Tekoälyagentit | Lisää moni-agenttien orkestrointi |

---

## 4. API:n modernisointi

### 4.1 Vanhentuneet API-kuviot (Migraatio valmis)

Kaikki Python- ja TypeScript-chat-esimerkit on muunnettu Chat Completions APIsta Responses APIin (`client.responses.create(...)` → `response.output_text`).

| Vanha kuvio | Uusi kuvio | Tila |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Valmis |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Valmis |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai` paketti `client.responses.create()` → `response.output_text` | Valmis |
| `df.append()` (pandas) | `pd.concat()` | Valmis |

> **Huom:** Microsoft Foundry Models -esimerkit, jotka käyttävät `azure-ai-inference` / `@azure-rest/ai-inference` SDK:ta (`client.complete()`), pysyvät Model Inference API:ssa, joka ei tue Responses APIa. `AzureOpenAI()` pidetään tarkoituksella siellä missä se edelleen on voimassa (embeddings ja kuvantuotanto).

### 4.2 Uudet API-ominaisuudet esitettäväksi

1. **Rakenteelliset vastaukset** (OpenAI)
   - JSON-tila
   - Funktiokutsut tiukkojen skeemojen kanssa

2. **Näkökyvyt**
   - Kuvanalyysi GPT-4o (vision) avulla
   - Monimodaaliset kehoteet

3. **Responses API:n sisäänrakennetut työkalut** (korvaa vanhan Assistants API:n)
   - Koodin tulkki
   - Tiedostohaku
   - Verkkohaku ja mukautetut työkalut

---

## 5. Infrastruktuurin parannukset

### 5.1 CI/CD-parannukset

Toteutettu tiedostossa [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): Pythonin linttaus/muotoilu (Ruff + Black) on **pakollinen** ylläpidetyssä `shared/` apuohjelmamoduulissa ja toimii **suosituksena** muissa opetussisällöissä, sekä suosituksena ESLint-käsky JavaScript/TypeScriptille. Esimerkkiperustaso oli:

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  python-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install ruff black mypy
      - run: ruff check .
      - run: black --check .

  js-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx eslint .
```

### 5.2 Turvallisuusskannaus

Toteutettu tiedostossa [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): CodeQL-analyysi Pythonille ja JavaScript/TypeScriptille (push, pull request ja viikoittain) sekä riippuvuuksien tarkastus pull requesteissa. Esimerkkiperustaso oli:

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3

  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
```

---

## 6. Kehittäjäkokemuksen parannukset

### 6.1 DevContainer-parannukset

Toteutettu tiedostoissa [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) ja [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): säiliö sisältää nyt Pylancen, Black-muotoilijan, Ruffin, ESLintin, Prettierin ja Copilotin laajennukset, sallii muotoilun tallennettaessa repo-laajuisella Black/Prettier-konfiguraatiolla ja asentaa kehitystyökalut (`ruff`, `black`, `mypy`, `pytest`), jotta [code-quality työnkulku](../../../.github/workflows/code-quality.yml) voidaan toistaa paikallisesti. `mcr.microsoft.com/devcontainers/universal` peruskuva sisältää Pythonin ja Noden, joten lisäominaisuuksia ei tarvita. Esimerkkiperustaso oli:

```json
{
  "name": "Generative AI for Beginners",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "github.copilot"
      ],
      "settings": {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "pip install -e .[dev] && npm install"
}
```

### 6.2 Interaktiivinen harjoitusympäristö

Harkitse seuraavia lisäyksiä:
- Jupyter-muistikirjat esitäytetyillä API-avaimilla (ympäristömuuttujien kautta)
- Gradio/Streamlit-demot visuaalisille oppijoille
- Interaktiiviset tietovisat tiedon arvioimiseksi

---

## 7. Monikielinen tuki

### 7.1 Nykyinen kielituki

| Teknologia | Käsitellyt oppitunnit | Tila |
|------------|-----------------|--------|
| Python | Kaikki | Täydellinen |
| TypeScript | 06-09, 11 | Osittainen |
| JavaScript | 06-08, 11 | Osittainen |
| .NET/C# | Jotkut | Osittainen |

### 7.2 Suositellut lisäykset

1. **Go** - Kasvava AI/ML-työkalujen kieli
2. **Rust** - Suorituskykykritiikka sovelluksissa
3. **Java/Kotlin** - Enterprise-sovellukset

---

## 8. Suorituskyvyn optimoinnit

### 8.1 Kooditasoiset optimoinnit

1. **Async/Await-mallit**
   - Lisää asynkronisia esimerkkejä eräprosessoinnista
   - Havainnollista rinnakkaiset API-kutsut

2. **Välimuististrategiat**
   - Lisää upotusten välimuistiesimerkkejä
   - Havainnollista vastausvälimuistimallit

3. **Tokenien optimointi**
   - Lisää tiktokenin käytön esimerkkejä
   - Havainnollista kehotteen pakkaustekniikoita

### 8.2 Kustannusten optimointiesimerkit

Lisää esimerkkejä, jotka osoittavat:
- Mallin valinnan tehtävän monimutkaisuuden mukaan
- Kehotteen optimointia token-efektiivisyyteen
- Eräprosessi bulk-toimintoihin

---

## 9. Saavutettavuus ja kansainvälistyminen

### 9.1 Nykyinen käännösten tila

Kaikki käännökset ovat **valmiit** ja tuotettu automaattisesti [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) -työkalulla, joka tuottaa ja pitää yli 50 kieliversiota opetussuunnitelmasta synkronoituna englanninkielisen lähteen kanssa. Käännetty sisältö sijaitsee `translations/`-kansiossa ja lokalisoidut kuvat `translated_images/`-kansiossa; kaikkien saatavilla olevien kielten täydellinen lista on julkaistu projektin README-tiedoston alussa.

| Näkökulma | Tila |
|--------|--------|
| Käännösten kattavuus | Täydellinen — yli 50 kieltä, kaikki oppitunnit |
| Käännösmenetelmä | Automaattinen Azure Co-op Translatorin kautta |
| Synkronoitu englanninkielisen lähteen kanssa | Kyllä — uudelleenluotu automaattisesti |

### 9.2 Saavutettavuuden parannukset

1. Lisää vaihtoehtoinen teksti kaikkiin kuviin
2. Varmista, että koodiesimerkeissä on asianmukainen syntaksiväritys
3. Lisää videotekstit kaikille videoaineistoille
4. Varmista, että värikontrasti täyttää WCAG-ohjeet

---

## 10. Toteutuksen priorisointi

### Vaihe 1: Välittömät toimet (Viikko 1-2)
- [x] Korjaa kriittiset turvallisuusongelmat
- [x] Lisää koodin laadun konfigurointi
- [x] Luo jaetut apuohjelmat
- [x] Dokumentoi turvallisuusohjeet

### Vaihe 2: Lyhyen aikavälin toimet (Viikko 3-4)
- [x] Päivitä vanhentuneet API-kuviot (Chat Completions → Responses API, Python + TypeScript)
- [ ] Lisää tyyppivihjeet kaikkiin Python-tiedostoihin (valmiina ylläpidetylle `shared/` moduulille; oppituntiesimerkit pidetään yksinkertaisina)
- [x] Lisää CI/CD-työnkulut koodin laadulle
- [x] Luo turvallisuusskannaus työnkulku

### Vaihe 3: Keskipitkän aikavälin toimet (Kuukaudet 2-3)
- [ ] Lisää uusi turvallisuusoppitunti
- [ ] Lisää tuotantoon käyttöönotto opetukseen
- [x] Paranna DevContainerin asetuksia
- [ ] Lisää interaktiiviset demot

### Vaihe 4: Pitkän aikavälin toimet (Kuukaudet 4+)
- [ ] Lisää edistynyt RAG-oppitunti
- [ ] Laajenna kielitukea
- [ ] Lisää kattava testauspaketti
- [ ] Luo sertifiointiohjelma

---

## Yhteenveto

Tämä tiekartta tarjoaa rakenteellisen lähestymistavan Generative AI for Beginners -opetussuunnitelman parantamiseen. Käsittelemällä turvallisuuskysymyksiä, modernisoimalla API:t ja lisäämällä opetussisältöjä, kurssi valmistaa opiskelijat paremmin käytännön tekoälysovellusten kehitykseen.

Kysymyksiä tai kontribuutioita varten avaa issue GitHub-repositoriossa.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->