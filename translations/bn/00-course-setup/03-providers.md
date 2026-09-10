# একটি LLM প্রদানকারী নির্বাচন ও কনফিগার করা 🔑

অ্যাসাইনমেন্টগুলো **হতে পারে** এক বা একাধিক বড় ভাষা মডেল (LLM) ডিপ্লয়মেন্টের বিরুদ্ধে কাজ করার জন্য একটিমাত্র সমর্থিত পরিষেবা প্রদানকারীর মাধ্যমে যেমন OpenAI, Azure বা Hugging Face। এগুলো একটি _হোস্টেড এন্ডপয়েন্ট_ (API) সরবরাহ করে যা আমরা প্রোগ্রাম্যাটিকভাবে প্রাপ্তি করতে পারি সঠিক পরিচয়পত্র (API কী বা টোকেন) দিয়ে। এই কোর্সে আমরা এই প্রোভাইডারগুলো আলোচনা করব:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) বিভিন্ন মডেলের সাথে যার মধ্যে রয়েছে মূল GPT সিরিজ।
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) OpenAI মডেলের জন্য প্রতিষ্ঠান-অনুকূলতাকে কেন্দ্র করে
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) একটি একক এন্ডপয়েন্ট ও API কী ব্যবহার করে OpenAI, Meta, Mistral, Cohere, Microsoft ইত্যাদি অনেক মডেল অ্যাক্সেস করার জন্য (GitHub Models এর বিকল্প, যা জুলাই ২০২৬ এর শেষ নাগাদ অবসর নেবে)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ওপেন-সোর্স মডেল ও ইনফারেন্স সার্ভারের জন্য
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) অথবা [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) যদি আপনি চাইতে পারেন নিজস্ব ডিভাইসে সম্পূর্ণ অফলাইন মডেল চালাবেন, কোন ক্লাউড সাবস্ক্রিপশন প্রয়োজন নেই

**এই অ্যাক্সারসাইজগুলো করার জন্য আপনাকে আপনার নিজস্ব অ্যাকাউন্ট ব্যবহার করতে হবে**। অ্যাসাইনমেন্টগুলো ঐচ্ছিক, তাই আপনি আপনার আগ্রহ অনুযায়ী এক বা সব অথবা কোন প্রোভাইডারই সেটআপ করতে পারেন না। সাইনআপের জন্য কিছু নির্দেশিকা:

| সাইনআপ | খরচ | API কী | প্লেগ্রাউন্ড | মন্তব্য |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [মূল্য নির্ধারণ](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [প্রকল্প ভিত্তিক](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [নো-কোড, ওয়েব](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | একাধিক মডেল উপলব্ধ |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [মূল্য নির্ধারণ](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK কুইকস্টার্ট](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [স্টুডিও কুইকস্টার্ট](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [অ্যাক্সেসের জন্য আগাম আবেদন করতে হবে](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [মূল্য নির্ধারণ](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [প্রকল্প ওভারভিউ পৃষ্ঠা](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry প্লেগ্রাউন্ড](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | ফ্রি টিয়ার উপলব্ধ; একাধিক মডেল প্রোভাইডারের জন্য এক এন্ডপয়েন্ট ও কী |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [মূল্য নির্ধারণ](https://huggingface.co/pricing) | [অ্যাক্সেস টোকেন](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat এর সীমিত মডেল](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | ফ্রি (আপনার ডিভাইসে চলে) | প্রয়োজন নেই | [লোকাল CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | সম্পূর্ণ অফলাইন, OpenAI-কম্প্যাটিবল এন্ডপয়েন্ট |
| | | | | |

নিচের নির্দেশনা অনুসরণ করে এই রিপোজিটরিটিকে বিভিন্ন প্রোভাইডারের সাথে ব্যবহার করার জন্য _কনফিগার_ করুন। নির্দিষ্ট প্রোভাইডার প্রয়োজন এমন অ্যাসাইনমেন্টের ফাইলনেমে নিম্নলিখিত কোনও ট্যাগ থাকবে:

- `aoai` - Azure OpenAI এন্ডপয়েন্ট, কী প্রয়োজন
- `oai` - OpenAI এন্ডপয়েন্ট, কী প্রয়োজন
- `hf` - Hugging Face টোকেন প্রয়োজন
- `githubmodels` - Microsoft Foundry Models এন্ডপয়েন্ট, কী প্রয়োজন (GitHub Models জুলাই ২০২৬ এর শেষে অবসর নিবে)

আপনি একটি, শূন্য অথবা সবগুলো প্রোভাইডার কনফিগার করতে পারেন। সংশ্লিষ্ট অ্যাসাইনমেন্টগুলোর ক্ষেত্রে প্রয়োজনীয় পরিচয়পত্র না থাকলে শুধু এরর দেখাবে।

## `.env` ফাইল তৈরি করুন

আমরা ধরে নিচ্ছি আপনি উপরের নির্দেশিকা পড়ে সংশ্লিষ্ট প্রোভাইডারে সাইন আপ করে প্রয়োজনীয় প্রমাণীকরণ তথ্য (API_KEY বা টোকেন) সংগ্রহ করেছেন। Azure OpenAI এর ক্ষেত্রে, আমরা ধরে নিচ্ছি আপনার কাছে Azure OpenAI সার্ভিসের একটি বৈধ ডিপ্লয়মেন্ট (এন্ডপয়েন্ট) আছে, যেখানে অন্তত একটি GPT মডেল চ্যাট কমপ্লিশনের জন্য ডিপ্লয় করা আছে।

পরবর্তী ধাপ হল আপনার **লোকাল পরিবেশ ভেরিয়েবলগুলি** এখানে কনফিগার করা:

১. রুট ফোল্ডারে `.env.copy` ফাইল দেখুন, যা নিচের মতো বিষয়বস্তু থাকবে:

   ```bash
   # OpenAI প্রদানকারী
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## মাইক্রোসফট ফাউন্ড্রিতে Azure OpenAI
   ## (Azure OpenAI পরিষেবা এখন মাইক্রোসফট ফাউন্ড্রির অংশ: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # ডিফল্ট সেট করা হয়েছে! (বর্তমান স্থিতিশীল GA API সংস্করণ)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## মাইক্রোসফট ফাউন্ড্রি মডেলসমূহ (বহু-প্রদানকারী মডেল ক্যাটালগ, GitHub মডেলগুলোর পরিবর্তে, যা জুলাই ২০২৬ এর শেষে অবসর নিচ্ছে)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

২. নিচের কমান্ড দিয়ে ফাইলটি `.env` নামে কপি করুন। এই ফাইলটি _gitignore-এ রাখা হয়েছে_, গোপনীয়তা সুরক্ষিত রাখে।

   ```bash
   cp .env.copy .env
   ```

৩. মানগুলো পূরণ করুন (`=` এর ডান পাশে প্লেসহোল্ডার পরিবর্তন করুন), নিচের অংশে বর্ণিত অনুযায়ী।

৪. (ঐচ্ছিক) যদি আপনি GitHub Codespaces ব্যবহার করেন, তাহলে এই রিপোজিটরির সাথে যুক্ত _Codespaces secrets_ হিসেবে পরিবেশ ভেরিয়েবলগুলি সংরক্ষণ করার অপশন পাবেন। সেই ক্ষেত্রে আপনাকে লোকাল .env ফাইল সেটআপ করার দরকার হবে না। **তবে, এই অপশন শুধুমাত্র GitHub Codespaces এর জন্যই কার্যকর।** Docker Desktop ব্যবহার করলে অবশ্য .env ফাইল সেটআপ করতে হবে।

## `.env` ফাইল পূরণ করুন

চলুন ভেরিয়েবল নামগুলো দেখে নেই, তারা কী প্রতিনিধিত্ব করে:

| ভেরিয়েবল  | বর্ণনা  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | এটি হল ব্যবহারকারী অ্যাক্সেস টোকেন যা আপনি আপনার প্রোফাইলে সেটআপ করেছেন |
| OPENAI_API_KEY | এটি হলো নন-Azure OpenAI এন্ডপয়েন্ট ব্যবহারের জন্য অনুমোদন কী |
| AZURE_OPENAI_API_KEY | এটি সেই পরিষেবার ব্যবহার অনুমোদনের কী |
| AZURE_OPENAI_ENDPOINT | এটি Azure OpenAI রিসোর্সের ডিপ্লয়মেন্ট এন্ডপয়েন্ট |
| AZURE_OPENAI_DEPLOYMENT | এটি _টেক্সট জেনারেশন_ মডেল ডিপ্লয়মেন্ট এন্ডপয়েন্ট |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | এটি _টেক্সট এম্বেডিংস_ মডেল ডিপ্লয়মেন্ট এন্ডপয়েন্ট |
| AZURE_INFERENCE_ENDPOINT | এটি Microsoft Foundry প্রকল্পের এন্ডপয়েন্ট, Microsoft Foundry মডেলের জন্য ব্যবহৃত |
| AZURE_INFERENCE_CREDENTIAL | এটি Microsoft Foundry প্রকল্পের API কী |
| | |

নোট: শেষ দুইটি Azure OpenAI ভেরিয়েবল চ্যাট কমপ্লিশন (টেক্সট জেনারেশন) ও ভেক্টর অনুসন্ধান (এম্বেডিংস) এর জন্য ডিফল্ট মডেল প্রতিফলিত করে। এগুলো কিভাবে সেটআপ করতে হবে তা সংশ্লিষ্ট অ্যাসাইনমেন্টে বর্ণিত হবে।

## Azure OpenAI কনফিগার করুন: পোর্টাল থেকে

> **নোট:** Azure OpenAI সার্ভিস এখন [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) এর অংশ। রিসোর্স ও ডিপ্লয়মেন্টগুলো এখনো Azure পোর্টালে প্রদর্শিত হয়, তবে দৈনন্দিন মডেল ব্যবস্থাপনা (ডিপ্লয়মেন্ট, প্লেগ্রাউন্ড, মনিটরিং) Foundry পোর্টালে ঘটে, পুরনো আলাদা "Azure OpenAI Studio" এর বদলে।

Azure OpenAI এন্ডপয়েন্ট ও কী মান [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)-এ পাওয়া যাবে, তাই শুরু করা যাক।

১. যান [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
১. সাইডবারের (বাম মেনু) **Keys and Endpoint** অপশনে ক্লিক করুন।
১. **Show Keys** ক্লিক করুন - KEY 1, KEY 2 এবং Endpoint দেখতে পাবেন।
১. AZURE_OPENAI_API_KEY এর জন্য KEY 1 মান ব্যবহার করুন
১. AZURE_OPENAI_ENDPOINT এর জন্য Endpoint মান ব্যবহার করুন

পরবর্তী, আমাদের প্রয়োজন যেসব মডেলের এন্ডপয়েন্ট নির্দিষ্ট।

১. Azure OpenAI রিসোর্সের জন্য সাইডবারের **Model deployments** অপশনে ক্লিক করুন।
১. গন্তব্য পৃষ্ঠায়, **Go to Microsoft Foundry portal** (বা **Manage Deployments**, রিসোর্স টাইপ অনুসারে) ক্লিক করুন

এটি আপনাকে Microsoft Foundry পোর্টালে নিয়ে যাবে, যেখানে নিচে বর্ণিত অন্যান্য মানগুলো পাওয়া যাবে।

## Azure OpenAI কনফিগার করুন: Microsoft Foundry পোর্টাল থেকে

১. উপরে বর্ণিত মতে [Microsoft Foundry পোর্টালে](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) যান **আপনার রিসোর্স থেকে**
১. সাইডবার (বাম) **Deployments** ট্যাব ক্লিক করে বর্তমানে ডিপ্লয়কৃত মডেল দেখুন।
১. আপনার কাঙ্ক্ষিত মডেল যদি ডিপ্লয় না করা থাকে, [মডেল ক্যাটালগ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) থেকে **Deploy model** ব্যবহার করে ডিপ্লয় করুন।
১. একটি _টেক্সট-জেনারেশন_ মডেল প্রয়োজন - আমরা সুপারিশ করি: **gpt-5-mini**
১. একটি _টেক্সট-এম্বেডিং_ মডেল প্রয়োজন - আমরা সুপারিশ করি **text-embedding-3-small**

এখন পরিবেশ ভেরিয়েবলগুলিকে আপডেট করুন ডিপ্লয়মেন্টের নাম প্রতিফলিত করার জন্য। এটি সাধারণত মডেলের নামের সমান হয় যদি আপনি স্পষ্টভাবে পরিবর্তন না করেন। উদাহরণস্বরূপ, আপনি থাকতে পারেন:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**কাজ শেষ হলে .env ফাইলটি সংরক্ষণ করতে ভুলবেন না**। এখন ফাইল থেকে বেরিয়ে আসুন এবং নোটবুক চালানোর নির্দেশনায় ফিরে যান।

## OpenAI কনফিগার করুন: প্রোফাইল থেকে

আপনার OpenAI API কী আপনার [OpenAI অ্যাকাউন্ট](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) এ পাওয়া যাবে। যদি না থাকে, একাউন্ট খুলে একটি API কী তৈরি করুন। কী পাওয়ার পরে, .env ফাইলে `OPENAI_API_KEY` ভেরিয়েবলে সেট করুন।

## Hugging Face কনফিগার করুন: প্রোফাইল থেকে

আপনার Hugging Face টোকেনটি আপনার প্রোফাইলে [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) অংশে পাওয়া যাবে। এগুলো প্রকাশ্যে পোস্ট বা শেয়ার করবেন না। বরং এই প্রকল্পের জন্য একটি নতুন টোকেন তৈরি করুন এবং সেটি `.env` ফাইলে `HUGGING_FACE_API_KEY` ভেরিয়েবলে রাখুন। _নোট:_ এটি প্রযুক্তিগত দিক থেকে API কী নয়, তবে প্রমাণীকরণের জন্য ব্যবহৃত হয়, তাই নামকরণ শৈলী ধরে রাখা হয়েছে।

## Microsoft Foundry Models কনফিগার করুন: পোর্টাল থেকে

> **নোট:** GitHub Models জুলাই ২০২৬ এর শেষে অবসর নিবে। Microsoft Foundry Models সরাসরি এর বিকল্প, একই ফ্রি-টু-ট্রাই মডেল ক্যাটালগ ও Azure AI Inference SDK / OpenAI SDK অভিজ্ঞতা প্রদান করে।

১. যান [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) এবং একটি Foundry প্রকল্প তৈরি বা খুলুন।
১. [মডেল ক্যাটালগ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ব্রাউজ করে একটি মডেল ডিপ্লয় করুন, উদাহরণস্বরূপ `gpt-5-mini`।
১. প্রকল্পের **ওভারভিউ** পেজে গিয়ে **এন্ডপয়েন্ট** এবং **API কী** কপি করুন।
১. `.env` ফাইলে `AZURE_INFERENCE_ENDPOINT` এর জন্য এন্ডপয়েন্ট মান এবং `AZURE_INFERENCE_CREDENTIAL` এর জন্য কী মান ব্যবহার করুন।

## অফলাইন / লোকাল প্রোভাইডার

আপনি যদি ক্লাউড সাবস্ক্রিপশন ব্যবহার না করতে চান, তবে আপনি সামঞ্জস্যপূর্ণ ওপেন মডেলগুলো সরাসরি আপনার নিজের ডিভাইসে চালাতে পারেন:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft-এর অন-ডিভাইস রানটাইম। এটি স্বয়ংক্রিয়ভাবে সেরা এক্সিকিউশন প্রোভাইডার (NPU, GPU, অথবা CPU) বেছে নেয় এবং OpenAI-কম্প্যাটিবল এন্ডপয়েন্ট প্রদান করে, তাই আপনি এই কোর্সের বেশিরভাগ স্যাম্পল কোড খুব কম পরিবর্তনে ব্যবহার করতে পারবেন। শুরু করতে [Foundry Local ডকুমেন্টেশন](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) দেখুন, অথবা `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) দিয়ে ইনস্টল করুন।
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral, Gemma এর মতো ওপেন মডেলগুলো লোকালি চালানোর জন্য একটি জনপ্রিয় বিকল্প।


দুইটি অপশন ব্যবহার করে হাতে কলমে উদাহরণের জন্য [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) দেখুন।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->