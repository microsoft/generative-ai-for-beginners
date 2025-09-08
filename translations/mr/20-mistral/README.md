<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:58:16+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "mr"
}
-->
# Mistral मॉडेल्ससह बिल्डिंग

## परिचय

या धड्यात आपण खालील गोष्टी पाहणार आहोत:  
- वेगवेगळ्या Mistral मॉडेल्सची ओळख  
- प्रत्येक मॉडेलच्या वापराच्या प्रकरणांची आणि परिस्थितींची समज  
- कोड नमुने जे प्रत्येक मॉडेलच्या खास वैशिष्ट्ये दाखवतात.

## Mistral मॉडेल्स

या धड्यात आपण 3 वेगवेगळ्या Mistral मॉडेल्सची ओळख करून घेणार आहोत:  
**Mistral Large**, **Mistral Small** आणि **Mistral Nemo**.

हे सर्व मॉडेल्स Github Model मार्केटप्लेसवर मोफत उपलब्ध आहेत. या नोटबुकमधील कोड या मॉडेल्सचा वापर करून चालवला जाईल. Github Models वापरून [AI मॉडेल्ससह प्रोटोटायपिंग](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) कसे करायचे याबाबत अधिक माहिती येथे आहे.

## Mistral Large 2 (2407)

Mistral Large 2 सध्या Mistral कडून उपलब्ध असलेले प्रमुख मॉडेल आहे आणि ते एंटरप्राइझ वापरासाठी डिझाइन केलेले आहे.

हे मॉडेल मूळ Mistral Large चा अपग्रेड आहे, ज्यामध्ये  
- मोठा Context Window - 128k विरुद्ध 32k  
- गणित आणि कोडिंग टास्कवर चांगली कामगिरी - सरासरी अचूकता 76.9% विरुद्ध 60.4%  
- बहुभाषिक कामगिरी वाढवली आहे - भाषांमध्ये इंग्रजी, फ्रेंच, जर्मन, स्पॅनिश, इटालियन, पोर्तुगीज, डच, रशियन, चायनीज, जपानीज, कोरियन, अरबी आणि हिंदी यांचा समावेश आहे.

या वैशिष्ट्यांमुळे Mistral Large खालील बाबतीत उत्कृष्ट आहे:  
- *Retrieval Augmented Generation (RAG)* - मोठ्या context window मुळे  
- *Function Calling* - या मॉडेलमध्ये नैसर्गिक function calling आहे ज्यामुळे बाह्य साधने आणि API शी एकत्रीकरण शक्य होते. हे कॉल्स एकाच वेळी किंवा अनुक्रमे केले जाऊ शकतात.  
- *Code Generation* - Python, Java, TypeScript आणि C++ कोड जनरेशनमध्ये हे मॉडेल उत्कृष्ट आहे.

### Mistral Large 2 वापरून RAG उदाहरण

या उदाहरणात, आपण Mistral Large 2 वापरून एका मजकूर दस्तऐवजावर RAG पॅटर्न चालवत आहोत. प्रश्न कोरियन भाषेत लिहिला आहे आणि लेखकाच्या कॉलेजपूर्वीच्या क्रियाकलापांविषयी विचारतो.

हे Cohere Embeddings Model वापरून मजकूर दस्तऐवज आणि प्रश्न यांचे embeddings तयार करते. या नमुन्यासाठी faiss Python पॅकेज व्हेक्टर स्टोअर म्हणून वापरले आहे.

Mistral मॉडेलला पाठवलेला प्रॉम्प्ट प्रश्न आणि प्रश्नाशी संबंधित पुनर्प्राप्त केलेले भाग दोन्ही समाविष्ट करतो. मॉडेल नंतर नैसर्गिक भाषेत उत्तर देते.

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

Mistral Small हा Mistral कुटुंबातील आणखी एक मॉडेल आहे जो प्रीमियर/एंटरप्राइझ श्रेणीत येतो. नावाप्रमाणे, हा एक Small Language Model (SLM) आहे. Mistral Small वापरण्याचे फायदे म्हणजे:  
- Mistral Large आणि NeMo सारख्या Mistral LLMs च्या तुलनेत खर्चात बचत - 80% किंमतीत कपात  
- कमी विलंब - Mistral च्या LLMs च्या तुलनेत जलद प्रतिसाद  
- लवचिक - कमी संसाधनांच्या गरजांसह विविध वातावरणांमध्ये सहज तैनात करता येतो.

Mistral Small चांगला आहे:  
- मजकूर आधारित कामांसाठी जसे की सारांश तयार करणे, भावना विश्लेषण आणि भाषांतर  
- जिथे वारंवार विनंत्या येतात अशा अनुप्रयोगांसाठी, कारण तो खर्चिकदृष्ट्या फायदेशीर आहे  
- कमी विलंब असलेल्या कोड कामांसाठी जसे की पुनरावलोकन आणि कोड सूचना

## Mistral Small आणि Mistral Large यांची तुलना

Mistral Small आणि Large मधील विलंबातील फरक दाखवण्यासाठी खालील सेल्स चालवा.

आपण 3-5 सेकंदांच्या फरकाचा प्रतिसाद वेळेत अनुभव घेऊ शकता. तसेच त्याच प्रॉम्प्टवर प्रतिसादाची लांबी आणि शैली यावरही लक्ष द्या.

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

या धड्यातील इतर दोन मॉडेल्सच्या तुलनेत, Mistral NeMo हा एकमेव मोफत मॉडेल आहे ज्याला Apache2 परवाना आहे.

हा Mistral च्या आधीच्या ओपन सोर्स LLM, Mistral 7B चा अपग्रेड मानला जातो.

NeMo मॉडेलची काही इतर वैशिष्ट्ये:  

- *अधिक कार्यक्षम टोकनायझेशन:* हे मॉडेल Tekken टोकनायझर वापरते, जो सामान्यतः वापरल्या जाणाऱ्या tiktoken पेक्षा वेगळा आहे. यामुळे अधिक भाषा आणि कोडवर चांगली कामगिरी होते.

- *फाइनट्यूनिंग:* बेस मॉडेल फाइनट्यूनिंगसाठी उपलब्ध आहे. यामुळे ज्या वापराच्या प्रकरणांमध्ये फाइनट्यूनिंग आवश्यक आहे त्यासाठी अधिक लवचिकता मिळते.

- *नैसर्गिक Function Calling* - Mistral Large प्रमाणे, या मॉडेलला function calling वर प्रशिक्षण दिले गेले आहे. त्यामुळे हे पहिले ओपन सोर्स मॉडेल्सपैकी एक आहे ज्यामध्ये ही क्षमता आहे.

### टोकनायझर्सची तुलना

या नमुन्यात, आपण पाहणार आहोत की Mistral NeMo Mistral Large च्या तुलनेत टोकनायझेशन कसे हाताळते.

दोन्ही नमुने एकाच प्रॉम्प्टवर आधारित आहेत, पण आपण पाहाल की NeMo तुलनेत कमी टोकन्स परत करते.

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

## शिकणे येथे थांबत नाही, प्रवास सुरू ठेवा

हा धडा पूर्ण केल्यानंतर, आमच्या [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ला भेट द्या आणि आपले Generative AI ज्ञान अधिक वाढवा!

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.