<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T09:02:38+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "my"
}
-->
# ဒီသင်ခန်းစာကို စတင်ပါ

Generative AI နဲ့ ဘာတွေ တည်ဆောက်ရင် စိတ်ကူးရမလဲဆိုတာကို ကြည့်ဖို့ သင်ခန်းစာကို စတင်ဖို့ ကျွန်တော်တို့ အရမ်း စိတ်လှုပ်ရှားနေပါတယ်!

သင့်အောင်မြင်မှုအတွက် ဒီစာမျက်နှာမှာ တပ်ဆင်ခြင်းအဆင့်များ၊ နည်းပညာလိုအပ်ချက်များနှင့် လိုအပ်ပါက အကူအညီရရှိနိုင်သောနေရာများကို ဖော်ပြထားသည်။

## တပ်ဆင်ခြင်းအဆင့်များ

ဒီသင်ခန်းစာကို စတင်ရန် သင်သည် အောက်ပါအဆင့်များကို ပြီးမြောက်ရမည်။

### 1. ဒီ Repo ကို Fork လုပ်ပါ

ဒီ repo အားလုံးကို သင်၏ GitHub အကောင့်သို့ [Fork လုပ်ပါ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)၊ သင်သည် code ကို ပြောင်းလဲရန်နှင့် စိန်ခေါ်မှုများကို ပြီးမြောက်ရန် စွမ်းရည်ရှိရန်။ သင်သည် ဒီ repo ကို အလွယ်တကူရှာဖွေရန်နှင့် သက်ဆိုင်သော repo များကို [star (🌟) လုပ်နိုင်သည်](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)။

### 2. Codespace တစ်ခုကို ဖန်တီးပါ

code ကို run လုပ်ရာတွင် မည်သည့် dependency ပြဿနာများမရှိစေရန်၊ ဒီသင်ခန်းစာကို [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) တွင် run လုပ်ရန် ကျွန်တော်တို့ အကြံပြုပါသည်။

ဒီ repo ၏ fork လုပ်ထားသော ဗားရှင်းတွင် `Code` ရွေးချယ်ခြင်းနှင့် **Codespaces** ရွေးချယ်ခြင်းအားဖြင့် ဖန်တီးနိုင်သည်။

![Dialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. သင့် API Key များကို သိမ်းဆည်းခြင်း

မည်သည့် application မဆို တည်ဆောက်ရာတွင် သင့် API key များကို လုံခြုံစွာ သိမ်းဆည်းထားခြင်းသည် အရေးကြီးသည်။ API key များကို သင့် code တွင် တိုက်ရိုက် သိမ်းဆည်းခြင်းကို ကျွန်တော်တို့ မလုပ်ရန် အကြံပြုပါသည်။ ထိုအသေးစိတ်များကို public repository သို့ commit လုပ်ခြင်းသည် လုံခြုံရေးပြဿနာများနှင့် မလိုလားအပ်သော ကုန်ကျစရိတ်များ ဖြစ်ပေါ်စေပါမည်။

Python အတွက် `.env` ဖိုင်ကို ဖန်တီးပြီး `GITHUB_TOKEN` ထည့်ရန် အဆင့်တစ်ဆင့်လမ်းညွှန်ချက်ကို ဤနေရာတွင် ရှာဖွေပါ:

1. **သင့် Project Directory သို့ သွားပါ**: သင့် terminal သို့မဟုတ် command prompt ကို ဖွင့်ပြီး `.env` ဖိုင်ကို ဖန်တီးလိုသော သင့် project ၏ root directory သို့ သွားပါ။

   ```bash
   cd path/to/your/project
   ```

2. **`.env` ဖိုင်ကို ဖန်တီးပါ**: သင်နှစ်သက်သော text editor ကို အသုံးပြုပြီး `.env` အမည်ရှိ ဖိုင်အသစ်ကို ဖန်တီးပါ။ သင် command line ကို အသုံးပြုနေပါက `touch` (on Unix-based systems) or `echo` ကို အသုံးပြုနိုင်သည် (Windows တွင်):

   Unix-based systems:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **`.env` ဖိုင်ကို တည်းဖြတ်ပါ**: `.env` ဖိုင်ကို text editor (ဥပမာ- VS Code, Notepad++, သို့မဟုတ် အခြား editor များ) တွင် ဖွင့်ပါ။ `your_github_token_here` ကို သင့် actual GitHub token ဖြင့် အစားထိုးပြီး ဖိုင်တွင် အောက်ပါလိုင်းကို ထည့်ပါ:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **ဖိုင်ကို သိမ်းဆည်းပါ**: ပြောင်းလဲမှုများကို သိမ်းဆည်းပြီး text editor ကို ပိတ်ပါ။

5. `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` package ကို `.env` ဖိုင်မှ environment variables များကို သင့် Python application သို့ load လုပ်ရန် install လုပ်ပါ။ သင် `pip` ကို အသုံးပြု၍ install လုပ်နိုင်သည်:

   ```bash
   pip install python-dotenv
   ```

6. **သင့် Python script တွင် Environment Variables များကို Load လုပ်ပါ**: သင့် Python script တွင် `.env` ဖိုင်မှ environment variables များကို load လုပ်ရန် `python-dotenv` package ကို အသုံးပြုပါ:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

ဒါဆိုပြီးပါပြီ! သင် `.env` ဖိုင်ကို အောင်မြင်စွာ ဖန်တီးပြီး၊ သင့် GitHub token ကို ထည့်ပြီး သင့် Python application သို့ load လုပ်ပြီးပါပြီ။

## သင့်ကွန်ပျူတာပေါ်တွင် locally run လုပ်ရန် ဘယ်လိုလုပ်ရမလဲ

သင့်ကွန်ပျူတာပေါ်တွင် code ကို locally run လုပ်ရန် [Python installed](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ၏ မည်သည့် ဗားရှင်းမဆို ရှိရမည်။

ဒီ repo ကို အသုံးပြုရန် သင်သည် clone လုပ်ရန် လိုအပ်ပါသည်:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

အရာအားလုံးကို စစ်ဆေးပြီးနောက် သင် စတင်နိုင်ပါပြီ!

## ရွေးချယ်နိုင်သော အဆင့်များ

### Miniconda ကို 설치하기

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) သည် [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python နှင့် အချို့သော packages များကို 설치 하기 위한 အလေးပေါ့ installer ဖြစ်သည်။ Conda ကိုယ်တိုင်သည် package manager ဖြစ်ပြီး Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) နှင့် packages များကို အလွယ်တကူ တပ်ဆင်ရန်နှင့် ပြောင်းရန် လွယ်ကူစေသည်။ `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` မှတဆင့် ရရှိနိုင်သော packages များကို 설치 하기 အတွက်လည်း အကျိုးရှိသည်။

အောက်ပါ snippet ဖြင့် သင့် environment ဖိုင်ကို ဖြည့်ပါ:

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

conda ကို အသုံးပြုရာတွင် error များရရှိနေသည်ကို တွေ့ရပါက terminal တွင် အောက်ပါ command ကို အသုံးပြုပြီး Microsoft AI Libraries ကို လက်စွဲဖြင့် 설치 လုပ်နိုင်ပါသည်။

```
conda install -c microsoft azure-ai-ml
```

environment ဖိုင်သည် လိုအပ်သော dependencies များကို ဖော်ပြသည်။ `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` သည် Python ၏ နောက်ဆုံးထွက် major version ဖြစ်သည်။

ဒါဆိုပြီးပါပြီ၊ သင်၏ command line/terminal တွင် အောက်ပါ command များကို run လုပ်ခြင်းအားဖြင့် သင့် Conda environment ကို ဖန်တီးနိုင်ပါပြီ

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

ပြဿနာများ ရှိပါက [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ကို ကိုးကားပါ။

### Python support extension ဖြင့် Visual Studio Code ကို အသုံးပြုခြင်း

ဒီသင်ခန်းစာအတွက် [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor ကို Python support extension ဖြင့် 설치 လုပ်ထားသော editor ကို အသုံးပြုရန် ကျွန်တော်တို့ အကြံပြုပါသည်။ ဒါပေမယ့် ဒီဟာက အကြံပြုချက်သာဖြစ်ပြီး အမိန့်မဟုတ်ပါ။

> **Note**: သင် VS Code တွင် သင်ခန်းစာ repository ကို ဖွင့်ခြင်းအားဖြင့် project ကို container အတွင်းတွင် တပ်ဆင်ရန် ရွေးချယ်စရာရှိသည်။ ၎င်းသည် သင်ခန်းစာ repository အတွင်း တွေ့ရှိသော [အထူး `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) directory ကြောင့် ဖြစ်သည်။ ၎င်းအကြောင်း အနည်းငယ်နောက်ပိုင်းတွင် ဖော်ပြပါမည်။

> **Note**: သင် VS Code တွင် directory ကို clone လုပ်ပြီး ဖွင့်သောအခါ Python support extension တပ်ဆင်ရန် အလိုအလျောက် အကြံပြုပါလိမ့်မည်။

> **Note**: VS Code သည် repository ကို container အတွင်းတွင် ပြန်ဖွင့်ရန် အကြံပြုပါက၊ locally installed Python version ကို အသုံးပြုရန် ဒီတောင်းဆိုမှုကို ငြင်းပယ်ပါ။

### Browser တွင် Jupyter ကို အသုံးပြုခြင်း

သင်သည် သင့် browser အတွင်း [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ကို အသုံးပြုပြီး project ကို လုပ်ဆောင်နိုင်ပါသည်။ classic Jupyter နှင့် [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) နှစ်ခုစလုံးသည် auto-completion, code highlighting စသည်တို့ကဲ့သို့သော လုပ်ဆောင်ချက်များနှင့်အတူ အလွန် ပျော်ရွှင်ဖွယ်ကောင်းသော development environment ကို ပေးသည်။

Jupyter ကို locally စတင်ရန် terminal/command line သို့ သွားပြီး သင်ခန်းစာ directory သို့ သွားပြီး အကောင်အထည်ဖော်ပါ:

```bash
jupyter notebook
```

သို့မဟုတ်

```bash
jupyterhub
```

ဒါက Jupyter instance ကို စတင်ပါလိမ့်မည်၊ ၎င်းကို access လုပ်ရန် URL ကို command line window အတွင်း တွေ့မြင်ပါလိမ့်မည်။

သင် URL ကို access လုပ်ပြီးနောက် သင် သင်ခန်းစာ အကြောင်းအရာကို မြင်ရမည်ဖြစ်ပြီး `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` ဖိုင်သို့ သွားရောက်နိုင်ပြီး code နှင့် output များကို ကြည့်နိုင်ပါမည်။

## Azure OpenAI Service ကို ပထမဆုံးအသုံးပြုခြင်း

သင်သည် Azure OpenAI service ကို ပထမဆုံးအသုံးပြုနေပါက [Azure OpenAI Service resource ကို ဖန်တီးပြီး deploy လုပ်ရန်](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) ဤလမ်းညွှန်ချက်ကို လိုက်နာပါ။

## OpenAI API ကို ပထမဆုံးအသုံးပြုခြင်း

သင်သည် OpenAI API ကို ပထမဆုံးအသုံးပြုနေပါက [Interface ကို ဖန်တီးပြီး အသုံးပြုရန်](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) လမ်းညွှန်ချက်ကို လိုက်နာပါ။

## အခြားသော သင်ယူသူများနှင့် တွေ့ဆုံပါ

ကျွန်တော်တို့သည် အခြားသော သင်ယူသူများနှင့် တွေ့ဆုံရန် အတွက် ကျွန်တော်တို့၏ [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) တွင် channel များ ဖန်တီးထားသည်။ ၎င်းသည် Generative AI တွင် အဆင့်မြှင့်တင်ရန် ကြိုးစားနေသော လုပ်ငန်းရှင်များ၊ တည်ဆောက်သူများ၊ ကျောင်းသားများနှင့် စိတ်တူဆန်တူရှိသော မည်သူမဆိုနှင့် ကွန်ယက်ဖွဲ့စည်းရန် အလွန်ကောင်းသော နည်းလမ်းဖြစ်သည်။

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

စီမံကိန်းအဖွဲ့သည် သင်ယူသူများအား ကူညီရန် ဒီ Discord server ပေါ်တွင်လည်း ရှိနေပါမည်။

## ပါဝင်ဆောင်ရွက်ပါ

ဒီသင်ခန်းစာသည် open-source လှုပ်ရှားမှုဖြစ်သည်။ အဆင်ပြေမှုများ သို့မဟုတ် ပြဿနာများကို တွေ့မြင်ပါက [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) တစ်ခု ဖန်တီးပါ သို့မဟုတ် [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) ကို မှတ်တမ်းတင်ပါ။

စီမံကိန်းအဖွဲ့သည် အားလုံးသော ပါဝင်မှုများကို လမ်းကြောင်းမှန်မှန် လိုက်နာနေပါမည်။ open source တွင် ပါဝင်ဆောင်ရွက်ခြင်းသည် Generative AI တွင် သင်၏ career ကို တည်ဆောက်ရန် အံ့သြဖွယ်ကောင်းသော နည်းလမ်းဖြစ်သည်။

အများဆုံး ပါဝင်မှုများသည် Contributor License Agreement (CLA) ကို သဘောတူရန် လိုအပ်သည်၊ သင်သည် သင့်ပါဝင်မှုကို အသုံးပြုရန် ကျွန်တော်တို့အား အခွင့်အရေးများကို ပေးရန် လက်မှတ်ထိုးရန် တကယ်ပဲ လက်မှတ်ထိုးရန် လိုအပ်ပါသည်။ အသေးစိတ်အချက်အလက်များအတွက် [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ပါ။

အရေးကြီး: ဒီ repo အတွင်း text ကို ဘာသာပြန်ရာတွင် machine translation ကို မသုံးပါစေနဲ့။ ကျွန်တော်တို့သည် ဘာသာပြန်ချက်များကို community မှတဆင့် စစ်ဆေးပါမည်၊ ထို့ကြောင့် သင် proficient ဖြစ်သော ဘာသာစကားများတွင်သာ ဘာသာပြန်ရန် အကြံပြုပါ။

သင် pull request တင်သောအခါ CLA-bot သည် သင် CLA ပေးရန် လိုအပ်သလားနှင့် အလိုအလျောက် စစ်ဆေးပြီး PR ကို သင့်လျော်စွာ အလှဆင်ပါမည် (ဥပမာ- label, comment)။ bot ပေးသော လမ်းညွှန်ချက်များကို လိုက်နာပါ။ ကျွန်တော်တို့၏ CLA ကို အသုံးပြုသော repo အားလုံးတွင် သင်ဤလုပ်ဆောင်မှုကို တစ်ကြိမ်သာ လုပ်ရပါမည်။

ဒီစီမံကိန်းသည် [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) ကို လက်ခံထားပါသည်။ Code of Conduct FAQ ကို ဖတ်ရန် သို့မဟုတ် [Email opencode](opencode@microsoft.com) ကို အပိုဆောင်းမေးခွန်းများ သို့မဟုတ် မှတ်ချက်များနှင့်အတူ ဆက်သွယ်ရန် အချက်အလက်များကို ဖတ်ပါ။

## စတင်ပါ

ဒီသင်ခန်းစာကို ပြီးမြောက်ရန် လိုအပ်သော အဆင့်များကို ပြီးမြောက်ပြီးနောက်၊ [Generative AI နှင့် LLMs အကြောင်းကို မိတ်ဆက်ခြင်း](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) ဖြင့် စတင်ကြပါစို့။

**အာမခံချက်**:  
ဒီစာရွက်ကို AI ဘာသာပြန်ဆန့်ကျင်ရေးဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြုပြီး ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုကို ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းမှုများ ပါဝင်နိုင်သည်ကို သိရှိထားရန် ကျေးဇူးပြုပြီး သတိပြုပါ။ ဒေသတွင်းဘာသာစကားဖြင့်ရေးသားထားသော အစစ်အမှန်စာရွက်ကို အာဏာရှိသောရင်းမြစ်အဖြစ် ထည့်သွင်းစဉ်းစားသင့်သည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားယွင်းမှုများ သို့မဟုတ် ချက်လက်မှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။