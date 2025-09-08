<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:59:22+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "it"
}
-->
# Costruire con i modelli Mistral

## Introduzione

In questa lezione vedremo:  
- Esplorare i diversi modelli Mistral  
- Comprendere i casi d’uso e gli scenari per ciascun modello  
- Esempi di codice che mostrano le caratteristiche uniche di ogni modello.

## I modelli Mistral

In questa lezione esploreremo 3 diversi modelli Mistral:  
**Mistral Large**, **Mistral Small** e **Mistral Nemo**.

Ognuno di questi modelli è disponibile gratuitamente sul marketplace Github Model. Il codice in questo notebook utilizzerà questi modelli per eseguire il codice. Qui trovi maggiori dettagli sull’uso dei modelli Github per [prototipare con modelli AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
Mistral Large 2 è attualmente il modello di punta di Mistral ed è progettato per uso aziendale.

Il modello rappresenta un aggiornamento rispetto all’originale Mistral Large offrendo:  
- Finestra di contesto più ampia - 128k contro 32k  
- Migliori prestazioni in compiti di matematica e programmazione - 76,9% di accuratezza media contro 60,4%  
- Maggiore performance multilingue - le lingue includono: inglese, francese, tedesco, spagnolo, italiano, portoghese, olandese, russo, cinese, giapponese, coreano, arabo e hindi.

Grazie a queste caratteristiche, Mistral Large eccelle in:  
- *Retrieval Augmented Generation (RAG)* - grazie alla finestra di contesto più ampia  
- *Function Calling* - questo modello supporta nativamente le chiamate di funzione, permettendo l’integrazione con strumenti esterni e API. Queste chiamate possono essere eseguite sia in parallelo che in sequenza.  
- *Generazione di codice* - questo modello è particolarmente efficace nella generazione di codice Python, Java, TypeScript e C++.

### Esempio RAG con Mistral Large 2

In questo esempio utilizziamo Mistral Large 2 per eseguire un pattern RAG su un documento di testo. La domanda è scritta in coreano e riguarda le attività dell’autore prima dell’università.

Si utilizza il modello Cohere Embeddings per creare gli embeddings sia del documento di testo che della domanda. Per questo esempio si usa il pacchetto Python faiss come archivio vettoriale.

Il prompt inviato al modello Mistral include sia la domanda che i frammenti recuperati simili alla domanda. Il modello fornisce quindi una risposta in linguaggio naturale.

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
Mistral Small è un altro modello della famiglia Mistral nella categoria premier/enterprise. Come suggerisce il nome, è un Small Language Model (SLM). I vantaggi di usare Mistral Small sono:  
- Risparmio sui costi rispetto ai LLM Mistral come Mistral Large e NeMo - riduzione del prezzo dell’80%  
- Bassa latenza - risposte più rapide rispetto agli LLM di Mistral  
- Flessibilità - può essere distribuito in diversi ambienti con meno restrizioni sulle risorse richieste.

Mistral Small è ideale per:  
- Compiti basati su testo come riassunti, analisi del sentiment e traduzione.  
- Applicazioni con richieste frequenti grazie al suo costo contenuto  
- Attività di codice a bassa latenza come revisione e suggerimenti di codice

## Confronto tra Mistral Small e Mistral Large

Per mostrare le differenze di latenza tra Mistral Small e Large, esegui le celle qui sotto.

Dovresti notare una differenza nei tempi di risposta tra 3 e 5 secondi. Nota anche la lunghezza e lo stile delle risposte con lo stesso prompt.

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

Rispetto agli altri due modelli trattati in questa lezione, Mistral NeMo è l’unico modello gratuito con licenza Apache2.

È considerato un aggiornamento del precedente LLM open source di Mistral, Mistral 7B.

Alcune altre caratteristiche del modello NeMo sono:

- *Tokenizzazione più efficiente:* questo modello utilizza il tokenizer Tekken invece del più comune tiktoken. Questo permette migliori prestazioni su più lingue e codice.

- *Finetuning:* il modello base è disponibile per il finetuning, offrendo maggiore flessibilità per casi d’uso che lo richiedono.

- *Native Function Calling* - Come Mistral Large, anche questo modello è stato addestrato per le chiamate di funzione. Questo lo rende unico come uno dei primi modelli open source a supportare questa funzionalità.

### Confronto tra tokenizer

In questo esempio vedremo come Mistral NeMo gestisce la tokenizzazione rispetto a Mistral Large.

Entrambi gli esempi usano lo stesso prompt, ma noterai che NeMo restituisce meno token rispetto a Mistral Large.

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

## L’apprendimento non finisce qui, continua il viaggio

Dopo aver completato questa lezione, dai un’occhiata alla nostra [collezione di apprendimento Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare le tue conoscenze sull’Intelligenza Artificiale Generativa!

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.