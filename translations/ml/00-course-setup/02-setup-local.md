# ലോക്കല്‍ സെറ്റപ്പ് 🖥️

**നിങ്ങളുടെ സ്വന്തം ലാപ്ടോപ്പിൽ എല്ലാം പ്രവർത്തിപ്പിക്കാൻ നിങ്ങൾ ഇഷ്ടപ്പെടുന്നുവെങ്കിൽ ഈ ഗൈഡ് ഉപയോഗിക്കുക.**  
നിങ്ങൾക്ക് രണ്ട് മാർഗ്ഗങ്ങൾ ഉണ്ട്: **(A) നേറ്റീവ് Python + virtual-env** അല്ലെങ്കിൽ **(B) Docker ഉപയോഗിച്ചുള്ള VS Code ഡെവ് കണ്ടെയ്‌നർ**.  
എളുപ്പം തോന്നുന്നവ തിരഞ്ഞെടുക്കുക—രണ്ടും ഒരേ പാഠങ്ങളിലേക്ക് നയിക്കുന്നു.

## 1. മുൻ‌വതനങ്ങൾ

| ഉപകരണം           | പതിപ്പ് / കുറിപ്പുകൾ                                                                 |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (<https://python.org> നിന്നു ലഭിക്കും)                                        |
| **Git**            | ഏറ്റവും പുതിയത് (Xcode / Git for Windows / Linux പാക്കേജ് മാനേജർ എന്നിവയില്‍ ഒത്തുകൂടുന്നു) |
| **VS Code**        | ചാർത്താവുന്നെങ്കിലും ശുപാർശ ചെയ്യപ്പെടുന്നു <https://code.visualstudio.com>              |
| **Docker Desktop** | ഓപ്ഷന്‍ B മാത്രമാണ് ആവശ്യമാണ്. സൗജന്യ ഇൻസ്റ്റാൾ: <https://docs.docker.com/desktop/> |

> 💡 **സൂചന** – ഒരു ടെർമിനലിൽ ഉപകരണങ്ങള്‍ പരിശോധിക്കുക:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. ഓപ്ഷൻ A – നേറ്റീവ് Python (ഏറ്റവും വേഗം)

### ഘട്ടം 1  ഈ റീപ്പോ ക്ലോൺ ചെയ്യുക

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### ഘട്ടം 2  ഒരു വെർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിക്കുകയും സജീവമാക്കുകയും ചെയ്യുക

```bash
python -m venv .venv          # ഒന്ന് 만들ുക
source .venv/bin/activate     # macOS / ലിനക്സ്
.\.venv\Scripts\activate      # വിൻഡോസ് പവർഷെൽ
```

✅ പ്രോംപ്റ്റ് ഇപ്പോൾ (.venv) എന്നത് കാണിച്ചാൽ നിങ്ങൾ ഏൻവിലുണ്ട് എന്നാണർത്ഥം.

### ഘട്ടം 3 ആശ്രിതമായ പാക്കേജുകൾ ഇൻസ്റ്റാൾ ചെയ്യുക

```bash
pip install -r requirements.txt
```

[API കീകൾ ചേർക്കൽ](#3-നിങ്ങളുടെ-api-കീകൾ-ചേർക്കുക) വിഭാഗം 3-ൽ പോവുക

## 2. ഓപ്ഷൻ B – VS Code ഡെവ് കണ്ടെയ്‌നർ (Docker)

Python3, .NET, Node.js, Java ഡെവലപ്പ്മെൻറ് സപ്പോർട്ട് ചെയ്യുന്ന ഒരു Universal runtime ഉള്ള [ഡെവലപ്പ്മെന്റ് കണ്ടെയ്‌നർ](https://containers.dev?WT.mc_id=academic-105485-koreyst) ഉപയോഗിച്ച് ഈ റീപോസിറ്ററി, കോഴ്സ് ഇൻസ്റ്റാൾ ചെയ്തിട്ടുണ്ട്. ബന്ധപ്പെട്ട ക്രമീകരണം ഈ റീപോസിറ്ററിയുടെ റൂട്ട്-ലെ `.devcontainer/` ഫോൾഡറിലുള്ള `devcontainer.json` ഫയലിൽ നിർവചിച്ചിരിക്കുന്നു.

>**എന്തുകൊണ്ട് ഇത് തിരഞ്ഞെടേക്കണം?**
>Codespaces-നെ പോലെ തുല്യമായ പരിസ്ഥിതി; ആശ്രിതത്വം മാറാൻ ഇടയില്ല.

### ഘട്ടം 0 അധിക സാമഗ്രികൾ ഇൻസ്റ്റാൾ ചെയ്യുക

Docker Desktop – ```docker --version``` പ്രവർത്തിക്കുന്നതായി സ്ഥിരീകരിക്കുക.
VS Code Remote – Containers എക്സ്റ്റൻഷൻ (ID: ms-vscode-remote.remote-containers).

### ഘട്ടം 1 റീപ്പോ VS Code-ൽ തുറക്കുക

ഫയൽ ▸ ഫോൾഡർ തുറക്കുക… → generative-ai-for-beginners

VS Code .devcontainer/ കണ്ടെത്തി ഒരു പ്രോംപ് കാണിക്കും.

### ഘട്ടം 2 കണ്ടെയ്‌നറിൽ വീണ്ടും തുറക്കുക

“Reopen in Container” ക്ലിക്ക് ചെയ്യുക. Docker ആദ്യം ഇമേജ് നിർമ്മിക്കുന്നു (≈ 3 മിനിറ്റ് ആദ്യമായി).
ടെർമിനൽ പ്രോംപ്റ്റ് കാണുമ്പോൾ, നിങ്ങൾ കണ്ടെയ്‌നറിനുള്ളിൽ ആണ്.

## 2. ഓപ്ഷൻ C – മിനികോണ്ട

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, കുറച്ച് പാക്കേജുകൾ ഇൻസ്റ്റാൾ ചെയ്യാൻ ഉപയോഗിക്കുന്ന ഒരു ലഘുവായ ഇൻസ്റ്റാളർ ആണ്.
Conda പാക്കേജ് മാനേജറാണ്, ഇത് വ്യത്യസ്ത Python [**virtual environment**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)കളിലും പാക്കേജുകളിലും എളുപ്പത്തിൽ മാറാനാകും. `pip` വഴി ലഭ്യമല്ലാത്ത പാക്കേജുകൾ ഇൻസ്റ്റാൾ ചെയ്യാൻ ഇത് സഹായിക്കുന്നു.

### ഘട്ടം 0  Miniconda ഇൻസ്റ്റാൾ ചെയ്യുക

[MiniConda ഇൻസ്റ്റളേഷൻ ഗൈഡ്](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) പിന്തുടരുക.

```bash
conda --version
```

### ഘട്ടം 1 ഒരു വെർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിക്കുക

പുതിയ environment.yml എന്ന എൻവയോൺമെന്റ് ഫയൽ സൃഷ്ടിക്കുക. Codespaces ഉപയോഗിക്കുന്നവരാണെങ്കിൽ, `.devcontainer` ഡയറക്ടറിയിൽ ഈ ഫയൽ സൃഷ്ടിക്കുക, ഉദാ: `.devcontainer/environment.yml`.

### ഘട്ടം 2 നിങ്ങളുടെ എൻവയോൺമെന്റ് ഫയൽ പൂരിപ്പിക്കുക

താഴെ കൊടുത്തിരിക്കുന്ന snippet `environment.yml` ഫയലിലേക്ക് ചേർക്കുക

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

### ഘട്ടം 3 നിങ്ങളുടെ Conda എൻവയോൺമെന്റ് സൃഷ്ടിക്കുക

താഴെ കൊടുത്തിരിക്കുന്ന കമാൻഡുകൾ നിങ്ങളുടെ കമാൻഡ് ലൈൻ/ടെർമിനലിൽ പ്രവർത്തിപ്പിക്കുക

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer ഉപപാതം കോഡ്സ്പെയ്സ് ക്രമീകരണങ്ങൾക്ക് മാത്രം ബാധകമാണ്
conda activate ai4beg
```

പ്രശ്നങ്ങൾ സംഭവിച്ചാൽ [Conda എൻവയോൺമെന്റുകൾ ഗൈഡ്](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) നോക്കുക.

## 2  ഓപ്ഷൻ D – ക്ലാസിക് Jupyter / Jupyter Lab (ബ്രൗസറിൽ)

> **ഇത് ആരுக்கാണ്?**  
> ക്ലാസിക് Jupyter ഇന്റർഫേസ് ഇഷ്ടപ്പെടുന്നവർക്ക് അല്ലെങ്കിൽ VS Code ഇല്ലാതെ നോട്ട്‌ബുക്കുകൾ ഓടിക്കാൻ ആഗ്രഹിക്കുന്നവർക്ക്.  

### ഘട്ടം 1  Jupyter ഇൻസ്റ്റാൾ ചെയ്തിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക

Jupyter ലോക്കലി തുടങ്ങാൻ, ടെർമിനലിലോ കമാൻഡ് ലൈനിലോ കോഴ്‌സ് ഡയറക്ടറിയിലേക്ക് നീങ്ങുക, ശേഷം താഴെ ആജ്ഞാപാലനം പ്രവർത്തിപ്പിക്കുക:

```bash
jupyter notebook
```

അല്ലെങ്കിൽ

```bash
jupyterhub
```

ഇത് ഒരു Jupyter ഇൻസ്റ്റൻസ് ആരംഭിക്കും, ആക്‌സസ് ചെയ്യാനുള്ള URL കമാൻഡ് ലൈൻ വിൻഡോയിൽ കാണിക്കും.

URL ആക്‌സസ് ചെയ്താൽ, കോഴ്‌സ് ഔട്ട്‌ലൈനും ഏതെങ്കിലും `*.ipynb` ഫയലുകളിലേക്ക് പ്രവേശനവും കാണാം. ഉദാ. `08-building-search-applications/python/oai-solution.ipynb`.

## 3. നിങ്ങളുടെ API കീകൾ ചേർക്കുക

API കീകൾ സുരക്ഷിതമായി സൂക്ഷിക്കുന്നതു് ഏത് ആപ്ലിക്കേഷനും നിർമ്മിക്കുമ്പോൾ വളരെ പ്രധാനമാണ്. നിങ്ങളുടെ കോഡിൽ നേരിട്ട് API കീകൾ സൂക്ഷിക്കാൻ സാദ്ധ്യമല്ല. അതേസമയം പബ്ലിക് റിപോസിറ്ററിയിൽ ഇത്തരത്തിലുള്ള വിവരങ്ങൾ കമിറ്റുചെയ്യുന്നതു് സുരക്ഷാ പ്രശ്നങ്ങൾക്കും അനാവശ്യ ചിലവുകൾക്കും ഇടയാക്കാം.
Python-ഇനുള്ള `.env` ഫയൽ സൃഷ്ടിക്കുകയും Microsoft Foundry Models ക്രെഡൻഷ്യലുകൾ ചേർക്കുന്നതിന്റെ വിശദമായ ഗൈഡ് ഇവിടെ:

> **കുറിപ്പ്:** GitHub Models-നും അതിന്റെ `GITHUB_TOKEN` ഗ്ലോബലിനും 2026 ജൂലൈ അവസാനം വിരമിക്കുന്നു. ഈ ഗൈഡ് [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ഉപയോഗിക്കുന്നു. അഞ്ചു ഓഫ്ലൈൻ ആയി പ്രവർത്തിക്കാൻ ആഗ്രഹിക്കുന്നുവെങ്കിൽ [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) കാണുക.

1. **നിങ്ങളുടെ പ്രോജക്ട് ഡയറക്ടറിയിലേക്ക് പോകുക**: ടെർമിനലോ കമാൻഡ് പ്രോംപ്റ്റിലോ തുറന്ന് `.env` ഫയൽ സൃഷ്ടിക്കാനുള്ള പ്രോജക്ട് റൂട്ട് ഡയറക്ടറിയിലേക്ക് പോകുക.

   ```bash
   cd path/to/your/project
   ```

2. **`.env` ഫയൽ സൃഷ്ടിക്കുക**: ഇഷ്ടമുള്ള ടെക്സറ്റ് എഡിറ്റർ ഉപയോഗിച്ച് `.env` എന്ന പുതിയ ഫയൽ സൃഷ്ടിക്കുക. കമാൻഡ് ലൈനിൽ ആണെങ്കിൽ Unix-ൽ `touch`, Windows-ൽ `echo` ഉപയോഗിക്കാം:

   Unix പ്ലാറ്റ്ഫോമുകൾ:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` ഫയൽ എഡിറ്റ് ചെയ്യുക**: VS Code, Notepad++ പോലുള്ള ടെക്സറ്റ് എഡിറ്ററിൽ `.env` തുറക്കുക. Microsoft Foundry പ്രോജക്ട് എൻഡ്‌പോയിന്റും API കീയും പൂരിപ്പിച്ച് താഴെ കൊടുത്ത വരികൾ ചേർക്കുക:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **ഫയൽ സെവ് ചെയ്യുക**: മാറ്റങ്ങൾ സേവ് ചെയ്ത് എഡിറ്റർ അടച്ചിടുക.

5. **`python-dotenv` ഇൻസ്റ്റാൾ ചെയ്യുക**: ഇതുവരെ ഇൻസ്റ്റാൾ ചെയ്തിട്ടില്ലെങ്കിൽ Python ആപ്ലിക്കേഷനിലേക്ക് `.env` ഫയലിൽ നിന്നുള്ള എൻവയോൺമെന്റ് വാരിയബിളുകൾ ലോഡ് ചെയ്യാൻ `python-dotenv` പാക്കേജ് ഇൻസ്റ്റാൾ വേണം. കാണിക്കാതെ `pip` ഉപയോഗിക്കുക:

   ```bash
   pip install python-dotenv
   ```

6. **Python സ്ക്രിപ്റ്റിൽ എൻവയോൺമെന്റ് വാരിയബിളുകൾ ലോഡ് ചെയ്യുക**: Python സ്ക്രിപ്റ്റിൽ `python-dotenv` പാക്കേജ് ഉപയോഗിച്ചെത്തി `.env` ഫയലിൽ നിന്നുള്ള റെക്കോർഡുകൾ ലോഡ് ചെയ്യുക:

   ```python
   from dotenv import load_dotenv
   import os

   # .env ഫയലിൽ നിന്ന് പരിസ്ഥിതി ചാരിത്തങ്ങൾ ലോഡ് ചെയ്യുക
   load_dotenv()

   # Microsoft Foundry Models ചാരിത്തങ്ങളിൽ പ്രവേശിക്കുക
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

കഴിഞ്ഞു! നിങ്ങൾ വിജയകരമായി `.env` ഫയൽ സൃഷ്ടിച്ചു, Microsoft Foundry Models ക്രെഡൻഷ്യലുകൾ ചേർത്തു, Python ആപ്ലിക്കേഷനിലേക്ക് ലോഡ് ചെയ്തു.

🔐 .env ഫയൽ കണ്ട്രോൾ അടയ്ക്കുക, അത് .gitignore-ലുണ്ട്.
മുഴുവൻ പ്രൊവൈഡർ നിർദ്ദേശങ്ങൾ [`providers.md`](03-providers.md) ൽ കാണാം.

## 4. ഇനി എന്ത്?

| ഞാൻ ചെയ്യണം…       | പോകുക…                                                                |
|---------------------|-------------------------------------------------------------------------|
| പാഠം 1 തുടങ്ങുക     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| LLM പ്രൊവൈഡർ സെറ്റപ്പ് ചെയ്യുക | [`providers.md`](03-providers.md)                                       |
| മറ്റ് പഠിതാക്കളെ കാണുക | [നമ്മുടെയൊരു Discord ൽ ചേർക്കുക](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. പ്രശ്നപരിഹാരം

| ലക്ഷണം                               | പരിഹാരം                                                           |
|-------------------------------------|-------------------------------------------------------------------|
| `python not found`                  | Python നെ PATH-ിൽ ചേർക്കുക അല്ലെങ്കിൽ ഇൻസ്റ്റാൾ ചെയ്ത ശേഷം ടെർമിനൽ വീണ്ടും തുറക്കുക       |
| `pip` വീലുകൾ (wheels) നിർമ്മിക്കാൻ കഴിയുന്നില്ല (Windows) | `pip install --upgrade pip setuptools wheel` പിന്നീട് വീണ്ടും ശ്രമിക്കുക.       |
| `ModuleNotFoundError: dotenv`       | `pip install -r requirements.txt` ഓടിക്കുക (എൻവ നിർമിച്ചിട്ടില്ല).               |
| Docker build പരാജയപ്പെടുന്നു *No space left* | Docker Desktop ▸ *Settings* ▸ *Resources* → ഡിസ്ക് വലുപ്പം വർദ്ധിപ്പിക്കുക.      |
| VS Code വീണ്ടും തുറക്കണമെന്ന് നിർബന്ധപ്പെടുന്നു | രണ്ടും പ്രവർത്തനത്തിൽ ഉള്ളതിനാൽ ഒന്ന് തിരഞ്ഞെടുത്തുക (venv **അല്ലെങ്കിൽ** കണ്ടെയ്‌നർ)     |
| OpenAI 401 / 429 പിശകുകൾ          | `OPENAI_API_KEY` മൂല്യം പരിശോധിക്കുക / അഭ്യർത്ഥന നിരക്ക് പരിധികൾ പരിശോധിക്കുക.          |
| Conda ഉപയോഗത്തിൽ പിശകുകൾ        | Microsoft AI ലൈബ്രറീസ് ഇൻസ്റ്റാൾ ചെയ്യാൻ `conda install -c microsoft azure-ai-ml` ഓടിക്കുക|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->