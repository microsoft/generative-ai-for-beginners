<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:21:49+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "sk"
}
-->
# Budovanie s modelmi Mistral

## Úvod

Táto lekcia pokryje:
- Preskúmanie rôznych modelov Mistral
- Pochopenie prípadov použitia a scenárov pre každý model
- Ukážky kódu, ktoré ukazujú jedinečné vlastnosti každého modelu.

## Modely Mistral

V tejto lekcii preskúmame 3 rôzne modely Mistral: **Mistral Large**, **Mistral Small** a **Mistral Nemo**.

Každý z týchto modelov je dostupný zadarmo na trhu modelov Github. Kód v tomto notebooku bude používať tieto modely na spustenie kódu. Tu sú ďalšie podrobnosti o používaní modelov Github na [prototypovanie s AI modelmi](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 je momentálne vlajkový model od Mistral a je navrhnutý pre podnikové použitie.

Model je vylepšením pôvodného Mistral Large tým, že ponúka:
- Väčšie kontextové okno - 128k vs 32k
- Lepší výkon pri matematických a kódovacích úlohách - 76,9% priemerná presnosť vs 60,4%
- Zvýšený výkon v oblasti viacjazyčnosti - jazyky zahŕňajú: angličtinu, francúzštinu, nemčinu, španielčinu, taliančinu, portugalčinu, holandčinu, ruštinu, čínštinu, japončinu, kórejčinu, arabčinu a hindčinu.

S týmito vlastnosťami, Mistral Large vyniká v:
- *Retrieval Augmented Generation (RAG)* - vďaka väčšiemu kontextovému oknu
- *Volanie funkcií* - tento model má natívne volanie funkcií, čo umožňuje integráciu s externými nástrojmi a API. Tieto volania môžu byť vykonané paralelne alebo postupne jeden po druhom.
- *Generovanie kódu* - tento model vyniká pri generovaní Pythonu, Java, TypeScript a C++.

### Príklad RAG pomocou Mistral Large 2

V tomto príklade používame Mistral Large 2 na spustenie vzoru RAG nad textovým dokumentom. Otázka je napísaná v kórejčine a pýta sa na aktivity autora pred vysokou školou.

Používa model Cohere Embeddings na vytvorenie embeddingov textového dokumentu ako aj otázky. Pre tento príklad používa Python balíček faiss ako vektorový úložisko.

Výzva zaslaná modelu Mistral obsahuje otázky a získané úseky, ktoré sú podobné otázke. Model potom poskytuje odpoveď v prirodzenom jazyku.

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
Mistral Small je ďalší model v rodine modelov Mistral pod kategóriou premier/podnikový. Ako naznačuje názov, tento model je malý jazykový model (SLM). Výhody používania Mistral Small sú:
- Úspora nákladov v porovnaní s LLM modelmi Mistral ako Mistral Large a NeMo - pokles ceny o 80%
- Nízka latencia - rýchlejšia odozva v porovnaní s LLM modelmi Mistral
- Flexibilita - môže byť nasadený v rôznych prostrediach s menšími obmedzeniami na potrebné zdroje.

Mistral Small je skvelý pre:
- Úlohy založené na texte, ako sú sumarizácia, analýza sentimentu a preklad.
- Aplikácie, kde sa často uskutočňujú požiadavky vďaka jeho efektívnosti nákladov
- Úlohy kódu s nízkou latenciou ako prehľad a návrhy kódu

## Porovnanie Mistral Small a Mistral Large

Na ukázanie rozdielov v latencii medzi Mistral Small a Large, spustite nasledujúce bunky.

Mali by ste vidieť rozdiel v časoch odozvy medzi 3-5 sekúnd. Tiež si všimnite dĺžky a štýl odpovedí na rovnakú výzvu.

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

V porovnaní s ostatnými dvoma modelmi diskutovanými v tejto lekcii, Mistral NeMo je jediný bezplatný model s licenciou Apache2.

Je považovaný za vylepšenie skoršieho open source LLM od Mistral, Mistral 7B.

Niektoré ďalšie vlastnosti modelu NeMo sú:

- *Efektívnejšia tokenizácia:* Tento model používa tokenizátor Tekken namiesto bežnejšie používaného tiktoken. To umožňuje lepší výkon vo viacerých jazykoch a kóde.

- *Finetuning:* Základný model je dostupný pre finetuning. To umožňuje väčšiu flexibilitu pre prípady použitia, kde môže byť potrebný finetuning.

- *Natívne volanie funkcií* - Podobne ako Mistral Large, tento model bol trénovaný na volanie funkcií. To ho robí jedinečným ako jeden z prvých open source modelov, ktorý to robí.

### Porovnanie tokenizátorov

V tomto príklade sa pozrieme, ako Mistral NeMo zvláda tokenizáciu v porovnaní s Mistral Large.

Oba príklady berú rovnakú výzvu, ale mali by ste vidieť, že NeMo vracia menej tokenov oproti Mistral Large.

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

## Učenie sa nekončí tu, pokračujte v ceste

Po dokončení tejto lekcie si pozrite našu [kolekciu učenia Generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali v zlepšovaní svojich znalostí o Generatívnej AI!

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by sa mal považovať za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vznikajúce z použitia tohto prekladu.