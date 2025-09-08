<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:12:05+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "sw"
}
-->
# Kuandaa data za uandishi wa maneno

Skripti za kuandaa data za uandishi wa maneno hupakua manukuu ya video za YouTube na kuziandaa kwa matumizi na mfano wa Semantic Search with OpenAI Embeddings and Functions.

Skripti za kuandaa data za uandishi wa maneno zimeshahakikiwa kwenye toleo la hivi karibuni la Windows 11, macOS Ventura na Ubuntu 22.04 (na zaidi).

## Tengeneza rasilimali zinazohitajika za Azure OpenAI Service

> [!IMPORTANT]
> Tunapendekeza usasishaji wa Azure CLI hadi toleo la hivi karibuni ili kuhakikisha ulinganifu na OpenAI
> Angalia [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Tengeneza kundi la rasilimali

> [!NOTE]
> Kwa maelekezo haya tunatumia kundi la rasilimali linaloitwa "semantic-video-search" katika East US.
> Unaweza kubadilisha jina la kundi la rasilimali, lakini unapobadilisha eneo la rasilimali,
> angalia [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Tengeneza rasilimali ya Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Pata endpoint na funguo kwa matumizi katika programu hii

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Sambaza mifano ifuatayo:
   - `text-embedding-ada-002` toleo `2` au zaidi, liitwe `text-embedding-ada-002`
   - `gpt-35-turbo` toleo `0613` au zaidi, liitwe `gpt-35-turbo`

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

## Programu zinazohitajika

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) au zaidi

## Mabadiliko ya mazingira

Mabadiliko yafuatayo ya mazingira yanahitajika kuendesha skripti za kuandaa data za uandishi wa maneno za YouTube.

### Kwenye Windows

Inashauriwa kuongeza mabadiliko haya kwenye mabadiliko ya mazingira ya `user`.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` kwa [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Kwenye Linux na macOS

Inashauriwa kuongeza amri zifuatazo za export kwenye faili yako ya `~/.bashrc` au `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Sakinisha maktaba za Python zinazohitajika

1. Sakinisha [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) kama bado haijasakinishwa.
1. Kutoka kwenye dirisha la `Terminal`, nakili mfano hadi folda yako unayopendelea ya repo.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Nenda kwenye folda ya `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Tengeneza mazingira ya virtual ya Python.

    Kwenye Windows:

    ```powershell
    python -m venv .venv
    ```

    Kwenye macOS na Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Washa mazingira ya virtual ya Python.

   Kwenye Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Kwenye macOS na Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Sakinisha maktaba zinazohitajika.

   Kwenye Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Kwenye macOS na Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Endesha skripti za kuandaa data za uandishi wa maneno za YouTube

### Kwenye Windows

```powershell
.\transcripts_prepare.ps1
```

### Kwenye macOS na Linux

```bash
./transcripts_prepare.sh
```

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.