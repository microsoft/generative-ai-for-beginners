<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T19:54:58+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "my"
}
-->
# LLM ပံ့ပိုးသူတစ်ဦးရွေးချယ်ခြင်းနှင့် ပြင်ဆင်သတ်မှတ်ခြင်း 🔑

အလုပ်အပ်ချက်များကို OpenAI, Azure သို့မဟုတ် Hugging Face ကဲ့သို့သော ပံ့ပိုးသူများမှ တစ်ဆင့် တစ်ခု သို့မဟုတ် တစ်ခုထက်ပိုသော Large Language Model (LLM) များနှင့် အလုပ်လုပ်နိုင်အောင် ပြင်ဆင်နိုင်ပါသည်။ ဤပံ့ပိုးသူများသည် _hosted endpoint_ (API) တစ်ခုကို ပံ့ပိုးပေးပြီး၊ မှန်ကန်သော အထောက်အထား (API key သို့မဟုတ် token) ဖြင့် အလိုအလျောက် ချိတ်ဆက်အသုံးပြုနိုင်ပါသည်။ ဒီသင်တန်းမှာတော့ အောက်ပါပံ့ပိုးသူများအကြောင်း ဆွေးနွေးသွားပါမယ်-

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) - GPT စီးရီးအပါအဝင် မော်ဒယ်အမျိုးမျိုးပါဝင်သည်။
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) - စီးပွားရေးအတွက် အထူးပြင်ဆင်ထားသော OpenAI မော်ဒယ်များ
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) - ဖွင့်လှစ်ရင်းမြစ် မော်ဒယ်များနှင့် inference server

**ဤလေ့ကျင့်ခန်းများအတွက် ကိုယ်ပိုင်အကောင့်များလိုအပ်ပါသည်**။ အလုပ်အပ်ချက်များသည် ရွေးချယ်စရာဖြစ်သဖြင့် သင်စိတ်ဝင်စားသလို တစ်ခုတည်း၊ အားလုံး သို့မဟုတ် မည်သည့်ပံ့ပိုးသူမျှ မသတ်မှတ်ဘဲ ပြင်ဆင်နိုင်ပါသည်။ အကောင့်ဖွင့်ရန်အတွက် အောက်ပါအကြံပြုချက်များကို လိုက်နာပါ-

| Signup | Cost | API Key | Playground | Comments |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pricing](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | မော်ဒယ်အမျိုးမျိုး ရရှိနိုင်သည် |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [အသုံးပြုခွင့်အတွက် ကြိုတင်လျှောက်ထားရမည်](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat တွင် မော်ဒယ်အနည်းငယ်သာ ရရှိနိုင်သည်](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

အောက်ပါ လမ်းညွှန်ချက်များအတိုင်း repository ကို ပံ့ပိုးသူအမျိုးမျိုးနှင့် အသုံးပြုနိုင်အောင် _ပြင်ဆင်သတ်မှတ်_ ပါ။ ပံ့ပိုးသူတစ်ခုအထူးလိုအပ်သော အလုပ်အပ်ချက်များတွင် အောက်ပါ tag များထဲမှ တစ်ခုကို filename တွင်ပါဝင်ပါလိမ့်မည်-

- `aoai` - Azure OpenAI endpoint နှင့် key လိုအပ်သည်
- `oai` - OpenAI endpoint နှင့် key လိုအပ်သည်
- `hf` - Hugging Face token လိုအပ်သည်

တစ်ခုတည်း၊ မည်သည့်ပံ့ပိုးသူမျှ မသတ်မှတ်ဘဲ သို့မဟုတ် အားလုံးကို ပြင်ဆင်နိုင်ပါသည်။ သက်ဆိုင်ရာ အလုပ်အပ်ချက်များသည် အထောက်အထား မရှိလျှင် error ပြပါလိမ့်မည်။

## `.env` ဖိုင်ဖန်တီးခြင်း

အထက်ပါ လမ်းညွှန်ချက်များကို ဖတ်ပြီး သက်ဆိုင်ရာ ပံ့ပိုးသူတွင် အကောင့်ဖွင့်ပြီးလိုအပ်သော authentication အထောက်အထားများ (API_KEY သို့မဟုတ် token) ရရှိပြီးသားဖြစ်သည်ဟု ယူဆပါသည်။ Azure OpenAI အတွက်တော့ Azure OpenAI Service (endpoint) တစ်ခုကို တရားဝင်ဖန်တီးပြီး chat completion အတွက် GPT မော်ဒယ်တစ်ခုခု deploy လုပ်ပြီးသားဖြစ်ရပါမည်။

နောက်တစ်ဆင့်မှာတော့ ကိုယ်ပိုင် **local environment variables** များကို အောက်ပါအတိုင်း ပြင်ဆင်ပါ-

1. root folder ထဲမှာ `.env.copy` ဆိုတဲ့ ဖိုင်ရှိမယ်၊ အဲဒီဖိုင်ထဲမှာ အောက်ပါအတိုင်းပါဝင်နေပါလိမ့်မယ်-

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

2. အဲဒီဖိုင်ကို `.env` ဆိုတဲ့နာမည်နဲ့ အောက်ပါ command နဲ့ ကူးယူပါ။ ဒီဖိုင်ကို _gitignore_ ထားတာမို့ လျှို့ဝှက်ချက်များလုံခြုံစေပါတယ်။

   ```bash
   cp .env.copy .env
   ```

3. နောက်ထပ်အပိုင်းမှာ ဖော်ပြထားသည့်အတိုင်း ( `=` ၏ညာဘက်ရှိ placeholder များကို) ကိုယ်ပိုင်တန်ဖိုးများဖြည့်ပါ။

4. (ရွေးချယ်စရာ) GitHub Codespaces ကို အသုံးပြုပါက environment variables များကို _Codespaces secrets_ အဖြစ် repository နှင့် ချိတ်ဆက်သိမ်းဆည်းနိုင်သည်။ ဒီအခါမှာတော့ local .env ဖိုင် ပြင်ဆင်စရာမလိုတော့ပါဘူး။ **သို့သော် ဒီနည်းလမ်းသည် GitHub Codespaces ကိုသာ အသုံးပြုပါက အလုပ်လုပ်ပါမယ်။** Docker Desktop အသုံးပြုပါက .env ဖိုင်ကို မဖြစ်မနေ ပြင်ဆင်ရပါမယ်။

## `.env` ဖိုင်ကို ဖြည့်သွင်းခြင်း

Variable name များအဓိပ္ပါယ်ကို အနည်းငယ်ရှင်းပြပါမယ်-

| Variable  | Description  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | ကိုယ်ပိုင် profile ထဲမှာ ပြင်ဆင်ထားတဲ့ user access token ပါ |
| OPENAI_API_KEY | non-Azure OpenAI endpoint များအတွက် အသုံးပြုသည့် authorization key ပါ |
| AZURE_OPENAI_API_KEY | Azure OpenAI service အသုံးပြုရန် authorization key ပါ |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI resource အတွက် deploy လုပ်ထားသော endpoint ပါ |
| AZURE_OPENAI_DEPLOYMENT | _text generation_ မော်ဒယ် deployment endpoint ပါ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _text embeddings_ မော်ဒယ် deployment endpoint ပါ |
| | |

မှတ်ချက်- နောက်ဆုံးအနည်းဆုံး Azure OpenAI variable နှစ်ခုသည် chat completion (text generation) နှင့် vector search (embeddings) အတွက် မူရင်းမော်ဒယ်ကို ကိုယ်စားပြုသည်။ ဤ variable များကို ပြင်ဆင်ရန် လမ်းညွှန်ချက်များကို သက်ဆိုင်ရာ အလုပ်အပ်ချက်များတွင် ဖော်ပြပါမည်။

## Azure ကို ပြင်ဆင်ခြင်း - Portal မှတစ်ဆင့်

Azure OpenAI endpoint နှင့် key တန်ဖိုးများကို [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) တွင် ရှာနိုင်ပါသည်။

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) သို့ ဝင်ပါ။
1. ဘယ်ဘက် sidebar (menu) မှ **Keys and Endpoint** ကို နှိပ်ပါ။
1. **Show Keys** ကို နှိပ်ပါ - KEY 1, KEY 2 နှင့် Endpoint တို့ကို မြင်ရပါလိမ့်မယ်။
1. AZURE_OPENAI_API_KEY အတွက် KEY 1 တန်ဖိုးကို အသုံးပြုပါ။
1. AZURE_OPENAI_ENDPOINT အတွက် Endpoint တန်ဖိုးကို အသုံးပြုပါ။

နောက်တစ်ဆင့်မှာတော့ ကိုယ် deploy လုပ်ထားတဲ့ မော်ဒယ်များအတွက် endpoint များလိုအပ်ပါမယ်။

1. Azure OpenAI resource အတွက် sidebar (left menu) မှ **Model deployments** ကို နှိပ်ပါ။
1. ပေါ်လာသော စာမျက်နှာတွင် **Manage Deployments** ကို နှိပ်ပါ။

ဒါက Azure OpenAI Studio website သို့ ချိတ်ဆက်ပေးပြီး အောက်တွင်ဖော်ပြထားသည့် တန်ဖိုးများကို ရှာနိုင်ပါမယ်။

## Azure ကို ပြင်ဆင်ခြင်း - Studio မှတစ်ဆင့်

1. အထက်ဖော်ပြပါအတိုင်း ကိုယ့် resource မှ [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) သို့ သွားပါ။
1. Sidebar (ဘယ်ဘက်) မှ **Deployments** tab ကို နှိပ်ပြီး လက်ရှိ deploy လုပ်ထားသော မော်ဒယ်များကို ကြည့်ပါ။
1. လိုချင်တဲ့ မော်ဒယ် မရှိသေးရင် **Create new deployment** ကို အသုံးပြုပြီး deploy လုပ်ပါ။
1. _text-generation_ မော်ဒယ်လိုအပ်ပါမယ် - **gpt-35-turbo** ကို အကြံပြုပါတယ်။
1. _text-embedding_ မော်ဒယ်လည်းလိုအပ်ပါမယ် - **text-embedding-ada-002** ကို အကြံပြုပါတယ်။

အခုတော့ environment variables များကို ကိုယ်အသုံးပြုထားသော _Deployment name_ နဲ့ ကိုက်ညီအောင် ပြင်ဆင်ပါ။ မော်ဒယ်နာမည်နဲ့ တူတတ်ပေမယ့် ကိုယ်ပြောင်းလဲထားလျှင် အဲဒီနာမည်ကို အသုံးပြုပါ။ ဥပမာအနေနဲ့-

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**ပြီးသွားရင် .env ဖိုင်ကို မမေ့ဘဲ သိမ်းပါ**။ အခုတော့ ဖိုင်ထဲကနေ ထွက်ပြီး notebook run လုပ်ရန် လမ်းညွှန်ချက်များဆီ ပြန်သွားနိုင်ပါပြီ။

## OpenAI ကို ပြင်ဆင်ခြင်း - Profile မှတစ်ဆင့်

OpenAI API key ကို ကိုယ့် [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) မှာ ရနိုင်ပါတယ်။ မရှိသေးရင် အကောင့်ဖွင့်ပြီး API key တစ်ခုဖန်တီးနိုင်ပါတယ်။ Key ရရှိပြီးပါက `.env` ဖိုင်ထဲက `OPENAI_API_KEY` variable မှာ ထည့်သွင်းနိုင်ပါပြီ။

## Hugging Face ကို ပြင်ဆင်ခြင်း - Profile မှတစ်ဆင့်

Hugging Face token ကို ကိုယ့် profile ထဲက [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) မှာ ရနိုင်ပါတယ်။ ဒီ token ကို အများသိအောင် မမျှဝေပါနှင့်။ ဒီ project အတွက် အသစ်တစ်ခုဖန်တီးပြီး `.env` ဖိုင်ထဲက `HUGGING_FACE_API_KEY` variable မှာ ထည့်ပါ။ _မှတ်ချက်- ဒီဟာက API key မဟုတ်ပေမယ့် authentication အတွက် အသုံးပြုတာမို့ နာမည်တူအောင်ထားထားပါတယ်။_

---

**သတိပေးချက်**:
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းသည် မူလဘာသာစကားဖြင့် အာဏာပိုင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာသော နားလည်မှုမှားခြင်း သို့မဟုတ် အနားလည်မှုမှားခြင်းများအတွက် ကျွန်ုပ်တို့ တာဝန်ယူမည်မဟုတ်ပါ။