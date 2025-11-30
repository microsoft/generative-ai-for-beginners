<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:03:26+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "sk"
}
-->
# Práca s modelmi Mistral

## Úvod

Táto lekcia pokrýva:  
- Preskúmanie rôznych modelov Mistral  
- Pochopenie prípadov použitia a scenárov pre každý model  
- Ukážky kódu, ktoré demonštrujú jedinečné vlastnosti jednotlivých modelov.

## Modely Mistral

V tejto lekcii preskúmame 3 rôzne modely Mistral:  
**Mistral Large**, **Mistral Small** a **Mistral Nemo**.

Každý z týchto modelov je dostupný zadarmo na Github Model marketplace. Kód v tomto notebooku bude používať tieto modely na spustenie kódu. Tu sú podrobnejšie informácie o používaní Github Models na [prototypovanie s AI modelmi](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 je momentálne vlajkový model od Mistral a je navrhnutý pre podnikové použitie.

Model je vylepšením pôvodného Mistral Large a ponúka:  
- Väčšie kontextové okno – 128k oproti 32k  
- Lepší výkon v matematických a programovacích úlohách – priemerná presnosť 76,9 % oproti 60,4 %  
- Zvýšený výkon v mnohých jazykoch – vrátane angličtiny, francúzštiny, nemčiny, španielčiny, taliančiny, portugalčiny, holandčiny, ruštiny, čínštiny, japončiny, kórejčiny, arabčiny a hindčiny.

Vďaka týmto vlastnostiam Mistral Large vyniká v:  
- *Retrieval Augmented Generation (RAG)* – vďaka väčšiemu kontextovému oknu  
- *Volanie funkcií* – tento model má natívnu podporu volania funkcií, čo umožňuje integráciu s externými nástrojmi a API. Volania môžu prebiehať paralelne alebo sekvenčne jedno za druhým.  
- *Generovanie kódu* – model exceluje v generovaní kódu v Pythone, Jave, TypeScripte a C++.

### Príklad RAG s použitím Mistral Large 2

V tomto príklade používame Mistral Large 2 na spustenie RAG vzoru nad textovým dokumentom. Otázka je napísaná v kórejčine a pýta sa na aktivity autora pred nástupom na vysokú školu.

Používa Cohere Embeddings Model na vytvorenie embeddingov textového dokumentu aj otázky. Pre tento príklad sa používa Python balík faiss ako vektorové úložisko.

Prompt zaslaný modelu Mistral obsahuje otázky aj získané časti textu, ktoré sú podobné otázke. Model potom poskytne odpoveď v prirodzenom jazyku.

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

Mistral Small je ďalší model v rodine Mistral, patriaci do kategórie premier/enterprise. Ako názov napovedá, ide o malý jazykový model (SLM). Výhody použitia Mistral Small sú:  
- Úspora nákladov v porovnaní s veľkými modelmi Mistral, ako sú Mistral Large a NeMo – zníženie ceny o 80 %  
- Nízka latencia – rýchlejšia odozva v porovnaní s veľkými modelmi Mistral  
- Flexibilita – môže byť nasadený v rôznych prostrediach s menšími požiadavkami na zdroje.

Mistral Small je ideálny pre:  
- Textové úlohy ako sumarizácia, analýza sentimentu a preklad  
- Aplikácie s častými požiadavkami vďaka svojej cenovej efektívnosti  
- Úlohy s nízkou latenciou, ako je kontrola kódu a návrhy kódu

## Porovnanie Mistral Small a Mistral Large

Pre zobrazenie rozdielov v latencii medzi Mistral Small a Large spustite nasledujúce bunky.

Mali by ste vidieť rozdiel v čase odozvy približne 3-5 sekúnd. Tiež si všimnite dĺžku a štýl odpovedí na rovnaký prompt.

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

V porovnaní s dvoma predchádzajúcimi modelmi je Mistral NeMo jediný bezplatný model s licenciou Apache2.

Je považovaný za vylepšenie predchádzajúceho open source LLM od Mistral, Mistral 7B.

Medzi ďalšie vlastnosti modelu NeMo patria:

- *Efektívnejšia tokenizácia:* Tento model používa tokenizer Tekken namiesto bežnejšieho tiktoken. To umožňuje lepší výkon v rôznych jazykoch a kóde.

- *Doladenie (finetuning):* Základný model je dostupný na doladenie, čo prináša väčšiu flexibilitu pre prípady použitia, kde je doladenie potrebné.

- *Natívne volanie funkcií* – Rovnako ako Mistral Large, aj tento model bol trénovaný na volanie funkcií. To ho robí jedinečným ako jeden z prvých open source modelov s touto schopnosťou.

### Porovnanie tokenizérov

V tomto príklade sa pozrieme, ako Mistral NeMo spracováva tokenizáciu v porovnaní s Mistral Large.

Oba príklady používajú rovnaký prompt, no mali by ste vidieť, že NeMo vracia menej tokenov ako Mistral Large.

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

## Učenie tu nekončí, pokračujte v ceste

Po dokončení tejto lekcie si pozrite našu [kolekciu Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a pokračujte v rozširovaní svojich znalostí o generatívnej AI!

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.