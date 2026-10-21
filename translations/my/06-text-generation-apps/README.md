# စာသား ဖန်တီးမှုလျှောက်လွှာများ တည်ဆောက်ခြင်း

[![စာသား ဖန်တီးမှုလျှောက်လွှာများ တည်ဆောက်ခြင်း](../../../translated_images/my/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(ဤသင်ခန်းစာရဲ့ ဗီဒီယိုကိုကြည့်ရန် အပေါ်ဓါတ်ပုံကို နှိပ်ပါ)_

သင်ဒီ သင်ခန်းစာစဉ်တွင် ယခုထိတွေ့မြင်ခဲ့သည့်အချက်မှာ prompt များကဲ့သို့ အချက်အလက်ဆန်းသစ်မှုအဓိက အစိတ်အပိုင်းများနှင့် "prompt engineering" ဟုခေါ်သော စနစ်တကျရှိသည်ဖြစ်သည်။ ChatGPT, Office 365, Microsoft Power Platform နှင့် အခြားကိရိယာများစွာသည် သင်တို့အား prompt များကိုအသုံးပြု၍ တစ်ခုခုအောင်မြင်စေသည်။

မိမိအက်ပ်တစ်ခုတွင် ဒီကဲ့သို့ အတွေ့အကြုံ ထည့်သွင်းရန်၊ prompt များ၊ completion များကဲ့သို့သော အယူအဆများအား နားလည်ခြင်းနှင့် အချက်အလက်လုပ်ဆောင်ရန် သုံးဆောင်ရန် စာကြည့်တိုက်တစ်ခု ရွေးချယ်ရန် လိုအပ်သည်။ ၎င်းကို အမြဲသင်ယူမည့်အပိုင်းဖြစ်သည်။

## နိဒါန်း

ဤအပိုင်းတွင် သင်သည်-

- openai စာကြည့်တိုက်နှင့် ၎င်း၏ အဓိက အယူအဆများကို သင်ယူမည်။
- openai သုံး၍ စာသား ဖန်တီးမှုအက်ပ်တစ်ခု တည်ဆောက်မည်။
- prompt, temperature, tokens ကဲ့သို့ အယူအဆများကို အသုံးပြုကာ စာသား ဖန်တီးမှုအက်ပ်တစ်ခု ဘယ်လိုတည်ဆောက်မည်ကို နားလည်မည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤသင်ခန်းစာ အဆုံးတွင် သင်သည်-

- စာသား ဖန်တီးမှု အက်ပ်ဆိုတာဘာလဲ ဆိုတာ ရှင်းလင်းတင်ပြနိုင်မည်။
- openai သုံး၍ စာသား ဖန်တီးမှု အက်ပ်တစ်ခု တည်ဆောက်နိုင်မည်။
- ထွက်ရှိသည့် စာသားသည် မတူညီမှုရှိစေရန် အက်ပ်တွင် tokens အရေအတွက်ပိုမိုသို့မဟုတ်နည်းချင်ခြင်းနှင့် temperature ကို ပြင်ဆင်နိုင်မည်။

## စာသား ဖန်တီးမှု အက်ပ် ဆိုတာဘာလဲ?

သာမန်အားဖြင့် အက်ပ်တစ်ခုတည်ဆောက်သောအခါ အောက်ပါအတိုင်း မျက်နှာပြင်တစ်မျိုးရှိသည်။

- ကော်မဏ့်ဖြင့် အုပ်ချုပ်မှု။ Console အက်ပ်များသည်ကိရိယာကို အသုံးပြု၍ အမိန့်ရေးသားဆောင်ရွက်ခြင်းဖြင့် တာဝန်တစ်ခုကို ပြီးမြောက်စေသည်။ ဥပမာအားဖြင့် `git` သည် ကော်မဏ့် အခြေပြု အက်ပ်တစ်ခုဖြစ်သည်။
- အသုံးပြုသူ မျက်နှာပြင် (UI)။ အချို့အက်ပ်များတွင် ပုံစံဆွဲထားသော အသုံးပြုသူမီနူးများ (GUI) ရှိပြီး ခလုတ်များကိုနှိပ်ခြင်း၊ စာသားထည့်သွင်းခြင်း၊ ရွေးချယ်မှုများ ပြုလုပ်ခြင်း စသဖြင့် ဆောင်ရွက်နိုင်သည်။

### Console နှင့် UI အက်ပ်များမှာ ကန့်သတ်ချက်ရှိသည်

ကော်မဏ့်ရိုက်ထည့်ရသော အက်ပ်တစ်ခုနှင့် နှိုင်းယှဉ်ပါ-

- **ကန့်သတ်ချက်ရှိသည်**။ မည်သည့်အမိန့်မဆိုရိုက်ထည့်၍ မရပါ၊ အက်ပ်ကအစစ်မှန် ထောက်ခံသည့် ကော်မဏ့်များသာအသုံးပြုနိုင်သည်။
- **ဘာသာစကားသီးသန့်ဖြစ်သည်**။ အချို့အက်ပ်များသည် ဘာသာစကားစုံ အထောက်အပံ့ပေးသော်လည်း ပုံမှန်အားဖြင့် သီးသန့်ဘာသာစကားတစ်ခုအတွက်တည်ဆောက်ထားပြီး နောက်ထပ် ဘာသာစကားများထည့်သွင်းနိုင်သည်။

### စာသား ဖန်တီးမှု အက်ပ်များ၏ အကျိုးကျေးဇူးများ

စာသား ဖန်တီးမှု အက်ပ်မျိုးက ဘယ်လိုကွာခြားသနည်း?

စာသား ဖန်တီးမှု အက်ပ်တွင် သင်အတွက် ပိုမိုလွယ်ကူသုံးနိုင်ခြင်းရှိပြီး အတိအကျ ကော်မဏ့်တစ်စုသို့မဟုတ် သီးသန့်Input ဘာသာစကားတစ်ခုတည်းမဟုတ်ပါ။ ၎င်းနေရာတွင် သဘာဝ ဘာသာစကားကို အသုံးပြု၍ အက်ပ်နှင့် ဆက်သွယ်နိုင်သည်။ ထို့အပြင် သင်အသုံးပြုပြီးသား အချက်အလက်အရင်းအမြစ်သည် ဗဟိုပြု စုစည်းထားသော သတင်းအချက်အလက်များ၏ ပြည့်ဝမှု့ကို စက်သင်ခန်းတက်၍ စီမံထားသော data ဖြစ်ပြီး ပရိတ်သတ်စာရင်းကို စီမံထားသော ပုံမှန်အက်ပ်များ၏ ဒေတာအခြေခံများနှင့် ကန့်သတ်မှုရှိသည်။

### စာသား ဖန်တီးမှု အက်ပ်ဖြင့် ဘာတွေ တည်ဆောက်နိုင်သလဲ?

သင်တည်ဆောက်နိုင်သည့် အရာများ ပိုများသည်။ ဥပမာ-

- **Chatbot**။ ကုမ္ပဏီနှင့် ထုတ်ကုန်များအကြောင်း မေးခွန်းများကို ဖြေကြားပေးနိုင်သော Chatbot တစ်ခုကို တည်ဆောက်နိုင်သည်။
- **အကူအညီပေးသူ**။ LLM များသည် စာတမ်းအနှစ်ချုပ်ခြင်း၊ စာသားမှ လမ်းညွှန်ချက်ရယူခြင်း၊ စာသားဖန်တီးခြင်း (ပြန်ကြားစာများအပါအဝင်) ကဲ့သို့သောအရာများတွင် ထူးခြားသည်။
- **ကုဒ် အကူအညီပေးသူ**။ သင်အသုံးပြုမည့် ဘာသာစကားပုံစံအပေါ် မူတည်၍ ကုဒ်ရေးသားရာတွင် အကူအညီပေးသည့် အကူအညီပေးသူကို တည်ဆောက်နိုင်သည်။ ဥပမာအားဖြင့် GitHub Copilot နှင့် ChatGPT ကို ကုဒ်ရေးသားရာတွင် အသုံးပြုနိုင်သည်။

## ဘယ်လို စတင်မလဲ?

အားလုံးအတွက် LLM နှင့် ပေါင်းစပ်ရန် နည်းလမ်း နှစ်မျိုးရှိသည် -

- API ကို အသုံးပြုရန်။ ဤနေရာတွင် သင်၏ prompt ဖြင့် web request များ ဖန်တီးပြီး ထုတ်ပေးထားသော စာသားများကို ပြန်လည်ရရှိပါမည်။
- စာကြည့်တိုက်တစ်ခုကို သုံးရန်။ စာကြည့်တိုက်များသည် API call များကို ထုပ်ပိုးကာ အသုံးပြုရန် ပိုလွယ်ကူစေသည်။

## စာကြည့်တိုက်များ/SDK များ

LLM များနှင့် လုပ်ဆောင်ရာတွင် လူသိများသော စာကြည့်တိုက်အချို့မှာ -

- **openai**၊ ၎င်းသည် သင့်မော်ဒယ်နှင့် ချိတ်ဆက်၍ prompt များ ပို့ရန် လွယ်ကူစေသည်။

ထို့အပြင် အဆင့်မြင့် စာကြည့်တိုက်များမှာ -

- **Langchain**။ Langchain သည် လူသိများပြီး Python ကို ထောက်ခံသည်။
- **Semantic Kernel**။ Semantic Kernel သည် Microsoft မှ ထုတ်လုပ်ပေးသော စာကြည့်တိုက်ဖြစ်ပြီး C#, Python, Java ဘာသာစကားများကို ထောက်ခံသည်။

## openai သုံး၍ ပထမဆုံး အက်ပ်တည်ဆောက်ခြင်း

ပထမဆုံး အက်ပ်တည်ဆောက်ပုံ၊ လိုအပ်သည့် စာကြည့်တိုက်များ၊ အထောက်အပံ့များကို ကြည့်လိုက်ရအောင်။

### openai ကို စနစ်တကျ ထည့်သွင်းခြင်း

OpenAI သို့မဟုတ် Azure OpenAI နှင့် ဆက်သွယ်ရန် စာကြည့်တိုက်များစွာ ရှိသည်။ C#, Python, JavaScript, Java နှင့် အခြား ဘာသာစကားများဖြင့် အသုံးပြုနိုင်ပါသည်။ ကျွန်တော်တို့ သဘောတူသည့် Python စာကြည့်တိုက် `openai` ကို သုံးမည့်အတွက် `pip` ဖြင့် ထည့်သွင်းမည်။

```bash
pip install openai
```

### အရင်းအမြစ် တည်ဆောက်ခြင်း

အောက်ပါ အဆင့်များကို ဆောင်ရွက်ရန် လိုအပ်သည် -

- Azure ပေါ်တွင် အကောင့်ဖွင့်ပါ [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)။
- Azure OpenAI အတွက် ဝင်ကြည့်ခွင့်ရပါသည်။ [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) သို့ သွား၍ ခွင့်တောင်းပါ။

  > [!NOTE]
  > ရေးသားချိန်တွင် Azure OpenAI အတွက် ဝင်ကြည့်ခွင့် တောင်းဆိုရသည်။

- Python ထည့်သွင်းပါ <https://www.python.org/>
- Azure OpenAI Service အရင်းအမြစ် တစ်ခုကို ဖန်တီးထားရမည်။ [အရင်းအမြစ် ဖန်တီးခြင်း](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst) သည့် လမ်းညွှန်ကို ကြည့်ပါ။

### API Key နှင့် Endpoint ရှာဖွေရန်

ယခုအချိန်၌ သင်၏ `openai` စာကြည့်တိုက်ကို ဘယ် API Key ကို သုံးမည်ဆိုသည်ကို ပြောပြရန် လိုအပ်သည်။ သင့် API Key ကို ရှာဖွေရန် Azure OpenAI အရင်းအမြစ်၏ "Keys and Endpoint" အခန်းတွင် သွားကာ "Key 1" အမျိုးအစားကို မိတ္တူကူးပါ။

![Azure Portal တွင် Keys and Endpoint resource blade](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

အချက်အလက်များကို မိတ္တူကူးပြီးနောက် စာကြည့်တိုက်များကို အသုံးပြုရန်ညွှန်ကြားပါ။

> [!NOTE]
> သင်၏ API Key ကို ကုဒ်နှင့်ခြားတကျထား သင့်သည်။ environment variable များမှတဆင့် ထားရှိနိုင်ပါသည်။
>
> - environment variable `OPENAI_API_KEY` ကို သင့် API Key ဖြင့် သတ်မှတ်ပါ။
>   `export OPENAI_API_KEY='sk-...'`

### Azure အတွက် ပြင်ဆင်မှုများ

သင်သည် Azure OpenAI (ယခင် Microsoft Foundry ၏ အစိတ်အပိုင်းတစ်ခု) ကို အသုံးပြုနေပါက ပြင်ဆင်မှု သဘောတူစာရင်းအတိုင်းဆောင်ရွက်ပါ။ ကျွန်တော်တို့သည် ရိုးရိုး `OpenAI` client ကို Azure OpenAI `/openai/v1/` endpoint ကို ညွှန်ပြပေးပြီး Responses API နှင့်အတူ အလုပ်လုပ်စေသော အသုံးပြုမှုဖြစ်ပါတယ်။ `api_version` မလိုအပ်ပါ။

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

အထက်တွင် ဤအရာများကို သတ်မှတ်ထားသည် -

- `api_key`၊ Azure Portal သို့မဟုတ် Microsoft Foundry portal မှ သိရှိသော သင့် API key ဖြစ်သည်။
- `base_url`၊ သင့် Foundry resource endpoint ဖြစ်ပြီး `/openai/v1/` ဖြင့် ပေါင်းထည့်ထားသည်။ stable v1 endpoint သည် OpenAI နှင့် Azure OpenAI နှစ်ခုတွင်ပါ အလုပ်လုပ်ပြီး `api_version` မလိုအပ်ပါ။

> [!NOTE] > `os.environ` သည် environment variable များကို ဖတ်ရှုနိုင်သည်။ `AZURE_OPENAI_API_KEY` နှင့် `AZURE_OPENAI_ENDPOINT` နဲ့ environment variable များ ဖတ်ရန် အသုံးပြုနိုင်သည်။ terminal မှ သို့မဟုတ် `dotenv` ကဲ့သို့စာကြည့်တိုက်သုံး၍ မိမိ ဆက်တင်များ ထားနိုင်သည်။

## စာသား ဖန်တီးမှု

စာသားဖန်တီးရန် နည်းလမ်းမှာ Responses API ကို `responses.create` နည်းလမ်းဖြင့် အသုံးပြုခြင်းဖြစ်သည်၊ ဥပမာတစ်ခုမှာ -

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

အထက်ပါ ကုဒ်တွင် response တစ်ခု ထုတ်လုပ်ပြီး မော်ဒယ်နှင့် prompt ဖြင့် ပေးပို့သည်။ ထို့နောက် `response.output_text` ဖြင့် ထုတ်ပေးသော စာသားကို ပြင့်နှုတ်ပြပါသည်။

### နှစ်ခုထပ်မိန့်ဖြေပြောဆိုချက်များ

Responses API သည် single-turn စာသားဖန်တီးခြင်းနှင့် multi-turn chatbot များနှစ်မျိုးလုံးအတွက် သင့်တော်သည် - ပြောဆိုချက်များကို `input` ထဲတွင် စာရင်းကောက် ဖန်တီးတင်ပြပါ။

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

ဤ လုပ်ဆောင်မှုအကြောင်း မနက်ဖြန်ဖော်ပြမည့်အပိုင်းတစ်ခုတွင် နောက်ထပ်ရှင်းလင်းသွားပါမည်။

## လေ့ကျင့်ခန်း - သင့် ပထမစာသားဖန်တီးမှုအက်ပ်

openai ကို ပြင်ဆင်ခြင်းနှင့် စတင်လုပ်ဆောင်ခြင်းသေချာသွားပြီဆိုရင်၊ သင့် ပထမ စာသားဖန်တီးမှု အက်ပ်ကို တည်ဆောက်စဉ်ဖြစ်သည်။ အောက်ပါအဆင့်များကို လိုက်နာပါ -

1. Virtual environment တစ်ခု ဖန်တီးပြီး openai ကို ထည့်သွင်းပါ:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows ကို သုံးနေပါက `venv\Scripts\activate` ကို `source venv/bin/activate` အစားရိုက်ပါ။

   > [!NOTE]
   > Azure OpenAI key ကို ရှာရန် [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) သို့ သွားပြီး `Open AI` ရှာပါ၊ `Open AI resource` ရွေးချယ်ပြီး `Keys and Endpoint` နှိပ်၍ `Key 1` ကို မိတ္တူကူးပါ။

1. _app.py_ ဖိုင်ကို ဖန်တီးပြီး အောက်ပါ ကုဒ် ထည့်သွင်းပါ:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make a request using the Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # print response
   print(response.output_text)
   ```

   > [!NOTE]
   > သင် plain OpenAI (Azure မဟုတ်) သုံးပါက `client = OpenAI(api_key="<replace this value with your OpenAI key>")` ကို ( `base_url` မလို) သုံးပြီး မော်ဒယ်အမည် (ဥပမာ `gpt-5-mini`) ကို deployment နေရာတွင် တစ်သက်တမ်း အသုံးပြုပါ။

   သင်သည် အောက်ပါအတိုင်း ထွက်ရှိမှုကို တွေ့မည် -

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## ကွဲပြားသည့် prompt အမျိုးအစားများ၊ မတူညီသည့် လုပ်ငန်းများအတွက်

ယခု သင် prompt ဖြင့် စာသား ဖန်တီးနည်းကို ကြည့်ရှုသင်ယူပြီး ဖြစ်သည်။ သင်သည် ဤနေရာတွင် မြှင့်တင်ပြီး စမ်းသပ်ပြီး မတူညီသော စာသားအမျိုးအစားများ ဖန်တီးနိုင်သော အပလီကေးရှင်း လက်ရှိလုပ်ဆောင်နေပြီဖြစ်သည်။

Prompt များကို အမျိုးမျိုး အလုပ်များအတွက် အသုံးပြုနိုင်သည်။ ဥပမာ -

- **စာသားအမျိုးအစား ဖန်တီးခြင်း**။ ဥပမာ၊ ကဗျာတစ်ပုဒ်၊ ရွေးကောက်ပြိုင်ပွဲမေးခွန်းများ စသည်ဖြင့် ဖန်တီးနိုင်သည်။
- **အချက်အလက် ရှာဖွေခြင်း**။ 'web development တွင် CORS ဆိုသည်မှာ ဘာဆိုသည်?' ကဲ့သို့ အချက်အလက် ရှာဖွေရန် prompt များကို အသုံးပြုနိုင်သည်။
- **ကုဒ် ဖန်တီးခြင်း**။ email မှန်ကန်မှု အတည်ပြုရန် regular expression တည်းဖြတ်မှုနှင့်ကဲ့သို့သောကုဒ်ရေးသားမှုကို ပေးနိုင်သည်။ သို့မဟုတ် တစ်လုံးပြည့် Web app တစ်ခု လည်း ဖန်တီးနိုင်သည်။

## အသုံးဝင်သည့် လက်တွေ့အသုံးပြုမှု များ: ဟင်းလျာဖန်တီးခြင်း

မိမိအိမ်၌ ပါဝင်ပစ္စည်းများ ရှိပြီး မုန့်ဟင်းခါး တစ်ခုချက်ချင်သည်။ ၎င်းအတွက်ဟင်းလျာလိုအပ်သည်။ ဟင်းလျာရှာဖွေရန် နည်းလမ်းတစ်ခုမှာ ရှာဖွေရေးစက်သုံးခြင်း သို့မဟုတ် LLM တစ်ခုကို အသုံးပြုခြင်း ဖြစ်သည်။

အောက်ပါအတိုင်း prompt တစ်ခုရေးနိုင်သည်။

> "အောက်ပါ ပါဝင်ပစ္စည်းများပါဝင်သည့် အစားအစာအမျိုးအစား ၅ မျိုးပြပါ- ကြက်သား၊ ဂေါ်ဖီ၊ မျှစေ့။ ဟင်းလျာ တစ်ခုစီတွင် ပါဝင်ပစ္စည်းအားလုံးကို ပြပါ။"

အထက်ဖော်ပြချက် prompt အရ တုံ့ပြန်ချက် အောက်ပါအတိုင်း ဖြစ်နိုင်သည် -

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

ဤရလဒ်သည် ကောင်းမွန်သည်၊ ကျွန်တော် မုန့်ဟင်းခါး ဘာချက်မည်ကို သိရှိသည်။ ဆက်လက် တိုးတက်စေရန်ဖြစ်ပေါ်နိုင်သည့် ကောင်းမွန်သော အချက်များမှာ-

- မကြိုက်သည့် ပါဝင်ပစ္စည်းများ သို့မဟုတ် အာလေရ်ဂျီသည့် ပစ္စည်းများကို ဖြုတ်ပစ်ရန်။
- မိမိအိမ်၌ မရှိသည့် ပါဝင်ပစ္စည်းများအတွက် ၀ယ်ရန်စာရင်း ထုတ်ပေးရန်။

အထက်ဖော်ပြချက်များအတွက် prompt အသစ် တစ်ခု ထည့်သွင်းပါ -

> "ကျွန်တော် အာလေရ်ဂျီရှိသောကြောင့် ကြက်သွန်ဖြူ ပါဝင်သော ဟင်းလျာများကို ဖြုတ်ပစ်ပေးပါ။ အစားထိုး ပစ္စည်းဖြင့် အစားထိုးပေးပါ။ ထို့အပြင် ဟင်းလျာများအတွက် ၀ယ်ရန်စာရင်း တင်ပြပေးပါ။ ကျွန်တော်တွင် ကြက်သား၊ ဂေါ်ဖီ၊ မျှစေ့ ရှိပြီးဖြစ်သည်။"

ယခု သင့်တွင် နောက်ဆုံးရလဒ် အသစ်ရှိပါသည်-

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```

ဒါဟာ သင့်အတွက် ၅ မျိုးဟင်းလျာဖြစ်ပြီး ကြက်သွန်ဖြူ ပါဝင်ခြင်း မရှိပါ။ ပြီးတော့ မိမိအိမ်တွင် ရှိပြီးသားအချက်အလက်များ အတွက် ၀ယ်ရန်စာရင်းလည်း ရှိပါသည်။

## လေ့ကျင့်ခန်း - ဟင်းလျာဖန်တီးရေး အက်ပ် တည်ဆောက်ခြင်း

သင့်အနေဖြင့် ဇာတ်လမ်းတစ်ပုဒ်ကို ဘယ်လို ပေါ်လွင်ပုံဖော်သလဲဆိုတာများ ပြပါပြီ။ ထို့ကြောင့် အောက်ပါ အဆင့်များနဲ့ code ရေးသားပါ -

1. ရှိပြီးသား _app.py_ ဖိုင်ကို စတင်အချက်အလက်အဖြစ် သုံးပါ။
1. `prompt` အပြောင်းအလဲရှိသော variable ကို ရှာပြီး အောက်ပါ code ဖြင့် ပြင်ဆင်ပါ။

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   ယခု code ကို run ပါက အောက်ပါအတိုင်း output ရရှိပါမည် -

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > စိတ်ကြိုက်ပြောရရင် သင်၏ LLM သည် နောက်ထပ် တိုက်ရိုက်မဟုတ်ပဲ ဖန်တီးမှုများ ကွဲပြားမှုရှိလိမ့်မည်။

   ကောင်း၊ ရှင်းပြလိုသည်မှာ code ကို ပိုမိုလျှောက်ထားနိုင်အောင် လုပ်ချင်သည်။ အဓိကအားဖြင့် ပါဝင်ပစ္စည်းများနှင့် ဟင်းလျာအရေအတွက် ပြောင်းလဲနိုင်မှု ရှိစေချင်သည်။

1. အောက်ပါနည်းဖြင့် code ကို ပြောင်းလဲလိုက်ပါ။

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   သTests run တစ်ခုကို ၎င်း code ကဲ့သို့ အမျိုးအစားထားနိုင်သည် -

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ထပ်မံတိုးတက်အောင် filter နှင့် shopping list ထည့်ခြင်း

ယခု ကျွန်တော်တို့တွင် ကောင်းမွန်စွာ အလုပ်လုပ်ဆောင်နိုင်ပြီး အသုံးပြုသူထုတ် အချက်အလက်များအပေါ် မူတည်သော အသုံးပြုမှု့ ပိုမိုရှုပ်ထွေးသည့် အက်ပ်ရှိပြီး ဟင်းလျာအရေအတွက်နှင့် ပါဝင်ပစ္စည်းများကို အလွယ်တကူပြောင်းလဲနိုင်ပါသည်။

ပိုမိုတိုးတက်စေရန် အောက်ပါအချက်များ ထည့်သွင်းလိုသည် -

- **ပါဝင်ပစ္စည်းများ ဖျက်ပစ်ခြင်း**။ မကြိုက်သော သို့မဟုတ် အာလေရ်ဂျီဖြစ်သော ပစ္စည်းများကို ဖြုတ်ပစ်လိုသည်။ ၎င်းအတွက် ရှိပြီးသား prompt ကို ပြင်ဆင်ပြီး ဖျက်ပစ်ရန် အခြေအနေတစ်ခု ထည့်သွင်းလိုက်သည်။

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  အထက်ပါတွင် prompt အဆုံးတွင် `{filter}` ထည့်သွင်းပြီး အသုံးပြုသူထံမှ ရရှိသည့် ဖျက်ပစ်မည့်တန်ဖိုးကိုလည်း ဖမ်းယူထားသည်။

  ယခု program run ထားလျှင် ထည့်သွင်းလိုက်သော စကားဝိုင်း ဥပမာ -

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

  milk ပါဝင်သော ဟင်းလျာအားလုံး စစ်ထုတ်ထားသည်ကို တွေ့ရသည်။ ဒါပေမယ့် lactase-intolerant လား ဆိုလျှင် cheese နှင့်ပါ စစ်ထုတ်ရန်လိုအပ်သည်ကိုလည်း မှတ်သားထားရန် လိုအပ်သည်။

- **၀ယ်ရန်စာရင်း ထုတ်ပေးခြင်း**။ မိမိအိမ်ရှိပစ္စည်းများကို လည်းယူဆောင်ပြီး ၀ယ်ရန်စာရင်း ထုတ်ပေးလိုသည်။

  ဤလုပ်ဆောင်ချက်အတွက် တစ်ခုတည်းသော prompt ဖြင့် ဖြေရှင်းနိုင်သော်လည်း ၂ ခန်း prompt ပြန်ခွဲ၍ အပိုဆောင်ရွက်နိုင်သည်။ ပြုလုပ်သော ပထမ prompt ရလဒ်ကို ဒုတိယ prompt ၏ ဖော်ပြချက်အဖြစ် ထည့်သွင်းရန် လိုအပ်သည်။

  ပထမ prompt ၏ အဖြေကို print ထုတ်နေသည့်ကုဒ်အပိုင်း ရှာပြီး၊ အောက်ပါကုဒ်ကို ထပ်ဖြည့်ပါ။

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  အောက်ပါအချက်များ သတိထားပါ -

  1. ပထမ prompt ထဲမှ ရလဒ်ကို ဒုတိယ prompt အတွက် အတိုင်းအတာprompt ဖန်တီးရာတွင် ထည့်သွင်းသည်။

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. မိမိတောင်းဆိုထားသော token အရေအတွက်ကို တွက်ချက်မှုတွင် ထည့်သွင်းပြီး ဒုတိယ prompt ဝင်သော token အတွက် `max_output_tokens` ကို ၁၂၀၀ ဟုသတ်မှတ်သည်။

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     ၎င်းကုဒ်ကို စမ်းသပ်ပြီး အောက်ပါ output ကို ရရှိမည်။

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## သင့်အသုံးပြုမှု့ ပိုမိုတိုးတက်စေရန်

လက်ရှိမှာ ကျွန်ုပ်တို့တွင် ကုဒ်သည် အလုပ်လုပ်နေသော်လည်း ပိုမိုတိုးတက်အောင် ပြင်ဆင်သင့်သည့် နည်းလမ်းအချို့ရှိပါသည်။ ကျွန်ုပ်တို့လုပ်သင့်သည့်အရာအချို့မှာ -

- **လျှို့ဝှက်ချက်များကို ကုဒ်နဲ့ မတူခွဲခြားပါ၊**API key ကဲ့သို့သော။ လျှို့ဝှက်ချက်များသည် ကုဒ်ထဲမှာမပါဝင်သင့်ဘဲ ဘေးကင်းလုံခြုံတဲ့နေရာမှာ သိမ်းဆည်းသင့်ပါတယ်။ လျှို့ဝှက်ချက်များကို ကုဒ်နဲ့ ခွဲခြားရန်အတွက် environment variables နဲ့ `python-dotenv` ကဲ့သို့သောစာကြည့်တိုက်များကို အသုံးပြု၍ ဖိုင်မှတဆင့် တင်နိုင်ပါတယ်။ ကုဒ်မှာ ဘယ်လိုပုံစံဖြစ်မလဲဆိုတာ အောက်ပါအတိုင်းဖြစ်ပါတယ်-

  1. အောက်ပါအကြောင်းအရာပါသော `.env` ဖိုင်ကို ဖန်တီးပါ-

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > မှတ်ချက်- Microsoft Foundry ပြိုင်ပွဲအတွက် Azure OpenAI ကို အသုံးပြုမယ်ဆိုရင် အောက်ပါ environment variables များကို အစားထိုးသတ်မှတ်ရန် လိုအပ်ပါသည်-

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     ကုဒ်ထဲမှာ environment variables များကို အောက်ပါအတိုင်း load လုပ်နိုင်ပါတယ်-

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Token ရဲ့ အရှည်အကြောင်း**။ စိတ်ကြိုက်စာသားထုတ်ဖော်ရန် ကြိုတင်လိုအပ်သည့် token အရေအတွက်ကို တွက်ချက်သင့်ပါတယ်။ token တွေမှာ ငွေကုန်ကျမည့် အရာဖြစ်သည့်ကြောင့် အသုံးပြု token အရေအတွက်ကို သီးသန့် စဉ်းစားရန် ပြုလုပ်သင့်သည်။ ဥပမာ prompt ကို အတိုချုံးဖွဲ့စည်း၍ token အနည်းငယ်သာ အသုံးပြုနိုင်ပါသလား?

  အသုံးပြု token များကို ပြောင်းလိုပါက `max_output_tokens` parameter ကို အသုံးပြုနိုင်သည်။ ဥပမာ token ၁၀၀ အသုံးပြုလိုပါက-

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **temperature ကို စမ်းသပ်ခြင်း**။ Temperature သည် ယနေ့ထိ မထည့်ထားပေမယ့် ကျွန်ုပ်တို့စီမံခန့်ခွဲမှုအတွက် အရေးကြီးသော အချက်ဖြစ်သည်။ Temperature တန်ဖိုး များပြားသည့်အခါ ရလဒ်များသည် ပိုမိုမတူကွဲပြားနေပြီး၊ တန်ဖိုးနိမ့်သည့်အခါ ရလဒ်များ ပိုမိုခန့်မှန်းနိုင်သည်။ ရလဒ်များမှာ မတူကွဲပြားမှုရှိမရှိ စဉ်းစားပါ။

  temperature ကို ပြင်ဆင်ချင်လျှင် `temperature` parameter ကို အသုံးပြုနိုင်သည်။ ဥပမာ temperature 0.5 သတ်မှတ်လိုပါက-

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > မှတ်ချက်- 1.0 နီးပါးသလောက် ရလဒ်သည် ပိုမိုကွဲပြားမှုရှိသည်။

- **အကြောင်းအရာခံ မော်ဒယ်များသည် `temperature` ကို မသုံးပါ**။ ၎င်းသည် ၂၀၂၆ ပြောင်းလဲမှုအရေးကြီးတစ်ခုဖြစ်သည်။ Microsoft Foundry တွင် လက်ရှိထုတ်လုပ်ထားသော၊ မဖျက်သိမ်းရသေးသော မော်ဒယ်များမှာ **အကြောင်းအရာခံ မော်ဒယ်များ** (GPT-5 မျိုးစု၊ o-series) ဖြစ်ပြီး၊ အဲဒီများသည် **`temperature` သို့မဟုတ် `top_p` ကို ထောက်ပံ့မပြုပါ** (တောင် `max_tokens` မဟုတ်ဘဲ; `max_output_tokens` ကို အသုံးပြုပါ)။ သင်သည် `temperature` ကို `gpt-5-mini` သို့ ပို့မည့်အခါ "parameter not supported" အမှားဖြစ်မည်။ ထို့ကြောင့် အပူချိန်ဥပမာကို စမ်းသပ်ရန် sampling controls များကို မေးခွန်းထည့်၍ ထောက်ပံ့သေးသည့် မော်ဒယ်တစ်ခုကို ရည်ညွှန်းပါ - ဥပမာ open **Llama** မော်ဒယ်တစ်ခုဖြစ်သော `Llama-3.3-70B-Instruct` ကို [Microsoft Foundry model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) မှ ရယူပြီး Foundry Models / Azure AI Inference endpoint (`githubmodels-*` နမူနာများနှင့် တူညီသည့် နည်းလမ်း) မှ ခေါ်ယူပါ။ GPT-5 ကဲ့သို့ အကြောင်းအရာခံ မော်ဒယ်များအတွက် ဖြစ်ပါက output ကို မတူညီစွာ အကြောင်းလုပ်နိုင်သည်-
  - **Prompt engineering** - ရှင်းလင်းသောညွှန်ကြားချက်များ၊ ဥပမာများ၊ နှင့် ဖွဲ့စည်းထားသော output (သင်ခန်းစာ [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ပါ) သည် sampling knobs များ လုပ်ဆောင်ခဲ့သောအလုပ်ကို ပြုလုပ်သည်။
  - **အကြောင်းပြချက်ထိန်းချုပ်မှုများ** - အကြောင်းပြချက်ကြိုးစားမှု/အသံကြီးထွားမှုတို့က အကြောင်းပြချက်၏အနက်အဓိပ္ပါယ်ကို နှောင့်နှေးမှုနှင့်ကုန်ကျစရိတ်နှင့် ဆန့်ကျင်ဘက်ဖလှယ်သည်။

  အတိုချုပ်မှာ - `temperature`/`top_p` များသည် မော်ဒယ်များစွာ (Llama, Mistral, Phi နှင့် GPT-4.x မျိုးစွဲများတွင် - GPT-4.x သည် တရားဝင်အသုံးမပြုတော့တာဖြစ်ပေမယ့်) မှာ သော့မှတ်ထားဆဲဖြစ်သော်လည်း၊ အနာဂတ်ကို ဦးတည်ရာမှာတော့ prompt engineering + reasoning controls ကို reasoning မော်ဒယ်များတွင် GPT-5 ကဲ့သို့ အသုံးပြုခြင်း ပိုမိုကျယ်ပြန့်လာမည် ဖြစ်သည်။

## တာဝန်ပေးခြင်း

ဤတာဝန်ပေးခြင်းအတွက် သင်အဆောက်အအုံ ဘယ်လိုလုပ်မယ်ဆိုတာ ရွေးချယ်နိုင်ပါသည်။

ဒီမှာ အကြံပြုချက်အချို့ရှိပါတယ်။

- ချက်ပြုတ်သော့ချက်ထုတ်ပေးသူ အက်ပ်ကို ပိုမိုတိုးတက်အောင် ပြင်ဆင်ပါ။ အပူချိန်တန်ဖိုးများနဲ့ တောင်းဆိုချက်များကို စမ်းသပ်ကစားပြီး မင်းဘာတွေ ထုတ်လွှင့်နိုင်မလဲ ကြည့်ပါ။
- "လေ့လာသူမိတ်ဆွေ" တစ်ယောက်တည်ဆောက်ပါ။ ဒီအက်ပ်က ကိုယ်ရွေးချယ်ထားတဲ့ ခေါင်းစဉ်တစ်ခုအကြောင်း မေးခွန်းတွေဆွေးနွေးပေးနိုင်ရမယ်၊ ဥပမာ Python အကြောင်းတစ်ခုဖြစ်တာ၊ မင်းမှာ "Python ထဲက ခေါင်းစဉ်တစ်ခုက ဘာလဲ?" လိုတောင်းဆိုချက်တွေလည်း ရရှိနိုင်ပါမယ်၊ ဒါမှမဟုတ် "ခေါင်းစဉ်တစ်ခုအတွက် ကုဒ်တွေပြပါ" လိုတောင်းဆိုချက်တွေလည်း ရနိုင်ပါတယ်။
- သမိုင်းဘော့၊ သမိုင်းကို အသက်ဝင်ဖို့ ဘော့ကို တိုက်တွန်းပြီး သမိုင်းကနေလူကြီးတစ်ဦးလို အသက်ရှင်ပြထားဖို့ ဖိတ်ကြားပြီး သူ့ ဘဝနဲ့ အချိန်တွေ အကြောင်း မေးခွန်းမေးနိုင်မှာဖြစ်ပါတယ်။

## ဖြေရှင်းချက်

### လေ့လာသူမိတ်ဆွေ

အောက်မှာ စတင်အသုံးပြုခွင့်ရှိသော တောင်းဆိုချက်တစ်ခုအား ရှေ့ပြထားတာ ဖြစ်ပြီး မင်းဘယ်လို အသုံးပြုပုံနဲ့ ပြင်ဆင်လို့ရမလဲ စမ်းကြည့်ပါ။

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### သမိုင်းဘော့

မင်းအသုံးပြုနိုင်တဲ့ တောင်းဆိုချက်အချို့က ဒီအတိုင်းပါ။

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## အသိပညာ စစ်ဆေးချက်

အပူချိန် (temperature) ဆိုတာဘာလုပ်သလဲ?

1. ထွက်ရှိမှုက မျှတမှုဘယ်လောက်ရှိမလဲ ဆိုတာကို ထိန်းချုပ်ပါတယ်။
1. ရုပ်သိမ်းမှုဖွဲ့စည်းမှု ဘယ်လောက်ကြီးမားမလဲ ဆိုတာ ထိန်းချုပ်ပါတယ်။
1. အသုံးပြုသည့် တို့ကင် (tokens) အရေအတွက်ကို ထိန်းချုပ်ပါတယ်။

## 🚀 စိန်ခေါ်မှု

အလုပ်ပေါ်မှာ အပူချိန်ကို စမ်းသပ်ကြည့်ပြီး 0, 0.5 နဲ့ 1 တန်ဖိုးများ သတ်မှတ်ကြည့်ပါ။ 0 က အနည်းဆုံး မျိုးစုံမှုရှိပြီး 1 က အများဆုံးမျိုးစုံမှုရှိသည်။ ဘယ်တန်ဖိုးက မင်းအက်ပ်အတွက် အကောင်းဆုံးလဲ?

## အလွန်ကောင်းမွန်သည်! သင်ယူမှု ဆက်လက်ပါ။

ဒီသင်ခန်းစာပြီးသွားပါက ကျွန်ုပ်တို့ရဲ့ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ရှု၍ မင်းရဲ့ Generative AI အသိပညာများ အဆင့်မြှင့်တင်ရအောင် ဆက်လက်သင်ယူပါ။

Lesson 7 ကို သွားပါက [chat applications တည်ဆောက်နည်း](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ရှုမယ်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->