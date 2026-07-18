# मिस्ट्रल मॉडेलसह बांधकाम 

## परिचय 

हा धडा खालील गोष्टी कव्हर करेल: 
- विविध मिस्ट्रल मॉडेल्सचा शोध 
- प्रत्येक मॉडेलसाठी वापर-केस आणि परिस्थिती समजून घेणे 
- प्रत्येक मॉडेलच्या विशेष वैशिष्ट्यांचे कोड नमुने पाहणे. 

## मिस्ट्रल मॉडेल्स 

या धड्यात आपण 3 वेगवेगळ्या मिस्ट्रल मॉडेल्सचा शोध घेणार आहोत: 
**मिस्ट्रल लार्ज**, **मिस्ट्रल स्मॉल** आणि **मिस्ट्रल नेमो**. 

या मॉडेल्समधील प्रत्येक [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) वर मोफत उपलब्ध आहे. या नोटबुकमधील कोडहे मॉडेल वापरून चालवले जाईल.

> **टीप:** GitHub Models जुलै 2026 च्या शेवटी बंद होणार आहे. AI मॉडेल्ससह प्रोटोटायपिंगसाठी [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) वापरण्याविषयी अधिक माहिती येथे आहे. 


## मिस्ट्रल लार्ज 2 (2407)
मिस्ट्रल लार्ज 2 सध्या मिस्ट्रलचा प्रमुख मॉडेल आहे आणि एंटरप्राइझ वापरासाठी डिझाईन केलेला आहे. 

हा मॉडेल मूळ मिस्ट्रल लार्जपेक्षा सुधारित आहे 
-  मोठा संदर्भ विंडो - 128k विरुद्ध 32k 
-  गणित आणि कोडिंग कामे यामध्ये चांगला कार्यप्रदर्शन - सरासरी अचूकता 76.9% विरुद्ध 60.4% 
-  वाढलेला बहुभाषिक कार्यप्रदर्शन - भाषांमध्ये समाविष्ट: इंग्रजी, फ्रेंच, जर्मन, स्पॅनिश, इटालियन, पोर्तुगीज, डच, रशियन, चिनी, जपानी, कोरियन, अरब आणि हिंदी.

या वैशिष्ट्यांमुळे, मिस्ट्रल लार्ज मध्ये उत्कृष्ट कार्यक्षमता आहे 
- *रिट्रीव्हल ऑगमेंटेड जनरेशन (RAG)* - मोठ्या संदर्भ विंडोमुळे
- *फंक्शन कॉलिंग* - या मॉडेलमध्ये नैसर्गिक फंक्शन कॉलिंग आहे जे बाह्य साधने आणि API सह एकत्रीकरणाची परवानगी देते. हे कॉल्स समांतर किंवा अनुक्रमे एका नंतर एक करता येतात. 
- *कोड जनरेशन* - या मॉडेलमध्ये Python, Java, TypeScript आणि C++ जनरेशनमध्ये उत्कृष्ट आहे. 

### मिस्ट्रल लार्ज 2 वापरून RAG उदाहरण 

या उदाहरणामध्ये, आपण मिस्ट्रल लार्ज 2 वापरून टेक्स्ट दस्तऐवजावर RAG पॅटर्न चालवत आहोत. प्रश्न कोरियन भाषेत लिहिला आहे आणि लेखकाचे महाविद्यालयापूर्वीचे उपक्रम विचारतो. 

यासाठी Cohere Embeddings Model वापरून टेक्स्ट दस्तऐवज आणि प्रश्न यांचे एम्बेडिंग तयार केले जाते. या नमुन्यासाठी, faiss Python पॅकेज वापरले जाते वेक्टर स्टोर म्हणून. 

मिस्ट्रल मॉडेलकडे पाठवलेला प्रॉम्प्टमध्ये प्रश्न आणि प्रश्नाशी मिळत-जुळत असलेल्या रिट्रीव्ह करून आलेल्या तुकड्यांचा समावेश आहे. मॉडेल नंतर नैसर्गिक भाषा प्रतिसाद प्रदान करते. 

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

# हे आपल्या Microsoft Foundry प्रोजेक्टच्या "अवलोकन" पृष्ठावरून घ्या
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # अंतर, अनुक्रमणिका
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

## मिस्ट्रल स्मॉल 
मिस्ट्रल स्मॉल हे मिस्ट्रल कुटुंबातील आणखी एक मॉडेल आहे जे प्रीमियर/एंटरप्राइझ वर्गातील आहे. नावाप्रमाणे, हे एक स्मॉल भाषा मॉडेल (SLM) आहे. मिस्ट्रल स्मॉल वापरण्याचे फायदे आहेत: 
- मिस्ट्रल LLMs सारख्या मिस्ट्रल लार्ज आणि नेमोच्या तुलनेत खर्च बचत - 80% किंमत कपात
- कमी विलंब - मिस्ट्रलच्या LLMs च्या तुलनेत जलद प्रतिसाद
- लवचिक - वेगळ्या वातावरणांमध्ये कमी संसाधनांच्या मर्यादांमध्येही लागू शकतो. 


मिस्ट्रल स्मॉल उत्तम आहे: 
- मजकूर आधारित कामांसाठी जसे की सारांश, भावना विश्लेषण आणि भाषांतर. 
- जिथे वारंवार विनंत्या केल्या जातात अशा अनुप्रयोगांसाठी खर्च कार्यक्षमतेमुळे 
- कमी विलंब असलेल्या कोड कामांसाठी जसे पुनरावलोकन आणि कोड सूचना 

## मिस्ट्रल स्मॉल आणि मिस्ट्रल लार्ज यांची तुलना 

मिस्ट्रल स्मॉल आणि लार्ज यांच्यातील विलंबातील फरक दाखवण्यासाठी खालील सेल्स चालवा. 

आपण 3-5 सेकंदांमध्ये प्रतिसाद वेळांतील फरक पाहू शकता. त्याच प्रॉम्प्टवर प्रतिसादांची लांबी आणि शैली याकाही लक्षात ठेवा.  

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

## मिस्ट्रल नेमो

या धड्यात चर्चा केलेल्या इतर दोन मॉडेल्सच्या तुलनेत, मिस्ट्रल नेमो हा एकमेव मोफत मॉडेल आहे ज्याला Apache2 परवाना आहे. 

हा पूर्वीच्या open source LLM, मिस्ट्रल 7B चा अपग्रेड मानला जातो. 

नेमो मॉडेलची काही इतर वैशिष्ट्ये आहेत: 

- *अधिक कार्यक्षम टोकनायझेशन:* हा मॉडेल tiktoken पेक्षा Tekken टोकनायझर वापरतो. यामुळे अधिक भाषा आणि कोडवर सुधारित कार्यक्षमतेस मदत होते. 

- *फाइनट्यूनिंग:* बेस मॉडेल फाइनट्यूनिंगसाठी उपलब्ध आहे. हे वापराचे लवचिकपण वाढवते जेथे फाइनट्यूनिंगची गरज असू शकते. 

- *नेटिव्ह फंक्शन कॉलिंग* - मिस्ट्रल लार्ज प्रमाणे, या मॉडेलमध्ये फंक्शन कॉलिंगचे प्रशिक्षण झाले आहे. हे त्याला पहिले ओपन सोर्स मॉडेल्सपैकी एक बनवते जे असे करते. 


### टोकनायझर्सची तुलना 

या नमुन्यात, आपण मिस्ट्रल नेमो टोकनायझेशन कसे हाताळतो हे मिस्ट्रल लार्जच्या तुलनेत पाहणार आहोत. 

दोन्ही नमुने समान प्रॉम्प्ट घेतात पण आपण पाहाल की नेमो मिस्ट्रल लार्जपेक्षा कमी टोकन्स परत करतो. 

```bash
pip install mistral-common
```

```python 
# आवश्यक पॅकेजेस आयात करा:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# मिस्टारल टोकनायझर लोड करा

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# संदेशांच्या यादीचे टोकन करा
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

# टोकनची संख्या मोजा
print(len(tokens))
```

```python
# आवश्यक पॅकेजेस आयात करा:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# मिस्ट्रल टोकनायझर लोड करा

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# संदेशांची यादी टोकन करा
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

# टोकन्सची संख्या मोजा
print(len(tokens))
```

## शिकणे येथे थांबत नाही, प्रवास सुरू ठेवा

हा धडा पूर्ण केल्यावर, आमचा [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) पहा आणि तुमचे Generative AI ज्ञान अजून वाढवा!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->