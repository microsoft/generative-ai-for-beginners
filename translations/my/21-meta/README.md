<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:14:11+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "my"
}
-->
# Meta မိသားစု မော်ဒယ်များဖြင့် ဆောက်လုပ်ခြင်း

## နိဒါန်း

ဒီသင်ခန်းစာမှာ ဖော်ပြမယ့်အကြောင်းအရာတွေကတော့ -

- Meta မိသားစုရဲ့ အဓိက မော်ဒယ်နှစ်ခုဖြစ်တဲ့ Llama 3.1 နဲ့ Llama 3.2 ကို ရှာဖွေသုံးသပ်ခြင်း  
- မော်ဒယ်တိုင်းအတွက် အသုံးပြုမှုနဲ့ အခြေအနေများကို နားလည်ခြင်း  
- မော်ဒယ်တိုင်းရဲ့ ထူးခြားချက်တွေကို ပြသဖို့ ကုဒ်နမူနာ  

## Meta မိသားစု မော်ဒယ်များ

ဒီသင်ခန်းစာမှာ Meta မိသားစု သို့မဟုတ် "Llama Herd" မှ မော်ဒယ် ၂ မျိုးဖြစ်တဲ့ Llama 3.1 နဲ့ Llama 3.2 ကို ရှာဖွေသုံးသပ်မှာဖြစ်ပါတယ်။

ဒီမော်ဒယ်တွေဟာ မတူညီတဲ့ ဗားရှင်းတွေဖြင့် ရရှိနိုင်ပြီး GitHub Model marketplace မှာလည်း ရနိုင်ပါတယ်။ GitHub Models ကို အသုံးပြုပြီး [AI မော်ဒယ်တွေနဲ့ prototype ပြုလုပ်ခြင်း](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) အကြောင်း ပိုမိုသိရှိနိုင်ပါတယ်။

မော်ဒယ် ဗားရှင်းများ -  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*မှတ်ချက် - Llama 3 ကိုလည်း GitHub Models မှာ ရနိုင်သော်လည်း ဒီသင်ခန်းစာမှာ မဖော်ပြပါ*

## Llama 3.1

405 ဘီလီယံ Parameters ရှိတဲ့ Llama 3.1 ဟာ open source LLM အမျိုးအစားထဲမှာ ပါဝင်ပါတယ်။

ဒီမော်ဒယ်ဟာ ယခင်ထွက်ရှိခဲ့တဲ့ Llama 3 ကို အဆင့်မြှင့်တင်ထားပြီး -

- ပိုကြီးမားတဲ့ context window - 128k tokens vs 8k tokens  
- ပိုကြီးမားတဲ့ Max Output Tokens - 4096 vs 2048  
- ပိုကောင်းမွန်တဲ့ ဘာသာစကားစုံထောက်ခံမှု - သင်ကြားမှု tokens တိုးမြှင့်မှုကြောင့်  

ဒီအချက်တွေကြောင့် Llama 3.1 ဟာ GenAI အက်ပလီကေးရှင်းတွေ ဖန်တီးရာမှာ ပိုမိုရှုပ်ထွေးတဲ့ အသုံးပြုမှုတွေကို ကိုင်တွယ်နိုင်ပါတယ်၊ အထူးသဖြင့် -  
- Native Function Calling - LLM workflow အပြင်ရှိ အပြင် tools နဲ့ function တွေကို ခေါ်ယူနိုင်ခြင်း  
- ပိုကောင်းမွန်တဲ့ RAG လုပ်ဆောင်ချက် - context window ကြီးမားမှုကြောင့်  
- Synthetic Data Generation - fine-tuning လုပ်ရန် အတွက် ထိရောက်တဲ့ ဒေတာဖန်တီးနိုင်ခြင်း  

### Native Function Calling

Llama 3.1 ကို function သို့မဟုတ် tool ခေါ်ယူမှုမှာ ပိုထိရောက်အောင် fine-tune လုပ်ထားပါတယ်။ ထို့အပြင် မော်ဒယ်က အသုံးပြုသူရဲ့ prompt အပေါ်မူတည်ပြီး အသုံးပြုရန်လိုအပ်တဲ့ tool နှစ်ခုကို သတ်မှတ်နိုင်ပါတယ်။ အဲဒီ tool တွေကတော့ -

- **Brave Search** - ဝဘ်ရှာဖွေရေးလုပ်ပြီး ရာသီဥတုလို အချက်အလက်အသစ်တွေ ရယူနိုင်သည်  
- **Wolfram Alpha** - ပိုရှုပ်ထွေးတဲ့ သင်္ချာတွက်ချက်မှုများအတွက် အသုံးပြုနိုင်ပြီး ကိုယ်ပိုင် function မရေးရပါ  

သင့်ကိုယ်ပိုင် custom tool တွေကိုလည်း LLM က ခေါ်ယူနိုင်အောင် ဖန်တီးနိုင်ပါတယ်။

အောက်ပါ ကုဒ်နမူနာမှာ -

- အသုံးပြုနိုင်တဲ့ tool တွေ (brave_search, wolfram_alpha) ကို system prompt မှာ သတ်မှတ်ထားသည်  
- အသုံးပြုသူက မြို့တစ်မြို့ရဲ့ ရာသီဥတုအခြေအနေကို မေးမြန်းသော prompt ပို့သည်  
- LLM က Brave Search tool ကို ခေါ်ယူမယ့် tool call ဖြင့် တုံ့ပြန်မည်ဖြစ်ပြီး `<|python_tag|>brave_search.call(query="Stockholm weather")` ဆိုပြီး ပြသမည်ဖြစ်သည်  

*မှတ်ချက် - ဤနမူနာမှာ tool call ကိုသာ ပြုလုပ်ထားပြီး ရလဒ်ရယူရန်အတွက် Brave API စာမျက်နှာတွင် အခမဲ့အကောင့်ဖွင့်ပြီး function ကို သတ်မှတ်ရပါမည်*

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

LLM ဖြစ်သော်လည်း Llama 3.1 ရဲ့ ကန့်သတ်ချက်တစ်ခုမှာ multimodality ဖြစ်ပါတယ်။ ဒါကတော့ ပုံများကဲ့သို့ input အမျိုးအစား မတူညီတဲ့ အချက်အလက်တွေကို prompt အဖြစ် အသုံးပြုနိုင်ခြင်းနဲ့ တုံ့ပြန်ချက်ပေးနိုင်ခြင်း ဖြစ်ပါတယ်။ ဒီစွမ်းဆောင်ရည်ဟာ Llama 3.2 ရဲ့ အဓိက အင်္ဂါရပ်တစ်ခုဖြစ်ပါတယ်။ အခြားအင်္ဂါရပ်တွေမှာ -

- Multimodality - စာသားနဲ့ ပုံ prompt နှစ်မျိုးလုံးကို သုံးသပ်နိုင်ခြင်း  
- အရွယ်အစား သေးငယ်မှ အလတ်စား (11B နဲ့ 90B) - တပ်ဆင်မှုရွေးချယ်စရာများ ပိုမိုလွယ်ကူစေခြင်း  
- စာသားပဲ အသုံးပြုတဲ့ ဗားရှင်းများ (1B နဲ့ 3B) - edge / mobile စက်ပစ္စည်းများတွင် တပ်ဆင်နိုင်ပြီး latency နည်းစေခြင်း  

Multimodal ထောက်ခံမှုဟာ open source မော်ဒယ်ကမ္ဘာမှာ အရေးကြီးတဲ့ တိုးတက်မှုတစ်ခုဖြစ်ပါတယ်။ အောက်ပါ ကုဒ်နမူနာမှာ ပုံနဲ့ စာသား prompt နှစ်မျိုးလုံးကို အသုံးပြုပြီး Llama 3.2 90B မှ ပုံကို ခွဲခြမ်းစိတ်ဖြာထားပါတယ်။

### Llama 3.2 နှင့် Multimodal ထောက်ခံမှု

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

## သင်ယူခြင်းကို ဒီမှာ မရပ်နားပါနဲ့၊ ခရီးကို ဆက်လက်သွားပါ

ဒီသင်ခန်းစာပြီးဆုံးပြီးနောက်မှာ ကျွန်တော်တို့ရဲ့ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ရှုဖို့ အကြံပြုပါတယ်၊ သင့် Generative AI အသိပညာကို ပိုမိုမြှင့်တင်နိုင်ဖို့!

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းမှုများ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ပညာရှင်များ၏ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။