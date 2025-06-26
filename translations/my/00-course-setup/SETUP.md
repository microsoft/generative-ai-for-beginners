<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:32:37+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "my"
}
-->
# သင့် Dev ပတ်ဝန်းကျင်ကို တပ်ဆင်ပါ

Python3, .NET, Node.js နှင့် Java အတွက် ဖွံ့ဖြိုးရေးကို ပံ့ပိုးပေးနိုင်သည့် Universal runtime ပါသော [ဖွံ့ဖြိုးရေးကွန်တိန်နာ](https://containers.dev?WT.mc_id=academic-105485-koreyst) ဖြင့် ဤ repository နှင့် သင်ခန်းစာကို ကျွန်ုပ်တို့ တပ်ဆင်ထားပါသည်။ သက်ဆိုင်ရာ ဖွဲ့စည်းပုံကို ဤ repository ၏ အမြစ်တွင်ရှိသော `.devcontainer/` ဖိုဒါထဲရှိ `devcontainer.json` ဖိုင်တွင် သတ်မှတ်ထားသည်။

dev ကွန်တိန်နာကို အကောင်အထည်ဖော်ရန် [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (Cloud-hosted runtime အတွက်) သို့မဟုတ် [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (ဒေသခံစက်ပေါ်တွင် runtime အတွက်) တွင် ဖြင့် စတင်ပါ။ VS Code တွင် dev ကွန်တိန်နာများ အလုပ်လုပ်ပုံအကြောင်း အသေးစိတ်ကို [ဤစာရွက်စာတမ်း](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) ကို ဖတ်ပါ။

> [!TIP]  
> အလွယ်တကူ စတင်နိုင်ရန် GitHub Codespaces ကို အသုံးပြုရန် အကြံပြုပါသည်။ ၎င်းသည် ပုဂ္ဂိုလ်ရေးအကောင့်များအတွက် [အခမဲ့သုံးစွဲခွင့်](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) ပေးပါသည်။ သင့် quota အသုံးပြုမှုကို အများဆုံး ဖြစ်စေရန် အလုပ်မလုပ်သော codespaces များကို ရပ်တန့်ရန် သို့မဟုတ် ဖျက်ရန် [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) ကို ပြင်ဆင်ပါ။

## 1. လုပ်ငန်းများကို အကောင်အထည်ဖော်ခြင်း

သင်ခန်းစာတိုင်းတွင် Python, .NET/C#, Java နှင့် JavaScript/TypeScript အပါအဝင် အတော်များများသော programming language များဖြင့် ပေးနိုင်သော _optional_ လုပ်ငန်းများ ရှိမည်ဖြစ်သည်။ ဤအပိုင်းတွင် ၎င်းတို့ကို အကောင်အထည်ဖော်ရာတွင် အသိပညာဖြစ်သော အကြံပြုချက်များကို ပေးပါသည်။

### 1.1 Python လုပ်ငန်းများ

Python လုပ်ငန်းများကို အပလီကေးရှင်းများ (`.py` ဖိုင်များ) သို့မဟုတ် Jupyter notebooks (`.ipynb` ဖိုင်များ) အဖြစ် ပေးသည်။
- notebook ကို အလုပ်လှုပ်ရန် Visual Studio Code တွင် ဖွင့်ပါ၊ ထို့နောက် _Select Kernel_ (အပေါ်ယံညာဘက်) ကို နှိပ်ပြီး အမှန်တကယ် Python 3 ရွေးချယ်ပါ။ notebook ကို အလုပ်လှုပ်ရန် _Run All_ ကို ယခုမှာ အသုံးပြုနိုင်ပါပြီ။
- command-line မှ Python အပလီကေးရှင်းများကို အလုပ်လှုပ်ရန် သေချာစွာ ရွေးချယ်ပြီး လိုအပ်သော အချက်အလက်များကို ပေးရန် လုပ်ငန်းအတွက် သီးခြားအညွှန်းများကို လိုက်နာပါ။

## 2. ပံ့ပိုးသူများကို ပြင်ဆင်ခြင်း

လုပ်ငန်းများကို **တစ်ခု သို့မဟုတ် အများအပြားသော** LLM (Large Language Model) deployments များနှင့် အလုပ်လုပ်နိုင်ရန် OpenAI, Azure သို့မဟုတ် Hugging Face ကဲ့သို့သော ပံ့ပိုးမှုပေးသူများမှ ထောက်ပံ့သော API အား အသုံးပြု၍ တပ်ဆင်နိုင်သည်။ ဤသင်ခန်းစာတွင် ၎င်းတို့အကြောင်း ပြောပါသည်:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) သည် GPT စီးရီး အပါအဝင် မော်ဒယ်များ များစွာဖြင့်
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) သည် စီးပွားရေးလုပ်ငန်းအတွက် အဆင်သင့်ဖြစ်ရန် အထူးပြုထားသော OpenAI မော်ဒယ်များ
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) သည် ဖွင့်လှစ်မော်ဒယ်များနှင့် အတုလုပ်ငန်းများအတွက်

**ဤလေ့ကျင့်မှုများအတွက် သင့်ကိုယ်ပိုင်အကောင့်များကို အသုံးပြုရန် လိုအပ်ပါသည်**။ လုပ်ငန်းများသည် optional ဖြစ်သောကြောင့် သင်၏ စိတ်ဝင်စားမှုအပေါ် မူတည်၍ တစ်ခု, အားလုံး - သို့မဟုတ် မည်သည့်အရာမျှ မတပ်ဆင်နိုင်ပါ။

| Signup | ကုန်ကျစရိတ် | API Key | Playground | မှတ်ချက်များ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pricing](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | မော်ဒယ်များ များစွာ ရရှိနိုင်သည် |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Must Apply Ahead For Access](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat has limited models](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

အောက်ပါညွှန်ကြားချက်များကို လိုက်နာပြီး အမျိုးမျိုးသော ပံ့ပိုးသူများနှင့် အသုံးပြုရန် ဤ repository ကို _configure_ လုပ်ပါ။ သတ်မှတ်ချက်တစ်ခုလိုအပ်သော လုပ်ငန်းများတွင် filename တွင် ဤ tag များထဲမှ တစ်ခုပါရှိမည်:
 - `aoai` - Azure OpenAI endpoint, key လိုအပ်သည်
 - `oai` - OpenAI endpoint, key လိုအပ်သည်
 - `hf` - Hugging Face token လိုအပ်သည်

သင်သည် တစ်ခု, မည်သည့်အရာမျှ, သို့မဟုတ် အားလုံးကို configure လုပ်နိုင်ပါသည်။ သက်ဆိုင်ရာ လုပ်ငန်းများသည် missing credentials များရှိလျှင် error ဖြစ်မည်ဖြစ်သည်။

###  2.1. `.env` ဖိုင် ဖန်တီးပါ

သင့်အနေဖြင့် အထက်ပါ ညွှန်ကြားချက်များကို ဖတ်ပြီး သက်ဆိုင်ရာ ပံ့ပိုးသူနှင့် လက်မှတ်ထိုးပြီး လိုအပ်သော အတည်ပြုချက်များ (API_KEY သို့မဟုတ် token) ရရှိပြီးဖြစ်သည်ဟု ချမှတ်ထားပါသည်။ Azure OpenAI အတွက် သင့်အနေဖြင့် chat completion အတွက် အနည်းဆုံး GPT မော်ဒယ် တစ်ခုနှင့် တပ်ဆင်ထားသော Azure OpenAI Service (endpoint) ၏ တရားဝင်တပ်ဆင်ထားသော တပ်ဆင်မှုရှိပြီးဖြစ်သည်ဟု ချမှတ်ထားပါသည်။

နောက်ထပ်အဆင့်မှာ သင့် **ဒေသခံပတ်ဝန်းကျင် အပြောင်းအလဲများ** ကို အောက်ပါအတိုင်း ပြင်ဆင်ပါ:

1. `.env.copy` ဖိုင်ကို အမြစ်ဖိုဒါတွင် ရှာကြည့်ပါ၊ ၎င်းတွင် အောက်ပါအတိုင်း ပါဝင်မှုများ ရှိရမည်:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. အောက်ပါ command ကို အသုံးပြု၍ `.env` သို့ ၎င်းဖိုင်ကို မိတ္တူယူပါ။ ဤဖိုင်သည် _gitignore-d_ ဖြစ်ပြီး လျှို့ဝှက်ချက်များကို ဘေးကင်းစေပါသည်။

   ```bash
   cp .env.copy .env
   ```

3. နောက်ဆက်တွဲအပိုင်းတွင် ဖော်ပြထားသည့်အတိုင်း တန်ဖိုးများကို (ညာဘက်တွင် `=` အတိုင်းပြောင်းပါ) ဖြည့်ပါ။

3. (ရွေးချယ်မှု) သင်သည် GitHub Codespaces ကို အသုံးပြုပါက ဤ repository နှင့် ဆက်စပ်သော _Codespaces secrets_ အဖြစ် ပတ်ဝန်းကျင်အပြောင်းအလဲများကို သိမ်းဆည်းနိုင်သည်။ ဤကိစ္စတွင်, ဒေသခံ .env ဖိုင်ကို တပ်ဆင်ရန် မလိုအပ်ပါ။ **သို့သော်, ဤရွေးချယ်မှုသည် GitHub Codespaces ကို သုံးပါကသာ အလုပ်လုပ်ပါသည်**။ Docker Desktop ကို အသုံးပြုပါက .env ဖိုင်ကို အလျှောက်အလုပ်လုပ်ရသေးမည်ဖြစ်သည်။

### 2.2. `.env` ဖိုင်ကို ဖြည့်ပါ

အောက်ပါကိန်းဂဏန်းများကို နားလည်ရန် အမြန်ကြည့်ကြပါစို့:

| Variable  | ဖော်ပြချက်  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | သင်၏ profile တွင် တပ်ဆင်ထားသော user access token |
| OPENAI_API_KEY | non-Azure OpenAI endpoints အတွက် ဝန်ဆောင်မှုကို အသုံးပြုရန် အတည်ပြုချက် |
| AZURE_OPENAI_API_KEY | ဝန်ဆောင်မှုကို အသုံးပြုရန် အတည်ပြုချက် |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI resource အတွက် တပ်ဆင်ထားသော endpoint |
| AZURE_OPENAI_DEPLOYMENT | ဤသည် _text generation_ မော်ဒယ် တပ်ဆင်မှု endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | ဤသည် _text embeddings_ မော်ဒယ် တပ်ဆင်မှု endpoint |
| | |

မှတ်ချက်: နောက်ဆုံးသော Azure OpenAI အပြောင်းအလဲနှစ်ခုသည် chat completion (text generation) နှင့် vector search (embeddings) အတွက် အမှန်တကယ်မော်ဒယ်ကို ကိုယ်စားပြုသည်။ ၎င်းတို့ကို သတ်မှတ်ရန် ညွှန်ကြားချက်များကို သက်ဆိုင်ရာ လုပ်ငန်းများတွင် ဖော်ပြထားပါမည်။

### 2.3 Azure ကို ပြင်ဆင်ပါ: Portal မှ

Azure OpenAI endpoint နှင့် key တန်ဖိုးများကို [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) တွင် ရှာတွေ့နိုင်ပါသည်။

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) သို့ သွားပါ
1. ဘေးဘက်တွင် **Keys and Endpoint** ရွေးချယ်မှုကို နှိပ်ပါ။
1. **Show Keys** ကို နှိပ်ပါ - သင် KEY 1, KEY 2 နှင့် Endpoint ကို မြင်ရပါမည်။
1. AZURE_OPENAI_API_KEY အတွက် KEY 1 တန်ဖိုးကို အသုံးပြုပါ
1. AZURE_OPENAI_ENDPOINT အတွက် Endpoint တန်ဖိုးကို အသုံးပြုပါ

နောက်တစ်ခုမှာ, ကျွန်ုပ်တို့ တပ်ဆင်ထားသော မော်ဒယ်များအတွက် endpoints များလိုအပ်သည်။

1. Azure OpenAI resource အတွက် ဘေးဘက်တွင် **Model deployments** ရွေးချယ်မှုကို နှိပ်ပါ။
1. အဆုံးသတ်စာမျက်နှာတွင်, **Manage Deployments** ကို နှိပ်ပါ

ဤသည်သည် Azure OpenAI Studio website သို့ သင့်ကို ခေါ်ဆောင်သွားမည်ဖြစ်ပြီး, အောက်တွင် ဖော်ပြထားသော အခြားတန်ဖိုးများကို ရှာတွေ့ပါမည်။

### 2.4 Azure ကို ပြင်ဆင်ပါ: Studio မှ

1. [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) သို့ သွားပါ
1. ဘေးဘက်တွင် **Deployments** tab ကို နှိပ်ပါ။
1. သင့်လိုချင်သော မော်ဒယ်မတပ်ဆင်ထားပါက, **Create new deployment** ကို အသုံးပြု၍ ၎င်းကို တပ်ဆင်ပါ။
1. သင့်အနေဖြင့် _text-generation_ မော်ဒယ်လိုအပ်ပါသည် - ကျွန်ုပ်တို့၏ အကြံပြုချက်မှာ: **gpt-35-turbo**
1. သင့်အနေဖြင့် _text-embedding_ မော်ဒယ်လိုအပ်ပါသည် - ကျွန်ုပ်တို့၏ အကြံပြုချက်မှာ **text-embedding-ada-002**

ယခု သင့်ပတ်ဝန်းကျင်အပြောင်းအလဲများကို _Deployment name_ အသုံးပြု၍ ပြောင်းလဲပါ။ ယင်းသည် မော်ဒယ်အမည်နှင့် အတူတူဖြစ်ရပါမည်၊ သင် ၎င်းကို ထူးခြားစွာပြောင်းလဲမထားပါက။ ဥပမာအားဖြင့် သင့်တွင်:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**.env ဖိုင်ကို ပြီးပါက သိမ်းရန် မမေ့ပါနှင့်**။ သင်သည် ယခု ဖိုင်မှ ထွက်ပြီး notebook ကို အလုပ်လှုပ်ရန် ညွှန်ကြားချက်များသို့ ပြန်သွားနိုင်ပါပြီ။

### 2.5 OpenAI ကို ပြင်ဆင်ပါ: Profile မှ

သင့် OpenAI API key ကို သင့် [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) တွင် ရှာတွေ့နိုင်ပါသည်။ သင်တွင် မရှိပါက, အကောင့်တစ်ခုအတွက် စာရင်းသွင်းပြီး API key တစ်ခု ဖန်တီးနိုင်သည်။ သင် key ရရှိပါက, ၎င်းကို `.env` ဖိုင်ထဲရှိ `OPENAI_API_KEY` အပြောင်းအလဲတွင် ဖြည့်နိုင်ပါသည်။

### 2.6 Hugging Face ကို ပြင်ဆင်ပါ: Profile မှ

သင့် Hugging Face token ကို သင့် profile ထဲရှိ [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) တွင် ရှာတွေ့နိုင်ပါသည်။ ၎င်းကို အများသူငါမသိအောင်, မဝေမျှပါနှင့်။ ဤ project အသုံးပြုမှုအတွက် token အသစ်တစ်ခု ဖန်တီးပြီး, ၎င်းကို `.env` ဖိုင်ထဲရှိ `HUGGING_FACE_API_KEY` အပြောင်းအလဲတွင် ကူးပါ။ _မှတ်ချက်:_ ဤသည် နည်းပညာပိုင်းအရ API key မဟုတ်ပေမယ့် အတည်ပြုချက်အတွက် အသုံးပြုသောကြောင့်, ဤအမည်ပေးပုံကို အဆက်မပြတ်ထားပါသည်။

**အာမခံချက်**:
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်စနစ် [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြုပြီး ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ထားသောအခါ မှားယွင်းမှုများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို လက်ခံထားသော အရင်းအမြစ်အဖြစ် တွက်ချက်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြု၍ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲသုံးလွဲများ သို့မဟုတ် အလွဲမှားများအတွက် ကျွန်ုပ်တို့တာဝန်မယူပါ။