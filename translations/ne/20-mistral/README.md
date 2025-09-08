<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:58:30+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "ne"
}
-->
# Mistral मोडेलहरूसँग निर्माण गर्ने

## परिचय

यस पाठले समेट्नेछ:  
- विभिन्न Mistral मोडेलहरूको अन्वेषण  
- प्रत्येक मोडेलका प्रयोग केसहरू र परिदृश्यहरू बुझ्ने  
- कोड नमूनाहरूले प्रत्येक मोडेलका अनौठा विशेषताहरू देखाउने  

## Mistral मोडेलहरू

यस पाठमा, हामी ३ विभिन्न Mistral मोडेलहरू अन्वेषण गर्नेछौं:  
**Mistral Large**, **Mistral Small** र **Mistral Nemo**।

यी प्रत्येक मोडेलहरू Github Model बजारमा निःशुल्क उपलब्ध छन्। यस नोटबुकको कोडले यी मोडेलहरू प्रयोग गरेर कोड चलाउनेछ। Github मोडेलहरूलाई [AI मोडेलहरूसँग प्रोटोटाइप गर्न](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) प्रयोग गर्ने बारे थप विवरण यहाँ छ।  

## Mistral Large 2 (2407)  
Mistral Large 2 हाल Mistral को प्रमुख मोडेल हो र उद्यम प्रयोगका लागि डिजाइन गरिएको छ।  

यो मोडेल मूल Mistral Large को अपग्रेड हो जसले प्रदान गर्दछ:  
- ठूलो सन्दर्भ विन्डो - १२८k बनाम ३२k  
- गणित र कोडिङ कार्यहरूमा राम्रो प्रदर्शन - ७६.९% औसत शुद्धता बनाम ६०.४%  
- बहुभाषिक प्रदर्शनमा वृद्धि - भाषाहरूमा: अंग्रेजी, फ्रेन्च, जर्मन, स्पेनिश, इटालियन, पोर्चुगिज, डच, रुसी, चिनियाँ, जापानी, कोरियन, अरबी, र हिन्दी समावेश छन्।  

यी विशेषताहरूका साथ, Mistral Large उत्कृष्ट छ:  
- *Retrieval Augmented Generation (RAG)* - ठूलो सन्दर्भ विन्डोको कारण  
- *Function Calling* - यस मोडेलमा नेटिभ फंक्शन कलिङ छ जसले बाह्य उपकरण र API हरूसँग एकीकरण गर्न अनुमति दिन्छ। यी कलहरू समानान्तर वा अनुक्रमिक रूपमा गर्न सकिन्छ।  
- *Code Generation* - यो मोडेल Python, Java, TypeScript र C++ कोड उत्पादनमा उत्कृष्ट छ।  

### Mistral Large 2 प्रयोग गरेर RAG उदाहरण  

यस उदाहरणमा, हामी Mistral Large 2 प्रयोग गरेर एउटा पाठ दस्तावेजमा RAG ढाँचा चलाउँदैछौं। प्रश्न कोरियन भाषामा लेखिएको छ र लेखकको कलेज अघि के गतिविधिहरू थिए भनेर सोध्छ।  

यसले Cohere Embeddings Model प्रयोग गरेर पाठ दस्तावेज र प्रश्न दुवैको embeddings बनाउँछ। यस नमूनामा, faiss Python प्याकेजलाई भेक्टर स्टोरको रूपमा प्रयोग गरिएको छ।  

Mistral मोडेललाई पठाइएको प्रॉम्प्टमा प्रश्नहरू र प्रश्नसँग मिल्दोजुल्दो पुनःप्राप्त खण्डहरू दुवै समावेश छन्। मोडेलले त्यसपछि प्राकृतिक भाषा प्रतिक्रिया प्रदान गर्दछ।  

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
Mistral Small Mistral परिवारको अर्को मोडेल हो जुन प्रिमियर/उद्यम वर्गमा पर्दछ। नामले नै जनाउँछ, यो सानो भाषा मोडेल (SLM) हो। Mistral Small प्रयोग गर्दा फाइदाहरू छन्:  
- Mistral LLM जस्तै Mistral Large र NeMo को तुलनामा लागत बचत - ८०% मूल्य घटावट  
- कम विलम्बता - Mistral का LLM हरूको तुलनामा छिटो प्रतिक्रिया  
- लचिलो - विभिन्न वातावरणहरूमा कम स्रोत आवश्यकतासँग सजिलै तैनाथ गर्न सकिन्छ।  

Mistral Small उत्कृष्ट छ:  
- पाठ आधारित कार्यहरू जस्तै सारांश, भावना विश्लेषण र अनुवादका लागि  
- लागत प्रभावकारिताका कारण बारम्बार अनुरोध गरिने अनुप्रयोगहरूमा  
- समीक्षा र कोड सुझाव जस्ता कम विलम्बता कोड कार्यहरूमा  

## Mistral Small र Mistral Large को तुलना  

Mistral Small र Large बीच विलम्बतामा फरक देखाउन तलका सेलहरू चलाउनुहोस्।  

तपाईंले ३-५ सेकेन्डको फरक प्रतिक्रिया समय देख्नु पर्नेछ। साथै एउटै प्रॉम्प्टमा प्रतिक्रिया लम्बाइ र शैलीमा पनि फरक नोट गर्नुहोस्।  

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

यस पाठमा छलफल गरिएका अन्य दुई मोडेलहरूको तुलनामा, Mistral NeMo मात्र Apache2 लाइसेन्स भएको निःशुल्क मोडेल हो।  

यसलाई Mistral को पहिलेको खुला स्रोत LLM, Mistral 7B को अपग्रेडको रूपमा हेरिन्छ।  

NeMo मोडेलका केही अन्य विशेषताहरू:  

- *अधिक प्रभावकारी टोकनाइजेशन:* यो मोडेलले सामान्यतया प्रयोग हुने tiktoken को सट्टा Tekken tokenizer प्रयोग गर्छ। यसले धेरै भाषाहरू र कोडमा राम्रो प्रदर्शन दिन्छ।  

- *फाइनट्यूनिङ:* आधार मोडेल फाइनट्यूनिङका लागि उपलब्ध छ। यसले फाइनट्यूनिङ आवश्यक पर्ने प्रयोग केसहरूमा बढी लचिलोपन दिन्छ।  

- *नेटिभ फंक्शन कलिङ* - Mistral Large जस्तै, यस मोडेललाई पनि फंक्शन कलिङमा तालिम दिइएको छ। यसले यसलाई पहिलो खुला स्रोत मोडेलहरूमध्ये एक बनाउँछ।  

### टोकनाइजर्सको तुलना  

यस नमूनामा, हामी Mistral NeMo ले टोकनाइजेशन कसरी गर्छ भनेर Mistral Large सँग तुलना गर्नेछौं।  

दुवै नमूनाले एउटै प्रॉम्प्ट लिन्छन् तर तपाईंले देख्नु पर्नेछ कि NeMo ले Mistral Large को तुलनामा कम टोकन फर्काउँछ।  

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

## सिकाइ यहाँ रोकिँदैन, यात्रा जारी राख्नुहोस्

यस पाठ पूरा गरेपछि, हाम्रो [Generative AI Learning संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) हेर्नुहोस् र आफ्नो Generative AI ज्ञानलाई अझ उचाइमा पुर्‍याउनुहोस्!

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।