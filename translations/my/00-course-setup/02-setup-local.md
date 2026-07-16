# ဒေသတွင်းစက်တင် 🖥️

**မိမိတို့ရဲ့ လက်ပ်တော့ပေါ်မှာ အားလုံးကို တိုက်ရိုက်လည်ပတ်လိုသူများအတွက် ဤလမ်းညွှန်ကို အသုံးပြုပါ။**   
လမ်းကြောင်း နှစ်ခုရှိပါတယ်။ **(A) မူရင်း Python + virtual-env** သို့မဟုတ် **(B) Docker ဖြင့် VS Code Dev Container** ။  
လွယ်ကူတယ်လို့ ခံစားရတဲ့ဟန်နဲ့ရွေးချယ်ပါ—နှစ်ခုစလုံးမှာ သင်ခန်းစာများ တူညီပဲဖြစ်ပါတယ်။

## 1.  လိုအပ်သော အကြိုပြင်ဆင်မှုများ

| ကိရိယာ             | ဗားရှင်း / မှတ်ချက်များ                                                                |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (<https://python.org> မှ ရယူနိုင်သည်)                                           |
| **Git**            | နောက်ဆုံးဗားရှင်း (Xcode၊ Git for Windows၊ Linux package manager နှင့် လာပါသည်)         |
| **VS Code**        | ရွေးချယ်စရာဖြစ်သော်လည်း အကြံပြုသည် <https://code.visualstudio.com>                     |
| **Docker Desktop** | *ရွေးချယ်မှု B အတွက်သာ။* အခမဲ့ 설치: <https://docs.docker.com/desktop/>                |

> 💡 **အကြံပြုချက်** – ကိရိယာများကို terminal မှာစစ်ဆေးပါ:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  ရွေးချယ်မှု A – မူရင်း Python (အမြန်ဆုံး)

### အဆင့် ၁  ဤ repo ကိုကလုံလုပ်ပါ

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### အဆင့် ၂ virtual environment တစ်ခု ဖန်တီးပြီး မှန်ကန်စွာ ဖွင့်ပါ

```bash
python -m venv .venv          # တစ်ခုဖန်တီးပါ
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ သင့် prompt သည် (.venv) ဖြင့် စတင်ပါက env အတွင်းမှာရှိနေသည်ကို ဆိုလိုသည်။

### အဆင့် ၃ လိုအပ်သော dependencies များ ထည့်သွင်းပါ

```bash
pip install -r requirements.txt
```

[API keys](#3-သင့်-api-keys-များ-ထည့်သွင်းခြင်း) အပိုင်း ၃ သို့ တိုက်ရိုက်သွားပါ

## 2. ရွေးချယ်မှု B – VS Code Dev Container (Docker)

ဤ repository နှင့် သင်တန်းကို [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) ဖြင့် ပြင်ဆင်ထားပြီး Universal runtime ပါရှိသည်၊ Python3, .NET, Node.js နှင့် Java ဖွံ့ဖြိုးမှုများကို ထောက်ပံ့နိုင်သည်။ ဆက်စပ်သော configuration ကို ဒီ repository ၏ root တွင်ရှိသော `.devcontainer/` ဖိုလ်ဒါအတွင်းရှိ `devcontainer.json` ဖိုင်တွင် သတ်မှတ်ထားသည်။

>**ဘာကြောင့် ဤကို ရွေးချယ်သလဲ?**
>Codespaces နှင့် တူညီသော ပတ်ဝန်းကျင်ဖြစ်၍ dependency ပြောင်းလဲမှု မရှိပဲဖြစ်သည်။

### အဆင့် ၀  အုတ်ဆောက်ပစ္စည်းများကို 설치ပါ

Docker Desktop – ```docker --version``` အလုပ်လုပ်ကြောင်း အတည်ပြုပါ။
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### အဆင့် ၁  repo ကို VS Code မှာ ဖွင့်ပါ

ဖိုင် ▸ ဖိုလ်ဒါဖွင့်… → generative-ai-for-beginners

VS Code က .devcontainer/ ကိုတွေ့ပြီး prompt ပေါ်ပေါက်စေပါသည်။

### အဆင့် ၂ container ထဲ ပြန်ဖွင့်ပါ

“Reopen in Container” ကိုနှိပ်ပါ။ Docker သည် ပုံတူကို တည်ဆောက်ပေးမည် (ပထမအကြိမ် ≈ ၃ မိနစ်)။
terminal prompt ပေါ်လာသည်နှင့် သင် container အတွင်းရှိပြီဖြစ်သည်။

## 2.  ရွေးချယ်မှု C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) သည် [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python နှင့် အချို့သော package များ ထည့်သွင်းရန် အလှည့်ကျ သာမန်ထည့်သွင်းသည့် ပရိုဂရမ်ဖြစ်သည်။
Conda ကိုယ်တိုင်သည် package manager ဖြစ်ပြီး Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) များနှင့် package များကို အလွယ်တကူ စီမံလုပ်ဆောင်နိုင်စေနိုင်သည်။ `pip` ဖြင့် မရရှိနိုင်သော package များကို ထည့်သွင်းရာတွင်လည်း အထောက်အကူဖြစ်သည်။

### အဆင့် ၀  Miniconda ကို 설치ပါ

[MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) အတိုင်း လိုက်နာရန်။

```bash
conda --version
```

### အဆင့် ၁  virtual environment တစ်ခု ဖန်တီးပါ

အသစ်သော environment ဖိုင် (*environment.yml*) ဖန်တီးပါ။ Codespaces ကိုလိုက်နာနေသူများအတွက် `.devcontainer` ဖိုလ်ဒါအတွင်း ဖန်တီးပါ၊ ဒါမှမဟုတ် `.devcontainer/environment.yml` ဖြစ်မည်။

### အဆင့် ၂  သင့် environment ဖိုင်ကို ဖြည့်စွက်ပါ

 `environment.yml` ထဲ သို့ အောက်ပါ အပိုဒ်ကိုထည့်ပါ

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

### အဆင့် ၃  Conda environment ကို ဖန်တီးပါ

အောက်ပါ command များကို command line/terminal တွင် chạy ပါ

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer နောက်ခံလမ်းကြောင်းသည် Codespace စနစ်တွင်သာအသုံးပြုသည်
conda activate ai4beg
```

ပြဿနာရှိပါက [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ကိုသွားကြည့်ပါ။

## 2  ရွေးချယ်မှု D – Classic Jupyter / Jupyter Lab (သင့် browser တွင်)

> **ဘယ်သူတွေအတွက်လဲ?**  
> classic Jupyter interface ကို သဘောကျသူ သို့မဟုတ် VS Code မပါဘဲ notebooks များ run လုပ်ချင်သူများအတွက်ဖြစ်သည်။

### အဆင့် ၁  Jupyter ထည့်သွင်းထားကြောင်း သေချာပါစေနိုင်ရန်

Jupyter ကို ဒေသတွင်း စတင်ရန် terminal/command line သို့သွားပြီး သင်တန်း ဖိုင်ကွက်သို့ သွားကာ အောက်ပါ command ကို ရိုက်ထည့်ပါ။

```bash
jupyter notebook
```

သို့မဟုတ်

```bash
jupyterhub
```

ဤသည်က Jupyter instance တစ်ခုကို စတင်မည်ဖြစ်ပြီး ဂျာနယ် URL ကို command line ကျယ်ပြန့်ထဲမှာ ပြသပါလိမ့်မည်။

URL ကို ဝင်ရောက်လိုက်ပါက သင်တန်း အကြောင်းအရာကို မြင်ရပြီး `*.ipynb` ဖိုင် မည်သည့်ထဲကိုမဆို လှည့်လည်ကြည့်ရှုနိုင်ပါသည်။ ဥပမာ၊ `08-building-search-applications/python/oai-solution.ipynb`

## 3. သင့် API Keys များ ထည့်သွင်းခြင်း

API key များကို လုံခြုံစွာ ထိန်းသိမ်းခြင်းမှာ မည်သည့် application မဆို တည်ဆောက်ရာတွင် အရေးကြီးသည်။ API key များကို ကိုယ်ရေးcode ထဲတွင်တိုက်ရိုက် မမှတ်တမ်းမတင်ရန် အကြံပြုပီး၊ အများပြည်သူ repo တွင် commit လုပ်ခြင်းသည် လုံခြုံရေးပြဿနာများနှင့် မလိုလားသော ကုန်ကျစရိတ်များ ဖြစ်နိုင်သည်။
သင့်၏ Microsoft Foundry Models အကြောင်း အဆိုပါ `.env` ဖိုင်တစ်ခု ဖန်တီးပြီး ထည့်သွင်းနည်း လမ်းညွှန်။

> **မှတ်ချက်:** GitHub Models (နှင့် ၎င်း၏ `GITHUB_TOKEN` variable) သည် ၂၀၂၆ ခုနှစ် ဇူလိုင်ကုန်တွင် သက်တမ်းကုန်ပါပြီ။ ဤလမ်းညွှန်တွင် [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) သာအသုံးပြုသည်။ အပြည့်အဝ အော့ဖ်လိုင်းလုပ်လိုပါသလား? [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ကိုကြည့်ပါ။

1. **သင့် ပရောဂျက် ဖိုင်တွဲသို့ သွားပါ**: terminal သို့ command prompt ကိုဖွင့်ပြီး `.env` ဖိုင် ဖန်တီးလိုသည့် သင့်ပရောဂျက် ရှေ့ပြေး directory သို့ သွားပါ။

   ```bash
   cd path/to/your/project
   ```

2. **`.env` ဖိုင်ကို ဖန်တီးပါ**: မိမိကြိုက်နှစ်သက်သည့် စာအယ်ဒီတာဖြင့် `.env` နာမည်ရှိသော ဖိုင်အသစ်တစ်ခု ဖန်တီးပါ။ command line ကိုသုံးပါက Unix-based စနစ်များတွင် `touch` သို့မဟုတ် Windows တွင် `echo` ကို အသုံးပြုနိုင်သည်။

   Unix-based စနစ်များ:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` ဖိုင်ကို တည်းဖြတ်ပါ**: `.env` ဖိုင်ကို text editor (ဥပမာ - VS Code, Notepad++ သို့မဟုတ် တခြား editor) ဖြင့် ဖွင့်ပြီး Microsoft Foundry project endpoint နှင့် API key တန်ဖိုးအစား ထည့်ပါ။

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **ဖိုင်ကို သိမ်းပါ**: ပြင်ဆင်မှုများကို သိမ်းပြီး text editor ကို ပိတ်လိုက်ပါ။

5. **`python-dotenv` ကို 설치ပါ**: မပြုလုပ်ထားသေးလျှင် `.env` ဖိုင်မှ environment variables များကို Python application ထဲသို့ ကိုင်တွယ်ဖို့ `python-dotenv` package ကို install လုပ်ရန် လိုအပ်သည်။ `pip` ဖြင့် install ရပါမည်။

   ```bash
   pip install python-dotenv
   ```

6. **Python script တွင် environment variables များကို ဖတ်ပါ**: Python script ထဲတွင် `python-dotenv` package ကို အသုံးပြု၍ `.env` ဖိုင်မှ environment variables များကို ဖတ်ပါ။

   ```python
   from dotenv import load_dotenv
   import os

   # .env ဖိုင်မှ ပတ်ဝန်းကျင်အပြောင်းအလဲများကို ပြန်ပြီးဖတ်ယူပါ
   load_dotenv()

   # Microsoft Foundry Models အပြောင်းအလဲများကို လက်လှမ်းမီအောင် ပြုလုပ်ပါ
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

သင်ပြုလုပ်ပြီးပါပြီ! `.env` ဖိုင်ကို အောင်မြင်စွာ ဖန်တီးပြီး Microsoft Foundry Models အချက်အလက်များ ထည့်သွင်းထားပြီး Python application သို့ စတင်သွင်းယူနိုင်ပါပြီ။

🔐 `.env` ကို မည်သည့်အချိန်မျှ commit မလုပ်ပါနှင့်—it’s already in .gitignore.
ပေးသွင်းသူ၏ လမ်းညွှန်ချက်များကို [`providers.md`](03-providers.md) တွင် ကြည့်ရှုနိုင်ပါသည်။

## 4. နောက်တစ်ဆင့် များ?

| ကျွန်တော်/ကျွန်မ ယနေ့…      | သွားရန်…                                                               |
|---------------------|-------------------------------------------------------------------------|
| သင်ခန်းစာ ၁ စတင်ရန်      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)       |
| LLM Provider တစ်ခု စတင်ရန် | [`providers.md`](03-providers.md)                                       |
| အခြား သင်ယူသူများနှင့် တွေ့ရန် | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. ပြဿနာဖြေရှင်းခြင်း

| လက္ခဏာ                                  | ဖြေရှင်းနည်း                                                       |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Python ကို PATH ထည့်ပါ သို့ terminal ကို install ပြီးနောက် ပြန်ဖွင့်ပါ            |
| `pip` cannot build wheels (Windows)       | `pip install --upgrade pip setuptools wheel` ပြီးနောက် ထပ်မံကြိုးစားပါ        |
| `ModuleNotFoundError: dotenv`             | `pip install -r requirements.txt` လုပ်ပါ (env ထည့်သွင်းထားခြင်းမရှိသေး)   |
| Docker build fails *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → disk size တိုးမြှင့်ပါ          |
| VS Code keeps prompting to reopen         | နှစ်ခုစလုံး အသုံးပြုနေသည့် အခြေအနေ ဖြစ်နိုင်သည်; တစ်ခုရွေးပါ (venv **သို့မဟုတ်** container)|
| OpenAI 401 / 429 errors                   | `OPENAI_API_KEY` တန်ဖိုးကိုစစ်ပါ / များ၍တောင်းဆိုမှု၊ rate limits ကိုစစ်ပါ      |
| Conda သုံးစွဲမှု ပြဿနာများ                 | Microsoft AI စာကြည့်တိုက်များကို `conda install -c microsoft azure-ai-ml` ဖြင့် 설치ပါ |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->