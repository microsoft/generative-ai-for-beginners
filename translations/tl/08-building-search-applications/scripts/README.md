# Paghahanda ng datos para sa transkripsyon

Ang mga script sa paghahanda ng datos para sa transkripsyon ay nagda-download ng mga transcript ng video sa YouTube at naghahanda ng mga ito para magamit sa halimbawa ng Semantic Search gamit ang OpenAI Embeddings at Functions.

Ang mga script sa paghahanda ng datos para sa transkripsyon ay nasubukan sa pinakabagong mga bersyon ng Windows 11, macOS Ventura at Ubuntu 22.04 (at mas bago).

## Lumikha ng kinakailangang mga resource sa Azure OpenAI Service

> [!IMPORTANT]
> Iminumungkahi namin na i-update mo ang Azure CLI sa pinakabagong bersyon upang matiyak ang pagiging compatible sa OpenAI
> Tingnan ang [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Lumikha ng resource group

> [!NOTE]
> Para sa mga tagubiling ito, ginagamit namin ang resource group na pinangalanang "semantic-video-search" sa East US.
> Maaari mong palitan ang pangalan ng resource group, ngunit kapag pinalitan ang lokasyon ng mga resource,
> tingnan ang [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Lumikha ng Azure OpenAI Service resource.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Kunin ang endpoint at mga susi para magamit sa aplikasyon na ito

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. I-deploy ang mga sumusunod na modelo:
   - `text-embedding-ada-002` bersyon `2` o mas mataas, na pinangalanang `text-embedding-ada-002`
   - `gpt-4o-mini` na pinangalanang `gpt-4o-mini`

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
    --deployment-name gpt-4o-mini \
    --model-name gpt-4o-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## Kinakailangang software

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) o mas mataas

## Mga environment variable

Ang mga sumusunod na environment variable ay kinakailangan upang patakbuhin ang mga script sa paghahanda ng datos ng YouTube transcription.

### Sa Windows

Inirerekomenda na idagdag ang mga variable sa iyong `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` para sa [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Maaari mong idagdag ang mga environment variable sa iyong PowerShell profile.

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### Sa Linux at macOS

Inirerekomenda na idagdag ang mga sumusunod na export sa iyong `~/.bashrc` o `~/.zshrc` file.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## I-install ang kinakailangang mga Python library

1. I-install ang [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) kung hindi pa ito naka-install.
1. Mula sa isang `Terminal` window, clone ang sample sa iyong nais na folder ng repo.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Pumunta sa `data_prep` folder.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Lumikha ng Python virtual environment.

    Sa Windows:

    ```powershell
    python -m venv .venv
    ```

    Sa macOS at Linux:

    ```bash
    python3 -m venv .venv
    ```

1. I-activate ang Python virtual environment.

   Sa Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Sa macOS at Linux:

   ```bash
   source .venv/bin/activate
   ```

1. I-install ang mga kinakailangang library.

   Sa windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Sa macOS at Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Patakbuhin ang mga script sa paghahanda ng datos ng YouTube transcription

### Sa windows

```powershell
.\transcripts_prepare.ps1
```

### Sa macOS at Linux

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->