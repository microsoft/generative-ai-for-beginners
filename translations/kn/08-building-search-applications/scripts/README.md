# ಲಿಪ್ಯಂತರಣ ಡೇಟಾ ಸಿದ್ಧತೆ

ಲಿಪ್ಯಂತರಣ ಡೇಟಾ ಸಿದ್ಧತೆ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳು YouTube ವೀಡಿಯೊ ಲಿಪ್ಯಂತರಣಗಳನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ Semantic Search with OpenAI Embeddings and Functions ಮಾದರಿಗಾಗಿ ಬಳಸಲು ಸಿದ್ಧಪಡಿಸುತ್ತವೆ.

ಲಿಪ್ಯಂತರಣ ಡೇಟಾ ಸಿದ್ಧತೆ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳನ್ನು Windows 11, macOS Ventura ಮತ್ತು Ubuntu 22.04 (ಮತ್ತು ಮೇಲ್ಪಟ್ಟಿರುವ) ಇತ್ತೀಚಿನ ಬಿಡುಗಡೆಯ ಮೇಲೆ ಪರೀಕ್ಷಿಸಲಾಗಿದೆ.

## ಅಗತ್ಯವಿರುವ Azure OpenAI ಸೇವಾ ಸಂಪನ್ಮೂಲಗಳನ್ನು ಸೃಷ್ಟಿಸಿ

> [!IMPORTANT]
> OpenAI ಜೊತೆ ಹೊಂದಾಣಿಕೆಯನ್ನು ಖಚಿತಪಡಿಸಲು ಸ್ವಲ್ಪಮಾಡಿದ Azure CLI ನವೀಕರಿಸುವುದನ್ನು ನಾವು ಶಿಫಾರಸು ಮಾಡುತ್ತೇವೆ
> [ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) ನೋಡಿ

1. ಒಂದು ಸಂಪನ್ಮೂಲ ಗುಂಪು ಸೃಷ್ಟಿಸಿ

> [!NOTE]
> ಈ ಸೂಚನೆಗಳಲ್ಲಿ, ನಾವು East US ನಲ್ಲಿ "semantic-video-search" ಎನ್ನುವ ಸಂಪನ್ಮೂಲ ಗುಂಪನ್ನು ಬಳಕೆ ಮಾಡುತ್ತಿದ್ದೇವೆ.
> ನೀವು ಸಂಪನ್ಮೂಲ ಗುಂಪಿನ ಹೆಸರನ್ನು ಬದಲಾಯಿಸಬಹುದು, ಆದರೆ ಸಂಪನ್ಮೂಲಗಳ ಸ್ಥಳವನ್ನು ಬದಲಿಸುವಾಗ
> [ಮಾದರಿ ಲಭ್ಯತೆಯ ಪಟ್ಟಿಯನ್ನು](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) ಪರಿಶೀಲಿಸಿ.

```console
az group create --name semantic-video-search --location eastus
```

1. ಒಂದು Azure OpenAI ಸೇವಾ ಸಂಪನ್ಮೂಲವನ್ನು ಸೃಷ್ಟಿಸಿ.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ಈ ಅಪ್ಲಿಕೇಶನ್‌ನಲ್ಲಿ ಉಪಯೋಗಿಸಲು ಎಂಡ್ಪಾಯಿಂಟ್ ಮತ್ತು ಕೀಗಳನ್ನು ಪಡೆಯಿರಿ

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. ಕೆಳಗಿನ ಮಾದರಿಗಳನ್ನು ನಿಯೋಜಿಸಿ:
   - `text-embedding-ada-002` ಆವೃತ್ತಿ `2` ಅಥವಾ ಮೇಲ್ಪಟ್ಟಿರುವ, `text-embedding-ada-002` ಎಂದು ಹೆಸರು ಮಾಡಲಾಗಿದೆ
   - `gpt-4o-mini` ಎಂದು ಹೆಸರು ಮಾಡಲಾಗಿದೆ `gpt-4o-mini`

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

## ಅಗತ್ಯವಿರುವ ಸಾಫ್ಟ್‌ವೇರ್

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ಅಥವಾ ಮೇಲ್ಪಟ್ಟಿರುವ

## ಪರಿಸರ ಚರಗಳು

YouTube ಲಿಪ್ಯಂತರಣ ಡೇಟಾ ಸಿದ್ಧತೆ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳನ್ನು ಚಾಲನೆ ಮಾಡುವ uchun ಕೆಳಗಿನ ಪರಿಸರ ಚರಗಳು ಅಗತ್ಯ.

### વિન્ડೋಸ್ ಮೇಲೆ

ನಿಮ್ಮ `user` ಪರಿಸರ ಚರಗಳಿಗೆ ವ್ಯತ್ಯಾಸಗಳನ್ನು ಸೇರಿಸಲು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ.
`Windows ಪ್ರಾರಂಭ` > `ಸಿಸ್ಟಂ ಪರಿಸರ ಚರಗಳನ್ನು ಸಂಪಾದಿಸಿ` > `ಪರಿಸರ ಚರಗಳು` > `[USER]`ಗಾಗಿ ಬಳಕೆದಾರ ಚರಗಳು > `ಹೊಸದು`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- ನೀವು ನಿಮ್ಮ PowerShell ಪ್ರೊಫೈಲ್‌ಗೆ ಪರಿಸರ ಚರಗಳನ್ನು ಸೇರಿಸಬಹುದು.

```powershell
$env:AZURE_OPENAI_API_KEY = "<ನಿಮ್ಮ Azure OpenAI ಸೇವೆ API ಕೀ>"
$env:AZURE_OPENAI_ENDPOINT = "<ನಿಮ್ಮ Azure OpenAI ಸೇವೆ ಎಂಡ್ಪಾಯಿಂಟ್>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<ನಿಮ್ಮ Azure OpenAI ಸೇವೆ ಮಾದರಿ ನಿಯೋಜನೆ ಹೆಸರು>"
$env:GOOGLE_DEVELOPER_API_KEY = "<ನಿಮ್ಮ Google ಅಭಿವೃದ್ಧಿ API ಕೀ>"
``` -->

### ಲಿನಕ್ಸ ಮತ್ತು macOS ನಲ್ಲಿ

ನಿಮ್ಮ `~/.bashrc` ಅಥವಾ `~/.zshrc` ಫೈಲಿನಲ್ಲಿ ಕೆಳಗಿನ ರಫ್ತುಗಳನ್ನು ಸೇರಿಸಲು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## ಅಗತ್ಯವಿರುವ Python ಲೈಬ್ರರಿಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

1. [git ಕ್ಲೈಂಟ್](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ಇಷ್ಟಿಲ್ಲದಿದ್ದರೆ ಅದನ್ನು ಸ್ಥಾಪಿಸಿ.
1. `ಟರ್ಮಿನಲ್` ಕಿಟಕಿಯಿಂದ, ಮಾದರಿಯನ್ನು ನಿಮ್ಮ ಇಚ್ಚಿತ ರೆಪೋ ಫೋಲ್ಡರ್‌ಗೆ ಕ್ಲೋನ್ ಮಾಡಿ.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` ಫೋಲ್ಡರ್‌ಗೆ ಹೋಗಿ.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ರಚಿಸಿ.

    Windows ನಲ್ಲಿ:

    ```powershell
    python -m venv .venv
    ```

    macOS ಮತ್ತು ಲಿನಕ್ಸಿನಲ್ಲಿ:

    ```bash
    python3 -m venv .venv
    ```

1. Python ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ.

   Windows ನಲ್ಲಿ:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS ಮತ್ತು ಲಿನಕ್ಸಿನಲ್ಲಿ:

   ```bash
   source .venv/bin/activate
   ```

1. ಅಗತ್ಯವಿರುವ ಲೈಬ್ರರಿಗಳನ್ನು ಸ್ಥಾಪಿಸಿ.

   Windows ನಲ್ಲಿ:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS ಮತ್ತು ಲಿನಕ್ಸಿನಲ್ಲಿ:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ಲಿಪ್ಯಂತರಣ ಡೇಟಾ ಸಿದ್ಧತೆ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳನ್ನು ನೆರವೇರಿಸಿ

### Windows ನಲ್ಲಿ

```powershell
.\transcripts_prepare.ps1
```

### macOS ಮತ್ತು ಲಿನಕ್ಸಿನಲ್ಲಿ

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->