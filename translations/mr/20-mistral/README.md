<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:14:38+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "mr"
}
-->
# मिस्त्रल मॉडेल्ससह बांधणी

## परिचय

या धड्यात आपण शिकणार आहोत:
- वेगवेगळ्या मिस्त्रल मॉडेल्सचा अभ्यास
- प्रत्येक मॉडेलसाठी वापराचे प्रकार आणि परिस्थिती समजून घेणे
- कोड नमुने जे प्रत्येक मॉडेलची अनोखी वैशिष्ट्ये दर्शवतात

## मिस्त्रल मॉडेल्स

या धड्यात, आपण 3 वेगवेगळ्या मिस्त्रल मॉडेल्सचा अभ्यास करू:
**मिस्त्रल लार्ज**, **मिस्त्रल स्मॉल** आणि **मिस्त्रल नेमो**.

ही सर्व मॉडेल्स Github मॉडेल मार्केटप्लेसवर मोफत उपलब्ध आहेत. या नोटबुकमधील कोड या मॉडेल्सचा वापर करून कोड चालवेल. [AI मॉडेल्ससह प्रोटोटाइप करण्यासाठी Github Models](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) वापरण्याबद्दल अधिक तपशील येथे आहेत.

## मिस्त्रल लार्ज 2 (2407)
मिस्त्रल लार्ज 2 हे सध्या मिस्त्रलचे प्रमुख मॉडेल आहे आणि ते एंटरप्राइझ वापरासाठी डिझाइन केलेले आहे.

मूळ मिस्त्रल लार्जच्या तुलनेत हे मॉडेल सुधारणा देते:
- मोठे संदर्भ विंडो - 128k विरुद्ध 32k
- गणित आणि कोडिंग कार्यांवर चांगली कामगिरी - 76.9% सरासरी अचूकता विरुद्ध 60.4%
- बहुभाषिक कामगिरी वाढली - भाषा समाविष्ट: इंग्रजी, फ्रेंच, जर्मन, स्पॅनिश, इटालियन, पोर्तुगीज, डच, रशियन, चिनी, जपानी, कोरियन, अरबी आणि हिंदी.

या वैशिष्ट्यांसह, मिस्त्रल लार्ज उत्कृष्ट आहे:
- *रिट्रीवल ऑगमेंटेड जनरेशन (RAG)* - मोठ्या संदर्भ विंडोमुळे
- *फंक्शन कॉलिंग* - या मॉडेलमध्ये स्थानिक फंक्शन कॉलिंग आहे जे बाह्य साधने आणि API सह एकत्रिकरण करण्यास अनुमती देते. हे कॉल्स समांतर किंवा एकानंतर एक अनुक्रमिक क्रमाने केले जाऊ शकतात.
- *कोड जनरेशन* - हे मॉडेल पायथन, जावा, टाइपस्क्रिप्ट आणि C++ जनरेशनवर उत्कृष्ट आहे.

### RAG उदाहरण मिस्त्रल लार्ज 2 वापरून

या उदाहरणात, आपण मिस्त्रल लार्ज 2 वापरून टेक्स्ट डॉक्युमेंटवर RAG पॅटर्न चालवत आहोत. प्रश्न कोरियन भाषेत लिहिला आहे आणि लेखकाच्या कॉलेजपूर्वीच्या क्रियाकलापांबद्दल विचारतो.

हे Cohere Embeddings मॉडेलचा वापर करून टेक्स्ट डॉक्युमेंट तसेच प्रश्नाचे एम्बेडिंग तयार करते. या नमुन्यासाठी, हे faiss पायथन पॅकेजला वेक्टर स्टोअर म्हणून वापरते.

मिस्त्रल मॉडेलला पाठवलेले प्रॉम्प्ट प्रश्न आणि प्रश्नाशी संबंधित समान तुकड्यांचा समावेश करते. मॉडेल नंतर नैसर्गिक भाषेत प्रतिसाद देते.

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
मिस्त्रल स्मॉल हे मिस्त्रल मॉडेल्सच्या कुटुंबातील आणखी एक मॉडेल आहे जे प्रीमियर/एंटरप्राइझ श्रेणीतील आहे. नावाप्रमाणे, हे मॉडेल एक लहान भाषा मॉडेल (SLM) आहे. मिस्त्रल स्मॉल वापरण्याचे फायदे म्हणजे:
- मिस्त्रल LLMs सारख्या मिस्त्रल लार्ज आणि नेमोच्या तुलनेत खर्च बचत - 80% किंमत कमी
- कमी विलंब - मिस्त्रलच्या LLMsच्या तुलनेत जलद प्रतिसाद
- लवचिक - कमी संसाधनांच्या आवश्यकता असलेल्या विविध वातावरणांमध्ये तैनात केले जाऊ शकते.

मिस्त्रल स्मॉल हे उत्कृष्ट आहे:
- सारांश, भावना विश्लेषण आणि भाषांतर यांसारख्या टेक्स्ट आधारित कार्यांसाठी.
- कमी खर्चामुळे वारंवार विनंत्या केल्या जातात अशा अनुप्रयोगांसाठी
- कमी विलंब कोड कार्यांसाठी जसे की पुनरावलोकन आणि कोड सूचना

## मिस्त्रल स्मॉल आणि मिस्त्रल लार्जची तुलना

मिस्त्रल स्मॉल आणि लार्जमधील विलंबातील फरक दाखवण्यासाठी, खालील सेल्स चालवा.

आपण प्रतिसाद वेळेत 3-5 सेकंदांचा फरक पाहू शकता. तसेच त्याच प्रॉम्प्टवरील प्रतिसादांची लांबी आणि शैली लक्षात घ्या.

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

या धड्यात चर्चा केलेल्या इतर दोन मॉडेल्सच्या तुलनेत, मिस्त्रल नेमो हे एकमेव मोफत मॉडेल आहे ज्यामध्ये Apache2 परवाना आहे.

हे मिस्त्रलच्या पूर्वीच्या ओपन सोर्स LLM, मिस्त्रल 7B चे अपग्रेड म्हणून पाहिले जाते.

नेमो मॉडेलची काही अन्य वैशिष्ट्ये आहेत:

- *अधिक कार्यक्षम टोकनायझेशन:* हे मॉडेल सामान्यतः वापरल्या जाणाऱ्या टिकटोकनच्या तुलनेत टेक्केन टोकनायझर वापरते. हे अधिक भाषांमध्ये आणि कोडवर चांगली कामगिरी करण्यास अनुमती देते.

- *फाइनट्यूनिंग:* बेस मॉडेल फाइनट्यूनिंगसाठी उपलब्ध आहे. ज्या वापराच्या प्रकरणांमध्ये फाइनट्यूनिंग आवश्यक असू शकते अशा अधिक लवचिकतेसाठी हे परवानगी देते.

- *मूळ फंक्शन कॉलिंग* - मिस्त्रल लार्जप्रमाणे, या मॉडेलला फंक्शन कॉलिंगवर प्रशिक्षण दिले गेले आहे. हे असे करणारे पहिले ओपन सोर्स मॉडेल म्हणून ते अद्वितीय बनवते.

### टोकनायझर्सची तुलना

या नमुन्यात, आपण मिस्त्रल नेमो कसे टोकनायझेशन हाताळते ते पाहू.

दोन्ही नमुने एकाच प्रॉम्प्टचा वापर करतात परंतु आपण पाहू शकता की नेमो मिस्त्रल लार्जच्या तुलनेत कमी टोकन्स परत करते.

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

हा धडा पूर्ण केल्यानंतर, आमच्या [जनरेटिव्ह AI लर्निंग संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ला पहा आणि आपल्या जनरेटिव्ह AI ज्ञानाला वाढवा!

**अस्वीकृती**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ भाषेतील दस्तऐवज अधिकृत स्रोत मानला पाहिजे. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थाबद्दल आम्ही जबाबदार नाही.