# Costruire con i modelli Mistral 

## Introduzione 

Questa lezione coprirà: 
- Esplorare i diversi modelli Mistral 
- Comprendere i casi d'uso e gli scenari per ciascun modello 
- Esplorare esempi di codice che mostrano le caratteristiche uniche di ogni modello. 

## I modelli Mistral 

In questa lezione, esploreremo 3 diversi modelli Mistral: 
**Mistral Large**, **Mistral Small** e **Mistral Nemo**. 

Ognuno di questi modelli è disponibile gratuitamente su [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Il codice in questo notebook utilizzerà questi modelli per eseguire il codice.

> **Nota:** GitHub Models sarà dismesso alla fine di luglio 2026. Ecco maggiori dettagli sull'utilizzo di [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) per prototipare con modelli AI. 


## Mistral Large 2 (2407)
Mistral Large 2 è attualmente il modello di punta di Mistral ed è progettato per l'uso aziendale. 

Il modello è un aggiornamento rispetto al Mistral Large originale offrendo 
- Finestra di contesto più ampia - 128k vs 32k 
- Migliore performance in compiti di matematica e programmazione - precisione media del 76,9% vs 60,4% 
- Performance multilingue aumentate - le lingue includono: inglese, francese, tedesco, spagnolo, italiano, portoghese, olandese, russo, cinese, giapponese, coreano, arabo e hindi.

Con queste caratteristiche, Mistral Large eccelle in 
- *Generazione aumentata da recupero (RAG)* - grazie alla finestra di contesto più ampia
- *Chiamata di Funzioni* - questo modello ha chiamata di funzione nativa che permette l'integrazione con strumenti e API esterne. Queste chiamate possono essere eseguite sia in parallelo che una dopo l'altra in ordine sequenziale. 
- *Generazione di codice* - questo modello eccelle nella generazione di Python, Java, TypeScript e C++. 

### Esempio RAG usando Mistral Large 2 

In questo esempio, stiamo usando Mistral Large 2 per eseguire un pattern RAG su un documento di testo. La domanda è scritta in coreano e chiede delle attività dell'autore prima del college. 

Usa il modello di embedding Cohere per creare embedding sia del documento di testo sia della domanda. Per questo esempio, utilizza il pacchetto Python faiss come archivio vettoriale. 

Il prompt inviato al modello Mistral include sia le domande che i frammenti recuperati simili alla domanda. Il modello fornisce quindi una risposta in linguaggio naturale. 

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

# Ottieni questi dalla pagina "Panoramica" del tuo progetto Microsoft Foundry
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # distanza, indice
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
Mistral Small è un altro modello della famiglia Mistral nella categoria premier/enterprise. Come suggerisce il nome, questo modello è un Small Language Model (SLM). I vantaggi di usare Mistral Small sono: 
- Risparmio sui costi rispetto ai LLM Mistral come Mistral Large e NeMo - riduzione del prezzo dell'80%
- Bassa latenza - risposta più veloce rispetto ai LLM di Mistral
- Flessibile - può essere distribuito in diversi ambienti con meno restrizioni sulle risorse richieste. 


Mistral Small è ottimo per: 
- Compiti basati su testo come riepilogo, analisi del sentimento e traduzione. 
- Applicazioni con richieste frequenti grazie alla sua convenienza 
- Compiti di codice a bassa latenza come revisione e suggerimenti di codice 

## Confronto tra Mistral Small e Mistral Large 

Per mostrare le differenze di latenza tra Mistral Small e Large, esegui le celle sottostanti. 

Dovresti vedere una differenza nei tempi di risposta tra 3-5 secondi. Nota anche la lunghezza e lo stile della risposta sullo stesso prompt.  

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

Rispetto agli altri due modelli discussi in questa lezione, Mistral NeMo è l'unico modello gratuito con licenza Apache2. 

È visto come un aggiornamento del precedente LLM open source di Mistral, Mistral 7B. 

Alcune altre caratteristiche del modello NeMo sono: 

- *Tokenizzazione più efficiente:* Questo modello utilizza il tokenizer Tekken al posto del più comunemente usato tiktoken. Questo consente migliori performance su più lingue e codice. 

- *Finetuning:* Il modello base è disponibile per il finetuning. Questo permette maggiore flessibilità per casi d'uso che ne richiedono l'adattamento. 

- *Chiamata di Funzione Nativa* - Come Mistral Large, questo modello è stato addestrato alla chiamata di funzioni. Questo lo rende unico come uno dei primi modelli open source a farlo. 


### Confronto tra tokenizer 

In questo esempio, esamineremo come Mistral NeMo gestisce la tokenizzazione rispetto a Mistral Large. 

Entrambi gli esempi usano lo stesso prompt ma dovresti vedere che NeMo restituisce meno token rispetto a Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Importa i pacchetti necessari:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Carica il tokenizer di Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenizza una lista di messaggi
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

# Conta il numero di token
print(len(tokens))
```

```python
# Importa i pacchetti necessari:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Carica il tokenizer di Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenizza una lista di messaggi
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

# Conta il numero di token
print(len(tokens))
```

## L'apprendimento non si ferma qui, continua il viaggio

Dopo aver completato questa lezione, consulta la nostra [collezione di apprendimento sull'IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare le tue conoscenze sull'IA Generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->