# এই কোর্স শুরু করা

আমরা অত্যন্ত উত্তেজিত যে আপনি এই কোর্স শুরু করছেন এবং দেখবেন আপনি Generative AI দিয়ে কী তৈরি করতে অনুপ্রাণিত হচ্ছেন!

আপনার সফলতা নিশ্চিত করার জন্য, এই পৃষ্ঠাটি সেটআপ ধাপ, প্রযুক্তিগত প্রয়োজনীয়তা এবং প্রয়োজনে সাহায্য কোথায় পাবেন তা বর্ণনা করে।

## সেটআপ ধাপ

এই কোর্স নিতে শুরু করার জন্য, আপনাকে নিম্নলিখিত ধাপগুলি সম্পন্ন করতে হবে।

### ১. এই রিপো ফর্ক করুন

[এই পুরো রিপো ফর্ক করুন](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) আপনার নিজস্ব GitHub অ্যাকাউন্টে যাতে আপনি যেকোনো কোড পরিবর্তন করতে এবং চ্যালেঞ্জগুলো সম্পন্ন করতে পারেন। আপনি এই রিপোটি সহজে খুঁজে পেতে এবং সম্পর্কিত রিপোগুলো পেতে [তারাও দিতে পারেন (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)।

### ২. একটি কোডস্পেস তৈরি করুন

কোড চালানোর সময় কোনো নির্ভরতার সমস্যা এড়াতে, আমরা সুপারিশ করছি এই কোর্সটি [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) এ চালানোর।

আপনার ফর্কে: **Code -> Codespaces -> New on main**

![কোডস্পেস তৈরি করার বাটন দেখানো ডায়ালগ](../../../translated_images/bn/who-will-pay.4c0609b1c7780f44.webp)

#### ২.১ একটি গোপনীয় তথ্য যোগ করুন

১. ⚙️ গিয়ার আইকন -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
২. নাম দিন OPENAI_API_KEY, আপনার কী পেস্ট করুন, Save করুন।

### ৩. পরবর্তী ধাপ কী?

| আমি চাই…           | যান…                                                                 |
|---------------------|----------------------------------------------------------------------|
| প্রথম পাঠ শুরু করুন | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)  |
| অফলাইন কাজ করুন    | [`setup-local.md`](02-setup-local.md)                                |
| একটি LLM প্রদানকারী সেটআপ করুন | [`providers.md`](03-providers.md)                               |
| অন্যান্য শিক্ষার্থীদের সাথে পরিচিত হন | [আমাদের Discord এ যোগ দিন](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## সমস্যা সমাধান


| লক্ষণ                                     | সমাধান                                                        |
|------------------------------------------|---------------------------------------------------------------|
| কন্টেইনার বিল্ড ১০ মিনিটের বেশি আটকে যায় | **Codespaces ➜ “Rebuild Container”**                         |
| `python: command not found`               | টার্মিনাল সংযুক্ত হয়নি; **+** ক্লিক করুন ➜ *bash*            |
| OpenAI থেকে `401 Unauthorized`            | ভুল / মেয়াদ উত্তীর্ণ `OPENAI_API_KEY`                       |
| VS Code দেখায় “Dev container mounting…” | ব্রাউজার ট্যাব রিফ্রেশ করুন—কোডস্পেস মাঝে মাঝে সংযোগ হারায় |
| নোটবুক কার্নেল মিসিং                       | নোটবুক মেনু ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   ইউনিক্স-ভিত্তিক সিস্টেম:

   ```bash
   touch .env
   ```

   উইন্ডোজ:

   ```cmd
   echo . > .env
   ```

৩. **`.env` ফাইল সম্পাদনা করুন**: একটি টেক্সট এডিটর (উদাহরণস্বরূপ, VS Code, Notepad++, অথবা অন্য যে কোনো এডিটর) এ `.env` ফাইলটি খুলুন। ফাইলটিতে নিচের লাইনগুলো যোগ করুন, যেখানে প্লেসহোল্ডারগুলো আপনার আসল Microsoft Foundry Models এন্ডপয়েন্ট এবং কী দিয়ে প্রতিস্থাপন করবেন ([`providers.md`](03-providers.md) দেখুন কীভাবে পাবেন):

   > **টিপ:** GitHub Models (এবং এর `GITHUB_TOKEN` ভেরিয়েবল) জুলাই ২০২৬ এর শেষে অবসর নিচ্ছে। বরং [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ব্যবহার করুন।

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

৪. **ফাইলটি সেভ করুন**: পরিবর্তনগুলো সেভ করুন এবং টেক্সট এডিটর বন্ধ করুন।

৫. **`python-dotenv` ইন্সটল করুন**: যদি এখনও না করে থাকেন, তাহলে `.env` ফাইল থেকে পরিবেশ ভেরিয়েবল লোড করার জন্য `python-dotenv` প্যাকেজটি ইনস্টল করতে হবে। পিপ ব্যবহার করে ইনস্টল করতে পারেন:

   ```bash
   pip install python-dotenv
   ```

৬. **আপনার পাইথন স্ক্রিপ্টে পরিবেশ ভেরিয়েবল লোড করুন**: আপনার পাইথন স্ক্রিপ্টে `python-dotenv` প্যাকেজ ব্যবহার করে `.env` ফাইল থেকে ভেরিয়েবল লোড করুন:

   ```python
   from dotenv import load_dotenv
   import os

   # .env ফাইল থেকে পরিবেশ ভেরিয়েবল লোড করুন
   load_dotenv()

   # Microsoft Foundry Models ভেরিয়েবলগুলিতে প্রবেশ করুন
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

এতই! আপনি সফলভাবে `.env` ফাইল তৈরি করেছেন, আপনার Microsoft Foundry Models সার্টিফিকেট যোগ করেছেন, এবং সেগুলো আপনার পাইথন অ্যাপ্লিকেশনে লোড করেছেন।

## আপনার কম্পিউটারে লোকালি কিভাবে চালাবেন

কোড লোকালি চালানোর জন্য আপনার কম্পিউটারে কিছু সংস্করণের [Python ইন্সটল থাকতে হবে](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)।

পরে রিপোসিটরিটি ব্যবহার করতে আপনাকে ক্লোন করতে হবে:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

সবকিছু চেক আউট করার পর আপনি শুরু করতে পারেন!

## ঐচ্ছিক ধাপ

### মিনিকন্ডা ইনস্টল করা

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) হলো হালকা ওজনের ইনস্টলার যা [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python এবং কিছু প্যাকেজ ইনস্টল করতে ব্যবহার হয়।
Conda নিজেই একটি প্যাকেজ ম্যানেজার, যা বিভিন্ন Python [**ভার্চুয়াল এনভায়রনমেন্ট**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) এবং প্যাকেজ সহজে সেটআপ ও সুইচ করতে দেয়। এটি `pip` এ পাওয়া না যাওয়া প্যাকেজ ইনস্টলেও সাহায্য করে।

[MiniConda ইনস্টলেশন গাইড](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) অনুসরণ করে এটি সেটআপ করতে পারেন।

মিনিকন্ডা ইনস্টল হওয়ার পর, আপনাকে [রিপোসিটরি](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ক্লোন করতে হবে (যদি এখনও না করে থাকেন)

পরবর্তী ধাপে একটি ভার্চুয়াল এনভায়রনমেন্ট তৈরি করতে হবে। Conda ব্যবহার করে এটি করার জন্য একটি নতুন এনভায়রনমেন্ট ফাইল (_environment.yml_) তৈরি করুন। আপনি যদি Codespaces ব্যবহার করেন, তাহলে এটি `.devcontainer` ডিরেক্টরির মধ্যে তৈরি করুন, অর্থাৎ `.devcontainer/environment.yml`।

নিচের কোড স্নিপেট ব্যবহার করে আপনার এনভায়রনমেন্ট ফাইল পূরণ করুন:

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

যদি কোন্ডা ব্যবহারের সময় ত্রুটি পান তাহলে Microsoft AI Libraries ম্যানুয়ালি ইনস্টল করতে টার্মিনালে নিচের কমান্ডটি ব্যবহার করতে পারেন।

```
conda install -c microsoft azure-ai-ml
```

এনভায়রনমেন্ট ফাইলটি আমাদের প্রয়োজনীয় ডিপেন্ডেন্সিগুলো নির্ধারণ করে। `<environment-name>` হলো আপনার পছন্দসই Conda এনভায়রনমেন্ট নাম, এবং `<python-version>` হলো ব্যবহার করতে চান এমন পাইথনের সংস্করণ, উদাহরণস্বরূপ, `3` হলো পাইথনের সর্বশেষ প্রধান সংস্করণ।

এরপর নিচের কমান্ডগুলো চালিয়ে আপনার Conda এনভায়রনমেন্ট তৈরি করুন:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer সাবপাথ শুধুমাত্র Codespace সেটআপগুলিতে প্রযোজ্য
conda activate ai4beg
```

কোনো সমস্যা হলে [Conda এনভায়রনমেন্ট গাইড](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) দেখুন।

### পাইথন সাপোর্ট এক্সটেনশনসহ Visual Studio Code ব্যবহার

আমরা এই কোর্সের জন্য [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) সম্পাদকটি সহ [Python সাপোর্ট এক্সটেনশন](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ইনস্টল করে ব্যবহারের পরামর্শ দিচ্ছি। তবে এটি একটি পরামর্শ এবং বাধ্যতামূলক নয়।

> **টিপ:** VS Code এ কোর্স রিপোসিটরি খুললে আপনি প্রজেক্টকে একটি কন্টেইনারের মধ্যে সেটআপ করার অপশন পাবেন। এর কারণ হলো কোর্স রিপোসিটরির মধ্যে থাকা [বিশেষ `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ডিরেক্টরি। এ ব্যাপারে পরে আরও বলা হবে।

> **টিপ:** রিপোসিটরি ক্লোন এবং VS Code এ খুললেই এটি স্বয়ংক্রিয়ভাবে Python সাপোর্ট এক্সটেনশন ইনস্টল করার পরামর্শ দেবে।

> **টিপ:** VS Code যদি আপনাকে রিপোসিটরি কন্টেইনারে পুনরায় খুলতে বলে, তবে লোকালি ইন্সটল করা Python ব্যবহার করতে সেই অনুরোধ ফিরিয়ে দিন।

### ব্রাউজারে Jupyter ব্যবহার

আপনি প্রকল্পে ব্রাউজারের মধ্যেই [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ব্যবহার করতে পারেন। ক্লাসিক্যাল Jupyter এবং [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) একটি সুখকর উন্নয়ন পরিবেশ প্রদান করে যেমন অটো-সম্পূর্ণতা, কোড হাইলাইটিং ইত্যাদি।

লোকালি Jupyter শুরু করতে টার্মিনালে যান, কোর্স ডিরেক্টরিতে নেভিগেট করুন, এবং চালান:

```bash
jupyter notebook
```

অথবা

```bash
jupyterhub
```

এটি একটি Jupyter ইনস্ট্যান্স শুরু করবে এবং অ্যাক্সেস করার URL কমান্ড লাইন উইন্ডোতে দেখাবে।

URL অ্যাক্সেস করলে আপনি কোর্সের আউটলাইন দেখতে পাবেন এবং যেকোনো `*.ipynb` ফাইলে নেভিগেট করতে পারবেন। উদাহরণস্বরূপ, `08-building-search-applications/python/oai-solution.ipynb`।

### কন্টেইনারে চালানো

আপনার কম্পিউটার বা কোডস্পেসে সবকিছু সেটআপ করার বিকল্প হলো একটি [কন্টেইনার](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) ব্যবহার করা। কোর্স রিপোসিটরির মধ্যে থাকা বিশেষ `.devcontainer` ফোল্ডারটি VS Code কে প্রজেক্টকে একটি কন্টেইনারের মধ্যে সেটআপ করার সুযোগ দেয়। কোডস্পেসের বাইরে, এটি করতে ডকার ইনস্টল করতে হবে এবং সেজন্য কিছুটা কাজ লাগবে, তাই আমরা কেবল কন্টেইনার ব্যবহারে অভিজ্ঞদের জন্য এই পদ্ধতি সুপারিশ করছি।

GitHub Codespaces ব্যবহার করার সময় API কী সুরক্ষিত রাখার সেরা উপায় হলো Codespace Secrets ব্যবহার করা। এই বিষয়ে জানার জন্য দয়া করে [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) গাইড অনুসরণ করুন।


## পাঠ এবং প্রযুক্তিগত প্রয়োজনীয়তা

এই কোর্সে ৬টি ধারণাগত পাঠ এবং ৬টি কোডিং পাঠ রয়েছে।

কোডিং পাঠের জন্য আমরা Azure OpenAI সেবা ব্যবহার করছি। এই কোড চালাতে আপনাকে Azure OpenAI সেবায় অ্যাক্সেস এবং API কী প্রয়োজন। অ্যাক্সেস পেতে [এই অ্যাপ্লিকেশনটি সম্পন্ন](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) করতে পারেন।

আপনার আবেদন প্রক্রিয়া চলাকালীন, প্রতিটি কোডিং পাঠের সাথে একটি `README.md` ফাইলও রয়েছে যেখানে আপনি কোড এবং আউটপুট দেখতে পারেন।

## প্রথমবার Azure OpenAI পরিষেবা ব্যবহার

এটি যদি আপনার প্রথমবার Azure OpenAI সেবা ব্যবহার, তাহলে [Azure OpenAI Service রিসোর্স তৈরি এবং ডিপ্লয়মেন্টের গাইড](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) অনুসরণ করুন।

## প্রথমবার OpenAI API ব্যবহার

এটি যদি আপনার প্রথমবার OpenAI API ব্যবহার, তাহলে [ইন্টারফেস তৈরি এবং ব্যবহারের গাইড](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) অনুসরণ করুন।

## অন্যান্য শিক্ষার্থীদের সাথে পরিচিত হন

আমরা আমাদের অফিসিয়াল [AI কমিউনিটি Discord সার্ভারে](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) চ্যানেল তৈরি করেছি যেখানে অন্যান্য শিক্ষার্থীদের সাথে মিলিত হওয়া যায়। এটি অন্যান্য সদৃশ-মনা উদ্যোক্তা, নির্মাতা, ছাত্র এবং যেকেউ যারা Generative AI এ উন্নতি করতে চায় তাদের সাথে নেটওয়ার্ক তৈরির দুর্দান্ত উপায়।

[![Discord চ্যানেলে যোগ দিন](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

প্রজেক্ট টিমও এই Discord সার্ভারে থাকবে শিক্ষার্থীদের সাহায্যের জন্য।

## অবদান রাখুন

এই কোর্স একটি ওপেন সোর্স উদ্যোগ। আপনি যদি উন্নতির কোনো ক্ষেত্র বা সমস্যা দেখেন, অনুগ্রহ করে একটি [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) তৈরি করুন অথবা একটি [GitHub ইস্যু লগ করুন](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)।

প্রজেক্ট টিম সব অবদান ট্র্যাক করবে। ওপেন সোর্সে অবদান রাখা Generative AI তে আপনার ক্যারিয়ার গড়ার একটি অসাধারণ উপায়।

বেশিরভাগ অবদানকারীকে একটি Contributor License Agreement (CLA) স্বীকার করতে হয় যা ঘোষণা করে যে আপনি আপনার অবদান ব্যবহার করার অধিকার আমাদের দিচ্ছেন। বিস্তারিত জানতে যান [CLA, Contributor License Agreement ওয়েবসাইটে](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)।

গুরুত্বপূর্ণ: এই রিপোতে লেখা অনুবাদের সময়, অনুগ্রহ করে নিশ্চিত করুন যে আপনি মেশিন অনুবাদ ব্যবহার করছেন না। আমরা অনুবাদগুলো কমিউনিটির মাধ্যমে যাচাই করব, তাই শুধু সেই ভাষার জন্যই স্বেচ্ছাসেবক হোন যার আপনি দক্ষ।

যখন আপনি একটি পুল রিকোয়েস্ট জমা দেবেন, একটি CLA-বট স্বয়ংক্রিয়ভাবে নির্ধারণ করবে আপনি CLA প্রদান করতে হবে কিনা এবং PR উপযুক্তভাবে সাজাবে (যেমন, লেবেল, মন্তব্য)। বটের নির্দেশনা অনুসরণ করুন। আমাদের CLA ব্যবহার করে সব রিপোতে একবার শুধু এটি করতে হবে।


এই প্রকল্পটি [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) গ্রহণ করেছে। আরও তথ্যের জন্য Code of Conduct FAQ পড়ুন অথবা অতিরিক্ত প্রশ্ন বা মন্তব্যের জন্য [Email opencode](opencode@microsoft.com) এ যোগাযোগ করুন।

## চলুন শুরু করি

এখন যেহেতু আপনি এই কোর্সটি সম্পূর্ণ করার জন্য প্রয়োজনীয় ধাপগুলি শেষ করেছেন, চলুন শুরু করা যাক [Generative AI এবং LLMs এর একটি পরিচিতি](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) নিয়ে।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->