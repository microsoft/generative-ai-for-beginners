<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:03:13+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "cs"
}
-->
# Práce s modely Mistral

## Úvod

Tato lekce pokrývá:  
- Prozkoumání různých modelů Mistral  
- Pochopení použití a scénářů pro každý model  
- Ukázky kódu, které demonstrují jedinečné vlastnosti jednotlivých modelů.

## Modely Mistral

V této lekci si představíme 3 různé modely Mistral:  
**Mistral Large**, **Mistral Small** a **Mistral Nemo**.

Všechny tyto modely jsou zdarma dostupné na Github Model marketplace. Kód v tomto notebooku bude používat právě tyto modely. Více informací o používání Github Modelů pro [prototypování s AI modely](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) najdete zde.

## Mistral Large 2 (2407)

Mistral Large 2 je v současnosti vlajkový model od Mistral a je navržen pro podnikové využití.

Model je vylepšením původního Mistral Large a nabízí:  
- Větší kontextové okno – 128k oproti 32k  
- Lepší výkon v matematických a programovacích úlohách – průměrná přesnost 76,9 % oproti 60,4 %  
- Zvýšený vícejazyčný výkon – podporované jazyky zahrnují: angličtinu, francouzštinu, němčinu, španělštinu, italštinu, portugalštinu, nizozemštinu, ruštinu, čínštinu, japonštinu, korejštinu, arabštinu a hindštinu.

Díky těmto vlastnostem Mistral Large vyniká v:  
- *Retrieval Augmented Generation (RAG)* – díky většímu kontextovému oknu  
- *Volání funkcí* – tento model má nativní podporu volání funkcí, což umožňuje integraci s externími nástroji a API. Volání lze provádět paralelně i sekvenčně.  
- *Generování kódu* – model exceluje v generování kódu v Pythonu, Javě, TypeScriptu a C++.

### Příklad RAG s Mistral Large 2

V tomto příkladu používáme Mistral Large 2 k provedení RAG vzoru nad textovým dokumentem. Otázka je napsaná v korejštině a ptá se na aktivity autora před nástupem na vysokou školu.

Používá Cohere Embeddings Model k vytvoření embeddingů textového dokumentu i otázky. Pro tento příklad je jako vektorové úložiště použita Python knihovna faiss.

Prompt zaslaný modelu Mistral obsahuje jak otázky, tak nalezené části textu podobné otázce. Model pak poskytne odpověď v přirozeném jazyce.

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

Mistral Small je další model z rodiny Mistral v kategorii premier/enterprise. Jak název napovídá, jedná se o malý jazykový model (SLM). Výhody používání Mistral Small jsou:  
- Úspora nákladů oproti větším modelům Mistral jako Mistral Large a NeMo – cena až o 80 % nižší  
- Nízká latence – rychlejší odezva než u větších modelů Mistral  
- Flexibilita – lze nasadit v různých prostředích s menšími nároky na zdroje.

Mistral Small je ideální pro:  
- Textové úlohy jako shrnutí, analýzu sentimentu a překlad  
- Aplikace s častými požadavky díky své cenové efektivitě  
- Úlohy s nízkou latencí, například kontrolu kódu a návrhy úprav

## Porovnání Mistral Small a Mistral Large

Pro zobrazení rozdílů v latenci mezi Mistral Small a Large spusťte níže uvedené buňky.

Měli byste vidět rozdíl v časech odezvy mezi 3–5 sekundami. Také si všimněte délky a stylu odpovědí na stejný prompt.

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

Ve srovnání s ostatními dvěma modely zmíněnými v této lekci je Mistral NeMo jediný bezplatný model s licencí Apache2.

Je považován za vylepšení dřívějšího open source LLM od Mistral, modelu Mistral 7B.

Další vlastnosti modelu NeMo jsou:

- *Efektivnější tokenizace:* Tento model používá tokenizer Tekken místo běžně používaného tiktoken. To umožňuje lepší výkon v různých jazycích a kódu.

- *Doladění (finetuning):* Základní model je dostupný pro doladění, což přináší větší flexibilitu pro případy, kdy je doladění potřeba.

- *Nativní volání funkcí* – Stejně jako Mistral Large, i tento model byl trénován na volání funkcí. Díky tomu je jedním z prvních open source modelů s touto schopností.

### Porovnání tokenizerů

V tomto příkladu se podíváme, jak Mistral NeMo zpracovává tokenizaci ve srovnání s Mistral Large.

Oba příklady používají stejný prompt, ale uvidíte, že NeMo vrací méně tokenů než Mistral Large.

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

## Učení zde nekončí, pokračujte na své cestě

Po dokončení této lekce si prohlédněte naši [kolekci Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a pokračujte v rozšiřování svých znalostí o generativní AI!

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.