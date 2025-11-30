<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:05:09+00:00",
  "source_file": "AGENTS.md",
  "language_code": "fi"
}
-->
# AGENTS.md

## Projektin yleiskatsaus

Tämä arkisto sisältää kattavan 21 oppitunnin kurssin, joka opettaa generatiivisen tekoälyn perusteet ja sovelluskehityksen. Kurssi on suunniteltu aloittelijoille ja kattaa kaiken peruskäsitteistä tuotantovalmiiden sovellusten rakentamiseen.

**Keskeiset teknologiat:**
- Python 3.9+ ja kirjastot: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript Node.js:n kanssa ja kirjastot: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API ja GitHub Models
- Jupyter Notebooks interaktiiviseen oppimiseen
- Dev Containers yhtenäisen kehitysympäristön varmistamiseksi

**Arkiston rakenne:**
- 21 numeroitua oppituntihakemistoa (00-21), jotka sisältävät README-tiedostoja, esimerkkikoodeja ja tehtäviä
- Useita toteutuksia: Python, TypeScript ja joskus .NET-esimerkkejä
- Käännöshakemisto, jossa yli 40 kieliversiota
- Keskitetty konfiguraatio `.env`-tiedoston kautta (käytä `.env.copy` mallina)

## Asennuskomennot

### Alkuperäinen arkiston asennus

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Python-ympäristön asennus

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Node.js/TypeScript-asennus

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container -asennus (suositeltu)

Arkisto sisältää `.devcontainer`-konfiguraation GitHub Codespacesille tai VS Code Dev Containersille:

1. Avaa arkisto GitHub Codespacesissa tai VS Codessa Dev Containers -laajennuksen kanssa
2. Dev Container asentaa automaattisesti:
   - Python-riippuvuudet `requirements.txt`-tiedostosta
   - Post-create-skriptin (`.devcontainer/post-create.sh`)
   - Jupyter-kernelin

## Kehitystyön kulku

### Ympäristömuuttujat

Kaikki oppitunnit, jotka vaativat API-yhteyttä, käyttävät `.env`-tiedostossa määriteltyjä ympäristömuuttujia:

- `OPENAI_API_KEY` - OpenAI API:lle
- `AZURE_OPENAI_API_KEY` - Azure OpenAI Service:lle
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI -palvelun URL-osoite
- `AZURE_OPENAI_DEPLOYMENT` - Chat completion -mallin käyttönimi
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings-mallin käyttönimi
- `AZURE_OPENAI_API_VERSION` - API-versio (oletus: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Hugging Face -malleille
- `GITHUB_TOKEN` - GitHub Models -palvelulle

### Python-esimerkkien suorittaminen

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### TypeScript-esimerkkien suorittaminen

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Jupyter Notebookien käyttö

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Erilaisten oppituntityyppien käsittely

- **"Learn"-oppitunnit**: Keskittyvät README.md-dokumentaatioon ja käsitteisiin
- **"Build"-oppitunnit**: Sisältävät toimivia esimerkkikoodeja Pythonilla ja TypeScriptillä
- Jokaisessa oppitunnissa on README.md, jossa on teoriaa, koodin läpikäyntiä ja linkkejä videomateriaaleihin

## Koodityyliohjeet

### Python

- Käytä `python-dotenv` ympäristömuuttujien hallintaan
- Tuo `openai`-kirjasto API-yhteyksiä varten
- Käytä `pylint` linttaamiseen (joissakin esimerkeissä on `# pylint: disable=all` yksinkertaisuuden vuoksi)
- Noudata PEP 8 -nimikäytäntöjä
- Tallenna API-tunnukset `.env`-tiedostoon, älä koskaan koodiin

### TypeScript

- Käytä `dotenv`-pakettia ympäristömuuttujille
- TypeScript-konfiguraatio `tsconfig.json`-tiedostossa jokaiselle sovellukselle
- Käytä `@azure/openai` tai `@azure-rest/ai-inference` Azure-palveluille
- Käytä `nodemon` kehitykseen automaattisella uudelleenlatauksella
- Käännä ennen suorittamista: `npm run build` ja sitten `npm start`

### Yleiset käytännöt

- Pidä koodiesimerkit yksinkertaisina ja opettavaisina
- Sisällytä kommentteja, jotka selittävät keskeiset käsitteet
- Jokaisen oppitunnin koodi tulee olla itsenäinen ja suoritettavissa
- Käytä johdonmukaista nimeämistä: `aoai-` Azure OpenAI:lle, `oai-` OpenAI API:lle, `githubmodels-` GitHub Modelsille

## Dokumentaatiokäytännöt

### Markdown-tyyli

- Kaikki URL-osoitteet tulee olla muodossa `[teksti](../../url)` ilman ylimääräisiä välilyöntejä
- Suhteellisten linkkien tulee alkaa `./` tai `../`
- Kaikki Microsoftin verkkotunnuksiin johtavat linkit tulee sisältää seurantatunnus: `?WT.mc_id=academic-105485-koreyst`
- Vältä maakohtaisia kielikoodeja URL-osoitteissa (vältä `/en-us/`)
- Kuvat tallennetaan `./images`-hakemistoon kuvaavilla nimillä
- Käytä tiedostonimissä englanninkielisiä merkkejä, numeroita ja viivoja

### Käännöstuki

- Arkisto tukee yli 40 kieltä automaattisten GitHub Actions -työnkulkujen kautta
- Käännökset tallennetaan `translations/`-hakemistoon
- Älä lähetä osittaisia käännöksiä
- Konekäännöksiä ei hyväksytä
- Käännetyt kuvat tallennetaan `translated_images/`-hakemistoon

## Testaus ja validointi

### Ennen lähettämistä

Tämä arkisto käyttää GitHub Actions -työnkulkuja validointiin. Ennen PR:n lähettämistä:

1. **Tarkista Markdown-linkit**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Manuaalinen testaus**:
   - Testaa Python-esimerkit: Aktivoi venv ja suorita skriptit
   - Testaa TypeScript-esimerkit: `npm install`, `npm run build`, `npm start`
   - Varmista, että ympäristömuuttujat on konfiguroitu oikein
   - Tarkista, että API-avaimet toimivat koodiesimerkkien kanssa

3. **Koodiesimerkit**:
   - Varmista, että kaikki koodi toimii ilman virheitä
   - Testaa sekä Azure OpenAI että OpenAI API, kun mahdollista
   - Varmista, että esimerkit toimivat GitHub Models -palvelun kanssa, jos tuettu

### Ei automatisoituja testejä

Tämä on opetusarkisto, joka keskittyy tutoriaaleihin ja esimerkkeihin. Ei ole yksikkötestejä tai integraatiotestejä suoritettavaksi. Validointi perustuu pääasiassa:
- Koodiesimerkkien manuaaliseen testaukseen
- GitHub Actions -työnkulkuihin Markdown-validointia varten
- Yhteisön arviointiin opetusmateriaalista

## Pull Request -ohjeet

### Ennen lähettämistä

1. Testaa koodimuutokset sekä Pythonilla että TypeScriptillä, kun mahdollista
2. Suorita Markdown-validointi (laukaistaan automaattisesti PR:ssä)
3. Varmista, että seurantatunnukset ovat kaikissa Microsoftin URL-osoitteissa
4. Tarkista, että suhteelliset linkit ovat kelvollisia
5. Varmista, että kuvat on viitattu oikein

### PR:n otsikkomuoto

- Käytä kuvaavia otsikoita: `[Lesson 06] Korjaa Python-esimerkin kirjoitusvirhe` tai `Päivitä README oppitunnille 08`
- Viittaa ongelmanumeroihin, kun mahdollista: `Fixes #123`

### PR:n kuvaus

- Selitä, mitä muutettiin ja miksi
- Linkitä liittyviin ongelmiin
- Koodimuutosten osalta kerro, mitkä esimerkit testattiin
- Käännös-PR:ssä sisällytä kaikki tiedostot täydellistä käännöstä varten

### Osallistumisvaatimukset

- Allekirjoita Microsoft CLA (automaattisesti ensimmäisessä PR:ssä)
- Haaroita arkisto omaan tiliisi ennen muutosten tekemistä
- Yksi PR per looginen muutos (älä yhdistä liittymättömiä korjauksia)
- Pidä PR:t keskittyneinä ja pieninä, kun mahdollista

## Yleiset työnkulut

### Uuden koodiesimerkin lisääminen

1. Siirry oikeaan oppituntihakemistoon
2. Luo esimerkki `python/` tai `typescript/` alihakemistoon
3. Noudata nimeämiskäytäntöä: `{provider}-{example-name}.{py|ts|js}`
4. Testaa oikeilla API-tunnuksilla
5. Dokumentoi uudet ympäristömuuttujat oppitunnin README-tiedostossa

### Dokumentaation päivittäminen

1. Muokkaa README.md-tiedostoa oppituntihakemistossa
2. Noudata Markdown-ohjeita (seurantatunnukset, suhteelliset linkit)
3. Käännösten päivitykset hoidetaan GitHub Actionsilla (älä muokkaa käsin)
4. Testaa, että kaikki linkit ovat kelvollisia

### Työskentely Dev Containerien kanssa

1. Arkisto sisältää `.devcontainer/devcontainer.json`-tiedoston
2. Post-create-skripti asentaa Python-riippuvuudet automaattisesti
3. Python- ja Jupyter-laajennukset ovat esikonfiguroituja
4. Ympäristö perustuu `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Julkaisu ja jakelu

Tämä on oppimisarkisto - ei ole julkaisuprosessia. Kurssimateriaali kulutetaan seuraavilla tavoilla:

1. **GitHub-arkisto**: Suora pääsy koodiin ja dokumentaatioon
2. **GitHub Codespaces**: Välitön kehitysympäristö esikonfiguroidulla asetuksella
3. **Microsoft Learn**: Sisältöä voidaan syndikoida viralliselle oppimisalustalle
4. **docsify**: Dokumentaatiosivusto, joka rakennetaan Markdownista (katso `docsifytopdf.js` ja `package.json`)

### Dokumentaatiosivuston rakentaminen

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Vianmääritys

### Yleiset ongelmat

**Python-tuontivirheet**:
- Varmista, että virtuaaliympäristö on aktivoitu
- Suorita `pip install -r requirements.txt`
- Tarkista, että Python-versio on 3.9+

**TypeScript-käännösvirheet**:
- Suorita `npm install` sovelluksen hakemistossa
- Tarkista, että Node.js-versio on yhteensopiva
- Tyhjennä `node_modules` ja asenna uudelleen tarvittaessa

**API-todennusvirheet**:
- Varmista, että `.env`-tiedosto on olemassa ja sisältää oikeat arvot
- Tarkista, että API-avaimet ovat voimassa eivätkä vanhentuneet
- Varmista, että URL-osoitteet ovat oikein alueellesi

**Puuttuvat ympäristömuuttujat**:
- Kopioi `.env.copy` tiedostoon `.env`
- Täytä kaikki tarvittavat arvot oppitunnille, jota työstät
- Käynnistä sovellus uudelleen `.env`-päivityksen jälkeen

## Lisäresurssit

- [Kurssin asennusopas](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Osallistumisohjeet](./CONTRIBUTING.md)
- [Toimintaohjeet](./CODE_OF_CONDUCT.md)
- [Tietoturvapolitiikka](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Kokoelma edistyneitä koodiesimerkkejä](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projektikohtaiset huomiot

- Tämä on **opetusarkisto**, joka keskittyy oppimiseen, ei tuotantokoodiin
- Esimerkit ovat tarkoituksella yksinkertaisia ja keskittyvät käsitteiden opettamiseen
- Koodin laatu tasapainotetaan opetuksellisen selkeyden kanssa
- Jokainen oppitunti on itsenäinen ja voidaan suorittaa erikseen
- Arkisto tukee useita API-palveluntarjoajia: Azure OpenAI, OpenAI ja GitHub Models
- Sisältö on monikielistä automaattisten käännöstyönkulkujen avulla
- Aktiivinen yhteisö Discordissa kysymyksiä ja tukea varten

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.