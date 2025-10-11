<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-10-11T11:41:39+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "et"
}
-->
# Kohalik seadistus 🖥️

**Kasuta seda juhendit, kui eelistad kõike oma sülearvutis käivitada.**  
Sul on kaks valikut: **(A) natiivne Python + virtual-env** või **(B) VS Code Dev Container koos Dockeriga**.  
Vali endale sobivam—mõlemad viivad samade õppetundideni.

## 1. Eeltingimused

| Tööriist            | Versioon / Märkused                                                                 |
|---------------------|-------------------------------------------------------------------------------------|
| **Python**          | 3.10+ (laadi alla <https://python.org>)                                            |
| **Git**             | Viimane (tuleb koos Xcode'i / Git for Windows / Linuxi paketihalduriga)            |
| **VS Code**         | Valikuline, kuid soovitatav <https://code.visualstudio.com>                        |
| **Docker Desktop**  | *Ainult* valiku B jaoks. Tasuta paigaldus: <https://docs.docker.com/desktop/>      |

> 💡 **Nõuanne** – Kontrolli tööriistu terminalis:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Valik A – Natiivne Python (kiireim)

### Samm 1 Klooni see repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Samm 2 Loo ja aktiveeri virtuaalne keskkond

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompt peaks nüüd algama (.venv)—see tähendab, et oled keskkonnas sees.

### Samm 3 Paigalda sõltuvused

```bash
pip install -r requirements.txt
```

Jätka jaotisega 3 [API võtmete lisamine](../../../00-course-setup)

## 2. Valik B – VS Code Dev Container (Docker)

Me oleme seadistanud selle repo ja kursuse [arenduskonteineriga](https://containers.dev?WT.mc_id=academic-105485-koreyst), millel on universaalne runtime, mis toetab Python3, .NET, Node.js ja Java arendust. Seotud konfiguratsioon on määratletud failis `devcontainer.json`, mis asub selle repo juurkataloogi `.devcontainer/` kaustas.

>**Miks valida see?**  
>Identne keskkond Codespaces'iga; ei mingeid sõltuvuste erinevusi.

### Samm 0 Paigalda lisad

Docker Desktop – kinnita, et ```docker --version``` töötab.  
VS Code Remote – Containers laiendus (ID: ms-vscode-remote.remote-containers).

### Samm 1 Ava repo VS Code'is

Fail ▸ Ava kaust… → generative-ai-for-beginners

VS Code tuvastab `.devcontainer/` ja kuvab hüpikakna.

### Samm 2 Ava konteineris uuesti

Klõpsa “Reopen in Container”. Docker ehitab pildi (≈ 3 min esimesel korral).  
Kui terminali prompt ilmub, oled konteineris sees.

## 2. Valik C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) on kerge paigaldaja [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python'i ja mõnede pakettide paigaldamiseks.  
Conda ise on paketihaldur, mis teeb lihtsaks erinevate Python'i [**virtuaalsete keskkondade**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ja pakettide seadistamise ja vahetamise. See on kasulik ka selliste pakettide paigaldamiseks, mis pole saadaval `pip` kaudu.

### Samm 0 Paigalda Miniconda

Järgi [Miniconda paigaldusjuhendit](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), et see seadistada.

```bash
conda --version
```

### Samm 1 Loo virtuaalne keskkond

Loo uus keskkonnafail (*environment.yml*). Kui kasutad Codespaces'i, loo see `.devcontainer` kataloogi, seega `.devcontainer/environment.yml`.

### Samm 2 Täida keskkonnafail

Lisa järgmine koodilõik oma `environment.yml` faili:

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

### Samm 3 Loo Conda keskkond

Käivita allolevad käsud oma käsureal/terminalis:

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Kui tekib probleeme, vaata [Conda keskkondade juhendit](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2. Valik D – Klassikaline Jupyter / Jupyter Lab (brauseris)

> **Kellele see sobib?**  
> Kõigile, kes armastavad klassikalist Jupyter'i liidest või tahavad käivitada märkmikke ilma VS Code'ita.

### Samm 1 Veendu, et Jupyter on paigaldatud

Jupyter'i käivitamiseks kohalikult mine terminali/käsureale, liigu kursuse kataloogi ja käivita:

```bash
jupyter notebook
```

või

```bash
jupyterhub
```

See käivitab Jupyter'i instantsi ja URL selle kasutamiseks kuvatakse käsurea aknas.

Kui pääsed URL-ile, peaksid nägema kursuse ülevaadet ja saama navigeerida mis tahes `*.ipynb` faili juurde. Näiteks `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Lisa oma API võtmed

API võtmete turvalisus ja kaitse on oluline igasuguse rakenduse loomisel. Soovitame mitte salvestada API võtmeid otse koodi. Nende andmete avalikku repo'sse lisamine võib põhjustada turvaprobleeme ja isegi soovimatuid kulusid, kui keegi pahatahtlik neid kasutab.  
Siin on samm-sammuline juhend, kuidas luua `.env` fail Python'i jaoks ja lisada `GITHUB_TOKEN`:

1. **Liigu oma projekti kataloogi**: Ava terminal või käsurida ja liigu oma projekti juurkataloogi, kuhu soovid `.env` faili luua.

   ```bash
   cd path/to/your/project
   ```

2. **Loo `.env` fail**: Kasuta oma eelistatud tekstiredaktorit, et luua uus fail nimega `.env`. Kui kasutad käsurida, saad kasutada `touch` (Unix-põhised süsteemid) või `echo` (Windows):

   Unix-põhised süsteemid:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Redigeeri `.env` faili**: Ava `.env` fail tekstiredaktoris (nt VS Code, Notepad++ või mõni muu). Lisa järgmine rida faili, asendades `your_github_token_here` oma tegeliku GitHub'i tokeniga:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salvesta fail**: Salvesta muudatused ja sulge tekstiredaktor.

5. **Paigalda `python-dotenv`**: Kui sa pole seda veel teinud, pead paigaldama `python-dotenv` paketi, et laadida keskkonnamuutujad `.env` failist oma Python'i rakendusse. Paigalda see `pip` abil:

   ```bash
   pip install python-dotenv
   ```

6. **Laadi keskkonnamuutujad oma Python'i skriptis**: Kasuta `python-dotenv` paketti, et laadida keskkonnamuutujad `.env` failist:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Valmis! Oled edukalt loonud `.env` faili, lisanud oma GitHub'i tokeni ja laadinud selle oma Python'i rakendusse.

🔐 Ära kunagi commit'i `.env`—see on juba `.gitignore` failis.  
Täielikud juhised pakkujate kohta leiad [`providers.md`](03-providers.md).

## 4. Mis edasi?

| Soovin…             | Mine…                                                                  |
|---------------------|------------------------------------------------------------------------|
| Alustada 1. õppetundi | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)   |
| Seadistada LLM pakkuja | [`providers.md`](03-providers.md)                                     |
| Kohtuda teiste õppijatega | [Liitu meie Discordiga](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Tõrkeotsing

| Sümptom                                   | Lahendus                                                         |
|-------------------------------------------|------------------------------------------------------------------|
| `python not found`                        | Lisa Python PATH-i või ava terminal pärast paigaldust uuesti.   |
| `pip` ei suuda rattaid ehitada (Windows)  | `pip install --upgrade pip setuptools wheel` ja proovi uuesti.  |
| `ModuleNotFoundError: dotenv`             | Käivita `pip install -r requirements.txt` (keskkond polnud paigaldatud). |
| Docker'i ehitus ebaõnnestub *No space left* | Docker Desktop ▸ *Settings* ▸ *Resources* → suurenda kettaruumi. |
| VS Code küsib pidevalt uuesti avamist     | Sul võib olla mõlemad valikud aktiivsed; vali üks (venv **või** konteiner). |
| OpenAI 401 / 429 vead                     | Kontrolli `OPENAI_API_KEY` väärtust / päringute limiite.         |
| Vead Conda kasutamisel                   | Paigalda Microsoft AI teegid käsuga `conda install -c microsoft azure-ai-ml`|

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.