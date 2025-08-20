<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:01:27+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "nl"
}
-->
# Bouwen met Mistral Modellen

## Introductie

Deze les behandelt:  
- Verkennen van de verschillende Mistral Modellen  
- Begrijpen van de toepassingsgebieden en scenario’s voor elk model  
- Codevoorbeelden die de unieke kenmerken van elk model laten zien.

## De Mistral Modellen

In deze les verkennen we 3 verschillende Mistral modellen:  
**Mistral Large**, **Mistral Small** en **Mistral Nemo**.

Elk van deze modellen is gratis beschikbaar op de Github Model marketplace. De code in dit notebook maakt gebruik van deze modellen om de code uit te voeren. Hier vind je meer informatie over het gebruik van Github Models om te [prototypen met AI-modellen](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
Mistral Large 2 is momenteel het vlaggenschipmodel van Mistral en is ontworpen voor zakelijk gebruik.

Het model is een upgrade van de originele Mistral Large en biedt:  
- Groter contextvenster - 128k versus 32k  
- Betere prestaties bij wiskunde- en programmeertaken - 76,9% gemiddelde nauwkeurigheid versus 60,4%  
- Verbeterde meertalige prestaties - talen omvatten: Engels, Frans, Duits, Spaans, Italiaans, Portugees, Nederlands, Russisch, Chinees, Japans, Koreaans, Arabisch en Hindi.

Met deze eigenschappen blinkt Mistral Large uit in:  
- *Retrieval Augmented Generation (RAG)* - dankzij het grotere contextvenster  
- *Function Calling* - dit model ondersteunt native function calling, wat integratie met externe tools en API’s mogelijk maakt. Deze aanroepen kunnen zowel parallel als sequentieel worden uitgevoerd.  
- *Codegeneratie* - dit model presteert uitstekend bij het genereren van Python, Java, TypeScript en C++ code.

### RAG Voorbeeld met Mistral Large 2

In dit voorbeeld gebruiken we Mistral Large 2 om een RAG-patroon toe te passen op een tekstdocument. De vraag is in het Koreaans gesteld en gaat over de activiteiten van de auteur vóór de universiteit.

Er wordt gebruikgemaakt van het Cohere Embeddings Model om embeddings te maken van het tekstdocument en de vraag. Voor dit voorbeeld wordt de faiss Python package gebruikt als vector store.

De prompt die naar het Mistral model wordt gestuurd bevat zowel de vraag als de opgehaalde tekstfragmenten die vergelijkbaar zijn met de vraag. Het model geeft vervolgens een antwoord in natuurlijke taal.

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
Mistral Small is een ander model binnen de Mistral-familie, behorend tot de premier/enterprise categorie. Zoals de naam al aangeeft, is dit een Small Language Model (SLM). De voordelen van Mistral Small zijn:  
- Kostenbesparend vergeleken met Mistral LLM’s zoals Mistral Large en NeMo - 80% prijsdaling  
- Lage latency - snellere reacties dan de grotere Mistral LLM’s  
- Flexibel - kan in verschillende omgevingen worden ingezet met minder beperkingen qua benodigde resources.

Mistral Small is ideaal voor:  
- Tekstgebaseerde taken zoals samenvatten, sentimentanalyse en vertalen  
- Toepassingen met frequente verzoeken vanwege de kosteneffectiviteit  
- Codegerelateerde taken met lage latency, zoals code review en suggesties

## Vergelijking tussen Mistral Small en Mistral Large

Om het verschil in latency tussen Mistral Small en Large te zien, voer je onderstaande cellen uit.

Je zou een verschil in responstijd van 3-5 seconden moeten zien. Let ook op de lengte en stijl van de antwoorden bij dezelfde prompt.

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

In vergelijking met de andere twee modellen in deze les is Mistral NeMo het enige gratis model met een Apache2-licentie.

Het wordt gezien als een upgrade van het eerdere open source LLM van Mistral, Mistral 7B.

Enkele andere kenmerken van het NeMo model zijn:

- *Efficiëntere tokenisatie:* Dit model gebruikt de Tekken tokenizer in plaats van de meer gebruikelijke tiktoken. Dit zorgt voor betere prestaties over meer talen en code.

- *Finetuning:* Het basismodel is beschikbaar voor finetuning, wat meer flexibiliteit biedt voor gebruikssituaties waar finetuning nodig kan zijn.

- *Native Function Calling* - Net als Mistral Large is dit model getraind op function calling. Dit maakt het uniek als een van de eerste open source modellen met deze mogelijkheid.

### Vergelijking van Tokenizers

In dit voorbeeld bekijken we hoe Mistral NeMo tokenisatie aanpakt in vergelijking met Mistral Large.

Beide voorbeelden gebruiken dezelfde prompt, maar je zult zien dat NeMo minder tokens teruggeeft dan Mistral Large.

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

## Leren stopt hier niet, ga door met de reis

Na het voltooien van deze les, bekijk onze [Generative AI Learning collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis van Generative AI verder te verdiepen!

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.