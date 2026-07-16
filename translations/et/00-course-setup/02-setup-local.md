# Kohalik seadistus 🖥️

**Kasuta seda juhendit, kui eelistad kõike oma sülearvutis jooksutada.**   
Sul on kaks võimalust: **(A) natiivne Python + virtual-env** või **(B) VS Code arenduskonteiner Dockeriga**.  
Vali see, mis tundub lihtsam — mõlemad viivad samade õppetükkideni.

## 1.  Eelnõuded

| Tööriist           | Versioon / Märkused                                                                  |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (saad aadressilt <https://python.org>)                                        |
| **Git**            | Viimane (tuleb koos Xcode / Git for Windows / Linuxi pakihalduriga)                   |
| **VS Code**        | Valikuline, kuid soovitatav <https://code.visualstudio.com>                          |
| **Docker Desktop** | *Ainult* variandis B. Tasuta paigaldus: <https://docs.docker.com/desktop/>           |

> 💡 **Nõuanne** – Kontrolli tööriistade olemasolu terminalis:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Variant A – Natiivne Python (kiireim)

### 1. samm Klooni see repositoorium

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### 2. samm Loo ja aktiveeri virtuaalkeskkond

```bash
python -m venv .venv          # tee üks
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Käsklus tuleb nüüd alustada (.venv)—see tähendab, et oled keskkonnas sees.

### 3. samm Paigalda sõltuvused

```bash
pip install -r requirements.txt
```

Liigu jaotise 3 juurde, kus on [API võtmed](#3-lisa-oma-api-võtmed)

## 2. Variant B – VS Code arenduskonteiner (Docker)

Me seadistasime selle hoidla ja kursuse [arenduskonteineriga](https://containers.dev?WT.mc_id=academic-105485-koreyst), mis sisaldab universaalset runtime'i, mis toetab Python3, .NET, Node.js ja Java arendust. Sellega seotud seadistus määratletakse failis `devcontainer.json`, mis asub selle hoidla juurkataloogis `.devcontainer/` kaustas.

>**Miks valida see?**
>Keskkond on identselt sama nagu Codespaces; puudub sõltuvuste kõikumine.

### 0. samm Paigalda lisaressursid

Docker Desktop – veendu, et käsk `docker --version` töötab.
VS Code Remote – Containers laiendus (ID: ms-vscode-remote.remote-containers).

### 1. samm Ava hoidla VS Codes

Fail ▸ Ava Kaust…  → generative-ai-for-beginners

VS Code tuvastab .devcontainer/ kausta ja kuvab vastava teate.

### 2. samm Ava uuesti konteineris

Klõpsa “Reopen in Container”. Docker ehitab pildi (≈ 3 minutit esimesel korral).
Kui terminali prompt ilmub, oled konteineri sees.

## 2.  Variant C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) on kerge paigaldaja [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ja mõne paketi paigaldamiseks.
Conda on pakihaldur, mis teeb lihtsaks erinevate Python [**virtuaalkeskkondade**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ja paketihalduse seadistamise ning vahetamise. See on samuti kasulik, kui on vaja paigaldada pakette, mida ei ole `pip` kaudu saadaval.

### 0. samm Paigalda Miniconda

Järgi [MiniConda paigaldusjuhendit](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

```bash
conda --version
```

### 1. samm Loo virtuaalkeskkond

Loo uus keskkonna fail (*environment.yml*). Kui kasutad Codespaces'i, loo see `.devcontainer` kaustas, st `.devcontainer/environment.yml`.

### 2. samm Täida keskkonna fail

Lisa järgmine lõik `environment.yml` faili

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

### 3. samm Loo Conda keskkond

Käivita alljärgnevad käsud oma käsureal/terminalis

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer alamtee kehtib ainult Codespace'i seadistuste puhul
conda activate ai4beg
```

Vaata [Conda keskkondade juhendit](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), kui tekib probleeme.

## 2  Variant D – Klassikaline Jupyter / Jupyter Lab (brauseris)

> **Kellele see on mõeldud?**  
> Neile, kes armastavad klassikalist Jupyter liidest või soovivad jooksutada märkmikke ilma VS Code'ita.  

### 1. samm Veendu, et Jupyter on paigaldatud

Jupyteri lokaalseks käivitamiseks mine terminali/käsureale, liigu kursuse kataloogi ja käivita:

```bash
jupyter notebook
```

või

```bash
jupyterhub
```

See käivitab Jupyteri instantsi ja selle URL kuvatakse käsurea aknas.

Kui valid selle URL-i, peaksid nägema kursuse sisukorda ja saad navigeerida `*.ipynb` failide juurde. Näiteks `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Lisa oma API võtmed

Oma API võtmete turvalisuse hoidmine on oluline iga rakenduse loomisel. Soovitame mitte salvestada API võtmeid otse koodi. Nende avaliku hoidla commitimine võib põhjustada turvariske ja tahtmatuid kulusid, kui neid kasutab keegi pahatahtlik.
Järgnev on samm-sammuline juhend, kuidas luua Pythonile `.env` fail ja lisada Microsoft Foundry mudelite mandaadid:

> **Märkus:** GitHub Models (ja selle `GITHUB_TOKEN` muutuja) läheb pensionile 2026. aasta juuli lõpus. See juhend kasutab selle asemel [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Eelistad täielikult võrguühenduseta töötada? Vaata [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Mine oma projekti kausta**: Ava terminal või käsureaaken ja liigu oma projekti juurkausta, kuhu soovid luua `.env` faili.

   ```bash
   cd path/to/your/project
   ```

2. **Loo `.env` fail**: Kasuta oma eelistatud tekstiakent või käsurida, et luua uus `.env` fail. Käsurealt saab kasutada `touch` (Unix-põhistes süsteemides) või `echo` (Windowsis):

   Unix-põhised süsteemid:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Redigeeri `.env` faili**: Ava `.env` fail tekstiarendajas (näiteks VS Code, Notepad++ või muu redaktor). Lisa järgmised read, asendades kohatäited oma Microsoft Foundry projektiga seotud lõpp-punkti ja API võtmega:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Salvesta fail**: Salvesta tehtud muudatused ja sulge tekstiredaktor.

5. **Paigalda `python-dotenv`**: Kui sul ei ole veel paigaldatud, pead installima `python-dotenv` paketi, et laadida keskkonnamuutujad `.env` failist oma Python rakendusse. Seda saab teha `pip` abil:

   ```bash
   pip install python-dotenv
   ```

6. **Laadi keskkonnamuutujad oma Python skriptis**: Kasuta `python-dotenv` paketti, et laadida keskkonnamuutujad `.env` failist oma Python skripti:

   ```python
   from dotenv import load_dotenv
   import os

   # Laadi keskkonnamuutujad .env failist
   load_dotenv()

   # Juurdepääs Microsoft Foundry Models muutujatele
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

See ongi kõik! Sa lõid edukalt `.env` faili, lisasid sinna Microsoft Foundry mudelite mandaadid ja laadisid need oma Python rakendusse.

🔐 Ära kunagi commiti .env faili — see on juba .gitignore's.
Täielikud teenusepakkuja juhised on saadaval failis [`providers.md`](03-providers.md).

## 4. Mis järgmiseks?

| Ma tahan…          | Liigu…                                                                   |
|---------------------|-------------------------------------------------------------------------|
| Alustada õppetundi 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Seadistada LLM teenusepakkuja | [`providers.md`](03-providers.md)                                       |
| Kohtuda teiste õppijatega | [Liitu meie Discordiga](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Probleemide lahendamine

| Sümptom                                 | Lahendus                                                         |
|-----------------------------------------|-----------------------------------------------------------------|
| `python not found`                      | Lisa Python PATH-i või ava terminal uuesti pärast paigaldust   |
| `pip` ei suuda luua wheele (Windows)   | `pip install --upgrade pip setuptools wheel` ja proovi uuesti. |
| `ModuleNotFoundError: dotenv`           | Käivita `pip install -r requirements.txt` (keskkond ei olnud paigaldatud).  |
| Docker build ebaõnnestub *No space left* | Docker Desktop ▸ *Seaded* ▸ *Ressursid* → suurenda kettamahtu.  |
| VS Code palub pidevalt taasavada        | Sul võivad olla mõlemad variandid korraga aktiivsed; vali üks (venv **või** konteiner) |
| OpenAI 401 / 429 vead                   | Kontrolli `OPENAI_API_KEY` väärtust / päringute limiite.       |
| Vigade ilmnemine Conda kasutamisel     | Paigalda Microsoft AI teegid käsuga `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->