<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:53:29+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "tl"
}
-->
# Paghahanda ng Data ng Transkripsyon

Ang mga script para sa paghahanda ng data ng transkripsyon ay nagda-download ng mga transcript ng video mula sa YouTube at inihahanda ang mga ito para magamit sa Semantic Search gamit ang OpenAI Embeddings at Functions sample.

Ang mga script para sa paghahanda ng data ng transkripsyon ay nasubukan sa mga pinakabagong bersyon ng Windows 11, macOS Ventura at Ubuntu 22.04 (at pataas).

## Gumawa ng kinakailangang mga resource para sa Azure OpenAI Service

1. Gumawa ng resource group

> [!NOTE]
> Para sa mga instruksyon na ito, ginagamit namin ang resource group na pinangalanang "semantic-video-search" sa East US.
> Maaari mong palitan ang pangalan ng resource group, ngunit kapag binabago ang lokasyon para sa mga resource,
> tingnan ang [talahanayan ng availability ng modelo](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Gumawa ng resource para sa Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Kunin ang endpoint at mga key para magamit sa application na ito

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. I-deploy ang mga sumusunod na modelo:
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

## Kinakailangang software

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) o mas mataas pa

## Mga environment variable

Ang mga sumusunod na environment variable ay kinakailangan upang patakbuhin ang mga script para sa paghahanda ng data ng transkripsyon mula sa YouTube.

### Sa Windows

Inirerekomenda na idagdag ang mga variable sa iyong `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Sa Linux at macOS

Inirerekomenda na idagdag ang mga sumusunod na exports sa iyong `~/.bashrc` or `~/.zshrc` file.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## I-install ang kinakailangang mga Python library

1. I-install ang [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) kung hindi pa ito naka-install.
1. Mula sa `Terminal` window, i-clone ang sample sa iyong nais na repo folder.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Pumunta sa `data_prep` folder.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Gumawa ng Python virtual environment.

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

1. I-install ang kinakailangang mga library.

   Sa Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Sa macOS at Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Patakbuhin ang mga script para sa paghahanda ng data ng transkripsyon mula sa YouTube

### Sa Windows

```powershell
.\transcripts_prepare.ps1
```

### Sa macOS at Linux

```bash
./transcripts_prepare.sh
```

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Habang sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga error o hindi tumpak na impormasyon. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na mapagkakatiwalaang mapagkukunan. Para sa kritikal na impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.