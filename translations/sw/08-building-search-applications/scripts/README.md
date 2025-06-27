<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-06-25T16:58:27+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "sw"
}
-->
# Maandalizi ya data ya unukuzi

Skripti za maandalizi ya data ya unukuzi hupakua nakala za video za YouTube na kuzitayarisha kwa matumizi na Utafutaji wa Semantiki na OpenAI Embeddings na Sampuli za Kazi.

Skripti za maandalizi ya data ya unukuzi zimejaribiwa kwenye matoleo mapya zaidi ya Windows 11, macOS Ventura na Ubuntu 22.04 (na zaidi).

## Unda rasilimali zinazohitajika za Huduma ya Azure OpenAI

> [!IMPORTANT]
> Tunapendekeza usasishe Azure CLI kwa toleo jipya zaidi ili kuhakikisha utangamano na OpenAI
> Tazama [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Unda kikundi cha rasilimali

> [!NOTE]
> Kwa maagizo haya tunatumia kikundi cha rasilimali kinachoitwa "semantic-video-search" katika Mashariki ya Marekani.
> Unaweza kubadilisha jina la kikundi cha rasilimali, lakini unapo badilisha eneo la rasilimali, 
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

1. Peleka modeli zifuatazo:
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

## Programu inayohitajika

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) au zaidi

## Vigezo vya mazingira

Vigezo vifuatavyo vya mazingira vinahitajika kuendesha skripti za maandalizi ya data ya unukuzi wa YouTube.

### Kwenye Windows

Pendekeza kuongeza vigezo kwenye `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Kwenye Linux na macOS

Pendekeza kuongeza exports zifuatazo kwenye faili yako ya `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Sakinisha maktaba zinazohitajika za Python

1. Sakinisha [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) kama haijasakinishwa tayari.
1. Kutoka kwenye dirisha la `Terminal`, clone sampuli kwenye folda yako unayopendelea ya repo.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Tembea hadi kwenye folda ya `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Unda mazingira ya kawaida ya Python.

    Kwenye Windows:

    ```powershell
    python -m venv .venv
    ```

    Kwenye macOS na Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Washa mazingira ya kawaida ya Python.

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

## Endesha skripti za maandalizi ya data ya unukuzi wa YouTube

### Kwenye Windows

```powershell
.\transcripts_prepare.ps1
```

### Kwenye macOS na Linux

```bash
./transcripts_prepare.sh
```

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya kiasili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.