<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:54:51+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "ne"
}
-->
# Mistral मोडेलहरूसँग निर्माण

## परिचय

यो पाठले समेट्नेछ:
- विभिन्न Mistral मोडेलहरूको अन्वेषण
- प्रत्येक मोडेलको प्रयोग केस र परिदृश्यहरूको बुझाइ
- कोड नमूनाहरूले प्रत्येक मोडेलको अद्वितीय विशेषताहरू देखाउँछन्।

## Mistral मोडेलहरू

यस पाठमा, हामी ३ विभिन्न Mistral मोडेलहरू अन्वेषण गर्नेछौं: **Mistral Large**, **Mistral Small** र **Mistral Nemo**।

यी मोडेलहरू प्रत्येक Github Model बजारमा निःशुल्क उपलब्ध छन्। यस नोटबुकको कोडले यी मोडेलहरू प्रयोग गरेर कोड चलाउनेछ। यहाँ Github Models प्रयोग गरेर [AI मोडेलहरूसँग प्रोटोटाइप गर्ने](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) बारे थप विवरणहरू छन्।

## Mistral Large 2 (2407)
Mistral Large 2 हाल Mistral बाट प्रमुख मोडेल हो र उद्यम प्रयोगको लागि डिजाइन गरिएको छ।

यो मोडेलले मूल Mistral Large मा सुधार गरेको छ:
- ठूलो सन्दर्भ विन्डो - 128k vs 32k
- गणित र कोडिङ कार्यहरूमा राम्रो प्रदर्शन - 76.9% औसत शुद्धता vs 60.4%
- बहुभाषी प्रदर्शनमा वृद्धि - भाषाहरूमा समावेश: अंग्रेजी, फ्रेन्च, जर्मन, स्पेनिश, इटालियन, पोर्तुगिज, डच, रसियन, चिनियाँ, जापानी, कोरियाली, अरबी, र हिन्दी।

यी विशेषताहरूको साथ, Mistral Large उत्कृष्ट छ:
- *Retrieval Augmented Generation (RAG)* - ठूलो सन्दर्भ विन्डोको कारण
- *Function Calling* - यस मोडेलसँग स्वदेशी फङ्क्शन कलिंग छ जसले बाह्य उपकरणहरू र API हरूसँग एकीकरणको अनुमति दिन्छ। यी कलहरू समानान्तरमा वा एक पछि अर्को क्रमिक रूपमा गर्न सकिन्छ।
- *Code Generation* - यो मोडेल Python, Java, TypeScript र C++ जेनेरेशनमा उत्कृष्ट छ।

### RAG उदाहरण Mistral Large 2 प्रयोग गर्दै

यस उदाहरणमा, हामी Mistral Large 2 प्रयोग गर्दै एक RAG ढाँचा टेक्स्ट दस्तावेजमा चलाउँदैछौं। प्रश्न कोरियाली भाषामा लेखिएको छ र लेखकको कलेज अघि गतिविधिहरूको बारेमा सोध्छ।

यो Cohere Embeddings Model प्रयोग गरेर टेक्स्ट दस्तावेजको साथै प्रश्नको इम्बेडिङ बनाउँछ। यस नमूनाको लागि, यसले faiss Python प्याकेजलाई भेक्टर स्टोरको रूपमा प्रयोग गर्दछ।

Mistral मोडेललाई पठाइएको प्रॉम्प्टमा प्रश्नहरू र प्रश्नसँग मिल्दोजुल्दो खण्डहरू समावेश छन्। मोडेलले त्यसपछि प्राकृतिक भाषा प्रतिक्रिया प्रदान गर्दछ।

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
Mistral Small Mistral मोडेलहरूको परिवारमा अर्को मोडेल हो प्रिमियर/उद्यम वर्गअन्तर्गत। नामले जनाएझैं, यो मोडेल एक सानो भाषा मोडेल (SLM) हो। Mistral Small प्रयोग गर्ने फाइदाहरू छन् कि यो:
- Mistral LLM जस्तै Mistral Large र NeMo भन्दा लागत बचत - 80% मूल्य कमी
- कम विलम्बता - Mistral का LLM हरूसँग तुलना गर्दा छिटो प्रतिक्रिया
- लचिलो - कम आवश्यक संसाधनहरूको सीमाबिना विभिन्न वातावरणहरूमा तैनात गर्न सकिन्छ।

Mistral Small उत्कृष्ट छ:
- पाठ आधारित कार्यहरू जस्तै संक्षेपण, भावना विश्लेषण र अनुवाद।
- यसको लागत प्रभावकारिताको कारण बारम्बार अनुरोध गरिने अनुप्रयोगहरूमा
- कम विलम्बता कोड कार्यहरू जस्तै समीक्षा र कोड सुझावहरू

## Mistral Small र Mistral Large तुलना गर्दै

Mistral Small र Large बीचको विलम्बता भिन्नता देखाउन, तलको सेलहरू चलाउनुहोस्।

तपाईंले ३-५ सेकेन्डको बीचमा प्रतिक्रिया समयको भिन्नता देख्नुपर्नेछ। साथै समान प्रॉम्प्टमा प्रतिक्रिया लम्बाई र शैली नोट गर्नुहोस्।

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

यस पाठमा छलफल गरिएको अन्य दुई मोडेलहरूसँग तुलना गर्दा, Mistral NeMo मात्र Apache2 लाइसेन्सको साथ निःशुल्क मोडेल हो।

यसलाई Mistral को प्रारम्भिक ओपन सोर्स LLM, Mistral 7B को अपग्रेडको रूपमा हेरिन्छ।

NeMo मोडेलका केही अन्य विशेषताहरू छन्:

- *अधिक कुशल टोकनाइजेशन:* यो मोडेलले सामान्यतया प्रयोग गरिने tiktoken भन्दा Tekken टोकनाइजर प्रयोग गर्दछ। यसले अधिक भाषाहरू र कोडमा राम्रो प्रदर्शनको अनुमति दिन्छ।

- *फाइनट्यूनिंग:* आधार मोडेल फाइनट्यूनिंगको लागि उपलब्ध छ। यसले फाइनट्यूनिंग आवश्यक हुनसक्ने प्रयोग केसहरूमा अधिक लचिलोपनको अनुमति दिन्छ।

- *स्वदेशी फङ्क्शन कलिंग* - Mistral Large जस्तै, यो मोडेल फङ्क्शन कलिंगमा प्रशिक्षित गरिएको छ। यसले यसलाई यस कार्यलाई गर्ने पहिलो ओपन सोर्स मोडेलहरू मध्ये एकको रूपमा अद्वितीय बनाउँछ।

### टोकनाइजरहरूको तुलना गर्दै

यस नमूनामा, हामी Mistral NeMo ले Mistral Large सँग तुलना गर्दा कसरी टोकनाइजेशनलाई ह्यान्डल गर्छ हेर्नेछौं।

दुबै नमूनाहरू समान प्रॉम्प्ट लिन्छन् तर तपाईंले NeMo ले Mistral Large भन्दा कम टोकनहरू फिर्ता गरेको देख्नुपर्नेछ।

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

## सिकाइ यहाँ रोकिदैन, यात्रा जारी राख्नुहोस्

यस पाठ समाप्त गरेपछि, हाम्रो [Generative AI Learning संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) जाँच गर्नुहोस् आफ्नो Generative AI ज्ञान स्तरवृद्धि गर्न जारी राख्न!

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) को प्रयोग गरेर अनुवाद गरिएको हो। हामी यथार्थताको लागि प्रयास गर्छौं, तर कृपया सचेत रहनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। यसको मौलिक भाषामा रहेको मूल दस्तावेजलाई प्राधिकृत स्रोत मान्नुपर्छ। महत्त्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुनेछैनौं।