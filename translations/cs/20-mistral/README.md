<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:21:29+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "cs"
}
-->
# Stavba s modely Mistral

## Úvod

Tato lekce se bude zabývat:
- Prozkoumáním různých modelů Mistral
- Porozuměním případům použití a scénářům pro každý model
- Ukázky kódu, které ukazují jedinečné vlastnosti každého modelu

## Modely Mistral

V této lekci prozkoumáme 3 různé modely Mistral: **Mistral Large**, **Mistral Small** a **Mistral Nemo**.

Každý z těchto modelů je k dispozici zdarma na trhu modelů Github. Kód v tomto zápisníku bude používat tyto modely k běhu kódu. Zde jsou další podrobnosti o používání Github Modelů pro [prototypování s AI modely](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 je v současnosti vlajkový model od Mistralu a je navržen pro podnikové použití.

Model je vylepšením původního Mistral Large a nabízí
- Větší kontextové okno - 128k vs 32k
- Lepší výkon při matematických a programovacích úlohách - 76,9% průměrná přesnost vs 60,4%
- Zvýšený výkon v mnoha jazycích - jazyky zahrnují: angličtinu, francouzštinu, němčinu, španělštinu, italštinu, portugalštinu, nizozemštinu, ruštinu, čínštinu, japonštinu, korejštinu, arabštinu a hindštinu.

S těmito funkcemi Mistral Large exceluje v
- *Retrieval Augmented Generation (RAG)* - díky většímu kontextovému oknu
- *Volání funkcí* - tento model má nativní volání funkcí, což umožňuje integraci s externími nástroji a API. Tyto volání lze provádět paralelně nebo po jednom v sekvenčním pořadí.
- *Generování kódu* - tento model exceluje v generování Pythonu, Javy, TypeScriptu a C++.

### Příklad RAG pomocí Mistral Large 2

V tomto příkladu používáme Mistral Large 2 k běhu RAG vzoru nad textovým dokumentem. Otázka je napsána v korejštině a ptá se na aktivity autora před vysokou školou.

Používá model Cohere Embeddings k vytvoření vnoření textového dokumentu i otázky. Pro tento příklad používá Python balíček faiss jako vektorový úložiště.

Výzva zaslaná modelu Mistral zahrnuje jak otázky, tak získané části, které jsou podobné otázce. Model poté poskytuje odpověď v přirozeném jazyce.

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
Mistral Small je další model v rodině modelů Mistral pod kategorií premier/podnikové. Jak název napovídá, tento model je Malý jazykový model (SLM). Výhody používání Mistral Small jsou, že je:
- Úsporný ve srovnání s Mistral LLM jako Mistral Large a NeMo - pokles ceny o 80%
- Nízká latence - rychlejší odezva ve srovnání s LLM od Mistralu
- Flexibilní - může být nasazen napříč různými prostředími s menšími omezeními na požadované zdroje.

Mistral Small je skvělý pro:
- Úlohy založené na textu, jako je shrnutí, analýza sentimentu a překlad.
- Aplikace, kde se často provádějí požadavky díky jeho nákladové efektivitě
- Úlohy s nízkou latencí, jako je kontrola a návrhy kódu

## Porovnání Mistral Small a Mistral Large

Pro zobrazení rozdílů v latenci mezi Mistral Small a Large spusťte níže uvedené buňky.

Měli byste vidět rozdíl v časech odezvy mezi 3-5 sekundami. Také si všimněte délky a stylu odpovědí na stejnou výzvu.

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

Ve srovnání s dalšími dvěma modely diskutovanými v této lekci je Mistral NeMo jediným volně dostupným modelem s licencí Apache2.

Je považován za vylepšení dřívějšího open source LLM od Mistralu, Mistral 7B.

Některé další vlastnosti modelu NeMo jsou:

- *Efektivnější tokenizace:* Tento model používá tokenizátor Tekken namísto běžněji používaného tiktoken. To umožňuje lepší výkon v různých jazycích a kódech.

- *Doladění:* Základní model je k dispozici pro doladění. To umožňuje větší flexibilitu pro případy použití, kde může být doladění potřebné.

- *Nativní volání funkcí* - Stejně jako Mistral Large byl tento model vycvičen na volání funkcí. To ho činí jedním z prvních open source modelů, který to dokáže.

### Porovnání tokenizátorů

V tomto příkladu se podíváme, jak Mistral NeMo zpracovává tokenizaci ve srovnání s Mistral Large.

Oba příklady mají stejnou výzvu, ale měli byste vidět, že NeMo vrací méně tokenů než Mistral Large.

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

## Učení zde nekončí, pokračujte v cestě

Po dokončení této lekce se podívejte na naši [kolekci učení o generativní AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste pokračovali ve zvyšování svých znalostí o generativní AI!

**Prohlášení**:  
Tento dokument byl přeložen pomocí AI překladové služby [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za žádné nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.