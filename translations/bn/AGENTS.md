<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T10:57:12+00:00",
  "source_file": "AGENTS.md",
  "language_code": "bn"
}
-->
# AGENTS.md

## প্রকল্পের সংক্ষিপ্ত বিবরণ

এই রিপোজিটরিতে ২১টি পাঠের একটি সম্পূর্ণ পাঠক্রম অন্তর্ভুক্ত রয়েছে যা জেনারেটিভ AI-এর মৌলিক বিষয় এবং অ্যাপ্লিকেশন ডেভেলপমেন্ট শেখায়। কোর্সটি নবাগতদের জন্য ডিজাইন করা হয়েছে এবং মৌলিক ধারণা থেকে শুরু করে প্রোডাকশন-রেডি অ্যাপ্লিকেশন তৈরির বিষয় পর্যন্ত সবকিছু কভার করে।

**মূল প্রযুক্তি:**
- Python 3.9+ এবং লাইব্রেরি: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript এবং Node.js লাইব্রেরি: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API, এবং GitHub Models
- ইন্টারঅ্যাকটিভ লার্নিংয়ের জন্য Jupyter Notebooks
- ডেভ কন্টেইনারস একটি সঙ্গতিপূর্ণ ডেভেলপমেন্ট পরিবেশের জন্য

**রিপোজিটরির কাঠামো:**
- ২১টি নম্বরযুক্ত পাঠের ডিরেক্টরি (00-21) যেখানে README, কোড উদাহরণ এবং অ্যাসাইনমেন্ট রয়েছে
- একাধিক ইমপ্লিমেন্টেশন: Python, TypeScript, এবং কখনও কখনও .NET উদাহরণ
- ৪০+ ভাষার অনুবাদসমূহের ডিরেক্টরি
- `.env` ফাইলের মাধ্যমে কেন্দ্রীয় কনফিগারেশন (টেমপ্লেট হিসেবে `.env.copy` ব্যবহার করুন)

## সেটআপ কমান্ড

### প্রাথমিক রিপোজিটরি সেটআপ

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Python পরিবেশ সেটআপ

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Node.js/TypeScript সেটআপ

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### ডেভ কন্টেইনার সেটআপ (প্রস্তাবিত)

রিপোজিটরিতে GitHub Codespaces বা VS Code Dev Containers-এর জন্য `.devcontainer` কনফিগারেশন অন্তর্ভুক্ত রয়েছে:

1. রিপোজিটরি GitHub Codespaces বা VS Code-এ Dev Containers এক্সটেনশন সহ খুলুন
2. ডেভ কন্টেইনার স্বয়ংক্রিয়ভাবে:
   - `requirements.txt` থেকে Python ডিপেনডেন্সি ইনস্টল করবে
   - পোস্ট-ক্রিয়েট স্ক্রিপ্ট চালাবে (`.devcontainer/post-create.sh`)
   - Jupyter কের্নেল সেটআপ করবে

## ডেভেলপমেন্ট ওয়ার্কফ্লো

### পরিবেশ ভেরিয়েবল

API অ্যাক্সেস প্রয়োজন এমন সমস্ত পাঠ `.env`-এ সংজ্ঞায়িত পরিবেশ ভেরিয়েবল ব্যবহার করে:

- `OPENAI_API_KEY` - OpenAI API-এর জন্য
- `AZURE_OPENAI_API_KEY` - Azure OpenAI Service-এর জন্য
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI এন্ডপয়েন্ট URL
- `AZURE_OPENAI_DEPLOYMENT` - চ্যাট কমপ্লিশন মডেল ডিপ্লয়মেন্ট নাম
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - এমবেডিং মডেল ডিপ্লয়মেন্ট নাম
- `AZURE_OPENAI_API_VERSION` - API সংস্করণ (ডিফল্ট: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Hugging Face মডেলের জন্য
- `GITHUB_TOKEN` - GitHub Models-এর জন্য

### Python উদাহরণ চালানো

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### TypeScript উদাহরণ চালানো

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Jupyter Notebooks চালানো

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### বিভিন্ন পাঠের ধরন নিয়ে কাজ করা

- **"Learn" পাঠসমূহ**: README.md ডকুমেন্টেশন এবং ধারণার উপর ফোকাস
- **"Build" পাঠসমূহ**: Python এবং TypeScript-এ কার্যকরী কোড উদাহরণ অন্তর্ভুক্ত
- প্রতিটি পাঠে README.md রয়েছে যেখানে তত্ত্ব, কোড ওয়াকথ্রু এবং ভিডিও কন্টেন্টের লিঙ্ক রয়েছে

## কোড স্টাইল নির্দেশিকা

### Python

- পরিবেশ ভেরিয়েবল ব্যবস্থাপনার জন্য `python-dotenv` ব্যবহার করুন
- API ইন্টারঅ্যাকশনের জন্য `openai` লাইব্রেরি ইমপোর্ট করুন
- লিন্টিংয়ের জন্য `pylint` ব্যবহার করুন (কিছু উদাহরণে সরলতার জন্য `# pylint: disable=all` অন্তর্ভুক্ত)
- PEP 8 নামকরণের নিয়ম অনুসরণ করুন
- API ক্রেডেনশিয়াল `.env` ফাইলে সংরক্ষণ করুন, কোডে নয়

### TypeScript

- পরিবেশ ভেরিয়েবলের জন্য `dotenv` প্যাকেজ ব্যবহার করুন
- প্রতিটি অ্যাপের জন্য `tsconfig.json`-এ TypeScript কনফিগারেশন
- Azure সার্ভিসের জন্য `@azure/openai` বা `@azure-rest/ai-inference` ব্যবহার করুন
- অটো-রিলোড সহ ডেভেলপমেন্টের জন্য `nodemon` ব্যবহার করুন
- চালানোর আগে বিল্ড করুন: `npm run build` তারপর `npm start`

### সাধারণ নিয়মাবলী

- কোড উদাহরণগুলো সহজ এবং শিক্ষামূলক রাখুন
- মূল ধারণাগুলি ব্যাখ্যা করার জন্য মন্তব্য অন্তর্ভুক্ত করুন
- প্রতিটি পাঠের কোড স্বয়ংসম্পূর্ণ এবং চালানোর যোগ্য হওয়া উচিত
- ধারাবাহিক নামকরণ ব্যবহার করুন: Azure OpenAI-এর জন্য `aoai-` প্রিফিক্স, OpenAI API-এর জন্য `oai-`, GitHub Models-এর জন্য `githubmodels-`

## ডকুমেন্টেশন নির্দেশিকা

### Markdown স্টাইল

- সমস্ত URL `[text](../../url)` ফরম্যাটে মোড়ানো থাকতে হবে, অতিরিক্ত স্পেস ছাড়াই
- আপেক্ষিক লিঙ্কগুলো `./` বা `../` দিয়ে শুরু করতে হবে
- Microsoft ডোমেইনের সমস্ত লিঙ্কে ট্র্যাকিং ID থাকতে হবে: `?WT.mc_id=academic-105485-koreyst`
- URL-এ দেশ-নির্দিষ্ট লোকেল থাকা যাবে না (যেমন `/en-us/` এড়িয়ে চলুন)
- `./images` ফোল্ডারে সংরক্ষিত চিত্রগুলোতে বর্ণনামূলক নাম ব্যবহার করুন
- ফাইল নামগুলোতে ইংরেজি অক্ষর, সংখ্যা এবং ড্যাশ ব্যবহার করুন

### অনুবাদ সমর্থন

- রিপোজিটরি ৪০+ ভাষায় স্বয়ংক্রিয় GitHub Actions-এর মাধ্যমে অনুবাদ সমর্থন করে
- অনুবাদসমূহ `translations/` ডিরেক্টরিতে সংরক্ষিত
- আংশিক অনুবাদ জমা দেওয়া যাবে না
- মেশিন অনুবাদ গ্রহণযোগ্য নয়
- অনুবাদিত চিত্রগুলো `translated_images/` ডিরেক্টরিতে সংরক্ষিত

## টেস্টিং এবং যাচাইকরণ

### জমা দেওয়ার আগে চেক

এই রিপোজিটরি GitHub Actions ব্যবহার করে যাচাই করে। PR জমা দেওয়ার আগে:

1. **Markdown লিঙ্ক চেক করুন**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **ম্যানুয়াল টেস্টিং**:
   - Python উদাহরণ টেস্ট করুন: venv অ্যাক্টিভেট করুন এবং স্ক্রিপ্ট চালান
   - TypeScript উদাহরণ টেস্ট করুন: `npm install`, `npm run build`, `npm start`
   - পরিবেশ ভেরিয়েবল সঠিকভাবে কনফিগার করা হয়েছে কিনা যাচাই করুন
   - API কী কোড উদাহরণের সাথে কাজ করছে কিনা নিশ্চিত করুন

3. **কোড উদাহরণ**:
   - নিশ্চিত করুন যে সমস্ত কোড ত্রুটি ছাড়াই চালানো যায়
   - প্রযোজ্য ক্ষেত্রে Azure OpenAI এবং OpenAI API উভয়ের সাথে টেস্ট করুন
   - যেখানে সমর্থিত, GitHub Models-এর সাথে উদাহরণগুলো কাজ করছে কিনা যাচাই করুন

### স্বয়ংক্রিয় টেস্ট নেই

এটি একটি শিক্ষামূলক রিপোজিটরি যা টিউটোরিয়াল এবং উদাহরণগুলোর উপর ফোকাস করে। এখানে কোনো ইউনিট টেস্ট বা ইন্টিগ্রেশন টেস্ট চালানোর প্রয়োজন নেই। যাচাইকরণ প্রধানত:
- কোড উদাহরণের ম্যানুয়াল টেস্টিং
- Markdown যাচাইয়ের জন্য GitHub Actions
- শিক্ষামূলক বিষয়বস্তুর কমিউনিটি রিভিউ

## পুল রিকোয়েস্ট নির্দেশিকা

### জমা দেওয়ার আগে

1. Python এবং TypeScript উভয় ক্ষেত্রেই প্রযোজ্য কোড পরিবর্তন টেস্ট করুন
2. Markdown যাচাই চালান (PR-এ স্বয়ংক্রিয়ভাবে ট্রিগার হয়)
3. Microsoft URL-এ ট্র্যাকিং ID উপস্থিত কিনা নিশ্চিত করুন
4. আপেক্ষিক লিঙ্কগুলো বৈধ কিনা যাচাই করুন
5. চিত্রগুলো সঠিকভাবে রেফারেন্স করা হয়েছে কিনা নিশ্চিত করুন

### PR শিরোনামের ফরম্যাট

- বর্ণনামূলক শিরোনাম ব্যবহার করুন: `[Lesson 06] Fix Python example typo` বা `Update README for lesson 08`
- প্রযোজ্য ক্ষেত্রে ইস্যু নম্বর উল্লেখ করুন: `Fixes #123`

### PR বিবরণ

- কী পরিবর্তন করা হয়েছে এবং কেন তা ব্যাখ্যা করুন
- সংশ্লিষ্ট ইস্যুর লিঙ্ক দিন
- কোড পরিবর্তনের ক্ষেত্রে, কোন উদাহরণগুলো টেস্ট করা হয়েছে তা উল্লেখ করুন
- অনুবাদ PR-এর ক্ষেত্রে, সম্পূর্ণ অনুবাদ অন্তর্ভুক্ত করুন

### অবদান রাখার প্রয়োজনীয়তা

- Microsoft CLA সাইন করুন (প্রথম PR-এ স্বয়ংক্রিয়)
- পরিবর্তন করার আগে রিপোজিটরি আপনার অ্যাকাউন্টে ফর্ক করুন
- এক PR-এ একাধিক সম্পর্কহীন পরিবর্তন একত্রিত করবেন না
- PR-গুলো ফোকাসড এবং ছোট রাখুন যেখানে সম্ভব

## সাধারণ ওয়ার্কফ্লো

### নতুন কোড উদাহরণ যোগ করা

1. প্রাসঙ্গিক পাঠের ডিরেক্টরিতে যান
2. `python/` বা `typescript/` সাবডিরেক্টরিতে উদাহরণ তৈরি করুন
3. নামকরণের নিয়ম অনুসরণ করুন: `{provider}-{example-name}.{py|ts|js}`
4. প্রকৃত API ক্রেডেনশিয়াল দিয়ে টেস্ট করুন
5. পাঠের README-তে নতুন পরিবেশ ভেরিয়েবল ডকুমেন্ট করুন

### ডকুমেন্টেশন আপডেট করা

1. পাঠের ডিরেক্টরিতে README.md সম্পাদনা করুন
2. Markdown নির্দেশিকা অনুসরণ করুন (ট্র্যাকিং ID, আপেক্ষিক লিঙ্ক)
3. অনুবাদ আপডেট GitHub Actions দ্বারা পরিচালিত হয় (ম্যানুয়ালি সম্পাদনা করবেন না)
4. সমস্ত লিঙ্ক বৈধ কিনা টেস্ট করুন

### ডেভ কন্টেইনার নিয়ে কাজ করা

1. রিপোজিটরিতে `.devcontainer/devcontainer.json` অন্তর্ভুক্ত রয়েছে
2. পোস্ট-ক্রিয়েট স্ক্রিপ্ট স্বয়ংক্রিয়ভাবে Python ডিপেনডেন্সি ইনস্টল করে
3. Python এবং Jupyter-এর জন্য এক্সটেনশন প্রি-কনফিগার করা
4. পরিবেশ `mcr.microsoft.com/devcontainers/universal:2.11.2`-এর উপর ভিত্তি করে

## ডিপ্লয়মেন্ট এবং প্রকাশনা

এটি একটি শিক্ষামূলক রিপোজিটরি - এখানে কোনো ডিপ্লয়মেন্ট প্রক্রিয়া নেই। পাঠক্রমটি নিম্নলিখিত মাধ্যমে ব্যবহৃত হয়:

1. **GitHub রিপোজিটরি**: কোড এবং ডকুমেন্টেশনে সরাসরি অ্যাক্সেস
2. **GitHub Codespaces**: প্রি-কনফিগারড সেটআপ সহ ইনস্ট্যান্ট ডেভেলপমেন্ট পরিবেশ
3. **Microsoft Learn**: বিষয়বস্তু অফিসিয়াল লার্নিং প্ল্যাটফর্মে সিন্ডিকেট করা হতে পারে
4. **docsify**: Markdown থেকে তৈরি ডকুমেন্টেশন সাইট (দেখুন `docsifytopdf.js` এবং `package.json`)

### ডকুমেন্টেশন সাইট তৈরি করা

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## সমস্যার সমাধান

### সাধারণ সমস্যা

**Python ইমপোর্ট ত্রুটি**:
- নিশ্চিত করুন যে ভার্চুয়াল পরিবেশ অ্যাক্টিভেট করা হয়েছে
- `pip install -r requirements.txt` চালান
- Python সংস্করণ 3.9+ কিনা যাচাই করুন

**TypeScript বিল্ড ত্রুটি**:
- নির্দিষ্ট অ্যাপ ডিরেক্টরিতে `npm install` চালান
- Node.js সংস্করণ সামঞ্জস্যপূর্ণ কিনা যাচাই করুন
- `node_modules` ক্লিয়ার করুন এবং পুনরায় ইনস্টল করুন যদি প্রয়োজন হয়

**API অথেনটিকেশন ত্রুটি**:
- নিশ্চিত করুন `.env` ফাইল বিদ্যমান এবং সঠিক মান রয়েছে
- API কী বৈধ এবং মেয়াদোত্তীর্ণ নয় কিনা যাচাই করুন
- আপনার অঞ্চলের জন্য এন্ডপয়েন্ট URL সঠিক কিনা নিশ্চিত করুন

**পরিবেশ ভেরিয়েবল অনুপস্থিত**:
- `.env.copy` থেকে `.env` কপি করুন
- আপনি যে পাঠে কাজ করছেন তার জন্য সমস্ত প্রয়োজনীয় মান পূরণ করুন
- `.env` আপডেট করার পরে আপনার অ্যাপ্লিকেশন পুনরায় চালু করুন

## অতিরিক্ত সম্পদ

- [কোর্স সেটআপ গাইড](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [অবদান রাখার নির্দেশিকা](./CONTRIBUTING.md)
- [আচরণবিধি](./CODE_OF_CONDUCT.md)
- [নিরাপত্তা নীতি](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [উন্নত কোড নমুনার সংগ্রহ](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## প্রকল্প-নির্দিষ্ট নোট

- এটি একটি **শিক্ষামূলক রিপোজিটরি** যা শেখার উপর ফোকাস করে, প্রোডাকশন কোড নয়
- উদাহরণগুলো ইচ্ছাকৃতভাবে সহজ এবং ধারণা শেখানোর উপর কেন্দ্রীভূত
- কোডের গুণমান শিক্ষামূলক স্পষ্টতার সাথে ভারসাম্যপূর্ণ
- প্রতিটি পাঠ স্বয়ংসম্পূর্ণ এবং স্বাধীনভাবে সম্পন্ন করা যেতে পারে
- রিপোজিটরি একাধিক API প্রদানকারী সমর্থন করে: Azure OpenAI, OpenAI, এবং GitHub Models
- বিষয়বস্তু বহুভাষিক এবং স্বয়ংক্রিয় অনুবাদ ওয়ার্কফ্লো সহ
- প্রশ্ন এবং সহায়তার জন্য Discord-এ সক্রিয় কমিউনিটি

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।