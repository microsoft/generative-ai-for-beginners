<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:00:34+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "sv"
}
-->
# Bygga med Mistral-modeller

## Introduktion

Den här lektionen täcker:  
- Utforska de olika Mistral-modellerna  
- Förstå användningsområden och scenarier för varje modell  
- Kodexempel som visar varje modells unika egenskaper.

## Mistral-modellerna

I den här lektionen kommer vi att utforska 3 olika Mistral-modeller:  
**Mistral Large**, **Mistral Small** och **Mistral Nemo**.

Var och en av dessa modeller finns tillgängliga gratis på Github Model marketplace. Koden i denna notebook använder dessa modeller för att köra koden. Här finns mer information om att använda Github Models för att [prototypa med AI-modeller](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
Mistral Large 2 är för närvarande Mistrals flaggskeppsmodell och är designad för företagsanvändning.

Modellen är en uppgradering av den ursprungliga Mistral Large och erbjuder  
- Större kontextfönster – 128k jämfört med 32k  
- Bättre prestanda på matematik- och kodningsuppgifter – 76,9 % genomsnittlig noggrannhet jämfört med 60,4 %  
- Förbättrad flerspråkig prestanda – språk inkluderar: engelska, franska, tyska, spanska, italienska, portugisiska, nederländska, ryska, kinesiska, japanska, koreanska, arabiska och hindi.

Med dessa egenskaper utmärker sig Mistral Large på  
- *Retrieval Augmented Generation (RAG)* – tack vare det större kontextfönstret  
- *Function Calling* – denna modell har inbyggd funktion för funktionsanrop som möjliggör integration med externa verktyg och API:er. Anropen kan göras parallellt eller sekventiellt.  
- *Kodgenerering* – modellen är särskilt bra på att generera Python, Java, TypeScript och C++.

### RAG-exempel med Mistral Large 2

I detta exempel använder vi Mistral Large 2 för att köra ett RAG-mönster över ett textdokument. Frågan är skriven på koreanska och handlar om författarens aktiviteter innan universitetet.

Den använder Cohere Embeddings Model för att skapa inbäddningar av textdokumentet samt frågan. För detta exempel används Python-paketet faiss som vektorlagring.

Prompten som skickas till Mistral-modellen innehåller både frågorna och de hämtade textbitarna som liknar frågan. Modellen ger sedan ett svar på naturligt språk.

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
Mistral Small är en annan modell i Mistral-familjen under premier/enterprise-kategorin. Som namnet antyder är detta en Small Language Model (SLM). Fördelarna med att använda Mistral Small är att den är:  
- Kostnadseffektiv jämfört med Mistral LLMs som Mistral Large och NeMo – 80 % lägre pris  
- Låg latens – snabbare svar jämfört med Mistrals LLMs  
- Flexibel – kan distribueras i olika miljöer med färre krav på resurser.

Mistral Small passar utmärkt för:  
- Textbaserade uppgifter som sammanfattning, sentimentanalys och översättning.  
- Applikationer med frekventa förfrågningar tack vare kostnadseffektiviteten  
- Koduppgifter med låg latens som granskning och kodförslag

## Jämförelse mellan Mistral Small och Mistral Large

För att visa skillnader i latens mellan Mistral Small och Large, kör cellerna nedan.

Du bör se en skillnad i svarstider på 3–5 sekunder. Notera också skillnader i svarslängd och stil för samma prompt.

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

Jämfört med de andra två modellerna som diskuteras i denna lektion är Mistral NeMo den enda gratismodellen med Apache2-licens.

Den ses som en uppgradering av den tidigare open source-LLM från Mistral, Mistral 7B.

Några andra egenskaper hos NeMo-modellen är:

- *Effektivare tokenisering:* Denna modell använder Tekken-tokenizer istället för den mer vanligt förekommande tiktoken. Det ger bättre prestanda över fler språk och kod.

- *Finjustering:* Basmodellen finns tillgänglig för finjustering, vilket ger större flexibilitet för användningsfall där finjustering kan behövas.

- *Inbyggd Function Calling* – Precis som Mistral Large har denna modell tränats för funktionsanrop. Det gör den unik som en av de första open source-modellerna med denna funktion.

### Jämförelse av tokenizers

I detta exempel tittar vi på hur Mistral NeMo hanterar tokenisering jämfört med Mistral Large.

Båda exemplen använder samma prompt, men du bör se att NeMo returnerar färre tokens jämfört med Mistral Large.

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

## Lärandet slutar inte här, fortsätt resan

Efter att ha genomfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla dina kunskaper inom Generativ AI!

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.