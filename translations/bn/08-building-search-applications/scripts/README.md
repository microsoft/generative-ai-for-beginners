# ট্রান্সক্রিপশন ডেটা প্রস্তুতি

ট্রান্সক্রিপশন ডেটা প্রস্তুতি স্ক্রিপ্টগুলি ইউটিউব ভিডিও ট্রান্সক্রিপ্ট ডাউনলোড করে এবং সেম্যানটিক সার্চ উইথ ওপেনএআই এমবেডিংস এবং ফাংশনস নমুনার সাথে ব্যবহারের জন্য প্রস্তুত করে।

ট্রান্সক্রিপশন ডেটা প্রস্তুতি স্ক্রিপ্টগুলি সর্বশেষ রিলিজ উইন্ডোজ ১১, ম্যাকওএস ভেন্টুরা এবং উবুন্টু ২২.০৪ (এবং ওপরে) তে পরীক্ষা করা হয়েছে।

## প্রয়োজনীয় Azure OpenAI সার্ভিস রিসোর্স তৈরি করুন

> [!IMPORTANT]
> আমরা সুপারিশ করি আপনি Azure CLI সর্বশেষ সংস্করণে আপডেট করুন যাতে OpenAI এর সাথে সামঞ্জস্যতা নিশ্চিত হয়
> দেখুন [ডকুমেন্টেশন](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

১. একটি রিসোর্স গ্রুপ তৈরি করুন

> [!NOTE]
> এই নির্দেশাবলীতে আমরা "semantic-video-search" নামক রিসোর্স গ্রুপটি East US-এ ব্যবহার করছি।
> আপনি রিসোর্স গ্রুপের নাম পরিবর্তন করতে পারেন, কিন্তু রিসোর্সের অবস্থান পরিবর্তন করার সময়,
> [মডেল উপলব্ধতা টেবিল](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) পরীক্ষা করুন।

```console
az group create --name semantic-video-search --location eastus
```

২. একটি Azure OpenAI সার্ভিস রিসোর্স তৈরি করুন।

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

৩. এই অ্যাপ্লিকেশনে ব্যবহার করার জন্য এন্ডপয়েন্ট ও কী পান

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

৪. নিম্নলিখিত মডেলগুলি ডিপ্লয় করুন:
   - `text-embedding-ada-002` সংস্করণ `2` বা বড়, যার নাম `text-embedding-ada-002`
   - `gpt-5-mini` যার নাম `gpt-5-mini`

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

## প্রয়োজনীয় সফটওয়্যার

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) বা বড়

## পরিবেশ পরিবর্তনশীল

YouTube ট্রান্সক্রিপশন ডেটা প্রস্তুতি স্ক্রিপ্ট চালানোর জন্য নিম্নলিখিত পরিবেশ পরিবর্তনশীল প্রয়োজন।

### উইন্ডোজে

আপনার `user` পরিবেশ পরিবর্তনশীলগুলিতে এই পরিবর্তনশীলগুলি যোগ করার পরামর্শ দেওয়া হয়।
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER] এর জন্য `User variables` > `New`।

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- আপনি আপনার PowerShell প্রোফাইলে পরিবেশ পরিবর্তনশীল যোগ করতে পারেন।

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### লিনাক্স এবং ম্যাকওএস-এ

নিম্নলিখিত এক্সপোর্টগুলি আপনার `~/.bashrc` বা `~/.zshrc` ফাইলে যোগ করার পরামর্শ দেওয়া হয়।

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## প্রয়োজনীয় পাইথন লাইব্রেরি ইনস্টল করুন

১. [git ক্লায়েন্ট](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ইনস্টল করুন যদি ইতিমধ্যে ইনস্টল করা না থাকে।
২. একটি `Terminal` উইন্ডো থেকে নমুনাটি আপনার পছন্দসই রেপো ফোল্ডারে ক্লোন করুন।

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

৩. `data_prep` ফোল্ডারে যান।

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

৪. একটি পাইথন ভার্চুয়াল পরিবেশ তৈরি করুন।

    উইন্ডোজে:

    ```powershell
    python -m venv .venv
    ```

    ম্যাকওএস এবং লিনাক্সে:

    ```bash
    python3 -m venv .venv
    ```

৫. পাইথন ভার্চুয়াল পরিবেশ সক্রিয় করুন।

   উইন্ডোজে:

   ```powershell
   .venv\Scripts\activate
   ```

   ম্যাকওএস এবং লিনাক্সে:

   ```bash
   source .venv/bin/activate
   ```

৬. প্রয়োজনীয় লাইব্রেরি ইনস্টল করুন।

   উইন্ডোজে:

   ```powershell
   pip install -r requirements.txt
   ```

   ম্যাকওএস এবং লিনাক্সে:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ট্রান্সক্রিপশন ডেটা প্রস্তুতি স্ক্রিপ্ট চালান

### উইন্ডোজে

```powershell
.\transcripts_prepare.ps1
```

### ম্যাকওএস এবং লিনাক্সে

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->