# மிஸ்ட்ரல் மாதிரிகள் மூலம் கட்டமைத்தல்

## அறிமுகம்

இந்த பாடத்தில் கையாளப்படும் பொருட்கள்:  
- வெவ்வேறு மிஸ்ட்ரல் மாதிரிகளை ஆராய்தல்  
- ஒவ்வொரு மாதிரிக்கும் பயன்பாடுகள் மற்றும் சூழ்நிலைகள் புரிந்துகொள்வது  
- ஒவ்வொரு மாதிரிக்கும் தனித்துவமான அம்சங்களை காட்டும் குறியீட்டு உதாரணங்களை ஆராய்தல்.

## மிஸ்ட்ரல் மாதிரிகள்

இந்த பாடத்தில், நாம் வெவ்வேறு 3 மிஸ்ட்ரல் மாதிரிகளை ஆராயப்போகிறோம்:  
**மிஸ்ட்ரல் லார்ஜ்**, **மிஸ்ட்ரல் ஸ்மால்** மற்றும் **மிஸ்ட்ரல் நீமோ**.

இவை அனைத்தும் GitHub மாதிரி சந்தையில் இலவசமாகக் கிடைக்கின்றன. இந்த நோட்புக்கில் உள்ள குறியீடு இந்த மாதிரிகளை பயன்படுத்தி இயங்கும். GitHub மாதிரிகள் பயன்படுத்தி [கலைமுனைப்பான எ.ஐ. மாதிரிகளை உருவாக்குவது](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) குறித்த மேலதிக விவரங்கள் இங்கே உள்ளன.

## மிஸ்ட்ரல் லார்ஜ் 2 (2407)  
மிஸ்ட்ரல் லார்ஜ் 2 தற்போது மிஸ்ட்ரலின் பிரதான மாதிரி ஆகும் மற்றும் கார்ப்பரேட் பயன்பாட்டிற்கு வடிவமைக்கப்பட்டுள்ளது.

இது மூல மிஸ்ட்ரல் லார்ஜ் மாதிரிக்கு புதிய மேம்பாடுகளை வழங்குகிறது:  
- பெரிய_Context_Window_ - 128k مقابل 32k  
- கணிதம் மற்றும் குறியீடு பணிகளில் சிறந்த செயல்திறன் - 76.9% சராசரி துல்லியம் مقابل 60.4%  
- அதிகபட்ச பன்மொழி செயல்திறன் - ஆங்கிலம், பிரஞ்சு, ஜெர்மன், ஸ்பானிஷ், இத்தாலிய, போருட்கீசிய, டச்சு, ரஷியன், சீன, ஜப்பானீஸ், கொரியன், அரபிக் மற்றும் இந்தி ஆகிய மொழிகள்.

இந்த அம்சங்களுடன் மிஸ்ட்ரல் லார்ஜ் சிறப்பாக செயல்படுகின்றது:  
- *மறுபக்கம் வாய்ந்த உருவாக்கம் (RAG)* - பெரிய_Context_Window_ காரணமாக  
- *ஃபங்க்ஷன் அழைப்பு* - இது இயல்பான ஃபங்க்ஷன் அழைப்பைக் கொண்டிருக்கும், வெளியீடு கருவிகளும் APIகளும் இணைக்க அனுமதிக்கிறது. ஒரே நேரத்தில் அல்லது தொடர் முறையில் அழைப்புகளைச் செய்ய முடியும்.  
- *குறியீட்டு உருவாக்கம்* - Python, Java, TypeScript மற்றும் C++ குறியீட்டில் சிறந்த செயல்திறன்.

### மிஸ்ட்ரல் லார்ஜ் 2 பாவனை கொண்டு RAG உதாரணம்

இந்த உதாரணத்தில், ஒரு உரை ஆவணத்தில் RAG மாதிரி செயல்படுத்த மிஸ்ட்ரல் லார்ஜ் 2 பயன்படுத்தப்படுகிறது. கேள்வி கொரிய மொழியில் எழுதப்பட்டு, எழுத்தாளர் கல்லூரிக்கு முன் என்ன செயல்பட்டார் என்று கேட்கிறது.

இது Cohere Embeddings மாதிரியைப் பயன்படுத்தி உரை ஆவணத்திற்கும் கேள்விக்கும் எம்பெடிங்குகள் உருவாக்குகிறது. இந்த மாதிரிக்கு faiss Python தொகுப்பை வெக்டர் சேமிப்பாக பயன்படுத்துகிறது.

மாடலுக்கு அனுப்பப்படும் ஊக்கவாக்கியம் கேள்விகள் மற்றும் அதற்குச் சேர்ந்த பெறப்பட்ட துணுக்குகளை இணைத்து அனுப்பப்படுகிறது. பின்னர் மாடல் இயல்பான மொழி பதிலை வழங்குகிறது.

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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # தொலைவு, அசையும் இடம்
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
  
## மிஸ்ட்ரல் ஸ்மால்  
மிஸ்ட்ரல் ஸ்மால் என்பது மிஸ்ட்ரல் குடும்பத்தின் மற்றொரு மாதிரி, முன்னணி/கார்ப்பரேட் பிரிவில் உள்ளது. அதன் பெயரிலும் தெரியப்படும் போல், இது ஒரு சிறிய மொழி மாதிரி (SLM). மிஸ்ட்ரல் ஸ்மால் பயன்படுத்துவதன் பலன்கள்:  
- மிஸ்ட்ரல் லார்ஜ் மற்றும் NeMo போன்ற பெரிய மாடல்களுடன் ஒப்பிடும்போது செலவு குறைப்பு - 80% விலை குறைப்பு  
- குறைந்த தாமதம் - மிஸ்ட்ரல் LLM களுடன் ஒப்பிடும்போது வேகமான பதில்கள்  
- விரைவான மற்றும் பல சூழல்களில் குறைந்த ஆதார தேவையுடன் நிறுவ முடியும்.

மிஸ்ட்ரல் ஸ்மால் சிறந்தது:  
- உரை அடிப்படையிலான பணிகள் (சுருக்கம், உணர்வு பகுப்பாய்வு, மொழிபெயர்ப்பு போன்றவை)  
- நிறைய கேள்விகள் இருந்தும் செலவு திறனை கருத்தில் கொண்டு செயல்படும் செயலிகள்  
- குறைந்த தாமதக் குறியீட்டு பணிகள் (கோட் விமர்சனங்கள் மற்றும் பரிந்துரைகள்).

## மிஸ்ட்ரல் ஸ்மால் மற்றும் மிஸ்ட்ரல் லார்ஜ் இடையேயான ஒப்பீடு

மிஸ்ட்ரல் ஸ்மால் மற்றும் லார்ஜ் மாதிரிகளுக்கு இடையேயான தாமத வேறுபாடுகளை காண கீழே உள்ள செல் நிரலை இயக்கவும்.

3 முதல் 5 விநாடிகள் வரை பதிலளியக வேறுபாடு காணப்படும். அதே ஊக்கவாக்கியத்தின் மீதான பதிலின் நீளம் மற்றும் பாணி கவனிக்கவும்.

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
  
## மிஸ்ட்ரல் நீமோ

இந்த பாடலில் விவாதிக்கப்பட்ட மற்ற இரண்டு மாதிரிகளுடன் ஒப்பிடுகையில், மிஸ்ட்ரல் நீமோ மட்டுமே Apache2 உரிமத்துடன் உள்ள இலவச மாதிரியாகும்.

இது முன்பு இருந்த மிஸ்ட்ரல் 7B என்ற திறந்த மூல பெரிய மொழி மாதிரியின் மேம்பாடாகப் பார்க்கப்படுகிறது.

NeMo மாதிரியின் சில முக்கிய அம்சங்கள்:  

- *மேம்பட்ட டோக்கனாக்கல்:* இந்த மாதிரி பொதுவாக பயன்படும் tiktokenக்கு பதிலாக Tekken டோக்கனரைப் பயன்படுத்துகிறது. இது மேலும் மொழிகள் மற்றும் குறியீடுகளுக்கு சிறந்த செயல்திறனை வழங்குகிறது.

- *முன்னேற்றம் செய்தல்:* அடிப்படை மாதிரி முன்னேற்றத்திற்கு (finetuning) கிடைக்கிறது. இது மேலதிக பயன்பாட்டு சூழல்களுக்கு தகுதியான சுழற்சிகளை வழங்குகிறது.

- *இயல்புச் செயல்பாட்டு அழைப்பு* - மிஸ்ட்ரல் லார்ஜ் போல, இந்த மாதிரியும் செயல்பாட்டு அழைப்பில் பயிற்சி பெற்றிருக்கிறது. இதன் மூலம் திறந்த மூலமாக முதன்மையாக இதனை குறிப்பிடலாம்.

### டோக்கனர்களை ஒப்பிடுதல்

இந்த மாதிரியில், மிஸ்ட்ரல் நீமோ மற்றும் மிஸ்ட்ரல் லார்ஜ் இருவரும் டோக்கனாக்கலை எப்படிச் செய்கிறார்கள் என்பதைக் காண்போம்.

இரண்டு மாதிரிகளும் ஒரே ஊக்கவாக்கியத்தை எடுத்துக் கொள்கின்றன, ஆனால் NeMo மாதிரி மிஸ்ட்ரல் லார்ஜை விட குறைந்த டோக்கன்களை நிகரிட்டு வழங்கும்.

```bash
pip install mistral-common
```
  
```python 
# தேவையான பாக்கேஜ்களை இறக்குமதி செய்க:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# மிஸ்ட்ரால் டோக்கனைசரை ஏற்று

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# செய்திகளின் பட்டியலை டோக்கன்செய்
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

# டோக்கன்களின் எண்ணிக்கையை கணக்கிடு
print(len(tokens))
```
  
```python
# தேவையான தொகுதிகளை இறக்குமதி செய்யவும்:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral டோக்கனைசரை ஏற்றவும்

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# செய்திகளின் பட்டியலை டோக்கனைஸ் செய்யவும்
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

# டோக்கன்களின் எண்ணிக்கையை எண்ணவும்
print(len(tokens))
```
  
## கற்றல் இங்கு நிற்காது, பயணத்தை தொடருங்கள்

இந்த பாடத்தை முடித்த பிறகு, எங்கள் [ஜெனரேட்டிவ் AI கற்றல் தொகுப்பை](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) சென்று உங்கள் ஜெனரேட்டிவ் AI அறிவை மேம்படுத்திக் கொண்டிருங்கள்!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**தயாரிப்பு அறிவிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவையான [Co-op Translator](https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்தன்மைக்கு முயற்சித்தாலும், தானாக இயங்கும் மொழிபெயர்ப்புகளில் தவறுகள் அல்லது பிழைகள் இருக்க வாய்ப்பு உள்ளது. அசல் ஆவணம் அதன் சொந்த மொழியில் செவ்வனே பார்க்கப்பட வேண்டியது முக்கியம். மிக முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பை பரிந்துரைக்கிறோம். இந்த மொழிபெயர்ப்பின் பயன்பாட்டால் ஏற்படும் எந்தவொரு தவறான புரிதலுக்கும் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பானவர்கள் அல்ல.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->