# একটি LLM প্রোভাইডার বাছাই এবং কনফিগার করা 🔑

অ্যাসাইনমেন্টগুলি **হতে পারে** এক বা একাধিক বড় ভাষা মডেল (LLM) ডিপ্লয়মেন্টের বিরুদ্ধে কাজ করার জন্য একটি সমর্থিত সার্ভিস প্রোভাইডার যেমন OpenAI, Azure বা Hugging Face এর মাধ্যমে সেটআপ করা। এগুলো একটি _হোস্টেড এন্ডপয়েন্ট_ (API) প্রদান করে যা আমরা সঠিক ক্রেডেনশিয়ালস (API কী বা টোকেন) দিয়ে প্রোগ্রাম্যাটিকালি অ্যাক্সেস করতে পারি। এই কোর্সে, আমরা এই প্রোভাইডারগুলো নিয়ে আলোচনা করি:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) বিভিন্ন মডেল সহ যার মধ্যে মূল GPT সিরিজ অন্তর্ভুক্ত।
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI মডেলসমূহের জন্য এন্টারপ্রাইজ প্রস্তুতির প্রতি ফোকাসসহ
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) একটি একক এন্ডপয়েন্ট এবং API কী দিয়ে OpenAI, Meta, Mistral, Cohere, Microsoft এবং অন্যান্য অনেক মডেলে অ্যাক্সেসের জন্য (GitHub Models এর পরিবর্তে, যা জুলাই ২০২৬ শেষে অবসান হচ্ছে)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ওপেন-সোর্স মডেল এবং ইনফারেন্স সার্ভারের জন্য
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) অথবা [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) যদি আপনি সম্পূৰ্ণ অফলাইনে আপনার নিজস্ব ডিভাইসে মডেল চালাতে চান, কোন ক্লাউড সাবস্ক্রিপশন ছাড়াই

**এই অনুশীলনগুলির জন্য আপনাকে নিজের অ্যাকাউন্ট ব্যবহার করতে হবে।** অ্যাসাইনমেন্টগুলি ঐচ্ছিক, তাই আপনি আপনার আগ্রহ অনুসারে এক, সব অথবা কোন প্রোভাইডার সেটআপ করতে পারেন বা না-ও করতে পারেন। সাইনআপের জন্য কিছু নির্দেশিকা:

| সাইনআপ | খরচ | API কী | প্লেগ্রাউন্ড | মন্তব্য |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [মূল্য নির্ধারণ](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [প্রোজেক্ট-ভিত্তিক](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [নো-কোড, ওয়েব](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | একাধিক মডেল উপলব্ধ |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [মূল্য নির্ধারণ](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK দ্রুত শুরু](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [স্টুডিও দ্রুত শুরু](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [অ্যাক্সেসের জন্য আগে আবেদন করতে হবে](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [মূল্য নির্ধারণ](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [প্রোজেক্ট ওভারভিউ পেজ](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry প্লেগ্রাউন্ড](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | বিনামূল্যের স্তর উপলব্ধ; একাধিক মডেল প্রোভাইডারের জন্য এক এন্ডপয়েন্ট + কী |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [মূল্য নির্ধারণ](https://huggingface.co/pricing) | [অ্যাক্সেস টোকেন](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat’এর মডেল সীমিত](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | ফ্রি (আপনার ডিভাইসে চালানো হয়) | প্রয়োজন নেই | [লোকাল CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | সম্পূর্ণ অফলাইন, OpenAI-অনুকূল এন্ডপয়েন্ট |
| | | | | |

নিচের নির্দেশনা অনুসরণ করে এই রিপোজিটরিটি বিভিন্ন প্রোভাইডারের জন্য _কনফিগার_ করুন। নির্দিষ্ট প্রোভাইডারের প্রয়োজন এমন অ্যাসাইনমেন্টগুলির ফাইলনেমে এই ট্যাগগুলোর একটি থাকবে:

- `aoai` - Azure OpenAI এন্ডপয়েন্ট, কী প্রয়োজন
- `oai` - OpenAI এন্ডপয়েন্ট, কী প্রয়োজন
- `hf` - Hugging Face টোকেন প্রয়োজন
- `githubmodels` - Microsoft Foundry Models এন্ডপয়েন্ট, কী প্রয়োজন (GitHub Models জুলাই ২০২৬ শেষে অবসান হচ্ছে)

আপনি এক, কোনটিও বা সব প্রোভাইডার কনফিগার করতে পারেন। সম্পর্কিত অ্যাসাইনমেন্ট গুলো ক্রেডেনশিয়ালস অনুপস্থিত থাকলে ত্রুটি দেখাবে।

## `.env` ফাইল তৈরি করুন

আমরা ধরে নিচ্ছি আপনি উপরের নির্দেশিকা পড়ে প্রযোজ্য প্রোভাইডারে সাইন আপ করেছেন এবং প্রয়োজনীয় প্রমাণীকরণ ক্রেডেনশিয়াল (API_KEY বা টোকেন) পেয়েছেন। Azure OpenAI এর ক্ষেত্রে, আপনার কাছে অন্তত একটি GPT মডেল ডিপ্লয়েড একটি বৈধ Azure OpenAI সার্ভিস (এন্ডপয়েন্ট) ডিপ্লয়মেন্ট আছে।

পরবর্তী ধাপ হল আপনার **লোকাল পরিবেশ ভেরিয়েবলসমূহ** নিম্নরূপ কনফিগার করা:

1. রুট ফোল্ডারে `.env.copy` নামে একটি ফাইল খুঁজুন যা এরকম কিছু থাকার কথা:

   ```bash
   # OpenAI প্রদানকারী
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## মাইক্রোসফট ফাউন্ড্রিতে Azure OpenAI
   ## (Azure OpenAI সার্ভিস এখন মাইক্রোসফট ফাউন্ড্রির অংশ: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # ডিফল্ট সেট করা হয়েছে! (বর্তমান স্থির GA API সংস্করণ)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## মাইক্রোসফট ফাউন্ড্রি মডেলস (মাল্টি-প্রোভাইডার মডেল ক্যাটালগ, যা গিটহাব মডেলসের পরিবর্তে, যা জুলাই ২০২৬ এর শেষের দিকে অবসর গ্রহণ করবে)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## হাগিং ফেস
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. নিচের কমান্ড ব্যবহার করে ফাইলটি `.env` নামে কপি করুন। এই ফাইলটি _gitignore করা হয়েছে_, ফলে সিক্রেটস সুরক্ষিত থাকে।

   ```bash
   cp .env.copy .env
   ```

3. পরবর্তী অংশে বর্ণিত অনুসারে মানগুলো পূরণ করুন (দাঁয়েতে `=` চিহ্নের পাশে প্লেসহোল্ডারগুলি প্রতিস্থাপন করুন)।

4. (ঐচ্ছিক) যদি আপনি GitHub Codespaces ব্যবহার করেন, তবে আপনি পরিবেশ ভেরিয়েবলসমূহ _Codespaces secrets_ হিসাবে সংরক্ষণ করার অপশন পাবেন যেটা এই রিপোজিটরির সাথে যুক্ত থাকবে। সেই ক্ষেত্রে, লোকাল .env ফাইল সেটআপ করার প্রয়োজন হবে না। **তবে লক্ষ্য করুন এই অপশন শুধুমাত্র GitHub Codespaces ব্যবহার করলে কাজ করে।** Docker Desktop ব্যবহার করলে এখনও .env ফাইল সেটআপ করতে হবে।

## `.env` ফাইল পূরণ করুন

চলুন দ্রুত ভেরিয়েবল নামগুলো দেখি যাতে আমরা বুঝতে পারি এগুলো কী বোঝায়:

| ভেরিয়েবল  | বর্ণনা  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | এটি ব্যবহারকারীর অ্যাক্সেস টোকেন যা আপনি আপনার প্রোফাইলে সেটআপ করেছেন |
| OPENAI_API_KEY | এটি সার্ভিস ব্যবহারের অনুমোদন কী, নন-Azure OpenAI এন্ডপয়েন্টের জন্য |
| AZURE_OPENAI_API_KEY | এটি ঐ সার্ভিস ব্যবহার করার অনুমোদন কী |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI রিসোর্সের ডিপ্লয় করা এন্ডপয়েন্ট |
| AZURE_OPENAI_DEPLOYMENT | এটি _টেক্সট জেনারেশন_ মডেলের ডিপ্লয়মেন্ট এন্ডপয়েন্ট |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | এটি _টেক্সট এমবেডডিংস_ মডেল ডিপ্লয়মেন্ট এন্ডপয়েন্ট |
| AZURE_INFERENCE_ENDPOINT | এটি আপনার Microsoft Foundry প্রোজেক্টের এন্ডপয়েন্ট, Microsoft Foundry Models ব্যবহারের জন্য |
| AZURE_INFERENCE_CREDENTIAL | এটি আপনার Microsoft Foundry প্রোজেক্টের API কী |
| | |

নোট: শেষ দুটি Azure OpenAI ভেরিয়েবল যথাক্রমে চ্যাট সম্পন্ন করার জন্য (টেক্সট জেনারেশন) এবং ভেক্টর সার্চ (এম্বেডডিংস) ডিফল্ট মডেল নির্দেশ করে। এগুলো কিভাবে সেট করতে হবে তা সম্পর্কিত অ্যাসাইনমেন্টে উল্লেখ থাকবে।

## Azure OpenAI কনফিগার করুন: পোর্টাল থেকে

> **নোট:** Azure OpenAI সার্ভিস এখন [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)-এর অংশ। রিসোর্স এবং ডিপ্লয়মেন্ট Azure পোর্টালে দেখা যাবে, কিন্তু দৈনন্দিন মডেল ব্যবস্থাপনা (ডিপ্লয়মেন্ট, প্লে গ্রাউন্ড, মনিটরিং) এখন পুরনো স্ট্যান্ডঅ্যালোন "Azure OpenAI Studio" এর পরিবর্তে Foundry পোর্টালে হয়।

Azure OpenAI এন্ডপয়েন্ট এবং কী এর মানগুলি [Azure পোর্টাল](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) এ পাওয়া যাবে, তাই শুরু করা যাক সেখানে থেকে।

1. [Azure পোর্টাল](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) এ যান
1. সাইডবারে (বাম মেনুতে) **Keys and Endpoint** বিকল্পে ক্লিক করুন।
1. **Show Keys** এ ক্লিক করুন - আপনি নিম্নলিখিত দেখতে পাবেন: KEY 1, KEY 2 এবং Endpoint।
1. AZURE_OPENAI_API_KEY এর জন্য KEY 1 মান ব্যবহার করুন
1. AZURE_OPENAI_ENDPOINT এর জন্য Endpoint মান ব্যবহার করুন

এবার, আমাদের ডিপ্লয় করা নির্দিষ্ট মডেলের এন্ডপয়েন্ট দরকার।

1. Azure OpenAI রিসোর্সের সাইডবারে (বাম মেনুতে) **Model deployments** বিকল্পে ক্লিক করুন।
1. গন্তব্য পেজে, **Go to Microsoft Foundry portal** (বা **Manage Deployments**, আপনার রিসোর্সের ধরন অনুসারে) এ ক্লিক করুন।

এটি আপনাকে Microsoft Foundry পোর্টালে নিয়ে যাবে, যেখানে আমরা নিচের মতো মান পেয়ে যাব।

## Azure OpenAI কনফিগার করুন: Microsoft Foundry পোর্টাল থেকে

1. উপরে বর্ণিত অনুসারে [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) এ আপনার রিসোর্স থেকে প্রবেশ করুন।
1. বর্তমানে ডিপ্লয় করা মডেল দেখতে **Deployments** ট্যাবে (সাইডবার, বাম) ক্লিক করুন।
1. আপনার কাঙ্খিত মডেল ডিপ্লয় করা না থাকলে, **Deploy model** ব্যবহার করে এটি [মডেল ক্যাটালগ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) থেকে ডিপ্লয় করুন।
1. আপনার একটি _টেক্সট-জেনারেশন_ মডেল দরকার - আমরা সুপারিশ করি: **gpt-4o-mini**
1. আপনার একটি _টেক্সট-এম্বেডিং_ মডেল দরকার - আমরা সুপারিশ করি **text-embedding-3-small**

এখন পরিবেশ ভেরিয়েবলগুলো আপডেট করুন যাতে _ডিপ্লয়মেন্ট নাম_ প্রতিফলিত হয়। সাধারণত এটি মডেলের নামের মতোই হয় যদি আপনি আলাদা করে নাম না দেন। উদাহরণস্বরূপ, আপনি থাকতে পারেন:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**শেষে .env ফাইল সংরক্ষণ করতে ভুলবেন না**। ফাইল থেকে বের হয়ে নোটবুক চালানোর নির্দেশনায় ফিরে যেতে পারেন।

## OpenAI কনফিগার করুন: প্রোফাইল থেকে

আপনার OpenAI API কী আপনার [OpenAI অ্যাকাউন্টে](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) পাওয়া যাবে। যদি না থাকে, একটি অ্যাকাউন্ট তৈরি করে API কী তৈরি করুন। একবার কী পেলে আপনি `.env` ফাইলে `OPENAI_API_KEY` ভেরিয়েবল পূরণ করতে পারবেন।

## Hugging Face কনফিগার করুন: প্রোফাইল থেকে

আপনার Hugging Face টোকেন আপনার প্রোফাইলে [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) অংশে পাওয়া যাবে। এগুলো জনসমক্ষে পোস্ট বা শেয়ার করবেন না। পরিবর্তে, এই প্রোজেক্টের জন্য একটি নতুন টোকেন তৈরি করুন এবং সেটি `.env` ফাইলে `HUGGING_FACE_API_KEY` ভেরিয়েবলে কপি করুন। _দ্রষ্টব্য:_ এটি প্রযুক্তিগতভাবে API কী নয় কিন্তু প্রমাণীকরণের জন্য ব্যবহৃত হয় তাই ধারাবাহিকতার জন্য সেই নাম ব্যবহার করা হচ্ছে।

## Microsoft Foundry Models কনফিগার করুন: পোর্টাল থেকে

> **নোট:** GitHub Models জুলাই ২০২৬ শেষে অবসান হচ্ছে। Microsoft Foundry Models সরাসরি বিকল্প, একই ফ্রি-টু-ট্রাই মডেল ক্যাটালগ এবং Azure AI Inference SDK / OpenAI SDK অভিজ্ঞতা প্রদান করে।

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) এ যান এবং একটি Foundry প্রোজেক্ট তৈরি (বা খুলুন) করুন।
1. [মডেল ক্যাটালগ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ব্রাউজ করুন এবং একটি মডেল ডিপ্লয় করুন, যেমন `gpt-4o-mini`।
1. প্রোজেক্টের **Overview** পেজে গিয়ে **এন্ডপয়েন্ট** এবং **API কী** কপি করুন।
1. `.env` ফাইলে `AZURE_INFERENCE_ENDPOINT` এর জন্য এন্ডপয়েন্ট মান এবং `AZURE_INFERENCE_CREDENTIAL` এর জন্য কী মান ব্যবহার করুন।

## অফলাইন / লোকাল প্রোভাইডার

যদি আপনি ক্লাউড সাবস্ক্রিপশন ব্যবহার করতে না চান, তাহলে আপনি উপযুক্ত ওপেন মডেল সরাসরি আপনার নিজের ডিভাইসে চালাতে পারেন:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft এর অন-ডিভাইস রানটাইম। এটি স্বয়ংক্রিয়ভাবে সেরা এক্সিকিউশন প্রোভাইডার (NPU, GPU, অথবা CPU) বেছে নেয় এবং একটি OpenAI-অনুকূল এন্ডপয়েন্ট উন্মোচন করে, তাই আপনি এই কোর্সের বেশিরভাগ নমুনা কোড খুব কম পরিবর্তনে ব্যবহার করতে পারবেন। শুরু করতে [Foundry Local ডকুমেন্টেশন](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) দেখুন, অথবা ইনস্টল করুন `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) দিয়ে।
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - একটি জনপ্রিয় বিকল্প যা Llama, Phi, Mistral এবং Gemma মত ওপেন মডেল লোকালি চালাতে দেয়।


উভয় বিকল্প ব্যবহার করে হাতে কলমে উদাহরণের জন্য [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) দেখুন।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->