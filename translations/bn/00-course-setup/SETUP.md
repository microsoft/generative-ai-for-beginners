<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:13:01+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "bn"
}
-->
# আপনার ডেভেলপমেন্ট এনভায়রনমেন্ট সেটআপ করুন

আমরা এই রেপোজিটরি এবং কোর্সটি একটি [ডেভেলপমেন্ট কন্টেইনার](https://containers.dev?WT.mc_id=academic-105485-koreyst) দিয়ে সেটআপ করেছি, যা একটি ইউনিভার্সাল রানটাইম সরবরাহ করে যা Python3, .NET, Node.js এবং Java ডেভেলপমেন্ট সমর্থন করতে পারে। সংশ্লিষ্ট কনফিগারেশনটি `.devcontainer/` ফোল্ডারে `devcontainer.json` ফাইলে সংজ্ঞায়িত করা হয়েছে, যা এই রেপোজিটরির রুটে অবস্থিত।

ডেভেলপমেন্ট কন্টেইনার সক্রিয় করতে, এটি [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (ক্লাউড-হোস্টেড রানটাইমের জন্য) অথবা [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (লোকাল ডিভাইস-হোস্টেড রানটাইমের জন্য) এ চালু করুন। VS Code এর মধ্যে ডেভেলপমেন্ট কন্টেইনারগুলি কীভাবে কাজ করে তা আরও বিস্তারিত জানার জন্য [এই ডকুমেন্টেশনটি](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) পড়ুন।

> [!TIP]  
> আমরা দ্রুত শুরু করার জন্য GitHub Codespaces ব্যবহারের সুপারিশ করি। এটি ব্যক্তিগত অ্যাকাউন্টগুলির জন্য একটি উদার [বিনামূল্যের ব্যবহার কোটার](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) প্রস্তাব দেয়। আপনার কোটার ব্যবহার সর্বাধিক করতে ইনঅ্যাকটিভ কোডস্পেস বন্ধ বা মুছে ফেলার জন্য [টাইমআউটগুলি](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) কনফিগার করুন।

## ১. অ্যাসাইনমেন্ট সম্পাদন করা

প্রতিটি পাঠে _ঐচ্ছিক_ অ্যাসাইনমেন্ট থাকবে যা এক বা একাধিক প্রোগ্রামিং ভাষায় প্রদান করা হতে পারে, যেমন: Python, .NET/C#, Java এবং JavaScript/TypeScript। এই বিভাগটি ঐ অ্যাসাইনমেন্টগুলি সম্পাদন করার সাথে সম্পর্কিত সাধারণ নির্দেশিকা প্রদান করে।

### ১.১ Python অ্যাসাইনমেন্ট

Python অ্যাসাইনমেন্টগুলি হয় অ্যাপ্লিকেশন (`.py` ফাইল) অথবা Jupyter নোটবুক (`.ipynb` ফাইল) হিসাবে প্রদান করা হয়।
- নোটবুক চালাতে, এটি Visual Studio Code এ খুলুন তারপর _Select Kernel_ (উপরে ডানদিকে) ক্লিক করুন এবং প্রদর্শিত ডিফল্ট Python 3 অপশনটি নির্বাচন করুন। এখন আপনি নোটবুকটি চালানোর জন্য _Run All_ করতে পারেন।
- কমান্ড-লাইন থেকে Python অ্যাপ্লিকেশন চালাতে, সুনির্দিষ্ট নির্দেশাবলী অনুসরণ করুন যাতে সঠিক ফাইলগুলি নির্বাচন করা এবং প্রয়োজনীয় আর্গুমেন্টগুলি প্রদান করা নিশ্চিত হয়।

## ২. প্রদানকারী কনফিগার করা

অ্যাসাইনমেন্টগুলি এক বা একাধিক বড় ভাষা মডেল (LLM) ডেপ্লয়মেন্টের সাথে কাজ করার জন্য সেটআপ করা হতে পারে একটি সমর্থিত সার্ভিস প্রদানকারীর মাধ্যমে যেমন OpenAI, Azure বা Hugging Face। এগুলি একটি _হোস্টেড এন্ডপয়েন্ট_ (API) সরবরাহ করে যা আমরা সঠিক শংসাপত্র (API কী বা টোকেন) দিয়ে প্রোগ্রাম্যাটিকভাবে অ্যাক্সেস করতে পারি। এই কোর্সে, আমরা এই প্রদানকারীদের আলোচনা করব:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) বিভিন্ন মডেল সহ মূল GPT সিরিজ।
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) এন্টারপ্রাইজ প্রস্তুতির ফোকাস সহ OpenAI মডেলের জন্য
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ওপেন-সোর্স মডেল এবং ইনফারেন্স সার্ভারের জন্য

**এই অনুশীলনগুলির জন্য আপনাকে আপনার নিজস্ব অ্যাকাউন্টগুলি ব্যবহার করতে হবে**। অ্যাসাইনমেন্টগুলি ঐচ্ছিক, তাই আপনি আপনার আগ্রহের উপর ভিত্তি করে একটি, সব - অথবা কোনো প্রদানকারী সেটআপ করতে পারেন। সাইনআপের জন্য কিছু নির্দেশিকা:

| সাইনআপ | খরচ | API কী | প্লেগ্রাউন্ড | মন্তব্য |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [মূল্য নির্ধারণ](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [প্রজেক্ট-ভিত্তিক](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [কোড-ছাড়া, ওয়েব](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | একাধিক মডেল উপলব্ধ |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [মূল্য নির্ধারণ](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK দ্রুত শুরু](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [স্টুডিও দ্রুত শুরু](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [অ্যাক্সেসের জন্য আগেই আবেদন করতে হবে](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [মূল্য নির্ধারণ](https://huggingface.co/pricing) | [অ্যাক্সেস টোকেন](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat এর সীমিত মডেল রয়েছে](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

বিভিন্ন প্রদানকারীর সাথে ব্যবহারের জন্য এই রেপোজিটরিটি _কনফিগার_ করতে নীচের নির্দেশাবলী অনুসরণ করুন। যেসব অ্যাসাইনমেন্টের জন্য একটি নির্দিষ্ট প্রদানকারী প্রয়োজন হবে তাদের ফাইলনামে এই ট্যাগগুলির মধ্যে একটি থাকবে:
- `aoai` - Azure OpenAI এন্ডপয়েন্ট, কী প্রয়োজন
- `oai` - OpenAI এন্ডপয়েন্ট, কী প্রয়োজন
- `hf` - Hugging Face টোকেন প্রয়োজন

আপনি এক, কোনোটিই, বা সব প্রদানকারী কনফিগার করতে পারেন। সম্পর্কিত অ্যাসাইনমেন্টগুলি কেবল শংসাপত্রের অভাবে ত্রুটি দেখাবে।

### ২.১ `.env` ফাইল তৈরি করুন

আমরা ধরে নিচ্ছি যে আপনি উপরের নির্দেশিকা ইতিমধ্যে পড়েছেন এবং সংশ্লিষ্ট প্রদানকারীর সাথে সাইন আপ করেছেন এবং প্রয়োজনীয় প্রমাণীকরণ শংসাপত্রগুলি (API_KEY বা টোকেন) পেয়েছেন। Azure OpenAI এর ক্ষেত্রে, আমরা ধরে নিচ্ছি যে আপনার কাছে একটি বৈধ Azure OpenAI সার্ভিস ডেপ্লয়মেন্ট (এন্ডপয়েন্ট) রয়েছে যেখানে অন্তত একটি GPT মডেল চ্যাট সম্পূর্ণতার জন্য ডেপ্লয় করা হয়েছে।

পরবর্তী পদক্ষেপ হল আপনার **লোকাল এনভায়রনমেন্ট ভেরিয়েবলগুলি** নিম্নরূপ কনফিগার করা:

1. `.env.copy` ফাইলটি রুট ফোল্ডারে দেখুন যা এই রকম কিছু বিষয়বস্তু থাকা উচিত:

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

2. নিচের কমান্ড ব্যবহার করে `.env` এ ফাইলটি কপি করুন। এই ফাইলটি _gitignore-d_, গোপনীয়তাগুলি সুরক্ষিত রাখে।

   ```bash
   cp .env.copy .env
   ```

3. পরবর্তী বিভাগে বর্ণিত হিসাবে মানগুলি পূরণ করুন (ডান পাশে প্লেসহোল্ডারগুলি প্রতিস্থাপন করুন)।

3. (ঐচ্ছিক) আপনি যদি GitHub Codespaces ব্যবহার করেন, তাহলে এই রেপোজিটরির সাথে সম্পর্কিত _Codespaces secrets_ হিসাবে পরিবেশ ভেরিয়েবল সংরক্ষণ করার বিকল্প রয়েছে। সেক্ষেত্রে, আপনাকে একটি লোকাল .env ফাইল সেটআপ করতে হবে না। **তবে, মনে রাখবেন যে এই বিকল্পটি কেবল তখনই কাজ করে যদি আপনি GitHub Codespaces ব্যবহার করেন।** আপনি যদি Docker Desktop ব্যবহার করেন তবে আপনাকে এখনও .env ফাইল সেটআপ করতে হবে।

### ২.২ `.env` ফাইল পূরণ করুন

চলুন ভেরিয়েবল নামগুলি দ্রুত দেখে নিই তারা কী উপস্থাপন করে তা বুঝতে:

| ভেরিয়েবল | বিবরণ |
| :--- | :--- |
| HUGGING_FACE_API_KEY | এটি আপনার প্রোফাইলে সেটআপ করা ব্যবহারকারী অ্যাক্সেস টোকেন |
| OPENAI_API_KEY | এটি নন-Azure OpenAI এন্ডপয়েন্টগুলির জন্য সার্ভিস ব্যবহার করার অনুমোদন কী |
| AZURE_OPENAI_API_KEY | এটি ঐ সার্ভিস ব্যবহার করার অনুমোদন কী |
| AZURE_OPENAI_ENDPOINT | এটি Azure OpenAI রিসোর্সের জন্য ডেপ্লয় করা এন্ডপয়েন্ট |
| AZURE_OPENAI_DEPLOYMENT | এটি _টেক্সট জেনারেশন_ মডেল ডেপ্লয়মেন্ট এন্ডপয়েন্ট |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | এটি _টেক্সট এম্বেডিংস_ মডেল ডেপ্লয়মেন্ট এন্ডপয়েন্ট |
| | |

বিঃদ্রঃ: শেষ দুটি Azure OpenAI ভেরিয়েবল যথাক্রমে চ্যাট সম্পূর্ণতার জন্য একটি ডিফল্ট মডেল (টেক্সট জেনারেশন) এবং ভেক্টর সার্চ (এম্বেডিংস) প্রতিফলিত করে। তাদের সেটআপের নির্দেশাবলী প্রাসঙ্গিক অ্যাসাইনমেন্টগুলিতে সংজ্ঞায়িত করা হবে।

### ২.৩ Azure কনফিগার করুন: পোর্টাল থেকে

Azure OpenAI এন্ডপয়েন্ট এবং কী মানগুলি [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) এ পাওয়া যাবে তাই চলুন সেখানে শুরু করি।

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) এ যান
1. সাইডবারে (বাম মেনুতে) **Keys and Endpoint** অপশনটি ক্লিক করুন।
1. **Show Keys** ক্লিক করুন - আপনি নিম্নলিখিতটি দেখতে পাবেন: KEY 1, KEY 2 এবং এন্ডপয়েন্ট।
1. AZURE_OPENAI_API_KEY এর জন্য KEY 1 মানটি ব্যবহার করুন
1. AZURE_OPENAI_ENDPOINT এর জন্য এন্ডপয়েন্ট মানটি ব্যবহার করুন

পরবর্তী, আমরা ডেপ্লয় করা নির্দিষ্ট মডেলগুলির জন্য এন্ডপয়েন্টগুলি প্রয়োজন।

1. Azure OpenAI রিসোর্সের জন্য সাইডবারে (বাম মেনুতে) **Model deployments** অপশনটি ক্লিক করুন।
1. গন্তব্য পৃষ্ঠায়, **Manage Deployments** ক্লিক করুন

এটি আপনাকে Azure OpenAI Studio ওয়েবসাইটে নিয়ে যাবে, যেখানে আমরা নীচে বর্ণিত অন্যান্য মানগুলি খুঁজে পাব।

### ২.৪ Azure কনফিগার করুন: স্টুডিও থেকে

1. [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) এ যান **আপনার রিসোর্স থেকে** উপরে বর্ণিত হিসাবে।
1. বর্তমানে ডেপ্লয় করা মডেলগুলি দেখতে **Deployments** ট্যাব (সাইডবার, বাম) ক্লিক করুন।
1. আপনার পছন্দসই মডেলটি ডেপ্লয় না হলে, এটি ডেপ্লয় করতে **Create new deployment** ব্যবহার করুন।
1. আপনার একটি _টেক্সট-জেনারেশন_ মডেল প্রয়োজন হবে - আমরা সুপারিশ করি: **gpt-35-turbo**
1. আপনার একটি _টেক্সট-এম্বেডিং_ মডেল প্রয়োজন হবে - আমরা সুপারিশ করি **text-embedding-ada-002**

এখন পরিবেশ ভেরিয়েবলগুলি আপডেট করুন যাতে ডেপ্লয়মেন্ট নামটি প্রতিফলিত হয়। এটি সাধারণত মডেল নামের মতোই হবে যদি না আপনি এটি স্পষ্টভাবে পরিবর্তন করেন। সুতরাং, উদাহরণস্বরূপ, আপনার থাকতে পারে:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**সম্পন্ন হলে .env ফাইলটি সংরক্ষণ করতে ভুলবেন না**। আপনি এখন ফাইল থেকে বেরিয়ে যেতে পারেন এবং নোটবুক চালানোর নির্দেশাবলীতে ফিরে আসতে পারেন।

### ২.৫ OpenAI কনফিগার করুন: প্রোফাইল থেকে

আপনার OpenAI API কী আপনার [OpenAI অ্যাকাউন্টে](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) পাওয়া যাবে। যদি আপনার না থাকে, আপনি একটি অ্যাকাউন্টের জন্য সাইন আপ করতে পারেন এবং একটি API কী তৈরি করতে পারেন। একবার আপনার কী হয়ে গেলে, আপনি `.env` ফাইলে `OPENAI_API_KEY` ভেরিয়েবলটি পূরণ করতে এটি ব্যবহার করতে পারেন।

### ২.৬ Hugging Face কনফিগার করুন: প্রোফাইল থেকে

আপনার Hugging Face টোকেন আপনার প্রোফাইলে [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) এর অধীনে পাওয়া যাবে। এগুলি প্রকাশ্যে পোস্ট বা শেয়ার করবেন না। পরিবর্তে, এই প্রকল্প ব্যবহারের জন্য একটি নতুন টোকেন তৈরি করুন এবং `.env` ফাইলে `HUGGING_FACE_API_KEY` ভেরিয়েবলের অধীনে সেটি কপি করুন। _নোট:_ এটি প্রযুক্তিগতভাবে একটি API কী নয় তবে প্রমাণীকরণের জন্য ব্যবহৃত হয় তাই আমরা ধারাবাহিকতার জন্য সেই নামকরণের প্রচলন বজায় রাখছি।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে সচেতন থাকুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। এর মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারের ফলে উদ্ভূত কোনও ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।