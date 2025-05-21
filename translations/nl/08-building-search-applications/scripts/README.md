<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:52:12+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "nl"
}
-->
# Voorbereiding van transcriptiegegevens

De scripts voor het voorbereiden van transcriptiegegevens downloaden YouTube-video transcripties en maken ze gereed voor gebruik met het voorbeeld van Semantische Zoekopdracht met OpenAI Embeddings en Functies.

De scripts voor het voorbereiden van transcriptiegegevens zijn getest op de nieuwste versies van Windows 11, macOS Ventura en Ubuntu 22.04 (en hoger).

## Vereiste Azure OpenAI Service resources aanmaken

> [!IMPORTANT]
> We raden aan de Azure CLI te updaten naar de nieuwste versie om compatibiliteit met OpenAI te garanderen.
> Zie [Documentatie](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Maak een resourcegroep aan

> [!NOTE]
> Voor deze instructies gebruiken we de resourcegroep genaamd "semantic-video-search" in East US.
> Je kunt de naam van de resourcegroep wijzigen, maar wanneer je de locatie voor de resources verandert,
> controleer dan de [modelbeschikbaarheidstabel](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Maak een Azure OpenAI Service resource aan.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Verkrijg de endpoint en sleutels voor gebruik in deze applicatie

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Implementeer de volgende modellen:
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

## Vereiste software

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) of hoger

## Omgevingsvariabelen

De volgende omgevingsvariabelen zijn vereist om de YouTube transcriptiegegevens voorbereidingsscripts uit te voeren.

### Op Windows

Aanbevolen om de variabelen toe te voegen aan je `user` environment variables.
`Windows Start` > `Systeemomgevingsvariabelen bewerken` > `Omgevingsvariabelen` > `Gebruikersvariabelen` for [USER] > `Nieuw`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Op Linux en macOS

Aanbevolen om de volgende exports toe te voegen aan je `~/.bashrc` or `~/.zshrc` bestand.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Installeer de vereiste Python bibliotheken

1. Installeer de [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) als deze nog niet is geïnstalleerd.
1. Vanuit een `Terminal` venster, kloon het voorbeeld naar je gewenste repo map.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Navigeer naar de `data_prep` map.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Maak een Python virtuele omgeving aan.

    Op Windows:

    ```powershell
    python -m venv .venv
    ```

    Op macOS en Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Activeer de Python virtuele omgeving.

   Op Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Op macOS en Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Installeer de vereiste bibliotheken.

   Op Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Op macOS en Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Voer de YouTube transcriptiegegevens voorbereidingsscripts uit

### Op Windows

```powershell
.\transcripts_prepare.ps1
```

### Op macOS en Linux

```bash
./transcripts_prepare.sh
```

**Disclaimer**:  
Dit document is vertaald met behulp van AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.