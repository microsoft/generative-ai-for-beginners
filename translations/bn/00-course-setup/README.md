# এই কোর্স দিয়ে শুরু করা

আমরা অত্যন্ত উত্তেজিত যে আপনি এই কোর্সটি শুরু করতে চলেছেন এবং দেখবেন আপনি জেনেরেটিভ AI দিয়ে কী তৈরি করার জন্য অনুপ্রাণিত হচ্ছেন!

আপনার সফলতা নিশ্চিত করার জন্য, এই পৃষ্ঠাটি সেটআপ ধাপগুলি, প্রযুক্তিগত প্রয়োজনীয়তাগুলি, এবং প্রয়োজনে সাহায্য কোথায় পাবেন তা নির্দেশ করে।

## সেটআপ ধাপ

এই কোর্স নেওয়া শুরু করতে, আপনাকে নিম্নলিখিত ধাপগুলি সম্পন্ন করতে হবে।

### ১. এই রিপো ফর্ক করুন

[Fork this entire repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) আপনার নিজের GitHub অ্যাকাউন্টে, যেন আপনি কোড পরিবর্তন করতে এবং চ্যালেঞ্জগুলি সম্পন্ন করতে পারেন। এছাড়াও আপনি [এই রিপোতে star (🌟) দিতে পারেন](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) যাতে এটিকে এবং সম্পর্কিত রিপো গুলোকে সহজে খুঁজে পান।

### ২. একটি কোডস্পেস তৈরি করুন

কোড চালানোর সময় কোনো নির্ভরতা সমস্যার এড়াতে, আমরা পরামর্শ দেই এই কোর্সটি [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) এ চালানোর।

আপনার ফর্কে: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/bn/who-will-pay.4c0609b1c7780f44.webp)

#### ২.১ একটি সিক্রেট যোগ করুন

1. ⚙️ গিয়ার আইকন -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret।
2. নাম দিন OPENAI_API_KEY, আপনার কী পেস্ট করুন, Save করুন।

### ৩. এরপর কী?

| আমি চাই…            | যান…                                                                   |
|---------------------|------------------------------------------------------------------------|
| লেসন ১ শুরু করতে    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| অফলাইন কাজ করতে    | [`setup-local.md`](02-setup-local.md)                                  |
| একটি LLM প্রদানকারী সেটআপ করতে | [`providers.md`](03-providers.md)                                    |
| অন্যান্য শিক্ষার্থীদের সাথে পরিচিত হতে | [আমাদের Discord-এ যোগ দিন](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## সমস্যার সমাধান

| লক্ষণ                                   | সমাধান                                                           |
|----------------------------------------|-----------------------------------------------------------------|
| কন্টেইনার বিল্ড ১০ মিনিটের বেশি আটকে থাকে | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`            | টার্মিনাল যুক্ত হয়নি; **+** তে ক্লিক করুন ➜ *bash*              |
| OpenAI থেকে `401 Unauthorized`         | ভুল / মেয়াদ উত্তীর্ণ `OPENAI_API_KEY`                         |
| VS Code “Dev container mounting…” দেখায় | ব্রাউজার ট্যাব রিফ্রেশ করুন—Codespaces কখনও কখনও কানেকশন হারায় |
| Notebook kernel মিসিং                   | Notebook মেনু ➜ **Kernel ▸ Select Kernel ▸ Python 3**            |

   ইউনিক্স-ভিত্তিক সিস্টেম:

   ```bash
   touch .env
   ```

   উইন্ডোজ:

   ```cmd
   echo . > .env
   ```

৩. **`.env` ফাইল সম্পাদনা করুন**: `.env` ফাইলটি একটি টেক্সট এডিটরে (যেমন VS Code, Notepad++, অথবা অন্য যেকোনো এডিটর) খুলুন। নিচের লাইনটি যোগ করুন, যেখানে `your_github_token_here` এর জায়গায় আপনার আসল GitHub টোকেন দিন:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

৪. **ফাইলটি সংরক্ষণ করুন**: পরিবর্তনগুলি সংরক্ষণ করুন এবং টেক্সট এডিটর বন্ধ করুন।

৫. **`python-dotenv` ইনস্টল করুন**: যদি এখনও না করে থাকেন, তাহলে `.env` ফাইল থেকে পরিবেশ পরিবর্তনশীলগুলি আপনার Python অ্যাপ্লিকেশনে লোড করার জন্য `python-dotenv` প্যাকেজটি ইনস্টল করতে হবে। এটি আপনি `pip` ব্যবহার করে ইনস্টল করতে পারেন:

   ```bash
   pip install python-dotenv
   ```

৬. **আপনার Python স্ক্রিপ্টে পরিবেশ পরিবর্তনশীল লোড করুন**: আপনার Python স্ক্রিপ্টে, `.env` ফাইল থেকে পরিবেশ পরিবর্তনশীলগুলি লোড করতে `python-dotenv` প্যাকেজ ব্যবহার করুন:

   ```python
   from dotenv import load_dotenv
   import os

   # .env ফাইল থেকে পরিবেশ পরিবর্তনশীলগুলি লোড করুন
   load_dotenv()

   # GITHUB_TOKEN পরিবর্তনশীলটি অ্যাক্সেস করুন
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

এইটুকুই! আপনি সফলভাবে একটি `.env` ফাইল তৈরি করেছেন, আপনার GitHub টোকেন যোগ করেছেন, এবং এটি আপনার Python অ্যাপ্লিকেশনে লোড করেছেন।

## আপনার কম্পিউটারে লোকালি কোড কিভাবে চালাবেন

আপনার কম্পিউটারে কোড লোকালি চালাতে, আপনাকে অবশ্যই [Python এর কোনো সংস্করণ ইন্সটল করতে হবে](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)।

তারপর রিপোজিটোরি ব্যবহার করার জন্য, আপনাকে এটি ক্লোন করতে হবে:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

সবকিছু ঠিকঠাক ক্লোন করার পর, আপনি শুরু করতে প্রস্তুত!

## ঐচ্ছিক ধাপ

### Miniconda ইনস্টলানো

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) হলো [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python এবং কিছু প্যাকেজ ইনস্টল করার জন্য একটি হালকা ইন্সটলার।
Conda নিজেই একটি প্যাকেজ ম্যানেজার, যা বিভিন্ন Python [**ভার্চুয়াল এনভায়রনমেন্ট**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) এবং প্যাকেজ সহজে সেটআপ ও পরিবর্তন করার সুযোগ দেয়। এছাড়াও `pip` এর মাধ্যমে না পাওয়া প্যাকেজ ইনস্টল করার জন্য এটি কাজ দেয়।

আপনি [MiniConda ইনস্টলেশন গাইড](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) অনুসরণ করতে পারেন এটি সেটআপ করার জন্য।

Miniconda ইনস্টল করা থাকলে, আপনাকে [রিপোজিটোরি ক্লোন করতে হবে](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (যদি না করে থাকেন)

এরপর, একটি ভার্চুয়াল এনভায়রনমেন্ট তৈরি করতে হবে। Conda দিয়ে এটি করতে, একটি নতুন এনভায়রনমেন্ট ফাইল (_environment.yml_) তৈরি করুন। Codespaces ব্যবহার করলে এটি `.devcontainer` ডিরেক্টরির মধ্যে তৈরি করুন, অর্থাৎ `.devcontainer/environment.yml`।

আপনার এনভায়রনমেন্ট ফাইলে নিচের স্নিপেটটি লিখুন:

```yml
name: <environment-name>
channels:
  - defaults
  - microsoft
dependencies:
  - python=<python-version>
  - openai
  - python-dotenv
  - pip
  - pip:
      - azure-ai-ml
```

যদি conda ব্যবহার করার সময় ত্রুটি পান, তবে টার্মিনালে নিচের কমান্ড ব্যবহার করে ম্যানুয়ালি Microsoft AI লাইব্রেরি ইনস্টল করতে পারেন।

```
conda install -c microsoft azure-ai-ml
```

এনভায়রনমেন্ট ফাইলটি আমাদের প্রয়োজনীয় ডিপেনডেন্সি নির্দেশ করে। `<environment-name>` আপনি যেই নাম দিতে চান আপনার Conda এনভায়রনমেন্টের জন্য, এবং `<python-version>` হল আপনি যে Python ভার্সন ব্যবহার করতে চান, উদাহরণস্বরূপ, `3` হলো Python এর সর্বশেষ প্রধান সংস্করণ।

এরপর, নিচের কমান্ড গুলো আপনার কমান্ড লাইন/টার্মিনালে চালিয়ে Conda এনভায়রনমেন্ট তৈরি করুন:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer সাবপাথ শুধুমাত্র Codespace সেটআপগুলিতে প্রযোজ্য
conda activate ai4beg
```

সমস্যা হলে [Conda এনভায়রনমেন্ট গাইড](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) দেখুন।

### Python সাপোর্ট এক্সটেনশন সহ Visual Studio Code ব্যবহার করা

আমরা এই কোর্সের জন্য [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) এডিটর এবং [Python সাপোর্ট এক্সটেনশন](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ইনস্টল করার পরামর্শ দিই। তবে এটি সুপারিশ মাত্র, অবশ্যই বাধ্যতামূলক নয়।

> **দ্রষ্টব্য**: কোর্স রিপোজিটোরিতে VS Code এ খুললে, আপনি প্রজেক্টকে একটি কন্টেইনারের মধ্যে সেটআপ করার অপশন পাবেন। এটা সম্ভব হয় কোর্স রিপোজিটোরির মধ্যে থাকা [বিশেষ `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ডিরেক্টরির কারণে। পরে এ সম্পর্কে আরও জানা যাবে।

> **দ্রষ্টব্য**: আপনি যখন রিপোজিটোরি ক্লোন করে VS Code-এ খুলবেন, তখন এটি স্বয়ংক্রিয়ভাবে Python সাপোর্ট এক্সটেনশন ইনস্টল করার পরামর্শ দিবে।

> **দ্রষ্টব্য**: VS Code যখন রিপোজিটোরি কন্টেইনারে পুনরায় খোলার পরামর্শ দেয়, আপনি এটি প্রত্যাখ্যান করুন যাতে আপনি আপনার লোকালি ইন্সটল করা Python ব্যবহার করতে পারেন।

### ব্রাউজারে Jupyter ব্যবহার

আপনি ব্রাউজারেই প্রকল্পে কাজ করতে পারেন [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ব্যবহার করে। ক্লাসিক Jupyter এবং [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) উভয়ই অটোমেটিক কমপ্লিশন, কোড হাইলাইটিং ইত্যাদি সুবিধাসহ একটি সুভো আচরণ পরিবেশ প্রদান করে।

লোকালিতে Jupyter শুরু করতে, টার্মিনালে/কমান্ড লাইনে যান, কোর্স ডিরেক্টরিতে প্রবেশ করুন এবং চালান:

```bash
jupyter notebook
```

অথবা

```bash
jupyterhub
```

এটি একটি Jupyter ইন্সট্যান্স চালু করবে এবং কমান্ড লাইন উইন্ডোতে URL দেখানো হবে।

URL-এ প্রবেশ করলে, আপনি কোর্সের লেখচিত্র দেখতে পাবেন এবং যেকোন `*.ipynb` ফাইলে যেতে পারবেন। যেমন, `08-building-search-applications/python/oai-solution.ipynb`।

### একটি কন্টেইনারে চালানো

আপনার কম্পিউটার বা কোডস্পেসে সবকিছু সেটআপ করার বিকল্প হলো [কন্টেইনার](<https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) ব্যবহার। কোর্স রিপোজিটোরির বিশেষ `.devcontainer` ফোল্ডারটি VS Code কে প্রজেক্টটি কন্টেইনারের মধ্যে সেটআপ করার সুযোগ দেয়। Codespaces ছাড়া, এর জন্য Docker ইনস্টল করতে হবে, এবং কাজটি তুলনামূলক কঠিন, তাই আমরা কেবল কন্টেইনার নিয়ে কাজের অভিজ্ঞতা থাকা লোকদের জন্য এ পরামর্শ দিই।

GitHub Codespaces ব্যবহার করার সময় আপনার API কীগুলো নিরাপদ রাখার অন্যতম সেরা উপায় হলো Codespace Secrets ব্যবহার করা। দয়া করে [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) গাইডটি অনুসরণ করুন।

## লেসন এবং প্রযুক্তিগত প্রয়োজনীয়তা

কোর্সে ৬টি ধারণাগত লেসন এবং ৬টি কোডিং লেসন রয়েছে।

কোডিং লেসনগুলোর জন্য, আমরা Azure OpenAI সার্ভিস ব্যবহার করছি। এই কোড চালাতে Azure OpenAI সার্ভিস অ্যাক্সেস এবং একটি API কী লাগবে। আপনি [এই অ্যাপ্লিকেশনটি পূরণ করে](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) অ্যাক্সেসের জন্য আবেদন করতে পারেন।

অ্যাপ্লিকেশন প্রক্রিয়াকরণের সময়, প্রতিটি কোডিং লেসনের সাথে একটি `README.md` ফাইলও রয়েছে যেখানে আপনি কোড এবং আউটপুট দেখতে পারেন।

## প্রথমবার Azure OpenAI সার্ভিস ব্যবহার

আপনি যদি প্রথমবার Azure OpenAI সার্ভিস ব্যবহার করছেন, অনুগ্রহ করে [কিভাবে Azure OpenAI সার্ভিস রিসোর্স তৈরি এবং ডিপ্লয় করবেন তা দেখুন](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)।

## প্রথমবার OpenAI API ব্যবহার

আপনি যদি প্রথমবার OpenAI API ব্যবহার করছেন, অনুগ্রহ করে [কিভাবে ইন্টারফেস তৈরি ও ব্যবহার করবেন তা দেখুন](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)।

## অন্যান্য শিক্ষার্থীদের সাথে পরিচিত হন

আমরা আমাদের অফিসিয়াল [AI কমিউনিটি Discord সার্ভারে](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) অন্যান্য শিক্ষার্থীদের সাথে পরিচিতি জন্য চ্যানেল তৈরি করেছি। এটি অন্যান্য সমমনা উদ্যোক্তা, নির্মাতা, ছাত্র এবং জেনেরেটিভ AI-তে উন্নতি করতে আগ্রহী কারো সাথে নেটওয়ার্ক গড়ে তোলার এক উত্তম উপায়।

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

প্রকল্প দলের সদস্যরাও এই Discord সার্ভারে থাকবেন শিক্ষার্থীদের সাহায্যের জন্য।

## অবদান রাখুন

এই কোর্স একটি ওপেন সোর্স উদ্যোগ। যদি আপনি কোনও উন্নতির সুযোগ বা সমস্যা দেখতে পান, তাহলে একটি [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) তৈরি করুন অথবা [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) লগ করুন।

প্রকল্প দল সব অবদান নজর রাখবে। ওপেন সোর্সে অবদান রাখা জেনেরেটিভ AI-তে আপনার ক্যারিয়ার গড়ার একটি অসাধারণ উপায়।

অধিকাংশ অবদানে আপনাকে একটি Contributor License Agreement (CLA) স্বীকার করতে হবে, যা ঘোষণা করে যে আপনি আপনার অবদানের ব্যবহার করার অধিকার আমাদের দিয়েছেন। বিস্তারিত জানতে যান [CLA, Contributor License Agreement ওয়েবসাইটে](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)।

গুরুত্বপূর্ণ: এই রিপোতে ভাষান্তর করার সময়, অনুগ্রহ করে নিশ্চিত করুন যে আপনি মেশিন অনুবাদ ব্যবহার করছেন না। আমরা অনুবাদগুলো কমিউনিটির মাধ্যমে যাচাই করব, তাই শুধুমাত্র আপনি যেসব ভাষায় পারদর্শী সে ভাষার জন্যই অনুবাদের জন্য স্বেচ্ছাসেবক হোন।

যখন আপনি একটি pull request জমা দেবেন, CLA-bot স্বয়ংক্রিয়ভাবে নির্ধারণ করবে আপনাকে CLA প্রদান করতে হবে কিনা এবং PR-এ উপযুক্ত লেবেল বা মন্তব্য যোগ করবে। বটের নির্দেশনা অনুসরণ করুন। এই প্রক্রিয়াটি আপনাকে সমস্ত রিপোজিটোরিতে একটি মাত্র করতে হবে।

এই প্রকল্পটি [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) গ্রহণ করেছে। আরও তথ্যের জন্য Code of Conduct FAQ পড়ুন অথবা [Email opencode](opencode@microsoft.com) তে যোগাযোগ করুন।

## চলুন শুরু করি!
এখন যেহেতু আপনি এই কোর্স সম্পূর্ণ করার জন্য প্রয়োজনীয় ধাপগুলি সম্পন্ন করেছেন, চলুন শুরু করা যাক [Generative AI এবং LLMs এর পরিচিতি](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) নিয়ে।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**বাতিলকরণ**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ভুল বা অস্বচ্ছতা থাকতে পারে। মূল নথি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারের কারণে হওয়া যেকোনো ভুল বোঝাবুঝি বা ব্যাখ্যার দায় আমরা গ্রহণ করব না।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->