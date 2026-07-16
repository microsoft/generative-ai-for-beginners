# Meta မိသားစု မော်ဒယ်များဖြင့် ဆောက်လုပ်ခြင်း 

## အကျဉ်းချုပ် 

ဤသင်ခန်းစာတွင် ပြောကြားသွားမည့်အကြောင်းအရာများမှာ- 

- Meta မိသားစု၏ အဓိကမော်ဒယ်နှစ်မျိုးဖြစ်သည့် Llama 3.1 နှင့် Llama 3.2 ပုံစံများကို ရှာဖွေတွေ့ရှိခြင်း 
- မော်ဒယ်တိုင်း အသုံးပြုမှုနှင့် သက်ဆိုင်ရာ အခြေအနေများကို နားလည်ခြင်း 
- မော်ဒယ်တစ်ခုချင်းစီ၏ ထူးခြားချက်များကို ပြသသည့် ကုဒ် နမူနာ 


## Meta မိသားစု၏ မော်ဒယ်များ 

ဤသင်ခန်းစာတွင် Meta မိသားစု သို့မဟုတ် "Llama Herd" မှ မော်ဒယ် ၂ မျိုးဖြစ်သည့် Llama 3.1 နှင့် Llama 3.2 ကို ရှာဖွေသွားမည်ဖြစ်သည်။

မော်ဒယ်များမှာ မတူညီသောဗားရှင်းများဖြင့် ရရှိနိုင်ပြီး [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) တွင်လည်း ရနိုင်ပါသည်။

> **မှတ်ချက်** - GitHub Models သည် ၂၀၂၆ ခုနှစ် ဇူလိုင်လ အကုန်တွင် ရပ်နားသည်။ [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ကို AI မော်ဒယ်များဖြင့် ပုံစံတင်ခြင်းအတွက် အသုံးပြုနိုင်သည့် အသေးစိတ်ကို အောက်ပိုင်းတွင် ကြည့်ရှုနိုင်ပါသည်။

မော်ဒယ်ဗားရှင်းများ- 
- Llama 3.1 - 70B အညွှန်း 
- Llama 3.1 - 405B အညွှန်း 
- Llama 3.2 - 11B Vision အညွှန်း 
- Llama 3.2 - 90B Vision အညွှန်း 

*မှတ်ချက်- Llama 3 ကို Microsoft Foundry Models တွင်လည်း ရနိုင်သော်လည်း ယခုသင်ခန်းစာတွင် မဖော်ပြပါ* 

## Llama 3.1 

၄၀၅ ဘီလျံ ပါရာမီတာနှင့်အတူ Llama 3.1 သည် open source LLM အမျိုးအစားတွင်ပါဝင်သည်။

ဤမော်ဒယ်သည် ယခင်ထွက်ရှိခဲ့သည့် Llama 3 ကို အထက်ပါအင်္ဂါရပ်များဖြင့် တိုးတက်စေသည် - 

- ကြီးမားသော context window - 128k token များ (8k token ပြိုင်) 
- ကြီးမားသော Max Output Tokens - 4096 (2048 ပြိုင်) 
- Multilingual Support ကောင်းမွန်ခြင်း - သင်ကြားမှု token များ တိုးပွားခြင်းကြောင့် 

၎င်းတို့ကြောင့် Llama 3.1 သည် GenAI အပလီကေးရှင်းများ ဆောက်လုပ်ရာတွင် ပိုမိုရှုပ်ထွေးသော အသုံးပြုမှုများကို ကျော်ဖြတ်နိုင်ပါသည်- 
- Native Function Calling - LLM workflow အပြင်ရှိ အပြင်ကိရိယာများနှင့် ဖွင့်လှစ်ပြီး သတ်မှတ်နိုင်ခြင်း 
- RAG လုပ်ဆောင်ချက်အကောင်းဆုံး - context window ကြီးမြတ်ခြင်းကြောင့် 
- သဘာဝဒေတာထုတ်လုပ်ခြင်း - ဥပမာ fine-tuning အတွက် ထိထိရောက်ရောက် ဒေတာများ ဖန်တီးနိုင်ခြင်း 

### Native Function Calling 

Llama 3.1 ကို function သို့မဟုတ် tool call များ အကျိုးရှိရှိ ပြုလုပ်နိုင်စေရန် fine-tune ပြုလုပ်ထားပြီး အသုံးပြုသူ၏ prompt အရ အသုံးပြုရန်လိုအပ်ချက်ကို မှတ်လင့်နိုင်သည့် tool နှစ်ခု ပါရှိသည်။ ထို tool များမှာ-

- **Brave Search** - web search ဖြင့် ရာသီဥတုအချက်အလက် စသည်များကို ရယူနိုင်သည် 
- **Wolfram Alpha** - ရိုက်ထားသည့် function မဟုတ်ပဲ ဆန်းစစ်ချက်ခက်ခဲသော သင်္ချာစိတ်ချက်များအတွက် အသုံးပြုနိုင်သည်။

LLM သည်သင့်ရဲ့ custom tools များကိုလည်း ခေါ်ယူနိုင်ပါသည်။

အောက်ပါကုဒ်နမူနာတွင်-

- System prompt ထဲတွင် available tools (brave_search, wolfram_alpha) များကို သတ်မှတ်ထားသည်။ 
- အသုံးပြုသူမှ ရပ်တည်ရာမြို့ရာသာရာ ရာသီဥတုမေးမြန်း prompt ပေးသည်။ 
- LLM သည် Brave Search tool ကို ခေါ်သုံးမည့် tool call တက်ပြမည်ဖြစ်ပြီး အတူတူလုပ်ဆောင်မည် `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*မှတ်ချက်- ဤနမူနာတွင် tool call သာလုပ်မည်ဖြစ်ပြီး ရလဒ်ရရှိရန်အတွက် Brave API စာမျက်နှာတွင် အခမဲ့အကောင့်ဖွင့်၍ function ကို သတ်မှတ်ရန် လိုအပ်ပါသည်* 

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# ဤအချက်အလက်များကို သင်၏ Microsoft Foundry ပရောဂျက်၏ "အနှစ်ချုပ်" စာမျက်နှာမှယူပါ။
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

Llama 3.1 သည် LLM ဖြစ်သော်လည်း multimodality မရှိခြင်းမှာ ကန့်အသတ်တစ်ခုဖြစ်သည်။ ဤသည်မှာ ပုံများကို prompt အဖြစ် သုံးနိုင်ခြင်းနှင့် တုံ့ပြန်မှုများ ပေးနိုင်ခြင်းမရှိခြင်းဖြစ်သည်။ Llama 3.2 မှာဤစွမ်းရည်ရှိပြီး ထိုဧရိယာများမှာ-

- Multimodality - စာသားနှင့် ပုံ prompt များနှစ်မျိုးလုံးကို ခွဲခြားသုံးသပ်နိုင်ခြင်း 
- အရွယ်အစား သေးငယ်မှ အလယ်အလတ်(11B နှင့် 90B) - တပ်ဆင်မှုရွေးချယ်မှု များ အလွယ်တကူ 
- စာသား သာ မျိုးစုံ (1B နှင့် 3B) - edge / mobile device များတွင် ပြေးနိုင်ပြီး latency နည်းခြင်း 

ဒီ multimodal support သည် open source မော်ဒယ်များ လောကအတွက် တိုးတက်မှု ကြီးတစ်ခု ဖြစ်သည်။ အောက်ပါ ကုဒ်နမူနာတွင် Llama 3.2 90B မှ ပုံနှင့် စာသား prompt နှစ်မျိုးလုံး ကိုယူ၍ ပုံကို ခွဲခြားသုံးသပ်ပေးမည်ဖြစ်သည်။


### Llama 3.2 တွင် Multimodal Support

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

# မိမိ၏ Microsoft Foundry စီမံကိန်း၏ "အနှောင့်အယှက်" စာမျက်နှာမှ ဤအချက်များကိုရယူပါ
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

## သင်ယူမှု ယခုမှာ မရပ်ပါနဲ့၊ ခရီးကို ဆက်လက်လိုက်ပါ

ဤသင်ခန်းစာပြီးပါက [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကို စစ်ဆေးပြီး သင်၏ Generative AI သိမြင်မှုကို နောက်တန်းမြှင့်တင်ပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->