<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:47:59+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "bn"
}
-->
# ট্রান্সক্রিপশন ডেটা প্রস্তুতি

ট্রান্সক্রিপশন ডেটা প্রস্তুতি স্ক্রিপ্টগুলি ইউটিউব ভিডিওর ট্রান্সক্রিপ্ট ডাউনলোড করে এবং সেগুলিকে সেম্যান্টিক সার্চ উইথ ওপেনএআই এমবেডিংস এবং ফাংশনস নমুনার সাথে ব্যবহারের জন্য প্রস্তুত করে।

ট্রান্সক্রিপশন ডেটা প্রস্তুতি স্ক্রিপ্টগুলি সর্বশেষ সংস্করণ উইন্ডোজ ১১, ম্যাকওএস ভেনচুরা এবং উবুন্টু ২২.০৪ (এবং এর উপরে) পরীক্ষা করা হয়েছে।

## প্রয়োজনীয় অ্যাজুর ওপেনএআই সার্ভিস রিসোর্স তৈরি করুন

> [!IMPORTANT]
> আমরা সুপারিশ করছি যে আপনি ওপেনএআই এর সাথে সামঞ্জস্যতা নিশ্চিত করতে অ্যাজুর সিএলআই সর্বশেষ সংস্করণে আপডেট করুন
> [ডকুমেন্টেশন](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) দেখুন

1. একটি রিসোর্স গ্রুপ তৈরি করুন

> [!NOTE]
> এই নির্দেশনার জন্য আমরা পূর্ব ইউএস-এ "সেম্যান্টিক-ভিডিও-সার্চ" নামক রিসোর্স গ্রুপটি ব্যবহার করছি।
> আপনি রিসোর্স গ্রুপের নাম পরিবর্তন করতে পারেন, তবে রিসোর্সগুলির অবস্থান পরিবর্তন করার সময়,
> [মডেল প্রাপ্যতা টেবিল](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) পরীক্ষা করুন।

```console
az group create --name semantic-video-search --location eastus
```

1. একটি অ্যাজুর ওপেনএআই সার্ভিস রিসোর্স তৈরি করুন।

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. এই অ্যাপ্লিকেশনে ব্যবহারের জন্য এন্ডপয়েন্ট এবং কী সংগ্রহ করুন

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. নিম্নলিখিত মডেলগুলি ডিপ্লয় করুন:
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

## প্রয়োজনীয় সফটওয়্যার

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) বা তার উপরে

## এনভায়রনমেন্ট ভেরিয়েবল

ইউটিউব ট্রান্সক্রিপশন ডেটা প্রস্তুতি স্ক্রিপ্টগুলি চালানোর জন্য নিম্নলিখিত এনভায়রনমেন্ট ভেরিয়েবলগুলি প্রয়োজন।

### উইন্ডোজে

আপনার `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New` এ ভেরিয়েবলগুলি যোগ করার পরামর্শ দেওয়া হচ্ছে।

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### লিনাক্স এবং ম্যাকওএসে

আপনার `~/.bashrc` or `~/.zshrc` ফাইলে নিম্নলিখিত এক্সপোর্টগুলি যোগ করার পরামর্শ দেওয়া হচ্ছে।

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## প্রয়োজনীয় পাইথন লাইব্রেরি ইনস্টল করুন

1. যদি এটি ইতিমধ্যে ইনস্টল না থাকে তবে [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ইনস্টল করুন।
1. একটি `Terminal` উইন্ডো থেকে, আপনার পছন্দের রেপো ফোল্ডারে নমুনাটি ক্লোন করুন।

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` ফোল্ডারে নেভিগেট করুন।

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. একটি পাইথন ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন।

    উইন্ডোজে:

    ```powershell
    python -m venv .venv
    ```

    ম্যাকওএস এবং লিনাক্সে:

    ```bash
    python3 -m venv .venv
    ```

1. পাইথন ভার্চুয়াল এনভায়রনমেন্ট সক্রিয় করুন।

   উইন্ডোজে:

   ```powershell
   .venv\Scripts\activate
   ```

   ম্যাকওএস এবং লিনাক্সে:

   ```bash
   source .venv/bin/activate
   ```

1. প্রয়োজনীয় লাইব্রেরিগুলি ইনস্টল করুন।

   উইন্ডোজে:

   ```powershell
   pip install -r requirements.txt
   ```

   ম্যাকওএস এবং লিনাক্সে:

   ```bash
   pip3 install -r requirements.txt
   ```

## ইউটিউব ট্রান্সক্রিপশন ডেটা প্রস্তুতি স্ক্রিপ্টগুলি চালান

### উইন্ডোজে

```powershell
.\transcripts_prepare.ps1
```

### ম্যাকওএস এবং লিনাক্সে

```bash
./transcripts_prepare.sh
```

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে সচেতন থাকুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসংগতি থাকতে পারে। এর মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসাবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোন ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।