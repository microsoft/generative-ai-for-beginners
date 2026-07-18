# Vývoj s modelmi Mistral 

## Úvod 

Táto lekcia pokrýva: 
- Preskúmanie rôznych modelov Mistral 
- Pochopenie prípadov použitia a scenárov pre každý model 
- Preskúmanie ukážok kódu, ktoré ukazujú jedinečné vlastnosti každého modelu. 

## Modely Mistral 

V tejto lekcii preskúmame 3 rôzne modely Mistral: 
**Mistral Large**, **Mistral Small** a **Mistral Nemo**. 

Každý z týchto modelov je k dispozícii zadarmo na [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Kód v tomto notebooku bude používať tieto modely na spustenie kódu.

> **Poznámka:** GitHub Models končí na konci júla 2026. Tu sú ďalšie informácie o používaní [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) na prototypovanie s AI modelmi. 


## Mistral Large 2 (2407)
Mistral Large 2 je momentálne vlajkový model od Mistral a je navrhnutý pre podnikové použitie. 

Model je vylepšením pôvodného Mistral Large a ponúka 
-  Väčšie kontextové okno - 128k vs 32k 
-  Lepší výkon pri matematických a kódovacích úlohách - priemerná presnosť 76,9 % vs 60,4 % 
-  Zvýšený viacjazyčný výkon - jazyky zahŕňajú: angličtinu, francúzštinu, nemčinu, španielčinu, taliančinu, portugalčinu, holandčinu, ruštinu, čínštinu, japončinu, kórejčinu, arabčinu a hindčinu.

Vďaka týmto vlastnostiam Mistral Large vyniká v 
- *Generácii podporenej vyhľadávaním (RAG)* - vďaka väčšiemu kontextovému oknu
- *Volaní funkcií* - tento model má natívne volanie funkcií, čo umožňuje integráciu s externými nástrojmi a API. Tieto volania je možné vykonávať paralelne alebo postupne za sebou.
- *Generovaní kódu* - tento model vyniká v generovaní Pythonu, Javy, TypeScriptu a C++.

### Príklad RAG s použitím Mistral Large 2 

V tomto príklade používame Mistral Large 2 na spustenie vzoru RAG nad textovým dokumentom. Otázka je napísaná kórejsky a pýta sa na aktivity autora pred vysokou školou. 

Používa model Cohere Embeddings na tvorbu vektorových reprezentácií textu dokumentu aj otázky. Pre túto ukážku používa Python balík faiss ako vektorovú databázu. 

Prompt, ktorý sa posiela modelu Mistral, obsahuje otázky aj načítané kúsky textu podobné otázke. Model potom poskytuje odpoveď v prirodzenom jazyku. 

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

# Získajte ich zo stránky "Prehľad" vášho projektu Microsoft Foundry
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # vzdialenosť, index
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
Mistral Small je ďalší model v rodine Mistral patriaci do kategórie prémiových/podnikových modelov. Ako naznačuje názov, tento model je Malý jazykový model (SLM). Výhody použitia Mistral Small sú: 
- Úspora nákladov v porovnaní s LLM Mistral ako Mistral Large a NeMo - pokles ceny o 80 %
- Nízka latencia - rýchlejšia odpoveď v porovnaní s LLM Mistral
- Flexibilita - môže byť nasadený v rôznych prostrediach s menšími obmedzeniami na požadované zdroje.


Mistral Small je vhodný pre: 
- Úlohy založené na texte ako sumarizácia, analýza sentimentu a preklad.
- Aplikácie s častými požiadavkami vďaka jeho cenovej efektívnosti
- Nízku latenciu pri úlohách súvisiacich s kódom, ako je kontrola kódu a návrhy kódu

## Porovnanie Mistral Small a Mistral Large 

Pre ukázanie rozdielov v latencii medzi Mistral Small a Large spustite nasledujúce bunky. 

Mali by ste vidieť rozdiel v čase odozvy medzi 3 až 5 sekundami. Tiež si všimnite dĺžky a štýlu odpovede na rovnaký prompt.  

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

V porovnaní s ostatnými dvoma modelmi spomenutými v tejto lekcii je Mistral NeMo jediný bezplatný model s licenciou Apache2. 

Je vnímaný ako vylepšenie predchádzajúceho open source LLM od Mistral, Mistral 7B. 

Niektoré ďalšie vlastnosti modelu NeMo sú: 

- *Efektívnejšia tokenizácia:* Tento model používa tokenizer Tekken namiesto bežnejšie používaného tiktoken. To umožňuje lepší výkon v rôznych jazykoch a kóde. 

- *Doladenie:* Základný model je k dispozícii na doladenie. To umožňuje väčšiu flexibilitu pre prípady použitia, kde je potrebné doladenie. 

- *Natívne volanie funkcií* - Rovnako ako Mistral Large, tento model bol trénovaný na volanie funkcií. To ho robí jedinečným ako jeden z prvých open source modelov, ktoré to umožňujú. 


### Porovnanie tokenizerov 

V tejto ukážke sa pozrieme, ako Mistral NeMo spracováva tokenizáciu v porovnaní s Mistral Large. 

Obe ukážky berú rovnaký prompt, ale mali by ste vidieť, že NeMo vracia menej tokenov než Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Importujte potrebné balíky:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Načítajte Mistral tokenizer

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenizujte zoznam správ
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

# Spočítajte počet tokenov
print(len(tokens))
```

```python
# Importujte potrebné balíky:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Načítajte Mistral tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenizujte zoznam správ
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

# Spočítajte počet tokenov
print(len(tokens))
```

## Učenie tu nekončí, pokračujte v ceste

Po dokončení tejto lekcie si pozrite našu [kolekciu Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste naďalej zlepšovali svoje znalosti v oblasti generatívnej AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->