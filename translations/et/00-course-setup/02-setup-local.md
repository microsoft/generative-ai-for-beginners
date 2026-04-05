# Kohalik seadistus 🖥️

**Kasuta seda juhendit, kui eelistad kõike oma sülearvutis käivitada.**  
Sul on kaks võimalust: **(A) natiivne Python + virtual-env** või **(B) VS Code Dev Container koos Dockeriga**.  
Vali see, mis tundub lihtsam—mõlemad viivad samade õppetükkideni.

## 1. Eeltingimused

| Tööriist           | Versioon / Märkused                                                                 |
|--------------------|------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (saad aadressilt <https://python.org>)                                      |
| **Git**            | Viimane (tuleb koos Xcode / Git for Windows / Linux pakihalduriga)                 |
| **VS Code**        | Valikuline, kuid soovitatav <https://code.visualstudio.com>                         |
| **Docker Desktop** | *Ainult* valiku B jaoks. Tasuta paigaldus: <https://docs.docker.com/desktop/>      |

> 💡 **Nipp** – Kontrolli tööriistu terminalis:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Valik A – Natiivne Python (kiireim)

### Samm 1  Klooni see hoidla

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Samm 2 Loo ja aktiveeri virtuaalne keskkond

```bash
python -m venv .venv          # tee üks
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Käsurea prompt peaks nüüd algama (.venv)—see tähendab, et oled keskkonnas sees.

### Samm 3 Paigalda sõltuvused

```bash
pip install -r requirements.txt
```

Jätka jaotise 3 juurde [API võtmete lisamine](../../../00-course-setup)

## 2. Valik B – VS Code Dev Container (Docker)

Me seadistasime selle hoidla ja kursuse [arendus konteineriga](https://containers.dev?WT.mc_id=academic-105485-koreyst), mis sisaldab universaalset runtime’i, mis toetab Python3, .NET, Node.js ja Java arendust. Seotud konfiguratsioon on määratletud failis `devcontainer.json`, mis asub selle hoidla juurkaustas `.devcontainer/` kaustas.

>**Miks valida see?**  
>Identsed keskkonnad nagu Codespaces; ei ole sõltuvuste nihkumist.

### Samm 0 Paigalda lisad

Docker Desktop – veendu, et käsk ```docker --version``` töötab.  
VS Code Remote – Containers laiendus (ID: ms-vscode-remote.remote-containers).

### Samm 1 Ava hoidla VS Codes

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code tuvastab .devcontainer/ ja kuvab prompti.

### Samm 2 Ava konteineris uuesti

Klõpsa “Reopen in Container”. Docker ehitab pildi (≈ 3 min esimesel korral).  
Kui terminali prompt ilmub, oled konteineris sees.

## 2. Valik C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) on kergekaaluline paigaldaja [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythoni ja mõne paketi paigaldamiseks.  
Conda ise on pakihaldur, mis teeb lihtsaks erinevate Python [**virtuaalkeskkondade**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ja pakettide seadistamise ning vahetamise. See on kasulik ka pakettide paigaldamiseks, mida `pip` kaudu ei ole saadaval.

### Samm 0  Paigalda Miniconda

Järgi [MiniConda paigaldusjuhendit](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

```bash
conda --version
```

### Samm 1 Loo virtuaalne keskkond

Loo uus keskkonna fail (*environment.yml*). Kui kasutad Codespaces, loo see `.devcontainer` kausta, st `.devcontainer/environment.yml`.

### Samm 2 Täida oma keskkonna fail

Lisa järgmine lõik faili `environment.yml`

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

### Samm 3 Loo oma Conda keskkond

Käivita alljärgnevad käsud oma käsureal/terminalis

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer alamtee kehtib ainult Codespace'i seadistuste puhul
conda activate ai4beg
```

Kui tekib probleeme, vaata [Conda keskkondade juhendit](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2  Valik D – Klassikaline Jupyter / Jupyter Lab (brauseris)

> **Kellele see sobib?**  
> Kõigile, kes armastavad klassikalist Jupyter liidest või soovivad käivitada märkmikke ilma VS Code’ita.

### Samm 1  Veendu, et Jupyter on paigaldatud

Jupyteri kohalikuks käivitamiseks ava terminal/käsurida, liigu kursuse kausta ja käivita:

```bash
jupyter notebook
```

või

```bash
jupyterhub
```

See käivitab Jupyteri instantsi ja URL, mille kaudu sellele ligi pääseda, kuvatakse käsurea aknas.

Kui avad URL-i, peaksid nägema kursuse ülevaadet ja saama navigeerida ükskõik millise `*.ipynb` faili juurde. Näiteks `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Lisa oma API võtmed

API võtmete turvaline hoidmine on oluline igasuguse rakenduse ehitamisel. Soovitame mitte salvestada API võtmeid otse koodi. Nende avalik hoidmine võib põhjustada turvariske ja isegi soovimatuid kulusid, kui neid kasutab pahatahtlik isik.  
Siin on samm-sammuline juhend, kuidas luua Pythonile `.env` fail ja lisada sinna `GITHUB_TOKEN`:

1. **Liigu oma projekti kausta**: Ava terminal või käsurida ja liigu oma projekti juurkausta, kuhu soovid `.env` faili luua.

   ```bash
   cd path/to/your/project
   ```

2. **Loo `.env` fail**: Kasuta oma eelistatud tekstiredaktorit, et luua uus fail nimega `.env`. Kui kasutad käsurida, võid kasutada `touch` (Unix-põhistes süsteemides) või `echo` (Windowsis):

   Unix-põhised süsteemid:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Muuda `.env` faili**: Ava `.env` fail tekstiredaktoris (nt VS Code, Notepad++ või mõni muu). Lisa faili järgmine rida, asendades `your_github_token_here` oma tegeliku GitHubi tokeniga:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salvesta fail**: Salvesta muudatused ja sulge tekstiredaktor.

5. **Paigalda `python-dotenv`**: Kui pole veel paigaldatud, paigalda `python-dotenv` pakett, et laadida keskkonnamuutujad `.env` failist oma Python rakendusse. Paigalda see `pip` abil:

   ```bash
   pip install python-dotenv
   ```

6. **Laadi keskkonnamuutujad oma Python skriptis**: Kasuta oma Python skriptis `python-dotenv` paketti, et laadida keskkonnamuutujad `.env` failist:

   ```python
   from dotenv import load_dotenv
   import os

   # Laadi keskkonnamuutujad failist .env
   load_dotenv()

   # Juurdepääs GITHUB_TOKEN muutujale
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

See ongi kõik! Sa lõid edukalt `.env` faili, lisasid sinna oma GitHubi tokeni ja laadisid selle oma Python rakendusse.

🔐 Ära kunagi commiti .env faili—see on juba .gitignore failis.  
Täielikud pakkuja juhised on failis [`providers.md`](03-providers.md).

## 4. Mis edasi?

| Ma tahan…           | Mine…                                                                   |
|---------------------|------------------------------------------------------------------------|
| Alustada õppetükki 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Seadistada LLM pakkuja | [`providers.md`](03-providers.md)                                     |
| Tutvuda teiste õppijatega | [Liitu meie Discordiga](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Tõrkeotsing

| Sümptom                                   | Lahendus                                                        |
|-------------------------------------------|----------------------------------------------------------------|
| `python not found`                        | Lisa Python PATH-i või ava terminal uuesti pärast paigaldust   |
| `pip` ei suuda ehitada rattaid (Windows) | Käivita `pip install --upgrade pip setuptools wheel` ja proovi uuesti. |
| `ModuleNotFoundError: dotenv`             | Käivita `pip install -r requirements.txt` (keskkond ei olnud paigaldatud). |
| Docker build ebaõnnestub *No space left* | Docker Desktop ▸ *Settings* ▸ *Resources* → suurenda kettaruumi. |
| VS Code pakub pidevalt uuesti avamist    | Sul võib olla mõlemad valikud aktiivsed; vali üks (venv **või** konteiner) |
| OpenAI 401 / 429 vead                      | Kontrolli `OPENAI_API_KEY` väärtust / päringute kiiruse piire.  |
| Vead Conda kasutamisel                    | Paigalda Microsoft AI teegid käsuga `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellekti tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->