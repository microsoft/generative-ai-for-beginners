<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:44:04+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "bn"
}
-->
# আপনার ডেভেলপমেন্ট পরিবেশ সেটআপ করুন

আমরা এই রিপোজিটরি এবং কোর্সটি একটি [ডেভেলপমেন্ট কন্টেইনার](https://containers.dev?WT.mc_id=academic-105485-koreyst) দিয়ে সেটআপ করেছি যা একটি ইউনিভার্সাল রানটাইম সহ Python3, .NET, Node.js এবং Java ডেভেলপমেন্ট সমর্থন করতে পারে। সম্পর্কিত কনফিগারেশনটি `devcontainer.json` ফাইলে সংজ্ঞায়িত করা হয়েছে যা এই রিপোজিটরির মূল অংশে `.devcontainer/` ফোল্ডারে অবস্থিত।

ডেভেলপমেন্ট কন্টেইনার সক্রিয় করতে, এটি [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) এ (ক্লাউড-হোস্টেড রানটাইমের জন্য) অথবা [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) এ (লোকাল ডিভাইস-হোস্টেড রানটাইমের জন্য) চালু করুন। VS Code এর মধ্যে ডেভেলপমেন্ট কন্টেইনার কীভাবে কাজ করে তার বিস্তারিত জানতে [এই ডকুমেন্টেশন](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) পড়ুন।

> [!TIP]  
> আমরা দ্রুত শুরু করার জন্য GitHub Codespaces ব্যবহার করার পরামর্শ দিই, যা ন্যূনতম প্রচেষ্টার সাথে শুরু করা যায়। এটি ব্যক্তিগত অ্যাকাউন্টের জন্য উদার [ফ্রি ব্যবহার কোটা](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) প্রদান করে। আপনার কোটা ব্যবহারের সর্বাধিক করতে [টাইমআউট](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) কনফিগার করুন যাতে অক্রিয় Codespaces বন্ধ বা মুছে ফেলা যায়।

## ১. অ্যাসাইনমেন্ট সম্পাদন করা

প্রত্যেক পাঠে _ঐচ্ছিক_ অ্যাসাইনমেন্ট থাকবে যা এক বা একাধিক প্রোগ্রামিং ভাষায় সরবরাহ করা হতে পারে, যেমন: Python, .NET/C#, Java এবং JavaScript/TypeScript। এই বিভাগটি সেই অ্যাসাইনমেন্টগুলি সম্পাদন করার সাথে সম্পর্কিত সাধারণ নির্দেশিকা প্রদান করে।

### ১.১ পাইথন অ্যাসাইনমেন্ট

পাইথন অ্যাসাইনমেন্টগুলি অ্যাপ্লিকেশন (`.py` ফাইল) অথবা Jupyter নোটবুক (`.ipynb` ফাইল) হিসাবে সরবরাহ করা হয়।
- নোটবুক চালানোর জন্য, Visual Studio Code এ এটি খুলুন তারপর _Select Kernel_ (উপরের ডানদিকে) ক্লিক করুন এবং প্রদর্শিত ডিফল্ট Python 3 অপশনটি নির্বাচন করুন। এখন আপনি নোটবুকটি সম্পাদন করতে _Run All_ করতে পারেন।
- কমান্ড-লাইন থেকে পাইথন অ্যাপ্লিকেশন চালানোর জন্য, নির্দিষ্ট অ্যাসাইনমেন্ট নির্দেশিকা অনুসরণ করুন যাতে আপনি সঠিক ফাইলগুলি নির্বাচন করেন এবং প্রয়োজনীয় আর্গুমেন্ট প্রদান করেন।

## ২. প্রদানকারী কনফিগার করা

অ্যাসাইনমেন্টগুলি **এক বা একাধিক বড় ভাষার মডেল (LLM)** মোতায়েনের বিরুদ্ধে কাজ করার জন্য OpenAI, Azure বা Hugging Face এর মতো একটি সমর্থিত পরিষেবা প্রদানকারীর মাধ্যমে সেটআপ করা হতে পারে। এগুলি একটি _হোস্টেড এন্ডপয়েন্ট_ (API) প্রদান করে যা আমরা সঠিক শংসাপত্র (API কী বা টোকেন) সহ প্রোগ্রাম্যাটিকভাবে অ্যাক্সেস করতে পারি। এই কোর্সে, আমরা এই প্রদানকারীদের আলোচনা করি:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) বিভিন্ন মডেল সহ মূল GPT সিরিজ সহ।
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) এন্টারপ্রাইজ প্রস্তুতির দিকে মনোযোগ সহ OpenAI মডেলগুলির জন্য
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ওপেন-সোর্স মডেল এবং অনুমান সার্ভারের জন্য

**এই অনুশীলনের জন্য আপনাকে আপনার নিজস্ব অ্যাকাউন্ট ব্যবহার করতে হবে**। অ্যাসাইনমেন্টগুলি ঐচ্ছিক, তাই আপনি আপনার আগ্রহের ভিত্তিতে একজন, সব - বা কোন প্রদানকারী সেটআপ করতে পারেন। সাইনআপের জন্য কিছু নির্দেশিকা:

| সাইনআপ | খরচ | API কী | প্লেগ্রাউন্ড | মন্তব্য |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [মূল্য নির্ধারণ](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [প্রকল্প-ভিত্তিক](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | একাধিক মডেল উপলব্ধ |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [মূল্য নির্ধারণ](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [অ্যাক্সেসের জন্য আগে আবেদন করতে হবে](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [মূল্য নির্ধারণ](https://huggingface.co/pricing) | [অ্যাক্সেস টোকেন](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat এর সীমিত মডেল আছে](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

নিচের নির্দেশাবলী অনুসরণ করে বিভিন্ন প্রদানকারীদের সাথে ব্যবহার করার জন্য এই রিপোজিটরিটি _কনফিগার_ করুন। নির্দিষ্ট প্রদানকারী প্রয়োজন এমন অ্যাসাইনমেন্টগুলি তাদের ফাইলনামে এই ট্যাগগুলির মধ্যে একটি থাকবে:
 - `aoai` - Azure OpenAI এন্ডপয়েন্ট, কী প্রয়োজন
 - `oai` - OpenAI এন্ডপয়েন্ট, কী প্রয়োজন
 - `hf` - Hugging Face টোকেন প্রয়োজন

আপনি একজন, কোন, বা সব প্রদানকারী কনফিগার করতে পারেন। সম্পর্কিত অ্যাসাইনমেন্টগুলি কেবলমাত্র অনুপস্থিত শংসাপত্রগুলিতে ত্রুটি প্রদর্শন করবে।

###  ২.১. `.env` ফাইল তৈরি করুন

আমরা ধরে নিচ্ছি যে আপনি ইতিমধ্যে উপরের নির্দেশিকা পড়েছেন এবং প্রাসঙ্গিক প্রদানকারীর সাথে সাইন আপ করেছেন এবং প্রয়োজনীয় প্রমাণীকরণ শংসাপত্র (API_KEY বা টোকেন) পেয়েছেন। Azure OpenAI এর ক্ষেত্রে, আমরা ধরে নিচ্ছি যে আপনার কাছে একটি বৈধ Azure OpenAI পরিষেবার মোতায়েন (এন্ডপয়েন্ট) রয়েছে যার সাথে অন্তত একটি GPT মডেল চ্যাট সম্পূর্ণতার জন্য মোতায়েন করা হয়েছে।

পরবর্তী পদক্ষেপটি আপনার **লোকাল পরিবেশের ভেরিয়েবলগুলি** নিম্নরূপ কনফিগার করা:

1. মূল ফোল্ডারে `.env.copy` ফাইলটি দেখুন যার বিষয়বস্তু নিম্নরূপ হওয়া উচিত:

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

2. নিচের কমান্ড ব্যবহার করে `.env` এ সেই ফাইলটি কপি করুন। এই ফাইলটি _gitignore-d_, যা গোপনীয়তা রক্ষা করে।

   ```bash
   cp .env.copy .env
   ```

3. পরবর্তী বিভাগে বর্ণিত হিসাবে মানগুলি পূরণ করুন (ডানদিকে `=` এর পাশে প্লেসহোল্ডারগুলি প্রতিস্থাপন করুন)।

3. (ঐচ্ছিক) আপনি যদি GitHub Codespaces ব্যবহার করেন, তাহলে আপনার কাছে এই রিপোজিটরির সাথে সম্পর্কিত _Codespaces secrets_ হিসাবে পরিবেশের ভেরিয়েবলগুলি সংরক্ষণ করার বিকল্প রয়েছে। সেই ক্ষেত্রে, আপনাকে একটি লোকাল .env ফাইল সেটআপ করতে হবে না। **তবে, লক্ষ্য করুন যে এই বিকল্পটি কেবলমাত্র আপনি যদি GitHub Codespaces ব্যবহার করেন তখনই কাজ করে।** আপনি যদি Docker Desktop ব্যবহার করেন তবে আপনাকে এখনও .env ফাইল সেটআপ করতে হবে।

### ২.২. `.env` ফাইল পূরণ করুন

ভেরিয়েবলগুলি কী প্রতিনিধিত্ব করে তা বুঝতে দ্রুত দেখে নেওয়া যাক:

| ভেরিয়েবল  | বর্ণনা  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | এটি আপনার প্রোফাইলে সেটআপ করা ইউজার অ্যাক্সেস টোকেন |
| OPENAI_API_KEY | এটি OpenAI এন্ডপয়েন্টগুলির জন্য সার্ভিস ব্যবহারের অনুমোদন কী |
| AZURE_OPENAI_API_KEY | এটি সেই সার্ভিস ব্যবহারের অনুমোদন কী |
| AZURE_OPENAI_ENDPOINT | এটি একটি Azure OpenAI সম্পদের জন্য মোতায়েনকৃত এন্ডপয়েন্ট |
| AZURE_OPENAI_DEPLOYMENT | এটি _টেক্সট জেনারেশন_ মডেল মোতায়েন এন্ডপয়েন্ট |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | এটি _টেক্সট এম্বেডিং_ মডেল মোতায়েন এন্ডপয়েন্ট |
| | |

নোট: শেষ দুটি Azure OpenAI ভেরিয়েবল যথাক্রমে চ্যাট সম্পূর্ণতার জন্য (টেক্সট জেনারেশন) এবং ভেক্টর অনুসন্ধানের জন্য (এম্বেডিং) একটি ডিফল্ট মডেল প্রতিফলিত করে। সেগুলি সেটআপ করার জন্য নির্দেশাবলী প্রাসঙ্গিক অ্যাসাইনমেন্টে সংজ্ঞায়িত করা হবে।

### ২.৩. Azure কনফিগার করুন: পোর্টাল থেকে

Azure OpenAI এন্ডপয়েন্ট এবং কী মানগুলি [Azure পোর্টাল](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) এ পাওয়া যাবে তাই চলুন সেখানে শুরু করি।

1. [Azure পোর্টাল](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) এ যান
1. সাইডবারে (বাম মেনুতে) **Keys and Endpoint** অপশনটি ক্লিক করুন।
1. **Show Keys** ক্লিক করুন - আপনি নিম্নলিখিত দেখতে পাবেন: KEY 1, KEY 2 এবং এন্ডপয়েন্ট।
1. AZURE_OPENAI_API_KEY এর জন্য KEY 1 মান ব্যবহার করুন
1. AZURE_OPENAI_ENDPOINT এর জন্য এন্ডপয়েন্ট মান ব্যবহার করুন

এরপর, আমরা যে নির্দিষ্ট মডেলগুলি মোতায়েন করেছি তার জন্য এন্ডপয়েন্টগুলির প্রয়োজন হবে।

1. Azure OpenAI সম্পদের জন্য সাইডবারে (বাম মেনুতে) **Model deployments** অপশনটি ক্লিক করুন।
1. গন্তব্য পৃষ্ঠায়, **Manage Deployments** ক্লিক করুন

এটি আপনাকে Azure OpenAI Studio ওয়েবসাইটে নিয়ে যাবে, যেখানে আমরা নিচে বর্ণিত অন্য মানগুলি পাব।

### ২.৪. Azure কনফিগার করুন: স্টুডিও থেকে

1. [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) এ **আপনার সম্পদ থেকে** যেমন উপরে বর্ণিত হয়েছে সেখানে যান।
1. বর্তমানে মোতায়েনকৃত মডেলগুলি দেখতে সাইডবার (বামে) **Deployments** ট্যাবটি ক্লিক করুন।
1. যদি আপনার পছন্দের মডেল মোতায়েন না হয়, তাহলে **Create new deployment** ব্যবহার করে এটি মোতায়েন করুন।
1. আপনার একটি _টেক্সট-জেনারেশন_ মডেল প্রয়োজন হবে - আমরা সুপারিশ করি: **gpt-35-turbo**
1. আপনার একটি _টেক্সট-এম্বেডিং_ মডেল প্রয়োজন হবে - আমরা সুপারিশ করি **text-embedding-ada-002**

এখন পরিবেশের ভেরিয়েবলগুলি আপডেট করুন যাতে মোতায়েন নাম প্রতিফলিত হয়। এটি সাধারণত মডেলের নামের সাথে একই হবে যদি না আপনি এটি স্পষ্টভাবে পরিবর্তন করেন। সুতরাং, উদাহরণস্বরূপ, আপনার থাকতে পারে:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**কাজ শেষ হলে .env ফাইলটি সংরক্ষণ করতে ভুলবেন না**। আপনি এখন ফাইলটি থেকে বেরিয়ে এসে নোটবুক চালানোর নির্দেশাবলীতে ফিরে যেতে পারেন।

### ২.৫. OpenAI কনফিগার করুন: প্রোফাইল থেকে

আপনার OpenAI API কীটি আপনার [OpenAI অ্যাকাউন্ট](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) এ পাওয়া যাবে। যদি আপনার না থাকে, তাহলে আপনি একটি অ্যাকাউন্টের জন্য সাইন আপ করতে পারেন এবং একটি API কী তৈরি করতে পারেন। একবার আপনি কীটি পেয়ে গেলে, আপনি এটি `.env` ফাইলে `OPENAI_API_KEY` ভেরিয়েবল পূরণ করতে ব্যবহার করতে পারেন।

### ২.৬. Hugging Face কনফিগার করুন: প্রোফাইল থেকে

আপনার Hugging Face টোকেন আপনার প্রোফাইলে [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) এর অধীনে পাওয়া যাবে। এগুলি সর্বজনীনভাবে পোস্ট বা শেয়ার করবেন না। পরিবর্তে, এই প্রকল্পের ব্যবহারের জন্য একটি নতুন টোকেন তৈরি করুন এবং `.env` ফাইলের `HUGGING_FACE_API_KEY` ভেরিয়েবলের অধীনে এটি কপি করুন। _নোট:_ এটি প্রযুক্তিগতভাবে একটি API কী নয় কিন্তু প্রমাণীকরণের জন্য ব্যবহৃত হয় তাই আমরা সামঞ্জস্যতার জন্য সেই নামকরণ কনভেনশন বজায় রাখছি।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিকতার জন্য চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।