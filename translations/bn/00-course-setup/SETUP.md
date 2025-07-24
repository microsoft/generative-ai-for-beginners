<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:26:17+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "bn"
}
-->
# আপনার ডেভেলপমেন্ট পরিবেশ সেটআপ করুন

আমরা এই রিপোজিটরি এবং কোর্সটি একটি [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) ব্যবহার করে সেটআপ করেছি, যা একটি ইউনিভার্সাল রানটাইম সরবরাহ করে যা Python3, .NET, Node.js এবং Java ডেভেলপমেন্ট সাপোর্ট করে। সংশ্লিষ্ট কনফিগারেশন `devcontainer.json` ফাইলে সংজ্ঞায়িত, যা এই রিপোজিটরির মূল `.devcontainer/` ফোল্ডারে অবস্থিত।

ডেভ কন্টেইনার চালু করতে, এটি [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (ক্লাউড-হোস্টেড রানটাইমের জন্য) অথবা [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (লোকাল ডিভাইস-হোস্টেড রানটাইমের জন্য) এ চালান। VS Code এর মধ্যে ডেভ কন্টেইনার কিভাবে কাজ করে সে সম্পর্কে আরও বিস্তারিত জানতে [এই ডকুমেন্টেশনটি](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) পড়ুন।  

> [!TIP]  
> দ্রুত শুরু করার জন্য আমরা GitHub Codespaces ব্যবহারের পরামর্শ দিই, যা ব্যক্তিগত অ্যাকাউন্টের জন্য একটি উদার [ফ্রি ব্যবহার কোটা](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) প্রদান করে। আপনার কোটা সর্বোচ্চ ব্যবহারের জন্য নিষ্ক্রিয় codespaces বন্ধ বা মুছে ফেলার জন্য [টাইমআউট কনফিগার](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) করুন।


## ১. অ্যাসাইনমেন্ট সম্পাদন

প্রতিটি লেসনে _ঐচ্ছিক_ অ্যাসাইনমেন্ট থাকবে যা এক বা একাধিক প্রোগ্রামিং ভাষায় দেওয়া হতে পারে, যেমন: Python, .NET/C#, Java এবং JavaScript/TypeScript। এই অংশে সেই অ্যাসাইনমেন্টগুলো সম্পাদনের জন্য সাধারণ নির্দেশনা দেওয়া হয়েছে।

### ১.১ Python অ্যাসাইনমেন্ট

Python অ্যাসাইনমেন্টগুলো অ্যাপ্লিকেশন (`.py` ফাইল) অথবা Jupyter নোটবুক (`.ipynb` ফাইল) হিসেবে দেওয়া হয়।  
- নোটবুক চালানোর জন্য, Visual Studio Code এ এটি খুলুন, তারপর উপরের ডানদিকে থাকা _Select Kernel_ এ ক্লিক করে ডিফল্ট Python 3 অপশনটি নির্বাচন করুন। এখন আপনি _Run All_ ক্লিক করে নোটবুকটি চালাতে পারবেন।  
- কমান্ড-লাইন থেকে Python অ্যাপ্লিকেশন চালানোর জন্য, অ্যাসাইনমেন্ট-নির্দিষ্ট নির্দেশনা অনুসরণ করুন যাতে সঠিক ফাইল নির্বাচন এবং প্রয়োজনীয় আর্গুমেন্ট প্রদান নিশ্চিত হয়।  

## ২. প্রোভাইডার কনফিগারেশন

অ্যাসাইনমেন্টগুলো **সম্ভবত** এক বা একাধিক বড় ভাষা মডেল (LLM) ডিপ্লয়মেন্টের বিরুদ্ধে কাজ করার জন্য OpenAI, Azure বা Hugging Face এর মতো সাপোর্টেড সার্ভিস প্রোভাইডারের মাধ্যমে সেটআপ করা হতে পারে। এরা একটি _হোস্টেড এন্ডপয়েন্ট_ (API) প্রদান করে যা আমরা সঠিক ক্রেডেনশিয়াল (API কী বা টোকেন) দিয়ে প্রোগ্রাম্যাটিক্যালি অ্যাক্সেস করতে পারি। এই কোর্সে আমরা নিম্নলিখিত প্রোভাইডারগুলো আলোচনা করব:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) বিভিন্ন মডেল সহ, যার মধ্যে মূল GPT সিরিজ অন্তর্ভুক্ত।  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI মডেলগুলোর জন্য এন্টারপ্রাইজ রেডিনেস ফোকাস সহ।  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ওপেন-সোর্স মডেল এবং ইনফারেন্স সার্ভারের জন্য।  

**এই অনুশীলনগুলোর জন্য আপনাকে আপনার নিজস্ব অ্যাকাউন্ট ব্যবহার করতে হবে**। অ্যাসাইনমেন্টগুলো ঐচ্ছিক, তাই আপনি আপনার আগ্রহ অনুযায়ী এক, সব অথবা কোন প্রোভাইডারই সেটআপ করতে পারেন না। সাইনআপের জন্য কিছু নির্দেশনা:

| সাইনআপ | খরচ | API কী | প্লেগ্রাউন্ড | মন্তব্য |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [মূল্য নির্ধারণ](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [প্রজেক্ট ভিত্তিক](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [নো-কোড, ওয়েব](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | একাধিক মডেল উপলব্ধ |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [মূল্য নির্ধারণ](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK দ্রুত শুরু](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [স্টুডিও দ্রুত শুরু](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [অ্যাক্সেসের জন্য আগেই আবেদন করতে হবে](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [মূল্য নির্ধারণ](https://huggingface.co/pricing) | [অ্যাক্সেস টোকেন](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat এর মডেল সীমিত](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

নিম্নলিখিত নির্দেশনা অনুসরণ করে এই রিপোজিটরিটি বিভিন্ন প্রোভাইডারের জন্য _কনফিগার_ করুন। নির্দিষ্ট প্রোভাইডার প্রয়োজন এমন অ্যাসাইনমেন্টের ফাইলনেমে নিম্নলিখিত ট্যাগগুলোর একটি থাকবে:  
 - `aoai` - Azure OpenAI এন্ডপয়েন্ট, কী প্রয়োজন  
 - `oai` - OpenAI এন্ডপয়েন্ট, কী প্রয়োজন  
 - `hf` - Hugging Face টোকেন প্রয়োজন  

আপনি এক, কোনোটাই বা সব প্রোভাইডার কনফিগার করতে পারেন। সংশ্লিষ্ট অ্যাসাইনমেন্টগুলো অনুপস্থিত ক্রেডেনশিয়ালে ত্রুটি দেখাবে।  

### ২.১ `.env` ফাইল তৈরি করুন

আমরা ধরে নিচ্ছি আপনি উপরের নির্দেশনা পড়ে প্রাসঙ্গিক প্রোভাইডারে সাইন আপ করেছেন এবং প্রয়োজনীয় অথেনটিকেশন ক্রেডেনশিয়াল (API_KEY বা টোকেন) পেয়েছেন। Azure OpenAI এর ক্ষেত্রে, আমরা ধরে নিচ্ছি আপনার কাছে Azure OpenAI সার্ভিসের একটি বৈধ ডিপ্লয়মেন্ট (এন্ডপয়েন্ট) আছে, যেখানে অন্তত একটি GPT মডেল চ্যাট কমপ্লিশনের জন্য ডিপ্লয় করা হয়েছে।

পরবর্তী ধাপ হলো আপনার **লোকাল এনভায়রনমেন্ট ভেরিয়েবলগুলো** নিম্নরূপ কনফিগার করা:

1. মূল ফোল্ডারে `.env.copy` নামে একটি ফাইল খুঁজুন, যার মধ্যে নিম্নরূপ বিষয়বস্তু থাকবে:

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

2. নিচের কমান্ড ব্যবহার করে ফাইলটি `.env` নামে কপি করুন। এই ফাইলটি _gitignore_ করা আছে, তাই গোপনীয়তা রক্ষা পাবে।

   ```bash
   cp .env.copy .env
   ```

3. পরবর্তী অংশে বর্ণিত অনুযায়ী মানগুলো পূরণ করুন (`=` এর ডান পাশে প্লেসহোল্ডারগুলো প্রতিস্থাপন করুন)।

3. (ঐচ্ছিক) আপনি যদি GitHub Codespaces ব্যবহার করেন, তাহলে এই রিপোজিটরির সাথে যুক্ত _Codespaces secrets_ হিসেবে এনভায়রনমেন্ট ভেরিয়েবলগুলো সংরক্ষণ করার অপশন পাবেন। সেই ক্ষেত্রে, আপনাকে লোকাল `.env` ফাইল সেটআপ করতে হবে না। **তবে, এই অপশন শুধুমাত্র GitHub Codespaces ব্যবহারের ক্ষেত্রে কাজ করে।** Docker Desktop ব্যবহার করলে আপনাকে `.env` ফাইল সেটআপ করতে হবে।


### ২.২ `.env` ফাইল পূরণ করুন

চলুন ভেরিয়েবল নামগুলো দেখে নিই এবং বুঝি এগুলো কী বোঝায়:

| ভেরিয়েবল  | বর্ণনা  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | এটি আপনার প্রোফাইলে সেট করা ইউজার অ্যাক্সেস টোকেন |
| OPENAI_API_KEY | Azure OpenAI ব্যতীত সার্ভিস ব্যবহারের জন্য অথরাইজেশন কী |
| AZURE_OPENAI_API_KEY | Azure OpenAI সার্ভিস ব্যবহারের জন্য অথরাইজেশন কী |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI রিসোর্সের ডিপ্লয় করা এন্ডপয়েন্ট |
| AZURE_OPENAI_DEPLOYMENT | _টেক্সট জেনারেশন_ মডেল ডিপ্লয়মেন্ট এন্ডপয়েন্ট |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _টেক্সট এমবেডিং_ মডেল ডিপ্লয়মেন্ট এন্ডপয়েন্ট |
| | |

দ্রষ্টব্য: শেষ দুইটি Azure OpenAI ভেরিয়েবল যথাক্রমে চ্যাট কমপ্লিশন (টেক্সট জেনারেশন) এবং ভেক্টর সার্চ (এম্বেডিংস) এর জন্য ডিফল্ট মডেল নির্দেশ করে। এগুলো সেটআপের নির্দেশনা সংশ্লিষ্ট অ্যাসাইনমেন্টে দেওয়া হবে।


### ২.৩ Azure কনফিগার করুন: পোর্টাল থেকে

Azure OpenAI এন্ডপয়েন্ট এবং কী এর মান [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) এ পাওয়া যাবে, তাই সেখান থেকে শুরু করা যাক।

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) এ যান  
1. সাইডবারে (বাম মেনু) **Keys and Endpoint** অপশনে ক্লিক করুন।  
1. **Show Keys** ক্লিক করুন - আপনি KEY 1, KEY 2 এবং Endpoint দেখতে পাবেন।  
1. AZURE_OPENAI_API_KEY এর জন্য KEY 1 এর মান ব্যবহার করুন।  
1. AZURE_OPENAI_ENDPOINT এর জন্য Endpoint এর মান ব্যবহার করুন।  

এরপর, আমাদের ডিপ্লয় করা নির্দিষ্ট মডেলগুলোর এন্ডপয়েন্ট দরকার।

1. Azure OpenAI রিসোর্সের সাইডবারে (বাম মেনু) **Model deployments** অপশনে ক্লিক করুন।  
1. গন্তব্য পৃষ্ঠায় **Manage Deployments** ক্লিক করুন।  

এটি আপনাকে Azure OpenAI Studio ওয়েবসাইটে নিয়ে যাবে, যেখানে আমরা নিচের মতো মানগুলো পাবো।


### ২.৪ Azure কনফিগার করুন: স্টুডিও থেকে

1. উপরে বর্ণিত রিসোর্স থেকে [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) তে যান।  
1. ডিপ্লয় করা মডেলগুলো দেখতে বাম সাইডবারে **Deployments** ট্যাবে ক্লিক করুন।  
1. আপনার কাঙ্ক্ষিত মডেল ডিপ্লয় করা না থাকলে, **Create new deployment** ব্যবহার করে ডিপ্লয় করুন।  
1. একটি _text-generation_ মডেল প্রয়োজন - আমরা সুপারিশ করি: **gpt-35-turbo**  
1. একটি _text-embedding_ মডেল প্রয়োজন - আমরা সুপারিশ করি **text-embedding-ada-002**  

এখন এনভায়রনমেন্ট ভেরিয়েবলগুলো আপডেট করুন যাতে _Deployment name_ প্রতিফলিত হয়। সাধারণত এটি মডেলের নামের সমান হবে যদি আপনি স্পষ্টভাবে পরিবর্তন না করে থাকেন। উদাহরণস্বরূপ, আপনার `.env` ফাইলে থাকতে পারে:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**ফাইল সম্পাদনার পর .env ফাইলটি সেভ করতে ভুলবেন না**। এরপর আপনি ফাইল থেকে বের হয়ে নোটবুক চালানোর নির্দেশনায় ফিরে যেতে পারেন।


### ২.৫ OpenAI কনফিগার করুন: প্রোফাইল থেকে

আপনার OpenAI API কী আপনার [OpenAI অ্যাকাউন্ট](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) এ পাওয়া যাবে। যদি না থাকে, তাহলে একটি অ্যাকাউন্ট তৈরি করে API কী তৈরি করুন। কী পাওয়ার পর `.env` ফাইলে `OPENAI_API_KEY` ভেরিয়েবলে এটি ব্যবহার করুন।


### ২.৬ Hugging Face কনফিগার করুন: প্রোফাইল থেকে

আপনার Hugging Face টোকেন আপনার প্রোফাইলে [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) এর অধীনে পাওয়া যাবে। এগুলো পাবলিকলি শেয়ার বা পোস্ট করবেন না। পরিবর্তে, এই প্রকল্পের জন্য একটি নতুন টোকেন তৈরি করুন এবং `.env` ফাইলে `HUGGING_FACE_API_KEY` ভেরিয়েবলে কপি করুন। _দ্রষ্টব্য:_ এটি প্রযুক্তিগতভাবে API কী নয়, তবে অথেনটিকেশনের জন্য ব্যবহৃত হয়, তাই সামঞ্জস্যের জন্য এই নামকরণ রাখা হয়েছে।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।