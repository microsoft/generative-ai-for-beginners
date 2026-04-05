# मिस्त्रल मॉडेलसह बिल्डिंग  

## परिचय  

ही धडा यात समाविष्ट आहे:  
- वेगवेगळ्या मिस्त्रल मॉडेलसची अन्वेषण  
- प्रत्येक मॉडेलसाठी उपयोग प्रकरणे आणि परिदृश्य समजून घेणे  
- प्रत्येक मॉडेलसच्या वैशिष्ट्ये दाखवणारे कोड सैंपल्स पाहणे.  

## मिस्त्रल मॉडेलस  

या धड्यात, आपण 3 वेगवेगळ्या मिस्त्रल मॉडेलसची अन्वेषण करू:  
**मिस्त्रल लार्ज**, **मिस्त्रल स्मॉल** आणि **मिस्त्रल निमो**.  

या प्रत्येक मॉडेलस गिटहब मॉडेल मार्केटप्लेसवर मोफत उपलब्ध आहेत. या नोटबुकमधील कोड हे मॉडेलस वापरून चालवले जाईल. GitHub मॉडेलस वापरून [AI मॉडेलसह प्रोटोटायपिंग](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) कसे करायचे याबद्दल अधिक माहिती येथे आहे. 


## मिस्त्रल लार्ज 2 (2407)
मिस्त्रल लार्ज 2 सध्या मिस्त्रलकडून प्रमुख मॉडेल आहे आणि ते एंटरप्राइज वापरासाठी डिझाइन केले आहे.  

हा मॉडेल मूळ मिस्त्रल लार्जचा अपग्रेड आहे ज्यामध्ये  
- मोठा कॉन्टेक्स्ट विंडो - 128k विरुद्ध 32k  
- गणित आणि कोडिंग कार्यांवर अधिक चांगली कामगिरी - सरासरी अचूकता 76.9% विरुद्ध 60.4%  
- बहुभाषिक कामगिरी वाढलेली - भाषांमध्ये: इंग्रजी, फ्रेंच, जर्मन, स्पॅनिश, इटालियन, पोर्तुगीज, डच, रशियन, चीनी, जपानी, कोरियन, अरबी आणि हिंदी यांचा समावेश आहे.  

या वैशिष्ट्यांसह, मिस्त्रल लार्ज उत्कृष्ट आहे  
- *रिट्रीव्हल अग्मेंटेड जनरेशन (RAG)* - मोठ्या कॉन्टेक्स्ट विंडोमुळे  
- *फंक्शन कॉलिंग* - या मॉडेलमध्ये नैसर्गिक फंक्शन कॉलिंग आहे जे बाह्य साधने आणि API सह एकत्रीकरणाची परवानगी देते. हे कॉल्स एकाच वेळी किंवा अनुक्रमाने केले जाऊ शकतात.  
- *कोड जनरेशन* - हा मॉडेल Python, Java, TypeScript आणि C++ जनरेशनवर उत्कृष्ट आहे.  

### मिस्त्रल लार्ज 2 वापरून RAG उदाहरण  

या उदाहरणात, आपण मिस्त्रल लार्ज 2 वापरून एक टेक्स्ट दस्तऐवजावर RAG पॅटर्न चालवत आहोत. प्रश्न कोरियनमध्ये लिहिला असून त्यात लेखकाच्या महाविद्यालय पूर्वीच्या क्रियाकलापांविषयी विचारले आहे.  

हे Cohere Embeddings मॉडेल वापरून टेक्स्ट दस्तऐवज तसेच प्रश्नाचे एम्बेडिंग तयार करते. या नमुन्यासाठी faiss Python पॅकेज व्हेक्टर स्टोअर म्हणून वापरले आहे.  

मिस्त्रल मॉडेलस पाठवलेला प्रॉम्प्ट प्रश्न आणि त्या प्रश्नाशी संबंधित पुनर्प्राप्त केलेल्या चंक्स दोन्ही समाविष्ट करतो. मॉडेल नंतर एक नैसर्गिक भाषा प्रतिसाद देते.  

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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # अंतर, निर्देशांक
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
मिस्त्रल स्मॉल हे मिस्त्रल कुटुंबातील आणखी एक मॉडेल आहे जे प्रीमियर/एंटरप्राइज श्रेणीमध्ये येते. नावाप्रमाणे, हे एक लहान भाषा मॉडेल (SLM) आहे. मिस्त्रल स्मॉल वापरण्याचे फायदे म्हणजे:  
- मिस्त्रल LLMs सारख्या मिस्त्रल लार्ज आणि निमोच्या तुलनेत खर्च बचत - 80% किमतीत कपात  
- कमी विलंब - मिस्त्रलच्या LLMs पेक्षा जलद प्रतिसाद  
- लवचीकता - विविध पर्यावरणांमध्ये कमी संसाधने आवश्यक असल्यामुळे सुलभपणे तैनात करता येते.  

मिस्त्रल स्मॉल उत्तम आहे:  
- मजकूर आधारित कार्यांसाठी जसे की सारांश तयार करणे, भावना विश्लेषण आणि भाषांतर.  
- जिथे वारंवार विनंत्या येतात अशा अनुप्रयोगांसाठी त्याचा खर्च परिणामकारकता मुळे  
- कमी विलंब असलेल्या कोड कार्यांसाठी जसे की पुनरावलोकन आणि कोड सूचनांसाठी  

## मिस्त्रल स्मॉल आणि मिस्त्रल लार्जची तुलना  

मिस्त्रल स्मॉल आणि लार्ज मधील विलंबातील फरक दाखवण्यासाठी खालील कोशिकाचा वापर करा.  

आपल्याला प्रतिसाद वेळांमध्ये 3-5 सेकंदाचा फरक दिसेल. तसेच त्याच प्रॉम्प्टवर प्रतिसादाची लांबी आणि शैली नोंदवा.  

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
  
## मिस्त्रल निमो  

या धड्यात चर्चा केल्या गेलेल्या इतर दोन मॉडेल्सच्या तुलनेत, मिस्त्रल निमो हा एकमेव मोफत मॉडेल आहे ज्याला Apache2 परवानगी आहे.  

त्याला मिस्त्रलच्या पूर्वीच्या मुक्त स्रोत LLM, मिस्त्रल 7B चा अपग्रेड मानले जाते.  

निमो मॉडेलची काही इतर वैशिष्ट्ये:  

- *अधिक कार्यक्षम टोकनायझेशन:* हा मॉडेल Tekken tokenizer वापरतो जो सर्वसामान्यत: वापरल्या जाणार्‍या tiktoken पेक्षा वेगळा आहे. हे अधिक भाषा आणि कोडवर चांगले कामगिरी करण्यास सक्षम करते.  

- *फायनट्युनिंग:* बेस मॉडेल फायनट्युनिंगसाठी उपलब्ध आहे. यामुळे जेथे फायनट्युनिंग आवश्यक असेल तेथे अधिक लवचीकता मिळते.  

- *नैसर्गिक फंक्शन कॉलिंग* - मिस्त्रल लार्जसारखे, या मॉडेलचे प्रशिक्षण फंक्शन कॉलिंगवर झाले आहे. हे त्याला मुक्त स्रोत मॉडेल्सपैकी एक म्हणून अनोखे बनवते.  


### टोकनायझर्सची तुलना  

या नमुन्यात, आपण मिस्त्रल निमो टोकनायझेशन कसे हाताळते त्याची तुलना मिस्त्रल लार्जशी करू.  

दोन्ही नमुने एकाच प्रॉम्प्टवर घेतले आहेत पण तुम्हाला दिसेल की निमो मिस्त्रल लार्जच्या तुलनेत कमी टोकन्स परत करतो.  

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

# मिस्टрал टोकनायझर लोड करा

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# संदेशांच्या यादीचे टोकनायझेशन करा
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

# मिस्ट्राल टोकनायझर लोड करा

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# संदेशांच्या यादीचे टोकनायझेशन करा
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
  
## शिक्षण येथे थांबत नाही, प्रवास सुरू ठेवा  

हा धडा पूर्ण केल्यावर, आमची [जनरेटिव्ह AI शिक्षण संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) तपासा आणि आपल्या जनरेटिव्ह AI ज्ञानाला पुढे वाढवा!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा असमर्थता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीच्या बाबतीत व्यावसायिक मानवी अनुवाद शिफारस केला जातो. या अनुवादाचा वापर केल्यामुळे उद्भवणा-या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थापाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->