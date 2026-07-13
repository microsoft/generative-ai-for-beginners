# Mistral मॉडल के साथ निर्माण 

## परिचय 

इस पाठ में शामिल होगा: 
- विभिन्न Mistral मॉडलों का अन्वेषण 
- प्रत्येक मॉडल के उपयोग-मामले और परिदृश्यों को समझना 
- प्रत्येक मॉडल की अनूठी विशेषताओं को दिखाने वाले कोड नमूनों का अन्वेषण। 

## Mistral मॉडल 

इस पाठ में, हम 3 विभिन्न Mistral मॉडलों का अन्वेषण करेंगे: 
**Mistral Large**, **Mistral Small** और **Mistral Nemo**। 

ये सभी मॉडल [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) पर निशुल्क उपलब्ध हैं। इस नोटबुक में कोड चलाने के लिए ये मॉडल उपयोग किए जाएंगे।

> **नोट:** GitHub Models जुलाई 2026 के अंत तक बंद हो रहे हैं। AI मॉडलों के साथ प्रोटोटाइपिंग के लिए [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) का उपयोग करने के बारे में अधिक विवरण यहां हैं। 


## Mistral Large 2 (2407)
Mistral Large 2 वर्तमान में Mistral का प्रमुख मॉडल है और इसे उद्यम उपयोग के लिए डिज़ाइन किया गया है। 

यह मॉडल मूल Mistral Large का उन्नयन है, जो प्रदान करता है: 
-  बड़ा कंटेक्स्ट विंडो - 128k बनाम 32k 
-  गणित और कोडिंग कार्यों में बेहतर प्रदर्शन - 76.9% औसत सटीकता बनाम 60.4% 
-  बढ़ी हुई बहुभाषी प्रदर्शन - भाषाओं में शामिल हैं: अंग्रेज़ी, फ़्रेंच, जर्मन, स्पेनिश, इतालवी, पुर्तगाली, डच, रूसी, चीनी, जापानी, कोरियन, अरब, और हिंदी।

इन विशेषताओं के साथ, Mistral Large उत्कृष्ट है:
- *प्राप्ति उन्नत जेनेरेशन (RAG)* - बड़े कंटेक्स्ट विंडो के कारण
- *फंक्शन कॉलिंग* - इस मॉडल में मूल फंक्शन कॉलिंग है जो बाहरी टूल्स और APIs के साथ एकीकरण की अनुमति देता है। ये कॉल्स समानांतर में या एक क्रमिक क्रम में की जा सकती हैं। 
- *कोड जनरेशन* - यह मॉडल Python, Java, TypeScript और C++ जनरेशन में उत्कृष्ट है। 

### Mistral Large 2 का उपयोग कर RAG उदाहरण 

इस उदाहरण में, हम Mistral Large 2 का उपयोग एक टेक्स्ट दस्तावेज़ पर RAG पैटर्न चलाने के लिए कर रहे हैं। प्रश्न कोरियाई में लिखा गया है और लेखक की कॉलेज से पहले की गतिविधियों के बारे में पूछता है। 

यह Cohere Embeddings मॉडल का उपयोग करता है टेक्स्ट दस्तावेज़ और प्रश्न के एम्बेडिंग बनाने के लिए। इस नमूने के लिए, यह faiss Python पैकेज को वेक्टर स्टोर के रूप में उपयोग करता है। 

Mistral मॉडल को भेजा गया प्रॉम्प्ट दोनों प्रश्न और समान प्रश्न से संबंधित पुनः प्राप्त किए गए चंक्स को शामिल करता है। मॉडल फिर एक प्राकृतिक भाषा प्रतिक्रिया प्रदान करता है। 

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

# इन्हें अपने Microsoft Foundry परियोजना के "ओवरव्यू" पेज से प्राप्त करें
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
Mistral Small Mistral परिवार में एक अन्य मॉडल है जो प्रीमियर/एंटरप्राइज श्रेणी के अंतर्गत आता है। जैसा कि नाम से पता चलता है, यह एक छोटा भाषा मॉडल (SLM) है। Mistral Small के उपयोग के लाभ हैं: 
- Mistral LLMs जैसे Mistral Large और NeMo की तुलना में लागत में बचत - 80% की कीमत में गिरावट
- कम विलंबता - Mistral के LLMs की तुलना में तेज़ प्रतिक्रिया
- लचीला - इसे कम संसाधन आवश्यकताओं के साथ विभिन्न वातावरणों में तैनात किया जा सकता है। 


Mistral Small अच्छा है: 
- टेक्स्ट आधारित कार्य जैसे सारांशण, भावना विश्लेषण और अनुवाद। 
- उन अनुप्रयोगों के लिए जहाँ लागत प्रभावशीलता के कारण बार-बार अनुरोध किए जाते हैं 
- समीक्षा और कोड सुझाव जैसी कम विलंबता वाले कोड कार्यों के लिए 

## Mistral Small और Mistral Large की तुलना 

Mistral Small और Large के बीच विलंबता में अंतर दिखाने के लिए, नीचे के सेल चलाएं। 

आपको 3-5 सेकंड के बीच प्रतिक्रिया समय में अंतर दिखाई देगा। साथ ही समान प्रॉम्प्ट पर प्रतिक्रिया की लंबाई और शैली पर ध्यान दें।  

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

इस पाठ में चर्चा किए गए अन्य दो मॉडलों की तुलना में, Mistral NeMo एकमात्र मुफ्त मॉडल है जिसमें Apache2 लाइसेंस है। 

इसे Mistral के पहले के ओपन-सोर्स LLM, Mistral 7B के उन्नयन के रूप में देखा जाता है। 

NeMo मॉडल की कुछ अन्य विशेषताएं हैं: 

- *अधिक कुशल टोकनाईज़ेशन:* यह मॉडल tiktoken की बजाय Tekken टोकनाइज़र का उपयोग करता है। इससे अधिक भाषाओं और कोड पर बेहतर प्रदर्शन होता है। 

- *फाइनट्यूनिंग:* बेस मॉडल फाइनट्यूनिंग के लिए उपलब्ध है। इससे उन उपयोग-मामलों के लिए अधिक लचीलेपन की अनुमति मिलती है जहाँ फाइनट्यूनिंग की आवश्यकता हो सकती है। 

- *मूल फंक्शन कॉलिंग* - Mistral Large की तरह, इस मॉडल को भी फंक्शन कॉलिंग पर प्रशिक्षित किया गया है। इसे पहले ओपन-सोर्स मॉडलों में से एक के रूप में अनूठा बनाता है। 


### टोकनाइज़र की तुलना 

इस नमूने में, हम देखेंगें कि Mistral NeMo टोकनाईज़ेशन को Mistral Large की तुलना में कैसे हैंडल करता है। 

दोनों नमूने एक ही प्रॉम्प्ट लेते हैं लेकिन आप देखेंगे कि NeMo Mistral Large की तुलना में कम टोकन लौटाता है। 

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

# Mistral टोकनाइज़र लोड करें

model_name = "open-mistral-nemo"

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

# टोकनों की संख्या गिनें
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

# Mistral टोकनाइज़र लोड करें

model_name = "mistral-large-latest"

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

## सीखना यहीं खत्म नहीं होता, यात्रा जारी रखें

इस पाठ को पूरा करने के बाद, हमारे [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) को देखें ताकि आप अपना जनरेटिव AI ज्ञान बढ़ाते रहें!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->