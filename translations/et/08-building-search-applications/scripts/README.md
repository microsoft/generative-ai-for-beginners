<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-10-11T11:25:03+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "et"
}
-->
# Transkriptsiooniandmete ettevalmistamine

Transkriptsiooniandmete ettevalmistamise skriptid laadivad alla YouTube'i videote transkriptsioonid ja valmistavad need ette kasutamiseks näidises "Semantiline otsing OpenAI Embeddings ja Functions abil".

Transkriptsiooniandmete ettevalmistamise skripte on testitud uusimate Windows 11, macOS Ventura ja Ubuntu 22.04 (ja uuemate) versioonidega.

## Vajalike Azure OpenAI Service ressursside loomine

> [!IMPORTANT]
> Soovitame värskendada Azure CLI uusimale versioonile, et tagada ühilduvus OpenAI-ga.
> Vaata [dokumentatsiooni](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Loo ressursigrupp

> [!NOTE]
> Nendes juhistes kasutame ressursigruppi nimega "semantic-video-search" asukohas East US.
> Ressursigrupi nime saab muuta, kuid ressursside asukoha muutmisel kontrollige [mudelite saadavuse tabelit](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Loo Azure OpenAI Service ressurss.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Hangi lõpp-punkt ja võtmed selle rakenduse kasutamiseks.

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Paigalda järgmised mudelid:
   - `text-embedding-ada-002` versioon `2` või uuem, nimega `text-embedding-ada-002`
   - `gpt-35-turbo` versioon `0613` või uuem, nimega `gpt-35-turbo`

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

## Vajalik tarkvara

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) või uuem

## Keskkonnamuutujad

Järgmised keskkonnamuutujad on vajalikud YouTube'i transkriptsiooniandmete ettevalmistamise skriptide käivitamiseks.

### Windowsis

Soovitame lisada muutujad oma `kasutaja` keskkonnamuutujatesse.
`Windows Start` > `Muuda süsteemi keskkonnamuutujaid` > `Keskkonnamuutujad` > `Kasutaja muutujad` [KASUTAJA] jaoks > `Uus`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Saate lisada keskkonnamuutujad oma PowerShelli profiili.

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### Linuxis ja macOS-is

Soovitame lisada järgmised ekspordid oma `~/.bashrc` või `~/.zshrc` faili.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Vajalike Python'i teekide paigaldamine

1. Paigalda [git klient](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), kui see pole veel paigaldatud.
1. Ava `Terminal` aken ja klooni näidis oma eelistatud repo kausta.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Liigu `data_prep` kausta.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Loo Python'i virtuaalne keskkond.

    Windowsis:

    ```powershell
    python -m venv .venv
    ```

    macOS-is ja Linuxis:

    ```bash
    python3 -m venv .venv
    ```

1. Aktiveeri Python'i virtuaalne keskkond.

   Windowsis:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS-is ja Linuxis:

   ```bash
   source .venv/bin/activate
   ```

1. Paigalda vajalikud teegid.

   Windowsis:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS-is ja Linuxis:

   ```bash
   pip3 install -r requirements.txt
   ```

## Käivita YouTube'i transkriptsiooniandmete ettevalmistamise skriptid

### Windowsis

```powershell
.\transcripts_prepare.ps1
```

### macOS-is ja Linuxis

```bash
./transcripts_prepare.sh
```

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.