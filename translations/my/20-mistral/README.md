# Mistral မော်ဒယ်များဖြင့် ဆောက်လုပ်ခြင်း

## နိဒါန်း

ဒီသင်ခန်းစာမှာဖော်ပြပေးမယ့်အကြောင်းအရာတွေမှာပါဝင်သည်။
- မတူကွဲပြားသော Mistral မော်ဒယ်များကို စူးစမ်းလေ့လာခြင်း
- မော်ဒယ်တစ်ခုချင်းစီကို အသုံးပြုနိုင်သော အကွာအဝေးနှင့် ရှုထောင့်များကို နားလည်ခြင်း
- မော်ဒယ်တစ်ခုချင်းစီ၏ ထူးခြားသော လက္ခဏာများကို ဖော်ပြသည့် ကုဒ်နမူနာများကို စူးစမ်းလေ့လာခြင်း။

## Mistral မော်ဒယ်များ

ဒီသင်ခန်းစာမှာ Mistral မော်ဒယ် ၃ မျိုးကို စူးစမ်းလေ့လာမယ်။
**Mistral Large**, **Mistral Small** နှင့် **Mistral Nemo** တို့ဖြစ်သည်။

မော်ဒယ်များအားလုံးကို [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) တွင် အခမဲ့ ရနိုင်သည်။ ဒီ notebook ထဲက ကုဒ်တွေမှာ ဒီမော်ဒယ်များကို အသုံးပြုမှာဖြစ်တယ်။

> **မှတ်ချက်:** GitHub Models သည် ၂၀၂၆ ခုနှစ်ဇူလိုင်လကုန်တွင် ပိတ်သိမ်းသွားမည်ဖြစ်သည်။ [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ကို AI မော်ဒယ်များဖြင့် prototype ပြုလုပ်ရာတွင် သုံးစွဲနိုင်ခြင်းအကြောင်း အသေးစိတ် အချက်အလက်များကို ဒီမှာ လေ့လာပါ။


## Mistral Large 2 (2407)
Mistral Large 2 သည် လက်ရှိ Mistral ၏ ခေါင်းဆောင်မော်ဒယ် ဖြစ်ပြီး စက်မှုလုပ်ငန်းအသုံးပြုမှုအတွက် ဒီဇိုင်းထုတ်ထားသည်။

မော်ဒယ်သည် မူလ Mistral Large ကို အဆင့်မြှင့်တင်ပြီး
- ပိုမိုကြီးမားသော Context Window - 128k နှင့် 32k တို့၏ ကွာခြားချက်
- သင်္ချာနှင့် ကုတ်ရေးဆွဲခြင်း တာဝန်များတွင် ပိုမိုကောင်းမွန်သော ဆောင်ရွက်မှု - 76.9% ပျမ်းမျှတိကျမှု နှိုင်းယှဉ်၍ 60.4%
- ဘာသာစကားစုံတွင် ပိုမိုမြင့်မားသော အရည်အသွေး - အင်္ဂလိပ်၊ ပြင်သစ်၊ ဂျာမဏီ၊ စပိန်၊ အီတလီ၊ ပေါ်တူဂီ၊ ဒတ်ချ်၊ ရုရှား၊ တရုတ်၊ ဂျပန်၊ ကိုရီးယား၊ အာရပ် နှင့် ဟိန္ဒီတို့ပါဝင်သည်။

ဒီအင်္ဂါရပ်များနှင့်အတူ Mistral Large သည် ထူးချွန်သည်
- *Retrieval Augmented Generation (RAG)* - ပိုမိုကြီးမားသော context window ကြောင့်
- *Function Calling* - ဒီမော်ဒယ်မှာ native function calling ပါဝင်ပြီး အပြင်ကိရိယာများနှင့် API များနှင့် ပေါင်းစည်းမှုကို ခွင့်ပြုသည်။ ဒီ function call တွေကို တပြိုင်နက်မှာနှင့် တကြိမ်ပြီးနောက်တကြိမ် စဉ်လိုက် အမိန့်ပေးနိုင်သည်။
- *Code Generation* - ဒီမော်ဒယ်မှာ Python၊ Java၊ TypeScript နှင့် C++ ကုတ်ရေးဆွဲခြင်းတွင် ထူးချွန်သည်။

### Mistral Large 2 ကို အသုံးပြု၍ RAG ဥပမာ

ဒီဥပမာမှာ Mistral Large 2 ကို အသုံးပြုပြီး စာသားစာတမ်းတစ်ခုကို RAG ပုံစံဖြင့် လည်ပတ်ခွင့်ပြုသည်။ မေးခွန်းကို ကိုရီးယားဘာသာဖြင့်ရေးသားထားပြီး၊ ကောလိပ်ဝင်မတိုင်မီ ကော်ရေးသားသူ၏ လှုပ်ရှားမှုများအကြောင်း မေးမြန်းထားသည်။

စာသားစာတမ်းအကြောင်းအရာအတွက် နှင့် မေးခွန်းအတွက် Cohere Embeddings Model ကို အသုံးပြု၍ embedding များ ဖန်တီးသည်။ ဤနမူနာတွင် faiss Python package ကို ဗက်တာစတိုးအဖြစ် သုံးထားသည်။

Mistral မော်ဒယ်ထံသို့ ပေးပို့သော prompt တွင် မေးခွန်းများနှင့် မေးခွန်းနှင့်ဆွဲသက်သော အစိတ်အပိုင်းများကို ထည့်သွင်းထားသည်။ မော်ဒယ်သည် ထိုအချက်အလက်များအားလုံးကို အခြေခံ၍ သဘာဝဘာသာဖြင့် အဖြေပြန်ပေးသည်။

```python 
pip install faiss-cpu
```

```python 
import requests
import numpy as np
import faiss
import os

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import EmbeddingsClient

# မိမိ Microsoft Foundry ပရောဂျက်ရဲ့ "အနှစ်ချုပ်" စာမျက်နှာမှ ဒီတွေအကို ရယူပါ
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-large"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = requests.get('https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt')
text = response.text

chunk_size = 2048
chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
len(chunks)

embed_model_name = "cohere-embed-v3-multilingual" 

embed_client = EmbeddingsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token)
)

embed_response = embed_client.embed(
    input=chunks,
    model=embed_model_name
)



text_embeddings = []
for item in embed_response.data:
    length = len(item.embedding)
    text_embeddings.append(item.embedding)
text_embeddings = np.array(text_embeddings)


d = text_embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(text_embeddings)

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # အကွာအဝေး၊ အညွှန်းဝ်
retrieved_chunks = [chunks[i] for i in I.tolist()[0]]

prompt = f"""
Context information is below.
---------------------
{retrieved_chunks}
---------------------
Given the context information and not prior knowledge, answer the query.
Query: {question}
Answer:
"""


chat_response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content=prompt),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(chat_response.choices[0].message.content)
```

## Mistral Small
Mistral Small သည် Mistral မော်ဒယ် မျိုးစုတွင် premier/enterprise အမျိုးအစားအောက်ရှိ မော်ဒယ်တစ်ခုဖြစ်သည်။ အမည်မှ ပြောလိုသည့်အတိုင်း ဒီမော်ဒယ်သည် စကားအချို့အတွက် အသေးစား Language Model (SLM) ဖြစ်သည်။ Mistral Small ကို အသုံးပြုရာတွင် အကျိုးများမှာ -
- Mistral Large နှင့် NeMo ကဲ့သို့သော Mistral LLM များနှင့် နှိုင်းယှဉ်လျှင် အသုံးစရိတ် လျော့နည်းခြင်း - ၈၀% နှုန်းကျဆင်းမှု
- အချိန်နှောင့်နှေးမှုနည်း - Mistral ၏ LLM များထက် တုံ့ပြန်ချိန် ပိုမိုလျင်မြန်သည်
- ပိုမိုလိုအပ်သော အရင်းအမြစ်များကို သက်သက်အသက်သာစွာ အသုံးပြုနိုင်သော မျိုးစုံပတ်ဝန်းကျင်များတွင် တပ်ဆင်နိုင်မှု


Mistral Small သည် အထူးသင့်တော်သည် -
- အကျဉ်းချုပ်ခြင်း၊ စိတ်ခံစားချက်ခွဲခြမ်းစိတ်ဖြာခြင်းနှင့် ဘာသာပြန်ခြင်းကဲ့သို့သော စာသားအခြေပြု တာဝန်များ
- မကြာခဏ တောင်းဆိုမှုများဖြစ်ပေါ်သော အပလီကေးရှင်းများတွင် အသုံးတည့်မှုရှိမှုကြောင့်
- လျှပ်စစ်တုံ့ပြန်ချက် နည်းသော ကုတ် ပေးတွဲ ဆုတောင်းခြင်းနှင့် ကုတ်အကြံပြုခြင်း

## Mistral Small နှင့် Mistral Large နှိုင်းယှဉ်ခြင်း

Mistral Small နှင့် Large များ၏ တုံ့ပြန်ချိန် ကွာခြားချက် ဖော်ပြရန် အောက်ပါ ကုဒ်တစ်ချို့ကို ပြေးပါ။

တုံ့ပြန်ချိန် ကွာခြားသည့် ၃ မှ ၅ စက္ကန့်အကြား တွေ့ရမည်ဖြစ်သည်။ ထို့အပြင် တုံ့ပြန်မှုအရှည်အတောနှင့် စတိုင်ကိုလည်း တူညီသည့် prompt အတွက် ဆန်းစစ်ကြည့်ပါ။

```python 

import os 
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-small"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

```python 

import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-large"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

## Mistral NeMo

ဒီသင်ခန်းစာတွင် ဆွေးနွေးထားသည့် မော်ဒယ်နှစ်ခုနှင့် နှိုင်းယှဉ်လျှင် Mistral NeMo သည် Apache2 လိုင်စင်ဖြင့် ရရှိနိုင်သည့် သာမာန်အခမဲ့ မော်ဒယ်တစ်ခုဖြစ်သည်။

ယခင် Open Source LLM ဖြစ်သော Mistral 7B ထက် မြှင့်တင်ထားသည့် မော်ဒယ်တစ်ခုအဖြစ် လေ့လာကြည့်မည်ဖြစ်သည်။

NeMo မော်ဒယ်၏ အခြား ထူးခြားသည့် အင်္ဂါရပ်များမှာ -

- *ပိုမိုထိရောက်သော tokenization:* ထိုမော်ဒယ်သည် ပိုမိုရေပန်းစားသော tiktoken ခြား Mistral Large မှ Tekken tokenizer ကို အသုံးပြုသည်။ ထို့ကြောင့် သဘာဝဘာသာစကားများနှင့် ကုတ်များကျော်ပိုမိုပြည့်စုံသော ဆောင်ရွက်မှု ရရှိစေသည်။

- *Finetuning:* အခြေခံမော်ဒယ်သည် finetuning အတွက် ရရှိနိုင်ပါသည်။ finetuning လိုအပ်သော အသုံးပြုမှုအတွက် ပိုမိုပျမ်းမျှ စိတ်ကြိုက် အသုံးပြုနိုင်ချိန် ပေးသည်။

- *Native Function Calling* - Mistral Large ကဲ့သို့ ဤမော်ဒယ်ကို function calling အတွက် သင်ကြားပေးထားသည်။ ၎င်းဖြစ်မှုရှုထောင့်မှာ ပထမဆုံး Open Source မော်ဒယ်များထဲမှ တစ်ခုဖြစ်စေသည်။


### Tokenizer များကို နှိုင်းယှဉ်ခြင်း

ဤနမူနာတွင် Mistral NeMo သည် Mistral Large နှင့် tokenization ကို မည်သို့ ကိုင်တွယ်ရေးဆွဲသည်ကို ကြည့်မယ်။

နမူနာနှစ်ခုလုံးသည် တူညီသော prompt ကို ယူသော်လည်း NeMo မှ ထွက်ရှိသော tokens မှတ်ချက်ဧရိယာသည် Mistral Large ထက် နည်းပါးသည်ကို တွေ့ရလိမ့်မည်။

```bash
pip install mistral-common
```

```python 
# လိုအပ်သော package များကို အတင်သွင်းပါ။
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral tokenizer ကိုဖြင့်ပါ။

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# စာတိုများစာရင်းကို token များဖြင့်ခွဲပါ။
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the user's location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# token စာရင်းအရေအတွက်ကို ရေတွက်ပါ။
print(len(tokens))
```

```python
# လိုအပ်သော ပက်ကေ့ချ်မ်ားကို အင်ပွတ်လုပ်ပါ။
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral tokenizer ကို lload လုပ်ပါ။

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# စာတိုက်ပို့စာရင်းကို token သွင်းပါ။
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the user's location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# token များ၏ အရေအတွက်ကိုတွက်ပါ။
print(len(tokens))
```

## သင်ယူမှုသည် ဒီမှာ မရပ်ပါ၊ ခရီးပေါ် ဆက်လက်သွားပါ

ဒီသင်ခန်းစာကို ပြီးစီးပြီးနောက် ကျွန်ုပ်တို့ရဲ့ [Generative AI သင်ယူမှုစုဆောင်းမှုပေါင်း](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ပြီး သင်၏ Generative AI သိပ္ပံနှင့် သိမြင်မှုကို တိုးတက်စေလိုက်ပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->