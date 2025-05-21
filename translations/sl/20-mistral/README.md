<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T11:04:13+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "sl"
}
-->
# Mistral මොඩල් සමඟ ගොඩනැගීම

## හැඳින්වීම

මෙම පාඩම ආවරණය කරනුයේ:
- විවිධ Mistral මොඩල් පරීක්ෂා කිරීම
- සෑම මොඩලයකටම ඇති භාවිතා කේස් සහ සිද්ධි අවබෝධය
- සෑම මොඩලයකම විශේෂාංග විශේෂිත කේත උදාහරණ

## Mistral මොඩල්

මෙම පාඩම තුළ අපි විවිධ Mistral මොඩල් 3ක් පරීක්ෂා කරමු: **Mistral Large**, **Mistral Small** සහ **Mistral Nemo**.

මෙම මොඩල් සියල්ල GitHub Model වෙළඳපොළේ නොමිලේ ලබා ගත හැක. මෙම සටහනේ කේතය මෙම මොඩල් භාවිතා කරමින් කේතය ක්‍රියාත්මක කරයි. [AI මොඩල් සමඟ ආදර්ශ නිරමාණය කිරීම](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) සඳහා Github Models භාවිතා කිරීම පිළිබඳ වැඩි විස්තර මෙන්න.

## Mistral Large 2 (2407)

Mistral Large 2 ව්‍යාපාරික භාවිතය සඳහා නිර්මාණය කර ඇති Mistral හි ප්‍රධාන මොඩලයයි.

මෙම මොඩලය මුල් Mistral Large එකට වඩා වර්ධනයක් ලබා දෙයි:
- විශාල පෙළ කවුළුව - 128k vs 32k
- ගණිත සහ කේත කාර්යයන්හි වැඩි කාර්ය සාධනය - 76.9% සාමාන්‍ය නිවැරදි බව vs 60.4%
- බහුභාෂා කාර්ය සාධනය වැඩි කිරීම - භාෂා: ඉංග්‍රීසි, ප්‍රංශ, ජර්මානු, ස්පාඤ්ඤ, ඉතාලි, පෘතුගීසි, ඩච්, රුසියානු, චීන, ජපන්, කොරියානු, අරාබි, හා හින්දි.

මෙම විශේෂාංගයන් සමඟ, Mistral Large විශිෂ්ටයි:
- *ප්‍රතිලාභ වර්ධිත ජනනය (RAG)* - විශාල පෙළ කවුළුව නිසා
- *කාර්ය ඇමතුම* - මෙම මොඩලය ස්වභාවික කාර්ය ඇමතුමක් ඇත, එය බාහිර මෙවලම් සහ API සමඟ ඒකාබද්ධ කිරීමට ඉඩ සලසයි. මෙම ඇමතුම් එකිනෙකට පසුපසින් හෝ සමකාලීනව කළ හැක.
- *කේත ජනනය* - මෙම මොඩලය Python, Java, TypeScript සහ C++ ජනනය සඳහා විශිෂ්ටයි.

### RAG උදාහරණයක් Mistral Large 2 භාවිතා කරමින්

මෙම උදාහරණයේදී, අපි Mistral Large 2 භාවිතා කරමින් පෙළ ලේඛනයක් මත RAG රටාවක් ක්‍රියාත්මක කරමු. ප්‍රශ්නය කොරියානු භාෂාවෙන් ලියා ඇති අතර විශ්වවිද්‍යාලයට පෙර ලේඛකයාගේ ක්‍රියාකාරකම් ගැන විමසයි.

එය Cohere Embeddings Model භාවිතා කරමින් පෙළ ලේඛනයේ සහ ප්‍රශ්නයේ ඇතුළත් කිරීම් නිර්මාණය කරයි. මෙම නියැදි සඳහා, එය faiss Python පැකේජය වෙක්ටර් ගබඩා ලෙස භාවිතා කරයි.

Mistral මොඩලයට යවන ප්‍රවේශය ප්‍රශ්න සහ ප්‍රශ්නයට සමාන ප්‍රතිලාභ ලැබුණු කැබලි දෙකම ඇතුළත් වේ. මොඩලය පරිසර භාෂාවෙන් පිළිතුරු ලබා දේ.

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

Mistral Small යනු ප්‍රධාන/ව්‍යාපාරික කාණ්ඩය යටතේ ඇති Mistral මොඩල් පවුලේ තවත් මොඩලයකි. නමෙන් පෙනෙන පරිදි, මෙම මොඩලය කුඩා භාෂා මොඩලයකි (SLM). Mistral Small භාවිතා කිරීමේ වාසි වන්නේ:
- Mistral LLMs වැනි Mistral Large සහ NeMo සමඟ සසඳන විට වියදම් ඉතිරි කිරීම - 80% මිල අඩුවීම
- අඩු ප්‍රමාදය - Mistral LLMs සමඟ සසඳන විට වේගවත් පිළිතුරු
- ප්‍රකෘතිමය - අවශ්‍ය සම්පත් මත සීමාකාරීතාව අඩුවෙන් විවිධ පරිසරයන් අතර පිහිටුවිය හැක.

Mistral Small විශිෂ්ටයි:
- සාරාංශ කිරීම, හැඟීම් විශ්ලේෂණය සහ පරිවර්තනය වැනි පෙළ මත පදනම් වූ කාර්යයන් සඳහා.
- එහි වියදම් කාර්යක්ෂමතාවය නිසා නිතර ඉල්ලීම් කරන යෙදුම් සඳහා
- සමාලෝචන සහ කේත යෝජනා වැනි අඩු ප්‍රමාද කේත කාර්යයන්

## Mistral Small සහ Mistral Large සසඳීම

Mistral Small සහ Large අතර ප්‍රමාදය වෙනස්කම් පෙන්වීම සඳහා පහත සෙල් ක්‍රියාත්මක කරන්න.

ඔබට පිළිතුරු කාලය අතර විනාඩි 3-5ක් වෙනසක් පෙනේවි. එමෙන්ම එකම ප්‍රවේශය මත පිළිතුරු දිග සහ ශෛලිය සටහන් කරන්න.

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

මෙම පාඩමෙන් සාකච්ඡා කරන අනෙකුත් මොඩල් දෙක සමඟ සසඳන විට, Mistral NeMo යනු Apache2 බලපත්‍රය සමඟ ඇති එකම නොමිලේ මොඩලයයි.

එය Mistral, Mistral 7B හි පෙර විවෘත මූලාශ්‍ර LLM එකට වර්ධනයක් ලෙස දකින්නෙකි.

NeMo මොඩලයේ අනෙකුත් විශේෂාංග කිහිපයක්:

- *වැඩි කාර්යක්ෂම ටෝකනීකරණය:* මෙම මොඩලය වැඩි භාෂා සහ කේතයක් මත වැඩි කාර්ය සාධනය සඳහා සාමාන්‍යයෙන් භාවිතා කරන tiktoken එකට වඩා Tekken ටෝකනීසර් භාවිතා කරයි.

- *සම්භාව්‍ය කිරීම:* මූලික මොඩලය සම්භාව්‍ය කිරීම සඳහා ලබා ගත හැක. සම්භාව්‍ය කිරීම අවශ්‍ය විය හැකි භාවිතා කේස් සඳහා වැඩි ප්‍රකෘතිමය සඳහා මෙය ඉඩ සලසයි.

- *ස්වභාවික කාර්ය ඇමතුම* - Mistral Large වැනි, මෙම මොඩලය කාර්ය ඇමතුම මත පුහුණු කර ඇත. මෙය එවැනි ප්‍රථම විවෘත මූලාශ්‍ර මොඩලයන්ගෙන් එකක් බවින් ඒකීය වේ.

### ටෝකනීසර් සසඳීම

මෙම උදාහරණයේදී, Mistral NeMo ටෝකනීකරණය Mistral Large සමඟ සසඳන ආකාරය අපි බලමු.

මොඩල් දෙකම එකම ප්‍රවේශය ගනී, නමුත් NeMo Mistral Large එකට වඩා අඩු ටෝකන ලබා දෙන බව ඔබට පෙනේවි.

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

## ඉගෙනීම මෙහිදී නතර නොකරන්න, ගමන දිගටම කරගෙන යන්න

මෙම පාඩම අවසන් කිරීමෙන් පසු, ඔබේ Generative AI දැනුම වර්ධනය කිරීමට [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) බලන්න!

**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku bi moral biti obravnavan kot avtoritativni vir. Za ključne informacije se priporoča profesionalni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.