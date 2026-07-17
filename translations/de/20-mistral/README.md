# Arbeiten mit Mistral-Modellen

## Einführung

Diese Lektion behandelt:
- Erkundung der verschiedenen Mistral-Modelle
- Verständnis der Anwendungsfälle und Szenarien für jedes Modell
- Untersuchung von Codebeispielen, die die einzigartigen Funktionen jedes Modells zeigen.

## Die Mistral-Modelle

In dieser Lektion werden wir 3 verschiedene Mistral-Modelle untersuchen:
**Mistral Large**, **Mistral Small** und **Mistral Nemo**.

Jedes dieser Modelle ist kostenlos auf [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) verfügbar. Der Code in diesem Notebook verwendet diese Modelle zum Ausführen des Codes.

> **Hinweis:** GitHub Models wird Ende Juli 2026 eingestellt. Hier finden Sie weitere Informationen zur Nutzung von [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) zum Prototyping mit KI-Modellen.


## Mistral Large 2 (2407)
Mistral Large 2 ist derzeit das Flaggschiff-Modell von Mistral und für den Unternehmenseinsatz konzipiert.

Das Modell ist ein Upgrade des ursprünglichen Mistral Large und bietet
- Größeres Kontextfenster - 128k statt 32k
- Bessere Leistung bei Mathe- und Programmieraufgaben - 76,9 % durchschnittliche Genauigkeit vs. 60,4 %
- Verbesserte mehrsprachige Leistung - Sprachen umfassen: Englisch, Französisch, Deutsch, Spanisch, Italienisch, Portugiesisch, Niederländisch, Russisch, Chinesisch, Japanisch, Koreanisch, Arabisch und Hindi.

Mit diesen Eigenschaften glänzt Mistral Large bei
- *Retrieval Augmented Generation (RAG)* - dank des größeren Kontextfensters
- *Function Calling* - dieses Modell verfügt über native Funktionsaufrufe, die die Integration mit externen Tools und APIs ermöglichen. Diese Aufrufe können sowohl parallel als auch sequenziell ausgeführt werden.
- *Codegenerierung* - dieses Modell ist hervorragend in der Generierung von Python, Java, TypeScript und C++.

### RAG-Beispiel mit Mistral Large 2

In diesem Beispiel verwenden wir Mistral Large 2, um ein RAG-Muster über ein Textdokument auszuführen. Die Frage ist auf Koreanisch verfasst und fragt nach den Aktivitäten des Autors vor dem Studium.

Es verwendet das Cohere Embeddings Model, um Einbettungen des Textdokuments sowie der Frage zu erstellen. Für dieses Beispiel wird das Python-Paket faiss als Vektorspeicher verwendet.

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

# Holen Sie diese von der "Übersicht"-Seite Ihres Microsoft Foundry-Projekts
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
Mistral Small ist ein weiteres Modell aus der Mistral-Familie im Premier/Enterprise-Bereich. Wie der Name schon sagt, handelt es sich hierbei um ein Small Language Model (SLM). Die Vorteile von Mistral Small sind:
- Kostenersparnis im Vergleich zu Mistral LLMs wie Mistral Large und NeMo - 80 % Preisersparnis
- Niedrige Latenz - schnellere Reaktionszeit im Vergleich zu Mistrals LLMs
- Flexibel - kann in unterschiedlichen Umgebungen mit weniger Einschränkungen bei den benötigten Ressourcen eingesetzt werden.


Mistral Small eignet sich hervorragend für:
- Textbasierte Aufgaben wie Zusammenfassung, Sentiment-Analyse und Übersetzung.
- Anwendungen, bei denen häufig Anfragen gestellt werden, aufgrund seiner Kosteneffizienz
- Niedriglatenz-Codeaufgaben wie Codeüberprüfung und Codevorschläge

## Vergleich Mistral Small und Mistral Large

Um die Latenzunterschiede zwischen Mistral Small und Large zu zeigen, führen Sie die folgenden Zellen aus.

Sie sollten einen Unterschied in den Antwortzeiten von 3-5 Sekunden sehen. Beachten Sie auch die Antwortenlängen und den Stil beim gleichen Prompt.

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

Im Vergleich zu den anderen zwei in dieser Lektion behandelten Modellen ist Mistral NeMo das einzige kostenlose Modell mit Apache2-Lizenz.

Es wird als Upgrade des früheren Open-Source-LLM von Mistral, Mistral 7B, angesehen.

Einige weitere Merkmale des NeMo-Modells sind:

- *Effizientere Tokenisierung:* Dieses Modell verwendet den Tekken-Tokenizer anstelle des häufiger genutzten tiktoken. Dies ermöglicht eine bessere Leistung über mehr Sprachen und Code.

- *Feinabstimmung:* Das Basismodell ist für Feinabstimmungen verfügbar. Dies ermöglicht mehr Flexibilität für Anwendungsfälle, bei denen eine Feinabstimmung notwendig sein kann.

- *Native Function Calling* - Wie Mistral Large wurde dieses Modell auf Funktionsaufruf trainiert. Dies macht es einzigartig, als eines der ersten Open-Source-Modelle diese Fähigkeit zu besitzen.


### Vergleich der Tokenizer

In diesem Beispiel betrachten wir, wie Mistral NeMo die Tokenisierung im Vergleich zu Mistral Large handhabt.

Beide Beispiele verwenden denselben Prompt, aber Sie sollten feststellen, dass NeMo weniger Tokens als Mistral Large zurückgibt.

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

# Lade Mistral Tokenizer

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

# Die Anzahl der Tokens zählen
print(len(tokens))
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

Nach Abschluss dieser Lektion sehen Sie sich unsere [Generative AI Learning Collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über Generative KI weiter auszubauen!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->