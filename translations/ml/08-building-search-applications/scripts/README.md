# ട്രാൻസ്ക്രിപ്ഷൻ ഡാറ്റ പ്രിപ്പ്

ട്രാൻസ്ക്രിപ്ഷൻ ഡാറ്റ പ്രിപ്പ് സ്ക്രിപ്റ്റുകൾ YouTube വീഡിയോ ട്രാൻസ്ക്രിപ്റ്റുകൾ ഡൗൺലോഡ് ചെയ്യുകയും OpenAI എംബെഡിംഗുകളും ഫംക്ഷനുകളും ഉപയോഗിക്കുന്ന സെമാന്റിക് സെർച്ചിനു വേണ്ടി തയ്യാറാക്കുകയും ചെയ്യുന്നു.

ട്രാൻസ്ക്രിപ്ഷൻ ഡാറ്റ പ്രിപ്പ് സ്ക്രിപ്റ്റുകൾ ഏറ്റവും പുതിയ റിലീസായ Windows 11, macOS Ventura, Ubuntu 22.04 (മാഫ്‌) എന്നിവയിൽ പരീക്ഷിക്കപ്പെട്ടിരിക്കുന്നു.

## ആവശ്യമായ Azure OpenAI Service വിഭവങ്ങൾ സൃഷ്ടിക്കൽ

> [!IMPORTANT]
> OpenAI-യുമായി പൊരുത്തപ്പെടുന്നതിനായി Azure CLI ഏറ്റവും പുതിയ പതിപ്പിലേക്ക് അപ്‌ഡേറ്റ് ചെയ്യാൻ നാം നിർദ്ദേശിക്കുന്നു
> [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) കാണുക

1. ഒരു റിസോർസ് ഗ്രൂപ്പ് സൃഷ്ടിക്കുക

> [!NOTE]
> ഈ നിർദ്ദേശങ്ങൾക്കായി നാം East US-ൽ നാമകരണം ചെയ്ത "semantic-video-search" റിസോഴ്സ് ഗ്രൂപ്പ് ഉപയോഗിക്കുന്നു.
> റിസോഴ്സുകളുടെ സ്ഥാനമാറ്റം വരുമ്പോൾ റിസോർസ് ഗ്രൂപ്പിന്റെ പേര് മാറ്റാം, പക്ഷേ 
> [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) പരിശോധിക്കുക.

```console
az group create --name semantic-video-search --location eastus
```

1. ഒരു Azure OpenAI Service വിഭവം സൃഷ്ടിക്കുക.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ഈ അപ്ലിക്കേഷനിൽ ഉപയോഗത്തിനായി എന്റ്പോയിന്റും കീകളും കൈപ്പറ്റുക

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. താഴെപ്പറയുന്ന മോഡലുകൾ വിന്യസിക്കുക:
   - `text-embedding-ada-002` പതിപ്പ് `2` അല്ലെങ്കിൽ അതിനുശേഷം, പേര് `text-embedding-ada-002`
   - `gpt-5-mini` പേര് `gpt-5-mini`

```console
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --scale-settings-scale-type "Standard"
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name gpt-5-mini \
    --model-name gpt-5-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## ആവശ്യമായ സോഫ്റ്റ്‌വെയർ

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) അല്ലെങ്കിൽ അതിനുശേഷം

## പരിസ്ഥിതി വ്യത്യസ്ഥങ്ങൾ

YouTube ട്രാൻസ്ക്രിപ്ഷൻ ഡാറ്റ പ്രിപ്പ് സ്ക്രിപ്റ്റുകൾ പ്രവർത്തിപ്പിക്കാൻ താഴെപ്പറയുന്ന പരിസ്ഥിതി വ്യത്യസ്ഥങ്ങൾ ആവശ്യമുണ്ട്.

### Windows-ൽ

`user` പരിസ്ഥിതി വ്യത്യസ്ഥങ്ങളെ നിങ്ങളുടെ സജസ്റ്റുചെയ്യുന്നു.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER] നുള്ള `User variables` > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- നിങ്ങൾ പരിസ്ഥിതി വ്യത്യസ്ഥങ്ങൾ നിങ്ങളുടെ PowerShell പ്രൊഫയലില്‍ ചേർക്കാം.

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### Linux-ഉം macOS-ഉം

നിങ്ങൾക്ക് ശുപാർശ ചെയ്യുന്നത് താഴെപ്പറയുന്ന എക്സ്പോർട്ടുകൾ നിങ്ങളുടെ `~/.bashrc` അല്ലെങ്കിൽ `~/.zshrc` ഫയലിൽ ചേർക്കുക എന്നതാണ്.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## ആവശ്യമായ Python ലൈബ്രറികൾ ഇൻസ്റ്റാൾ ചെയ്യുക

1. [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ഇന്സ്റ്റാൾ ചെയ്തിട്ടില്ലെങ്കിൽ ഇൻസ്റ്റാൾ ചെയ്യുക.
1. `Terminal` വിംഡോയിൽ നിന്നു് സാമ്പിൾ നിങ്ങളുടെ ഇഷ്ടപ്പെട്ട റെപ്പോ ഫോൾഡറിലേക്ക് ക്ലോൺ ചെയ്യുക.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` ഫോൾഡർ കാണുക.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. ഒരു Python വെർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിക്കുക.

    Windows-ൽ:

    ```powershell
    python -m venv .venv
    ```

    macOS-ഉം Linux-ഉം:

    ```bash
    python3 -m venv .venv
    ```

1. Python വെർച്വൽ എൻവയോൺമെന്റ് സജീവമാക്കുക.

   Windows-ൽ:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS-ഉം Linux-ഉം:

   ```bash
   source .venv/bin/activate
   ```

1. ആവശ്യമായ ലൈബ്രറികൾ ഇൻസ്റ്റാൾ ചെയ്യുക.

   Windows-ൽ:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS-ഉം Linux-ഉം:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ട്രാൻസ്ക്രിപ്ഷൻ ഡാറ്റ പ്രിപ്പ് സ്ക്രിപ്റ്റുകൾ പ്രവർത്തിപ്പിക്കുക

### Windows-ൽ

```powershell
.\transcripts_prepare.ps1
```

### macOS-ഉം Linux-ഉം

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->