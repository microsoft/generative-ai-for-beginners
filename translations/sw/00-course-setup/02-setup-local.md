# Usanidi wa Mitaa 🖥️

**Tumia mwongozo huu ikiwa unapendelea kuendesha kila kitu kwenye kompyuta yako binafsi.**  
Una njia mbili: **(A) Python asili + virtual-env** au **(B) VS Code Dev Container na Docker**.  
Chagua ile inayokuonekana rahisi—zote zinaelekeza kwenye masomo sawa.

## 1.  Mahitaji ya Awali

| Zana               | Toleo / Maelezo                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (ipate kutoka <https://python.org>)                                            |
| **Git**            | Toleo la hivi karibuni (huja na Xcode / Git kwa Windows / meneja wa pakiti wa Linux)  |
| **VS Code**        | Hiari lakini inapendekezwa <https://code.visualstudio.com>                             |
| **Docker Desktop** | *Kwa chaguo B tu.* Usakinishaji wa bure: <https://docs.docker.com/desktop/>           |

> 💡 **Ushauri** – Thibitisha zana kwenye terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Chaguo A – Python Asili (haraka zaidi)

### Hatua 1  Nakili repo hii

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Hatua 2 Tengeneza & wezesha mazingira pepe

```bash
python -m venv .venv          # tengeneza moja
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Mwito sasa unapaswa kuanza na (.venv)—hiyo ina maana uko ndani ya mazingira pepe.

### Hatua 3 Sakinisha utegemezi

```bash
pip install -r requirements.txt
```

Ruka hadi Sehemu ya 3 kuhusu [funguo za API](../../../00-course-setup)

## 2. Chaguo B – VS Code Dev Container (Docker)

Tumeandaa hazina hii na kozi kwa kutumia [kontena ya maendeleo](https://containers.dev?WT.mc_id=academic-105485-koreyst) ambayo ina runtime ya Universal inayoweza kuunga mkono Python3, .NET, Node.js na maendeleo ya Java. Mipangilio inayohusiana imefafanuliwa katika faili `devcontainer.json` iliyoko kwenye folda `.devcontainer/` kwenye mzizi wa hazina hii.

>**Kwa nini uchague hii?**  
>Hali sawa na Codespaces; hakuna mabadiliko ya utegemezi.

### Hatua 0 Sakinisha vitu vya ziada

Docker Desktop – thibitisha ```docker --version``` inafanya kazi.  
VS Code Remote – ugani wa Containers (ID: ms-vscode-remote.remote-containers).

### Hatua 1 Fungua repo kwenye VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code inatambua .devcontainer/ na inaonyesha mwito.

### Hatua 2 Fungua tena ndani ya kontena

Bonyeza “Reopen in Container”. Docker hujenga picha (≈ dakika 3 mara ya kwanza).  
Unapopata mwito wa terminal, uko ndani ya kontena.

## 2.  Chaguo C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ni msakinishaji mwepesi wa kusakinisha [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, pamoja na pakiti chache.  
Conda yenyewe ni meneja wa pakiti, inayorahisisha kuanzisha na kubadilisha kati ya [**mazingira pepe**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) tofauti za Python na pakiti. Pia ni muhimu kwa kusakinisha pakiti ambazo hazipatikani kupitia `pip`.

### Hatua 0  Sakinisha Miniconda

Fuata [mwongozo wa usakinishaji wa MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) kuisanidi.

```bash
conda --version
```

### Hatua 1 Tengeneza mazingira pepe

Tengeneza faili mpya ya mazingira (*environment.yml*). Ikiwa unafuata kwa kutumia Codespaces, tengeneza hii ndani ya saraka `.devcontainer`, yaani `.devcontainer/environment.yml`.

### Hatua 2  Jaza faili lako la mazingira

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

### Hatua 3 Tengeneza mazingira yako ya Conda

Endesha amri zifuatazo kwenye mstari wa amri/terminal yako

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Njia ndogo ya .devcontainer inahusu tu usanidi wa Codespace
conda activate ai4beg
```

Rejea kwenye [mwongozo wa mazingira ya Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ikiwa utakutana na matatizo yoyote.

## 2  Chaguo D – Jupyter wa Klasiki / Jupyter Lab (kivinjari chako)

> **Hii ni kwa nani?**  
> Yeyote anayependa kiolesura cha Jupyter cha klasiki au anayetaka kuendesha daftari bila VS Code.  

### Hatua 1  Hakikisha Jupyter imesakinishwa

Kuanza Jupyter kwa mtaa, nenda kwenye terminal/mstari wa amri, elekea kwenye saraka ya kozi, na endesha:

```bash
jupyter notebook
```

au

```bash
jupyterhub
```

Hii itaanzisha mfano wa Jupyter na URL ya kuifikia itaonyeshwa ndani ya dirisha la mstari wa amri.

Ukifikia URL, unapaswa kuona muhtasari wa kozi na uweze kuvinjari faili yoyote ya `*.ipynb`. Kwa mfano, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Ongeza Funguo Zako za API

Kuhifadhi funguo zako za API salama ni muhimu wakati wa kujenga aina yoyote ya programu. Tunapendekeza usihifadhi funguo za API moja kwa moja kwenye msimbo wako. Kuweka maelezo hayo kwenye hazina ya umma kunaweza kusababisha matatizo ya usalama na hata gharama zisizotarajiwa ikiwa zitatumika na mtu mbaya.  
Hapa kuna mwongozo wa hatua kwa hatua jinsi ya kuunda faili `.env` kwa Python na kuongeza `GITHUB_TOKEN`:

1. **Elekea kwenye Saraka ya Mradi Wako**: Fungua terminal au mstari wa amri na elekea kwenye saraka kuu ya mradi wako ambapo unataka kuunda faili `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Tengeneza Faili `.env`**: Tumia mhariri wa maandishi unayopendelea kuunda faili mpya iitwayo `.env`. Ikiwa unatumia mstari wa amri, unaweza kutumia `touch` (kwa mifumo ya Unix) au `echo` (kwa Windows):

   Mifumo ya Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Hariri Faili `.env`**: Fungua faili `.env` katika mhariri wa maandishi (mfano, VS Code, Notepad++, au mhariri mwingine wowote). Ongeza mstari ufuatao kwenye faili, ukibadilisha `your_github_token_here` na tokeni yako halisi ya GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Hifadhi Faili**: Hifadhi mabadiliko na funga mhariri wa maandishi.

5. **Sakinisha `python-dotenv`**: Ikiwa bado hujasakinisha, utahitaji kusakinisha pakiti ya `python-dotenv` ili kupakia vigezo vya mazingira kutoka faili `.env` kwenye programu yako ya Python. Unaweza kuisakinisha kwa kutumia `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Pakia Vigezo vya Mazingira kwenye Skripti Yako ya Python**: Katika skripti yako ya Python, tumia pakiti ya `python-dotenv` kupakia vigezo vya mazingira kutoka faili `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Pakia vigezo vya mazingira kutoka kwa faili la .env
   load_dotenv()

   # Pata thamani ya kigezo cha GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Hiyo ni yote! Umefanikiwa kuunda faili `.env`, kuongeza tokeni yako ya GitHub, na kuipakia kwenye programu yako ya Python.

🔐 Kamwe usiweka .env kwenye git—imekwisha kwenye .gitignore.  
Maelekezo kamili ya mtoa huduma yapo katika [`providers.md`](03-providers.md).

## 4. Nini Kifuatacho?

| Nataka…            | Nenda kwa…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Anza Somo la 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Sanidi Mtoa LLM     | [`providers.md`](03-providers.md)                                       |
| Kutana na wanafunzi wengine | [Jiunge na Discord yetu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Utatuzi wa Matatizo

| Dalili                                    | Suluhisho                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Ongeza Python kwenye PATH au fungua tena terminal baada ya usakinishaji |
| `pip` haiwezi kujenga magurudumu (Windows) | `pip install --upgrade pip setuptools wheel` kisha jaribu tena. |
| `ModuleNotFoundError: dotenv`             | Endesha `pip install -r requirements.txt` (mazingira hayakuwekwa). |
| Ujenzi wa Docker unashindwa *Hakuna nafasi* | Docker Desktop ▸ *Settings* ▸ *Resources* → ongeza ukubwa wa diski. |
| VS Code inaendelea kukuuliza ufungue tena | Huenda una chaguzi zote mbili zikiwa hai; chagua moja (venv **au** kontena) |
| Makosa ya OpenAI 401 / 429                | Angalia thamani ya `OPENAI_API_KEY` / viwango vya maombi.       |
| Makosa kutumia Conda                      | Sakinisha maktaba za Microsoft AI kwa kutumia `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiarifa cha Kukataa**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->