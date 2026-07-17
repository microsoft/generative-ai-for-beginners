# ဒီသင်တန်းနဲ့ စတင်လိုက်ပါ

ဒီသင်တန်းကို စတင်ကြည့်ရှုဖို့အတွက် အရမ်းဝမ်းသာပါတယ် ဒီသင်တန်းမှ Generative AI နဲ့ ဘာကိုတည်ဆောက်ချင်တယ်ဆိုတာကို ကြည့်ရှု့ဖို့ဖြစ်ပါတယ်!

သင့်ရဲ့ အောင်မြင်မှုအတွက် ဒီစာမျက်နှာမှာ Setup လုပ်ရန် အဆင့်များ၊ နည်းပညာလိုအပ်ချက်များ၊ ပြဿနာဖြေရှင်းရန် ဘယ်မှာအကူအညီရနိုင်မလဲဆိုတာတွေကို ဖော်ပြထားပါတယ်။

## Setup အဆင့်များ

ဒီသင်တန်းကို စတင်ထည့်သွင်းရန်အတွက် အောက်ပါအဆင့်များကို ပြီးမြောက်ရန်လိုပါတယ်။

### 1. ဒီ Repo ကို Fork လုပ်ပါ

[ဒီ repo အားလုံးကို Fork လုပ်ပါ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ကိုယ်ပိုင် GitHub အကောင့်ထဲသို့ ကိုယ်စိတ်ကြိုက်ကုဒ်ပြင်ဆင်နိုင်ဖို့နှင့် စိန်ခေါ်မှုများကို ပြီးမြောက်ချက်လုပ်ဖို့။ သင်နိုင်ပါတယ် [ဒီ repo ကို star (🌟) လုပ်ပါ](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) မှာ ရှာဖွေရန်နှင့် ဆက်စပ် repo များကို အလွယ်တကူ ရှာဖွေရန်။

### 2. Codespace တစ်ခု ဖန်တီးပါ

ကုဒ်ကို chạy ဖို့ သမာဓိပြုရန် အားလုံး Run မှားမှုများ မဖြစ်စေရန် ဒီသင်တန်းကို [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) မှာ chạy ဖို့အကြံပြုပါတယ်။

ကိုယ်နှစ်သက် fork ထဲမှာ: **Code -> Codespaces -> New on main**

![Codespace ဖန်တီးဖို့ ညွှန်ပြတဲ့ Dialog](../../../translated_images/my/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Secret တစ်ခု ထည့်ပါ

1. ⚙️ ကိရိယာသင်္ကေတ -> Command Pallete-> Codespaces : Manage user secret -> Secret အသစ်ထည့်ပါ။
2. OpenAI_API_KEY အမည်ပေးပြီး ကိုယ့် key ကို ကူးထည့်၊ သိမ်းဆည်းပါ။

### 3. နောက်တစ်ဆင့်ဘာလုပ်မလဲ?

| ကျွန်ုပ်နှစ်သက်သည်…       | သွားရန်…                                                                  |
|---------------------------|-----------------------------------------------------------------------------|
| သင်ခန်းစာ 1 စတင်ရန်      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)           |
| အော့ဖ်လိုင်းလုပ်ရန်         | [`setup-local.md`](02-setup-local.md)                                       |
| LLM Provider တစ်ခု Setup လုပ်ရန် | [`providers.md`](03-providers.md)                                            |
| အခြားကျောင်းသူများ နှုတ်ဆက်ဖို့ | [ကျွန်တော်တို့ရဲ့ Discord ကို Join လုပ်ပါ](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)             |

## ပြဿနာဖြေရှင်းခြင်း


| ရောဂါလက္ခဏာ                         | ဖြေရှင်းချက်                                                             |
|--------------------------------------|-------------------------------------------------------------------------|
| Container တည်ဆောက်ခြင်း ၁၀ မိနစ် ကျော် ရပ်တနောက်               | **Codespaces ➜ “Rebuild Container”**                                  |
| `python: command not found`            | Terminal က မတွဲနေပါဘူး; **+** ကိုနှိပ်ပြီး *bash* ရွေးပါ                   |
| OpenAI မှ `401 Unauthorized` error      | မှားသည့် / ကုန်ဆုံးသွားသော `OPENAI_API_KEY`                              |
| VS Code မှ “Dev container mounting...” ပြတယ်   | Browser tab ကို ပြန် Refresh လုပ်ပါ—Codespaces သည် connection ပျောက်သွားတတ်သည်      |
| Notebook kernel မရှိပါ                       | Notebook မီနူး ➜ **Kernel ▸ Select Kernel ▸ Python 3**                  |

   Unix-based စနစ်များအတွက်:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` ဖိုင်ကို ပြင်ဆင်ပါ**: `.env` ဖိုင်ကို စာသားတည်းဖြတ်စက် (ဥပမာ - VS Code, Notepad++, သို့မဟုတ် တခြားတည်းဖြတ်စက်) ဖြင့် ဖွင့်ပါ။ တန်းတူ Microsoft Foundry Models endpoint နှင့် key (ရယူနည်းအတွက် [`providers.md`](03-providers.md) ကိုကြည့်ပါ) များကို ထည့်သွင်းပြီး အောက်ပါလိုင်းများထည့်ပါ။

   > **မှတ်ချက်:** GitHub Models (နှင့် ၎င်းရဲ့ `GITHUB_TOKEN` variable) ကို ၂၀၂၆ ခုနှစ် ဇူလိုင်လကုန်တွင် ပိတ်သိမ်းမည်ဖြစ်သည်။ အစားအစာအဖြစ် [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ကို သုံးပါ။

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **ဖိုင်ကို သိမ်းပါ**: ပြင်ဆင်မှုများကို သိမ်းပြီး စာသားတည်းဖြတ်စက်ကိုပိတ်ပါ။

5. **`python-dotenv` ကို တပ်ဆင်ပါ**: မတပ်ဆင်ထားပါက `.env` ဖိုင်မှ ပတ်ဝန်းကျင် များကို Python အပလီကေးရှင်းထဲသို့ ကြိုတင် load လုပ်ရန် `python-dotenv` ပက်ကေ့ဂျ်ကို တပ်ဆင်ရန်လိုမယ်။ သင် `pip` ဖြင့် တပ်ဆင်နိုင်ပါတယ်။

   ```bash
   pip install python-dotenv
   ```

6. **Python script ထဲမှာ ပတ်ဝန်းကျင် များကို load လုပ်ပါ**: Python script ထဲမှာ `python-dotenv` package ကို အသုံးပြုပြီး `.env` ဖိုင်မှ ပတ်ဝန်းကျင် များကို load လုပ်ပါ။

   ```python
   from dotenv import load_dotenv
   import os

   # .env ဖိုင်မှ ပတ်ဝန်းကျင်အပြောင်းအလဲများကို ဖတ်ယူမည်
   load_dotenv()

   # Microsoft Foundry Models အပြောင်းအလဲများကို 접근မည်
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

အဲ့ဒါဆိုပြီးပါပြီ! သင် .env ဖိုင်တစ်ခုကို အောင်မြင်စွာ ဖန်တီးပြီး Microsoft Foundry Models မ်ားအတွက် ထိုးထည့်ချက်များကို ထည့်သွင်းပြီး Python အပလီကေးရှင်းထဲ load လုပ်နိုင်ပါပြီ။

## ကိုယ့်ကွန်ပျူတာမှာ locally လည်ပတ်စေဖို့

ကွန်ပျူတာမှာ locally ကုဒ်ကို လည်ပတ်ရန် Python တစ်ခုခု ရှိဖို့လိုပါတယ်။ [Python ကို 설치](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) လုပ်ထားဖို့လိုအပ်ပါသည်။

အဲ့ဒီနောက် repository ကို clone လုပ်ဖို့လိုပါသည်။

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

အားလုံးစစ်ဆေးပြီး သင်ဝင်ကြည့်နိုင်ပါပြီ!

## ရွေးချယ်လိုဖြစ်စေသော အဆင့်များ

### Miniconda တပ်ဆင်ခြင်း

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) သည် [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python နှင့် တခြား ပက်ကေ့ဂျ်အနည်းငယ်များ တပ်ဆင်ရန် အလင်းချိန် အင်စတော်လာ ဖြစ်ပါတယ်။
Conda က ပက်ကေ့ဂျ် မန်နေဂျာတစ်ခုဖြစ်ပြီး Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) များနဲ့ ပက်ကေ့ဂျ်များကို ဖွဲ့စည်းပြောင်းလဲရန် အရမ်းလွယ်ကူစေပါတယ်။ ဒါ့အပြင် pip ဖြင့် မရနိုင်တဲ့ packages များကို တပ်ဆင်ရာတွင်လည်း အထောက်အကူပြုပါတယ်။

[MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ကို နည်းလမ်းလိုက်ပြီး တပ်ဆင်နိုင်ပါတယ်။

Miniconda တပ်ဆင်ပြီးရင် [repository ကို clone ထပ်လျှင်](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (မလုပ်ရသေးပါက)

နောက်တစ်ဆင့် virtual environment တစ်ခု ဖန်တီးရန်လိုမယ်။ Conda ဖြင့် အဲ့ဒါလုပ်ရန်တော့ environment ဖိုင် များ (_environment.yml_) ဖန်တီးပါ။ Codespaces ကို အသုံးပြုနေပါက `.devcontainer` ဖိုလ်ဒါအတွင်း `.devcontainer/environment.yml` မှာ ထည့်ပြုလုပ်ပါ။

အောက်ပါ snippet ဖြင့် environment ဖိုင်ကို ဖြည့်ပေးပါ။

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

Conda အသုံးပြုရာတွင် အမှားတွေ ကြားရင် Microsoft AI Libraries ကို terminal ထဲမှာ အောက်ပါ command ဖြင့် စာရင်းသွင်းနိုင်သည်။

```
conda install -c microsoft azure-ai-ml
```

အဲ့ဒီ environment ဖိုင်မှာ လိုအပ်ချက်တွေ အပ်နှံထားပြီး `<environment-name>` ဆိုတာ သင် အသုံးပြုလိုသော Conda environment အမည်ဖြစ်ပြီး `<python-version>` က သင် သုံးလိုသော Python ဗားရှင်း ဖြစ်သည်၊ ဥပမာ `3` သည်ล่าสุด Python များ၏ Major version ဖြစ်သည်။

အဲ့ဒါလုပ်ပြီးရင် command line/terminal ထဲမှာ အောက်ပါ command ကို ဖြင့် Conda environment ဖန်တီးနိုင်ပါသည်။

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer အောက်မယ်ဖြစ်သော လမ်းကြောင်းကို Codespace တပ်ဆင်မှုများတွင်သာ သက်ရောက်သည်။
conda activate ai4beg
```

[Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ကို ပြဿနာတွေဖြစ်ရင် ရှာဖွေနိုင်ပါတယ်။

### Visual Studio Code ကို Python support extension နဲ့ သုံးခြင်း

ဒီသင်တန်းအတွက် [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor ကို [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ပါ တပ်ဆင်ပြီး သုံးနိုင်ဖို့ အကြံပြုပါတယ်။ ဒါပေမဲ့ ဤဟာ တပ်ဆင်ရန်ဆိုတာ တစ်ခုအကြံပြုချက်ဖြစ်ပြီး အတည်ပြုလိုက်ဘက်မဟုတ်ပါ။

> **မှတ်ချက်**: သင်တန်း repository ကို VS Code မှာဖွင့်လိုက်တဲ့အခါ project ကို container အတွင်း သတ်မှတ်ဖို့ အခွင့်အရေး ရပါတယ်။ ဒီဟာက သင်တန်း repo အတွင်းရှိ [အထူး `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ဖိုလ်ဒါကြောင့်ဖြစ်ပါတယ်။ နောက်ပိုင်းမှာ ဒါအကြောင်းပိုပြောပါမယ်။

> **မှတ်ချက်**: သင် clone လုပ်ပြီး VS Code မှာ directory ဖွင့်လို့ရပြီဆို Python support extension တပ်ဆင်ဖို့ အလိုအလျောက် အကြံပြုပါလိမ့်မယ်။

> **မှတ်ချက်**: VS Code က repo ကို container အတွင်း ပြန်ဖွင့်ဖို့ အကြံပြုပြီဆိုထားရင် ဒါကို ငြင်းဆိုပြီး လက်ရှိ locally တပ်ဆင်ထားတဲ့ Python ထည့်သုံးဖို့ သတိပြုပါ။

### Browser အတွင်း Jupyter သုံးခြင်း

Project ကို browser အတွင်း [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) သုံးပြီးလည်း အလုပ်လုပ်နိုင်တယ်။ classic Jupyter နှင့် [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) တွေက အော်တိုပြီးခွဲခြမ်းမှု၊ ကုဒ် highlight စတဲ့ features တွေနဲ့ စိတ်ချမ်းသာစရာ တိုးတက်မှုကောင်းပါတယ်။

Jupyter ကို locally start လုပ်ရန် terminal/command line မှာ သင်တန်း directory ကိုသွားပြီး အောက်က command ကို run ပါ။

```bash
jupyter notebook
```

or

```bash
jupyterhub
```

ဒီဟာက Jupyter instance တစ်ခု စတင်ဖြင့်ပေးပြီး ဝင်ရောက်ရန် URL ကို command line window ထဲမှာ ပြပါလိမ့်မယ်။

URL ကို ဝင်ရောက်ပြီးသွားသည်နှင့် သင်တန်း အကြောင်းအရာကို တွေ့နိုင်ပြီး `*.ipynb` ဖိုင်များပြုလုပ်နိုင်ပါသည်။ ဥပမာ `08-building-search-applications/python/oai-solution.ipynb` ကို run နိုင်ပါတယ်။

### Container အတွင်း Run ချင်

ကိုယ့်ကွန်ပျူတာမှာ သို့မဟုတ် Codespace မှာ တစ်ခုချင်းစီ setup လုပ်ရန် အစား [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) တစ်ခု သုံးနိုင်ပါတယ်။ သင်တန်း repo အတွင်း အထူး `.devcontainer` ဖိုလ်ဒါကြောင့် VS Code သည် container အတွင်း project သက်ဆိုင် setup လုပ်နိုင်ပါတယ်။ Codespaces မဟုတ်တဲ့အခါ Docker တပ်ဆင်ရမယ်။ အနေအထားကို လုပ်ကိုင်ရင်းနည်းနည်းရှုပ်တတ်လို့ container နှင့်အတွေ့အကြုံရှိသူတွေလည်းသာ အကြံပြုပါတယ်။

GitHub Codespaces အသုံးပြုမှုတွင် API keys များကို မနက်မဲထားရန်အတွက် Codespace Secrets ကိုအသုံးပြုရတာထိပ်ဆုံးနည်းလမ်း ဖြစ်ပါတယ်။ ဒီအကြောင်းအရာကို သေချာ သေချာနားလည်ဖို့ [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) လမ်းညွှန်ကို နှစ်သက်စွာ လိုက်နာပါ။


## သင်ခန်းစာများနှင့် နည်းပညာလိုအပ်ချက်များ

သင်တန်းတွင် Generative AI အကြောင်းများကို ရှင်းပြသည့် "Learn" သင်ခန်းစာများနှင့် လက်တွေ့ကုတ်နမူနာပါရှိသည့် **Python** နှင့် **TypeScript** ဘာသာစကားများဖြင့် "Build" သင်ခန်းစာများ ပါဝင်သည်။

ကုတ်ရေးရာသင်ခန်းစာများအတွက် Microsoft Foundry တွင် Azure OpenAI ကို အသုံးပြုပါတယ်။ Azure subscription နဲ့ API key လိုအပ်ပါသည်။ ဝင်ရောက်ခွင့်ပိတ်ထားမှုမရှိ၊ လျ်သောမတောင်းဆိုဘဲ [Microsoft Foundry resource တစ်ခု ဖန်တီးပြီး model တင်ပါ](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) API endpoint နှင့် key ကိုရယူနိုင်ပါတယ်။

အားလုံး coding သင်ခန်းစာများမှာ ကိုယ် run မလုပ်ဘဲ ကုဒ်နဲ့ output တွေကို ကြည့်ရှုနိုင်တဲ့ `README.md` ဖိုင်လည်း ပါဝင်ပါတယ်။

## Azure OpenAI ဝန်ဆောင်မှုကို ပထမဆုံး အသုံးပြုခြင်း

Azure OpenAI ဝန်ဆောင်မှုနှင့် ပထမဆုံးအကြိမ် အလုပ်လုပ်သူများအတွက် ဒီလမ်းညွှန်ကို လိုက်နာပါ [Azure OpenAI Service resource ဖန်တီးပုံ](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)။

## OpenAI API ကို ပထမဆုံး အသုံးပြုခြင်း

OpenAI API ကို ပထမဆုံးအကြိမ်အသုံးပြုသူများအတွက် ဒီလမ်းညွှန်ကို လိုက်နာပါ [Interface ဖန်တီးပုံနှင့် အသုံးပြုနည်း](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)။

## အခြားကျောင်းသားတွေနဲ့ တွေ့ဆုံခြင်း

ကျောင်းသားတွေကို တွေ့ဆုံဖို့အတွက် ကျွန်ုပ်တို့ရဲ့ တရားဝင် [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) မှာ channel များ ဖန်တီးထားပါတယ်။ ဒီနေရာမှာ ထက်မြတ်သော စက္ကန့်စုတော်များ၊ ဆောက်လုပ်သူများ၊ ကျောင်းသားများ နှင့် Generative AI တွင် အဆင့်တက်လိုသူ တွေနဲ့ ကောင်းမွန်တဲ့ ကွန်ယက်တည်ဆောက်နိုင်ပါတယ်။

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

ဒီ project အဖွဲ့ဝင်များသည်လည်း ဒီ Discord server ထဲမှာ ကျောင်းသားများအား အကူအညီပေးရန် ရှိနေပါသည်။

## တစ်ဆက်လက် ထောက်ပံ့ရန်

ဒီသင်တန်းမှာ အဖွဲ့အစည်းဖြစ်ပြီး အခမဲ့စေ့စပ်စွာ အသုံးပြုနိုင်ပါတယ်။ တိုးတက်မှု ဒါမှမဟုတ် ပြဿနာတွေတွေ့ရင် [Pull Request တင်ပါ](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) သို့မဟုတ် [GitHub issue တစ်ခု တင်ပါ](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)။

Project အဖွဲ့သည် အားလုံးရဲ့ ပံ့ပိုးမှုများကို စောင့်ကြည့်မည်ဖြစ်သည်။ Open source ခြေရာ့မှုက Generative AI ထဲတွင် သင့်အလုပ်အကိုင် တိုးတက်မှုအတွက် မဟာထူးကောင်းသော နည်းလမ်းတစ်ခုဖြစ်သည်။

များစုသော ပံ့ပိုးမှုများအတွက် Contributor License Agreement (CLA) ကို သဘောတူရန် လိုအပ်ပြီး သင့်ပံ့ပိုးမှုကို အသုံးပြုခွင့် ကျွန်ုပ်တို့ကို ချမှတ်ပေးသည်ကို ထောက်ခံရမည် ဖြစ်သည်။ အသေးစိတ်အချက်အလက်များအတွက် [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) ကို သွားရောက်ကြည့်ရှုပါ။

အရေးကြီးချက်: ဒီ repo ထဲမှာ စာများကို ဘာသာပြန်ရာတွင် မျှော်လင့်ချက်ထားသော ကြားဖြတ်ဘာသာပြန်ခြင်း မလုပ်သင့်ပါ။ များစွာသောဘာသာပြန်မူများကို လုပ်ငန်းအသိုင်းအဝိုင်းမှ စစ်ဆေးမည်ဖြစ်ပြီး သင် အကျွမ်းတဝင်ငံအတွက်သာ ဘာသာပြန်မှုအတွက် ပါဝင်ပါ။


သင် pull request တင်သောအခါ၊ CLA-bot သည် သင် CLA ပေးအပ်ရန် လိုအပ်သည်ဟုကိုယ်တိုင် ဆုံးဖြတ်ပြီး PR အတွက် သင့်တော်သလို အမှတ်အသား (ဥပမာ၊ label, comment) ပေးပါလိမ့်မည်။ bot မှ ပေးထားသော အညွှန်းများကိုသာ လိုက်နာဆောင်ရွက် ပါ။ ဤအရာကို ကျွန်ုပ်တို့၏ CLA ကို အသုံးပြုသော ပေါင်းစပ်ထားသော repository များတွင် တစ်ကြိမ်တည်းသာ လုပ်ဆောင်ရပါမည်။

ဤပရောဂျက်သည် [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) ကို လက်ခံလိုက်ပါသည်။ ပိုမိုသိရှိလိုပါက Code of Conduct FAQ ကို ဖတ်ပါ သို့မဟုတ် ဘယ်မေးလ် [Email opencode](opencode@microsoft.com) ကိုဆက်သွယ်မေးမြန်းနိုင်ပါသည်။

## စတင်လိုက်စို့

ယခု သင်သည် ဒီသင်တန်းကို ပြီးမြောက်ရန်လိုအပ်သည့် အဆင့်များ ပြီးမြောက်သွားပါပြီ၊ ဒါဆို [Generative AI နှင့် LLM များအကြောင်း နမူနာများ](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) ရယူခြင်းဖြင့် စတင်လိုက်ရအောင်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->