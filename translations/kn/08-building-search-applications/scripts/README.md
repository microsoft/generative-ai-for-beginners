# ಟ್ರಾನ್ಸ್ಕ್ರಿಪ್ಷನ್ ಡೇಟಾ ತಯಾರಿ

ಟ್ರಾನ್ಸ್ಕ್ರಿಪ್ಷನ್ ಡೇಟಾ ತಯಾರಿ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳು YouTube ವೀಡಿಯೊ ಟ್ರಾನ್ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ Semantic Search with OpenAI Embeddings and Functions ಮಾದರಿಗಾಗಿ ಬಳಸಲು ಸಿದ್ಧಪಡಿಸುತ್ತವೆ.

ಟ್ರಾನ್ಸ್ಕ್ರಿಪ್ಷನ್ ಡೇಟಾ ತಯಾರಿ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳನ್ನು ಇತ್ತೀಚಿನ ಬಿಡುಗಡೆಗಳಾದ Windows 11, macOS Ventura ಮತ್ತು Ubuntu 22.04 (ಮತ್ತು ಮೇಲಿನ) ಮೇಲೆ ಪರೀಕ್ಷಿಸಲಾಗಿದೆ.

## ಅಗತ್ಯವಿರುವ Azure OpenAI ಸೇವಾ ಸಂಪನ್ಮೂಲಗಳನ್ನು ರಚಿಸಿ

> [!IMPORTANT]
> OpenAI ಜೊತೆಗೆ ಹೊಂದಾಣಿಕೆಗೆ ಖಚಿತಪಡಿಸಲು ನಾವು ನಿಮಗೆ Azure CLI ಅನ್ನು ಇತ್ತೀಚಿನ ಆವೃತ್ತಿಗೆ ನವೀಕರಿಸಲು ಸಲಹೆ ನೀಡುತ್ತೇವೆ
> [ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) ನೋಡಿ

1. ಒಂದು ರಿಸೋರ್ಸ್ ಗ್ರೂಪ್ ರಚಿಸಿ

> [!NOTE]
> ಈ ಸೂಚನೆಗಳಿಗೆ ನಾವು "semantic-video-search" ಎಂಬ ರಿಸೋರ್ಸ್ ಗ್ರೂಪ್ ಅನ್ನು East US ನಲ್ಲಿ ಬಳಸುತ್ತಿದ್ದೇವೆ.
> ನೀವು ರಿಸೋರ್ಸ್ ಗ್ರೂಪ್ ಹೆಸರನ್ನು ಬದಲಾಯಿಸಬಹುದು, ಆದರೆ ಸಂಪನ್ಮೂಲಗಳ ಸ್ಥಳವನ್ನು ಬದಲಾಯಿಸುವಾಗ,
> [ಮಾದರಿ ಲಭ್ಯತೆ ಟೇಬಲ್](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) ಪರಿಶೀಲಿಸಿ.

```console
az group create --name semantic-video-search --location eastus
```

1. ಒಂದು Azure OpenAI ಸೇವಾ ಸಂಪನ್ಮೂಲವನ್ನು ರಚಿಸಿ.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ಈ ಅಪ್ಲಿಕೇಶನ್‌ನಲ್ಲಿ ಬಳಕೆಗಾಗಿ ಎಂಡ್ಪಾಯಿಂಟ್ ಮತ್ತು ಕೀಗಳನ್ನು ಪಡೆಯಿರಿ

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. ಕೆಳಗಿನ ಮಾದರಿಗಳನ್ನು ನಿಯೋಜಿಸಿ:
   - `text-embedding-ada-002` ಆವೃತ್ತಿ `2` ಅಥವಾ ಹೆಚ್ಚಿನದು, ಹೆಸರಿಸಲಾಗಿದೆ `text-embedding-ada-002`
   - `gpt-35-turbo` ಆವೃತ್ತಿ `0613` ಅಥವಾ ಹೆಚ್ಚಿನದು, ಹೆಸರಿಸಲಾಗಿದೆ `gpt-35-turbo`

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

## ಅಗತ್ಯವಿರುವ ಸಾಫ್ಟ್‌ವೇರ್

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ಅಥವಾ ಹೆಚ್ಚಿನದು

## ಪರಿಸರ ಚರಗಳು

YouTube ಟ್ರಾನ್ಸ್ಕ್ರಿಪ್ಷನ್ ಡೇಟಾ ತಯಾರಿ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳನ್ನು ಚಾಲನೆ ಮಾಡಲು ಕೆಳಗಿನ ಪರಿಸರ ಚರಗಳು ಅಗತ್ಯವಿವೆ.

### ವಿಂಡೋಸ್‌ನಲ್ಲಿ

ನಿಮ್ಮ `user` ಪರಿಸರ ಚರಗಳಿಗೆ ಈ ಚರಗಳನ್ನು ಸೇರಿಸುವುದನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER] ಗೆ `User variables` > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- ನೀವು ನಿಮ್ಮ PowerShell ಪ್ರೊಫೈಲ್‌ಗೆ ಪರಿಸರ ಚರಗಳನ್ನು ಸೇರಿಸಬಹುದು.

```powershell
$env:AZURE_OPENAI_API_KEY = "<ನಿಮ್ಮ Azure OpenAI ಸೇವಾ API ಕೀ>"
$env:AZURE_OPENAI_ENDPOINT = "<ನಿಮ್ಮ Azure OpenAI ಸೇವಾ ಎಂಡ್ಪಾಯಿಂಟ್>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<ನಿಮ್ಮ Azure OpenAI ಸೇವಾ ಮಾದರಿ ನಿಯೋಜನೆ ಹೆಸರು>"
$env:GOOGLE_DEVELOPER_API_KEY = "<ನಿಮ್ಮ Google ಡೆವಲಪರ್ API ಕೀ>"
``` -->

### ಲಿನಕ್ಸ ಮತ್ತು macOS ನಲ್ಲಿ

ನಿಮ್ಮ `~/.bashrc` ಅಥವಾ `~/.zshrc` ಫೈಲ್‌ಗೆ ಕೆಳಗಿನ ಎಕ್ಸ್ಪೋರ್ಟ್‌ಗಳನ್ನು ಸೇರಿಸುವುದನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## ಅಗತ್ಯವಿರುವ Python ಲೈಬ್ರರಿಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

1. [git ಕ್ಲೈಂಟ್](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ಈಗಾಗಲೇ ಸ್ಥಾಪಿತವಾಗಿಲ್ಲದಿದ್ದರೆ ಅದನ್ನು ಸ್ಥಾಪಿಸಿ.
1. `Terminal` ವಿಂಡೋದಿಂದ, ಮಾದರಿಯನ್ನು ನಿಮ್ಮ ಇಚ್ಛಿತ ರೆಪೋ ಫೋಲ್ಡರ್‌ಗೆ ಕ್ಲೋನ್ ಮಾಡಿ.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` ಫೋಲ್ಡರ್‌ಗೆ ನವಿಗೇಟ್ ಮಾಡಿ.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ರಚಿಸಿ.

    ವಿಂಡೋಸ್‌ನಲ್ಲಿ:

    ```powershell
    python -m venv .venv
    ```

    macOS ಮತ್ತು ಲಿನಕ್ಸ್ನಲ್ಲಿ:

    ```bash
    python3 -m venv .venv
    ```

1. Python ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ.

   ವಿಂಡೋಸ್‌ನಲ್ಲಿ:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS ಮತ್ತು ಲಿನಕ್ಸ್ನಲ್ಲಿ:

   ```bash
   source .venv/bin/activate
   ```

1. ಅಗತ್ಯವಿರುವ ಲೈಬ್ರರಿಗಳನ್ನು ಸ್ಥಾಪಿಸಿ.

   ವಿಂಡೋಸ್‌ನಲ್ಲಿ:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS ಮತ್ತು ಲಿನಕ್ಸ್ನಲ್ಲಿ:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ಟ್ರಾನ್ಸ್ಕ್ರಿಪ್ಷನ್ ಡೇಟಾ ತಯಾರಿ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳನ್ನು ಚಾಲನೆ ಮಾಡಿ

### ವಿಂಡೋಸ್‌ನಲ್ಲಿ

```powershell
.\transcripts_prepare.ps1
```

### macOS ಮತ್ತು ಲಿನಕ್ಸ್ನಲ್ಲಿ

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->