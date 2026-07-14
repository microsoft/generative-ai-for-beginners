# Budowanie z modelami Mistral 

## Wprowadzenie 

Ta lekcja obejmie: 
- Eksplorację różnych modeli Mistral 
- Zrozumienie zastosowań i scenariuszy dla każdego modelu 
- Przegląd przykładów kodu pokazujących unikalne cechy każdego modelu. 

## Modele Mistral 

W tej lekcji zapoznamy się z 3 różnymi modelami Mistral: 
**Mistral Large**, **Mistral Small** oraz **Mistral Nemo**. 

Każdy z tych modeli jest dostępny za darmo na [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Kod w tym notatniku będzie korzystał z tych modeli do uruchamiania kodu.

> **Uwaga:** GitHub Models zostanie wycofany pod koniec lipca 2026. Tutaj znajdziesz więcej informacji o korzystaniu z [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) do prototypowania modeli AI. 


## Mistral Large 2 (2407)
Mistral Large 2 to obecnie flagowy model Mistral zaprojektowany do użytku korporacyjnego. 

Model jest ulepszeniem oryginalnego Mistral Large, oferując: 
- Większe okno kontekstu - 128k kontra 32k 
- Lepszą wydajność w zadaniach związanych z matematyką i kodowaniem - średnia dokładność 76,9% vs 60,4% 
- Zwiększoną wielojęzyczną wydajność - języki to: angielski, francuski, niemiecki, hiszpański, włoski, portugalski, niderlandzki, rosyjski, chiński, japoński, koreański, arabski i hindi.

Dzięki tym cechom Mistral Large wyróżnia się w 
- *Generowaniu Wzbogaconym o Pozyskiwanie Informacji (RAG)* - dzięki większemu oknu kontekstu
- *Wywoływaniu funkcji* - model posiada natywne wywoływanie funkcji, co umożliwia integrację z zewnętrznymi narzędziami i interfejsami API. Wywołania te mogą być wykonywane równolegle lub jedno po drugim w kolejności sekwencyjnej. 
- *Generowaniu kodu* - model wyróżnia się generowaniem kodu w Pythonie, Javie, TypeScript i C++. 

### Przykład RAG z użyciem Mistral Large 2 

W tym przykładzie używamy Mistral Large 2 do realizacji wzorca RAG na dokumencie tekstowym. Pytanie jest napisane po koreańsku i dotyczy działań autora przed studiami. 

Do tworzenia embeddingów tekstu dokumentu oraz pytania używany jest Cohere Embeddings Model. W tym przykładzie używa się pakietu faiss Pythona jako magazynu wektorowego. 

Polecenie wysyłane do modelu Mistral zawiera zarówno pytania, jak i pobrane fragmenty podobne do pytania. Model następnie generuje odpowiedź w języku naturalnym. 

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

# Pobierz je ze strony "Przegląd" projektu Microsoft Foundry
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
Mistral Small to kolejny model z rodziny modeli Mistral w kategorii premier/korporacyjnej. Jak sama nazwa wskazuje, jest to Mały Model Językowy (SLM). Zalety korzystania z Mistral Small to: 
- Oszczędność kosztów w porównaniu do dużych modeli LLM Mistral jak Mistral Large i NeMo - spadek ceny o 80%
- Niskie opóźnienia - szybsza reakcja w porównaniu do dużych modeli Mistral
- Elastyczność - może być wdrażany w różnych środowiskach z mniejszymi ograniczeniami dotyczącymi wymaganych zasobów. 


Mistral Small świetnie nadaje się do: 
- Zadań opartych na tekście takich jak streszczanie, analiza sentymentu i tłumaczenie. 
- Aplikacji, w których często są wysyłane zapytania ze względu na efektywność kosztową 
- Zadań kodowych o niskich opóźnieniach, takich jak przegląd i sugestie kodu 

## Porównanie Mistral Small i Mistral Large 

Aby zobaczyć różnice w opóźnieniach między Mistral Small i Large, uruchom poniższe komórki. 

Powinieneś zobaczyć różnicę w czasie odpowiedzi od 3 do 5 sekund. Zwróć także uwagę na długość i styl odpowiedzi przy tym samym poleceniu.  

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

W porównaniu do dwóch pozostałych modeli omówionych w tej lekcji, Mistral NeMo jest jedynym modelem darmowym z licencją Apache2. 

Jest postrzegany jako ulepszenie wcześniejszego modelu open source Mistral 7B. 

Niektóre inne cechy modelu NeMo to: 

- *Wydajniejsza tokenizacja:* Ten model korzysta z tokenizatora Tekken zamiast powszechnie używanego tiktoken. Pozwala to na lepszą wydajność w przypadku większej liczby języków i kodu. 

- *Dostrajanie:* Model bazowy jest dostępny do dostrajania. Daje to większą elastyczność zastosowań, gdzie dostrajanie może być potrzebne. 

- *Natywne wywoływanie funkcji* - podobnie jak Mistral Large, model ten został wytrenowany pod kątem wywoływania funkcji. Czyni go to wyjątkowym jako jeden z pierwszych otwartych modeli, które to oferują. 


### Porównanie tokenizatorów 

W tym przykładzie przeanalizujemy, jak Mistral NeMo radzi sobie z tokenizacją w porównaniu do Mistral Large. 

Oba przykłady używają tego samego polecenia, ale powinno być widać, że NeMo zwraca mniej tokenów niż Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Zaimportuj potrzebne pakiety:
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
# Zaimportuj potrzebne pakiety:
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

## Nauka na tym się nie kończy, kontynuuj podróż

Po zakończeniu tej lekcji sprawdź naszą [kolekcję nauki o Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej podnosić swoje umiejętności w generatywnej sztucznej inteligencji!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->