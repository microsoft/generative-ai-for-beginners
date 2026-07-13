# Paikallinen asennus 🖥️

**Käytä tätä opasta, jos haluat ajaa kaiken omalla kannettavallasi.**  
Sinulla on kaksi vaihtoehtoa: **(A) natiivi Python + virtual-env** tai **(B) VS Code Dev Container Dockerilla**.  
Valitse se, mikä tuntuu helpommalta—molemmat johtavat samoihin oppitunteihin.

## 1. Esivaatimukset

| Työkalu            | Versio / Huomautukset                                                             |
|--------------------|----------------------------------------------------------------------------------|
| **Python**         | 3.10+ (lataa osoitteesta <https://python.org>)                                   |
| **Git**            | Uusin (sisältyy Xcodeen / Git for Windowsiin / Linux-paketinhallintaan)          |
| **VS Code**        | Valinnainen mutta suositeltu <https://code.visualstudio.com>                      |
| **Docker Desktop** | *Vain* vaihtoehtoon B. Ilmainen asennus: <https://docs.docker.com/desktop/>      |

> 💡 **Vinkki** – Varmista työkalut terminaalissa:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Vaihtoehto A – natiiv Python (nopein)

### Vaihe 1  Kloonaa tämä repositorio

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Vaihe 2 Luo ja aktivoi virtuaaliympäristö

```bash
python -m venv .venv          # tee yksi
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Kehote alkaa nyt (.venv)—se tarkoittaa, että olet ympäristössä.

### Vaihe 3 Asenna riippuvuudet

```bash
pip install -r requirements.txt
```

Ohita suoraan kohtaan 3 [API-avaimet](#3-lisää-api-avaimesi)

## 2. Vaihtoehto B – VS Code Dev Container (Docker)

Olemme määrittäneet tämän repositorion ja kurssin [kehityssäiliöllä](https://containers.dev?WT.mc_id=academic-105485-koreyst), jolla on Universal runtime tuki Python3:lle, .NET:lle, Node.js:lle ja Java-kehitykselle. Tätä liittyvä määrittely on tiedostossa `devcontainer.json`, joka sijaitsee `.devcontainer/`-kansiossa tämän repositorion juurihakemistossa.

>**Miksi valita tämä?**
>Ympäristö on identtinen Codespacesin kanssa; ei riippuvuuksien hajontaa.

### Vaihe 0 Asenna lisäosat

Docker Desktop – varmista, että ```docker --version``` toimii.
VS Code Remote – Containers -laajennus (ID: ms-vscode-remote.remote-containers).

### Vaihe 1 Avaa repo VS Codessa

Tiedosto ▸ Avaa kansio…  → generative-ai-for-beginners

VS Code havaitsee .devcontainer/-kansion ja näyttää kehotteen.

### Vaihe 2 Avaa uudelleen säiliössä

Napsauta ”Reopen in Container”. Docker rakentaa kuvan (≈ 3 min ensimmäisellä kerralla).
Kun terminaalin kehotte näyttää, olet säiliön sisällä.

## 2. Vaihtoehto C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) on kevyt asennustyökalu asentamaan [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonin sekä muutamia paketteja.
Conda itsessään on paketinhallintaohjelma, joka helpottaa erilaisten Python [**virtuaaliympäristöjen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ja pakettien käyttöönottoa ja vaihtamista. Se on myös hyödyllinen asentamaan paketteja, joita ei ole saatavilla `pip`:illä.

### Vaihe 0  Asenna Miniconda

Noudata [MiniConda asennusopasta](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) asentaaksesi sen.

```bash
conda --version
```

### Vaihe 1 Luo virtuaaliympäristö

Luo uusi ympäristötiedosto (*environment.yml*). Jos seuraat mukana Codespacesin kautta, luo tämä `.devcontainer`-kansioon, eli `.devcontainer/environment.yml`.

### Vaihe 2 Täytä ympäristötiedosto

Lisää seuraava koodinpätkä tiedostoon `environment.yml`

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

### Vaihe 3 Luo Conda-ympäristö

Suorita alla olevat komennot komentorivillä/terminaalissa

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer-alipolku koskee vain Codespace-asetuksia
conda activate ai4beg
```

Katso [Conda ympäristöjen käyttöopas](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), jos kohtaat ongelmia.

## 2  Vaihtoehto D – Klassinen Jupyter / Jupyter Lab (selaimessasi)

> **Kenelle tämä sopii?**  
> Kenelle tahansa, joka rakastaa klassista Jupyter-käyttöliittymää tai haluaa ajaa muistiinpanoja ilman VS Codea.  

### Vaihe 1  Varmista, että Jupyter on asennettu

Jupyterin käynnistämiseksi paikallisesti mene terminaaliin/komentoriville, siirry kurssihakemistoon ja suorita:

```bash
jupyter notebook
```

tai

```bash
jupyterhub
```

Tämä käynnistää Jupyter-instanssin ja URL näkyy komentorivillä.

Kun avaat URL:n, näet kurssin rungon ja voit siirtyä mihin tahansa `*.ipynb`-tiedostoon. Esimerkiksi `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Lisää API-avaimesi

API-avainten pitäminen turvassa on tärkeää missä tahansa sovelluksen rakentamisessa. Suosittelemme, ettei API-avaimia tallenneta suoraan koodiin. Näiden tietojen tallentaminen julkiseen repositorioon voi aiheuttaa tietoturvaongelmia ja jopa ei-toivottuja kustannuksia, jos niitä käyttää väärinkäyttäjä.
Tässä on yksityiskohtainen opas siitä, miten luot `.env`-tiedoston Pythonille ja lisäät Microsoft Foundry Models -tunnistautumistiedot:

> **Huom:** GitHub Models (ja sen `GITHUB_TOKEN`-muuttuja) poistuvat käytöstä heinäkuun 2026 lopussa. Tämä opas käyttää sen sijaan [Microsoft Foundry Modelsia](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Haluatko työskennellä täysin offline-tilassa? Katso [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Siirry projektihakemistoon**: Avaa terminaali tai komentokehote ja mene projektisi juurihakemistoon, johon haluat luoda `.env`-tiedoston.

   ```bash
   cd path/to/your/project
   ```

2. **Luo `.env`-tiedosto**: Käytä haluamaasi tekstieditoria luodaksesi uuden tiedoston nimeltä `.env`. Jos käytät komentoriviä, voit käyttää `touch`-komentoa (Unix-järjestelmissä) tai `echo`-komentoa (Windowsissa):

   Unix-järjestelmissä:

   ```bash
   touch .env
   ```

   Windowsissa:

   ```cmd
   echo . > .env
   ```

3. **Muokkaa `.env`-tiedostoa**: Avaa `.env`-tiedosto tekstieditorissa (esimerkiksi VS Code, Notepad++ tai muu editori). Lisää tiedostoon seuraavat rivit korvaten paikkamerkit oikeilla Microsoft Foundry -projektisi päätepisteellä ja API-avaimella:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Tallenna tiedosto**: Tallenna muutokset ja sulje editori.

5. **Asenna `python-dotenv`**: Jos et ole vielä tehnyt niin, sinun täytyy asentaa `python-dotenv`-paketti, jotta Python-sovelluksesi voi lukea `.env`-tiedoston ympäristömuuttujat. Voit asentaa sen `pip`-komennolla:

   ```bash
   pip install python-dotenv
   ```

6. **Lataa ympäristömuuttujat Python-skriptissäsi**: Käytä Python-skriptissäsi `python-dotenv`-pakettia ladataksesi ympäristömuuttujat `.env`-tiedostosta:

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

Siinä kaikki! Olet onnistuneesti luonut `.env`-tiedoston, lisännyt Microsoft Foundry Models -tunnistautumistietosi ja ladannut ne Python-sovellukseen.

🔐 Älä koskaan commitoi `.env`-tiedostoa—se on jo .gitignore-tiedostossa.
Täydelliset tarjoajaohjeet löytyvät tiedostosta [`providers.md`](03-providers.md).

## 4. Mitä seuraavaksi?

| Haluan…             | Mene kohtaan…                                                           |
|---------------------|-------------------------------------------------------------------------|
| Aloita Oppitunti 1  | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Määritä LLM-palveluntarjoaja | [`providers.md`](03-providers.md)                                       |
| Tapaa muita oppijoita | [Liity Discordiin](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)  |

## 5. Vianetsintä

| Oire                                    | Korjaus                                                      |
|----------------------------------------|-------------------------------------------------------------|
| `python not found`                      | Lisää Python PATHiin tai avaa terminaali uudelleen asennuksen jälkeen      |
| `pip` ei pysty rakentamaan whel-gemmiä (Windows) | `pip install --upgrade pip setuptools wheel` ja kokeile uudelleen.        |
| `ModuleNotFoundError: dotenv`           | Suorita `pip install -r requirements.txt` (ympäristöä ei asennettu).      |
| Docker build epäonnistuu *Ei tilaa jäljellä* | Docker Desktop ▸ *Asetukset* ▸ *Resurssit* → kasvata levykokoa.           |
| VS Code kehottaa jatkuvasti avaamaan uudelleen | Saatat olla käynnistänyt molemmat vaihtoehdot; valitse toinen (venv **tai** container)|
| OpenAI 401 / 429 virheitä               | Tarkista `OPENAI_API_KEY` -arvo / pyynnön nopeusrajoitukset.            |
| Virheitä Condaa käyttäessä              | Asenna Microsoft AI -kirjastot komennolla `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->