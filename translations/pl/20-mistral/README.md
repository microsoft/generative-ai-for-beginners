<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:16:37+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "pl"
}
-->
# Budowanie z modelami Mistral

## Wprowadzenie

Ta lekcja obejmie:
- Badanie różnych modeli Mistral
- Zrozumienie zastosowań i scenariuszy dla każdego modelu
- Przykłady kodu pokazujące unikalne cechy każdego modelu

## Modele Mistral

W tej lekcji zbadamy 3 różne modele Mistral: **Mistral Large**, **Mistral Small** i **Mistral Nemo**.

Każdy z tych modeli jest dostępny za darmo na rynku modeli Github. Kod w tym notebooku będzie korzystał z tych modeli do uruchamiania kodu. Oto więcej szczegółów na temat używania modeli Github do [prototypowania z modelami AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 jest obecnie flagowym modelem Mistral i jest zaprojektowany do użytku korporacyjnego.

Model ten jest ulepszeniem oryginalnego Mistral Large, oferując:
- Większe okno kontekstowe - 128k vs 32k
- Lepszą wydajność w zadaniach matematycznych i programistycznych - średnia dokładność 76,9% vs 60,4%
- Zwiększoną wydajność wielojęzyczną - języki obejmują: angielski, francuski, niemiecki, hiszpański, włoski, portugalski, holenderski, rosyjski, chiński, japoński, koreański, arabski i hindi.

Dzięki tym funkcjom, Mistral Large doskonale sprawdza się w:
- *Retrieval Augmented Generation (RAG)* - dzięki większemu oknu kontekstowemu
- *Wywołaniach funkcji* - ten model ma wbudowane wywołania funkcji, co pozwala na integrację z zewnętrznymi narzędziami i API. Te wywołania mogą być realizowane zarówno równolegle, jak i sekwencyjnie.
- *Generacji kodu* - model ten świetnie radzi sobie z generowaniem kodu w Pythonie, Java, TypeScript i C++.

### Przykład RAG z użyciem Mistral Large 2

W tym przykładzie używamy Mistral Large 2 do uruchomienia wzorca RAG na dokumencie tekstowym. Pytanie jest napisane po koreańsku i dotyczy działań autora przed studiami.

Używa modelu Cohere Embeddings do tworzenia osadzeń dokumentu tekstowego oraz pytania. Dla tego przykładu używa pakietu faiss Python jako magazynu wektorów.

Zachęta wysłana do modelu Mistral zawiera zarówno pytania, jak i pobrane fragmenty podobne do pytania. Model następnie dostarcza odpowiedź w języku naturalnym.

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

Mistral Small to kolejny model z rodziny modeli Mistral w kategorii premier/korporacyjnej. Jak sama nazwa wskazuje, jest to mały model językowy (SLM). Zalety korzystania z Mistral Small to:
- Oszczędność kosztów w porównaniu do LLM-ów Mistral, takich jak Mistral Large i NeMo - 80% spadek ceny
- Niska latencja - szybsza odpowiedź w porównaniu do LLM-ów Mistral
- Elastyczność - może być wdrażany w różnych środowiskach z mniejszymi ograniczeniami dotyczącymi wymaganych zasobów.

Mistral Small jest doskonały do:
- Zadań opartych na tekście, takich jak streszczenie, analiza sentymentu i tłumaczenie.
- Aplikacji, w których składane są częste żądania ze względu na efektywność kosztową
- Zadań związanych z kodem o niskiej latencji, takich jak przegląd i sugestie kodu

## Porównanie Mistral Small i Mistral Large

Aby pokazać różnice w latencji między Mistral Small i Large, uruchom poniższe komórki.

Powinieneś zauważyć różnicę w czasach odpowiedzi między 3-5 sekund. Zwróć również uwagę na długości i styl odpowiedzi dla tej samej zachęty.

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

W porównaniu do dwóch pozostałych modeli omówionych w tej lekcji, Mistral NeMo jest jedynym darmowym modelem z licencją Apache2.

Jest postrzegany jako ulepszenie wcześniejszego open source LLM od Mistral, Mistral 7B.

Niektóre inne cechy modelu NeMo to:

- *Bardziej efektywna tokenizacja:* Ten model używa tokenizera Tekken zamiast bardziej powszechnie używanego tiktoken. Pozwala to na lepszą wydajność w większej liczbie języków i kodów.

- *Dostrajanie:* Model bazowy jest dostępny do dostrajania. Pozwala to na większą elastyczność w przypadkach użycia, w których dostrajanie może być potrzebne.

- *Wbudowane wywołania funkcji* - Podobnie jak Mistral Large, ten model został przeszkolony do wywoływania funkcji. Czyni go to jednym z pierwszych modeli open source, które to robią.

### Porównanie tokenizatorów

W tym przykładzie przyjrzymy się, jak Mistral NeMo radzi sobie z tokenizacją w porównaniu do Mistral Large.

Oba przykłady przyjmują tę samą zachętę, ale powinieneś zauważyć, że NeMo zwraca mniej tokenów w porównaniu do Mistral Large.

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

## Nauka się nie kończy tutaj, kontynuuj podróż

Po ukończeniu tej lekcji, sprawdź naszą [kolekcję nauki o Generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby kontynuować rozwijanie swojej wiedzy o Generatywnej AI!

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.