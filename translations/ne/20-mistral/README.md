# मिस्टारल मोडेलहरूसँग निर्माण गर्दै 

## परिचय 

यस पाठ्यक्रमले समेट्नेछ: 
- विभिन्न मिस्टारल मोडेलहरूको अन्वेषण 
- प्रत्येक मोडेलका प्रयोग र परिस्थिति बुझ्नु 
- प्रत्येक मोडेलका विशेषताहरू देखाउने कोड नमूनाहरूको अन्वेषण। 

## मिस्टारल मोडेलहरू 

यस पाठ्यक्रममा, हामी ३ विभिन्न मिस्टारल मोडेलहरू अन्वेषण गर्नेछौं: 
**मिस्टारल ठूलो**, **मिस्टारल सानो** र **मिस्टारल नेमो**। 

यी प्रत्येक मोडेलहरु GitHub मोडेल मार्केटप्लेसमा निःशुल्क उपलब्ध छन्। यस नोटबुकमा रहेको कोडले यी मोडेलहरू चलाउन प्रयोग गर्नेछ। GitHub मोडेलहरू प्रयोग गरि AI मोडेलहरूसँग [प्रोटोटाइप गर्ने](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) सम्बन्धी थप विवरणहरू यहाँ छन्। 


## मिस्टारल ठूलो २ (२४०७)
मिस्टारल ठूलो २ हाल मिस्टारलको प्रमुख मोडेल हो र यो उद्यम प्रयोगका लागि डिजाइन गरिएको हो। 

यो मोडेल मूल मिस्टारल ठूलोको एक उन्नयन हो जसले प्रदान गर्दछ 
-  ठूलो सन्दर्भ विन्डो - १२८क बनाम ३२क 
-  गणित र कोडिङ कार्यहरूमा राम्रो प्रदर्शन - ७६.९% औसत शुद्धता बनाम ६०.४% 
-  बहुभाषिक प्रदर्शनमा वृद्धि - भाषाहरूमा समावेश छन्: अंग्रेजी, फ्रेन्च, जर्मन, स्पेनिश, इटालियन, पोर्चुगिज, डच, रसियन, चिनियाँ, जापानी, कोरियन, अरबी, र हिन्दी।

यी सुविधाहरूका साथ, मिस्टारल ठूलो उत्कृष्ट छ 
- *रिट्राइवल अग्मेन्टेड जेनेरेसन (RAG)* - ठूलो सन्दर्भ विन्डोको कारणले गर्दा
- *फंक्शन कलिंग* - यस मोडेलमा देशी फंक्शन कलिंग छ जसले बाह्य उपकरण र API सँग एकीकरण अनुमति दिन्छ। यी कलहरू एकै समयमा वा क्रमशः एकपछि अर्को गरिन सक्छन्। 
- *कोड जेनेरेसन* - यस मोडेलले पाइथन, जाभा, टाइपस्क्रिप्ट, र C++ जेनेरेसनमा उत्कृष्टता देखाउँछ। 

### मिस्टारल ठूलो २ प्रयोग गरेर RAG उदाहरण 

यस उदाहरणमा, हामी मिस्टारल ठूलो २ प्रयोग गरी RAG ढाँचा एउटा पाठ दस्तावेजमा चलाउँदैछौं। प्रश्न कोरियनमा लेखिएको छ र लेखकका कलेज अघि गरेका गतिविधिहरूको बारेमा सोध्छ। 

यसले पाठ दस्तावेजको र प्रश्नको एम्बेडिङ बनाउन Cohere Embeddings मोडेल प्रयोग गर्छ। यस नमूनामा, faiss पाइथन प्याकेज भेक्टर स्टोरको रूपमा प्रयोग गरिएको छ। 

मिस्टारल मोडेलमा पठाइएको प्रॉम्प्टमा दुबै प्रश्न र प्रश्नसँग समान retrieved chunks समावेश छन्। मोडेलले त्यसपछि प्राकृतिक भाषा उत्तर दिन्छ। 

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

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # दूरी, सुचकांक
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

## मिस्टारल सानो 
मिस्टारल सानो मोडेल मिस्टारल परिवारको अर्को मोडेल हो जुन प्रिमियर/उद्यम श्रेणीमा पर्दछ। नामले नै संकेत गरेझैं, यो मोडेल सानो भाषा मोडेल (SLM) हो। मिस्टारल सानो प्रयोग गर्दा फाइदाहरू हुन्: 
- मिस्टारल LLM जस्तै मिस्टारल ठूलो र NeMo को तुलनामा लागत बचत - ८०% मूल्य घटावट
- कम विलम्बता - मिस्टारलका LLMहरूभन्दा छिटो प्रतिक्रिया
- लचिलो - कम आवश्यक स्रोतहरूसँग विभिन्न वातावरणहरूमा स्थापना गर्न सकिन्छ। 


मिस्टारल सानो राम्रो छ: 
- सारांश, भावना विश्लेषण र अनुवाद जस्ता पाठ आधारित कार्यहरूका लागि। 
- लागत प्रभावकारिताका कारण बारम्बार अनुरोध गरिने अनुप्रयोगहरूका लागि 
- समीक्षा र कोड सुझावहरू जस्ता कम विलम्बता कोड कार्यहरूका लागि 

## मिस्टारल सानो र मिस्टारल ठूलो तुलना 

मिस्टारल सानो र ठूलो बीच विलम्बता भिन्नता देखाउन तलको सेलहरू चलाउनुहोस्। 

तपाईंले ३-५ सेकेन्ड बीच विभिन्न प्रतिक्रिया समय देख्नुहुनेछ। साथै एउटै प्रॉम्प्टमा प्रतिक्रिया लम्बाइ र शैली पनि नोट गर्नुहोस्।  

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

## मिस्टारल NeMo

यस पाठ्यक्रममा छलफल गरिएको अन्य दुई मोडेलहरूको तुलनामा, मिस्टारल NeMo मात्र अपाचे २ लाइसेन्स सहितको निःशुल्क मोडेल हो। 

यसलाई पहिलेको खुला स्रोत LLM मिस्टारल ७B को उन्नयनको रूपमा हेरिन्छ। 

NeMo मोडेलका केही अन्य विशेषताहरू यस प्रकारका छन्: 

- *अधिक प्रभावकारी टोकनाइजेशन:* यस मोडेलले व्यापक रूपमा प्रयोग हुने tiktoken भन्दा Tekken टोकनाइजर प्रयोग गर्दछ। यसले बढी भाषाहरू र कोडमा राम्रो प्रदर्शन सुनिश्चित गर्दछ। 

- *फाइनट्युनिङ:* आधारभूत मोडेल फाइनट्युनिङका लागि उपलब्ध छ। यसले फाइनट्युनिङ आवश्यक पर्ने प्रयोगहरूमा बढी लचिलोपन दिन्छ। 

- *देशी फंक्शन कलिंग* - मिस्टारल ठूलोझैं, यस मोडेललाई पनि फंक्शन कलिंगमा प्रशिक्षित गरिएको छ। यसले यसलाई पहिलो खुला स्रोत मोडेलहरू मध्ये एक बनाउँछ जुन यस्तो गर्छ। 


### टोकनाइजरहरू तुलना गर्दै 

यस नमूनामा, हामी हेरौं कि मिस्टारल NeMo कसरी टोकनाइजेशन गर्छ मिस्टारल ठूलोको तुलनामा। 

दुबै नमूनाले एउटै प्रॉम्प्ट लिन्छन् तर तपाईंले देख्नुहुनेछ कि NeMo मिस्टारल ठूलो भन्दा कम टोकन फर्काउँछ। 

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

# सन्देशहरूको सूची टोकनाइज गर्नुहोस्
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

# टोकनहरूको संख्या गन्नुहोस्
print(len(tokens))
```

## सिकाइ यहाँ समाप्त हुँदैन, यात्रालाई जारी राख्नुहोस्

यस पाठ्यक्रम पूरा गरेपछि, हाम्रो [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) मा हेरि आफ्नो Generative AI ज्ञानमा थप उन्नति गर्नुहोस्!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**प्रत्याख्यान**:
यो दस्तावेज [Co-op Translator](https://github.com/Azure/co-op-translator) नामक एआई अनुवाद सेवा प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्नेछ। मूल दस्तावेज यसको मौलिक भाषामा प्रमाणिक स्रोत मानिनेछ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमि वा गलत व्याख्याको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->