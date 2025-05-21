<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:53:43+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "sw"
}
-->
# Maandalizi ya Data ya Unukuzi

Skripti za maandalizi ya data ya unukuzi hupakua maandiko ya video za YouTube na kuyaandaa kwa matumizi na Mfano wa Utafutaji wa Kisemantiki na OpenAI Embeddings na Functions.

Skripti za maandalizi ya data ya unukuzi zimejaribiwa kwenye matoleo mapya ya Windows 11, macOS Ventura na Ubuntu 22.04 (na zaidi).

## Unda rasilimali zinazohitajika za Huduma ya Azure OpenAI

> [!IMPORTANT]
> Tunapendekeza usasishe Azure CLI hadi toleo la hivi karibuni ili kuhakikisha inafanya kazi na OpenAI
> Tazama [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Unda kikundi cha rasilimali

> [!NOTE]
> Kwa maelekezo haya tunatumia kikundi cha rasilimali kinachoitwa "semantic-video-search" huko East US.
> Unaweza kubadilisha jina la kikundi cha rasilimali, lakini unapobadilisha eneo la rasilimali, 
> angalia [jedwali la upatikanaji wa modeli](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Unda rasilimali ya Huduma ya Azure OpenAI.

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

1. Sambaza modeli zifuatazo:
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

## Programu zinazohitajika

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) au zaidi

## Vigezo vya mazingira

Vigezo vya mazingira vifuatavyo vinahitajika kuendesha skripti za maandalizi ya data ya unukuzi wa YouTube.

### Kwenye Windows

Tunapendekeza kuongeza vigezo kwenye `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Kwenye Linux na macOS

Tunapendekeza kuongeza exports zifuatazo kwenye faili yako ya `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Sakinisha maktaba zinazohitajika za Python

1. Sakinisha [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ikiwa haijasakinishwa tayari.
1. Kutoka kwenye dirisha la `Terminal`, clone mfano kwenye folda unayopendelea ya repo.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Nenda kwenye folda ya `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Unda mazingira halisi ya Python.

    Kwenye Windows:

    ```powershell
    python -m venv .venv
    ```

    Kwenye macOS na Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Washa mazingira halisi ya Python.

   Kwenye Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Kwenye macOS na Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Sakinisha maktaba zinazohitajika.

   Kwenye windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Kwenye macOS na Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Endesha skripti za maandalizi ya data ya unukuzi wa YouTube

### Kwenye windows

```powershell
.\transcripts_prepare.ps1
```

### Kwenye macOS na Linux

```bash
./transcripts_prepare.sh
```

**Kanusho**: 
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwepo kwa usahihi. Hati ya awali katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya kibinadamu inapendekezwa. Hatuwajibiki kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.