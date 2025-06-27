<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-06-25T16:53:37+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "pa"
}
-->
# ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡਾਟਾ ਤਿਆਰੀ

ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡਾਟਾ ਤਿਆਰੀ ਸਕ੍ਰਿਪਟਸ ਯੂਟਿਊਬ ਵੀਡੀਓ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟਸ ਨੂੰ ਡਾਊਨਲੋਡ ਕਰਦੀਆਂ ਹਨ ਅਤੇ ਉਹਨਾਂ ਨੂੰ ਸੈਮੈਂਟਿਕ ਸਰਚ ਵਿਥ ਓਪਨਏਆਈ ਐਮਬੈਡਿੰਗਸ ਅਤੇ ਫੰਕਸ਼ਨਜ਼ ਨਮੂਨੇ ਨਾਲ ਵਰਤਣ ਲਈ ਤਿਆਰ ਕਰਦੀਆਂ ਹਨ।

ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡਾਟਾ ਤਿਆਰੀ ਸਕ੍ਰਿਪਟਸ ਨੂੰ ਨਵੀਂਤਮ ਰਿਲੀਜ਼ਾਂ ਜਿਵੇਂ ਕਿ Windows 11, macOS Ventura ਅਤੇ Ubuntu 22.04 (ਅਤੇ ਉੱਪਰ) 'ਤੇ ਟੈਸਟ ਕੀਤਾ ਗਿਆ ਹੈ।

## ਲੋੜੀਂਦੇ ਐਜ਼ਰ ਓਪਨਏਆਈ ਸਰਵਿਸ ਸਰੋਤ ਬਣਾਓ

1. ਇੱਕ ਸਰੋਤ ਸਮੂਹ ਬਣਾਓ

> [!NOTE]
> ਇਨ੍ਹਾਂ ਨਿਰਦੇਸ਼ਾਂ ਲਈ ਅਸੀਂ East US ਵਿੱਚ "semantic-video-search" ਨਾਮਕ ਸਰੋਤ ਸਮੂਹ ਵਰਤ ਰਹੇ ਹਾਂ।
> ਤੁਸੀਂ ਸਰੋਤ ਸਮੂਹ ਦਾ ਨਾਮ ਬਦਲ ਸਕਦੇ ਹੋ, ਪਰ ਜਦੋਂ ਸਰੋਤਾਂ ਲਈ ਸਥਾਨ ਬਦਲੋ, 
> ਤਾਂ [ਮਾਡਲ ਉਪਲਬਧਤਾ ਟੇਬਲ](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) ਦੀ ਜਾਂਚ ਕਰੋ।

```console
az group create --name semantic-video-search --location eastus
```

1. ਇੱਕ ਐਜ਼ਰ ਓਪਨਏਆਈ ਸਰਵਿਸ ਸਰੋਤ ਬਣਾਓ।

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ਇਸ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਵਰਤੋਂ ਲਈ ਐਂਡਪੋਇੰਟ ਅਤੇ ਕੁੰਜੀਆਂ ਪ੍ਰਾਪਤ ਕਰੋ

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. ਹੇਠ ਲਿਖੇ ਮਾਡਲ ਡਿਪਲੋਇ ਕਰੋ:
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

## ਲੋੜੀਂਦਾ ਸਾਫਟਵੇਅਰ

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ਜਾਂ ਇਸ ਤੋਂ ਵੱਧ

## ਵਾਤਾਵਰਨ ਵੈਰੀਏਬਲਸ

ਯੂਟਿਊਬ ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡਾਟਾ ਤਿਆਰੀ ਸਕ੍ਰਿਪਟਸ ਨੂੰ ਚਲਾਉਣ ਲਈ ਹੇਠ ਲਿਖੇ ਵਾਤਾਵਰਨ ਵੈਰੀਏਬਲਸ ਦੀ ਲੋੜ ਹੈ।

### Windows 'ਤੇ

ਸੁਝਾਅ ਹੈ ਕਿ ਆਪਣੇ `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New` ਵਿੱਚ ਵੈਰੀਏਬਲਸ ਸ਼ਾਮਲ ਕਰੋ।

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Linux ਅਤੇ macOS 'ਤੇ

ਸੁਝਾਅ ਹੈ ਕਿ ਆਪਣੇ `~/.bashrc` or `~/.zshrc` ਫਾਈਲ ਵਿੱਚ ਹੇਠ ਲਿਖੇ ਐਕਸਪੋਰਟਸ ਸ਼ਾਮਲ ਕਰੋ।

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## ਲੋੜੀਂਦੇ Python ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇੰਸਟਾਲ ਕਰੋ

1. [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਇੰਸਟਾਲ ਕਰੋ ਜੇਕਰ ਇਹ ਪਹਿਲਾਂ ਤੋਂ ਇੰਸਟਾਲ ਨਹੀਂ ਹੈ।
1. ਇੱਕ `Terminal` ਵਿੰਡੋ ਤੋਂ, ਨਮੂਨੇ ਨੂੰ ਆਪਣੇ ਪਸੰਦੀਦਾ ਰਿਪੋ ਫੋਲਡਰ ਵਿੱਚ ਕਲੋਨ ਕਰੋ।

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` ਫੋਲਡਰ ਵਿੱਚ ਜਾਓ।

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. ਇੱਕ Python ਵਰਚੁਅਲ ਵਾਤਾਵਰਨ ਬਣਾਓ।

    Windows 'ਤੇ:

    ```powershell
    python -m venv .venv
    ```

    macOS ਅਤੇ Linux 'ਤੇ:

    ```bash
    python3 -m venv .venv
    ```

1. Python ਵਰਚੁਅਲ ਵਾਤਾਵਰਨ ਨੂੰ ਐਕਟੀਵੇਟ ਕਰੋ।

   Windows 'ਤੇ:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS ਅਤੇ Linux 'ਤੇ:

   ```bash
   source .venv/bin/activate
   ```

1. ਲੋੜੀਂਦੇ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇੰਸਟਾਲ ਕਰੋ।

   Windows 'ਤੇ:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS ਅਤੇ Linux 'ਤੇ:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਡਾਟਾ ਤਿਆਰੀ ਸਕ੍ਰਿਪਟਸ ਚਲਾਓ

### Windows 'ਤੇ

```powershell
.\transcripts_prepare.ps1
```

### macOS ਅਤੇ Linux 'ਤੇ

```bash
./transcripts_prepare.sh
```

**ਅਸਵੀਕਾਰ:**
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਪਰ ਕਿਰਪਾ ਕਰਕੇ ਜਾਣਕਾਰੀ ਹੋਵੇ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੰਗਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਉਤਪੰਨ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।