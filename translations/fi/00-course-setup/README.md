# Aloittaminen tämän kurssin kanssa

Olemme erittäin innoissamme, että aloitat tämän kurssin ja näet, mitä saat inspiraatiota rakentaa Generatiivisen tekoälyn avulla!

Varmistaaksemme menestyksesi, tämä sivu kuvaa asennusvaiheet, tekniset vaatimukset ja mistä saat apua tarvittaessa.

## Asennusvaiheet

Kurssin aloittamiseksi sinun tulee suorittaa seuraavat vaiheet.

### 1. Forkkaa tämä repositorio

[Forkkaa tämä koko repositorio](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) omaan GitHub-tiliisi, jotta voit muokata koodia ja suorittaa haasteet. Voit myös [tähdittää (🌟) tämän repositorion](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) löytääksesi sen ja siihen liittyvät repositoriot helpommin.

### 2. Luo codespace

Välttääksesi riippuvuusongelmia koodia ajettaessa, suosittelemme ajamaan tämän kurssin [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) -ympäristössä.

Forkissasi: **Code -> Codespaces -> New on main**

![Dialogi, jossa näkyy napit codespacen luomiseen](../../../translated_images/fi/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Lisää salaisuus

1. ⚙️ Hammasratas-kuvake -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Nimeä se OPENAI_API_KEY, liitä avaimesi, tallenna.

### 3. Mitä seuraavaksi?

| Haluan…            | Siirry kohtaan…                                                        |
|---------------------|-------------------------------------------------------------------------|
| Aloita Oppitunti 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Työskennellä offline | [`setup-local.md`](02-setup-local.md)                                   |
| Määritä LLM-palveluntarjoaja | [`providers.md`](03-providers.md)                                        |
| Tapaa muita oppijoita | [Liity Discord-ryhmäämme](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Vianmääritys


| Oire                                      | Korjaus                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| Kontin rakentaminen jumissa yli 10 min    | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Pääte ei liittänyt; klikkaa **+** ➜ *bash*                       |
| `401 Unauthorized` OpenAI:ltä              | Väärä/vanhentunut `OPENAI_API_KEY`                               |
| VS Code näyttää “Dev container mounting…” | Päivitä selainvälilehti—Codespaces saattaa joskus menettää yhteyden |
| Notebook-ytin puuttuminen                 | Notebook-valikko ➜ **Kernel ▸ Valitse Kernel ▸ Python 3**         |

   Unix-pohjaiset järjestelmät:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Muokkaa `.env`-tiedostoa**: Avaa `.env`-tiedosto tekstieditorissa (esim. VS Code, Notepad++ tai muu editori). Lisää tiedostoon seuraavat rivit korvaten paikkamerkit omalla Microsoft Foundry Models -päätepisteellä ja avaimella (katso [`providers.md`](03-providers.md) ohjeet niiden hankintaan):

   > **Huom:** GitHub Models (ja sen `GITHUB_TOKEN`-muuttuja) poistuu käytöstä heinäkuun 2026 lopussa. Käytä sen sijaan [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Tallenna tiedosto**: Tallenna tekemäsi muutokset ja sulje tekstieditori.

5. **Asenna `python-dotenv`**: Jos et ole vielä asentanut, sinun täytyy asentaa `python-dotenv`-paketti ympäristömuuttujien lataamista varten Python-sovellukseesi `.env`-tiedostosta. Asenna se käyttämällä `pip`-komentoa:

   ```bash
   pip install python-dotenv
   ```

6. **Lataa ympäristömuuttujat Python-skriptissäsi**: Käytä `python-dotenv`-pakettia Python-koodissasi ladataksesi ympäristömuuttujat `.env`-tiedostosta:

   ```python
   from dotenv import load_dotenv
   import os

   # Lataa ympäristömuuttujat .env-tiedostosta
   load_dotenv()

   # Käytä Microsoft Foundry Models -muuttujia
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Siinä kaikki! Olet luonut `.env`-tiedoston, lisännyt Microsoft Foundry Models -tunnistetietosi ja ladannut ne Python-sovellukseesi.

## Kuinka ajaa paikallisesti omalla tietokoneellasi

Ajaaksesi koodia paikallisesti koneellasi, sinulla tulee olla asennettuna jonkinlainen [Python-versio](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Käyttääksesi repositoriota sinun täytyy kloonata se:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kun olet saanut kaiken valmiiksi, voit aloittaa!

## Valinnaiset vaiheet

### Minicondan asennus

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) on kevyt asentaja [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonin ja joidenkin pakettien asentamiseen.
Conda itsessään on pakettien hallintaohjelma, joka helpottaa eri Python [virtuaaliympäristöjen](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ja pakettien asennusta ja hallintaa. Se on myös hyödyllinen silloin, kun haluat asentaa paketteja, joita ei ole saatavilla `pip`-komennolla.

Voit seurata [MiniConda-asennusohjetta](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) sen määrittämiseksi.

Kun Miniconda on asennettu, sinun tulee kloonata [repositorio](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jos et ole vielä tehnyt niin)

Seuraavaksi sinun tulee luoda virtuaaliympäristö. Conda-ympäristön luomiseksi luo uusi ympäristötiedosto (_environment.yml_). Jos käytät Codespacesia, luo tiedosto `.devcontainer`-hakemistoon, eli `.devcontainer/environment.yml`.

Täytä ympäristötiedosto seuraavalla koodinpätkällä:

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

Jos saat virheitä condaa käytettäessä, voit asentaa Microsoft AI Libraries -kirjastot manuaalisesti komennolla terminaalissa.

```
conda install -c microsoft azure-ai-ml
```

Ympäristötiedosto määrittelee tarvittavat riippuvuudet. `<environment-name>` on Conda-ympäristön nimi ja `<python-version>` Pythonin versio, esimerkiksi `3` on uusin pääversio.

Tämän jälkeen voit luoda Conda-ympäristösi suorittamalla ala olevat komennot komentorivillä/terminaalissa

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer-alihakupolku koskee vain Codespace-asetuksia
conda activate ai4beg
```

Katso [Conda-ympäristöohjeet](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), jos kohtaat ongelmia.

### Visual Studio Coden käyttö Python-laajennuksen kanssa

Suosittelemme kurssille [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) -editorin käyttöä yhdessä [Python-laajennuksen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) kanssa. Tämä on kuitenkin enemmän suositus kuin pakollinen vaatimus.

> **Huom:** Kun avaat kurssin repositorion VS Codessa, voit valita hankkeen ajamisen kontissa. Tämä on mahdollista [erikoisen `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) -hakemiston ansiosta. Tästä lisää myöhemmin.

> **Huom:** Kun kloonaat ja avaat hakemiston VS Codessa, se ehdottaa automaattisesti Python-laajennuksen asentamista.

> **Huom:** Jos VS Code ehdottaa repositorion avaamista uudelleen kontissa, hylkää pyyntö, jos haluat käyttää paikallisesti asennettua Python-versiota.

### Jupyterin käyttö selaimessa

Voit myös työskennellä projektin parissa käyttämällä [Jupyter-ympäristöä](https://jupyter.org?WT.mc_id=academic-105485-koreyst) suoraan selaimessasi. Sekä klassinen Jupyter että [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) tarjoavat miellyttävän kehitysympäristön, jossa on automaattinen täydennys, koodin korostus jne.

Käynnistääksesi Jupytern paikallisesti, mene terminaaliin/komentoriville, siirry kurssihakemistoon ja suorita:

```bash
jupyter notebook
```

tai

```bash
jupyterhub
```

Tämä käynnistää Jupyter-instanssin, ja pääsyosoite näytetään komentorivi-ikkunassa.

Kun käyt osoitteessa, näet kurssin sisällön ja voit selata kaikkia `*.ipynb`-tiedostoja. Esimerkiksi `08-building-search-applications/python/oai-solution.ipynb`.

### Suorittaminen kontissa

Vaihtoehtona oman koneen tai Codespacen käytölle on [kontin](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) käyttö. Kurssin repositorion `.devcontainer`-kansio mahdollistaa VS Coden projektin ajamisen kontissa. Codespacen ulkopuolella kontin käyttö edellyttää Dockerin asennusta ja vie hieman vaivaa, joten suosittelemme tätä vain niille, joilla on kokemusta konteista.

Yksi parhaista tavoista suojata API-avaimesi GitHub Codespacesissa on käyttää Codespace Secrets -ominaisuutta. Lue lisää [Codespacesin salausten hallinnasta](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).


## Oppitunnit ja tekniset vaatimukset

Kurssilla on "Learn" -oppitunnit, jotka selittävät Generatiivisen tekoälyn käsitteitä, ja "Build" -oppitunnit, joissa on käytännön koodiesimerkkejä sekä **Pythonilla** että **TypeScriptille**, kun se on mahdollista.

Koodausoppitunneilla käytämme Azure OpenAI -palvelua Microsoft Foundryssa. Tarvitset Azure-tilauksen ja API-avaimen. Pääsy on avoin - hakuja ei vaadita - joten voit [luoda Microsoft Foundry -resurssin ja ottaa mallin käyttöön](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) saadaksesi päätepisteen ja avaimen.

Jokaisessa koodausoppitunnissa on myös `README.md`-tiedosto, jossa voit katsoa koodia ja tuloksia ajamatta mitään.

## Azure OpenAI -palvelun ensimmäinen käyttökerta

Jos käytät Azure OpenAI -palvelua ensimmäistä kertaa, seuraa tätä ohjetta siitä, miten [luot ja otat käyttöön Azure OpenAI -palvelun resurssin.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API:n ensimmäinen käyttökerta

Jos käytät OpenAI API:a ensimmäistä kertaa, seuraa ohjetta siitä, miten [luot ja käytät rajapintaa.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Tapaa muita oppijoita

Olemme luoneet kanavia viralliselle [AI-yhteisön Discord-palvelimellemme](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) muiden oppijoiden tapaamiseksi. Tämä on loistava tapa verkostoitua muiden samankaltaisten yrittäjien, kehittäjien, opiskelijoiden ja generatiivisen tekoälyn taitojen kehittämisestä kiinnostuneiden kanssa.

[![Liity discord-kanavalle](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektitiimi on myös mukana tässä Discord-palvelimessa auttamassa oppijoita.

## Osallistu

Tämä kurssi on avoimen lähdekoodin hanke. Jos löydät parannettavaa tai ongelmia, luo [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) tai kirjaa [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektitiimi seuraa kaikkia kontribuutioita. Osallistuminen avoimeen lähdekoodiin on loistava tapa rakentaa uraasi generatiivisen tekoälyn parissa.

Useimmat kontribuutiot edellyttävät Contributor License Agreementin (CLA) hyväksymistä, jolla vahvistat, että sinulla on oikeus antaa meille oikeudet käyttää panostustasi. Lisätietoja saat CLA:n verkkosivuilta: [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Tärkeää: Kun käännät tekstejä tässä repositoriossa, varmista, että et käytä konekäännöksiä. Tarkistamme käännökset yhteisön kautta, joten tarjoudu vain kääntämään kieliä, joissa olet sujuva.


Kun lähetät vetopyynnön, CLA-botti määrittää automaattisesti, tarvitseeko sinun toimittaa CLA ja merkitsee PR:n asianmukaisesti (esim. tunniste, kommentti). Noudata vain botin antamia ohjeita. Sinun tarvitsee tehdä tämä vain kerran kaikissa CLA:ta käyttävissä repositorioissa.

Tämä hanke on ottanut käyttöön [Microsoftin avoimen lähdekoodin käytännesäännöt](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Lisätietoja saat lukemalla Käytännesääntöjen UKK:n tai ottamalla yhteyttä sähköpostitse [Email opencode](opencode@microsoft.com) mahdollisissa lisäkysymyksissä tai -kommenteissa.

## Aloitetaan

Nyt kun olet suorittanut tarvittavat vaiheet tämän kurssin suorittamiseksi, aloitetaan saamalla [johdanto Generative AI:hin ja LLM:iin](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->