<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:46:07+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "en"
}
-->
# Transcription data prep

The transcription data prep scripts download YouTube video transcripts and prepare them for use with the Semantic Search with OpenAI Embeddings and Functions sample.

The transcription data prep scripts have been tested on the latest releases of Windows 11, macOS Ventura, and Ubuntu 22.04 (and above).

## Create required Azure OpenAI Service resources

> [!IMPORTANT]
> We suggest you update the Azure CLI to the latest version to ensure compatibility with OpenAI
> See [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Create a resource group

> [!NOTE]
> For these instructions, we're using the resource group named "semantic-video-search" in East US.
> You can change the name of the resource group, but when changing the location for the resources,
> check the [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Create an Azure OpenAI Service resource.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Get the endpoint and keys for usage in this application

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Deploy the following models:
   - `text-embedding-ada-002` version `2` or greater, named `text-embedding-ada-002`
   - `gpt-35-turbo` version `0613` or greater, named `gpt-35-turbo`

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

## Required software

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) or greater

## Environment variables

The following environment variables are required to run the YouTube transcription data prep scripts.

### On Windows

Recommend adding the variables to your `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### On Linux and macOS

Recommend adding the following exports to your `~/.bashrc` or `~/.zshrc` file.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Install the required Python libraries

1. Install the [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) if it's not already installed.
1. From a `Terminal` window, clone the sample to your preferred repo folder.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Navigate to the `data_prep` folder.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Create a Python virtual environment.

    On Windows:

    ```powershell
    python -m venv .venv
    ```

    On macOS and Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Activate the Python virtual environment.

   On Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   On macOS and Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Install the required libraries.

   On Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   On macOS and Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Run the YouTube transcription data prep scripts

### On Windows

```powershell
.\transcripts_prepare.ps1
```

### On macOS and Linux

```bash
./transcripts_prepare.sh
```

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.