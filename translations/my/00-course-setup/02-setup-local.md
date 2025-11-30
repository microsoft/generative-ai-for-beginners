<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T19:54:30+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "my"
}
-->
# Local Setup 🖥️

**ဒီလမ်းညွှန်ကို သင့်ရဲ့ laptop ပေါ်မှာ တစ်ခုချင်းစီ run လုပ်ချင်သူများအတွက် အသုံးပြုပါ။**  
သင့်မှာ လမ်းကြောင်းနှစ်ခု ရွေးနိုင်ပါတယ် - **(A) native Python + virtual-env** သို့မဟုတ် **(B) VS Code Dev Container နဲ့ Docker**  
အလွယ်ဆုံးထင်တဲ့နည်းကို ရွေးပါ—နှစ်ခုလုံးက တူညီတဲ့ သင်ခန်းစာတွေကိုရောက်ပါတယ်။

## 1.  လိုအပ်ချက်များ

| Tool               | Version / Notes                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (<https://python.org> မှရယူနိုင်သည်)                                         |
| **Git**            | နောက်ဆုံးထွက် (Xcode / Git for Windows / Linux package manager တွင်ပါဝင်သည်)         |
| **VS Code**        | Optional ဖြစ်ပေမယ့် အကြံပြုသည် <https://code.visualstudio.com>                      |
| **Docker Desktop** | *Option B အတွက်သာ*။ အခမဲ့ install: <https://docs.docker.com/desktop/>              |

> 💡 **Tip** – Terminal မှာ tool တွေစစ်ကြည့်ပါ:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Option A – Native Python (အလွယ်ဆုံး)

### Step 1  ဒီ repo ကို clone လုပ်ပါ

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Step 2 Virtual environment တစ်ခုဖန်တီးပြီး activate လုပ်ပါ

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompt မှာ (.venv) နဲ့စတင်လာရင် သင့်အနေနဲ့ env ထဲဝင်ပြီးသားဖြစ်ပါတယ်။

### Step 3 လိုအပ်တဲ့ dependency တွေ install လုပ်ပါ

```bash
pip install -r requirements.txt
```

[API keys](../../../00-course-setup) အပိုင်း 3 ကို ဆက်လက်လုပ်ဆောင်ပါ

## 2. Option B – VS Code Dev Container (Docker)

ဒီ repository နဲ့ သင်တန်းကို [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) နဲ့ပြင်ဆင်ထားပါတယ်။ Universal runtime ပါဝင်ပြီး Python3, .NET, Node.js နဲ့ Java development တွေကို support လုပ်နိုင်ပါတယ်။ သက်ဆိုင်ရာ configuration ကို `devcontainer.json` ဖိုင်မှာ `.devcontainer/` folder ထဲမှာထားပါတယ်။

>**ဘာကြောင့် ဒီနည်းကို ရွေးသင့်လဲ?**
>Codespaces နဲ့ တူညီတဲ့ environment ဖြစ်ပြီး dependency drift မရှိပါ။

### Step 0 လိုအပ်တဲ့ extras တွေ install လုပ်ပါ

Docker Desktop – ```docker --version``` အလုပ်လုပ်တာစစ်ပါ။
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers) ကို install လုပ်ပါ။

### Step 1 Repo ကို VS Code ထဲမှာဖွင့်ပါ

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code က .devcontainer/ ကိုသိပြီး prompt တစ်ခုပေါ်လာပါလိမ့်မယ်။

### Step 2 Container ထဲမှာ ပြန်ဖွင့်ပါ

“Reopen in Container” ကိုနှိပ်ပါ။ Docker က image ကို build လုပ်ပါလိမ့်မယ် (ပထမဆုံးအကြိမ် ≈ 3 မိနစ်ခန့်ယူနိုင်ပါတယ်)။
Terminal prompt ပေါ်လာရင် သင် container ထဲမှာရှိပြီးသားဖြစ်ပါတယ်။

## 2.  Option C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) က [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python နဲ့ အနည်းငယ် package တွေကို install လုပ်ဖို့အတွက် lightweight installer တစ်ခုပါ။
Conda ကို package manager အနေနဲ့ အသုံးပြုနိုင်ပြီး Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) နဲ့ package တွေကို အလွယ်တကူ setup လုပ်နိုင်ပါတယ်။ pip နဲ့မရနိုင်တဲ့ package တွေကို install လုပ်ဖို့လည်း အသုံးဝင်ပါတယ်။

### Step 0  Miniconda ကို install လုပ်ပါ

[MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ကိုလိုက်နာပြီး install လုပ်ပါ။

```bash
conda --version
```

### Step 1 Virtual environment တစ်ခုဖန်တီးပါ

environment file (*environment.yml*) အသစ်တစ်ခုဖန်တီးပါ။ Codespaces ကိုအသုံးပြုနေပါက `.devcontainer` directory ထဲမှာ `.devcontainer/environment.yml` အနေနဲ့ ဖန်တီးပါ။

### Step 2  Environment file ကို အချက်အလက်ဖြည့်ပါ

`environment.yml` ထဲကို အောက်ပါ code ကိုထည့်ပါ

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

### Step 3 Conda environment ကိုဖန်တီးပါ

Command line/terminal မှာ အောက်ပါ command တွေကို run လုပ်ပါ

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

ပြဿနာတက်ရင် [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ကိုကြည့်ပါ။

## 2  Option D – Classic Jupyter / Jupyter Lab (Browser မှာ)

> **ဘယ်သူတွေအတွက်လဲ?**  
> Jupyter interface အဟောင်းကိုနှစ်သက်သူများ သို့မဟုတ် VS Code မလိုဘဲ notebook တွေ run လုပ်ချင်သူများအတွက်။  

### Step 1  Jupyter install လုပ်ထားတာစစ်ပါ

Jupyter ကို local မှာစတင်ဖို့ terminal/command line ကိုသွားပြီး သင်တန်း directory ကိုသွားပါ၊ ပြီးတော့ အောက်ပါ command ကို run လုပ်ပါ:

```bash
jupyter notebook
```

သို့မဟုတ်

```bash
jupyterhub
```

Jupyter instance တစ်ခုစတင်ပြီး URL ကို command line window မှာပြပါလိမ့်မယ်။

URL ကိုသွားရောက်လျှင် သင်တန်းအကြောင်းအရာတွေကိုမြင်ရပြီး `*.ipynb` ဖိုင်တစ်ခုချင်းစီကိုသွားနိုင်ပါလိမ့်မယ်။ ဥပမာ `08-building-search-applications/python/oai-solution.ipynb` တို့။

## 3. သင့်ရဲ့ API Keys တွေထည့်ပါ

Application တစ်ခုခုတည်ဆောက်တဲ့အခါ API keys တွေကို လုံခြုံစွာထားရှိဖို့အရေးကြီးပါတယ်။ API keys တွေကို code ထဲမှာတိုက်ရိုက်သိမ်းမထားဖို့ အကြံပြုပါတယ်။ Public repository မှာ commit လုပ်မိရင် လုံခြုံရေးပြဿနာတွေ၊ မလိုလားအပ်တဲ့ကုန်ကျစရိတ်တွေဖြစ်နိုင်ပါတယ်။
Python အတွက် `.env` ဖိုင်တစ်ခုဖန်တီးပြီး `GITHUB_TOKEN` ထည့်သွင်းနည်းကို အဆင့်လိုက်ရှင်းပြထားပါတယ် -

1. **Project Directory ကိုသွားပါ**: Terminal သို့မဟုတ် command prompt ကိုဖွင့်ပြီး သင့် project ရဲ့ root directory ကိုသွားပါ။ `.env` ဖိုင်ဖန်တီးမယ့်နေရာပါ။

   ```bash
   cd path/to/your/project
   ```

2. **`.env` ဖိုင်ဖန်တီးပါ**: သင်နှစ်သက်တဲ့ text editor ကိုသုံးပြီး `.env` ဆိုတဲ့ဖိုင်အသစ်တစ်ခုဖန်တီးပါ။ Command line ကိုသုံးမယ်ဆိုရင် Unix-based systems မှာ `touch` သုံးနိုင်ပါတယ်၊ Windows မှာ `echo` သုံးနိုင်ပါတယ် -

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` ဖိုင်ကို edit လုပ်ပါ**: `.env` ဖိုင်ကို text editor (ဥပမာ VS Code, Notepad++ သို့မဟုတ် အခြား editor) နဲ့ဖွင့်ပါ။ အောက်ပါလိုင်းကိုထည့်ပါ၊ `your_github_token_here` ကို သင့်ရဲ့ GitHub token နဲ့အစားထိုးပါ -

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **ဖိုင်ကိုသိမ်းပါ**: ပြင်ဆင်ပြီးရင် သိမ်းပြီး editor ကိုပိတ်ပါ။

5. **`python-dotenv` ကို install လုပ်ပါ**: မလုပ်ရသေးရင် `python-dotenv` package ကို install လုပ်ပါ။ `.env` ဖိုင်ထဲက environment variable တွေကို Python application ထဲသို့ load လုပ်နိုင်ဖို့ပါ။ `pip` နဲ့ install လုပ်နိုင်ပါတယ် -

   ```bash
   pip install python-dotenv
   ```

6. **Python script ထဲမှာ Environment Variables တွေ load လုပ်ပါ**: Python script ထဲမှာ `python-dotenv` package ကိုသုံးပြီး `.env` ဖိုင်ထဲက environment variable တွေကို load လုပ်ပါ -

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

ပြီးပါပြီ! `.env` ဖိုင်ဖန်တီးပြီး GitHub token ထည့်သွင်းပြီး Python application ထဲသို့ load လုပ်နိုင်ပါပြီ။

🔐 .env ကိုဘယ်တော့မှ commit မလုပ်ပါ—it’s already in .gitignore.
Provider အသေးစိတ်လမ်းညွှန်တွေကို [`providers.md`](03-providers.md) မှာကြည့်နိုင်ပါတယ်။

## 4. နောက်ထပ် ဘာလုပ်မလဲ?

| လုပ်ချင်တာ            | သွားရမယ့်နေရာ                                                      |
|---------------------|-------------------------------------------------------------------------|
| Lesson 1 စတင်ချင်တယ်      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| LLM Provider တစ်ခု setup လုပ်ချင်တယ် | [`providers.md`](03-providers.md)                                       |
| တခြားလေ့လာသူတွေနဲ့တွေ့ချင်တယ် | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. ပြဿနာဖြေရှင်းနည်း

| ပြဿနာအမျိုးအစား                         | ဖြေရှင်းနည်း                                                    |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Python ကို PATH ထဲထည့်ပါ သို့မဟုတ် install ပြီးရင် terminal ကိုပြန်ဖွင့်ပါ |
| `pip` cannot build wheels (Windows)       | `pip install --upgrade pip setuptools wheel` ပြီး retry လုပ်ပါ။        |
| `ModuleNotFoundError: dotenv`             | `pip install -r requirements.txt` ကို run လုပ်ပါ (env မ install ရသေးပါ)   |
| Docker build fails *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → disk size ကိုတိုးပါ။         |
| VS Code keeps prompting to reopen         | Option နှစ်ခုလုံး active ဖြစ်နေလို့ ဖြစ်နိုင်ပါတယ်; တစ်ခုကိုသာရွေးပါ (venv **သို့မဟုတ်** container)|
| OpenAI 401 / 429 errors                   | `OPENAI_API_KEY` value / request rate limits ကိုစစ်ပါ။             |
| Errors using Conda                        | Microsft AI libraries ကို `conda install -c microsoft azure-ai-ml` နဲ့ install လုပ်ပါ|

---

**သတိပေးချက်**:
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူလစာရွက်စာတမ်းသည် မူလဘာသာစကားဖြင့် အာဏာရှိသော ရင်းမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာနိုင်သော နားလည်မှုမှားခြင်း သို့မဟုတ် အနားလည်မှားခြင်းများအတွက် ကျွန်ုပ်တို့သည် တာဝန်ယူမည်မဟုတ်ပါ။