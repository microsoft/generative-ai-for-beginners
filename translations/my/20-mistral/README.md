# Mistral မော်ဒယ်များဖြင့် ဆောက်ခြင်း

## နိဒါန်း

ဤသင်ခန်းစာတွင် ဖော်ပြမည့်အကြောင်းအရာများမှာ-
- Mistral မော်ဒယ်များအမျိုးမျိုးကို စူးစမ်းလေ့လာခြင်း
- မော်ဒယ်တိုင်း၏ အသုံးချမှုများနှင့် ဖြစ်ပေါ်နိုင်သော အခြေအနေများကို နားလည်ခြင်း
- မော်ဒယ်တိုင်း၏ ထူးခြားချက်များကို ပြသထားသည့် ကုဒ်နမူနာများကို စူးစမ်းလေ့လာခြင်း ဖြစ်သည်။

## Mistral မော်ဒယ်များ

ဤသင်ခန်းစာတွင် Mistral မော်ဒယ် ၃ မျိုးကို စူးစမ်းလေ့လာမည်။
**Mistral Large**, **Mistral Small** နှင့် **Mistral Nemo** ဖြစ်ပါသည်။

မော်ဒယ်တိုင်းသည် GitHub Model စျေးကွက်တွင် အခမဲ့ရရှိနိုင်သည်။ ဤ notebook တွင် သုံးသောကုဒ်များမှာ မော်ဒယ်များကို အသုံးပြု၍ ကိုယ့်ရဲ့ကုဒ်များကို လည်ပတ်စေသည်။ GitHub Models သုံး၍ [AI မော်ဒယ်များဖြင့် prototype ပြုလုပ်ခြင်း](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) သတင်းအချက်အလက်ပိုများကို ဒီမှာ ဖတ်နိုင်ပါသည်။

## Mistral Large 2 (2407)

Mistral Large 2 သည် ယခုအချိန်တွင် Mistral ၏ ဦးဆောင်မော်ဒယ်ဖြစ်ပြီး စီးပွားရေးအသုံးပြုမှုအတွက် တီထွင်ထားသည်။

ဤမော်ဒယ်သည် မူလ Mistral Large ကို အဆင့်မြှင့်တင်ထားပြီး-
- မြင့်မားသော Context Window - 128k နှင့် 32k
- သင်္ချာနှင့် ကုဒ်ရေးဆွဲရေး လုပ်ငန်းစဉ်များတွင် ပိုမိုကောင်းမွန်သော အောင်မြင်မှု - 76.9% ပျမ်းမျှတိကျမှုနှင့် 60.4%
- ဘာသာစကားများအတွက် ပိုမိုကောင်းမွန်သောစွမ်းဆောင်ရည် - အင်္ဂလိပ်၊ ပြင်သစ်၊ ဂျာမန်၊ စပါိန်၊ အီတလီ၊ ပေါ်တူဂီ၊ ဒတ်ချ်၊ ရုရှား၊ တရုတ်၊ ဂျပန်၊ ကိုရီးယား၊ အာရဘီ နှင့် ဟိန္ဒီတို့ ပါဝင်သည်။

ဤအင်္ဂါရပ်များဖြင့် Mistral Large သည်-
- *Retrieval Augmented Generation (RAG)* - ကြီးမားသော context window ကြောင့် ထူးခြားသည်။
- *Function Calling* - ဤမော်ဒယ်တွင် function calling ကိုဇာတိရှိပြီး အပြင် tools နှင့် API များနှင့် ထည့်သွင်းအသုံးပြုနိုင်သည်။ ၎င်း function call များကို 병렬သို့မဟုတ် တန်းစီစွာ ခလုတ်တိုက်ခိုက်နိုင်သည်။
- *Code Generation* - Python, Java, TypeScript နှင့် C++ စသည်ဖြင့် ကုဒ်ဖန်တီးရာတွင် ထူးခြားသည်။

### Mistral Large 2 ဖြင့် RAG ဥပမာ

ဤဥပမာတွင် Mistral Large 2 ကို အသုံးပြု၍ စာသားစာတမ်းတစ်ခုအပေါ် RAG ပုံစံကို ပြုလုပ်ပါသည်။ မေးခွန်းကို ကိုရီးယားဘာသာဖြင့်ရေးထားပြီး ယူနီဗာစတီဝင်မတိုင်မီ စာရေးသူ၏ လုပ်ဆောင်ချက်များအကြောင်း ဆွေးနွေးထားသည်။

စာသားစာတမ်းနှင့် မေးခွန်းတို့၏ embedding များကို ဖန်တီးရန် Cohere Embeddings Model ကို အသုံးပြုသည်။ ဤနမူနာတွင် faiss Python package ကို vector store အဖြစ် အသုံးပြုသည်။

Mistral မော်ဒယ်သို့ ပို့သော prompt တွင် မေးခွန်းများနှင့် မေးခွန်းနှင့် အလားတူသော ရယူထားသော chunks များပါဝင်သည်။ မော်ဒယ်က ထို့နောက် သဘာဝဘာသာဖြင့်အဖြေ ပေးသည်။

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

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # အကွာအဝေး၊ အညွှန်း
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

Mistral Small သည် Mistral မော်ဒယ် များအတွင်း premier/enterprise အမျိုးအစား၏ နောက်တစ်ခုဖြစ်သည်။ အမည်အရ၊ ဤမော်ဒယ်မှာ Small Language Model (SLM) ဖြစ်သည်။ Mistral Small ကို အသုံးပြုခြင်း၏ အားသာချက်များမှာ-
- Mistral Large နှင့် NeMo ကဲ့သို့သော Mistral LLM များနှင့် နှိုင်းယှဉ်နိုင်သော စျေးနှုန်းသက်သာမှု - ၈၀% စျေးလျော့
- Latency နည်း - Mistral LLM များထက် မြန်ဆန်သော တုံ့ပြန်မှု
- တတ်နိုင်သမျှ စူးစမ်းနိုင်မှု - လိုအပ်သည့် အရင်းအမြစ်များကို ပိုမိုလျော့နည်းစေပြီး မတူညီသော ပတ်ဝန်းကျင်များတွင် တပ်ဆင်နိုင်သည်။

Mistral Small သည်-
- စာသားအခြေပြု လုပ်ငန်းများ (အကျဉ်းချုပ်၊ စိတ်ထားခွဲခြမ်းစိတ်ဖြာခြင်း နှင့် ဘာသာပြန်ခြင်း) အတွက် အထူးသင့်တော်သည်။
- အလွယ်တကူ တုံ့ပြန်ရမည့် လျှောက်လွှာများအတွက် အသုံးချဖို့ သက်သာသော ဈေးနှုန်းကြောင့် ကောင်းမွန်သည်။
- Latency နည်းသော ကုဒ်လုပ်ငန်းများ (ပြုပြင်မှုနှင့် ကုဒ် အကြံပြုခြင်း) အတွက် သင့်တော်သည်။

## Mistral Small နှင့် Mistral Large နှိုင်းယှဉ်ခြင်း

Mistral Small နှင့် Large တို့သည် တုံ့ပြန်မှုအချိန်မှာ ကွာခြားမှုရှိကြောင်းပြသရန်အတွက် အောက်ပါကြဲပြားချက်များကို အကောင်အထည်ဖော်ပါ။

တုံ့ပြန်ချိန်မှာ ၃ မှ ၅ စက္ကန့်ကွာခြားမှုကို ကြည့်နိုင်မည်ဖြစ်သည်။ ထို့ပြင် တုံ့ပြန်မှု၏ အရှည်နှင့်စတိုင်ကိုလည်း တူညီသော prompt ပေါ်တွင် မှတ်သားကြည့်ပါ။

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

ဤသင်ခန်းစာ၌ ပြောသော မော်ဒယ်နှစ်ခုနှင့် နှိုင်းယှဉ်ပါက Mistral NeMo သည် Apache2 လိုင်စင်ဖြင့် ရရှိနိုင်သည့် တစ်ခုတည်းသော အခမဲ့မော်ဒယ်ဖြစ်သည်။

ဤသည်သည် Mistral 7B မှာရှိသည့် ရင်းမြစ်ဖွင့် LLM အား အဆင့်မြှင့်တင်ထားသည်ဟု ဖော်ပြသည်။

NeMo မော်ဒယ်၏ အခြားထူးခြားချက်များမှာ -

- *ပိုမိုထိရောက်သော tokenization* - ဤမော်ဒယ်သည် ပိုမိုအသုံးပြုကြသော tiktoken ထက် Tekken tokenizer ကို အသုံးပြုသည်။ ဤကိစ္စက ဘာသာစကားများနှင့် ကုဒ်အမျိုးမျိုးတွင် ပိုမိုကောင်းမွန်သော စွမ်းဆောင်ရည် ရရှိစေသည်။

- *Finetuning* - အခြေခံမော်ဒယ်ကို finetuning အတွက် ရနိုင်သည်။ ဤနေရာက finetuning လိုအပ်ချက်ရှိသော အသုံးပြုမှုအတွက် ပိုမိုလွယ်ကူသော မော်ဒယ် ဖြစ်စေသည်။

- *Native Function Calling* - Mistral Large ကဲ့သို့ ဤမော်ဒယ်တွင် function calling သင်ကြားပေးထားသည်။ ၎င်းသည် အများဆုံး ရင်းမြစ်ဖွင့်မော်ဒယ်များထဲမှ ပထမဆုံးဖြစ်စဉ်တစ်ခုအနေဖြင့် ထူးခြားသော မော်ဒယ်တစ်ခု ဖြစ်စေသည်။

### Tokenizers နှိုင်းယှဉ်ခြင်း

ဤနမူနာတွင် Mistral NeMo က Mistral Large နှင့် နှိုင်းယှဉ်၍ tokenization ကို မည်သို့ ကိုင်တွယ်သည်ကို ကြည့်မည်။

နမူနာနှစ်ခုသည် တူညီသော prompt ကို ယူထားပြီး NeMo သည် Mistral Large ထက် token ပမာဏနည်းကြောင်း တွေ့ရမည်။

```bash
pip install mistral-common
```

```python 
# လိုအပ်သော package များတင်သွင်းပါ:
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

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# စာတိုများစာရင်းကို token များဖြင့်ခွဲပါ
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

# token အရေအတွက်ကိုတွက်ပါ
print(len(tokens))
```

```python
# လိုအပ်သော package များကို Import လုပ်ပါ။
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral tokenizer ကို Load လုပ်ပါ။

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# စာတိုများစာရင်းကို Tokenize လုပ်ပါ။
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

# token အရေအတွက်ကိုတွက်ပါ။
print(len(tokens))
```

## သင်ယူမှုသည် ဤနေရာတွင် မရပ်တန့်ပေ၊ ခရီးဆက်မည်

ဤသင်ခန်းစာပြီးစီးပြီးနောက်၊ [Generative AI သင်ယူမှု စုစည်းမှု](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ရှု၍ သင်၏ Generative AI အသိပညာအား ဆက်လက်တိုးမြှင့်ပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ဂရုပြုချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှုဖြစ်သော [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် မှန်ကန်မှုကို ကြိုးပမ်းထားပေမယ့် စက်ဘားသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါ။ မူရင်းစာတမ်းကို သဘာဝဘာသာဖြင့်သာ အတည်ပြုရင်းအရင်းအမြစ်အဖြစ် သတ်မှတ်ရန် လိုအပ်ပါသည်။ အရေးကြီးသောအချက်အလက်များအတွက် လုပ်ငန်းအတတ်ပညာရှင်များ၏ လူ့ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုမှုကြောင့်ဖြစ်ပေါ်လာသော နားလည်မှုမှားယွင်းမှုများ သို့မဟုတ် အဓိပ္ပါယ်ဖယောင်းဖျောမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->