# Meta မိသားစု မော်ဒယ်များဖြင့် တည်ဆောက်ခြင်း

## နိဒါန်း

ဒီသင်ခန်းစာမှာ မျှဝေပါမယ့်အချက်တွေက -

- Meta မိသားစုမော်ဒယ် အဓိက ၂ မော်ဒယ်များဖြစ်သော Llama 3.1 နှင့် Llama 3.2 ကို ရှာဖွေကြည့်ရှုခြင်း၊ တစ်ခါတည်း ရိုးရာ မော်ဒယ်ယူနစ်များဖြစ်သည့် Llama 3.3 နှင့် Llama 4 ပါဝင်သော အနေနဲ့ ကုဒ်နမူနာတွင် သုံးထားသော နောက်ထပ် ရွေးချယ်စရာများ
- မော်ဒယ်တိုင်း၏ အသုံးပြုမှုကိစ္စများနှင့် လမ်းကြောင်းများကို နားလည်ခြင်း
- မော်ဒယ်တစ်ခုစီ၏ ထူးခြားချက်များကို ပြသထားသော ကုဒ်နမူနာ


## Meta မိသားစု မော်ဒယ်များ

ဒီသင်ခန်းစာတွင် ကျွန်တော်တို့သည် Meta မိသားစု သို့မဟုတ် "Llama Herd" မှ မော်ဒယ် ၂ မော်ဒယ်ဖြစ်သည့် Llama 3.1 နှင့် Llama 3.2 ကို စူးစမ်းလေ့လာပါမည်။ လည်ပတ်နိုင်သော ကုဒ်နမူနာများတွင် Llama 3.3 နှင့် Llama 4 ကို သုံးထားပြီး၊ ၎င်းတို့မှာ လက်ရှိ Microsoft Foundry Models စာရင်း၌ ရနိုင်သော ရွေးချယ်စရာများသာဖြစ်ပါသည်။

မော်ဒယ်များသည် မတူညီသောဗားရှင်းအသွင်အပြင်များဖြင့် ရရှိနိုင်ပြီး [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) မှာလည်း ရရှိနိုင်ပါသည်။

> **မှတ်ချက်။** GitHub Models သည် ၂၀၂၆ ခုနှစ် ဇူလိုင်လကုန်တွင် ဖျက်သိမ်းမည် ဖြစ်သည်။ AI မော်ဒယ်များနှင့် Prototype ပြုလုပ်ရန် [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ကို အသုံးပြုခြင်းအကြောင်း အသေးစိတ် ပိုမိုသိရှိနိုင်ပါသည်။

> **မှတ်ချက်။** ဒီသင်ခန်းစာပထမဦးစွာရေးသားသည့် မော်ဒယ်ဗားရှင်းအသေးစိတ် (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct) များကို Microsoft Foundry Models စာရင်းမှ ရယူ ဖျက်သိမ်းထားပါသည်။ 下記のコードサンプルは`Llama-3.3-70B-Instruct` မှတ်တိုင်းကို သုံးထားပြီး Microsoft Foundry Models စာရင်းတွင် လက်ရှိ ရရှိနိုင်သော ရွေးချယ်စရာများဖြစ်သော `Llama-4-Scout-17B-16E-Instruct` ကို အသုံးပြုသည်။

မော်ဒယ်ဗားရှင်းများ (ဒီသင်ခန်းစာဖော်ပြချက်အရ):
- Llama 3.1 - 70B Instruct (ဖျက်သိမ်းပြီး)
- Llama 3.1 - 405B Instruct (ဖျက်သိမ်းပြီး)
- Llama 3.2 - 11B Vision Instruct (ဖျက်သိမ်းပြီး)
- Llama 3.2 - 90B Vision Instruct (ဖျက်သိမ်းပြီး)

လက်ရှိကိစ္စၥအတွက် ကုဒ် နမူနာတွင် အသုံးပြု နိုင်သော ရွေးချယ်စရာများ:
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`)
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`)

*မှတ်ချက်။ အထက်ဖော်ပြထားသော Llama 3 အသွင်များသည် သမိုင်းအခြေနေများအတွက်သာ ထိန်းသိမ်းထားပြီး Microsoft Foundry Models တွင် ထပ်မံရရှိနိုင်မှာမဟုတ်ပါ။*

## Llama 3.1

Llama 3.1 သည် 405 ဘီလျံ ပားရာမီတာများဖြင့် open source LLM အမျိုးအစားထဲတွင် ပါဝင်သည်။

ယခင်ထုတ်လုပ်မှု Llama 3 ကို ဦးတည်၍ အဆင့်မြှင့်တင်မှုများမှာ:

- ပိုကြီးတဲ့ context window - 128k token များ လို့ 8k tokens နှင့် နှိုင်းယှဉ်
- Max Output Tokens ပိုကြီး - 4096 က 2048 နှင့် နှိုင်းယှဉ်
- ပိုကောင်းတဲ့ बहुभाषीय ဒြပ်ပေါင်း - သင်ကြားမှု token များပိုမိုလာမှုကြောင့်

ဒီအချက်တွေကြောင့် Llama 3.1 သည် GenAI application တွေ တည်ဆောက်ရာမှာ များစွာရှုပ်ထွေးတဲ့ အသုံးပြုမှုအခြေအနေများကောင်းစွာ ကိုင်တွယ်နိုင်ပေသည်၊ ဤနှင့်:
- Native Function Calling - LLM workflow ပေါ်က အပြင်ကူးယူးမှုများနှင့် function များကို ခေါ်ယူနိုင်ခြင်း
- Better RAG Performance - ပိုကြီးတဲ့ context window ကြောင့်
- Synthetic Data Generation - fine-tuning ကဲ့သို့သောအလုပ်များအတွက် ထိရောက်တဲ့ ဒေတာ ဖန်တီးနိုင်ခြင်း

### Native Function Calling

Llama 3.1 ကို function သို့မဟုတ် tool ခေါ်လိုရာတွင် ပိုထိရောက်စေဖို့ fine-tune ပြုလုပ်ထားသည်။ မော်ဒယ်တွင် သုံးစွဲသူ၏ prompt အရ သုံးရန်လိုအပ်ကြောင်းတိတိကျကျသိရှိနိုင်သော tool ၂ ခုပါဝင်သည်။

- **Brave Search** - web ရှာဖွေပေး၍ ရာသီဥတုဆိုင်ရာ အပ်ဒိတ်များရစေရန် အသုံးပြုနိုင်သည်
- **Wolfram Alpha** - ရိုးရာ mathematical တွက်ချက်မှုများအတွက် အသုံးပြုနိုင်ပြီး ကိုယ့် function မရေးသားဘဲ အသုံးပြုနိုင်သည်

သင်သည် မိမိကိုယ်ပိုင် custom tool များကိုလည်း မော်ဒယ်က ခေါ်ယူနိုင်စေရန် ဖန်တီးနိုင်သည်။

အောက်ပါ ကုဒ်နမူနာတွင် -

- စနစ် prompt တွင် ရရှိနိုင်သည့် tool များ (brave_search, wolfram_alpha) ကို ပြသသည်
- သတိထားစရာ prompt တစ်ခုကို သုံးစွဲသူထံမှ ပေးပို့သည်၊ ဥပမာ - တစ်မြို့ရဲ့ ရာသီဥတု အခြေအနေ
- LLM သည် Brave Search tool ကို ခေါ်သလိုပုံ ဖြစ်လာပြီး အောက်ပါအတိုင်းသည် `<|python_tag|>brave_search.call(query="Stockholm weather")` ဖြစ်သည်။

*မှတ်ချက်။ ဒီနမူနာက tool call ကိုသာ ပြုလုပ်ပြီး ရလဒ်ရရှိရန်အတွက် သင်သည် Brave API စာမျက်နှာတွင် အခမဲ့ အကောင့်ဖွင့်၍ function ကို ကိုယ်တိုင် သတ်မှတ်ရပါမည်။

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Meta-Llama-3.1-405B-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-3.3-70B-Instruct, a currently available alternative, instead
model_name = "Llama-3.3-70B-Instruct"

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

Llama 3.1 သည် LLM ဖြစ်သော်လည်း multimodality ထောက်ပံ့မှုမရှိခြင်းသည် လွှမ်းမိုးမှုတစ်ခုဖြစ်သည်။ အဲဒါက တစ်ခုက input အမျိုးမျိုးဖြစ်သော ဓာတ်ပုံများကို prompt အဖြစ်သုံး၍ တုံ့ပြန်ချက်ပေးခြင်း မဖြစ်နိုင်ခြင်း ဖြစ်သည်။ ဒီလိုအင်္ဂါရပ်တွေထဲမှာ Llama 3.2 ရဲ့ အဓိကအင်္ဂါရပ်တစ်ခုဖြစ်ပါသည်။ ဒီအင်္ဂါရပ်များမှာ-

- Multimodality - စာသားနှင့် ဓာတ်ပုံ prompt များ စနစ်တကျ ဖတ်ရှုနိုင်ခြင်း
- အသေး/အလတ်စား အရွယ်အစားဗားရှင်းများ (11B နှင့် 90B) - ပြောရမယ်ဆို flexible deployment options ထောက်ပံ့မှု
- စာသားအတွက်သာဖြစ်သော ဗားရှင်းများ (1B နှင့် 3B) - edge / mobile device တွင် deploy လုပ်နိုင်ပြီး latency နည်းသည့် အတွက်

ဒီ multimodal support သည် open source မော်ဒယ်အတွက် ကြီးမားသော တိုးတက်မှုတစ်ခုဖြစ်သည်။ အောက်ပါကုဒ်နမူနာတွင် ဓာတ်ပုံနှင့် စာသား prompt နှစ်ခုစလုံးကိုယူပြီး ဓာတ်ပုံကို စိစစ်ခြင်း လုပ်ဆောင်သည်။ ကဲ က Llama 3.2 90B Vision Instruct ကို အသုံးမပြုတော့ပါ၊ ထိုနမူနာမှာ လက်ရှိရရှိနိုင်ပြီး native multimodal alternative ဖြစ်သော `Llama-4-Scout-17B-16E-Instruct` ကိုအသုံးပြုထားပါသည်။


### Llama 3.2 နှင့် multimodal support

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

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Llama-3.2-90B-Vision-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-4-Scout-17B-16E-Instruct, a currently available natively multimodal alternative, instead
model_name = "Llama-4-Scout-17B-16E-Instruct"

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

## သင်ယူခြင်းများမှာ အစမှာမပဲ ဆက်လက်သွားရန်

ဒီသင်ခန်းစာပြီးဆုံးပြီးနောက် ကျွန်တော်တို့ရဲ့ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ရှုပြီး သင်၏ Generative AI အတတ်ပညာ ကို ပိုမိုမြှင့်တင်လိုက်ပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->