<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:15:02+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "ne"
}
-->
# Mistral मोडेलहरू संग निर्माण

## परिचय

यो पाठले समेट्नेछ:
- विभिन्न Mistral मोडेलहरूको अन्वेषण
- प्रत्येक मोडेलका लागि प्रयोग केस र परिदृश्यहरूको बुझाइ
- कोड नमूनाहरूले प्रत्येक मोडेलको अनौठो विशेषताहरू देखाउँछन्।

## Mistral मोडेलहरू

यस पाठमा, हामी 3 विभिन्न Mistral मोडेलहरूको अन्वेषण गर्नेछौं: **Mistral Large**, **Mistral Small** र **Mistral Nemo**।

यी प्रत्येक मोडेलहरू Github Model बजारमा निःशुल्क उपलब्ध छन्। यस नोटबुकमा कोडले यी मोडेलहरूलाई प्रयोग गरेर कोड चलाउनेछ। यहाँ Github Models प्रयोग गरेर [AI मोडेलहरूसँग प्रोटोटाइप बनाउने](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) बारे थप विवरणहरू छन्।

## Mistral Large 2 (2407)

Mistral Large 2 हाल Mistral को प्रमुख मोडेल हो र उद्यम प्रयोगको लागि डिजाइन गरिएको छ।

यो मोडेलले मूल Mistral Large को अपग्रेड गर्दै निम्नलिखित सुविधा प्रदान गर्दछ:
- ठूलो सन्दर्भ विन्डो - 128k vs 32k
- गणित र कोडिङ कार्यहरूमा राम्रो प्रदर्शन - 76.9% औसत शुद्धता vs 60.4%
- बहुभाषी प्रदर्शनमा वृद्धि - भाषाहरू समावेश: अंग्रेजी, फ्रेन्च, जर्मन, स्पेनिश, इटालियन, पोर्तुगिज, डच, रूसी, चिनियाँ, जापानी, कोरियाली, अरबी, र हिन्दी।

यी सुविधाहरूको साथ, Mistral Large निम्नमा उत्कृष्ट छ:
- *Retrieval Augmented Generation (RAG)* - ठूलो सन्दर्भ विन्डोका कारण
- *Function Calling* - यस मोडेलले स्वदेशी फङ्सन कलिङ समावेश गर्दछ जसले बाह्य उपकरण र API हरूसँग एकीकरण गर्न अनुमति दिन्छ। यी कलहरू समानान्तरमा वा एक पछि अर्को क्रमबद्ध रूपमा गर्न सकिन्छ।
- *Code Generation* - यो मोडेल Python, Java, TypeScript र C++ जेनेरेसनमा उत्कृष्ट छ।

### RAG उदाहरण Mistral Large 2 प्रयोग गर्दै

यस उदाहरणमा, हामी Mistral Large 2 प्रयोग गरेर एक RAG ढाँचालाई पाठ दस्तावेजमा चलाउँदैछौं। प्रश्न कोरियाली भाषामा लेखिएको छ र लेखकको कलेज अघि गतिविधिहरूको बारेमा सोध्छ।

यसले Cohere Embeddings Model प्रयोग गरेर पाठ दस्तावेज र प्रश्नको इम्बेडिङहरू बनाउँछ। यस नमूनाका लागि, यसले faiss Python प्याकेजलाई भेक्टर स्टोरको रूपमा प्रयोग गर्दछ।

Mistral मोडेलमा पठाइएको प्रम्प्टमा प्रश्नहरू र प्रश्नसँग मिल्दोजुल्दो पुनःप्राप्त टुक्राहरू समावेश छन्। मोडेलले प्राकृतिक भाषा प्रतिक्रिया प्रदान गर्दछ।

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

Mistral Small, Mistral परिवारको अर्को मोडेल हो, जुन प्रमुख/उद्यम श्रेणी अन्तर्गत पर्दछ। नामले संकेत गरेजस्तै, यो मोडेल एक सानो भाषा मोडेल (SLM) हो। Mistral Small प्रयोग गर्ने फाइदाहरू निम्नलिखित छन्:
- लागत बचत Mistral LLMs जस्तै Mistral Large र NeMo सँग तुलना गर्दा - 80% मूल्य घटावट
- कम विलम्बता - Mistral का LLMs सँग तुलना गर्दा छिटो प्रतिक्रिया
- लचिलो - कम स्रोत आवश्यकताहरूमा विभिन्न वातावरणहरूमा तैनाती गर्न सकिन्छ।

Mistral Small निम्नका लागि उत्कृष्ट छ:
- पाठ आधारित कार्यहरू जस्तै सारांश, भावना विश्लेषण र अनुवाद।
- लागत प्रभावकारिताका कारण बारम्बार अनुरोध गरिने एप्लिकेसनहरू
- कम विलम्बता कोड कार्यहरू जस्तै समीक्षा र कोड सुझावहरू

## Mistral Small र Mistral Large को तुलना

Mistral Small र Large बीचको विलम्बता भिन्नता देखाउन, तलका कोषहरू चलाउनुहोस्।

तपाईंले 3-5 सेकेन्डको प्रतिक्रिया समयको भिन्नता देख्नुपर्छ। साथै समान प्रम्प्टमा प्रतिक्रिया लम्बाई र शैलीलाई नोट गर्नुहोस्।

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

यस पाठमा छलफल गरिएका अन्य दुई मोडेलहरूसँग तुलना गर्दा, Mistral NeMo मात्र एक निःशुल्क मोडेल हो जुन Apache2 लाइसेन्सको साथ आउँछ।

यसलाई पहिलेको खुला स्रोत LLM Mistral, Mistral 7B को अपग्रेडको रूपमा हेरिन्छ।

NeMo मोडेलका केही अन्य विशेषताहरू छन्:

- *अधिक कुशल टोकनाइजेशन:* यो मोडेलले साधारणतया प्रयोग गरिने tiktoken भन्दा Tekken टोकनाइजर प्रयोग गर्दछ। यसले धेरै भाषाहरू र कोडमा राम्रो प्रदर्शनको अनुमति दिन्छ।

- *फाइनट्यूनिङ:* आधार मोडेल फाइनट्यूनिङको लागि उपलब्ध छ। यसले फाइनट्यूनिङ आवश्यक हुन सक्ने प्रयोग केसहरूको लागि बढी लचिलोपनको अनुमति दिन्छ।

- *स्वदेशी फङ्सन कलिङ* - Mistral Large जस्तै, यो मोडेल फङ्सन कलिङमा प्रशिक्षित गरिएको छ। यसले यसलाई पहिलो खुला स्रोत मोडेलहरू मध्ये एक बनाउँछ जसले यस्तो गर्दछ।

### टोकनाइजरहरूको तुलना

यस नमूनामा, हामी Mistral NeMo ले Mistral Large सँग तुलना गर्दा टोकनाइजेशन कसरी सम्हाल्छ हेर्नेछौं।

दुवै नमूनाहरूले समान प्रम्प्ट लिन्छन् तर तपाईंले देख्नुपर्छ कि NeMo ले Mistral Large भन्दा कम टोकनहरू फिर्ता गर्छ।

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

## सिकाइ यहाँ रोकिन्न, यात्रा जारी राख्नुहोस्

यो पाठ पूरा गरेपछि, हाम्रो [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) हेर्नुहोस् ताकि आफ्नो Generative AI ज्ञानलाई अझ उचाइमा पुर्याउन सक्नुहोस्!

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको छ। हामी यथार्थताको प्रयास गर्दैछौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा असत्यताहरू हुन सक्छ। यसको मूल भाषा मा रहेको दस्तावेजलाई आधिकारिक स्रोत मान्नुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुनेछैनौं।