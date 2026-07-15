# LLM ပရိုဗိုက်ဒါ ရွေးချယ်ခြင်းနှင့် ဖွင့်ဆောင်ခြင်း 🔑

အစီအစဉ်များကို OpenAI၊ Azure သို့မဟုတ် Hugging Face ကဲ့သို့သော ပံ့ပိုးမှုရှိသော တစ်ဦး၊ တစ်ခုထက်မပိုသော ကြီးမားသောဘာသာစကားမာဒယ် (LLM) တပ်ဆင်မှုများနှင့် အလုပ်လုပ်ရန် စီစဉ်နိုင်သည်။ ၎င်းများသည် ကျွန်ုပ်တို့ စနစ်တကျ ဝင်ခွင့် (API key သို့မဟုတ် token) ဖြင့် ပရိုဂရမ်မှတစ်ဆင့် ရောက်ရှိနိုင်သော _hosted endpoint_ (API) ကို ပေးပါသည်။ ဒီသင်တန်းတွင် ဤပရိုဗိုက်ဒါများကို ဆွေးနွေးပါမည်။

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) - GPT စီးရီးနှင့် အမျိုးမျိုးသော မော်ဒယ်များပါဝင်သည်။
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) - ရုံးပဏာမအဆင့်အတန်းထားပြီး OpenAI မော်ဒယ်များအတွက်
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) - OpenAI၊ Meta၊ Mistral၊ Cohere၊ Microsoft အပါအ ၀ င် မော်ဒယ်စုစုပေါင်းများကို တစ်ခုတည်းသော endpoint နှင့် API key ဖြင့် လက်လှမ်းရောက်အောင် (GitHub Models ကို ၂၀၂၆ ခုနှစ် ဇူလိုင်အဆုံးတွင် အဆုံးသတ်နေပါသည်၊ အစားထိုးသည်)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) - အ ဖွင့်အရင်းအမြစ် မော်ဒယ်များနှင့် အင်ဖာရမ်ဆာ ဆာဗာအတွက်
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) သို့မဟုတ် [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) - မိမိစက်ပေါ်တွင် အပြည့်အဝ အော့ဖ်လိုင်း မော်ဒယ်များကို cloud subscription လိုအပ်ခြင်းမရှိပဲ စစ်ဆေးကစားရန်

**ဤလေ့ကျင့်ခန်းများအတွက် သင်၏ ကိုယ်ပိုင် အကောင့်များကို အသုံးပြုရမည်ဖြစ်သည်။** စီစဉ်ချက်များသည် ရွေးချယ်ရန် အလွတ် ဖြစ်သဖြင့် သင်စိတ်ဝင်စားရာ အရပ်ရပ်ရှိ ပရိုဗိုက်ဒါ တစ်ခု၊ အားလုံး သို့မဟုတ် မည်သည့်ရပ်တစ်ခုမှ မရွေး ချိန်ညှိနိုင်ပါသည်။ အကောင့်ဖွင့်မှုအတွက် အညွှန်းအတွက် -

| အကောင့်ဖွင့်မည် | စရိတ် | API Key | Playground | မှတ်ချက်များ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [စျေးနှုန်း](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | မော်ဒယ်အမျိုးမျိုး ရရှိနိုင်သည် |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [စျေးနှုန်း](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ဝင်ခွင့်ရရန် ယူနော်လုပ်ရန်လိုအပ်သည်](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [စျေးနှုန်း](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Project အကြောင်းအရာ စာမျက်နှာ](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | အခမဲ့အဆင့် ရရှိနိုင်သည်; endpoint တစ်ခု + key တစ်ခုဖြင့် မော်ဒယ်ပရိုဗိုက်ဒါများ အများအပြားကို ဝင်ရောက်ယူနိုင်ပါသည် |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [စျေးနှုန်း](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat တို့တွင် မော်ဒယ်ကန့်သတ်မှုရှိသည်](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | အခမဲ့ (သင်၏စက်ပေါ်တွင် အလုပ်လုပ်သည်) | လိုအပ်မှုမရှိ | [Local CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | အပြည့်အဝ အော့ဖ်လိုင်းဖြစ်ပြီး OpenAI များနဲ့ ကိုက်ညီသော endpoint |
| | | | | |

အောက်ပါညွှန်ကြားချက်များကို လိုက်နာကာ ဒီ repository ကို မတူညီသော ပရိုဗိုက်ဒါများနှင့် အသုံးပြုရန် _ဖွဲ့စည်း_ ပါ။ သတ်မှတ်ထားသော ပရိုဗိုက်ဒါလိုအပ်သော အစီအစဉ်များသည် ဖိုင်နာမည်၌ အောက်ပါ tags တစ်ခုခု ပါဝင်ပါမည် -

- `aoai` - Azure OpenAI endpoint, key လိုအပ်သည်
- `oai` - OpenAI endpoint, key လိုအပ်သည်
- `hf` - Hugging Face token လိုအပ်သည်
- `githubmodels` - Microsoft Foundry Models endpoint, key လိုအပ်သည် (GitHub Models သည် ၂၀၂၆ ခုနှစ် ဇူလိုင်အဆုံးတွင် အဆုံးသတ်မည်)

သင်သည် တစ်ခု၊ မရှိပါ၊ သို့မဟုတ် အားလုံးကိုဖွဲ့စည်းနိုင်သည်။ ပတ်သက်သည့် အစီအစဉ်များသည် လိုအပ်သော အတည်ပြုချက် မရှိပါက error ဖြစ်ပါမည်။

## `.env` ဖိုင် ဖန်တီးခြင်း

ကျွန်ုပ်တို့သည် သင်သည် အပေါ်ဖော်ပြခဲ့သည့် ညွှန်ကြားချက်များကို ဖတ်ပြီး သက်ဆိုင်ရာ ပရိုဗိုက်ဒါထံ အကောင့်ဖွင့်ထားပြီး လိုအပ်သော အတည်ပြုချက်များ (API_KEY သို့မဟုတ် token) ကို ရရှိထားကြောင်း ထင်မြင်ထားသည်။ Azure OpenAI အတွက်တော့ Azure OpenAI Service (endpoint) တွင် GPT မော်ဒယ်တစ်ခုအနည်းဆုံး ဖြန့်ချိထားသည်ဟု သင်ယူထားသည်။

နောက်တစ်ဆင့်မှာ သင်၏ **ဒေသခံ environment variables** တွေကို အောက်ပါအတိုင်း ဖြည့်စွက်ရေးသားခြင်းဖြစ်သည် -

1. root ဖိုldr တြက္ `.env.copy` ဖိုင်တစ်ခုကို ရှာပါ၊ ၎င်းမှာ အောက်ပါအကြောင်းအရာများ ပါရှိပုံမျိုး ဖြစ်နိုင်သည် -

   ```bash
   # OpenAI ပံ့ပိုးသူ
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry မှာ Azure OpenAI
   ## (Azure OpenAI Service သည် ယခု Microsoft Foundry ၏ အစိတ်အပိုင်း ဖြစ်လာပြီးပါပြီ: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # ပုံမှန် သတ်မှတ်ထားပြီး! (လက်ရှိ အတည်ပြု GA API ဗားရှင်း)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry မော်ဒယ်များ (စုပေါင်းပံ့ပိုးသူ မော်ဒယ် နှစ်လုံးစာရင်း၊ GitHub မော်ဒယ်များ အစားထိုး၊ ၂၀၂၆ ခုနှစ် ဇူလိုင်လ အဆုံးတွင် ပိတ်မည်)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. ဖိုင်ကို `.env` ဟူ၍ အောက်ပါ command ဖြင့် ကူးယူပါ။ ဤဖိုင်ကို _gitignore ထားသောကြောင့် လျှို့ဝှက်ချက်များကို ကာကွယ်ထားသည်။

   ```bash
   cp .env.copy .env
   ```

3. ထိုအချက်အလက်များတွင် ( `=` အညာဘက်ရှိ placeholder များကို အစားထိုး၍) အောက်ပါ အပိုဒ်တွင် ဖော်ပြထားသည့်အတိုင်း ထည့်သွင်းပါ။

4. (ရွေးချယ်နိုင်သည်) သင်သည် GitHub Codespaces ကို သုံးလျှင် အဆိုပါ repository နှင့် လက်စွဲသော _Codespaces secrets_ အဖြစ် environment variables များ သိမ်းဆည်းနိုင်သော်လည်း၊ ဒါမှမဟုတ် local တစ်ခုအဖြစ် `.env` ဖိုင် ပြင်ဆင်ရန် မလိုအပ်ပါ။ **သို့သော် ဒီရွေးချယ်မှုသည် GitHub Codespaces သုံးသောအခါသာ 작동ဖြစ်ပါသည်။** Docker Desktop အသုံးပြုပါက `.env` ဖိုင် ပြင်ဆင်ရလိမ့်မည်။

## `.env` ဖိုင် ဖြည့်စွက်ခြင်း

ဤအလိုက်သော Variable နာမည်များကို တင်ပြခြင်းဖြင့် ၎င်းတို့ ဖြစ်ရပ်ကို နားလည်ကြည့်မယ်။

| Variable  | ဖော်ပြချက်  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | သင်၏ပရိုဖိုင်တွင် တပ်ဆင်ထားသော အသုံးပြုခွင့် token |
| OPENAI_API_KEY | non-Azure OpenAI endpoint များသုံးရန် ဆွဲယူခွင့် key |
| AZURE_OPENAI_API_KEY | ဒီဝန်ဆောင်မှုသုံးရန် ခွင့်လက်မှတ် key |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI resource အသုံးပြုမှုအတွက် ဖွဲ့စည်းထားသော endpoint |
| AZURE_OPENAI_DEPLOYMENT | _စာသားဖန်တီးခြင်း_ မော်ဒယ် deployment endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _စာသားထိုးထင်မှု_ မော်ဒယ် deployment endpoint |
| AZURE_INFERENCE_ENDPOINT | Microsoft Foundry project အတွက် endpoint၊ Microsoft Foundry Models အတွက် အသုံးပြုသည် |
| AZURE_INFERENCE_CREDENTIAL | Microsoft Foundry project အတွက် API key |
| | |

မှတ်ချက်။ မတ်တပ်ရပ်များနှစ်ခုမှာ Azure OpenAI အတွက် chat completion (စာသားဖန်တီးခြင်း) နှင့် vector search (ထိုးထင်မှုများ) အတွက် ပြီးသားသတ်မှတ်ထားသော မော်ဒယ်များသည် အဓိကဖြစ်သည်။ ၎င်းတို့ကို သတ်မှတ်ရန် ညွှန်ကြားချက်များကို သတ်မှတ်ထားသော အစီအစဉ်များတွင် ဖော်ပြပါမည်။

## Azure OpenAI ကို ဖွဲ့စည်းခြင်း: Portal မှတစ်ဆင့်

> **မှတ်ချက်:** Azure OpenAI ဝန်ဆောင်မှုသည် ယခု [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ၏ အစိတ်ဖြစ်လာပါပြီ။ Azure Portal တွင် အရင်းအမြစ်များနှင့် ပြန့်နှံဖြန့်ဆဲများကို ယခုတုန်းလည်း တွေ့ရမည်၊ သို့သော် မော်ဒယ် စီမံခန့်ခွဲမှု (deployment, playground, ထိန်းသိမ်းမှု) ကို အဟောင်း "Azure OpenAI Studio" ထက် Foundry portal မှာသာ ဆောင်ရွက်မည်ဖြစ်သည်။

Azure OpenAI endpoint နှင့် key အချက်အလက်များကို Azure Portal မှာ တွေ့ကြုံနိုင်သည်၊ ထို့ကြောင့် အဲ့ဒီနေရာကစရအောင်။

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) သို့ သွားပါ။
1. Sidebar (ဘယ်ဘက် မီနူး) ထဲမှ **Keys and Endpoint** ကို နှိပ်ပါ။
1. **Show Keys** ကိုနှိပ်ပါ၊ KEY 1၊ KEY 2 နှင့် Endpoint ကိုတွေ့ရမည်။
1. KEY 1 ကို AZURE_OPENAI_API_KEY အတွက်အသုံးပြုပါ။
1. Endpoint ကို AZURE_OPENAI_ENDPOINT အတွက် အသုံးပြုပါ။

နောက်တစ်ဆင့်မှာ ကျွန်ုပ်တို့ ဖြန့်ချိထားသော မော်ဒယ်အတိုင်း endpoint များ လိုအပ်ပါသည်။

1. Azure OpenAI အရင်းအမြစ် (sidebar, ဘယ်ဘက်မီနူး) မှ **Model deployments** ကို နှိပ်ပါ။
1. နောက်ခံစာမျက်နှာတွင် **Go to Microsoft Foundry portal** (သို့) **Manage Deployments** ကို နှိပ်ပါ။

ဒီနေရာက Microsoft Foundry portal သို့ သွားမည်၊ အောက်တွင် ဖော်ပြထားသလို တခြား အချက်များကို ဒီမှာ ရှာဖွေလိမ့်မည်။

## Azure OpenAI ကို ဖွဲ့စည်းခြင်း: Microsoft Foundry portal မှတဆင့်

1. [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) သို့ သင့်ရဲ့ resource မှတစ်ဆင့် သွားပါ။
1. နောက်ခံအကြောင်းအရာ ဝင်ပါက **Deployments** tab ကို (sidebar, ဘယ်) နှိပ်ပါ။
1. သင့်မြင်မည့် မော်ဒယ် မရှိလျှင် **Deploy model** ကို နှိပ်ပြီး သင်ကြိုက်နှစ်သက်သော မော်ဒယ်တွေ (မော်ဒယ်ကတ်လော့ဂ်) မှ ဖြန့်ချိပါ။
1. _စာသားဖန်တီးမှု_ မော်ဒယ်တစ်ခု လိုအပ်မည်ဖြစ်ပြီး - သင့်အား **gpt-4o-mini** ကို အကြံပြုပါသည်။
1. _စာသားထိုးထင်မှု_ မော်ဒယ်တစ်ခုလည်း လိုအပ်ပြီး - **text-embedding-3-small** ကို အကြံပြုပါသည်။

ယခု environment variables များကို _Deployment name_ အား ပြောင်းလဲ ထားပါ။ ၎င်းသည် သာမန်အားဖြင့် သင်ပြောင်းလဲမထားလျှင် မော်ဒယ်နာမည်နှင့် တူသည်။ ဥပမာ အနေဖြင့် -

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**အလုပ်ပြီးလျှင် .env ဖိုင်ကို သိမ်းရန် မမေ့ပါနှင့်။** အဲဒီဖိုင်ထဲကနေ ထွက်ပြီး notebook လည်ပတ်ရေးညွှန်ကြားချက်သို့ ပြန်သွားနိုင်ပါပြီ။

## OpenAI ဖွဲ့စည်းခြင်း: ကိုယ်ရေးအချက်အလက်မှ

သင်၏ OpenAI API key ကို [OpenAI အကောင့်](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) တွင်တွေ့ရမည်။ မရှိလျှင် အကောင့်ဖွင့်ပြီး API key တစ်ခု ဖန်တီးနိုင်သည်။ ရရှိပြီးပါက `.env` ဖိုင်ရှိ `OPENAI_API_KEY` variable ထဲ ဖြည့်စွက်နိုင်သည်။

## Hugging Face ဖွဲ့စည်းခြင်း: ကိုယ်ရေးအချက်အလက်မှ

သင်၏ Hugging Face token ကို [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) တွင် သင်၏ ပရိုဖိုင် ဒေသအောက်မှာ တွေ့နိုင်သည်။ ၎င်းများအား အများပြည်သူနှင့် မမျှဝေပါနှင့်။ ဒီပရို့်ဂျက်အတွက် အသစ်တစ်ခု ဖန်တီးကာ `.env` ဖိုင်ရှိ `HUGGING_FACE_API_KEY` variable ထဲ ထည့်ပါ။ _မှတ်ချက်_ - ဒီ token ကို API key မဟုတ်သော်လည်း အတည်ပြုမှုအတွက် အသုံးပြုသော်လည်း နာမည်သတင်းစကားအနေဖြင့် ထိန်းသိမ်းထားသည်။

## Microsoft Foundry Models ဖွဲ့စည်းခြင်း: Portal မှတစ်ဆင့်

> **မှတ်ချက်:** GitHub Models သည် ၂၀၂၆ ခုနှစ် ဇူလိုင်လအဆုံးတွင် အဆုံးသတ်မည်ဖြစ်သည်။ Microsoft Foundry Models သည် အစားထိုးတင်ဆက်မှုဖြစ်ပြီး အခမဲ့စမ်းသပ်ရန် မော်ဒယ်ကတ်လော့ဂ်နှင့် Azure AI Inference SDK / OpenAI SDK အတွေ့အကြုံကို ထပ်မံပေးသည်။

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) သို့ သွား၍ Foundry project ကို ဖန်တီး (သို့) ဖွင့်ပါ။
1. [မော်ဒယ်ကတ်လော့ဂ်](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) တွင် ကြည့်ရှု၍ မော်ဒယ်တစ်ခု (ဥပမာ `gpt-4o-mini`) ကို ဖြန့်ချိပါ။
1. Project ရဲ့ **Overview** စာမျက်နှာတွင် **endpoint** နှင့် **API key** ကို ကူးယူပါ။
1. `.env` ဖိုင်တွင် `AZURE_INFERENCE_ENDPOINT` အတွက် endpoint တန်ဖိုးကို နှင့် `AZURE_INFERENCE_CREDENTIAL` အတွက် key ကို အသုံးပြုပါ။

## အော့ဖ်လိုင်း / ဒေသခံ ပရိုဗိုက်ဒါများ

လုံးဝ cloud subscription မလိုပါက မိမိစက်ပေါ်တွင် ကိုက်ညီသော အဖွင့်မော်ဒယ်များကို တိုက်ရိုက် အလုပ်လုပ်စေနိုင်သည်။

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft ၏ စက်ပေါ် runtime ဖြစ်ပြီး အကောင်းဆုံး execution provider (NPU, GPU, သို့မဟုတ် CPU) ကို အလိုအလျောက် ရွေးချယ်ပေးပြီး OpenAI-compatible endpoint ကို ရနေသည်၊ သင်သည် ဤသင်တန်းတွင် နမူနာကုဒ်များကို တစိတ်တပိုင်း ပြင်ဆင်မှုနည်းနည်းဖြင့် သုံးနိုင်သည်။ အစပြုရန် [Foundry Local မှတ်တမ်း](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) ကိုကြည့်ပါ၊ နောက်တစ်ခုမှာ `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) ဖြင့် ထည့်သွင်းနိုင်သည်။
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral, Gemma တို့ကဲ့သို့သော ဖွင့်မော်ဒယ်များကို ဒေသခံတွင် လည်ပတ်ရန် လူကြိုက်များသော ရွေးချယ်မှု


ရွေးချယ်စရာ နှစ်ခုစလုံးကို အသုံးပြု၍ လက်တွေ့လုပ်ဆောင်ချက်များအတွက် [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->