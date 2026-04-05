# Parannettujen ominaisuuksien ja parannusten tiekartta

Tässä asiakirjassa esitetään suositellut parannukset ja kehitysehdotukset Generative AI for Beginners -opintojaksolle, perustuen kattavaan koodikatselmukseen ja alan parhaiden käytäntöjen analyysiin.

## Tiivistelmä

Koodikanta on analysoitu turvallisuuden, koodin laadun ja opetuksellisen tehokkuuden näkökulmasta. Tämä asiakirja tarjoaa suosituksia välittömistä korjauksista, lähiajan parannuksista ja tulevista kehityksistä.

---

## 1. Turvallisuuden parannukset (Prioriteetti: Kriittinen)

### 1.1 Välittömät korjaukset (Valmistunut)

| Ongelmakohta | Vaikuttavat tiedostot | Tila |
|--------------|----------------------|-------|
| Kovakoodattu SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Korjattu |
| Puuttuva ympäristömuuttujien validointi | Useita JS/TS-tiedostoja | Korjattu |
| Turvattomat funktion kutsut | `11-integrating-with-function-calling/js-githubmodels/app.js` | Korjattu |
| Tiedostokahvojen vuoto | `08-building-search-applications/scripts/` | Korjattu |
| Puuttuvat pyyntöaikakatkaisut | `09-building-image-applications/python/` | Korjattu |

### 1.2 Suositellut lisäturvaominaisuudet

1. **Rajapintakutsujen rajoitusesimerkit**
   - Lisää esimerkkikoodi, joka näyttää, miten rajapintakutsujen määrää rajoitetaan
   - Havainnollista eksponentiaalisen viiveen (exponential backoff) mallinnusta

2. **API-avainten kierto**
   - Lisää ohjeet API-avainten kiertämisen parhaista käytännöistä
   - Sisällytä esimerkkejä Azure Key Vaultin tai vastaavien palveluiden käytöstä

3. **Sisällön turvamoduulien integrointi**
   - Lisää esimerkkejä Azure Content Safety API:n käyttämisestä
   - Havainnollista syötteen ja tuloksen moderointimalleja

---

## 2. Koodin laadun parannukset

### 2.1 Lisätyt konfiguraatiotiedostot

| Tiedosto | Tarkoitus |
|----------|-----------|
| `.eslintrc.json` | JavaScript/TypeScript linttausasetukset |
| `.prettierrc` | Koodinmuotoilun standardit |
| `pyproject.toml` | Python-työkalujen konfiguraatio (Black, Ruff, mypy) |

### 2.2 Luodut jaetut apuohjelmat

Uusi `shared/python/` moduuli sisältää:
- `env_utils.py` - Ympäristömuuttujien käsittely
- `input_validation.py` - Syötteen validointi ja puhdistus
- `api_utils.py` - Turvalliset API-pyyntöjen kääreet

### 2.3 Suositellut koodin parannukset

1. **Tyyppivihjeiden kattavuus**
   - Lisää tyyppivihjeet kaikkiin Python-tiedostoihin
   - Ota käyttöön tiukka TypeScript-tila kaikissa TS-projekteissa

2. **Dokumentointistandardit**
   - Lisää docstringit kaikkiin Python-funktioihin
   - Lisää JSDoc-kommentit kaikkiin JavaScript/TypeScript-funktioihin

3. **Testauskehys**
   - Lisää pytest-konfiguraatio ja esimerkkitestit
   - Lisää Jest-konfiguraatio JavaScript/TypeScript:lle

---

## 3. Opetusparannukset

### 3.1 Uudet oppituntien aiheet

1. **Turvallisuus AI-sovelluksissa** (Ehdotettu oppitunti 22)
   - Kehoteinjektiohyökkäykset ja puolustukset
   - API-avainhallinta
   - Sisällön moderointi
   - Kutsujen rajoittaminen ja väärinkäytön estäminen

2. **Tuotantoon vieminen** (Ehdotettu oppitunti 23)
   - Konttiteknologia Dockerilla
   - CI/CD-putket
   - Valvonta ja lokitus
   - Kustannusten hallinta

3. **Edistyneet RAG-tekniikat** (Ehdotettu oppitunti 24)
   - Hybridihaku (avainsanat + semantiikka)
   - Uudelleenjärjestelystrategiat
   - Monimodaalinen RAG
   - Arviointimittarit

### 3.2 Nykyisten oppituntien parannukset

| Oppitunti | Suositeltu parannus |
|-----------|---------------------|
| 06 - Tekstin generointi | Lisää suoratoistovaste-esimerkkejä |
| 07 - Chat-sovellukset | Lisää keskustelumuistimallit |
| 08 - Hakusovellukset | Lisää vektoritietokannan vertailu |
| 09 - Kuvagenerointi | Lisää kuvan muokkaus-/vaihtoehtoesimerkkejä |
| 11 - Funktiokutsut | Lisää rinnakkaisten funktiokutsujen esimerkkejä |
| 15 - RAG | Lisää paloitusstrategioiden vertailu |
| 17 - AI-agentit | Lisää moniagenttien orkestrointi |

---

## 4. API:n modernisointi

### 4.1 Päivitettävät vanhentuneet API-mallit

| Vanha malli | Uusi malli | Vaikuttavat tiedostot |
|-------------|------------|-----------------------|
| `openai.api_type = "azure"` | `AzureOpenAI()` -asiakas | Useita skriptejä `08-building-search-applications/` |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | Useita Jupyter-muistikirjoja |
| `df.append()` (pandas) | `pd.concat()` | RAG-muistikirja |

### 4.2 Demonstroitavat uudet API-ominaisuudet

1. **Rakenteiset tulosteet** (OpenAI)
   - JSON-tila
   - Funktiokutsut tiukoilla skeemoilla

2. **Näkökyvyn ominaisuudet**
   - Kuvan analyysi GPT-4V:llä
   - Monimodaaliset promptit

3. **Assistants API**
   - Koodin tulkki
   - Tiedoston haku
   - Räätälöidyt työkalut

---

## 5. Infrastruktuurin parannukset

### 5.1 CI/CD-parannukset

Nykyiset työnkulut hoitavat markdownin validoinnin. Suositellut lisäykset:

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

### 5.2 Turvatarkastukset

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

Päivitä `.devcontainer/devcontainer.json`:

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

### 6.2 Interaktiivinen oppimisympäristö

Harkitse lisäämistä:
- Jupyter-muistikirjat valmiiksi asetetuilla API-avaimilla (ympäristön kautta)
- Gradio/Streamlit-demoja visuaalisille oppijoille
- Interaktiivisia visailuja tiedon arviointiin

---

## 7. Monikielinen tuki

### 7.1 Nykyinen kielituki

| Teknologia | Käsitellyt oppitunnit | Tila |
|------------|-----------------------|-------|
| Python | Kaikki | Täydellinen |
| TypeScript | 06-09, 11 | Osittainen |
| JavaScript | 06-08, 11 | Osittainen |
| .NET/C# | Joitakin | Osittainen |

### 7.2 Suositellut lisäykset

1. **Go** - Kasvava AI/ML-työkaluissa
2. **Rust** - Suorituskykykriittiset sovellukset
3. **Java/Kotlin** - Yrityssovellukset

---

## 8. Suorituskyvyn optimoinnit

### 8.1 Koodi­tason optimoinnit

1. **Async/Await-mallit**
   - Lisää asynkronisia esimerkkejä eräajoon
   - Havainnollista rinnakkaisia API-kutsuja

2. **välimuististrategiat**
   - Lisää upotusten (embedding) välimuistin esimerkkejä
   - Havainnollista vasteiden välimuistimallinnusta

3. **Tokenien optimointi**
   - Lisää tiktokenin käyttöönottoesimerkkejä
   - Havainnollista prompttien pakkaustekniikoita

### 8.2 Kustannusten optimointiesimerkit

Lisää esimerkkejä, jotka näyttävät:
- Mallin valinnan tehtävän kompleksisuuden mukaan
- Prompttien suunnittelun token-tehokkuuden parantamiseksi
- Eräajon tehokas käyttäminen suurissa toiminnoissa

---

## 9. Saavutettavuus ja kansainvälistyminen

### 9.1 Nykyinen käännöstila

| Kieli | Tila |
|--------|--------|
| Englanti | Täydellinen |
| Kiina (yksinkertaistettu) | Täydellinen |
| Japani | Täydellinen |
| Korea | Täydellinen |
| Espanja | Osittainen |
| Portugali | Osittainen |
| Turkki | Osittainen |
| Puola | Osittainen |

### 9.2 Saavutettavuuden parannukset

1. Lisää alt-tekstit kaikkiin kuviin
2. Varmista koodiesimerkkien oikea syntaksin korostus
3. Lisää videoiden tekstitykset kaikkiin videotiedostoihin
4. Varmista, että värikontrastit täyttävät WCAG-ohjeistukset

---

## 10. Toteutuksen priorisointi

### Vaihe 1: Välitön (Viikot 1-2)
- [x] Korjaa kriittiset turvallisuusongelmat
- [x] Lisää koodin laadun konfiguraatio
- [x] Luo jaetut apuohjelmat
- [x] Dokumentoi turvallisuusohjeet

### Vaihe 2: Lyhyen aikavälin (Viikot 3-4)
- [ ] Päivitä vanhentuneet API-mallit
- [ ] Lisää tyyppivihjeet kaikkiin Python-tiedostoihin
- [ ] Lisää CI/CD-työnkulut koodin laadulle
- [ ] Luo turvatarkastus työnkulku

### Vaihe 3: Keskipitkän aikavälin (Kuukaudet 2-3)
- [ ] Lisää uusi turvallisuusopetus
- [ ] Lisää tuotantoon viemisen opetus
- [ ] Paranna DevContainer-asetuksia
- [ ] Lisää interaktiiviset demonstroinnit

### Vaihe 4: Pitkän aikavälin (Kuukaudet 4+)
- [ ] Lisää edistynyt RAG-opetus
- [ ] Laajenna kielitukea
- [ ] Lisää kattava testikattavuus
- [ ] Luo sertifiointiohjelma

---

## Yhteenveto

Tämä tiekartta tarjoaa jäsennellyn lähestymistavan Generative AI for Beginners -opintojakson parantamiseen. Käsittelemällä turvallisuushaasteita, modernisoimalla rajapintoja ja lisäämällä opetussisältöä, kurssi valmistaa opiskelijoita paremmin todellisiin AI-sovelluskehityksen haasteisiin.

Kysymyksiä tai osallistumisia varten, avaa ongelma GitHub-repositoriossa.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty tekoälypohjaisella käännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta automaattisissa käännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaisen ihmiskääntäjän käyttöä. Emme ota vastuuta mahdollisista väärinymmärryksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->