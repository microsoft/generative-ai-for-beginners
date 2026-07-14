# Usanidi wa Mitaa 🖥️

**Tumia mwongozo huu ikiwa unapendelea kuendesha kila kitu kwenye kompyuta yako binafsi.**   
Una njia mbili: **(A) Python ya asili + virtual-env** au **(B) VS Code Dev Container na Docker**.  
Chagua ile yoyote inayohisi rahisi—zote zinapeleka kwenye somo moja.

## 1. Mahitaji ya Awali

| Zana               | Toleo / Maelezo                                                                    |
|--------------------|-----------------------------------------------------------------------------------|
| **Python**         | 3.10 + (pata kutoka <https://python.org>)                                         |
| **Git**            | Zaidi ya zote (huja na Xcode / Git kwa Windows / menyu ya pakiti ya Linux)         |
| **VS Code**        | Si ya lazima lakini inashauriwa <https://code.visualstudio.com>                    |
| **Docker Desktop** | *Kwanza* kwa Chaguo B. Usanidi bure: <https://docs.docker.com/desktop/>           |

> 💡 **Ushauri** – Thibitisha zana kwenye terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Chaguo A – Python Asili (kwa haraka zaidi)

### Hatua 1 Nakili git repo hii

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Hatua 2 Unda na wezesha mazingira pepe

```bash
python -m venv .venv          # tengeneza moja
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Kidokezo sasa kinapaswa kuanza na (.venv)—hii inamaanisha uko ndani ya mazingira.

### Hatua 3 Sakinisha utegemezi

```bash
pip install -r requirements.txt
```

Ruka hadi Sehemu 3 kuhusu [vifunguo vya API](#3-ongeza-vifunguo-vyako-vya-api)

## 2. Chaguo B – VS Code Dev Container (Docker)

Tumeandaa hazina hii na kozi kwa kutumia [kontena la maendeleo](https://containers.dev?WT.mc_id=academic-105485-koreyst) ambalo lina runtime ya Universal inayounga mkono maendeleo ya Python3, .NET, Node.js na Java. Mipangilio husika imefafanuliwa katika faili `devcontainer.json` iliyoko kwenye folda `.devcontainer/` kwenye mzizi wa hazina hii.

>**Kwa nini uchague hii?**
>Mazingira sawa na Codespaces; hakuna mabadiliko ya utegemezi.

### Hatua 0 Sakinisha ziada

Docker Desktop – hakikisha ```docker --version``` inafanya kazi.
VS Code Remote – ugani wa Containers (ID: ms-vscode-remote.remote-containers).

### Hatua 1 Fungua repo katika VS Code

Faili ▸ Fungua Folda… → generative-ai-for-beginners

VS Code hugundua .devcontainer/ na kuonyesha kidokezo.

### Hatua 2 Fungua tena ndani ya kontena

Bonyeza “Reopen in Container”. Docker hujenga picha (karibu dakika 3 mara ya kwanza).
Unapopata kidokezo cha terminal, uko ndani ya kontena.

## 2. Chaguo C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ni kifungaji nyepesi cha kusakinisha [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, pamoja na pakiti chache.
Conda ni meneja wa pakiti, ambaye hufanya iwe rahisi kuanzisha na kubadili kati ya [mazingira pepe ya Python](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) na pakiti. Pia ni msaada kwa kusakinisha pakiti zisizopatikana kupitia `pip`.

### Hatua 0 Sakinisha Miniconda

Fuata [mwongozo wa usakinishaji wa MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) kuiweka.

```bash
conda --version
```

### Hatua 1 Unda mazingira pepe

Unda faili mpya ya mazingira (*environment.yml*). Ikiwa unafuata kupitia Codespaces, tengeneza hili ndani ya saraka ya `.devcontainer`, kwa hivyo `.devcontainer/environment.yml`.

### Hatua 2 Jaza faili lako la mazingira

Ongeza kipande kinachofuata kwenye `environment.yml`

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

### Hatua 3 Unda mazingira ya Conda

Endesha amri hapa chini katika mstari wa amri/terminal yako

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Njia ndogo ya .devcontainer inatumika tu kwa mipangilio ya Codespace
conda activate ai4beg
```

Rejelea [mwongozo wa mazingira ya Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ikiwa utakutana na matatizo yoyote.

## 2 Chaguo D – Jupyter Klasiki / Jupyter Lab (kutumia kivinjari chako)

> **Hii ni kwa nani?**  
> Yeye yeyote anayependa kiolesura cha klasik cha Jupyter au anataka kuendesha daftari bila VS Code.  

### Hatua 1 Hakikisha Jupyter imesakinishwa

Ili kuanza Jupyter kwa luga, nenda kwenye terminal/mstari wa amri, elekea kwenye saraka ya kozi, na endesha:

```bash
jupyter notebook
```

au

```bash
jupyterhub
```

Hii itaanzisha mfano wa Jupyter na URL ya kuupata itaonyeshwa ndani ya dirisha la mstari wa amri.

Mara utakaporejea URL hiyo, utapata muhtasari wa kozi na kupata navigeta kwa faili yoyote ya `*.ipynb`. Kwa mfano, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Ongeza Vifunguo Vyako vya API

Kuhifadhi vifunguo vyako vya API salama ni muhimu unapoanzisha aina yoyote ya programu. Tunapendekeza kutoweka vifunguo vya API moja kwa moja kwenye msimbo wako. Kuweka maelezo hayo kwenye hazina ya umma kunaweza kusababisha matatizo ya usalama na hata gharama zisizotarajiwa kama zitumiwa na mtu hasi.
Hapa kuna mwongozo hatua kwa hatua wa jinsi ya kuunda faili `.env` ya Python na kuongeza maelezo yako ya mikopo ya Microsoft Foundry Models:

> **Kumbuka:** Mfano wa GitHub (na kigezo chake `GITHUB_TOKEN`) unakwisha uhai mwishoni mwa Julai 2026. Mwongozo huu unatumia [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) badala yake. Unapendelea kufanya kazi bila mtandao kabisa? Tazama [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Nenda kwenye Saraka ya Mradi Wako**: Fungua terminal au amri na elekea kwenye saraka kuu ya mradi ambapo unataka kuunda faili `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Unda Faili `.env`**: Tumia mhariri wa maandishi unaopendelea kuunda faili jipya liitwalo `.env`. Ikiwa unatumia mstari wa amri, unaweza kutumia `touch` (kwa mifumo ya Unix) au `echo` (kwa Windows):

   Mfumo wa Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Hariri Faili `.env`**: Fungua faili `.env` kwa mhariri wa maandishi (mfano, VS Code, Notepad++, au mhariri mwingine yeyote). Ongeza mistari ifuatayo kwenye faili, ukibadilisha sehemu za maelezo na anwani halisi ya mradi wa Microsoft Foundry na ufunguo wa API:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Hifadhi Faili**: Hifadhi mabadiliko na fungua mhariri wa maandishi.

5. **Sakinisha `python-dotenv`**: Ikiwa bado hujasakinisha, utahitaji pakiti `python-dotenv` ili kupakia mabadiliko ya mazingira kutoka faili `.env` kwenye programu yako ya Python. Unaweza kuisakinisha kwa kutumia `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Pakia Mabadiliko ya Mazingira katika Script yako ya Python**: Katika script ya Python, tumia pakiti `python-dotenv` kupakia mabadiliko ya mazingira kutoka faili `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Pakua vigezo vya mazingira kutoka kwa faili .env
   load_dotenv()

   # Pata vigezo vya Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Hiyo ndiyo! Umefanikiwa kuunda faili `.env`, kuongeza maelezo yako ya mikopo ya Microsoft Foundry Models, na kwaya yao ndani ya programu yako ya Python.

🔐 Usawili faili .env—tayari ipo kwenye .gitignore.
Maelekezo kamili ya mtoa huduma yako yapo katika [`providers.md`](03-providers.md).

## 4. Nini kinachofuata?

| Ninataka…         | Nenda kwa…                                                              |
|---------------------|------------------------------------------------------------------------|
| Anza Somo la 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Sanidi Mtoa Huduma wa LLM | [`providers.md`](03-providers.md)                                       |
| Kutana na wanafunzi wengine | [Jiunge na Discord yetu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Utatuzi wa Matatizo

| Dalili                                   | Fix                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Ongeza Python kwenye PATH au fungua tena terminal baada ya usakinishaji |
| `pip` haiwezi kujenga wheels (Windows)   | `pip install --upgrade pip setuptools wheel` kisha jaribu tena.        |
| `ModuleNotFoundError: dotenv`             | Endesha `pip install -r requirements.txt` (mazingira hayakwasishwa).          |
| Ujenzi wa Docker unabomoka *Hakuna nafasi iliyobaki*| Docker Desktop ▸ *Mipangilio* ▸ *Rasilimali* → ongeza ukubwa wa diski. |
| VS Code inaendelea kubonyeza kufungua tena | Inawezekana kuwa chaguzi zote zimewashwa; chagua moja (venv **au** kontena)|
| Makosa ya OpenAI 401 / 429               | Angalia thamani ya `OPENAI_API_KEY` / mipaka ya kiwango cha maombi.       |
| Makosa wakati wa kutumia Conda           | Sakinisha maktaba za AI za Microsoft kwa kutumia `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->