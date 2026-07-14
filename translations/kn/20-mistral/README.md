# ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗಳೊಂದಿಗೆ ನಿರ್ಮಿಸಿ

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ ಒಳಗೊಂಡಿದೆ:
- ವಿಭಿನ್ನ ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗಳನ್ನು ಅನ್ವೇಷಿಸುವುದು
- ಪ್ರತಿ ಮಾದರಿಯ ಬಳಕೆ-ಕೇಸುಗಳು ಮತ್ತು ಪರಿಕಠಣಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು
- ಪ್ರತಿ ಮಾದರಿಯ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ತೋರಿಸುವ ಕೋಡ್ ಉದಾಹರಣೆಗಳನ್ನು ಅನ್ವೇಷಿಸುವುದು.

## ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗಳು

ಈ ಪಾಠದಲ್ಲಿ, ನಾವು ಮೂರು ವಿಭಿನ್ನ ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗಳನ್ನು ಅನ್ವೇಷಿಸೋಣ:
**ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್**, **ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್** ಮತ್ತು **ಮಿಸ್ಟ್ರಾಲ್ ನೀಮೊ**.

ಈ ಪ್ರತಿ ಮಾದರಿ [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ನಲ್ಲಿ ಉಚಿತವಾಗಿ ಲಭ್ಯವಿದೆ. ಈ ನೋಟ್ಬುಕ್‌ನಲ್ಲಿನ ಕೋಡ್ ಇವುಗಳನ್ನು ಬಳಸುತ್ತದೆ.

> **ಸೂಚನೆ:** GitHub Models ಜುಲೈ 2026 ರ ಕೊನೆಯಲ್ಲಿ ನಿವೃತ್ತಿಯಾಗುತ್ತಿದೆ. [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ಬಳಸಿ AI ಮಾದರಿಗಳೊಂದಿಗೆ ಪ್ರೋಟೋಟೈಪಿಂಗ್ ಬಗ್ಗೆ ಹೆಚ್ಚಿನ ವಿವರಗಳು ಇಲ್ಲಿವೆ.


## ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ 2 (2407)
ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ 2 ಪ್ರಸ್ತುತ ಮಿಸ್ಟ್ರಾಲ್‌ನ ಪ್ರಮುಖ ಮಾದರಿ ಮತ್ತು ಉದ್ಯಮ ಬಳಕೆಗೆ ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ.

ಈ ಮಾದರಿ ಮೂಲ ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್‌ನ ಅಪ್ಗ್ರೇಡ್ ಆಗಿದ್ದು,
-  ದೊಡ್ಡ ಸಂದರ್ಭ ವಿಂಡೋ - 128k ವಿರುದ್ಧ 32k
-  ಗಣಿತ ಮತ್ತು ಕೋಡಿಂಗ್ ಕಾರ್ಯಗಳಲ್ಲಿ ಉತ್ತಮ ಕಾರ್ಯಕ್ಷಮತೆ - 76.9% ಸರಾಸರಿ ನಿಖರತೆ ವಿರುದ್ಧ 60.4%
-  ಹೆಚ್ಚಿಸಿದ ಬಹುಭಾಷಾ ಕಾರ್ಯಕ್ಷಮತೆ - ಭಾಷೆಗಳು: ಇಂಗ್ಲಿಷ್, ಫ್ರೆಂಚ್, ಜರ್ಮನ್, ಸ್ಪಾನಿಷ್, ಇಟಾಲಿಯನ್, ಪೋರ್ಚುಗೀಸ್, ಡಚ್, ರಶಿಯನ್, ಚೈನೀಸ್, ಜಪಾನೀಸ್, ಕೊರಿಯನ್, ಅರೆಬಿಕ್, ಮತ್ತು ಹಿಂದಿ.

ಈ ವೈಶಿಷ್ಟ್ಯಗಳೊಂದಿಗೆ, ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ ಉತ್ತಮವಾಗಿದೆ:
- *ರಿಟ್ರೀವಲ್ ಆಗ್ಮೆಂಟೆಡ್ ಜನರೇಷನ್ (RAG)* - ದೊಡ್ಡ ಸಂದರ್ಭ ವಿಂಡೋ ಕಾರಣದಿಂದ
- *ಫังก್ಷನ್ ಕಾಲಿಂಗ್* - ಈ ಮಾದರಿಯಲ್ಲಿ ಮೂಲಭೂತ ಫังก್ಷನ್ ಕಾಲಿಂಗ್ ಇದೆ, ಇದು ಹೊರಗಿನ ಸಾಧನಗಳು ಮತ್ತು API ಗಳೊಂದಿಗೆ ಏಕೀಕರಣಕ್ಕೆ ಅನುಮತಿಸುತ್ತದೆ. ಈ ಕಾಲ್‌ಗಳನ್ನು ಸಮಾಂತರವಾಗಿ ಅಥವಾ ಕ್ರಮವಾಗಿ ಮಾಡಬಹುದು.
- *ಕೋಡ್ ಜನರೇಷನ್* - ಈ ಮಾದರಿ পাইಥಾನ್, ಜಾವಾ, ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್ ಮತ್ತು C++ ಜನರೇಷನ್ನಲ್ಲಿ ಉತ್ತಮವಾಗಿದೆ.

### ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ 2 ಬಳಸಿ RAG ಉದಾಹರಣೆ

ಈ ಉದಾಹರಣೆಯಲ್ಲಿ, ನಾವು ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ 2 ಬಳಸಿ ಪಠ್ಯ ಡಾಕ್ಯುಮೆಂಟ್ ಮೇಲೆ RAG ಮಾದರಿಯನ್ನು ಚಲಾಯಿಸುತ್ತಿದ್ದೇವೆ. ಪ್ರಶ್ನೆ ಕೊರಿಯನ್ ಭಾಷೆಯಲ್ಲಿ ಬರೆಯಲಾಗಿದೆ ಮತ್ತು ಲೇಖಕ ಕಾಲೇಜಿಗೆ ಹೋದ ಮುಂಚೆ ಏನು ಮಾಡುತ್ತಿದ್ದನು ಎಂದು ಕೇಳುತ್ತದೆ.

ಇದು Cohere Embeddings Model ಬಳಸಿ ಪಠ್ಯ ಡಾಕ್ಯುಮೆಂಟ್ ಮತ್ತು ಪ್ರಶ್ನೆಯ ಇಂಬರ್‍ಡಿಂಗ್‌ಗಳನ್ನು ಸೃಷ್ಟಿಸುತ್ತದೆ. ಈ ಉದಾಹರಣೆಗೆ faiss Python ಪ್ಯಾಕೇಜ್ ಅನ್ನು ವ್ಯಕ್ಟರ್ ಸ್ಟೋರ್ ಆಗಿ ಬಳಸುತ್ತದೆ.

ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗೆ ಕಳುಹಿಸಿದ ಪ್ರಾಂಪ್ಟ್‌ನಲ್ಲಿ ಪ್ರಶ್ನೆಗಳು ಮತ್ತು ಪ್ರಶ್ನೆಗೆ ಸಾಮಾನ್ಯವಾದ ದಾಖಲೆಯ ತುಂಡುಗಳನ್ನು ಸೇರಿಸಲಾಗಿದೆ. ನಂತರ ಮಾದರಿ ಸ್ವಾಭಾವಿಕ ಭಾಷೆ ಉತ್ತರ ನೀಡುತ್ತದೆ.

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

# ನಿಮ್ಮ Microsoft Foundry ಯೋಜನೆಯ "ಒವರ್‌ವ್ಯೂ" ಪುಟದಿಂದ ಇದನ್ನು ಪಡೆಯಿರಿ
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
ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಮಿಸ್ಟ್ರಾಲ್ ಕುಟುಂಬದ ಮತ್ತೊಂದು ಮಾದರಿ, ಪ್ರೀಮಿಯರ್/ಎಂಟರ್‌ಪ್ರೈಸ್ ವರ್ಗಕ್ಕೆ ಸೇರಿದದ್ದು. ಹೆಸರು ಸೂಚಿಸುವಂತೆ, ಇದು ಸಣ್ಣ ಭಾಷಾ ಮಾದರಿ (SLM). ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಬಳಸಲು ಲಾಭಗಳಾಗುವ ಅಂಶಗಳು:
- ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ ಮತ್ತು ನೀಮೊ ಬೇರೆ LLM ಗಿಂತ ವೆಚ್ಚ ಅಥವಾ ಬೆಲೆ ಉಳಿತಾಯ - 80% ಕಡಿತ
- ಕಡಿಮೆ ವಿಳಂಬ - ಮಿಸ್ಟ್ರಾಲ್ LLM ಗಿಂತ ವೇಗವಾಗಿ ಪ್ರತಿಕ್ರಿಯೆ ನೀಡುತ್ತದೆ
- ಲವಚಿಕ - ಕಡಿಮೆ ಸಂಪನ್ಮೂಲ ಅವಶ್ಯಕತೆಗಳೊಂದಿಗೆ ವಿವಿಧ ಪರಿಸರಗಳಲ್ಲಿ ನಿಯೋಜಿಸಬಹುದು.


ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಉತ್ತಮವಾಗಿದೆ:
- ಪಠ್ಯ ಆಧಾರಿತ ಕಾರ್ಯಗಳು, ಉದಾಹರಣೆಗೆ ಸಮ್ಮರಿ ಮಾಡುವಿಕೆ, ಭಾವ ವಿಶ್ಲೇಷಣೆ ಮತ್ತು ಅನುವಾದ.
- ಖರ್ಚು ಸಹಜತೆ ಕಾರಣವಾಗಿ ಹಲವಾರು ವಿನಂತಿಗಳು ಮಾಡಬೇಕಾಗುವ ಅಪ್ಲಿಕೇಶನ್ಗಳು
- ಕಡಿಮೆ ವಿಳಂಬ ಕೋಡ್ ಕಾರ್ಯಗಳು ಹಾಗು ವಿಮರ್ಶೆ ಮತ್ತು ಕೋಡ್ ಸೂಚನೆಗಳು

## ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಮತ್ತು ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ ಹೋಲಿಕೆ

ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಹಾಗೂ ಲಾರ್ಜ್ ನಡುವೆ ವಿಳಂಬದ ಭೇದವನ್ನು ತೋರಿಸಲು ಕೆಳಗಿನ ಸೆಲ್‌ಗಳನ್ನು ಚಾಲನೆ ಮಾಡಿ.

3-5 ಸೆಕೆಂಡುಗಳ ನಡುವಿನ ಪ್ರತಿಕ್ರಿಯೆ ಸಮಯದ ವ್ಯತ್ಯಾಸವನ್ನು ನೀವು ನೋಡಬಹುದು. ಅದೇ ಪ್ರಾಂಪ್ಟ್ ಮೇಲೆ ಪ್ರತಿಕ್ರಿಯೆಯ ಉದ್ದಗಳು ಮತ್ತು ಶೈಲಿಯನ್ನೂ ಗಮನಿಸಿ.

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

## ಮಿಸ್ಟ್ರಾಲ್ ನೀಮೊ

ಈ ಪಾಠದಲ್ಲಿ ಚರ್ಚಿಸಿದ ಇತರ ಎರಡು ಮಾದರಿಗಳಿಗಿಂತ, ಮಿಸ್ಟ್ರಾಲ್ ನೀಮೊ ಏಕೈಕ ಉಚಿತ ಮಾದರಿ ಆಗಿದ್ದು Apache2 ಪರವಾನಗಿ ಹೊಂದಿದೆ.

ಇದು ಮಿಸ್ಟ್ರಾಲ್‌ನ ಮೊದಲ ಲೈವ್ ಮೂಲ ಲಾಂಗ್ವೇಜ್ ಮಾದರಿ ಮಿಸ್ಟ್ರಾಲ್ 7B ಗೆ ಅಪ್ಗ್ರೇಡ್ ಆಗಿ ಪರಿಗಣಿಸಲಾಗಿದೆ.

ನೀಮೊ ಮಾದರಿಯ ಕೆಲವು ಪ್ರಮುಖ ವೈಶಿಷ್ಟ್ಯಗಳು:

- *ಎಷ್ಟು ಕಾರ್ಯಕ್ಷಮವಾದ ಟೋಕನೈಜೇಶನ್:* ಈ ಮಾದರಿ ಹೆಚ್ಚು ಜನಪ್ರಿಯ tiktoken ಬದಲಾಗಿ Tekken ಟೋಕನೈಜರ್ ಬಳಸುತ್ತದೆ. ಇದು ಹೆಚ್ಚಿನ ಭಾಷೆಗಳಿಗೆ ಮತ್ತು ಕೋಡ್ ಗೆ ಉತ್ತಮ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಸಿಗಿಸುತ್ತದೆ.

- *ಫೈನ್‌ಟ್ಯೂನಿಂಗ್:* ಮೂಲ ಮಾದರಿ ಫೈನ್‌ಟ್ಯೂನಿಂಗ್‌ಗೆ ಲಭ್ಯವಿದೆ. ಇದರಿಂದ ಹೆಚ್ಚಿನ ಬಳಕೆ ಪ್ರಕರಣಗಳಿಗೆ ಹೊಂದಿಕೊಳ್ಳಲು ಸಾಧ್ಯ.

- *ಮೂಲಭೂತ ಫังก್ಷನ್ ಕಾಲಿಂಗ್* - ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ ಹಾಗೆಯೇ, ಈ ಮಾದರಿಯೂ ಫังก್ಷನ್ ಕಾಲಿಂಗ್ ತರಬೇತಿ ಪಡೆದಿದೆ. ಇದು ಮುಕ್ತ ಮೂಲ ಮಾದರಿಗಳಲ್ಲಿ ಮೊದಲಗಳಲ್ಲೊಂದು ಎಂದು ವಿಶಿಷ್ಟತೆ கொண்டಿದೆ.


### ಟೋಕನೈಜರ್‌ಗಳ ಹೋಲಿಕೆ

ಈ ಉದಾಹರಣೆಯಲ್ಲಿ, ಮಿಸ್ಟ್ರಾಲ್ ನೀಮೊ ಮತ್ತು ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ ಟೋಕನೈಜೇಶನ್ ಹೇಗೆ ನಡೆಸುತ್ತವೆ ಎಂದು ನೋಡೋಣ.

ಎರಡೂ ಮಾದರಿಗಳು ಅದೇ ಪ್ರಾಂಪ್ಟ್ ತೆಗೆದುಕೊಂಡಿದ್ದರೂ, ನೀಮೊ ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ ಗಿಂತ ಕಡಿಮೆ ಟೋಕನ್ ಗಳನ್ನೆಂದ ಪ್ರತ್ಯುತ್ತರ ನೀಡುತ್ತದೆ ಎಂದು ನೀವು ಗಮನಿಸುತ್ತೀರಿ.

```bash
pip install mistral-common
```

```python 
# ಬೇಕಾದ ಪ್ಯಾಕೇಜ್‌ಗಳನ್ನು ಆಮದುಮಾಡಿ:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# ಮಿಸ್ಟ್ರಲ್ ಟೋಕನೈಸರ್ ಲೋಡ್ ಮಾಡಿ

model_name = "open-mistral-nemo"

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

```python
# ಅಗತ್ಯವಿರುವ ಪ್ಯಾಕೇಜ್‌ಗಳನ್ನು ಆಮದುಮಾಡಿ:
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

# ಟೋಕನ್‌ಗಳ ಸಂಖ್ಯೆಯನ್ನು ಎಣಿಸಿ
print(len(tokens))
```

## ಕಲಿಕೆ ಇಲ್ಲಿ ನಿಲ್ಲುವುದಿಲ್ಲ, ಪ್ರಯಾಣವನ್ನು ಮುಂದುವರೆಸಿ

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನಮ್ಮ [ಜನರೇಟಿವ್ AI ಕಲಿಕಾ ಸಂಗ್ರಹ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ನೋಡಿಕೊಳ್ಳಿ ಮತ್ತು ನಿಮ್ಮ ಜನರೇಟಿವ್ AI ಜ್ಞಾನವನ್ನು ಹೆಚ್ಚಿಸಿ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->