<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T18:38:38+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "sw"
}
-->
# Usanidi wa Kwenye Kompyuta 🖥️

**Tumia mwongozo huu ikiwa unapendelea kuendesha kila kitu kwenye laptop yako mwenyewe.**  
Una njia mbili: **(A) Python asilia + virtual-env** au **(B) VS Code Dev Container na Docker**.  
Chagua ile unayohisi ni rahisi—zote zinafika kwenye masomo yale yale.

## 1.  Mahitaji ya Awali

| Zana                | Toleo / Maelezo                                                                      |
|---------------------|--------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (pakua kutoka <https://python.org>)                                           |
| **Git**             | Toleo jipya (huja na Xcode / Git for Windows / Linux package manager)                |
| **VS Code**         | Si lazima lakini inashauriwa <https://code.visualstudio.com>                         |
| **Docker Desktop**  | *Kwa Option B pekee.* Pakua bure: <https://docs.docker.com/desktop/>                 |

> 💡 **Tip** – Hakikisha zana kwenye terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Chaguo A – Python Asilia (haraka zaidi)

### Hatua ya 1  Nakili repo hii

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Hatua ya 2 Tengeneza & washa mazingira ya virtual

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompt sasa inapaswa kuanza na (.venv)—hii inamaanisha uko ndani ya mazingira.

### Hatua ya 3 Sakinisha mahitaji

```bash
pip install -r requirements.txt
```

Ruka hadi Sehemu ya 3 kuhusu [API keys](../../../00-course-setup)

## 2. Chaguo B – VS Code Dev Container (Docker)

Tumeandaa repo hii na kozi na [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) yenye Universal runtime inayoweza kuendesha Python3, .NET, Node.js na Java. Mpangilio husika umeandikwa kwenye faili `devcontainer.json` ndani ya folda `.devcontainer/` kwenye mzizi wa repo hii.

>**Kwa nini uchague hii?**
> Mazingira sawa kabisa na Codespaces; hakuna tofauti za utegemezi.

### Hatua ya 0 Sakinisha vitu vya ziada

Docker Desktop – hakikisha ```docker --version``` inafanya kazi.
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### Hatua ya 1 Fungua repo kwenye VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code inatambua .devcontainer/ na inatoa prompt.

### Hatua ya 2 Fungua tena ndani ya container

Bonyeza “Reopen in Container”. Docker inatengeneza image (≈ dakika 3 mara ya kwanza).
Ukiona prompt ya terminal, uko ndani ya container.

## 2.  Chaguo C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ni installer nyepesi kwa ajili ya [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, na baadhi ya packages.
Conda yenyewe ni package manager, inayorahisisha kuanzisha na kubadilisha kati ya [**mazingira ya virtual**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) na packages tofauti za Python. Pia inasaidia kusakinisha packages ambazo hazipatikani kupitia `pip`.

### Hatua ya 0  Sakinisha Miniconda

Fuata [Mwongozo wa usakinishaji wa MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ili kuiweka.

```bash
conda --version
```

### Hatua ya 1 Tengeneza mazingira ya virtual

Tengeneza faili mpya ya mazingira (*environment.yml*). Kama unafuata kozi kupitia Codespaces, tengeneza hii ndani ya folda `.devcontainer`, yaani `.devcontainer/environment.yml`.

### Hatua ya 2  Jaza faili ya mazingira

Ongeza kipande hiki kwenye `environment.yml` yako

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

### Hatua ya 3 Tengeneza mazingira yako ya Conda

Endesha amri hizi kwenye command line/terminal yako

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Rejea [Mwongozo wa mazingira ya Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) kama ukipata changamoto.

## 2  Chaguo D – Jupyter ya Kawaida / Jupyter Lab (kwenye kivinjari chako)

> **Hii ni kwa nani?**  
> Yeyote anayependa interface ya Jupyter ya zamani au anayetaka kuendesha notebooks bila VS Code.  

### Hatua ya 1  Hakikisha Jupyter imesakinishwa

Ili kuanzisha Jupyter kwenye kompyuta yako, nenda kwenye terminal/command line, elekea kwenye folda ya kozi, na endesha:

```bash
jupyter notebook
```

au

```bash
jupyterhub
```

Hii itaanzisha Jupyter na URL ya kuifikia itaonyeshwa kwenye dirisha la command line.

Ukifungua URL hiyo, utaona muhtasari wa kozi na utaweza kufungua faili yoyote ya `*.ipynb`. Kwa mfano, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Ongeza API Keys Zako

Kuhifadhi API keys zako salama ni muhimu unapojenga programu yoyote. Tunashauri usihifadhi API keys moja kwa moja kwenye code yako. Ukiweka hizo kwenye repo ya wazi inaweza kusababisha masuala ya usalama na hata gharama zisizotarajiwa kama zitatumiwa vibaya.
Hapa kuna mwongozo wa hatua kwa hatua jinsi ya kutengeneza faili `.env` kwa Python na kuongeza `GITHUB_TOKEN`:

1. **Nenda kwenye folda ya mradi wako**: Fungua terminal au command prompt na elekea kwenye mzizi wa mradi wako ambapo unataka kutengeneza faili `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Tengeneza faili `.env`**: Tumia editor unayopenda kutengeneza faili jipya liitwalo `.env`. Ukiwa kwenye command line, unaweza kutumia `touch` (kwa Unix-based systems) au `echo` (kwa Windows):

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Hariri faili `.env`**: Fungua faili `.env` kwenye editor (mfano VS Code, Notepad++, au nyingine yoyote). Ongeza mstari huu kwenye faili, ukibadilisha `your_github_token_here` na token yako halisi ya GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Hifadhi faili**: Hifadhi mabadiliko na funga editor.

5. **Sakinisha `python-dotenv`**: Kama bado hujasakinisha, utahitaji kusakinisha package ya `python-dotenv` ili kupakia environment variables kutoka kwenye faili `.env` kwenye programu yako ya Python. Unaweza kusakinisha kwa kutumia `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Pakia environment variables kwenye script yako ya Python**: Kwenye script yako ya Python, tumia package ya `python-dotenv` kupakia environment variables kutoka kwenye faili `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Imekamilika! Umetengeneza faili `.env`, umeongeza token yako ya GitHub, na umeipakia kwenye programu yako ya Python.

🔐 Usikabidhi .env—tayari ipo kwenye .gitignore.
Maelezo kamili ya watoa huduma yapo kwenye [`providers.md`](03-providers.md).

## 4. Nini kinafuata?

| Nataka…              | Nenda kwenye…                                                            |
|----------------------|--------------------------------------------------------------------------|
| Anza Somo la 1       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Sanidi LLM Provider  | [`providers.md`](03-providers.md)                                        |
| Kutana na wanafunzi wengine | [Jiunge na Discord yetu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Kutatua Matatizo

| Tatizo                                    | Suluhisho                                                        |
|-------------------------------------------|------------------------------------------------------------------|
| `python not found`                        | Ongeza Python kwenye PATH au funga na fungua tena terminal       |
| `pip` haiwezi kujenga wheels (Windows)    | `pip install --upgrade pip setuptools wheel` kisha jaribu tena.  |
| `ModuleNotFoundError: dotenv`             | Endesha `pip install -r requirements.txt` (mazingira hayajasakinishwa).|
| Docker build inashindwa *No space left*   | Docker Desktop ▸ *Settings* ▸ *Resources* → ongeza ukubwa wa diski.|
| VS Code inaendelea kutoa prompt ya kufungua tena | Huenda una Options zote mbili; chagua moja (venv **au** container)|
| OpenAI 401 / 429 errors                   | Angalia thamani ya `OPENAI_API_KEY` / mipaka ya maombi.          |
| Makosa ukitumia Conda                     | Sakinisha maktaba za Microsft AI kwa `conda install -c microsoft azure-ai-ml`|

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya utafsiri wa kibinadamu wa kitaalamu. Hatuwajibiki kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.