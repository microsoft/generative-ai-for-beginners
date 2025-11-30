<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T19:41:42+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "fi"
}
-->
# Aloittaminen tämän kurssin kanssa

Olemme todella innoissamme siitä, että aloitat tämän kurssin ja näemme, mitä inspiroidut rakentamaan Generatiivisen tekoälyn avulla!

Tämän sivun avulla varmistamme onnistumisesi: se sisältää asennusvaiheet, tekniset vaatimukset ja ohjeet avun saamiseen tarvittaessa.

## Asennusvaiheet

Aloittaaksesi kurssin, sinun tulee suorittaa seuraavat vaiheet.

### 1. Haarauta tämä repo

[Haarauta tämä koko repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) omaan GitHub-tiliisi, jotta voit muokata koodia ja suorittaa haasteet. Voit myös [merkitä tähdellä (🌟) tämän repon](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), jotta löydät sen ja siihen liittyvät repositoriot helpommin.

### 2. Luo Codespace

Välttääksesi riippuvuusongelmat koodia suoritettaessa, suosittelemme kurssin suorittamista [GitHub Codespacesissa](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Haarautuksessasi: **Code -> Codespaces -> New on main**

![Valintaikkuna, jossa näkyy painikkeet Codespacen luomiseen](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Lisää salaisuus

1. ⚙️ Ratasikoni -> Komentopaletti -> Codespaces: Manage user secret -> Lisää uusi salaisuus.
2. Nimeä OPENAI_API_KEY, liitä avain, Tallenna.

### 3. Mitä seuraavaksi?

| Haluan…             | Siirry…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Aloittaa oppitunnin 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Työskennellä offline-tilassa | [`setup-local.md`](02-setup-local.md)                                   |
| Määrittää LLM-palveluntarjoajan | [`providers.md`](03-providers.md)                                        |
| Tavata muita oppijoita | [Liity Discord-kanavallemme](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Vianmääritys

| Oire                                      | Korjaus                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| Kontin rakentaminen kestää yli 10 minuuttia | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Pääte ei kiinnittynyt; klikkaa **+** ➜ *bash*                    |
| `401 Unauthorized` OpenAI:lta            | Väärä / vanhentunut `OPENAI_API_KEY`                            |
| VS Code näyttää “Dev container mounting…” | Päivitä selaimen välilehti—Codespaces menettää joskus yhteyden   |
| Notebook-ydin puuttuu                    | Notebook-valikko ➜ **Kernel ▸ Select Kernel ▸ Python 3**         |

   Unix-pohjaiset järjestelmät:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Muokkaa `.env`-tiedostoa**: Avaa `.env`-tiedosto tekstieditorissa (esim. VS Code, Notepad++ tai mikä tahansa muu editori). Lisää seuraava rivi tiedostoon korvaten `your_github_token_here` oikealla GitHub-tunnuksellasi:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Tallenna tiedosto**: Tallenna muutokset ja sulje tekstieditori.

5. **Asenna `python-dotenv`**: Jos et ole vielä tehnyt sitä, sinun täytyy asentaa `python-dotenv`-paketti, jotta ympäristömuuttujat voidaan ladata `.env`-tiedostosta Python-sovellukseesi. Voit asentaa sen käyttämällä `pip`-komentoa:

   ```bash
   pip install python-dotenv
   ```

6. **Lataa ympäristömuuttujat Python-skriptissäsi**: Käytä Python-skriptissäsi `python-dotenv`-pakettia ympäristömuuttujien lataamiseen `.env`-tiedostosta:

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

## Kuinka suorittaa koodi paikallisesti tietokoneellasi

Suorittaaksesi koodin paikallisesti tietokoneellasi, sinulla tulee olla jokin versio [Pythonista asennettuna](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Käyttääksesi repositoriota, sinun täytyy kloonata se:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kun kaikki on ladattu, voit aloittaa!

## Valinnaiset vaiheet

### Minicondan asentaminen

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) on kevyt asennusohjelma [Condan](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonin ja muutaman paketin asentamiseen.
Conda itsessään on pakettienhallintaohjelma, joka helpottaa erilaisten Pythonin [**virtuaaliympäristöjen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ja pakettien asennusta ja hallintaa. Se on myös kätevä sellaisten pakettien asentamiseen, joita ei ole saatavilla `pip`-komennolla.

Voit seurata [Miniconda-asennusopasta](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) asentaaksesi sen.

Kun Miniconda on asennettu, sinun tulee kloonata [repositorio](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jos et ole jo tehnyt sitä).

Seuraavaksi sinun tulee luoda virtuaaliympäristö. Voit tehdä tämän Condalla luomalla uuden ympäristötiedoston (_environment.yml_). Jos seuraat ohjeita Codespacesissa, luo tämä tiedosto `.devcontainer`-hakemistoon, eli `.devcontainer/environment.yml`.

Täytä ympäristötiedosto alla olevalla koodilla:

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

Jos kohtaat virheitä Condan käytössä, voit asentaa Microsoft AI -kirjastot manuaalisesti seuraavalla komennolla terminaalissa.

```
conda install -c microsoft azure-ai-ml
```

Ympäristötiedosto määrittää tarvittavat riippuvuudet. `<environment-name>` viittaa nimeen, jonka haluat antaa Conda-ympäristöllesi, ja `<python-version>` on Pythonin versio, jota haluat käyttää, esimerkiksi `3` on uusin Pythonin pääversio.

Kun tämä on tehty, voit luoda Conda-ympäristön suorittamalla alla olevat komennot komentorivillä/terminaalissa:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Jos kohtaat ongelmia, tutustu [Condan ympäristöjen oppaaseen](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Visual Studio Coden käyttö Python-tuen laajennuksella

Suosittelemme käyttämään [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) -editoria, jossa on [Python-tuen laajennus](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) asennettuna tätä kurssia varten. Tämä on kuitenkin vain suositus, ei ehdoton vaatimus.

> **Huomio**: Kun avaat kurssin repositorion VS Codessa, sinulla on mahdollisuus asettaa projekti konttiin. Tämä johtuu kurssin repositoriossa olevasta [erityisestä `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) -hakemistosta. Lisää tästä myöhemmin.

> **Huomio**: Kun kloonaat ja avaat hakemiston VS Codessa, se ehdottaa automaattisesti Python-tuen laajennuksen asentamista.

> **Huomio**: Jos VS Code ehdottaa repositorion avaamista kontissa, hylkää tämä pyyntö käyttääksesi paikallisesti asennettua Python-versiota.

### Jupyterin käyttö selaimessa

Voit myös työskennellä projektin parissa [Jupyter-ympäristössä](https://jupyter.org?WT.mc_id=academic-105485-koreyst) suoraan selaimessasi. Sekä perinteinen Jupyter että [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) tarjoavat miellyttävän kehitysympäristön, jossa on esimerkiksi automaattinen täydennys ja koodin korostus.

Aloittaaksesi Jupyterin paikallisesti, siirry terminaaliin/komentoriville, navigoi kurssihakemistoon ja suorita:

```bash
jupyter notebook
```

tai

```bash
jupyterhub
```

Tämä käynnistää Jupyter-instanssin, ja URL-osoite sen käyttämiseen näytetään komentorivin ikkunassa.

Kun pääset URL-osoitteeseen, sinun pitäisi nähdä kurssin sisältö ja pystyä navigoimaan mihin tahansa `*.ipynb`-tiedostoon. Esimerkiksi `08-building-search-applications/python/oai-solution.ipynb`.

### Suorittaminen kontissa

Vaihtoehtona kaiken asettamiselle tietokoneellesi tai Codespaceen on käyttää [konttia](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Kurssin repositorion erityinen `.devcontainer`-kansio mahdollistaa projektin asettamisen konttiin VS Codessa. Codespacesin ulkopuolella tämä vaatii Dockerin asennuksen, ja rehellisesti sanottuna se vaatii hieman työtä, joten suosittelemme tätä vain niille, joilla on kokemusta konttien kanssa työskentelystä.

Yksi parhaista tavoista pitää API-avaimesi turvassa käyttäessäsi GitHub Codespacesia on käyttää Codespace Secrets -ominaisuutta. Seuraa [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) -opasta oppiaksesi lisää tästä.

## Oppitunnit ja tekniset vaatimukset

Kurssi sisältää 6 konseptioppituntia ja 6 koodausoppituntia.

Koodausoppitunneilla käytämme Azure OpenAI -palvelua. Tarvitset pääsyn Azure OpenAI -palveluun ja API-avaimen koodin suorittamiseen. Voit hakea pääsyä [täyttämällä tämän hakemuksen](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Kun odotat hakemuksesi käsittelyä, jokainen koodausoppitunti sisältää myös `README.md`-tiedoston, jossa voit tarkastella koodia ja tuloksia.

## Azure OpenAI -palvelun käyttö ensimmäistä kertaa

Jos käytät Azure OpenAI -palvelua ensimmäistä kertaa, seuraa tätä opasta siitä, miten [luoda ja ottaa käyttöön Azure OpenAI -palveluresurssi.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API:n käyttö ensimmäistä kertaa

Jos käytät OpenAI API:ta ensimmäistä kertaa, seuraa opasta siitä, miten [luoda ja käyttää käyttöliittymää.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Tapaa muita oppijoita

Olemme luoneet kanavia viralliselle [AI Community Discord -palvelimellemme](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), jotta voit tavata muita oppijoita. Tämä on loistava tapa verkostoitua muiden samanhenkisten yrittäjien, rakentajien, opiskelijoiden ja kaikkien generatiivisesta tekoälystä kiinnostuneiden kanssa.

[![Liity Discord-kanavalle](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektitiimi on myös tällä Discord-palvelimella auttamassa oppijoita.

## Osallistu

Tämä kurssi on avoimen lähdekoodin hanke. Jos huomaat parannettavaa tai ongelmia, luo [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) tai kirjaa [GitHub-ongelma](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektitiimi seuraa kaikkia kontribuutioita. Avoimeen lähdekoodiin osallistuminen on upea tapa rakentaa uraa generatiivisen tekoälyn parissa.

Useimmat kontribuutiot vaativat, että hyväksyt Contributor License Agreement (CLA) -sopimuksen, jossa vakuutat, että sinulla on oikeus ja halu antaa meille oikeudet käyttää kontribuutiotasi. Lisätietoja saat [CLA, Contributor License Agreement -sivustolta](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Tätä projektia koskee [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Lisätietoja saat lukemalla Code of Conduct FAQ tai ottamalla yhteyttä [Email opencode](opencode@microsoft.com) mahdollisten lisäkysymysten tai kommenttien osalta.

## Aloitetaan!
Nyt kun olet suorittanut tarvittavat vaiheet tämän kurssin loppuun saattamiseksi, aloitetaan tutustumalla [Generatiiviseen tekoälyyn ja LLM:iin](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.