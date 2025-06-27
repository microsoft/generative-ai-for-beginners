<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:14:01+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "hi"
}
-->
# मिस्त्रल मॉडल्स के साथ निर्माण

## परिचय

इस पाठ में शामिल होंगे:
- विभिन्न मिस्त्रल मॉडल्स का अन्वेषण
- प्रत्येक मॉडल के उपयोग के मामले और परिदृश्य को समझना
- कोड नमूने जो प्रत्येक मॉडल की अनोखी विशेषताएं दिखाते हैं।

## मिस्त्रल मॉडल्स

इस पाठ में, हम 3 अलग-अलग मिस्त्रल मॉडल्स का अन्वेषण करेंगे: **मिस्त्रल लार्ज**, **मिस्त्रल स्मॉल** और **मिस्त्रल नीमो**।

इनमें से प्रत्येक मॉडल Github Model मार्केटप्लेस पर मुफ्त में उपलब्ध है। इस नोटबुक में कोड इन मॉडल्स का उपयोग करके कोड चलाने के लिए होगा। Github Models का उपयोग करके [AI मॉडल्स के साथ प्रोटोटाइप बनाना](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) के बारे में अधिक विवरण यहां दिए गए हैं।

## मिस्त्रल लार्ज 2 (2407)
मिस्त्रल लार्ज 2 वर्तमान में मिस्त्रल का प्रमुख मॉडल है और इसे उद्यम उपयोग के लिए डिज़ाइन किया गया है।

मॉडल मूल मिस्त्रल लार्ज का अपग्रेड है, जिसमें निम्नलिखित विशेषताएं हैं:
- बड़ा संदर्भ विंडो - 128k बनाम 32k
- गणित और कोडिंग कार्यों पर बेहतर प्रदर्शन - 76.9% औसत सटीकता बनाम 60.4%
- बहुभाषी प्रदर्शन में वृद्धि - भाषाओं में शामिल हैं: अंग्रेजी, फ्रेंच, जर्मन, स्पेनिश, इटालियन, पुर्तगाली, डच, रूसी, चीनी, जापानी, कोरियाई, अरबी, और हिंदी।

इन विशेषताओं के साथ, मिस्त्रल लार्ज उत्कृष्ट है:
- *रिट्रीवल ऑगमेंटेड जनरेशन (RAG)* - बड़े संदर्भ विंडो के कारण
- *फंक्शन कॉलिंग* - इस मॉडल में नेटिव फंक्शन कॉलिंग है जो बाहरी उपकरणों और API के साथ एकीकरण की अनुमति देता है। ये कॉल्स समानांतर में या एक के बाद एक क्रमिक क्रम में किए जा सकते हैं।
- *कोड जनरेशन* - यह मॉडल पायथन, जावा, टाइपस्क्रिप्ट और C++ जनरेशन पर उत्कृष्ट है।

### मिस्त्रल लार्ज 2 का उपयोग करके RAG उदाहरण

इस उदाहरण में, हम मिस्त्रल लार्ज 2 का उपयोग एक टेक्स्ट डॉक्यूमेंट पर RAG पैटर्न चलाने के लिए कर रहे हैं। सवाल कोरियाई में लिखा गया है और लेखक की कॉलेज से पहले की गतिविधियों के बारे में पूछता है।

यह कोहेरे एम्बेडिंग्स मॉडल का उपयोग टेक्स्ट डॉक्यूमेंट और सवाल के एम्बेडिंग्स बनाने के लिए करता है। इस नमूने के लिए, यह faiss पायथन पैकेज का उपयोग एक वेक्टर स्टोर के रूप में करता है।

मिस्त्रल मॉडल को भेजा गया प्रॉम्प्ट सवालों और प्राप्त किए गए चंक्स को शामिल करता है जो सवाल के समान हैं। मॉडल फिर एक प्राकृतिक भाषा प्रतिक्रिया प्रदान करता है।

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
मिस्त्रल स्मॉल मिस्त्रल मॉडल्स के परिवार में एक और मॉडल है जो प्रीमियर/उद्यम श्रेणी के अंतर्गत आता है। जैसा कि नाम से पता चलता है, यह मॉडल एक छोटा भाषा मॉडल (SLM) है। मिस्त्रल स्मॉल का उपयोग करने के लाभ हैं:
- मिस्त्रल LLMs जैसे मिस्त्रल लार्ज और नीमो की तुलना में लागत बचत - 80% मूल्य में कमी
- कम विलंबता - मिस्त्रल के LLMs की तुलना में तेज़ प्रतिक्रिया
- लचीला - विभिन्न परिवेशों में कम आवश्यक संसाधनों के साथ तैनात किया जा सकता है।

मिस्त्रल स्मॉल के लिए उत्कृष्ट है:
- टेक्स्ट आधारित कार्य जैसे संक्षेपण, भावना विश्लेषण और अनुवाद।
- अनुप्रयोग जहां लागत प्रभावशीलता के कारण बार-बार अनुरोध किए जाते हैं
- कम विलंबता कोड कार्य जैसे समीक्षा और कोड सुझाव

## मिस्त्रल स्मॉल और मिस्त्रल लार्ज की तुलना

मिस्त्रल स्मॉल और लार्ज के बीच विलंबता में अंतर दिखाने के लिए, नीचे दिए गए सेल्स को चलाएं।

आपको 3-5 सेकंड के बीच प्रतिक्रिया समय में अंतर दिखाई देना चाहिए। साथ ही, समान प्रॉम्प्ट पर प्रतिक्रिया लंबाई और शैली पर ध्यान दें।

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

इस पाठ में चर्चा किए गए अन्य दो मॉडल्स की तुलना में, मिस्त्रल नीमो एकमात्र मुफ्त मॉडल है जिसमें Apache2 लाइसेंस है।

इसे मिस्त्रल के पहले ओपन सोर्स LLM, मिस्त्रल 7B का अपग्रेड माना जाता है।

नीमो मॉडल की कुछ अन्य विशेषताएं हैं:

- *अधिक कुशल टोकनाइजेशन:* यह मॉडल अधिक सामान्य रूप से उपयोग किए जाने वाले tiktoken के बजाय Tekken टोकनाइज़र का उपयोग करता है। यह अधिक भाषाओं और कोड पर बेहतर प्रदर्शन की अनुमति देता है।

- *फाइनट्यूनिंग:* बेस मॉडल फाइनट्यूनिंग के लिए उपलब्ध है। यह उन उपयोग मामलों के लिए अधिक लचीलापन की अनुमति देता है जहां फाइनट्यूनिंग की आवश्यकता हो सकती है।

- *नेटिव फंक्शन कॉलिंग* - मिस्त्रल लार्ज की तरह, इस मॉडल को फंक्शन कॉलिंग पर प्रशिक्षित किया गया है। इसे ऐसा करने वाला पहला ओपन सोर्स मॉडल होने के नाते इसे अनोखा बनाता है।

### टोकनाइज़र्स की तुलना

इस नमूने में, हम देखेंगे कि मिस्त्रल नीमो टोकनाइज़ेशन को मिस्त्रल लार्ज की तुलना में कैसे संभालता है।

दोनों नमूने समान प्रॉम्प्ट लेते हैं, लेकिन आपको देखना चाहिए कि नीमो मिस्त्रल लार्ज की तुलना में कम टोकन वापस करता है।

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

इस पाठ को पूरा करने के बाद, हमारे [जनरेटिव AI लर्निंग संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) को देखें ताकि आप अपनी जनरेटिव AI ज्ञान को बढ़ा सकें!

**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।