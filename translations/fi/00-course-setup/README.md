<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:12:04+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "fi"
}
-->
# Aloittaminen tällä kurssilla

Olemme todella innoissamme, että aloitat tämän kurssin ja näet, mitä innostavaa voit rakentaa Generatiivisen tekoälyn avulla!

Varmistaaksesi menestyksesi, tällä sivulla käydään läpi asennusvaiheet, tekniset vaatimukset ja mistä saat apua tarvittaessa.

## Asennusvaiheet

Aloittaaksesi kurssin suorittamisen sinun tulee tehdä seuraavat vaiheet.

### 1. Forkkaa tämä repositorio

[Forkkaa koko tämä repositorio](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) omaan GitHub-tiliisi, jotta voit muokata koodia ja suorittaa haasteet. Voit myös [tähtiä (🌟) tämän repositorion](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), jotta löydät sen ja siihen liittyvät repositoriot helpommin.

### 2. Luo codespace

Välttääksesi riippuvuusongelmia koodia ajettaessa, suosittelemme suorittamaan tämän kurssin [GitHub Codespacesissa](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Codespace luodaan valitsemalla `Code`-valikko forkkaamastasi repositoriosta ja valitsemalla **Codespaces**-vaihtoehto.

![Dialogi, jossa näkyy painikkeet codespacen luomiseen](../../../00-course-setup/images/who-will-pay.webp)

### 3. API-avainten tallentaminen

API-avainten turvallinen säilyttäminen on tärkeää minkä tahansa sovelluksen rakentamisessa. Emme suosittele tallentamaan API-avaimia suoraan koodiin. Julkiseen repositorioon tallentaminen voi aiheuttaa tietoturvaongelmia ja jopa ei-toivottuja kustannuksia, jos joku väärinkäyttää avaimia.

Tässä on vaiheittainen ohje, miten luoda `.env`-tiedosto Pythonille ja lisätä `GITHUB_TOKEN`:

1. **Siirry projektihakemistoon**: Avaa terminaali tai komentokehote ja siirry projektisi juurihakemistoon, johon haluat luoda `.env`-tiedoston.

   ```bash
   cd path/to/your/project
   ```

2. **Luo `.env`-tiedosto**: Käytä haluamaasi tekstieditoria luodaksesi uusi tiedosto nimeltä `.env`. Jos käytät komentoriviä, voit käyttää `touch` (Unix-järjestelmissä) tai `echo` (Windowsissa):

   Unix-järjestelmät:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Muokkaa `.env`-tiedostoa**: Avaa `.env`-tiedosto tekstieditorissa (esim. VS Code, Notepad++ tai muu editori). Lisää tiedostoon seuraava rivi, korvaten `your_github_token_here` omalla GitHub-tokenillasi:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Tallenna tiedosto**: Tallenna muutokset ja sulje editori.

5. **Asenna `python-dotenv`**: Jos et ole vielä asentanut, sinun tulee asentaa `python-dotenv`-paketti, jotta voit ladata ympäristömuuttujat `.env`-tiedostosta Python-sovellukseesi. Asennus onnistuu `pip`-komennolla:

   ```bash
   pip install python-dotenv
   ```

6. **Lataa ympäristömuuttujat Python-skriptissäsi**: Käytä Python-skriptissäsi `python-dotenv`-pakettia ladataksesi ympäristömuuttujat `.env`-tiedostosta:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Siinä se! Olet onnistuneesti luonut `.env`-tiedoston, lisännyt GitHub-tokenisi ja ladannut sen Python-sovellukseesi.

## Kuinka suorittaa paikallisesti omalla tietokoneella

Jos haluat suorittaa koodin paikallisesti omalla tietokoneellasi, sinun tulee olla asennettuna jokin versio [Pythonista](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Käyttääksesi repositoriota sinun tulee kloonata se:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kun olet saanut kaiken valmiiksi, voit aloittaa!

## Valinnaiset vaiheet

### Minicondan asentaminen

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) on kevyt asennustyökalu [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonin ja muutamien pakettien asentamiseen. Conda on pakettienhallintaohjelma, joka helpottaa erilaisten Python [**virtuaaliympäristöjen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ja pakettien hallintaa. Se on myös hyödyllinen pakettien asentamiseen, joita ei ole saatavilla `pip`-komennolla.

Voit seurata [MiniConda asennusohjetta](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) asentaaksesi sen.

Kun Miniconda on asennettu, sinun tulee kloonata [repositorio](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jos et ole vielä tehnyt sitä).

Seuraavaksi sinun tulee luoda virtuaaliympäristö. Condalla tämä tehdään luomalla uusi ympäristötiedosto (_environment.yml_). Jos seuraat kurssia Codespacesissa, luo tämä `.devcontainer`-hakemistoon, eli `.devcontainer/environment.yml`.

Täytä ympäristötiedosto alla olevalla koodinpätkällä:

```yml
name: <environment-name>
channels:
  - defaults
  - microsoft
dependencies:
  - python=<python-version>
  - openai
  - python-dotenv
  - pip
  - pip:
      - azure-ai-ml
```

Jos saat virheitä condaa käyttäessäsi, voit asentaa Microsoft AI Libraries -kirjastot manuaalisesti seuraavalla komennolla terminaalissa.

```
conda install -c microsoft azure-ai-ml
```

Ympäristötiedosto määrittelee tarvitsemamme riippuvuudet. `<environment-name>` tarkoittaa nimeä, jonka haluat antaa Conda-ympäristöllesi, ja `<python-version>` on Pythonin versio, jota haluat käyttää, esimerkiksi `3` on uusin pääversio.

Kun tämä on tehty, voit luoda Conda-ympäristösi suorittamalla alla olevat komennot komentorivillä/terminaalissa:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Katso tarvittaessa [Conda environments -opas](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Visual Studio Coden käyttäminen Python-laajennuksella

Suosittelemme käyttämään [Visual Studio Codea (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) tämän kurssin editorina yhdessä [Python-laajennuksen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) kanssa. Tämä on kuitenkin enemmän suositus kuin pakollinen vaatimus.

> **Huom:** Kun avaat kurssin repositorion VS Codessa, sinulla on mahdollisuus asentaa projekti konttiin. Tämä johtuu kurssin repositoriossa olevasta [erityisestä `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) -kansiosta. Tästä lisää myöhemmin.

> **Huom:** Kun kloonaat ja avaat hakemiston VS Codessa, se ehdottaa automaattisesti Python-laajennuksen asentamista.

> **Huom:** Jos VS Code ehdottaa repositorion uudelleenavaamista kontissa, hylkää pyyntö, jos haluat käyttää paikallisesti asennettua Python-versiota.

### Jupyterin käyttäminen selaimessa

Voit myös työskennellä projektin parissa käyttämällä [Jupyter-ympäristöä](https://jupyter.org?WT.mc_id=academic-105485-koreyst) suoraan selaimessasi. Sekä klassinen Jupyter että [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) tarjoavat miellyttävän kehitysympäristön, jossa on mm. automaattinen täydennys ja koodin korostus.

Aloittaaksesi Jupyteriä paikallisesti, siirry terminaaliin/komentoriville, mene kurssihakemistoon ja suorita:

```bash
jupyter notebook
```

tai

```bash
jupyterhub
```

Tämä käynnistää Jupyter-instanssin, ja pääsyosoite näytetään komentorivillä.

Kun avaat osoitteen, näet kurssin sisällön ja voit siirtyä mihin tahansa `*.ipynb`-tiedostoon, esimerkiksi `08-building-search-applications/python/oai-solution.ipynb`.

### Suorittaminen kontissa

Vaihtoehtona kaiken asentamiselle omalle koneelle tai Codespaceen on käyttää [konttia](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Kurssin repositoriossa oleva erityinen `.devcontainer`-kansio mahdollistaa VS Coden projektin asentamisen konttiin. Codespacesin ulkopuolella tämä vaatii Dockerin asentamisen, ja rehellisesti sanottuna se vaatii hieman työtä, joten suosittelemme tätä vain, jos sinulla on kokemusta konttien kanssa työskentelystä.

Yksi parhaista tavoista pitää API-avaimesi turvassa GitHub Codespacesissa on käyttää Codespace Secrets -ominaisuutta. Tutustu [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) -oppaaseen saadaksesi lisätietoja.

## Oppitunnit ja tekniset vaatimukset

Kurssilla on 6 konseptituntia ja 6 koodausoppituntia.

Koodausoppitunneilla käytämme Azure OpenAI Servicea. Sinun tulee saada pääsy Azure OpenAI -palveluun ja API-avain koodin suorittamista varten. Voit hakea pääsyä [täyttämällä tämän hakemuksen](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Hakemuksen käsittelyn aikana jokaisella koodausoppitunnilla on myös `README.md`-tiedosto, jossa voit tarkastella koodia ja tuloksia.

## Azure OpenAI -palvelun ensimmäinen käyttökerta

Jos käytät Azure OpenAI -palvelua ensimmäistä kertaa, seuraa tätä ohjetta, miten [luoda ja ottaa käyttöön Azure OpenAI Service -resurssi.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API:n ensimmäinen käyttökerta

Jos käytät OpenAI API:a ensimmäistä kertaa, seuraa ohjetta, miten [luoda ja käyttää rajapintaa.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Tapaa muita oppijoita

Olemme luoneet kanavia viralliselle [AI Community Discord -palvelimellemme](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) muiden oppijoiden tapaamista varten. Tämä on loistava tapa verkostoitua samanhenkisten yrittäjien, rakentajien, opiskelijoiden ja kaikkien kanssa, jotka haluavat kehittyä Generatiivisen tekoälyn parissa.

[![Liity discord-kanavalle](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektitiimi on myös mukana tässä Discord-palvelimessa auttamassa oppijoita.

## Osallistu

Tämä kurssi on avoimen lähdekoodin hanke. Jos huomaat parannusehdotuksia tai ongelmia, luo [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) tai kirjaa [GitHub-issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektitiimi seuraa kaikkia kontribuutioita. Avoimen lähdekoodin projekteihin osallistuminen on loistava tapa rakentaa uraasi Generatiivisen tekoälyn parissa.

Useimmat kontribuutiot edellyttävät, että hyväksyt Contributor License Agreementin (CLA), jossa vakuutat, että sinulla on oikeus ja myönnät meille oikeudet käyttää panostustasi. Lisätietoja löydät [CLA, Contributor License Agreement -sivustolta](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Tärkeää: kun käännät tekstiä tässä repositoriossa, varmista, ettet käytä konekäännöstä. Tarkistamme käännökset yhteisön avulla, joten ilmoittaudu vapaaehtoiseksi vain kielillä, joissa olet taitava.

Kun lähetät pull requestin, CLA-botti tarkistaa automaattisesti, tarvitsetko CLA:n ja merkitsee PR:n asianmukaisesti (esim. tunnisteella tai kommentilla). Noudata botin ohjeita. Tämä riittää tekemään vain kerran kaikissa CLA:ta käyttävissä repositorioissa.

Tämä projekti on ottanut käyttöön [Microsoft Open Source Code of Conductin](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Lisätietoja löydät Code of Conductin UKK:sta tai ota yhteyttä [Email opencode](opencode@microsoft.com) -osoitteeseen, jos sinulla on lisäkysymyksiä tai kommentteja.

## Aloitetaan

Nyt kun olet suorittanut tarvittavat vaiheet tämän kurssin aloittamiseksi, aloitetaan tutustumalla [Generatiiviseen tekoälyyn ja LLM-malleihin](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.