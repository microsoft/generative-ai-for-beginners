# এই কোর্স শুরু করা

আমরা খুবই উৎসাহিত যে আপনি এই কোর্স শুরু করতে যাচ্ছেন এবং দেখতে পাবেন আপনি Generative AI দিয়ে কী তৈরি করতে অনুপ্রাণিত হচ্ছেন!

আপনার সফলতা নিশ্চিত করতে, এই পৃষ্ঠাটি সেটআপ ধাপ, প্রযুক্তিগত প্রয়োজনীয়তা এবং প্রয়োজনে সাহায্য কোথায় পাবেন তা নির্দেশ করে।

## সেটআপ ধাপ

এই কোর্স নেওয়া শুরু করার জন্য, আপনাকে নিম্নলিখিত ধাপগুলি সম্পন্ন করতে হবে।

### ১। এই রিপো ফর্ক করুন

[এই পুরো রিপো ফর্ক করুন](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) আপনার নিজস্ব GitHub অ্যাকাউন্টে যাতে আপনি যেকোনো কোড পরিবর্তন করতে এবং চ্যালেঞ্জগুলি সম্পন্ন করতে পারেন। আপনি [এই রিপো (🌟) স্টার](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) করেও খুঁজে পেতে পারেন এবং সম্পর্কিত রিপোগুলো সহজে খুঁজে পেতে পারেন।

### ২। একটি কোডস্পেস তৈরি করুন

কোড চালানোর সময় ডিপেন্ডেন্সি সমস্যা এড়াতে, আমরা এই কোর্সটি [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) এ চালানোর পরামর্শ দিই।

আপনার ফর্কে: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/bn/who-will-pay.4c0609b1c7780f44.webp)

#### ২.১ একটি সিক্রেট যোগ করুন

১। ⚙️ গিয়ার আইকন -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
২। নাম দিন OPENAI_API_KEY, আপনার কী পেস্ট করুন, Save করুন।

### ৩। পরবর্তীতে কী করবেন?

| আমি যা করতে চাই…        | যান…                                                                    |
|-------------------------|-------------------------------------------------------------------------|
| পাঠ ১ শুরু করুন          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| অফলাইনে কাজ করুন         | [`setup-local.md`](02-setup-local.md)                                   |
| একটি LLM প্রদানকারী সেটআপ করুন | [`providers.md`](03-providers.md)                                        |
| অন্য শেখোয়ালাদের সাথে পরিচিত হন | [আমাদের Discord এ যোগ দিন](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## সমস্যা সমাধান


| উপসর্গ                                   | সমাধান                                                             |
|------------------------------------------|-----------------------------------------------------------------|
| কন্টেইনার বিল্ড ১০ মিনিটের বেশি আটকে রয়েছে | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | টার্মিনাল সংযুক্ত হয়নি; ক্লিক করুন **+** ➜ *bash*                |
| OpenAI থেকে `401 Unauthorized`             | ভুল / মেয়াদউত্তীর্ণ `OPENAI_API_KEY`                            |
| VS Code দেখায় “Dev container mounting…”   | ব্রাউজার ট্যাব রিফ্রেশ করুন—কখনও কখনও Codespaces সংযোগ হারায়  |
| নোটবুক কার্নেল অনুপস্থিত                   | নোটবুক মেনু ➜ **Kernel ▸ Select Kernel ▸ Python 3**               |

   ইউনিক্স-বেইজড সিস্টেম:

   ```bash
   touch .env
   ```

   উইন্ডোজ:

   ```cmd
   echo . > .env
   ```

৩. **`.env` ফাইল সম্পাদনা করুন**: `.env` ফাইলটি একটি টেক্সট এডিটরে (যেমন, VS Code, Notepad++, বা অন্য কোনো এডিটর) খুলুন। ফাইলটিতে নিম্নলিখিত লাইনগুলি যোগ করুন, প্লেসহোল্ডারগুলোর পরিবর্তে আপনার আসল Microsoft Foundry Models এর এন্ডপয়েন্ট এবং কী দিন (কিভাবে পাওয়া যায় দেখুন [`providers.md`](03-providers.md)):

   > **মন্তব্য:** GitHub Models (এবং এর `GITHUB_TOKEN` ভেরিয়েবল) জুলাই ২০২৬ শেষের মধ্যে অবসর নিচ্ছে। পরিবর্তে [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ব্যবহার করুন।

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

৪. **ফাইল সংরক্ষণ করুন**: পরিবর্তনগুলি সংরক্ষণ করুন এবং টেক্সট এডিটর বন্ধ করুন।

৫. **`python-dotenv` ইনস্টল করুন**: যদি আপনি ইতিমধ্যে না করে থাকেন, তাহলে `.env` ফাইল থেকে পরিবেশ ভেরিয়েবল লোড করার জন্য `python-dotenv` প্যাকেজ ইনস্টল করতে হবে। আপনি `pip` দিয়ে এটি ইনস্টল করতে পারেন:

   ```bash
   pip install python-dotenv
   ```

৬. **আপনার পাইথন স্ক্রিপ্টে পরিবেশ ভেরিয়েবল লোড করুন**: আপনার পাইথন স্ক্রিপ্টে, `.env` ফাইল থেকে পরিবেশ ভেরিয়েবল লোড করার জন্য `python-dotenv` প্যাকেজ ব্যবহার করুন:

   ```python
   from dotenv import load_dotenv
   import os

   # .env ফাইল থেকে পরিবেশ ভেরিয়েবলগুলি লোড করুন
   load_dotenv()

   # Microsoft Foundry মডেল ভেরিয়েবলগুলিতে অ্যাক্সেস করুন
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

এতেই শেষ! আপনি সফলভাবে `.env` ফাইল তৈরি করেছেন, আপনার Microsoft Foundry Models ক্রেডেনশিয়াল যোগ করেছেন, এবং সেগুলো আপনার পাইথন অ্যাপ্লিকেশনে লোড করেছেন।

## আপনার কম্পিউটারে লোকালি কীভাবে চালাবেন

আপনার কম্পিউটারে কোড লোকালি চালানোর জন্য, আপনার কাছে কিছু সংস্করণের [Python ইনস্টল থাকতে হবে](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)।

এরপর রিপো ব্যবহার করার জন্য, এটিকে ক্লোন করতে হবে:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

একবার সবকিছু চেকআউট হয়ে গেলে, আপনি শুরু করতে পারেন!

## ঐচ্ছিক ধাপ

### মিনিকন্ডা ইনস্টলেশন

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) হল হালকা একটি ইনস্টলার যা [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, এবং কিছু প্যাকেজ ইনস্টল করতে সাহায্য করে।
Conda নিজেই একটি প্যাকেজ ম্যানেজার, যা বিভিন্ন Python [**ভার্চুয়াল পরিবেশ**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) এবং প্যাকেজ সহজে সেটআপ ও পরিবর্তন করতে দেয়। এটি এমন প্যাকেজ ইনস্টলেও কাজে লাগে যা `pip` দিয়ে পাওয়া যায় না।

আপনি [MiniConda ইনস্টলেশন গাইড](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) অনুসরণ করে এটি সেটআপ করতে পারেন।

মিনিকন্ডা ইনস্টল করার পর, আপনাকে রিপোটি [ক্লোন করতে হবে](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (যদি না করে থাকেন)

এরপর আপনাকে একটি ভার্চুয়াল পরিবেশ তৈরি করতে হবে। conda দিয়ে এটি করতে, একটি নতুন পরিবেশ ফাইল (_environment.yml_) তৈরি করুন। যদি আপনি Codespaces ব্যবহার করছেন, তাহলে এটি `.devcontainer` ডিরেক্টরির মধ্যে থাকুক, অর্থাৎ `.devcontainer/environment.yml`।

নিচের স্নিপেট দিয়ে আপনার environment ফাইলটি পূরণ করুন:

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

যদি conda ব্যবহার করতে গিয়ে ত্রুটি পান, তাহলে টার্মিনালে নিচের কমান্ড দিয়ে Microsoft AI Libraries ম্যানুয়ালি ইনস্টল করতে পারেন।

```
conda install -c microsoft azure-ai-ml
```

পরিবেশ ফাইলটি আমাদের দরকার এমন ডিপেন্ডেন্সিগুলো উল্লেখ করে। `<environment-name>` মানে আপনার কন্ডা পরিবেশের নাম, আর `<python-version>` হল আপনি যে পায়থনের সংস্করণ ব্যবহার করতে চান, উদাহরণস্বরূপ, `3` হল সর্বশেষ প্রধান সংস্করণ।

এটা করার পর, নিচের কমান্ডগুলো চালিয়ে কন্ডা পরিবেশ তৈরি করুন:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer সাব পাথ শুধুমাত্র কোডস্পেস সেটআপগুলিতে প্রযোজ্য
conda activate ai4beg
```

কোনো সমস্যা হলে [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) দেখুন।

### পাইথন সাপোর্ট এক্সটেনশনসহ ভিজুয়াল স্টুডিও কোড ব্যবহার

আমরা এই কোর্সের জন্য [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) সম্পাদকটির [Python সাপোর্ট এক্সটেনশন](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ইনস্টল করে ব্যবহার করার পরামর্শ দিই। তবে এটা বাধ্যতামূলক নয়, শুধুমাত্র পরামর্শ।

> **মন্তব্য**: কোর্স রিপো VS Code এ খুললে, আপনি প্রজেক্টকে একটি কন্টেইনারের মধ্যে সেটআপ করার অপশন পাবেন। কারণ কোর্স রিপোর মধ্যে একটি [বিশেষ `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ডিরেক্টরি রয়েছে। পরে এ সম্পর্কে আরও।

> **মন্তব্য**: রিপো ক্লোন ও VS Code এ খুললে, এটি স্বয়ংক্রিয়ভাবে পাইথন সাপোর্ট এক্সটেনশন ইনস্টল করার প্রস্তাব দেবে।

> **মন্তব্য**: যদি VS Code রিপোটি কন্টেইনারে পুনরায় খোলার প্রস্তাব দেয়, তাহলে স্থানীয় ইনস্টল করা পাইথন ব্যবহার করতে এটি প্রত্যাখ্যান করুন।

### ব্রাউজারে জুপিটার ব্যবহার

আপনি প্রজেক্টে ব্রাউজারের মধ্যেই [Jupyter পরিবেশ](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ব্যবহার করে কাজ করতে পারেন। ক্লাসিক্যাল জুপিটার এবং [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) দুটোই একটি আরামদায়ক ডেভেলপমেন্ট পরিবেশ প্রদান করে, যার মধ্যে আছে অটো-কাম্পলিশন, কোড হাইলাইটিং, ইত্যাদি।

লোকালি জুপিটার শুরু করতে, টার্মিনাল/কমান্ড লাইনে যান, কোর্স ডিরেক্টরিতে নেভিগেট করুন, এবং চালান:

```bash
jupyter notebook
```

অথবা

```bash
jupyterhub
```

এটি একটি জুপিটার ইনস্ট্যান্স শুরু করবে এবং অ্যাক্সেসের URL কমান্ড লাইন উইন্ডোতে প্রদর্শিত হবে।

একবার URL এ অ্যাক্সেস করলে, আপনি কোর্সের আউটলাইন দেখতে পাবেন এবং যেকোনো `*.ipynb` ফাইলে যেতে পারবেন। উদাহরণস্বরূপ, `08-building-search-applications/python/oai-solution.ipynb`।

### একটি কন্টেইনারে চালানো

আপনার কম্পিউটার বা কোডস্পেসে সবকিছু সেটআপ করার পরিবর্তে [কন্টেইনার](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) ব্যবহার করা যেতে পারে। কোর্স রিপোর বিশেষ `.devcontainer` ফোল্ডারটি VS Code কে প্রজেক্টকে একটি কন্টেইনারের মধ্যে সেটআপ করতে সাহায্য করে। Codespaces এ বাইরে, এর জন্য ডকার ইনস্টল করতে হবে, এবং এটি কিছুটা কাজের ব্যাপার, তাই আমরা শুধুমাত্র কন্টেইনার নিয়ে কাজের অভিজ্ঞতা থাকা লোকেদের জন্যই এটি পরামর্শ দিই।

GitHub Codespaces ব্যবহার করার সময় API কী নিরাপদে রাখতে Codespace Secrets ব্যবহার করা উত্তম। বিস্তারিত জানতে [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) গাইডটি অনুসরণ করুন।


## পাঠ এবং প্রযুক্তিগত প্রয়োজনীয়তা

কোর্সটিতে "শিখুন" পাঠ রয়েছে যা Generative AI ধারণাগুলি ব্যাখ্যা করে এবং "তৈরি করুন" পাঠ রয়েছে যেগুলোতে সম্ভব হলে **Python** এবং **TypeScript** এ হাতে-কলমে কোড উদাহরণ দেওয়া হয়েছে।

কোডিং পাঠের জন্য, আমরা Microsoft Foundry এর Azure OpenAI ব্যবহার করি। আপনার একটি Azure সাবস্ক্রিপশন এবং API কী থাকা প্রয়োজন। অ্যাক্সেস খোলা - কোনো আবেদন প্রয়োজন নেই - তাই আপনি [Microsoft Foundry রিসোর্স তৈরি করুন এবং একটি মডেল ডিপ্লয় করুন](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) আপনার এন্ডপয়েন্ট এবং কী পেতে।

প্রতিটি কোডিং পাঠের সাথে একটি `README.md` ফাইলও থাকে যেখানে আপনি কোড এবং আউটপুট না চালিয়েও দেখতে পারেন।

## প্রথমবার Azure OpenAI সেবা ব্যবহার করা

যদি এটি আপনার প্রথমবার Azure OpenAI সেবা ব্যবহার করা হয়, তাহলে অনুগ্রহ করে [Azure OpenAI সেবা রিসোর্স কিভাবে তৈরি এবং ডিপ্লয় করবেন](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) গাইডটি অনুসরণ করুন।

## প্রথমবার OpenAI API ব্যবহার করা

যদি এটি আপনার প্রথমবার OpenAI API কাজ করা হয়, তাহলে অনুগ্রহ করে [ইন্টারফেস কিভাবে তৈরি এবং ব্যবহার করবেন](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) গাইডটি অনুসরণ করুন।

## অন্যান্য শেখোয়ালাদের সাথে পরিচিত হওয়া

আমরা আমাদের অফিসিয়াল [AI Community Discord সার্ভারে](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) অন্যান্য শেখোয়ালাদের সাথে মিটিং চ্যানেল তৈরি করেছি। এটা অনুরূপ আকাঙ্ক্ষাসম্পন্ন উদ্যোক্তা, নির্মাতা, ছাত্র, এবং Generative AI-তে উন্নতি করতে আগ্রহী যেকেউ সাথে নেটওয়ার্ক করার জন্য চমৎকার উপায়।

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

প্রকল্প দলও এই Discord সার্ভারে থাকবে শেখোয়ালাদের সাহায্য করার জন্য।

## অবদান রাখা

এই কোর্স একটি ওপেন-সোর্স উদ্যোগ। যদি আপনি উন্নতির ক্ষেত্র বা সমস্যা দেখতে পান, অনুগ্রহ করে একটি [পুল রিকোয়েস্ট](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) তৈরি করুন বা [GitHub ইস্যু](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) লগ করুন।

প্রকল্প দল সব অবদান ট্র্যাক করবে। ওপেন সোর্সে অবদান রাখা Generative AI এর ক্ষেত্রে আপনার ক্যারিয়ার গড়ার চমৎকার উপায়।

বেশিরভাগ অবদানে আপনার Contributor License Agreement (CLA) মেনে চলা প্রয়োজন, যা আপনাকে নিশ্চিত করতে হবে যে আপনি আপনার অবদান ব্যবহারের অধিকার রাখেন এবং আসলেই অনুমতি দেন। বিস্তারিত জানতে [CLA, Contributor License Agreement ওয়েবসাইট](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) দেখুন।

গুরুত্বপূর্ণ: এই রিপোতে অনুবাদ করার সময়, দয়া করে মেশিন ট্রান্সলেশন ব্যবহার করবেন না। আমরা অনুবাদ কমিউনিটির মাধ্যমে যাচাই করব, তাই শুধুমাত্র যে ভাষায় আপনি পারদর্শী, সেই ভাষায় অনুবাদের জন্য স্বেচ্ছাসেবক হোন।


যখন আপনি একটি পুল রিকোয়েস্ট জমা দেবেন, একটি CLA-বট স্বয়ংক্রিয়ভাবে নির্ধারণ করবে আপনার CLA প্রদান করতে হবে কিনা এবং উপযুক্তভাবে PR সজ্জিত করবে (যেমন, লেবেল, মন্তব্য)। শুধুমাত্র বট দ্বারা প্রদত্ত নির্দেশাবলী অনুসরণ করুন। সমস্ত রিপোজিটরির জন্য আমাদের CLA ব্যবহার করার সময় আপনাকে এটি একবারই করতে হবে।

এই প্রকল্পটি [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) গ্রহণ করেছে। আরও তথ্যের জন্য কোড অফ কন্ডাক্ট FAQ পড়ুন অথবা অতিরিক্ত প্রশ্ন বা মন্তব্যের জন্য [Email opencode](opencode@microsoft.com) এ যোগাযোগ করুন।

## চল শুরু করা যাক

এখন যেহেতু আপনি এই কোর্সটি সম্পন্ন করার জন্য প্রয়োজনীয় ধাপগুলো শেষ করেছেন, চল শুরু করা যাক একটি [Generative AI এবং LLMs এর ভূমিকা](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) পেয়ে।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->