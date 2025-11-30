<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-18T01:55:45+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "my"
}
-->
# ဒီသင်ခန်းစာကို စတင်ပါ

Generative AI ကို အသုံးပြုပြီး ဘာတွေ ဖန်တီးနိုင်မလဲဆိုတာကို ကြည့်ရှုနိုင်ဖို့ သင်ခန်းစာကို စတင်ဖို့အတွက် ကျွန်တော်တို့ အရမ်းလှုပ်လှုပ်ရှားရှားရှိနေပါတယ်!

သင့်အောင်မြင်မှုကို အာမခံဖို့အတွက် ဒီစာမျက်နှာမှာ စတင်ရန် လိုအပ်ချက်များ၊ နည်းပညာလိုအပ်ချက်များနှင့် အကူအညီလိုအပ်ပါက ဘယ်မှာရနိုင်မလဲဆိုတာကို ဖော်ပြထားပါတယ်။

## စတင်ရန်အဆင့်များ

ဒီသင်ခန်းစာကို စတင်လေ့လာဖို့အတွက် အောက်ပါအဆင့်များကို ပြီးမြောက်စေရန် လိုအပ်ပါသည်။

### ၁။ ဒီ Repo ကို Fork လုပ်ပါ

ဒီ [Repo အားလုံးကို Fork လုပ်ပါ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) သင့်ရဲ့ GitHub အကောင့်မှာထားပြီး Code တွေကို ပြောင်းလဲနိုင်ရန်နှင့် စိန်ခေါ်မှုများကို ပြီးမြောက်နိုင်ရန်။ သင် [ဒီ Repo ကို Star (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) လုပ်ပြီး အလွယ်တကူ ရှာဖွေနိုင်ပါသည်။

### ၂။ Codespace တစ်ခု ဖန်တီးပါ

Code ကို run လုပ်တဲ့အခါ Dependency ပြဿနာများ မဖြစ်စေရန် [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) မှာ ဒီသင်ခန်းစာကို run လုပ်ဖို့ အကြံပြုပါသည်။

သင့် Fork မှာ: **Code -> Codespaces -> New on main**

![Codespace ဖန်တီးရန် Button များကို ပြသသော Dialog](../../../00-course-setup/images/who-will-pay.webp)

#### ၂.၁ Secret တစ်ခု ထည့်ပါ

1. ⚙️ Gear icon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Name OPENAI_API_KEY, သင့် key ကို paste လုပ်ပါ၊ Save.

### ၃။ နောက်တစ်ခုက ဘာလဲ?

| ကျွန်တော်/မ ကျေးဇူးပြု၍... | သွားရန်...                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Lesson 1 ကို စတင်ရန် | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Offline မှာ အလုပ်လုပ်ရန် | [`setup-local.md`](02-setup-local.md)                                   |
| LLM Provider ကို Setup လုပ်ရန် | [`providers.md`](03-providers.md)                                        |
| အခြားသော သင်ယူသူများနှင့် တွေ့ဆုံရန် | [ကျွန်တော်တို့ရဲ့ Discord ကို Join လုပ်ပါ](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## ပြဿနာများကို ဖြေရှင်းခြင်း

| ပြဿနာ                                   | ဖြေရှင်းနည်း                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| Container build stuck > 10 min            | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal မတပ်ဆင်ထားပါ; **+** ➜ *bash* ကို click လုပ်ပါ                    |
| `401 Unauthorized` from OpenAI            | မှားနေသော / သက်တမ်းကုန်သွားသော `OPENAI_API_KEY`                                |
| VS Code မှာ “Dev container mounting…”   | Browser tab ကို Refresh လုပ်ပါ—Codespaces sometimes loses connection   |
| Notebook kernel မရှိပါ                   | Notebook menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

၃။ **`.env` ဖိုင်ကို ပြင်ဆင်ပါ**: `.env` ဖိုင်ကို text editor (ဥပမာ - VS Code, Notepad++ သို့မဟုတ် အခြား editor) မှာ ဖွင့်ပါ။ အောက်ပါလိုင်းကို ဖိုင်ထဲမှာ ထည့်ပါ၊ `your_github_token_here` ကို သင့် GitHub token နဲ့ အစားထိုးပါ:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

၄။ **ဖိုင်ကို Save လုပ်ပါ**: ပြင်ဆင်မှုများကို Save လုပ်ပြီး text editor ကို ပိတ်ပါ။

၅။ **`python-dotenv` ကို Install လုပ်ပါ**: သင် Install မလုပ်ရသေးပါက `.env` ဖိုင်မှ Environment Variables များကို သင့် Python application ထဲသို့ Load လုပ်ရန် `python-dotenv` package ကို Install လုပ်ရန် လိုအပ်ပါသည်။ `pip` ကို အသုံးပြု၍ Install လုပ်နိုင်ပါသည်:

   ```bash
   pip install python-dotenv
   ```

၆။ **သင့် Python Script မှာ Environment Variables များကို Load လုပ်ပါ**: သင့် Python script မှာ `python-dotenv` package ကို အသုံးပြု၍ `.env` ဖိုင်မှ Environment Variables များကို Load လုပ်ပါ:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

ဒါပေမယ့် အဆင်ပြေပါပြီ! သင် `.env` ဖိုင်ကို ဖန်တီးပြီး သင့် GitHub token ကို ထည့်ပြီး Python application ထဲသို့ Load လုပ်ပြီးဖြစ်ပါသည်။

## သင့်ကွန်ပျူတာမှာ Local မှာ Run လုပ်နည်း

Code ကို သင့်ကွန်ပျူတာမှာ Local မှာ Run လုပ်ဖို့အတွက် [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ရဲ့ version တစ်ခုခုကို Install လုပ်ထားဖို့ လိုအပ်ပါသည်။

Repo ကို အသုံးပြုရန်အတွက် Clone လုပ်ရန် လိုအပ်ပါသည်:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

အရာအားလုံးကို Check Out ပြီးပါက စတင်နိုင်ပါပြီ!

## ရွေးချယ်နိုင်သော အဆင့်များ

### Miniconda ကို Install လုပ်ခြင်း

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) သည် [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python နှင့် အချို့သော packages များကို Install လုပ်ရန်အတွက် အလွယ်တကူ Installer တစ်ခုဖြစ်သည်။
Conda သည် package manager တစ်ခုဖြစ်ပြီး Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) နှင့် packages များကို setup လုပ်ရန်နှင့် switch လုပ်ရန် အလွယ်တကူဖြစ်စေသည်။ `pip` မှတဆင့် Install လုပ်လို့မရသော packages များကို Install လုပ်ရန်လည်း အထောက်အကူပြုသည်။

[MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ကို လိုက်နာပြီး setup လုပ်ပါ။

Miniconda ကို Install လုပ်ပြီးပါက [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ကို Clone လုပ်ရန် လိုအပ်ပါသည် (သင် မလုပ်ရသေးပါက)

နောက်တစ်ခုမှာ Virtual Environment တစ်ခု ဖန်တီးရန် လိုအပ်ပါသည်။ Conda ကို အသုံးပြု၍ Environment File (_environment.yml_) အသစ်တစ်ခု ဖန်တီးပါ။ Codespaces ကို အသုံးပြုနေပါက `.devcontainer` directory ထဲမှာ ဖန်တီးပါ၊ ဒါဆို `.devcontainer/environment.yml` ဖြစ်ပါသည်။

Environment File ကို အောက်ပါ snippet ဖြင့် Populate လုပ်ပါ:

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

Conda ကို အသုံးပြုရာမှာ Error တွေ ရှိနေပါက Terminal မှာ အောက်ပါ Command ကို အသုံးပြု၍ Microsoft AI Libraries ကို Manual Install လုပ်နိုင်ပါသည်။

```
conda install -c microsoft azure-ai-ml
```

Environment File မှာ လိုအပ်သော Dependencies များကို ဖော်ပြထားသည်။ `<environment-name>` သည် သင့် Conda Environment အတွက် သင် အသုံးပြုလိုသော အမည်ဖြစ်ပြီး `<python-version>` သည် သင် အသုံးပြုလိုသော Python ရဲ့ Version ဖြစ်သည်။ ဥပမာအားဖြင့် `3` သည် Python ရဲ့ နောက်ဆုံး Major Version ဖြစ်သည်။

ဒါပြီးပါက Command line/terminal မှာ အောက်ပါ Command များကို Run လုပ်ပြီး Conda Environment ကို ဖန်တီးနိုင်ပါသည်။

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

ပြဿနာများ ရှိပါက [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ကို ရှာဖွေကြည့်ပါ။

### Python support extension ပါရှိသော Visual Studio Code ကို အသုံးပြုခြင်း

ဒီသင်ခန်းစာအတွက် [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor ကို [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ဖြင့် အသုံးပြုရန် ကျွန်တော်တို့ အကြံပြုပါသည်။ ဒါဟာ အကြံပြုချက်သာဖြစ်ပြီး မဖြစ်မဖြစ်လိုအပ်သော အချက်မဟုတ်ပါ။

> **မှတ်ချက်**: သင် VS Code မှာ သင်ခန်းစာ repository ကို ဖွင့်တဲ့အခါ Project ကို Container ထဲမှာ setup လုပ်နိုင်တဲ့ အခွင့်အရေး ရှိပါတယ်။ ဒါဟာ သင်ခန်းစာ repository ထဲမှာ [အထူး `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) directory ရှိတဲ့အတွက် ဖြစ်ပါတယ်။ ဒီအကြောင်းကို နောက်ပိုင်းမှာ ဆက်လက်ရှင်းပြပါမည်။

> **မှတ်ချက်**: သင် VS Code မှာ Directory ကို Clone လုပ်ပြီး ဖွင့်တဲ့အခါ Python support extension ကို Install လုပ်ရန် အလိုအလျောက် အကြံပြုပါလိမ့်မည်။

> **မှတ်ချက်**: VS Code က သင့်ကို Repository ကို Container ထဲမှာ ပြန်ဖွင့်ရန် အကြံပြုပါက, locally installed version of Python ကို အသုံးပြုရန်အတွက် ဒီတောင်းဆိုမှုကို ပယ်ဖျက်ပါ။

### Browser မှာ Jupyter ကို အသုံးပြုခြင်း

သင် [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ကို Browser မှာတင် အသုံးပြုပြီး Project ကို အလုပ်လုပ်နိုင်ပါသည်။ Classic Jupyter နှင့် [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) နှစ်ခုစလုံးမှာ Auto-completion, Code highlighting စတဲ့ အဆင်ပြေတဲ့ Development Environment ကို ပေးစွမ်းနိုင်ပါတယ်။

Jupyter ကို Local မှာ စတင်ရန် Terminal/Command Line ကို သွားပြီး သင်ခန်းစာ Directory ကို ရောက်အောင် သွားပြီး အောက်ပါ Command ကို Run လုပ်ပါ:

```bash
jupyter notebook
```

သို့မဟုတ်

```bash
jupyterhub
```

ဒါဟာ Jupyter instance ကို စတင်ပြီး URL ကို Command Line Window မှာ ပြပါလိမ့်မည်။

URL ကို Access လုပ်ပြီးပါက သင် သင်ခန်းစာ အကြောင်းအရာကို မြင်ရပြီး `*.ipynb` ဖိုင်များကို Navigate လုပ်နိုင်ပါသည်။ ဥပမာအားဖြင့် `08-building-search-applications/python/oai-solution.ipynb`။

### Container မှာ Run လုပ်ခြင်း

သင့်ကွန်ပျူတာမှာ သို့မဟုတ် Codespace မှာ အရာအားလုံးကို setup လုပ်ခြင်းအစား [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) ကို အသုံးပြုနိုင်ပါသည်။ သင်ခန်းစာ repository ထဲမှာရှိတဲ့ အထူး `.devcontainer` folder က VS Code ကို Container ထဲမှာ Project ကို setup လုပ်နိုင်စေပါတယ်။ Codespaces အပြင်မှာတော့ Docker ကို Install လုပ်ရန် လိုအပ်ပြီး အလုပ်များတတ်သောကြောင့် Containers တွေကို အတွေ့အကြုံရှိသူများသာ အသုံးပြုရန် အကြံပြုပါသည်။

GitHub Codespaces ကို အသုံးပြုတဲ့အခါ API keys တွေကို လုံခြုံစွာထားရှိရန် အကောင်းဆုံးနည်းလမ်းတစ်ခုက Codespace Secrets ကို အသုံးပြုခြင်းဖြစ်ပါတယ်။ [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide ကို လိုက်နာပါ။

## သင်ခန်းစာများနှင့် နည်းပညာလိုအပ်ချက်များ

ဒီသင်ခန်းစာမှာ အကြောင်းအရာ သင်ခန်းစာ ၆ ခုနှင့် Coding သင်ခန်းစာ ၆ ခု ပါဝင်ပါတယ်။

Coding သင်ခန်းစာများအတွက် Azure OpenAI Service ကို အသုံးပြုထားပါတယ်။ ဒီ Code ကို Run လုပ်ရန် Azure OpenAI Service နှင့် API key ရရှိရန် လိုအပ်ပါသည်။ [ဒီအတန်းလျှောက်လွှာ](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) ကို ဖြည့်စွက်ပြီး Access ရယူနိုင်ပါသည်။

သင့်လျှောက်လွှာကို စစ်ဆေးနေစဉ်အတွင်း Coding သင်ခန်းစာတစ်ခုစီမှာ `README.md` ဖိုင်ပါဝင်ပြီး Code နှင့် Outputs ကို ကြည့်ရှုနိုင်ပါသည်။

## Azure OpenAI Service ကို ပထမဆုံးအသုံးပြုခြင်း

သင် Azure OpenAI Service ကို ပထမဆုံးအသုံးပြုနေပါက [Azure OpenAI Service resource ကို ဖန်တီးပြီး Deploy လုပ်နည်း](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) guide ကို လိုက်နာပါ။

## OpenAI API ကို ပထမဆုံးအသုံးပြုခြင်း

OpenAI API ကို ပထမဆုံးအသုံးပြုနေပါက [Interface ကို ဖန်တီးပြီး အသုံးပြုနည်း](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) guide ကို လိုက်နာပါ။

## အခြားသော သင်ယူသူများနှင့် တွေ့ဆုံခြင်း

ကျွန်တော်တို့ရဲ့ [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) မှာ အခြားသော သင်ယူသူများနှင့် တွေ့ဆုံရန် Channel များကို ဖန်တီးထားပါတယ်။ Generative AI မှာ အဆင့်မြှင့်တင်လိုသော စီးပွားရေးလုပ်ငန်းရှင်များ၊ ဖန်တီးသူများ၊ ကျောင်းသားများနှင့် အခြားသော စိတ်ဝင်စားသူများနှင့် အဆက်အသွယ် ရှိရန် အကောင်းဆုံးနည်းလမ်းဖြစ်ပါတယ်။

[![discord channel ကို Join လုပ်ပါ](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Project Team လည်း ဒီ Discord server မှာ ရှိပြီး သင်ယူသူများကို ကူညီပေးပါမည်။

## အထောက်အကူပြုပါ

ဒီသင်ခန်းစာသည် open-source အစီအစဉ်တစ်ခုဖြစ်သည်။ တိုးတက်မှုများ သို့မဟုတ် ပြဿနာများကို တွေ့ရှိပါက [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) တစ်ခု ဖန်တီးပါ သို့မဟုတ် [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) တစ်ခု Log လုပ်ပါ။

Project Team သည် အားလုံးသော အထောက်အကူပြုမှုများကို စောင့်ကြည့်နေပါမည်။ Open Source ကို အထောက်အကူပြုခြင်းသည် Generative AI မှာ သင့်ရဲ့ အလုပ်အကိုင်ကို တိုးတက်စေမည့် နည်းလမ်းတစ်ခုဖြစ်သည်။

အများဆုံး အထောက်အကူပြုမှုများသည် Contributor License Agreement (CLA) ကို သဘောတူရန် လိုအပ်ပြီး သင့်အနေဖြင့် သင့်ရဲ့ အထောက်အကူပြုမှုကို အသုံးပြုခွင့်ရှိသည်နှင့် အမှန်တကယ်ပေးအပ်သည်ကို ကြေငြာရန် လိုအပ်ပါသည်။ အသေးစိတ်အချက်အလက်များအတွက် [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) ကို သွားရောက်ကြည့်ရှုပါ။

Pull Request တစ်ခုကို တင်သွင်းသောအခါ CLA-bot သည် သင် CLA ကို ပေးအပ်ရန် လိုအပ်သည်ကို အလိုအလျောက် ဆုံးဖြတ်ပြီး PR ကို သင့်တော်သော Label, Comment ဖြင့် အလှဆင်
အခု သင်တန်းကို ပြီးမြောက်စွာ အဆင့်ဆင့်ပြီးစီးလိုက်ပြီဆိုတော့ [Generative AI နှင့် LLMs အကြောင်းအကျဉ်းချုပ်](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) ကို စတင်လေ့လာကြမယ်။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။