<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:45:15+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "de"
}
-->
# Bauen mit Mistral-Modellen

## Einführung

Diese Lektion behandelt:
- Erkundung der verschiedenen Mistral-Modelle
- Verständnis der Anwendungsfälle und Szenarien für jedes Modell
- Codebeispiele zeigen die einzigartigen Merkmale jedes Modells.

## Die Mistral-Modelle

In dieser Lektion werden wir 3 verschiedene Mistral-Modelle erkunden: **Mistral Large**, **Mistral Small** und **Mistral Nemo**.

Jedes dieser Modelle ist kostenlos auf dem Github Model-Marktplatz verfügbar. Der Code in diesem Notizbuch wird diese Modelle verwenden, um den Code auszuführen. Hier sind weitere Details zur Nutzung von Github-Modellen zum [Prototyping mit KI-Modellen](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 ist derzeit das Flaggschiff-Modell von Mistral und ist für den Unternehmenseinsatz konzipiert.

Das Modell ist ein Upgrade des ursprünglichen Mistral Large und bietet:
- Größeres Kontextfenster - 128k vs 32k
- Bessere Leistung bei Mathematik- und Codierungsaufgaben - 76,9 % durchschnittliche Genauigkeit vs 60,4 %
- Erhöhte mehrsprachige Leistung - Sprachen umfassen: Englisch, Französisch, Deutsch, Spanisch, Italienisch, Portugiesisch, Niederländisch, Russisch, Chinesisch, Japanisch, Koreanisch, Arabisch und Hindi.

Mit diesen Funktionen glänzt Mistral Large bei:
- *Retrieval Augmented Generation (RAG)* - aufgrund des größeren Kontextfensters
- *Funktionsaufrufe* - dieses Modell hat native Funktionsaufrufe, die die Integration mit externen Tools und APIs ermöglichen. Diese Aufrufe können sowohl parallel als auch nacheinander in einer sequenziellen Reihenfolge erfolgen.
- *Code-Generierung* - dieses Modell glänzt bei der Generierung von Python, Java, TypeScript und C++.

### RAG-Beispiel mit Mistral Large 2

In diesem Beispiel verwenden wir Mistral Large 2, um ein RAG-Muster über ein Textdokument auszuführen. Die Frage ist auf Koreanisch geschrieben und fragt nach den Aktivitäten des Autors vor dem Studium.

Es verwendet das Cohere Embeddings Model, um Einbettungen des Textdokuments sowie der Frage zu erstellen. Für dieses Beispiel wird das faiss Python-Paket als Vektorspeicher verwendet.

Der an das Mistral-Modell gesendete Prompt enthält sowohl die Fragen als auch die abgerufenen Abschnitte, die der Frage ähnlich sind. Das Modell liefert dann eine Antwort in natürlicher Sprache.

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

Mistral Small ist ein weiteres Modell in der Mistral-Modellfamilie unter der Kategorie Premier/Enterprise. Wie der Name schon sagt, ist dieses Modell ein kleines Sprachmodell (SLM). Die Vorteile der Verwendung von Mistral Small sind, dass es:
- Kostensparend im Vergleich zu Mistral LLMs wie Mistral Large und NeMo - 80 % Preisreduktion
- Geringe Latenz - schnellere Reaktion im Vergleich zu Mistrals LLMs
- Flexibel - kann in verschiedenen Umgebungen mit weniger Einschränkungen bei den erforderlichen Ressourcen eingesetzt werden.

Mistral Small eignet sich hervorragend für:
- Textbasierte Aufgaben wie Zusammenfassung, Stimmungsanalyse und Übersetzung.
- Anwendungen, bei denen häufig Anfragen gestellt werden, aufgrund seiner Kosteneffizienz
- Aufgaben mit geringer Latenz wie Codeüberprüfung und Codevorschläge

## Vergleich von Mistral Small und Mistral Large

Um Unterschiede in der Latenz zwischen Mistral Small und Large zu zeigen, führen Sie die folgenden Zellen aus.

Sie sollten einen Unterschied in den Antwortzeiten von 3-5 Sekunden sehen. Beachten Sie auch die Antwortlängen und den Stil bei demselben Prompt.

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

Im Vergleich zu den beiden anderen in dieser Lektion besprochenen Modellen ist Mistral NeMo das einzige kostenlose Modell mit einer Apache2-Lizenz.

Es wird als Upgrade des früheren Open-Source-LLM von Mistral, Mistral 7B, betrachtet.

Einige weitere Merkmale des NeMo-Modells sind:

- *Effizientere Tokenisierung:* Dieses Modell verwendet den Tekken-Tokenizer anstelle des häufiger verwendeten tiktoken. Dies ermöglicht eine bessere Leistung bei mehr Sprachen und Code.

- *Feintuning:* Das Basismodell ist für Feintuning verfügbar. Dies ermöglicht mehr Flexibilität für Anwendungsfälle, bei denen Feintuning erforderlich sein könnte.

- *Native Funktionsaufrufe* - Wie Mistral Large wurde dieses Modell auf Funktionsaufrufe trainiert. Dies macht es einzigartig als eines der ersten Open-Source-Modelle, die dies tun.

### Vergleich der Tokenizer

In diesem Beispiel werden wir uns ansehen, wie Mistral NeMo die Tokenisierung im Vergleich zu Mistral Large handhabt.

Beide Beispiele verwenden denselben Prompt, aber Sie sollten sehen, dass NeMo weniger Tokens zurückgibt als Mistral Large.

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

## Lernen hört hier nicht auf, setze die Reise fort

Nach Abschluss dieser Lektion schauen Sie sich unsere [Generative AI Learning Collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über Generative KI weiter zu vertiefen!

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.