<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:04:49+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "my"
}
-->
# Mistral မော်ဒယ်များဖြင့် ဆောက်လုပ်ခြင်း

## နိဒါန်း

ဒီသင်ခန်းစာမှာ ဖော်ပြမယ့်အကြောင်းအရာများမှာ -  
- Mistral မော်ဒယ်အမျိုးအစားများကို ရှာဖွေခြင်း  
- မော်ဒယ်တိုင်းအတွက် အသုံးပြုမှုနှင့် အခြေအနေများကို နားလည်ခြင်း  
- မော်ဒယ်တိုင်းရဲ့ ထူးခြားချက်များကို ပြသသည့် ကုဒ်နမူနာများ  

## Mistral မော်ဒယ်များ

ဒီသင်ခန်းစာမှာ Mistral မော်ဒယ် ၃ မျိုးကို ရှာဖွေကြမယ် -  
**Mistral Large**, **Mistral Small** နဲ့ **Mistral Nemo**။

မော်ဒယ်တွေကို Github Model marketplace မှာ အခမဲ့ရနိုင်ပါတယ်။ ဒီ notebook ထဲက ကုဒ်တွေမှာ ဒီမော်ဒယ်တွေကို အသုံးပြုထားပါတယ်။ Github Models ကို [AI မော်ဒယ်တွေနဲ့ prototype ပြုလုပ်ခြင်း](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) အကြောင်း ပိုမိုသိရှိနိုင်ပါတယ်။

## Mistral Large 2 (2407)

Mistral Large 2 သည် Mistral ရဲ့ အဓိက flagship မော်ဒယ်ဖြစ်ပြီး စီးပွားရေးအသုံးပြုမှုအတွက် ဒီဇိုင်းထုတ်ထားသည်။

မူလ Mistral Large ကို အဆင့်မြှင့်တင်ထားပြီး  
- ပိုကြီးမားသော Context Window - 128k နှင့် 32k  
- သင်္ချာနှင့် ကုဒ်ရေးခြင်းလုပ်ငန်းများတွင် ပိုမိုကောင်းမွန်သော စွမ်းဆောင်ရည် - 76.9% ပျမ်းမျှတိကျမှု နှင့် 60.4%  
- ဘာသာစကားစုံလင်မှု တိုးတက်မှု - အင်္ဂလိပ်၊ ပြင်သစ်၊ ဂျာမန်၊ စပိန်၊ အီတလီ၊ ပေါ်တူဂီ၊ ဒတ်ချ်၊ ရုရှား၊ တရုတ်၊ ဂျပန်၊ ကိုရီးယား၊ အာရပ်၊ ဟိန္ဒီ စသည့် ဘာသာစကားများပါဝင်သည်။

ဒီအင်္ဂါရပ်များကြောင့် Mistral Large သည်  
- *Retrieval Augmented Generation (RAG)* - ပိုကြီးမားသော context window ကြောင့် ထူးခြားသည်  
- *Function Calling* - ဒီမော်ဒယ်မှာ native function calling ပါဝင်ပြီး အပြင်ကိရိယာများနှင့် API များနှင့် ပေါင်းစည်းနိုင်သည်။ အဲဒီ function call များကို တပြိုင်နက်တည်း သို့မဟုတ် တစ်ခုချင်းစီ အဆက်မပြတ် ချိတ်ဆက်နိုင်သည်။  
- *Code Generation* - Python, Java, TypeScript နဲ့ C++ ကုဒ်များ ဖန်တီးရာတွင် ထူးခြားသည်။

### Mistral Large 2 ဖြင့် RAG ဥပမာ

ဒီဥပမာမှာ Mistral Large 2 ကို အသုံးပြုပြီး စာရွက်စာတမ်းတစ်ခုအပေါ် RAG ပုံစံကို လည်ပတ်နေသည်။ မေးခွန်းကို ကိုရီးယားဘာသာဖြင့်ရေးထားပြီး စာရေးသူ၏ တက္ကသိုလ်မတက်ခင် လုပ်ဆောင်ချက်များကို မေးမြန်းထားသည်။

Cohere Embeddings Model ကို စာရွက်စာတမ်းနှင့် မေးခွန်း၏ embedding များ ဖန်တီးရန် အသုံးပြုသည်။ ဤနမူနာတွင် faiss Python package ကို vector store အဖြစ် အသုံးပြုထားသည်။

Mistral မော်ဒယ်ထံ ပို့သော prompt တွင် မေးခွန်းများနှင့် မေးခွန်းနှင့် ဆင်တူသော ရယူထားသော အပိုင်းများ ပါဝင်သည်။ မော်ဒယ်က သဘာဝဘာသာဖြင့် တုံ့ပြန်ချက် ပေးသည်။

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

Mistral Small သည် Mistral မော်ဒယ် မျိုးစုံအတွင်း premier/enterprise category အောက်ရှိ မော်ဒယ်တစ်ခုဖြစ်သည်။ အမည်အရ Mistral Small သည် Small Language Model (SLM) ဖြစ်သည်။ Mistral Small ကို အသုံးပြုခြင်း၏ အားသာချက်များမှာ -  
- Mistral Large နဲ့ NeMo ကဲ့သို့သော Mistral LLM များနှင့် နှိုင်းယှဉ်လျှင် စျေးနှုန်းသက်သာမှု - ၈၀% လျော့နည်းခြင်း  
- Latency နည်းခြင်း - Mistral LLM များထက် တုံ့ပြန်မှု မြန်ဆန်ခြင်း  
- ပိုမိုလွယ်ကူသော အသုံးပြုမှု - လိုအပ်သော အရင်းအမြစ်များအပေါ် ကန့်သတ်ချက်နည်းပြီး မတူညီသော ပတ်ဝန်းကျင်များတွင် တပ်ဆင်နိုင်ခြင်း  

Mistral Small သည် အထူးသင့်တော်သည် -  
- စာသားအခြေပြု လုပ်ငန်းများဖြစ်သော အကျဉ်းချုပ်ခြင်း၊ စိတ်ခံစားချက်ခွဲခြမ်းစိတ်ဖြာခြင်းနှင့် ဘာသာပြန်ခြင်း  
- စျေးနှုန်းသက်သာမှုကြောင့် မကြာခဏ တောင်းဆိုမှုများရှိသော အပလီကေးရှင်းများ  
- Latency နည်းသော ကုဒ်လုပ်ငန်းများဖြစ်သော ပြန်လည်သုံးသပ်ခြင်းနှင့် ကုဒ်အကြံပြုချက်များ  

## Mistral Small နှင့် Mistral Large နှိုင်းယှဉ်ခြင်း

Mistral Small နဲ့ Large တို့၏ latency ကွာခြားမှုကို ပြသရန် အောက်ပါ ကုဒ်များကို လည်ပတ်ပါ။

တုံ့ပြန်ချိန်ကွာခြားမှု ၃-၅ စက္ကန့်ရှိကြောင်း တွေ့ရမည်။ ထို့အပြင် တူညီသော prompt အပေါ် တုံ့ပြန်ချက်၏ အရှည်နှင့် စတိုင်ကိုလည်း သတိပြုပါ။

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

ဒီသင်ခန်းစာမှာ ဆွေးနွေးထားသော မော်ဒယ်နှစ်ခုနှင့် နှိုင်းယှဉ်လျှင် Mistral NeMo သည် Apache2 License ဖြင့် အခမဲ့ရရှိနိုင်သည့် တစ်ခုတည်းသော မော်ဒယ်ဖြစ်သည်။

Mistral ရဲ့ ယခင် open source LLM ဖြစ်သော Mistral 7B ကို အဆင့်မြှင့်တင်ထားသည့် မော်ဒယ်အဖြစ် တွေ့ရှိရသည်။

NeMo မော်ဒယ်၏ အခြားအင်္ဂါရပ်များမှာ -  

- *ပိုမိုထိရောက်သော tokenization:* ဒီမော်ဒယ်မှာ tiktoken ထက် ပိုမိုအသုံးများသော Tekken tokenizer ကို အသုံးပြုသည်။ ဒါကြောင့် ဘာသာစကားများနှင့် ကုဒ်များအပေါ် ပိုမိုကောင်းမွန်သော စွမ်းဆောင်ရည် ရရှိသည်။  

- *Finetuning:* အခြေခံမော်ဒယ်ကို finetuning အတွက် ရရှိနိုင်သည်။ ဒါက finetuning လိုအပ်သော အသုံးပြုမှုများအတွက် ပိုမိုလွယ်ကူမှု ပေးသည်။  

- *Native Function Calling* - Mistral Large ကဲ့သို့ ဒီမော်ဒယ်မှာ function calling အတွက် သင်ကြားပေးထားသည်။ ဒါကြောင့် ပထမဆုံး open source မော်ဒယ်များထဲမှ တစ်ခုအဖြစ် ထူးခြားသည်။  

### Tokenizer များနှိုင်းယှဉ်ခြင်း

ဒီနမူနာမှာ Mistral NeMo က tokenization ကို Mistral Large နှင့် နှိုင်းယှဉ်ကြည့်မယ်။

နမူနာနှစ်ခုလုံးမှာ တူညီသော prompt ကို အသုံးပြုသော်လည်း NeMo မှ token အရေအတွက်နည်းပြီး Mistral Large ထက် နည်းပါးသည်ကို တွေ့ရမည်။

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

## သင်ယူခြင်းသည် ဒီမှာ မရပ်နားပါ၊ ခရီးကို ဆက်လက်သွားပါ

ဒီသင်ခန်းစာပြီးဆုံးပြီးနောက် ကျွန်ုပ်တို့ရဲ့ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ရှု၍ သင်၏ Generative AI အသိပညာကို ပိုမိုမြှင့်တင်ပါ!

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။