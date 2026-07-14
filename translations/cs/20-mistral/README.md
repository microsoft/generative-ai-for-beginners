# Stavba s modely Mistral 

## Úvod 

Tato lekce pokryje: 
- Prozkoumání různých modelů Mistral 
- Pochopení použití a scénářů pro každý model 
- Prozkoumání ukázek kódu, které ukazují jedinečné funkce každého modelu. 

## Modely Mistral 

V této lekci prozkoumáme 3 různé modely Mistral: 
**Mistral Large**, **Mistral Small** a **Mistral Nemo**. 

Každý z těchto modelů je zdarma dostupný na [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Kód v tomto sešitě bude tyto modely používat k spuštění kódu.

> **Poznámka:** GitHub Models bude ukončen na konci července 2026. Zde jsou podrobnější informace o použití [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) pro prototypování s AI modely. 


## Mistral Large 2 (2407)
Mistral Large 2 je momentálně vlajkový model od Mistral určený pro podnikové použití. 

Model je vylepšením původního Mistral Large tím, že nabízí 
-  Větší kontextové okno - 128k vs 32k 
-  Lepší výkon v matematických a kódovacích úlohách - průměrná přesnost 76,9 % vs 60,4 % 
-  Zvýšený vícejazyčný výkon - jazyky zahrnují: angličtina, francouzština, němčina, španělština, italština, portugalština, nizozemština, ruština, čínština, japonština, korejština, arabština a hindština.

Díky těmto funkcím vyniká Mistral Large v 
- *Generování doplněné vyhledáváním (RAG)* - díky většímu kontextovému oknu
- *Volání funkcí* - tento model má nativní volání funkcí, které umožňuje integraci s externími nástroji a API. Tyto volání mohou být prováděna souběžně nebo jedno po druhém v sekvenčním pořadí. 
- *Generování kódu* - tento model exceluje v generování Pythonu, Javy, TypeScriptu a C++. 

### Příklad použití RAG s Mistral Large 2 

V tomto příkladu používáme Mistral Large 2 k provedení vzoru RAG nad textovým dokumentem. Otázka je napsaná korejsky a ptá se na aktivity autora před vysokou školou. 

Používá model Cohere Embeddings k vytvoření embeddingů textového dokumentu i otázky. Pro tento příklad používá Python balíček faiss jako vektorové úložiště. 

Prompt zaslaný modelu Mistral zahrnuje jak otázky, tak nalezené úseky podobné otázce. Model pak poskytuje odpověď v přirozeném jazyce. 

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

# Získejte tyto z "Přehledu" vašeho projektu Microsoft Foundry
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # vzdálenost, index
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
Mistral Small je další model z rodiny Mistral v kategorii premier/enterprise. Jak název napovídá, tento model je malý jazykový model (SLM). Výhody používání Mistral Small jsou: 
- Úspora nákladů ve srovnání s modely LLM od Mistral jako Mistral Large a NeMo - snížení ceny o 80 %
- Nízká latence - rychlejší odpověď ve srovnání s LLM od Mistral
- Flexibilní - může být nasazen v různých prostředích s menšími omezeními na požadované zdroje. 


Mistral Small je skvělý pro: 
- Textové úkoly jako shrnutí, analýzu sentimentu a překlady. 
- Aplikace, kde jsou časté požadavky díky jeho cenové efektivitě 
- Úkoly s nízkou latencí pro kód, jako revize a návrhy kódu 

## Porovnání Mistral Small a Mistral Large 

Pro ukázku rozdílů v latenci mezi Mistral Small a Large spusťte následující buňky. 

Vidíte rozdíl v časech odezvy asi 3-5 sekund. Také si všimněte délek a stylu odpovědí na stejný prompt.  

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

Ve srovnání s ostatními dvěma modely probíranými v této lekci je Mistral NeMo jediný bezplatný model s licencí Apache2. 

Je považován za vylepšení dřívějšího open source LLM od Mistral, Mistral 7B. 

Některé další vlastnosti modelu NeMo jsou: 

- *Efektivnější tokenizace:* Tento model používá tokenizer Tekken místo běžně používaného tiktoken. To umožňuje lepší výkon nad více jazyky a kódem. 

- *Doladění (Finetuning):* Základní model je dostupný pro doladění. To poskytuje větší flexibilitu pro případy použití, kde může být doladění potřeba. 

- *Nativní volání funkcí* - Stejně jako Mistral Large, tento model byl trénován na volání funkcí. To ho činí unikátním jako jeden z prvních open source modelů, který to umí. 


### Porovnání tokenizerů 

V tomto příkladu se podíváme, jak Mistral NeMo zpracovává tokenizaci ve srovnání s Mistral Large. 

Oba příklady berou stejný prompt, ale měli byste vidět, že NeMo vrací méně tokenů než Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Importujte potřebné balíčky:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Načtěte Mistral tokenizer

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenizujte seznam zpráv
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

# Spočítejte počet tokenů
print(len(tokens))
```

```python
# Importujte potřebné balíčky:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Načtěte tokenizer Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenizujte seznam zpráv
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

# Spočítejte počet tokenů
print(len(tokens))
```

## Učení zde nekončí, pokračujte na své cestě

Po dokončení této lekce se podívejte na naši [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste mohli pokračovat v rozšiřování svých znalostí o generativní AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->