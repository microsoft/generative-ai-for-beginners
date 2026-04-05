# ဒီသင်တန်းနဲ့ စတင်လိုက်ပါ

ဒီသင်တန်းကို စတင်ကြည့်ရှုပြီး Generative AI နဲ့ ဘာတွေဖန်တီးဖို့ စိတ်အားထက်သန်လာမလဲဆိုတာ ကြည့်ရတာ ကျွန်တော်တို့အတွက် အရမ်းဝမ်းသာပါတယ်!

သင်ကြားမှု အောင်မြင်စေရန် ဒီစာမျက်နှာမှာ အဆင့်ဆင့်ပြုပြင်ထောက်ပံ့မှု လိုအပ်ချက်တွေ၊ နည်းပညာဆိုင်ရာ လိုအပ်ချက်တွေ၊ လိုအပ်ရင် ကူညီပေးနိုင်မယ့် နေရာတွေကို ရှင်းလင်းဖော်ပြထားပါတယ်။

## ပြင်ဆင်လုပ်ဆောင်ရမည့်အဆင့်များ

ဒီသင်တန်းကို စတင်ယူမယ့်အခါ အောက်ပါအဆင့်တွေကို ပြီးမြောက်စေရပါမယ်။

### 1. ဒီ Repo ကို Fork လုပ်ပါ

[ဒီ repo အားလုံးကို Fork လုပ်ပါ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) သင့်ရဲ့ GitHub အကောင့်မှာ၊ ကွန်ရက်ကုဒ်များပြောင်းလဲနိုင်ဖို့နှင့် စိန်ခေါ်မှုများကို ပြီးမြောက်စေရန်။ သင်ကြိုက်လျှင် [ဒီ repo ကို ⭐ star လုပ်ပါ](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)၊ ဒါနဲ့ ဆက်စပ် repo တွေကိုလည်း ရှာဖွေရှူရှာဖို့ ပိုလွယ်ကူပါလိမ့်မယ်။

### 2.  Codespace တစ်ခု ဖန်တီးပါ

ကုဒ် run တဲ့အချိန်မှာ dependency ပြဿနာမဖြစ်အောင် ဒီသင်တန်းကို [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) မှာ သုံးဖို့ အကြံပြုပါတယ်။

သင့်fork အတွင်း: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/my/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Secret တစ်ခု ထည့်ပါ

1. ⚙️ သားငယ်ပုံသဏ္ဌာန် နဲ့ Gear icon -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret။
2. အမည် OPENAI_API_KEY ထည့်ပြီး သင့် key ကို paste လုပ်ပါ။ Save လုပ်ပါ။

### 3. နောက်တစ်ခုဘာလဲ?

| ဘာလုပ်ချင်လဲ           | သွားရမယ့်နေရာ                                                        |
|-------------------------|------------------------------------------------------------------------|
| Lesson 1 စတင်လိုက်ပါ     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Offline အလုပ်လုပ်ချင်     | [`setup-local.md`](02-setup-local.md)                                  |
| LLM Provider တစ်ခု ဖန်တီးချင် | [`providers.md`](03-providers.md)                                       |
| အခြားလေ့လာသူတွေနဲ့တွေ့ချင် | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)       |

## ပြဿနာဖြေရှင်းခြင်း


| ပြဿနာလက္ခဏာ                            | ဖြေရှင်းနည်း                                                       |
|------------------------------------------|------------------------------------------------------------------|
| Container build တစ်ခု ၁၀ မိနစ်ကျော် ရပ်တန့်နေခြင်း | **Codespaces ➜ “Rebuild Container”**                             |
| `python: command not found`               | Terminal မပူးပေါင်းထားဝါ့ထား; **+** ကိုနှိပ်ပြီး *bash* ရွေးပါ   |
| OpenAI ကနေ `401 Unauthorized` error     | မှားနေသော / သက်တမ်းကုန် `OPENAI_API_KEY`                        |
| VS Code မှာ “Dev container mounting…” ပြနေခြင်း   | Browser tab ကို Refresh လုပ်ပါ—Codespaces တခါတရံ ချိတ်ဆက်မှု ပျောက်ကွက်နိုင်တယ်  |
| Notebook kernel မရှိခြင်း                | Notebook menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**              |

   Unix-based စနစ်များအတွက်:

   ```bash
   touch .env
   ```

   Windows အတွက်:

   ```cmd
   echo . > .env
   ```

3. **`.env` ဖိုင်ကို ပြုပြင်ချင်သလား**: `.env` ဖိုင်ကို VS Code, Notepad++, ဒါမှမဟုတ် အခြားတစ်ခုခု text editor ဖြင့်ဖွင့်ပါ။ “your_github_token_here” ကို သင့် GitHub token နဲ့ အစားထိုးပြီး အောက်ပါစာကြောင်းကို ထည့်ပါ။

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **ဖိုင်ကို သိမ်းပါ**: ပြင်ဆင်မှုများ သိမ်းပြီး text editor ကို ပိတ်ပါ။

5. **`python-dotenv` ကို install လုပ်ပါ**: သင်မပြုလုပ်ထားပါက `.env` ဖိုင်မှာရှိတဲ့ environment variables ကို Python application ထဲသို့ သွင်းဖို့ `python-dotenv` package ကို `pip` နဲ့ install လုပ်ရန် လိုအပ်ပါသည်။

   ```bash
   pip install python-dotenv
   ```

6. **Python script ထဲမှာ Environment Variables ကို load လုပ်ပါ**: Python script မှာ `python-dotenv` package ကိုအသုံးပြုပြီး `.env` ဖိုင်မှ variables များကို load လုပ်ပါ။

   ```python
   from dotenv import load_dotenv
   import os

   # .env ဖိုင်ထဲကနေ ပတ်ဝန်းကျင် အလွှာများကို ဖတ်သည်
   load_dotenv()

   # GITHUB_TOKEN အလွှာကို လက်လှမ်းရောက်စေသည်
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

ဒါဆိုပြီးပါပြီ! `.env` ဖိုင်ကိုအောင်မြင်စွာ ဖန်တီးပြီး၊ GitHub token ထည့်ပြီး Python application ထဲသို့ load လုပ်ထားပါပြီ။

## ကိုယ်ပိုင် ကွန်ပျူတာမှာ run မယ်ဆိုရင်

ကိုယ်ပိုင်ကွန်ပျူတာမှာ အဲဒီကုဒ်ကို run လုပ်ချင်ရင် [Python ရှိဖို့လိုပါမယ်](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)။

အဲဒီပြီးရင် repo ကို clone ချပါ။

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

အားလုံး စစ်ဆေးပြီးတဲ့နောက် စတင်လုပ်ဆောင်နိုင်ပါပြီ!

## ရွေးချယ်စရာအဆင့်များ

### Miniconda 설치하기

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) သည် [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)၊ Python နှင့် အခြား package များကို ထည့်သွင်းဖို့ အလေးချိန်လျှော့ installer တစ်ခုဖြစ်ပါတယ်။ Conda သည် package manager တစ်ခု ဖြစ်ပြီး Python တွင် [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) နှင့် package များကို လွယ်ကူစွာ စီမံရန် အသုံးပြုသည့်စနစ်ဖြစ်ပါသည်။ pip မှာမရရှိနိုင်တဲ့ package များကို အထူးအဆင်ပြေစေပါတယ်။

[MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ကို လိုက်နာပြီး အဆင့်ဆင့် ပြုလုပ်နိုင်ပါတယ်။

Miniconda ထည့်သွင်းပြီးနောက်၊ သင် cloned repository ရှိပြီးသား မဟုတ်ရင် [repository ကို clone လုပ်ပါ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)။

နောက်တစ်ဆင့်မှာ virtual environment ဖန်တီးပါ။ Conda နဲ့ချိတ်ဆက်ဖို့ environment file (_environment.yml_) အသစ် ဖန်တီးပါ။ Codespaces သုံးနေကြတဲ့အခါ `.devcontainer` ဖိုလ်ဒါထဲမှာ, ဒါမှမဟုတ် `.devcontainer/environment.yml` လို့ ဖိုင်ထဲမှာ ပြုလုပ်ပါ။

အောက်ပါ code snippet နဲ့ environment file ကို ဖြည့်ပါ:

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

conda သုံးစဉ် error တွေ ကြုံရင် terminal မှာ အောက်ပါ command ဖြင့် Microsoft AI Libraries ကို manually install လုပ်နိုင်ပါတယ်။

```
conda install -c microsoft azure-ai-ml
```

Environment file မှာ ကျွန်တော်တို့ အလိုအလျောက်လိုအပ်နေတဲ့ dependencies တွေ ဖော်ပြထားပါတယ်။ `<environment-name>` က သင် Conda environment အတွက် သတ်မှတ်ချင်တဲ့ အမည်ဖြစ်ပြီး `<python-version>` က သင်သုံးချင်တဲ့ Python ဗားရှင်းဖြစ်သည်။ ဥပမာအားဖြင့် `3` က Python နောက်ဆုံး major version ဖြစ်ပါတယ်။

ပြီးဆုံးရင် command line/terminal မှာ အောက်ပါ commands ဖြင့် Conda environment ကို ဖန်တီးလိုက်ပါ။

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer ရဲ့ သေးငယ်တဲ့ လမ်းကြောင်းက Codespace ပြင်ဆင်မှုတွေ အတွက်သာ ဖြစ်ပါတယ်။
conda activate ai4beg
```

ပြဿနာတွေရှိရင် [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ကို ကိုးကားပါ။

### Visual Studio Code ကို Python extension နဲ့သုံးခြင်း

ဒီသင်တန်းအတွက် [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) နဲ့ [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ကို အသုံးပြုဖို့ အကြံပြုပါတယ်။ ဒါပေမယ့် ဤအကြံပြုချက်က တစ်ခုတည်းသောလိုအပ်ချက်မဟုတ်ပါ။

> **မှတ်ချက်**: သင်သင်တန်း repo ကို VS Code ပါ ထည့်လိုက်ရင် ဒီ project ကို container အတွင်းမှာ setup လုပ်ဖို့ ရွေးချယ်နိုင်ပါတယ်။ ဒါဟာ repo ထဲမှာ ရှိတဲ့ [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ပထမဦးဆုံး folder များကြောင့် ဖြစ်ပါတယ်။ နောက်ပိုင်း ဆက်လက်ရှင်းပြပါမယ်။

> **မှတ်ချက်**: Repo ကို clone လုပ်ပြီး VS Code နဲ့ ဖွင့်တဲ့အခါ Python support extension ထည့်ရန် အလိုအလျောက် အကြံပြုပါလိမ့်မယ်။

> **မှတ်ချက်**: VS Code က repo ကို container ထဲ ထပ်ဖွင့်ဖို့ အကြံပြုရင် ဒါကို မလိုလားဘဲ ပြတ်စဲပြီး locally installed Python ကို သုံးပါ။

### Browser ထဲမှာ Jupyter သုံးခြင်း

သင်တန်းကို ဘရောက်ဇာမှတဆင့် [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) သုံးပြီးလည်း development လုပ်နိုင်ပါတယ်။ Classic Jupyter နဲ့ [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) နှစ်မျိုးလုံး auto-completion၊ code highlight စတာတွေ ပါဝင်တဲ့ တွန်းအားကောင်းတဲ့ဘက်ဒ်စတိုင်ပလက်ဖောင်းများ ဖြစ်ပါတယ်။

အိမ်စောင့် Jupyter စတင်ဖို့ terminal/command line ကိုဖွင့်ပြီး သင်တန်း directory ကို သွားပါ၊ နောက် ထည့်သွင်းချင်သည့် command ကို run ပါ။

```bash
jupyter notebook
```

သို့မဟုတ်

```bash
jupyterhub
```

ဒါက Jupyter instance ကို စတင်ပြီး URL ကို command line ပေါ်မှာ ပြပါလိမ့်မယ်။

URL ကို ဝင်ရောက်ပြီးနောက် သင်တန်း၊ ကိုယ်လို လိုင်း `*.ipynb` ဖိုင်တွေကို ရွှေ့နိုင်ပါပြီ။ ဥပမာ `08-building-search-applications/python/oai-solution.ipynb` ဟာပါ။

### Container တစ်ခုထဲမှာ အလုပ်လုပ်ခြင်း

ကိုယ်ပိုင်ကွန်ပျူတာမှာ သို့မဟုတ် Codespace မှာ စီစဉ်ဖွဲ့စည်းဖို့ အစား [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) သုံးနိုင်ပါတယ်။ သင်တန်း repo ထဲရှိ `.devcontainer` ဖိုလ်ဒါကြောင့် VS Code မှာ project ကို container အတွင်းမှာ setup လုပ်ဖို့ ခွင့်ရှိပါတယ်။ Codespaces မဟုတ်တဲ့ အခြေအနေမှာ Docker install လုပ်ရပါမည်။ ဒါကြောင့် container နဲ့ အတွေ့အကြုံရှိသူများအတွက်သာ အကြံပြုပါတယ်။

GitHub Codespaces သုံးတဲ့အခါ API key တွေ လုံခြုံစေရန်အတွက် Codespace Secrets ကို သုံးဖို့ အကောင်းဆုံးနည်းလမ်းဖြစ်ပါတယ်။ [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) လမ်းညွှန်ကို လိုက်နာပါ။

## သင်ခန်းစာများနှင့် နည်းပညာလိုအပ်ချက်များ

ဒီသင်တန်းမှာ သိပ္ပံအခြေခံ 6 ခုနဲ့ ကွန်ပျူတာရေးသင်ခန်းစာ 6 ခုပါဝင်ပါတယ်။

Coding သင်ခန်းစာများအတွက် Azure OpenAI Service ကို အသုံးပြုထားပါတယ်။ ဒီကုဒ်ကို run ဖို့ Azure OpenAI service ရယူထားပြီး API key လိုအပ်ပါမယ်။ [ဒီဖောင်ကို ဖြည့်ပြီး လျှောက်ထားနိုင်ပါတယ်](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)။

လျှောက်ထားချက်ကို စောင့်ဆိုင်းစဉ် Coding သင်ခန်းစာတစ်ခုချင်းစီမှာ `README.md` ဖိုင် ပါဝင်ပြီး ကုဒ်နဲ့ ထွက်ရှိချက်ကို ကြည့်ရှုနိုင်ပါတယ်။

## Azure OpenAI Service ကို ပထမဆုံးသုံးစရာ

Azure OpenAI service ကို ပထမဆုံး သုံးစရာဖြစ်ရင် [Azure OpenAI Service resource ဖန်တီးနည်းနဲ့ အသုံးပြုနည်း](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) လမ်းညွှန်ကိုလိုက်နာပါ။

## OpenAI API ကို ပထမဆုံးသုံးစရာ

OpenAI API ပထမဆုံး သုံးမယ်ဆိုရင် [API ဖန်တီးနည်းနဲ့အသုံးပြုနည်း](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) လမ်းညွှန်လိုက်နာပါ။

## အခြားလေ့လာသူတွေနဲ့တွေ့ဆုံခြင်း

ကျွန်တော်တို့ရဲ့ [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) မှာလေ့လာသူတွေ ဆက်ဆံဖို့ ချန်နယ်တွေဖွင့်ထားပါတယ်။ ဒီမှာ ကိုယ့်လိုပဲ စိတ်ဝင်စားသူများ၊ စိတ်အားထက်သန်သူများ၊ ကျောင်းသား၊ စီးပွားရေးရှင်၊ နည်းပညာရှင်တွေနဲ့ ဆက်သွယ်ပြီး Generative AI ထိပ်တန်းအတတ်ပညာကောင်းဖို့ ချိတ်ဆက်ရန် အကောင်းဆုံးနေရာပါ။

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

ဒီ Discord server မှာ လေ့လာသူတွေကူညီရန် project အဖွဲ့သားများလည်း ရှိပါသည်။

## အတူတူလုပ်ဆောင်ကြမယ်

ဒီသင်တန်းကို open-source စရိတ်ဖြစ်ပါတယ်။ တိုးတက်အောင်မြင်ဖို့၊ ပြဿနာတွေရှိရင် [Pull Request တင်ပါ](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) သို့မဟုတ် [GitHub issue log လုပ်ပါ](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)။

Project အဖွဲ့က ဆက်လက်ကြိုတင်စောင့်ကြည့်မယ်။ Open source သုံးစွဲခြင်းက Generative AI ရဲ့ လုပ်ငန်းခွင်မှာ ကြီးမားတဲ့ အခွင့်အလမ်းတစ်ခုဖြစ်ပါတယ်။

အများစုသော အထောက်အထားများမှာ Contributor License Agreement (CLA) သို့လက်ခံပါရန် သတ်မှတ်ထားပြီး၊ သင်၏ အထောက်အထားအသုံးပြုခွင့်ရှိကြောင်းကြေညာရမည် ဖြစ်သည်။ ပိုမိုသိရှိလိုပါက [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) ကို သွားရောက် ဖတ်ရှုနိုင်ပါသည်။

အရေးကြီးချက်- ဘာသာပြန်ခြင်းအတွက် အင်္ဂါရပ်တွင် မော်တော်ဖြင့်ဘာသာပြန်မှု (machine translation) မသုံးရပါ။ ကျွန်တော်တို့အဖွဲ့မှာ ဘာသာပြန်မှုများကို ပြည်သူများမှ သုံးသပ်စစ်ဆေးမည် ဖြစ်သောကြောင့် သင့်ဘာသာစကားကို ပြည့်စုံကျွမ်းကျင်စွာအသုံးပြုနိုင်သူများသာ တာဝန်ယူပါ။ 

pull request တင်တဲ့အခါ CLA-bot က သင် CLA ယူရန် လိုအပ်မလား စစ်ဆေးပြီး, သင့် PR ကို label, comment ဖြစ်စေခြင်းများ ပြုလုပ်ပါမည်။ bot ၏အညွှန်း လိုက်နာရန် လိုအပ်သည်။ Repo တစ်ခုလုံးတွင် ရှိသော CLA တစ်ခုချင်း စိစစ်မှုကို တစ်ကြိမ်တည်းသာ ပြုလုပ်ပါမည်။

ဒီ project မှာ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) ကို လိုက်နာပါသည်။ အသေးစိတ်သိရှိလိုပါက Code of Conduct FAQ ကိုဖတ်ရှုပါ၊ ဒါမှမဟုတ် ပိုမိုမေးမြန်းလိုပါက [Email opencode](opencode@microsoft.com) ဆီ ဆက်သွယ်စုံစမ်းနိုင်ပါသည်။

## စတင်ကြ ပါစို့!
ယခု သင်သည် ဤသင်တန်းကို ပြီးမြောက်အောင် လိုအပ်သည့် အဆင့်များကို ပြီးမြောက်ခဲ့ပါပြီ။ ယခု မှ [Generative AI နှင့် LLMs အတွက် မိတ်ဆက်](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) ကို ရယူကာ စတင်လိုက်ကြပါစို့။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အချိုးအစားချုပ်ချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားခြင်းဖြစ်ပါသည်။ တိကျမှုရှိစေရန် ကြိုးစားသော်လည်း ကွန်ပျူတာဖြင့် အလိုအလျောက် ဘာသာပြန်မှုတွင် အမှားများ သို့မဟုတ် တိကျမှုမရှိမှုများ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် အသိပေးလိုပါသည်။ မူလစာတမ်းကို မိခင်ဘာသာဖြင့်သာ တရားဝင်အစွန်းအထင်း အခန်းကဏ္ဍအဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှု အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများ သို့မဟုတ် အနားမလွတ်သတ်ချက်များအတွက် ကျနော်တို့ တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->