<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:53:58+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "hu"
}
-->
# Átirat adat-előkészítés

Az átirat adat-előkészítő szkriptek letöltik a YouTube videók átiratait, és előkészítik azokat a Semantikus keresés OpenAI Beágyazásokkal és Funkciókkal minta használatához.

Az átirat adat-előkészítő szkripteket tesztelték a legújabb Windows 11, macOS Ventura és Ubuntu 22.04 (és újabb) kiadásokon.

## Szükséges Azure OpenAI Szolgáltatás erőforrások létrehozása

> [!IMPORTANT]
> Javasoljuk, hogy frissítse az Azure CLI-t a legújabb verzióra a kompatibilitás biztosítása érdekében az OpenAI-val.
> Lásd [Dokumentáció](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Hozzon létre egy erőforráscsoportot

> [!NOTE]
> Ezekhez az utasításokhoz az "semantic-video-search" nevű erőforráscsoportot használjuk Kelet-USA-ban.
> Megváltoztathatja az erőforráscsoport nevét, de amikor az erőforrások helyét változtatja, 
> ellenőrizze a [modell elérhetőségi táblázatot](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Hozzon létre egy Azure OpenAI Szolgáltatás erőforrást.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Szerezze be a végpontot és a kulcsokat az alkalmazás használatához

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Telepítse a következő modelleket:
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

## Szükséges szoftver

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) vagy újabb

## Környezeti változók

A következő környezeti változók szükségesek a YouTube átirat adat-előkészítő szkriptek futtatásához.

### Windows-on

Javasoljuk, hogy adja hozzá a változókat a `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Linux és macOS esetén

Javasoljuk, hogy adja hozzá a következő exportokat a `~/.bashrc` or `~/.zshrc` fájlhoz.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## A szükséges Python könyvtárak telepítése

1. Telepítse a [git klienst](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), ha még nincs telepítve.
1. Egy `Terminál` ablakból klónozza a mintát a preferált repo mappájába.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Navigáljon a `data_prep` mappába.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Hozzon létre egy Python virtuális környezetet.

    Windows-on:

    ```powershell
    python -m venv .venv
    ```

    macOS és Linux esetén:

    ```bash
    python3 -m venv .venv
    ```

1. Aktiválja a Python virtuális környezetet.

   Windows-on:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS és Linux esetén:

   ```bash
   source .venv/bin/activate
   ```

1. Telepítse a szükséges könyvtárakat.

   Windows-on:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS és Linux esetén:

   ```bash
   pip3 install -r requirements.txt
   ```

## A YouTube átirat adat-előkészítő szkriptek futtatása

### Windows-on

```powershell
.\transcripts_prepare.ps1
```

### macOS és Linux esetén

```bash
./transcripts_prepare.sh
```

**Felelősség kizárása**:  
Ezt a dokumentumot az AI fordítási szolgáltatással, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő a hiteles forrásnak. Fontos információk esetén javasolt a professzionális emberi fordítás. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félremagyarázásokért.