# மிஸ்ட்ரல் மாதிரிகளுடன் கட்டமைக்கல்

## அறிமுகம்

இந்த பாடத்தில் பின்வரும் விவரங்கள் கூறப்படும்:
- மிஸ்ட்ரல் மாதிரிகளின் வேறுபாடுகளை ஆராய்தல்
- ஒவ்வொரு மாதிரிக்கும் பயன்பாடுகள் மற்றும் சூழல்களை புரிந்துகொள்வது
- ஒவ்வொரு மாதிரிக்கும் தனித்துவமான அம்சங்களை காட்டும் குறியீட்டு உதாரணங்களை ஆராய்தல்.

## மிஸ்ட்ரல் மாதிரிகள்

இந்த பாடத்தில், நாங்கள் 3 மிஸ்ட்ரல் மாதிரிகளை ஆராய்வோம்:
**மிஸ்ட்ரல் லார்ஜ்**, **மிஸ்ட்ரல் ஸ்மால்** மற்றும் **மிஸ்ட்ரல் நீமோ**.

இந்த மாதிரிகள் அனைத்தும் [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) இல் இலவசமாக கிடைப்பதுடன், இந்த நோட்புக்கில் உள்ள குறியீடு இந்த மாதிரிகளைப் பயன்படுத்தி இயங்கும்.

> **கவனம்:** GitHub Models 2026 ஜூலை இறுதியில் ஓய்வு பெறுகிறது. [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ஐ பயன்படுத்தி AI மாதிரிகளுடன் முன்மாதிரிகள் உருவாக்குவது பற்றிய மேலதிக விவரங்கள் இங்கே உள்ளன.


## மிஸ்ட்ரல் லார்ஜ் 2 (2407)
மிஸ்ட்ரல் லார்ஜ் 2 தற்போது மிஸ்ட்ரல் நிறுவனத்தின் முக்கிய மாதிரி மற்றும் நிறுவன பயன்பாட்டிற்கு உருவாக்கப்பட்டுள்ளது.

இந்த மாதிரி அசல் மிஸ்ட்ரல் லார்ஜை மேம்படுத்தி வழங்குகிறது 
-  பெரிய உள்ளடக்க சாளரம் - 128k எதிர்ப்பு 32k 
-  கணித மற்றும் குறியீட்டு பணிகளில் சிறந்த செயல்திறன் - சராசரி துல்லியம் 76.9% எதிர்ப்பு 60.4%
-  அதிகரிக்கப்பட்ட பல்மொழி செயல்திறன் - மொழிகள்: ஆங்கிலம், பிரஞ்சு, ஜெர்மன், ஸ்பானிஷ், இத்தாலி, போர்ச்சுகீஸ், டச்சு, ரஷ்யன், சீனம், ஜப்பானீஸ், கோரியன், அரபிக் மற்றும் ஹிந்தி.

இந்த அம்சங்களுடன், மிஸ்ட்ரல் லார்ஜ் சிறந்து விளங்குகிறது
- *Retrieval Augmented Generation (RAG)* - பெரிய உள்ளடக்க சாளரத்தால்
- *Function Calling* - இந்த மாதிரியில் சொந்த செயல்பாட்டு அழைப்புகள் உள்ளன, இது வெளியிடமான கருவிகள் மற்றும் API களுடன் இணைக்க அனுமதிக்கிறது. இந்த அழைப்புகள் ஒன்றுக்கு பின் ஒன்று அல்லது ஒரே நேரத்தில் செய்யப்படலாம்.
- *Code Generation* - Python, Java, TypeScript மற்றும் C++ உருவாக்கத்தில் சிறந்து விளங்கும்.

### மிஸ்ட்ரல் லார்ஜ் 2 பயன்படுத்தி RAG எடுத்துக்காட்டு

இந்த எடுத்துக்காட்டில், நாம் மிஸ்ட்ரல் லார்ஜ் 2 ஐ பயன்படுத்தி ஒரு உரை ஆவணத்தில் RAG முறைப் படத்தைக் இயக்குகின்றோம். கேள்வி கோரியன் மொழியில் எழுதப்பட்டு எழுத்தாளர் கல்லூரிக்கு முன் செய்த செயல்கள் பற்றி கேட்டுக்கொள்கிறது.

இது Cohere Embeddings Model ஐ பயன்படுத்தி உரை ஆவணத்தையும் கேள்வியையும் உள்ளடக்கங்கள் உருவாக்குகிறது. இந்த மாதிரிக்கு faiss Python தொகுப்பை வெக்டர் இடைமுகமாக பயன்படுத்துகிறது.

மிஸ்ட்ரல் மாதிரிக்கு அனுப்பப்படும் முன்பொது கேள்விகளும், கேள்வியுடன் தொடர்புடைய எடுக்கும் பகுதிகளும் அடங்கும். பின்னர் மாதிரி இயற்கை மொழி பதிலை வழங்குகிறது.

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

# உங்கள் Microsoft Foundry திட்டத்தின் "கண்ணோட்டம்" பக்கத்தில் இருந்து இதை பெறவும்
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

## மிஸ்ட்ரல் ஸ்மால்
மிஸ்ட்ரல் ஸ்மால் மிஸ்ட்ரல் குடும்பத்தின் மற்றொரு மாதிரி ஆகும், இது முதலிட/நிறுவன வகைக்கு உட்பட்டது. அதன் பெயரைப்படி, இது ஒரு சிறிய மொழி மாதிரியாகும் (SLM). மிஸ்ட்ரல் ஸ்மால் பயன்படுத்துவதன் நன்மைகள்:
- மிஸ்ட்ரல் லார்ஜ் மற்றும் நீமோ போன்ற LLM கள் கொண்டிருந்து செலவு குறைவாகும் - 80% விலை இழிவு
- குறைந்த தாமதம் - மிஸ்ட்ரல் LLM களுடன் ஒப்பிடுகையில் வேகமான பதில்
- நெகிழ்வானது - தேவையான வளங்களுக்கு குறைவான கட்டுப்பாடுகளுடன் பல விதமான சூழல்களில் பரவல் செய்யக்கூடியது.


மிஸ்ட்ரல் ஸ்மால் சிறந்தது:
- உரை அடிப்படையிலான பணிகள், போன்றவை சுருக்கம், உணர்வு பகுப்பு மற்றும் மொழிபெயர்ப்பு.
- செலவு சிக்கனமானதால் அடிக்கடி கோரிக்கை செய்யப்படும் பயன்பாடுகள்
- குறைந்த தாமதமாக கூட்டு குறியீட்டு பணிகள், ஆய்வு மற்றும் குறியீட்டு பரிந்துரைகள்

## மிஸ்ட்ரல் ஸ்மால் மற்றும் மிஸ்ட்ரல் லார்ஜ் ஒப்பீடு

மிஸ்ட்ரல் ஸ்மால் மற்றும் லார்ஜ் இடையேயான தாமத வேறுபாடுகளை காட்ட கீழ்காணும் செல்கள் இயக்கவும்.

3-5 விநாடிகளுக்குள் பதிலளிக்கும் வேறுபாடு காணப்படும். அதே முன்பொதுவில் பதில் நீளம் மற்றும் பாணி வேறுபாடுகளையும் கவனியுங்கள்.

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

## மிஸ்ட்ரல் நீமோ

மிஸ்ட்ரல் நீமோ இந்த பாடத்தில் விவாதிக்கப்பட்ட மற்ற இரண்டு மாதிரிகளுடன் ஒப்பிடுகையில், Apache2 உரிமம் கொண்ட ஒரே இலவச மாதிரியாகும்.

இது மிஸ்ட்ரல் நிறுவனத்தால் முன்பு வெளியிடப்பட்ட திறந்த மூல LLM, மிஸ்ட்ரல் 7B க்கு மேம்படுத்தலாகக் கருதப்படுகிறது.

நீமோ மாதிரியின் சில மற்ற அம்சங்கள்:

- *மேம்பட்ட டோக்கன் பிரிப்புஉத்தரவாதம்:* இந்த மாதிரி பொதுவாக பயன்படுத்தப்படும் tiktokenக்கு பதிலாக Tekken டோக்கனைசரைப் பயன்படுத்துகிறது. இது பல மொழிகளிலும் குறியீட்டிலும் சிறந்த செயல்திறன் அளிக்கிறது.

- *நுட்ப தொகுப்புப்பின் மேம்பாடு:* அடிப்படை மாதிரி நுட்பத் தொகுப்பிற்கு கிடைக்கிறது. இது நுட்பத் தொகுப்பு தேவைப்படும் பயன்பாடுகளுக்கு அதிக நெகிழ்வுத்தன்மையை வழங்குகிறது.

- *சொந்த செயல்பாட்டு அழைப்புகள்* - மிஸ்ட்ரல் லார்ஜ் போல, இந்த மாதிரியும் செயல்பாட்டு அழைப்பில் பயிற்சி பெற்றுள்ளது. இது திறந்த மூல மாதிரிகளில் முதன்முதலாக ஒன்று.


### டோக்கனைசர்கள் ஒப்பீடு

இந்த எடுத்துக்காட்டில், மிஸ்ட்ரல் நீமோ எப்படி டோக்கன்களை நிர்வகிக்கிறது என்று மிஸ்ட்ரல் லார்ஜுடன் ஒப்பிட்டு பார்க்கப் போகிறோம்.

இரு எடுத்துக்காட்டுகளும் ஒரே முன்பொதுவைப் பயன்படுத்தினாலும், நீமோ மாதிரி மிஸ்ட்ரல் லார்ஜ் மாதிரைக்குக் குறைவான டோக்கன்களைத் திருப்பி அளிக்கும்.

```bash
pip install mistral-common
```

```python 
# தேவையான தொகுப்புகளை இறக்குமதி செய்க:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral டோக்கனைசரை ஏற்றுகொள்

model_name = "open-mistral-nemo"

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

# டோக்கன்களின் எண்ணிக்கையை எண்ணுக
print(len(tokens))
```

```python
# தேவையான தொகுப்புகளை இறக்குமதி செய்க:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral tokenizeஅரை ஏற்றுக

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# செய்தி பட்டியலை tokenize செய்க
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

# tokenகளின் எண்ணிக்கையை எண்ணுக
print(len(tokens))
```

## கற்பது இங்கே நிறையாது, பயணத்தை தொடருங்கள்

இந்த பாடத்தை முடித்த பிறகு, உங்கள் உருவாக்கும் AI அறிவை மேம்படுத்த [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ஐக் காணவும்!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->