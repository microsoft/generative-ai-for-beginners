<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:38:58+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "my"
}
-->
# သင့် Dev ပတ်ဝန်းကျင်ကို စတင်ပြင်ဆင်ခြင်း

ဒီ repository နဲ့ သင်တန်းကို Python3, .NET, Node.js နဲ့ Java ဖွံ့ဖြိုးရေးကို ထောက်ပံ့နိုင်တဲ့ Universal runtime ပါဝင်တဲ့ [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) နဲ့ ပြင်ဆင်ထားပါတယ်။ ဆက်စပ် configuration ကို ဒီ repository ရဲ့ root မှာရှိတဲ့ `.devcontainer/` ဖိုလ်ဒါအတွင်းရှိ `devcontainer.json` ဖိုင်မှာ သတ်မှတ်ထားပါတယ်။

dev container ကို အသုံးပြုဖို့ [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (cloud-hosted runtime အတွက်) သို့မဟုတ် [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (local device-hosted runtime အတွက်) မှာ ဖွင့်ပါ။ VS Code အတွင်း dev containers များ ဘယ်လိုအလုပ်လုပ်ကြောင်း ပိုမိုသိရှိရန် [ဒီစာရွက်စာတမ်း](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) ကို ဖတ်ရှုပါ။

> [!TIP]  
> အလျင်အမြန် စတင်လိုသူများအတွက် GitHub Codespaces ကို အသုံးပြုရန် အကြံပြုပါတယ်။ ပုဂ္ဂိုလ်ရေးအကောင့်များအတွက် [အခမဲ့ အသုံးပြုခွင့်](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) ကို ပေးထားပါတယ်။ သင့် quota ကို အများဆုံးအသုံးပြုနိုင်ရန် အလုပ်မလုပ်သော codespaces များကို ရပ်တန့်ရန် သို့မဟုတ် ဖျက်ရန် [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) ကို ပြင်ဆင်ပါ။

## 1. အလုပ်အပ်တာများကို အကောင်အထည်ဖော်ခြင်း

တစ်ခုချင်းသင်ခန်းစာတိုင်းမှာ Python, .NET/C#, Java နဲ့ JavaScript/TypeScript အပါအဝင် အစီအစဉ်ဘာသာစကားတစ်ခု သို့မဟုတ် အများကြီးဖြင့် _optional_ အလုပ်အပ်တာများ ပါဝင်နိုင်ပါတယ်။ ဒီအပိုင်းမှာ အလုပ်အပ်တာများကို ဘယ်လို အကောင်အထည်ဖော်ရမယ်ဆိုတာ အထွေထွေ လမ်းညွှန်ချက်များ ပေးထားပါတယ်။

### 1.1 Python အလုပ်အပ်တာများ

Python အလုပ်အပ်တာများကို application (`.py` ဖိုင်များ) သို့မဟုတ် Jupyter notebook (`.ipynb` ဖိုင်များ) အဖြစ် ပေးထားပါတယ်။
- notebook ကို run ဖို့ Visual Studio Code မှာ ဖွင့်ပြီး အပေါ်ညာဘက်ရှိ _Select Kernel_ ကို နှိပ်ပြီး ပုံမှန် Python 3 ကို ရွေးချယ်ပါ။ အခု _Run All_ ကို နှိပ်ပြီး notebook ကို အကောင်အထည်ဖော်နိုင်ပါပြီ။
- command-line မှာ Python application များ run ဖို့ အလုပ်အပ်တာအလိုက် သတ်မှတ်ထားတဲ့ လမ်းညွှန်ချက်များကို လိုက်နာပြီး မှန်ကန်တဲ့ ဖိုင်များကို ရွေးချယ်ပြီး လိုအပ်တဲ့ argument များကို ထည့်သွင်းပါ။

## 2. Provider များကို ပြင်ဆင်ခြင်း

အလုပ်အပ်တာများကို OpenAI, Azure သို့မဟုတ် Hugging Face ကဲ့သို့သော ဝန်ဆောင်မှုပေးသူတစ်ခု သို့မဟုတ် အများကြီးရှိတဲ့ Large Language Model (LLM) deployment များနှင့် အလုပ်လုပ်အောင် ပြင်ဆင်ထားနိုင်ပါတယ်။ ၎င်းတို့က _hosted endpoint_ (API) ကို မှန်ကန်တဲ့ အတည်ပြုချက်များ (API key သို့မဟုတ် token) ဖြင့် အလိုအလျောက် အသုံးပြုနိုင်စေပါတယ်။ ဒီသင်တန်းမှာ အောက်ပါ provider များကို ဆွေးနွေးထားပါတယ်-

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) - core GPT စီးရီးအပါအဝင် မော်ဒယ်မျိုးစုံပါဝင်သည်။
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) - OpenAI မော်ဒယ်များအတွက် စီးပွားရေးအသုံးပြုမှုအတွက် အထူးပြင်ဆင်ထားသည်။
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) - open-source မော်ဒယ်များနှင့် inference server များအတွက်။

**ဒီလေ့ကျင့်ခန်းများအတွက် သင့်ကိုယ်ပိုင် အကောင့်များကို အသုံးပြုရပါမည်။** အလုပ်အပ်တာများမှာ ရွေးချယ်စရာဖြစ်သောကြောင့် သင်စိတ်ဝင်စားရာ provider တစ်ခု၊ အားလုံး သို့မဟုတ် မည်သည့် provider ကိုမှ မပြင်ဆင်နိုင်ပါ။ စာရင်းသွင်းခြင်းအတွက် လမ်းညွှန်ချက်အချို့-

| စာရင်းသွင်းရန် | ကုန်ကျစရိတ် | API Key | Playground | မှတ်ချက်များ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [စျေးနှုန်း](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | မော်ဒယ်များစွာ ရရှိနိုင်သည် |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [စျေးနှုန်း](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [အသုံးပြုခွင့် ရယူရန် ကြိုတင်လျှောက်ထားရမည်](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [စျေးနှုန်း](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat တွင် မော်ဒယ်ကန့်သတ်ချက်ရှိသည်](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

ဒီ repository ကို provider များအလိုက် _configure_ လုပ်ရန် အောက်ပါ လမ်းညွှန်ချက်များကို လိုက်နာပါ။ အလုပ်အပ်တာတစ်ခုမှာ provider တစ်ခု သတ်မှတ်ထားရင် ဖိုင်နာမည်မှာ အောက်ပါ tag များထဲမှ တစ်ခုပါဝင်ပါမယ်-
 - `aoai` - Azure OpenAI endpoint နဲ့ key လိုအပ်သည်
 - `oai` - OpenAI endpoint နဲ့ key လိုအပ်သည်
 - `hf` - Hugging Face token လိုအပ်သည်

သင်တစ်ခု၊ မရှိ၊ သို့မဟုတ် အားလုံးကို configure လုပ်နိုင်ပါတယ်။ ဆက်စပ် အလုပ်အပ်တာများမှာ အတည်ပြုချက် မရှိရင် error ဖြစ်ပါလိမ့်မယ်။

###  2.1. `.env` ဖိုင် ဖန်တီးခြင်း

အထက်ပါ လမ်းညွှန်ချက်များကို ဖတ်ပြီး သင့်အတွက် သင့်လျော်သော provider တွင် စာရင်းသွင်းပြီး လိုအပ်သော အတည်ပြုချက်များ (API_KEY သို့မဟုတ် token) ရရှိထားကြောင်း သတ်မှတ်ထားသည်ဟု ယူဆပါသည်။ Azure OpenAI အတွက်ဆိုရင် Azure OpenAI Service (endpoint) တစ်ခုမှာ GPT မော်ဒယ်တစ်ခုခု chat completion အတွက် တပ်ဆင်ပြီး ရှိကြောင်းလည်း ယူဆပါသည်။

နောက်တစ်ဆင့်မှာ သင့် **local environment variables** ကို အောက်ပါအတိုင်း ပြင်ဆင်ပါ-

1. root ဖိုလ်ဒါမှာ `.env.copy` ဖိုင်ရှိမရှိ စစ်ဆေးပါ။ အဲဒီဖိုင်ထဲမှာ အောက်ပါအတိုင်း ပါဝင်နိုင်ပါတယ်-

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

2. အောက်ပါ command ဖြင့် `.env.copy` ကို `.env` အဖြစ် ကူးယူပါ။ ဒီဖိုင်က _gitignore_ ထားပြီး လျှို့ဝှက်ချက်များကို ကာကွယ်ထားပါတယ်။

   ```bash
   cp .env.copy .env
   ```

3. နောက်ပိုင်း အပိုင်းမှာ ဖော်ပြထားသလို `=` အနားက placeholder များကို သင့်အချက်အလက်ဖြင့် ဖြည့်စွက်ပါ။

3. (ရွေးချယ်စရာ) GitHub Codespaces ကို အသုံးပြုပါက ဒီ repository နဲ့ ဆက်စပ်ထားတဲ့ _Codespaces secrets_ အဖြစ် environment variables များကို သိမ်းဆည်းနိုင်ပါတယ်။ ဒီလိုလုပ်ရင် local .env ဖိုင် မလိုတော့ပါဘူး။ **သို့သော် ဒီရွေးချယ်မှုက GitHub Codespaces ကိုသာ အသုံးပြုတဲ့အခါမှာသာ အလုပ်လုပ်ပါမယ်။** Docker Desktop ကို အသုံးပြုရင်တော့ .env ဖိုင်ကို ပြင်ဆင်ထားရပါမယ်။

### 2.2 `.env` ဖိုင်ကို ဖြည့်စွက်ခြင်း

variable နာမည်တွေက ဘာကို ကိုယ်စားပြုတာလဲဆိုတာ အမြန်ကြည့်ကြရအောင်-

| Variable  | ဖော်ပြချက်  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | သင့် profile မှာ သတ်မှတ်ထားတဲ့ user access token ဖြစ်သည် |
| OPENAI_API_KEY | non-Azure OpenAI endpoint များအတွက် ဝန်ဆောင်မှု အသုံးပြုခွင့် key ဖြစ်သည် |
| AZURE_OPENAI_API_KEY | Azure OpenAI ဝန်ဆောင်မှု အသုံးပြုခွင့် key ဖြစ်သည် |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI resource အတွက် တပ်ဆင်ထားသော endpoint ဖြစ်သည် |
| AZURE_OPENAI_DEPLOYMENT | _text generation_ မော်ဒယ် deployment endpoint ဖြစ်သည် |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _text embeddings_ မော်ဒယ် deployment endpoint ဖြစ်သည် |
| | |

မှတ်ချက်- နောက်ဆုံး Azure OpenAI variable နှစ်ခုဟာ chat completion (text generation) နဲ့ vector search (embeddings) အတွက် ပုံမှန် မော်ဒယ်များကို ကိုယ်စားပြုပါတယ်။ ၎င်းတို့ကို သတ်မှတ်ရန် လမ်းညွှန်ချက်များကို ဆက်စပ် အလုပ်အပ်တာများမှာ ဖော်ပြပါလိမ့်မယ်။

### 2.3 Azure ကို Portal မှတဆင့် ပြင်ဆင်ခြင်း

Azure OpenAI endpoint နဲ့ key တန်ဖိုးများကို [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) မှာ ရှာတွေ့နိုင်ပါသည်။ အဲဒီနေရာကနေ စတင်ကြရအောင်-

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) သို့ သွားပါ။
1. Sidebar (ဘယ်ဘက် menu) မှ **Keys and Endpoint** ကို နှိပ်ပါ။
1. **Show Keys** ကို နှိပ်ပါ - KEY 1, KEY 2 နဲ့ Endpoint ကို မြင်ရပါမယ်။
1. AZURE_OPENAI_API_KEY အတွက် KEY 1 ကို အသုံးပြုပါ။
1. AZURE_OPENAI_ENDPOINT အတွက် Endpoint ကို အသုံးပြုပါ။

နောက်တစ်ဆင့်မှာ တပ်ဆင်ထားတဲ့ မော်ဒယ်အတွက် endpoint များလိုအပ်ပါသည်။

1. Azure OpenAI resource အတွက် sidebar (ဘယ်ဘက် menu) မှ **Model deployments** ကို နှိပ်ပါ။
1. ရောက်ရှိသော စာမျက်နှာတွင် **Manage Deployments** ကို နှိပ်ပါ။

ဒီနေရာကနေ Azure OpenAI Studio ဝက်ဘ်ဆိုက်သို့ သွားရောက်ပြီး အောက်ပါအတိုင်း တန်ဖိုးများကို ရှာဖွေပါမယ်။

### 2.4 Azure ကို Studio မှတဆင့် ပြင်ဆင်ခြင်း

1. အထက်ဖော်ပြထားသလို သင့် resource မှ [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) သို့ သွားပါ။
1. sidebar (ဘယ်ဘက်) မှ **Deployments** tab ကို နှိပ်ပြီး လက်ရှိ တပ်ဆင်ထားသော မော်ဒယ်များကို ကြည့်ပါ။
1. သင်လိုချင်သော မော်ဒယ် မတပ်ဆင်ထားရင် **Create new deployment** ကို အသုံးပြုပြီး တပ်ဆင်ပါ။
1. _text-generation_ မော်ဒယ်တစ်ခု လိုအပ်ပါမယ် - အကြံပြုချက်မှာ **gpt-35-turbo** ဖြစ်ပါတယ်။
1. _text-embedding_ မော်ဒယ်တစ်ခု လိုအပ်ပါမယ် - အကြံပြုချက်မှာ **text-embedding-ada-002** ဖြစ်ပါတယ်။

အခုတော့ environment variables တွေကို သုံးထားတဲ့ _Deployment name_ နဲ့ ကိုက်ညီအောင် ပြင်ဆင်ပါ။ မူလအားဖြင့် မော်ဒယ်နာမည်နဲ့ တူညီပါလိမ့်မယ်၊ သင်ပြောင်းလဲထားရင်တော့ အဲဒီအတိုင်းဖြစ်ပါမယ်။ ဥပမာ-

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**ပြင်ဆင်ပြီး .env ဖိုင်ကို သိမ်းမမေ့ပါနဲ့။** ဖိုင်ကို ပိတ်ပြီး notebook run လုပ်ရန် လမ်းညွှန်ချက်များဆီ ပြန်သွားနိုင်ပါပြီ။

### 2.5 OpenAI ကို Profile မှတဆင့် ပြင်ဆင်ခြင်း

သင့် OpenAI API key ကို သင့် [OpenAI အကောင့်](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) မှာ ရှာတွေ့နိုင်ပါသည်။ မရှိသေးရင် အကောင့်ဖွင့်ပြီး API key တစ်ခု ဖန်တီးနိုင်ပါတယ်။ key ရရှိပြီးပါက `.env` ဖိုင်ထဲမှာ `OPENAI_API_KEY` variable ကို ဖြည့်ပါ။

### 2.6 Hugging Face ကို Profile မှတဆင့် ပြင်ဆင်ခြင်း

သင့် Hugging Face token ကို သင့် profile အောက်က [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) မှာ ရှာတွေ့နိုင်ပါသည်။ ဒီ token များကို အများသို့ မဖော်ပြသင့်ပါ။ ဒီ project အတွက် အသစ် token တစ်ခု ဖန်တီးပြီး `.env` ဖိုင်ထဲ `HUGGING_FACE_API_KEY` variable အဖြစ် ကူးထည့်ပါ။ _မှတ်ချက်- ဒီ token ဟာ နည်းပညာပိုင်းဆိုင်ရာ API key မဟုတ်ပေမယ့် authentication အတွက် အသုံးပြုတာဖြစ်လို့ အမည်ကို တူညီစွာ သုံးထားတာ ဖြစ်ပါတယ်။_

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။