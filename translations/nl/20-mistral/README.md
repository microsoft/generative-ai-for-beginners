# Bouwen met Mistral-modellen 

## Introductie 

Deze les behandelt: 
- Verkenning van de verschillende Mistral-modellen 
- Begrip van de gebruiksscenario's voor elk model 
- Verkenning van codevoorbeelden die de unieke kenmerken van elk model laten zien. 

## De Mistral-modellen 

In deze les zullen we 3 verschillende Mistral-modellen verkennen: 
**Mistral Large**, **Mistral Small** en **Mistral Nemo**. 

Elk van deze modellen is gratis beschikbaar op [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). De code in dit notitieboek maakt gebruik van deze modellen om de code uit te voeren.

> **Opmerking:** GitHub Models wordt eind juli 2026 uitgefaseerd. Hier zijn meer details over het gebruik van [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) om te prototypen met AI-modellen. 


## Mistral Large 2 (2407)
Mistral Large 2 is momenteel het vlaggenschipmodel van Mistral en is ontworpen voor zakelijk gebruik. 

Het model is een upgrade van de originele Mistral Large door het aanbieden van 
-  Groter contextvenster - 128k vs 32k 
-  Betere prestaties op wiskunde- en codeertaken - 76,9% gemiddelde nauwkeurigheid vs 60,4% 
-  Verbeterde meertalige prestaties - talen omvatten: Engels, Frans, Duits, Spaans, Italiaans, Portugees, Nederlands, Russisch, Chinees, Japans, Koreaan, Arabisch en Hindi.

Met deze functies blinkt Mistral Large uit in 
- *Retrieval Augmented Generation (RAG)* - dankzij het grotere contextvenster
- *Functieoproep* - dit model heeft native functieoproepen waarmee integratie met externe tools en API's mogelijk is. Deze oproepen kunnen zowel parallel als achtereenvolgens in een sequentiële volgorde worden uitgevoerd. 
- *Codegeneratie* - dit model blinkt uit in Python, Java, TypeScript en C++ generatie. 

### RAG-voorbeeld met Mistral Large 2 

In dit voorbeeld gebruiken we Mistral Large 2 om een RAG-patroon toe te passen op een tekstdocument. De vraag is in het Koreaans geschreven en gaat over de activiteiten van de auteur vóór de universiteit. 

Het gebruikt het Cohere Embeddings Model om embeddings te maken van het tekstdocument en de vraag. Voor dit voorbeeld wordt de faiss Python-pakket als vectoropslag gebruikt. 

De prompt die naar het Mistral-model wordt gestuurd, bevat zowel de vragen als de opgehaalde stukken die vergelijkbaar zijn met de vraag. Het model levert vervolgens een natuurlijk taalantwoord. 

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

# Verkrijg deze van de "Overzicht" pagina van je Microsoft Foundry-project
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
Mistral Small is een ander model in de Mistral-familie binnen de premier/ondernemingscategorie. Zoals de naam al zegt, is dit model een Klein Taalmodel (SLM). De voordelen van het gebruik van Mistral Small zijn: 
- Kostenbesparing in vergelijking met Mistral LLM's zoals Mistral Large en NeMo - 80% prijsdaling
- Lage latency - snellere reactie in vergelijking met Mistrals LLM's
- Flexibel - kan in verschillende omgevingen worden ingezet met minder beperkingen op vereiste middelen. 


Mistral Small is uitstekend voor: 
- Tekstgebaseerde taken zoals samenvatting, sentimentanalyse en vertaling. 
- Toepassingen waar frequent verzoeken worden gedaan vanwege de kosteneffectiviteit 
- Codeertaken met lage latency zoals beoordeling en codevoorstellen 

## Vergelijking tussen Mistral Small en Mistral Large 

Om de verschillen in latency tussen Mistral Small en Large te laten zien, voer je de onderstaande cellen uit. 

Je zou een verschil in responstijden van 3-5 seconden moeten zien. Let ook op de responslengte en stijl bij dezelfde prompt.  

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

Vergeleken met de andere twee modellen besproken in deze les, is Mistral NeMo het enige gratis model met een Apache2-licentie. 

Het wordt gezien als een upgrade van het eerdere open-source LLM van Mistral, Mistral 7B. 

Enkele andere kenmerken van het NeMo-model zijn: 

- *Efficiëntere tokenisatie:* Dit model gebruikt de Tekken-tokenizer in plaats van de meer gebruikte tiktoken. Dit zorgt voor betere prestaties bij meerdere talen en code. 

- *Fijn afstellen:* Het basismodel is beschikbaar voor fijn afstellen. Dit maakt het flexibeler voor gebruikssituaties waar fijn afstellen vereist kan zijn. 

- *Native functieoproepen* - Net als Mistral Large is dit model getraind op functieoproepen. Dit maakt het uniek als een van de eerste open-source modellen die dit kunnen. 


### Vergelijking van tokenizers 

In dit voorbeeld bekijken we hoe Mistral NeMo tokenisatie afhandelt in vergelijking met Mistral Large. 

Beide voorbeelden nemen dezelfde prompt, maar je zult zien dat NeMo minder tokens retourneert dan Mistral Large. 

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

# Laad Mistral-tokenizer

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

# Laad Mistral-tokenizer

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

## Leren stopt hier niet, ga door met de reis

Na het voltooien van deze les, kijk dan eens naar onze [Generative AI Learning collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis van Generative AI verder uit te breiden!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->