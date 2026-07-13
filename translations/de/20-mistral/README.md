# Arbeiten mit Mistral-Modellen 

## Einführung 

Diese Lektion behandelt: 
- Erkundung der verschiedenen Mistral-Modelle 
- Verständnis der Anwendungsfälle und Szenarien für jedes Modell 
- Untersuchung von Codebeispielen, die die einzigartigen Funktionen jedes Modells zeigen. 

## Die Mistral-Modelle 

In dieser Lektion werden wir 3 verschiedene Mistral-Modelle erkunden: 
**Mistral Large**, **Mistral Small** und **Mistral Nemo**. 

Jedes dieser Modelle ist kostenlos auf [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) verfügbar. Der Code in diesem Notebook verwendet diese Modelle, um den Code auszuführen.

> **Hinweis:** GitHub Models wird Ende Juli 2026 eingestellt. Hier finden Sie weitere Informationen zur Nutzung von [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) zum Prototyping mit KI-Modellen. 


## Mistral Large 2 (2407)
Mistral Large 2 ist derzeit das Flaggschiffmodell von Mistral und für den Unternehmenseinsatz konzipiert. 

Das Modell ist ein Upgrade des ursprünglichen Mistral Large und bietet 
-  Größeres Kontextfenster - 128k vs 32k 
-  Bessere Leistung bei Mathematik- und Programmieraufgaben - 76,9 % durchschnittliche Genauigkeit vs. 60,4 % 
-  Verbesserte mehrsprachige Leistung - Sprachen: Englisch, Französisch, Deutsch, Spanisch, Italienisch, Portugiesisch, Niederländisch, Russisch, Chinesisch, Japanisch, Koreanisch, Arabisch und Hindi.

Mit diesen Funktionen glänzt Mistral Large bei 
- *Retrieval Augmented Generation (RAG)* - aufgrund des größeren Kontextfensters
- *Funktion Aufruf* - dieses Modell besitzt native Funktionsaufrufe, die die Integration mit externen Tools und APIs ermöglichen. Diese Aufrufe können sowohl parallel als auch nacheinander sequentiell durchgeführt werden. 
- *Code-Generierung* - dieses Modell ist besonders gut in der Generierung von Python, Java, TypeScript und C++ Code. 

### RAG-Beispiel mit Mistral Large 2 

In diesem Beispiel verwenden wir Mistral Large 2, um ein RAG-Muster über ein Textdokument auszuführen. Die Frage ist auf Koreanisch geschrieben und fragt nach den Aktivitäten des Autors vor dem College. 

Es verwendet das Cohere Embeddings Modell, um Einbettungen des Textdokuments sowie der Frage zu erstellen. Für dieses Beispiel wird das Python-Paket faiss als Vektorspeicher verwendet. 

Die Eingabeaufforderung an das Mistral-Modell enthält sowohl die Fragen als auch die abgerufenen Textabschnitte, die der Frage ähnlich sind. Das Modell gibt dann eine Antwort in natürlicher Sprache zurück. 

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

# Holen Sie diese von der "Überblick"-Seite Ihres Microsoft Foundry-Projekts
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # Abstand, Index
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
Mistral Small ist ein weiteres Modell aus der Mistral-Familie im Premium-/Enterprise-Bereich. Wie der Name schon sagt, handelt es sich bei diesem Modell um ein kleines Sprachmodell (SLM). Die Vorteile von Mistral Small sind: 
- Kosteneinsparungen im Vergleich zu Mistral LLMs wie Mistral Large und NeMo - 80% Preisreduktion
- Niedrige Latenz - schnellere Reaktionszeiten im Vergleich zu Mistrals LLMs
- Flexibel - kann in verschiedenen Umgebungen mit weniger Einschränkungen bei den benötigten Ressourcen eingesetzt werden. 


Mistral Small ist ideal für: 
- Textbasierte Aufgaben wie Zusammenfassung, Sentiment-Analyse und Übersetzung. 
- Anwendungen mit häufigen Anfragen aufgrund der Kostenersparnis 
- Latenzarme Programmieraufgaben wie Code-Review und Code-Vorschläge 

## Vergleich von Mistral Small und Mistral Large 

Um Unterschiede in der Latenz zwischen Mistral Small und Large zu demonstrieren, führen Sie die folgenden Zellen aus. 

Sie sollten eine Differenz in den Antwortzeiten von 3-5 Sekunden sehen. Beachten Sie auch die Antwortlängen und den Stil bei demselben Prompt.  

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

Im Vergleich zu den anderen beiden in dieser Lektion besprochenen Modellen ist Mistral NeMo das einzige kostenlose Modell mit einer Apache2-Lizenz. 

Es wird als Upgrade des früheren Open-Source-LLM von Mistral, Mistral 7B, angesehen. 

Einige weitere Merkmale des NeMo-Modells sind: 

- *Effizientere Tokenisierung:* Dieses Modell verwendet den Tekken-Tokenizer anstelle des häufiger verwendeten tiktoken. Dies ermöglicht bessere Leistung bei mehr Sprachen und Code. 

- *Finetuning:* Das Basismodell ist für Finetuning verfügbar. Dies bietet mehr Flexibilität für Anwendungsfälle, in denen Finetuning erforderlich ist. 

- *Native Funktionsaufrufe* - Wie Mistral Large wurde dieses Modell auf Funktionsaufrufe trainiert. Das macht es einzigartig als eines der ersten Open-Source-Modelle mit dieser Fähigkeit. 


### Vergleich der Tokenizer 

In diesem Beispiel sehen wir uns an, wie Mistral NeMo die Tokenisierung im Vergleich zu Mistral Large handhabt. 

Beide Beispiele verwenden denselben Prompt, aber Sie sollten sehen, dass NeMo weniger Tokens als Mistral Large zurückgibt. 

```bash
pip install mistral-common
```

```python 
# Benötigte Pakete importieren:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral-Tokenizer laden

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Eine Liste von Nachrichten tokenisieren
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

# Die Anzahl der Token zählen
print(len(tokens))
```

```python
# Notwendige Pakete importieren:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral-Tokenizer laden

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Eine Liste von Nachrichten tokenisieren
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

# Die Anzahl der Tokens zählen
print(len(tokens))
```

## Lernen hört hier nicht auf, setze die Reise fort

Nach Abschluss dieser Lektion schauen Sie sich unsere [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über Generative KI weiter zu vertiefen!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->