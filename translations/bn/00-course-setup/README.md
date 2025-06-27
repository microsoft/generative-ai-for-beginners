<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:42:32+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "bn"
}
-->
# এই কোর্সের সাথে শুরু করা

আমরা অত্যন্ত আনন্দিত যে আপনি এই কোর্স শুরু করছেন এবং জেনারেটিভ এআই দিয়ে কী তৈরি করতে অনুপ্রাণিত হচ্ছেন তা দেখতে!

আপনার সাফল্য নিশ্চিত করতে, এই পৃষ্ঠায় সেটআপ ধাপ, প্রযুক্তিগত প্রয়োজনীয়তা এবং প্রয়োজন হলে সাহায্য কোথায় পাবেন তা তুলে ধরা হয়েছে।

## সেটআপ ধাপ

এই কোর্স নেওয়া শুরু করতে, আপনাকে নিম্নলিখিত ধাপগুলি সম্পন্ন করতে হবে।

### ১. এই রিপোটি ফর্ক করুন

[এই পুরো রিপোটি ফর্ক করুন](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) আপনার নিজের গিটহাব অ্যাকাউন্টে যাতে আপনি কোড পরিবর্তন করতে পারেন এবং চ্যালেঞ্জগুলি সম্পন্ন করতে পারেন। আপনি এটিকে এবং সম্পর্কিত রিপোগুলিকে সহজে খুঁজে পেতে [স্টার (🌟) করতে পারেন](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)।

### ২. একটি কোডস্পেস তৈরি করুন

কোড চালানোর সময় কোনও নির্ভরতা সমস্যা এড়াতে, আমরা এই কোর্সটি একটি [গিটহাব কোডস্পেসে](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) চালানোর পরামর্শ দিই।

এটি তৈরি করতে আপনার ফর্ক করা রিপোতে `Code` অপশনটি নির্বাচন করুন এবং **কোডস্পেস** অপশনটি নির্বাচন করুন।

![কোডস্পেস তৈরি করার বোতামগুলি দেখানো ডায়ালগ](../../../00-course-setup/images/who-will-pay.webp)

### ৩. আপনার এপিআই কী সংরক্ষণ করা

কোনও প্রকার অ্যাপ্লিকেশন তৈরি করার সময় আপনার এপিআই কী নিরাপদ রাখা গুরুত্বপূর্ণ। আমরা সুপারিশ করি যে আপনার কোডে সরাসরি কোনও এপিআই কী সংরক্ষণ করবেন না। এই তথ্যগুলি একটি পাবলিক রিপোজিটরিতে কমিট করলে নিরাপত্তা সমস্যা এবং এমনকি খারাপ ব্যবহারকারীর দ্বারা ব্যবহার করা হলে অনাকাঙ্ক্ষিত খরচ হতে পারে।
পাইথনের জন্য `.env` ফাইল তৈরি এবং `GITHUB_TOKEN` যোগ করার জন্য একটি ধাপে ধাপে গাইড এখানে দেওয়া হল:

1. **আপনার প্রকল্প ডিরেক্টরিতে যান**: আপনার টার্মিনাল বা কমান্ড প্রম্পট খুলুন এবং যেখানে আপনি `.env` ফাইল তৈরি করতে চান সেই প্রকল্পের মূল ডিরেক্টরিতে যান।

   ```bash
   cd path/to/your/project
   ```

2. **`.env` ফাইল তৈরি করুন**: আপনার পছন্দের টেক্সট এডিটর ব্যবহার করে `.env` নামে একটি নতুন ফাইল তৈরি করুন। আপনি যদি কমান্ড লাইন ব্যবহার করছেন, তবে `touch` (on Unix-based systems) or `echo` ব্যবহার করতে পারেন (উইন্ডোজে):

   ইউনিক্স-ভিত্তিক সিস্টেম:
   ```bash
   touch .env
   ```

   উইন্ডোজ:
   ```cmd
   echo . > .env
   ```

3. **`.env` ফাইল সম্পাদনা করুন**: `.env` ফাইলটি একটি টেক্সট এডিটরে (যেমন, ভিএস কোড, নোটপ্যাড++, বা অন্য কোনো এডিটর) খুলুন। ফাইলে নিম্নলিখিত লাইনটি যোগ করুন, `your_github_token_here` এর পরিবর্তে আপনার প্রকৃত গিটহাব টোকেন দিন:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **ফাইলটি সংরক্ষণ করুন**: পরিবর্তনগুলি সংরক্ষণ করুন এবং টেক্সট এডিটর বন্ধ করুন।

5. **পাইথন অ্যাপ্লিকেশনে `.env` ফাইল থেকে পরিবেশ ভেরিয়েবল লোড করতে `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` প্যাকেজ ইনস্টল করুন। এটি `pip` ব্যবহার করে ইনস্টল করতে পারেন:

   ```bash
   pip install python-dotenv
   ```

6. **আপনার পাইথন স্ক্রিপ্টে পরিবেশ ভেরিয়েবল লোড করুন**: আপনার পাইথন স্ক্রিপ্টে, `.env` ফাইল থেকে পরিবেশ ভেরিয়েবল লোড করতে `python-dotenv` প্যাকেজ ব্যবহার করুন:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

এটাই! আপনি সফলভাবে একটি `.env` ফাইল তৈরি করেছেন, আপনার গিটহাব টোকেন যোগ করেছেন এবং এটি আপনার পাইথন অ্যাপ্লিকেশনে লোড করেছেন।

## আপনার কম্পিউটারে লোকালভাবে চালানো

আপনার কম্পিউটারে লোকালভাবে কোড চালানোর জন্য, আপনার [পাইথনের কিছু সংস্করণ ইনস্টল করা](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) থাকতে হবে।

এরপর রিপোজিটরি ব্যবহার করতে, আপনাকে এটি ক্লোন করতে হবে:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

সবকিছু চেক আউট হয়ে গেলে, আপনি শুরু করতে পারেন!

## ঐচ্ছিক ধাপসমূহ

### মিনিকন্ডা ইনস্টল করা

[মিনিকন্ডা](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) হল [কন্ডা](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), পাইথন, এবং কিছু প্যাকেজ ইনস্টল করার জন্য একটি লাইটওয়েট ইনস্টলার।
কন্ডা নিজেই একটি প্যাকেজ ম্যানেজার, যা বিভিন্ন পাইথন [**ভার্চুয়াল পরিবেশ**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) এবং প্যাকেজ সেটআপ এবং সুইচ করা সহজ করে তোলে। এটি এমন প্যাকেজ ইনস্টল করার জন্যও সুবিধাজনক যা `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` এর মাধ্যমে পাওয়া যায় না।

নিচের স্নিপেটটি দিয়ে আপনার পরিবেশ ফাইল পূরণ করুন:

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

যদি আপনি কন্ডা ব্যবহার করে ত্রুটি পান তবে আপনি ম্যানুয়ালি টার্মিনালে নিম্নলিখিত কমান্ড ব্যবহার করে মাইক্রোসফট এআই লাইব্রেরিগুলি ইনস্টল করতে পারেন।

```
conda install -c microsoft azure-ai-ml
```

পরিবেশ ফাইলটি আমাদের প্রয়োজনীয় নির্ভরতা নির্দিষ্ট করে। `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` হল পাইথনের সর্বশেষ প্রধান সংস্করণ।

এটি সম্পন্ন হয়ে গেলে, আপনি নিচের কমান্ডগুলি চালিয়ে আপনার কন্ডা পরিবেশ তৈরি করতে পারেন আপনার কমান্ড লাইন/টার্মিনালে

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

যদি কোনও সমস্যা হয় তবে [কন্ডা পরিবেশ গাইড](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) দেখুন।

### পাইথন সাপোর্ট এক্সটেনশন সহ ভিজ্যুয়াল স্টুডিও কোড ব্যবহার করা

আমরা এই কোর্সের জন্য [ভিজ্যুয়াল স্টুডিও কোড (ভিএস কোড)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) এডিটর ব্যবহার করার পরামর্শ দিই, যেখানে [পাইথন সাপোর্ট এক্সটেনশন](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ইনস্টল করা আছে। তবে এটি একটি সুপারিশ মাত্র, আবশ্যিক নয়।

> **নোট**: ভিএস কোডে কোর্স রিপোজিটরি খুললে, আপনি একটি কন্টেইনারের মধ্যে প্রকল্পটি সেটআপ করার অপশন পাবেন। এটি কোর্স রিপোজিটরির মধ্যে পাওয়া [বিশেষ `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ডিরেক্টরির কারণে। এটি পরে আরও বিস্তারিত জানানো হবে।

> **নোট**: যখন আপনি ডিরেক্টরিটি ক্লোন এবং ভিএস কোডে খুলবেন, তখন এটি স্বয়ংক্রিয়ভাবে আপনাকে একটি পাইথন সাপোর্ট এক্সটেনশন ইনস্টল করার সুপারিশ করবে।

> **নোট**: যদি ভিএস কোড আপনাকে একটি কন্টেইনারে রিপোজিটরিটি পুনরায় খোলার সুপারিশ করে, তবে স্থানীয়ভাবে ইনস্টল করা পাইথন সংস্করণ ব্যবহার করতে এই অনুরোধটি প্রত্যাখ্যান করুন।

### ব্রাউজারে জুপিটার ব্যবহার করা

আপনি ব্রাউজারের মধ্যে [জুপিটার পরিবেশ](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ব্যবহার করেও প্রকল্পে কাজ করতে পারেন। উভয় ক্লাসিক জুপিটার এবং [জুপিটার হাব](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) বেশ সুন্দর একটি উন্নয়ন পরিবেশ প্রদান করে, যেমন অটো-কমপ্লিশন, কোড হাইলাইটিং ইত্যাদি।

লোকালভাবে জুপিটার শুরু করতে, টার্মিনাল/কমান্ড লাইনে যান, কোর্স ডিরেক্টরিতে নেভিগেট করুন এবং চালান:

```bash
jupyter notebook
```

অথবা

```bash
jupyterhub
```

এটি একটি জুপিটার ইনস্ট্যান্স শুরু করবে এবং এটি অ্যাক্সেস করার ইউআরএলটি কমান্ড লাইন উইন্ডোতে দেখানো হবে।

একবার আপনি ইউআরএলটি অ্যাক্সেস করলে, আপনি কোর্সের আউটলাইন দেখতে পাবেন এবং যে কোনও `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` ফাইলে নেভিগেট করতে পারবেন যেখানে আপনি কোড এবং আউটপুট দেখতে পারবেন।

## প্রথমবারের জন্য আজুর ওপেনএআই সার্ভিস ব্যবহার করা

যদি এটি আপনার প্রথমবার আজুর ওপেনএআই সার্ভিসের সাথে কাজ করা হয়, তাহলে কীভাবে [আজুর ওপেনএআই সার্ভিস রিসোর্স তৈরি এবং মোতায়েন করবেন](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) সেই গাইডটি অনুসরণ করুন।

## প্রথমবারের জন্য ওপেনএআই এপিআই ব্যবহার করা

যদি এটি আপনার প্রথমবার ওপেনএআই এপিআই এর সাথে কাজ করা হয়, তাহলে কীভাবে [ইন্টারফেস তৈরি এবং ব্যবহার করবেন](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) সেই গাইডটি অনুসরণ করুন।

## অন্যান্য শিক্ষার্থীদের সাথে পরিচিত হন

আমরা আমাদের অফিসিয়াল [এআই কমিউনিটি ডিসকর্ড সার্ভারে](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) অন্যান্য শিক্ষার্থীদের সাথে পরিচিত হওয়ার জন্য চ্যানেল তৈরি করেছি। এটি একই মানসিকতার উদ্যোক্তা, নির্মাতা, শিক্ষার্থী এবং জেনারেটিভ এআই-এ উন্নতি করতে ইচ্ছুক যে কোনও ব্যক্তির সাথে নেটওয়ার্কিং করার একটি দুর্দান্ত উপায়।

[![ডিসকর্ড চ্যানেলে যোগ দিন](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

প্রকল্প দলটিও এই ডিসকর্ড সার্ভারে থাকবে শিক্ষার্থীদের সহায়তা করার জন্য।

## অবদান রাখুন

এই কোর্সটি একটি ওপেন সোর্স উদ্যোগ। যদি আপনি উন্নতির ক্ষেত্র বা সমস্যা দেখতে পান, তাহলে একটি [পুল রিকোয়েস্ট](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) তৈরি করুন বা একটি [গিটহাব সমস্যা](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) লগ করুন।

প্রকল্প দলটি সমস্ত অবদান ট্র্যাক করবে। ওপেন সোর্সে অবদান রাখা জেনারেটিভ এআই-এ আপনার ক্যারিয়ার গড়ার একটি অসাধারণ উপায়।

অধিকাংশ অবদান আপনাকে একটি কন্ট্রিবিউটর লাইসেন্স এগ্রিমেন্ট (সিএলএ) সম্মত হতে প্রয়োজন, যা ঘোষণা করে যে আপনি আমাদের আপনার অবদান ব্যবহারের অধিকার দেওয়ার অধিকার এবং আসলে তা করেন। বিস্তারিত জানার জন্য [সিএলএ, কন্ট্রিবিউটর লাইসেন্স এগ্রিমেন্ট ওয়েবসাইট](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) দেখুন।

গুরুত্বপূর্ণ: এই রিপোতে পাঠ্য অনুবাদ করার সময়, দয়া করে নিশ্চিত করুন যে আপনি মেশিন অনুবাদ ব্যবহার করবেন না। আমরা সম্প্রদায়ের মাধ্যমে অনুবাদ যাচাই করব, তাই দয়া করে শুধুমাত্র সেই ভাষায় অনুবাদের জন্য স্বেচ্ছাসেবক করুন যেখানে আপনি দক্ষ।

যখন আপনি একটি পুল রিকোয়েস্ট জমা দেন, তখন একটি সিএলএ-রোবট স্বয়ংক্রিয়ভাবে নির্ধারণ করবে যে আপনাকে সিএলএ প্রদান করতে হবে কিনা এবং পিআরটি যথাযথভাবে সাজিয়ে দেবে (যেমন, লেবেল, মন্তব্য)। রোবট দ্বারা প্রদত্ত নির্দেশাবলী অনুসরণ করুন। আমাদের সিএলএ ব্যবহারকারী সমস্ত রিপোজিটরিতে এটি একবার করতে হবে।

এই প্রকল্পটি [মাইক্রোসফট ওপেন সোর্স কোড অফ কন্ডাক্ট](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) গ্রহণ করেছে। আরও তথ্যের জন্য কোড অফ কন্ডাক্ট FAQ পড়ুন বা [ইমেইল ওপেনকোড](opencode@microsoft.com) এ যোগাযোগ করুন যে কোনও অতিরিক্ত প্রশ্ন বা মন্তব্যের জন্য।

## চলুন শুরু করি

এখন আপনি এই কোর্সটি সম্পন্ন করার জন্য প্রয়োজনীয় ধাপগুলি সম্পন্ন করেছেন, আসুন [জেনারেটিভ এআই এবং এলএলএমস-এর পরিচিতি](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) দিয়ে শুরু করি।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে সচেতন থাকুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অশুদ্ধি থাকতে পারে। এর নিজস্ব ভাষায় মূল নথিটি কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনও ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।