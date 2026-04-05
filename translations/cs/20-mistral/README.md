# Budování s modely Mistral

## Úvod

Tato lekce pokryje:  
- Prozkoumání různých modelů Mistral  
- Porozumění případům použití a scénářům pro každý model  
- Prozkoumání ukázek kódu, které ukazují jedinečné vlastnosti každého modelu.

## Modely Mistral

V této lekci prozkoumáme 3 různé modely Mistral:  
**Mistral Large**, **Mistral Small** a **Mistral Nemo**.

Každý z těchto modelů je zdarma dostupný na tržišti modelů GitHub. Kód v tomto notebooku bude používat tyto modely k běhu kódu. Zde jsou podrobnosti o použití modelů GitHub k [prototypování s AI modely](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 je aktuálně vlajkový model od Mistral a je navržen pro podnikové využití.

Model je vylepšením původního Mistral Large tím, že nabízí  
- Větší kontextové okno - 128k vs 32k  
- Lepší výkon na matematických a programovacích úlohách - průměrná přesnost 76,9 % vs 60,4 %  
- Zvýšený výkon v mnoha jazycích - jazyky zahrnují: angličtinu, francouzštinu, němčinu, španělštinu, italštinu, portugalštinu, holandštinu, ruštinu, čínštinu, japonštinu, korejštinu, arabštinu a hindštinu.

S těmito funkcemi Mistral Large vyniká v  
- *Retrieval Augmented Generation (RAG)* - díky většímu kontextovému oknu  
- *Volání funkcí* - tento model má nativní podporu volání funkcí, což umožňuje integraci s externími nástroji a API. Tyto volání lze provádět paralelně nebo sekvenčně jedno po druhém.  
- *Generování kódu* - tento model vyniká v generování Pythonu, Javy, TypeScriptu a C++.

### Příklad RAG s použitím Mistral Large 2

V tomto příkladu používáme Mistral Large 2 pro běh RAG vzoru na textovém dokumentu. Otázka je napsána v korejštině a ptá se na aktivity autora před vysokou školou.

Používá Cohere Embeddings Model k vytvoření embeddingů textového dokumentu i otázky. Pro tento vzorek používá balíček faiss v Pythonu jako vektorové úložiště.

Prompt zaslaný modelu Mistral obsahuje jak otázky, tak načtené části textu, které jsou podobné otázce. Model poskytne odpověď v přirozeném jazyce.

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
Mistral Small je další model v rodině modelů Mistral zařazený do kategorie premier/enterprise. Jak název napovídá, jedná se o malý jazykový model (SLM). Výhody použití Mistral Small jsou:  
- Úspora nákladů oproti modelům Mistral LLM jako Mistral Large a NeMo - pokles ceny o 80 %  
- Nízká latence - rychlejší odpověď ve srovnání s modely Mistral LLM  
- Flexibilita - může být nasazen v různých prostředích s menšími nároky na požadované zdroje.

Mistral Small je skvělý pro:  
- Textové úkoly jako shrnutí, analýza sentimentu a překlad  
- Aplikace, kde jsou časté požadavky kvůli své cenové efektivitě  
- Úkoly s nízkou latencí, jako je revize kódu a návrhy kódu

## Porovnání Mistral Small a Mistral Large

Pro zobrazení rozdílů v latenci mezi Mistral Small a Large spusťte následující buňky.

Měli byste vidět rozdíl v době odpovědi mezi 3–5 sekundami. Také si všimněte délek odpovědí a stylu na stejný prompt.

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

Ve srovnání s ostatními dvěma modely diskutovanými v této lekci je Mistral NeMo jediný bezplatný model s licencí Apache2.

Je považován za vylepšení dřívějšího open source LLM od Mistral, Mistral 7B.

Některé další vlastnosti modelu NeMo jsou:

- *Efektivnější tokenizace:* Tento model používá tokenizer Tekken místo častěji používaného tiktoken. To umožňuje lepší výkon v různých jazycích a kódu.

- *Doladění:* Základní model je dostupný k doladění. To umožňuje větší flexibilitu pro případy použití, kde je doladění potřeba.

- *Nativní volání funkcí* - Stejně jako Mistral Large, tento model byl trénován na volání funkcí. To z něj činí jeden z prvních open source modelů s touto schopností.

### Porovnání tokenizérů

V tomto příkladu se podíváme, jak Mistral NeMo zpracovává tokenizaci ve srovnání s Mistral Large.

Oba vzorky berou stejný prompt, ale měli byste vidět, že NeMo vrací méně tokenů než Mistral Large.

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

# Načtěte tokenizér Mistral

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

# Načíst Mistral tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenizovat seznam zpráv
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

# Spočítat počet tokenů
print(len(tokens))
```
  
## Učení zde nekončí, pokračujte na cestě dál

Po dokončení této lekce si prohlédněte naši [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste dál rozšiřovali své znalosti o generativní AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->