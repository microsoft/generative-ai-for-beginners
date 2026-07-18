# Meta မိသားစု မော်ဒယ်များဖြင့် ဆောက်လုပ်ခြင်း

## အကြောင်းအရာဝင်

ဒီသင်ခန်းစာမှာ လေ့လာမယ့်အကြောင်းအရာတွေက:

- Meta မိသားစု၏ အဓိက မော်ဒယ်နှစ်မျိုးဖြစ်တဲ့ Llama 3.1 နဲ့ Llama 3.2 ကို ရှာဖွေခြင်း
- မော်ဒယ်တိုင်းအတွက် အသုံးပြုမှုနှင့် နောက်ခံအခြေအနေများကို နားလည်ခြင်း
- မော်ဒယ်တစ်ခုချင်းစီ၏ ထူးခြားတဲ့ လက္ခဏာများကိုပြသရန် ကုဒ်နမူနာ


## Meta မိသားစု မော်ဒယ်များ

ဒီသင်ခန်းစာမှာတော့ Meta မိသားစု သို့မဟုတ် "Llama Herd" က မော်ဒယ် ၂ မျိုးဖြစ်တဲ့ Llama 3.1 နဲ့ Llama 3.2 ကို အကျယ်ကြီး လေ့လာပါမယ်။

မော်ဒယ်တွေဟာ မတူညီတဲ့ ဗားရှင်းတွေထဲက ရရှိနိုင်ပြီး [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) မှာ ရရှိနိုင်ပါတယ်။

> **မှတ်ချက်။** GitHub Models ကို 2026 ခုနှစ် ဇူလိုင်လ အဆုံးတွင် သုံးရပ်သွားပါပြီ။ AI မော်ဒယ်များနဲ့ စမ်းသပ်ဖို့ [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ကို အသုံးပြုခြင်းအကြောင်း အသေးစိတ်ကို ဒီမှာ ကြည့်နိုင်ပါတယ်။

မော်ဒယ် ဗားရှင်းများ:
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*မှတ်ချက်။ Llama 3 ကို Microsoft Foundry Models မှာလည်း ရနိုင်သော်လည်း ဒီသင်ခန်းစာမှာ မဖော်ပြပါဘူး*

## Llama 3.1

Parameters ၄၀၅ ဘီလီယံပါဝင်သော Llama 3.1 သည် အခမဲ့ LLM များအုပ်စုတွင်ပါဝင်သည်။

ဒီမော်ဒယ်ဟာ Llama 3 ရဲ့ ဒေသန္တရ version ကို အောက်ပါအတိုင်း အဆင့်မြှင့်ထားတာဖြစ်ပါတယ်။

- ကြီးမားသည့် context window - ၁၂၈ကေတင် vs ၈ကေတင်
- ကြီးမားသည့် Max Output Tokens - ၄၀၉၆ vs ၂၀၄၈
- Multilingual ပိုမိုကောင်းမွန်စွာ ထောက်ပံ့မှု - သင်ကြားမှု token များ ပိုမိုရှိခြင်းကြောင့်

ဒီအရာတွေကြောင့် Llama 3.1 ဟာ GenAI အက်ပ်လီကေးရှင်းတွေကို ဆောက်လုပ်ချိန်မှာ ပိုမိုရှုပ်ထွေးတဲ့ အသုံးချမှုနယ်ပယ်များကို ကိုင်တွယ်နိုင်ပါတယ်။
- Native Function Calling - LLM workflow ပြင်ပက ကိရိယာများနှင့် လုပ်ဆောင်ချက်များကို ခေါ်ယူနိုင်စွမ်း
- ပိုမိုကောင်းမွန်သည့် RAG ဖော်ဆောင်ချက် - context window ကြီးပါသောကြောင့်
- Synthetic Data Generation - fine-tuning စသည့် လုပ်ငန်းများအတွက် ထိရောက်သော ဒေတာဖန်တီးနိုင်ခြင်း

### Native Function Calling

Llama 3.1 ကို function သို့မဟုတ် tool call များကို ပိုကောင်းစွာ ပြုလုပ်နိုင်ရန် အကောင်းဆုံး ပြုလုပ်ရေး ထားပြီး ရှိပါတယ်။ မော်ဒယ်မှာ အသုံးပြုသူ၏ prompt အရ ထောက်ခံရန် လိုအပ်သော ပြင်ပ tools နှစ်ခု built-in ပါဝင်သည်။ အဲ့ဒီ tool များမှာ:

- **Brave Search** - ဘာသာရပ် အသစ်များကို ရှာဖွေရန် အင်တာနက်ရှာဖွေရေးအတွက် အသုံးပြုနိုင်သည်၊ ဥပမာ - ရာသီဥတု
- **Wolfram Alpha** - ပိုမိုရှုပ်ထွေးသော သင်္ချာကဏ္ဍများတွက်ချက်ရန်အသုံးပြုနိုင်ပြီး ကိုယ်ပိုင် function ရေးရန် မလိုအပ်ပါ။

လဲ၊ LLM က ခေါ်ယူနိုင်တဲ့ ကိုယ်ပိုင် tools များကိုလည်း ဖန်တီးနိုင်ပါတယ်။

အောက်တွင် ကုဒ်ဥပမာမှာ:

- စနစ် prompt ထဲမှာ အသုံးပြုနိုင် tool များ (brave_search, wolfram_alpha) ကို သတ်မှတ်ထားပါတယ်။
- အသုံးပြုသူက ထူးခြားတဲ့ မြို့တစ်မြို့ရဲ့ ရာသီဥတုကို မေးမြန်းတဲ့ prompt ပို့သည်။
- LLM က Brave Search tool ကို tool call အဖြစ် တုံ့ပြန်ပါလိမ့်မယ်။ ဥပမာ `<|python_tag|>brave_search.call(query="Stockholm weather")`

*မှတ်ချက်။ ဒီဥပမာမှာ tool call ကိုသာ ပြုလုပ်ထားပြီး၊ ရလဒ်ရရှိရန်အတွက် Brave API စာမျက်နှာမှာ အခမဲ့ အကောင့်ဖွင့်ပြီး function ကို သင့်ဘာသာ သတ်မှတ်ရပါမယ်။

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# သင်၏ Microsoft Foundry ပရောဂျက်၏ "အကျဉ်းချုပ်" စာမျက်နှာမှ ဒီအချက်တွေကိုရယူပါ
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

Llama 3.1 သည် LLM ဖြစ်ပေမယ့် မျိုးစုံ input များကို အသုံးပြု၍ တုံ့ပြန်နိုင်ခြင်းမရှိခြင်းမှာ အားနည်းချက်တစ်ခုဖြစ်သည်။ ဤစွမ်းရည်သည် Llama 3.2 ၏ အခြေခံ လက္ခဏာတစ်ခုဖြစ်သည်။ ထို့အပြင် အခြား feature များမှာ:

- Multimodality - စာသားနှင့် ဓာတ်ပုံ prompt နှစ်မျိုးကိုလည်း သုံးပြီး ဖော်ထုတ်နိုင်စွမ်း
- အရွယ်အစား အသေးစားမှ အလယ်အလတ် (11B နှင့် 90B) - ကြိုက်တဲ့ deployment options ပေးသည်
- စာသားပဲ ပါဝင်သော အမျိုးအစားများ (1B နှင့် 3B) - edge / mobile devices တွင် တပ်ဆင်ရန် လွယ်ကူပြီး latency နည်းစေသည်

Multimodal support သည် အခမဲ့ models လောကတွင် အဆင့်ကြီးတစ်ခု ဖြစ်သည်။ အောက်ပါကုဒ်ဥပမာသည် Llama 3.2 90B မှ အဖြေကို ရယူရန် ဓာတ်ပုံနှင့် စာသား prompt နှစ်ခုကို လက်ခံသည်။


### Llama 3.2 ဖြင့် Multimodal Support

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

# သင့် Microsoft Foundry ပရောဂျက်၏ "အကျဉ်းချုပ်" စာမျက်နှာမှ ဤအချက်များကို ရယူပါ
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
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

## သင်ယူမှုကို ဒီမှာ မရပ်ပါနဲ့၊ ခြေလှမ်းဆက်လက်လျောက်ပါ

ဒီသင်ခန်းစာပြီးစီးပြီးနောက်၊ ကျွန်ုပ်တို့၏ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ရှု၍ Generative AI အသိပညာကို ဆက်လက်မြှင့်တင်ပါ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->