# Mistral मोडेलहरूसँग निर्माण गर्दै 

## परिचय 

यस पाठले समावेश गर्दछ: 
- विभिन्न Mistral मोडेलहरूको अन्वेषण 
- हरेक मोडेलका प्रयोग केसहरू र परिदृश्यहरूको बुझाइ 
- हरेक मोडेलका अनौठा सुविधाहरू देखाउने कोड नमूनाहरूको अन्वेषण। 

## Mistral मोडेलहरू 

यस पाठमा, हामी ३ विभिन्न Mistral मोडेलहरू अन्वेषण गर्नेछौँ: 
**Mistral Large**, **Mistral Small** र **Mistral Nemo**। 

यी मध्ये प्रत्येक मोडेल [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) मा निःशुल्क उपलब्ध छ। यस नोटबुकको कोड चलाउन यी मोडेलहरू प्रयोग गरिनेछ। 

> **ध्यान दिनुहोस्:** GitHub Models जुलाई २०२६ को अन्त्यमा सेवा बन्द गर्दैछ। यहाँ [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) प्रयोग गरेर AI मोडेलहरूसँग प्रोटोटाइपिङ गर्ने बारे थप विवरणहरू छन्। 


## Mistral Large 2 (२४०७)
Mistral Large 2 हाल Mistral बाट प्रमुख मोडेल हो र उद्यम प्रयोगको लागि डिजाइन गरिएको छ। 

यो मोडेल मूल Mistral Large को उन्नत संस्करण हो जसले प्रदान गर्दछ 
-  ठूलो सन्दर्भ विन्डो - १२८k बनाम ३२k 
-  गणित र कोडिङ कार्यहरूमा सुधारिएको प्रदर्शन - ७६.९% औसत शुद्धता बनाम ६०.४% 
-  बढेको बहुभाषिक प्रदर्शन - भाषा समावेश: अंग्रेजी, फ्रेंच, जर्मन, स्पेनिश, इटालियन, पोर्तुगाली, डच, रुसी, चिनियाँ, जापानी, कोरियन, अरबी, र हिन्दी।

यी सुविधाहरूका साथ, Mistral Large उत्कृष्ट छ 
- *रिट्रिभल अगुमेण्टेड जेनेरेशन (RAG)* - ठूलो सन्दर्भ विन्डोका कारण
- *फंक्शन कलिङ* - यो मोडेलसँग स्थानीय फंक्शन कलिङ छ जसले बाह्य उपकरणहरू र API हरूसँग एकीकृत गर्न अनुमति दिन्छ। यी कलहरू समानान्तरमा वा एकपश्चात अर्को क्रममा गर्न सकिन्छ। 
- *कोड जेनेरेशन* - यो मोडेलले Python, Java, TypeScript र C++ निर्माणमा उत्कृष्टता देखाउँछ। 

### Mistral Large 2 प्रयोग गरेर RAG उदाहरण 

यो उदाहरणमा, हामी Mistral Large 2 प्रयोग गरेर एउटा पाठ दस्तावेजमा RAG ढाँचा चलाउँदैछौं। प्रश्न कोरियन भाषामा लेखिएको छ र लेखकको कलेजअघि गतिविधिहरूको बारेमा सोधिएको छ। 

यसले Cohere Embeddings मोडेल प्रयोग गरेर पाठ दस्तावेज र प्रश्नको एम्बेडिङ बनाउँछ। यस नमूनाको लागि, faiss Python प्याकेज भेक्टर स्टोरको रूपमा प्रयोग गरिन्छ। 

जुन प्रम्प्ट Mistral मोडेललाई पठाइन्छ, त्यसमा दुवै प्रश्न र सोधिएको प्रश्नसँग मिल्दोजुल्दो फेला पारिएका भागहरू छन्। त्यसपछि मोडेलले प्राकृतिक भाषा प्रतिक्रियाहरू प्रदान गर्दछ। 

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

# यी तपाइँको Microsoft Foundry परियोजनाको "अवलोकन" पृष्ठबाट प्राप्त गर्नुहोस्
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # दूरी, अनुक्रमणिका
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
Mistral Small पनि Mistral परिवारको प्रिमियर/उद्यम वर्ग अन्तर्गतको अर्को मोडेल हो। नामले संकेत गर्ने गरी, यो मोडेल सानो भाषा मोडेल (SLM) हो। Mistral Small प्रयोग गर्दा फाइदाहरू हुन्: 
- Mistral LLMs जस्तै Mistral Large र NeMo भन्दा लागत बचत - ८०% मूल्य कमी
- न्यून विलम्ब - Mistral का LLMs भन्दा छिटो प्रतिक्रिया
- लचिलो - आवश्यक स्रोतहरूमा कम प्रतिबन्धका साथ विभिन्न वातावरणमा तैनाथ गर्न सकिन्छ। 


Mistral Small उत्कृष्ट छ: 
- सारांश, भावना विश्लेषण र अनुवादजस्ता पाठ आधारित कार्यहरूको लागि। 
- बारम्बार अनुरोधहरू हुने अनुप्रयोगहरूमा यसको लागत प्रभावशीलताका कारण 
- न्यून विलम्ब कोड कार्यहरू जस्तै समीक्षा र कोड सुझावहरू

## Mistral Small र Mistral Large को तुलना 

Mistral Small र Large बीच विलम्बता फरक देखाउन तलको सेल्लहरू चलाउनुहोस्। 

तपाईले प्रतिक्रिया समयमा ३-५ सेकेन्डको फरक देख्नुहुनेछ। साथै एउटै प्रम्प्टमा प्रतिक्रिया लम्बाइ र शैली पनि नोट गर्नुहोस्।  

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

## Mistral NeMo

यी दुई मोडेलहरू भन्दा छुट्टै, Mistral NeMo मात्रै नि:शुल्क मोडेल हो जसमा Apache2 लाइसेन्स छ। 

यसलाई प्रारम्भिक खुला स्रोत LLM, Mistral 7B को उन्नत संस्करणको रूपमा हेरिन्छ। 

NeMo मोडेलका केही अन्य सुविधाहरू छन्: 

- *अधिक कुशल टोकनाइजेशन:* यो मोडेलले सामान्यतः प्रयोग हुने tiktoken भन्दा Tekken टोकनाइजर प्रयोग गर्छ। यसले बढी भाषाहरू र कोडमा राम्रो प्रदर्शन दिन्छ। 

- *फिनट्यूनिङ:* आधार मोडेल फिनट्यूनिङका लागि उपलब्ध छ। यसले फिनट्यूनिङ आवश्यक पर्ने प्रयोग केसहरूमा बढी लचिलोपन दिन्छ। 

- *स्थानीय फंक्शन कलिङ* - Mistral Large जस्तै, यो मोडेल पनि फंक्शन कलिङमा तालिम प्राप्त छ। यसले खोल्ला स्रोत मोडेलहरूमा पहिलोहरूमध्ये एक बनेको छ। 


### टोकनाइजरहरूको तुलना 

यस नमूनामा, हामी हेरौं कि Mistral NeMo कसरी Mistral Large संग तुलना गर्दा टोकनाइजेशन ह्यान्डल गर्छ। 

दुबै नमूनाले एउटै प्रम्प्ट लिन्छ तर तपाईंले देख्नुहुनेछ कि NeMo ले Mistral Large भन्दा कम टोकनहरू फर्काउँछ। 

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

# Mistral टोकनाइजर लोड गर्नुहोस्

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# सन्देशहरूको सूचीलाई टोकनाइज गर्नुहोस्
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

# सन्देशहरूको सूचीलाई टोकनाइज गर्नुहोस्
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

## सिकाइ यहाँ रोकिएन, यात्रा जारी राख्नुहोस्

यस पाठ पूर्ण गरेपछि, हाम्रो [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) मा जानुहोस् र आफ्नो Generative AI ज्ञानलाई अझ उच्च स्तरमा लैजानुहोस्!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->