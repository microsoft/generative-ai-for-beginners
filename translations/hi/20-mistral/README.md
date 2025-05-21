<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:53:47+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "hi"
}
-->
# मिस्त्रल मॉडल्स के साथ निर्माण

## परिचय

यह पाठ शामिल करेगा:
- विभिन्न मिस्त्रल मॉडल्स की खोज
- प्रत्येक मॉडल के उपयोग के मामले और परिदृश्यों को समझना
- कोड नमूने जो प्रत्येक मॉडल की अनूठी विशेषताएं दिखाते हैं।

## मिस्त्रल मॉडल्स

इस पाठ में, हम 3 विभिन्न मिस्त्रल मॉडल्स की खोज करेंगे: **मिस्त्रल लार्ज**, **मिस्त्रल स्मॉल** और **मिस्त्रल नीमो**।

इनमें से प्रत्येक मॉडल गिटहब मॉडल मार्केटप्लेस पर मुफ्त में उपलब्ध है। इस नोटबुक में कोड चलाने के लिए इन मॉडलों का उपयोग किया जाएगा। गिटहब मॉडल्स का उपयोग करके [एआई मॉडल्स के साथ प्रोटोटाइप बनाना](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) के बारे में अधिक जानकारी यहाँ है।

## मिस्त्रल लार्ज 2 (2407)
मिस्त्रल लार्ज 2 वर्तमान में मिस्त्रल का प्रमुख मॉडल है और इसे उद्यम उपयोग के लिए डिज़ाइन किया गया है।

यह मॉडल मूल मिस्त्रल लार्ज का एक उन्नयन है जो प्रदान करता है:
- बड़ा संदर्भ विंडो - 128k बनाम 32k
- गणित और कोडिंग कार्यों पर बेहतर प्रदर्शन - 76.9% औसत सटीकता बनाम 60.4%
- बहुभाषी प्रदर्शन में वृद्धि - भाषाओं में शामिल हैं: अंग्रेजी, फ्रेंच, जर्मन, स्पेनिश, इतालवी, पुर्तगाली, डच, रूसी, चीनी, जापानी, कोरियाई, अरबी, और हिंदी।

इन विशेषताओं के साथ, मिस्त्रल लार्ज उत्कृष्ट है:
- *रिट्रीवल ऑगमेंटेड जेनरेशन (RAG)* - बड़े संदर्भ विंडो के कारण
- *फंक्शन कॉलिंग* - इस मॉडल में नेटिव फंक्शन कॉलिंग है जो बाहरी उपकरणों और एपीआई के साथ एकीकरण की अनुमति देता है। ये कॉल समानांतर या एक के बाद एक क्रम में की जा सकती हैं।
- *कोड जेनरेशन* - यह मॉडल पायथन, जावा, टाइपस्क्रिप्ट और सी++ जेनरेशन में उत्कृष्ट है।

### मिस्त्रल लार्ज 2 का उपयोग करके RAG उदाहरण

इस उदाहरण में, हम मिस्त्रल लार्ज 2 का उपयोग एक पाठ दस्तावेज़ पर RAG पैटर्न चलाने के लिए कर रहे हैं। प्रश्न कोरियाई में लिखा गया है और लेखक की कॉलेज से पहले की गतिविधियों के बारे में पूछता है।

यह कोहेयर एम्बेडिंग्स मॉडल का उपयोग पाठ दस्तावेज़ और प्रश्न के एम्बेडिंग बनाने के लिए करता है। इस नमूने के लिए, यह faiss पायथन पैकेज का उपयोग एक वेक्टर स्टोर के रूप में करता है।

मिस्त्रल मॉडल को भेजा गया प्रॉम्प्ट प्रश्नों और प्रश्न के समान पुनः प्राप्त अंशों को शामिल करता है। फिर मॉडल एक प्राकृतिक भाषा प्रतिक्रिया प्रदान करता है।

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
मिस्त्रल स्मॉल मिस्त्रल मॉडल्स के परिवार में एक और मॉडल है जो प्रीमियर/उद्यम श्रेणी के अंतर्गत आता है। जैसा कि नाम से पता चलता है, यह मॉडल एक स्मॉल लैंग्वेज मॉडल (SLM) है। मिस्त्रल स्मॉल का उपयोग करने के लाभ हैं कि यह:
- मिस्त्रल LLMs जैसे मिस्त्रल लार्ज और नीमो की तुलना में लागत की बचत करता है - 80% मूल्य में कमी
- कम विलंबता - मिस्त्रल के LLMs की तुलना में तेज़ प्रतिक्रिया
- लचीला - इसे विभिन्न वातावरणों में कम संसाधनों की आवश्यकता के साथ तैनात किया जा सकता है।

मिस्त्रल स्मॉल के लिए उपयुक्त है:
- पाठ आधारित कार्य जैसे संक्षेपण, भावना विश्लेषण और अनुवाद।
- अनुप्रयोग जहां इसकी लागत प्रभावशीलता के कारण बार-बार अनुरोध किए जाते हैं
- कम विलंबता कोड कार्य जैसे समीक्षा और कोड सुझाव

## मिस्त्रल स्मॉल और मिस्त्रल लार्ज की तुलना

मिस्त्रल स्मॉल और लार्ज के बीच विलंबता में अंतर दिखाने के लिए, नीचे दिए गए कोशिकाओं को चलाएं।

आपको 3-5 सेकंड के बीच प्रतिक्रिया समय में अंतर दिखाई देना चाहिए। साथ ही, एक ही प्रॉम्प्ट पर प्रतिक्रिया की लंबाई और शैली को नोट करें।

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

## मिस्त्रल नीमो

इस पाठ में चर्चा किए गए अन्य दो मॉडलों की तुलना में, मिस्त्रल नीमो एकमात्र मुफ्त मॉडल है जिसमें अपाचे2 लाइसेंस है।

इसे मिस्त्रल के पहले के ओपन सोर्स LLM, मिस्त्रल 7B का उन्नयन माना जाता है।

नीमो मॉडल की कुछ अन्य विशेषताएं हैं:

- *अधिक कुशल टोकनाइजेशन:* यह मॉडल अधिक सामान्यतः उपयोग किए जाने वाले tiktoken के बजाय टेक्केन टोकनाइज़र का उपयोग करता है। यह अधिक भाषाओं और कोड पर बेहतर प्रदर्शन की अनुमति देता है।

- *फाइनट्यूनिंग:* बेस मॉडल फाइनट्यूनिंग के लिए उपलब्ध है। यह उन उपयोग के मामलों के लिए अधिक लचीलापन प्रदान करता है जहां फाइनट्यूनिंग की आवश्यकता हो सकती है।

- *नेटिव फंक्शन कॉलिंग* - मिस्त्रल लार्ज की तरह, इस मॉडल को फंक्शन कॉलिंग पर प्रशिक्षित किया गया है। यह इसे ऐसा करने वाले पहले ओपन सोर्स मॉडल्स में से एक के रूप में अद्वितीय बनाता है।

### टोकनाइज़र की तुलना

इस नमूने में, हम देखेंगे कि मिस्त्रल नीमो टोकनाइजेशन को मिस्त्रल लार्ज की तुलना में कैसे संभालता है।

दोनों नमूने एक ही प्रॉम्प्ट लेते हैं, लेकिन आपको देखना चाहिए कि नीमो मिस्त्रल लार्ज की तुलना में कम टोकन वापस करता है।

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

## सीखना यहीं नहीं रुकता, यात्रा जारी रखें

इस पाठ को पूरा करने के बाद, हमारे [जनरेटिव एआई लर्निंग संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) को देखें ताकि आप अपनी जनरेटिव एआई ज्ञान को बढ़ा सकें!

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। इसकी मूल भाषा में मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।