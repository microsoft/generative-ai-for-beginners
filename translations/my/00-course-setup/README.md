<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T19:55:31+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "my"
}
-->
# ဒီသင်တန်းကို စတင်အသုံးပြုခြင်း

သင် ဒီသင်တန်းကို စတင်လေ့လာဖို့ စိတ်လှုပ်ရှားနေကြောင်း ကျွန်ုပ်တို့ ဝမ်းသာပါတယ်။ Generative AI နဲ့ ဘာတွေ တည်ဆောက်နိုင်မလဲဆိုတာလည်း စောင့်မျှော်နေပါတယ်။

သင်အောင်မြင်စွာ လေ့လာနိုင်ဖို့အတွက် ဒီစာမျက်နှာမှာ တပ်ဆင်မှုအဆင့်များ၊ နည်းပညာလိုအပ်ချက်များနဲ့ အကူအညီလိုအပ်လျှင် ဘယ်မှာ ရနိုင်မလဲဆိုတာ ဖော်ပြထားပါတယ်။

## တပ်ဆင်မှုအဆင့်များ

ဒီသင်တန်းကို စတင်လေ့လာဖို့ အောက်ပါအဆင့်များကို ပြီးမြောက်စေဖို့ လိုအပ်ပါတယ်။

### ၁။ ဒီ Repo ကို Fork လုပ်ပါ

[Fork လုပ်ပါ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ကိုယ်ပိုင် GitHub အကောင့်ထဲသို့ ပြောင်းယူပြီး code များ ပြင်ဆင်ခြင်း၊ စိန်ခေါ်မှုများ ပြီးမြောက်အောင်လုပ်နိုင်ပါမယ်။ [Star (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) လည်း ထားနိုင်ပါတယ်၊ ပြန်ရှာရလွယ်အောင်ပါ။

### ၂။ Codespace တစ်ခု ဖန်တီးပါ

Code ကို run လုပ်တဲ့အခါ dependency ပြဿနာမဖြစ်စေရန် [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) မှာ သင်တန်းကို run လုပ်ဖို့ အကြံပြုပါတယ်။

သင် fork လုပ်ထားတဲ့ repo မှာ - **Code -> Codespaces -> New on main** ကိုနှိပ်ပါ။

![Dialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

#### ၂.၁ Secret တစ်ခု ထည့်ပါ

၁။ ⚙️ Gear icon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
၂။ OPENAI_API_KEY လို့ နာမည်ပေးပြီး သင့် key ကို paste လုပ်ပါ၊ Save နှိပ်ပါ။

### ၃။ နောက်ထပ် ဘာလုပ်မလဲ?

| လုပ်ချင်တာ            | သွားရမယ့်နေရာ                                                      |
|---------------------|--------------------------------------------------------------------|
| Lesson 1 စတင်ချင်တယ် | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md) |
| Offline လုပ်ချင်တယ်  | [`setup-local.md`](02-setup-local.md)                              |
| LLM Provider တပ်ဆင်ချင်တယ် | [`providers.md`](providers.md)                                 |
| တခြားလေ့လာသူတွေ့ချင်တယ် | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## ပြဿနာဖြေရှင်းခြင်း

| လက္ခဏာ                                    | ဖြေရှင်းနည်း                                                    |
|-------------------------------------------|-----------------------------------------------------------------|
| Container build ၁၀ မိနစ်ကျော် တိတ်နေတယ်   | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal မချိတ်သွားဘူး; **+** ➜ *bash* ကိုနှိပ်ပါ                |
| OpenAI မှာ `401 Unauthorized`            | `OPENAI_API_KEY` မှား/သက်တမ်းကုန်သွားတယ်                       |
| VS Code မှာ “Dev container mounting…”    | Browser tab ကို refresh လုပ်ပါ—Codespaces sometimes connection ပြတ်တတ်တယ် |
| Notebook kernel မပေါ်ဘူး                  | Notebook menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

၃။ **`.env` ဖိုင်ကို ပြင်ပါ** - `.env` ဖိုင်ကို text editor (ဥပမာ VS Code, Notepad++ သို့မဟုတ် အခြား editor) ဖြင့်ဖွင့်ပါ။ အောက်ပါလိုင်းကို ထည့်ပါ၊ `your_github_token_here` ကို သင့် GitHub token နဲ့ အစားထိုးပါ -

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

၄။ **ဖိုင်ကို သိမ်းပါ** - ပြင်ဆင်ပြီးရင် သိမ်းပြီး editor ကိုပိတ်ပါ။

၅။ **`python-dotenv` ကို တပ်ဆင်ပါ** - မတပ်ရသေးရင် `python-dotenv` package ကို pip နဲ့ တပ်ဆင်ပါ -

   ```bash
   pip install python-dotenv
   ```

၆။ **Python Script ထဲမှာ Environment Variables ကို Load လုပ်ပါ** - Python script ထဲမှာ `python-dotenv` ကိုသုံးပြီး `.env` ဖိုင်ထဲက environment variables တွေကို load လုပ်ပါ -

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

ဒါဆိုပြီးပါပြီ။ သင် `.env` ဖိုင်တစ်ခု ဖန်တီးပြီး GitHub token ထည့်ပြီး Python application ထဲသို့ load လုပ်နိုင်ပါပြီ။

## ကိုယ်ပိုင်ကွန်ပျူတာမှာ Local Run လုပ်နည်း

Code ကို ကိုယ်ပိုင်ကွန်ပျူတာမှာ run လုပ်ချင်ရင် [Python တစ်ခုခု](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) တပ်ဆင်ထားဖို့ လိုအပ်ပါတယ်။

Repository ကို အသုံးပြုဖို့ clone လုပ်ပါ -

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

အားလုံး ပြီးသွားရင် စတင်လေ့လာနိုင်ပါပြီ။

## ရွေးချယ်နိုင်သော အဆင့်များ

### Miniconda တပ်ဆင်ခြင်း

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) က [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python နဲ့ အနည်းငယ်သော packages တွေကို တပ်ဆင်ဖို့ အလွယ်တကူ installer တစ်ခုပါ။
Conda ကို package manager အနေနဲ့ သုံးနိုင်ပြီး Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) နဲ့ packages တွေကို အလွယ်တကူ ပြောင်းလဲတပ်ဆင်နိုင်ပါတယ်။ pip နဲ့ မရနိုင်တဲ့ packages တွေကိုတောင် Conda နဲ့ တပ်ဆင်နိုင်ပါတယ်။

[MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ကိုလိုက်နာပြီး တပ်ဆင်နိုင်ပါတယ်။

Miniconda တပ်ဆင်ပြီးရင် [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ကို clone လုပ်ပါ (မလုပ်ရသေးရင်)။

နောက်တစ်ဆင့်မှာ virtual environment တစ်ခုဖန်တီးရပါမယ်။ Conda နဲ့လုပ်မယ်ဆိုရင် environment file (_environment.yml_) အသစ်တစ်ခုဖန်တီးပါ။ Codespaces သုံးနေတယ်ဆိုရင် `.devcontainer` directory ထဲမှာ `.devcontainer/environment.yml` လို့ဖန်တီးပါ။

အောက်ပါ code snippet ကို သင့် environment file ထဲထည့်ပါ -

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

Conda သုံးတဲ့အခါ error တက်တယ်ဆိုရင် Microsoft AI Libraries ကို terminal မှာ အောက်ပါ command နဲ့ ကိုယ်တိုင်တပ်ဆင်နိုင်ပါတယ်။

```
conda install -c microsoft azure-ai-ml
```

Environment file မှာ လိုအပ်တဲ့ dependencies တွေ ဖော်ပြထားပါတယ်။ `<environment-name>` ဆိုတာ သင် Conda environment အတွက် သတ်မှတ်ချင်တဲ့နာမည်၊ `<python-version>` ကတော့ သုံးချင်တဲ့ Python version ပါ။ ဥပမာ `3` ဆိုရင် Python ရဲ့ နောက်ဆုံး major version ဖြစ်ပါတယ်။

ပြီးသွားရင် အောက်ပါ command တွေကို command line/terminal မှာ run လုပ်ပြီး Conda environment ကို ဖန်တီးနိုင်ပါပြီ -

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

ပြဿနာတက်ရင် [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ကို ကိုးကားပါ။

### Visual Studio Code နဲ့ Python support extension သုံးခြင်း

ဒီသင်တန်းအတွက် [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor နဲ့ [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) တပ်ဆင်ထားဖို့ အကြံပြုပါတယ်။ ဒါပေမယ့် မဖြစ်မနေလိုအပ်တာတော့ မဟုတ်ပါဘူး။

> **Note**: VS Code ထဲမှာ သင်တန်း repository ကိုဖွင့်လိုက်တာနဲ့ project ကို container ထဲမှာတပ်ဆင်နိုင်တဲ့ option ရှိပါတယ်။ ဒါက သင်တန်း repository ထဲမှာ [အထူး `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) directory ပါဝင်လို့ပါ။ နောက်ပိုင်းမှာ ပိုမိုရှင်းပြပါမယ်။

> **Note**: Directory ကို clone လုပ်ပြီး VS Code ထဲမှာဖွင့်လိုက်တာနဲ့ Python support extension တပ်ဆင်ဖို့ အလိုအလျောက် အကြံပြုပါလိမ့်မယ်။

> **Note**: VS Code က repository ကို container ထဲမှာ ပြန်ဖွင့်ဖို့ အကြံပြုလာရင်၊ ကိုယ့်ကွန်ပျူတာမှာတပ်ဆင်ထားတဲ့ Python ကို သုံးချင်ရင် ငြင်းပယ်ပါ။

### Browser ထဲမှာ Jupyter သုံးခြင်း

[Browser ထဲမှာ Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ကိုသုံးပြီးလည်း ဒီ project ကို လုပ်နိုင်ပါတယ်။ Jupyter နဲ့ [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) နှစ်ခုလုံးမှာ auto-completion, code highlighting စတဲ့ အဆင်ပြေတဲ့ features တွေပါဝင်ပါတယ်။

Jupyter ကို local မှာစတင်ဖို့ terminal/command line ကိုသွားပြီး သင်တန်း directory ကိုသွားပါ၊ အောက်ပါ command ကို run လုပ်ပါ -

```bash
jupyter notebook
```

သို့မဟုတ်

```bash
jupyterhub
```

ဒါနဲ့ Jupyter instance တစ်ခုစတင်ပြီး URL ကို command line window ထဲမှာ ပြပါလိမ့်မယ်။

URL ကိုသွားရင် သင်တန်းအကြောင်းအရာတွေကို မြင်ရပြီး `*.ipynb` ဖိုင်တစ်ခုခုကို သွားနိုင်ပါပြီ။ ဥပမာ `08-building-search-applications/python/oai-solution.ipynb` လို့ပါ။

### Container ထဲမှာ Run လုပ်ခြင်း

ကိုယ့်ကွန်ပျူတာမှာ သို့မဟုတ် Codespace မှာ အားလုံးတပ်ဆင်စရာမလိုဘဲ [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) ကိုသုံးနိုင်ပါတယ်။ သင်တန်း repository ထဲက `.devcontainer` folder ကြောင့် VS Code က project ကို container ထဲမှာတပ်ဆင်နိုင်ပါတယ်။ Codespaces မဟုတ်ဘူးဆိုရင် Docker တပ်ဆင်ဖို့လိုအပ်ပြီး အလုပ်အနည်းငယ်များပါတယ်။ ဒါကြောင့် container နဲ့အလုပ်လုပ်ဖူးသူတွေအတွက်သာ အကြံပြုပါတယ်။

GitHub Codespaces သုံးတဲ့အခါ API keys တွေကိုလုံခြုံစွာထားဖို့ Codespace Secrets ကိုသုံးတာ အကောင်းဆုံးနည်းလမ်းတစ်ခုပါ။ [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide ကိုလိုက်နာပါ။

## သင်ခန်းစာများနှင့် နည်းပညာလိုအပ်ချက်များ

သင်တန်းမှာ အယူအဆသင်ခန်းစာ ၆ ခုနဲ့ coding သင်ခန်းစာ ၆ ခု ပါဝင်ပါတယ်။

Coding သင်ခန်းစာများအတွက် Azure OpenAI Service ကိုသုံးထားပါတယ်။ ဒီ code ကို run လုပ်ဖို့ Azure OpenAI service နဲ့ API key လိုအပ်ပါတယ်။ [ဒီ application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) ဖြည့်ပြီး ဝင်ရောက်ခွင့်တောင်းနိုင်ပါတယ်။

သင့် application ကို စစ်ဆေးနေချိန်မှာလည်း coding သင်ခန်းစာတိုင်းမှာ `README.md` ဖိုင်ပါဝင်ပြီး code နဲ့ output တွေကို ကြည့်နိုင်ပါတယ်။

## Azure OpenAI Service ကို ပထမဆုံးအသုံးပြုခြင်း

Azure OpenAI service ကို ပထမဆုံးအသုံးပြုမယ်ဆိုရင် [Azure OpenAI Service resource တစ်ခု ဖန်တီးပြီး deploy လုပ်နည်း](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) ကို လိုက်နာပါ။

## OpenAI API ကို ပထမဆုံးအသုံးပြုခြင်း

OpenAI API ကို ပထမဆုံးအသုံးပြုမယ်ဆိုရင် [Interface တစ်ခု ဖန်တီးပြီး အသုံးပြုနည်း](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) ကို လိုက်နာပါ။

## တခြားလေ့လာသူများနဲ့ တွေ့ဆုံခြင်း

တခြားလေ့လာသူများနဲ့ တွေ့ဆုံနိုင်ဖို့ ကျွန်ုပ်တို့ရဲ့ [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) မှာ channel တွေဖန်တီးထားပါတယ်။ Generative AI ကို စိတ်ဝင်စားတဲ့ စီးပွားရေးလုပ်ငန်းရှင်၊ တည်ဆောက်သူ၊ ကျောင်းသား၊ တိုးတက်ချင်သူတိုင်းအတွက် ကောင်းတဲ့ network ဖြစ်ပါတယ်။

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Project team လည်း ဒီ Discord server မှာ အကူအညီပေးဖို့ ရှိနေပါမယ်။

## ပူးပေါင်းပါ

ဒီသင်တန်းက open-source initiative တစ်ခုပါ။ တိုးတက်စေချင်တာ၊ ပြဿနာတွေ တွေ့ရင် [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) တစ်ခုတင်ပါ၊ ဒါမှမဟုတ် [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) တင်နိုင်ပါတယ်။

Project team က ပူးပေါင်းမှုအားလုံးကို စောင့်ကြည့်နေပါမယ်။ Open source ကို ပူးပေါင်းခြင်းက Generative AI လောကမှာ ကိုယ့်အလုပ်အကိုင်တိုးတက်ဖို့ အကောင်းဆုံးနည်းလမ်းတစ်ခုပါ။

အများစုသော ပူးပေါင်းမှုတွေမှာ Contributor License Agreement (CLA) ကို သဘောတူဖို့လိုပါတယ်။ ဒါက သင့်ပေးအပ်မှုကို ကျွန်ုပ်တို့အသုံးပြုခွင့်ရှိကြောင်း သက်သေပြတာပါ။ အသေးစိတ်ကို [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) မှာ ဖတ်ရှုနိုင်ပါတယ်။

အရေးကြီးချက် - ဒီ repo ထဲက စာသားကို ဘာသာပြန်တဲ့အခါ machine translation မသုံးပါနဲ့။ Community က verify လုပ်မယ်၊ ကိုယ်တကယ်ကျွမ်းကျင်တဲ့ ဘာသာစကားတွေအတွက်သာ volunteer လုပ်ပါ။

Pull request တင်တဲ့အခါ CLA-bot က CLA လိုအပ်/မလိုအပ် စစ်ပြီး PR ကို label, comment နဲ့ decorate လုပ်ပါလိမ့်မယ်။ Bot ရဲ့ညွှန်ကြားချက်ကို လိုက်နာပါ။ ဒီ CLA ကို Microsoft ရဲ့ repo အားလုံးမှာ တစ်ကြိမ်တည်းသာ လုပ်ရပါမယ်။

ဒီ project မှာ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) ကို လက်ခံအသုံးပြုထားပါတယ်။ အသေးစိတ်သိချင်ရင် Code of Conduct FAQ ကိုဖတ်ပါ၊ သို့မဟုတ် [Email opencode](opencode@microsoft.com) ကို မေးမြန်းနိုင်ပါတယ်။

## စတင်လိုက်ကြစို့
ဒီသင်တန်းကိုပြီးစီးဖို့လိုအပ်တဲ့အဆင့်တွေကိုပြီးမြောက်ပြီးသားဖြစ်ပြီဆိုတော့၊ အခုတော့ [Generative AI နဲ့ LLMs အကြောင်းမိတ်ဆက်](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) ကိုစတင်လေ့လာကြမယ်။

---

**သတိပေးချက်**:
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူလစာရွက်စာတမ်းသည် မူရင်းဘာသာစကားဖြင့်သာ အာဏာရှိသော ရင်းမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာသော နားလည်မှုမှားခြင်း သို့မဟုတ် အနားလည်မှားခြင်းများအတွက် ကျွန်ုပ်တို့သည် တာဝန်ယူမည်မဟုတ်ပါ။