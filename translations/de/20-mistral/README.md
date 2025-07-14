<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:55:31+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "de"
}
-->
# Arbeiten mit Mistral-Modellen

## Einführung

Diese Lektion behandelt:  
- Die verschiedenen Mistral-Modelle kennenlernen  
- Anwendungsfälle und Szenarien für jedes Modell verstehen  
- Codebeispiele, die die besonderen Merkmale der einzelnen Modelle zeigen.

## Die Mistral-Modelle

In dieser Lektion werden wir 3 verschiedene Mistral-Modelle vorstellen:  
**Mistral Large**, **Mistral Small** und **Mistral Nemo**.

Alle diese Modelle sind kostenlos im Github Model Marketplace verfügbar. Der Code in diesem Notebook verwendet diese Modelle zur Ausführung. Hier finden Sie weitere Informationen zur Nutzung von Github Models zum [Prototyping mit KI-Modellen](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
Mistral Large 2 ist derzeit das Flaggschiff-Modell von Mistral und wurde für den Unternehmenseinsatz entwickelt.

Das Modell ist ein Upgrade des ursprünglichen Mistral Large und bietet:  
- Größeres Kontextfenster – 128k statt 32k  
- Bessere Leistung bei Mathematik- und Programmieraufgaben – 76,9 % durchschnittliche Genauigkeit statt 60,4 %  
- Verbesserte mehrsprachige Leistung – Sprachen umfassen: Englisch, Französisch, Deutsch, Spanisch, Italienisch, Portugiesisch, Niederländisch, Russisch, Chinesisch, Japanisch, Koreanisch, Arabisch und Hindi.

Mit diesen Eigenschaften ist Mistral Large besonders geeignet für:  
- *Retrieval Augmented Generation (RAG)* – dank des größeren Kontextfensters  
- *Function Calling* – dieses Modell unterstützt native Funktionsaufrufe, die eine Integration mit externen Tools und APIs ermöglichen. Diese Aufrufe können sowohl parallel als auch nacheinander in einer Reihenfolge ausgeführt werden.  
- *Code-Generierung* – das Modell ist besonders stark bei der Generierung von Python-, Java-, TypeScript- und C++-Code.

### RAG-Beispiel mit Mistral Large 2

In diesem Beispiel verwenden wir Mistral Large 2, um ein RAG-Muster auf ein Textdokument anzuwenden. Die Frage ist auf Koreanisch geschrieben und erkundigt sich nach den Aktivitäten des Autors vor dem Studium.

Es wird das Cohere Embeddings Model verwendet, um Einbettungen des Textdokuments sowie der Frage zu erstellen. Für dieses Beispiel kommt das Python-Paket faiss als Vektorspeicher zum Einsatz.

Der an das Mistral-Modell gesendete Prompt enthält sowohl die Fragen als auch die abgerufenen Textabschnitte, die der Frage ähnlich sind. Das Modell liefert dann eine Antwort in natürlicher Sprache.

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
Mistral Small ist ein weiteres Modell aus der Mistral-Familie im Bereich Premier/Enterprise. Wie der Name schon sagt, handelt es sich um ein Small Language Model (SLM). Die Vorteile von Mistral Small sind:  
- Kosteneinsparungen im Vergleich zu Mistral LLMs wie Mistral Large und NeMo – 80 % günstigere Preise  
- Geringe Latenz – schnellere Antwortzeiten im Vergleich zu Mistral LLMs  
- Flexibilität – kann in verschiedenen Umgebungen mit weniger Einschränkungen bei den benötigten Ressourcen eingesetzt werden.

Mistral Small eignet sich besonders für:  
- Textbasierte Aufgaben wie Zusammenfassungen, Sentiment-Analysen und Übersetzungen  
- Anwendungen mit häufigen Anfragen aufgrund der Kosteneffizienz  
- Codeaufgaben mit niedriger Latenz wie Code-Reviews und Vorschläge

## Vergleich von Mistral Small und Mistral Large

Um die Unterschiede in der Latenz zwischen Mistral Small und Large zu zeigen, führen Sie die folgenden Zellen aus.

Sie sollten eine Differenz in den Antwortzeiten von 3-5 Sekunden feststellen. Beachten Sie auch die Unterschiede in der Antwortlänge und im Stil bei demselben Prompt.

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

Im Vergleich zu den anderen beiden in dieser Lektion besprochenen Modellen ist Mistral NeMo das einzige kostenlose Modell mit Apache2-Lizenz.

Es gilt als Upgrade des früheren Open-Source-LLM von Mistral, Mistral 7B.

Einige weitere Merkmale des NeMo-Modells sind:

- *Effizientere Tokenisierung:* Dieses Modell verwendet den Tekken-Tokenizer anstelle des häufiger genutzten tiktoken. Dadurch wird eine bessere Leistung bei mehr Sprachen und Code erreicht.

- *Feinabstimmung:* Das Basismodell steht für Feinabstimmungen zur Verfügung. Das ermöglicht mehr Flexibilität für Anwendungsfälle, in denen eine Feinabstimmung erforderlich ist.

- *Native Function Calling* – Wie Mistral Large wurde dieses Modell auf Funktionsaufrufe trainiert. Das macht es einzigartig als eines der ersten Open-Source-Modelle mit dieser Fähigkeit.

### Vergleich der Tokenizer

In diesem Beispiel sehen wir uns an, wie Mistral NeMo die Tokenisierung im Vergleich zu Mistral Large handhabt.

Beide Beispiele verwenden denselben Prompt, aber Sie werden feststellen, dass NeMo weniger Tokens zurückgibt als Mistral Large.

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

## Lernen hört hier nicht auf – setze deine Reise fort

Nach Abschluss dieser Lektion empfehlen wir, unsere [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) zu besuchen, um dein Wissen im Bereich Generative KI weiter auszubauen!

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.