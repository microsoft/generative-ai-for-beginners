# Bouwen met Mistral-modellen

## Inleiding

Deze les behandelt:
- Het verkennen van de verschillende Mistral-modellen
- Het begrijpen van de toepassingsgebieden en scenario’s voor elk model
- Het verkennen van codevoorbeelden die de unieke kenmerken van elk model laten zien.

## De Mistral-modellen

In deze les verkennen we 3 verschillende Mistral-modellen:
**Mistral Large**, **Mistral Small** en **Mistral Nemo**.

Elk van deze modellen is gratis beschikbaar op de GitHub Model-marktplaats. De code in dit notitieboek gebruikt deze modellen om code uit te voeren. Hier zijn meer details over het gebruik van GitHub-modellen om te [prototypen met AI-modellen](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 is momenteel het vlaggenschipmodel van Mistral en is ontworpen voor zakelijk gebruik.

Het model is een upgrade van de originele Mistral Large door te bieden:
- Groter contextvenster - 128k versus 32k
- Betere prestaties bij wiskunde- en programmeertaken - 76,9% gemiddelde nauwkeurigheid versus 60,4%
- Verhoogde meertalige prestaties - talen omvatten: Engels, Frans, Duits, Spaans, Italiaans, Portugees, Nederlands, Russisch, Chinees, Japans, Koreaans, Arabisch en Hindi.

Met deze kenmerken blinkt Mistral Large uit in
- *Retrieval Augmented Generation (RAG)* - dankzij het grotere contextvenster
- *Functie-aanroep* - dit model heeft native functie-aanroeping die integratie met externe tools en API's mogelijk maakt. Deze aanroepen kunnen parallel of achtereenvolgens in volgorde worden uitgevoerd.
- *Codegeneratie* - dit model blinkt uit in Python-, Java-, TypeScript- en C++-generatie.

### RAG-voorbeeld met Mistral Large 2

In dit voorbeeld gebruiken we Mistral Large 2 om een RAG-patroon toe te passen op een tekstdocument. De vraag is in het Koreaans geschreven en gaat over de activiteiten van de auteur vóór de universiteit.

Het gebruikt Cohere Embeddings Model om embeddings te maken van het tekstdocument en de vraag. Voor dit voorbeeld maakt het gebruik van het Python-pakket faiss als een vectorstore.

De prompt die aan het Mistral-model wordt gestuurd, bevat zowel de vragen als de opgehaalde stukken die vergelijkbaar zijn met de vraag. Het model geeft vervolgens een natuurlijke taalrespons.

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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # afstand, index
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
Mistral Small is een ander model in de Mistral-familie binnen de premier/enterprise categorie. Zoals de naam al aangeeft, is dit een Small Language Model (SLM). De voordelen van het gebruik van Mistral Small zijn dat het:
- Kostenbesparend is in vergelijking met Mistral-LLM's zoals Mistral Large en NeMo - 80% prijsverlaging
- Lage latency - snellere respons in vergelijking met Mistral's LLM's
- Flexibel - kan in verschillende omgevingen worden ingezet met minder beperkingen qua benodigde resources.

Mistral Small is uitstekend voor:
- Tekstgebaseerde taken zoals samenvatting, sentimentanalyse en vertaling.
- Toepassingen waar frequent aanvragen worden gedaan vanwege de kosteneffectiviteit
- Low latency code taken zoals code review en suggesties

## Vergelijking tussen Mistral Small en Mistral Large

Om de verschillen in latency tussen Mistral Small en Large te zien, voer je onderstaande cellen uit.

Je zou een verschil in reactietijden van 3-5 seconden moeten zien. Let ook op de antwoordlengtes en stijl bij dezelfde prompt.

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

Vergeleken met de andere twee modellen die in deze les worden besproken, is Mistral NeMo het enige gratis model met een Apache2-licentie.

Het wordt gezien als een upgrade van het eerdere open-source LLM van Mistral, Mistral 7B.

Enkele andere kenmerken van het NeMo-model zijn:

- *Efficiëntere tokenisatie:* Dit model gebruikt de Tekken-tokenizer in plaats van de meer gebruikte tiktoken. Dit zorgt voor betere prestaties bij meer talen en code.

- *Fijnafstelling:* Het basismodel is beschikbaar voor fijnafstelling. Dit biedt meer flexibiliteit voor use-cases waarbij fijnafstelling nodig kan zijn.

- *Native functie-aanroep* - Net als Mistral Large is dit model getraind op functie-aanroepen. Dit maakt het uniek als een van de eerste open-source modellen die dit doen.

### Vergelijking tokenizers

In dit voorbeeld bekijken we hoe Mistral NeMo tokenisatie afhandelt vergeleken met Mistral Large.

Beide voorbeelden nemen dezelfde prompt, maar je zou moeten zien dat NeMo minder tokens teruggeeft dan Mistral Large.

```bash
pip install mistral-common
```

```python 
# Importeer benodigde pakketten:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Laad Mistral tokenizer

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokeniseer een lijst met berichten
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

# Tel het aantal tokens
print(len(tokens))
```

```python
# Importeer benodigde pakketten:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Laad Mistral tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokeniseer een lijst met berichten
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

# Tel het aantal tokens
print(len(tokens))
```

## Het leren stopt hier niet, ga verder op je reis

Na het voltooien van deze les, bekijk onze [Generative AI Learning-collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis van Generatieve AI verder te verdiepen!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel wij streven naar nauwkeurigheid, kan deze automatische vertaling fouten of onnauwkeurigheden bevatten. Het oorspronkelijke document in de originele taal moet als de gezaghebbende bron worden beschouwd. Voor belangrijke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerd geïnterpreteerde informatie voortvloeiend uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->