<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:19:16+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "my"
}
-->
# ဒီသင်တန်းနဲ့ စတင်ခြင်း

ဒီသင်တန်းကို စတင်ဖို့အတွက် ကျွန်တော်တို့ အရမ်းဝမ်းသာပါတယ်၊ Generative AI နဲ့ ဘာတွေ ဖန်တီးချင်သလဲဆိုတာကို ကြည့်ရှုရမှာပါ!

အောင်မြင်မှုအတွက် ဒီစာမျက်နှာမှာ စတင်ပြင်ဆင်ရမယ့်အဆင့်တွေ၊ နည်းပညာလိုအပ်ချက်တွေ၊ အကူအညီလိုအပ်ရင် ဘယ်မှာရယူရမလဲဆိုတာ ဖော်ပြထားပါတယ်။

## စတင်ပြင်ဆင်ရမယ့်အဆင့်များ

ဒီသင်တန်းကို စတင်ယူရန်အတွက် အောက်ပါအဆင့်များကို ပြီးမြောက်ရပါမယ်။

### ၁။ ဒီ Repo ကို Fork လုပ်ပါ

[Fork လုပ်ပြီး သင့် GitHub အကောင့်ထဲသို့ ယူပါ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)၊ ဒါမှသာ ကုဒ်တွေကို ပြင်ဆင်နိုင်ပြီး စိန်ခေါ်မှုတွေကို ပြီးမြောက်နိုင်မှာဖြစ်ပါတယ်။ ဒီ repo ကို [star (🌟) လုပ်ထားလည်း](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ရှာဖွေဖို့ လွယ်ကူပါလိမ့်မယ်။

### ၂။ codespace တစ်ခု ဖန်တီးပါ

ကုဒ်ကို run လုပ်တဲ့အခါ dependency ပြဿနာတွေ မဖြစ်အောင် ဒီသင်တန်းကို [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) မှာ run လုပ်ဖို့ အကြံပြုပါတယ်။

ဒီ codespace ကို သင့် fork လုပ်ထားတဲ့ repo မှာ `Code` ကိုရွေးပြီး **Codespaces** ကိုရွေးခြင်းဖြင့် ဖန်တီးနိုင်ပါတယ်။

![Dialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

### ၃။ သင့် API Keys များကို သိမ်းဆည်းခြင်း

API keys များကို လုံခြုံစိတ်ချစွာ သိမ်းဆည်းထားခြင်းဟာ မည်သည့် application မဆို တည်ဆောက်ရာမှာ အရေးကြီးပါတယ်။ API keys များကို တိုက်ရိုက်ကုဒ်ထဲမှာ သိမ်းမထားသင့်ပါ။ Public repository မှာ commit လုပ်ခြင်းက လုံခြုံရေးပြဿနာတွေ ဖြစ်ပေါ်စေနိုင်ပြီး မကောင်းဆိုးရွားသူတွေက အသုံးပြုလျှင် မလိုလားအပ်တဲ့ ကုန်ကျစရိတ်တွေ ဖြစ်ပေါ်နိုင်ပါတယ်။

Python အတွက် `.env` ဖိုင် ဖန်တီးပြီး `GITHUB_TOKEN` ထည့်သွင်းနည်းကို အဆင့်ဆင့် လမ်းညွှန်ချက်အဖြစ် ဖော်ပြထားပါတယ်-

1. **Project Directory သို့ သွားပါ**: Terminal သို့ command prompt ကိုဖွင့်ပြီး `.env` ဖိုင် ဖန်တီးမယ့် project ရဲ့ root directory သို့ သွားပါ။

   ```bash
   cd path/to/your/project
   ```

2. **`.env` ဖိုင် ဖန်တီးပါ**: သင့်နှစ်သက်ရာ text editor ဖြင့် `.env` ဆိုတဲ့ ဖိုင်အသစ် ဖန်တီးပါ။ Command line အသုံးပြုမယ်ဆို Unix-based စနစ်တွင် `touch` သို့မဟုတ် Windows တွင် `echo` ကို အသုံးပြုနိုင်ပါတယ်-

   Unix-based စနစ်များ:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` ဖိုင်ကို ပြင်ဆင်ပါ**: `.env` ဖိုင်ကို VS Code, Notepad++ သို့မဟုတ် အခြား editor တစ်ခုဖြင့် ဖွင့်ပါ။ အောက်ပါလိုင်းကို ထည့်သွင်းပြီး `your_github_token_here` ကို သင့် GitHub token နဲ့ အစားထိုးပါ-

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **ဖိုင်ကို သိမ်းဆည်းပြီး ပိတ်ပါ**။

5. **`python-dotenv` ကို install လုပ်ပါ**: `.env` ဖိုင်မှ environment variables များကို Python application ထဲသို့ load လုပ်ဖို့ `python-dotenv` package ကို install လုပ်ရန်လိုအပ်ပါသည်။ `pip` ဖြင့် install လုပ်နိုင်ပါတယ်-

   ```bash
   pip install python-dotenv
   ```

6. **Python script ထဲတွင် Environment Variables များကို load လုပ်ပါ**: Python script ထဲတွင် `python-dotenv` package ကို အသုံးပြု၍ `.env` ဖိုင်မှ environment variables များကို load လုပ်ပါ-

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

ဒါဆိုပြီးပါပြီ! `.env` ဖိုင်ကို အောင်မြင်စွာ ဖန်တီးပြီး GitHub token ကို ထည့်သွင်းပြီး Python application ထဲသို့ load လုပ်နိုင်ပါပြီ။

## ကိုယ်ပိုင်ကွန်ပျူတာပေါ်တွင် run လုပ်နည်း

ကိုယ်ပိုင်ကွန်ပျူတာပေါ်တွင် ကုဒ်ကို run လုပ်ရန် [Python တစ်ခုခု version တပ်ဆင်ထားရပါမယ်](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)။

ပြီးရင် repository ကို clone လုပ်ရပါမယ်-

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

အားလုံးစစ်ဆေးပြီးပါက စတင်လုပ်ဆောင်နိုင်ပါပြီ!

## ရွေးချယ်စရာ အဆင့်များ

### Miniconda တပ်ဆင်ခြင်း

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) သည် [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python နှင့် အချို့သော package များကို တပ်ဆင်ရန် အလွယ်တကူ installer တစ်ခုဖြစ်သည်။
Conda သည် package manager တစ်ခုဖြစ်ပြီး Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) နှင့် package များကို လွယ်ကူစွာ စီမံခန့်ခွဲနိုင်စေသည်။ `pip` ဖြင့် မရနိုင်သော package များကို တပ်ဆင်ရာတွင်လည်း အထောက်အကူဖြစ်သည်။

[MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ကို လိုက်နာပြီး တပ်ဆင်နိုင်ပါသည်။

Miniconda တပ်ဆင်ပြီးပါက [repository ကို clone](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) လုပ်ပါ (မလုပ်ရသေးရင်)။

နောက်တစ်ခုက virtual environment တစ်ခု ဖန်တီးရပါမယ်။ Conda ဖြင့် ဖန်တီးရန် environment file (_environment.yml_) အသစ်တစ်ခု ဖန်တီးပါ။ Codespaces ကို အသုံးပြုနေပါက `.devcontainer` ဖိုလ်ဒါအတွင်း `.devcontainer/environment.yml` အဖြစ် ဖန်တီးပါ။

အောက်ပါ snippet ဖြင့် environment file ကို ဖြည့်စွက်ပါ-

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

conda အသုံးပြုရာတွင် error တွေ ဖြစ်လာရင် terminal မှာ အောက်ပါ command ဖြင့် Microsoft AI Libraries ကို manually install လုပ်နိုင်ပါတယ်-

```
conda install -c microsoft azure-ai-ml
```

environment file မှာ လိုအပ်သော dependencies များ ဖော်ပြထားသည်။ `<environment-name>` သည် သင့် Conda environment အမည်ဖြစ်ပြီး `<python-version>` သည် သင့်အသုံးပြုလိုသော Python ဗားရှင်းဖြစ်သည်၊ ဥပမာ `3` သည် Python ၏ နောက်ဆုံး major ဗားရှင်းဖြစ်သည်။

ပြီးလျှင် အောက်ပါ command များကို command line/terminal မှာ run လုပ်ပြီး Conda environment ကို ဖန်တီးနိုင်ပါသည်-

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

ပြဿနာများရှိပါက [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ကို ရှာဖွေကြည့်ပါ။

### Visual Studio Code ကို Python support extension နဲ့ အသုံးပြုခြင်း

ဒီသင်တန်းအတွက် [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor ကို [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) နဲ့ တပ်ဆင်ပြီး အသုံးပြုရန် အကြံပြုပါတယ်။ ဒါပေမယ့် အတိအကျလိုအပ်ချက် မဟုတ်ပါ။

> **Note**: သင်တန်း repo ကို VS Code မှာ ဖွင့်လျှင် project ကို container အတွင်း စီစဉ်နိုင်ရန် ရွေးချယ်စရာ ရှိပါတယ်။ ဒါဟာ သင်တန်း repo ထဲရှိ [အထူး `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ဖိုလ်ဒါကြောင့် ဖြစ်ပါတယ်။ နောက်ပိုင်းမှာ ပိုမိုရှင်းပြပါမယ်။

> **Note**: Repo ကို clone လုပ်ပြီး VS Code မှာ ဖွင့်လျှင် Python support extension တပ်ဆင်ရန် အကြံပြုချက်ကို အလိုအလျောက် ပြပါလိမ့်မယ်။

> **Note**: VS Code က repo ကို container အတွင်း ပြန်ဖွင့်ဖို့ အကြံပြုလာရင်၊ ကိုယ့်ကွန်ပျူတာမှာ တပ်ဆင်ထားတဲ့ Python ကို အသုံးပြုချင်ရင် ဒီတောင်းဆိုမှုကို ငြင်းပယ်ပါ။

### Browser မှာ Jupyter အသုံးပြုခြင်း

[Browser](https://jupyter.org?WT.mc_id=academic-105485-koreyst) မှာ Jupyter environment ကို အသုံးပြု၍ project ပေါ်မှာ အလုပ်လုပ်နိုင်ပါတယ်။ Classic Jupyter နဲ့ [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) နှစ်မျိုးလုံးမှာ auto-completion, code highlighting စတဲ့ အဆင်ပြေတဲ့ feature တွေ ပါဝင်ပါတယ်။

Jupyter ကို ကိုယ်ပိုင်ကွန်ပျူတာမှာ စတင်ဖို့ terminal/command line ကိုဖွင့်ပြီး သင်တန်း directory သို့ သွားပြီး အောက်ပါ command ကို run ပါ-

```bash
jupyter notebook
```

သို့မဟုတ်

```bash
jupyterhub
```

ဒါက Jupyter instance ကို စတင်ပေးပြီး URL ကို command line မှာ ပြပါလိမ့်မယ်။

URL ကို ဝင်ရောက်ပြီး သင်တန်းအကြောင်းအရာကို ကြည့်ရှုနိုင်ပြီး `*.ipynb` ဖိုင်များသို့ သွားရောက်နိုင်ပါသည်။ ဥပမာ `08-building-search-applications/python/oai-solution.ipynb`။

### Container အတွင်း run လုပ်ခြင်း

ကိုယ်ပိုင်ကွန်ပျူတာ သို့မဟုတ် Codespace မှာ အားလုံးကို တပ်ဆင်ဖို့ အစား [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) ကို အသုံးပြုနိုင်ပါတယ်။ သင်တန်း repo ထဲရှိ အထူး `.devcontainer` ဖိုလ်ဒါကြောင့် VS Code က project ကို container အတွင်း စီစဉ်နိုင်ပါတယ်။ Codespaces အပြင်မှာတော့ Docker တပ်ဆင်ရမည်ဖြစ်ပြီး အလုပ်အတော်များတာကြောင့် container တွေနဲ့ အတွေ့အကြုံရှိသူတွေအတွက်သာ အကြံပြုပါတယ်။

GitHub Codespaces အသုံးပြုတဲ့အခါ API keys များကို လုံခြုံစွာ ထိန်းသိမ်းဖို့ Codespace Secrets ကို အသုံးပြုနိုင်ပါတယ်။ [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) လမ်းညွှန်ကို လိုက်နာပါ။

## သင်ခန်းစာများနှင့် နည်းပညာလိုအပ်ချက်များ

သင်တန်းမှာ အကြောင်းအရာ သင်ခန်းစာ ၆ ခုနဲ့ ကုဒ်ရေးသင်ခန်းစာ ၆ ခု ပါဝင်ပါတယ်။

ကုဒ်ရေးသင်ခန်းစာများအတွက် Azure OpenAI Service ကို အသုံးပြုထားပါတယ်။ ဒီကုဒ်ကို run လုပ်ဖို့ Azure OpenAI service နှင့် API key လိုအပ်ပါမယ်။ [ဒီလျှောက်လွှာကို ဖြည့်ပြီး](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) ဝင်ခွင့်ရယူနိုင်ပါတယ်။

လျှောက်လွှာကို စစ်ဆေးနေစဉ်မှာ ကုဒ်ရေးသင်ခန်းစာတိုင်းမှာ `README.md` ဖိုင်ပါဝင်ပြီး ကုဒ်နဲ့ output များကို ကြည့်ရှုနိုင်ပါတယ်။

## Azure OpenAI Service ကို ပထမဆုံးအသုံးပြုခြင်း

Azure OpenAI service ကို ပထမဆုံး အသုံးပြုမယ်ဆိုရင် [Azure OpenAI Service resource ဖန်တီးခြင်းနှင့် deploy လုပ်ခြင်း](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) လမ်းညွှန်ကို လိုက်နာပါ။

## OpenAI API ကို ပထမဆုံးအသုံးပြုခြင်း

OpenAI API ကို ပထမဆုံး အသုံးပြုမယ်ဆိုရင် [Interface ဖန်တီးခြင်းနှင့် အသုံးပြုခြင်း](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) လမ်းညွှန်ကို လိုက်နာပါ။

## အခြားသင်ယူသူများနှင့် တွေ့ဆုံခြင်း

ကျွန်တော်တို့ရဲ့ တရားဝင် [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) မှာ အခြားသင်ယူသူတွေနဲ့ တွေ့ဆုံဖို့ channel များ ဖန်တီးထားပါတယ်။ ဒီနေရာက Generative AI ကို တိုးတက်လိုသူ စီးပွားရေးလုပ်ငန်းရှင်များ၊ ဖန်တီးသူများ၊ ကျောင်းသားများနဲ့ အခြားသူများနဲ့ ဆက်သွယ်ဖလှယ်ဖို့ အကောင်းဆုံးနေရာဖြစ်ပါတယ်။

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Project အဖွဲ့ကလည်း ဒီ Discord server မှာ သင်ယူသူများကို ကူညီပေးမှာ ဖြစ်ပါတယ်။

## ပံ့ပိုးပါ

ဒီသင်တန်းဟာ open-source initiative တစ်ခုဖြစ်ပါတယ်။ တိုးတက်စရာရှိတာတွေ သို့မဟုတ် ပြဿနာတွေ တွေ့ရင် [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) တစ်ခု ဖန်တီးပါ၊ ဒါမှမဟုတ် [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) တင်ပါ။

Project အဖွဲ့က အားလုံးသော ပံ့ပိုးမှုများကို စောင့်ကြည့်ပါမယ်။ Open source ကို ပံ့ပိုးခြင်းဟာ Generative AI လောကမှာ သင့်အလုပ်အကိုင် တည်ဆောက်ရာမှာ အလွန်ကောင်းမွန်တဲ့ နည်းလမ်းတစ်ခုဖြစ်ပါတယ်။

အများစုသော ပံ့ပိုးမှုများအတွက် Contributor License Agreement (CLA) ကို သဘောတူရမည်ဖြစ်ပြီး သင့်ပံ့ပိုးမှုကို အသုံးပြုခွင့်ပေးသည်ကို သက်သေပြရပါမယ်။ အသေးစိတ်အချက်အလက်များအတွက် [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ရှုပါ။

အရေးကြီးချက်- ဒီ repo ထဲမှာ ဘာသာပြန်ရာတွင် machine translation မသုံးရပါ။ ကျွန်တော်တို့က community မှတစ်ဆင့် ဘာသာပြန်ချက်များကို စစ်ဆေးမယ်၊ ထို့ကြောင့် သင်ကျွမ်းကျင်တဲ့ ဘာသာစကားများအတွက်သာ volunteer လုပ်ပါ။

Pull request တင်တဲ့အခါ CLA-bot က သင့်အား CLA လိုအပ်မလား ဆုံးဖြတ်ပြီး PR ကို သင့်တော်စွာ အမှတ်အသားပြုပါလိမ့်မယ် (ဥပမာ label, comment)။ Bot ရဲ့ ညွှန်ကြားချက်များကို လိုက်နာပါ။ CLA လိုအပ်မှုကို repository အားလုံးအတွက် တစ်ကြိမ်တည်းသာ ပြုလုပ်ရပါမယ်။

ဒီ project က [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) ကို လက်ခံအသုံးပြုထားပါတယ်။ ပိုမိုသိရှိလိုပါက Code of Conduct FAQ ကို ဖတ်ရှုပါ၊ သို့မဟုတ်

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းမှုများ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။