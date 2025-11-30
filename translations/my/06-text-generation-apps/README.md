<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df027997f1448323d6159b78a1b669bf",
  "translation_date": "2025-10-18T01:50:02+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "my"
}
-->
# စာသားထုတ်လုပ်မှုအက်ပလီကေးရှင်းများ တည်ဆောက်ခြင်း

[![စာသားထုတ်လုပ်မှုအက်ပလီကေးရှင်းများ တည်ဆောက်ခြင်း](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.my.png)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(အထက်ပါပုံကိုနှိပ်ပြီး ဒီသင်ခန်းစာရဲ့ဗီဒီယိုကိုကြည့်ပါ)_

ဒီသင်ခန်းစာတွင် သင်တွေ့ရှိခဲ့တာက prompt တွေလို အဓိကအကြောင်းအရာများနှင့် "prompt engineering" လို့ခေါ်တဲ့ အတတ်ပညာတစ်ခုတောင်ရှိတယ်ဆိုတာပါပဲ။ ChatGPT, Office 365, Microsoft Power Platform စတဲ့ tools တွေကို သင်အသုံးပြုနိုင်ပြီး prompt တွေကိုအသုံးပြုပြီး တစ်စုံတစ်ခုကို ပြုလုပ်နိုင်ပါတယ်။

ဒီလိုအတွေ့အကြုံကို သင့်အက်ပလီကေးရှင်းထဲမှာ ထည့်သွင်းဖို့ဆိုရင် prompt, completions စတဲ့အကြောင်းအရာတွေကို နားလည်ဖို့လိုပါတယ်။ ဒီအခန်းမှာ အဲ့ဒီအကြောင်းတွေကို သင်လေ့လာရမှာပါ။

## အကျဉ်းချုပ်

ဒီအခန်းမှာ သင် -

- openai library နဲ့ အဓိကအကြောင်းအရာတွေကို လေ့လာပါမယ်။
- openai ကိုအသုံးပြုပြီး စာသားထုတ်လုပ်မှုအက်ပလီကေးရှင်းတစ်ခုကို တည်ဆောက်ပါမယ်။
- prompt, temperature, tokens စတဲ့အကြောင်းအရာတွေကို အသုံးပြုပြီး စာသားထုတ်လုပ်မှုအက်ပလီကေးရှင်းတစ်ခုကို တည်ဆောက်ပုံကို နားလည်ပါမယ်။

## သင်ယူရမယ့်ရည်မှန်းချက်များ

ဒီသင်ခန်းစာအဆုံးမှာ သင် -

- စာသားထုတ်လုပ်မှုအက်ပလီကေးရှင်းဆိုတာဘာလဲဆိုတာ ရှင်းပြနိုင်ပါမယ်။
- openai ကိုအသုံးပြုပြီး စာသားထုတ်လုပ်မှုအက်ပလီကေးရှင်းတစ်ခုကို တည်ဆောက်နိုင်ပါမယ်။
- သင့်အက်ပလီကေးရှင်းကို tokens ပိုသုံး/နည်းစေဖို့နဲ့ varied output ရဖို့ temperature ကိုပြောင်းနိုင်ပါမယ်။

## စာသားထုတ်လုပ်မှုအက်ပလီကေးရှင်းဆိုတာဘာလဲ?

ပုံမှန်အားဖြင့် သင်အက်ပလီကေးရှင်းတစ်ခုကို တည်ဆောက်တဲ့အခါမှာ အောက်ပါလို interface တစ်ခုခုရှိပါတယ် -

- **Command-based**။ Console apps တွေက command-based apps တွေဖြစ်ပြီး သင် command တစ်ခုကို ရိုက်ထည့်ပြီး task တစ်ခုကိုလုပ်ဆောင်ပါတယ်။ ဥပမာ `git` က command-based app တစ်ခုဖြစ်ပါတယ်။
- **User interface (UI)**။ အချို့ apps တွေမှာ graphical user interfaces (GUIs) ရှိပြီး သင် button တွေကိုနှိပ်ခြင်း၊ စာသားရိုက်ထည့်ခြင်း၊ option တွေကိုရွေးခြင်းစတဲ့အရာတွေကိုလုပ်နိုင်ပါတယ်။

### Console နဲ့ UI apps တွေက အကန့်အသတ်ရှိပါတယ်

Command-based app နဲ့ နှိုင်းယှဉ်ကြည့်ပါ -

- **အကန့်အသတ်ရှိတယ်**။ သင် app က support လုပ်တဲ့ command တွေကိုသာ ရိုက်နိုင်ပြီး အခြား command တွေကို ရိုက်လို့မရပါဘူး။
- **ဘာသာစကားအထူးပြု**။ အချို့ apps တွေက ဘာသာစကားများစွာကို support လုပ်ပေမယ့် ပုံမှန်အားဖြင့် app ကို အထူးပြုထားတဲ့ ဘာသာစကားအတွက် တည်ဆောက်ထားပါတယ်။ သို့သော် အခြားဘာသာစကား support ကို ထည့်သွင်းနိုင်ပါတယ်။

### စာသားထုတ်လုပ်မှုအက်ပလီကေးရှင်းများ၏ အကျိုးကျေးဇူးများ

စာသားထုတ်လုပ်မှုအက်ပလီကေးရှင်းက ဘာကြောင့် ကွဲပြားတာလဲ?

စာသားထုတ်လုပ်မှုအက်ပလီကေးရှင်းမှာ သင်ပိုပြီး flexible ဖြစ်ပြီး command တွေတစ်ခုခုနဲ့ input language တစ်ခုခုမှာ အကန့်အသတ်မရှိပါဘူး။ အစား သင် app နဲ့ natural language ကိုအသုံးပြုပြီး ဆက်သွယ်နိုင်ပါတယ်။ အခြားအကျိုးကျေးဇူးတစ်ခုကတော့ သင် database ထဲမှာရှိတဲ့အချက်အလက်တွေမှာသာ အကန့်အသတ်မရှိဘဲ အချက်အလက်များစွာကို training လုပ်ထားတဲ့ data source နဲ့ ဆက်သွယ်နေပါတယ်။

### စာသားထုတ်လုပ်မှုအက်ပလီကေးရှင်းနဲ့ ဘာတွေတည်ဆောက်နိုင်မလဲ?

တည်ဆောက်နိုင်တဲ့အရာတွေ အများကြီးရှိပါတယ်။ ဥပမာ -

- **Chatbot**။ သင့်ကုမ္ပဏီနဲ့ ထုတ်ကုန်တွေကို အကြောင်းပြောတဲ့ chatbot တစ်ခုက သင့်တော်တဲ့ရွေးချယ်မှုတစ်ခုဖြစ်နိုင်ပါတယ်။
- **Helper**။ LLMs တွေက စာသားကို အကျဉ်းချုပ်ခြင်း၊ အချက်အလက်တွေကို ရှာဖွေခြင်း၊ စာသားတွေကို ထုတ်လုပ်ခြင်း (ဥပမာ - ရာထူးလျှောက်လွှာ) စတဲ့အရာတွေမှာ အထူးကောင်းပါတယ်။
- **Code assistant**။ သင်အသုံးပြုတဲ့ language model ပေါ်မူတည်ပြီး သင် code ရေးဖို့ကူညီပေးတဲ့ code assistant တစ်ခုကို တည်ဆောက်နိုင်ပါတယ်။ ဥပမာ GitHub Copilot နဲ့ ChatGPT တို့ကို အသုံးပြုပြီး code ရေးဖို့ကူညီပေးနိုင်ပါတယ်။

## ဘယ်လိုစတင်နိုင်မလဲ?

အရင်ဆုံး LLM နဲ့ပေါင်းစည်းဖို့နည်းလမ်းတစ်ခုကို ရှာဖွေရပါမယ်။ အဲဒါက အောက်ပါနည်းလမ်းနှစ်ခုကိုပါဝင်ပါတယ် -

- **API ကိုအသုံးပြုပါ**။ ဒီမှာ သင့် prompt ကို web requests တွေတည်ဆောက်ပြီး generated text ကိုပြန်ရရှိမှာဖြစ်ပါတယ်။
- **Library ကိုအသုံးပြုပါ**။ Library တွေက API calls တွေကို encapsulate လုပ်ပြီး အသုံးပြုရလွယ်ကူစေပါတယ်။

## Libraries/SDKs

LLMs တွေနဲ့အလုပ်လုပ်ဖို့အတွက် နာမည်ကြီး library အချို့ရှိပါတယ် -

- **openai**၊ ဒီ library က သင့် model နဲ့ချိတ်ဆက်ပြီး prompt တွေကို ပေးပို့ဖို့ လွယ်ကူစေပါတယ်။

ပြီးတော့ အဆင့်မြင့်အဆင့်မှာ အလုပ်လုပ်တဲ့ library တွေရှိပါတယ် -

- **Langchain**။ Langchain က နာမည်ကြီးပြီး Python ကို support လုပ်ပါတယ်။
- **Semantic Kernel**။ Semantic Kernel က Microsoft ရဲ့ library ဖြစ်ပြီး C#, Python, Java ဘာသာစကားတွေကို support လုပ်ပါတယ်။

## openai ကိုအသုံးပြုပြီး ပထမဆုံးအက်ပလီကေးရှင်းတည်ဆောက်ခြင်း

openai ကိုအသုံးပြုပြီး ပထမဆုံးအက်ပလီကေးရှင်းတစ်ခုကို ဘယ်လိုတည်ဆောက်ရမလဲ၊ ဘယ်လို library တွေလိုအပ်မလဲ၊ ဘယ်လောက်အလုပ်လုပ်ရမလဲဆိုတာကို ကြည့်ကြမယ်။

### openai ကို install လုပ်ပါ

OpenAI သို့မဟုတ် Azure OpenAI နဲ့အလုပ်လုပ်ဖို့ library တွေ အများကြီးရှိပါတယ်။ C#, Python, JavaScript, Java စတဲ့ programming languages အမျိုးမျိုးကိုလည်း အသုံးပြုနိုင်ပါတယ်။ ကျွန်တော်တို့က `openai` Python library ကိုရွေးလိုက်ပြီးတော့ `pip` ကိုအသုံးပြုပြီး install လုပ်ပါမယ်။

```bash
pip install openai
```

### Resource တစ်ခုကိုဖန်တီးပါ

အောက်ပါအဆင့်တွေကိုလုပ်ဆောင်ရပါမယ် -

- Azure မှာ account တစ်ခုဖွင့်ပါ [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)။
- Azure OpenAI ကို access ရယူပါ။ [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ကိုသွားပြီး access ကိုတောင်းဆိုပါ။

  > [!NOTE]
  > ဒီစာရေးချိန်မှာ Azure OpenAI ကို access ရဖို့အတွက် တောင်းဆိုရပါမယ်။

- Python ကို install လုပ်ပါ <https://www.python.org/>
- Azure OpenAI Service resource တစ်ခုကို ဖန်တီးထားပါ။ [resource တစ်ခုကို ဖန်တီးပုံ](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst) guide ကိုကြည့်ပါ။

### API key နဲ့ endpoint ကိုရှာပါ

ဒီအချိန်မှာ သင့် `openai` library ကို အသုံးပြုဖို့ API key ကိုပြောပြရပါမယ်။ သင့် API key ကိုရှာဖို့ဆိုရင် Azure OpenAI resource ရဲ့ "Keys and Endpoint" အပိုင်းကိုသွားပြီး "Key 1" value ကို copy လုပ်ပါ။

![Azure Portal ရဲ့ Keys and Endpoint resource blade](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

အခု သင်အဲ့ဒီအချက်အလက်တွေကို copy လုပ်ပြီးရင် library တွေကိုအသုံးပြုဖို့ setup လုပ်ပါ။

> [!NOTE]
> သင့် API key ကို code ထဲကနေ ခွဲထားတာကောင်းပါတယ်။ Environment variables တွေကိုအသုံးပြုပြီး အဲ့ဒီအရာကိုလုပ်နိုင်ပါတယ်။
>
> - Environment variable `OPENAI_API_KEY` ကို သင့် API key အဖြစ် set လုပ်ပါ။
>   `export OPENAI_API_KEY='sk-...'`

### Azure configuration ကို setup လုပ်ပါ

Azure OpenAI ကိုအသုံးပြုနေတယ်ဆိုရင် configuration ကို setup လုပ်ပုံက ဒီလိုပါ -

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

အထက်မှာ ကျွန်တော်တို့ `api_type` ကို `azure` အဖြစ် set လုပ်ထားပြီး library ကို Azure OpenAI ကိုအသုံးပြုဖို့ပြောထားပါတယ်။
- `api_key` က Azure Portal မှာရှိတဲ့ API key ဖြစ်ပါတယ်။
- `api_version` က သင်အသုံးပြုချင်တဲ့ API ရဲ့ version ဖြစ်ပါတယ်။ ဒီစာရေးချိန်မှာ နောက်ဆုံး version က `2023-05-15` ဖြစ်ပါတယ်။
- `api_base` က API ရဲ့ endpoint ဖြစ်ပါတယ်။ သင့် API key အနီးမှာ Azure Portal မှာရှာနိုင်ပါတယ်။

> [!NOTE] > `os.getenv` က environment variables တွေကိုဖတ်တဲ့ function တစ်ခုဖြစ်ပါတယ်။ `OPENAI_API_KEY` နဲ့ `API_BASE` လို environment variables တွေကို ဖတ်ဖို့အသုံးပြုနိုင်ပါတယ်။ ဒီ environment variables တွေကို သင့် terminal မှာ set လုပ်ပါ သို့မဟုတ် `dotenv` လို library တစ်ခုကိုအသုံးပြုပါ။

## စာသားထုတ်လုပ်ခြင်း

စာသားထုတ်လုပ်ဖို့ `Completion` class ကိုအသုံးပြုရပါတယ်။ ဥပမာ -

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

အထက်က code မှာ ကျွန်တော်တို့ completion object တစ်ခုကိုဖန်တီးပြီး model နဲ့ prompt ကို pass လုပ်ပါတယ်။ ပြီးတော့ generated text ကို print လုပ်ပါတယ်။

### Chat completions

အခုထိ ကျွန်တော်တို့ `Completion` ကိုအသုံးပြုပြီး စာသားထုတ်လုပ်ပုံကိုကြည့်ခဲ့ပါတယ်။ ဒါပေမယ့် chatbot တွေအတွက်ပိုသင့်တော်တဲ့ `ChatCompletion` လို့ခေါ်တဲ့ class တစ်ခုရှိပါတယ်။ အဲ့ဒီကိုအသုံးပြုပုံက ဒီလိုပါ -

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

ဒီ functionality အကြောင်းကို နောက်အခန်းမှာ ပိုမိုလေ့လာပါမယ်။

## လေ့ကျင့်ခန်း - သင့်ပထမဆုံးစာသားထုတ်လုပ်မှုအက်ပလီကေးရှင်း

openai ကို setup လုပ်နဲ့ configure လုပ်ပုံကို သင်လေ့လာပြီးတဲ့အခါမှာ သင့်ပထမဆုံးစာသားထုတ်လုပ်မှုအက်ပလီကေးရှင်းကို တည်ဆောက်ဖို့အချိန်ရောက်ပါပြီ။ အက်ပလီကေးရှင်းကိုတည်ဆောက်ဖို့ အောက်ပါအဆင့်တွေကိုလိုက်နာပါ -

1. Virtual environment တစ်ခုဖန်တီးပြီး openai ကို install လုပ်ပါ -

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows ကိုအသုံးပြုနေတယ်ဆိုရင် `venv\Scripts\activate` ကို `source venv/bin/activate` အစားရိုက်ပါ။

   > [!NOTE]
   > သင့် Azure OpenAI key ကို [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) ကိုသွားပြီး `Open AI` ကိုရှာပါ၊ `Open AI resource` ကိုရွေးပြီး `Keys and Endpoint` ကိုရွေးပြီး `Key 1` value ကို copy လုပ်ပါ။

1. _app.py_ ဖိုင်တစ်ခုဖန်တီးပြီး အောက်ပါ code ကိုထည့်ပါ -

   ```python
   import openai

   openai.api_key = "<replace this value with your open ai key or Azure OpenAI key>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint found in Azure Portal where your API key is>"
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"
   messages = [{"role": "user", "content": prompt}]

   # make completion
   completion = openai.chat.completions.create(model=deployment_name, messages=messages)

   # print response
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > Azure OpenAI ကိုအသုံးပြုနေတယ်ဆိုရင် `api_type` ကို `azure` အဖြစ် set လုပ်ပြီး `api_key` ကို သင့် Azure OpenAI key အဖြစ် set လုပ်ပါ။

   သင် output ကို အောက်ပါလိုမျိုးတွေ့ရပါမယ် -

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Prompt အမျိုးမျိုး၊ အမျိုးမျိုးသောအရာများအတွက်

အခု သင် prompt ကိုအသုံးပြုပြီး စာသားထုတ်လုပ်ပုံကိုကြည့်ပြီးပြီ။ သင် modify လုပ်ပြီး text အမျိုးမျိုးကိုထုတ်လုပ်ဖို့ program တစ်ခု run လုပ်နိုင်ပါပြီ။

Prompt တွေကို task အမျိုးမျိုးအတွက် အသုံးပြုနိုင်ပါတယ်။ ဥပမာ -

- **စာသားအမျိုးအစားတစ်ခုကိုထုတ်လုပ်ပါ**။ ဥပမာ - ကဗျာ၊ quiz အတွက်မေးခွန်းတွေ စသည်ဖြင့်။
- **အချက်အလက်ရှာဖွေခြင်း**။ Prompt တွေကို အသုံးပြုပြီး အချက်အလက်တွေကိုရှာဖွေနိုင်ပါတယ်။ ဥပမာ 'What does CORS mean in web development?'.
- **Code ထုတ်လုပ်ခြင်း**။ Prompt တွေကိုအသုံးပြုပြီး code ကိုထုတ်လုပ်နိုင်ပါတယ်။ ဥပမာ email တွေကို validate လုပ်ဖို့ regular expression တစ်ခုကိုတည်ဆောက်ခြင်း သို့မဟုတ် web app တစ်ခုလို program တစ်ခုလုံးကိုတည်ဆောက်ခြင်း။

## ပိုမိုအသုံးဝင်တဲ့အသုံးချမှု - အစားအစာချက်ပြုတ်နည်းထုတ်လုပ်ခြင်း

သင်အိမ်မှာရှိတဲ့အစားအစာတွေကို အသုံးပြုပြီး တစ်ခုခုချက်ချင်တယ်ဆိုပါစို့။ အဲ့ဒီအတွက် အစားအစာချက်ပြုတ်နည်းတစ်ခုလိုအပ်ပါတယ်။ အစားအစာချက်ပြုတ်နည်းတွေကိုရှာဖို့ search engine တစ်ခုကိုအသုံးပြုနိုင်သလို LLM ကိုလည်းအသုံးပြုနိုင်ပါတယ်။

သင် prompt ကို ဒီလိုရေးနိုင်ပါတယ် -

> "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"

အထက်ပါ prompt ကိုပေးလိုက်တဲ့အခါမှာ သင်ရရှိနိုင်တဲ့အဖြေက -

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

ဒီရလဒ်ကောင်းပါတယ်၊ ကျွန်တော်တို့ဘာချက်ရမလဲဆိုတာသိပါတယ်။ ဒီအချိန်မှာ အသုံးဝင်တဲ့တိုးတက်မှုတွေက -

- သင်မကြိုက်တဲ့အစားအစာတွေ သို့မဟုတ် အာလူးပျက်တဲ့အစားအစာတွေကို ဖယ်ထုတ်ခြင်း။
- အိမ်မှာမရှိတဲ့အစားအစာတွေကို ဝယ်ဖို့ shopping list တစ်ခုထုတ်လုပ်ခြင်း။

အထက်ပါအခြေအနေတွေအတွက် prompt တစ်ခုထပ်ထည့်ပါ -

> "Please remove recipes with garlic as I'm allergic and replace it with something else. Also, please produce a shopping list for the recipes, considering I already have chicken, potatoes and carrots at home."

အခု သင့်ရလဒ်အသစ်က -

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

ဒါက သင့်ရဲ့ အစားအစာချက်ပြုတ်နည်း ၅ ခုဖြစ်ပြီး garlic မပါဘဲ ရရှိပါတယ်။ အိမ်မှာရှိပြီးသားအစားအစာတွေကိုထည့်သွင်းပြီး shopping list ကိုလည်းရရှိပါတယ်။

## လေ့ကျင့်ခန်း - အစားအစာချက်ပြုတ်နည်းထုတ်လုပ်ခြင်း

အခု ကျွန်တော်တို့အခြေအနေတစ်ခုကို ပြသပြီးပြီဆိုတော့ အဲ့ဒီအ
  ```python
  old_prompt_result = completion.choices[0].message.content
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  messages = [{"role": "user", "content": new_prompt}]
  completion = openai.Completion.create(engine=deployment_name, messages=messages, max_tokens=1200)

  # print response
  print("Shopping list:")
  print(completion.choices[0].message.content)
  ```

  အောက်ပါအချက်များကို သတိပြုပါ:

  1. ပထမဆုံး prompt မှရလဒ်ကို အသစ်သော prompt ထဲသို့ ထည့်သွင်းပြီး prompt အသစ်တစ်ခုကို တည်ဆောက်နေပါသည်။

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. အသစ်သောတောင်းဆိုမှုတစ်ခုကို ပြုလုပ်ပါ၊ သို့သော် ပထမဆုံး prompt တွင် တောင်းဆိုခဲ့သော token အရေအတွက်ကိုလည်း ထည့်သွင်းစဉ်းစားပါ၊ ထို့ကြောင့် ဒီတစ်ခါမှာတော့ `max_tokens` ကို 1200 ဟု ပြောပါ။

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     ဒီ code ကို စမ်းကြည့်ပြီးနောက်မှာတော့ အောက်ပါ output ကို ရရှိလာပါပြီ:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## သင့် setup ကို တိုးတက်အောင်လုပ်ပါ

အခုအချိန်ထိ ကျွန်တော်တို့မှာ အလုပ်လုပ်တဲ့ code ရှိပြီးသားဖြစ်ပေမယ့် အချို့အရာတွေကို ပိုမိုကောင်းမွန်အောင် ပြုပြင်သင့်ပါတယ်။ ကျွန်တော်တို့ ပြုလုပ်သင့်တဲ့အရာတွေကတော့:

- **Secrets ကို code မှ ခွဲထုတ်ပါ**, API key ကဲ့သို့သော Secrets တွေကို code ထဲမှာ မထည့်သင့်ပါဘူး။ Secrets တွေကို လုံခြုံတဲ့နေရာမှာ သိမ်းဆည်းထားသင့်ပါတယ်။ Secrets တွေကို code မှ ခွဲထုတ်ဖို့အတွက် environment variables တွေကို အသုံးပြုနိုင်ပြီး `python-dotenv` ကဲ့သို့သော library တွေကို အသုံးပြု၍ ဖိုင်ထဲမှ load လုပ်နိုင်ပါတယ်။ ဒါကို code မှာ ဘယ်လိုလုပ်ရမလဲဆိုတာကတော့:

  1. `.env` ဖိုင်တစ်ခုကို အောက်ပါအကြောင်းအရာများဖြင့် ဖန်တီးပါ:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Azure အတွက်တော့ အောက်ပါ environment variables တွေကို သတ်မှတ်ရန်လိုအပ်ပါသည်:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     Code မှာတော့ environment variables တွေကို အောက်ပါအတိုင်း load လုပ်ပါ:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Token အရေအတွက်အကြောင်း**. ကျွန်တော်တို့လိုချင်တဲ့ text ကို ဖန်တီးဖို့အတွက် token အရေအတွက်ကို စဉ်းစားသင့်ပါတယ်။ Token တွေက ပိုက်ဆံကုန်ကျစေပါတယ်၊ ထို့ကြောင့် အလားအလာရှိသမျှ token အရေအတွက်ကို သက်သာစွာ အသုံးပြုဖို့ ကြိုးစားသင့်ပါတယ်။ ဥပမာအားဖြင့် prompt ကို အနည်းဆုံး token တွေကို အသုံးပြုနိုင်အောင် ပြောဆိုနိုင်ပါသလား?

  Token တွေကို ပြောင်းလဲဖို့ `max_tokens` parameter ကို အသုံးပြုနိုင်ပါတယ်။ ဥပမာအားဖြင့် 100 tokens ကို အသုံးပြုချင်တယ်ဆိုရင်တော့:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Temperature ကို စမ်းသပ်ခြင်း**. Temperature ဆိုတာ ကျွန်တော်တို့ အခုထိ မပြောခဲ့သေးပေမယ့် ကျွန်တော်တို့ရဲ့ program အလုပ်လုပ်ပုံအပေါ် အရေးကြီးတဲ့ context တစ်ခုဖြစ်ပါတယ်။ Temperature value ပိုမြင့်လျှင် output ပိုမို random ဖြစ်လာပါမည်။ အပြန်အလှန် Temperature value ပိုနိမ့်လျှင် output ပိုမိုခန့်မှန်းနိုင်သော ဖြစ်လာပါမည်။ Output မှာ အမျိုးမျိုးပြောင်းလဲမှုရှိစေချင်သလား မရှိစေချင်သလား စဉ်းစားပါ။

  Temperature ကို ပြောင်းလဲဖို့ `temperature` parameter ကို အသုံးပြုနိုင်ပါတယ်။ ဥပမာအားဖြင့် temperature ကို 0.5 သတ်မှတ်ချင်တယ်ဆိုရင်တော့:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > သတိပြုပါ၊ 1.0 နီးစပ်လျှင် output ပိုမိုအမျိုးမျိုးပြောင်းလဲမှုရှိပါမည်။

## အလုပ်ပေးခြင်း

ဒီအလုပ်ပေးမှုအတွက် သင်တစ်ခုခုကို ဖန်တီးနိုင်ပါတယ်။

အောက်ပါအကြံပြုချက်များကို ကြည့်ပါ:

- Recipe generator app ကို ပိုမိုကောင်းမွန်အောင် ပြုပြင်ပါ။ Temperature value တွေကို စမ်းသပ်ပြီး prompt တွေကို ပြောင်းလဲကြည့်ပါ။
- "Study buddy" တစ်ခုကို ဖန်တီးပါ။ ဒီ app က Python ကဲ့သို့သော အကြောင်းအရာတစ်ခုအကြောင်းကို မေးခွန်းများကို ဖြေဆိုနိုင်ရမည်။ ဥပမာအားဖြင့် "Python မှာ အကြောင်းအရာတစ်ခုက ဘာလဲ?" ဆိုပြီး prompt တွေကို အသုံးပြုနိုင်ပါတယ်၊ ဒါမှမဟုတ် "အကြောင်းအရာတစ်ခုအတွက် code ကို ပြပါ" ဆိုတဲ့ prompt ကို အသုံးပြုနိုင်ပါတယ်။
- History bot, သမိုင်းကို အသက်ဝင်အောင်လုပ်ပါ၊ bot ကို သမိုင်းဆိုင်ရာ လူပုဂ္ဂိုလ်တစ်ဦးအဖြစ် သတ်မှတ်ပြီး သူ့ရဲ့ဘဝနှင့်အချိန်ကာလအကြောင်းကို မေးခွန်းများမေးပါ။

## ဖြေရှင်းချက်

### Study buddy

အောက်တွင် starter prompt တစ်ခုရှိပါတယ်၊ သင့်အကြိုက်အတိုင်း ပြောင်းလဲအသုံးပြုနိုင်ပါတယ်။

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### History bot

သင်အသုံးပြုနိုင်မည့် prompt အချို့မှာ:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## အသိပညာစစ်ဆေးခြင်း

Temperature ဆိုတဲ့ အယူအဆက ဘာလုပ်ပေးသလဲ?

1. Output ဘယ်လောက် random ဖြစ်မလဲဆိုတာကို ထိန်းချုပ်ပေးသည်။
1. Response ဘယ်လောက်ကြီးမလဲဆိုတာကို ထိန်းချုပ်ပေးသည်။
1. အသုံးပြုမည့် token အရေအတွက်ကို ထိန်းချုပ်ပေးသည်။

## 🚀 စိန်ခေါ်မှု

အလုပ်ပေးမှုကို လုပ်နေစဉ်မှာ Temperature ကို ပြောင်းလဲကြည့်ပါ၊ 0, 0.5, 1 ကို သတ်မှတ်ကြည့်ပါ။ 0 က အနည်းဆုံး varied ဖြစ်ပြီး 1 က အများဆုံး varied ဖြစ်သည်။ သင့် app အတွက် ဘယ် value က အကောင်းဆုံးအလုပ်လုပ်မလဲ?

## အလွန်ကောင်းမွန်သောအလုပ်! သင့်ရဲ့ သင်ယူမှုကို ဆက်လက်လုပ်ဆောင်ပါ

ဒီသင်ခန်းစာကို ပြီးမြောက်ပြီးနောက်မှာ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ပြီး သင့်ရဲ့ Generative AI အသိပညာကို ဆက်လက်မြှင့်တင်ပါ!

Lesson 7 သို့ သွားပါ၊ အဲဒီမှာ [chat applications ဖန်တီးပုံ](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ပါ!

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာပိုင်အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။