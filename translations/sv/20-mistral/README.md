# Bygga med Mistral-modeller 

## Introduktion 

Denna lektion kommer att täcka: 
- Utforska de olika Mistral-modellerna 
- Förstå användningsområden och scenarier för varje modell 
- Utforska kodexempel som visar varje modells unika funktioner. 

## Mistral-modellerna 

I denna lektion kommer vi att utforska 3 olika Mistral-modeller: 
**Mistral Large**, **Mistral Small** och **Mistral Nemo**. 

Var och en av dessa modeller finns gratis på GitHub Model marketplace. Koden i denna anteckningsbok kommer att använda dessa modeller för att köra koden. Här är mer information om att använda GitHub Models för att [prototypa med AI-modeller](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst). 


## Mistral Large 2 (2407)
Mistral Large 2 är för närvarande Mistrals flaggskeppsmodell och är designad för företagsanvändning. 

Modellen är en uppgradering av den ursprungliga Mistral Large genom att erbjuda 
-  Större kontextfönster - 128k vs 32k 
-  Bättre prestanda på matematik- och kodningsuppgifter - 76,9 % genomsnittlig noggrannhet vs 60,4 % 
-  Ökad flerspråkig prestanda - språk inkluderar: engelska, franska, tyska, spanska, italienska, portugisiska, nederländska, ryska, kinesiska, japanska, koreanska, arabiska och hindi.

Med dessa funktioner utmärker sig Mistral Large på 
- *Retrieval Augmented Generation (RAG)* - på grund av det större kontextfönstret
- *Funktionsanrop* - denna modell har inbyggda funktionsanrop som möjliggör integration med externa verktyg och API:er. Dessa anrop kan göras både parallellt eller efter varandra i en sekventiell ordning. 
- *Kodgenerering* - denna modell är särskilt bra på generering av Python, Java, TypeScript och C++. 

### RAG-exempel med Mistral Large 2 

I detta exempel använder vi Mistral Large 2 för att köra ett RAG-mönster över ett textdokument. Frågan är skriven på koreanska och handlar om författarens aktiviteter innan universitetet. 

Den använder Cohere Embeddings-modellen för att skapa inbäddningar av textdokumentet samt frågan. För detta exempel används faiss Python-paket som en vektorlager. 

Prompten som skickas till Mistral-modellen inkluderar både frågorna och de hämtade delar som liknar frågan. Modellen ger sedan ett svar på naturligt språk. 

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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # avstånd, index
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
Mistral Small är en annan modell i Mistral-familjen under premier/enterprise-kategorin. Som namnet antyder är detta en liten språklig modell (SLM). Fördelarna med att använda Mistral Small är att den är: 
- Kostnadsbesparande jämfört med Mistral LLMs som Mistral Large och NeMo - 80 % prisminskning
- Låg latens - snabbare svar jämfört med Mistrals LLMs
- Flexibel - kan distribueras i olika miljöer med mindre restriktioner på nödvändiga resurser. 


Mistral Small är utmärkt för: 
- Textbaserade uppgifter såsom sammanfattning, sentimentanalys och översättning. 
- Applikationer där frekventa förfrågningar görs på grund av dess kostnadseffektivitet 
- Koduppgifter med låg latens som granskning och kodförslag 

## Jämförelse mellan Mistral Small och Mistral Large 

För att visa skillnader i latens mellan Mistral Small och Large, kör nedanstående celler. 

Du bör se en skillnad i svarstider på mellan 3-5 sekunder. Notera även skillnader i svarslängder och stil för samma prompt.  

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

Jämfört med de andra två modellerna som diskuteras i denna lektion är Mistral NeMo den enda gratismodellen med en Apache2-licens. 

Den ses som en uppgradering av den tidigare open source LLM från Mistral, Mistral 7B. 

Några andra funktioner hos NeMo-modellen är: 

- *Mer effektiv tokenisering:* Denna modell använder Tekken-tokenizer istället för den mer allmänt använda tiktoken. Detta ger bättre prestanda för fler språk och kod. 

- *Finjustering:* Basmodellen är tillgänglig för finjustering. Detta möjliggör större flexibilitet för användningsfall där finjustering kan behövas. 

- *Inbyggda funktionsanrop* - Liksom Mistral Large har denna modell tränats på funktionsanrop. Detta gör den unik som en av de första open source-modellerna att göra detta. 


### Jämförelse av tokenizers 

I detta exempel tittar vi på hur Mistral NeMo hanterar tokenisering jämfört med Mistral Large. 

Båda exemplen använder samma prompt men du bör se att NeMo returnerar färre tokens än Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Importera nödvändiga paket:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Ladda Mistral-tokenizer

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenisera en lista med meddelanden
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

# Räkna antalet tokens
print(len(tokens))
```

```python
# Importera nödvändiga paket:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Ladda Mistral-tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenisera en lista med meddelanden
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

# Räkna antalet tokens
print(len(tokens))
```

## Lärandet slutar inte här, fortsätt resan

Efter att ha slutfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta höja dina kunskaper om Generativ AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->