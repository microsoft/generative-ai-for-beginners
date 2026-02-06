# LLM ပံ့ပိုးသူ ရွေးချယ်ခြင်းနှင့် ပြင်ဆင်ခြင်း 🔑

အလုပ်များကို OpenAI, Azure သို့မဟုတ် Hugging Face ကဲ့သို့ ပံ့ပိုးပေးသော ဝန်ဆောင်မှု ပံ့ပိုးသူတစ်ခု သို့မဟုတ် အများအပြားရှိသော ကြီးမားသော ဘာသာစကား မော်ဒယ် (LLM) တပ်ဆင်မှုများနှင့် အလုပ်လုပ်ရန် စီစဉ်နိုင်သည်။ ၎င်းတို့သည် ကျွန်ုပ်တို့ အတည်ပြုချက်မှန်ကန်မှု (API key သို့မဟုတ် token) ဖြင့် ပရိုဂရမ်ဖြင့် ဝင်ရောက် အသုံးပြုနိုင်သော _hosted endpoint_ (API) ကို ပံ့ပိုးပေးသည်။ ဤသင်တန်းတွင် ကျွန်ုပ်တို့သည် အောက်ပါ ပံ့ပိုးသူများကို ဆွေးနွေးပါမည်-

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) - core GPT စီးရီးအပါအဝင် မော်ဒယ်မျိုးစုံပါဝင်သည်။
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) - OpenAI မော်ဒယ်များအတွက် စီးပွားရေးအသုံးပြုမှုအတွက် အာရုံစိုက်ထားသည်။
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) - open-source မော်ဒယ်များနှင့် inference server အတွက်။

**ဤလေ့ကျင့်ခန်းများအတွက် သင်၏ ကိုယ်ပိုင် အကောင့်များကို အသုံးပြုရမည်ဖြစ်သည်။** အလုပ်များသည် ရွေးချယ်စရာဖြစ်ပြီး သင်၏ စိတ်ဝင်စားမှုအပေါ် မူတည်၍ တစ်ခု၊ အားလုံး သို့မဟုတ် မည်သည့် ပံ့ပိုးသူမျှ မတပ်ဆင်နိုင်ပါ။ စာရင်းသွင်းခြင်းအတွက် အကြံပြုချက်အချို့-

| စာရင်းသွင်းခြင်း | ကုန်ကျစရိတ် | API Key | Playground | မှတ်ချက်များ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [စျေးနှုန်း](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | မော်ဒယ်များစွာ ရရှိနိုင်သည် |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [စျေးနှုန်း](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [အသုံးပြုခွင့် ရယူရန် ကြိုတင်လျှောက်ထားရမည်](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [စျေးနှုန်း](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat တွင် မော်ဒယ်ကန့်သတ်ချက်ရှိသည်](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

အောက်ပါ ညွှန်ကြားချက်များအတိုင်း ဤ repository ကို မတူညီသော ပံ့ပိုးသူများနှင့် အသုံးပြုရန် _ပြင်ဆင်_ ပါ။ သတ်မှတ်ထားသော ပံ့ပိုးသူတစ်ခုလိုအပ်သော အလုပ်များတွင် ဖိုင်နာမည်တွင် အောက်ပါ tag များထဲမှ တစ်ခုပါရှိမည်-

- `aoai` - Azure OpenAI endpoint နှင့် key လိုအပ်သည်
- `oai` - OpenAI endpoint နှင့် key လိုအပ်သည်
- `hf` - Hugging Face token လိုအပ်သည်

သင်သည် တစ်ခု၊ မည်သည့်ပံ့ပိုးသူမျှ မတပ်ဆင်နိုင်သလို အားလုံးကိုလည်း ပြင်ဆင်နိုင်သည်။ ဆက်စပ် အလုပ်များတွင် အတည်ပြုချက် မရှိပါက error ဖြစ်မည်ဖြစ်သည်။

## `.env` ဖိုင် ဖန်တီးခြင်း

အထက်ပါ ညွှန်ကြားချက်များကို ဖတ်ပြီး သင့်အား သက်ဆိုင်ရာ ပံ့ပိုးသူနှင့် စာရင်းသွင်းပြီး လိုအပ်သော အတည်ပြုချက်များ (API_KEY သို့မဟုတ် token) ရရှိထားကြောင်း သတ်မှတ်ထားသည်။ Azure OpenAI ၏ အခြေအနေတွင် သင်တွင် Azure OpenAI Service (endpoint) တစ်ခုတပ်ဆင်ပြီး GPT မော်ဒယ်တစ်ခုထက်ပို chat completion အတွက် တပ်ဆင်ထားကြောင်းလည်း သတ်မှတ်ထားသည်။

နောက်တစ်ဆင့်မှာ သင့် **ဒေသခံ ပတ်ဝန်းကျင် အပြောင်းအလဲများ** ကို အောက်ပါအတိုင်း ပြင်ဆင်ရမည်-

1. root ဖိုလ်ဒါတွင် `.env.copy` ဖိုင်ရှိသည်ကို ကြည့်ပါ၊ ၎င်းတွင် အောက်ပါအတိုင်း ပါဝင်သည်-

   ```bash
   # OpenAI ပံ့ပိုးသူ
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # ပုံမှန်တန်ဖိုး သတ်မှတ်ပြီးပါပြီ!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. အောက်ပါ command ဖြင့် ဖိုင်ကို `.env` သို့ ကူးယူပါ။ ဤဖိုင်သည် _gitignore-d_ ဖြစ်ပြီး လျှို့ဝှက်ချက်များကို ကာကွယ်ထားသည်။

   ```bash
   cp .env.copy .env
   ```

3. နောက်ပိုင်း အပိုင်းတွင် ဖော်ပြထားသည့်အတိုင်း တန်ဖိုးများကို ဖြည့်ပါ (`=` ဘေးရှိ placeholder များကို အစားထိုးပါ)။

4. (ရွေးချယ်စရာ) GitHub Codespaces ကို အသုံးပြုပါက ဤ repository နှင့် ဆက်စပ် Codespaces secrets အဖြစ် ပတ်ဝန်းကျင် အပြောင်းအလဲများကို သိမ်းဆည်းနိုင်သည်။ ထိုအခါ ဒေသခံ .env ဖိုင် တပ်ဆင်ရန် မလိုအပ်ပါ။ **သို့သော် ဤရွေးချယ်စရာသည် GitHub Codespaces ကိုသာ အသုံးပြုပါကသာ အလုပ်လုပ်သည်။** Docker Desktop ကို အသုံးပြုပါက .env ဖိုင်ကို ထပ်မံ ပြင်ဆင်ရမည်ဖြစ်သည်။

## `.env` ဖိုင် ဖြည့်စွက်ခြင်း

အောက်ပါ variable အမည်များကို ကြည့်ပြီး ၎င်းတို့၏ အဓိပ္ပါယ်ကို နားလည်ကြည့်ကြမည်-

| Variable  | ဖော်ပြချက်  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | သင့်ပရိုဖိုင်တွင် သတ်မှတ်ထားသော အသုံးပြုသူ access token ဖြစ်သည် |
| OPENAI_API_KEY | non-Azure OpenAI endpoint များအတွက် ဝန်ဆောင်မှု အသုံးပြုခွင့် key ဖြစ်သည် |
| AZURE_OPENAI_API_KEY | ၎င်းဝန်ဆောင်မှု အသုံးပြုခွင့် key ဖြစ်သည် |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI resource အတွက် တပ်ဆင်ထားသော endpoint ဖြစ်သည် |
| AZURE_OPENAI_DEPLOYMENT | _text generation_ မော်ဒယ် တပ်ဆင်မှု endpoint ဖြစ်သည် |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _text embeddings_ မော်ဒယ် တပ်ဆင်မှု endpoint ဖြစ်သည် |
| | |

မှတ်ချက်- နောက်ဆုံး Azure OpenAI variable နှစ်ခုသည် chat completion (text generation) နှင့် vector search (embeddings) အတွက် ပုံမှန် မော်ဒယ်များကို ကိုယ်စားပြုသည်။ ၎င်းတို့ကို သတ်မှတ်ရန် ညွှန်ကြားချက်များကို ဆက်စပ် အလုပ်များတွင် ဖော်ပြမည်ဖြစ်သည်။

## Azure ကို ပြင်ဆင်ခြင်း: Portal မှ

Azure OpenAI endpoint နှင့် key တန်ဖိုးများကို [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) တွင် ရှာဖွေနိုင်သည်၊ ထို့ကြောင့် အဲဒီနေရာမှ စတင်ကြရအောင်။

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) သို့ သွားပါ။
1. Sidebar (ဘယ်ဘက် မီနူး) တွင် **Keys and Endpoint** ရွေးချယ်ပါ။
1. **Show Keys** ကို နှိပ်ပါ - KEY 1, KEY 2 နှင့် Endpoint ကို မြင်ရမည်။
1. AZURE_OPENAI_API_KEY အတွက် KEY 1 တန်ဖိုးကို အသုံးပြုပါ။
1. AZURE_OPENAI_ENDPOINT အတွက် Endpoint တန်ဖိုးကို အသုံးပြုပါ။

နောက်တစ်ဆင့်မှာ တပ်ဆင်ထားသော မော်ဒယ်များအတွက် endpoint များလိုအပ်သည်။

1. Azure OpenAI resource အတွက် sidebar (ဘယ်ဘက် မီနူး) တွင် **Model deployments** ကို နှိပ်ပါ။
1. ရောက်ရှိသော စာမျက်နှာတွင် **Manage Deployments** ကို နှိပ်ပါ။

ဤနေရာတွင် Azure OpenAI Studio ဝက်ဘ်ဆိုက်သို့ သွားရောက်ပြီး အောက်ပါအတိုင်း တန်ဖိုးများကို ရှာဖွေနိုင်မည်ဖြစ်သည်။

## Azure ကို ပြင်ဆင်ခြင်း: Studio မှ

1. အထက်ဖော်ပြသည့်အတိုင်း သင့် resource မှ [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) သို့ သွားပါ။
1. လက်ရှိ တပ်ဆင်ထားသော မော်ဒယ်များကို ကြည့်ရန် sidebar (ဘယ်ဘက်) တွင် **Deployments** tab ကို နှိပ်ပါ။
1. သင်လိုချင်သော မော်ဒယ် မတပ်ဆင်ထားပါက **Create new deployment** ကို အသုံးပြု၍ တပ်ဆင်ပါ။
1. _text-generation_ မော်ဒယ်တစ်ခု လိုအပ်မည် - ကျွန်ုပ်တို့ အကြံပြုသည်မှာ **gpt-35-turbo** ဖြစ်သည်။
1. _text-embedding_ မော်ဒယ်တစ်ခု လိုအပ်မည် - ကျွန်ုပ်တို့ အကြံပြုသည်မှာ **text-embedding-ada-002** ဖြစ်သည်။

ယခု _Deployment name_ ကို အသုံးပြု၍ ပတ်ဝန်းကျင် အပြောင်းအလဲများကို အပ်ဒိတ်လုပ်ပါ။ ၎င်းသည် မော်ဒယ်အမည်နှင့် တူညီသော အမည်ဖြစ်နိုင်သည်၊ သို့မဟုတ် သင် တိတိကျကျ ပြောင်းလဲထားနိုင်သည်။ ဥပမာအနေဖြင့်-

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**ပြီးဆုံးပါက .env ဖိုင်ကို သိမ်းဆည်းရန် မမေ့ပါနှင့်**။ ဖိုင်မှ ထွက်ပြီး notebook ကို လည်ပတ်ရန် ညွှန်ကြားချက်များသို့ ပြန်သွားနိုင်ပါပြီ။

## OpenAI ကို ပြင်ဆင်ခြင်း: Profile မှ

သင့် OpenAI API key ကို သင့် [OpenAI အကောင့်](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) တွင် ရှာဖွေနိုင်သည်။ မရှိပါက အကောင့်သစ် ဖွင့်ပြီး API key တစ်ခု ဖန်တီးနိုင်သည်။ key ရရှိပြီးပါက `.env` ဖိုင်ရှိ `OPENAI_API_KEY` variable တွင် ထည့်သွင်းနိုင်သည်။

## Hugging Face ကို ပြင်ဆင်ခြင်း: Profile မှ

သင့် Hugging Face token ကို သင့်ပရိုဖိုင်အောက်ရှိ [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) တွင် ရှာဖွေနိုင်သည်။ ၎င်းကို အများသို့ မဖော်ပြရန် သတိပြုပါ။ ၎င်းကို ဤ project အတွက် အသစ်တစ်ခု ဖန်တီးပြီး `.env` ဖိုင်ရှိ `HUGGING_FACE_API_KEY` variable တွင် ကူးယူထည့်သွင်းပါ။ _မှတ်ချက်_ - ၎င်းသည် နည်းပညာပိုင်းဆိုင်ရာ API key မဟုတ်သော်လည်း အတည်ပြုမှုအတွက် အသုံးပြုသည်၊ ထို့ကြောင့် အမည်ပုံစံကို တူညီစေရန် ထိုအတိုင်း ထားရှိထားသည်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများ သို့မဟုတ် မှားဖတ်ရှုမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->