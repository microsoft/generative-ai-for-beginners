# Tvorba s modelmi Mistral

## Úvod

Táto lekcia pokryje:  
- Preskúmanie rôznych modelov Mistral  
- Pochopenie prípadov použitia a scenárov pre každý model  
- Preskúmanie ukážok kódu, ktoré ukazujú jedinečné vlastnosti každého modelu.

## Modely Mistral

V tejto lekcii preskúmame 3 rôzne modely Mistral:  
**Mistral Large**, **Mistral Small** a **Mistral Nemo**.

Každý z týchto modelov je dostupný zadarmo na GitHub Model marketplace. Kód v tomto notebooku bude používať tieto modely na spustenie kódu. Tu sú ďalšie detaily o používaní GitHub Modelov na [prototypovanie s AI modelmi](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
Mistral Large 2 je momentálne vlajkový model od Mistral a je navrhnutý pre podnikové použitie.

Model je vylepšením pôvodného Mistral Large ponúkajúc:  
- Väčšie kontextové okno - 128k vs 32k  
- Lepší výkon v matematických a programovacích úlohách - priemerná presnosť 76,9 % vs 60,4 %  
- Zvýšený výkon v mnohých jazykoch - jazyky zahŕňajú: angličtinu, francúzštinu, nemčinu, španielčinu, taliančinu, portugalčinu, holandčinu, ruštinu, čínštinu, japončinu, kórejčinu, arabčinu a hindčinu.

S týmito vlastnosťami Mistral Large vyniká v:  
- *Retrieval Augmented Generation (RAG)* - vďaka väčšiemu kontextovému oknu  
- *Volanie funkcií* - tento model má natívne volanie funkcií, ktoré umožňuje integráciu s externými nástrojmi a API. Tieto volania môžu byť vykonávané paralelne alebo jedno po druhom v sekvenčnom poradí.  
- *Generovanie kódu* - tento model exceluje v generovaní kódu v jazykoch Python, Java, TypeScript a C++.

### Príklad RAG použitia s Mistral Large 2

V tomto príklade používame Mistral Large 2 na spustenie vzoru RAG nad textovým dokumentom. Otázka je napísaná po kórejsky a pýta sa na aktivity autora pred fakultou.

Používa sa model Cohere Embeddings na vytvorenie vektorových reprezentácií textového dokumentu aj otázky. Pre tento príklad sa používa balík faiss pre Python ako vektorové úložisko.

Výzva poslaná modelu Mistral obsahuje otázky aj načítané kúsky textu, ktoré sú podobné otázke. Model potom poskytne odpoveď v prirodzenom jazyku.

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
Mistral Small je ďalší model v rodine Mistral v rámci kategórie premier/podnikových modelov. Ako názov napovedá, ide o malý jazykový model (SLM). Výhody používania Mistral Small sú:  
- Úspora nákladov v porovnaní s Mistral LLM ako Mistral Large a NeMo - zníženie ceny o 80 %  
- Nízka latencia - rýchlejšia odpoveď v porovnaní s Mistral LLM  
- Flexibilita - môže byť nasadený v rôznych prostrediach s menšími požiadavkami na zdroje.

Mistral Small je skvelý pre:  
- Textové úlohy ako zhrnutie, analýza sentimentu a preklad  
- Aplikácie, kde sú časté požiadavky kvôli cenovej efektívnosti  
- Úlohy s nízkou latenciou, ako sú recenzie kódu a návrhy kódu

## Porovnanie Mistral Small a Mistral Large

Na zobrazenie rozdielov v latencii medzi Mistral Small a Large spustite nižšie uvedené bunky.

Mali by ste vidieť rozdiel v časoch odozvy medzi 3-5 sekundami. Tiež si všimnite dĺžku a štýl odpovede na rovnakú výzvu.

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

V porovnaní s ostatnými dvoma modelmi diskutovanými v tejto lekcii je Mistral NeMo jediný bezplatný model s licenciou Apache2.

Považuje sa za vylepšenie skoršieho open source LLM od Mistral, Mistral 7B.

Medzi ďalšie vlastnosti modelu NeMo patria:

- *Efektívnejšia tokenizácia:* Tento model používa tokenizer Tekken namiesto častejšie používaného tiktoken. To umožňuje lepší výkon v širšom spektre jazykov a kódu.

- *Doladenie (finetuning):* Základný model je dostupný na doladenie, čo poskytuje väčšiu flexibilitu pre prípady použitia, kde je doladenie potrebné.

- *Natívne volanie funkcií* - Rovnako ako Mistral Large, aj tento model bol trénovaný na volanie funkcií. To z neho robí jeden z prvých open source modelov, ktoré túto schopnosť majú.

### Porovnanie tokenizérov

V tomto príklade si ukážeme, ako Mistral NeMo spracováva tokenizáciu v porovnaní s Mistral Large.

Oba príklady používajú tú istú výzvu, no mali by ste vidieť, že NeMo vracia menej tokenov než Mistral Large.

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

# Načítajte tokenizer Mistral

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
  
## Učenie sa tu nekončí, pokračujte v ceste

Po dokončení tejto lekcie si pozrite našu [kolekciu Generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali vo zvyšovaní svojich znalostí o Generatívnej AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladateľa [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, vezmite prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by sa mal považovať za autoritatívny zdroj. Pre kritické informácie sa odporúča využiť profesionálny ľudský preklad. Nenesieme zodpovednosť za žiadne nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->