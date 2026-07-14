# మిస్ట్రాల్ మోడల్స్‌తో నిర్మాణం  

## పరిచయం  

ఈ పాఠం లో కవరచేయబడుతుంది:  
- వివిధ మిస్ట్రాల్ మోడల్స్ అన్వేషణ  
- ప్రతి మోడల్ కోసం ఉపయోగ کیسులు మరియు పరిస్థితులను అర్థం చేసుకోవడం  
- ప్రతి మోడల్ యొక్క ప్రత్యేక లక్షణాలను చూపించే కోడ్ నమూనాలను అన్వేషించడం.  

## మిస్ట్రాల్ మోడల్స్  

ఈ పాఠంలో, మేము 3 వేర్వేరు మిస్ట్రాల్ మోడల్స్‌ను అన్వేషిస్తాము:  
**మిస్ట్రాల్ లార్జ్**, **మిస్ట్రాల్ స్మాల్** మరియు **మిస్ట్రాల్ నేమో**.  

ఈ మోడల్స్‌లో ప్రతీటి [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) లో ఉచితంగా అందుబాటులో ఉన్నాయి. ఈ నోట్‌బుక్ లోని కోడ్ ఈ మోడల్స్ ఉపయోగించి అమలు చేయబడుతుంది.  

> **గమనిక:** GitHub Models 2026 జూలై చివర నాటికి రిటైర్ అవుతున్నారు. AI మోడల్స్ తో ప్రోటోటైపింగ్ కోసం [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ఉపయోగించుటకు మరింత వివరాలు ఇక్కడ ఉన్నాయి.  


## మిస్ట్రాల్ లార్జ్ 2 (2407)  
మిస్ట్రాల్ లార్జ్ 2 ప్రస్తుతం మిస్ట్రాల్ నుండి ప్రముఖ మోడల్ మరియు ఇది సంస్థా ఉపయోగానికి రూపొందించబడింది.  

ఈ మోడల్ అసలు మిస్ట్రాల్ లార్జ్‌కు అప్గ్రేడ్‌గా అందిస్తుంది  
- పెద్ద కంటెక్స్ట్ విండో - 128k వర్సెస్ 32k  
- గణితం మరియు కోడింగ్ పనులపై మెరుగైన పనితీరు - సగటు ఖచ్చితత్వం 76.9% వర్సెస్ 60.4%  
- పెంచబడిన బహుభాషా పనితీరు - భాషలు ఉంటాయి: ఆంగ్లం, ఫ్రెంచ్, జర్మన్, స్పానిష్, ఇటాలియన్, పోర్చుగీస్, డచ్, రష్యన్, చైనీస్, జపనీస్, కొరియన్, అరబిక్ మరియు హిందీ.  

ఈ లక్షణాలతో, మిస్ట్రాల్ లార్జ్ ప్రత్యేకంగా బాగున్నది  
- *రిట్రీవల్ ఆగ్మెంటడ్ జనరేషన్ (RAG)* - పెద్ద కంటెక్స్ట్ విండో కారణంగా  
- *ఫంక్షన్ కాలింగ్* - ఈ మోడల్ స్థానిక ఫంక్షన్ కాలింగ్ కలిగి ఉంది, ఇది బాహ్య టూల్స్ మరియు API లతో ఇంటిగ్రేషన్‌కు వీలు ఇస్తుంది. ఈ కాల్స్ పైరలల్‌లో లేదా పరస్పరం వరసగా ఒకదానికి తర్వాత ఒకటి చేయవచ్చు.  
- *కోడ్ జనరేషన్* - ఈ మోడల్ పైథాన్, జావా, టైప్స్క్రిప్ట్ మరియు C++ జనరేషన్‌లో బాగా పనిచేస్తుంది.  

### మిస్ట్రాల్ లార్జ్ 2 ఉపయోగించి RAG ఉదాహరణ  

ఈ ఉదాహరణలో, మేము మిస్ట్రాల్ లార్జ్ 2 ఉపయోగించి RAG నమూనాను ఒక టెక్స్ట్ డాక్యుమెంట్ పై అమలు చేస్తున్నాము. ప్రశ్న కొరియన్ భాషలో ఉంది మరియు రచయిత కళాశాలను ముందు చేసిన కార్యకలాపాల గురించి అడుగుతుంది.  

ఇది Cohere Embeddings మోడల్ ఉపయోగించి టెక్స్ట్ డాక్యుమెంట్ మరియు ప్రశ్న embedding లను సృష్టిస్తుంది. ఈ నమూనాకు faiss Python ప్యాకేజ్‌ను వెక్టర్ స్టోర్‌గా ఉపయోగిస్తుంది.  

మిస్ట్రాల్ మోడల్‌కు పంపిన ప్రాంప్ట్ ప్రశ్నలు మరియు ప్రశ్నకు సమానమైన రిట్రీవ్ అయిన భాగాలను రెండింటినీ కలిగి ఉంటుంది. ఈ మోడల్ సహజ భాషలో స్పందన ఇస్తుంది.  

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

# మీ Microsoft Foundry ప్రాజెక్ట్ యొక్క "సారాంశం" పేజీ నుండి ఇవి పొందండి
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # దూరం, సూచిక
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

## మిస్ట్రాల్ స్మాల్  
మిస్ట్రాల్ స్మాల్ మిస్ట్రాల్ కుటుంబంలోని మరో మోడల్, ఇది ప్రముఖ/కంపెనీ వర్గానికి చెందినది. పేరు సూచించేటట్టు ఈ మోడల్ ఒక చిన్న భాషా మోడల్ (SLM). మిస్ట్రాల్ స్మాల్ ఉపయోగించే ప్రయోజనాలు:  
- మిస్ట్రాల్ LLM లాంటి మిస్ట్రాల్ లార్జ్ మరియు NeMo కన్నా ఖర్చు తక్కువ - 80% ధర తగ్గింపు  
- తక్కువ ఆలస్యం - మిస్ట్రాల్ యొక్క LLM లతో పోలిస్తే వేగవంతమైన స్పందన  
- అనుకూలత - తక్కువ వనరుల అవసరంతో విభిన్న పరిసరాలలో అమలు చేయగలదు.  


మిస్ట్రాల్ స్మాల్ మంచి అనువర్తనాలు:  
- సారాంశం, భావ విశ్లేషణ మరియు అనువాదం వంటి టెక్స్ట్ ఆధారిత పనులు.  
- ఖర్చు సమర్థవంతంగా ఉండటం వల్ల తరచుగా అభ్యర్థనలు వచ్చే అనువర్తనాలు  
- సమీక్ష మరియు కోడ్ సూచనల వంటి తక్కువ ఆలస్యం కలిగిన కోడ్ పనులు  

## మిస్ట్రాల్ స్మాల్ మరియు మిస్ట్రాల్ లార్జ్ తులన  

మిస్ట్రాల్ స్మాల్ మరియు లార్జ్ మధ్య ఆలస్యం తేడాను చూపడానికి, దిగువ సెల్‌లను అమలు చేయండి.  

ఒకే ప్రాంప్ట్ మీద స్పందన సమయాలలో 3-5 సెకన్ల వరకు తేడా కనిపిస్తుంది. అలాగే ప్రతిస్పందన లెన్త్‌లు మరియు శైలుల ప్రకారం కూడా గమనించండి.  

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

## మిస్ట్రాల్ నేమో  

ఈ పాఠంలో చర్చించిన రెండుపై మోడల్స్‌తో పోలిస్తే, మిస్ట్రాల్ నేమో ఏపాచీ2 లైసెన్స్ కలిగిన ఏకైక ఉచిత మోడల్.  

ఇది మరుపురాని ఫ్రీ సోర్స్ LLM, మిస్ట్రాల్ 7B కు ఒక కొత్త సంస్కరణగా పరిగణించబడుతుంది.  

నేమో మోడల్ కొన్ని ఇతర లక్షణాలు:  

- *మరింత సమర్థవంతమైన టోకనైజేషన్:* ఈ మోడల్ tiktoken కంటే ఎక్కువగా ఉపయోగించే Tekken టోకనైజర్ ఉపయోగిస్తుంది. ఇది ఎక్కువ భాషలు మరియు కోడ్‌లో మెరుగైన పనితీరును అందిస్తుంది.  

- *ఫైన్‌ట్యూనింగ్:* బేస్ మోడల్ ఫైన్‌ట్యూన్ కోసం అందుబాటులో ఉంది. ఇది ఫైన్‌ట్యూనింగ్ అవసరమయ్యే వాడుక కేసులకు ఎక్కువ అనుకూలత ఇస్తుంది.  

- *స్థానిక ఫంక్షన్ కాలింగ్* - మిస్ట్రాల్ లార్జ్ లా, ఈ మోడల్ ఫంక్షన్ కాలింగ్ పై శిక్షణ పొందింది. ఇది మొదటి ఓపెన్ సోర్స్ మోడల్స్ లో ఒకటిగా ప్రత్యేకత కలిగింది.  


### టోకనైజర్స్ తులన  

ఈ ఉదాహరణలో, మేము మిస్ట్రాల్ నేమో టోకనైజేషన్‌ను మిస్ట్రాల్ లార్జ్‌తో ఎలా నిర్వహిస్తుందో చూస్తాము.  

రెండు నమూనాలు ఒకే ప్రాంప్ట్ తీసుకుంటాయి కానీ నేమో మిస్ట్రాల్ లార్జ్ కంటే తక్కువ టోకెన్స్ తిరిగి ఇస్తుంది.  

```bash
pip install mistral-common
```

```python 
# అవసరమైన ప్యాకేజీలను దిగుమతి చేసుకోండి:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# మిస్ట్రల్ టోకనైజర్ ని లోడ్ చేయండి

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# సందేశాల జాబితాను టోకనైజ్ చేయండి
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

# టోకెన్ల సంఖ్యను లెక్కించండి
print(len(tokens))
```

```python
# అవసరమైన ప్యాకేజీలను దిగుమతి చేసుకోండి:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# మిస్ట్రల్ టోకెనైజర్‌ను లోడ్ చేయండి

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# సందేశాల జాబితాను టోకెనైజ్ చేయండి
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

# టోకెన్ల సంఖ్యను లెక్కించండి
print(len(tokens))
```

## నేర్చుకోవడం ఇక్కడ ఆగదు, ప్రయాణాన్ని కొనసాగించండి  

ఈ పాఠాన్ని పూర్తిచేసిన తర్వాత, మా [Generative AI నేర్చుకునే సేకరణ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) చూసి మీ Generative AI జ్ఞానాన్ని మరింత పెంచుకోండి!  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->