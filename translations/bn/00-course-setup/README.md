<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T15:33:33+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "bn"
}
-->
# এই কোর্সটি শুরু করা

আপনি এই কোর্সটি শুরু করতে যাচ্ছেন বলে আমরা খুবই উচ্ছ্বসিত এবং দেখতে চাই আপনি জেনারেটিভ এআই দিয়ে কী কী নতুন কিছু তৈরি করতে অনুপ্রাণিত হন!

আপনার সফলতার জন্য, এই পাতায় সেটআপ ধাপ, টেকনিক্যাল চাহিদা এবং কোথায় সাহায্য পাবেন তা উল্লেখ করা হয়েছে।

## সেটআপ ধাপসমূহ

এই কোর্সটি নিতে হলে আপনাকে নিচের ধাপগুলো সম্পন্ন করতে হবে।

### ১. এই রিপোটি ফর্ক করুন

[এই পুরো রিপোটি ফর্ক করুন](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) আপনার নিজের GitHub অ্যাকাউন্টে, যাতে আপনি কোড পরিবর্তন করতে এবং চ্যালেঞ্জগুলো সম্পন্ন করতে পারেন। এছাড়াও, [রিপোতে স্টার (🌟) দিন](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) যাতে এটি এবং সংশ্লিষ্ট রিপোগুলো সহজে খুঁজে পান।

### ২. একটি কোডস্পেস তৈরি করুন

কোড চালানোর সময় ডিপেন্ডেন্সি সমস্যা এড়াতে, আমরা এই কোর্সটি [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)-এ চালানোর পরামর্শ দিই।

আপনার ফর্কে: **Code -> Codespaces -> New on main**

![কোডস্পেস তৈরির জন্য ডায়ালগ বক্সের ছবি](../../../00-course-setup/images/who-will-pay.webp)

#### ২.১ একটি সিক্রেট যোগ করুন

১. ⚙️ গিয়ার আইকন -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret।
২. নাম দিন OPENAI_API_KEY, আপনার কী পেস্ট করুন, Save করুন।

### ৩. এরপর কী করবেন?

| আমি চাই…             | যান…                                                                      |
|----------------------|---------------------------------------------------------------------------|
| লেসন ১ শুরু করতে     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)        |
| অফলাইনে কাজ করতে     | [`setup-local.md`](02-setup-local.md)                                     |
| LLM Provider সেটআপ   | [`providers.md`](providers.md)                                            |
| অন্যান্য শিক্ষার্থীদের সাথে দেখা | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## সমস্যা সমাধান

| উপসর্গ                                    | সমাধান                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| কন্টেইনার বিল্ড ১০ মিনিটের বেশি সময় নিচ্ছে | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | টার্মিনাল সংযুক্ত হয়নি; **+** ➜ *bash* ক্লিক করুন               |
| OpenAI থেকে `401 Unauthorized`            | ভুল / মেয়াদোত্তীর্ণ `OPENAI_API_KEY`                           |
| VS Code-এ “Dev container mounting…”       | ব্রাউজার ট্যাব রিফ্রেশ করুন—Codespaces মাঝে মাঝে সংযোগ হারায়    |
| নোটবুক কার্নেল অনুপস্থিত                  | Notebook menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   ইউনিক্স-ভিত্তিক সিস্টেমের জন্য:

   ```bash
   touch .env
   ```

   উইন্ডোজের জন্য:

   ```cmd
   echo . > .env
   ```

৩. **`.env` ফাইলটি সম্পাদনা করুন**: `.env` ফাইলটি কোনো টেক্সট এডিটরে (যেমন VS Code, Notepad++, বা অন্য যেকোনো এডিটর) খুলুন। নিচের লাইনটি যোগ করুন, যেখানে `your_github_token_here`-এর জায়গায় আপনার আসল GitHub টোকেন দিন:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

৪. **ফাইলটি সংরক্ষণ করুন**: পরিবর্তনগুলো সংরক্ষণ করুন এবং এডিটর বন্ধ করুন।

৫. **`python-dotenv` ইনস্টল করুন**: যদি আগে না করে থাকেন, তাহলে `python-dotenv` প্যাকেজটি ইনস্টল করতে হবে যাতে `.env` ফাইল থেকে এনভায়রনমেন্ট ভেরিয়েবল লোড করা যায়। `pip` দিয়ে ইনস্টল করুন:

   ```bash
   pip install python-dotenv
   ```

৬. **আপনার পাইথন স্ক্রিপ্টে এনভায়রনমেন্ট ভেরিয়েবল লোড করুন**: আপনার পাইথন স্ক্রিপ্টে `python-dotenv` ব্যবহার করে `.env` ফাইল থেকে এনভায়রনমেন্ট ভেরিয়েবল লোড করুন:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

ব্যাস! আপনি সফলভাবে `.env` ফাইল তৈরি করেছেন, আপনার GitHub টোকেন যোগ করেছেন এবং এটি আপনার পাইথন অ্যাপ্লিকেশনে লোড করেছেন।

## কীভাবে আপনার কম্পিউটারে লোকালি চালাবেন

আপনার কম্পিউটারে কোড চালাতে হলে, [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)-এর কোনো একটি ভার্সন ইনস্টল থাকতে হবে।

এরপর রিপোজিটরি ব্যবহার করতে হলে, আপনাকে এটি ক্লোন করতে হবে:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

সবকিছু চেকআউট হয়ে গেলে, আপনি শুরু করতে পারবেন!

## ঐচ্ছিক ধাপসমূহ

### Miniconda ইনস্টল করা

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) হলো [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python এবং কিছু প্যাকেজ ইনস্টল করার জন্য একটি হালকা ইন্সটলার।
Conda নিজেই একটি প্যাকেজ ম্যানেজার, যা বিভিন্ন Python [**ভার্চুয়াল এনভায়রনমেন্ট**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) এবং প্যাকেজ সেটআপ ও সুইচ করা সহজ করে। এছাড়াও, এটি এমন প্যাকেজ ইনস্টলের জন্যও কাজে লাগে, যেগুলো `pip`-এ নেই।

আপনি [MiniConda ইনস্টলেশন গাইড](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) অনুসরণ করে সেটআপ করতে পারেন।

Miniconda ইনস্টল হয়ে গেলে, আপনাকে [রিপোজিটরি](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ক্লোন করতে হবে (যদি আগে না করে থাকেন)।

এরপর, আপনাকে একটি ভার্চুয়াল এনভায়রনমেন্ট তৈরি করতে হবে। Conda দিয়ে করতে চাইলে, একটি নতুন environment ফাইল (_environment.yml_) তৈরি করুন। যদি Codespaces ব্যবহার করেন, তাহলে এটি `.devcontainer` ডিরেক্টরির মধ্যে তৈরি করুন, অর্থাৎ `.devcontainer/environment.yml`।

নিচের স্নিপেট দিয়ে environment ফাইলটি পূরণ করুন:

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

যদি conda ব্যবহার করতে গিয়ে কোনো সমস্যা হয়, তাহলে নিচের কমান্ড দিয়ে ম্যানুয়ালি Microsoft AI লাইব্রেরিগুলো ইনস্টল করতে পারেন।

```
conda install -c microsoft azure-ai-ml
```

এনভায়রনমেন্ট ফাইলে আমাদের দরকারি ডিপেন্ডেন্সিগুলো উল্লেখ করা আছে। `<environment-name>` হলো আপনার পছন্দের conda environment-এর নাম, এবং `<python-version>` হলো আপনি কোন ভার্সনের Python ব্যবহার করতে চান, যেমন `3` মানে Python-এর সর্বশেষ মেজর ভার্সন।

এটা হয়ে গেলে, নিচের কমান্ডগুলো টার্মিনালে চালিয়ে আপনার conda environment তৈরি করুন

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

যদি কোনো সমস্যা হয়, [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) দেখুন।

### Python সাপোর্ট এক্সটেনশনসহ Visual Studio Code ব্যবহার

আমরা এই কোর্সের জন্য [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) এডিটর এবং [Python সাপোর্ট এক্সটেনশন](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ইনস্টল করার পরামর্শ দিই। তবে এটি বাধ্যতামূলক নয়, শুধু সুপারিশ।

> **Note**: কোর্স রিপোজিটরি VS Code-এ খুললে, আপনি চাইলে প্রজেক্টটি কন্টেইনারে সেটআপ করতে পারবেন। কারণ কোর্স রিপোজিটরিতে [বিশেষ `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ডিরেক্টরি আছে। পরে এ নিয়ে আরও বলা হবে।

> **Note**: রিপো ক্লোন করে ডিরেক্টরি VS Code-এ খুললে, এটি স্বয়ংক্রিয়ভাবে Python সাপোর্ট এক্সটেনশন ইনস্টল করার পরামর্শ দেবে।

> **Note**: যদি VS Code রিপোজিটরি কন্টেইনারে পুনরায় খুলতে বলে, তাহলে অনুরোধটি প্রত্যাখ্যান করুন যাতে লোকালি ইনস্টল করা Python ব্যবহার করতে পারেন।

### ব্রাউজারে Jupyter ব্যবহার

আপনি চাইলে [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ব্যবহার করে সরাসরি ব্রাউজারেই প্রজেক্টে কাজ করতে পারেন। ক্লাসিক Jupyter এবং [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) দুটোই অটো-কমপ্লিশন, কোড হাইলাইটিং ইত্যাদি সুবিধাসহ সুন্দর ডেভেলপমেন্ট এনভায়রনমেন্ট দেয়।

লোকালি Jupyter চালু করতে, টার্মিনাল/কমান্ড লাইনে যান, কোর্স ডিরেক্টরিতে যান এবং চালান:

```bash
jupyter notebook
```

অথবা

```bash
jupyterhub
```

এতে একটি Jupyter ইনস্ট্যান্স চালু হবে এবং অ্যাক্সেসের URL কমান্ড লাইনে দেখাবে।

URL-এ গেলে, কোর্সের আউটলাইন দেখতে পাবেন এবং যেকোনো `*.ipynb` ফাইলে যেতে পারবেন। যেমন, `08-building-search-applications/python/oai-solution.ipynb`।

### কন্টেইনারে চালানো

আপনার কম্পিউটার বা Codespace-এ সবকিছু সেটআপ করার বিকল্প হিসেবে [কন্টেইনার](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) ব্যবহার করতে পারেন। কোর্স রিপোজিটরির বিশেষ `.devcontainer` ফোল্ডারটি VS Code-কে কন্টেইনারে প্রজেক্ট সেটআপ করতে সাহায্য করে। Codespaces-এর বাইরে এটি করতে হলে Docker ইনস্টল করতে হবে, এবং কিছুটা জটিল, তাই কন্টেইনার নিয়ে অভিজ্ঞদের জন্যই এটি সুপারিশ করা হয়।

GitHub Codespaces ব্যবহার করার সময় API কী নিরাপদ রাখার অন্যতম ভালো উপায় হলো Codespace Secrets ব্যবহার করা। বিস্তারিত জানতে [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) গাইড দেখুন।

## লেসন ও টেকনিক্যাল চাহিদা

এই কোর্সে ৬টি কনসেপ্ট লেসন এবং ৬টি কোডিং লেসন আছে।

কোডিং লেসনগুলোর জন্য আমরা Azure OpenAI Service ব্যবহার করছি। এই কোড চালাতে হলে Azure OpenAI সার্ভিসে অ্যাক্সেস এবং একটি API কী লাগবে। [এই আবেদনপত্র পূরণ করে](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) অ্যাক্সেসের জন্য আবেদন করতে পারেন।

আপনার আবেদন প্রক্রিয়াধীন থাকাকালীন, প্রতিটি কোডিং লেসনে একটি `README.md` ফাইল আছে যেখানে কোড ও আউটপুট দেখতে পারবেন।

## প্রথমবার Azure OpenAI Service ব্যবহার

যদি Azure OpenAI সার্ভিস প্রথমবার ব্যবহার করেন, তাহলে [Azure OpenAI Service resource তৈরি ও ডিপ্লয় করার গাইড](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) অনুসরণ করুন।

## প্রথমবার OpenAI API ব্যবহার

যদি OpenAI API প্রথমবার ব্যবহার করেন, তাহলে [ইন্টারফেস তৈরি ও ব্যবহারের গাইড](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) অনুসরণ করুন।

## অন্যান্য শিক্ষার্থীদের সাথে পরিচিত হন

আমাদের অফিসিয়াল [AI Community Discord সার্ভার](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)-এ অন্যান্য শিক্ষার্থীদের সাথে পরিচিত হওয়ার জন্য চ্যানেল তৈরি করা হয়েছে। এটি একই চিন্তাধারার উদ্যোক্তা, নির্মাতা, শিক্ষার্থী এবং জেনারেটিভ এআই-তে দক্ষতা বাড়াতে আগ্রহীদের জন্য নেটওয়ার্কিংয়ের দারুণ সুযোগ।

[![ডিসকর্ড চ্যানেলে যোগ দিন](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

প্রজেক্ট টিমও এই Discord সার্ভারে থাকবে, যাতে শিক্ষার্থীদের সাহায্য করতে পারে।

## অবদান রাখুন

এই কোর্সটি একটি ওপেন সোর্স উদ্যোগ। যদি উন্নতির সুযোগ বা কোনো সমস্যা দেখেন, তাহলে [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) তৈরি করুন অথবা [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) লগ করুন।

প্রজেক্ট টিম সব অবদান ট্র্যাক করবে। ওপেন সোর্সে অবদান রাখা জেনারেটিভ এআই-তে আপনার ক্যারিয়ার গড়ার অসাধারণ উপায়।

বেশিরভাগ অবদানের জন্য আপনাকে Contributor License Agreement (CLA)-তে সম্মতি দিতে হবে, যাতে আপনি আমাদেরকে আপনার অবদান ব্যবহারের অধিকার দেন। বিস্তারিত জানতে [CLA, Contributor License Agreement ওয়েবসাইট](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) দেখুন।

গুরুত্বপূর্ণ: এই রিপোতে টেক্সট অনুবাদ করার সময়, দয়া করে মেশিন অনুবাদ ব্যবহার করবেন না। আমরা কমিউনিটির মাধ্যমে অনুবাদ যাচাই করব, তাই কেবলমাত্র আপনি যেসব ভাষায় দক্ষ, সেসব ভাষার অনুবাদের জন্য স্বেচ্ছাসেবক হোন।

আপনি যখন pull request জমা দেবেন, একটি CLA-bot স্বয়ংক্রিয়ভাবে নির্ধারণ করবে আপনাকে CLA দিতে হবে কিনা এবং PR-এ যথাযথভাবে লেবেল/কমেন্ট দেবে। বটের নির্দেশনা অনুসরণ করুন। একবার CLA দিলে, আমাদের CLA ব্যবহার করা সব রিপোজিটরিতে আর দিতে হবে না।

এই প্রজেক্টে [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) গ্রহণ করা হয়েছে। আরও জানতে Code of Conduct FAQ পড়ুন অথবা [Email opencode](opencode@microsoft.com)-এ যোগাযোগ করুন।

## চলুন শুরু করি
এখন যেহেতু আপনি এই কোর্সটি সম্পন্ন করার জন্য প্রয়োজনীয় ধাপগুলো শেষ করেছেন, চলুন শুরু করি [জেনারেটিভ এআই এবং এলএলএম সম্পর্কে পরিচিতি](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) দিয়ে।

---

**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য নির্ভুলতা বজায় রাখার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল ভাষায় লেখা নথিটিই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হবে। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।