# Transcriptie data voorbereiding

De transcriptie data voorbereiding scripts downloaden YouTube video transcripties en bereiden deze voor gebruik met de Voorbeeld ‘Semantische Zoekopdracht met OpenAI Embeddings en Functies’.

De transcriptie data voorbereiding scripts zijn getest op de nieuwste versies van Windows 11, macOS Ventura en Ubuntu 22.04 (en hoger).

## Maak vereiste Azure OpenAI Service bronnen aan

> [!IMPORTANT]
> We raden aan de Azure CLI bij te werken naar de nieuwste versie om compatibiliteit met OpenAI te waarborgen.
> Zie [Documentatie](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Maak een resourcegroep aan

> [!NOTE]
> Voor deze instructies gebruiken we de resourcegroep genaamd "semantic-video-search" in East US.
> Je kunt de naam van de resourcegroep wijzigen, maar wanneer je ook de locatie wijzigt, 
> controleer dan de [tabel met modelbeschikbaarheid](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

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

1. Deploy de volgende modellen:
   - `text-embedding-ada-002` versie `2` of hoger, met de naam `text-embedding-ada-002`
   - `gpt-5-mini` met de naam `gpt-5-mini`

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
    --deployment-name gpt-5-mini \
    --model-name gpt-5-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## Vereiste software

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) of hoger

## Omgevingsvariabelen

De volgende omgevingsvariabelen zijn vereist om de YouTube transcriptie data voorbereiding scripts te draaien.

### Op Windows

We raden aan de variabelen toe te voegen aan je `user` omgevingsvariabelen.
`Windows Start` > `Systeemomgevingsvariabelen bewerken` > `Omgevingsvariabelen` > `Gebruikersvariabelen` voor [USER] > `Nieuw`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Je kunt de omgevingsvariabelen ook toevoegen aan je PowerShell-profiel.

```powershell
$env:AZURE_OPENAI_API_KEY = "<jouw Azure OpenAI Service API sleutel>"
$env:AZURE_OPENAI_ENDPOINT = "<jouw Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<jouw Azure OpenAI Service model deployment naam>"
$env:GOOGLE_DEVELOPER_API_KEY = "<jouw Google developer API sleutel>"
``` -->

### Op Linux en macOS

We raden aan de volgende exports toe te voegen aan je `~/.bashrc` of `~/.zshrc` bestand.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Installeer de vereiste Python libraries

1. Installeer de [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) indien deze nog niet geïnstalleerd is.
1. Clone vanaf een `Terminal` venster de sample naar je voorkeursrepo map.

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

1. Installeer de vereiste libraries.

   Op Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Op macOS en Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Draai de YouTube transcriptie data voorbereiding scripts

### Op Windows

```powershell
.\transcripts_prepare.ps1
```

### Op macOS en Linux

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->