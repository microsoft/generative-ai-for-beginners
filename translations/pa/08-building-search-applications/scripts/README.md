# ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡੇਟਾ ਤਿਆਰੀ

ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡੇਟਾ ਤਿਆਰੀ ਸਕ੍ਰਿਪਟ YouTube ਵੀਡੀਓ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਡਾਊਨਲੋਡ ਕਰਦੀਆਂ ਹਨ ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ OpenAI ਐਮਬੈੱਡਿੰਗ ਅਤੇ ਫੰਕਸ਼ਨਸ ਦੇ ਨਾਲ Semantic Search ਦੇ ਨਮੂਨੇ ਲਈ ਤਿਆਰ ਕਰਦੀਆਂ ਹਨ।

ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡੇਟਾ ਤਿਆਰੀ ਸਕ੍ਰਿਪਟਾਂ ਨੂੰ ਨਵੀਆਂ ਰਿਲੀਜ਼ਾਂ Windows 11, macOS Ventura ਅਤੇ Ubuntu 22.04 (ਅਤੇ ਉੱਪਰ) 'ਤੇ ਟੈਸਟ ਕੀਤਾ ਗਿਆ ਹੈ।

## ਲੋੜੀਂਦੇ Azure OpenAI ਸਰਵਿਸ ਸਾਧਨ ਬਣਾਓ

> [!IMPORTANT]
> ਅਸੀਂ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ ਕਿ ਤੁਸੀਂ OpenAI ਨਾਲ ਸੁਮੇਲਤਾ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ Azure CLI ਨੂੰ ਨਵੀਂ ਵਰਜਨ 'ਤੇ ਅੱਪਡੇਟ ਕਰੋ
> ਵੇਖੋ [ਡੌਕਯੂਮੇਂਟੇਸ਼ਨ](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. ਏਕ ਰਿਸੋਰਸ ਗਰੁੱਪ ਬਣਾਓ

> [!NOTE]
> ਇਹਨਾਂ ਹਦਾਇਤਾਂ ਲਈ ਅਸੀਂ East US ਵਿੱਚ "semantic-video-search" ਨਾਮਕ ਰਿਸੋਰਸ ਗਰੁੱਪ ਵਰਤ ਰਹੇ ਹਾਂ।
> ਤੁਸੀਂ ਰਿਸੋਰਸ ਗਰੁੱਪ ਦਾ ਨਾਮ ਬਦਲ ਸਕਦੇ ਹੋ, ਪਰ ਜਦੋਂ ਤੁਸੀਂ ਸਾਧਨਾਂ ਦੀ ਥਾਂ ਬਦਲਦੇ ਹੋ,
> ਤਾਂ [ਮਾਡਲ ਉਪਲਬਧਤਾ ਟੇਬਲ](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਵੇਖੋ।

```console
az group create --name semantic-video-search --location eastus
```

1. ਇੱਕ Azure OpenAI ਸਰਵਿਸ ਸਾਧਨ ਬਣਾਓ।

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ਇਸ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਵਰਤੋਂ ਲਈ ਐਂਡਪੁਆਇੰਟ ਅਤੇ ਕੁੰਜੀਆਂ ਪ੍ਰਾਪਤ ਕਰੋ

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. ਹੇਠਾਂ ਦਿੱਤੇ ਮਾਡਲ ਤਾਇਨਾਤ ਕਰੋ:
   - `text-embedding-ada-002` ਵਰਜਨ `2` ਜਾਂ ਵੱਧ, ਜਿਸਨੂੰ `text-embedding-ada-002` ਨਾਮ ਦਿੱਤਾ ਗਿਆ ਹੈ
   - `gpt-4o-mini` ਜਿਸਨੂੰ `gpt-4o-mini` ਨਾਮ ਦਿੱਤਾ ਗਿਆ ਹੈ

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

## ਲੋੜੀਂਦਾ ਸਾਫਟਵੇਅਰ

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ਜਾਂ ਵੱਧ

## ਮਾਹੌਲੀਆ ਵੈਰੀਏਬਲ

YouTube ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡੇਟਾ ਤਿਆਰੀ ਸਕ੍ਰਿਪਟ ਚਲਾਉਣ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਮਾਹੌਲੀਆ ਵੈਰੀਏਬਲ ਲੋੜੀਂਦੇ ਹਨ।

### ਵਿੰਡੋਜ਼ 'ਤੇ

ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਕਿ ਤੁਸੀਂ ਇਹ ਵੈਰੀਏਬਲ ਆਪਣੇ `user` ਮਾਹੌਲ ਵੈਰੀਏਬਲਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ।
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `[USER]` ਲਈ `User variables` > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- ਤੁਸੀਂ ਇਹ ਮਾਹੌਲ ਵੈਰੀਏਬਲ ਆਪਣੇ PowerShell ਪ੍ਰੋਫਾਈਲ ਵਿੱਚ ਵੀ ਜੋੜ ਸਕਦੇ ਹੋ।

```powershell
$env:AZURE_OPENAI_API_KEY = "<ਤੁਹਾਡੀ Azure OpenAI ਸਰਵਿਸ API ਕੁੰਜੀ>"
$env:AZURE_OPENAI_ENDPOINT = "<ਤੁਹਾਡਾ Azure OpenAI ਸਰਵਿਸ ਐਂਡਪੁਆਇੰਟ>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<ਤੁਹਾਡਾ Azure OpenAI ਸਰਵਿਸ ਮਾਡਲ ਤਾਇਨਾਤੀ ਨਾਮ>"
$env:GOOGLE_DEVELOPER_API_KEY = "<ਤੁਹਾਡੀ ਗੂਗਲ ਡਿਵੈਲਪਰ API ਕੁੰਜੀ>"
``` -->

### ਲਿਨਕਸ ਅਤੇ macOS 'ਤੇ

ਸੋਝੀਦਾਰੀ ਹੈ ਕਿ ਤੁਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਨਿਰਯਾਤ ਆਪਣੇ `~/.bashrc` ਜਾਂ `~/.zshrc` ਫਾਈਲ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ।

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## ਲੋੜੀਂਦੀਆਂ Python ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਸਟਾਲ ਕਰੋ

1. ਜੇ ਨਹੀਂ ਕੀਤਾ ਤੁਸੀਂ [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ਇੰਸਟਾਲ ਕਰੋ।
1. ਇੱਕ `Terminal` ਵਿੰਡੋ ਤੋਂ, ਨਮੂਨਾ ਆਪਣੇ ਮਨਪਸੰਦ ਰੇਪੋ ਫੋਲਡਰ ਵਿੱਚ ਕਲੋਨ ਕਰੋ।

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` ਫੋਲਡਰ ਵਿੱਚ ਜਾਓ।

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. ਇੱਕ Python ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ।

    ਵਿੰਡੋਜ਼ 'ਤੇ:

    ```powershell
    python -m venv .venv
    ```

    macOS ਅਤੇ ਲਿਨਕਸ 'ਤੇ:

    ```bash
    python3 -m venv .venv
    ```

1. Python ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਸਰਗਰਮ ਕਰੋ।

   ਵਿੰਡੋਜ਼ 'ਤੇ:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS ਅਤੇ ਲਿਨਕਸ 'ਤੇ:

   ```bash
   source .venv/bin/activate
   ```

1. ਲੋੜੀਂਦੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਸਟਾਲ ਕਰੋ।

   ਵਿੰਡੋਜ਼ 'ਤੇ:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS ਅਤੇ ਲਿਨਕਸ 'ਤੇ:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡੇਟਾ ਤਿਆਰੀ ਸਕ੍ਰਿਪਟਾਂ ਚਲਾਓ

### ਵਿੰਡੋਜ਼ 'ਤੇ

```powershell
.\transcripts_prepare.ps1
```

### macOS ਅਤੇ ਲਿਨਕਸ 'ਤੇ

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->