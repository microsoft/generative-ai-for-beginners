# मिस्ट्राल मोडेलहरू सँग निर्माण 

## परिचय 

यस पाठमा समेटिनेछ: 
- विभिन्न मिस्ट्राल मोडेलहरूको अन्वेषण 
- प्रत्येक मोडेलका प्रयोग केसहरू र परिदृश्यहरूको बुझाइ 
- प्रत्येक मोडेलका अनौठा विशेषताहरू प्रदर्शन गर्ने कोड नमूनाहरूको अन्वेषण। 

## मिस्ट्राल मोडेलहरू 

यस पाठमा हामी ३ विभिन्न मिस्ट्राल मोडेलहरूको अन्वेषण गर्नेछौं: 
**मिस्ट्राल ठूलो**, **मिस्ट्राल सानो** र **मिस्ट्राल नेमो**। 

यी मध्ये प्रत्येक मोडेल [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) मा निशुल्क उपलब्ध छन्। यस नोटबुकमा कोड चलाउन यी मोडेलहरू प्रयोग गरिनेछ। 

> **नोट:** GitHub Models जुलाई २०२६ को अन्त्यमा सेवानिवृत्त हुँदैछ। AI मोडेलहरू संग प्रोटोटाइप गर्न [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) प्रयोग गर्ने थप विवरणहरूको लागि यहाँ जानुहोस्। 


## मिस्ट्राल ठूलो २ (२४०७)
मिस्ट्राल ठूलो २ हाल मिस्ट्रालको प्रमुख मोडेल हो र यसलाई उद्यम प्रयोगको लागि डिजाइन गरिएको छ। 

यो मोडेल मूल मिस्ट्राल ठूलोको अपग्रेड हो जसले प्रदान गर्दछ 
-  ठूलो कन्टेक्स्ट विन्डो - १२८k बनाम ३२k 
-  गणित र कोडिङ कार्यहरूमा सुधारिएको प्रदर्शन - ७६.९% औसत सटीकता बनाम ६०.४% 
-  बहुभाषी प्रदर्शनमा वृद्धि - भाषाहरूमा समावेश: अंग्रेजी, फ्रेन्च, जर्मन, स्पेनिश, इटालियन, पोर्चुगिज, डच, रसियाली, चिनियाँ, जापानी, कोरियन, अरेबिक र हिन्दी।

यी विशेषताहरूका साथ, मिस्ट्राल ठूलो मा उत्कृष्टता छ 
- *रेकभरी अग्मेन्टेड जेनेरेसन (RAG)* - ठूलो कन्टेक्स्ट विन्डोका कारण
- *फंक्शन कलिङ* - यस मोडेलमा नेटिभ फंक्शन कलिङ छ जसले बाह्य उपकरण र API हरूसँग एकीकरण अनुमति दिन्छ। यी कलहरू समानान्तर वा अनुक्रमिक रूपमा क्रमशः गर्न सकिन्छ। 
- *कोड जेनेरेसन* - यो मोडेल पाइथन, जाभा, टाइपस्क्रिप्ट र C++ जेनेरेशनमा उत्कृष्ट छ। 

### मिस्ट्राल ठूलो २ प्रयोग गरी RAG उदाहरण 

यस उदाहरणमा, हामी मिस्ट्राल ठूलो २ प्रयोग गरी पाठ दस्तावेज़मा RAG ढाँचाले चलाइरहेका छौं। प्रश्न कोरियाली भाषामा लेखिएको छ र लेखकका कलेजअघि गरेका गतिविधिहरूका बारेमा सोध्छ। 

यसले Cohere Embeddings Model प्रयोग गरी पाठ दस्तावेज़ र प्रश्न दुवैको embeddings सिर्जना गर्छ। यस नमूनामा, faiss पाइथन प्याकेजलाई भेक्टर स्टोरको रूपमा प्रयोग गरिएको छ। 

मिस्ट्राल मोडेलमा पठाइएको प्राँप्तमा प्रश्न र प्रश्नसँग समान chunks दुवै समावेश हुन्छन्। मोडेलले त्यसपछि प्राकृतिक भाषा प्रतिक्रिया प्रदान गर्दछ। 

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

# यी तपाईंको Microsoft Foundry प्रोजेक्टको "अवलोकन" पृष्ठबाट प्राप्त गर्नुहोस्
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # दूरी, सूचकाङ्क
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

## मिस्ट्राल सानो 
मिस्ट्राल सानो मिस्ट्राल परिवारको अर्को मोडेल हो जुन प्रिमियर/उद्यम वर्ग अन्तर्गत छ। नामले जनाउँछ, यो एउटा सानो भाषा मोडेल (SLM) हो। मिस्ट्राल सानो प्रयोग गर्ने फाइदाहरू हुन्: 
- मिस्ट्राल LLMs जस्तै मिस्ट्राल ठूलो र नेमो भन्दा लागत बचत - ८०% मूल्य कटौती
- कम विलम्बता - मिस्ट्रालका LLMs भन्दा छिटो प्रतिक्रिया
- लचिलो - कम आवश्यक स्रोतहरूका साथ विभिन्न वातावरणमा तैनाथ गर्न सकिन्छ। 


मिस्ट्राल सानो उपयुक्त छ: 
- पाठ आधारित कार्यहरू जस्तै सारांश, भावना विश्लेषण र अनुवाद। 
- बारम्बार अनुरोध गरिने अनुप्रयोगहरू जहाँ लागत प्रभावशीलता आवश्यक छ 
- कम विलम्बता कोड कार्यहरू जस्तै समीक्षा र कोड सुझावहरू 

## मिस्ट्राल सानो र मिस्ट्राल ठूलो तुलना 

मिस्ट्राल सानो र ठूलो बीच विलम्बता भिन्नता देखाउन, तलका सेलहरू चलाउनुहोस्। 

तपाईंले प्रतिक्रियाको समय ३-५ सेकेण्ड फरक देख्नुहुनेछ। त्यस्तै, सोही प्राँप्तमा प्रतिक्रिया लामो र शैलीमा पनि भिन्नता हुनेछ।  

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

## मिस्ट्राल नेमो

यस पाठमा छलफल गरिएका अन्य दुई मोडेलसँग तुलना गर्दा, मिस्ट्राल नेमो मात्र एकमात्र निशुल्क मोडेल हो जसले Apache2 लाइसेन्स पाएको छ। 

यो मिस्ट्रालको पुरानो खुला स्रोत LLM, मिस्ट्राल 7B, को एक अपग्रेडको रूपमा हेरिन्छ। 

नेमो मोडेलका केही अन्य विशेषताहरू यस्ता छन्: 

- *अधिक प्रभावकारी टोकनाइजेसन:* यो मोडेलले सामान्यतया प्रयोग हुने tiktoken भन्दा Tekken टोकनाइजर प्रयोग गर्दछ। यसले बढी भाषाहरू र कोडमा राम्रो प्रदर्शन दिन्छ। 

- *फिनेट्युनिङ:* आधार मोडेल फिनेट्युनिङका लागि उपलब्ध छ। यसले आवश्यक परेका प्रयोग केसहरूमा बढी लचिलोपन दिन्छ। 

- *नेटिभ फंक्शन कलिङ* - मिस्ट्राल ठूलो जस्तै, यो मोडेल फंक्शन कलिङमा प्रशिक्षित छ। यसले यसलाई पहिलो खुला स्रोत मोडेलहरू मध्ये एकको रूपमा विशिष्ट बनाउँछ। 


### टोकनाइजर्सको तुलना 

यस नमूनामा, हामी मिस्ट्राल नेमोले टोकनाइजेसन कसरी गर्छ भनी मिस्ट्राल ठूूलोसँग तुलना गर्नेछौं। 

दुवै नमूनाले सोही प्राँप्त लिन्छन् तर तपाईंले देख्नुहुनेछ नेमोले कम टोकन फिर्ता गर्यो भन्दा मिस्ट्राल ठूलो। 

```bash
pip install mistral-common
```

```python 
# आवश्यक प्याकेजहरू आयात गर्नुहोस्:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# मिस्टआरल टोकनाइजर लोड गर्नुहोस्

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# सन्देशहरूको सूचीलाई टोकनाइज़ गर्नुहोस्
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

# टोकनहरूको संख्या गणना गर्नुहोस्
print(len(tokens))
```

```python
# आवश्यक प्याकेजहरू आयात गर्नुहोस्:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral टोकनाइजर लोड गर्नुहोस्

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# सन्देशहरूको सूची टोकन गर्नुहोस्
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

# टोकनहरूको संख्या गणना गर्नुहोस्
print(len(tokens))
```

## सिक्ने क्रम यहीँ बन्द हुँदैन, यात्रा जारी राख्नुहोस्

यस पाठ पूरा गरेपछि, हाम्रो [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) हेर्नुहोस् र आफ्नो जनरेटिभ AI ज्ञानलाई अझ उचाइमा पुर्‍याउनुहोस्!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->