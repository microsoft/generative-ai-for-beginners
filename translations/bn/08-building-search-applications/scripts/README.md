# ট্রান্সক্রিপশন ডেটা প্রস্তুতি

ট্রান্সক্রিপশন ডেটা প্রস্তুতি স্ক্রিপ্টগুলি YouTube ভিডিও ট্রান্সক্রিপ্ট ডাউনলোড করে এবং সেগুলি Semantic Search with OpenAI Embeddings and Functions নমুনার সাথে ব্যবহারের জন্য প্রস্তুত করে।

ট্রান্সক্রিপশন ডেটা প্রস্তুতি স্ক্রিপ্টগুলি সর্বশেষ রিলিজ Windows 11, macOS Ventura এবং Ubuntu 22.04 (এবং তার উপরের) এ পরীক্ষা করা হয়েছে।

## প্রয়োজনীয় Azure OpenAI সার্ভিস রিসোর্স তৈরি করুন

> [!IMPORTANT]
> আমরা পরামর্শ দিই Azure CLI সর্বশেষ সংস্করণে আপডেট করার যাতে OpenAI এর সঙ্গে সামঞ্জস্য নিশ্চিত হয়
> দেখুন [ডকুমেন্টেশন](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. একটি রিসোর্স গ্রুপ তৈরি করুন

> [!NOTE]
> এই নির্দেশাবলীতে আমরা East US-এ "semantic-video-search" নামে রিসোর্স গ্রুপ ব্যবহার করছি।
> আপনি রিসোর্স গ্রুপের নাম পরিবর্তন করতে পারেন, কিন্তু যখন রিসোর্সের অবস্থান পরিবর্তন করবেন,
> [মডেল উপলব্ধতার টেবিলটি](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) পরীক্ষা করুন।

```console
az group create --name semantic-video-search --location eastus
```

1. একটি Azure OpenAI সার্ভিস রিসোর্স তৈরি করুন।

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. এই অ্যাপ্লিকেশনে ব্যবহারের জন্য এন্ডপয়েন্ট এবং কী পেতে

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. নিম্নলিখিত মডেলগুলি ডেপ্লয় করুন:
   - `text-embedding-ada-002` সংস্করণ `2` বা বড়, যা `text-embedding-ada-002` নামে আছে
   - `gpt-4o-mini` নামে `gpt-4o-mini`

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

## প্রয়োজনীয় সফটওয়্যার

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) বা বড়

## পরিবেশ পরিবর্তনশীলসমূহ

YouTube ট্রান্সক্রিপশন ডেটা প্রস্তুতি স্ক্রিপ্ট রান করার জন্য নিম্নলিখিত পরিবেশ পরিবর্তনশীলগুলির প্রয়োজন।

### Windows-এ

আপনার `user` পরিবেশ পরিবর্তনশীলগুলিতে এগুলি যোগ করার পরামর্শ দিচ্ছি।
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER] এর জন্য `User variables` > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- আপনি পরিবেশ পরিবর্তনশীলগুলি আপনার PowerShell প্রোফাইলে যোগ করতে পারেন।

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### Linux এবং macOS-এ

আপনার `~/.bashrc` অথবা `~/.zshrc` ফাইলে নিচের এক্সপোর্টগুলি যোগ করার পরামর্শ দিচ্ছি।

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## প্রয়োজনীয় Python লাইব্রেরি ইনস্টল করুন

1. যদি পূর্বে ইনস্টল না থাকে তবে [git ক্লায়েন্ট](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ইনস্টল করুন।
1. একটি `Terminal` উইন্ডো থেকে, নমুনাটি আপনার পছন্দসই রিপো ফোল্ডারে ক্লোন করুন।

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` ফোল্ডারে যান।

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. একটি Python ভার্চুয়াল পরিবেশ তৈরি করুন।

    Windows-এ:

    ```powershell
    python -m venv .venv
    ```

    macOS এবং Linux-এ:

    ```bash
    python3 -m venv .venv
    ```

1. Python ভার্চুয়াল পরিবেশ সক্রিয় করুন।

   Windows-এ:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS এবং Linux-এ:

   ```bash
   source .venv/bin/activate
   ```

1. প্রয়োজনীয় লাইব্রেরিগুলি ইনস্টল করুন।

   Windows-এ:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS এবং Linux-এ:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ট্রান্সক্রিপশন ডেটা প্রস্তুতি স্ক্রিপ্টগুলি চালান

### Windows-এ

```powershell
.\transcripts_prepare.ps1
```

### macOS এবং Linux-এ

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->