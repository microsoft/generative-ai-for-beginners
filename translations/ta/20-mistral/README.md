<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-10-11T11:22:25+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "ta"
}
-->
# மிஸ்ட்ரல் மாடல்களுடன் கட்டமைத்தல்

## அறிமுகம்

இந்த பாடத்தில் நாம் கற்கப்போகிறோம்:
- மிஸ்ட்ரல் மாடல்களை ஆராய்வது
- ஒவ்வொரு மாடலின் பயன்பாடுகள் மற்றும் சூழல்களைப் புரிந்துகொள்வது
- ஒவ்வொரு மாடலின் தனித்துவமான அம்சங்களை காட்டும் குறியீட்டு மாதிரிகள்.

## மிஸ்ட்ரல் மாடல்கள்

இந்த பாடத்தில், நாம் மிஸ்ட்ரல் மாடல்களின் மூன்று வெவ்வேறு வகைகளை ஆராய்வோம்:  
**மிஸ்ட்ரல் லார்ஜ்**, **மிஸ்ட்ரல் ஸ்மால்**, மற்றும் **மிஸ்ட்ரல் நீமோ**.

இந்த மாடல்கள் அனைத்தும் Github Model சந்தையில் இலவசமாக கிடைக்கின்றன. இந்த நோட்புக்கில் உள்ள குறியீடு இந்த மாடல்களை பயன்படுத்தி செயல்படுத்தப்படும். Github Models-ஐ பயன்படுத்தி [AI மாடல்களுடன் முன்னோட்டம் செய்வது](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) குறித்த மேலும் விவரங்கள் இங்கே உள்ளன.

## மிஸ்ட்ரல் லார்ஜ் 2 (2407)

மிஸ்ட்ரல் லார்ஜ் 2 தற்போது மிஸ்ட்ரல் நிறுவனத்தின் முக்கிய மாடலாகும் மற்றும் நிறுவன பயன்பாட்டிற்காக வடிவமைக்கப்பட்டுள்ளது.

இந்த மாடல் மிஸ்ட்ரல் லார்ஜின் முதன்மை பதிப்பை மேம்படுத்துகிறது:
- பெரிய சூழல் சாளரம் - 128k vs 32k
- கணிதம் மற்றும் குறியீட்டு பணிகளில் மேம்பட்ட செயல்திறன் - சராசரி துல்லியம் 76.9% vs 60.4%
- பல மொழிகளில் மேம்பட்ட செயல்திறன் - மொழிகள்: ஆங்கிலம், பிரெஞ்சு, ஜெர்மன், ஸ்பானிஷ், இத்தாலியன், போர்ச்சுகீஸ், டச்சு, ரஷ்யன், சீனம், ஜப்பானியம், கொரியன், அரபி, மற்றும் இந்தி.

இந்த அம்சங்களுடன், மிஸ்ட்ரல் லார்ஜ் சிறப்பாக செயல்படுகிறது:
- *Retrieval Augmented Generation (RAG)* - பெரிய சூழல் சாளரத்தால்
- *Function Calling* - இந்த மாடல் இயல்பாகவே function calling-ஐ ஆதரிக்கிறது, இது வெளிப்புற கருவிகள் மற்றும் APIகளுடன் ஒருங்கிணைக்க உதவுகிறது. இந்த அழைப்புகள் ஒரே நேரத்தில் அல்லது தொடர்ச்சியாக செய்யப்படலாம்.
- *Code Generation* - Python, Java, TypeScript மற்றும் C++ குறியீட்டில் சிறப்பாக செயல்படுகிறது.

### RAG உதாரணம் மிஸ்ட்ரல் லார்ஜ் 2 பயன்படுத்தி

இந்த உதாரணத்தில், மிஸ்ட்ரல் லார்ஜ் 2-ஐ பயன்படுத்தி ஒரு RAG முறை ஒரு உரை ஆவணத்தில் செயல்படுத்தப்படுகிறது. கேள்வி கொரிய மொழியில் எழுதப்பட்டுள்ளது மற்றும் கல்லூரிக்கு முன் ஆசிரியரின் செயல்பாடுகளைப் பற்றி கேட்கிறது.

இது Cohere Embeddings Model-ஐ பயன்படுத்தி உரை ஆவணத்தின் மற்றும் கேள்வியின் embeddings உருவாக்குகிறது. இந்த மாதிரிக்காக, faiss Python தொகுப்பை ஒரு வெக்டர் சேமிப்பகமாக பயன்படுத்துகிறது.

மிஸ்ட்ரல் மாடலுக்கு அனுப்பப்படும் ப்ராம்ப்ட், கேள்விகளையும் கேள்விக்கு ஒத்த துண்டுகளையும் உள்ளடக்கியது. மாடல் பின்னர் ஒரு இயல்பான மொழி பதிலை வழங்குகிறது.

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
  

## மிஸ்ட்ரல் ஸ்மால்

மிஸ்ட்ரல் ஸ்மால் என்பது மிஸ்ட்ரல் மாடல்களின் குடும்பத்தில் மற்றொரு மாடலாகும், இது முதன்மை/நிறுவன வகையைச் சேர்ந்தது. பெயரே சொல்வது போல, இந்த மாடல் ஒரு சிறிய மொழி மாடல் (SLM) ஆகும். மிஸ்ட்ரல் ஸ்மாலின் நன்மைகள்:  
- மிஸ்ட்ரல் லார்ஜ் மற்றும் NeMo போன்ற மாடல்களுடன் ஒப்பிடும்போது செலவுச்செலுத்தல் - 80% செலவுக் குறைப்பு  
- குறைந்த தாமதம் - மிஸ்ட்ரல் LLMகளுடன் ஒப்பிடும்போது வேகமான பதில்  
- நெகிழ்வானது - குறைந்த வளங்களுடன் பல சூழல்களில் பயன்படுத்த முடியும்.  

மிஸ்ட்ரல் ஸ்மால் சிறந்தது:  
- சுருக்கம், உணர்ச்சி பகுப்பாய்வு மற்றும் மொழிபெயர்ப்பு போன்ற உரை அடிப்படையிலான பணிகளுக்கு.  
- அதன் செலவுச்செலுத்தல் காரணமாக அடிக்கடி கோரிக்கைகள் செய்யப்படும் பயன்பாடுகளுக்கு.  
- குறைந்த தாமத குறியீட்டு பணிகள், உதாரணமாக மதிப்பாய்வு மற்றும் குறியீட்டு பரிந்துரைகள்.  

## மிஸ்ட்ரல் ஸ்மால் மற்றும் மிஸ்ட்ரல் லார்ஜ் ஒப்பீடு

மிஸ்ட்ரல் ஸ்மால் மற்றும் லார்ஜ் மாடல்களுக்கிடையிலான தாமத வேறுபாடுகளை காட்ட, கீழே உள்ள செல்களை இயக்கவும்.

ஒரே ப்ராம்ப்டில் பதிலளிக்கும் நேரங்களில் 3-5 விநாடிகளுக்குள் வேறுபாடு காணலாம். பதில்களின் நீளங்கள் மற்றும் பாணியையும் கவனிக்கவும்.  

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

இந்த பாடத்தில் விவாதிக்கப்பட்ட மற்ற இரண்டு மாடல்களுடன் ஒப்பிடும்போது, மிஸ்ட்ரல் நீமோ மட்டுமே Apache2 உரிமத்துடன் இலவசமாக கிடைக்கிறது.

இது மிஸ்ட்ரல் நிறுவனத்தின் முந்தைய திறந்த மூல LLM, மிஸ்ட்ரல் 7B-க்கு மேம்படுத்தலாக பார்க்கப்படுகிறது.

NeMo மாடலின் சில பிற அம்சங்கள்:  
- *மேம்பட்ட டோக்கனேஷன்:* இந்த மாடல் பொதுவாக பயன்படுத்தப்படும் tiktoken-க்கு பதிலாக Tekken tokenizer-ஐ பயன்படுத்துகிறது. இது பல மொழிகள் மற்றும் குறியீட்டில் சிறந்த செயல்திறனை வழங்குகிறது.  
- *Finetuning:* அடிப்படை மாடல் finetuning செய்ய கிடைக்கிறது. இது finetuning தேவைப்படும் பயன்பாடுகளுக்கு அதிக நெகிழ்வுத்தன்மையை வழங்குகிறது.  
- *இயல்பான Function Calling* - மிஸ்ட்ரல் லார்ஜ் போலவே, இந்த மாடலும் function calling-ல் பயிற்சி பெற்றுள்ளது. இது இதனை திறந்த மூல மாடல்களில் முதன்மையானதாக ஆக்குகிறது.  

### டோக்கனேஷன் ஒப்பீடு

இந்த மாதிரியில், மிஸ்ட்ரல் நீமோ மாடல் மற்றும் மிஸ்ட்ரல் லார்ஜ் மாடலின் டோக்கனேஷன் செயல்பாட்டை ஒப்பிடுவோம்.

இரண்டு மாதிரிகளும் ஒரே ப்ராம்ப்டை எடுத்துக்கொள்கின்றன, ஆனால் நீமோ மாடல் மிஸ்ட்ரல் லார்ஜ் மாடலுடன் ஒப்பிடும்போது குறைவான டோக்கன்களை திருப்பி வழங்குவதை நீங்கள் காணலாம்.  

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
  

## கற்றல் இங்கே நிற்காது, பயணத்தை தொடருங்கள்

இந்த பாடத்தை முடித்த பிறகு, எங்கள் [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)-ஐ பார்வையிடுங்கள், உங்கள் Generative AI அறிவை மேலும் மேம்படுத்த!

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.