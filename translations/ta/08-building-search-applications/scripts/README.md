# எழுத்துப்பரிமாற்ற தரவு தயாரிப்பு

எழுத்துப்பரிமாற்ற தரவு தயாரிப்பு ஸ்கிரிப்ட்கள் யுடியூப் வீடியோ உரை மாற்றங்களை பதிவிறக்கம் செய்து, அவற்றை Semantic Search with OpenAI Embeddings and Functions மாதிரிக்குரிய பயன்பாட்டிற்கு தயார் செய்கின்றன.

எழுத்துப்பரிமாற்ற தரவு தயாரிப்பு ஸ்கிரிப்ட்கள் Windows 11, macOS Ventura மற்றும் Ubuntu 22.04 (மேலும் மேல்) சமீபத்திய வெளியீடுகளில் சோதிக்கப்பட்டுள்ளன.

## தேவைப்படும் Azure OpenAI சேவை வளங்களை உருவாக்குக

> [!IMPORTANT]
> OpenAI உடன் பொருந்துதலுக்கு Azure CLI-ஐ சமீபத்திய பதிப்பிற்கு மேம்படுத்த பரிந்துரைக்கிறோம்
> பார்க்கவும் [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. ஒரு வளக் குழுவை உருவாக்குக

> [!NOTE]
> இந்த வழிமுறைகளுக்கு, East US இல் "semantic-video-search" என்ற வளக் குழு பயன்படுத்தப்படுகிறது.
> நீங்கள் வளக் குழுவின் பெயரை மாற்றலாம், ஆனால் வளங்களின் இடத்தை மாற்றும்போது,
> [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) ஐ சரிபார்க்கவும்.

```console
az group create --name semantic-video-search --location eastus
```

1. ஒரு Azure OpenAI சேவை வளத்தை உருவாக்குக.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. இந்த பயன்பாட்டில் பயன்படுத்துகிறீர்கள் என்ற முனையில் அதி முகவரி மற்றும் விசைகளை பெறுக

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. பின்வரும் மாடல்களை அமைக்கவும்:
   - `text-embedding-ada-002` பதிப்பு `2` அல்லது அதற்கு மேலாக, `text-embedding-ada-002` என்ற பெயரில்
   - `gpt-4o-mini` என்ற பெயரில் `gpt-4o-mini`

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

## தேவையான மென்பொருள்

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) அல்லது அதற்கு மேலாக

## சூழல் மாறிகள்

YouTube எழுத்துப்பரிமாற்ற தரவு தயாரிப்பு ஸ்கிரிப்ட்களை இயக்கு பின்வரும் சூழல் மாறிகள் தேவை.

### விண்டோஸில்

பரிந்துரைக்கப்படுகிறது இந்த மாறிகளை உங்கள் `user` சூழல் மாறிகளாகச் சேர்க்க.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER]க்கு `User variables` > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- நீங்கள் இந்த சூழல் மாறிகளை உங்கள் PowerShell சுயவிவரத்தில் சேர்க்கலாம்.

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### லினக்ஸ் மற்றும் macOS இல்

பின்வரும் ஏற்றுதல்களை உங்கள் `~/.bashrc` அல்லது `~/.zshrc` கோப்பில் சேர்க்க பரிந்துரைக்கப்படுகிறது.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## தேவையான Python நூலகங்களை நிறுவுக

1. [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) இன்னும் நிறுவப்படவில்லை என்றால் இன்ஸ்டால் செய்யவும்.
1. `Terminal` சாளரத்திலிருந்து உங்கள் விருப்பமான சேமிப்பிடம் கோப்பகத்தில் மாதிரியைக் கிளோன் செய்யவும்.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` கோப்பகத்துக்கு செல்லவும்.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python க்கான மெய்நிகர் சூழலை உருவாக்கவும்.

    விண்டோஸில்:

    ```powershell
    python -m venv .venv
    ```

    macOS மற்றும் லினக்சில்:

    ```bash
    python3 -m venv .venv
    ```

1. Python மெய்நிகர் சூழலை செயல்படுத்தவும்.

   விண்டோஸில்:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS மற்றும் லினக்சில்:

   ```bash
   source .venv/bin/activate
   ```

1. தேவையான நூலகங்களை நிறுவவும்.

   விண்டோஸில்:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS மற்றும் லினக்சில்:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube எழுத்துப்பரிமாற்ற தரவு தயாரிப்பு ஸ்கிரிப்ட்களை இயக்குக

### விண்டோஸில்

```powershell
.\transcripts_prepare.ps1
```

### macOS மற்றும் லினக்சில்

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->