# Budowanie z modelami Mistral

## Wprowadzenie

Ta lekcja obejmie:
- Poznanie różnych modeli Mistral
- Zrozumienie zastosowań i scenariuszy dla każdego modelu
- Przegląd przykładów kodu pokazujących unikalne cechy każdego modelu.

## Modele Mistral

W tej lekcji przyjrzymy się 3 różnym modelom Mistral:
**Mistral Large**, **Mistral Small** oraz **Mistral Nemo**.

Każdy z tych modeli jest dostępny bezpłatnie na rynku modeli GitHub. Kod w tym notatniku będzie korzystał z tych modeli do uruchamiania kodu. Oto więcej szczegółów o korzystaniu z modeli GitHub do [prototypowania z modelami AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).


## Mistral Large 2 (2407)
Mistral Large 2 jest obecnie flagowym modelem firmy Mistral i jest przeznaczony do użytku korporacyjnego.

Model jest ulepszeniem oryginalnego Mistral Large oferując:
- Większe okno kontekstu - 128k vs 32k
- Lepszą wydajność w zadaniach matematycznych i kodowaniu - 76,9% średniej dokładności vs 60,4%
- Zwiększoną wielojęzyczność - języki obejmują: angielski, francuski, niemiecki, hiszpański, włoski, portugalski, niderlandzki, rosyjski, chiński, japoński, koreański, arabski i hindi.

Dzięki tym cechom Mistral Large wyróżnia się w:
- *Generowaniu z uzupełnieniem przez wyszukiwanie (RAG)* - ze względu na większe okno kontekstu
- *Wywoływaniu funkcji* - ten model posiada natywne wywoływanie funkcji, co pozwala na integrację z narzędziami zewnętrznymi i API. Wywołania mogą być wykonywane równolegle lub jedno po drugim w kolejności sekwencyjnej.
- *Generowaniu kodu* - model ten świetnie radzi sobie z generowaniem w Pythonie, Javie, TypeScript i C++.

### Przykład RAG z użyciem Mistral Large 2

W tym przykładzie używamy Mistral Large 2 do przeprowadzenia wzorca RAG na dokumencie tekstowym. Pytanie jest napisane po koreańsku i dotyczy działań autora przed studiami.

Używa modelu embedingów Cohere do tworzenia reprezentacji tekstu oraz pytania. W tym przykładzie używa pakietu Python faiss jako sklepu wektorowego.

Podpowiedź wysłana do modelu Mistral zawiera zarówno pytania, jak i pobrane fragmenty podobne do pytania. Model następnie udziela odpowiedzi w języku naturalnym.

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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # odległość, indeks
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
Mistral Small to kolejny model w rodzinie Mistral w kategorii premier/enterprise. Jak sama nazwa wskazuje, jest to Mały Model Językowy (SLM). Zalety korzystania z Mistral Small to:
- Oszczędność kosztów w porównaniu do dużych modeli Mistral, takich jak Mistral Large i NeMo - spadek ceny o 80%
- Niskie opóźnienia - szybsza odpowiedź w porównaniu do dużych modeli Mistral
- Elastyczność - może być wdrażany w różnych środowiskach z mniejszymi ograniczeniami zasobów.

Mistral Small jest świetny do:
- Zadań tekstowych takich jak streszczanie, analiza sentymentu i tłumaczenie.
- Aplikacji, w których realizowane są częste zapytania ze względu na opłacalność
- Zadań kodowania o niskim opóźnieniu takich jak przegląd i sugestie kodu

## Porównanie Mistral Small i Mistral Large

Aby zobaczyć różnice w opóźnieniach między Mistral Small a Large, uruchom poniższe komórki.

Powinieneś zobaczyć różnicę w czasie odpowiedzi od 3 do 5 sekund. Zwróć też uwagę na długość i styl odpowiedzi dla tego samego promptu.

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

W porównaniu do dwóch pozostałych modeli opisywanych w tej lekcji, Mistral NeMo jest jedynym darmowym modelem na licencji Apache2.

Jest uważany za ulepszenie wcześniejszego otwartoźródłowego LLM od Mistral, Mistral 7B.

Inne cechy modelu NeMo to:

- *Bardziej efektywna tokenizacja:* Model używa tokenizer Tekken zamiast bardziej powszechnie stosowanego tiktoken. Pozwala to na lepszą wydajność w różnych językach i kodach.

- *Dostępność do fine-tuningu:* Model bazowy jest dostępny do fine-tuningu. Zapewnia to większą elastyczność w przypadkach użycia, gdzie fine-tuning jest potrzebny.

- *Natywne wywoływanie funkcji* - Podobnie jak Mistral Large, ten model był trenowany na wywoływaniu funkcji. To czyni go wyjątkowym jako jeden z pierwszych otwartoźródłowych modeli z taką funkcjonalnością.

### Porównanie tokenizerów

W tym przykładzie zobaczymy, jak Mistral NeMo radzi sobie z tokenizacją w porównaniu do Mistral Large.

Oba przykłady używają tego samego promptu, ale powinieneś zauważyć, że NeMo zwraca mniej tokenów niż Mistral Large.

```bash
pip install mistral-common
```

```python 
# Importuj potrzebne pakiety:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Załaduj tokenizer Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenizuj listę wiadomości
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

# Policz liczbę tokenów
print(len(tokens))
```

```python
# Importuj potrzebne pakiety:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Załaduj tokenizer Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenizuj listę wiadomości
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

# Policz liczbę tokenów
print(len(tokens))
```

## Nauka tutaj się nie kończy, kontynuuj swoją podróż

Po ukończeniu tej lekcji, zapoznaj się z naszą [kolekcją nauki o Generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę o Generatywnej AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrzeczenie się odpowiedzialności**:  
Niniejszy dokument został przetłumaczony za pomocą automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego ojczystym języku powinien być traktowany jako źródło autorytatywne. W przypadku informacji istotnych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->