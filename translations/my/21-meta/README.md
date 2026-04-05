# Meta မျိုးဆက် မော်ဒယ်များဖြင့် ဆောက်လုပ်ခြင်း

## မိတ်ဆက်

ဒီ သင်ခန်းစာတွင် ဖော်ပြပါအကြောင်းများ ပါဝင်မည်-

- Meta မျိုးဆက် မော်ဒယ် အဓိက နှစ်မျိုးဖြစ်သည့် Llama 3.1 နှင့် Llama 3.2 ကို ရှာဖွေတယ်
- မော်ဒယ်တိုင်း၏ သုံးစွဲမှုကိစ္စများနှင့် ရှုမြင်ချက်များကို နားလည်တယ်
- မော်ဒယ်တိုင်း၏ ထူးခြားသည့် အင်္ဂါရပ်များကို ဖော်ပြရန် ကုဒ်နမူနာ

## Meta မျိုးဆက် မော်ဒယ်များ

ဒီသင်ခန်းစာတွင် Meta မျိုးဆက် သို့မဟုတ် "Llama Herd" က မော်ဒယ်နှစ်မျိုးဖြစ်သည့် Llama 3.1 နှင့် Llama 3.2 ကို ရှာဖွေပါမည်။

ဒီ မော်ဒယ်များမှာ မတူကွဲပြားသောဗားရှင်းများဖြင့် ရရှိနိုင်ပြီး GitHub Model စျေးကွက်တွင် ရနိုင်ပါသည်။ AI မော်ဒယ်များဖြင့် [prototype ပြုလုပ်ခြင်းအတွက် GitHub မော်ဒယ်အသုံးပြုပုံ](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) ကို ပိုမိုသိရှိနိုင်ပါသည်။

မော်ဒယ်ဗားရှင်းများ-  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*မှတ်ချက်- Llama 3 ကိုလည်း GitHub Models တွင် ရနိုင်သော်လည်း ဒီသင်ခန်းစာတွင် မဖော်ပြသည့်အချက်*

## Llama 3.1

405 ဘီလီယံ ပါရာမီတာများနှင့်အတူ Llama 3.1 သည် ဖွင့်လှစ်မော်ဒယ် LLM အမျိုးအစားထဲတွင် ပါဝင်သည်။

ဒီ မော်ဒယ်သည် ယခင်ထွက်ရှိခဲ့သော Llama 3 ကို အဆင့်မြှင့်တင်ပြီး-

- ကြီးမားသော context ပြခန်း - 128k tokens နှင့် 8k tokens ကို ဆန့်ကျင်
- အများဆုံး ထွက်ရှိနိုင်သည့် Token အရေအတွက် - 4096 နှင့် 2048 ကို ဆန့်ကျင်
- ပလူရာဘာသာစကား ထောက်ပံ့မှုကောင်းမွန်ခြင်း - လေ့ကျင့်မှု token များ တိုးမြှင့်မှုကြောင့်

ဒီအင်္ဂါရပ်များက Llama 3.1 ကို GenAI အက်ပလီကေးရှင်းများ တည်ဆောက်ရာ၌ ပိုမိုရှုပ်ထွေးသော အသုံးပြုမှုများကို ကိုင်တွယ်နိုင်စေပါသည် -

- Native Function Calling - LLM workflow အပြင်ရှိ tools နှင့် function များကို ခေါ်ယူနိုင်ခြင်း
- RAG အကောင်အထည်ဖော်မှု ကောင်းမွန်ခြင်း - ကြီးမားသော context ပြခန်းကြောင့်
- Synthetic Data Generation - ဆင်တူ အချက်အလက်များ ဖန်တီးနိုင်ခြင်း (fine-tuning အတွက် အသုံးပြုနိုင်သည်)

### Native Function Calling

Llama 3.1 ကို function သို့မဟုတ် tool များ ခေါ်ယူရာတွင် ထိရောက်မှုရှိအောင် fine-tune လုပ်ထားသည်။ ထို့အပြင် မော်ဒယ်သည် အသုံးပြုသူထံမှ prompt အရ အသုံးပြုရန် လိုအပ်သော two built-in tool များကို မှတ်ထားနိုင်သည်။ 
ဒီ tools များမှာ-

- **Brave Search** - ဝက်ဘ်ရှာဖွေမှုဖြင့် ရာသီဥတုကဲ့သို့ ခေတ်မှီသည့် သတင်းအချက်အလက် ရယူနိုင်သည်
- **Wolfram Alpha** - ပိုရှုပ်ထွေးသော သင်္ချာတွက်ချက်မှုများအတွက် အသုံးပြုနိုင်သည်။ ကိုယ့် function ကို မရေးရ

သင့်ပိုင် custom tool များကို လည်း LLM သည် ခေါ်ယူနိုင်သည်။

အောက်ပါ ကုဒ်နမူနာတွင်-

- အောက်ပါ tools (brave_search, wolfram_alpha) ကို system prompt တွင် သတ်မှတ်ထားသည်။
- အသုံးပြုသူ၏ prompt မှာ မြို့တစ်မြို့၏ ရာသီဥတုအကြောင်း မေးမြန်းထားသည်။
- LLM သည် Brave Search tool ကို ခေါ်သည့် response များဖြင့် ပြန်ကြားမည်။ ဥပမာ `<|python_tag|>brave_search.call(query="Stockholm weather")` ဖြစ်သည်။

*မှတ်ချက်- ဤနမူနာသည် tool ခေါ်သုံးခြင်းမှသာ ဖြစ်ပြီး ရလဒ်ရရှိရန်အတွက် Brave API စာမျက်နှာတွင် အခမဲ့ အကောင့်ဖွင့်ပြီး function ကို သတ်မှတ်ရန် လိုအပ်ပါသည်။

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

LLM ဖြစ်သော်လည်း Llama 3.1 ၏ ကန့်သတ်ချက်တစ်ခုမှာ မူလ input အမျိုးအစား များကို မပေါင်းစပ်နိုင်ခြင်း ဖြစ်သည်။ ဥပမာ- ပုံများကို prompt အဖြစ် သုံးပြီး မျက်နှာစာ များကို တုံ့ပြန်ပေးရန် မလုပ်နိုင်ခြင်း ဖြစ်သည်။ 
Llama 3.2 ၏ ထူးခြားချက်တစ်ခုမှာ ဒီစွမ်းရည်ဖြစ်သည်။ ထို့အပြင် အောက်ပါ feature များပါရှိသည်-

- Multimodality - စာသား နှင့်ပုံရိပ် prompt နှစ်မျိုးစလုံးကို သုံးနိုင်ခြင်း
- သေးငယ်မှ အလတ်စားအရွယ်အစားမျိုးစုံ (11B နှင့် 90B) - တပ်ဆင်ရာတွင် စိတ်ကြိုက်ရွေးချယ်နိုင်
- စာသားချင်းသာဗားရှင်းများ (1B နှင့် 3B) - Edge သို့မဟုတ် မိုဘိုင်း စက်များတွင် တပ်ဆင်နိုင်ပြီး latency နည်းမည်

Multimodal ထောက်ပံ့မှုသည် ဖွင့်လှစ်မော်ဒယ်ကမာၻတွင် များထူးခြားသော တိုးတက်မှု ဖြစ်သည်။ အောက်ပါကုဒ်နမူနာတွင် Llama 3.2 90B မှ ပုံနှင့် စာသား prompt နှစ်မျိုးစလုံးကို အသုံးပြုပြီး ပုံကို သုံးသပ်မှုရယူမည်။

### Llama 3.2 နှင့် Multimodal ထောက်ပံ့မှု

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

## သင်ယူခြင်းကို ဒီမှာ မရပ်နားပါနဲ့၊ ခရီးကို ဆက်လက် သွားပါ

ဒီသင်ခန်းစာပြီးပါက [Generative AI စာသင်ခန်းစုစည်းမှု](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ရှု၍ သင့် Generative AI သိမြင်မှုကို ဆက်လက်မြှင့်တင်ပါ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ငြင်းဆိုချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားခြင်းဖြစ်ပါသည်။ တိကျမှုအတွက် ကြိုးပမ်းပေမယ့် အလိုအလျောက်ဘာသာပြန်ချက်များတွင် လွဲမှားမှုများ သို့မဟုတ် တိကျမှုနည်းပါးမှုများ ရှိနိုင်လေသည်ကို ကျေးဇူးပြု၍ သိရှိပါ။ မူရင်းစာတမ်းကို မိမိဘာသာဖြင့် ရှိသည့်အတိုင်း တရားဝင် အချက်အလက်အရင်းအမြစ်အဖြစ်ယူဆ သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် သေချာသော လူ့ဘာသာပြန် ဝန်ဆောင်မှုကို ဦးစားပေးအသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုမှုမှ ကြုံတွေ့လာနိုင်သည့် နားလည်မှုခွင့်မမှန်မှုများအတွက် ကျွန်ုပ်တို့၏ တာဝန်မရှိပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->