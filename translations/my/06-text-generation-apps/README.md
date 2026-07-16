# စာသားထုတ်လုပ်ခြင်းအတွက် အက်ပလီကေးရှင်းများ တည်ဆောက်ခြင်း

[![Building Text Generation Applications](../../../translated_images/my/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(ဒီသင်ခန်းစာ ရုပ်ရှင်ကို ကြည့်ရန် ဓာတ်ပုံကို နှိပ်ပါ)_

ဒီသင်ခန်းစာအစီအစဉ်ပေါ်မှာ မှတ်သားလာတာက prompt လို အခြေခံအယူအဆတွေရှိပြီး "prompt engineering" လို့ခေါ်တဲ့ စနစ်တစ်ခုလုံးလည်း ရှိတယ်ဆိုတာ ဖြစ်ပါတယ်။ ChatGPT, Office 365, Microsoft Power Platform နဲ့ အခြားကိရိယာတွေ အများကြီးက prompt တွေ့အရ အသုံးပြုပြီး တစ်ခုခုကို ပြုလုပ်နိုင်ဖို့ ကူညီတယ်။

သင့်အက်ပလီကေးရှင်းမှာ အဲ့ဒီနည်းလမ်းကို ထည့်သွင်းချင်ရင် prompt, completion နဲ့ အတူလက်တွဲသတ်မှတ်ရန် နက်နဲတဲ့ သိရှိမှုတွေ ရှိဖို့ လိုအပ်တယ်။ ဒီဘာသာရပ်မှာ သင်သင်ယူရမယ့်အရာတွေဟာ အဲဒီအကြောင်းတွေပါပဲ။

## နိဒါန်း

ဒီအခန်းမှာ သင်သည် -

- openai library နှင့် ၎င်း၏ အဓိကအယူအဆများကို သင်ယူမည်။
- openai ကို အသုံးပြုပြီး စာသားထုတ်လုပ်ခြင်း application တစ်ခု တည်ဆောက်မည်။
- prompt, temperature, tokens စသည့် အယူအဆများကို အသုံးပြု၍ စာသားထုတ်လုပ်ခြင်း app တည်ဆောက်နည်းကို နားလည်မည်။

## သင်ယူမှု ရည်မှန်းချက်များ

ဒီသင်ခန်းစာအဆုံးတွင် သင်သည် -

- စာသားထုတ်လုပ်ခြင်း app ဆိုတာဘာလဲ ဆိုတာ ရှင်းပြနိုင်မည်။
- openai ကို အသုံးပြုပြီး စာသားထုတ်လုပ်ခြင်း app တည်ဆောက်နိုင်မည်။
- ဆက်လက် အသုံးပြုမှု အတွက် tokens ပမာဏ များ/နည်းခြင်း၊ temperature ကို ပြောင်းလဲ၍ အထွက်အလွှာ မတူညီရေး ဆက်လက် ပြင်ဆင်နိုင်မည်။

## စာသားထုတ်လုပ်ခြင်း app ဆိုတာ ဘာလဲ?

အက်ပလီကေးရှင်းတစ်ခု တည်ဆောက်တဲ့အခါ များသောအားဖြင့် အောက်ပါမျိုးစုံ နည်းလမ်းတွေနဲ့ ပါလာတတ်ပါတယ် -

- ကွန်မန်းဖြင့် စီမံခြင်း။ Console app တွေမှာ command တစ်ချက်လို့ ရိုက်ထည့်လိုက်ရင် အလုပ်တစ်ခု ထွက်ခွာ တာဖြစ်ပါတယ်။ ဥပမာ `git` ဆိုတာက command-based app တစ်ခုပါ။
- အသုံးပြုသူအင်တာဖေ့( UI)။ အချို့ app တွေမှာ graphical user interfaces (GUI) ရှိပြီး ခလုတ်တွေ နှိပ်၊ စာထည့်၊ ရွေးချယ်မှုများ ပြုလုပ်နိုင်ပါတယ်။

### Console နဲ့ UI app တွေမှာ ကန့်သတ်ချက်တွေ ရှိတယ်

command-based app တစ်ခုမှာ command များ ရိုက်ထည့်တဲ့အခြေအနေနဲ့ နှိုင်းယှဉ်ကြည့်ပါ -

- **ကန့်သတ်ထားတယ်**။ ဘယ်အရာမဆို command ရိုက်၍ မရပါ။ app မှ ထောက်ခံထားတဲ့ command တွေပဲရိုက်နိုင်သည်။
- **ဘာသာစကားအထူးပြု**။ အချို့ app တွေက ဘာသာစကားများစွာကို ထောက်ခံပေမယ့် မူလတည်းက အတွက်တစ်ခု အတွက် တည်ဆောက်ထားပြီး နောက်ထပ် ဘာသာစကား ထည့်သွင်းနိုင်သည်။

### စာသားထုတ်လုပ် app ရဲ့ အကျိုးဖြစ်ရပ်များ

စာသားထုတ်လုပ် app တစ်ခုက ဘာကွာခြားလဲ?

စာသားထုတ်လုပ် app တွင် အသုံးပြုသူ ထက်ပို၍ လွတ်လပ်မှု ရှိသည်၊ ကန့်သတ်ထားသော command များ သို့မဟုတ် တိကျသော input language မှသာမက ပုံမှန်ဘာသာစကားဖြင့် အပြန်အလှန် ဆက်သွယ်နိုင်သည်။ ထိုအပြင် စာသားထုတ်လုပ်ထားသော app တွင် ကြီးမားသော သတင်းအချက်အလက်စုစည်းမှုအား လေ့ကျင့်ထားသော data source နဲ့ အပြန်အလှန် ဆက်သွယ်နေရသည်၊ ထိုသို့ မဟုတ် traditional အက်ပလီကေးရှင်းတွင် database ထဲမှာ ရှိသည့် အချက်အလက်များ အကန့်အသတ်ရရှိနိုင်သည်။

### စာသားထုတ်လုပ် app နဲ့ ဘာတွေ တည်ဆောက်နိုင်မလဲ?

များစွာ တန်ဆာပလာများ ရှိပါတယ်။ ဥပမာ -

- **Chatbot**။ သင့်ကုမ္ပဏီနဲ့ ထုတ်ကုန်များအကြောင်း မေးခွန်းများကို ဖြေဆိုပေးသော chatbot အကျိုးရှိနိုင်သည်။
- **ကူညီသူ**။ LLMs သည် စာသားအကျဉ်းချုပ်ျခင်း၊ အချက်အလက်သုံးသပ်ခြင်း၊ ရှာဖွေရေးစာတမ်း စသည်ဖြင့် စပ်ဆိုင်ရာ စာသားများပြုလုပ်ရာတွင် ကျွမ်းကျင်သည်။
- **Code assistant**။ သင်အသုံးပြုမည့် language model မူတည်ပြီး၊ ကုဒ်ရေးရာကူညီရန် code assistant တစ်ခု တည်ဆောက်နိုင်သည်။ ဥပမာ GitHub Copilot နှင့် ChatGPT တို့ အသုံးပြု၍ ကုဒ်ရေးရာ ကူညီနိုင်သည်။

## ဘယ်လို စတင်မလဲ?

LLM ထဲနှင့် ပေါင်းစပ်ရန် လမ်းကြောင်း နှစ်ခု ရှိသည် -

- API အသုံးပြုခြင်း။ သင်၏ prompt ဖြင့် web request များ ဖန်တီးပြီး ထုတ်ဖော်ထားသော စာသားများ ရယူသည်။
- Library အသုံးပြုခြင်း။ Libraries များက API ခေါ်ဆိုမှုများ ထုပ်ပိုးပေးပြီး အသုံးပြုရ လွယ်ကူသည်။

## Libraries/SDKs

LLMs နှင့် လုပ်ကိုင်ရာတွင် ကျော်ကြားသော libraries အနည်းငယ်ရှိပါသည် -

- **openai**၊ ဒီ library က သင့် model နဲ့ လွယ်ကူစွာ ချိတ်ဆက်ပြီး prompt တွေ ပို့နိုင်သည်။

ထို့အပြင် အဆင့်မြင့် library များလည်း ရှိသည် -

- **Langchain**။ Langchain သည် နာမည်ကြီး၍ Python ကို ထောက်ပံ့သည်။
- **Semantic Kernel**။ Semantic Kernel သည် Microsoft ၏ library ဖြစ်ပြီး C#, Python, Java ဘာသာစကားများကို ထောက်ပံ့သည်။

## openai အသုံးပြုပြီး ပထမဆုံး app တည်ဆောက်ခြင်း

ပထမဆုံး app ကို မည်သို့တည်ဆောက်ရမည်၊ မည်သည့် libraries လိုအပ်သည်၊ လိုအပ်သလောက် မည်မျှရှိသည် စသဖြင့် ကြည့်ကြပါစို့။

### openai ထည့်သွင်းခြင်း

OpenAI သို့မဟုတ် Azure OpenAI တွင် ဆက်သွယ်ရန် library များအများအပြားရှိသည်။ C#, Python, JavaScript, Java စသည့် programming languages များကိုလည်း အသုံးပြုနိုင်သည်။ ကျွန်တော်တို့က `openai` Python library ကို ရွေးချယ်ဖြစ်ပြီး `pip` ဖြင့် ထည့်သွင်းမှာ ဖြစ်သည်။

```bash
pip install openai
```

### resource တစ်ခု ဖန်တီးခြင်း

အောက်ပါတိုင်း ဆောင်ရွက်ရမည် -

- Azure ပေါ်မှာ အကောင့်တစ်ခု ဖန်တီးပါ [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)။
- Azure OpenAI အသုံးပြုခွင့် ရယူပါ။ [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) သို့ သွား၍ အသုံးပြုခွင့် တင်သွင်းပါ။

  > [!NOTE]
  > ယခုအချိန်တွင် Azure OpenAI အသုံးပြုခွင့် ရရန် လျှောက်ထားရပါမည်။

- Python ကို ထည့်သွင်းပါ <https://www.python.org/>
- Azure OpenAI Service resource တစ်ခု ဖန်တီးပြီးဖြစ်ပါက ဒီလမ်းညွှန်အား လိုက်နာပါ [create a resource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)။

### API key နဲ့ endpoint ကို ရှာဖွေခြင်း

ဒီအချိန်တွင် `openai` library မှ ဘယ် API key ကို အသုံးပြုမလဲ ပြောပြရန်လိုအပ်သည်။ API key ရှာဖွေရန် အတွက် Azure OpenAI resource ထဲရှိ "Keys and Endpoint" ခေါင်းစဉ်သို့ သွားပြီး "Key 1" ကို ကူးယူပါ။

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

ဒီအချက်အလက်များ ကူးယူပြီးနောက် library များကို အသုံးပြုအတွက် ညွှန်ကြားပေးပါ.

> [!NOTE]
> API key ကို ကိုးကားနေရာမှ သီးခြားထားသင့်သည်။ environment variable များအသုံးပြု၍ လုပ်ဆောင်နိုင်သည်။
>
> - environment variable `OPENAI_API_KEY` ကို API key သို့ သတ်မှတ်ပါ။
>   `export OPENAI_API_KEY='sk-...'`

### Azure အတွက် configuration ပြုလုပ်ခြင်း

Azure OpenAI (ယခု Microsoft Foundry ၏ အစိတ်အပိုင်း) ကို အသုံးပြုပါက configuration ပြုလုပ်နည်းမှာ အောက်ပါအတိုင်း ဖြစ်သည်။ `OpenAI` client ကို Azure OpenAI `/openai/v1/` endpoint သို့ ကျယ်ပြန့်စွာနှင့် သုံးနိုင်ပြီး Responses API အတွက် အတွက် `api_version` မလိုအပ်ပါ။

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

အထက်မှာလည်း အောက်ပါများ သတ်မှတ်ထားသည်

- `api_key`၊ Azure Portal သို့မဟုတ် Microsoft Foundry portal ထဲက API key ဖြစ်သည်။
- `base_url`၊ Foundry resource endpoint ဖြစ်ပြီး `/openai/v1/` ကို ပေါင်းထည့်ထားသည်။ stable v1 endpoint သည် OpenAI နှင့် Azure OpenAI နှစ်ခုလုံးတွင် `api_version` မလို အလုပ်လုပ်နိုင်သည်။

> [!NOTE] > `os.environ` သည် environment variable များ လုပ်ဆောင်ရေးဖြစ်သည်။ `AZURE_OPENAI_API_KEY` နှင့် `AZURE_OPENAI_ENDPOINT` စသည့် environment variables များကို terminal ထဲသို့ သတ်မှတ် သို့မဟုတ် `dotenv` စသည့် library ဖြင့် သတ်မှတ်နိုင်သည်။

## စာသား ထုတ်လုပ်ခြင်း

Responses API ကို `responses.create` method ဖြင့် စာသားထုတ်လုပ်နိုင်သည်။ ဥပမာ -

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # ဒါက သင့်မော်ဒယ်တပ်ဆင်မည့်နာမည် ဖြစ်ပါတယ်
    input=prompt,
    store=False,
)
print(response.output_text)
```

အထက်ပါကုဒ်တွင် response တစ်ခု ဖန်တီးပြီး အသုံးပြုမည့် model နှင့် prompt ကို ထည့်သွင်းသည်။ ထို့နောက် `response.output_text` မှ ချပြထားသော စာသား ထုတ်လုပ်မှုကို ပြသည်။

### ပြောဆိုမှုများ မျိုးစုံ

Responses API သည် တစ်ချက်တည်း စာသားထုတ်လုပ်ခြင်းနှင့် multi-turn chatbot များရေးဆွဲရာတွင် သင့်တော်သည်။ `input` ထဲတွင် စကားပြောစာရင်းများ ထည့်သွင်းကာ ဆက်သွယ်မှုတည်ဆောက်နိုင်သည် -

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

ဤ အသုံးပြုမှုဆိုင်ရာ လုပ်ဆောင်မှုများကို နောက်ဆုံးအခန်းတွင် ဆက်လက် ရှင်းလင်းမည်။

## လေ့ကျင့်ခန်း - သင်၏ ပထမဆုံး စာသားထုတ်လုပ်ခြင်း app

openai ကို စတင် လေ့လာပြီး သင်၏ ပထမဆုံး စာသားထုတ်လုပ်ခြင်း app တည်ဆောက်ချိန် ဖြစ်ပါသည်။ ဤအက်ပလီကေးရှင်း တည်ဆောက်ရန် အောက်ပါအဆင့်များ လိုက်နာပါ -

1. virtual environment တစ်ခု ဖန်တီးပြီး openai ထည့်သွင်းပါ။

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows အသုံးပြုပါက `venv\Scripts\activate` ကို `source venv/bin/activate` အစား ရိုက်ထည့်ပါ။

   > [!NOTE]
   > Azure OpenAI key ကို [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) သို့ သွား၍ `Open AI` ရှာပြီး `Open AI resource` အား ရွေးချယ်ပါ၊ ပြီးနောက် `Keys and Endpoint` ကိုနှိပ်ကူးယူပါ။

2. _app.py_ ဖိုင် တစ်ခု ဖန်တီးပြီး အောက်ပါကုဒ် ထည့်ပါ -

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # သင့်ပြီးစီးမှုကုဒ်ကို ထည့်ပါ
   prompt = "Complete the following: Once upon a time there was a"

   # Responses API ကို အသုံးပြု၍ တောင်းဆိုချက် တစ်ခု ပြုလုပ်ပါ
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # တုံ့ပြန်ချက်ကို ပုံနှိပ်ပါ
   print(response.output_text)
   ```

   > [!NOTE]
   > OpenAI (Azure မဟုတ်) အသုံးပြုပါက `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (base_url မပါ) သုံးပြီး `gpt-4o-mini` ကဲ့သို့ model name ထည့်သွင်းပါ။

   အောက်ပါ Output တူ အဖြေကို မြင်ရမည် -

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## prompt မျိုးစုံ၊ အလုပ်အမျိုးမျိုးအတွက်

ယခု သင် prompt အသုံးပြုပြီး စာသား ထုတ်လုပ်နည်း သိရှိသွားပြီး ဖြစ်သည်။ သင်သည် ပြင်ဆင်နိုင်ပြီး အမျိုးအစားကွဲပြားသော စာသားများ ထုတ်လုပ်နိုင်မည် programs တစ်ခု ရှိပြီ ဖြစ်သည်။

prompt များသည် အလုပ်အမျိုးမျိုးအတွက် အသုံးပြုနိုင်သည်။ ဥပမာ -

- **စာသားတစ်မျိုး အထုတ်သဖြင့် ထုတ်လုပ်ခြင်း**။ သီချင်း၊ မေးခွန်း စသည်ကို ထုတ်လုပ်နိုင်သည်။
- **အချက်အလက် ရှာဖွေမှု**။ prompt တွေ ကို အသုံးပြုပြီး နောက်ထပ် data ကို ရှာဖွေနိုင်သည်။ ဥပမာ 'What does CORS mean in web development?' ဆိုသည်နှင့် စသည်။
- **ကုဒ် ထုတ်လုပ်ခြင်း**။ စကားပြော prompt တစ်ခု ဖြင့် ကုဒ်ရေးဆွဲနိုင်သည်။ ဥပမာ email ကို စစ်ဆေးသုံးစွဲရန် regular expression ဖြင့် ဖန်တီးခြင်း၊ ဒါမှ မဟုတ် အက်ပလီကေးရှင်း တစ်ခုလုံး ဖန်တီးခြင်း။

## အသုံးချနိုင်သည့် နမူနာ - ဟင်းချက်နည်း ထုတ်လုပ်သူ

မိမိဆိုင်ရာ ပစ္စည်းတွေ ရှိပြီး အစားအသောက် ပြုလုပ်ချင်လျှင် အသုံးပြုနိုင်တဲ့ ဟင်းချက်နည်းလိုအပ်သည်။ ဟင်းချက်နည်း ရှာဖွေရန် search engine သုံးပါ၊ ဒါမှ မဟုတ် LLM ကို အသုံးပြုပါ။

Prompt ကို အောက်ပါအတိုင်း ရေးနိုင်သည် -

> "Chicken, potatoes, carrots ပါဝင်သည့် ဟင်းမုန့်အမျိုးအစား ၅ ခုပြပါ။ ဟင်းချက်နည်းတစ်ခုစီအတွက် ပါဝင်သော ပစ္စည်းအားလုံး ကို ကျေးဇူးပြု၍ စာရင်းပြုစုပါ။"

အရင် prompt ပေးသလို ဒီလို အဖြေ ပြန်လာနိုင်သည် -

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

ဒီအဖြေက အရမ်းကောင်းပါတယ်၊ မိမိချက်ဖို့ ကောင်းမွန်ပြီ။ ဒီအချိန်မှာ အဆင်ပြေသမားများက -

- ကိုကြိုက်သော် သို့မဟုတ် အစာအဆာဖြစ်သူ ပစ္စည်း မပါဝင်စေချင်မှု။
- ပစ္စည်းအားလုံး မရှိမှန်း သတိပြုပြီး စျေးဝယ် စာရင်း ထုတ်ပေးရန်။

အထက်ပါ သဘောတူချက်များအတွက် prompt အသစ် တစ်ခုပြုလုပ်ပါ -

> "Please remove recipes with garlic as I'm allergic and replace it with something else. Also, please produce a shopping list for the recipes, considering I already have chicken, potatoes and carrots at home."

ယခု အဖြေ အသစ် ရရှိပြီ၊ ဟင် -

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

ဒါဟာ သင့်ဟင်းချက်နည်း ၅ ခုပဲ ဖြစ်ပြီး ကြက်သွန်ဖြူ မပါရှိပါ။ သင့်အိမ်ရှိ ဆိုသလို စျေးဝယ်စာရင်းပါ ရှိသည်။

## လေ့ကျင့်ခန်း - ဟင်းချက်နည်း ထုတ်လုပ်သူ တည်ဆောက်ခြင်း

ပြသထားသည့် အခြေအနေ ကို အကောင်အထည် ဖော်ရန် ကုဒ်ရေးပါ။ အောက်ပါအဆင့်များ လိုက်နာပါ -

1. ရှိပြီးသား _app.py_ ဖိုင်ကို စတင်အခြေခံအနေဖြင့် သုံးပါ။
1. `prompt` ပြောင်းလဲ ပြင်ဆင်ပြီး အောက်ပါ ကုဒ်အတိုင်း ပြောင်းတင်ပါ -

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   အခု၊ ကုဒ်ကို ပြေးရင် အောက်ပါ အဖြေ မျိုး ရှိလာမည်။

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > သတိပြုရန်၊ သင့် LLM သည် non-deterministic ဖြစ်ပြီး အချိန်တိုင်းအခြေအနေပေါ် မူတည်၍ အဖြေ မတူကြာနိုင်ပါသည်။

   ကောင်းမွန်ပါတယ်၊ ပိုမိုကောင်းမွန်အောင် ပြင်ဆင်မှု လုပ်ကြရအောင်။ ပြင်ဆင်မှုများမှာ ဟင်းပွဲအရေအတွက်နှင့် ပစ္စည်းများ ရွေးချယ်မှု ပြောင်းလဲနိုင်စေရန် ဖြစ်သည်။

1. ကုဒ်ကို အောက်ပါအတိုင်း ပြင်ဆင်ပါ -

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # မုန့်ချက်နည်းများ၏အရေအတွက်ကို prompt နှင့် ပါဝင်ပစ္စည်းများထဲသို့ အတွဲထည့်ပါ။
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   စမ်းသပ်မှုပြုမှာ ဒီလို ဖြစ်နိုင်သည် -

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### စစ်ထုတ်ခြင်းနှင့် စျေးဝယ်စာရင်း ထည့်ခြင်းဖြင့် တိုးတက် ပြောင်းလဲမှု

ယခင်က အလုပ်လုပ်သော app တစ်ခု ရှိပြီး ယခုမှာ အသုံးပြုသူ ထံမှ ပြန်ဝင်တဲ့ အချက်အလက်များဖြင့် ဟင်းချက်နည်းအရေအတွက် နှင့် ပါဝင်ပစ္စည်းများကို လွယ်ကူပြောင်းလဲနိုင်သည်။

ပိုမိုတိုးတက်အောင် လုပ်လိုပါက အောက်ပါ အချက်များ လိုအပ်သည် -

- **ပစ္စည်းများကို စစ်ထုတ်ခြင်း**။ မကြိုက်သော သို့မဟုတ် အစာအဆာဖြစ်သော ပစ္စည်းများ ကို ဖယ်ရှားနိုင်စေရန်။  ဤအတွက် စစ်ထုတ်မှု အခြေအနေ prompt အဆုံးတွင် ထည့်သွင်း ပြင်ဆင်နိုင်ပါသည် -

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  အထက်မှာ prompt အဆုံးတွင် `{filter}` ထည့်သွင်းပြီး အသုံးပြုသူထံမှ filter တန်ဖိုး သိမ်းဆည်းထားသည်။

  ဖော်ပြမှုပုံစံတစ်ခုမှာ အောက်ပါအတိုင်း ဖြစ်နိုင်သည် -

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

  မြင်နိုင်သလို ၊ အက်乳ထဲ သောက်သောဟင်းချက်များကို ဖယ်ရှားထားသည်။ Lactose intolerance ရှိသူများအတွက် ချိ့စ်ပါ ဟင်းချက်များကိုလည်း ဖယ်ရှားနိုင်ရန် လိုအပ်သည်၊ ထို့ကြောင့် ရှင်းလင်းစွာ အဝိုင်းဖွဲ့တင်ပြရန် လိုအပ်ပါသည်။


- **စျေးဝယ်စာရင်းတစ်ခု ရေးဆွဲပါ**။ ကျွန်တော်တို့မှာ အိမ်မှာရှိပြီးသား ပစ္စည်းတွေကို ထည့်သွင်းစဉ်းစားပြီး စျေးဝယ်စာရင်းတစ်ခု ရေးဆွဲချင်ပါတယ်။

  ဒီဖွင့်ပြောချက်အတွက် ကျွန်တော်တို့အနေဖြင့် တစ်ချက်တည်းမှာပဲ အားလုံးကို ဖြေရှင်းဖို့ကြိုးစားလို့ရပေမဲ့ နှစ်ချက်ခွဲပြီးခွဲဝေဖို့လည်း ရှိပါတယ်။ နောက်အဆင့်နဲ့စမ်းကြည့်ပါမယ်။ ဒီမှာ နောက်ထပ် prompt တစ်ခု ထည့်သွင်းဖို့ အကြံပြုထားပေမဲ့ အလုပ်ဖြစ်ဖို့ အရင် prompt ရဲ့ရလဒ်ကို နောက် prompt ရဲ့ context အဖြစ် ထည့်သွင်းဖို့ လိုအပ်ပါတယ်။

  ပထမ prompt မှရလဒ်ကို print ထုတ်နေတဲ့ code အပိုင်းကိုရှာပြီး အောက်ပါ code ကို ထည့်သွင်းပါ။

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # တုံ့ပြန်ချက်ကို ပရင့်ထုတ်ပါ
  print("Shopping list:")
  print(response.output_text)
  ```

  အောက်ပါအချက်တွေကို သတိပြုပါ။

  1. ပထမ prompt ကရလဒ်ကို နောက် prompt ထဲကို ထည့်ပြီး prompt အသစ်တစ်ခု တည်ဆောက်နေပါတယ်။

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. ငါတို့ အသစ်တောင်းဆိုမှုတစ်ချက် ပြုလုပ်ပါတယ်၊ ဒါပေမဲ့ ပထမ prompt မှာ တောင်းခဲ့တဲ့ token အရေအတွက်ကိုလည်း ထည့်သွင်းစဉ်းစားပြီး ဒီတစ်ခါ `max_output_tokens` ကို ၁၂၀၀ လို့ပြောပါတယ်။

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     ဒီ code ကို စမ်းသပ်သုံးစွဲတဲ့အခါ အောက်ပါ output ကို ရလဒ်အဖြစ် ရောက်ရှိပါပြီ။

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## သင့် Setup ကိုတိုးတက်ကောင်းမွန်လာစေမယ့်အချက်များ

ယနေ့အထိ ရရှိထားတာက အလုပ်လုပ်တယ်၊ ဒါပေမဲ့ နောက်ထပ် တိုးတက်လာစေဖို့ ပြင်ဆင်သင့်တဲ့ အချက်အချို့ ရှိပါတယ်။ ကျွန်တော်တို့လုပ်သင့်တာတွေကတော့ -

- **Code ကနေ secrets တွေကို ချွတ်ထုတ်ပါ**၊ အဖြစ် API key များကဲ့သို့သော secrets သည် code ထဲမှာမရှိသင့်ပါ၊ လုံခြုံစိတ်ချရသောနေရာတွင် သိမ်းဆည်းထားသင့်သည်။ Code ကနေ secrets ကို ခွဲထုတ်ဖို့အတွက် environment variables နဲ့ `python-dotenv` ကဲ့သို့သော library များကို ဖိုင်မှ load ရန် အသုံးပြုနိုင်ပါတယ်။ ကုဒ်အတွင်း ဒီလိုပြသပါမယ်။

  1. အောက်ပါ အကြောင်းအရာပါ .env ဖိုင်တစ်ခု ဖန်တီးပါ။

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > သတိပေးချက်၊ Microsoft Foundry တွေရှိ Azure OpenAI အတွက် အောက်ပါ environment variables များကို သတ်မှတ်ပေးသင့်ပါတယ်။

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Code ထဲမှာ environment variables များကို အောက်ပါနည်းဖြင့် load လုပ်ပါ။

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Token ရဲ့ရေတွက်အကြောင်း**။ ကျွန်တော်တို့ လိုချင်တဲ့စာသား ထွက်ရှိဖို့ အတွက် ဘယ်လောက် token လိုအပ်မလဲ ဆိုတာ စဉ်းစားသင့်ပါတယ်။ Token များမှာ စျေးပေါက်မှုရှိတဲ့အတွက် အလကား token မဖြုတ်အောင် စဉ်းစားသင့်ပါတယ်။ ဥပမာနဲ့ဆို prompt ကို ဘယ်လိုဖော်ပြရင် token အနည်းငယ်သုံးနိုင်မယ်ဆိုတာစဉ်းစားပါ။

  Token အသုံးပြုမှုကို ပြောင်းလဲရန် `max_output_tokens` parameter ကိုအသုံးပြုပေးနိုင်ပါတယ်။ ဥပမာ token ၁၀၀ သုံးချင်လျှင် အောက်ပါအတိုင်းရေးနိုင်ပါတယ်။

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **temperature ကိုစမ်းသပ်ခြင်း**။ Temperature ဆိုတာ ခုတိုင်မပြောဖူးပေမဲ့ ကျွန်တော်တို့ program လုပ်ဆောင်ပုံအတွက် အရေးပါတဲ့ context တစ်ခုပါ။ Temperature ဆွဲတယ်ဆို output ရဲ့ ပုံစံ ပိုမို ယုံကြည်လို့ရမလား မယုံကြည်နိုင်လောက်အောင် ရောက်နေပုံမျိုး ဖြစ်ပါတယ်။ Temperature မြင့်လာတိုင်း output ပို ရောထွေးမယ်၊ temperature နည်းလာတိုင်း output အတိအကျ ရှိလာမယ်။ output မှာ လွတ်လပ်ချွတ်ချော်မှုရှိချင်တာရှိမရှိ စဉ်းစားပါ။

  temperature ကို ပြောင်းလဲချင်ရင် `temperature` parameter ကိုအသုံးပြုပေးနိုင်ပါတယ်။ ဥပမာ temperature 0.5 သတ်မှတ်ချင်ရင် အောက်ပါအတိုင်းရေးနိုင်ပါတယ်။

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > သတိပေးချက်၊ 1.0 နီးကျင်လာသလောက် output ပိုမိုကွဲပြားသွားပါသည်။

## အလုပ်တာဝန်

ဒီတာဝန်အတွက် သင်ဘာလုပ်ချင်သလဲကို ရွေးချယ်နိုင်ပါတယ်။

အကြံပြုချက်အချို့မှာ -

- Recipe generator app ကိုပို၍ တိုးတက်အောင် ပြင်ဆင်ပါ။ temperature တန်ဖိုးများနဲ့ prompt များကို ကစားပြီး ဘာရနိုင်မလဲ ကြည့်ပါ။
- "study buddy" app တစ်ခု တည်ဆောက်ပါ။ ဥပမာ Topics တစ်ခုအကြောင်းအဖြေများပေးနိုင်တဲ့ Python အကြောင်းဖြစ်နိုင်ပါတယ်၊ “Python မှ သီးသန့်အကြောင်းဘာလဲ?” ကဲ့သို့ prompt များ သို့မဟုတ် "သီးသန့် topic အတွက် code ပြပါ" ကဲ့သို့ prompt များ ထည့်ပေးနိုင်ပါသည်။
- History bot တည်ဆောက်ပါ၊ သမိုင်းကို အသက်ရှင်စေပါ၊ သက်ဆိုင်ရာ သမိုင်းဇာတ်ကောင်တစ်ကောင်ကို ဖော်ပြစေပြီး သူ့ဘဝနဲ့ အချိန်ကာလအကြောင်း တွေကို မေးမြန်းစေပါ။

## ဖြေရှင်းချက်

### Study buddy

အောက်မှာ စတင်ဖော်ပြထားတဲ့ prompt တစ်ခုရှိပါတယ်၊ သင် ဘယ်လိုအသုံးပြုပြီး သင်ကြိုက်သလို ပြင်ဆင်နိုင်လဲ ကြည့်ပါ။

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### History bot

သုံးနိုင်တဲ့ prompt အချို့က ဒီအတိုင်းပါ။

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## အသိပညာစစ်တမ်း

temperature ဆိုတဲ့ အယူအဆကဘာလဲ?

1. အကုန် output ပေါ်မှာ ဘယ်လောက် မမှန်ကန်မှုရှိမလဲ ကို ထိန်းချုပ်တယ်။
1. ဘယ်လောက် ပြန်ကြားချက် အကြီးကြီးရှိမလဲကို ထိန်းချုပ်တယ်။
1. ဘယ်လောက် token သုံးမလဲ ဆိုတာကို ထိန်းချုပ်တယ်။

## 🚀 စိန်ခေါ်မှု

အလုပ်တာဝန်မှာ ကုဒ်ရေးဆွဲတဲ့အခါ temperature ကို အမျိုးမျိုးပြောင်းလဲပြီး စမ်းကြည့်ပါ၊ 0, 0.5, နဲ့ 1 အဖြစ် သတ်မှတ်ပါ။ 0 က အနည်းဆုံး ကွဲပြားမှုရှိပြီး 1 က အများဆုံးပါ။ သင့် app အတွက် ဘယ်တန်ဖိုးက အကောင်းဆုံးလဲ ဆိုတာ ရှာဖွေပါ။

## အလွန်ကောင်းတာ! သင်ကြားမှုကို ဆက်လက်လုပ်ဆောင်ပါ

ဒီသင်ခန်းစာပြီးမြောက်ပါက ကျွန်တော်တို့ရဲ့ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ရှုပြီး Generative AI အသိပညာတိုးမြှင့် ဆက်လက်လုပ်ဆောင်နိုင်ပါတယ်!

သင်ခန်းစာ ၇ မှာ သွားရောက်ပြီး [chat applications ဆောက်ပုံ](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ရှုပါ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->