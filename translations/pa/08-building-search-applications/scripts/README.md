# ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡਾਟਾ ਤਿਆਰ ਕਰਨਾ

ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡਾਟਾ ਤਿਆਰ ਕਰਨ ਵਾਲੇ ਸਕ੍ਰਿਪਟ ਯੂਟਿਊਬ ਵੀਡੀਓ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟਸ ਡਾਊਨਲੋਡ ਕਰਦੇ ਹਨ ਅਤੇ ਇਹਨਾਂ ਨੂੰ Semantic Search with OpenAI Embeddings and Functions ਸੈਂਪਲ ਨਾਲ ਵਰਤੋਂ ਲਈ ਤਿਆਰ ਕਰਦੇ ਹਨ।

ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡਾਟਾ ਤਿਆਰ ਕਰਨ ਵਾਲੇ ਸਕ੍ਰਿਪਟ ਨਵੀਨਤਮ ਰਿਲੀਜ਼ਾਂ Windows 11, macOS Ventura ਅਤੇ Ubuntu 22.04 (ਅਤੇ ਉਪਰ) 'ਤੇ ਟੈਸਟ ਕੀਤੇ ਗਏ ਹਨ।

## ਲੋੜੀਂਦੇ Azure OpenAI Service ਸਰੋਤ ਬਣਾਓ

> [!IMPORTANT]
> ਅਸੀਂ ਤੁਹਾਨੂੰ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ ਕਿ ਤੁਸੀਂ OpenAI ਨਾਲ ਅਨੁਕੂਲਤਾ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ Azure CLI ਨੂੰ ਨਵੇਂ ਵਰਜਨ ਵਿੱਚ ਅਪਡੇਟ ਕਰੋ
> ਦੇਖੋ [ਦਸਤਾਵੇਜ਼](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. ਇੱਕ ਰਿਸੋਰਸ ਗਰੁੱਪ ਬਣਾਓ

> [!NOTE]
> ਇਨ੍ਹਾਂ ਹਿਦਾਇਤਾਂ ਲਈ ਅਸੀਂ "semantic-video-search" ਨਾਂ ਦਾ ਰਿਸੋਰਸ ਗਰੁੱਪ East US ਵਿੱਚ ਵਰਤ ਰਹੇ ਹਾਂ।
> ਤੁਸੀਂ ਰਿਸੋਰਸ ਗਰੁੱਪ ਦਾ ਨਾਂ ਬਦਲ ਸਕਦੇ ਹੋ, ਪਰ ਜਦੋਂ ਸਰੋਤਾਂ ਦੀ ਜਗ੍ਹਾ ਬਦਲਦੇ ਹੋ,
> ਤਾਂ [ਮਾਡਲ ਉਪਲਬਧਤਾ ਟੇਬਲ](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) ਦੀ ਜਾਂਚ ਕਰੋ।

```console
az group create --name semantic-video-search --location eastus
```

1. ਇੱਕ Azure OpenAI Service ਸਰੋਤ ਬਣਾਓ।

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ਇਸ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਵਰਤੋਂ ਲਈ ਐਂਡਪੌਇੰਟ ਅਤੇ ਕੁੰਜੀਆਂ ਪ੍ਰਾਪਤ ਕਰੋ

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. ਹੇਠ ਲਿਖੇ ਮਾਡਲ ਤਾਇਨਾਤ ਕਰੋ:
   - `text-embedding-ada-002` ਵਰਜਨ `2` ਜਾਂ ਵੱਧ, ਜਿਸਦਾ ਨਾਂ `text-embedding-ada-002` ਹੈ
   - `gpt-5-mini` ਜਿਸਦਾ ਨਾਂ `gpt-5-mini` ਹੈ

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

## ਲੋੜੀਂਦੀ ਸਾਫਟਵੇਅਰ

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ਜਾਂ ਵੱਧ

## ਵਾਤਾਵਰਣ ਪਰਿਵਰਤਨਸ਼ੀਲ

ਯੂਟਿਊਬ ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡਾਟਾ ਤਿਆਰ ਕਰਨ ਵਾਲੇ ਸਕ੍ਰਿਪਟ ਚਲਾਉਣ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਵਾਤਾਵਰਣ ਪਰਿਵਰਤਨਸ਼ੀਲ ਲੋੜੀਂਦੇ ਹਨ।

### Windows 'ਤੇ

ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਕਿ ਇਹ ਪਰਿਵਰਤਨਸ਼ੀਲ ਆਪਣੇ `user` ਵਾਤਾਵਰਣ ਪਰਿਵਰਤਨਸ਼ੀਲਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ।
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `[USER]` ਲਈ `User variables` > `New`।

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- ਤੁਸੀਂ ਇਹ ਵਾਤਾਵਰਣ ਪਰਿਵਰਤਨਸ਼ੀਲ ਆਪਣੇ PowerShell ਪ੍ਰੋਫਾਈਲ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰ ਸਕਦੇ ਹੋ।

```powershell
$env:AZURE_OPENAI_API_KEY = "<ਤੁਹਾਡਾ Azure OpenAI Service API ਕੁੰਜੀ>"
$env:AZURE_OPENAI_ENDPOINT = "<ਤੁਹਾਡਾ Azure OpenAI Service ਐਂਡਪੌਇੰਟ>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<ਤੁਹਾਡਾ Azure OpenAI Service ਮਾਡਲ ਤਾਇਨਾਤੀ ਨਾਂ>"
$env:GOOGLE_DEVELOPER_API_KEY = "<ਤੁਹਾਡਾ Google ਡਿਵੈਲਪਰ API ਕੁੰਜੀ>"
``` -->

### Linux ਅਤੇ macOS 'ਤੇ

ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਕਿ ਹੇਠਾਂ ਦਿੱਤੇ ਐਕਸਪੋਰਟ ਆਪਣੇ `~/.bashrc` ਜਾਂ `~/.zshrc` ਫਾਈਲ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ।

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## ਲੋੜੀਂਦੇ Python ਲਾਇਬ੍ਰੇਰੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ

1. [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ਇੰਸਟਾਲ ਕਰੋ ਜੇਕਰ ਪਹਿਲਾਂ ਇੰਸਟਾਲ ਨਹੀਂ ਹੈ।
1. ਇੱਕ `Terminal` ਵਿਂਡੋ ਤੋਂ ਸੈਂਪਲ ਨੂੰ ਆਪਣੀ ਪਸੰਦ ਦੇ ਰਿਪੋ ਫੋਲਡਰ ਵਿੱਚ ਕਲੋਨ ਕਰੋ।

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` ਫੋਲਡਰ ਵਿੱਚ ਜਾਓ।

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. ਇੱਕ Python ਵਰਚੁਅਲ ਅਵਰਨਾਰਨਮੈਂਟ ਬਣਾਓ।

    Windows 'ਤੇ:

    ```powershell
    python -m venv .venv
    ```

    macOS ਅਤੇ Linux 'ਤੇ:

    ```bash
    python3 -m venv .venv
    ```

1. Python ਵਰਚੁਅਲ ਅਵਰਨਾਰਨਮੈਂਟ ਐਕਟੀਵੇਟ ਕਰੋ।

   Windows 'ਤੇ:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS ਅਤੇ Linux 'ਤੇ:

   ```bash
   source .venv/bin/activate
   ```

1. ਲੋੜੀਂਦੀਆਂ ਲਾਇਬ੍ਰੇਰੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ।

   Windows 'ਤੇ:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS ਅਤੇ Linux 'ਤੇ:

   ```bash
   pip3 install -r requirements.txt
   ```

## ਯੂਟਿਊਬ ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡਾਟਾ ਤਿਆਰ ਕਰਨ ਵਾਲੇ ਸਕ੍ਰਿਪਟ ਚਲਾਓ

### Windows 'ਤੇ

```powershell
.\transcripts_prepare.ps1
```

### macOS ਅਤੇ Linux 'ਤੇ

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->