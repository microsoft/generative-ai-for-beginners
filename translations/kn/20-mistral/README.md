<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-12-19T18:53:34+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "kn"
}
-->
# ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗಳೊಂದಿಗೆ ನಿರ್ಮಾಣ

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ ನಾವು ಈ ವಿಷಯಗಳನ್ನು ಆವರಿಸುವೆವು:  
- ವಿಭಿನ್ನ ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗಳನ್ನು ಅನ್ವೇಷಿಸುವುದು  
- ಪ್ರತಿ ಮಾದರಿಯ ಬಳಕೆ ಪ್ರಕರಣಗಳು ಮತ್ತು ಸಂದರ್ಭಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು  
- ಪ್ರತಿ ಮಾದರಿಯ ವಿಶಿಷ್ಟ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ತೋರಿಸುವ ಕೋಡ್ ಉದಾಹರಣೆಗಳು.

## ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗಳು

ಈ ಪಾಠದಲ್ಲಿ, ನಾವು 3 ವಿಭಿನ್ನ ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗಳನ್ನು ಅನ್ವೇಷಿಸುವೆವು:  
**ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್**, **ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್** ಮತ್ತು **ಮಿಸ್ಟ್ರಾಲ್ ನೆಮೊ**.

ಈ ಪ್ರತಿಯೊಂದು ಮಾದರಿಯೂ ಗಿಥಬ್ ಮಾದರಿ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಉಚಿತವಾಗಿ ಲಭ್ಯವಿದೆ. ಈ ನೋಟ್ಬುಕ್‌ನಲ್ಲಿನ ಕೋಡ್ ಈ ಮಾದರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಕೋಡ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡುತ್ತದೆ. ಗಿಥಬ್ ಮಾದರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು [AI ಮಾದರಿಗಳೊಂದಿಗೆ ಪ್ರೋಟೋಟೈಪಿಂಗ್](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) ಕುರಿತು ಹೆಚ್ಚಿನ ವಿವರಗಳು ಇಲ್ಲಿವೆ.

## ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ 2 (2407)  
ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ 2 ಪ್ರಸ್ತುತ ಮಿಸ್ಟ್ರಾಲ್‌ನ ಪ್ರಮುಖ ಮಾದರಿ ಮತ್ತು ಉದ್ಯಮ ಬಳಕೆಗೆ ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ.

ಈ ಮಾದರಿ ಮೂಲ ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್‌ಗೆ ಹೋಲಿಸಿದಾಗ ಅಪ್‌ಗ್ರೇಡ್ ಆಗಿದ್ದು,  
- ದೊಡ್ಡ ಕಾನ್ಟೆಕ್ಸ್ಟ್ ವಿಂಡೋ - 128k ವಿರುದ್ಧ 32k  
- ಗಣಿತ ಮತ್ತು ಕೋಡಿಂಗ್ ಕಾರ್ಯಗಳಲ್ಲಿ ಉತ್ತಮ ಕಾರ್ಯಕ್ಷಮತೆ - ಸರಾಸರಿ ಶುದ್ಧತೆ 76.9% ವಿರುದ್ಧ 60.4%  
- ಬಹುಭಾಷಾ ಕಾರ್ಯಕ್ಷಮತೆ ಹೆಚ್ಚಳ - ಭಾಷೆಗಳು: ಇಂಗ್ಲಿಷ್, ಫ್ರೆಂಚ್, ಜರ್ಮನ್, ಸ್ಪ್ಯಾನಿಷ್, ಇಟಾಲಿಯನ್, ಪೋರ್ಚುಗೀಸ್, ಡಚ್, ರಷ್ಯನ್, ಚೈನೀಸ್, ಜಪಾನೀಸ್, ಕೊರಿಯನ್, ಅರೇಬಿಕ್ ಮತ್ತು ಹಿಂದಿ.

ಈ ವೈಶಿಷ್ಟ್ಯಗಳೊಂದಿಗೆ, ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ ಉತ್ತಮವಾಗಿದೆ:  
- *ರಿಟ್ರಿವಲ್ ಆಗ್ಮೆಂಟೆಡ್ ಜನರೇಶನ್ (RAG)* - ದೊಡ್ಡ ಕಾನ್ಟೆಕ್ಸ್ಟ್ ವಿಂಡೋ ಕಾರಣ  
- *ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್* - ಈ ಮಾದರಿಯಲ್ಲಿ ಸ್ಥಳೀಯ ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್ ಇದೆ, ಇದು ಬಾಹ್ಯ ಸಾಧನಗಳು ಮತ್ತು API ಗಳೊಂದಿಗೆ ಸಂಯೋಜನೆಗೆ ಅನುಮತಿಸುತ್ತದೆ. ಈ ಕಾಲ್‌ಗಳನ್ನು ಸಮಾಂತರವಾಗಿ ಅಥವಾ ಕ್ರಮವಾಗಿ ಒಂದರ ನಂತರ ಒಂದನ್ನು ಮಾಡಬಹುದು.  
- *ಕೋಡ್ ಜನರೇಶನ್* - ಈ ಮಾದರಿ ಪೈಥಾನ್, ಜಾವಾ, ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್ ಮತ್ತು C++ ಜನರೇಶನ್‌ನಲ್ಲಿ ಉತ್ತಮವಾಗಿದೆ.

### ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ 2 ಬಳಸಿ RAG ಉದಾಹರಣೆ

ಈ ಉದಾಹರಣೆಯಲ್ಲಿ, ನಾವು ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ 2 ಅನ್ನು ಬಳಸಿ ಪಠ್ಯ ಡಾಕ್ಯುಮೆಂಟ್ ಮೇಲೆ RAG ಮಾದರಿಯನ್ನು ಚಾಲನೆ ಮಾಡುತ್ತಿದ್ದೇವೆ. ಪ್ರಶ್ನೆ ಕೊರಿಯನ್ ಭಾಷೆಯಲ್ಲಿ ಬರೆಯಲ್ಪಟ್ಟಿದ್ದು, ಲೇಖಕ ಕಾಲೇಜಿಗೆ ಹೋಗುವ ಮೊದಲು ಮಾಡಿದ ಚಟುವಟಿಕೆಗಳ ಬಗ್ಗೆ ಕೇಳುತ್ತದೆ.

ಇದು Cohere Embeddings ಮಾದರಿಯನ್ನು ಬಳಸಿ ಪಠ್ಯ ಡಾಕ್ಯುಮೆಂಟ್ ಮತ್ತು ಪ್ರಶ್ನೆಯ embeddings ರಚಿಸುತ್ತದೆ. ಈ ಮಾದರಿಗಾಗಿ faiss ಪೈಥಾನ್ ಪ್ಯಾಕೇಜ್ ಅನ್ನು ವೆಕ್ಟರ್ ಸ್ಟೋರ್ ಆಗಿ ಬಳಸುತ್ತದೆ.

ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗೆ ಕಳುಹಿಸಲಾದ ಪ್ರಾಂಪ್ಟ್‌ನಲ್ಲಿ ಪ್ರಶ್ನೆಗಳು ಮತ್ತು ಪ್ರಶ್ನೆಗೆ ಸಮಾನವಾದ ರಿಟ್ರೀವ್ ಮಾಡಿದ ಚಂಕ್‌ಗಳು ಎರಡೂ ಸೇರಿವೆ. ನಂತರ ಮಾದರಿ ಸಹಜ ಭಾಷೆಯ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನೀಡುತ್ತದೆ.

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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # ದೂರ, ಸೂಚ್ಯಂಕ
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
  
## ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್  
ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಮಿಸ್ಟ್ರಾಲ್ ಕುಟುಂಬದ ಮತ್ತೊಂದು ಮಾದರಿ, ಪ್ರೀಮಿಯರ್/ಉದ್ಯಮ ವರ್ಗದಡಿ ಬರುತ್ತದೆ. ಹೆಸರಿನಂತೆ, ಇದು ಸಣ್ಣ ಭಾಷಾ ಮಾದರಿ (SLM). ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಬಳಕೆಯ ಲಾಭಗಳು:  
- ಮಿಸ್ಟ್ರಾಲ್ LLM ಗಳಾದ ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ ಮತ್ತು ನೆಮೊಗೆ ಹೋಲಿಸಿದರೆ ವೆಚ್ಚ ಉಳಿತಾಯ - 80% ಬೆಲೆ ಇಳಿಕೆ  
- ಕಡಿಮೆ ವಿಳಂಬ - ಮಿಸ್ಟ್ರಾಲ್ LLM ಗಳಿಗಿಂತ ವೇಗವಾದ ಪ್ರತಿಕ್ರಿಯೆ  
- ಲವಚಿಕತೆ - ಕಡಿಮೆ ಸಂಪನ್ಮೂಲಗಳ ಅಗತ್ಯವಿರುವ ವಿವಿಧ ಪರಿಸರಗಳಲ್ಲಿ ನಿಯಮಿತವಾಗಿ ನಿಯೋಜಿಸಬಹುದು.

ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಉತ್ತಮವಾಗಿದೆ:  
- ಸಾರಾಂಶ, ಭಾವನಾತ್ಮಕ ವಿಶ್ಲೇಷಣೆ ಮತ್ತು ಅನುವಾದದಂತಹ ಪಠ್ಯ ಆಧಾರಿತ ಕಾರ್ಯಗಳಿಗೆ  
- ವೆಚ್ಚ ಪರಿಣಾಮಕಾರಿತ್ವದಿಂದಾಗಿ ನಿಯಮಿತ ವಿನಂತಿಗಳು ಇರುವ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ  
- ವಿಮರ್ಶೆ ಮತ್ತು ಕೋಡ್ ಸಲಹೆಗಳಂತಹ ಕಡಿಮೆ ವಿಳಂಬ ಕೋಡ್ ಕಾರ್ಯಗಳಿಗೆ

## ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಮತ್ತು ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ ಹೋಲಿಕೆ

ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಮತ್ತು ಲಾರ್ಜ್ ನಡುವಿನ ವಿಳಂಬ ವ್ಯತ್ಯಾಸವನ್ನು ತೋರಿಸಲು ಕೆಳಗಿನ ಸೆಲ್‌ಗಳನ್ನು ಚಾಲನೆ ಮಾಡಿ.

ನೀವು 3-5 ಸೆಕೆಂಡುಗಳ ನಡುವಿನ ಪ್ರತಿಕ್ರಿಯೆ ಸಮಯ ವ್ಯತ್ಯಾಸವನ್ನು ನೋಡಬಹುದು. ಅದೇ ಪ್ರಾಂಪ್ಟ್ ಮೇಲೆ ಪ್ರತಿಕ್ರಿಯೆಯ ಉದ್ದ ಮತ್ತು ಶೈಲಿಯನ್ನೂ ಗಮನಿಸಿ.

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
  
## ಮಿಸ್ಟ್ರಾಲ್ ನೆಮೊ

ಈ ಪಾಠದಲ್ಲಿ ಚರ್ಚಿಸಲಾದ ಇತರ ಎರಡು ಮಾದರಿಗಳಿಗಿಂತ ಭಿನ್ನವಾಗಿ, ಮಿಸ್ಟ್ರಾಲ್ ನೆಮೊ ಏಕೈಕ ಉಚಿತ ಮಾದರಿ ಆಗಿದ್ದು, Apache2 ಪರವಾನಗಿ ಹೊಂದಿದೆ.

ಇದು ಮಿಸ್ಟ್ರಾಲ್‌ನ ಮೊದಲ ಮುಕ್ತ ಮೂಲ LLM, ಮಿಸ್ಟ್ರಾಲ್ 7B ಗೆ ಅಪ್‌ಗ್ರೇಡ್ ಆಗಿ ಪರಿಗಣಿಸಲಾಗಿದೆ.

ನೆಮೊ ಮಾದರಿಯ ಕೆಲವು ಇತರ ವೈಶಿಷ್ಟ್ಯಗಳು:  

- *ಹೆಚ್ಚು ಪರಿಣಾಮಕಾರಿ ಟೋಕನೈಜೆಷನ್:* ಈ ಮಾದರಿ ಸಾಮಾನ್ಯವಾಗಿ ಬಳಸುವ tiktoken ಬದಲು Tekken ಟೋಕನೈಜರ್ ಅನ್ನು ಬಳಸುತ್ತದೆ. ಇದು ಹೆಚ್ಚಿನ ಭಾಷೆಗಳು ಮತ್ತು ಕೋಡ್ ಮೇಲೆ ಉತ್ತಮ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಒದಗಿಸುತ್ತದೆ.

- *ಫೈನ್ಟ್ಯೂನಿಂಗ್:* ಮೂಲ ಮಾದರಿ ಫೈನ್ಟ್ಯೂನಿಂಗ್‌ಗೆ ಲಭ್ಯವಿದೆ. ಇದು ಫೈನ್ಟ್ಯೂನಿಂಗ್ ಅಗತ್ಯವಿರುವ ಬಳಕೆ ಪ್ರಕರಣಗಳಿಗೆ ಹೆಚ್ಚು ಲವಚಿಕತೆಯನ್ನು ನೀಡುತ್ತದೆ.

- *ಸ್ಥಳೀಯ ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್* - ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್‌ನಂತೆ, ಈ ಮಾದರಿಯು ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್‌ನಲ್ಲಿ ತರಬೇತಿ ಪಡೆದಿದೆ. ಇದು ಮುಕ್ತ ಮೂಲ ಮಾದರಿಗಳಲ್ಲಿ ಮೊದಲನೆಯದಾಗಿ ಇದನ್ನು ಮಾಡುತ್ತಿರುವುದಾಗಿ ವಿಶಿಷ್ಟವಾಗಿದೆ.

### ಟೋಕನೈಜರ್‌ಗಳ ಹೋಲಿಕೆ

ಈ ಉದಾಹರಣೆಯಲ್ಲಿ, ನಾವು ಮಿಸ್ಟ್ರಾಲ್ ನೆಮೊ ಟೋಕನೈಜೇಶನ್ ಅನ್ನು ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ ಜೊತೆಗೆ ಹೋಲಿಸುತ್ತೇವೆ.

ಎರಡೂ ಮಾದರಿಗಳು ಅದೇ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ತೆಗೆದುಕೊಳ್ಳುತ್ತವೆ ಆದರೆ ನೆಮೊ ಕಡಿಮೆ ಟೋಕನ್ಗಳನ್ನು ಹಿಂತಿರುಗಿಸುವುದನ್ನು ನೀವು ನೋಡಬಹುದು.

```bash
pip install mistral-common
```
  
```python 
# ಅಗತ್ಯ ಪ್ಯಾಕೇಜುಗಳನ್ನು ಆಮದುಮಾಡಿ:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# ಮಿಸ್ಟ್ರಾಲ್ ಟೋಕನೈಜರ್ ಅನ್ನು ಲೋಡ್ ಮಾಡಿ

model_name = "open-mistral-nemo	"

tokenizer = MistralTokenizer.from_model(model_name)

# ಸಂದೇಶಗಳ ಪಟ್ಟಿಯನ್ನು ಟೋಕನೈಸ್ ಮಾಡಿ
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

# ಟೋಕನ್ಗಳ ಸಂಖ್ಯೆಯನ್ನು ಎಣಿಸಿ
print(len(tokens))
```
  
```python
# ಅಗತ್ಯ ಪ್ಯಾಕೇಜುಗಳನ್ನು ಆಮದುಮಾಡಿ:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# ಮಿಸ್ಟ್ರಾಲ್ ಟೋಕನೈಜರ್ ಅನ್ನು ಲೋಡ್ ಮಾಡಿ

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# ಸಂದೇಶಗಳ ಪಟ್ಟಿಯನ್ನು ಟೋಕನೈಸ್ ಮಾಡಿ
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

# ಟೋಕನ್ಗಳ ಸಂಖ್ಯೆಯನ್ನು ಎಣಿಸಿ
print(len(tokens))
```
  
## ಕಲಿಕೆ ಇಲ್ಲಿ ನಿಲ್ಲುವುದಿಲ್ಲ, ಪ್ರಯಾಣವನ್ನು ಮುಂದುವರೆಸಿ

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನಮ್ಮ [ಜನರೇಟಿವ್ AI ಕಲಿಕೆ ಸಂಗ್ರಹ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ಅನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ನಿಮ್ಮ ಜನರೇಟಿವ್ AI ಜ್ಞಾನವನ್ನು ಮುಂದುವರೆಸಿ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->