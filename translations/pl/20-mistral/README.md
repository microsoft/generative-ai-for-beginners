<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:59:34+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "pl"
}
-->
# Budowanie z modelami Mistral

## Wprowadzenie

W tej lekcji omówimy:  
- Przegląd różnych modeli Mistral  
- Zrozumienie zastosowań i scenariuszy dla każdego modelu  
- Przykłady kodu pokazujące unikalne cechy każdego modelu.

## Modele Mistral

W tej lekcji przyjrzymy się 3 różnym modelom Mistral:  
**Mistral Large**, **Mistral Small** oraz **Mistral Nemo**.

Każdy z tych modeli jest dostępny za darmo na Github Model marketplace. Kod w tym notatniku będzie korzystał z tych modeli do uruchamiania kodu. Więcej informacji o korzystaniu z Github Models do [prototypowania z modelami AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
Mistral Large 2 to obecnie flagowy model Mistral, zaprojektowany z myślą o zastosowaniach korporacyjnych.

Model jest ulepszeniem oryginalnego Mistral Large, oferując:  
- Większe okno kontekstu – 128k vs 32k  
- Lepszą wydajność w zadaniach matematycznych i programistycznych – średnia dokładność 76,9% vs 60,4%  
- Zwiększoną wydajność wielojęzyczną – obsługiwane języki to: angielski, francuski, niemiecki, hiszpański, włoski, portugalski, niderlandzki, rosyjski, chiński, japoński, koreański, arabski i hindi.

Dzięki tym cechom Mistral Large wyróżnia się w:  
- *Retrieval Augmented Generation (RAG)* – dzięki większemu oknu kontekstu  
- *Wywoływaniu funkcji* – model posiada natywne wywoływanie funkcji, co pozwala na integrację z zewnętrznymi narzędziami i API. Wywołania mogą być wykonywane równolegle lub sekwencyjnie.  
- *Generowaniu kodu* – model świetnie radzi sobie z generowaniem kodu w Pythonie, Javie, TypeScript i C++.

### Przykład RAG z użyciem Mistral Large 2

W tym przykładzie używamy Mistral Large 2 do uruchomienia wzorca RAG na dokumencie tekstowym. Pytanie jest napisane po koreańsku i dotyczy aktywności autora przed studiami.

Wykorzystuje model Cohere Embeddings do tworzenia osadzeń dokumentu tekstowego oraz pytania. W tym przykładzie używa pakietu faiss w Pythonie jako magazynu wektorów.

Prompt wysłany do modelu Mistral zawiera zarówno pytania, jak i pobrane fragmenty podobne do pytania. Model następnie generuje odpowiedź w języku naturalnym.

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
Mistral Small to kolejny model z rodziny Mistral, należący do kategorii premier/enterprise. Jak sama nazwa wskazuje, jest to mały model językowy (SLM). Zaletami korzystania z Mistral Small są:  
- Oszczędność kosztów w porównaniu do dużych modeli Mistral, takich jak Mistral Large i NeMo – spadek ceny o 80%  
- Niska latencja – szybsze odpowiedzi w porównaniu do dużych modeli Mistral  
- Elastyczność – może być wdrażany w różnych środowiskach z mniejszymi wymaganiami dotyczącymi zasobów.

Mistral Small sprawdza się świetnie w:  
- Zadaniach tekstowych, takich jak streszczanie, analiza sentymentu i tłumaczenia  
- Aplikacjach, gdzie często wysyłane są zapytania, ze względu na opłacalność kosztową  
- Zadaniach kodowania o niskiej latencji, takich jak przegląd i sugestie kodu

## Porównanie Mistral Small i Mistral Large

Aby zobaczyć różnice w latencji między Mistral Small a Large, uruchom poniższe komórki.

Powinieneś zauważyć różnicę w czasie odpowiedzi wynoszącą od 3 do 5 sekund. Zwróć też uwagę na długość i styl odpowiedzi na ten sam prompt.

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

W porównaniu do pozostałych dwóch modeli omawianych w tej lekcji, Mistral NeMo jest jedynym darmowym modelem na licencji Apache2.

Jest postrzegany jako ulepszenie wcześniejszego otwartoźródłowego modelu LLM od Mistral, Mistral 7B.

Inne cechy modelu NeMo to:

- *Bardziej efektywna tokenizacja:* Model używa tokenizera Tekken zamiast częściej stosowanego tiktoken. Pozwala to na lepszą wydajność w większej liczbie języków i kodu.

- *Dostępność do fine-tuningu:* Model bazowy jest dostępny do fine-tuningu, co daje większą elastyczność w zastosowaniach wymagających dostosowania modelu.

- *Natywne wywoływanie funkcji* – podobnie jak Mistral Large, model został wytrenowany do wywoływania funkcji. To czyni go jednym z pierwszych otwartoźródłowych modeli z taką funkcjonalnością.

### Porównanie tokenizerów

W tym przykładzie zobaczymy, jak Mistral NeMo radzi sobie z tokenizacją w porównaniu do Mistral Large.

Oba przykłady używają tego samego promptu, ale powinieneś zauważyć, że NeMo zwraca mniej tokenów niż Mistral Large.

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

## Nauka nie kończy się tutaj, kontynuuj podróż

Po ukończeniu tej lekcji sprawdź naszą [kolekcję nauki Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę na temat Generative AI!

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.