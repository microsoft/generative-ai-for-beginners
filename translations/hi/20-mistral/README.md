# Mistral मॉडल के साथ निर्माण

## परिचय

यह पाठ कवर करेगा:
- विभिन्न Mistral मॉडलों का अन्वेषण
- प्रत्येक मॉडल के उपयोग-मामलों और परिदृश्यों को समझना
- प्रत्येक मॉडल की अद्वितीय विशेषताओं को दिखाने वाले कोड नमूनों का अन्वेषण

## Mistral मॉडल

इस पाठ में, हम 3 अलग-अलग Mistral मॉडल्स का अन्वेषण करेंगे:
**Mistral Large**, **Mistral Small** और **Mistral Nemo**।

इनमें से प्रत्येक मॉडल GitHub मॉडल मार्केटप्लेस पर मुफ्त उपलब्ध है। इस नोटबुक में कोड को चलाने के लिए ये मॉडल उपयोग किए जाएंगे। GitHub मॉडलों का उपयोग कर [AI मॉडलों के साथ प्रोटोटाइप बनाने](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) के बारे में अधिक जानकारी यहां है।

## Mistral Large 2 (2407)
Mistral Large 2 वर्तमान में Mistral का प्रमुख मॉडल है और इसे एंटरप्राइज उपयोग के लिए डिज़ाइन किया गया है।

यह मॉडल मूल Mistral Large का अपग्रेड है जो प्रदान करता है
- बड़ा कॉन्टेक्स्ट विंडो - 128k बनाम 32k
- गणित और कोडिंग कार्यों पर बेहतर प्रदर्शन - 76.9% औसत सटीकता बनाम 60.4%
- बहुभाषी प्रदर्शन में वृद्धि - भाषाओं में शामिल हैं: अंग्रेज़ी, फ्रेंच, जर्मन, स्पैनिश, इतालवी, पुर्तगाली, डच, रूसी, चीनी, जापानी, कोरियाई, अरबी, और हिंदी।

इन विशेषताओं के साथ, Mistral Large उत्कृष्ट है
- *रिट्रीवल ऑगमेंटेड जनरेशन (RAG)* - बड़े कॉन्टेक्स्ट विंडो के कारण
- *फ़ंक्शन कॉलिंग* - इस मॉडल में नेटिव फ़ंक्शन कॉलिंग है जो बाहरी टूल्स और APIs के साथ एकीकरण की अनुमति देता है। ये कॉल एक साथ या एक-के-बाद-एक क्रम में किए जा सकते हैं।
- *कोड जनरेशन* - यह मॉडल Python, Java, TypeScript और C++ जनरेशन में उत्कृष्ट है।

### Mistral Large 2 का उपयोग करते हुए RAG उदाहरण

इस उदाहरण में, हम Mistral Large 2 का उपयोग एक टेक्स्ट दस्तावेज़ पर RAG पैटर्न चलाने के लिए कर रहे हैं। प्रश्न कोरियाई में लिखा गया है और लेखक की कॉलेज से पहले की गतिविधियों के बारे में पूछता है।

यह Cohere Embeddings मॉडल का उपयोग करता है दस्तावेज़ और प्रश्न के एम्बेडिंग बनाने के लिए। इस नमूने में, faiss Python पैकेज को वेक्टर स्टोर के रूप में उपयोग किया गया है।

Mistral मॉडल को भेजा गया प्रॉम्प्ट प्रश्न और उन पुनः प्राप्त चंक्स दोनों को शामिल करता है जो प्रश्न से समान हैं। मॉडल फिर एक प्राकृतिक भाषा प्रतिक्रिया प्रदान करता है।

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
Mistral Small Mistral परिवार का एक और मॉडल है जो प्रीमियर/एंटरप्राइज श्रेणी के अंतर्गत आता है। जैसा कि नाम से पता चलता है, यह एक छोटा भाषा मॉडल (SLM) है। Mistral Small के उपयोग के लाभ हैं:
- Mistral LLMs जैसे Mistral Large और NeMo की तुलना में लागत में कमी - 80% मूल्य गिरावट
- कम विलंबता - Mistral के LLMs की तुलना में तेज़ प्रतिक्रिया
- लचीलापन - आवश्यक संसाधनों पर कम प्रतिबंधों के साथ विभिन्न पर्यावरणों में तैनात किया जा सकता है।

Mistral Small के लिए उपयुक्त है:
- सारांश, भावना विश्लेषण और अनुवाद जैसे पाठ आधारित कार्य
- ऐसे अनुप्रयोग जहां बार-बार अनुरोध होते हैं क्योंकि यह लागत प्रभावी है
- समीक्षा और कोड सुझाव जैसे कम विलंबता वाले कोड कार्य

## Mistral Small और Mistral Large की तुलना

Mistral Small और Large के बीच विलंबता में अंतर दिखाने के लिए नीचे दिए गए सेल चलाएं।

आपको प्रतिक्रिया समय में 3-5 सेकंड का अंतर दिखाई देगा। साथ ही एक ही प्रॉम्प्ट पर प्रतिक्रिया की लंबाई और शैली पर ध्यान दें।

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

इस पाठ में चर्चा किए गए दो अन्य मॉडलों की तुलना में, Mistral NeMo एकमात्र मुफ्त मॉडल है जिसके साथ Apache2 लाइसेंस है।

इसे Mistral के पहले के ओपन सोर्स LLM, Mistral 7B का अपग्रेड माना जाता है।

NeMo मॉडल के कुछ अन्य फीचर्स हैं:

- *अधिक कुशल टोकनाइजेशन:* यह मॉडल ज्यादा सामान्य रूप से उपयोग किए जाने वाले tiktoken के बजाय Tekken टोकनाइज़र का उपयोग करता है। इससे अधिक भाषाओं और कोड पर बेहतर प्रदर्शन मिलती है।

- *फाइनट्यूनिंग:* बेस मॉडल फाइनट्यूनिंग के लिए उपलब्ध है। यह उन उपयोग-मामलों के लिए अधिक लचीलापन प्रदान करता है जहां फाइनट्यूनिंग आवश्यक हो सकती है।

- *नेटिव फ़ंक्शन कॉलिंग* - Mistral Large की तरह, इस मॉडल को फ़ंक्शन कॉलिंग के लिए प्रशिक्षित किया गया है। यह इसे पहले के खुले स्रोत मॉडलों में से एक बनाता है जो ऐसा करते हैं।

### टोकनाइज़र की तुलना

इस नमूने में, हम देखेंगे कि Mistral NeMo टोकनाइजेशन को Mistral Large की तुलना में कैसे संभालता है।

दोनों नमूने एक ही प्रॉम्प्ट लेते हैं लेकिन आपको देखना चाहिए कि NeMo Mistral Large की तुलना में कम टोकन लौटाता है।

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

# मिस्टрал टोकनाइज़र लोड करें

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

## सीखना यहीं खत्म नहीं होता, अपनी यात्रा जारी रखें

इस पाठ को पूरा करने के बाद, हमारे [Generative AI Learning संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) को देखें ताकि आप अपनी जनरेटिव AI ज्ञान को और विस्तार दे सकें!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान रखें कि स्वचालित अनुवादों में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->