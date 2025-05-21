<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:29:28+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "fi"
}
-->
# Kurssin Aloittaminen

Olemme todella innoissamme, että aloitat tämän kurssin ja näet, mitä inspiroidut rakentamaan Generatiivisen tekoälyn avulla!

Menestyksesi varmistamiseksi tämä sivu esittelee asennusvaiheet, tekniset vaatimukset ja mistä saat apua tarvittaessa.

## Asennusvaiheet

Aloittaaksesi tämän kurssin, sinun tulee suorittaa seuraavat vaiheet.

### 1. Haarauta tämä Repo

[Haarauta tämä koko repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) omaan GitHub-tiliisi voidaksesi muuttaa koodia ja suorittaa haasteet. Voit myös [tähti (🌟) tätä repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) helpottaaksesi sen ja siihen liittyvien repositorion löytämistä.

### 2. Luo kooditila

Välttääksesi riippuvuusongelmat koodin suorittamisen aikana, suosittelemme kurssin suorittamista [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) -palvelussa.

Tämä voidaan luoda valitsemalla `Code` -vaihtoehto haarautetusta versiostasi tästä reposta ja valitsemalla **Codespaces**-vaihtoehto.

![Dialogi, joka näyttää painikkeet kooditilan luomiseksi](../../../00-course-setup/images/who-will-pay.webp)

### 3. API-avaimiesi säilyttäminen

API-avaimiesi turvallinen säilyttäminen on tärkeää minkä tahansa sovelluksen rakentamisessa. Suosittelemme, ettet tallenna API-avaimia suoraan koodiisi. Näiden tietojen sitominen julkiseen repositorioon voi aiheuttaa turvallisuusongelmia ja jopa ei-toivottuja kustannuksia, jos niitä käyttää pahantahtoinen henkilö.
Tässä on vaiheittainen opas, kuinka luodaan `.env`-tiedosto Pythonille ja lisätään `GITHUB_TOKEN`:

1. **Siirry projektihakemistoon**: Avaa terminaali tai komentokehote ja siirry projektin juurihakemistoon, jossa haluat luoda `.env`-tiedoston.

   ```bash
   cd path/to/your/project
   ```

2. **Luo `.env`-tiedosto**: Käytä haluamaasi tekstieditoria luodaksesi uuden tiedoston nimeltä `.env`. Jos käytät komentoriviä, voit käyttää `touch` (on Unix-based systems) or `echo` (Windowsissa):

   Unix-pohjaiset järjestelmät:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Muokkaa `.env`-tiedostoa**: Avaa `.env`-tiedosto tekstieditorissa (esim. VS Code, Notepad++ tai jokin muu editori). Lisää seuraava rivi tiedostoon, korvaten `your_github_token_here` todellisella GitHub-tunnuksellasi:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Tallenna tiedosto**: Tallenna muutokset ja sulje tekstieditori.

5. **Asenna `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv`-paketti ladataksesi ympäristömuuttujat `.env`-tiedostosta Python-sovellukseesi. Voit asentaa sen käyttämällä `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Lataa ympäristömuuttujat Python-skriptissäsi**: Python-skriptissäsi käytä `python-dotenv`-pakettia ladataksesi ympäristömuuttujat `.env`-tiedostosta:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Siinä kaikki! Olet onnistuneesti luonut `.env`-tiedoston, lisännyt GitHub-tunnuksesi ja ladannut sen Python-sovellukseesi.

## Kuinka ajaa paikallisesti tietokoneellasi

Jotta voit ajaa koodia paikallisesti tietokoneellasi, sinulla tulisi olla jokin versio [Pythonista asennettuna](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Käyttääksesi repositoriota, sinun tulee kloonata se:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kun kaikki on tarkistettu, voit aloittaa!

## Valinnaiset vaiheet

### Miniconda-asennus

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) on kevyt asennusohjelma [Condan](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonin sekä muutamien pakettien asentamiseen.
Conda itse on paketinhallintaohjelma, joka tekee helpon eri Python [**virtuaaliympäristöjen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ja pakettien asennuksen ja vaihtamisen välillä. Se on myös hyödyllinen sellaisten pakettien asentamisessa, joita ei ole saatavilla `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Täytä ympäristötiedostosi alla olevalla koodinpätkällä:

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

Jos saat virheitä Condan käytössä, voit asentaa Microsoft AI -kirjastot manuaalisesti seuraavalla komennolla terminaalissa.

```
conda install -c microsoft azure-ai-ml
```

Ympäristötiedosto määrittää tarvitsemamme riippuvuudet. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` on uusin Pythonin pääversio.

Kun tämä on tehty, voit luoda Conda-ympäristösi suorittamalla alla olevat komennot komentorivillä/terminaalissa

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Katso [Condan ympäristöopas](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), jos kohtaat ongelmia.

### Visual Studio Coden käyttö Python-tuen laajennuksella

Suosittelemme käyttämään [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) -editoria, jossa on [Python-tuen laajennus](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) asennettuna tätä kurssia varten. Tämä on kuitenkin enemmän suositus kuin ehdoton vaatimus.

> **Huom**: Avaamalla kurssin repositorion VS Codessa, sinulla on mahdollisuus asettaa projekti konttiin. Tämä johtuu kurssin repositorion sisällä olevasta [erityisestä `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) -hakemistosta. Lisää tästä myöhemmin.

> **Huom**: Kun kloonaat ja avaat hakemiston VS Codessa, se ehdottaa automaattisesti Python-tuen laajennuksen asentamista.

> **Huom**: Jos VS Code ehdottaa repositorion uudelleenavaamista kontissa, hylkää tämä pyyntö käyttääksesi paikallisesti asennettua Python-versiota.

### Jupyterin käyttö selaimessa

Voit myös työskennellä projektin parissa käyttämällä [Jupyter-ympäristöä](https://jupyter.org?WT.mc_id=academic-105485-koreyst) suoraan selaimessasi. Sekä klassinen Jupyter että [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) tarjoavat miellyttävän kehitysympäristön ominaisuuksilla kuten automaattinen täydennys, koodin korostus jne.

Aloittaaksesi Jupyterin paikallisesti, siirry terminaaliin/komentoriville, navigoi kurssihakemistoon ja suorita:

```bash
jupyter notebook
```

tai

```bash
jupyterhub
```

Tämä käynnistää Jupyter-instanssin ja URL-osoite sen käyttöön näytetään komentorivi-ikkunassa.

Kun pääset URL-osoitteeseen, sinun pitäisi nähdä kurssin sisältö ja pystyä navigoimaan mihin tahansa `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md`-tiedostoon, jossa voit tarkastella koodia ja tulosteita.

## Azure OpenAI-palvelun käyttö ensimmäistä kertaa

Jos käytät Azure OpenAI-palvelua ensimmäistä kertaa, seuraa tätä opasta siitä, kuinka [luoda ja ottaa käyttöön Azure OpenAI-palveluresurssi.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API:n käyttö ensimmäistä kertaa

Jos käytät OpenAI API:a ensimmäistä kertaa, seuraa opasta siitä, kuinka [luoda ja käyttää käyttöliittymää.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Tapaa Muita Oppijoita

Olemme luoneet kanavia virallisessa [AI Community Discord -palvelimessa](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) muiden oppijoiden tapaamiseen. Tämä on loistava tapa verkostoitua muiden samankaltaisten yrittäjien, rakentajien, opiskelijoiden ja kaikkien kanssa, jotka haluavat kehittää Generatiivista tekoälyä.

[![Liity discord-kanavaan](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektitiimi on myös tällä Discord-palvelimella auttamassa oppijoita.

## Osallistu

Tämä kurssi on avoimen lähdekoodin hanke. Jos näet parannuskohteita tai ongelmia, luo [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) tai kirjaa [GitHub-ongelma](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektitiimi seuraa kaikkia osallistumisia. Osallistuminen avoimeen lähdekoodiin on mahtava tapa rakentaa uraasi Generatiivisessa tekoälyssä.

Useimmat osallistumiset vaativat sinua hyväksymään Contributor License Agreement (CLA) -sopimuksen, jossa ilmoitat, että sinulla on oikeus ja todellakin annat meille oikeudet käyttää panostasi. Lisätietoja löytyy [CLA, Contributor License Agreement -verkkosivustolta](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Tärkeää: kun käännät tekstiä tässä repossa, varmista, ettet käytä konekäännöstä. Varmistamme käännökset yhteisön kautta, joten ole hyvä ja osallistu käännöksiin vain kielissä, joissa olet taitava.

Kun lähetät pull requestin, CLA-bot automaattisesti määrittää, tarvitsetko CLA:n ja koristelee PR:n asianmukaisesti (esim. etiketti, kommentti). Seuraa vain botin antamia ohjeita. Sinun tarvitsee tehdä tämä vain kerran kaikissa repositorioissa, jotka käyttävät CLA:ta.

Tämä projekti on omaksunut [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Lisätietoja saat lukemalla Code of Conduct FAQ tai ottamalla yhteyttä [Email opencode](opencode@microsoft.com) lisäkysymyksillä tai kommenteilla.

## Aloitetaan

Nyt kun olet suorittanut tarvittavat vaiheet kurssin suorittamiseksi, aloitetaan [Johdannolla Generatiiviseen tekoälyyn ja LLM:iin](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä AI-käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomaa, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi katsoa olevan auktoritatiivinen lähde. Tärkeää tietoa varten suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.