# Átirat-adatelőkészítés

Az átirat-adatelőkészítő szkriptek letöltik a YouTube videó átiratokat, és előkészítik azokat a Semantic Search with OpenAI Embeddings and Functions minta használatához.

Az átirat-adatelőkészítő szkripteket teszteltük a legújabb Windows 11, macOS Ventura és Ubuntu 22.04 (és újabb) kiadásokon.

## Szükséges Azure OpenAI szolgáltatás erőforrások létrehozása

> [!IMPORTANT]
> Javasoljuk, hogy frissítse az Azure CLI-t a legújabb verzióra az OpenAI kompatibilitás biztosítása érdekében
> Lásd a [Dokumentáció](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) oldalt

1. Hozzon létre egy erőforráscsoportot

> [!NOTE]
> Az útmutatásban a "semantic-video-search" nevű erőforráscsoportot használjuk, amely az East US régióban található.
> Megváltoztathatja az erőforráscsoport nevét, de ha módosítja az erőforrások helyét,
> ellenőrizze a [modell elérhetőségi táblázatot](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Hozzon létre egy Azure OpenAI szolgáltatás erőforrást.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Szerezze meg a végpontot és kulcsokat az alkalmazás használatához

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Telepítse a következő modelleket:
   - `text-embedding-ada-002` verzió `2` vagy magasabb, neve `text-embedding-ada-002`
   - `gpt-5-mini` neve `gpt-5-mini`

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

## Szükséges szoftver

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) vagy újabb

## Környezeti változók

A YouTube átirat-adatelőkészítő szkriptek futtatásához az alábbi környezeti változók szükségesek.

### Windows rendszeren

Ajánlott hozzáadni a változókat a `user` környezeti változókhoz.
`Windows Start` > `A rendszer környezeti változóinak szerkesztése` > `Környezeti változók` > `[FELHASZNÁLÓ]` felhasználói változók > `Új`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- A környezeti változókat hozzáadhatja a PowerShell profiljához.

```powershell
$env:AZURE_OPENAI_API_KEY = "<az Azure OpenAI Service API kulcsa>"
$env:AZURE_OPENAI_ENDPOINT = "<az Azure OpenAI Service végpontja>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<az Azure OpenAI Service modell telepítésének neve>"
$env:GOOGLE_DEVELOPER_API_KEY = "<az Ön Google fejlesztői API kulcsa>"
``` -->

### Linux és macOS rendszeren

Javasolt az alábbi exportokat hozzáadni a `~/.bashrc` vagy `~/.zshrc` fájlhoz.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Szükséges Python könyvtárak telepítése

1. Telepítse a [git klienst](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), ha még nincs telepítve.
1. A `Terminál` ablakból klónozza a mintát a kívánt repó mappába.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Navigáljon a `data_prep` mappába.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Hozzon létre egy Python virtuális környezetet.

    Windows rendszeren:

    ```powershell
    python -m venv .venv
    ```

    macOS és Linux rendszeren:

    ```bash
    python3 -m venv .venv
    ```

1. Aktiválja a Python virtuális környezetet.

   Windows rendszeren:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS és Linux rendszeren:

   ```bash
   source .venv/bin/activate
   ```

1. Telepítse a szükséges könyvtárakat.

   Windows rendszeren:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS és Linux rendszeren:

   ```bash
   pip3 install -r requirements.txt
   ```

## Futtassa a YouTube átirat-adatelőkészítő szkripteket

### Windows rendszeren

```powershell
.\transcripts_prepare.ps1
```

### macOS és Linux rendszeren

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->