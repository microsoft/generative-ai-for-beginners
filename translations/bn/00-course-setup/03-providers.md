<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T15:33:09+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "bn"
}
-->
# LLM প্রদানকারী নির্বাচন ও কনফিগারেশন 🔑

এসাইনমেন্টগুলো **এক বা একাধিক** Large Language Model (LLM) ডিপ্লয়মেন্টের সাথে কাজ করার জন্য OpenAI, Azure বা Hugging Face-এর মতো সাপোর্টেড সার্ভিস প্রদানকারীর মাধ্যমে সেটআপ করা যেতে পারে। এরা একটি _হোস্টেড এন্ডপয়েন্ট_ (API) দেয়, যেটি আমরা সঠিক ক্রেডেনশিয়াল (API key বা token) দিয়ে প্রোগ্রামেটিকভাবে অ্যাক্সেস করতে পারি। এই কোর্সে আমরা নিচের প্রদানকারীদের নিয়ে আলোচনা করেছি:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) - বিভিন্ন মডেল, মূল GPT সিরিজসহ।
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) - OpenAI মডেল, এন্টারপ্রাইজ ফোকাসে
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) - ওপেন-সোর্স মডেল ও ইনফারেন্স সার্ভার

**এই এক্সারসাইজগুলোতে আপনাকে নিজের অ্যাকাউন্ট ব্যবহার করতে হবে।** এসাইনমেন্টগুলো ঐচ্ছিক, তাই আপনি ইচ্ছা করলে একটি, সবগুলো বা কোনোটিই সেটআপ না করেও করতে পারেন। সাইনআপের জন্য কিছু নির্দেশনা:

| সাইনআপ | খরচ | API Key | প্লেগ্রাউন্ড | মন্তব্য |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [প্রাইসিং](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [প্রজেক্ট-ভিত্তিক](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [নো-কোড, ওয়েব](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | একাধিক মডেল উপলব্ধ |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [প্রাইসিং](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [অ্যাক্সেসের জন্য আগে আবেদন করতে হবে](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [প্রাইসিং](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat-এ সীমিত মডেল আছে](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

নিচের নির্দেশনা অনুসরণ করে এই রিপোজিটরিটি বিভিন্ন প্রদানকারীর সাথে ব্যবহার করার জন্য _কনফিগার_ করুন। যেসব এসাইনমেন্ট নির্দিষ্ট প্রদানকারী চায়, তাদের ফাইলনেমে নিচের ট্যাগগুলো থাকবে:

- `aoai` - Azure OpenAI endpoint, key লাগবে
- `oai` - OpenAI endpoint, key লাগবে
- `hf` - Hugging Face token লাগবে

আপনি একটি, কোনোটিই না, বা সবগুলো প্রদানকারী কনফিগার করতে পারেন। সংশ্লিষ্ট এসাইনমেন্টে ক্রেডেনশিয়াল না থাকলে এরর দেখাবে।

## `.env` ফাইল তৈরি করুন

ধরা হচ্ছে, আপনি উপরের নির্দেশনা পড়ে সংশ্লিষ্ট প্রদানকারীতে সাইনআপ করেছেন এবং প্রয়োজনীয় অথেন্টিকেশন ক্রেডেনশিয়াল (API_KEY বা token) পেয়েছেন। Azure OpenAI-এর ক্ষেত্রে, ধরে নিচ্ছি আপনার একটি বৈধ Azure OpenAI Service (endpoint) ডিপ্লয় করা আছে এবং অন্তত একটি GPT মডেল চ্যাট কমপ্লিশনের জন্য ডিপ্লয় করা আছে।

পরবর্তী ধাপে **লোকাল এনভায়রনমেন্ট ভেরিয়েবল** নিচের মতো কনফিগার করুন:

1. রুট ফোল্ডারে `.env.copy` নামে একটি ফাইল দেখুন, যার কনটেন্ট সাধারণত এমন হবে:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. নিচের কমান্ড দিয়ে ওই ফাইলটি `.env` নামে কপি করুন। এই ফাইলটি _gitignore_-এ রাখা, যাতে সিক্রেট নিরাপদ থাকে।

   ```bash
   cp .env.copy .env
   ```

3. পরবর্তী সেকশনে বর্ণিত মতো মানগুলো (ডান পাশে `=` এর পরের প্লেসহোল্ডার) পূরণ করুন।

4. (ঐচ্ছিক) যদি আপনি GitHub Codespaces ব্যবহার করেন, তাহলে এনভায়রনমেন্ট ভেরিয়েবলগুলো _Codespaces secrets_ হিসেবে এই রিপোজিটরির সাথে সংরক্ষণ করতে পারেন। সে ক্ষেত্রে লোকাল .env ফাইল সেটআপ করতে হবে না। **তবে, এই অপশন শুধু GitHub Codespaces-এ কাজ করে।** আপনি যদি Docker Desktop ব্যবহার করেন, তাহলে .env ফাইল সেটআপ করতেই হবে।

## `.env` ফাইল পূরণ করুন

চলুন, ভেরিয়েবল নামগুলো দেখে নেই, এগুলো কী বোঝায়:

| ভেরিয়েবল  | বর্ণনা  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | এটি আপনার প্রোফাইলে সেটআপ করা ইউজার অ্যাক্সেস টোকেন |
| OPENAI_API_KEY | এটি non-Azure OpenAI endpoint-এর জন্য সার্ভিস ব্যবহারের অথরাইজেশন key |
| AZURE_OPENAI_API_KEY | এটি ঐ সার্ভিস ব্যবহারের অথরাইজেশন key |
| AZURE_OPENAI_ENDPOINT | এটি Azure OpenAI রিসোর্সের ডিপ্লয় করা endpoint |
| AZURE_OPENAI_DEPLOYMENT | এটি _টেক্সট জেনারেশন_ মডেল ডিপ্লয়মেন্ট endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | এটি _টেক্সট এম্বেডিং_ মডেল ডিপ্লয়মেন্ট endpoint |
| | |

নোট: শেষের দুটি Azure OpenAI ভেরিয়েবল ডিফল্ট মডেল চ্যাট কমপ্লিশন (টেক্সট জেনারেশন) এবং ভেক্টর সার্চ (এম্বেডিং) বোঝায়। এগুলো কীভাবে সেট করবেন, সংশ্লিষ্ট এসাইনমেন্টে বলা থাকবে।

## Azure কনফিগার করুন: পোর্টাল থেকে

Azure OpenAI endpoint ও key মানগুলো [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) থেকে পাওয়া যাবে, চলুন শুরু করি।

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) এ যান
1. সাইডবারে (বাম মেনু) **Keys and Endpoint** অপশন ক্লিক করুন।
1. **Show Keys** ক্লিক করুন - KEY 1, KEY 2 এবং Endpoint দেখতে পাবেন।
1. AZURE_OPENAI_API_KEY-এর জন্য KEY 1 ব্যবহার করুন
1. AZURE_OPENAI_ENDPOINT-এর জন্য Endpoint মান ব্যবহার করুন

এবার, আমরা ডিপ্লয় করা নির্দিষ্ট মডেলগুলোর endpoint লাগবে।

1. Azure OpenAI রিসোর্সের জন্য সাইডবারে (বাম মেনু) **Model deployments** অপশন ক্লিক করুন।
1. গন্তব্য পেজে **Manage Deployments** ক্লিক করুন

এতে আপনি Azure OpenAI Studio ওয়েবসাইটে চলে যাবেন, যেখানে নিচের মতো করে বাকি মানগুলো পাবেন।

## Azure কনফিগার করুন: স্টুডিও থেকে

1. [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) তে **আপনার রিসোর্স থেকে** যান, যেমন উপরে বলা হয়েছে।
1. সাইডবারে (বাম) **Deployments** ট্যাব ক্লিক করুন, ডিপ্লয় করা মডেলগুলো দেখতে।
1. আপনার কাঙ্ক্ষিত মডেল ডিপ্লয় না থাকলে **Create new deployment** দিয়ে ডিপ্লয় করুন।
1. _টেক্সট-জেনারেশন_ মডেল লাগবে - আমরা সাজেস্ট করি: **gpt-35-turbo**
1. _টেক্সট-এম্বেডিং_ মডেল লাগবে - আমরা সাজেস্ট করি **text-embedding-ada-002**

এখন এনভায়রনমেন্ট ভেরিয়েবলগুলোতে _Deployment name_ আপডেট করুন। সাধারণত এটি মডেল নামের মতোই হবে, যদি না আপনি আলাদাভাবে নাম দেন। উদাহরণস্বরূপ, আপনার থাকতে পারে:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**শেষ হলে .env ফাইলটি সেভ করতে ভুলবেন না।** এখন ফাইল থেকে বেরিয়ে নোটবুক চালানোর নির্দেশনায় ফিরে যান।

## OpenAI কনফিগার করুন: প্রোফাইল থেকে

আপনার OpenAI API key [OpenAI অ্যাকাউন্টে](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) পাওয়া যাবে। যদি না থাকে, অ্যাকাউন্ট খুলে API key তৈরি করুন। key পেলে, `.env` ফাইলে `OPENAI_API_KEY` ভেরিয়েবল পূরণ করুন।

## Hugging Face কনফিগার করুন: প্রোফাইল থেকে

আপনার Hugging Face token প্রোফাইলে [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) এ পাবেন। এগুলো পাবলিকলি পোস্ট বা শেয়ার করবেন না। বরং, এই প্রজেক্টের জন্য নতুন token তৈরি করুন এবং `.env` ফাইলে `HUGGING_FACE_API_KEY` ভেরিয়েবলে কপি করুন। _নোট:_ এটি টেকনিক্যালি API key নয়, অথেন্টিকেশনের জন্য ব্যবহৃত হয়, তাই কনসিস্টেন্সির জন্য এই নাম রাখা হয়েছে।

---

**দায়িত্ব পরিত্যাগের ঘোষণা**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য নির্ভুলতা বজায় রাখার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হবে। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হচ্ছে। এই অনুবাদের ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।