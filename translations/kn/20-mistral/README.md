# ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗಳೊಂದಿಗೆ ನಿರ್ಮಿಸುವುದು

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ ಕಾಣಿಸುತ್ತಿರುವವು:
- ವಿಭಿನ್ನ ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗಳನ್ನು ಅನ್ವೇಷಿಸುವುದು
- ಪ್ರತಿ ಮಾದರಿಯ ಬಳಕೆ-ಕೇಸುಗಳು ಮತ್ತು ಸಂದರ್ಭದಲ್ಲಿ ಅರಿತುಕೊಳ್ಳುವುದು
- ಪ್ರತಿ ಮಾದರಿಯ ವಿಶಿಷ್ಟ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ತೋರಿಸುವ ಕೋಡ್ ಉದಾಹರಣೆಗಳನ್ನು ಅನ್ವೇಷಿಸುವುದು.

## ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗಳು

ಈ ಪಾಠದಲ್ಲಿ, ನಾವು ಮೂರು ವಿಭಿನ್ನ ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗಳನ್ನು ಅನ್ವೇಷಿಸುವೆವು:
**ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್**, **ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್** ಮತ್ತು **ಮಿಸ್ಟ್ರಾಲ್ ನೆಮೊ**.

ಪ್ರತಿ ಈ ಮಾದರಿಗಳು ಗಿಥಬ್ ಮಾದರಿ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಉಚಿತವಾಗಿ ಲಭ್ಯವ আছে. ಈ ನೋಟುಬುಕುಲ್ಲಿನ ಕೋಡ್ ಈ ಮಾದರಿಗಳನ್ನು ಬಳಸುವ ಮೂಲಕ ಚಲಿಸುತ್ತದೆ. ಗಿಥಬ್ ಮಾದರಿಗಳನ್ನು [AI ಮಾದರಿಗಳೊಂದಿಗೆ ಪ್ರೋಟೋಟೈಪಿಂಗ್](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) ಮಾಡಲು ಹೆಚ್ಚಿನ ವಿವರಗಳು ಇಲ್ಲಿವೆ.

## ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ 2 (2407)
ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ 2 ಪ್ರಸ್ತುತ ಮಿಸ್ಟ್ರಾಲ್‌ನ ಪ್ರಮುಖ ಮಾದರಿಯಾಗಿದ್ದು, ಉದ್ಯಮ ಬಳಕೆಗಾಗಿ ವಿನ್ಯಾಸಗೊಳ್ಳಲಾಗಿದೆ.

ಈ ಮಾದರಿ ಮೂಲ ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್‌ನ ಅಪ್‌ಗ್ರೇಡ್ ಆಗಿದ್ದು, 
-  ದೊಡ್ಡ ಕಾನ್ಟೆಕ್ಸ್ಟ್ ವಿಂಡೋ - 128k ವಿರುದ್ಧ 32k
-  ಗಣಿತ ಮತ್ತು ಕೋಡಿಂಗ್ ಕಾರ್ಯಗಳಲ್ಲಿ ಉತ್ತಮ ಕಾರ್ಯಕ್ಷಮತೆ - ಸರಾಸರಿ 76.9% ಶುದ್ಧತೆ ವಿರುದ್ಧ 60.4%
-  ಹೆಚ್ಚಾದ ಬಹುಭಾಷಾ ಕಾರ್ಯಕ್ಷಮತೆ - ಭಾಷೆಗಳು: ಇಂಗ್ಲೀಷ್, ಫ್ರೆಂಚ್, ಜರ್ಮನ್, ಸ್ಪ್ಯಾನಿಷ್, ಇಟಲಿಯನ್, ಪೋರ್ಚುಗೀಸ್, ಡಚ್, ರಶಿಯನ್, ಚೈನೀಸ್, ಜಪಾನೀಸ್, ಕೊರಿಯನ್, ಅರೇಬಿಕ್ ಮತ್ತು ಹಿಂದಿ.

ಈ ವೈಶಿಷ್ಟ್ಯಗಳೊಂದಿಗೆ, ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ ಕೆಳಗಿನ ಕಾರ್ಯಗಳಲ್ಲಿ ಉತ್ತಮವಾಗಿದೆ
- *ರಿಟ್ರಿವಲ್ ಆಗ್ಮೆಂಟೆಡ್ Jennaration (RAG)* - ಹೆಚ್ಚಿನ ಕಾನ್ಟೆಕ್ಸ್ಟ್ ವಿಂಡೋ ಕಾರಣದಿಂದ
- *ಫಂಕ್ಷನ್ ಕರೆ* - ಈ ಮಾದರಿಯಲ್ಲಿ ಸ್ಥಳೀಯ ಫಂಕ್ಷನ್ ಕರೆಗಳಿವೆ, ಇದು ಬಾಹ್ಯ ಉಪಕರಣಗಳು ಮತ್ತು APIಗಳೊಂದಿಗೆ ಏಕೀಕರಣಕ್ಕೆ ಅನುಮತಿಸುತ್ತದೆ. ಈ ಕರೆಗಳನ್ನು ಪರಸ್ಪರ ಏಕಕಾಲದಲ್ಲಿ ಅಥವಾ ಕ್ರಮವಾಗಿ ಒಂದು ನಂತರ ಒಂದಾಗಿ ಮಾಡಲು ಸಾಧ್ಯ.
- *ಕೋಡ್ Jennaration* - ಈ ಮಾದರಿ ಪೈಥಾನ್, ಜಾವಾ, ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್ ಮತ್ತು C++ Jennaration ನಲ್ಲಿ ಉತ್ತಮ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ತೋರಿಸುತ್ತದೆ.

### ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ 2 ಬಳಸಿ RAG ಉದಾಹರಣೆ

ಈ ಉದಾಹರಣೆಯಲ್ಲಿ, ನಾವು ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ 2 ಅನ್ನು RAG ಮಾದರಿಯಲ್ಲಿ ಪಠ್ಯ ಡಾಕ್ಯುಮೆಂಟ್ ಮೇಲೆ ಚಲಿಸುತ್ತಿದ್ದೇವೆ. ಪ್ರಶ್ನೆ ಕೊರಿಯನ್ ಭಾಷೆಯಲ್ಲಿ ಬರೆಯಲಾಗಿದೆ ಮತ್ತು ಲೇಖಕರ ಕಾಲೇಜಿಗೆ ಹೋಗುವ ಮೊದಲು ನಡೆಸಿದ ಚಟುವಟಿಕೆಗಳ ಬಗ್ಗೆ ಕೇಳುತ್ತದೆ.

ಇದು Cohere Embeddings ಮಾದರಿಯನ್ನು ಬಳಸಿಕೊಂಡು ಪಠ್ಯ ಡಾಕ್ಯುಮೆಂಟ್ ಮತ್ತು ಪ್ರಶ್ನೆಯ ಎంబೆಡ್ಡಿಂಗ್‌ಗಳನ್ನು ಸೃಷ್ಟಿಸುತ್ತದೆ. ಈ ನುಡಿಮುತ್ತು, faiss ಪೈಥಾನ್ ಪ್ಯಾಕೇಜ್ ಅನ್ನು ವೆಕ್ಟರ್ ಸ್ಟೋರ್ ಆಗಿ ಬಳಸುತ್ತದೆ.

ಮಾದರಿಗೆ ಕಳುಹಿಸುವ ಪ್ರಾಂಪ್ಟ್‌ನಲ್ಲಿ ಪ್ರಶ್ನೆಗಳು ಮತ್ತು ಪ್ರಶ್ನೆಯ ಹೊತ್ತುಶೋಧ್ಯರಾದ ಚಂಕ್ಗಳನ್ನು ಒಳಗೊಂಡಿದೆ. ನಂತರ ಮಾದರಿ ಪ್ರಕೃತಭಾಷಾ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನೀಡುತ್ತದೆ.

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
ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಮಿಸ್ಟ್ರಾಲ್ ಕುಟುಂಬದ ಮತ್ತೊಂದು ಪ್ರೀಮಿಯರ್/ಉದ್ಯಮ ಪ್ರಕಾರದ ಮಾದರಿಯಾಗಿದೆ. ಹೆಸರಿನಿಂದ ಕಾಣಿಸಿಕೊಳ್ಳುತ್ತದೆಂತೆ, ಇದು ಸಣ್ಣ ಭಾಷಾ ಮಾದರಿ (SLM).

ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಬಳಸುವ ಲಾಭಗಳು:
- ಮಿಸ್ಟ್ರಾಲ್ LLMಗಳು (ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ ಮತ್ತು ನೆಮೊ)ಗೆ ಹೋಲಿಸಿದಾಗ ವೆಚ್ಚ ಉಳಿತಾಯ - 80% ಬೆಲೆ ಇಳಿಕೆ
- ಕಡಿಮೆ ವಿಳಂಬ - ಮಿಸ್ಟ್ರಾಲ್ LLMಗಳಿಗೆ ಹೋಲಿಸಿದಾಗ ವೇಗವಾದ ಪ್ರತಿಕ್ರಿಯೆ
- ಲವಚಿಕತೆ - ಕಡಿಮೆ ಸಂಪನ್ಮೂಲಗಳ ಅಗತ್ಯವಿರುವ ವಿವಿಧ ಪರಿಸರಗಳಲ್ಲಿ ನಿಯಂತ್ರಣ ಕಡಿಮೆ ಹೊಂದಿ ನಿಯೋಜಿಸಬಹುದು.

ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಯೋಗ್ಯವಾಗಿದೆ:
- ಸಂಕ್ಷಿಪ್ತೀಕರಣ, ಭಾವಾವ್ಯ ವಿವರಣೆ ಮತ್ತು ಭಾಷಾಂತರಿಸುವಂತಿದ ಚಾರಿತ್ರ್ಯ ಪಠ್ಯ ಕಾರ್ಯಗಳಿಗೆ
- ಹೆಚ್ಚಾಗಿ ವಿನಂತಿಗಳನ್ನು ಮಾಡಲು ಅನುವು ಮಾಡಿಕೊಡುವ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ ವೆಚ್ಚದ ದೃಷ್ಟಿಕೋನದಿಂದ
- ಕಡಿಮೆ ವಿಳಂಬ ಕೋಡ್ ಕಾರ್ಯಗಳು, ಉದಾಹರಣೆಗೆ ವಿಮರ್ಶನ ಮತ್ತು ಕೋಡ್ ಸಲಹೆಗಳು.

## ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಮತ್ತು ಲಾರ್ಜ್ ಹೋಲಿಕೆ

ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಮತ್ತು ಲಾರ್ಜ್ ನಡುವಿನ ವಿಳಂಬ ವ್ಯತ್ಯಾಸವನ್ನು ತೋರಿಸಲು ಕೆಳಗಿನ ಕೋಶಗಳನ್ನು ಚಲಿಸಿ.

3-5 ಸೆಕೆಂಡುಗಳ ವ್ಯಾಪ್ತಿಯು ಪ್ರತಿಕ್ರಿಯೆಯ ಸಮಯದಲ್ಲಿ ವ್ಯತ್ಯಾಸ ಕಾಣಿಸಬೇಕು. ಹಾಗೆಯೇ ಪ್ರತಿಕ್ರಿಯೆಯ ಉದ್ದ ಮತ್ತು ಶೈಲಿಯನ್ನು ಒಂದೇ ಪ್ರಾಂಪ್ಟ್ ಮೇಲೆ ಗಮನಿಸಿ.

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

ಈ ಪಾಠದಲ್ಲಿ ಚರ್ಚಿಸಲಾದ ಇತರ ಎರಡು ಮಾದರಿಗಳಿಗಿಂತ ಭಿನ್ನವಾಗಿ, ಮಿಸ್ಟ್ರಾಲ್ ನೆಮೊ ಏಕಮಾತ್ರ ಉಚಿತ ಮಾದರಿ ಆಗಿದ್ದು, Apache2 ಪರವಾನಿಗೆ ಹೊಂದಿದೆ.

ಇದನ್ನು ಮಿಸ್ಟ್ರಾಲ್‌ನ ಮುಂಚಿನ open source LLM, ಮಿಸ್ಟ್ರಾಲ್ 7Bಗೆ ಅಪ್‌ಗ್ರೇಡ್ ಎಂದು ನೋಡಲಾಗುತ್ತದೆ.

ನೆಮೊ ಮಾದರಿಯ ಕೆಲವು ಇತರ ವೈಶಿಷ್ಟ್ಯಗಳು:

- *ಹೆಚ್ಚಿನ ಕಾರ್ಯಕ್ಷಮ ಟೋಕನೈಸೇಷನ್:* ಈ ಮಾದರಿ ಸಾಮಾನ್ಯವಾಗಿ ಬಳಕೆಯಲ್ಲಿರುವ tiktokenನಿಂದ ಬಿಟ್ಟ Tekken ಟೋಕನೈಸರ್ ಬಳಸುತ್ತದೆ. ಇದರಿಂದ ಹೆಚ್ಚು ಭಾಷೆ ಮತ್ತು ಕೋಡ್ ಮೇಲೆ ಉತ್ತಮ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಒದಗಿಸುತ್ತದೆ.

- *ಫೈನ್ಟ್ಯೂನಿಂಗ್:* ಬೇಸ್ ಮಾದರಿ ಫೈನ್ಟ್ಯೂನಿಂಗ್‌ಗೆ ಲಭ್ಯವಿದೆ. ಇದು ಫೈನ್ಟ್ಯೂನಿಂಗ್‌ನಲ್ಲಿ ಅಗತ್ಯವಿರುವ ಬಳಕೆ-ದೃಶ್ಯಗಳಿಗೆ ಹೆಚ್ಚುವರಿ ಹವ್ಯಾಸ ದೊರಕಿಸುತ್ತದೆ.

- *ಸ್ಥಳೀಯ ಫಂಕ್ಷನ್ ಕರೆ* - ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್‌ನಂತೆ, ಈ ಮಾದರಿಯೂ ಫಂಕ್ಷನ್ ಕರೆ ತರಬೇತಿಯನ್ನು ಪಡೆದಿದೆ. ಇದರಿಂದ ಇದು ಮೊದಲೊಮ್ಮೆ ಉಚಿತ open source ಮಾದರಿಗಳಲ್ಲಿ ಒಂದು ವಿಶೇಷವಾಗಿರುತ್ತದೆ.

### ಟೋಕನೈಸರ್‌ಗಳ ಹೋಲಿಕೆ

ಈ ಉದಾಹರಣೆಯಲ್ಲಿ, ನಾವು ಮಿಸ್ಟ್ರಾಲ್ ನೆಮೊ ಮತ್ತು ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ ಉದ್ಘಾಟನೆಯ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಹೋಲಿಸುತ್ತಿದ್ದೇವೆ.

ಎರಡೂ ಮಾದರಿಗಳು ಒಂದೇ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ತೆಗೆದುಕೊಳ್ಳುತ್ತವೆ ಆದರೆ ನೆಮೊ ಮಂದಿಗಿಂತ ಕಡಿಮೆ ಟೋಕನ್‌ಗಳನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ.

```bash
pip install mistral-common
```

```python 
# ಅಗತ್ಯವಾದ ಪ್ಯಾಕೇಜುಗಳನ್ನು ಆಮದುಮಾಡಿ:
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

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# ಸಂದೇಶಗಳ ಪಟ್ಟಿ ಟೋಕನೈಸ್ ಮಾಡಿ
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

# ಟೋಕನ್ಗಳ ಸಂಖ್ಯೆಯನ್ನು ಎಣಿಸಿ
print(len(tokens))
```

```python
# ಅಗತ್ಯವಾದ ಪ್ಯಾಕೇಜಸ್ ಆಮದುಮಾಡಿ:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# ಮಿಸ್ಟ್ರಾಲ್ ಟೋಕನೈಸರ್ ಅನ್ನು ಲೋಡ್ ಮಾಡಿ

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

# ಟೋಕನ್‌ಗಳ ಸಂಖ್ಯೆಯನ್ನು ಎಣಿಸಿ
print(len(tokens))
```

## ಕಲಿಕೆಯು ಇಲ್ಲೇ ನಿಲ್ಲುವುದಿಲ್ಲ, ಪ್ರಯಾಣವನ್ನು ಮುಂದುವರೆಸಿರಿ

ಈ ಪಾಠ ಪೂರ್ಣಗೊಂಡ ಮೇಲೆ, ನಮ್ಮ [ಜನೆರೇಟಿವ್ AI ಕಲಿಕೆ ಸಂಗ್ರಹ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ನೋಡಿ ನಿಮ್ಮ ಜನೆರೇಟಿವ್ AI ವಿಚಾರಧಾರೆಯನ್ನು ಮತ್ತಷ್ಟು ಏರಿಸಿಕೊಳ್ಳಿರಿ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ತಜ್ಞಾಪನೆ**:  
ಈ ದಾಖಲೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಗಾಗಿ ಪ್ರಯತ್ನಿಸುವ ಅಗತ್ಯವಿದೆಯಾದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳಾಗಬಹುದು ಅಥವಾ ಅಸತ್ಯತೆಗಳಾಗಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿ ಇರುವ ಮೂಲ ದಾಖಲೆ ಪ್ರಾಮಾಣಿಕ ಮೂಲವಾಗಿವೆ ಎಂದು ಪರಿಗಣಿಸಬೇಕು. ಅತ್ಯಾವಶ್ಯಕ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸದಿರುವುದರಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪುರ್ಥಗಳನ್ನು ಅಥವಾ ಅರ್ಥ ಕಳವುಗಳನ್ನು ನಾವು ಹೊಣೆಗಾರರಾಗಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->