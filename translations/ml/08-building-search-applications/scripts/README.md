# ട്രാൻസ്‌ക്രിപ്ഷൻ ഡാറ്റ തയ്യാറാക്കൽ

ട്രാൻസ്‌ക്രിപ്ഷൻ ഡാറ്റ തയ്യാറാക്കൽ സ്ക്രിപ്റ്റുകൾ YouTube വീഡിയോകളുടെ ട്രാൻസ്‌ക്രിപ്റ്റുകൾ ഡൗൺലോഡ് ചെയ്ത് Semantic Search with OpenAI Embeddings and Functions സാംപിളിനായി ഉപയോഗിക്കാൻ തയ്യാറാക്കുന്നു.

ട്രാൻസ്‌ക്രിപ്ഷൻ ഡാറ്റ തയ്യാറാക്കൽ സ്ക്രിപ്റ്റുകൾ അടുത്തിടെ പുറത്തിറങ്ങിയ Windows 11, macOS Ventura, Ubuntu 22.04 (മറ്റും മുകളിൽ) എന്നിവയിൽ പരീക്ഷിച്ചിട്ടുണ്ട്.

## ആവശ്യമായ Azure OpenAI സർവീസ് വിഭവങ്ങൾ സൃഷ്‌ടിക്കുക

> [!IMPORTANT]
> OpenAI-യുമായുള്ള അനുയോജ്യത ഉറപ്പാക്കാൻ നിങ്ങൾ Azure CLI ഏറ്റവും പുതിയ പതിപ്പിലേക്ക് അപ്ഡേറ്റ് ചെയ്യണമെന്ന് നാം നിർദ്ദേശിക്കുന്നു
> [ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) കാണുക

1. ഒരു റിസോഴ്‌സ് ഗ്രൂപ്പ് സൃഷ്‌ടിക്കുക

> [!NOTE]
> ഈ നിർദ്ദേശങ്ങൾക്കായി നാം "semantic-video-search" എന്ന പേരിലുള്ള റിസോഴ്‌സ് ഗ്രൂപ്പ് East US-യിൽ ഉപയോഗിക്കുന്നുണ്ട്.
> റിസോഴ്‌സുകളുടെ സ്ഥാനം മാറ്റുമ്പോഴെന്തെങ്കിലും, റിസോഴ്‌സ് ഗ്രൂപ്പിന്റെ പേര് നിങ്ങൾ മാറ്റാൻ കഴിയും,
> [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) പരിശോധിക്കുക.

```console
az group create --name semantic-video-search --location eastus
```

1. ഒരു Azure OpenAI സർവീസ് റിസോഴ്‌സ് സൃഷ്‌ടിക്കുക.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ഈ ആപ്ലിക്കേഷൻ ഉപയോഗിക്കുന്നതിന് എൻഡ്പോയിന്റും കീകളും നേടുക

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. താഴെപ്പറയുന്ന മോഡലുകൾ ഡിപ്ലോയ് ചെയ്യുക:
   - `text-embedding-ada-002` പതിപ്പ് `2` അല്ലെങ്കിൽ അതിൽ കൂടുതൽ, പേര് `text-embedding-ada-002`
   - `gpt-4o-mini` പേരുള്ളത് `gpt-4o-mini`

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
    --deployment-name gpt-4o-mini \
    --model-name gpt-4o-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## ആവശ്യമായ സോഫ്‌റ്റ്‌വെയർ

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) അല്ലെങ്കിൽ അതിൽ കൂടുതൽ

## പരിസ്ഥിതി വ്യത്യാസങ്ങൾ

YouTube ട്രാൻസ്‌ക്രിപ്ഷൻ ഡാറ്റ തയ്യാറാക്കൽ സ്ക്രിപ്റ്റുകൾ പ്രവർത്തിക്കാൻ താഴെ പറയുന്ന പരിസ്ഥിതി വ്യത്യാസങ്ങൾ ആവശ്യമാണ്.

### Windows-ൽ

ഈ വ്യത്യാസങ്ങൾ നിങ്ങളുടെ `user` പരിസ്ഥിതി വ്യത്യാസങ്ങളിൽ ചേർക്കാൻ ശുപാർശ ചെയ്‌യുന്നു.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER]ന്റെ `User variables` > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- നിങ്ങൾക്ക് ഈ പരിസ്ഥിതി വ്യത്യാസങ്ങൾ നിങ്ങളുടെ PowerShell പ്രൊഫൈലിൽ ചേർക്കാം.

```powershell
$env:AZURE_OPENAI_API_KEY = "<നിങ്ങളുടെ Azure OpenAI സർവീസ് API കീ>"
$env:AZURE_OPENAI_ENDPOINT = "<നിങ്ങളുടെ Azure OpenAI സർവീസ് എൻഡ്പോയിന്റ്>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<നിങ്ങളുടെ Azure OpenAI സർവീസ് മോഡൽ ഡിപ്ലോയ്മെന്റ് പേര്>"
$env:GOOGLE_DEVELOPER_API_KEY = "<നിങ്ങളുടെ Google ഡെവലപ്പർ API കീ>"
``` -->

### Linux, macOS-ൽ

ഈ‍റെ എക്സ്പോർട്ടുകൾ നിങ്ങളുടെ `~/.bashrc` അല്ലെങ്കിൽ `~/.zshrc` ഫയലിൽ ചേർക്കാൻ ശുപാർശ ചെയ്യുന്നു.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## ആവശ്യമായ Python ലൈബ്രററികൾ ഇൻസ്റ്റാൾ ചെയ്യുക

1. [Git ക്ലയന്റ്](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ഇൻസ്റ്റാൾ ചെയ്തിട്ടില്ലെങ്കിൽ അത് ഇൻസ്റ്റാൾ ചെയ്യുക.
1. ഒരു `Terminal` വിൻഡോയിൽ നിന്ന് സാംപിൾ നിങ്ങളുടെ ഇഷ്ടപ്പെട്ട റിപ്പോ ഫോൾഡറിലേക്ക് ക്ലോൺ ചെയ്യുക.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` ഫോൾഡറിലേക്ക് നാവിഗേറ്റ് ചെയ്യുക.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. ഒരു Python വെർച്ച്വൽ എൻവയോൺമെന്റ് സൃഷ്‌ടിക്കുക.

    Windows-ൽ:

    ```powershell
    python -m venv .venv
    ```

    macOS, Linux-ൽ:

    ```bash
    python3 -m venv .venv
    ```

1. Python വെർച്ച്വൽ എൻവയോൺമെന്റ് ആക്ടിവേറ്റ് ചെയ്യുക.

   Windows-ൽ:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS, Linux-ൽ:

   ```bash
   source .venv/bin/activate
   ```

1. ആവശ്യമായ ലൈബ്രററികൾ ഇൻസ്റ്റാൾ ചെയ്യുക.

   Windows-ൽ:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS, Linux-ൽ:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ട്രാൻസ്‌ക്രിപ്ഷൻ ഡാറ്റ തയ്യാറാക്കൽ സ്ക്രിപ്റ്റുകൾ chạy

### Windows-ൽ

```powershell
.\transcripts_prepare.ps1
```

### macOS, Linux-ൽ

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->