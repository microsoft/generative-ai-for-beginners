# ഈ കോഴ്സ് ആരംഭിക്കുന്നത്

ജനറേറ്റീവ് AI ഉപയോഗിച്ച് നിങ്ങൾ നിർമ്മിക്കുന്നതിൽ സംബന്ധിക്കാൻ തുടങ്ങിയതിൽ ഞങ്ങൾ വളരെ ആവേശത്തോടെ പോകുന്നു!

നിങ്ങളുടെ വിജയം ഉറപ്പാക്കാൻ, ഈ പേജ് സജ്ജീകരണ നടപടികൾ, സാങ്കേതിക ആവശ്യകതകൾ, സഹായം എടുക്കേണ്ടിടങ്ങൾ എന്നിവ വിശദീകരിക്കുന്നു.

## സജ്ജീകരണ നടപടികൾ

ഈ കോഴ്സ് ആരംഭിക്കാൻ, നിങ്ങൾ താഴെ കൊടുത്തിരിക്കുന്ന കാര്യങ്ങൾ പൂർത്തിയാക്കേണ്ടതാണ്.

### 1. ഈ റിപൊ ഫോർക്ക് ചെയ്യുക

[ഈ മുഴുവൻ റിപൊ ഫോർക്ക് ചെയ്യുക](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) നിങ്ങളുടെ ഗിറ്റ്‌ഹബ് അക്കൗണ്ടിൽ, കോഡ് മാറ്റാനും ചലഞ്ചുകൾ പൂർത്തിയാക്കാനും. നിങ്ങൾക്ക് ഇത് [സ്റ്റാർ ചെയ്യാനും (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) സാധിക്കും, ഇത് കണ്ടെത്താനും ബന്ധപ്പെട്ട റിപോസിറ്ററികൾ കണ്ടെത്താനും സഹായിക്കും.

### 2. കോഡ്സ്പേസ് സൃഷ്ടിക്കുക

കോഡ് ഓടുന്‌പോൾ ആശ്രിത പ്രശ്നങ്ങൾ ഒഴിവാക്കാൻ, ഈ കോഴ്സ് [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) ൽ ഓടിക്കാൻ ഞങ്ങൾ ശുപാർശ ചെയ്യുന്നു.

നിങ്ങളുടെ ഫോർക്കിൽ: **Code -> Codespaces -> New on main**

![കോഡ്സ്പേസ് സൃഷ്ടിക്കാൻ ബട്ടണുകൾ കാണിക്കുന്ന ഡയലോഗ്](../../../translated_images/ml/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 ഒരു സീക്രട്ട് ചേർക്കുക

1. ⚙️ ഗിയർ ഐകൺ -> കമാൻഡ് പാലറ്റ് -> Codespaces : Manage user secret -> പുതിയ ഒരു സീക്രട്ട് ചേർക്കുക.
2. പേര് OPENAI_API_KEY ആക്കി, നിങ്ങളുടെ കീ പേസ്റ്റ് ചെയ്ത്, സേവ് ചെയ്യുക.

### 3. ഇനി എന്തുകണ്ട?

| ഞാൻ ചെയ്യാൻ ആഗ്രഹിക്കുന്നു… | പോകുക…                                                                                   |
|---------------------|-------------------------------------------------------------------------|
| പാഠം 1 ആരംഭിക്കുക      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ഓഫ്ലൈനായി ജോലി ചെയ്യുക        | [`setup-local.md`](02-setup-local.md)                                   |
| ഒരു LLM പ്രൊവൈഡർ സജ്ജീകരിക്കുക | [`providers.md`](03-providers.md)                                        |
| മറ്റ് പഠിതാക്കളെ കാണുക | [ഞങ്ങളുടെ ഡിസ്കോർഡ് ചതകടിയിലേക്ക് ചേരുക](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## പ്രശ്നപരിഹാരം


| ലക്ഷണം                                   | പരിഹാരം                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| കണ്ടെയ്‌നർ നിർമ്മാണം 10 മിനിറ്റ് വരെ നിലച്ചിരിക്കുന്നു            | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | ടെർമിനൽ ചേർക്കപ്പെട്ടിട്ടില്ല; ക്ലിക്ക് ചെയ്യുക **+** ➜ *bash*                    |
| OpenAI-യിൽ നിന്നുള്ള `401 Unauthorized`            | തെറ്റായ / കാലഹരണപ്പെട്ട `OPENAI_API_KEY`                                |
| VS Code “Dev container mounting…” കാണിക്കുന്നു   | ബ്രൗസർ ടാബ് റിഫ്രഷ് ചെയ്യുക—Codespaces ചിലപ്പോൾ ബന്ധം നഷ്ടപ്പെടുന്നു   |
| നോട്ട്‌ബുക്ക് കേർണൽ കാണുന്നില്ല                   | നോട്ട്‌ബുക്ക് മെനു ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix അടിസ്ഥാനപരമായ സിസ്റ്റങ്ങളിലേക്ക്:

   ```bash
   touch .env
   ```

   വിൻഡോസ്:

   ```cmd
   echo . > .env
   ```

3. **`.env` ഫയൽ എഡിറ്റ് ചെയ്യുക**: ഒരു ടെക്സ്റ്റ് എഡിറ്ററില (ഉദാ: VS Code, Notepad++, അല്ലെങ്കിൽ മറ്റേതെങ്കിലും എഡിറ്റർ) `.env` ഫയൽ തുറക്കുക. നിങ്ങളുടെ യഥാർത്ഥ Microsoft Foundry Models എന്റ്പോയിന്റ്, കീ എന്നിവ ഉൾപ്പെടുന്ന വയർഹോൾഡറുകൾ മാറ്റി താഴെ നൽകുന്ന വരികൾ ഫയലിൽ ചേർക്കുക ([`providers.md`](03-providers.md) കാണുക).

   > **ഗുരുതര വാർത്ത:** GitHub മോഡലുകൾ (അതിന്റെ `GITHUB_TOKEN` വേരിയബിൾ ഉടൻ 2026 ജൂലൈ അവസാനത്തോടെ പിരിച്ചുനീക്കം ചെയ്യപ്പെടുന്നു). പകരം [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ഉപയോഗിക്കുക.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **ഫയൽ സേവ് ചെയ്യുക**: മാറ്റങ്ങൾ സേവ് ചെയ്ത് ടെക്സ്റ്റ് എഡിറ്റർ അടയ്ക്കുക.

5. **`python-dotenv` ഇൻസ്റ്റാൾ ചെയ്യുക**: നിങ്ങൾ ഇതിനകം ഇതു ഇൻസ്റ്റാൾ ചെയ്തിട്ടില്ലെങ്കിൽ, `.env` ഫയലിൽ നിന്നുള്ള എൻവയോൺമെന്റ് വേരിയബിൾസ് നിങ്ങളുടെ Python അപ്പ്ലിക്കേഷനിലേക്ക് ലോഡ് ചെയ്യാൻ `python-dotenv` പാക്കേജ് ഇൻസ്റ്റാൾ ചെയ്യേണ്ടതാണ്. ഇത് `pip` ഉപയോഗിച്ച് ഇൻസ്റ്റാൾ ചെയ്യാം:

   ```bash
   pip install python-dotenv
   ```

6. **Python സ്ക്രിപ്റ്റിൽ എൻവയോൺമെന്റ് വേരിയബിൾസ് ലോഡ് ചെയ്യുക**: നിങ്ങളുടെ Python സ്ക്രിപ്റ്റിൽ, `.env` ഫയലിൽ നിന്നുള്ള എൻവയോൺമെന്റ് വേരിയബിൾസ് ലോഡ് ചെയ്യാൻ `python-dotenv` പാക്കേജ് ഉപയോഗിക്കുക:

   ```python
   from dotenv import load_dotenv
   import os

   # .env ഫയലിൽ നിന്നുള്ള പരിതസ്ഥിതി മാറ്റങ്ങൾ ലോഡ് ചെയ്യുക
   load_dotenv()

   # Microsoft Foundry മോഡലുകളുടെ മാറ്റങ്ങളിലേക്ക് ആക്‌സസ് ചെയ്യുക
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

അതല്ലോ! നിങ്ങൾ വിജയകരമായി `.env` ഫയൽ സൃഷ്ടിച്ചു, Microsoft Foundry Models ക്രെഡെൻഷ്യലുകൾ ഉൾപ്പെടുത്തി, Python അപ്പ്ലിക്കേഷനിൽ ലോഡ് ചെയ്തു.

## നിങ്ങളുടെ കമ്പ്യൂട്ടറിൽ ലോക്കലായി പ്രവർത്തിപ്പിക്കാൻ

കമ്പ്യൂട്ടറിൽ കോഡ് ലോക്കലായി പ്രവർത്തിപ്പിക്കാൻ, നിങ്ങൾക്കു ഏതെങ്കിലും പതിപ്പിൽ [Python ഇൻസ്റ്റാൾ ചെയ്ത്](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) വെച്ചിരിക്കണം.

പിന്നീട് ഈ റിപോസിറ്ററി ഉപയോഗിക്കാനായി, അതു ക്ലോൺ ചെയ്യണം:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

എല്ലാം പരിശോധിച്ചശേഷം, നിങ്ങൾ ആരംഭിക്കാം!

## ഓപ്ഷണൽ നടപടികൾ

### മിനികോണ്ട ഇൻസ്റ്റാൾ ചെയ്യുക

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, ചില പാക്കേജുകൾ ലളിതമായി ഇൻസ്റ്റാൾ ചെയ്യാൻ ഉപയോഗിക്കുന്ന ഒരു ലളിതമായ ഇൻസ്റ്റാളർ ആണ്.
Conda സ്വയം ഒരു പാക്കേജ് മാനേജറാണ്, Python [**വർച്വൽ എൻവയോൺമെന്റുകൾ**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) കൂടാതെ പാക്കേജുകൾ സജ്ജീകരിക്കാൻ, മാറാൻ സുഖമാക്കുന്നു. `pip` വഴി ലഭ്യമല്ലാത്ത പാക്കേജുകൾ ഇൻസ്റ്റാൾ ചെയ്യാൻ ഇത് സഹായിക്കും.

[MiniConda ഇൻസ്റ്റാളേഷൻ ഗൈഡ്](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) അനുഗമിച്ച് സജ്ജമാക്കാം.

മിനികോണ്ട ഇൻസ്റ്റാൾ ചെയ്തശേഷം, നിങ്ങൾക്ക് റിപോസിറ്ററി [ക്ലോൺ ചെയ്യേണ്ടതാണ്](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ഇനിയും ചെയ്യാതെ ഉണ്ടായാൽ)

തുടർന്ന്, നിങ്ങൾക്ക് ഒരു വർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിക്കണം. ഇതിന് conda ഉപയോഗിച്ച് ആണ്, പുതിയ എൻവയോൺമെന്റ് ഫയൽ (_environment.yml_) സൃഷ്ടിക്കുക. Codespaces ഉപയോഗിച്ച് പോവുകയാണെങ്കിൽ, `.devcontainer` ഡയറക്ടറിയിൽ ഇത് സൃഷ്ടിക്കുക, അതായത് `.devcontainer/environment.yml`.

താഴെ കാണുന്ന കോഡ് സെർപ്പറ്റിനൊപ്പം നിങ്ങളുടെ എൻവയോൺമെന്റ് ഫയൽ പൂരിപ്പിക്കുക:

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

conda ഉപയോഗിക്കുന്നതിൽ പിഴവുകൾ സംഭവിക്കുകയാണെങ്കിൽ, താഴെക്കൊടുത്ത കമാൻഡ് ടേർമിനലിൽ ഓടിച്ച് Microsoft AI ലൈബ്രറികളു ന് മാനുവലായി ഇൻസ്റ്റാൾ ചെയ്യുക.

```
conda install -c microsoft azure-ai-ml
```

എൻവയോൺമെന്റ് ഫയൽ ഞങ്ങളുടെ ആവശ്യമായ ആശ്രിതങ്ങൾ വ്യക്തമാക്കുന്നു. `<environment-name>` എന്ന് പറയുന്നത് നിങ്ങളുടെ Conda എൻവയോൺമെന്റിനായി നാമം നൽകേണ്ടത്, `<python-version>` എന്ന് പറയുന്നത് നിങ്ങൾ ഉപയോഗിക്കാൻ ആഗ്രഹിക്കുന്ന Python പതിപ്പ്, ഉദാ: `3` എന്നത് Python ന്റെ ഏറ്റവും പുതിയ മേജർ പതിപ്പാണ്.

ഇത് പൂർത്തിയായി, താഴെയുള്ള കമാൻഡുകൾ നിങ്ങളുടെ കമാൻഡ് ലൈൻ/ടേർമിനലിൽ ഓടിച്ച് Conda എൻവയോൺമെന്റ് സൃഷ്ടിക്കാം

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer ഉപപാതം yalnızca Codespace ക്രമീകരണങ്ങൾക്ക് ബാധകമാണ്
conda activate ai4beg
```

പ്രശ്നങ്ങൾയുണ്ടെങ്കിൽ [Conda എൻവയോൺമെന്റ് മാർഗ്ഗനിർദേശം](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) കാണുക.

### Python പിന്തുണാ എക്സ്റ്റൻഷൻ ഉൾക്കൊള്ളിച്ച Visual Studio Code ഉപയോഗിക്കൽ

ഈ കോഴ്സ് തുടർച്ചയായി ഉപയോഗിക്കാൻ [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) എഡിറ്ററിനൊപ്പം [Python പിന്തുണാ എക്സ്റ്റൻഷൻ](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ഇൻസ്റ്റാൾ ചെയ്യാൻ ഞങ്ങൾ ശുപാർശ ചെയ്യുന്നു. ഇത് നിർബന്ധമല്ല, ഒരു ശുപാർശ മാത്രമാണ്.

> **ഗുരുതര കുറിപ്പ്**: കോഴ്സ് റിപോസിറ്ററി VS Code ൽ തുറക്കുമ്പോൾ, പ്രോജക്ട് ഒരു കണ്ടെയ്‌നറിൽ സജ്ജീകരിക്കാൻ നിങ്ങളുടെ ഓപ്ഷൻ ഉണ്ട്. ഇത് കോഴ്സ് റിപോസിറ്ററിയിലുള്ള പ്രത്യേക `.devcontainer` ഡയറക്ടറിയാണ് കാരണം. ഇതിനെ കുറിച്ച് പിന്നീട് വിശദീകരിക്കുന്നു.

> **ഗുരുതര കുറിപ്പ്**: നിങ്ങൾ ക്ലോൺ ചെയ്ത് ഡയറക്ടറി VS Code ൽ തുറന്നാൽ, ഇത് നിങ്ങളുടെ Python പിന്തുണാ എക്സ്റ്റൻഷൻ ഇൻസ്റ്റാൾ ചെയ്യാൻ സ്വാഭാവികമായി നിർദ്ദേശിക്കും.

> **ഗുരുതര കുറിപ്പ്**: VS Code നിങ്ങൾക്ക് റിപോസിറ്ററി കണ്ടെയ്‌നറിൽ വീണ്ടും തുറക്കാൻ നിർദ്ദേശിക്കുമ്പോൾ, ലൊക്കലി ഇൻസ്റ്റാൾ ചെയ്ത Python വേർഷൻ ഉപയോഗിക്കാൻ ആ അപേക്ഷ കാണാതെപോയി.

### ബ്രൗസറിൽ Jupyter ഉപയോഗിക്കൽ

നിങ്ങൾ കുറേ മനോഹരമായ വികസന പരിതസ്ഥിതി സൂക്ഷിക്കുന്ന [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) പരിതസ്ഥിതി, ബ്രൗസറിൽ തന്നെയാണ് പ്രവർത്തിപ്പിക്കാൻ കഴിയുന്നത്. ക്ലാസിക് Jupyter, [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) എന്നിവ ഓട്ടോ-കമ്പ്ലിഷൻ, കോഡ് ഹൈലൈറ്റിംഗ് തുടങ്ങിയ സൗകര്യങ്ങൾ നൽകുന്നു.

Jupyter ലോക്കലായി പ്രവർത്തിപ്പിക്കാൻ, ടേർമിനൽ/കമാൻഡ് ലൈൻ തുറന്ന് കോഴ്സ് ഡയറക്ടറിയിൽ പോകുക, പിന്നെ നടപ്പിലാക്കുക:

```bash
jupyter notebook
```

അല്ലെങ്കിൽ

```bash
jupyterhub
```

ഇത് ഒരു Jupyter ഇൻസ്റ്റൻസ് ആരംഭിക്കും, അതിന്റെ URL കമാൻഡ് ലൈൻ വിൻഡോയിൽ കാണിക്കും.

URL ആക്സസ് ചെയ്താൽ, കോഴ്സ് റിലേഷൻ കാണാനും ഏതെങ്കിലും `*.ipynb` ഫയലിലേക്ക് പോകാനും കഴിയും. ഉദാ: `08-building-search-applications/python/oai-solution.ipynb`.

### കണ്ടെയ്‌നറിൽ പ്രവർത്തിപ്പിക്കൽ

നിങ്ങളുടെ കമ്പ്യൂട്ടറിൽ അല്ലെങ്കിൽ Codespace ൽ എല്ലാം സജ്ജീകരിക്കുന്നതിന് പകരം [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) ഉപയോഗിക്കാം. കോഴ്സ് റിപോസിറ്ററിയിലെ പ്രത്യേക `.devcontainer` ഫോൾഡർ VS Code-ന് പ്രോജക്ട് കണ്ടെയ്‌നറിൽ സജ്ജീകരിക്കാൻ സഹായിക്കുന്നു. Codespaces ഒഴികെയുള്ള ഇടങ്ങളിൽ ഇത് Docker ഇൻസ്റ്റാൾ ചെയ്യേണ്ടതാണ്, വളരെ പ്രവർത്തനക്ഷമതയും വേണം, അതിനാൽ കണ്ടെയ്‌നറിൽ പരിചയസമ്പന്നരായി മാത്രം ഞങ്ങൾ ശുപാർശ ചെയ്യുന്നു.

GitHub Codespaces ന്റെ ഉപയോഗത്തിൽ നിങ്ങളുടെ API കീകൾ സുരക്ഷിതമാക്കാൻ വേണ്ടത് Codespace Secrets ആണ്. ഇതിനെക്കുറിച്ച് കൂടുതൽ അറിയാൻ, [Codespaces സീക്രറ്റ്സ് മാനേജ്മന്റ്](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) ഗൈഡ് പിന്തുടരുക.


## പാഠങ്ങളും സാങ്കേതിക ആവശ്യകതകളും

കോഴ്സ് ഉൾക്കൊള്ളുന്ന 6 ആശയ പാഠങ്ങളും 6 കോഡിങ്ങ് പാഠങ്ങളും ഉണ്ട്.

കോഡിങ്ങ് പാഠങ്ങൾക്കായി ഞങ്ങൾ Azure OpenAI സർവീസ് ഉപയോഗിക്കുന്നു. ഈ കോഡ് ഓടിക്കാൻ Azure OpenAI സർവീസും API കീയും ഉപയോഗിക്കേണ്ടതാണ്. ആക്‌സസ് നേടാൻ [ഈ അപേക്ഷ അയയ്ക്കാം](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

നിങ്ങളുടെ അപേക്ഷ പരിശോധിക്കപ്പെടുമ്പോൾ, ഓരോ കോഡിങ്ങ് പാഠത്തിലും `README.md` ഫയൽ ഉൾപ്പെടുത്തിയിട്ടുണ്ട്, കോഡും ഔട്ട്‌പുട്ടും അവിടെ കാണാം.

## Azure OpenAI സർവീസ് ആദ്യമായ് ഉപയോഗിക്കുന്നത്

Azure OpenAI സർവീസ് ആദ്യമായി ഉപയോഗിക്കുമ്പോൾ, ദയവായി [Azure OpenAI Service റിസോഴ്‌സ് സൃഷ്ടിക്കുകയും വിന്യാസം ചെയ്യുകയും ചെയ്യാൻ](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) ഈ ഗൈഡ് പിന്തുടരുക.

## OpenAI API ആദ്യമായി ഉപയോഗിക്കുന്നത്

OpenAI API ആദ്യമായി ഉപയോഗിക്കുമ്പോൾ ദയവായി [ഇന്റർഫേസ് സൃഷ്ടിക്കുകയും ഉപയോഗിക്കുകയും](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) ചെയ്യാൻ ഗൈഡ് പിന്തുടരുക.

## മറ്റ് പഠിതാക്കളെ കാണുക

ഞങ്ങളുടേതായ [AI Community Discord സെർവർ](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) ൽ മറ്റുള്ള പഠിതാക്കളെ കാണാൻ ചാനലുകൾ സൃഷ്ടിച്ചിരിക്കുന്നു. ഇത് സാദൃശ്യമുള്ള സംരംഭകരോട്, നിർമ്മാതാക്കളോട്, വിദ്യാർത്ഥികളോടു കുടിയേറ്റം കണ്ടെത്താനും Generative AI-യിൽ മെച്ചപ്പെടാനും നല്ല ഒരു മാർഗമാണ്.

[![discord ചാനലിൽ ചേരുക](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

പ്രോജക്ട് ടീം ഈ Discord സെർവറിൽ ഉണ്ടാകും, പഠിതാക്കൾക്കായി സഹായം നൽകാൻ.

## സംഭാവന ചെയ്യുക

ഈ കോഴ്‌സ് ഒരു ഓപ്പൺ-സോഴ്‌സ് സംരംഭമാണ്. മെച്ചപ്പെടുത്തൽ സാധ്യതകൾ അല്ലെങ്കിൽ പ്രശ്നങ്ങൾ കണ്ടാൽ, ഒരു [പുൾ അഭ്യർത്ഥന](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) സൃഷ്ടിക്കുക അല്ലെങ്കിൽ [GitHub പ്രശ്നം ലോഗ് ചെയ്യുക](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

പ്രോജക്ട് ടീം എല്ലാ സംഭാവനകളും നിരീക്ഷിക്കും. ഓപ്പൺ സോഴ്‌സിൽ സംഭാവന ചെയ്യുന്നത് Generative AI-യിൽ നിങ്ങളുടെ കരിയർ നിർമ്മിക്കാൻ മനോഹരമായ മാർഗമാണ്.

ഏറെ സംഭാവനകൾക്ക് നിങ്ങളുടെ അവകാശങ്ങളും ഞങ്ങൾക്ക് നൽകുന്നതായി അടയാളപ്പെടുത്തി Contributor License Agreement (CLA) ലെക്കം ആവശ്യമാണ്. വിശദാംശങ്ങൾക്ക് [CLA, Contributor License Agreement വെബ്‌സൈറ്റ്](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) സന്ദർശിക്കുക.

പ്രധാനമായി: ഈ റിപോയിൽ ഉള്ള വാചകങ്ങൾ വിവർത്തനം ചെയ്യുമ്പോൾ, മെഷീൻ വിവർത്തനം ഉപയോഗിക്കല്ലേ. പരിഗണിക്കുന്ന ഭാഷകളിൽ മാത്രം പരിചയസമ്പന്നരായവർ വിവർത്തനം ചെയ്യാൻ മുൻതൂക്കം നൽകും.

ഒരു പുൾ അഭ്യർത്ഥന സമർപ്പിക്കുമ്പോൾ, CLA-ബോട്ട് നിങ്ങൾക്ക് CLA നൽകേണ്ടതുണ്ടോ എന്ന് സ്വയം നിർണയിച്ച് ആവശ്യാനുസരണം ലേബലുകൾ, കമന്റുകൾ നൽകും. ബോട്ടിന്റെ നിർദേശങ്ങൾ പാലിക്കുക. നിങ്ങൾക്ക് ഇത് ഒരിക്കൽ മാത്രം ആവശ്യമായിരിക്കും, പകരം വെല്ലിയുള്ള എല്ലാ റിപോസിറ്ററികളിലും.


ഈ പദ്ധതിയിൽ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) സ്വീകരിച്ചിരിക്കുകയാണ്. കൂടുതൽ വിവരങ്ങൾക്ക് Code of Conduct FAQ വായിക്കുക അല്ലെങ്കിൽ കൂടുതൽ ചോദ്യങ്ങളോ അഭിപ്രായങ്ങളോ ഉണ്ടെങ്കിൽ [Email opencode](opencode@microsoft.com) ന് ബന്ധപ്പെടുക.

## വരാം തുടങ്ങാം

ഈ കോഴ്സ് പൂർത്തിയാക്കുന്നതിനുള്ള ആവശ്യമായ നടപടിക്രമങ്ങൾ നിങ്ങൾ പൂർത്തിയാക്കിയതിനുശേഷം, Generative AI നും LLMs നും ഒരു [പരിചയം](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) നേടുന്നതിലൂടെ തുടങ്ങാം.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->