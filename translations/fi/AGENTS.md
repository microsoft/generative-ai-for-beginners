# AGENTS.md

## Projektin yleiskatsaus

Tämä arkisto sisältää kattavan 21 oppitunnin opetussuunnitelman, joka opettaa generatiivisen tekoälyn perusteet ja sovelluskehityksen. Kurssi on suunniteltu aloittelijoille ja kattaa kaiken peruskäsitteistä tuotantovalmiiden sovellusten rakentamiseen.

**Keskeiset teknologiat:**
- Python 3.9+ kirjastoilla: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript Node.js:llä ja kirjastoilla: `openai` (Azure OpenAI v1-päätepisteen kautta + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry -mallit)
- Azure OpenAI Service, OpenAI API ja Microsoft Foundry Models (GitHub Models poistuu käytöstä heinäkuun 2026 lopussa)
- Jupyter-muistikirjat interaktiiviseen oppimiseen
- Dev Containers yhdenmukaiseen kehitysympäristöön

**Arkiston rakenne:**
- 21 numeroitua oppituntihakemistoa (00-21), jotka sisältävät README:t, koodiesimerkit ja tehtävät
- Useita toteutuksia: Python, TypeScript ja toisinaan .NET-esimerkit
- Käännöshakemisto, jossa yli 40 kieliversiota
- Keskitetty konfiguraatio `.env`-tiedoston kautta (käytä `.env.copy` mallina)

## Asennuskomennot

### Alkukasitus arkistosta

```bash
# Kloonaa repositorio
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Kopioi ympäristöpohja
cp .env.copy .env
# Muokkaa .env tiedostoa API-avaimillasi ja päätepisteilläsi
```

### Python-ympäristön asennus

```bash
# Luo virtuaaliympäristö
python3 -m venv venv

# Aktivoi virtuaaliympäristö
# macOS/Linux-käyttöjärjestelmässä:
source venv/bin/activate
# Windows-käyttöjärjestelmässä:
venv\Scripts\activate

# Asenna riippuvuudet
pip install -r requirements.txt
```

### Node.js/TypeScript:n asennus

```bash
# Asenna juuritason riippuvuudet (dokumentaatiotyökaluille)
npm install

# Yksittäisten oppituntien TypeScript-esimerkkeihin siirry tiettyyn oppituntiin:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Containerin asennus (suositeltu)

Arkisto sisältää `.devcontainer`-konfiguraation GitHub Codespacesille tai VS Code Dev Containers -laajennukselle:

1. Avaa arkisto GitHub Codespacesissa tai VS Codessa Dev Containers -laajennuksella
2. Dev Container suorittaa automaattisesti:
   - Asentaa Python-riippuvuudet `requirements.txt`-tiedostosta
   - Suorittaa post-create-skriptin (`.devcontainer/post-create.sh`)
   - Määrittää Jupyter-ytimen

## Kehitysprosessi

### Ympäristömuuttujat

Kaikki oppitunnit, jotka tarvitsevat API-käyttöoikeuden, käyttävät `.env`-tiedostossa määriteltyjä ympäristömuuttujia:

- `OPENAI_API_KEY` - OpenAI API:lle
- `AZURE_OPENAI_API_KEY` - Azure OpenAI:lle Microsoft Foundryssa (Azure OpenAI Service on nyt osa Microsoft Foundrya: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI -päätepisteen URL (Foundry-resurssipäätepiste)
- `AZURE_OPENAI_DEPLOYMENT` - Chat completion -mallin käyttöönoton nimi (kurssin oletus: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings-mallin käyttöönoton nimi (kurssin oletus: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - API-version (oletus: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Hugging Face -malleille
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Models -päätepiste (monitoimittajamallien luettelo)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models -API-avain (korvaa poistuvan `GITHUB_TOKEN`:in)
- `AZURE_INFERENCE_CHAT_MODEL` - Ei-päättelymalli (esim. `Llama-3.3-70B-Instruct`), jota käytetään `temperature`-esimerkeissä, koska päättelymallit eivät tue otantaa sääteleviä asetuksia

### Mallikäytännöt (tärkeää)

- **Oletus chat-malli on `gpt-5-mini`** – nykyinen, ei vanhentunut **päättelymalli**. Vuodesta 2026 lähtien vanhemmat otantaa tukevat ”mini”-mallit (`gpt-4o-mini`, `gpt-4.1-mini`) ovat poistumassa käytöstä, joten opetussuunnitelma standardisoi GPT-5 -perheeseen.
- **Päättelymallit hylkäävät `temperature` ja `top_p`** ja käyttävät `max_output_tokens` (Responses API) / `max_completion_tokens` (chat completions) arvoa `max_tokens` sijaan. Älä lisää `temperature`/`top_p`/`max_tokens` arvoja esimerkkeihin, jotka käyttävät `gpt-5-mini`-mallia.
- **`temperature`-asetuksen havainnollistamiseksi** esimerkeissä käytetään **Llama**-mallia (`Llama-3.3-70B-Instruct`) Microsoft Foundry Models -päätepisteen (`AZURE_INFERENCE_CHAT_MODEL`) kautta. Ohjaa päättelymalleja kehotetekniikalla ja päättelyohjauksilla otantapainikkeiden sijaan.
- **Hienosäätö (oppitunti 18)** käyttää edelleen `gpt-4.1-mini`-mallia: GPT-5 tukee vain vahvistusoppimista (RFT), ei valvottua hienosäätöä (SFT), jota siellä näytetään.
- Oppitunnit 20 (Mistral) ja 21 (Meta) käyttävät edelleen `temperature`/`max_tokens` asetuksia, koska ne kohdistuvat Mistral/Llama-malleihin, jotka niitä tukevat.

### Python-esimerkkien ajaminen

```bash
# Siirry oppitunnin hakemistoon
cd 06-text-generation-apps/python

# Suorita Python-skripti
python aoai-app.py
```

### TypeScript-esimerkkien ajaminen

```bash
# Siirry TypeScript-sovelluksen hakemistoon
cd 06-text-generation-apps/typescript/recipe-app

# Käännä TypeScript-koodi
npm run build

# Suorita sovellus
npm start
```

### Jupyter-muistikirjojen ajaminen

```bash
# Käynnistä Jupyter repositorion juurihakemistossa
jupyter notebook

# Tai käytä VS Codea Jupyter-laajennuksella
```

### Työskentely eri oppityyppien kanssa

- **"Learn"-oppitunnit**: Painopiste README.md-dokumentaatiossa ja konsepteissa
- **"Build"-oppitunnit**: Sisältävät toimivat koodiesimerkit Pythonilla ja TypeScriptillä
- Jokaisella oppitunnilla on README.md, jossa teoria, koodikävelyt ja linkit videotietoihin

## Koodityyliohjeet

### Python

- Käytä `python-dotenv` ympäristömuuttujien hallintaan
- Tuo `openai`-kirjasto API-kutsuihin
- Käytä `pylint`-tyylistä lintitys työkalua (joissakin esimerkeissä `# pylint: disable=all` yksinkertaisuuden vuoksi)
- Noudata PEP 8 nimeämiskäytäntöjä
- Tallenna API-tunnukset `.env` tiedostoon, älä koodiin

### TypeScript

- Käytä `dotenv`-pakettia ympäristömuuttujille
- TypeScriptin konfiguraatio löytyy kunkin sovelluksen `tsconfig.json` tiedostosta
- Käytä `openai`-pakettia Azure OpenAI:lle (kohdista asiakas `/openai/v1/` päätepisteeseen ja kutsu `client.responses.create`); käytä `@azure-rest/ai-inference` Microsoft Foundry Models -malleille
- Käytä `nodemon`-työkalua kehitykseen automaattisella uudelleenkäynnistyksellä
- Rakenna ennen ajoa: `npm run build` ja sitten `npm start`

### Yleiset käytännöt

- Pidä koodiesimerkit yksinkertaisina ja opetuksellisina
- Sisällytä kommentteja, jotka selittävät avainkäsiteitä
- Kunkin oppitunnin koodin tulee olla itsenäistä ja suoritettavissa
- Käytä yhdenmukaista nimeämistä: `aoai-` etuliite Azure OpenAI:lle, `oai-` OpenAI API:lle, `githubmodels-` Microsoft Foundry Models:lle (perinteinen GitHub Models ajalta säilynyt etuliite)

## Dokumentaation ohjeistukset

### Markdown-tyyli

- Kaikki URL-osoitteet tulee kääriä muotoon `[teksti](../../url)` ilman ylimääräisiä välilyöntejä
- Relatiivisten linkkien tulee alkaa `./` tai `../`
- Kaikkien Microsoftin verkkotunnusten linkkien tulee sisältää seuranta-ID: `?WT.mc_id=academic-105485-koreyst`
- Älä käytä maakohtaisia paikallisia polkuja URL-osoitteissa (vältä `/en-us/`)
- Kuvat tallennetaan `./images`-kansioon kuvaavilla nimillä
- Käytä tiedostonimissä englanninkielisiä merkkejä, numeroita ja viivoja

### Käännöksen tuki

- Arkisto tukee yli 40 kieltä automatisoidun GitHub Actions -prosessin kautta
- Käännökset tallennetaan `translations/`-hakemistoon
- Älä lähetä keskeneräisiä käännöksiä
- Konekäännöksiä ei hyväksytä
- Käännetyt kuvat tallennetaan `translated_images/`-hakemistoon

## Testaus ja validointi

### Tarkistukset ennen lähettämistä

Tämä arkisto käyttää GitHub Actions -palvelua validointiin. Ennen PR:n lähettämistä:

1. **Tarkista Markdown-linkit**:
   ```bash
   # validate-markdown.yml-työnkulku tarkistaa:
   # - Rikkinäiset suhteelliset polut
   # - Puuttuvat seuranta-ID:t poluissa
   # - Puuttuvat seuranta-ID:t URL-osoitteissa
   # - Maan paikallisversioilla varustetut URL-osoitteet
   # - Rikkinäiset ulkoiset URL-osoitteet
   ```

2. **Manuaalinen testaus**:
   - Testaa Python-esimerkit: Aktivoi venv ja suorita skriptit
   - Testaa TypeScript-esimerkit: `npm install`, `npm run build`, `npm start`
   - Varmista, että ympäristömuuttujat on määritelty oikein
   - Tarkista API-avaimien toimivuus koodiesimerkeissä

3. **Koodiesimerkit**:
   - Varmista, että kaikki koodi toimii ilman virheitä
   - Testaa sekä Azure OpenAI että OpenAI API, kun sovellettavissa
   - Varmista, että esimerkit toimivat Microsoft Foundry Models -malleilla, kun niitä tuetaan

### Automatisoituja testejä ei ole

Tämä on oppimiseen keskittyvä arkisto, joka sisältää tutoriaaleja ja esimerkkejä. Yksikkö- tai integraatiotestejä ei ole suorittaa. Validointi perustuu pääasiassa:
- Manuaaliseen koodiesimerkkien testaamiseen
- GitHub Actions -työkaluun Markdownin tarkistamiseen
- Yhteisön arvioon opetusmateriaalista

## Pull Request -ohjeet

### Ennen lähettämistä

1. Testaa koodimuutokset Pythonissa ja TypeScriptissä, kun sovellettavissa
2. Suorita markdown-validointi (käynnistyy automaattisesti PR:ssä)
3. Varmista, että seuranta-ID:t ovat mukana kaikissa Microsoftin URL-osoitteissa
4. Tarkista, että relatiiviset linkit ovat voimassa
5. Varmista, että kuvat on asianmukaisesti viitattu

### PR-otsikkotyylit

- Käytä kuvaavia otsikoita: `[Lesson 06] Korjaa Python-esimerkin kirjoitusvirhe` tai `Päivitä README oppitunnissa 08`
- Viittaa tarvittaessa issuetunnuksiin: `Fixes #123`

### PR-kuvaus

- Selitä, mitä ja miksi muutettiin
- Lisää linkkejä asiaankuuluviin issueihin
- Koodimuutoksissa kerro, mitä esimerkkejä testattiin
- Käännös-PR:issä liitä kaikki tiedostot täydelliseen käännökseen

### Osallistumisvaatimukset

- Allekirjoita Microsoft CLA (automaattisesti ensimmäisessä PR:ssa)
- Tee fork omaan tiliisi ennen muutosten tekemistä
- Yksi PR per looginen muutos (älä yhdistä epäyhteensopivia korjauksia)
- Pidä PR:t keskittyneinä ja pieninä mahdollisuuksien mukaan

## Yleiset työnkulut

### Uuden koodiesimerkin lisääminen

1. Siirry sopivaan oppituntihakemistoon
2. Luo esimerkki `python/` tai `typescript/` alihakemistoon
3. Noudata nimeämiskäytäntöä: `{provider}-{example-name}.{py|ts|js}`
4. Testaa varsinaisilla API-tunnuksilla
5. Dokumentoi mahdolliset uudet ympäristömuuttujat oppitunnin README:hen

### Dokumentaation päivittäminen

1. Muokkaa oppitunnin README.md-tiedostoa
2. Noudata Markdown-ohjeita (seuranta-ID:t, relatiiviset linkit)
3. Käännösten päivitys hoituu GitHub Actionsien kautta (älä muokkaa manuaalisesti)
4. Testaa, että kaikki linkit toimivat

### Työskentely Dev Containereiden kanssa

1. Arkistossa on `.devcontainer/devcontainer.json`
2. Post-create-skripti asentaa Python-riippuvuudet automaattisesti
3. Python- ja Jupyter-laajennukset on esikonfiguroitu
4. Ympäristö perustuu `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Julkaisu ja käyttöönotto

Tämä on oppimisarkisto - käyttöönottoa ei ole. Opetussuunnitelman kuluttavat:

1. **GitHub-arkisto**: Suora pääsy koodiin ja dokumentaatioon
2. **GitHub Codespaces**: Välitön kehitysympäristö esiasetuksilla
3. **Microsoft Learn**: Sisältö voi olla mukana virallisella oppimisalustalla
4. **docsify**: Dokumentaatiosivusto, joka rakennetaan Markdownista (katso `docsifytopdf.js` ja `package.json`)

### Dokumentaation sivuston rakentaminen

```bash
# Luo PDF dokumentaatiosta (tarvittaessa)
npm run convert
```

## Vianmääritys

### Yleisiä ongelmia

**Pythonin tuontivirheet**:
- Varmista, että virtuaaliympäristö on aktivoitu
- Suorita `pip install -r requirements.txt`
- Tarkista, että Python-versio on 3.9 tai uudempi

**TypeScriptin käännösvirheet**:
- Suorita `npm install` sovelluskohtaisessa hakemistossa
- Tarkista Node.js version yhteensopivuus
- Tyhjennä `node_modules` ja asenna uudelleen tarvittaessa

**API-todennusvirheet**:
- Varmista, että `.env`-tiedosto on olemassa ja oikein täytetty
- Tarkista, että API-avaimet ovat voimassa eivätkä ole vanhentuneet
- Varmista, että päätepisteen URL-osoitteet ovat oikeat alueellasi

**Puuttuvat ympäristömuuttujat**:
- Kopioi `.env.copy` tiedostoksi `.env`
- Täytä kaikki tarvittavat arvot kulloiseenkin oppituntiin liittyen
- Käynnistä sovellus uudelleen `.env`-päivityksen jälkeen

## Lisäresurssit

- [Kurssin asennusopas](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Osallistumisohjeet](./CONTRIBUTING.md)
- [Käyttäytymissäännöt](./CODE_OF_CONDUCT.md)
- [Tietoturvapolitiikka](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Kokoelma edistyneitä koodiesimerkkejä](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projektiin liittyviä huomioita

- Tämä on **opetuksellinen arkisto**, keskittyy oppimiseen, ei tuotantokoodiin
- Esimerkit on tarkoituksella yksinkertaisia ja opetuksellisia
- Koodin laatu ja opetuksen selkeys on tasapainotettu
- Jokainen oppitunti on itsenäinen ja mahdollista suorittaa itsenäisesti
- Arkisto tukee useita API-toimittajia: Azure OpenAI, OpenAI, Microsoft Foundry Models sekä offline-toimittajia kuten Foundry Local ja Ollama
- Sisältö on monikielistä automatisoitujen käännösten työnkululla
- Aktiivinen yhteisö Discordissa kysymyksiä ja tukea varten

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->