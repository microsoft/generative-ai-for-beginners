<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-10-11T11:24:51+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "ta"
}
-->
# உரை தரவுகளை தயாரித்தல்

உரை தரவுகளை தயாரிக்கும் ஸ்கிரிப்ட்கள் YouTube வீடியோ உரைகளை பதிவிறக்கம் செய்து, Semantic Search with OpenAI Embeddings மற்றும் Functions மாதிரியில் பயன்படுத்த தயாராக செய்கின்றன.

உரை தரவுகளை தயாரிக்கும் ஸ்கிரிப்ட்கள் Windows 11, macOS Ventura மற்றும் Ubuntu 22.04 (மேலும் அதற்கு மேல்) ஆகியவற்றின் சமீபத்திய வெளியீடுகளில் சோதிக்கப்பட்டுள்ளன.

## தேவையான Azure OpenAI Service வளங்களை உருவாக்குதல்

> [!IMPORTANT]
> OpenAI உடன் இணக்கமாக செயல்பட Azure CLI-யை சமீபத்திய பதிப்புக்கு மேம்படுத்த பரிந்துரைக்கிறோம்.
> [ஆவணத்தை](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) பார்க்கவும்.

1. ஒரு resource group உருவாக்கவும்

> [!NOTE]
> இந்த வழிமுறைகளுக்கு, East US-ல் "semantic-video-search" எனப்படும் resource group-ஐ பயன்படுத்துகிறோம்.
> resource group பெயரை மாற்றலாம், ஆனால் வளங்களுக்கான இடத்தை மாற்றும்போது, 
> [மாதிரி கிடைக்கும் அட்டவணையை](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) சரிபார்க்கவும்.

```console
az group create --name semantic-video-search --location eastus
```

1. Azure OpenAI Service வளத்தை உருவாக்கவும்.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. இந்த பயன்பாட்டில் பயன்படுத்த endpoint மற்றும் keys-ஐ பெறவும்.

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. பின்வரும் மாதிரிகளை deploy செய்யவும்:
   - `text-embedding-ada-002` பதிப்பு `2` அல்லது அதற்கு மேல், `text-embedding-ada-002` என பெயரிடப்பட்டது
   - `gpt-35-turbo` பதிப்பு `0613` அல்லது அதற்கு மேல், `gpt-35-turbo` என பெயரிடப்பட்டது

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

## தேவையான மென்பொருள்

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) அல்லது அதற்கு மேல்

## சூழல் மாறிகள்

YouTube உரை தரவுகளை தயாரிக்கும் ஸ்கிரிப்ட்களை இயக்க, பின்வரும் சூழல் மாறிகள் தேவை.

### Windows-ல்

சூழல் மாறிகளை உங்கள் `user` சூழல் மாறிகளில் சேர்க்க பரிந்துரைக்கிறோம்.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER]-க்கான `User variables` > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- சூழல் மாறிகளை உங்கள் PowerShell profile-ல் சேர்க்கலாம்.

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### Linux மற்றும் macOS-ல்

பின்வரும் exports-ஐ உங்கள் `~/.bashrc` அல்லது `~/.zshrc` கோப்பில் சேர்க்க பரிந்துரைக்கிறோம்.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## தேவையான Python நூலகங்களை நிறுவுதல்

1. [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) நிறுவப்படவில்லை என்றால் அதை நிறுவவும்.
1. `Terminal` சாளரத்தில் இருந்து, மாதிரியை உங்கள் விருப்பமான repo கோப்பகத்துக்கு clone செய்யவும்.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` கோப்பகத்துக்கு செல்லவும்.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python virtual environment உருவாக்கவும்.

    Windows-ல்:

    ```powershell
    python -m venv .venv
    ```

    macOS மற்றும் Linux-ல்:

    ```bash
    python3 -m venv .venv
    ```

1. Python virtual environment-ஐ செயல்படுத்தவும்.

   Windows-ல்:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS மற்றும் Linux-ல்:

   ```bash
   source .venv/bin/activate
   ```

1. தேவையான நூலகங்களை நிறுவவும்.

   Windows-ல்:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS மற்றும் Linux-ல்:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube உரை தரவுகளை தயாரிக்கும் ஸ்கிரிப்ட்களை இயக்குதல்

### Windows-ல்

```powershell
.\transcripts_prepare.ps1
```

### macOS மற்றும் Linux-ல்

```bash
./transcripts_prepare.sh
```

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.