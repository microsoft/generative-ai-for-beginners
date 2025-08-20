<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:09:01+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "pa"
}
-->
# ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡੇਟਾ ਤਿਆਰੀ

ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡੇਟਾ ਤਿਆਰੀ ਸਕ੍ਰਿਪਟ ਯੂਟਿਊਬ ਵੀਡੀਓ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਡਾਊਨਲੋਡ ਕਰਦੀਆਂ ਹਨ ਅਤੇ Semantic Search with OpenAI Embeddings and Functions ਸੈਂਪਲ ਨਾਲ ਵਰਤੋਂ ਲਈ ਤਿਆਰ ਕਰਦੀਆਂ ਹਨ।

ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡੇਟਾ ਤਿਆਰੀ ਸਕ੍ਰਿਪਟਾਂ ਨੂੰ ਨਵੀਂ ਰਿਲੀਜ਼ਾਂ Windows 11, macOS Ventura ਅਤੇ Ubuntu 22.04 (ਅਤੇ ਉੱਪਰ) 'ਤੇ ਟੈਸਟ ਕੀਤਾ ਗਿਆ ਹੈ।

## ਲੋੜੀਂਦੇ Azure OpenAI Service ਸਰੋਤ ਬਣਾਓ

> [!IMPORTANT]
> ਅਸੀਂ ਤੁਹਾਨੂੰ ਸਲਾਹ ਦਿੰਦੇ ਹਾਂ ਕਿ ਤੁਸੀਂ Azure CLI ਨੂੰ ਨਵੀਂ ਵਰਜਨ 'ਤੇ ਅਪਡੇਟ ਕਰੋ ਤਾਂ ਜੋ OpenAI ਨਾਲ ਸੰਗਤਤਾ ਯਕੀਨੀ ਬਣਾਈ ਜਾ ਸਕੇ
> ਵੇਖੋ [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. ਇੱਕ resource group ਬਣਾਓ

> [!NOTE]
> ਇਨ੍ਹਾਂ ਹਦਾਇਤਾਂ ਲਈ ਅਸੀਂ East US ਵਿੱਚ "semantic-video-search" ਨਾਮਕ resource group ਵਰਤ ਰਹੇ ਹਾਂ।
> ਤੁਸੀਂ resource group ਦਾ ਨਾਮ ਬਦਲ ਸਕਦੇ ਹੋ, ਪਰ ਜਦੋਂ ਸਰੋਤਾਂ ਲਈ ਸਥਾਨ ਬਦਲਦੇ ਹੋ,
> ਤਾਂ [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਚੈੱਕ ਕਰੋ।

```console
az group create --name semantic-video-search --location eastus
```

1. ਇੱਕ Azure OpenAI Service resource ਬਣਾਓ।

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ਇਸ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਵਰਤੋਂ ਲਈ endpoint ਅਤੇ keys ਪ੍ਰਾਪਤ ਕਰੋ

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. ਹੇਠ ਲਿਖੇ ਮਾਡਲ ਡਿਪਲੋਇ ਕਰੋ:
   - `text-embedding-ada-002` ਵਰਜਨ `2` ਜਾਂ ਵੱਧ, ਨਾਮ `text-embedding-ada-002`
   - `gpt-35-turbo` ਵਰਜਨ `0613` ਜਾਂ ਵੱਧ, ਨਾਮ `gpt-35-turbo`

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

## ਲੋੜੀਂਦਾ ਸਾਫਟਵੇਅਰ

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ਜਾਂ ਵੱਧ

## ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ

ਯੂਟਿਊਬ ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡੇਟਾ ਤਿਆਰੀ ਸਕ੍ਰਿਪਟ ਚਲਾਉਣ ਲਈ ਹੇਠ ਲਿਖੇ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਲੋੜੀਂਦੇ ਹਨ।

### Windows 'ਤੇ

ਸਿਫਾਰਸ਼ ਹੈ ਕਿ ਤੁਸੀਂ ਇਹ ਵੈਰੀਏਬਲ ਆਪਣੇ `user` ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ।
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER] ਲਈ `User variables` > `New`।

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Linux ਅਤੇ macOS 'ਤੇ

ਸਿਫਾਰਸ਼ ਹੈ ਕਿ ਹੇਠ ਲਿਖੇ exports ਨੂੰ ਆਪਣੇ `~/.bashrc` ਜਾਂ `~/.zshrc` ਫਾਇਲ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ।

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## ਲੋੜੀਂਦੇ Python ਲਾਇਬ੍ਰੇਰੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ

1. ਜੇਕਰ [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ਪਹਿਲਾਂ ਤੋਂ ਇੰਸਟਾਲ ਨਹੀਂ ਹੈ ਤਾਂ ਇੰਸਟਾਲ ਕਰੋ।
1. ਇੱਕ `Terminal` ਵਿੰਡੋ ਤੋਂ, ਸੈਂਪਲ ਨੂੰ ਆਪਣੇ ਮਨਪਸੰਦ ਰਿਪੋ ਫੋਲਡਰ ਵਿੱਚ ਕਲੋਨ ਕਰੋ।

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` ਫੋਲਡਰ ਵਿੱਚ ਜਾਓ।

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. ਇੱਕ Python ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ।

    Windows 'ਤੇ:

    ```powershell
    python -m venv .venv
    ```

    macOS ਅਤੇ Linux 'ਤੇ:

    ```bash
    python3 -m venv .venv
    ```

1. Python ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਐਕਟੀਵੇਟ ਕਰੋ।

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

## ਯੂਟਿਊਬ ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡੇਟਾ ਤਿਆਰੀ ਸਕ੍ਰਿਪਟ ਚਲਾਓ

### Windows 'ਤੇ

```powershell
.\transcripts_prepare.ps1
```

### macOS ਅਤੇ Linux 'ਤੇ

```bash
./transcripts_prepare.sh
```

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।