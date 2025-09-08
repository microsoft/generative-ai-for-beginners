<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:08:31+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "bn"
}
-->
# ট্রান্সক্রিপশন ডেটা প্রস্তুতি

ট্রান্সক্রিপশন ডেটা প্রস্তুতি স্ক্রিপ্টগুলো YouTube ভিডিওর ট্রান্সক্রিপ্ট ডাউনলোড করে এবং সেগুলোকে Semantic Search with OpenAI Embeddings and Functions স্যাম্পলের জন্য প্রস্তুত করে।

ট্রান্সক্রিপশন ডেটা প্রস্তুতি স্ক্রিপ্টগুলো সর্বশেষ রিলিজ Windows 11, macOS Ventura এবং Ubuntu 22.04 (এবং তার উপরে) তে পরীক্ষা করা হয়েছে।

## প্রয়োজনীয় Azure OpenAI Service রিসোর্স তৈরি করুন

> [!IMPORTANT]
> OpenAI এর সাথে সামঞ্জস্য নিশ্চিত করতে আমরা আপনাকে Azure CLI সর্বশেষ সংস্করণে আপডেট করার পরামর্শ দিচ্ছি
> দেখুন [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. একটি রিসোর্স গ্রুপ তৈরি করুন

> [!NOTE]
> এই নির্দেশনাগুলোর জন্য আমরা East US-এ "semantic-video-search" নামের রিসোর্স গ্রুপ ব্যবহার করছি।
> আপনি রিসোর্স গ্রুপের নাম পরিবর্তন করতে পারেন, কিন্তু রিসোর্সের অবস্থান পরিবর্তন করলে,
> [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) চেক করুন।

```console
az group create --name semantic-video-search --location eastus
```

1. একটি Azure OpenAI Service রিসোর্স তৈরি করুন।

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. এই অ্যাপ্লিকেশনে ব্যবহারের জন্য endpoint এবং keys সংগ্রহ করুন

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. নিম্নলিখিত মডেলগুলো ডিপ্লয় করুন:
   - `text-embedding-ada-002` সংস্করণ `2` বা তার উপরে, নাম `text-embedding-ada-002`
   - `gpt-35-turbo` সংস্করণ `0613` বা তার উপরে, নাম `gpt-35-turbo`

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

## প্রয়োজনীয় সফটওয়্যার

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) বা তার উপরে

## পরিবেশ ভেরিয়েবল

YouTube ট্রান্সক্রিপশন ডেটা প্রস্তুতি স্ক্রিপ্ট চালানোর জন্য নিম্নলিখিত পরিবেশ ভেরিয়েবলগুলো প্রয়োজন।

### Windows-এ

আপনার `user` পরিবেশ ভেরিয়েবলে ভেরিয়েবলগুলো যোগ করার পরামর্শ দেওয়া হয়।
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER] এর জন্য `User variables` > `New`।

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Linux এবং macOS-এ

আপনার `~/.bashrc` বা `~/.zshrc` ফাইলে নিম্নলিখিত export গুলো যোগ করার পরামর্শ দেওয়া হয়।

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## প্রয়োজনীয় Python লাইব্রেরি ইনস্টল করুন

1. যদি ইতিমধ্যে ইনস্টল না থাকে, তাহলে [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ইনস্টল করুন।
1. একটি `Terminal` উইন্ডো থেকে, স্যাম্পলটি আপনার পছন্দের রিপো ফোল্ডারে ক্লোন করুন।

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` ফোল্ডারে যান।

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. একটি Python ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন।

    Windows-এ:

    ```powershell
    python -m venv .venv
    ```

    macOS এবং Linux-এ:

    ```bash
    python3 -m venv .venv
    ```

1. Python ভার্চুয়াল এনভায়রনমেন্ট সক্রিয় করুন।

   Windows-এ:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS এবং Linux-এ:

   ```bash
   source .venv/bin/activate
   ```

1. প্রয়োজনীয় লাইব্রেরি ইনস্টল করুন।

   Windows-এ:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS এবং Linux-এ:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ট্রান্সক্রিপশন ডেটা প্রস্তুতি স্ক্রিপ্ট চালান

### Windows-এ

```powershell
.\transcripts_prepare.ps1
```

### macOS এবং Linux-এ

```bash
./transcripts_prepare.sh
```

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।