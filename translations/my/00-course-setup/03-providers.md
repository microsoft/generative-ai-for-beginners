# LLM ပံ့ပိုးသူ တစ်ဦးကို ရွေးချယ်ခြင်းနှင့် ပြင်ဆင်ခြင်း 🔑

အပ်မြစ်များကို OpenAI, Azure သို့မဟုတ် Hugging Face ကဲ့သို့ ဖြည့်ဆည်းပေးသော ဝန်ဆောင်မှုပံ့ပိုးသူများမှ တစ်ဆင့် တစ်ခု သို့မဟုတ် အများပြားသော ကြီးမားသော ဘာသာစကား မော်ဒယ် (LLM) ဖွဲ့စည်းတပ်ဆင်မှုများကို လုပ်ဆောင်ရန် ပြင်ဆင်နိုင်သည်။ ၎င်းတို့သည် ရိုက်ချက်မှန်သော ခွင့်ပြုချက်များ (API key သို့မဟုတ် token) ဖြင့် စီမံခြင်းဖြစ်သော _hosted endpoint_ (API) ကို ပရိုဂရမ်မှ လက်လှမ်းမှီနိုင်စေသည်။ ယင်းစာသင်ခန်းတွင် ကျွန်ုပ်တို့သည် ဒီပံ့ပိုးသူများ ကို ဆွေးနွေးပါမည်။

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) - မူလ GPT စီးရီး ရောနှောစုဆောင်းသော မော်ဒယ်များပါရှိသည်။
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) - OpenAI မော်ဒယ်များအတွက် စီးပွားရေးအသုံးပြုမှု အာရုံစူးစိုက်ထားသည်။
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) - OpenAI, Meta, Mistral, Cohere, Microsoft နှင့် အခြား မော်ဒယ် ၁ရာကျော်ကို တစ်ခုသော endpoint နှင့် API key ဖြင့် အလွယ်တကူ အသုံးပြုနိုင်သည် (GitHub Models အစားထိုး, ၂၀၂၆ ခုနှစ် ဇူလိုင် အဆုံးတွင် ပယ်ချ ထားမည်)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) - open-source မော်ဒယ်များနှင့် အကြံဉာဏ်ဆာဗာအတွက်
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) သို့မဟုတ် [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) - မည်သည့် cloud subscription မလိုအပ်ပဲ ကိုယ့် device ပေါ်တွင် မော်ဒယ်များကို အပြည့်အဝ offline အနေနှင့် ပြေးနိုင်ရန်

**ဤလေ့ကျင့်ခန်းများအတွက် သင်၏ ကိုယ်ပိုင်အကောင့်များကို အသုံးပြုရမည်။** အပ်မြစ်များသည် ရွေးချယ်စရာဖြစ်ပြီး သင်၏ စိတ်ဝင်စားမှုအရ တစ်ခု၊ အားလုံး သို့မဟုတ် တခုမှ မတခုကို ဦးစားပေးပြင်ဆင်နိုင်သည်။ အကောင့်ဖွင့်ရန် ညွှန်ကြားချက်အနည်းငယ်မှာ -

| အကောင့်ဖွင့်ရန် | ကုန်ကျစရိတ် | API Key | Playground | မှတ်ချက်များ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [စျေးနှုန်း](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | မော်ဒယ်များ များစွာ ရနိုင်ပါသည် |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [စျေးနှုန်း](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [အသုံးပြုခွင့် ရရှိရန် ကြိုတင်လျှောက်ထားရန် လိုအပ်သည်](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [စျေးနှုန်း](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Project Overview page](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | အခမဲ့ ကွက်တာ ရရှိနိုင်သည်; မော်ဒယ် ပံ့ပိုးသူများ အတွက် endpoint တစ်ခုနှင့် key တစ်ခု |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [စျေးနှုန်း](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat တွင် မော်ဒယ် ကန့်သတ်ချက်ရှိသည်](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | အခမဲ့ (သင့် device ပေါ်တွင် ပြေးဆိုင်သည်) | လိုအပ်မှုမရှိ | [Local CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | အပြည့်အဝ offline ဖြစ်ပြီး OpenAIညီတူ endpoint ဖြစ်သည် |
| | | | | |

ကွဲပြားသော ပံ့ပိုးသူများအတွက် ဒီ repository ကို _ပြင်ဆင်ရန်_ အောက်ပါ အညွှန်းများကို လိုက်နာပါ။ အထူးသတ်မှတ် ပံ့ပိုးသူတစ်ဦးလိုအပ်သော အပ်မြစ်များတွင် သင်၏ ဖိုင်နာမည်တွင် ဤ tag များထဲမှ တစ်ခု ပါရှိလိမ့်မည် -

- `aoai` - Azure OpenAI endpoint နှင့် key လိုအပ်သည်
- `oai` - OpenAI endpoint နှင့် key လိုအပ်သည်
- `hf` - Hugging Face token လိုအပ်သည်
- `githubmodels` - Microsoft Foundry Models endpoint နှင့် key လိုအပ်သည် (GitHub Models သည် ၂၀၂၆ ခုနှစ် ဇူလိုင် အဆုံးတွင် ပယ်ချ သွားမည်)

သင်သည် တစ်ခု, မတခုမှ မတခု, သို့မဟုတ် အားလုံးကို ပြင်ဆင်နိုင်သည်။ ဆက်စပ်သော အပ်မြစ်များတွင် လိုအပ်သည့် ခွင့်ပြုချက်များ မရှိပါက ပြဿနာဖြစ်နိုင်သည်။

## `.env` ဖိုင် ဖန်တီးခြင်း

ကျွန်ုပ်တို့သည် ထပ်ဆင့် ညွှန်ကြားချက်များကို ဖတ်ပြီး သက်ဆိုင်ရာ ပံ့ပိုးသူနှင့် အကောင့်ဖွင့်ပြီး လိုအပ်သော ခွင့်ပြုချက် ပစ္စည်းများ (API_KEY သို့မဟုတ် token) ရရှိထားကြောင်း ရှုမြင်ထားပါသည်။ Azure OpenAI ၏ အခြေအနေတွင်လည်း ဝန်ဆောင်မှု တပ်ဆင်ထားသည့် Azure OpenAI Service (endpoint) တစ်ခုနှင့် chat ပြီးမြောက်ရေးအတွက် GPT မော်ဒယ် တစ်ခု သို့မဟုတ် ပိုမို ကြီးမွန်းသော မော်ဒယ် တပ်ဆင်ထားကြောင်း အားလုံးကို သတ်မှတ်ထားပါသည်။

နောက်တစ်ဆင့်မှာ သင့်ရဲ့ **ဒေသခံ ပတ်ဝန်းကျင် ဇာတ်ညွှန်းများ** ကို ဒီအတိုင်း ပြင်ဆင်ပါ -

1. အမြစ်ဖိုလ်ဒါတွင် `.env.copy` ဖိုင်တစ်ခု ရှိကြောင်းကြည့်ပါ၊ ၎င်းတွင် အောက်ပါအတိုင်းမပါဝင်နိုင်သည် -

   ```bash
   # OpenAI ပံ့ပိုးသူ
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry တွင် Azure OpenAI
   ## (Azure OpenAI ဝန်ဆောင်မှုသည် ယခု Microsoft Foundry အစိတ်အပိုင်း ဖြစ်သည် - https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # ရယူထားသည့် စံစဉ်ကို သတ်မှတ်ပြီး! (လက်ရှိတည်ငြိမ်သော GA API ဗားရှင်း)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry ပုံစံများ (ပံ့ပိုးသူအများအပြား ပုံစံစာရင်း, GitHub ပုံစံများကို အစားထိုး, ၂၀၂၆ ခုနှစ် ဇူလိုင်လ အဆုံးတွင် ပိတ်သိမ်းမည်)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. အဲဒီဖိုင်ကို `.env` သို့ အောက်ပါ command ဖြင့် ကူးယူပါ။ ဤဖိုင်သည် _gitignore သတ်မှတ်ထားပြီး_ လျှို့ဝှက်ချက်များကို ကာကွယ်ပေးပါသည်။

   ```bash
   cp .env.copy .env
   ```

3. တန်ဖိုးများကို ဖြည့်ပါ (`=` ၏ ညာဘက်တွင်ရှိသော placeholder များကို အစားထိုး၍)၊ နောက်တစ်ပိုင်းတွင် ဖော်ပြထားသော နည်းပညာအရ။

4. (ရွေးချယ်မှု) သင်သည် GitHub Codespaces ကို အသုံးပြုပါက ဒီ repository နှင့် ဆက်နွယ်သော _Codespaces secrets_ အနေဖြင့် ပတ်ဝန်းကျင် ဇာတ်ညွှန်းများကို သိမ်းဆည်းနိုင်သည်။ ထိုအချိန်တွင် ဒေသခံ `.env` ဖိုင်ကို ပြင်ဆင်ရန် မလိုအပ်ပါ။ **သို့သော် ဤရွေးချယ်မှုသည် GitHub Codespaces အသုံးပြုသော အခါသာ လုပ်ဆောင်နိုင်သည်။** Docker Desktop ကိုအသုံးပြုပါက `.env` ဖိုင် ပြင်ဆင်ရမည်ဖြစ်သည်။

## `.env` ဖိုင် ပြည့်စုံစွာ ဖြည့်စွက်ခြင်း

သက်ဆိုင်ရာ variable အမည်များကို ရှုမြင်ကာ ၎င်းတို့၏ အဓိပ္ပါယ်ကို နားလည်ကြရအောင်။

| Variable  | ရည်ညွှန်းချက်  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | သုံးစွဲသူ access token၊ သင့်ပရိုဖိုင်တွင် ပြင်ဆင်ထားသည့်  token တန်ဖိုး |
| OPENAI_API_KEY | Azure မဟုတ်သော OpenAI endpoints များအသုံးပြုရာတွင် ခွင့်ပြုချက် key |
| AZURE_OPENAI_API_KEY | ကျွန်ုပ်တို့အသုံးပြုသော ဝန်ဆောင်မှု၏ ခွင့်ပြုချက် key |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI မှ တပ်ဆင်ထားသည့် endpoint |
| AZURE_OPENAI_DEPLOYMENT | _text generation_ မော်ဒယ် တပ်ဆင်မှု endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _text embeddings_ မော်ဒယ် တပ်ဆင်မှု endpoint |
| AZURE_INFERENCE_ENDPOINT | Microsoft Foundry project အတွက် endpoint၊ Microsoft Foundry Models အသုံးပြုသည် |
| AZURE_INFERENCE_CREDENTIAL | Microsoft Foundry project အတွက် API key |
| | |

မှတ်ချက် - နောက်ဆုံး Azure OpenAI ဇာတ်ညွှန်းနှစ်ခုသည် chat ပြီးမြောက်ရေး (text generation) နှင့် vector ရှာဖွေရေး (embeddings) အတွက် ပုံမှန်မော်ဒယ်များကို ကိုယ်စားပြုသည်။ ၎င်းတို့အား သက်ဆိုင်ရာ အပ်မြစ်များတွင် သတ်မှတ်မည်။

## Azure OpenAI ကို ပြင်ဆင်ခြင်း - Portal မှ

> **မှတ်ချက်:** Azure OpenAI ဝန်ဆောင်မှုသည် ယခု [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ၏ အစိတ်အပိုင်း ဖြစ်ပါသည်။ ရင်းမြစ်များနှင့် တပ်ဆင်မှုများ Azure Portal တွင်ထင်ရှားသေးပြီး လက်ရှိအချိန်တွင် မော်ဒယ် စီမံခန့်ခွဲမှု (တပ်ဆင်ခြင်း၊ playground, စောင့်ကြည့်မှု) မှာ Foundry Portal တွင်သာ ဖြစ်ပါသည်၊ ယခင် "Azure OpenAI Studio" ကို သီးသန့်သုံးခွင့်မရှိတော့ပါ။

Azure OpenAI endpoint နှင့် key တန်ဖိုးများကို [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) တွင် ရှာတွေ့နိုင်ပါသည်၊ ထို့ကြောင့်ဆိုလျှင် အဲဒီမှစလိုပါ။

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) သို့ သွားပါ
1. Sidebar (ဘယ်ဘက် menu) မှ **Keys and Endpoint** ကို နှိပ်ပါ။
1. **Show Keys** ကို နှိပ်ပါ - KEY 1, KEY 2 နှင့် Endpoint ကို မြင်ရပါမည်။
1. KEY 1 တန်ဖိုးကို AZURE_OPENAI_API_KEY အတွက် သုံးပါ
1. Endpoint တန်ဖိုးကို AZURE_OPENAI_ENDPOINT အတွက် သုံးပါ

လိုအပ်သည့် မော်ဒယ် အထူး endpoint များ ရယူရန် အောက်ပါအတိုင်း ဆက်လုပ်ပါ။

1. Azure OpenAI resource အတွက် sidebar (ဘယ်ဘက် menu) မှ **Model deployments** ကိုနှိပ်ပါ။
1. ရောက်ရှိသော စာမျက်နှာတွင် **Go to Microsoft Foundry portal** (သို့မဟုတ် **Manage Deployments**, သင်၏ resource အမျိုးအစား ပေါ်မူတည်၍) ကိုနှိပ်ပါ။

ယခု Microsoft Foundry portal သို့ သွားရောက်ပြီး အောက်ပါအတိုင်း တန်ဖိုးများ ရှာဖွေပါမည်။

## Azure OpenAI ကို ပြင်ဆင်ခြင်း - Microsoft Foundry portal မှ

1. အပေါ်ပါအတိုင်း သင်၏ resource မှ  [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) သို့ ရောက်ရှိပါ။
1. လက်ရှိတပ်ဆင်ထားသော မော်ဒယ်များကို ကြည့်ရန် sidebar (ဘယ်ဘက်) မှ **Deployments** ခလုတ်ကို နှိပ်ပါ။
1. သင်လိုချင်သော မော်ဒယ် မတပ်ဆင်ထားပါက [model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) မှ **Deploy model** ဖြင့် တပ်ဆင်နိုင်သည်။
1. _text-generation_ မော်ဒယ် တစ်ခုလိုအပ်ပါသည် - ကျွန်ုပ်တို့၏ အကြံပြုချက်မှာ: **gpt-5-mini**
1. _text-embedding_ မော်ဒယ်တစ်ခုလိုအပ်ပါသည် - ကျွန်ုပ်တို့၏ အကြံပြုချက်မှာ **text-embedding-3-small**

ယခု ပြင်ဆင်ထားသည့် _Deployment name_ ကို ပတ်ဝန်းကျင် ဇာတ်ညွှန်းတွင် ပြောင်းလဲပါ။ ၎င်းသည် မူလ မော်ဒယ်နာမည်နှင့် တူညီနေမည်ဟု မျှော်လင့်ပါသည်၊ သင် အမှန်တကယ် ပြောင်းလဲထားခြင်းမရှိပါက။ ဥပမာ အနေဖြင့် -

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**လုပ်ဆောင်ပြီးပါက .env ဖိုင်ကို သိမ်းဆည်းရန် မမေ့ပါနှင့်**။ ဖိုင်မှ ထွက်ပြီး notebook ကို လုပ်ဆောင်ရန် ညွှန်ကြားချက်များသို့ ပြန် သွားနိုင်ပါပြီ။

## OpenAI ကို ပြင်ဆင်ခြင်း - Profile မှ

သင့် OpenAI API key ကို သင့်၏ [OpenAI အကောင့်](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) တွင် ရှာဖွေနိုင်ပါသည်။ မရှိပါက အကောင့်ဖွင့်၍ API key တစ်ခုဖန်တီးနိုင်သည်။ key ရရှိပြီးပါက `.env` ဖိုင်ရှိ `OPENAI_API_KEY` variable အတွက် ဖြည့်သွင်းနိုင်ပါသည်။

## Hugging Face ကို ပြင်ဆင်ခြင်း - Profile မှ

သင့် Hugging Face token ကို သင့် ပရိုဖိုင်တွင် [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) အောက်တွင် ရှာဖွေနိုင်ပါသည်။ အများပြည်သူထံ မဖော်ပြပါနှင့် မမျှဝေရန် သတိပြုပါ။ ဤပရောဂျက်အတွက် အသုံးပြုရန် token အသစ်ဖန်တီးပြီး `.env` ဖိုင်ရှိ `HUGGING_FACE_API_KEY` variable တွင် ထည့်သွင်းပါ။ _မှတ်ချက်_ - ၎င်းသည် သိပ္ပံနည်းကျ API key မဟုတ်ပေမယ့် အသက်မွေးဝမ်းကျောင်းအတွက် သုံးသော token ဖြစ်သည်၊ ထို့ကြောင့် အမည်ပုံစံကို မပြောင်းလဲထားပါ။

## Microsoft Foundry Models ကို ပြင်ဆင်ခြင်း - Portal မှ

> **မှတ်ချက်:** GitHub Models သည် ၂၀၂၆ ခုနှစ် ဇူလိုင် အဆုံးတွင် ပယ်ချ သွားမည်ဖြစ်သည်။ Microsoft Foundry Models သည် တိုက်ရိုက် အစားထိုးရာဖြစ်ကာ အခမဲ့စမ်းသပ်နိုင်သည့် မော်ဒယ် များနှင့် Azure AI Inference SDK / OpenAI SDK အတွေ့အကြုံကို ဆက်လက် ပံ့ပိုးပေးပါသည်။

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) သို့သွား၍ Foundry project တစ်ခု ဖန်တီး (သို့မဟုတ် ဖွင့်) လုပ်ပါ။
1. [model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ကို သွားရောက် ကြည့်ရှု၍ မော်ဒယ်တစ်ခု (ဥပမာ `gpt-5-mini`) တပ်ဆင်ပါ။
1. Project ရဲ့ **Overview** စာမျက်နှာ၌ **endpoint** နှင့် **API key** ကို ကူးယူပါ။
1. `.env` ဖိုင်တွင် `AZURE_INFERENCE_ENDPOINT` အတွက် endpoint တန်ဖိုး၊ `AZURE_INFERENCE_CREDENTIAL` အတွက် key တန်ဖိုး ကို အသုံးပြုပါ။

## Offline / Local ပံ့ပိုးသူများ

မည်သည့် cloud subscription ကို မသုံးချင်ပါက ကိုယ်ပိုင် device ပေါ်တွင် တိုက်ရိုက် open မော်ဒယ်များ ကို ပြေး ဆောင်ရန် ဖြစ်သည်။

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft ၏ ပစ္စည်းပေါ်တွင် လုပ်ဆောင်သည့် runtime ဖြစ်သည်။ ၎င်းသည် အကောင်းဆုံး ထိန်းချုပ်မှု ပံ့ပိုးပေးသူ (NPU, GPU သို့မဟုတ် CPU) ကို အလိုအလျောက် ရွေးချယ်ပေးပြီး OpenAI-ညီတည့်သော endpoint ကို ဖော်ပြပေးသဖြင့် ဒီသင်ခန်းစာ၏ နမူနာကုဒ်များလည်း နည်းနည်းပြောင်းလဲမှုဖြင့် သုံးနိုင်သည်။ စတင်ရန် [Foundry Local အသုံးပြုခြင်း လမ်းညွှန်](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ပါ၊ သို့မဟုတ် `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) ဖြင့် ထည့်သွင်းနိုင်သည်။
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral, Gemma တို့ကဲ့သို့သော open မော်ဒယ်များကို ဒေသတြင်း၌ run ဖို့ နာမည်ကြီးသော နည်းလမ်း။


လက်တွေ့ အသုံးပြုနည်းများအတွက် [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->