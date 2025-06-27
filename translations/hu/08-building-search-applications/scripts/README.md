<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-06-25T16:58:41+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "hu"
}
-->
# Átirat adat előkészítése

Az átirat adat előkészítő szkriptek letöltik a YouTube videók átiratait és előkészítik őket az OpenAI Beágyazásokkal és Funkciókkal való Szemantikai Keresés mintához.

Az átirat adat előkészítő szkriptek tesztelve lettek a legújabb Windows 11, macOS Ventura és Ubuntu 22.04 (és újabb) kiadásokon.

## Szükséges Azure OpenAI Service erőforrások létrehozása

> [!IMPORTANT]
> Javasoljuk, hogy frissítse az Azure CLI-t a legújabb verzióra a kompatibilitás biztosítása érdekében az OpenAI-val.
> Lásd [Dokumentáció](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Erőforrás csoport létrehozása

> [!NOTE]
> Ezekhez az utasításokhoz a "semantic-video-search" nevű erőforrás csoportot használjuk Kelet USA-ban.
> Megváltoztathatja az erőforrás csoport nevét, de ha megváltoztatja az erőforrások helyét, 
> ellenőrizze a [modell elérhetőségi táblázatot](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Azure OpenAI Service erőforrás létrehozása.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Szerezze meg az alkalmazás használatához szükséges végpontot és kulcsokat.

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

## Szükséges szoftverek

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) vagy újabb

## Környezeti változók

A következő környezeti változók szükségesek a YouTube átirat adat előkészítő szkriptek futtatásához.

### Windows-on

Ajánlott hozzáadni a változókat a `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`-hoz.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Linux és macOS-en

Ajánlott hozzáadni a következő exportokat a `~/.bashrc` or `~/.zshrc` fájlhoz.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Szükséges Python könyvtárak telepítése

1. Telepítse a [git kliens](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst)-t, ha még nincs telepítve.
1. Egy `Terminal` ablakból klónozza a mintát a kívánt repo mappába.

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

    macOS és Linux-on:

    ```bash
    python3 -m venv .venv
    ```

1. Aktiválja a Python virtuális környezetet.

   Windows-on:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS és Linux-on:

   ```bash
   source .venv/bin/activate
   ```

1. Telepítse a szükséges könyvtárakat.

   Windows-on:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS és Linux-on:

   ```bash
   pip3 install -r requirements.txt
   ```

## Futtassa a YouTube átirat adat előkészítő szkripteket

### Windows-on

```powershell
.\transcripts_prepare.ps1
```

### macOS és Linux-on

```bash
./transcripts_prepare.sh
```

**Jogi nyilatkozat**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatással lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.