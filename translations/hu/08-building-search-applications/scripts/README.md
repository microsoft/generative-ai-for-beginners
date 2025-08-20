<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:12:18+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "hu"
}
-->
# Átirat adat-előkészítés

Az átirat adat-előkészítő szkriptek letöltik a YouTube videók átiratait, és előkészítik azokat a Semantic Search with OpenAI Embeddings and Functions mintaalkalmazáshoz.

Az átirat adat-előkészítő szkripteket a legújabb Windows 11, macOS Ventura és Ubuntu 22.04 (vagy újabb) verziókon teszteltük.

## Szükséges Azure OpenAI Service erőforrások létrehozása

> [!IMPORTANT]
> Javasoljuk, hogy frissítsd az Azure CLI-t a legújabb verzióra, hogy biztosítsd az OpenAI-val való kompatibilitást.
> Lásd a [Dokumentációt](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Hozz létre egy erőforráscsoportot

> [!NOTE]
> Ezekhez az utasításokhoz az "semantic-video-search" nevű erőforráscsoportot használjuk az East US régióban.
> Az erőforráscsoport nevét megváltoztathatod, de ha az erőforrások helyét módosítod,
> ellenőrizd a [modell elérhetőségi táblázatot](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Hozz létre egy Azure OpenAI Service erőforrást.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Szerezd meg az alkalmazásban használatos végpontot és kulcsokat

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Telepítsd a következő modelleket:
   - `text-embedding-ada-002` verzió `2` vagy újabb, `text-embedding-ada-002` néven
   - `gpt-35-turbo` verzió `0613` vagy újabb, `gpt-35-turbo` néven

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

A YouTube átirat adat-előkészítő szkriptek futtatásához a következő környezeti változók szükségesek.

### Windows rendszeren

Ajánlott a változókat a `user` környezeti változók közé felvenni.
`Windows Start` > `A rendszer környezeti változóinak szerkesztése` > `Környezeti változók` > `Felhasználói változók` [USER] > `Új`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Linux és macOS rendszeren

Ajánlott a következő exportokat hozzáadni a `~/.bashrc` vagy `~/.zshrc` fájlhoz.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## A szükséges Python könyvtárak telepítése

1. Telepítsd a [git klienst](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), ha még nincs telepítve.
1. Egy `Terminál` ablakból klónozd a mintát a kívánt repó mappába.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Navigálj a `data_prep` mappába.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Hozz létre egy Python virtuális környezetet.

    Windows rendszeren:

    ```powershell
    python -m venv .venv
    ```

    macOS és Linux rendszeren:

    ```bash
    python3 -m venv .venv
    ```

1. Aktiváld a Python virtuális környezetet.

   Windows rendszeren:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS és Linux rendszeren:

   ```bash
   source .venv/bin/activate
   ```

1. Telepítsd a szükséges könyvtárakat.

   Windows rendszeren:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS és Linux rendszeren:

   ```bash
   pip3 install -r requirements.txt
   ```

## Futtasd a YouTube átirat adat-előkészítő szkripteket

### Windows rendszeren

```powershell
.\transcripts_prepare.ps1
```

### macOS és Linux rendszeren

```bash
./transcripts_prepare.sh
```

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.