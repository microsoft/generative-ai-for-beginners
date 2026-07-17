# ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗಳೊಂದಿಗೆ ನಿರ್ಮಿಸುವುದು 

## ಪರಿಚയം 

ಈ ಪಾಠದಲ್ಲಿ ಕಾಣುವವು: 
- ವಿಭಿನ್ನ ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗಳನ್ನು ಅನ್ವೇಷಿಸುವುದು 
- ಪ್ರತಿಯೊಂದು ಮಾದರಿಯ ಬಳಕೆ-ಕೇಸುಗಳು ಮತ್ತು ಪರಿಸ್ಥಿತಿಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು 
- ಪ್ರತಿಯೊಂದು ಮಾದರಿಯ ವಿಶಿಷ್ಟ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ತೋರಿಸುವ ಕೋಡ್ ಮಾದರಿಗಳನ್ನು ಅನ್ವೇಷಿಸುವುದು. 

## ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗಳು 

ಈ ಪಾಠದಲ್ಲಿ, ನಾವು 3 ವಿಭಿನ್ನ ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗಳನ್ನು ಪರಿಶೀಲಿಸುವೆವು: 
**ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್**, **ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್** ಮತ್ತು **ಮಿಸ್ಟ್ರಾಲ್ ನೀಮೊ**. 

ಈ ಮಾದರಿಗಳು [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ನಲ್ಲಿ ಉಚಿತವಾಗಿ ಲಭ್ಯವಿವೆ. ಈ ನೋಟ್ಬುಕ್‌ನ ಕೋಡ್ ಈ ಮಾದರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಕಾರ್ಯಾಚರಣೆ ಮಾಡುತ್ತದೆ.

> **ಗಮನಿಸಿ:** GitHub Models 2026 ಜುಲೈ ಕೊನೆಯಲ್ಲಿ ನಿವೃತ್ತಿಯಾಗುತ್ತಿದೆ. AI ಮಾದರಿಗಳೊಂದಿಗೆ ಪ್ರೋಟೋಟೈಪ್ ಮಾಡಲು [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ಬಳಕೆಯ ಬಗ್ಗೆ ಹೆಚ್ಚಿನ ಮಾಹಿತಿಗಾಗಿ ಇಲ್ಲಿಗೆ ಭೇಟಿ ನೀಡಿ. 


## ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ 2 (2407)
ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ 2 ಇತ್ತೀಚಿನ ಕಾಲದಲ್ಲಿ ಮಿಸ್ಟ್ರಾಲ್‌ನ ಮುಂಭಾಗದ ಮಾದರಿಯಾಗಿದ್ದು, ಉದ್ಯಮ ಬಳಕೆಗೆ ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ. 

ಈ ಮಾದರಿ ಮೂಲ ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್‌ಗೆ ಹೊಸ ಅವಕಾಶಗಳನ್ನು ನೀಡುತ್ತದೆ, ಉದಾಹರಣೆಗೆ 
-  ದೊಡ್ಡ ಕನ್ಟೆಕ್ಸ್ಟ್ ವಿಂಡೋ - 128k ವಿರುದ್ಧ 32k 
- ಗಣಿತ ಮತ್ತು ಕೋಡಿಂಗ್ ಕಾರ್ಯಗಳಲ್ಲಿ ಉತ್ತಮ ಪ್ರದರ್ಶನ - ಸರಾಸರಿ ನಿಖರತೆ 76.9% ವಿರುದ್ಧ 60.4% 
- ಹೆಚ್ಚಾದ ಬಹುತ್ವ ಭಾಷಾ ಕಾರ್ಯಕ್ಷಮತೆ - ಭಾಷೆಗಳು: ಇಂಗ್ಲಿಷ್, ಫ್ರೆಂಚ್, ಜರ್ಮನ್, ಸ್ಪ್ಯಾನಿಷ್, ಇಟಾಲಿಯನ್, ಪೋರ್ಚುಗೀಸ್, ಡಚ್, ರಷ್ಯನ್, ಚೈನೀಸ್, ಜಪಾನೀಸ್, ಕೊರಿಯನ್, ಅರबी, ಮತ್ತು ಹಿಂದಿ.

ಈ ವೈಶಿಷ್ಟ್ಯಗಳೊಂದಿಗೆ, ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ ಅತ್ಯುತ್ತಮವಾಗಿದೆ 
- *ರಿಟ್ರೀವಲ್ ಅಗ್ಗುಮೆಂಟೆಡ್ ಜನರೇಷನ್ (RAG)* - ದೊಡ್ಡ ಕನ್ಟೆಕ್ಸ್ಟ್ ವಿಂಡೋ ಇರುವುದರಿಂದ
- *ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್* - ಈ ಮಾದರಿಗೆ ಸ್ಥಳೀಯ ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್ ಇರುವುದರಿಂದ ಬಾಹ್ಯ ಸಾಧನಗಳು ಮತ್ತು APIಗಳೊಂದಿಗೆ ಸಂಯೋಜನೆ ಮಾಡಬಹುದು. ಈ ಕರೆಗಳನ್ನು ಸಮಾಂತರವಾಗಿ ಅಥವಾ ಕ್ರಮಬದ್ಧವಾಗಿ ಮತ್ತೊಬ್ಬ ನಂತರ ಮತ್ತೊಂದು ಕ್ರಮದಲ್ಲಿ ಮಾಡಬಹುದು. 
- *ಕೋಡ್ ಜನರೇಷನ್* - Python, Java, TypeScript ಮತ್ತು C++ ಜನರೇಷನ್‌ನಲ್ಲಿ ಈ ಮಾದರಿ ಅದ್ಭುತವಾಗಿ ಕಾರ್ಯ ನಿರ್ವಹಿಸುತ್ತದೆ. 

### ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ 2 ಬಳಸಿ RAG ಉದಾಹರಣೆ 

ಈ ಉದಾಹರಣೆಯಲ್ಲಿ, ನಾವು ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ 2 ನ್ನು ಪ್ರತಿಯೊಂದು ಪಠ್ಯ ದಾಖಲೆ ಮೇಲೆ RAG ಮಾದರಿಯನ್ನು ನಡೆಸಲು ಬಳಸುತ್ತಿದ್ದೇವೆ. ಪ್ರಶ್ನೆಯನ್ನು ಕೊರಿಯನ್ ಭಾಷೆಯಲ್ಲಿ ಬರೆಯಲಾಗಿದೆ ಮತ್ತು ಲೇಖಕ ಕಾಲೇಜಿಗೆ ಹೋದ ಮುಂಚಿನ ಚಟುವಟಿಕೆಗಳ ಬಗ್ಗೆ ಕೇಳುತ್ತದೆ. 

ಇದು Cohere Embeddings Model ಬಳಸಿ ಪಠ್ಯ ದಾಖಲೆ ಮತ್ತು ಪ್ರಶ್ನೆಯೇ ಎರಡರ embeds ಸೃಷ್ಟಿಸುತ್ತದೆ. ಈ ಮಾದರಿಗಾಗಿ, faiss Python ಪ್ಯಾಕೇಜ್ ಅನ್ನು ವೆಕ್ಟರ್ ಸ್ಟೋರ್ ಆಗಿ ಬಳಕೆ ಮಾಡಲಾಗಿದೆ. 

ಮಿಸ್ಟ್ರಾಲ್ ಮಾದರಿಗೆ ಪ್ರಸಾರ ಮಾಡಲಾದ ಪ್ರಾಂಪ್ಟ್‌ನಲ್ಲಿ ಪ್ರಶ್ನೆಗಳು ಮತ್ತು ಪ್ರಶ್ನೆಗೆ ಸಮಾನವಾದ ಪುನಃಮತ್ತಿ ಮಾದರಿಗಳು ಸೇರಿವೆ. ನಂತರ ಮಾದರಿ ಸಹಜ ಭಾಷೆಯಲ್ಲಿ ಉತ್ತರ ಕೊಡುತ್ತದೆ. 

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

# ನಿಮ್ಮ Microsoft Foundry ಪ್ರಾಜೆಕ್ಟ್‌ನ "ಒವರ್‌ವ್ಯೂ" ಪುಟದಿಂದ ಇವುಗಳನ್ನು ಪಡೆಯಿರಿ
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # ದೂರ, ಸೂಚಕ
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
ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಮಿಸ್ಟ್ರಾಲ್ ಕುಟುಂಬದ ಇನ್ನೊಂದು ಮಾದರಿ ಮತ್ತು ಅವು ಪ್ರೀಮಿಯರ್/ಉದ್ಯಮ ವರ್ಗದೊಳಗೆ ಬರುತ್ತದೆ. ಹೆಸರಿನಿಂದ ತಿಳಿಯುವಂತೆ, ಇದು ಒಂದು ಸಣ್ಣ ಭಾಷಾ ಮಾದರಿ (SLM). ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಬಳಸುವುದರಿಂದ ಲಾಭಗಳು ಇವೆ: 
- ಮಿಸ್ಟ್ರಾಲ್ LLMs ಗಿಂತ ಕಡಿಮೆ ವೆಚ್ಚ - 80% ಬೆಲೆ ಇಳಿಕೆ 
- ಕಡಿಮೆ ವಿಳಂಬ - ಮಿಸ್ಟ್ರಾಲ್ LLMs ಗಿಂತ ವೇಗವಾದ ಪ್ರತಿಕ್ರಿಯೆ 
- ಅನುಕೂಲಕರ - ಕಡಿಮೆ ಸಂಪನ್ಮೂಲ ಅವಶ್ಯಕತೆಗಳೊಂದಿಗೆ ವಿವಿಧ ಪರಿಸರಗಳಲ್ಲಿ ನಿಗಧಿಪಡಿಸಬಹುದು. 


ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಇದಕ್ಕೆ ಉತ್ತಮ: 
- ಸಾರಾಂಶ, ಭಾವನಾತ್ಮಕ ವಿಶ್ಲೇಷಣೆ ಮತ್ತು ಅನುವಾದಂತಹ ಪಠ್ಯ ಆಧಾರಿತ ಕಾರ್ಯಗಳು. 
- ವೆಚ್ಚ ಪರಿಣಾಮಕಾರಿತ್ವದಿಂದ ನಿಯಮಿತ ವಿನಂತಿಗಳು ಮಾಡುವ ಅಪ್ಲಿಕೇಶನ್ಗಳು 
- ವಿಮರ್ಶೆ ಮತ್ತು ಕೋಡ್ ಸಲಹೆಗಳಂತಹ ಕಡಿಮೆ ವಿಳಂಬದ ಕೋಡ್ ಕಾರ್ಯಗಳು 

## ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಮತ್ತು ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ ಹೋಲಿಕೆ 

ಮಿಸ್ಟ್ರಾಲ್ ಸ್ಮಾಲ್ ಮತ್ತು ಲಾರ್ಜ್ ನಡುವಿನ ವಿಳಂಬ ವ್ಯತ್ಯಾಸಗಳನ್ನು ತೋರಿಸಲು ಕೆಳಗಿನ ಸೆಲ್‌ಗಳನ್ನು ರನ್ ಮಾಡಿ. 

3-5 ಸೆಕೆಂಡ್‌ಗಳ ನಡುವೆ ಪ್ರತಿಕ್ರಿಯೆ ಸಮಯದಲ್ಲಿ ವ್ಯತ್ಯಾಸವನ್ನು ಕಾಣಬಹುದು. ಇನ್ನು ಅದೇ ಪ್ರಾಂಪ್ಟ್ ಮೇಲೆ ಪ್ರತಿಕ್ರಿಯೆಯ ದೈರ್ಘ್ಯ ಮತ್ತು ಶೈಲಿಯನ್ನು ಗಮನಿಸಿ.  

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

ಇತರ ಎರಡು ಮಾದರಿಗಳಿಗಿಂತಲೂ, ಮಿಸ್ಟ್ರಾಲ್ ನೀಮೊ ಏಪಾಚಿ2 ಪರವಾನಗಿಯೊಂದಿಗೆ ಉಚಿತ ಮಾದರಿಯೇ ಆಗಿದೆ. 

ಇದು ಮಿಸ್ಟ್ರಾಲ್ ನ ಹಿಂದಿನ ಮುಕ್ತ ಮೂಲ LLM, ಮಿಸ್ಟ್ರಾಲ್ 7B ನ ಅಪ್ಗ್ರೇಡ್ ಎಂದು ಕಾಣಲಾಗುತ್ತದೆ. 

ನೀಮೊ ಮಾದರಿಯ ಇನ್ನಿತರ ಕೆಲವು ವೈಶಿಷ್ಟ್ಯಗಳು: 

- *ಕಾರ್ಯಕ್ಷಮ ಟೋಕನೈಜೆಷನ್:* ಈ ಮಾದರಿ ಸಾಮಾನ್ಯವಾಗಿ ಬಳಕೆಯಾಗುವ tiktoken ವಿಷಯಕ್ಕಿಂತ Tekken ಟೋಕನೈಸರ್ ಬಳಕೆ ಮಾಡುತ್ತದೆ. ಇದು ಹೆಚ್ಚಿನ ಭಾಷೆಗಳನ್ನು ಮತ್ತು ಕೋಡ್ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಉತ್ತಮಗೊಳಿಸುತ್ತದೆ. 

- *ಫೈನ್ಟ್ಯೂನಿಂಗ್:* ಮೂಲ ಮಾದರಿಯನ್ನು ಫೈನ್ಟ್ಯೂನಿಂಗ್ ಗೆ ಲಭ್ಯವಿದೆ. ಇದು ಫೈನ್ಟ್ಯೂನಿಂಗ್ ಅಗತ್ಯವಿರುವ ಬಳಕೆಕೆಸುಗಳಿಗೆ ಹೆಚ್ಚು ಲಚೀಲತೆಯನ್ನು ಒದಗಿಸುತ್ತದೆ. 

- *ಸ್ಥಳೀಯ ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್* - ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್ ಗಳಂತೆ, ಈ ಮಾದರಿಯು ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್ ಮೇಲೆ ತರಬೇತಿ ಪಡೆದಿದೆ. ಇದು ಮುಕ್ತ ಮೂಲದಲ್ಲಿ ಮೊದಲನೆಯದಾದಂತಹ ಮಾದರಿಗಳಲ್ಲಿ ಒಂದಾಗಿದೆ. 


### ಟೋಕನೈಸರ್‌ಗಳನ್ನು ಹೋಲಿಕೆ 

ಈ ಮಾದರಿಯಲ್ಲಿ, ನಾವು ಮಿಸ್ಟ್ರಾಲ್ ನೀಮೊ ಮತ್ತು ಮಿಸ್ಟ್ರಾಲ್ ಲಾರ್ಜ್‌ಗಳ ಟೋಕನೈಸಿಂಗ್ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಹೋಲಿಸುವೆವು. 

ಎರಡೂ ಮಾದರಿಗಳು ಒಂದೇ ಪ್ರಾಂಪ್ಟ್ ಕೈಗೊಂಡರೂ, ನೀಮೊ ಕಡಿಮೆ ಟೋಕನ್ಗಳನ್ನು ವಾಪಸು ನೀಡುತ್ತದೆ ಎಂದು ನೀವು ಗಮನಿಸುವಿರಿ. 

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

# ಮಿಸ್ಟ್ರಲ್ ಟೊಕನೈಜರ್ ಲೋಡ್ ಮಾಡಿ

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# ಸಂದೇಶಗಳ ಪಟ್ಟಿ ಟೊಕನೈಸ್ ಮಾಡಿ
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

# ಟೊಕನ್ಸ್ ಗಳ ಸಂಖ್ಯೆಯನ್ನು ಎಣಿಸಿ
print(len(tokens))
```

```python
# ಅಗತ್ಯವಾದ ಪ್ಯಾಕೇಜ್‌ಗಳನ್ನು ಆಮದುಮಾಡಿ:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# ಮಿಸ್ಟ್ರಲ್ ಟೋಕನೈಜರ್ ಅನ್ನು ಲೋಡ್ ಮಾಡಿ

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

## ಅಧ್ಯಯನ ಇಲ್ಲಿ ನಿಲ್ಲುವುದಿಲ್ಲ, ಪ್ರಯಾಣ ಮುಂದುವರೆಸಿ

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನಮ್ಮ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ಅನ್ನು ಪರಿಶೀಲಿಸಿ ನಿಮ್ಮ ಜನರೇಟಿವ್ AI ಜ್ಞಾನವನ್ನು ಮತ್ತಷ್ಟು ಹೆಚ್ಚಿಸಿ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->