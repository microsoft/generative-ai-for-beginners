# Tämän kurssin aloitus

Olemme todella innoissamme, että aloitat tämän kurssin ja näet, mitä saat inspiraatiota rakentaa Generatiivisen tekoälyn avulla!

Varmistaaksemme menestyksesi, tällä sivulla kerrotaan asennusvaiheet, tekniset vaatimukset ja mistä saada apua tarvittaessa.

## Asennusvaiheet

Kurssin aloittamiseksi sinun tulee suorittaa seuraavat vaiheet.

### 1. Forkkaa tämä repo

[Forkkaa koko repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) omaan GitHub-tiliisi, jotta voit muokata koodia ja suorittaa haasteet. Voit myös [tähtiä (🌟) tämän repoin](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) helpottaaksesi sen ja siihen liittyvien repoiden löytämistä.

### 2. Luo codespace

Välttääksesi riippuvuusongelmia koodia suoritettaessa suosittelemme tämän kurssin suorittamista [GitHub Codespacesissä](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Forkissasi: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/fi/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Lisää salaisuus

1. ⚙️ Hammasratas-kuvake -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Nimeä OPENAI_API_KEY, liitä avain, Tallenna.

### 3. Mitä seuraavaksi?

| Haluan…            | Mene kohtaan…                                                           |
|---------------------|-------------------------------------------------------------------------|
| Aloita Lesson 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Työskennellä offline | [`setup-local.md`](02-setup-local.md)                                   |
| Asenna LLM-palveluntarjoaja | [`providers.md`](03-providers.md)                                        |
| Tapaa muita oppijoita | [Liity Discordiin](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Vianmääritys


| Oire                                    | Korjaus                                                        |
|----------------------------------------|----------------------------------------------------------------|
| Kontin rakentaminen jumissa > 10 min   | **Codespaces ➜ “Rebuild Container”**                           |
| `python: command not found`              | Terminaali ei liitetty; klikkaa **+** ➜ *bash*                 |
| `401 Unauthorized` OpenAI:lta             | Väärä / vanhentunut `OPENAI_API_KEY`                           |
| VS Code näyttää “Dev container mounting…” | Päivitä selainvälilehti—Codespaces menettää toisinaan yhteyden  |
| Notebookin ydin puuttuu                  | Notebook-valikko ➜ **Kernel ▸ Select Kernel ▸ Python 3**       |

   Unix-pohjaiset järjestelmät:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Muokkaa `.env`-tiedostoa**: Avaa `.env`-tiedosto tekstieditorissa (esim. VS Code, Notepad++ tai muu editori). Lisää tiedostoon seuraavat rivit, korvaten paikkamerkit omalla Microsoft Foundry Models -päätepisteelläsi ja avaimellasi (katso [`providers.md`](03-providers.md) ohjeet niiden saamiseen):

   > **Huom:** GitHub Models (ja sen `GITHUB_TOKEN`-muuttuja) poistuu käytöstä heinäkuun 2026 lopussa. Käytä sen sijaan [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Tallenna tiedosto**: Tallenna muutokset ja sulje tekstieditori.

5. **Asenna `python-dotenv`**: Jos et ole vielä asentanut, sinun täytyy asentaa `python-dotenv`-paketti, jotta ympäristömuuttujat ladataan `.env`-tiedostosta Python-sovellukseesi. Voit asentaa sen `pip`-komennolla:

   ```bash
   pip install python-dotenv
   ```

6. **Lataa ympäristömuuttujat Python-skriptissäsi**: Python-skriptissäsi käytä `python-dotenv`-pakettia lataamaan ympäristömuuttujat `.env`-tiedostosta:

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

Siinä se! Olet onnistuneesti luonut `.env`-tiedoston, lisännyt Microsoft Foundry Models -tunnisteesi ja ladannut ne Python-sovellukseesi.

## Miten suorittaa paikallisesti tietokoneellasi

Suorittaaksesi koodin paikallisesti tietokoneellasi, sinun pitää olla asennettuna jokin versio [Pythonista](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Käyttääksesi repositiota sinun tulee kloonata se:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kun olet saanut kaiken valmiiksi, voit aloittaa!

## Valinnaiset vaiheet

### Minicondan asennus

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) on kevyt asentaja [Condan](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonin sekä muutamien pakettien asentamiseen.
Conda itsessään on pakettien hallintaohjelma, joka helpottaa erilaisten Python- [**virtuaaliympäristöjen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ja pakettien asettelua ja vaihtamista. Se on myös hyödyllinen asentamaan paketteja, joita ei voi asentaa `pip`-komennolla.

Voit seurata [MiniCondan asennusopasta](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) sen asentamiseksi.

Minicondan asennettuasi kloonaa [repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jos et ole jo tehnyt).

Seuraavaksi sinun tulee luoda virtuaaliympäristö. Condalla tämä onnistuu luomalla uusi ympäristötiedosto (_environment.yml_). Jos seuraat tätä oppaana Codespacesin kautta, luo tiedosto `.devcontainer`-kansioon, eli `.devcontainer/environment.yml`.

Täytä ympäristötiedosto alla olevalla koodikatkelmalla:

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

Jos saat virheitä condaa käytettäessä, voit asentaa Microsoft AI -kirjastot manuaalisesti seuraavalla terminaalikomennolla.

```
conda install -c microsoft azure-ai-ml
```

Ympäristötiedostossa määritellään tarvittavat riippuvuudet. `<environment-name>` tarkoittaa nimeä, jonka haluat antaa Conda-ympäristöllesi, ja `<python-version>` on haluamasi Python-versio, esimerkiksi `3` on uusin iso Python-versio.

Kun tiedosto on valmis, voit luoda Conda-ympäristön suorittamalla seuraavat komennot komentorivillä/terminaalissa:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer-alikansio koskee vain Codespace-asetuksia
conda activate ai4beg
```

Katso [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jos kohtaat ongelmia.

### Visual Studio Coden käyttö Python-tukilaajennuksella

Suosittelemme käyttämään tätä kurssia varten [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) -editoria, johon on asennettu [Python-tukilaajennus](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Tämä on kuitenkin enemmän suositus kuin pakollinen vaatimus.

> **Huom:** Avaamalla kurssin repoin VS Codessa sinulla on mahdollisuus asentaa projekti säilöön (container). Tämä johtuu reposta löytyvästä [erityisestä `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) -kansiosta. Lisätietoja tästä myöhemmin.

> **Huom:** Kloonattuasi ja avatessasi kansion VS Codessa, sinulle suositellaan automaattisesti Python-tukilaajennuksen asentamista.

> **Huom:** Jos VS Code ehdottaa repoin avaamista uudestaan säilössä, hylkää tämä pyyntö käyttääksesi paikallisesti asennettua Python-versiota.

### Jupyterin käyttö selaimessa

Voit myös tehdä projektia [Jupyter-ympäristössä](https://jupyter.org?WT.mc_id=academic-105485-koreyst) suoraan selaimessasi. Sekä klassinen Jupyter että [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) tarjoavat miellyttävän kehitysympäristön ominaisuuksineen, kuten koodin automaattisen täydennyksen ja korostamisen.

Jupyterin lokalisoitu käynnistys: Mene terminaaliin/komentoriville, siirry kurssin kansion sisään ja suorita:

```bash
jupyter notebook
```

tai

```bash
jupyterhub
```

Tämä käynnistää Jupyter-instanssin ja saat sen URL-osoitteen komentoriville näytettäväksi.

Kun pääset URL-osoitteeseen, näet kurssin sisällön ja voit navigoida mihin tahansa `*.ipynb`-tiedostoon. Esimerkiksi `08-building-search-applications/python/oai-solution.ipynb`.

### Suoritus säilössä (container)

Vaihtoehtona kaiken asentamiselle tietokoneelle tai Codespaceen on käyttää [säilöä](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Kurssirepon erityinen `.devcontainer`-kansio mahdollistaa projektin asentamisen VS Codessa säilöön. Codespacesin ulkopuolella tämä vaatii Dockerin asennuksen, ja on aika työlästä, joten suosittelemme tätä vain säilöjen kanssa kokeneille.

Yksi parhaista tavoista pitää API-avaimesi turvassa GitHub Codespacesissä on käyttää Codespace Secrets -ominaisuutta. Seuraa [Codespacesin salaisuuksien hallintaopasta](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) lisätietojen saamiseksi.


## Oppitunnit ja tekniset vaatimukset

Kurssilla on 6 teoriaoppituntia ja 6 koodaustuntia.

Koodaustunneilla käytämme Azure OpenAI -palvelua. Sinun tulee saada pääsy Azure OpenAI -palveluun ja API-avain koodin suorittamiseksi. Voit hakea pääsyä [täyttämällä tämän hakemuksen](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Kun odotat hakemuksen käsittelyä, jokaisen koodaustunnin mukana on myös `README.md`-tiedosto, jossa voit tarkastella koodia ja tuloksia.

## Azure OpenAI -palvelun ensimmäinen käyttö

Jos käytät Azure OpenAI -palvelua ensimmäistä kertaa, seuraa tätä opasta, kuinka [luoda ja ottaa käyttöön Azure OpenAI Service -resurssi.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API:n ensimmäinen käyttö

Jos käytät OpenAI API:a ensimmäistä kertaa, seuraa opasta miten [luoda ja käyttää rajapintaa.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Tapaa muita oppijoita

Olemme luoneet kanavia viralliselle [AI Community Discord -palvelimellemme](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) muiden oppijoiden tapaamista varten. Tämä on loistava tapa verkostoitua samanhenkisten yrittäjien, rakentajien, opiskelijoiden ja kaikkien kanssa, jotka haluavat kehittyä Generatiivisessa tekoälyssä.

[![Liity Discord-kanavalle](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektitiimi on myös mukana tässä Discord-palvelimella auttamassa oppijoita.

## Osallistu

Tämä kurssi on avoimen lähdekoodin aloitte. Jos näet parannettavaa tai ongelmia, tee [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) tai kirjaa [GitHub-issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektitiimi seuraa kaikkia panoksia. Avoimen lähdekoodin osallistuminen on upea tapa rakentaa uraasi Generatiivisessa tekoälyssä.

Useimmat osallistumiset edellyttävät, että hyväksyt Contributor License Agreementin (CLA), jossa vahvistat, että sinulla on oikeus myöntää meille oikeudet käyttää panostasi. Lisätietoja saat osoitteesta [CLA, Contributor License Agreement -sivusto](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Tärkeää: käännettäessä tekstiä tässä repossa varmista, ettei käytetä konekäännöksiä. Varmistamme käännökset yhteisön kautta, joten toimi käännösten vapaaehtoisena vain kielissä, joissa olet taitava.

Kun teet pull requestin, CLA-botti määrittää automaattisesti, tarvitseeko sinun toimittaa CLA ja merkitsee PR:n asianmukaisesti (esim. tunnisteella, kommentilla). Seuraa vain botin ohjeita. Tämä tarvitaan vain kerran kaikissa CLA:ta käyttävissä repositioissa.


Tämä projekti on ottanut käyttöön [Microsoftin avoimen lähdekoodin käytösohjeet](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Lisätietoja löytyy Käytösohjeiden UKK:sta tai voit ottaa yhteyttä osoitteeseen [Email opencode](opencode@microsoft.com) mahdollisia lisäkysymyksiä tai kommentteja varten.

## Aloitetaan

Nyt kun olet suorittanut kurssin vaaditut vaiheet, aloitetaan tutustumalla [johdantoon generatiiviseen tekoälyyn ja suurriippuvuusmalleihin](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->