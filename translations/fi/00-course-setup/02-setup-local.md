<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T17:41:05+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "fi"
}
-->
# Paikallinen asennus 🖥️

**Käytä tätä ohjetta, jos haluat ajaa kaiken omalla koneellasi.**  
Sinulla on kaksi vaihtoehtoa: **(A) natiivi Python + virtual-env** tai **(B) VS Code Dev Container Dockerilla**.  
Valitse se, mikä tuntuu helpoimmalta—molemmat vievät samoihin oppitunteihin.

## 1.  Esivaatimukset

| Työkalu             | Versio / Huomioita                                                                |
|---------------------|-----------------------------------------------------------------------------------|
| **Python**          | 3.10 + (lataa <https://python.org>)                                               |
| **Git**             | Uusin (sisältyy Xcodeen / Git for Windowsiin / Linuxin pakettienhallintaan)       |
| **VS Code**         | Valinnainen, mutta suositeltu <https://code.visualstudio.com>                     |
| **Docker Desktop**  | *Vain* vaihtoehtoon B. Ilmainen asennus: <https://docs.docker.com/desktop/>       |

> 💡 **Vinkki** – Tarkista työkalut terminaalissa:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Vaihtoehto A – Natiivi Python (nopein)

### Vaihe 1  Kloonaa tämä repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Vaihe 2 Luo & aktivoi virtuaaliympäristö

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Kehote alkaa nyt (.venv)—tämä tarkoittaa, että olet ympäristössä.

### Vaihe 3 Asenna riippuvuudet

```bash
pip install -r requirements.txt
```

Hyppää kohtaan 3 [API-avaimet](../../../00-course-setup)

## 2. Vaihtoehto B – VS Code Dev Container (Docker)

Tämä repositorio ja kurssi on rakennettu [kehityskontilla](https://containers.dev?WT.mc_id=academic-105485-koreyst), jossa on universaali ajonaika, joka tukee Python3:a, .NET:iä, Node.js:ää ja Javaa. Konfiguraatio löytyy `devcontainer.json`-tiedostosta, joka sijaitsee `.devcontainer/`-kansiossa tämän repositorion juuressa.

>**Miksi valita tämä?**
>Ympäristö on identtinen Codespacesin kanssa; ei riippuvuusongelmia.

### Vaihe 0 Asenna lisäosat

Docker Desktop – varmista että ```docker --version``` toimii.
VS Code Remote – Containers -laajennus (ID: ms-vscode-remote.remote-containers).

### Vaihe 1 Avaa repo VS Codessa

Tiedosto ▸ Avaa kansio…  → generative-ai-for-beginners

VS Code tunnistaa .devcontainer/-kansion ja näyttää kehotteen.

### Vaihe 2 Avaa uudelleen kontissa

Klikkaa “Reopen in Container”. Docker rakentaa kuvan (≈ 3 min ensimmäisellä kerralla).
Kun terminaalin kehote tulee näkyviin, olet kontissa.

## 2.  Vaihtoehto C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) on kevyt asennusohjelma [Condan](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonin ja muutaman paketin asentamiseen.
Conda on pakettienhallinta, jonka avulla on helppo luoda ja vaihtaa eri Pythonin [**virtuaaliympäristöjen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ja pakettien välillä. Se on myös kätevä, kun tarvitsee asentaa paketteja, joita ei saa `pip`:llä.

### Vaihe 0  Asenna Miniconda

Seuraa [MiniConda-asennusohjetta](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) asentaaksesi sen.

```bash
conda --version
```

### Vaihe 1 Luo virtuaaliympäristö

Luo uusi ympäristötiedosto (*environment.yml*). Jos käytät Codespacesia, luo tämä `.devcontainer`-kansioon eli `.devcontainer/environment.yml`.

### Vaihe 2  Täydennä ympäristötiedosto

Lisää seuraava pätkä `environment.yml`-tiedostoon

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

### Vaihe 3 Luo Conda-ympäristösi

Aja alla olevat komennot komentorivillä/terminaalissa

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Katso [Conda-ympäristöjen ohje](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jos tulee ongelmia.

## 2  Vaihtoehto D – Klassinen Jupyter / Jupyter Lab (selaimessa)

> **Kenelle tämä sopii?**  
> Kaikille, jotka pitävät klassisesta Jupyter-käyttöliittymästä tai haluavat ajaa muistikirjoja ilman VS Codea.  

### Vaihe 1  Varmista, että Jupyter on asennettu

Jotta voit käynnistää Jupytern paikallisesti, avaa terminaali/komentorivi, siirry kurssikansioon ja suorita:

```bash
jupyter notebook
```

tai

```bash
jupyterhub
```

Tämä käynnistää Jupyterin ja näyttää URL-osoitteen, jolla pääset siihen komentorivillä.

Kun avaat URL-osoitteen, näet kurssin sisällön ja voit siirtyä mihin tahansa `*.ipynb`-tiedostoon. Esimerkiksi `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Lisää API-avaimesi

API-avainten pitäminen turvassa on tärkeää, kun rakennat sovelluksia. Suosittelemme, ettet tallenna API-avaimia suoraan koodiin. Jos tallennat ne julkiseen repositorioon, se voi aiheuttaa tietoturvaongelmia ja jopa ylimääräisiä kustannuksia, jos joku käyttää niitä väärin.
Tässä vaiheittainen ohje, miten luot `.env`-tiedoston Pythonille ja lisäät `GITHUB_TOKEN`in:

1. **Siirry projektikansioosi**: Avaa terminaali tai komentokehote ja siirry projektisi juurikansioon, johon haluat luoda `.env`-tiedoston.

   ```bash
   cd path/to/your/project
   ```

2. **Luo `.env`-tiedosto**: Käytä haluamaasi tekstieditoria uuden `.env`-tiedoston luomiseen. Komentorivillä voit käyttää `touch` (Unix-pohjaiset järjestelmät) tai `echo` (Windows):

   Unix-pohjaiset järjestelmät:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Muokkaa `.env`-tiedostoa**: Avaa `.env`-tiedosto tekstieditorissa (esim. VS Code, Notepad++ tai muu editori). Lisää seuraava rivi tiedostoon, korvaten `your_github_token_here` omalla GitHub-tokenillasi:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Tallenna tiedosto**: Tallenna muutokset ja sulje editori.

5. **Asenna `python-dotenv`**: Jos et ole jo asentanut, sinun täytyy asentaa `python-dotenv`-paketti, jotta voit ladata ympäristömuuttujat `.env`-tiedostosta Python-sovellukseen. Asenna se `pip`:llä:

   ```bash
   pip install python-dotenv
   ```

6. **Lataa ympäristömuuttujat Python-skriptissäsi**: Käytä `python-dotenv`-pakettia ladataksesi ympäristömuuttujat `.env`-tiedostosta:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Siinä kaikki! Olet nyt luonut `.env`-tiedoston, lisännyt GitHub-tokenin ja ladannut sen Python-sovellukseen.

🔐 Älä koskaan commitoi .env-tiedostoa—se on jo .gitignore:ssa.
Täydelliset ohjeet palveluntarjoajille löytyvät [`providers.md`](03-providers.md).

## 4. Mitä seuraavaksi?

| Haluan…             | Siirry…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Aloittaa oppitunnin 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Asentaa LLM-palvelun | [`providers.md`](03-providers.md)                                       |
| Tavata muita oppijoita | [Liity Discordiin](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Vianmääritys

| Oire                                      | Korjaus                                                          |
|-------------------------------------------|------------------------------------------------------------------|
| `python not found`                        | Lisää Python PATHiin tai avaa terminaali uudelleen asennuksen jälkeen |
| `pip` ei voi rakentaa wheel-paketteja (Windows) | `pip install --upgrade pip setuptools wheel` ja yritä uudelleen. |
| `ModuleNotFoundError: dotenv`             | Suorita `pip install -r requirements.txt` (ympäristöä ei asennettu). |
| Dockerin rakennus epäonnistuu *No space left* | Docker Desktop ▸ *Settings* ▸ *Resources* → lisää levytilaa.     |
| VS Code kehottaa jatkuvasti avaamaan uudelleen | Sinulla voi olla molemmat vaihtoehdot aktiivisena; valitse yksi (venv **tai** kontti)|
| OpenAI 401 / 429 virheet                  | Tarkista `OPENAI_API_KEY` arvo / pyyntöjen määrärajoitukset.     |
| Virheitä Condan käytössä                  | Asenna Microsoftin AI-kirjastot komennolla `conda install -c microsoft azure-ai-ml`|

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen omalla kielellä tulee pitää ensisijaisena lähteenä. Kriittisissä tapauksissa suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa tämän käännöksen käytöstä mahdollisesti aiheutuvista väärinkäsityksistä tai tulkintavirheistä.