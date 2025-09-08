<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T15:32:39+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "bn"
}
-->
# লোকাল সেটআপ 🖥️

**যদি আপনি সবকিছু নিজের ল্যাপটপে চালাতে চান, তাহলে এই গাইডটি ব্যবহার করুন।**  
আপনার জন্য দুটি পথ আছে: **(A) নেটিভ পাইথন + ভার্চুয়াল-এনভি** অথবা **(B) VS Code ডেভ কন্টেইনার উইথ Docker**।  
যেটা সহজ মনে হয় সেটাই বেছে নিন—দুটোতেই একই লেসনে পৌঁছাতে পারবেন।

## ১. প্রয়োজনীয়তা

| টুল                | ভার্সন / নোটস                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | ৩.১০ + (ডাউনলোড করুন <https://python.org> থেকে)                                     |
| **Git**            | সর্বশেষ (Xcode / Git for Windows / Linux package manager-এ আসে)                     |
| **VS Code**        | অপশনাল, তবে সুপারিশকৃত <https://code.visualstudio.com>                              |
| **Docker Desktop** | *শুধুমাত্র* অপশন B-র জন্য। ফ্রি ইন্সটল: <https://docs.docker.com/desktop/>           |

> 💡 **টিপ** – টার্মিনালে টুলগুলো যাচাই করুন:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## ২. অপশন A – নেটিভ পাইথন (সবচেয়ে দ্রুত)

### ধাপ ১  এই রিপো ক্লোন করুন

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### ধাপ ২ ভার্চুয়াল এনভায়রনমেন্ট তৈরি ও অ্যাক্টিভেট করুন

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ এখন প্রম্পটের শুরুতে (.venv) দেখা যাবে—মানে আপনি এনভায়রনমেন্টের ভিতরে আছেন।

### ধাপ ৩ ডিপেন্ডেন্সি ইন্সটল করুন

```bash
pip install -r requirements.txt
```

[API কী](../../../00-course-setup) সেকশনে চলে যান

## ২. অপশন B – VS Code ডেভ কন্টেইনার (Docker)

আমরা এই রিপোজিটরি ও কোর্সটি [ডেভেলপমেন্ট কন্টেইনার](https://containers.dev?WT.mc_id=academic-105485-koreyst) দিয়ে সেটআপ করেছি, যাতে ইউনিভার্সাল রানটাইম আছে যা Python3, .NET, Node.js এবং Java ডেভেলপমেন্ট সাপোর্ট করে। সংশ্লিষ্ট কনফিগারেশন `devcontainer.json` ফাইলে সংজ্ঞায়িত, যা এই রিপোজিটরির রুটে `.devcontainer/` ফোল্ডারে আছে।

>**কেন এটা বেছে নেবেন?**
>Codespaces-এর সাথে একদম একই পরিবেশ; ডিপেন্ডেন্সি ড্রিফট নেই।

### ধাপ ০ এক্সট্রা টুল ইন্সটল করুন

Docker Desktop – নিশ্চিত করুন ```docker --version``` কাজ করে।
VS Code Remote – Containers এক্সটেনশন (ID: ms-vscode-remote.remote-containers) ইন্সটল করুন।

### ধাপ ১ রিপোটি VS Code-এ ওপেন করুন

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code `.devcontainer/` ডিটেক্ট করবে এবং একটি প্রম্পট দেখাবে।

### ধাপ ২ কন্টেইনারে পুনরায় ওপেন করুন

“Reopen in Container” ক্লিক করুন। Docker ইমেজ বিল্ড করবে (প্রথমবার ≈ ৩ মিনিট)।
টার্মিনাল প্রম্পট আসলে বুঝবেন আপনি কন্টেইনারের ভিতরে আছেন।

## ২. অপশন C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) হলো [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python এবং কিছু প্যাকেজ ইন্সটলের জন্য হালকা ওজনের ইন্সটলার।
Conda নিজেই একটি প্যাকেজ ম্যানেজার, যা বিভিন্ন Python [**ভার্চুয়াল এনভায়রনমেন্ট**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ও প্যাকেজ সেটআপ ও সুইচ করা সহজ করে। এছাড়াও, `pip`-এ না থাকা প্যাকেজ ইন্সটল করতেও কাজে লাগে।

### ধাপ ০  Miniconda ইন্সটল করুন

[MiniConda ইন্সটলেশন গাইড](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) অনুসরণ করে সেটআপ করুন।

```bash
conda --version
```

### ধাপ ১ ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন

নতুন এনভায়রনমেন্ট ফাইল (*environment.yml*) তৈরি করুন। যদি Codespaces ব্যবহার করেন, তাহলে `.devcontainer` ডিরেক্টরির মধ্যে তৈরি করুন, অর্থাৎ `.devcontainer/environment.yml`।

### ধাপ ২  এনভায়রনমেন্ট ফাইলটি পূরণ করুন

আপনার `environment.yml`-এ নিচের স্নিপেটটি যোগ করুন

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

### ধাপ ৩ আপনার Conda এনভায়রনমেন্ট তৈরি করুন

নিচের কমান্ডগুলো কমান্ড লাইন/টার্মিনালে চালান

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

কোনো সমস্যা হলে [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) দেখুন।

## ২  অপশন D – ক্লাসিক Jupyter / Jupyter Lab (ব্রাউজারে)

> **কার জন্য?**  
> যারা ক্লাসিক Jupyter ইন্টারফেস পছন্দ করেন বা VS Code ছাড়াই নোটবুক চালাতে চান।  

### ধাপ ১  নিশ্চিত করুন Jupyter ইন্সটল আছে

লোকালি Jupyter চালাতে টার্মিনাল/কমান্ড লাইনে যান, কোর্স ডিরেক্টরিতে যান, এবং চালান:

```bash
jupyter notebook
```

অথবা

```bash
jupyterhub
```

এতে Jupyter চালু হবে এবং অ্যাক্সেসের URL কমান্ড লাইনে দেখাবে।

URL-এ গেলে কোর্সের আউটলাইন দেখতে পাবেন এবং যেকোনো `*.ipynb` ফাইলে যেতে পারবেন। যেমন, `08-building-search-applications/python/oai-solution.ipynb`।

## ৩. আপনার API কী যোগ করুন

যেকোনো অ্যাপ্লিকেশন বানানোর সময় API কী নিরাপদ রাখা খুবই গুরুত্বপূর্ণ। আমরা পরামর্শ দিই, কখনোই কোডে সরাসরি API কী রাখবেন না। এগুলো পাবলিক রিপোজিটরিতে কমিট করলে নিরাপত্তা ঝুঁকি ও অপ্রত্যাশিত খরচ হতে পারে, যদি কেউ অপব্যবহার করে।
এখানে Python-এর জন্য `.env` ফাইল তৈরি ও `GITHUB_TOKEN` যোগ করার ধাপে ধাপে গাইড:

১. **প্রজেক্ট ডিরেক্টরিতে যান**: টার্মিনাল বা কমান্ড প্রম্পট খুলে, যেখানে `.env` ফাইল তৈরি করতে চান, সেই ডিরেক্টরিতে যান।

   ```bash
   cd path/to/your/project
   ```

২. **`.env` ফাইল তৈরি করুন**: আপনার পছন্দের টেক্সট এডিটর দিয়ে `.env` নামে নতুন ফাইল তৈরি করুন। কমান্ড লাইনে করতে চাইলে, `touch` (Unix-এ) বা `echo` (Windows-এ) ব্যবহার করুন:

   Unix-ভিত্তিক সিস্টেম:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

৩. **`.env` ফাইল এডিট করুন**: `.env` ফাইলটি টেক্সট এডিটরে (যেমন VS Code, Notepad++ বা অন্য যেকোনো এডিটর) খুলুন। নিচের লাইনটি যোগ করুন, `your_github_token_here`-এর জায়গায় আপনার আসল GitHub টোকেন দিন:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

৪. **ফাইলটি সেভ করুন**: পরিবর্তনগুলো সেভ করে এডিটর বন্ধ করুন।

৫. **`python-dotenv` ইন্সটল করুন**: যদি আগে না করে থাকেন, তাহলে `.env` ফাইল থেকে এনভায়রনমেন্ট ভেরিয়েবল লোড করতে `python-dotenv` প্যাকেজ ইন্সটল করতে হবে। `pip` দিয়ে ইন্সটল করুন:

   ```bash
   pip install python-dotenv
   ```

৬. **Python স্ক্রিপ্টে এনভায়রনমেন্ট ভেরিয়েবল লোড করুন**: আপনার Python স্ক্রিপ্টে `python-dotenv` ব্যবহার করে `.env` ফাইল থেকে এনভায়রনমেন্ট ভেরিয়েবল লোড করুন:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

ব্যাস! আপনি সফলভাবে `.env` ফাইল তৈরি করেছেন, GitHub টোকেন যোগ করেছেন, এবং Python অ্যাপে লোড করেছেন।

🔐 কখনোই .env কমিট করবেন না—এটা আগেই .gitignore-এ আছে।
সম্পূর্ণ প্রোভাইডার নির্দেশনা [`providers.md`](03-providers.md)-এ আছে।

## ৪. এরপর কী করবেন?

| আমি চাই…            | যান…                                                                       |
|---------------------|----------------------------------------------------------------------------|
| লেসন ১ শুরু করতে    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)         |
| LLM প্রোভাইডার সেটআপ | [`providers.md`](03-providers.md)                                           |
| অন্য শিক্ষার্থীদের সাথে পরিচিত হতে | [আমাদের Discord-এ যোগ দিন](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## ৫. সমস্যা সমাধান

| উপসর্গ                                    | সমাধান                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Python-কে PATH-এ যোগ করুন বা ইন্সটলের পর টার্মিনাল রিস্টার্ট করুন |
| `pip` cannot build wheels (Windows)       | `pip install --upgrade pip setuptools wheel` তারপর আবার চেষ্টা করুন |
| `ModuleNotFoundError: dotenv`             | `pip install -r requirements.txt` চালান (env ইন্সটল হয়নি)।      |
| Docker build fails *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → ডিস্ক সাইজ বাড়ান।   |
| VS Code বারবার রিওপেন করতে বলছে           | হয়তো দুই অপশনই অ্যাক্টিভ; যেকোনো একটিতে থাকুন (venv **অথবা** container)|
| OpenAI 401 / 429 errors                   | `OPENAI_API_KEY` ভ্যালু / রিকোয়েস্ট রেট লিমিট চেক করুন।         |
| Conda ব্যবহার করতে সমস্যা                 | `conda install -c microsoft azure-ai-ml` দিয়ে Microsoft AI লাইব্রেরি ইন্সটল করুন|

---

**দায়িত্ব পরিত্যাগের ঘোষণা**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য নির্ভুলতা বজায় রাখার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিই চূড়ান্ত ও কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হবে। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হচ্ছে। এই অনুবাদের ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।