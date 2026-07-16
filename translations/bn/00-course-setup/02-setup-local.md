# স্থানীয় সেটআপ 🖥️

**এই গাইডটি ব্যবহার করুন যদি আপনি সবকিছু আপনার নিজস্ব ল্যাপটপে চালাতে চান।**  
আপনার দুইটি পথ আছে: **(A) নেটিভ পাইথন + ভার্চুয়াল-এনভ** অথবা **(B) VS কোড ডেভ কন্টেইনার উইথ ডকার**।  
যে কোনটি সহজ মনে হয় তা নির্বাচন করুন— দুটোই একই পাঠে নিয়ে যায়।

## ১. পূর্বপ্রয়োজনীয়তা

| টুল               | সংস্করণ / নোটস                                                                       |
|--------------------|--------------------------------------------------------------------------------------|
| **পাইথন**         | ৩.১০+ (পেতে <https://python.org> থেকে ডাউনলোড করুন)                               |
| **গিট**            | সর্বশেষ (Xcode / Git for Windows / Linux প্যাকেজ ম্যানেজারের সাথে আসে)             |
| **VS কোড**         | ঐচ্ছিক কিন্তু সুপারিশকৃত <https://code.visualstudio.com>                          |
| **ডকার ডেস্কটপ**   | *শুধুমাত্র* অপশন বি জন্য। ফ্রি ইন্সটল: <https://docs.docker.com/desktop/>          |

> 💡 **টিপ** – টার্মিনালে টুলগুলি যাচাই করুন:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## ২. অপশন এ – নেটিভ পাইথন (সর্বকনিষ্ঠ)

### ধাপ ১ এই রিপো ক্লোন করুন

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### ধাপ ২ ভার্চুয়াল এনভায়রনমেন্ট তৈরি ও সক্রিয় করুন

```bash
python -m venv .venv          # একটি তৈরি করুন
source .venv/bin/activate     # ম্যাকওএস / লিনাক্স
.\.venv\Scripts\activate      # উইন্ডোজ পাওয়ারশেল
```

✅ প্রম্পট এখন (.venv) দিয়ে শুরু হওয়া উচিত—এর মানে আপনি পরিবেশের ভিতরে আছেন।

### ধাপ ৩ নির্ভরতাগুলো ইন্সটল করুন

```bash
pip install -r requirements.txt
```

[API কী](#৩-আপনার-api-কী-যুক্ত-করুন) এর বিভাগ ৩ তে সরাসরি চলে যান

## ২. অপশন বি – VS কোড ডেভ কন্টেইনার (ডকার)

আমরা এই রিপোজিটরি এবং কোর্সটি একটি [ডেভেলপমেন্ট কন্টেইনার](https://containers.dev?WT.mc_id=academic-105485-koreyst) সহ সেটআপ করেছি, যা ইউনিভার্সাল রানটাইম সরবরাহ করে যেটি Python3, .NET, Node.js এবং Java ডেভেলপমেন্ট সাপোর্ট করে। সংশ্লিষ্ট কনফিগারেশন `devcontainer.json` ফাইলে সংজ্ঞায়িত, যা এই রিপোজিটরির মূল `.devcontainer/` ফোল্ডারে অবস্থিত।

>**কেন এটা বেছে নিবেন?**
>Codespaces এর সাথে একই পরিবেশ; কোন ডিপেনডেন্সি ড্রিফট নেই।

### ধাপ ০ অতিরিক্ত সফটওয়্যার ইন্সটল করুন

Docker Desktop – নিশ্চিত করুন ```docker --version``` কাজ করে।
VS কোড রিমোট – কন্টেইনার্স এক্সটেনশন (ID: ms-vscode-remote.remote-containers)।

### ধাপ ১ VS কোডে রিপো ওপেন করুন

File ▸ Open Folder…  → generative-ai-for-beginners

VS কোড `.devcontainer/` সনাক্ত করে এবং একটি প্রম্পট দেখায়।

### ধাপ ২ কন্টেইনারে পুনরায় খুলুন

“Reopen in Container” ক্লিক করুন। ডকার ইমেজ বিল্ড করে (প্রথমবার ≈ ৩ মিনিট)।
টার্মিনাল প্রম্পট আসলে আপনি কন্টেইনারের ভিতরে।

## ২. অপশন সি – মিনিকন্ডা

[মিনিকন্ডা](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) হল একটি লাইটওয়েট ইনস্টলার যা [কন্ডা](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), পাইথন এবং কয়েকটি প্যাকেজ ইন্সটল করার জন্য।
কন্ডা নিজেই একটি প্যাকেজ ম্যানেজার, যা বিভিন্ন পাইথন [**ভার্চুয়াল এনভায়রনমেন্ট**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) এবং প্যাকেজ সেটআপ ও সুইচ করা সহজ করে তোলে। এর মাধ্যমে `pip`-এ না থাকা প্যাকেজও ইন্সটল করা যায়।

### ধাপ ০ মিনিকন্ডা ইন্সটল করুন

সেটআপ করতে [MiniConda ইন্সটল গাইড](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) অনুসরণ করুন।

```bash
conda --version
```

### ধাপ ১ ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন

একটি নতুন এনভায়রনমেন্ট ফাইল তৈরি করুন (*environment.yml*)। আপনি যদি Codespaces ব্যবহার করে থাকেন, তাহলে `.devcontainer` ডিরেক্টরির মধ্যে এটি তৈরি করুন, অর্থাৎ `.devcontainer/environment.yml`।

### ধাপ ২ আপনার এনভায়রনমেন্ট ফাইল পূরণ করুন

আপনার `environment.yml` ফাইলে নিম্নলিখিত অংশটি যুক্ত করুন

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

### ধাপ ৩ কন্ডা এনভায়রনমেন্ট তৈরি করুন

আপনার কমান্ড লাইন/টার্মিনালে নিচের কমান্ডগুলি চালান

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer সাব পাথ শুধুমাত্র Codespace সেটআপে প্রযোজ্য।
conda activate ai4beg
```

সমস্যা হলে [কন্ডা এনভায়রনমেন্ট গাইড](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) দেখুন।

## ২. অপশন ডি – ক্লাসিক জুপিটার / জুপিটার ল্যাব (আপনার ব্রাউজারে)

> **কার জন্য?**  
> যে কেউ যিনি ক্লাসিক জুপিটার ইন্টারফেস পছন্দ করেন অথবা VS কোড ছাড়া নোটবুক চালাতে চান।  

### ধাপ ১ নিশ্চিত করুন জুপিটার ইন্সটল আছে

স্থানীয়ভাবে জুপিটার চালু করতে, টার্মিনাল/কমান্ড লাইনে যান, কোর্সের ডিরেক্টরিতে নেভিগেট করুন, এবং চালান:

```bash
jupyter notebook
```

অথবা

```bash
jupyterhub
```

এটি একটি জুপিটার ইনস্ট্যান্স শুরু করবে এবং তার URL কমান্ড লাইনে দেখাবে।

URL-এ প্রবেশ করলে, আপনি কোর্সের আউটলাইন দেখতে পাবেন এবং যেকোনো `*.ipynb` ফাইলে যেতে পারবেন। উদাহরণস্বরূপ, `08-building-search-applications/python/oai-solution.ipynb`।

## ৩. আপনার API কী যুক্ত করুন

যেকোনো ধরনের অ্যাপ তৈরি করতে API কী নিরাপদে রাখা জরুরি। আমরা সুপারিশ করি কোডে সরাসরি কোনো API কী সংরক্ষণ করবেন না। পাবলিক রিপোজিটরিতে এটি কমিট করলে নিরাপত্তা ঝুঁকি এবং অনাকাঙ্ক্ষিত খরচের সম্ভাবনা থাকে যদি খারাপ কেউ এটি ব্যবহার করে।
এখানে ধাপে ধাপে গাইড দেয়া হলো কীভাবে Python-এর জন্য `.env` ফাইল তৈরি করবেন এবং আপনার Microsoft Foundry Models ক্রেডেনশিয়ালস যুক্ত করবেন:

> **বিঃদ্রঃ:** GitHub Models (এবং এর `GITHUB_TOKEN` ভেরিয়েবল) জুলাই ২০২৬-এর শেষে অবসর নিচ্ছে। এই গাইডে [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ব্যবহার করা হয়েছে। পুরোপুরি অফলাইন কাজ করতে চান? দেখুন [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)।

১. **আপনার প্রকল্প ডিরেক্টরিতে নেভিগেট করুন**: টার্মিনাল বা কমান্ড প্রম্পট খুলে আপনার প্রকল্পের মূল ডিরেক্টরিতে যান যেখানে `.env` ফাইল তৈরি করতে চান।

   ```bash
   cd path/to/your/project
   ```

২. **`.env` ফাইল তৈরি করুন**: পছন্দসই টেক্সট এডিটর দিয়ে `.env` নামে একটি নতুন ফাইল তৈরি করুন। আপনি যদি কমান্ড লাইন ব্যবহার করেন, তাহলে `touch` (ইউনিক্স-ভিত্তিক সিস্টেমে) অথবা `echo` (উইন্ডোজে) ব্যবহার করতে পারেন:

   ইউনিক্স-ভিত্তিক সিস্টেম:

   ```bash
   touch .env
   ```

   উইন্ডোজ:

   ```cmd
   echo . > .env
   ```

৩. **`.env` ফাইল সম্পাদনা করুন**: `.env` ফাইলটি একটি টেক্সট এডিটরে খুলুন (যেমন VS কোড, Notepad++ অথবা অন্য যেকোন এডিটর)। নিচের লাইনগুলো যুক্ত করুন, প্লেসহোল্ডারগুলো আপনার প্রকৃত Microsoft Foundry প্রজেক্ট এন্ডপয়েন্ট এবং API কী দিয়ে প্রতিস্থাপন করে:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

৪. **ফাইলটি সংরক্ষণ করুন**: পরিবর্তনগুলি সেভ করুন এবং টেক্সট এডিটর বন্ধ করুন।

৫. **`python-dotenv` ইন্সটল করুন**: যদি আগে না করে থাকেন, তাহলে `.env` ফাইল থেকে পরিবেশ ভেরিয়েবলগুলো আপনার পাইথন অ্যাপ্লিকেশনে লোড করার জন্য `python-dotenv` প্যাকেজ ইন্সটল করতে হবে। আপনি এটি `pip` দিয়ে ইন্সটল করতে পারেন:

   ```bash
   pip install python-dotenv
   ```

৬. **পাইথন স্ক্রিপ্টে পরিবেশ ভেরিয়েবল লোড করুন**: আপনার পাইথন স্ক্রিপ্টে, `python-dotenv` প্যাকেজ ব্যবহার করে `.env` ফাইল থেকে পরিবেশ ভেরিয়েবলগুলো লোড করুন:

   ```python
   from dotenv import load_dotenv
   import os

   # .env ফাইল থেকে এনভায়রনমেন্ট ভেরিয়েবল লোড করুন
   load_dotenv()

   # Microsoft Foundry Models ভেরিয়েবল অ্যাকসেস করুন
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

এতেই শেষ! আপনি সফলভাবে `.env` ফাইল তৈরি করেছেন, Microsoft Foundry Models এর ক্রেডেনশিয়ালস যুক্ত করেছেন এবং সেগুলোকে আপনার পাইথন অ্যাপ্লিকেশনে লোড করেছেন।

🔐 কখনো .env ফাইল কমিট করবেন না—এটি ইতিমধ্যে .gitignore-এ আছে।
পুরো প্রোভাইডার নির্দেশনাগুলো [`providers.md`](03-providers.md) এ আছে।

## ৪. এখন কি?

| আমি চাই…          | যান…                                                                   |
|---------------------|-------------------------------------------------------------------------|
| লেসন ১ শুরু করুন    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| একটি LLM প্রোভাইডার সেটআপ করুন | [`providers.md`](03-providers.md)                                       |
| অন্য শিক্ষার্থীদের সাথে পরিচিত হন | [আমাদের Discord এ যোগ দিন](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## ৫. সমস্যা সমাধান

| লক্ষণ                                   | সমাধান                                                             |
|----------------------------------------|--------------------------------------------------------------------|
| `python not found`                    | ইনস্টলের পর পাইথন PATH-এ যোগ করুন অথবা টার্মিনাল পুনরায় খুলুন      |
| `pip` চাকা (wheels) তৈরি করতে পারে না (উইন্ডোজ)  | `pip install --upgrade pip setuptools wheel` চালান তারপর পুনরায় চেষ্টা করুন।  |
| `ModuleNotFoundError: dotenv`         | `pip install -r requirements.txt` চালান (এনভায়রনমেন্ট তৈরি হয়নি)।          |
| Docker build ব্যর্থ *No space left*    | Docker Desktop ▸ *Settings* ▸ *Resources* → ডিস্ক সাইজ বাড়ান।               |
| VS কোড বার বার পুনরায় খোলার প্রম্পট দেয় | হতে পারে উভয় অপশন একযোগে চালু আছে; একটি নির্বাচন করুন (venv **অথবা** container)  |
| OpenAI 401 / 429 ত্রুটি                  | `OPENAI_API_KEY` মান পরীক্ষা করুন / রিকোয়েস্ট রেট লিমিট দেখুন।               |
| কন্ডা ব্যবহারে সমস্যা                     | Microsoft AI লাইব্রেরি ইন্সটল করুন `conda install -c microsoft azure-ai-ml` কমান্ড দিয়ে |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->