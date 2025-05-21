<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:54:32+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "mr"
}
-->
# मिस्त्रल मॉडेल्ससह बांधकाम 

## परिचय 

या धड्यात आपण कव्हर करणार आहोत: 
- विविध मिस्त्रल मॉडेल्सची शोध 
- प्रत्येक मॉडेलसाठी वापर-केस आणि परिस्थिती समजून घेणे 
- कोड नमुने प्रत्येक मॉडेलच्या विशेष वैशिष्ट्ये दर्शवतात. 

## मिस्त्रल मॉडेल्स 

या धड्यात, आपण 3 विविध मिस्त्रल मॉडेल्सची शोध घेणार आहोत: 
**मिस्त्रल लार्ज**, **मिस्त्रल स्मॉल** आणि **मिस्त्रल नेमो**. 

प्रत्येक मॉडेल Github मॉडेल मार्केटप्लेसवर मोफत उपलब्ध आहे. या नोटबुकमधील कोड या मॉडेल्सचा वापर करून कोड चालवणार आहे. Github मॉडेल्स वापरून [AI मॉडेल्ससह प्रोटोटाइप तयार करण्यासाठी](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) अधिक तपशील येथे आहेत. 

## मिस्त्रल लार्ज 2 (2407)
मिस्त्रल लार्ज 2 सध्या मिस्त्रलचा प्रमुख मॉडेल आहे आणि एंटरप्राइज वापरासाठी डिझाइन केले आहे. 

मॉडेल मूळ मिस्त्रल लार्जमध्ये सुधारणा देतो 
- मोठे संदर्भ विंडो - 128k vs 32k 
- गणित आणि कोडिंग कार्यांवर चांगली कार्यक्षमता - 76.9% सरासरी अचूकता vs 60.4% 
- बहुभाषिक कार्यक्षमता वाढवली - भाषांमध्ये समाविष्ट आहे: इंग्रजी, फ्रेंच, जर्मन, स्पॅनिश, इटालियन, पोर्तुगीज, डच, रशियन, चीनी, जपानी, कोरियन, अरबी, आणि हिंदी.

या वैशिष्ट्यांसह, मिस्त्रल लार्ज उत्कृष्ट आहे 
- *रिट्रीव्हल ऑगमेंटेड जनरेशन (RAG)* - मोठ्या संदर्भ विंडोमुळे 
- *फंक्शन कॉलिंग* - या मॉडेलमध्ये नैसर्गिक फंक्शन कॉलिंग आहे ज्यामुळे बाह्य साधने आणि APIs सह एकत्रीकरण होते. हे कॉल्स एकाचवेळी किंवा अनुक्रमिक क्रमाने एकमेकानंतर केले जाऊ शकतात. 
- *कोड जनरेशन* - हे मॉडेल Python, Java, TypeScript आणि C++ जनरेशनवर उत्कृष्ट आहे. 

### मिस्त्रल लार्ज 2 वापरून RAG उदाहरण 

या उदाहरणात, आम्ही मिस्त्रल लार्ज 2 वापरून एक RAG पॅटर्न एका टेक्स्ट डॉक्युमेंटवर चालवत आहोत. प्रश्न कोरियनमध्ये लिहिला आहे आणि लेखकाच्या कॉलेजपूर्वीच्या क्रियाकलापांबद्दल विचारतो. 

हे Cohere Embeddings मॉडेल वापरून टेक्स्ट डॉक्युमेंट तसेच प्रश्नाचे एम्बेडिंग्स तयार करते. या नमुन्यासाठी, हे faiss Python पॅकेजचा वापर करते एक वेक्टर स्टोअर म्हणून. 

मिस्त्रल मॉडेलला पाठवलेला प्रॉम्प्ट प्रश्न आणि प्रश्नाशी संबंधित समान चंक्स समाविष्ट करतो. मॉडेल नंतर नैसर्गिक भाषेत प्रतिसाद देते. 

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

## मिस्त्रल स्मॉल 
मिस्त्रल स्मॉल हा मिस्त्रल मॉडेल्सच्या कुटुंबातील आणखी एक मॉडेल आहे जो प्रीमियर/एंटरप्राइज श्रेणीत येतो. नावानुसार, हे मॉडेल एक स्मॉल लँग्वेज मॉडेल (SLM) आहे. मिस्त्रल स्मॉलचा वापर करण्याचे फायदे आहेत: 
- मिस्त्रल LLMs सारखे मिस्त्रल लार्ज आणि नेमोच्या तुलनेत खर्च बचत - 80% किंमत कमी 
- कमी विलंबता - मिस्त्रलच्या LLMs च्या तुलनेत जलद प्रतिसाद 
- लवचिक - कमी संसाधनांच्या आवश्यकतेवर कमी निर्बंधांसह विविध वातावरणात तैनात केले जाऊ शकते. 

मिस्त्रल स्मॉल उत्कृष्ट आहे: 
- टेक्स्ट आधारित कार्यांसाठी जसे की संक्षेपण, भावना विश्लेषण आणि अनुवाद. 
- त्याच्या खर्च प्रभावीतेमुळे वारंवार विनंत्या केल्या जातात अशा अनुप्रयोगांसाठी 
- कमी विलंबता कोड कार्यांसाठी जसे की पुनरावलोकन आणि कोड सूचनांसाठी 

## मिस्त्रल स्मॉल आणि मिस्त्रल लार्ज तुलना 

मिस्त्रल स्मॉल आणि लार्जच्या विलंबता मध्ये फरक दर्शवण्यासाठी, खालील सेल्स चालवा. 

आपण 3-5 सेकंदांच्या प्रतिसाद वेळांमध्ये फरक पाहावा. तसेच त्याच प्रॉम्प्टवर प्रतिसादांची लांबी आणि शैली लक्षात घ्या.  

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

## मिस्त्रल नेमो

या धड्यात चर्चा केलेल्या इतर दोन मॉडेल्सच्या तुलनेत, मिस्त्रल नेमो एकमेव मोफत मॉडेल आहे ज्याला Apache2 लाइसेंस आहे. 

हे मिस्त्रलच्या पूर्वीच्या ओपन सोर्स LLM, मिस्त्रल 7B चे अपग्रेड म्हणून पाहिले जाते. 

नेमो मॉडेलच्या काही इतर वैशिष्ट्ये आहेत: 

- *अधिक कार्यक्षम टोकनायझेशन:* हे मॉडेल सामान्यतः वापरले जाणारे tiktoken ऐवजी Tekken टोकनायझर वापरते. यामुळे अधिक भाषांवर आणि कोडवर चांगली कार्यक्षमता मिळते. 

- *फिनेट्यूनिंग:* बेस मॉडेल फिनेट्यूनिंगसाठी उपलब्ध आहे. यामुळे ज्या वापर-केसमध्ये फिनेट्यूनिंगची आवश्यकता असू शकते अशा वापर-केससाठी अधिक लवचिकता मिळते. 

- *नैसर्गिक फंक्शन कॉलिंग* - मिस्त्रल लार्ज प्रमाणे, हे मॉडेल फंक्शन कॉलिंगवर प्रशिक्षित आहे. यामुळे हे एक अद्वितीय बनते की ओपन सोर्स मॉडेल्सपैकी एक आहे ज्याने असे केले आहे. 

### टोकनायझर्स तुलना 

या नमुन्यात, आपण मिस्त्रल नेमो टोकनायझेशन कसे हाताळते हे मिस्त्रल लार्जच्या तुलनेत पाहणार आहोत. 

दोन्ही नमुने एकाच प्रॉम्प्ट घेतात परंतु आपण पाहावे की नेमो मिस्त्रल लार्जच्या तुलनेत कमी टोकन्स परत करते. 

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

हा धडा पूर्ण केल्यानंतर, आमच्या [जनरेटिव AI लर्निंग कलेक्शन](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) पाहा, आपल्या जनरेटिव AI ज्ञानाला पुढे नेण्यासाठी!

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज हा अधिकारिक स्रोत मानला पाहिजे. महत्त्वपूर्ण माहितीसाठी, व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.