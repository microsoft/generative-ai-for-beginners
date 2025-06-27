<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:24:00+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "my"
}
-->
# Mistral မော်ဒယ်များနှင့် တည်ဆောက်ခြင်း

## မိတ်ဆက်

ဒီသင်ခန်းစာမှာ အောက်ပါအကြောင်းအရာများကို လေ့လာပါမည်။
- မစ်စထရယ် မော်ဒယ်များကို ရှာဖွေခြင်း
- မော်ဒယ်တစ်ခုချင်းစီအတွက် အသုံးပြုမှုနှင့် ရှုခင်းများကို နားလည်ခြင်း
- မော်ဒယ်တစ်ခုချင်းစီ၏ ထူးခြားသော လုပ်ဆောင်ချက်များကို ပြသသည့် ကုဒ်နမူနာများ

## မစ်စထရယ် မော်ဒယ်များ

ဒီသင်ခန်းစာမှာ မစ်စထရယ် မော်ဒယ် ၃ မျိုးကို လေ့လာပါမည်။
**Mistral Large**, **Mistral Small** နှင့် **Mistral Nemo**.

ဒီမော်ဒယ်တွေကို Github Model marketplace မှာ အခမဲ့ ရနိုင်ပါတယ်။ ဒီ notebook ထဲမှာ ပါတဲ့ ကုဒ်တွေက ဒီမော်ဒယ်တွေကို အသုံးပြုပြီး ကုဒ်ကို အကောင်အထည်ဖော်မှာပါ။ Github Models ကို [AI မော်ဒယ်များဖြင့် နမူနာဖန်တီးခြင်း](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) အတွက် အသုံးပြုခြင်းဆိုင်ရာ အသေးစိတ်ကို ဤနေရာတွင် ကြည့်ပါ။

## Mistral Large 2 (2407)
Mistral Large 2 ဟာ လက်ရှိ Mistral ရဲ့ အထင်ကရ မော်ဒယ်ဖြစ်ပြီး စီးပွားရေးလုပ်ငန်းအတွက် ဒီဇိုင်းထုတ်ထားပါတယ်။

ဒီမော်ဒယ်ဟာ မူရင်း Mistral Large ကို အဆင့်မြှင့်တင်ခြင်းဖြစ်ပြီး
- ပိုကြီးတဲ့ Context Window - 128k vs 32k
- သင်္ချာနှင့် Coding Tasks တွေမှာ ပိုကောင်းတဲ့ စွမ်းဆောင်ရည် - 76.9% ပျမ်းမျှတိကျမှု vs 60.4%
- ဘာသာစကားစွမ်းဆောင်ရည်မြှင့်တင်မှု - ဘာသာစကားများမှာ: အင်္ဂလိပ်, ပြင်သစ်, ဂျာမန်, စပိန်, အီတလီ, ပေါ်တူဂီ, ဒတ်ချ်, ရုရှ, တရုတ်, ဂျပန်, ကိုးရီးယား, အာရဗီနှင့် ဟိန္ဒီ

ဒီလုပ်ဆောင်ချက်တွေနဲ့အတူ Mistral Large ဟာ အထူးပြောရမယ့်နေရာမှာ
- *Retrieval Augmented Generation (RAG)* - ပိုကြီးတဲ့ context window ရဲ့ကြောင့်
- *Function Calling* - ဒီမော်ဒယ်မှာ native function calling ရှိပြီး အပြင် Tools နှင့် APIs တွေကို ပေါင်းစည်းနိုင်ပါတယ်။ ဒီ call တွေကို ပရီးမီးလ်မော်ဒယ်တွေလို ထပ်တလဲလဲ သို့မဟုတ် တစ်ခုချင်းစီ ဆက်တိုက် လုပ်နိုင်ပါတယ်။
- *Code Generation* - Python, Java, TypeScript နှင့် C++ generation မှာ အထူးကောင်းပါတယ်။

### Mistral Large 2 ကို အသုံးပြုပြီး RAG နမူနာ

ဒီနမူနာမှာ Mistral Large 2 ကို အသုံးပြုပြီး စာတမ်းတစ်ခုကို RAG pattern ဖြင့် လုပ်ဆောင်မှာပါ။ မေးခွန်းကို ကိုးရီးယားဘာသာစကားဖြင့် ရေးထားပြီး ကောလိပ်မတက်ခင် အရေးအသားသူရဲ့ လုပ်ဆောင်ချက်များကို မေးထားပါတယ်။

Cohere Embeddings Model ကို အသုံးပြုပြီး စာတမ်းနှင့် မေးခွန်းကို embedding ဖန်တီးထားပါတယ်။ ဒီနမူနာအတွက် faiss Python package ကို vector store အဖြစ် အသုံးပြုထားပါတယ်။

Mistral မော်ဒယ်ကို ပေးပို့တဲ့ prompt ထဲမှာ မေးခွန်းတွေအပြင် မေးခွန်းနဲ့ ဆင်တူတဲ့ retrieved chunks တွေလည်း ပါပါတယ်။ မော်ဒယ်က နောက်ဆုံးတွင် သဘာဝဘာသာစကားဖြင့် ပြန်လည်ဖြေကြားပေးပါတယ်။

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

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

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

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?？"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # distance, index
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
Mistral Small ဟာ Mistral မော်ဒယ်များ၏ အခြားတစ်ခုဖြစ်ပြီး premier/enterprise အမျိုးအစားအောက်မှာ ပါဝင်ပါတယ်။ အမည်အတိုင်း ဒီမော်ဒယ်ဟာ Small Language Model (SLM) ဖြစ်ပါတယ်။ Mistral Small ကို အသုံးပြုခြင်းရဲ့ အကျိုးကျေးဇူးများက:
- Mistral LLMs များဖြစ်သော Mistral Large နှင့် NeMo တွေနဲ့ နှိုင်းယှဉ်ပါက ကုန်ကျစရိတ် လျော့နည်းခြင်း - 80% စျေးလျော့
- ကြိမ်နှုန်းနည်းခြင်း - Mistral LLMs တွေနဲ့ နှိုင်းယှဉ်ပါက ပိုမြန်သော တုံ့ပြန်မှု
- လွယ်ကူခြင်း - လိုအပ်သော အရင်းအမြစ်များအပေါ် ကန့်သတ်ချက်နည်းသည့် ကွဲပြားခြားနားသော ပတ်ဝန်းကျင်များတွင် ဖြန့်ဝေနိုင်ခြင်း

Mistral Small ဟာ အထူးပြောရမယ့်နေရာမှာ:
- စာသားအခြေခံ လုပ်ငန်းများဖြစ်သော အကျဉ်းချုပ်ရေးခြင်း, ခံစားမှု ခွဲခြားခြင်းနှင့် ဘာသာပြန်ခြင်း
- ကုန်ကျစရိတ်ထိရောက်မှုကြောင့် မကြိမ်ကြိမ် တောင်းဆိုမှုများရှိသော အက်ပလီကေးရှင်းများ
- ကြိမ်နှုန်းနည်းသော ကုဒ်လုပ်ငန်းများဖြစ်သော ပြန်လည်သုံးသပ်ခြင်းနှင့် ကုဒ်အကြံပြုချက်များ

## Mistral Small နှင့် Mistral Large ကို နှိုင်းယှဉ်ခြင်း

Mistral Small နှင့် Large အကြား ကြိမ်နှုန်းကွာခြားချက်ကို ပြသရန် အောက်ပါ cells တွေကို run လုပ်ပါ။

တုံ့ပြန်မှုအချိန်ကွာခြားချက် 3-5 စက္ကန့်အတွင်း တွေ့ရလိမ့်မည်။ တစ်ချိန်တည်းမှာ တုံ့ပြန်မှု အရှည်နှင့် စတိုင်ကိုလည်း မှတ်ပါ။

```python 

import os 
endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-small"
token = os.environ["GITHUB_TOKEN"]

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

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

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

ဒီသင်ခန်းစာမှာ ဆွေးနွေးထားတဲ့ အခြားမော်ဒယ် ၂ ခုနှင့် နှိုင်းယှဉ်ပါက Mistral NeMo ဟာ Apache2 License နဲ့ အခမဲ့ရရှိနိုင်တဲ့ တစ်ခုတည်းသော မော်ဒယ်ဖြစ်ပါတယ်။

ဒါဟာ မစ်စထရယ်ရဲ့ အရင်က သုံးထားတဲ့ open source LLM ဖြစ်တဲ့ Mistral 7B ကို အဆင့်မြှင့်တင်ထားတာဖြစ်ပါတယ်။

NeMo မော်ဒယ်ရဲ့ အခြားလုပ်ဆောင်ချက်များမှာ:

- *ပိုထိရောက်တဲ့ tokenization:* ဒီမော်ဒယ်ဟာ Tekken tokenizer ကို အသုံးပြုပြီး လူသုံးများတဲ့ tiktoken ကို အစားထိုးထားပါတယ်။ ဒါက ပိုများတဲ့ ဘာသာစကားများနှင့် ကုဒ်များအပေါ် ပိုကောင်းတဲ့ စွမ်းဆောင်ရည်ကို ပေးနိုင်ပါတယ်။

- *Finetuning:* အခြေခံမော်ဒယ်ကို finetuning အတွက် ရရှိနိုင်ပါတယ်။ ဒါဟာ finetuning လိုအပ်နိုင်တဲ့ အသုံးပြုမှုများအတွက် ပိုလွယ်ကူမှုကို ပေးနိုင်ပါတယ်။

- *Native Function Calling* - Mistral Large လိုပါပဲ ဒီမော်ဒယ်ဟာ function calling အပေါ် လေ့ကျင့်ထားပါတယ်။ ဒါက open source မော်ဒယ်များထဲမှာ ပထမဆုံးသော မော်ဒယ်တစ်ခုအဖြစ် ထူးခြားပါတယ်။

### Tokenizers များကို နှိုင်းယှဉ်ခြင်း

ဒီနမူနာမှာ Mistral NeMo က Mistral Large နှင့် နှိုင်းယှဉ်ပြီး tokenization ကို ဘယ်လို လုပ်ဆောင်သလဲဆိုတာကို ကြည့်ပါမည်။

နမူနာနှစ်ခုလုံးမှာ တူညီတဲ့ prompt ကို ယူထားပေမယ့် NeMo က Mistral Large ထက် tokens နည်းနည်းနဲ့ ပြန်ပေးထားတာကို တွေ့ရပါမည်။

```bash
pip install mistral-common
```

```python 
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "open-mistral-nemo	"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
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
                                "description": "The temperature unit to use. Infer this from the users location.",
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

# Count the number of tokens
print(len(tokens))
```

```python
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
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
                                "description": "The temperature unit to use. Infer this from the users location.",
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

# Count the number of tokens
print(len(tokens))
```

## သင်ယူမှုဟာ ဒီမှာ မသိမ်းဆည်းပါ၊ ခရီးကို ဆက်လက်ဖြတ်သန်းပါ

ဒီသင်ခန်းစာပြီးဆုံးပြီးနောက် [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကိုကြည့်ပါ။ Generative AI သတင်းအချက်အလက်ကို ဆက်လက် မြှင့်တင်ပါ!

**ဖြေရှင်းချက်**:
ဒီစာရွက်ကို AI ဘာသာပြန်စနစ် [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြုပြီး ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို ကျေးဇူးပြု၍ သတိပြုပါ။ မူရင်းစာရွက်ကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာသော နားလည်မှုမှားများ သို့မဟုတ် မှားဖွယ်ကိစ္စများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မရှိပါ။