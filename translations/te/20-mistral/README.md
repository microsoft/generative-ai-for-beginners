# మిస్ట్రాల్ నమూనాలు తో నిర్మాణం

## పరిచయం

ఈ పాఠం కవర్ చేస్తుంది:
- వివిధ మిస్ట్రాల్ నమూనాలను అన్వేషించడం
- ప్రతి నమూనా కోసం వినియోగ సందర్భాలు మరియు పరిస్థితులను అవగాహన చేసుకోవడం
- ప్రతి నమూనా యొక్క ప్రత్యేక లక్షణాలను చూపించే కోడ్ నమూనాలను అన్వేషించడం.

## మిస్ట్రాల్ నమూనాలు

ఈ పాఠంలో, మేము మూడు వేర్వేర్వు మిస్ట్రాల్ నమూనాలను అన్వేషిస్తాము:
**మిస్ట్రాల్ లార్జ్**, **మిస్ట్రాల్ స్మాల్** మరియు **మిస్ట్రాల్ నేమో**.

ఈ ప్రతి నమూనా [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) లో ఉచితంగా అందుబాటులో ఉంది. ఈ నోట్‌బుక్ లోని కోడ్ ఈ నమూనాలను ఉపయోగించి కోడ్‌ను నడిపిస్తుంది.

> **గమనిక:** GitHub Models జూలై 2026 చివరికి రిటైర్ అవుతోంది. AI నమూనాలను ప్రోటోటైప్ చేయడానికి [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ఉపయోగించే మరిన్ని వివరాలు ఇక్కడ ఉన్నాయి.


## మిస్ట్రాల్ లార్జ్ 2 (2407)
మిస్ట్రాల్ లార్జ్ 2 ప్రస్తుతముగా మిస్ట్రాల్ నుండి ప్రధాన నమూనా మరియు ఇది సంస్థ వాడుక కోసం రూపొందించబడింది.

ఈ నమూనా అసలు మిస్ట్రాల్ లార్జ్ కి ఒక అప్‌గ్రేడ్:
-  పెద్ద కాంటెక్స్ట్ విండో - 128k వర్సెస్ 32k
-  గణితం మరియు కోడింగ్ పనులపై మెరుగైన ప్రదర్శన - 76.9% సగటు ఖచ్చితత్వం వర్సెస్ 60.4%
-  పెరిగిన బహుభాషా ప్రదర్శన - భాషలు: ఇంగ్లీష్, ఫ్రెంచ్, జర్మన్, స్పానిష్, ఇటాలియన్, పోర్చుగీస్, డచ్, రషియన్, చైనీస్, జపనీస్, కొరియన్, అరబిక్, హింది.

ఈ లక్షణాలతో, మిస్ట్రాల్ లార్జ్ క్రింది విషయాలలో మెరుగ్గా పనిచేస్తుంది:
- *రిట్రీవల్ ఆగ్మెంటెడ్ జనరేషన్ (RAG)* - పెద్ద కాంటెక్స్ట్ విండో కారణంగా
- *ఫంక్షన్ కాలింగ్* - ఈ నమూనాకు స్వదేశీ ఫంక్షన్ కాలింగ్ ఉంది, ఇది బాహ్య సాధనాలు మరియు API లతో ఇంటిగ్రేషన్‌ను అనుమతిస్తుంది. ఈ కాల్స్ సమాంతరంగా లేదా క్రమం తప్పకుండా నిర్వహించవచ్చు.
- *కోడ్ జనరేషన్* - ఈ నమూనా Python, Java, TypeScript మరియు C++ జనరేషన్‌లో మెరుగ్గా పనిచేస్తుంది.

### మిస్ట్రాల్ లార్జ్ 2 ఉపయోగించి RAG ఉదాహరణ

ఈ ఉదాహరణలో, మేము మిస్ట్రాల్ లార్జ్ 2 ని ఉపయోగించి ఒక RAG విధానం ద్వారా టెక్స్ట్ డాక్యుమెంట్ పై నడుపుతున్నాము. ప్రశ్న కొరియన్ లో ఉంది మరియు రచయిత కళాశాల ముందు చేసిన కార్యకలాపాల గురించి అడుగుతుంది.

ఇది Cohere ఎంబెడింగ్స్ నమూనాను ఉపయోగించి టెక్స్ట్ డాక్యుమెంట్ మరియు ప్రశ్న కోసం ఎంబెడింగ్స్ సృష్టిస్తుంది. ఈ నమూనా faiss Python ప్యాకేజీని వెక్టర్ స్టోర్ గా ఉపయోగిస్తుంది.

మిస్ట్రాల్ నమూనాకు పంపబడిన ప్రాంప్ట్ లో ప్రశ్నలు మరియు ప్రశ్నకు సాదృశ్యమైన రిట్రీవ్ చేసిన చంక్‌లు ఉన్నాయి. నమూనా సహజ భాషా సమాధానం అందిస్తుంది.

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

# Microsoft Foundry ప్రాజెక్ట్ యొక్క "సామగ్రి" పేజీ నుండి ఇవి పొందండి
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
మిస్ట్రాల్ స్మాల్ మిస్ట్రాల్ కుటుంబంలోని మరో నమూనా, ప్రీమియర్/ఎంటర్ప్రైజ్ వర్గంలో ఉంది. పేరుసారంగా, ఇది ఒక చిన్న భాషా నమూనా (SLM). మిస్ట్రాల్ స్మాల్ ఉపయోగించే లాభాలు ఉన్నాయి:
- మిస్ట్రాల్ LLM లాంటివి (మిస్ట్రాల్ లార్జ్, NeMo) కంటే ఖర్చు ఆదా - 80% ధర తగ్గింపు
- తక్కువ లేటెన్సీ - మిస్ట్రాల్ యొక్క LLMలతో పోల్చితే వేగవంతమైన ప్రతిస్పందన
- అనుకూలం - తక్కువ వనరుల అవసరాలతో విభిన్న వాతావరణాల్లో అమలు చేయవచ్చు.


మిస్ట్రాల్ స్మాల్ ఈ పనులకెక్కినది:
- సారాంశం, భావ విశ్లేషణ మరియు అనువాదం వంటి టెక్స్ట్ ఆధారిత పనులు
- తరచుగా అభ్యర్థనలు వస్తున్న అనువర్తనాలు దీని ఖర్చు సమర్థత కారణంగా
- సమీక్ష మరియు కోడ్ సూచనల వంటి తక్కువ లేటెన్సీ కోడ్ పనులు

## మిస్ట్రాల్ స్మాల్ మరియు మిస్ట్రాల్ లార్జ్ ను పోల్చడం

మిస్ట్రాల్ స్మాల్ మరియు లార్జ్ మధ్య లేటెన్సీ తేడాలను చూపించడానికి క్రింది సెల్స్ నడపండి.

మీరు 3-5 సెకన్ల మధ్య ప్రతిస్పందన సమయాలలో తేడా చూడగలరు. అలాగే అదే ప్రాంప్ట్ పై ప్రతిస్పందన పొడవులు మరియు శైలిని గమనించండి.

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

## మిస్ట్రాల్ נేమో

ఈ పాఠంలో చర్చించిన ఇతర రెండు నమూనాలతో పోలిస్తే, మిస్ట్రాల్ నేమో ఒకే ఫ్రీ నమూనా మరియు Apache2 లైసెన్స్ కలిగివుంది.

ఇది మిస్ట్రాల్ నుండి పూర్వం ఉన్న ఓపెన్ సోర్సు LLM మిస్ట్రాల్ 7B కి అప్‌గ్రేడ్ గా వీక్షించబడుతుంది.

నేమో నమూనా యొక్క కొన్ని ఇతర లక్షణాలు:

- *మరుగైన టోకనైజేషన్:* ఈ నమూనా ఎక్కువగా ఉపయోగించే tiktoken పై టెక్కెన్ టోకనైజర్ ఉపయోగిస్తుంది. ఇది మరిన్ని భాషలు మరియు కోడ్ పై మెరుగైన ప్రదర్శన అందిస్తుంది.

- *ఫైన్ట్యూనింగ్:* బేస్ నమూనా ఫైన్ట్యూనింగ్ కోసం అందుబాటులో ఉంది. అవసరమైన సందర్భాలలో ఫైన్ట్యూనింగ్ కు ఇది ఎక్కువ అనుకూలత ఇస్తుంది.

- *స్థానిక ఫంక్షన్ కాలింగ్* - మిస్ట్రాల్ లార్జ్ లాగే, ఈ నమూనా ఫంక్షన్ కాలింగ్ పై శిక్షణ పొందింది. ఇది ఓపెన్ సోర్సు నమూనాలలో మొదటిదిగా ఉండటంలో ప్రత్యేకమైనది.


### టోకనైజర్లను పోల్చడం

ఈ ఉదాహరణలో, మేము మిస్ట్రాల్ నేమో టోకనైజేషన్ ను మిస్ట్రాల్ లార్జ్ తో పోల్చి చూస్తాము.

రెండు నమూనాలు ఒకే ప్రాంప్ట్ తీసుకుంటాయి కానీ నేమో మిస్ట్రాల్ లార్జ్ కన్నా తక్కువ టోకన్లను తిరిగి ఇస్తుంది.

```bash
pip install mistral-common
```

```python 
# అవసరమైన ప్యాకేజీలు దిగుమతి చేసుకోండి:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# మిస్ట్రాల్ టోకనైజర్ లోడ్ చేయండి

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
# అవసరమైన ప్యాకేజీలు దిగుమతి చేసుకోండి:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# మిస్ట్రాల్ టోకనైజర్‌ను లోడ్ చేయండి

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

## నేర్చుకునే ప్రక్రియ ఇక్కడ ముగియదు, ప్రయాణం కొనసాగించండి

ఈ పాఠం పూర్తి చేసిన తర్వాత, మా [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ను పరిశీలించి మీ జెనరేటివ్ AI జ్ఞానాన్ని మెరుగుపరచండి!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->