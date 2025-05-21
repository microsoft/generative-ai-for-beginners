<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:56:25+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "it"
}
-->
# Costruire con i modelli Mistral

## Introduzione

Questa lezione coprirà:
- Esplorare i diversi modelli Mistral
- Comprendere i casi d'uso e gli scenari per ciascun modello
- Campioni di codice mostrano le caratteristiche uniche di ciascun modello.

## I modelli Mistral

In questa lezione, esploreremo 3 diversi modelli Mistral: **Mistral Large**, **Mistral Small** e **Mistral Nemo**.

Ciascuno di questi modelli è disponibile gratuitamente sul marketplace dei modelli di Github. Il codice in questo notebook utilizzerà questi modelli per eseguire il codice. Ecco maggiori dettagli sull'utilizzo dei modelli Github per [prototipare con modelli AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 è attualmente il modello di punta di Mistral ed è progettato per uso aziendale.

Il modello è un aggiornamento rispetto al Mistral Large originale offrendo
- Finestra di contesto più grande - 128k contro 32k
- Migliori prestazioni su compiti di matematica e codifica - 76.9% di precisione media contro 60.4%
- Prestazioni multilingue aumentate - le lingue includono: inglese, francese, tedesco, spagnolo, italiano, portoghese, olandese, russo, cinese, giapponese, coreano, arabo e hindi.

Con queste caratteristiche, Mistral Large eccelle in
- *Generazione aumentata dal recupero (RAG)* - grazie alla finestra di contesto più grande
- *Chiamata di funzione* - questo modello ha la chiamata di funzione nativa che permette l'integrazione con strumenti e API esterni. Queste chiamate possono essere effettuate sia in parallelo che una dopo l'altra in ordine sequenziale.
- *Generazione di codice* - questo modello eccelle nella generazione di Python, Java, TypeScript e C++.

### Esempio di RAG utilizzando Mistral Large 2

In questo esempio, stiamo usando Mistral Large 2 per eseguire un pattern RAG su un documento di testo. La domanda è scritta in coreano e chiede delle attività dell'autore prima del college.

Utilizza il modello di embeddings Cohere per creare embeddings del documento di testo così come della domanda. Per questo esempio, utilizza il pacchetto Python faiss come archivio vettoriale.

Il prompt inviato al modello Mistral include sia le domande che i frammenti recuperati che sono simili alla domanda. Il modello fornisce quindi una risposta in linguaggio naturale.

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
Mistral Small è un altro modello della famiglia di modelli Mistral sotto la categoria premier/enterprise. Come suggerisce il nome, questo modello è un Small Language Model (SLM). I vantaggi dell'utilizzo di Mistral Small sono che è:
- Risparmio sui costi rispetto agli LLM di Mistral come Mistral Large e NeMo - riduzione del prezzo del 80%
- Bassa latenza - risposta più veloce rispetto agli LLM di Mistral
- Flessibile - può essere distribuito su diversi ambienti con meno restrizioni sulle risorse richieste.

Mistral Small è ideale per:
- Compiti basati su testo come riassunto, analisi del sentimento e traduzione.
- Applicazioni dove vengono effettuate richieste frequenti grazie alla sua convenienza economica
- Compiti di codice a bassa latenza come revisione e suggerimenti di codice

## Confronto tra Mistral Small e Mistral Large

Per mostrare le differenze di latenza tra Mistral Small e Large, esegui le celle sottostanti.

Dovresti vedere una differenza nei tempi di risposta tra 3-5 secondi. Nota anche la lunghezza e lo stile delle risposte rispetto allo stesso prompt.

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

Rispetto agli altri due modelli discussi in questa lezione, Mistral NeMo è l'unico modello gratuito con una licenza Apache2.

È visto come un aggiornamento rispetto al precedente LLM open source di Mistral, Mistral 7B.

Alcune altre caratteristiche del modello NeMo sono:

- *Tokenizzazione più efficiente:* Questo modello utilizza il tokenizer Tekken rispetto al più comunemente usato tiktoken. Questo permette migliori prestazioni su più lingue e codice.

- *Fine tuning:* Il modello base è disponibile per il fine tuning. Questo permette maggiore flessibilità per casi d'uso dove potrebbe essere necessario il fine tuning.

- *Chiamata di funzione nativa* - Come Mistral Large, questo modello è stato addestrato sulla chiamata di funzione. Questo lo rende unico essendo uno dei primi modelli open source a farlo.

### Confronto tra tokenizzatori

In questo esempio, vedremo come Mistral NeMo gestisce la tokenizzazione rispetto a Mistral Large.

Entrambi gli esempi prendono lo stesso prompt ma dovresti vedere che NeMo restituisce meno token rispetto a Mistral Large.

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

## L'apprendimento non si ferma qui, continua il viaggio

Dopo aver completato questa lezione, dai un'occhiata alla nostra [collezione di apprendimento sull'AI generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare ad approfondire la tua conoscenza sull'AI generativa!

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per l'accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.