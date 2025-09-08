<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:10:25+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "sv"
}
-->
# Transkriptionsdataförberedelse

Skript för transkriptionsdataförberedelse laddar ner YouTube-videotranskript och förbereder dem för användning med exemplet Semantic Search med OpenAI Embeddings och Functions.

Skripten för transkriptionsdataförberedelse har testats på de senaste versionerna av Windows 11, macOS Ventura och Ubuntu 22.04 (och senare).

## Skapa nödvändiga Azure OpenAI Service-resurser

> [!IMPORTANT]
> Vi rekommenderar att du uppdaterar Azure CLI till den senaste versionen för att säkerställa kompatibilitet med OpenAI
> Se [Dokumentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Skapa en resursgrupp

> [!NOTE]
> För dessa instruktioner använder vi resursgruppen med namnet "semantic-video-search" i East US.
> Du kan ändra namnet på resursgruppen, men om du ändrar platsen för resurserna,
> kontrollera [modellens tillgänglighetstabell](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Skapa en Azure OpenAI Service-resurs.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Hämta endpoint och nycklar för användning i denna applikation

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Distribuera följande modeller:
   - `text-embedding-ada-002` version `2` eller högre, med namnet `text-embedding-ada-002`
   - `gpt-35-turbo` version `0613` eller högre, med namnet `gpt-35-turbo`

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

## Nödvändig programvara

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) eller senare

## Miljövariabler

Följande miljövariabler krävs för att köra skripten för YouTube-transkriptionsdataförberedelse.

### På Windows

Vi rekommenderar att du lägger till variablerna i dina `user`-miljövariabler.
`Windows Start` > `Redigera systemets miljövariabler` > `Miljövariabler` > `Användarvariabler` för [USER] > `Ny`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```



### På Linux och macOS

Vi rekommenderar att du lägger till följande exports i din `~/.bashrc` eller `~/.zshrc`-fil.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Installera nödvändiga Python-bibliotek

1. Installera [git-klienten](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) om den inte redan är installerad.
1. Från ett `Terminal`-fönster, klona exemplet till din föredragna mapp för repo.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Navigera till mappen `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Skapa en Python-virtuell miljö.

    På Windows:

    ```powershell
    python -m venv .venv
    ```

    På macOS och Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Aktivera den virtuella Python-miljön.

   På Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   På macOS och Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Installera de nödvändiga biblioteken.

   På Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   På macOS och Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Kör skripten för YouTube-transkriptionsdataförberedelse

### På Windows

```powershell
.\transcripts_prepare.ps1
```

### På macOS och Linux

```bash
./transcripts_prepare.sh
```

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.