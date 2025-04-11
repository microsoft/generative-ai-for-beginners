# Budowanie z modelami Mistral

## Wprowadzenie

Ta lekcja obejmie:

- Odkrywanie różnych modeli Mistral
- Zrozumienie przypadków użycia i scenariuszy dla każdego modelu
- Przykłady kodu pokazujące unikalne cechy każdego modelu.

## Modele Mistral

W tej lekcji omówimy 3 różne modele Mistral:
**Mistral Large**, **Mistral Small** i **Mistral Nemo**.

Każdy z tych modeli jest dostępny za darmo na rynku modeli Github. Kod w tym notatniku będzie używał tych modeli do uruchomienia kodu. Oto więcej szczegółów na temat używania modeli Github do [prototypowania z modelami AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 jest obecnie flagowym modelem firmy Mistral i jest przeznaczony do użytku korporacyjnego.

Model ten jest ulepszeniem oryginalnego Mistral Large, oferując

- Większe okno kontekstowe - 128k vs 32k
- Lepszą wydajność w zadaniach matematycznych i kodowania - średnia dokładność 76,9% vs 60,4%
- Zwiększoną wydajność wielojęzyczną - obsługiwane języki to: angielski, francuski, niemiecki, hiszpański, włoski, portugalski, holenderski, rosyjski, chiński, japoński, koreański, arabski i hindi.

Dzięki tym funkcjom Mistral Large doskonale radzi sobie z

- _Retrieval Augmented Generation (RAG)_ - ze względu na większe okno kontekstowe
- _Wywoływanie funkcji_ - ten model ma natywne wywoływanie funkcji, co pozwala na integrację z zewnętrznymi narzędziami i API. Wywołania te mogą być wykonywane zarówno równolegle, jak i jedno po drugim w porządku sekwencyjnym.
- _Generowanie kodu_ - ten model doskonale radzi sobie z generowaniem kodu w językach Python, Java, TypeScript i C++.

### Przykład RAG przy użyciu Mistral Large 2

W tym przykładzie używamy Mistral Large 2 do uruchomienia wzorca RAG na dokumencie tekstowym. Pytanie jest napisane w języku koreańskim i dotyczy działań autora przed studiami.

Wykorzystuje model Embeddings Cohere do tworzenia embeddingów dokumentu tekstowego oraz pytania. W tej próbce używa pakietu faiss w Pythonie jako magazynu wektorów.

Prompt wysłany do modelu Mistral zawiera zarówno pytania, jak i pobrane fragmenty podobne do pytania. Model następnie dostarcza odpowiedź w języku naturalnym.

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

D, I = index.search(question_embeddings.reshape(1, -1), k=2) # odległość, indeks
retrieved_chunks = [chunks[i] for i in I.tolist()[0]]

prompt = f"""
Informacje kontekstowe znajdują się poniżej.
---------------------
{retrieved_chunks}
---------------------
Biorąc pod uwagę informacje kontekstowe, a nie wcześniejszą wiedzę, odpowiedz na zapytanie.
Zapytanie: {question}
Odpowiedź:
"""

chat_response = client.complete(
    messages=[
        SystemMessage(content="Jesteś pomocnym asystentem."),
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

Mistral Small to kolejny model z rodziny modeli Mistral należący do kategorii premier/enterprise. Jak sama nazwa wskazuje, model ten jest Małym Modelem Językowym (SLM). Zalety korzystania z Mistral Small to:

- Oszczędność kosztów w porównaniu do LLM Mistral, takich jak Mistral Large i NeMo - spadek ceny o 80%
- Niskie opóźnienie - szybsza odpowiedź w porównaniu do LLM Mistral
- Elastyczność - może być wdrażany w różnych środowiskach z mniejszymi ograniczeniami dotyczącymi wymaganych zasobów.

Mistral Small doskonale nadaje się do:

- Zadań tekstowych, takich jak podsumowywanie, analiza sentymentu i tłumaczenie.
- Aplikacji, w których często wysyłane są żądania, ze względu na opłacalność
- Zadań związanych z kodem o niskim opóźnieniu, takich jak przegląd i sugestie kodu

## Porównanie Mistral Small i Mistral Large

Aby pokazać różnice w opóźnieniach między Mistral Small i Large, uruchom poniższe komórki.

Powinieneś zauważyć różnicę w czasach odpowiedzi wynoszącą 3-5 sekund. Zwróć również uwagę na długości i styl odpowiedzi dla tego samego promptu.

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
        SystemMessage(content="Jesteś pomocnym asystentem kodowania."),
        UserMessage(content="Czy możesz napisać funkcję w Pythonie do testu fizz buzz?"),
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
        SystemMessage(content="Jesteś pomocnym asystentem kodowania."),
        UserMessage(content="Czy możesz napisać funkcję w Pythonie do testu fizz buzz?"),
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

Jest postrzegany jako ulepszenie wcześniejszego otwartego LLM od Mistral, Mistral 7B.

Inne cechy modelu NeMo to:

- _Bardziej wydajna tokenizacja:_ Ten model używa tokenizera Tekken zamiast częściej używanego tiktoken. Pozwala to na lepszą wydajność w większej liczbie języków i kodu.

- _Dostrajanie:_ Model podstawowy jest dostępny do dostrajania. Daje to większą elastyczność w przypadkach użycia, w których może być potrzebne dostrajanie.

- _Natywne wywoływanie funkcji_ - Podobnie jak Mistral Large, ten model został wytrenowany na wywoływaniu funkcji. Czyni go to wyjątkowym jako jeden z pierwszych modeli open source, który to potrafi.

### Porównanie Tokenizerów

W tej próbce przyjrzymy się, jak Mistral NeMo obsługuje tokenizację w porównaniu do Mistral Large.

Obie próbki przyjmują ten sam prompt, ale powinieneś zauważyć, że NeMo zwraca mniej tokenów niż Mistral Large.

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

model_name = "open-mistral-nemo\t"

tokenizer = MistralTokenizer.from_model(model_name)
```

```python
# Załaduj tokenizer Mistral
tokenizer = MistralTokenizer.from_model(model_name)

# Tokenizuj listę wiadomości
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Pobierz aktualną pogodę",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "Miasto i stan, np. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "Jednostka temperatury do użycia. Wywnioskuj to z lokalizacji użytkownika.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="Jaka jest dzisiaj pogoda w Paryżu"),
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
                    description="Pobierz aktualną pogodę",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "Miasto i stan, np. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "Jednostka temperatury do użycia. Wywnioskuj to z lokalizacji użytkownika.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="Jaka jest dzisiaj pogoda w Paryżu"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# Policz liczbę tokenów
print(len(tokens))
```

## Nauka się tu nie kończy, kontynuuj Podróż

Po ukończeniu tej lekcji sprawdź naszą [Kolekcję Nauki o Generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej podnosić swoją wiedzę o Generatywnej AI!
