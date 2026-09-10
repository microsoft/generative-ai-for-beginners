# உரைமாற்று தரவு தயார்

உரைமாற்று தரவு தயார் ஸ்கிரிப்ட்கள் YouTube வீடியோ உரைகளை 다운로드 செய்து, Semantic Search with OpenAI Embeddings and Functions மாதிரிக்கான பயன்பாட்டிற்கு தயாரிக்கின்றன.

உரைமாற்று தரவு தயார் ஸ்கிரிப்ட்கள் Windows 11, macOS Ventura மற்றும் Ubuntu 22.04 (மற்றும் மேலதிக பதிப்புகள்) சமீபத்திய வெளியீடுகளில் பரிசோதிக்கப்பட்டுள்ளன.

## தேவையான Azure OpenAI சேவை வளங்களை உருவாக்கவும்

> [!IMPORTANT]
> OpenAI உடன் இணக்கமாக இருப்பதற்காக Azure CLI ஐ சமீபத்திய பதிப்பிற்கு புதுப்பிப்பதை நாம் பரிந்துரைக்கிறோம்
> [டாக்குமென்டேஷன்](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) ஐ பார்க்கவும்

1. ஒரு Resource group ஐ உருவாக்கவும்

> [!NOTE]
> இந்த வழிமுறைகளில் East US இல் உள்ள "semantic-video-search" என்ற resource group பயன்படுத்தப்படுகிறது.
> resource group பெயரை மாற்றிக்கொள் முடியும், ஆனால் வளங்களுக்கான இடத்தை மாற்றும்போது, 
> [மாதிரி கிடைக்கும் அட்டவணை](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) を சரிபார்க்கவும்.

```console
az group create --name semantic-video-search --location eastus
```

1. ஒரு Azure OpenAI சேவை வளத்தை உருவாக்கு.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. இந்த பயன்பாட்டில் பயன்படுத்துவதற்கான எண்ட்பாயிண்ட் மற்றும் விசைகள் பெறவும்

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. கீழ்கண்ட மாதிரிகளை இயக்கவும்:
   - `text-embedding-ada-002` பதிப்பு `2` அல்லது அதற்கு மேற்பட்டது, `text-embedding-ada-002` என பெயரிடப்பட்டது
   - `gpt-5-mini` `gpt-5-mini` என பெயரிடப்பட்டது

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

## தேவையான மென்பொருள்

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) அல்லது அதற்கு மேற்பட்ட பதிப்பு

## சுற்றுச்சூழல் மாறிகள்

YouTube உரைமாற்று தரவு தயாரிக்கும் ஸ்கிரிப்ட்களை இயக்க தேவையான சுற்றுச்சூழல் மாறிகள் பின்வருமாறு உள்ளன.

### விண்டோஸ் இயங்குதளத்தில்

உங்கள் `user` சுற்றுச்சூழல் மாறிகளில் இவ்வாறாக சேர்க்க பரிந்துரைக்கப்படுகிறது.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER] க்கான `User variables` > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- நீங்கள் உங்கள் PowerShell ப்ரொஃபைலிலும் சுற்றுச்சூழல் மாறிகளைச் சேர்க்கலாம்.

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### லினக்ஸ் மற்றும் macOS இல்

பின்வரும் எக்ஸ்போர்ட்களை உங்கள் `~/.bashrc` அல்லது `~/.zshrc` கோப்பில் சேர்க்க பரிந்துரைக்கப்படுகிறது.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## தேவையான Python நூலகங்களை நிறுவுக

1. [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) கணிணியில் இல்லை என்றால் நிறுவுக.
1. `Terminal` சாளரை திறந்து மாதிரியை உங்கள் விருப்பமான நிரலுணமை கோப்புறையில் கிளோன் செய்வதற்காக.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` கோப்புறைக்கு செல்லவும்.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python மெய்நிகர் சுற்றுச்சூழலை உருவாக்கவும்.

    விண்டோஸில்:

    ```powershell
    python -m venv .venv
    ```

    macOS மற்றும் லினக்ஸில்:

    ```bash
    python3 -m venv .venv
    ```

1. Python மெய்நிகர் சுற்றுச்சூழலை செயல்படுத்தவும்.

   விண்டோஸில்:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS மற்றும் லினக்ஸில்:

   ```bash
   source .venv/bin/activate
   ```

1. தேவையான நூலகங்களை நிறுவவும்.

   விண்டோஸில்:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS மற்றும் லினக்ஸில்:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube உரைமாற்று தரவு தயார் ஸ்கிரிப்ட்களை இயக்கவும்

### விண்டோஸில்

```powershell
.\transcripts_prepare.ps1
```

### macOS மற்றும் லினக்ஸில்

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->