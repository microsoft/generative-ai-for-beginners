# Transcription data prep

Di transcription data prep scripts dey download YouTube video transcripts den prepare dem for use wit di Semantic Search wit OpenAI Embeddings and Functions sample.

Di transcription data prep scripts don test for di latest releases Windows 11, macOS Ventura and Ubuntu 22.04 (and above).

## Create required Azure OpenAI Service resources

> [!IMPORTANT]
> We suggest make you update di Azure CLI to di latest version to sure say e go fit work wit OpenAI
> See [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Create one resource group

> [!NOTE]
> For these instructions we dey use di resource group wey dem call "semantic-video-search" for East US.
> You fit change di name of di resource group, but if you dey change di location for di resources,
> check di [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Create one Azure OpenAI Service resource.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Collect di endpoint and keys wey you go use for dis application

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Deploy di following models:
   - `text-embedding-ada-002` version `2` or better, wey dem name `text-embedding-ada-002`
   - `gpt-4o-mini` wey dem name `gpt-4o-mini`

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

## Wetin you need for software

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) or better

## Environment variables

Di following environment variables dey required to run di YouTube transcription data prep scripts.

### For Windows

We recommend say make you add di variables to your `user` environment variables.
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

We recommend say make you add di following exports to your `~/.bashrc` or `~/.zshrc` file.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## How to install di required Python libraries

1. Install di [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) if e never install before.
1. From one `Terminal` window, clone di sample to your preferred repo folder.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Go enter the `data_prep` folder.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Create one Python virtual environment.

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

1. Install di required libraries.

   For Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   For macOS and Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Run di YouTube transcription data prep scripts

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
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->