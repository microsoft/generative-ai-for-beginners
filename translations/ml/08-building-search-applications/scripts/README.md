<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-12-19T20:45:21+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "ml"
}
-->
# ട്രാൻസ്ക്രിപ്ഷൻ ഡാറ്റ പ്രിപ്പ്

ട്രാൻസ്ക്രിപ്ഷൻ ഡാറ്റ പ്രിപ്പ് സ്ക്രിപ്റ്റുകൾ YouTube വീഡിയോ ട്രാൻസ്ക്രിപ്റ്റുകൾ ഡൗൺലോഡ് ചെയ്ത് Semantic Search with OpenAI Embeddings and Functions സാമ്പിളിനായി ഉപയോഗിക്കാൻ തയ്യാറാക്കുന്നു.

ട്രാൻസ്ക്രിപ്ഷൻ ഡാറ്റ പ്രിപ്പ് സ്ക്രിപ്റ്റുകൾ ഏറ്റവും പുതിയ റിലീസുകൾ ആയ Windows 11, macOS Ventura, Ubuntu 22.04 (മറ്റും മുകളിൽ) എന്നിവയിൽ പരീക്ഷിച്ചിട്ടുണ്ട്.

## ആവശ്യമായ Azure OpenAI സർവീസ് റിസോഴ്‌സുകൾ സൃഷ്ടിക്കുക

> [!IMPORTANT]
> OpenAI-യുമായി പൊരുത്തപ്പെടുന്നതിനായി Azure CLI ഏറ്റവും പുതിയ പതിപ്പിലേക്ക് അപ്ഡേറ്റ് ചെയ്യാൻ ഞങ്ങൾ നിർദ്ദേശിക്കുന്നു
> [ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) കാണുക

1. ഒരു റിസോഴ്‌സ് ഗ്രൂപ്പ് സൃഷ്ടിക്കുക

> [!NOTE]
> ഈ നിർദ്ദേശങ്ങൾക്ക് ഞങ്ങൾ East US-ൽ "semantic-video-search" എന്ന പേരിലുള്ള റിസോഴ്‌സ് ഗ്രൂപ്പ് ഉപയോഗിക്കുന്നു.
> റിസോഴ്‌സ് ഗ്രൂപ്പിന്റെ പേര് മാറ്റാം, പക്ഷേ റിസോഴ്‌സുകളുടെ സ്ഥലം മാറ്റുമ്പോൾ,
> [മോഡൽ ലഭ്യത പട്ടിക](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) പരിശോധിക്കുക.

```console
az group create --name semantic-video-search --location eastus
```

1. ഒരു Azure OpenAI സർവീസ് റിസോഴ്‌സ് സൃഷ്ടിക്കുക.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ഈ അപ്ലിക്കേഷനിൽ ഉപയോഗിക്കാൻ എൻഡ്‌പോയിന്റും കീകളും നേടുക

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. താഴെപ്പറയുന്ന മോഡലുകൾ ഡിപ്ലോയ് ചെയ്യുക:
   - `text-embedding-ada-002` പതിപ്പ് `2` അല്ലെങ്കിൽ അതിൽ മുകളിൽ, പേര് `text-embedding-ada-002`
   - `gpt-35-turbo` പതിപ്പ് `0613` അല്ലെങ്കിൽ അതിൽ മുകളിൽ, പേര് `gpt-35-turbo`

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
    --deployment-name gpt-35-turbo \
    --model-name gpt-35-turbo \
    --model-version "0613"  \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## ആവശ്യമായ സോഫ്റ്റ്‌വെയർ

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) അല്ലെങ്കിൽ അതിൽ മുകളിൽ

## പരിസ്ഥിതി വ്യത്യാസങ്ങൾ

YouTube ട്രാൻസ്ക്രിപ്ഷൻ ഡാറ്റ പ്രിപ്പ് സ്ക്രിപ്റ്റുകൾ പ്രവർത്തിപ്പിക്കാൻ താഴെപ്പറയുന്ന പരിസ്ഥിതി വ്യത്യാസങ്ങൾ ആവശ്യമാണ്.

### Windows-ൽ

നിങ്ങളുടെ `user` പരിസ്ഥിതി വ്യത്യാസങ്ങളിൽ ഈ വ്യത്യാസങ്ങൾ ചേർക്കാൻ ശുപാർശ ചെയ്യുന്നു.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER] ന്റെ `User variables` > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- നിങ്ങൾക്ക് ഈ പരിസ്ഥിതി വ്യത്യാസങ്ങൾ നിങ്ങളുടെ PowerShell പ്രൊഫൈലിൽ ചേർക്കാം.

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### Linux, macOS-ൽ

താഴെപ്പറയുന്ന എക്സ്പോർട്ടുകൾ നിങ്ങളുടെ `~/.bashrc` അല്ലെങ്കിൽ `~/.zshrc` ഫയലിൽ ചേർക്കാൻ ശുപാർശ ചെയ്യുന്നു.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## ആവശ്യമായ Python ലൈബ്രറികൾ ഇൻസ്റ്റാൾ ചെയ്യുക

1. [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ഇൻസ്റ്റാൾ ചെയ്തിട്ടില്ലെങ്കിൽ ഇൻസ്റ്റാൾ ചെയ്യുക.
1. ഒരു `Terminal` വിൻഡോയിൽ നിന്ന്, സാമ്പിൾ നിങ്ങളുടെ ഇഷ്ടപ്പെട്ട റിപോ ഫോൾഡറിൽ ക്ലോൺ ചെയ്യുക.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` ഫോൾഡറിലേക്ക് നാവിഗേറ്റ് ചെയ്യുക.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. ഒരു Python വെർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിക്കുക.

    Windows-ൽ:

    ```powershell
    python -m venv .venv
    ```

    macOS, Linux-ൽ:

    ```bash
    python3 -m venv .venv
    ```

1. Python വെർച്വൽ എൻവയോൺമെന്റ് ആക്ടിവേറ്റ് ചെയ്യുക.

   Windows-ൽ:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS, Linux-ൽ:

   ```bash
   source .venv/bin/activate
   ```

1. ആവശ്യമായ ലൈബ്രറികൾ ഇൻസ്റ്റാൾ ചെയ്യുക.

   Windows-ൽ:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS, Linux-ൽ:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ട്രാൻസ്ക്രിപ്ഷൻ ഡാറ്റ പ്രിപ്പ് സ്ക്രിപ്റ്റുകൾ പ്രവർത്തിപ്പിക്കുക

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
**അസൂയാപത്രം**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, യന്ത്രം ചെയ്ത വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->