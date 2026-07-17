# ಲಿಪ್ಯಂತರಣ ಡೇಟಾ ತಯಾರಿ

ಲಿಪ್ಯಂತರಣ ಡೇಟಾ ತಯಾರಿ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳು YouTube ವಿಡಿಯೋ ಲಿಪ್ಯಂತರಗಳನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡುತ್ತವೆ ಮತ್ತು ಅವನ್ನು OpenAI ಅಂಟಿಕೆಗಳೊಂದಿಗೆ ಸೆಮಾಂಟಿಕ್ ಸರ್ಚ್ ಮತ್ತು ಕ್ರಿಯೆಗಳ ಉದಾಹರಣೆಯಲ್ಲಿ ಬಳಕೆಗೆ ತಯಾರಿಸುತ್ತವೆ.

ಲಿಪ್ಯಂತರಣ ಡೇಟಾ ತಯಾರಿ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳಿಗೆ ಇತ್ತೀಚಿನ ಬಿಡುಗಡೆಯಾದ Windows 11, macOS Ventura ಮತ್ತು Ubuntu 22.04 (ಮತ್ತು ಮೇಲಕರು) ಮೇಲೆ ಪರೀಕ್ಷಿಸಲಾಗಿದೆ.

## ಅಗತ್ಯವಿರುವ Azure OpenAI ಸೇವೆ ಸಂಪನ್ಮೂಲಗಳನ್ನು ರಚಿಸಿ

> [!IMPORTANT]
> OpenAI ಸಹಕಾರಕ್ಕಾಗಿ ಖಚಿತತೆ ಮಾಡಿಕೊಳ್ಳಲು Azure CLI ಅನ್ನು ಇತ್ತೀಚಿನ ಆವೃತ್ತಿಗೆ ನವಿಕರಿಸಲು ನಾವು ಸಲಹೆ ನೀಡುತ್ತೇವೆ
> [ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) ನೋಡಿ

1. ಒಂದು ಸಂಪನ್ಮೂಲ ಗುಂಪನ್ನು ರಚಿಸಿ

> [!NOTE]
> ಈ ಸೂಚನೆಗಳಿಗೆ ನಾವು "semantic-video-search" ಎನ್ನುವ ಹೆಸರಿನ ಸಂಪನ್ಮೂಲ ಗುಂಪನ್ನು ಈಸ್ಟ್ ಯುಎಸ್ ನಲ್ಲಿ ಬಳಸುತ್ತಿದ್ದೇವೆ.
> ಸಂಪನ್ಮೂಲಗಳ ಸ್ಥಾನವನ್ನು ಬದಲಾಯಿಸುವಾಗ, ನೀವು ಸಂಪನ್ಮೂಲ ಗುಂಪಿನ ಹೆಸರನ್ನು ಬದಲಾಯಿಸಬಹುದು,
> [ಮಾದರಿ ಲಭ್ಯತೆ ಫಲಕ](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) ಅನ್ನು ಪರಿಶೀಲಿಸಿ.

```console
az group create --name semantic-video-search --location eastus
```

1. ಒಂದು Azure OpenAI ಸೇವೆ ಸಂಪನ್ಮೂಲವನ್ನು ರಚಿಸಿ.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ಈ ಅಪ್ಲಿಕೇಶನ್‌ನಲ್ಲಿ ಬಳಕೆಗೆ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಮತ್ತು ಕೀಗಳನ್ನು ಪಡೆಯಿರಿ

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. ಕೆಳಗಿನ ಮಾದರಿಗಳನ್ನು ನಿಯೋಜಿಸಿ:
   - `text-embedding-ada-002` ಸಂಸ್ಕರಣಾ `2` ಅಥವಾ ಹಿರಿಯ, ಹೆಸರು `text-embedding-ada-002`
   - `gpt-5-mini` ಹೆಸರು `gpt-5-mini`

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

## ಅಗತ್ಯವಿರುವ ಸಾಫ್ಟ್‌ವೇರ್

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ಅಥವಾ ಮೇಲಿನ ಆವೃತ್ತಿ

## ಪರಿಸರ ವ್ಯತ್ಯاسಗಳು

YouTube ಲಿಪ್ಯಂತರಣ ಡೇಟಾ ತಯಾರಿ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳನ್ನು ಚಾಲನೆ ಮಾಡಲು ಕೆಳಗಿನ ಪರಿಸರ ವ್ಯತ್ಯಾಸಗಳು ಅಗತ್ಯವಿದ್ದು.

### ವಿಂಡೋಸ್ ನಲ್ಲಿ

ನಿಮ್ಮ `user` ಪರಿಸರ ವ್ಯತ್ಯಾಸಗಳಲ್ಲಿ ವ್ಯತ್ಯಾಸಗಳನ್ನು ಸೇರಿಸುವುದು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER] ಗೆ `User variables` > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- ನೀವು ನಿಮ್ಮ PowerShell ಪ್ರೊಫೈಲ್‌ಗೆ ಪರಿಸರ ವ್ಯತ್ಯಾಸಗಳನ್ನು ಸೇರಿಸಬಹುದು.

```powershell
$env:AZURE_OPENAI_API_KEY = "<ನಿಮ್ಮ Azure OpenAI ಸರ್ವಿಸ್ API ಕೀ>"
$env:AZURE_OPENAI_ENDPOINT = "<ನಿಮ್ಮ Azure OpenAI ಸರ್ವಿಸ್ ಎಂಡ್ ಪಾಯಿಂಟ್>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<ನಿಮ್ಮ Azure OpenAI ಸರ್ವಿಸ್ ಮಾದರಿ ನಿಯೋಜನೆ ಹೆಸರು>"
$env:GOOGLE_DEVELOPER_API_KEY = "<ನಿಮ್ಮ Google ಡೆವಲಪರ್ API ಕೀ>"
``` -->

### ಲಿನಕ್ಸ ಮತ್ತು macOS ನಲ್ಲಿ

ಕೆಳಗಿನ ರಫ್ತಿಗಳನ್ನು ನಿಮ್ಮ `~/.bashrc` ಅಥವಾ `~/.zshrc` ಫೈಲ್ ಗೆ ಸೇರಿಸಲು ಶಿಫಾರಸು ಮಾಡುತ್ತದೆ.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## ಅಗತ್ಯ Python ಗ್ರಂಥಾಲಯಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

1. ನೀವು ಈಗಾಗಲೇ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡದಿದ್ದರೆ [git ಕ್ಲೈಂಟ್](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ಅನ್ನು ಸ್ಥಾಪಿಸಿ.
1. `Terminal` ಕಿಟಕಿಯಿಂದ, ನಿಮ್ಮ ಇಚ್ಛಿತ ರೆಪೋ ಫೋಲ್ಡರ್‌ಗೆ ಉದಾಹರಣೆಯನ್ನು ಕ್ಲೋನ್ ಮಾಡಿ.

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

1. ಅಗತ್ಯವಿರುವ ಗ್ರಂಥಾಲಯಗಳನ್ನು ಸ್ಥಾಪಿಸಿ.

   ವಿಂಡೋಸ್‌ನಲ್ಲಿ:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS ಮತ್ತು ಲಿನಕ್ಸ್ನಲ್ಲಿ:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ಲಿಪ್ಯಂತರಣ ಡೇಟಾ ತಯಾರಿ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳನ್ನು ರನ್ ಮಾಡಿ

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
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->