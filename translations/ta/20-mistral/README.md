# Mistral மாடல்களுடன் கட்டுமானம்  

## அறிமுகம்  

இந்த பாடத்தில் கையாளப்படும் விஷயங்கள்:  
- வெவ்வேறு Mistral மாடல்களை ஆராய்தல்  
- ஒவ்வொரு மாடலின் பயன்பாடுகள் மற்றும் சூழல்களை புரிந்து கொள்வது  
- ஒவ்வொரு மாடலின் தனித்துவமான அம்சங்களை காட்டும் குறியீடு உதாரணங்களை ஆராய்தல்.  

## Mistral மாடல்கள்  

இந்த பாடத்தில், நாம் 3 வேறுபட்ட Mistral மாடல்களை ஆராய்வோம்:  
**Mistral Large**, **Mistral Small** மற்றும் **Mistral Nemo**.  

இந்த மாடல்கள் அனைத்தும் [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) இலவசமாக கிடைக்கின்றன. இந்த நோட்புக் உள்ள குறியீடு இந்த மாடல்களை பயன்படுத்தி இயங்கும்.  

> **குறிப்பு:** GitHub Models 2026 ஜுலை மாத இறுதியில் புறக்கணிக்கப்பட உள்ளது. மேலும் விவரங்களுக்கு மற்றும் [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) பயன்படுத்தி AI மாடல்களை உருவாக்குவதற்கான வழிகாட்டலுக்கு இங்கே காணவும்.  


## Mistral Large 2 (2407)  
Mistral Large 2 தற்போது Mistral இன் தலைமை மாடலாகும் மற்றும் நிறுவனம் பயன்பாட்டிற்கு வடிவமைக்கப்பட்டுள்ளது.  

இந்த மாடல் ஒரிஜினல் Mistral Large மதிப்பீட்டிற்கு மேம்படுத்தல் ஆகும்:  
-  அதிக பெரிய Context சாளரம் - 128k மற்றும் 32k  
-  கணித மற்றும் குறியீட்டு பணிகளுக்கு சிறந்த செயல்திறன் - 76.9% சராசரி துல்லியம் மற்றும் 60.4%  
-  பன்மொழி செயல்திறன் அதிகரிப்பு - மொழிகள்: ஆங்கிலம், பிரஞ்சு, ஜெர்மன், ஸ்பானிஷ், இத்தாலிய, போர்ச்சுகீஸ், டச்சு, ரஷ்யன், சீன, ஜப்பானீஸ், கொரியான, அரபிக் மற்றும் ஹிந்தி.  

இந்த அம்சங்களுடன், Mistral Large சிறப்பாக செய்கிறது:  
- *Retrieval Augmented Generation (RAG)* - பெரிய Context சாளரத்தால்  
- *Function Calling* - இந்த மாடல் இயற்கையாகவே செயல்பாடுகள் அழைப்பை கொண்டுள்ளது, இது வெளி கருவிகள் மற்றும் API களுடன் ஒருங்கிணைக்க உதவுகிறது. இந்த அழைப்புகள் ஒரே நேரத்தில் அல்லது தொடர் முறையில் நடைமுறைப்படுத்தலாம்.  
- *குறியீடு உருவாக்கம்* - Python, Java, TypeScript மற்றும் C++ உருவாக்கத்தில் சிறப்பாக செயல்படுகிறது.  

### Mistral Large 2 பயன்படுத்தி RAG உதாரணம்  

இந்த உதாரணத்தில், நாம் Mistral Large 2 கொண்டு ஒரு உரை ஆவணத்தில் RAG மாதிரியை இயக்குகிறோம். கேள்வி கொரிய மொழியில் எழுதப்பட்டுள்ளது மற்றும் ஆசிரியர் கல்லூரிக்கு முன் செய்த செயல்கள் பற்றி கேட்கிறது.  

இது Cohere Embeddings மாடலை பயன்படுத்தி உரை ஆவணமும் கேள்வியும் embedding செய்து உருவாக்குகிறது. இந்த எடுத்துக்காட்டிற்கு faiss Python தொகுப்பை வெக்டர் சேமிப்பாக பயன்படுத்துகிறது.  

Mistral மாடலுக்கு அனுப்பப்படும் பிராம்ட், கேள்விகளையும் கேள்வியுடன் தொடர்புடைய துண்டுகளையும் உள்ளடக்கியது. மாடல் பின்னர் நான்கு மொழியில் பதில் அளிக்கிறது.  

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

# உங்கள் Microsoft Foundry திட்டத்தின் "மேலோட்டம்" பக்கத்திலிருந்து இதை பெறவும்
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # தூரம், குறியீடு
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
Mistral Small என்பது Mistral குடும்பத்தின் மற்றொரு மாடல், இது முன்னணி/நிறுவன வகை வடிவத்தில் உள்ளது. பெயர் தென்றல் படி, இது ஒரு சிறிய மொழி மாடல் (SLM). Mistral Small பயன்படுத்தும் நன்மைகள்:  
- Mistral Large மற்றும் NeMo போன்ற Mistral LLM களைவிட குறைந்த செலவு - 80% விலை தள்ளுபடி  
- குறைந்த தாமத தன்மை - Mistral LLM களைவிட வேகமான பதில்  
- தழுவல் - குறைந்த வளங்களுக்கு குறைவான கட்டுப்பாடுகளுடன் பல சூழல்களில் பயன்படுத்தலாம்.  


Mistral Small சிறந்தது:  
- சுருக்கம், உணர்வு பகுப்பு மற்றும் மொழிபெயர்ப்பு போன்ற உரை சார்ந்த பணிகளுக்கு  
- அதிக அடிக்கடி கேள்விகள் வருவதால் செலவு செயல்திறன் தேவையான பயன்பாடுகள்  
- குறைந்த தாமதம் உள்ள குறியீடு பணிகள் மற்றும் வழிகாட்டி உதவிகளுக்கு  

## Mistral Small மற்றும் Mistral Large ஒப்பீடு  

Mistral Small மற்றும் Large இடையே latency வேறுபாடுகளை காண கீழ்கண்ட செல்ஸ்களை இயக்கவும்.  

பதில் நேரங்களில் 3-5 விநாடிகள் வரையிலான வேறுபாடு காணலாம். அதே பிராம்டில் பதில் நீளம் மற்றும் பாணியையும் கவனிக்க வேண்டும்.  

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

இந்தப் பாடலில் விவாதிக்கப்பட்ட மற்ற இரண்டு மாடல்களுடன் ஒப்பிடுகையில், Mistral NeMo மறைமுக Apache2 உரிமத்துடன் இலவசமாக கிடைக்கும் ஒரே மாடல் ஆகும்.  

இது Mistral இன் முந்தைய திறந்த மூல LLM, Mistral 7B க்கு மேம்பாடு என்று பார்க்கப்படுகிறது.  

NeMo மாடலின் பிற அம்சங்கள்:  

- *மேலும் திறமையான tokenization:* இந்த மாடல் பொதுவான tiktoken க்கு பதிலாக Tekken tokenizer பயன்படுத்துகிறது. இது அதிக மொழிகள் மற்றும் குறியீடுகளில் சிறந்த செயல்திறனைக் கொடுக்கிறது.  

- *Finetuning:* அடிப்படை மாடல் finetuning க்கு கிடைக்கிறது. இது தேவையான பயன்பாடுகளுக்கான அதிக தழுவலை வழங்குகிறது.  

- *சொந்த செயல்பாடு அழைப்பு* - Mistral Large போலே இந்த மாடலும் செயல்பாடு அழைப்பில் பயிற்சி பெற்றுள்ளது. இது திறந்த மூல மாடல்களில் முதல் முறையாக இருப்பதைக் குறிப்பிடுகிறது.  


### Tokenizer களை ஒப்பிடல்  

இந்த எடுத்துக்காட்டில், Mistral NeMo tokenization ஐ Mistral Large உடன் ஒப்பிடப்போவது.  

இரண்டும் ஒரே பிராம்டை எடுக்கின்றன, ஆனால் NeMo குறைவான token களை வழங்குவதை நீங்கள் காணலாம்.  

```bash
pip install mistral-common
```

```python 
# தேவையான பேக்கேஜ்களை இறக்குமதி செய்க:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# மிஸ்ட்ரல் டோக்கனைசரை ஏற்றவும்

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# செய்திகளின் பட்டியலை டோக்கன்செய்க
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

# டோக்கன்களின் எண்ணிக்கையை எண்ணுக
print(len(tokens))
```

```python
# தேவைப்படும் பாக்கேஜ்களை இறக்குமதி செய்க:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# மிஸ்ட்ரால் டோக்கனைசரை ஏற்றுகொள்

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# செய்திகளின் பட்டியலை டோக்கனைஸ் செய்க
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

# டோக்கன்களின் எண்ணிக்கை கணக்கிடுக
print(len(tokens))
```

## கற்குதல் இங்கே நிற்பது இல்லை, பயணத்தை தொடருங்கள்  

இந்த பாடத்தை முடித்த பிறகு, நமது [Generative AI கற்றல் தொகுப்பை](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) பார்வையிட்டு உங்கள் Generative AI அறிவை மேம்படுத்திக் கொள்ளுங்கள்!  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->