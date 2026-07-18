# Mistral မော်ဒယ်များဖြင့် တည်ဆောက်ခြင်း 

## နိဒါန်း 

ဒီသင်ခန်းစာတွင်ဖော်ပြပါ့မည်မှာ- 
- Mistral မော်ဒယ်အမျိုးအစားများကို ရှာဖွေခြင်း 
- မော်ဒယ်တိုင်းအတွက် အသုံးပြုမှုနှင့် ရှုထောင့်များကို နားလည်ခြင်း 
- မော်ဒယ်တိုင်း၏ ထူးခြားတဲ့ လက္ခဏာများကို ဖော်ပြသည့် ကုဒ်နမူနာများကို ရှာဖွေခြင်း။ 

## Mistral မော်ဒယ်များ 

ဒီသင်ခန်းစာမှာ Mistral မော်ဒယ် ၃ မျိုးကို ရှာဖွေရန်ဖြစ်ပါသည်- 
**Mistral Large**, **Mistral Small** နှင့် **Mistral Nemo**။ 

မော်ဒယ်များအားလုံးကို [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) တွင်အခမဲ့ရရှိနိုင်ပါသည်။ ဒီ notebook မှာ မော်ဒယ်တွေကို အသုံးပြုပြီး ကုဒ်များကို ပြေးခြင်းအတွက် အသုံးပြုမှာဖြစ်သည်။ 

> **မှတ်ချက်။** GitHub မော်ဒယ်များကို ၂၀၂၆ ခုနှစ် ဇူလိုင်လကုန်တွင် ရပ်ဆိုင်းနေပါပြီ။ [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ရဲ့အသုံးပြုနည်းတွေနဲ့ AI မော်ဒယ်များကို prototype လုပ်နိုင်ရေး နောက်ထပ်အသေးစိတ်ကို ဒီမှာ ကြည့်ရှုနိုင်ပါသည်။ 


## Mistral Large 2 (2407)
Mistral Large 2 သည် လက်ရှိ Mistral ၏အဓိကမော်ဒယ်ဖြစ်ပြီး စီးပွားရေးအသုံးပြုမှုအတွက်ဒီဇိုင်းရေးဆွဲထားသည်။ 

မော်ဒယ်တွင် Mistral Large မူလမော်ဒယ်၏တိုးတက်မှုများမှာ- 
-  ကြီးမားသော Context Window - 128k နှင့် 32k 
-  သင်္ချာနှင့် ကုဒ်ရေးခြင်း လုပ်ငန်းများတွင် ပိုမိုကောင်းမွန်သော စွမ်းဆောင်ရည် - 76.9% စံချိန်တိကျမှုနှင့် 60.4% 
-  ဘာသာစကားစုံ ကျွမ်းကျင်မှု တိုးတက်ခြင်း - အင်္ဂလိပ်၊ ပြင်သစ်၊ ဂျာမနီ၊ စပိန်၊ အီတလီ၊ ပေါ်တူဂီ၊ ဒတ်ချ်၊ ရုရှား၊ တရုတ်၊ ဂျပန်၊ ကိုရီးယား၊ အာရဗီနှင့် ဟိန္ဒီတို့ပါဝင်သည်။ 

ဒီထူးခြားချက်များကြောင့် Mistral Large သည်အောက်ပါအရာများတွင် ထူးချွန်ပါသည်- 
- *Retrieval Augmented Generation (RAG)* - ကြီးမားသော context window ရှိသောကြောင့် 
- *Function Calling* - ဒီမော်ဒယ်တွင် function calling မူရင်းပုံစံပါရှိပြီး ပြင်ပ tools နှင့် APIs တို့နှင့် ပေါင်းစည်းသုံးစွဲနိုင်သည်။ ခေါ်ဆိုမှုများကို တပြိုင်နက်၊ သို့မဟုတ် ဆက်တိုက်အလိုက်လည်းလုပ်နိုင်သည်။ 
- *ကုဒ်ဖန်တီးခြင်း* - Python, Java, TypeScript နှင့် C++ စနစ်များတွင် ထူးခြားသော စွမ်းဆောင်ရည်ရှိသည်။ 

### Mistral Large 2 ကို အသုံးပြုပြီး RAG ဥပမာ 

ဒီဥပမာတွင် Mistral Large 2 ကို အသုံးပြုပြီး စာတမ်းတစ်စောင်မှာ RAG ပုံစံဖြင့် ဆောင်ရွက်နေသည်။ မေးခွန်းသည် ကိုရီးယားဘာသာဖြင့်ရေးဆွဲပြီး အဖွဲ့ဝင်တက်သင်ခန်းမမတိုင်မီ၊ သူ၏ လုပ်ငန်းများကို မေးမြန်းထားသည်။ 

Cohere Embeddings Model ကို သုံးပြီး စာတမ်းနှင့် မေးခွန်းတို့၏ embeddings များ ဖန်တီးသည်။ ဤနမူနာတွင် faiss Python package ကို vector store အဖြစ် သုံးထားသည်။ 

Mistral မော်ဒယ်ထံ ကျွေးပေးသော prompt တွင် မေးခွန်းနှင့် မေးခွန်းနှင့်ဆင်တူသော chunk များပါဝင်ပြီး မော်ဒယ်သည် သဘာဝဘာသာဖြင့် ဖြေကြားချက်ပေးသည်။ 

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

# သင်၏ Microsoft Foundry ပရောဂျက်၏ "အကျဉ်းချုပ်" စာမျက်နှာမှ ဒီတွေကို ရယူပါ
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # အကွာအဝေး၊ အညွှန်းနံပါတ်
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
Mistral Small သည် Mistral မော်ဒယ်မျိုးများအတွင်း premier/enterprise အမျိုးအစားအောက်တွင် တစ်ခုတည်းသော မော်ဒယ်ဖြစ်ပြီး၊ အမည်အရ Small Language Model (SLM) ဖြစ်သည်။ Mistral Small ကိုအသုံးပြုရာတွင် အားသာချက်များမှာ- 
- Mistral Large နှင့် NeMo ကဲ့သို့ Mistral LLM များနှင့် နှိုင်းယှဉ်လျှင် ကုန်ကျစရိတ်သက်သာခြင်း - ၈ဝ% စျေးနှုန်းကျဆင်းခြင်း 
- Latency နည်းခြင်း - Mistral LLM များနှင့်နှိုင်းလျှင် အမြန်ပြန်လည်ဖြေကြားမှု 
- ပြောင်းလဲနိုင်မှုများရှိခြင်း - မတူညီသောပတ်ဝန်းကျင်များတွင် လိုအပ်သော အရင်းအမြစ်များကနည်း၍ ဖြန့်ဖြူးနိုင်ခြင်း 


Mistral Small ကို အထူးသင့်တော်မည့် အခန်းကဏ္ဍများမှာ- 
- စာသားအခြေခံ အလုပ်များ ဖြစ်သော အနှစ်ချုပ်၊ စိတ်ခံစားမှုခွဲခြမ်းသုံ၊ ဘာသာပြန်ခြင်း စသည်တို့ 
- မကြာခဏ တောင်းဆိုမှုများရှိသည့် လျှော့စျေးသက်သာသော လျှောက်လွှာများ 
- latency နည်းသော ကုဒ်လုပ်ငန်းများ ဖြစ်သော စစ်ဆေးခြင်းနှင့် ကုဒ်အကြံပြုချက်များ 

## Mistral Small နှင့် Mistral Large ကို နှိုင်းယှဉ်ခြင်း 

Mistral Small နှင့် Large ၏ latency ကွာခြားမှုကို ပြသရန် အောက်ပါ ဆဲလ်များကို ပြေးပါ။ 

တုံ့ပြန်ချိန်များတွင် ၃-၅ စက္ကန့်ကွာခြားမှုကို တွေ့မြင်ရမည်ဖြစ်သည်။ ထို့အပြင် တူညီသော prompt ထဲတွင် သုံးစကားနှင့် အမျိုးအစားကိုလည်း မှတ်သားပါ။  

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

ဒီသင်ခန်းစာတွင် ဆွေးနွေးခဲ့သည့် အခြားမော်ဒယ် နှစ်ခုနှင့် နှိုင်းယှဉ်လျှင် Mistral NeMo သည် Apache2 လိုင်စင် ဖြင့် ရရှိနိုင်သည့် တစ်ခုတည်းသောအခမဲ့မော်ဒယ်ဖြစ်သည်။ 

Mistral ၏ ရှေးကာလ open source LLM ဖြစ်သည့် Mistral 7B ကိုတိုးတက်အဆင့်မြှင့်ထားသော မော်ဒယ်အဖြစ် ကြည့်မြင်သည်။ 

NeMo မော်ဒယ်၏ အခြားသော လက္ခဏာများမှာ- 

- *ပိုမိုထိရောက်သော tokenization:* ဒီမော်ဒယ်သည် ပိုပြီး အသုံးများသော tiktoken ၏အစား Tekken tokenizer ကို သုံးသည်။ ဒါကြောင့် ဘာသာစကားများစွာနှင့် ကုဒ်များ၌ ပိုမိုကောင်းမွန်သော စွမ်းဆောင်ရည်ရရှိသည်။ 

- *Finetuning:* အခြေခံမော်ဒယ်ကို finetuning ပြုလုပ်ရန်ရရှိနိုင်သည်။ ဒါက finetuning လိုအပ်သော အသုံးပြုမှုများအတွက် ပိုမိုလွယ်ကူသော လုပ်ငန်းစဉ်ကို ပေးနိုင်သည်။ 

- *Native Function Calling* - Mistral Large ကဲ့သို့ ဒီမော်ဒယ်ကို function calling အတွက်လေ့ကျင့်ထားပြီး သွယ်ဝိုက်မှုကို ရရှိထားသည်။ ဒီလိုဖြစ်မှုကြောင့် ဒါဟာ ပထမဆုံး open source မော်ဒယ်များထဲမှ တစ်ခုအနေနဲ့ ထူးခြားချက်ရှိသည်။ 


### Tokenizer များကို နှိုင်းယှဉ်ခြင်း 

ဒီနမူနာတွင် Mistral NeMo သည် Mistral Large နှင့် tokenization ကို မည်သို့ xử lýကြောင်း ကြည့်ရှုမည်။ 

နှစ်ခုစလုံးမှာ တူညီသော prompt ကို အသုံးပြုသည်၊ သို့သော် NeMo သည် Mistral Large ထက် token စနစ်နည်းနည်းသာ ပြန်လည်ပေးသည့်အချက်ကို တွေ့မြင်ရမည်။ 

```bash
pip install mistral-common
```

```python 
# လိုအပ်သော ပက်ကေ့ဂျ်များကို သွင်းယူပါ။
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral tokenizer ကို ဖတ်ယူပါ။

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# မက်ဆေ့ချ်များစာရင်းကို token များသို့ ခွဲထုတ်ပါ။
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

# token အရေအတွက်ကို မှန်ချက်ပါ။
print(len(tokens))
```

```python
# လိုအပ်သော package များကိုသွင်းယူပါ။
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral tokenizer ကို load လုပ်ပါ

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# သတင်းစာစာရင်းကို token ပြုလုပ်ပါ
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

# token များ၏ အရေအတွက်ကိုရေတွက်ပါ
print(len(tokens))
```

## သင်ယူခြင်းသည် ဒီနေရာမှာ မသိပ်တော့ပဲ များသားစွမ်းဆောင်ပါ 

ဒီသင်ခန်းစာပြီးချိန်နောက်ပိုင်း [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကိုကြည့်ရှု၍ သင်၏ Generative AI အသိပညာအဆင့်မြှင့်တင်မှုကို ဆက်လက်တိုးတက်အောင်လုပ်ပါ! 

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->