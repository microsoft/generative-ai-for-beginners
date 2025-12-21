<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5cf0b10ab3c485e6334101f5784f1f3",
  "translation_date": "2025-12-19T17:40:46+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "my"
}
-->
# ဒေသတွင်း စတင်ပြင်ဆင်ခြင်း 🖥️

**သင့်ရဲ့ ကိုယ်ပိုင် လက်ပ်တော့ပေါ်မှာ အားလုံးကို ပြေးဆွဲချင်ရင် ဒီလမ်းညွှန်ကို အသုံးပြုပါ။**  
သင်မှာ နှစ်ခုသော လမ်းကြောင်းရှိပါတယ် - **(A) native Python + virtual-env** သို့မဟုတ် **(B) VS Code Dev Container with Docker**။  
လွယ်ကူသလို ခံစားရတဲ့ ဘယ်ဟာမဆို ရွေးချယ်ပါ—နှစ်ခုလုံးက တူညီတဲ့ သင်ခန်းစာတွေကို ဦးတည်ပါတယ်။

## 1.  မလိုအပ်မီ အချက်အလက်များ

| ကိရိယာ               | ဗားရှင်း / မှတ်ချက်များ                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (<https://python.org> မှ ရယူပါ)                                            |
| **Git**            | နောက်ဆုံးဗားရှင်း (Xcode / Git for Windows / Linux package manager တွေနဲ့ ပါလာတယ်)                   |
| **VS Code**        | ရွေးချယ်စရာဖြစ်ပေမယ့် အကြံပြုပါတယ် <https://code.visualstudio.com>                             |
| **Docker Desktop** | *Option B အတွက်သာ* အခမဲ့ ထည့်သွင်းနိုင်ပါတယ်: <https://docs.docker.com/desktop/>                |

> 💡 **အကြံပြုချက်** – Terminal မှာ ကိရိယာတွေကို စစ်ဆေးပါ:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Option A – Native Python (အမြန်ဆုံး)

### အဆင့် 1  ဒီ repo ကို clone လုပ်ပါ

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### အဆင့် 2  virtual environment တစ်ခု ဖန်တီးပြီး ဖွင့်ပါ

```bash
python -m venv .venv          # တစ်ခုလုပ်ပါ
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompt မှာ (.venv) ဆိုပြီး စတင်လာရင် သင်ဟာ env အတွင်းမှာ ရှိနေပြီဖြစ်ပါတယ်။

### အဆင့် 3  လိုအပ်သော dependencies များ ထည့်သွင်းပါ

```bash
pip install -r requirements.txt
```

[API keys](../../../00-course-setup) အပိုင်း 3 ကို ဆက်ဖတ်ပါ

## 2. Option B – VS Code Dev Container (Docker)

ဒီ repository နဲ့ သင်တန်းကို [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) နဲ့ ပြင်ဆင်ထားပြီး Python3, .NET, Node.js နဲ့ Java ဖွံ့ဖြိုးရေးကို ထောက်ပံ့နိုင်တဲ့ Universal runtime ပါဝင်ပါတယ်။ ဆက်စပ် configuration ကို ဒီ repository ရဲ့ အမြစ်မှာရှိတဲ့ `.devcontainer/` ဖိုလ်ဒါအတွင်းရှိ `devcontainer.json` ဖိုင်မှာ သတ်မှတ်ထားပါတယ်။

>**ဘာကြောင့် ဒီဟာကို ရွေးချယ်သင့်တာလဲ?**  
>Codespaces နဲ့ တူညီတဲ့ ပတ်ဝန်းကျင်ဖြစ်ပြီး dependency drift မဖြစ်စေပါ။

### အဆင့် 0  အပိုဆောင်းတွေ ထည့်သွင်းပါ

Docker Desktop – ```docker --version``` က အလုပ်လုပ်တာကို အတည်ပြုပါ။  
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers) ကို ထည့်သွင်းပါ။

### အဆင့် 1  VS Code မှာ repo ကို ဖွင့်ပါ

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code က .devcontainer/ ကို တွေ့ပြီး prompt တစ်ခု ပြပါလိမ့်မယ်။

### အဆင့် 2  container ထဲ ပြန်ဖွင့်ပါ

“Reopen in Container” ကို နှိပ်ပါ။ Docker က image ကို တည်ဆောက်ပါလိမ့်မယ် (ပထမဆုံးအကြိမ်မှာ ≈ ၃ မိနစ်)။  
Terminal prompt ပေါ်လာတဲ့အခါ သင်ဟာ container အတွင်းမှာ ရှိနေပြီဖြစ်ပါတယ်။

## 2.  Option C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) သည် [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python နဲ့ အချို့သော package များကို ထည့်သွင်းဖို့ အလင်းလေး installer ဖြစ်ပါတယ်။  
Conda သည် package manager တစ်ခုဖြစ်ပြီး Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) နဲ့ package များကို လွယ်ကူစွာ စီမံခန့်ခွဲနိုင်စေပါတယ်။ `pip` နဲ့ မရနိုင်တဲ့ package များကို ထည့်သွင်းဖို့လည်း အသုံးဝင်ပါတယ်။

### အဆင့် 0  Miniconda ကို ထည့်သွင်းပါ

[MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ကို လိုက်နာပြီး ထည့်သွင်းပါ။

```bash
conda --version
```

### အဆင့် 1  virtual environment တစ်ခု ဖန်တီးပါ

environment ဖိုင်အသစ် (*environment.yml*) တစ်ခု ဖန်တီးပါ။ Codespaces ကို အသုံးပြုနေပါက `.devcontainer` ဖိုလ်ဒါအတွင်းမှာ ဖန်တီးပါ၊ ဒါမှမဟုတ် `.devcontainer/environment.yml` ဖြစ်ပါလိမ့်မယ်။

### အဆင့် 2  environment ဖိုင်ကို ဖြည့်စွက်ပါ

`environment.yml` ထဲကို အောက်ပါ snippet ကို ထည့်ပါ

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

### အဆင့် 3  Conda environment ကို ဖန်တီးပါ

အောက်ပါ command များကို command line/terminal မှာ ပြေးပါ

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer အောက်ပိုင်းလမ်းကြောင်းသည် Codespace စနစ်များတွင်သာ အသုံးပြုသည်။
conda activate ai4beg
```

ပြဿနာတက်ရင် [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ကို ရည်ညွှန်းပါ။

## 2  Option D – Classic Jupyter / Jupyter Lab (သင့် browser မှာ)

> **ဘယ်သူတွေအတွက်လဲ?**  
> Classic Jupyter interface ကို ကြိုက်နှစ်သက်သူများ သို့မဟုတ် VS Code မလိုအပ်ဘဲ notebook များကို ပြေးချင်သူများအတွက်ဖြစ်ပါတယ်။  

### အဆင့် 1  Jupyter ထည့်သွင်းထားကြောင်း သေချာစေပါ

Jupyter ကို ဒေသတွင်းမှာ စတင်ဖို့ terminal/command line ကို သွားပြီး သင်တန်း directory ကို ရောက်ရှိပါ၊ ပြီးတော့ အောက်ပါ command ကို အလုပ်လုပ်ပါ:

```bash
jupyter notebook
```

သို့မဟုတ်

```bash
jupyterhub
```

ဒါက Jupyter instance တစ်ခု စတင်ပြီး URL ကို command line ပြတင်းပေါ်မှာ ပြပါလိမ့်မယ်။

URL ကို ဝင်ရောက်ပြီးနောက် သင်တန်း အကြောင်းအရာကို မြင်ရမယ်၊ `*.ipynb` ဖိုင် များကို လွယ်ကူစွာ သွားရောက်နိုင်ပါလိမ့်မယ်။ ဥပမာ - `08-building-search-applications/python/oai-solution.ipynb`။

## 3. သင့် API Keys များ ထည့်သွင်းခြင်း

API keys များကို လုံခြုံစွာ ထိန်းသိမ်းထားခြင်းသည် မည်သည့် application မဆို တည်ဆောက်ရာတွင် အရေးကြီးပါသည်။ API keys များကို သင့် code ထဲမှာ တိုက်ရိုက် သိမ်းဆည်းခြင်း မပြုသင့်ပါ။ Public repository တစ်ခုမှာ commit လုပ်ခြင်းက လုံခြုံရေး ပြဿနာများ ဖြစ်ပေါ်စေနိုင်ပြီး မကောင်းသော အသုံးပြုသူများကြောင့် မလိုလားအပ်သော ကုန်ကျစရိတ်များ ဖြစ်ပေါ်နိုင်ပါသည်။  
Python အတွက် `.env` ဖိုင် ဖန်တီးပြီး `GITHUB_TOKEN` ထည့်သွင်းနည်း အဆင့်ဆင့် လမ်းညွှန်မှာ အောက်ပါအတိုင်း ဖြစ်ပါတယ် -

1. **သင့် Project Directory ကို သွားပါ**: Terminal သို့မဟုတ် command prompt ကို ဖွင့်ပြီး `.env` ဖိုင် ဖန်တီးလိုသော သင့် project ရဲ့ root directory ကို သွားပါ။

   ```bash
   cd path/to/your/project
   ```

2. **`.env` ဖိုင် ဖန်တီးပါ**: သင်နှစ်သက်ရာ text editor ဖြင့် `.env` ဆိုတဲ့ ဖိုင်အသစ် တစ်ခု ဖန်တီးပါ။ Command line ကို အသုံးပြုပါက Unix-based စနစ်များမှာ `touch` ကို၊ Windows မှာ `echo` ကို အသုံးပြုနိုင်ပါတယ် -

   Unix-based စနစ်များ:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` ဖိုင်ကို ပြင်ဆင်ပါ**: `.env` ဖိုင်ကို text editor (ဥပမာ - VS Code, Notepad++, သို့မဟုတ် အခြား editor) ဖြင့် ဖွင့်ပါ။ အောက်ပါလိုင်းကို ထည့်ပါ၊ `your_github_token_here` ကို သင့်ရဲ့ အမှန် GitHub token နဲ့ အစားထိုးပါ။

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **ဖိုင်ကို သိမ်းပါ**: ပြင်ဆင်မှုများကို သိမ်းပြီး editor ကို ပိတ်ပါ။

5. **`python-dotenv` ကို ထည့်သွင်းပါ**: `.env` ဖိုင်မှ environment variables များကို Python application ထဲသို့ load ဖို့ `python-dotenv` package ကို ထည့်သွင်းရန် လိုအပ်ပါသည်။ `pip` ဖြင့် ထည့်သွင်းနိုင်ပါသည် -

   ```bash
   pip install python-dotenv
   ```

6. **Python script မှာ Environment Variables များကို Load လုပ်ပါ**: Python script ထဲမှာ `python-dotenv` package ကို အသုံးပြုပြီး `.env` ဖိုင်မှ environment variables များကို load လုပ်ပါ -

   ```python
   from dotenv import load_dotenv
   import os

   # .env ဖိုင်မှ ပတ်ဝန်းကျင်အပြောင်းအလဲများကို ဖတ်ယူပါ
   load_dotenv()

   # GITHUB_TOKEN အပြောင်းအလဲကို အသုံးပြုပါ
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

ဒါဆို အဆင်ပြေပါပြီ! `.env` ဖိုင်ကို အောင်မြင်စွာ ဖန်တီးပြီး GitHub token ကို ထည့်သွင်းပြီး Python application ထဲသို့ load လုပ်နိုင်ပြီ ဖြစ်ပါတယ်။

🔐 `.env` ကို မည်သည့်အချိန်မှ commit မလုပ်ပါနဲ့—ဒါဟာ `.gitignore` ထဲမှာ ရှိပြီးသားပါ။  
Provider များအတွက် လမ်းညွှန်ချက်များကို [`providers.md`](03-providers.md) မှာ ကြည့်ရှုနိုင်ပါသည်။

## 4. နောက်တစ်ဆင့်မှာ ဘာလုပ်မလဲ?

| ကျွန်တော်/ကျွန်မ လုပ်ချင်တာ…          | သွားမယ့်နေရာ…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| သင်ခန်းစာ ၁ စတင်မယ်      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| LLM Provider တစ်ခု စတင်ချင်တယ် | [`providers.md`](03-providers.md)                                       |
| အခြား သင်ယူသူတွေနဲ့ တွေ့ဆုံချင်တယ် | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. ပြဿနာဖြေရှင်းခြင်း

| ရောဂါလက္ခဏာ                                   | ဖြေရှင်းနည်း                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Python ကို PATH ထဲ ထည့်ပါ သို့မဟုတ် ထည့်သွင်းပြီးနောက် terminal ကို ပြန်ဖွင့်ပါ            |
| `pip` cannot build wheels (Windows)       | `pip install --upgrade pip setuptools wheel` ပြီးနောက် ထပ်မံကြိုးစားပါ        |
| `ModuleNotFoundError: dotenv`             | `pip install -r requirements.txt` ကို ပြေးပါ (env မထည့်သွင်းထားပါ)   |
| Docker build fails *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → disk size ကို တိုးပါ |
| VS Code keeps prompting to reopen         | Options နှစ်ခုလုံး အလုပ်လုပ်နေတတ်ပါတယ်; တစ်ခုကိုသာ ရွေးချယ်ပါ (venv **သို့မဟုတ်** container)|
| OpenAI 401 / 429 errors                   | `OPENAI_API_KEY` တန်ဖိုး / request rate limits ကို စစ်ဆေးပါ             |
| Conda အသုံးပြုရာမှာ အမှားများ                        | Microsoft AI libraries ကို `conda install -c microsoft azure-ai-ml` ဖြင့် ထည့်သွင်းပါ|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် သတ်မှတ်စဉ်းစားသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->