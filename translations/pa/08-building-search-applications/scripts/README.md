<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:49:21+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "pa"
}
-->
# ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡਾਟਾ ਤਿਆਰੀ

ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡਾਟਾ ਤਿਆਰੀ ਸਕ੍ਰਿਪਟ YouTube ਵੀਡੀਓ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਡਾਊਨਲੋਡ ਕਰਦੇ ਹਨ ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ OpenAI ਐਮਬੈਡਿੰਗ ਅਤੇ ਫੰਕਸ਼ਨ ਦੇ ਨਮੂਨੇ ਨਾਲ ਸੈਮਾਂਟਿਕ ਖੋਜ ਲਈ ਵਰਤਣ ਲਈ ਤਿਆਰ ਕਰਦੇ ਹਨ।

ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡਾਟਾ ਤਿਆਰੀ ਸਕ੍ਰਿਪਟ ਨੂੰ ਨਵੀਂ ਰਿਲੀਜ਼ ਕੀਤੀਆਂ ਗਈਆਂ Windows 11, macOS Ventura ਅਤੇ Ubuntu 22.04 (ਅਤੇ ਇਸ ਤੋਂ ਉੱਪਰ) 'ਤੇ ਟੈਸਟ ਕੀਤਾ ਗਿਆ ਹੈ।

## ਲੋੜੀਂਦੇ Azure OpenAI ਸੇਵਾ ਸਰੋਤ ਬਣਾਓ

1. ਸਰੋਤ ਸਮੂਹ ਬਣਾਓ

> [!NOTE]
> ਇਸ ਹਦਾਇਤਾਂ ਲਈ ਅਸੀਂ East US ਵਿੱਚ "semantic-video-search" ਨਾਮਕ ਸਰੋਤ ਸਮੂਹ ਦੀ ਵਰਤੋਂ ਕਰ ਰਹੇ ਹਾਂ।
> ਤੁਸੀਂ ਸਰੋਤ ਸਮੂਹ ਦਾ ਨਾਮ ਬਦਲ ਸਕਦੇ ਹੋ, ਪਰ ਜਦੋਂ ਸਰੋਤਾਂ ਲਈ ਸਥਾਨ ਬਦਲਦੇ ਹੋ, 
> [ਮਾਡਲ ਉਪਲਬਧਤਾ ਟੇਬਲ](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) ਦੀ ਜਾਂਚ ਕਰੋ।

```console
az group create --name semantic-video-search --location eastus
```

1. ਇੱਕ Azure OpenAI ਸੇਵਾ ਸਰੋਤ ਬਣਾਓ।

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

1. ਹੇਠਾਂ ਦਿੱਤੇ ਮਾਡਲ ਤੈਨਾਤ ਕਰੋ:
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

## ਲੋੜੀਂਦਾ ਸੌਫਟਵੇਅਰ

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ਜਾਂ ਇਸ ਤੋਂ ਵੱਧ

## ਵਾਤਾਵਰਣ ਚਲ

ਹੇਠਾਂ ਦਿੱਤੇ ਵਾਤਾਵਰਣ ਚਲਾਂ ਦੀ ਲੋੜ ਹੈ YouTube ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡਾਟਾ ਤਿਆਰੀ ਸਕ੍ਰਿਪਟ ਚਲਾਉਣ ਲਈ।

### Windows 'ਤੇ

ਸੁਝਾਅ ਹੈ ਕਿ ਇਹ ਚਲ ਆਪਣੇ `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New` ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ।

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Linux ਅਤੇ macOS 'ਤੇ

ਸੁਝਾਅ ਹੈ ਕਿ ਹੇਠਾਂ ਦਿੱਤੇ ਐਕਸਪੋਰਟਸ ਨੂੰ ਆਪਣੇ `~/.bashrc` or `~/.zshrc` ਫਾਇਲ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ।

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## ਲੋੜੀਂਦੇ Python ਲਾਇਬ੍ਰੇਰੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ

1. ਜੇਕਰ [git ਕਲਾਇੰਟ](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ਪਹਿਲਾਂ ਤੋਂ ਇੰਸਟਾਲ ਨਹੀਂ ਹੈ ਤਾਂ ਉਸਨੂੰ ਇੰਸਟਾਲ ਕਰੋ।
1. ਇੱਕ `Terminal` ਵਿੰਡੋ ਤੋਂ, ਨਮੂਨੇ ਨੂੰ ਆਪਣੇ ਪਸੰਦੀਦਾ ਰੇਪੋ ਫੋਲਡਰ ਵਿੱਚ ਕਲੋਨ ਕਰੋ।

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

1. Python ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਨੂੰ ਐਕਟੀਵੇਟ ਕਰੋ।

   Windows 'ਤੇ:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS ਅਤੇ Linux 'ਤੇ:

   ```bash
   source .venv/bin/activate
   ```

1. ਲੋੜੀਂਦੇ ਲਾਇਬ੍ਰੇਰੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ।

   Windows 'ਤੇ:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS ਅਤੇ Linux 'ਤੇ:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡਾਟਾ ਤਿਆਰੀ ਸਕ੍ਰਿਪਟ ਚਲਾਓ

### Windows 'ਤੇ

```powershell
.\transcripts_prepare.ps1
```

### macOS ਅਤੇ Linux 'ਤੇ

```bash
./transcripts_prepare.sh
```

**ਅਸਵੀਕਰਤੀਕਰਨ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਛੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪ੍ਰੋਫੈਸ਼ਨਲ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।