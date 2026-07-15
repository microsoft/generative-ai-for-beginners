# ဒီသင်တန်းနဲ့ စတင်ခြင်း

သင်ဤသင်တန်းကို စတင်ဖို့နှင့် Generative AI နဲ့ ဘာတွေဖန်တီးလိုသလဲဆိုတာအား စိတ်လှုပ်ရှားစွာ ကြိုဆိုပါတယ်!

သင့်အောင်မြင်မှုအတွက် ဒီစာမျက်နှာအတွင်း ကွပ်မျက်ခြင်းဆိုင်ရာအဆင့်များ၊ နည်းပညာလိုအပ်ချက်များနဲ့ အကူအညီရယူနိုင်မည့်နေရာများကို ဖော်ပြထားသည်။

## ကွပ်မျက်ခြင်းဆိုင်ရာ အဆင့်များ

ဒီသင်တန်းကို စတင်ဝင်ရောက်သင်ယူရန် အောက်ပါအဆင့်များကို ပြီးစီးရန် လိုအပ်သည်။

### ၁။ ဒီ Repo ကို Fork လုပ်ပါ

[Repo ကို မိမိ GitHub အကောင့်အောက်သို့ Fork လုပ်ပါ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)။ ဒီနေရာမှာ သင်သည် ကုဒ်များကို ပြင်ဆင်နိုင်ပြီး စိန်ခေါ်မှုများကို ပြီးမြောက်စေရန် ဖြစ်သည်။ ထို့အပြင် [repo ကို star (🌟) ပေးနိုင်ပါသည်](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)၊ သင်နှင့်ဆက်နွယ်သော repos များကို လွယ်ကူစွာ ရှာဖွေပါ။

### ၂။ Codespace တည်ဆောက်ပါ

ကုဒ်တွင် မည်သည့် dependency ပြဿနာမရှိစေရန်အတွက် [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) တွင် ဒီသင်တန်းကို ပြုလုပ်ရန် တိုက်တွန်းပါသည်။

သင့် Fork တွင်: **Code -> Codespaces -> New on main**

![codespace ဖန်တီးရန် button များပြသထားသော ဆွဲချက်ပြပုံ](../../../translated_images/my/who-will-pay.4c0609b1c7780f44.webp)

#### ၂.၁ Secret တစ်ခုပေါင်းထည့်ပါ

၁။ ⚙️ဂီယာ အိုင်ကွန် -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret။
၂။ OPENAI_API_KEY အမည်ပေးပြီး ကိုယ်ပိုင် key ကို ကူးထည့်ပါ၊ သိမ်းဆည်းပါ။

### ၃။ ဒါနောက်ဘာလဲ?

| ငါပြုလုပ်ချင်တာ…  | သွားရန်…                                                   |
|---------------------|-----------------------------------------------------------|
| Lesson 1 စတင်ရန်   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md) |
| Offline အလုပ်လုပ်ရန် | [`setup-local.md`](02-setup-local.md)                         |
| LLM ပံ့ပိုးသူ တပ်ဆင်ရန် | [`providers.md`](03-providers.md)                                |
| အခြားသင်ယူသူများနှင့် တွေ့ဆုံရန် | [Discord ကို ဝင်ရောက်ပါ](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)  |

## ပြဿနာဖြေရှင်းမှု


| လက္ခဏာ                                  | ဖြေရှင်းချက်                                                 |
|-----------------------------------------|-------------------------------------------------------------|
| Container တည်ဆောက်ခြင်း ၁၀ မိနစ်ကျော် ရပ်တန့်နေခြင်း | **Codespaces ➜ “Rebuild Container”**                         |
| `python: command not found`               | Terminal မဆက်သွယ်ခဲ့ပါ; **+** ➜ *bash* ကိုနှိပ်ပါ              |
| OpenAI မှ `401 Unauthorized` ပြန်လာခြင်း       | မှားနေသော / သက်တမ်းကုန်ဆုံးသွားသော `OPENAI_API_KEY`             |
| VS Code တွင် “Dev container mounting…” ပြသခြင်း | Browser tab ကို Refresh လုပ်ပါ—Codespaces အချိန်ကာလတစ်ခုတွင် ချိတ်ဆက်မှု ပျောက်ကွယ်နိုင်သည် |
| Notebook kernel ပျောက်ဆုံးခြင်း                  | Notebook menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Unix-based စနစ်များအတွက်:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

၃။ **`.env` ဖိုင်ကို ပြန်စီမယ်**: `.env` ဖိုင်ကို စာတည်းဖြင့် ဖွင့်ပါ (ဥပမာ, VS Code, Notepad++ သို့မဟုတ် အခြားဖြည့်စွက် စာတည်းရေးစက်များ)။ အောက်ပါကြောင်းများကိုထည့်ပြီး သင်၏ Microsoft Foundry Models endpoint နှင့် key ကို သင့်ကိုယ်ပိုင်အသေးစိတ်ဖြင့် ပြောင်းပါ (ရယူနည်းကို [`providers.md`](03-providers.md) တွင် ကြည့်ရူနိုင်သည်)။

   > **မှတ်ချက်**: GitHub Models (နှင့် `GITHUB_TOKEN` variable) သည် ၂၀၂၆ ခုနှစ် ဇူလိုင်လ အဆုံးတွင်ရပ်စဲတော့မည်။ အစား [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ကိုအသုံးပြုပါ။

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

၄။ **ဖိုင်ကို သိမ်းဆည်းပါ**: ပြင်ဆင်ပြီး ပြီးသည့်နောက် ဖိုင်ကို သိမ်းဆည်းပြီး စာတည်းရေးစက်ကို ပိတ်ပါ။

၅။ **`python-dotenv` ကို တပ်ဆင်ပါ**: သင် မတပ်ဆင်ထားသေးပါက `.env` ဖိုင်မှ ပတ်ဝန်းကျင် အပြောင်းအလဲများကို Python အပ်လီကေးရှင်းသို့ အသုံးပြုရန် `python-dotenv` package ကို တပ်ဆင်ရန် လိုအပ်ပါသည်။ `pip` ဖြင့် တပ်ဆင်နိုင်သည်။

   ```bash
   pip install python-dotenv
   ```

၆။ **Python script တွင် စည်းမျဉ်းအပြောင်းအလဲများကို Load ပြုလုပ်ရန်**: Python script တွင် `python-dotenv` package ကို အသုံးပြု၍ `.env` ဖိုင်မှ ပတ်ဝန်းကျင် အပြောင်းအလဲများကို load ပြုလုပ်ပါ။

   ```python
   from dotenv import load_dotenv
   import os

   # .env ဖိုင်မှ ပတ်ဝန်းကျင် biếnများကို လုပ်ဆောင်ပါ
   load_dotenv()

   # Microsoft Foundry Models biếnများကို ဝင်ရောက် အသုံးပြုပါ
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

ဒီထိပါပဲ! `.env` ဖိုင် ဖန်တီးပြီး Microsoft Foundry Models ချိတ်ဆက်ချက်များ ထည့်သွင်းထားပြီး Python အပ်လီကေးရှင်းထဲသို့ load ပြုလုပ်နိုင်ပြီ ဖြစ်သည်။

## ကိုယ်ပိုင်ကွန်ပျူတာတွင် ဘယ်လို run လုပ်မလဲ

ကိုယ်ပိုင်ကွန်ပျူတာတွင် ကုဒ် run လုပ်ရန် [Python တစ်ခုခု တပ်ဆင်ထား] (https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ရမည်။

ဘယ်လိုrepo ကိုအသုံးပြုမည့်အတွက် ကွန်ပျူတာတွင် clone လုပ်ရပါမည်။

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

အားလုံးပြီးချိန်မှ စတင်နိုင်ပြီ ဖြစ်သည်။

## ရွေးချယ်စရာ လုပ်ဆောင်ချက်များ

### Miniconda တပ်ဆင်ခြင်း

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) သည် [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)၊ Python နှင့် package များ များကို တပ်ဆင်ရန် အလျော့ချInstaller ဖြစ်သည်။
Conda သည် package manager ဖြစ်ပြီး Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) အသစ်များဖြစ်စေ၊ package များပြောင်းလဲအသုံးပြုဖို့ လွယ်ကူစေရန် ဖြစ်သည်။ `pip` ဖြင့် မရရှိနိုင်သည့် package များလည်း တပ်ဆင်နိုင်စေသည်။

[MiniConda တပ်ဆင်လမ်းညွန်](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ကို လိုက်နာပြီး တပ်ဆင်နိုင်သည်။

Miniconda တပ်ဆင်ပြီးပါက၊ [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ကို clone လုပ်ပါ (အလုပ်မလုပ်ခင်)

နောက်တစ်ဆင့်အဖြစ် virtual environment ဖန်တီးရမည်။ Conda အသုံးပြုပြီးအလုပ်လုပ်မည်ဆိုလျှင် `_environment.yml_` ဖိုင်အသစ် တည်ဆောက်ပါ။ Codespaces ကိုနောက်ခံရင်း အသုံးပြုနေပါက `.devcontainer` ဖိုဒါထဲတွင် ဖန်တီးပါ၊ ဒါမှ `.devcontainer/environment.yml` ဖြစ်စေ။

အောက်ပါအတိုင်း environment ဖိုင်ကို ဖြည့်ပါ။

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

Conda အပိုင်းတွင် အမှားဖြစ်ပါက terminal တွင် အောက်ပါ command ဖြင့် Microsoft AI Libraries ကို manually တပ်ဆင်နိုင်သည်။

```
conda install -c microsoft azure-ai-ml
```

Environment file သည် လိုအပ်သော dependency များ ဖော်ပြသည်။ `<environment-name>` သည် သင်သတ်မှတ်လိုသော Conda environment အမည်ဖြစ်ပြီး၊ `<python-version>` သည် သင်အသုံးပြုလိုသော Python ဗားရှင်းဖြစ်သည်၊ ဥပမာ `3` သည် Python ၏ နောက်ဆုံးကြီးမားသောဗားရှင်းဖြစ်သည်။

ပြီးဆုံးသွားပါက Command line သို့မဟုတ် terminal တွင် အောက်ပါ command များကို चलाकर Conda environment ကိုဖန်တီးနိုင်သည်။

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path သည် Codespace ဆက်တပ်ခွင့်များအတွက်သာ အသုံးပြုသည်။
conda activate ai4beg
```

အခက်အခဲများရှိပါက [Conda environments လမ်းညွန်](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ရှုပါ။

### Python Support Extension ပါတဲ့ Visual Studio Code အသုံးပြုခြင်း

ဒီသင်တန်းအတွက် [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) ကို [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ထည့်သွင်းထားပြီး အသုံးပြုရန် တိုက်တွန်းပါသည်။ ဒါပေမဲ့ ပြီးပြည့်စုံတဲ့လိုအပ်ချက်မဟုတ်ပါ။

> **မှတ်ချက်**: သင်သည် သင်တန်း repo ကို VS Code တွင်ဖွင့်လှစ်သည့်အခါ၊ project ကို container အတွင်းတည်ဆောက်ရန် ရွေးချယ်နိုင်သည်။ ဘာဖြစ်လို့လဲဆိုတော့ သင်တန်း repo ထဲတွင် [အထူး `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ဖိုဒါပါရှိပါသည်။ နောက်ပိုင်းတွင် ထပ်မံရှင်းပြပါမည်။

> **မှတ်ချက်**: repo ကိုcloneလုပ်ပြီး VS Code တွင်ဖွင့်လှစ်သည်နှင့်အတူ Python support extension တပ်ဆင်ရန် အလိုအလျောက် အကြံပြုချက် ပြမည်။

> **မှတ်ချက်**: VS Code သည် repo ကို container ထဲတွင် မဖွင့်ချင်ကာဆိုသည်နှင့်အတူ reject လုပ်ခြင်းဖြင့် ကိုယ်ပိုင် Python ဗားရှင်း အသုံးပြုနိုင်ပါသည်။

### Browser အတွင်း Jupyter အသုံးပြုခြင်း

သင်သည် သင်၏ browser အတွင်း [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ဖြင့်လည်း ပရောဂျက်ကို လုပ်ဆောင်နိုင်သည်။ Classic Jupyter နှင့် [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) သည် auto-completion ၊ ကုဒ်အဓိပ္ပာယ်ဖော်ပြခြင်းစသည်တို့ ပါဝင်သည့် ဒီဗဲလပ်မှု ပတ်၀န်းကျင်အသစ်များပေးသည်။

Jupyter ကို ကိုယ်ပိုင်စက်ပေါ်တွင် စတင်ရန် terminal/command line ကိုဖွင့်ပြီး သင်တန်း directory ထဲသို့ သွား၍ အောက်ပါ command ကို အ执行ပါ။

```bash
jupyter notebook
```

သို့မဟုတ်

```bash
jupyterhub
```

ဤကိရိယာက Jupyter instance တစ်ခု စတင်ပေးမည် ဖြစ်ပြီး အကောက် URL ကို command line ပြတင်းပေါ်တွင် ပြမည်။

URL ကို ဝင်ရောက်လျှင် သင်တန်း အကြောင်းအရာစာရင်းကို ကြည့်နိုင်ပြီး မည်သည့် `*.ipynb` ဖိုင်ကိုမဆို သွားရောက်နိုင်သည်။ ဥပမာ၊ `08-building-search-applications/python/oai-solution.ipynb` ။

### Container ထဲတွင် အလုပ်လုပ်ခြင်း

ကိုယ်ပိုင်ကွန်ပျူတာ သို့မဟုတ် Codespace တွင် အားလုံးကိုတပ်ဆင်ခြင်းအစား [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) အသုံးပြုနိုင်သည်။ သင်တန်း repo ထဲရှိ အထူး `.devcontainer` ဖိုဒါက VS Code အတွက် project ကို container အတွင်းမှာ တပ်ဆင်ပေးနိုင်စေသည်။ Codespaces အပြင် Docker တပ်ဆင်ရန် လိုမည်ဖြစ်ပြီး တတ်ကြွမှု အနည်းငယ်လိုအပ်သည့်အတွက် အတွေ့အကြုံရှိသူများအတွက်သာ အကြံပြုပါသည်။

GitHub Codespaces အသုံးပြုသည့်အခါ သင့် API key များကို လုံခြုံစေရန် Codespace Secrets ကို အသုံးပြုပါ။ အသေးစိတ်အတွက် [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) လမ်းညွှန်ကို လေ့လာပါ။


## သင်ခန်းစာများနှင့် နည်းပညာလိုအပ်ချက်များ

သင်တန်းတွင် အတွေးအခေါ် သင်ခန်းစာ ၆ ခုနှင့် ကုဒ်ရေးသင်ခန်းစာ ၆ ခု ပါဝင်သည်။

ကုဒ်ရေးသင်ခန်းစာများအတွက် Azure OpenAI Service ကို အသုံးပြုသည်။ သင်သည် Azure OpenAI service နှင့် API key ရယူထားရမည်။ အသုံးပြုခွင့်ရရန် [ဒီလျှောက်လွှာကို ပြုလုပ်ပါ](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)။

သင့်လျှောက်လွှာကို အတည်ပြုဆောင်ရွက်ခြင်းခံရသည်အထိ စောင့်ဆိုင်းနေစဉ်တွင် ကုဒ်နှင့် output များ ကြည့်ရှုနိုင်သော `README.md` ဖိုင်ကို ကုဒ်ရေးသင်ခန်းစာတွင် ပါရှိသည်။

## Azure OpenAI Service ကို ပထမဆုံးအသုံးပြုခြင်း

Azure OpenAI service ကို ပထမဆုံးအသုံးပြုမည်ဆိုလျှင် ဒီလမ်းညွှန်အတိုင်း [Azure OpenAI Service resource တည်ဆောက်ခြင်းနှင့် Deploy လုပ်ခြင်း](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) ကို လိုက်နာပါ။

## OpenAI API ကို ပထမဆုံးအသုံးပြုခြင်း

OpenAI API ကို ပထမဆုံးအသုံးပြုမည်ဆိုလျှင် ဒီလမ်းညွှန်အတိုင်း [Interface တည်ဆောက်ခြင်းနှင့် အသုံးပြုခြင်း](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) ကိုလိုက်နာပါ။

## အခြားသင်ယူသူများနှင့် တွေ့ဆုံခြင်း

ကျွန်ုပ်တို့သည် တရားဝင် [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) တွင် အခြားသင်ယူသူများနှင့် တွေ့ဆုံရန် channel များဖန်တီးထားသည်။ ဒီနေရာမှာ ဒီဇိုင်နာများ၊ စီမံခန့်ခွဲသူများ၊ ကျောင်းသားများနှင့် Generative AI စွမ်းရည်မြှင့်တင်လိုသူများအတွက် ကြိုဆိုခွင့်ရှိသည်။

[![Discord channel ကို ဝင်ရောက်ရန်](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

ပရောဂျက်အဖွဲ့သည်လည်း ဒီ Discord server တွင် မည်သည့်သင်ယူသူကိုမဆို အကူအညီပေးရန် ရှိပါသည်။

## ပံ့ပိုးပါ

ဒီသင်တန်းသည် အခမဲ့ ရင်းမြစ်ဖြစ်ပါသည်။ တိုးတက်အဆင့်မြှင့်ရန် သို့မဟုတ် ပြဿနာတွေ့ပါက [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) တစ်ခုတင်လိုက်ပါ သို့မဟုတ် [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) တင်ပါ။

ပရောဂျက်အဖွဲ့သည် မည်သည့်ပံ့ပိုးမှုများကိုမဆို နှစ်သက်စွာ လိုက်လံစောင့်ကြည့်ပါမည်။ open source ပံ့ပိုးမှုသည် Generative AI ကြားက အလုပ်အကိုင် တိုးတက်မြင့်မားရန် အဖိုးတန်နည်းလမ်းတစ်ခုဖြစ်သည်။

အများအားဖြင့် ပံ့ပိုးမှုရရှိရန် Contributor License Agreement (CLA) သဘောတူညီချက်ကို သင် အတည်ပြုရမည်ဖြစ်ပြီး၊ သင်၏ပံ့ပိုးမှု အသုံးပြုခွင့်ကို ကျွန်ုပ်တို့အား ထောက်ခံပေးသည်ဟု မှတ်ပြုလက်ခံရပါမည်။ အသေးစိတ်အချက်အလက်များအတွက် [CLA, Contributor License Agreement ဝက်ဘ်ဆိုက်](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) သွားရောက် ကြည့်ရှုနိုင်ပါသည်။

အရေးကြီး: repo တွင် စာသားဘာသာပြန်သည့်အခါ မစက်ကိရိယာဘာသာပြန်တော်တော်ကို မသုံးပါနှင့်။ ဘာသာပြန်မှုကို အသိုင်းအဝိုင်းမှ သုံးသပ်ကြည့်ရှုမည်ဖြစ်ပြီး၊ သင့်ဘာသာစကားတွင်ကျွမ်းကျင်သူများသာ စိတ်ပါဝင်စားပါကသာ ဘာသာပြန်ရန် လိုအပ်ပါသည်။

Pull request တင်သည်နှင့်အမျှ CLA-bot သည် သင့်ထည့်သွင်းမှုအတွက် CLA လိုအပ်ခြင်းရှိ/မရှိကို အလိုအလျောက် သတ်မှတ်ပေးပြီး PR ကို သင့်တင့်စွာ အမှတ်အသားပေးပါမည်။ bot ပေးသော ညွှန်ကြားချက်များကို လိုက်နာသွားပါက စာရင်းသွင်းချက်များအတွက် တစ်ကြိမ်တည်း လုပ်ရမည် ဖြစ်သည်။


ဤပရောဂျက်သည် [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) ကို လက်ခံအသုံးပြုထားပါသည်။ အသေးစိတ်သိရှိလိုပါက Code of Conduct FAQ ကို ဖတ်ရှုပြီး သို့မဟုတ် ထပ်မံမေးမြန်းလိုသည့် မေးခွန်းများ သို့မဟုတ် မှတ်ချက်များအတွက် [Email opencode](opencode@microsoft.com) ကို ဆက်သွယ်ပါ။

## စတင်လိုက်ပါစို့

ဒီသင်ကြားမှုကို ပြီးစီးရန် လိုအပ်သော အဆင့်များကို ပြီးမြောက်သွားသဖြင့်၊ [Generative AI နှင့် LLMs အကြောင်းအညွှန်း](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) ကို ရယူခြင်းဖြင့် စတင်လိုက်ပါစို့။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->