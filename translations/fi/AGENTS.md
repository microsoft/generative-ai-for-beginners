# AGENTS.md

## Projektin yleiskatsaus

Tämä varasto sisältää kattavan 21 oppitunnin opetussuunnitelman, joka opettaa generatiivisen tekoälyn perusteet ja sovelluskehityksen. Kurssi on suunnattu aloittelijoille ja kattaa kaiken peruskäsitteistä tuotantovalmiiden sovellusten rakentamiseen.

**Keskeiset teknologiat:**
- Python 3.9+ kirjastoilla: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript Node.js:llä ja kirjastoilla: `openai` (Azure OpenAI v1-päätepiste + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry -mallit)
- Azure OpenAI Service, OpenAI API ja Microsoft Foundry -mallit (GitHub Models poistuu käytöstä heinäkuun 2026 lopussa)
- Jupyter-muistikirjat interaktiiviseen oppimiseen
- Dev Containerit johdonmukaiseen kehitysympäristöön

**Varaston rakenne:**
- 21 numeroitua oppituntikansiota (00–21), jotka sisältävät README-tiedostot, koodiesimerkit ja tehtävät
- Useita toteutuksia: Python, TypeScript ja joskus .NET-esimerkit
- Käännöskansio, jossa yli 40 kieliversiota
- Keskitetty konfiguraatio `.env`-tiedoston kautta (käytä `.env.copy` mallina)

## Asennuskomennot

### Varaston alkuasetukset

```bash
# Kopioi arkisto
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
# macOS/Linuxissa:
source venv/bin/activate
# Windowsissa:
venv\Scripts\activate

# Asenna riippuvuudet
pip install -r requirements.txt
```

### Node.js/TypeScript-asennus

```bash
# Asenna juuritason riippuvuudet (dokumentaatiotyökaluille)
npm install

# Yksittäisiä oppituntien TypeScript-esimerkkejä varten siirry tiettyyn oppituntiin:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container -asennus (suositeltu)

Varasto sisältää `.devcontainer`-konfiguraation GitHub Codespaces- tai VS Code Dev Containers -käyttöä varten:

1. Avaa varasto GitHub Codespacesissa tai VS Code:n Dev Containers -laajennuksella
2. Dev Container asentaa automaattisesti:
   - Python-riippuvuudet `requirements.txt` -tiedostosta
   - Suorittaa post-create-skriptin (`.devcontainer/post-create.sh`)
   - Määrittää Jupytern ytimen

## Kehitystyön työnkulku

### Ympäristömuuttujat

Kaikki API-kutsuja vaativat oppitunnit käyttävät `.env`-tiedostoon määriteltyjä ympäristömuuttujia:

- `OPENAI_API_KEY` - OpenAI API:lle
- `AZURE_OPENAI_API_KEY` - Azure OpenAI:lle Microsoft Foundryssa (Azure OpenAI Service on osa Microsoft Foundrya: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI -päätepisteen URL (Foundryn resurssipäätepiste)
- `AZURE_OPENAI_DEPLOYMENT` - Chat completion -mallin käyttöönoton nimi
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Upotemallin käyttöönoton nimi
- `AZURE_OPENAI_API_VERSION` - API-versio (oletus: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Hugging Face -malleille
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Models -päätepiste (monitoimittajamallikatalogi)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models API-avain (korvaa poistuvan `GITHUB_TOKEN`in)

### Python-esimerkkien suorittaminen

```bash
# Siirry oppituntihakemistoon
cd 06-text-generation-apps/python

# Suorita Python-skripti
python aoai-app.py
```

### TypeScript-esimerkkien suorittaminen

```bash
# Siirry TypeScript-sovelluksen hakemistoon
cd 06-text-generation-apps/typescript/recipe-app

# Käännä TypeScript-koodi
npm run build

# Käynnistä sovellus
npm start
```

### Jupyter-muistikirjojen suorittaminen

```bash
# Käynnistä Jupyter arkiston juuressa
jupyter notebook

# Tai käytä VS Codea Jupyter-laajennuksella
```

### Erilaisten oppituntityyppien käsittely

- **"Learn" -oppitunnit**: Keskittyvät README.md-dokumentaatioon ja käsitteisiin
- **"Build" -oppitunnit**: Sisältävät toimivia koodiesimerkkejä Pythonissa ja TypeScriptissä
- Jokaisella oppitunnilla on README.md, jossa teoriaa, koodin selitykset ja linkit videoihin

## Koodityyliohjeet

### Python

- Käytä `python-dotenv`-kirjastoa ympäristömuuttujien hallintaan
- Tuo `openai` kirjasto API-kutsuja varten
- Käytä `pylint`-työkalua koodin tarkistukseen (joissain esimerkeissä `# pylint: disable=all` yksinkertaisuuden vuoksi)
- Noudata PEP 8 -nimikkeistöä
- Tallenna API-tiedot `.env`-tiedostoon, älä koskaan koodiin

### TypeScript

- Käytä `dotenv`-pakettia ympäristömuuttujien hallintaan
- Tallenna TypeScript-konfiguraatio `tsconfig.json`-tiedostoon jokaista sovellusta varten
- Käytä `openai`-pakettia Azure OpenAI:lle (suuntaa asiakas `/openai/v1/` -päätepisteeseen ja kutsu `client.responses.create`); käytä `@azure-rest/ai-inference` Microsoft Foundry -malleille
- Käytä `nodemon`iä kehitykseen automaattisen uudelleenkäynnistyksen kanssa
- Luo rakennus ennen suorittamista: `npm run build` ja sitten `npm start`

### Yleiset käytännöt

- Pidä koodiesimerkit yksinkertaisina ja opetuksellisina
- Sisällytä kommentteja, jotka selittävät keskeisiä käsitteitä
- Kunkin oppitunnin koodin tulee olla itsenäinen ja suoritettavissa
- Käytä yhtenäistä nimeämiskäytäntöä: `aoai-` prefiksi Azure OpenAI:lle, `oai-` OpenAI API:lle, `githubmodels-` Microsoft Foundry -malleille (perintönä GitHub Models -ajalta)

## Dokumentaatio-ohjeet

### Markdown-tyyli

- Kaikki URL-osoitteet tulee kääriä muotoon `[text](../../url)` ilman ylimääräisiä välilyöntejä
- Relatiiviset linkit alkavat `./` tai `../`
- Kaikkien Microsoftin domaineihin menevien linkkien tulee sisältää seuranta-ID: `?WT.mc_id=academic-105485-koreyst`
- Vältä maakohtaisia paikallisia URL-osoitteita (ei `/en-us/`)
- Kuvia säilytetään `./images` -kansiossa kuvaavilla nimillä
- Käytä tiedostonimissä englanninkielisiä merkkejä, numeroita ja viivoja

### Käännöstuki

- Varasto tukee yli 40 kieltä automatisoidun GitHub Actions -työnkulun avulla
- Käännökset säilytetään `translations/`-kansiossa
- Älä toimita osittaisia käännöksiä
- Konekäännöksiä ei hyväksytä
- Käännetyt kuvat tallennetaan `translated_images/`-kansioon

## Testaus ja validointi

### Ennen lähettämistä tehtävät tarkistukset

Tämä varasto käyttää GitHub Actions -toimintoja validointiin. Ennen PR:n lähettämistä:

1. **Tarkista Markdown-linkit**:
   ```bash
   # validate-markdown.yml-työnkulku tarkistaa:
   # - Rikkinäiset suhteelliset polut
   # - Poluista puuttuvat seuranta-ID:t
   # - URL-osoitteista puuttuvat seuranta-ID:t
   # - Maa-aluekoodilliset URL-osoitteet
   # - Rikkinäiset ulkoiset URL-osoitteet
   ```

2. **Manuaalinen testaus**:
   - Testaa Python-esimerkit: Aktivoi venv ja suorita skriptit
   - Testaa TypeScript-esimerkit: `npm install`, `npm run build`, `npm start`
   - Varmista ympäristömuuttujien oikeellisuus
   - Tarkista API-avainten toimivuus koodiesimerkkien kanssa

3. **Koodiesimerkit**:
   - Varmista, että kaikki koodi suorittuu ilman virheitä
   - Testaa sekä Azure OpenAI että OpenAI API:tä, kun sovellettavissa
   - Varmista, että esimerkit toimivat Microsoft Foundry -mallien kanssa, missä tuettu

### Ei automatisoituja testejä

Tämä on opetustarkoitukseen tarkoitettu varasto, joka keskittyy opetusmateriaaleihin ja esimerkkeihin. Yksikkö- tai integraatiotestejä ei ole. Validointi perustuu pääasiassa:
- Koodiesimerkkien manuaaliseen testaukseen
- GitHub Actionsin Markdown-validaatioon
- Yhteisön arvioon opetusmateriaalista

## Pull request -ohjeet

### Ennen lähettämistä

1. Testaa koodimuutokset sekä Pythonissa että TypeScriptissä, jos sovellettavissa
2. Suorita Markdownin validointi (käynnistyy automaattisesti PR:ssä)
3. Varmista, että kaikkiin Microsoftin URL-osoitteisiin on lisätty seuranta-ID:t
4. Tarkista, että relatiiviset linkit ovat voimassa
5. Varmista kuvien asianmukainen viittaus

### PR-otsikon muotoilu

- Käytä kuvaavia otsikoita: `[Lesson 06] Fix Python example typo` tai `Update README for lesson 08`
- Viittaa ongelmannumeroihin, kun sovellettavissa: `Fixes #123`

### PR-kuvaus

- Selitä, mitä muutettiin ja miksi
- Linkitä liittyviin ongelmiin
- Koodimuutosten kohdalla ilmoita testatut esimerkit
- Käännös-PR:issä sisällytä kaikki tiedostot täydelliseen käännökseen

### Osallistumisvaatimukset

- Allekirjoita Microsoftin CLA (automaattinen ensimmäisessä PR:ssä)
- Haarauta varasto tilillesi ennen muutosten tekemistä
- Yksi PR loogista muutosta kohden (älä yhdistä epäyhtenäisiä korjauksia)
- Pidä PR:ät keskittyneinä ja pieninä, jos mahdollista

## Yleiset työnkulut

### Uuden koodiesimerkin lisääminen

1. Siirry sopivaan oppituntikansioon
2. Luo esimerkki `python/` tai `typescript/` -alikansioon
3. Noudata nimeämiskäytäntöä: `{provider}-{example-name}.{py|ts|js}`
4. Testaa oikeilla API-tunnisteilla
5. Dokumentoi uudet ympäristömuuttujat oppitunnin README:ssä

### Dokumentaation päivittäminen

1. Muokkaa oppitunnin README.md-tiedostoa
2. Noudata Markdown-ohjeita (seuranta-ID:t, relatiiviset linkit)
3. Käännösten päivitys hoidetaan GitHub Actionsin avulla (älä muokkaa manuaalisesti)
4. Testaa, että kaikki linkit toimivat

### Dev Containerien käyttö

1. Varastossa on `.devcontainer/devcontainer.json`
2. Post-create-skripti asentaa Python-riippuvuudet automaattisesti
3. Python- ja Jupyter-laajennukset ovat esikonfiguroituja
4. Ympäristö perustuu `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Julkaisu ja julkaiseminen

Tämä on oppimiseen tarkoitettu varasto – julkaisuprosessia ei ole. Opetussisältöä käytetään:

1. **GitHub-varasto**: Suora pääsy koodiin ja dokumentaatioon
2. **GitHub Codespaces**: Välitön kehitysympäristö valmiiksi määritettynä
3. **Microsoft Learn**: Sisältö voidaan sijoittaa viralliselle oppimisalustalle
4. **docsify**: Dokumentaatiosivusto rakennettu Markdownista (ks. `docsifytopdf.js` ja `package.json`)

### Dokumentaatiosivuston rakentaminen

```bash
# Luo PDF dokumentaatiosta (tarvittaessa)
npm run convert
```

## Vianmääritys

### Yleiset ongelmat

**Pythonin tuontivirheet**:
- Varmista, että virtuaaliympäristö on aktivoitu
- Suorita `pip install -r requirements.txt`
- Tarkista, että Python-versio on 3.9+

**TypeScriptin käännösvirheet**:
- Suorita `npm install` sovelluskansiossa
- Tarkista Node.js:n yhteensopivuus
- Tyhjennä `node_modules` ja asenna uudelleen tarvittaessa

**API-todennusvirheet**:
- Varmista, että `.env`-tiedosto on olemassa ja arvot oikein
- Tarkista, että API-avaimet ovat voimassa eivätkä vanhentuneet
- Varmista, että päätepisteen URL on oikea alueellesi

**Puuttuvat ympäristömuuttujat**:
- Kopioi `.env.copy` tiedostoksi `.env`
- Täytä kaikki vaaditut arvot oppitunnin mukaan
- Käynnistä sovellus uudelleen `.env`-päivityksen jälkeen

## Lisäresurssit

- [Kurssin asentamisopas](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Osallistumisohjeet](./CONTRIBUTING.md)
- [Toimintakoodi](./CODE_OF_CONDUCT.md)
- [Tietoturvapolitiikka](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Kokoelma edistyneitä koodiesimerkkejä](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projektikohtaiset huomiot

- Tämä on **opetustarkoitukseen tarkoitettu varasto**, ei tuotantokoodi
- Esimerkit ovat tarkoituksella yksinkertaisia ja keskittyvät käsitteiden opettamiseen
- Koodin laatu on tasapainossa opetuksellisen selkeyden kanssa
- Jokainen oppitunti on itsenäinen ja suoritettavissa erikseen
- Varasto tukee useita API-toimittajia: Azure OpenAI, OpenAI, Microsoft Foundry Models sekä offline-toimittajia kuten Foundry Local ja Ollama
- Sisältö on monikielistä automaattisten käännöstyönkulkujen avulla
- Aktiivinen yhteisö Discordissa kysymyksiä ja tukea varten

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->