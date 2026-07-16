# Práca s modelmi Mistral 

## Úvod 

Táto lekcia pokryje: 
- Preskúmanie rôznych modelov Mistral 
- Pochopenie prípadov použitia a scenárov pre každý model 
- Preskúmanie ukážok kódu, ktoré ukazujú jedinečné vlastnosti každého modelu. 

## Modely Mistral 

V tejto lekcii preskúmame 3 rôzne modely Mistral: 
**Mistral Large**, **Mistral Small** a **Mistral Nemo**. 

Každý z týchto modelov je zadarmo dostupný na [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Kód v tomto notebooku bude používať tieto modely na spúšťanie kódu.

> **Poznámka:** GitHub Models bude ukončený koncom júla 2026. Tu sú ďalšie podrobnosti o používaní [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) na prototypovanie s AI modelmi. 


## Mistral Large 2 (2407)
Mistral Large 2 je momentálne vlajkový model od Mistralu určený na podnikové použitie. 

Tento model je vylepšením pôvodného Mistral Large, ponúkajúc: 
- Väčšie kontextové okno - 128k vs 32k 
- Lepší výkon v matematických a programovacích úlohách - priemerná presnosť 76,9 % vs 60,4 % 
- Zvýšený výkon v mnohých jazykoch - jazyky zahŕňajú: angličtina, francúzština, nemčina, španielčina, taliančina, portugalčina, holandčina, ruština, čínština, japončina, kórejčina, arabčina a hindčina.

Vďaka týmto vlastnostiam Mistral Large vyniká v: 
- *Retrieval Augmented Generation (RAG)* - vďaka väčšiemu kontextovému oknu
- *Volanie funkcií* - tento model má natívne volanie funkcií, čo umožňuje integráciu s externými nástrojmi a API. Tieto volania môžu byť vykonávané paralelne alebo sekvenčne v poradí. 
- *Generovanie kódu* - tento model vyniká v generovaní Python, Java, TypeScript a C++ kódu. 

### Príklad RAG s použitím Mistral Large 2 

V tomto príklade používame Mistral Large 2 na spustenie RAG vzoru nad textovým dokumentom. Otázka je napísaná v kórejčine a pýta sa na aktivity autora pred vysokou školou. 

Používa model Cohere Embeddings na vytvorenie vektorov textového dokumentu aj otázky. Tento príklad používa Python balík faiss ako vektorové úložisko. 

Prompt odoslaný do modelu Mistral zahŕňa otázky aj získané časti textu, ktoré sú podobné otázke. Model potom poskytuje odpoveď v prirodzenom jazyku. 

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
Mistral Small je ďalší model rodiny Mistral v kategórii premier/enterprise. Ako názov napovedá, tento model je Small Language Model (SLM). Výhody použitia Mistral Small sú: 
- Úspora nákladov v porovnaní s Mistral LLM ako Mistral Large a NeMo - pokles ceny o 80 %
- Nízka latencia - rýchlejšia odpoveď v porovnaní s Mistral LLM
- Flexibilita - môže byť nasadený v rôznych prostrediach s menšími obmedzeniami na požadované zdroje. 


Mistral Small je ideálny pre: 
- Textové úlohy ako sumarizácia, analýza sentimentu a preklad. 
- Aplikácie, kde sa vykonávajú časté požiadavky kvôli jeho cenovej efektívnosti 
- Nízkolatenčné úlohy kódovania ako kontrola a návrhy kódu 

## Porovnanie Mistral Small a Mistral Large 

Pre ukázanie rozdielu v latencii medzi Mistral Small a Large spustite nižšie bunky. 

Mali by ste vidieť rozdiel v čase odozvy približne 3-5 sekúnd. Tiež si všimnite dĺžku a štýl odpovede na rovnaký prompt.  

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

V porovnaní s dvoma predchádzajúcimi modelmi diskutovanými v tejto lekcii je Mistral NeMo jediný bezplatný model s licenciou Apache2. 

Je považovaný za vylepšenie predchádzajúceho open source LLM od Mistral, Mistral 7B. 

Niektoré ďalšie vlastnosti modelu NeMo sú: 

- *Efektívnejšia tokenizácia:* Tento model používa tokenizer Tekken namiesto bežnejšieho tiktoken. To umožňuje lepší výkon pri viacerých jazykoch a kóde. 

- *Doladenie:* Základný model je dostupný na doladenie. To umožňuje väčšiu flexibilitu pre prípady použitia, kde je potrebné doladenie. 

- *Natívne volanie funkcií* - Rovnako ako Mistral Large, tento model bol trénovaný na volanie funkcií. Čím sa stal unikátnym ako jeden z prvých open source modelov s touto schopnosťou. 


### Porovnanie tokenizerov 

V tomto príklade sa pozrieme, ako Mistral NeMo spracováva tokenizáciu v porovnaní s Mistral Large. 

Obe ukážky používajú rovnaký prompt, ale mali by ste vidieť, že NeMo vracia menej tokenov než Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Importujte potrebné balíčky:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Načítajte tokenizér Mistral

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

# Načítajte tokenizer Mistral

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

Po dokončení tejto lekcie si pozrite našu [kolekciu Generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste naďalej zvyšovali svoje znalosti o generatívnej AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->