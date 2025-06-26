<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:36:58+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "my"
}
-->
# Meta မိသားစု မော်ဒယ်များဖြင့် ဆောက်လုပ်ခြင်း

## နိဒါန်း

ဒီသင်ခန်းစာမှာ အောက်ပါအကြောင်းအရာများကို လေ့လာပါမည် -

- Meta မိသားစုမော်ဒယ်များ၏ အဓိကနှစ်ခုဖြစ်သော Llama 3.1 နှင့် Llama 3.2 ကို ရှာဖွေခြင်း
- မော်ဒယ်တစ်ခုစီ၏ အသုံးပြုမှုများနှင့် ရှင်းလင်းမှုများကို နားလည်ခြင်း
- မော်ဒယ်တစ်ခုစီ၏ ထူးခြားသော လက္ခဏာများကို ပြသသော ကုဒ်နမူနာ

## Meta မိသားစု မော်ဒယ်များ

ဒီသင်ခန်းစာမှာ Meta မိသားစုမှ "Llama Herd" အဖြစ်လူသိများသော မော်ဒယ်နှစ်ခုဖြစ်သော Llama 3.1 နှင့် Llama 3.2 ကို ရှာဖွေပါမည်

ဒီမော်ဒယ်များသည် မျိုးကွဲများစွာရှိပြီး GitHub Model Marketplace တွင် ရရှိနိုင်ပါသည်။ GitHub Models ကို အသုံးပြုပြီး [AI မော်ဒယ်များဖြင့် ပုံစံတူလုပ်ဆောင်ခြင်း](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) ကို အသုံးပြုခြင်းနှင့် ပတ်သက်သော အသေးစိတ်ကို ဒီမှာတွေ့ပါ။

မော်ဒယ်မျိုးကွဲများ:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Note: Llama 3 သည် GitHub Models တွင်လည်း ရရှိနိုင်ပါသည် သို့သော် ဒီသင်ခန်းစာမှာ မလွှမ်းခြုံပါ*

## Llama 3.1

405 Billion Parameters ရှိသော Llama 3.1 သည် အမှီအခိုကင်းသော LLM ကဏ္ဍတွင် ပါဝင်သည်။

ဒီမော်ဒယ်သည် Llama 3 ၏ ယခင်ထုတ်ဝေမှုကို အဆင့်မြှင့်တင်ခြင်းဖြင့် ပေးသွင်းသည် -

- ကြီးမားသော အကြောင်းအရာဝင်းဒိုး - 128k tokens vs 8k tokens
- ကြီးမားသော အထွက် Tokens အများဆုံး - 4096 vs 2048
- မြန်မာဘာသာစကား အထောက်အပံ့ပိုမိုကောင်းမွန် - လေ့ကျင့်မှု tokens အရေအတွက်များများကြောင့်

ဒီအချက်များသည် GenAI လျှောက်လွှာများ ဆောက်လုပ်ရာတွင် ပိုမိုစိစစ်ရလွယ်ကူသော အသုံးပြုမှုများကို Llama 3.1 အတွက် စီမံခန့်ခွဲနိုင်စေသည် -
- ပွင့်လင်းသော လုပ်ဆောင်မှုခေါ်ယူမှု - LLM လုပ်ငန်းစဉ်အပြင်မှာ အပြင်ဘက်ကိရိယာများနှင့် လုပ်ဆောင်မှုများကို ခေါ်ယူနိုင်ခြင်း
- RAG စွမ်းဆောင်ရည် ပိုမိုကောင်းမွန်ခြင်း - အကြောင်းအရာဝင်းဒိုးကြီးမားခြင်းကြောင့်
- သင်္ဘောစစ်ဆေးမှုအတွက် ထိရောက်သော ဒေတာဖန်တီးခြင်း - အထူးပြုပြင်မှုများနှင့် အခြားလုပ်ငန်းများအတွက် ဒေတာကို ဖန်တီးနိုင်ခြင်း

### ပွင့်လင်းသော လုပ်ဆောင်မှုခေါ်ယူမှု

Llama 3.1 သည် လုပ်ဆောင်မှုခေါ်ယူမှုများကို ပိုမိုထိရောက်စေဖို့ အထူးပြုပြင်ထားသည်။ ဒါ့အပြင် မော်ဒယ်သည် အသုံးပြုသူ၏ အကြောင်းအရာပေးသည့်အရ လိုအပ်သော ကိရိယာများကို မှတ်မိနိုင်သော ကိရိယာနှစ်ခု ပါဝင်သည်။ အဆိုပါ ကိရိယာများမှာ -

- **Brave Search** - မိုးလေဝသကို ကြည့်ရှုရန်လိုအပ်သည့်အချက်အလက်များကို အွန်လိုင်းရှာဖွေရန် အသုံးပြုနိုင်သည်
- **Wolfram Alpha** - ပိုမိုခက်ခဲသော သင်္ချာတွက်ချက်မှုများအတွက် အသုံးပြုနိုင်ပြီး ကိုယ်ပိုင်လုပ်ဆောင်မှုများရေးရန် မလိုအပ်ပါ

သင်၏ကိုယ်ပိုင်ထုံးစံကိရိယာများကို LLM ကခေါ်ယူနိုင်ရန် ဖန်တီးနိုင်ပါသည်။

အောက်ပါကုဒ်နမူနာတွင် -

- စနစ်အကြောင်းအရာမှာ ရရှိနိုင်သော ကိရိယာများ (brave_search, wolfram_alpha) ကို သတ်မှတ်ပါ။
- ရှိသောမြို့၏ မိုးလေဝသကို မေးသော အသုံးပြုသူ၏ အကြောင်းအရာပေးပါ။
- LLM သည် Brave Search ကိရိယာကို ခေါ်ယူသည့် ကိရိယာခေါ်ယူမှုဖြင့် တုံ့ပြန်လိမ့်မည် `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Note: ဤနမူနာသည် ကိရိယာခေါ်ယူမှုကိုသာ ပြုလုပ်သည်၊ ရလဒ်ကို ရယူလိုပါက Brave API စာမျက်နှာတွင် အခမဲ့အကောင့်ဖန်တီးပြီး လုပ်ဆောင်မှုကို သတ်မှတ်ရန် လိုအပ်ပါသည်*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2

Llama 3.1 သည် LLM ဖြစ်သော်လည်း သုံးနိုင်မှုအကန့်အသတ်တစ်ခုရှိသည်။ ဒါကတော့ input အမျိုးအစားများကို အသုံးပြုပြီး ပုံတူရေးသားခြင်းဖြင့် တုံ့ပြန်နိုင်ခြင်းဖြစ်သည်။ ဤစွမ်းရည်သည် Llama 3.2 ၏ အဓိကလက္ခဏာများထဲမှ တစ်ခုဖြစ်သည်။ အဆိုပါ လက္ခဏာများတွင် -

- Multimodality - စာသားနှင့် ပုံတူများကို အကဲဖြတ်နိုင်ခြင်း
- သေးငယ်မှ အလယ်အလတ်အရွယ်အစားမျိုးကွဲများ (11B နှင့် 90B) - ဒါကတော့ တပ်ဆင်မှုရွေးချယ်မှုများကို ပေးသည်
- စာသားသာလျှင်မျိုးကွဲများ (1B နှင့် 3B) - မော်ဒယ်ကို edge / mobile devices တွင် တပ်ဆင်ရန်နှင့် နိမ့်သော latency ကို ပေးသည်

Multimodal အထောက်အပံ့သည် အမှီအခိုကင်းသော မော်ဒယ်များ၏ ကမ္ဘာတွင် အကြီးမားသော အဆင့်တစ်ခုကို ကိုယ်စားပြုသည်။ အောက်ပါကုဒ်နမူနာသည် ပုံတူနှင့် စာသားအကြောင်းအရာကို ယူပြီး Llama 3.2 90B မှ ပုံတူ၏ အကဲဖြတ်ချက်ကို ရယူပါမည်။

### Llama 3.2 ဖြင့် Multimodal အထောက်အပံ့

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## လေ့လာမှုသည် ဤနေရာတွင် မဆုံးပါ၊ ခရီးကို ဆက်လက်လုပ်ဆောင်ပါ

ဒီသင်ခန်းစာကို ပြီးမြောက်ပြီးနောက်၊ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ရှုပြီး Generative AI အသိပညာကို ဆက်လက်မြှင့်တင်ပါ!

**ထုတ်ပြန်ချက်**:  
ဤစာရွက်ကို AI ဘာသာပြန်ရေးဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် မှန်ကန်မှုကို လှုပ်ရှားကြသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းမှုများ ပါဝင်နိုင်ကြောင်း သိရှိထားရန် ကျေးဇူးပြု၍ သတိပြုပါ။ မူရင်းစာရွက်ကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာရှိသော အရင်းအမြစ်အဖြစ် ရှုမြင်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူ့ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားယွင်းမှုများ သို့မဟုတ် အဓိပ္ပာယ်အလွဲများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။