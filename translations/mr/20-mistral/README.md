# मिस्त्राल मॉडेल्ससह बिल्डिंग 

## परिचय 

हा धडा यावर माहिती देईल: 
- वेगवेगळ्या मिस्त्राल मॉडेल्सचा अभ्यास 
- प्रत्येक मॉडेलसाठी वापर प्रकरणे व परिस्थिती समजून घेणे 
- प्रत्येक मॉडेलच्या अनोख्या वैशिष्ट्यांचे उदाहरणात्मक कोड वापरून एक्सप्लोर करणे. 

## मिस्त्राल मॉडेल्स 

या धड्यात, आपण 3 वेगवेगळ्या मिस्त्राल मॉडेल्सचा अभ्यास करू: 
**मिस्त्राल लार्ज**, **मिस्त्राल स्मॉल** आणि **मिस्त्राल नेमो**. 

या मॉडेल्सपैकी प्रत्येक [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) वर मोफत उपलब्ध आहे. या नोटबुकमधील कोड या मॉडेल्सचा वापर करून चालवला जाईल.

> **टीप:** GitHub Models जुलै 2026 च्या शेवटी बंद होत आहे. AI मॉडेल्ससह प्रोटोटाइप करण्यासाठी [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) वापरण्याबाबत अधिक तपशील येथे आहेत. 


## मिस्त्राल लार्ज 2 (2407)
मिस्त्राल लार्ज 2 सध्या मिस्त्रालचे प्रमुख मॉडेल आहे आणि ते एंटरप्राइझ वापरासाठी डिझाईन केले आहे. 

हे मॉडेल मूळ मिस्त्राल लार्जचे अपग्रेड आहे जे पुरवते 
-  मोठे संदर्भ विंडो - 128k विरुद्ध 32k 
-  गणित आणि कोडिंग कार्यांवरील उत्कृष्ट कामगिरी - 76.9% सरासरी अचूकता विरुद्ध 60.4% 
-  वाढलेली बहुभाषिक कामगिरी - भाषांमध्ये समाविष्ट आहेत: इंग्रजी, फ्रेंच, जर्मन, स्पॅनिश, इटालियन, पोर्तुगीज, डच, रशियन, चिनी, जपानी, कोरियन, अरबी, आणि हिंदी.

या वैशिष्ट्यांमुळे, मिस्त्राल लार्ज उत्कृष्ट आहे 
- *रिट्रीव्हल ऑगमेंटेड जेनरेशन (RAG)* - मोठ्या संदर्भ विंडोमुळे
- *फंक्शन कॉलिंग* - या मॉडेलमध्ये स्थानिक फंक्शन कॉलिंग आहे ज्यामुळे बाह्य टूल्स आणि API सह एकत्रीकरण शक्य होते. हे कॉल एकाच वेळी किंवा एकाच नंतर एक क्रमाने केले जाऊ शकतात. 
- *कोड जनरेशन* - या मॉडेलमध्ये Python, Java, TypeScript आणि C++ जनरेशनमध्ये उत्कृष्ट कामगिरी आहे. 

### मिस्त्राल लार्ज 2 वापरून RAG उदाहरण 

या उदाहरणात, आपण मिस्त्राल लार्ज 2 वापरून एका मजकूर दस्तऐवजात RAG नमुना चालवत आहोत. प्रश्न कोरियन भाषेत लिहिला आहे आणि लेखकाच्या महाविद्यालयाआधीच्या क्रियाकलापांबद्दल विचारतो. 

हे Cohere Embeddings मॉडेल वापरते जे मजकूर दस्तऐवज तसेच प्रश्नाचे एम्बेडिंग तयार करते. या नमुन्यासाठी, faiss Python पॅकेज व्हेक्टर स्टोर म्हणून वापरले जाते. 

मिस्त्राल मॉडेलला पाठवलेला प्रॉम्प्ट मध्ये प्रश्न तसेच प्रश्नाशी संबंधित पुनर्प्राप्त केलेले तुकडे दोन्ही समाविष्ट आहेत. मॉडेल नंतर नैसर्गिक भाषा प्रतिसाद प्रदान करते. 

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

# हे आपल्या Microsoft Foundry प्रकल्पाच्या "अवलोकन" पृष्ठातून घ्या
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # अंतर, निर्देशांक
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

## मिस्त्राल स्मॉल 
मिस्त्राल स्मॉल हा मिस्त्राल कुटुंबातील आणखी एक मॉडेल आहे जे प्रीमियर/एंटरप्राइझ श्रेणीखाली येतो. नावाप्रमाणे, हे मॉडेल एक लहान भाषा मॉडेल (SLM) आहे. मिस्त्राल स्मॉल वापरण्याचे फायदे आहेत: 
- मिस्त्राल लार्ज आणि NeMo सारख्या मोठ्या LLM च्या तुलनेत खर्च कमी - 80% किंमतीत घट
- कमी विलंब - मिस्त्रालच्या LLM पेक्षा जलद प्रतिसाद
- लवचिक - विविध पर्यावरणांमध्ये कमी संसाधने आवश्यक असल्यामुळे सहज तैनात करता येऊ शकते. 


मिस्त्राल स्मॉल उत्तम आहे: 
- मजकूर आधारित कार्यांसाठी जसे की सारांश तयार करणे, भावना विश्लेषण आणि भाषांतर. 
- ज्या अर्जांमध्ये वारंवार विनंत्या होतात कारण ते खर्च प्रभावी आहे 
- कमी विलंब असलेल्या कोड कामांसाठी जसे समीक्षा आणि कोड सूचना 

## मिस्त्राल स्मॉल आणि मिस्त्राल लार्जची तुलना 

मिस्त्राल स्मॉल आणि लार्जमधील विलंबता फरक दर्शविण्यासाठी खालील सेल्स चालवा. 

तुम्हाला प्रत्युत्तर वेळेत 3-5 सेकंदांचा फरक दिसेल. तसेच त्याच प्रॉम्प्टवर प्रतिसादाची लांबी आणि शैलीही लक्षात घ्या.  

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

## मिस्त्राल नेमॉ

या धड्यात चर्चा केलेल्या इतर दोन मॉडेल्सशी तुलना करता, मिस्त्राल नेमॉ हा एकमेव मोफत मॉडेल आहे ज्याला Apache2 परवानगी आहे. 

हे पूर्वीच्या मिस्त्रालच्या मुक्त स्रोत LLM, मिस्त्राल 7B वर एक अपग्रेड म्हणून पाहिले जाते. 

नेमॉ मॉडेलची काही इतर वैशिष्ट्ये: 

- *अधिक कार्यक्षम टोकनायझेशन:* हे मॉडेल Tekken टोकनायझर वापरते जो सामान्यतः वापरल्या जाणाऱ्या tiktoken पेक्षा वेगळा आहे. यामुळे अधिक भाषा आणि कोडवर चांगली कामगिरी होते. 

- *फायनट्यूनिंग:* बेस मॉडेल फायनट्यूनिंगसाठी उपलब्ध आहे. त्यामुळे ज्यांना फायनट्यूनिंगची आवश्यकता आहे अशा वापर प्रकरणांमध्ये अधिक लवचिकता मिळते. 

- *निवडक फंक्शन कॉलिंग* - मिस्त्राल लार्जसारखे, या मॉडेलला फंक्शन कॉलिंगसाठी प्रशिक्षित केले गेले आहे. त्यामुळे हे एकमेव मुक्त स्रोत मॉडेल्सपैकी एक आहे जे हे कार्य करते. 


### टोकनायझरची तुलना 

या नमुन्यात, आपण पाहू कसे मिस्त्राल नेमॉ टोकनायझेशन हाताळतो मिस्त्राल लार्जच्या तुलनेत. 

दोन्ही नमुने एकसारखा प्रॉम्प्ट घेतात पण तुम्हाला दिसेल की नेमॉ लार्जच्या तुलनेत कमी टोकन्स परत करतो. 

```bash
pip install mistral-common
```

```python 
# आवश्यक पॅकेजेस आयात करा:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# मिस्ट्रल टोकनायझर लोड करा

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# संदेशांची यादी टोकनायझ करा
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

# टोकन्सची संख्या मोजा
print(len(tokens))
```

```python
# आवश्यक पॅकेजेस आयात करा:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral टोकनायझर लोड करा

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# संदेशांची यादी टोकन करा
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

# टोकनची संख्या मोजा
print(len(tokens))
```

## शिकणे येथे थांबत नाही, प्रवास सुरू ठेवा

हा धडा पूर्ण केल्यावर, आमची [जनरेटिव्ह AI शिकण्याची संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) तपासा आणि तुमचे जनरेटिव्ह AI ज्ञान पुढे वाढवा!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->