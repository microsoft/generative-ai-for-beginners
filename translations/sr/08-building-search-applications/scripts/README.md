<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:55:22+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "sr"
}
-->
# Priprema podataka za transkripciju

Skripte za pripremu podataka za transkripciju preuzimaju transkripte YouTube videa i pripremaju ih za korišćenje sa primerom Semantičke pretrage koristeći OpenAI Ugradnje i Funkcije.

Skripte za pripremu podataka za transkripciju su testirane na najnovijim verzijama Windows 11, macOS Ventura i Ubuntu 22.04 (i novijim).

## Kreiranje potrebnih resursa za Azure OpenAI uslugu

> [!IMPORTANT]
> Preporučujemo da ažurirate Azure CLI na najnoviju verziju kako biste osigurali kompatibilnost sa OpenAI
> Pogledajte [Dokumentaciju](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Kreirajte grupu resursa

> [!NOTE]
> Za ova uputstva koristimo grupu resursa nazvanu "semantic-video-search" u East US.
> Možete promeniti ime grupe resursa, ali kada menjate lokaciju za resurse,
> proverite [tabelu dostupnosti modela](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Kreirajte resurs za Azure OpenAI uslugu.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Preuzmite krajnju tačku i ključeve za korišćenje u ovoj aplikaciji

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Implementirajte sledeće modele:
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

## Potreban softver

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ili noviji

## Promenljive okruženja

Sledeće promenljive okruženja su potrebne za pokretanje skripti za pripremu podataka za transkripciju sa YouTube-a.

### Na Windows-u

Preporučujemo dodavanje promenljivih u vaš `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Na Linux-u i macOS-u

Preporučujemo dodavanje sledećih eksportova u vaš `~/.bashrc` or `~/.zshrc` fajl.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Instalacija potrebnih Python biblioteka

1. Instalirajte [git klijent](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ako već nije instaliran.
1. Iz `Terminal` prozora, klonirajte primer u željeni folder za repozitorijume.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Idite u `data_prep` folder.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Kreirajte Python virtuelno okruženje.

    Na Windows-u:

    ```powershell
    python -m venv .venv
    ```

    Na macOS-u i Linux-u:

    ```bash
    python3 -m venv .venv
    ```

1. Aktivirajte Python virtuelno okruženje.

   Na Windows-u:

   ```powershell
   .venv\Scripts\activate
   ```

   Na macOS-u i Linux-u:

   ```bash
   source .venv/bin/activate
   ```

1. Instalirajte potrebne biblioteke.

   Na Windows-u:

   ```powershell
   pip install -r requirements.txt
   ```

   Na macOS-u i Linux-u:

   ```bash
   pip3 install -r requirements.txt
   ```

## Pokrenite skripte za pripremu podataka za transkripciju sa YouTube-a

### Na Windows-u

```powershell
.\transcripts_prepare.ps1
```

### Na macOS-u i Linux-u

```bash
./transcripts_prepare.sh
```

**Одрицање од одговорности**:  
Овај документ је преведен користећи AI услугу за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да будете свесни да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације, препоручује се професионални људски превод. Не сносимо одговорност за било каква неспоразума или погрешна тумачења која произилазе из употребе овог превода.