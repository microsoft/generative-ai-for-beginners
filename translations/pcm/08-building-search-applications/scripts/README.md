# How to prepare transcription data

Dis script wey go help prepare transcription data go download YouTube video transcript and arrange am make e fit work well with Semantic Search wey dey use OpenAI Embeddings and Functions sample.

Dem don test dis transcription data prep script for di latest Windows 11, macOS Ventura and Ubuntu 22.04 (and above).

## How to create di Azure OpenAI Service resources wey you need

> [!IMPORTANT]
> We dey advise say make you update di Azure CLI to di latest version so e go fit work well with OpenAI.
> Check [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Create resource group

> [!NOTE]
> For dis instruction, we dey use resource group wey dem name "semantic-video-search" for East US.
> You fit change di name of di resource group, but if you wan change di location for di resources, 
> make sure say you check di [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Create Azure OpenAI Service resource.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Collect di endpoint and keys wey you go use for dis application.

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Deploy di models wey dey below:
   - `text-embedding-ada-002` version `2` or higher, wey dem name `text-embedding-ada-002`
   - `gpt-35-turbo` version `0613` or higher, wey dem name `gpt-35-turbo`

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

## Software wey you need

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) or higher

## Environment variables

Di environment variables wey dey below na wetin you need to run di YouTube transcription data prep scripts.

### For Windows

E good make you add di variables to your `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- You fit add di environment variables to your PowerShell profile.

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### For Linux and macOS

E good make you add di exports wey dey below to your `~/.bashrc` or `~/.zshrc` file.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## How to install di Python libraries wey you need

1. Install [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) if e never dey your system.
1. For `Terminal` window, clone di sample go di repo folder wey you like.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Enter di `data_prep` folder.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Create Python virtual environment.

    For Windows:

    ```powershell
    python -m venv .venv
    ```

    For macOS and Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Activate di Python virtual environment.

   For Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   For macOS and Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Install di libraries wey you need.

   For Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   For macOS and Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## How to run di YouTube transcription data prep scripts

### For Windows

```powershell
.\transcripts_prepare.ps1
```

### For macOS and Linux

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go fit trust. For important information, e good make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->