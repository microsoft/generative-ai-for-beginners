# Mistral मॉडल के साथ निर्माण  

## परिचय  

इस पाठ में हम कवर करेंगे:  
- विभिन्न Mistral मॉडलों का अन्वेषण  
- प्रत्येक मॉडल के उपयोग-मामलों और परिदृश्यों की समझ  
- प्रत्येक मॉडल की अनोखी विशेषताओं को दर्शाने वाले कोड उदाहरणों का अन्वेषण।  

## Mistral मॉडल  

इस पाठ में, हम 3 अलग-अलग Mistral मॉडलों का अन्वेषण करेंगे:  
**Mistral Large**, **Mistral Small** और **Mistral Nemo**।  

ये प्रत्येक मॉडल [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) पर मुफ्त उपलब्ध हैं। इस नोटबुक में कोड चलाने के लिए ये मॉडल उपयोग किए जा रहे हैं।  

> **नोट:** GitHub Models जुलाई 2026 के अंत में बंद हो रहा है। AI मॉडल्स के साथ प्रोटोटाइप बनाने के लिए [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) के उपयोग पर अधिक जानकारी यहाँ देखें।  


## Mistral Large 2 (2407)  
Mistral Large 2 वर्तमान में Mistral का प्रमुख मॉडल है और इसे एंटरप्राइज उपयोग के लिए डिज़ाइन किया गया है।  

यह मॉडल मूल Mistral Large का उन्नयन है जो निम्नलिखित विशेषताएं प्रदान करता है:  
-  बड़ा कॉन्टेक्स्ट विंडो - 128k बनाम 32k  
-  गणित और कोडिंग कार्यों में बेहतर प्रदर्शन - 76.9% औसत सटीकता बनाम 60.4%  
-  बहुभाषी प्रदर्शन में वृद्धि - भाषाओं में शामिल हैं: अंग्रेज़ी, फ्रेंच, जर्मन, स्पेनिश, इतालवी, पुर्तगाली, डच, रूसी, चीनी, जापानी, कोरियाई, अरबी, और हिंदी।  

इन विशेषताओं के साथ, Mistral Large निम्नलिखित में उत्कृष्ट है:  
- *रीट्रीवल ऑगमेंटेड जनरेशन (RAG)* - बड़े संदर्भ विंडो के कारण  
- *फंक्शन कॉलिंग* - इस मॉडल में मूल फंक्शन कॉलिंग है जो बाहरी टूल्स और API के साथ इंटीग्रेशन की अनुमति देता है। ये कॉल समानांतर या अनुक्रमिक क्रम में की जा सकती हैं।  
- *कोड जनरेशन* - यह मॉडल पायथन, जावा, टाइपस्क्रिप्ट और C++ जनरेशन में उत्कृष्ट है।  

### Mistral Large 2 का उपयोग करके RAG उदाहरण  

इस उदाहरण में, हम Mistral Large 2 का उपयोग एक टेक्स्ट दस्तावेज़ पर RAG पैटर्न चलाने के लिए कर रहे हैं। प्रश्न कोरियाई में लिखा गया है और लेखक की कॉलेज से पहले की गतिविधियों के बारे में पूछता है।  

यह टेक्स्ट दस्तावेज़ और प्रश्न दोनों के एम्बेडिंग बनाने के लिए Cohere Embeddings मॉडल का उपयोग करता है। इस नमूने के लिए यह faiss पायथन पैकेज को वेक्टर स्टोर के रूप में उपयोग करता है।  

Mistral मॉडल को भेजे गए प्रॉम्प्ट में प्रश्न और उन्हीं प्रश्न के समान पुनः प्राप्त किए गए खंड दोनों शामिल होते हैं। मॉडल फिर प्राकृतिक भाषा में प्रतिक्रिया प्रदान करता है।  

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

# इन्हें अपने Microsoft Foundry प्रोजेक्ट के "अवलोकन" पृष्ठ से प्राप्त करें
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # दूरी, सूचकांक
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
Mistral Small Mistral परिवार का एक और मॉडल है जो प्रीमियर/एंटरप्राइज श्रेणी में आता है। जैसा कि नाम से पता चलता है, यह एक छोटा भाषा मॉडल (SLM) है। Mistral Small के उपयोग के लाभ हैं:  
- Mistral के LLMs जैसे Mistral Large और NeMo की तुलना में लागत बचत - 80% कीमत में कमी  
- कम लेटेंसी - Mistral के LLMs की तुलना में तेज़ प्रतिक्रिया  
- लचीला - आवश्यक संसाधनों पर कम प्रतिबंधों के साथ विभिन्न पर्यावरणों में तैनात किया जा सकता है।  


Mistral Small के लिए उपयुक्त हैं:  
- पाठ आधारित कार्य जैसे सारांश, भावना विश्लेषण और अनुवाद।  
- ऐसे अनुप्रयोग जहां लागत प्रभावशीलता के कारण अक्सर अनुरोध किए जाते हैं  
- समीक्षा और कोड सुझाव जैसे कम लेटेंसी वाले कोड कार्य  

## Mistral Small और Mistral Large की तुलना  

Mistral Small और Large के बीच लेटेंसी के अंतर को दिखाने के लिए, नीचे दिए गए सेल चलाएं।  

आपको 3-5 सेकंड के बीच प्रतिक्रिया समय में अंतर दिखाई देना चाहिए। समान प्रॉम्प्ट पर प्रतिक्रिया की लंबाई और शैली पर भी ध्यान दें।  

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

इस पाठ में चर्चा किए गए अन्य दो मॉडलों की तुलना में, Mistral NeMo एकमात्र मुफ्त मॉडल है जिसके पास Apache2 लाइसेंस है।  

इसे Mistral के पहले मुक्त स्रोत LLM, Mistral 7B, का उन्नयन माना जाता है।  

NeMo मॉडल की कुछ अन्य विशेषताएं हैं:  

- *अधिक कुशल टोकनाइजेशन:* यह मॉडल अधिक सामान्य Tiktoken के बजाय Tekken टोकनाइज़र का उपयोग करता है। यह अधिक भाषाओं और कोड पर बेहतर प्रदर्शन की अनुमति देता है।  

- *फाइनट्यूनिंग:* आधार मॉडल फाइनट्यूनिंग के लिए उपलब्ध है। यह उन उपयोग-मामलों के लिए अधिक लचीलापन प्रदान करता है जहां फाइनट्यूनिंग की आवश्यकता हो सकती है।  

- *मूल फंक्शन कॉलिंग* - Mistral Large की तरह, इस मॉडल को भी फंक्शन कॉलिंग पर प्रशिक्षित किया गया है। यह इसे पहले मुक्त स्रोत मॉडलों में से एक बनाता है जो ऐसा करता है।  


### टोकनाइज़र की तुलना  

इस उदाहरण में, हम देखेंगे कि Mistral NeMo टोकनाइजेशन को Mistral Large की तुलना में कैसे संभालता है।  

दोनों नमूने एक समान प्रॉम्प्ट लेते हैं, लेकिन आप देखेंगे कि NeMo Mistral Large की तुलना में कम टोकन लौटाता है।  

```bash
pip install mistral-common
```

```python 
# आवश्यक पैकेज आयात करें:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# मिस्त्रल टोकनाइज़र लोड करें

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# संदेशों की एक सूची को टोकनाइज़ करें
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

# टोकन की संख्या गिनें
print(len(tokens))
```

```python
# आवश्यक पैकेज आयात करें:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# मिस्ट्रल टोकनाइज़र लोड करें

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# संदेशों की सूची को टोकनाइज़ करें
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

# टोकन की संख्या गिनें
print(len(tokens))
```

## सीखना यहीं खत्म नहीं होता, यात्रा जारी रखें  

इस पाठ को पूरा करने के बाद, हमारे [जनरेटिव AI सीखने के संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) को देखें ताकि आप अपनी जनरेटिव AI ज्ञान को और आगे बढ़ा सकें!  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->