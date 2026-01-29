# మిస్ట్రాల్ మోడల్స్‌తో నిర్మాణం

## పరిచయం

ఈ పాఠం కవర్ చేస్తుంది:  
- వివిధ మిస్ట్రాల్ మోడల్స్‌ను అన్వేషించడం  
- ప్రతి మోడల్ కోసం ఉపయోగాలూ మరియు సందర్భాలను అర్థం చేసుకోవడం  
- కోడ్ నమూనాలు ప్రతి మోడల్ యొక్క ప్రత్యేక లక్షణాలను చూపించడం.

## మిస్ట్రాల్ మోడల్స్

ఈ పాఠంలో, మేము 3 విభిన్న మిస్ట్రాల్ మోడల్స్‌ను అన్వేషిస్తాము:  
**మిస్ట్రాల్ లార్జ్**, **మిస్ట్రాల్ స్మాల్** మరియు **మిస్ట్రాల్ నేమో**.

ఈ మోడల్స్ అందుబాటులో ఉన్నాయి గిట్హబ్ మోడల్ మార్కెట్‌ప్లేస్‌లో ఉచితంగా. ఈ నోట్‌బుక్‌లోని కోడ్ ఈ మోడల్స్‌ను ఉపయోగించి కోడ్ నడుపుతుంది. గిట్హబ్ మోడల్స్‌ను ఉపయోగించి [AI మోడల్స్‌తో ప్రోటోటైపింగ్](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) గురించి మరిన్ని వివరాలు ఇక్కడ ఉన్నాయి.

## మిస్ట్రాల్ లార్జ్ 2 (2407)  
మిస్ట్రాల్ లార్జ్ 2 ప్రస్తుతం మిస్ట్రాల్ నుండి ఫ్లాగ్‌షిప్ మోడల్ మరియు ఇది ఎంటర్ప్రైజ్ ఉపయోగం కోసం రూపొందించబడింది.

ఈ మోడల్ ఒరిజినల్ మిస్ట్రాల్ లార్జ్‌కు అప్‌గ్రేడ్‌గా ఉంది, అందిస్తుంది:  
- పెద్ద కాంటెక్స్ట్ విండో - 128k వర్సెస్ 32k  
- గణితం మరియు కోడింగ్ పనులపై మెరుగైన పనితీరు - 76.9% సగటు ఖచ్చితత్వం వర్సెస్ 60.4%  
- బహుభాషా పనితీరు పెరిగింది - భాషలు: ఇంగ్లీష్, ఫ్రెంచ్, జర్మన్, స్పానిష్, ఇటాలియన్, పోర్చుగీస్, డచ్, రష్యన్, చైనీస్, జపనీస్, కొరియన్, అరబిక్, మరియు హిందీ.

ఈ లక్షణాలతో, మిస్ట్రాల్ లార్జ్ ప్రత్యేకంగా మెరుగుపడింది:  
- *రిట్రీవల్ ఆగ్మెంటెడ్ జనరేషన్ (RAG)* - పెద్ద కాంటెక్స్ట్ విండో కారణంగా  
- *ఫంక్షన్ కాలింగ్* - ఈ మోడల్ స్థానిక ఫంక్షన్ కాలింగ్ కలిగి ఉంది, ఇది బాహ్య టూల్స్ మరియు APIs తో ఇంటిగ్రేషన్‌ను అనుమతిస్తుంది. ఈ కాల్స్‌ను సమాంతరంగా లేదా వరుసగా ఒకదాని తర్వాత ఒకటి చేయవచ్చు.  
- *కోడ్ జనరేషన్* - ఈ మోడల్ పైథాన్, జావా, టైప్‌స్క్రిప్ట్ మరియు C++ జనరేషన్‌లో మెరుగ్గా పనిచేస్తుంది.

### మిస్ట్రాల్ లార్జ్ 2 ఉపయోగించి RAG ఉదాహరణ

ఈ ఉదాహరణలో, మేము మిస్ట్రాల్ లార్జ్ 2 ఉపయోగించి ఒక RAG ప్యాటర్న్‌ను టెక్స్ట్ డాక్యుమెంట్‌పై నడుపుతున్నాము. ప్రశ్న కొరియన్‌లో రాయబడింది మరియు రచయిత కళాశాలకి ముందు చేసిన కార్యకలాపాల గురించి అడుగుతుంది.

ఇది కోహియర్ ఎంబెడ్డింగ్స్ మోడల్‌ను ఉపయోగించి టెక్స్ట్ డాక్యుమెంట్ మరియు ప్రశ్న యొక్క ఎంబెడ్డింగ్స్ సృష్టిస్తుంది. ఈ నమూనాకు, ఇది faiss పైథాన్ ప్యాకేజీని వెక్టర్ స్టోర్‌గా ఉపయోగిస్తుంది.

మిస్ట్రాల్ మోడల్‌కు పంపిన ప్రాంప్ట్‌లో ప్రశ్నలు మరియు ప్రశ్నకు సమానమైన రిట్రీవ్ చేసిన చంక్స్ రెండూ ఉంటాయి. మోడల్ తరువాత సహజ భాషా ప్రతిస్పందనను అందిస్తుంది.

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
మిస్ట్రాల్ స్మాల్ మిస్ట్రాల్ కుటుంబంలోని మరో మోడల్, ఇది ప్రీమియర్/ఎంటర్ప్రైజ్ వర్గంలో ఉంది. పేరుకి అనుగుణంగా, ఈ మోడల్ ఒక చిన్న భాషా మోడల్ (SLM). మిస్ట్రాల్ స్మాల్ ఉపయోగించడంలో లాభాలు:  
- మిస్ట్రాల్ LLMs (మిస్ట్రాల్ లార్జ్ మరియు నేమో వంటి) తో పోల్చితే ఖర్చు ఆదా - 80% ధర తగ్గింపు  
- తక్కువ లేటెన్సీ - మిస్ట్రాల్ LLMs తో పోల్చితే వేగవంతమైన ప్రతిస్పందన  
- సౌలభ్యం - తక్కువ వనరులపై తక్కువ పరిమితులతో వివిధ వాతావరణాలలో అమలు చేయవచ్చు.

మిస్ట్రాల్ స్మాల్‌కు అనుకూలమైనవి:  
- సారాంశం, భావ విశ్లేషణ మరియు అనువాదం వంటి టెక్స్ట్ ఆధారిత పనులు  
- తరచుగా అభ్యర్థనలు చేయబడే అప్లికేషన్లు, దీని ఖర్చు సమర్థత కారణంగా  
- సమీక్ష మరియు కోడ్ సూచనల వంటి తక్కువ లేటెన్సీ కోడ్ పనులు

## మిస్ట్రాల్ స్మాల్ మరియు మిస్ట్రాల్ లార్జ్ తులన

మిస్ట్రాల్ స్మాల్ మరియు లార్జ్ మధ్య లేటెన్సీ తేడాను చూపించడానికి, క్రింది సెల్స్ నడపండి.

3-5 సెకన్ల మధ్య ప్రతిస్పందన సమయాల్లో తేడా కనిపిస్తుంది. అలాగే అదే ప్రాంప్ట్‌పై ప్రతిస్పందన పొడవు మరియు శైలిని గమనించండి.

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
  
## మిస్ట్రాల్ నేమో

ఈ పాఠంలో చర్చించిన మిగతా రెండు మోడల్స్‌తో పోల్చితే, మిస్ట్రాల్ నేమో ఏపాచీ2 లైసెన్స్‌తో ఉచిత మోడల్ మాత్రమే.

ఇది మిస్ట్రాల్ నుండి ముందుగా విడుదలైన ఓపెన్ సోర్స్ LLM, మిస్ట్రాల్ 7B కి అప్‌గ్రేడ్‌గా భావించబడుతుంది.

నేమో మోడల్ యొక్క కొన్ని ఇతర లక్షణాలు:

- *మరింత సమర్థవంతమైన టోకనైజేషన్:* ఈ మోడల్ సాధారణంగా ఉపయోగించే tiktoken కంటే Tekken టోకనైజర్‌ను ఉపయోగిస్తుంది. ఇది మరిన్ని భాషలు మరియు కోడ్‌పై మెరుగైన పనితీరును అందిస్తుంది.

- *ఫైన్‌ట్యూనింగ్:* బేస్ మోడల్ ఫైన్‌ట్యూనింగ్ కోసం అందుబాటులో ఉంది. ఇది ఫైన్‌ట్యూనింగ్ అవసరమయ్యే ఉపయోగాల కోసం మరింత సౌలభ్యాన్ని ఇస్తుంది.

- *స్థానిక ఫంక్షన్ కాలింగ్* - మిస్ట్రాల్ లార్జ్‌లాగా, ఈ మోడల్ కూడా ఫంక్షన్ కాలింగ్‌పై శిక్షణ పొందింది. ఇది మొదటి ఓపెన్ సోర్స్ మోడల్స్‌లో ఒకటిగా ప్రత్యేకతను కలిగి ఉంది.

### టోకనైజర్ల తులన

ఈ నమూనాలో, మిస్ట్రాల్ నేమో టోకనైజేషన్‌ను మిస్ట్రాల్ లార్జ్‌తో పోల్చి చూస్తాము.

రెండు నమూనాలు కూడా అదే ప్రాంప్ట్ తీసుకుంటాయి, కానీ నేమో తక్కువ టోకెన్లను తిరిగి ఇస్తుంది మిస్ట్రాల్ లార్జ్‌తో పోల్చితే.

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

# మిస్ట్రాల్ టోకనైజర్‌ను లోడ్ చేయండి

model_name = "open-mistral-nemo	"

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

# టోకన్ల సంఖ్యను లెక్కించండి
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

# మిస్ట్రాల్ టోకనైజర్‌ను లోడ్ చేయండి

model_name = "mistral-large-latest"

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

# టోకెన్ల సంఖ్యను లెక్కించండి
print(len(tokens))
```
  
## నేర్చుకోవడం ఇక్కడ ఆగదు, ప్రయాణం కొనసాగించండి

ఈ పాఠం పూర్తి చేసిన తర్వాత, మా [జెనరేటివ్ AI లెర్నింగ్ సేకరణ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)ను చూడండి, మీ జెనరేటివ్ AI జ్ఞానాన్ని మరింత పెంచుకోండి!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారుల బాధ్యత మేము తీసుకోము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->