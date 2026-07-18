# ഈ കോഴ്സ് തുടങ്ങുന്നത്

നിങ്ങൾ ഈ കോഴ്സ് ആരംഭിച്ച് ജനററ്റീവ് AI-യോട് എന്തുചേർത്ത് നിർമ്മിക്കാനുള്ള പ്രചോദനം നേടും എന്നതിന് ഞങ്ങൾ വളരെ ആഹ്ലാദത്തിലാണ്!

നിങ്ങളുടെ വിജയത്തിനായി, ഈ പേജ് സെറ്റപ്പ് ഘട്ടങ്ങൾ, സാങ്കേതിക ആവശ്യങ്ങൾ, ദുരിതസമയങ്ങളിൽ സഹായം എവിടെ ലഭിക്കും എന്നതിൽ വിശദീകരിക്കുന്നു.

## സെറ്റപ്പ് ഘട്ടങ്ങൾ

ഈ കോഴ്സ് തുടങ്ങാനായി, താഴെയുള്ള ഘട്ടങ്ങൾ പൂർത്തിയാക്കേണ്ടതാണ്.

### 1. ഈ റിപ്പൊ ഫോർക്ക് ചെയ്യുക

[ഈ മുഴുവൻ റിപ്പൊ ഫോർക്ക് ചെയ്യുക](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) നിങ്ങളുടെ സ്വന്തം GitHub അക്കൗണ്ടിലേക്ക്, കോഡ് മാറ്റാനും ചാലഞ്ചുകൾ പൂർത്തിയാക്കാനും. കൂടാതെ നിങ്ങള്ക്ക് [ഈ റിപ്പൊക്ക് സ്റ്റാർ (🌟) ചെയ്യാം](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ഇത് കണ്ടെത്താനും ബന്ധപ്പെട്ട റിപ്പൊസ് എളുപ്പത്തിൽ കാണാനും.

### 2. കോഡ്സ്പേസ് സൃഷ്ടിക്കുക

കോഡ് ഓടിക്കുമ്പോൾ ആശ്രിത പ്രശ്നങ്ങൾ ഒഴിവാക്കാൻ, ഈ കോഴ്സ് [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) ഉപയോഗിച്ച് നടത്താൻ ഞങ്ങൾ ശുപാർശ ചെയ്യുന്നു.

നിങ്ങളുടെ ഫോർക്കിൽ: **Code -> Codespaces -> New on main**

![കോഡ്സ്പേസ് സൃഷ്ടിക്കാൻ ബട്ടണുകൾ കാണിക്കുന്ന ഡയലോഗ്](../../../translated_images/ml/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 ഒരു രഹസ്യം ചേർക്കുക

1. ⚙️ ഗിയർ ഐകൺ -> കമാൻഡ് പാലറ്റ് -> Codespaces : Manage user secret -> Add a new secret.
2. OPENAI_API_KEY എന്നു പേരിടുക, നിങ്ങളുടെ കീ പസ്റ്റ് ചെയ്ത്, Save ചെയ്യുക.

### 3. അടുത്തത് എന്ത് ചെയ്യാം?

| ഞാൻ എന്ത് ചെയ്യണമെന്ന് ആഗ്രഹിക്കുന്നു... | ഈ ഭാഗത്ത് പോവുക...                                            |
|---------------------|-------------------------------------------------------------------------|
| പാഠം 1 തുടങ്ങിയാൽ      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ഓഫ്‌ലൈൻ ജോലി        | [`setup-local.md`](02-setup-local.md)                                   |
| LLM പ്രൊവൈഡർ സജ്ജീകരിക്കുക | [`providers.md`](03-providers.md)                                        |
| മറ്റു പഠിച്ചവരുമായി കൂടുക | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## പ്രശ്നപരിഹാര മാർഗങ്ങൾ


| ലക്ഷണം                                  | പരിഹാരം                                                       |
|-------------------------------------------|-----------------------------------------------------------------|
| കണ്ടെയ്‌നർ നിർമ്മാണം 10 മിനിറ്റ് കഴിഞ്ഞും സ്തംഭിച്ചു | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | ടെർമിനൽ ചേരാത്തത്; **+** ക്ലിക്കുചെയ്യുക ➜ *bash*               |
| OpenAI-ൽ നിന്നുള്ള `401 Unauthorized`    | തെറ്റായ / കാലഹരണപ്പെട്ട `OPENAI_API_KEY`                        |
| VS Code “Dev container mounting…” കാണിക്കുന്നു | ബ്രൗസർ ടാബ് റിഫ്രഷ് ചെയ്യുക—Codespaces ക sometimes വഴിയേ ബന്ധം നഷ്ടപ്പെടുത്തുന്നു  |
| നോട്ട്‌ബുക്ക് കർണൽ കാണുന്നില്ല         | നോട്ട്‌ബുക്ക് മേനു ➜ **Kernel ▸ Select Kernel ▸ Python 3**         |

   Unix അടിസ്ഥാനമാക്കിയുള്ള സിസ്റ്റങ്ങൾ:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` ഫയൽ എഡിറ്റ് ചെയ്യുക**: `.env` ഫയൽ ഒരു ടെക്സ്റ്റ് എഡിറ്ററിൽ (ഉദാ: VS Code, Notepad++, അല്ലെങ്കിൽ മറ്റേതെങ്കിലും എഡിറ്റർ) തുറന്ന്, താഴെ കാണുന്നതുപോലെ നിങ്ങളുടെ Microsoft Foundry Models എന്റ്പോയിന്റും കീയും ഉൾപ്പെടുത്തുക (എങ്ങനെ ലഭിക്കാം ഇത്തരം വിശദാംശങ്ങൾക്ക് [`providers.md`](03-providers.md) കാണുക):

   > **കുറിപ്പ്:** GitHub മോഡലുകൾ (അവയുടെ `GITHUB_TOKEN` വേരിയബിൾ കൂടി) ജൂലൈ 2026 അവസാനം റിടയറിങ്ങ് ചെയ്യും. അതിന്റെ പകരം [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ഉപയോഗിക്കുക.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **ഫയൽ സേവ് ചെയ്യുക**: മാറ്റങ്ങൾ സേവ് ചെയ്ത് ടെക്സ്റ്റ് എഡിറ്റർ അടയ്ക്കുക.

5. **`python-dotenv` ഇൻസ്റ്റാൾ ചെയ്യുക**: നിങ്ങൾ ഇതിനകം ഇൻസ്റ്റാൾ ചെയ്തിട്ടില്ലെങ്കിൽ, Python ആപ്ലിക്കേഷനിലേക്ക് `.env` ഫയൽ നിന്നുള്ള പരിസര വ്യത്യാസങ്ങൾ (environment variables) ലോഡ് ചെയ്യാൻ `python-dotenv` പാക്കേജ് ഇൻസ്റ്റാൾ ചെയ്യേണ്ടതാണ്. അതിനായി `pip` ഉപയോഗിക്കാം:

   ```bash
   pip install python-dotenv
   ```

6. **Python സ്ക്രിപ്റ്റിൽ പരിസര വ്യത്യാസങ്ങൾ ലോഡ് ചെയ്യുക**: Python സ്ക്രിപ്റ്റിൽ `python-dotenv` പാക്കേജ് ഉപയോഗിച്ച് `.env` ഫയൽ നിന്നുള്ള പരിസര വ്യത്യാസങ്ങൾ ലോഡ് ചെയ്യുക:

   ```python
   from dotenv import load_dotenv
   import os

   # .env ഫയലിൽ നിന്നുള്ള പരിസ്ഥിതി ചാരങ്ങൾ ലോഡ് ചെയ്യുക
   load_dotenv()

   # Microsoft Foundry Models ചാരങ്ങൾ ആക്സസ് ചെയ്യുക
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

എല്ലാം പൂർത്തിയായി! നിങ്ങൾ വിജയകരമായി `.env` ഫയൽ സൃഷ്ടിച്ച്, Microsoft Foundry Models ക്രെഡൻഷ്യലുകൾ ചേർത്ത്, Python ആപ്ലിക്കേഷനിലേക്ക് ലോഡ് ചെയ്തു.

## നിങ്ങളുടെ കമ്പ്യൂട്ടറിൽ ലൊക്കലി കോഡ് നടത്തുന്നത് എങ്ങനെ

കോഡ് നിങ്ങളുടെ കമ്പ്യൂട്ടറിൽ ലൊക്കലി ഓടിക്കാൻ, നിങ്ങൾക്കു [Python-ന്റെ ഒരു പതിപ്പ് ഇൻസ്റ്റാൾ ചെയ്ത](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)ിരിക്കേണ്ടതാണ്.

അപ്പോൾ റിപ്പൊ ക്ലോൺ ചെയ്യേണ്ടതാണ്:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

എല്ലാം ചെക്ക് ഔട്ട് ചെയ്തശേഷം, നിങ്ങൾ തുടങ്ങാം!

## ഐച്ഛിക ഘട്ടങ്ങൾ

### മിനികോണ്ട ഇൻസ്റ്റാൾ ചെയ്യൽ

[മിനികോണ്ട](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ലഘുവായ ഒരു ഇൻസ്റ്റോളർ ആണ് [കോണ്ട](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, കൂടാതെ ചില പാക്കേജുകൾ ഇൻസ്റ്റാൾ ചെയ്യാൻ ഉപകരിക്കും.
കോണ്ട തന്നെ ഒരു പാക്കേജ് മാനേജറാണ്, വ്യത്യസ്ത Python [**വെർച്ച്വൽ എൻവയോൺമെന്റുകളും**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) പാക്കേജുകളും എളുപ്പത്തിൽ സജ്ജീകരിക്കുകയും മാറുകയും ചെയ്യാൻ സഹായിക്കുന്നു. കൂടാതെ `pip` വഴി ലഭ്യമല്ലാത്ത പാക്കേജുകൾ ഇൻസ്റ്റാൾ ചെയ്യാനുമായി ഇത് ഏറെ ഉപകരിക്കും.

[MiniConda ഇൻസ്റ്റലേഷൻ ഗൈഡ്](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) പിന്തുടർന്ന് സജ്ജീകരണം നടത്താം.

മിനികോണ്ട ഇൻസ്റ്റാൾ ചെയ്തശേഷം, നിങ്ങൾക്ക് റിപ്പൊ ക്ലോൺ ചെയ്യേണ്ടതാണ് (ഇതിനകം ചെയ്തിട്ടില്ലെങ്കിൽ)

തുടർന്ന് ഒരു വെർച്ച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിക്കേണ്ടതാണ്. കോണ്ട ഉപയോഗിച്ച് അത് ചെയ്യാൻ, ഒരു പുതിയ എൻവയോൺമെന്റ് ഫയൽ (_environment.yml_) സൃഷ്ടിക്കുക. നിങ്ങൾ Codespaces ഉപയോഗിക്കുന്നുണ്ടെങ്കിൽ, ഇത് `.devcontainer` ഡയറക്ടറിയിൽ സൃഷ്ടിക്കുക, അതായത് `.devcontainer/environment.yml`.

താഴെ കൊടുത്തിരിക്കുന്ന സ്നിപ്പെറ്റ് ഉപയോഗിച്ച് നിങ്ങളുടെ എൻവയോൺമെന്റ് ഫയൽ പൂരിപ്പിക്കുക:

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

നിങ്ങൾക്ക് കോണ്ട ഉപയോഗിക്കുമ്പോളുണ്ടാകുന്ന പിശകുകൾ നിങ്ങൾ കണ്ടെത്തിയാൽ താഴെയുള്ള കമാൻഡ് ഉപയോഗിച്ച് മൈക്രോസോഫ്റ്റ് AI ലൈബ്രറികൾ മാൻവലായി ഇൻസ്റ്റാൾ ചെയ്യാം.

```
conda install -c microsoft azure-ai-ml
```

എൻവയോൺമെന്റ് ഫയൽ ഞങ്ങൾക്കു വേണ്ട ആശ്രിതങ്ങൾ വിശദീകരിക്കുന്നു. `<environment-name>` എന്നത് നിങ്ങളുടെ കോണ്ട എൻവയോൺമെന്റിനായി നിങ്ങൾക്ക് തരാനിഷ്ടമുള്ള പേര് ആണ്, `<python-version>` അതിന്റെ Python പതിപ്പ്. ഉദാഹരണത്തിന്, `3` ഏറ്റവും പുതിയ പ്രധാന Python പതിപ്പാണ്.

ഇത് പൂർത്തിയാക്കിയ ശേഷം, താഴെയുള്ള കമാൻഡുകൾ നിങ്ങളുടെ കമാൻഡ് ലൈൻ/റ്റർമിനലിൽ ഓടിച്ച് കോണ്ട എൻവയോൺമെന്റ് സൃഷ്ടിക്കാം

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer സബ് പാത്ത് കോഡ്സ്പേസ് സെറ്റപ്പുകൾക്ക് മാത്രമേ ബാധകമായുള്ളൂ
conda activate ai4beg
```

പ്രശ്നങ്ങൾ ഉണ്ടെങ്കിൽ [Conda എൻവയോൺമെന്റ് ഗൈഡ്](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) കാണുക.

### Python സപ്പോർട്ട് എക്സ്റ്റെൻഷനോടെയുള്ള Visual Studio Code ഉപയോഗിക്കൽ

ഈ കോഴ്സിന് [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) എഡിറ്ററിനും [Python സപ്പോർട്ട് എക്സ്റ്റെൻഷൻ](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ഇൻസ്റ്റാൾ ചെയ്തിരിക്കാനാണ് ഞങ്ങൾ ശുപാർശ ചെയ്യുന്നത്. ഇതു ശുപാർശ മാത്രമാണ്, നിർബന്ധമല്ല.

> **കുറിപ്പ്**: കോഴ്സ് റിപ്പൊ VS Code-യിൽ തുറന്നാൽ, പ്രോജക്റ്റ് ഒരു കണ്ടെയ്‌നറിനുള്ളിൽ സജ്ജമാക്കാനുള്ള ഓപ്‌ഷൻ ലഭിക്കും. ഇത് കോഴ്സ് റിപ്പൊയിലെ [പ്രത്യേക `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ഡയറക്ടറിയുള്ളതിനാൽ ആണ്. വിശദാംശങ്ങൾ പിന്നീട്.

> **കുറിപ്പ്**: റിപ്പൊ ക്ലോൺ ചെയ്ത് VS Code-യിൽ തുറന്നാൽ, Python സപ്പോർട്ട് എക്സ്റ്റെൻഷൻ ഇൻസ്റ്റാൾ ചെയ്യാൻ സ്വയം നിർദേശിക്കും.

> **കുറിപ്പ്**: VS Code റിപ്പൊ കണ്ടെയ്‌നറിൽ തുറക്കണമെന്ന് നിർദേശിക്കുമ്പോൾ അത് നിഷേധിക്കുക, നിങ്ങളുടെ കമ്പ്യൂട്ടറിലെ Python പതിപ്പ് ഉപയോഗിക്കാൻ.

### ബ്രൗസറിൽ Jupyter ഉപയോഗിക്കൽ

നിങ്ങളുക്ക് ബ്രൗസറിനുള്ളിൽനിന്ന് തന്നെ [Jupyter പരിസരത്ത്](https://jupyter.org?WT.mc_id=academic-105485-koreyst) പ്രോജക്റ്റിൽ പ്രവർത്തിക്കാം. ക്ലാസിക് Jupyter ഉം [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ഉം ഓട്ടോ-കമ്പ്ലീഷൻ, കോഡ് ഹൈലൈറ്റിംഗ് തുടങ്ങിയ സവിശേഷതകളോടെ മികച്ച പ്രവർത്തനപരിസരം നൽകുന്നു.

Jupyter ലൊക്കലി സ്റ്റാർട്ട് ചെയ്യാനായി, ടെർമിനൽ/കമാൻഡ് ലൈൻ തുറന്ന്, കോഴ്സ് ഡയറക്ടറിയിലേക്ക് പോയി, താഴെ കൊടുത്തത് നടപ്പിലാക്കുക:

```bash
jupyter notebook
```

അല്ലെങ്കിൽ

```bash
jupyterhub
```

ഇത് Jupyter സെഷൻ ആരംഭിക്കും, അതിന്റെ URL കമാൻഡ് ലൈൻ വിൻഡോയിലിൽ കാണിക്കും.

URL ആക്സസ് ചെയ്താൽ, നിങ്ങൾക്ക് കോഴ്സ് ഔട്ട്‌ലൈൻ കാണാനാകും കൂടാതെ ഏതെങ്കിലും `*.ipynb` ഫയലിലേക്ക് പോകാം. ഉദാ: `08-building-search-applications/python/oai-solution.ipynb`.

### കണ്ടെയ്നറിൽ പ്രവർത്തിക്കുക

നിങ്ങളുടെ കമ്പ്യൂട്ടറിൽ അല്ലെങ്കിൽ Codespaces-ൽ എല്ലാം സജ്ജമാക്കുന്നതിന് പകരം, [കണ്ടെയ്നർ](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) ഉപയോഗിക്കാം. കോഴ്സ് റിപ്പൊയിലെ പ്രത്യേക `.devcontainer` ഫോൾഡർ ഉപയോഗിച്ച് VS Code പ്രോജക്റ്റ് കാണെയ്‌നറിൽ സജ്ജീകരിക്കാൻ കഴിയും. Codespaces ഒഴികെയുള്ള സാഹചര്യങ്ങളിൽ Docker ഇൻസ്റ്റാൾ ചെയ്യണം, ഇത് കുറച്ച ദൈർഘ്യമേറിയതും സങ്കീർണമായതുമായ പ്രവൃത്തി ആയതിനാൽ കണ്ടെയ്നറുകൾ ഉപയോഗിച്ച അനുഭവമുള്ളവർക്ക് മാത്രമെ ഇത് ശുപാർശ ചെയ്യൂ.

GitHub Codespaces ഉപയോഗിക്കുമ്പോൾ നിങ്ങളുടെ API കീകൾ സുരക്ഷിതമായി സൂക്ഷിക്കാനുള്ള ഏറ്റവും നല്ല മാർഗങ്ങളിൽ ഒന്നാണ് Codespace Secrets ഉപയോഗിക്കുക. ഇതിനായി [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) ഗൈഡ് പിന്തുടരുക.


## പാഠങ്ങളും സാങ്കേതിക ആവശ്യങ്ങളും

കോഴ്സിൽ "Learn" പാഠങ്ങൾ ജനറേറ്റീവ് AI ആശയങ്ങൾ വിശദീകരിക്കുന്നു, കൂടാതെ "Build" പാഠങ്ങളിൽ **Python**-ഉം **TypeScript**-ഉം ഉപയോഗിച്ച് হাতেകഴിവുള്ള കോഡ് ഉദാഹരണങ്ങൾ നൽകുന്നു.

കോഡിംഗ് പാഠങ്ങൾക്കായി, ഞങ്ങൾ Microsoft Foundry-യിൽ Azure OpenAI ഉപയോഗിക്കുന്നു. ഇതിന് Azure സബ്സ്ക്രിപ്ഷനും API കീയും ആവശ്യമാണ്. ആക്സസ് തുറന്നതാണ് - അപേക്ഷ വേണമെന്നില്ല - അതിനാൽ [Microsoft Foundry resource സൃഷ്ടിച്ച് മോഡൽ ഡെപ്ലോയ് ചെയ്യാൻ](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) കഴിയും.

ഓരോ കോഡിംഗ് പാഠത്തിനും ഒരു `README.md` ഫയൽ ഉണ്ട്, അതിൽ കോഡ് ഓടിക്കാതെ തന്നെ കോഡ് ഉത്‌പാദനങ്ങൾ കാണാനാകും.

## Azure OpenAI സേവനം ആദ്യമായി ഉപയോഗിക്കുന്നത്

Azure OpenAI സേവനം ആദ്യം ഉപയോഗിക്കുന്നവർക്ക്, [Azure OpenAI Service resource സൃഷ്ടിച്ച് ഡെപ്ലോയ് ചെയ്യുന്നതിന്റെ](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) ഗൈഡ് പാലിക്കേണ്ടതാണ്.

## OpenAI API ആദ്യമായി ഉപയോഗിക്കുന്നത്

OpenAI API ആദ്യം ഉപയോഗിക്കുന്നവർക്ക്, [ഇന്റർഫേസ് സൃഷ്ടിച്ച് ഉപയോഗിക്കാൻ](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) ഗൈഡ് പിന്തുടരുക.

## മറ്റു learners-നെ കാണുക

നമ്മുടെ ഔദ്യോഗിക [AI Community Discord സെർവറിൽ](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) മറ്റ് learners-നെ കാണാനുള്ള ചാനലുകൾ സൃഷ്ടിച്ചിട്ടുണ്ട്. ഇവിടെ നിങ്ങൾക്ക് സമാനമനസ്സുള്ള സംരംഭകർ, നിർമ്മാതാക്കൾ, വിദ്യാർത്ഥികൾ എന്നിവരുമായി ബന്ധപ്പെടാനും ജനറേറ്റീവ് AI-യിൽ മുന്നേറാനും സഹായകമാണ്.

[![discord ചാനൽയിൽ ചേരുക](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

പദ്ധതിദലവും learners-നെ സഹായിക്കാൻ ഈ Discord സെർവറിൽ ഉണ്ടാകും.

## സംഭാവന ചെയ്യുക

ഈ കോഴ്സ് ഒരു ഓപ്പൺ-സോഴ്‌സ് സംരംഭമാണ്. മെച്ചപ്പെടുത്തലുകൾ അല്ലെങ്കിൽ പ്രശ്നങ്ങൾ കണ്ടെത്തിയാൽ, ദയവായി ഒരു [പുൾ റിക്വസ്റ്റ്](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) സമർപ്പിക്കുകയോ [GitHub Issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) രജിസ്റ്റർ ചെയ്യുകയോ ചെയ്യുക.

പദ്ധതിദലം എല്ലാ സംഭാവനകളും നിരീക്ഷിക്കും. ഓപ്പൺ-സോഴ്‌സിലേക്ക് സംഭാവനം ജനറേറ്റീവ് AIയിൽ നിങ്ങളുടെ കരിയർ നിർമ്മിക്കാനുള്ള ഏറ്റവും മികച്ച മാർഗമായിരിക്കും.

ഭൂരിഭാഗം സംഭാവനകൾക്കായി നിങ്ങൾ ഒരു Contributor License Agreement (CLA) സമ്മതിക്കണം, ആയത് നിങ്ങൾക്ക് സംഭാവന ഉപയോഗപ്പെടുത്താനുള്ള അവകാശം ഉണ്ടെന്നും അതോടൊപ്പം നമ്മൾക്ക് ഉപയോഗിക്കാനും അവകാശം ‌കിൽപ്പിൻ ഇവിടെ തരും എന്നതും ഉറപ്പാക്കും. വിശദാംശങ്ങൾക്ക് [CLA, Contributor License Agreement വെബ്സൈറ്റ്](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) സന്ദർശിക്കുക.

പ്രധാനപ്പെട്ടതെന്തായാൽ: ഈ റിപ്പോയിലെ പരിവർത്തനങ്ങൾക്ക് യന്ത്ര പരിഭാഷ ഉപയോഗിക്കരുത്. നാം സമുദായത്തിലൂടെ വിവർത്തനങ്ങൾ പരിശോധിക്കും, അതിനാൽ നിങ്ങൾ നന്നായി അറിയുന്ന ഭാഷകളിൽ മാത്രമേ വിവർത്തനങ്ങൾക്കായി സഹായം നൽകുക.


നിങ്ങൾ ഒരു പുള്‍ റിക്വസ്റ്റ് സമര്‍പ്പിക്കുമ്പോൾ, CLA-ബോട്ട് സ്വയമേവ നിങ്ങൾക്ക് CLA നൽകേണ്ടതുണ്ടോ എന്ന് നിർണയിക്കും, പിന്നെ PR യ 적절മായി അലങ്കരിക്കും (ഉദാ., ലേബൽ, കമന്റ്). ബോട്ട് നൽകുന്ന നിർദ്ദേശങ്ങൾ പാലിക്കുക. ഞങ്ങളുടെ CLA ഉപയോഗിക്കുന്ന എല്ലാ റിപോസിറ്ററികളിലും നിങ്ങൾക്ക് ഇത് ഒരിക്കല്‍ മാത്രമേ ചെയ്യേണ്ടവയുള്ളൂ.

ഈ പ്രോജക്ട് [Microsoft ഓപ്പൺ സോഴ്‌സ് കോഡ് ഓഫ് കണ്ടക്റ്റ്](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) അപ്പൂർവ്വികരിച്ചിരിക്കുന്നു. കൂടുതൽ വിവരങ്ങൾക്ക്, കോഡ് ഓഫ് കണ്ടക്റ്റ് FAQ വായിക്കുക അല്ലെങ്കിൽ ഏത് അധിക ചോദ്യങ്ങൾക്കോ അഭിപ്രായങ്ങൾക്കോ [Email opencode](opencode@microsoft.com) ബന്ധപ്പെടുക.

## തുടങ്ങാം

ഈ കോഴ്‌സ് പൂർത്തിയാക്കാൻ ആവശ്യമായ ഘട്ടങ്ങൾ നിങ്ങൾ പൂർത്തിയാക്കിയതിനാൽ, [ജനറേറ്റീവ് AI-ക്കും LLM-കൾക്കും പൂർവവതരണമായി](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) ആരംഭിക്കാം.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->