# Paikallinen asennus 🖥️

**Käytä tätä opasta, jos haluat ajaa kaiken omalla kannettavallasi.**  
Sinulla on kaksi vaihtoehtoa: **(A) natiivi Python + virtual-env** tai **(B) VS Code Dev Container Dockerilla**.  
Valitse kumpi tahansa tuntuu helpommalta—molemmat johtavat samoihin oppitunteihin.

## 1. Esivaatimukset

| Työkalu            | Versio / Huomautukset                                                               |
|--------------------|-------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (lataa osoitteesta <https://python.org>)                                     |
| **Git**            | Uusin (sisältyy Xcodeen / Git for Windowsiin / Linuxin pakettienhallintaan)          |
| **VS Code**        | Valinnainen mutta suositeltava <https://code.visualstudio.com>                       |
| **Docker Desktop** | *Vain* vaihtoehtoon B. Ilmainen asennus: <https://docs.docker.com/desktop/>          |

> 💡 **Vinkki** – Tarkista työkalut terminaalissa:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Vaihtoehto A – Natiivi Python (nopein)

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

Siirry kohtaan 3 [API-avaimet](../../../00-course-setup)

## 2. Vaihtoehto B – VS Code Dev Container (Docker)

Olemme määrittäneet tämän repositorion ja kurssin [kehityssäiliöllä](https://containers.dev?WT.mc_id=academic-105485-koreyst), joka sisältää Universal runtime -ympäristön, joka tukee Python3:ta, .NET:iä, Node.js:ää ja Java-kehitystä. Asiaankuuluva konfiguraatio on määritelty `devcontainer.json`-tiedostossa, joka sijaitsee `.devcontainer/`-kansiossa tämän repositorion juuressa.

>**Miksi valita tämä?**  
>Ympäristö on identtinen Codespacesin kanssa; ei riippuvuuksien hajontaa.

### Vaihe 0 Asenna lisäosat

Docker Desktop – varmista, että ```docker --version``` toimii.  
VS Code Remote – Containers -laajennus (ID: ms-vscode-remote.remote-containers).

### Vaihe 1 Avaa repo VS Codessa

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code tunnistaa .devcontainer/-kansion ja näyttää kehotteen.

### Vaihe 2 Avaa uudelleen säiliössä

Klikkaa “Reopen in Container”. Docker rakentaa kuvan (≈ 3 min ensimmäisellä kerralla).  
Kun terminaalin kehotus ilmestyy, olet säiliön sisällä.

## 2. Vaihtoehto C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) on kevyt asennusohjelma [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonin sekä muutamien pakettien asentamiseen.  
Conda on pakettienhallinta, joka helpottaa erilaisten Python [**virtuaaliympäristöjen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ja pakettien hallintaa ja vaihtamista. Se on myös hyödyllinen pakettien asentamiseen, joita ei ole saatavilla `pip`-komennolla.

### Vaihe 0  Asenna Miniconda

Seuraa [MiniConda asennusopasta](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) asentaaksesi sen.

```bash
conda --version
```

### Vaihe 1 Luo virtuaaliympäristö

Luo uusi ympäristötiedosto (*environment.yml*). Jos seuraat mukana Codespacesissa, luo tämä `.devcontainer`-kansioon, eli `.devcontainer/environment.yml`.

### Vaihe 2 Täytä ympäristötiedosto

Lisää seuraava koodi `environment.yml`-tiedostoon

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

Suorita alla olevat komennot komentorivillä/terminaalissa

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer-alipolku koskee vain Codespace-asetuksia
conda activate ai4beg
```

Katso [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), jos kohtaat ongelmia.

## 2  Vaihtoehto D – Klassinen Jupyter / Jupyter Lab (selaimessasi)

> **Kenelle tämä sopii?**  
> Kenelle tahansa, joka rakastaa klassista Jupyter-käyttöliittymää tai haluaa ajaa muistikirjoja ilman VS Codea.

### Vaihe 1  Varmista, että Jupyter on asennettu

Aloittaaksesi Jupyterin paikallisesti, avaa terminaali/komentorivi, siirry kurssin kansioon ja suorita:

```bash
jupyter notebook
```

tai

```bash
jupyterhub
```

Tämä käynnistää Jupyter-instanssin ja URL-osoite sen käyttämiseen näytetään komentorivillä.

Kun avaat URL-osoitteen, näet kurssin sisällön ja voit navigoida mihin tahansa `*.ipynb`-tiedostoon. Esimerkiksi `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Lisää API-avaimesi

API-avainten turvallinen säilyttäminen on tärkeää minkä tahansa sovelluksen rakentamisessa. Suosittelemme, ettet tallenna API-avaimia suoraan koodiisi. Julkiseen repositorioon tallentaminen voi aiheuttaa turvallisuusongelmia ja jopa ei-toivottuja kustannuksia, jos joku väärinkäyttää niitä.  
Tässä vaiheittainen opas `.env`-tiedoston luomiseen Pythonille ja `GITHUB_TOKEN`-avaimen lisäämiseen:

1. **Siirry projektikansioosi**: Avaa terminaali tai komentokehote ja siirry projektisi juurikansioon, johon haluat luoda `.env`-tiedoston.

   ```bash
   cd path/to/your/project
   ```

2. **Luo `.env`-tiedosto**: Käytä haluamaasi tekstieditoria luodaksesi uuden tiedoston nimeltä `.env`. Jos käytät komentoriviä, voit käyttää `touch` (Unix-järjestelmissä) tai `echo` (Windowsissa):

   Unix-järjestelmät:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Muokkaa `.env`-tiedostoa**: Avaa `.env`-tiedosto tekstieditorissa (esim. VS Code, Notepad++ tai muu editori). Lisää tiedostoon seuraava rivi korvaten `your_github_token_here` omalla GitHub-tokenillasi:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Tallenna tiedosto**: Tallenna muutokset ja sulje editori.

5. **Asenna `python-dotenv`**: Jos et ole vielä asentanut, sinun täytyy asentaa `python-dotenv`-paketti, jotta voit ladata ympäristömuuttujat `.env`-tiedostosta Python-sovellukseesi. Asenna se `pip`-komennolla:

   ```bash
   pip install python-dotenv
   ```

6. **Lataa ympäristömuuttujat Python-skriptissäsi**: Käytä Python-skriptissäsi `python-dotenv`-pakettia ladataksesi ympäristömuuttujat `.env`-tiedostosta:

   ```python
   from dotenv import load_dotenv
   import os

   # Lataa ympäristömuuttujat .env-tiedostosta
   load_dotenv()

   # Käytä GITHUB_TOKEN-muuttujaa
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Siinä kaikki! Olet onnistuneesti luonut `.env`-tiedoston, lisännyt GitHub-tokenisi ja ladannut sen Python-sovellukseesi.

🔐 Älä koskaan tallenna .env-tiedostoa versionhallintaan—se on jo .gitignore-tiedostossa.  
Täydelliset ohjeet palveluntarjoajille löytyvät tiedostosta [`providers.md`](03-providers.md).

## 4. Mitä seuraavaksi?

| Haluan…             | Mene kohtaan…                                                           |
|---------------------|------------------------------------------------------------------------|
| Aloita oppitunti 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Määritä LLM-palveluntarjoaja | [`providers.md`](03-providers.md)                                       |
| Tapaa muita oppijoita | [Liity Discordiin](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Vianetsintä

| Oire                                     | Korjaus                                                          |
|------------------------------------------|-----------------------------------------------------------------|
| `python not found`                       | Lisää Python PATHiin tai avaa terminaali uudelleen asennuksen jälkeen |
| `pip` ei pysty rakentamaan wheel-paketteja (Windows) | Suorita `pip install --upgrade pip setuptools wheel` ja yritä uudelleen. |
| `ModuleNotFoundError: dotenv`            | Suorita `pip install -r requirements.txt` (ympäristöä ei asennettu). |
| Docker build epäonnistuu *No space left* | Docker Desktop ▸ *Settings* ▸ *Resources* → kasvata levytilaa.  |
| VS Code kehottaa jatkuvasti avaamaan uudelleen | Sinulla saattaa olla molemmat vaihtoehdot aktiivisina; valitse yksi (venv **tai** säiliö) |
| OpenAI 401 / 429 virheet                 | Tarkista `OPENAI_API_KEY`-arvo / pyyntöjen rajoitukset.         |
| Virheitä Condan kanssa                   | Asenna Microsoftin AI-kirjastot komennolla `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->