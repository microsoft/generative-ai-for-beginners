<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:04:09+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "sr"
}
-->
# Рад са Мистрал моделима

## Увод

Овај час ће обухватити:  
- Истраживање различитих Мистрал модела  
- Разумевање случајева употребе и сценарија за сваки модел  
- Примере кода који показују јединствене карактеристике сваког модела.

## Мистрал модели

У овом часу ћемо истражити 3 различита Мистрал модела:  
**Mistral Large**, **Mistral Small** и **Mistral Nemo**.

Сви ови модели су бесплатно доступни на Github Model marketplace-у. Код у овом нотебуку користиће ове моделе за извршавање. Ево више детаља о коришћењу Github модела за [прототиповање са AI моделима](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 је тренутно водећи модел из Мистрал породице и дизајниран је за коришћење у предузећима.

Овај модел је надоградња оригиналног Mistral Large и нуди:  
- Веће контекстно окно - 128k уместо 32k  
- Боље перформансе у задацима из математике и програмирања - 76.9% просечне тачности уместо 60.4%  
- Побољшане мултилингвалне перформансе - подржава језике као што су: енглески, француски, немачки, шпански, италијански, португалски, холандски, руски, кинески, јапански, корејски, арапски и хинди.

Са овим карактеристикама, Mistral Large се истиче у:  
- *Retrieval Augmented Generation (RAG)* - захваљујући већем контекстном окну  
- *Function Calling* - овај модел има уграђену подршку за позив функција што омогућава интеграцију са спољним алатима и API-јима. Позиви могу бити извршавани паралелно или један за другим у секвенцијалном редоследу.  
- *Code Generation* - овај модел је одличан у генерисању кода на Python, Java, TypeScript и C++.

### Пример RAG-а користећи Mistral Large 2

У овом примеру користимо Mistral Large 2 да извршимо RAG образац над текстуалним документом. Питање је написано на корејском и тиче се активности аутора пре факултета.

Користи се Cohere Embeddings Model за креирање угнежђених представки текста и питања. За овај пример користи се faiss Python пакет као векторска база.

Порука послата Mistral моделу садржи и питања и пронађене делове текста који су слични питању. Модел затим даје одговор на природном језику.

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

Mistral Small је још један модел из Мистрал породице у премијум/ентерприс категорији. Као што име каже, овај модел је мали језички модел (SLM). Предности коришћења Mistral Small су:  
- Уштеда трошкова у односу на Mistral LLM моделе као што су Mistral Large и NeMo - смањење цене за 80%  
- Ниска латенција - бржи одговор у поређењу са Mistral LLM моделима  
- Флексибилност - може се распоредити у различитим окружењима са мање ограничења у погледу потребних ресурса.

Mistral Small је одличан за:  
- Текстуалне задатке као што су резимирање, анализа сентимента и превођење  
- Апликације са честим захтевима због своје економичности  
- Задатке са ниском латенцијом као што су преглед и предлози кода

## Поређење Mistral Small и Mistral Large

Да бисте видели разлике у латенцији између Mistral Small и Large, покрените следеће ћелије.

Требало би да приметите разлику у времену одговора од 3-5 секунди. Такође обратите пажњу на дужину и стил одговора на исти упит.

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

У поређењу са остала два модела из овог часа, Mistral NeMo је једини бесплатан модел са Apache2 лиценцом.

Сматра се надоградњом ранијег отвореног LLM модела из Мистрал породице, Mistral 7B.

Неке друге карактеристике NeMo модела су:

- *Ефикаснија токенизација:* Овај модел користи Tekken токенизер уместо чешће коришћеног tiktoken. Ово омогућава боље перформансе на више језика и кода.

- *Финетјунинг:* Основни модел је доступан за финетјунинг, што пружа већу флексибилност за случајеве када је потребно прилагођавање.

- *Native Function Calling* - Као и Mistral Large, овај модел је трениран за позив функција. Ово га чини јединственим као један од првих отворених модела са овом могућношћу.

### Поређење токенизера

У овом примеру погледаћемо како Mistral NeMo обрађује токенизацију у поређењу са Mistral Large.

Оба примера користе исти упит, али требало би да видите да NeMo враћа мање токена у односу на Mistral Large.

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

## Учити се овде не завршава, наставите путовање

Након завршетка овог часа, погледајте нашу [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) и наставите да унапређујете своје знање о генеративној вештачкој интелигенцији!

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.