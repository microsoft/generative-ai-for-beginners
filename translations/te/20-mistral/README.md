# మిస్ట్రాల్ మోడల్స్‌తో నిర్మించడం

## పరిచయం

ఈ పాఠం కింది అంశాలను కవర్ చేస్తుంది:
- వివిధ మిస్ట్రాల్ మోడల్స్‌ను అన్వేషించడం
- ప్రతి మోడల్ కోసం వినియోగ సందర్భాలు మరియు పరిస్థితులను అర్థం చేసుకోవడం
- ప్రతి మోడల్ యొక్క ప్రత్యేక లక్షణాలను చూపించే కోడ్ నమూనాలను అన్వేషించడం.

## మిస్ట్రాల్ మోడల్స్

ఈ పాఠంలో, మేము 3 వివిధ మిస్ట్రాల్ మోడల్స్‌ను అన్వేషిస్తాము:
**మిస్ట్రాల్ లార్జ్**, **మిస్ట్రాల్ స్మాల్** మరియు **మిస్ట్రాల్ నేమో**.

ఈ మోడల్స్ ప్రతీటి GitHub మోడల్ మార్కెట్‌ప్లేస్‌లో ఉచితంగా అందుబాటులో ఉన్నాయి. ఈ నోట్‌బుక్‌లో ఉన్న కోడ్ ఈ మోడల్స్‌ను ఉపయోగించి కోడ్ నడుపుతుంది. GitHub మోడల్స్‌ను ఉపయోగించి [AI మోడల్స్‌తో ప్రోటోటైప్ చేయడం](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) గురించి మరిన్ని వివరాలు ఇక్కడ ఉన్నవి.

## మిస్ట్రాల్ లార్జ్ 2 (2407)
మిస్ట్రాల్ లార్జ్ 2 ప్రస్తుతం మిస్ట్రాల్ నుండి ప్రధాన మోడల్‌గా ఉంది మరియు ఎంటర్‌ప్రైజ్ వినియోగం కోసం రూపొందించబడింది.

ఈ మోడల్ అసలు మిస్ట్రాల్ లార్జ్‌ను అప్గ్రేడ్ చేయడం ద్వారా వచ్చినది:
- పెద్ద కాంటెక్స్ట్ విండో - 128k vs 32k
- గణితం మరియు కోడింగ్ పనులపై మెరుగైన పనితీరు - సగటు ఖచ్చితత్వం 76.9% vs 60.4%
- బహుభాషా పనితీరు పెరుగుదల - భాషలు: ఆంగ్లం, ఫ్రెంచ్, జర్మన్, స్పానిష్, ఇటాలియన్, పోర్చుగీస్, డచ్, రష్యన్, చైనీస్, జపనీస్, కొరియన్, అరబిక్, మరియు హిందీ

ఈ లక్షణాల కారణంగా, మిస్ట్రాల్ లార్జ్ మెరుగ్గా పనిచేస్తుంది:
- *రీట్రీవల్ ఆగ్మెంటెడ్ జనరేషన్ (RAG)* - పెద్ద కాంటెక్స్ట్ విండో కారణంగా
- *ఫంక్షన్ కాలింగ్* - ఈ మోడల్ లో సహజ ఫంక్షన్ కాలింగ్ ఉంది, ఇది బాహ్య కరెంలతో మరియు APIs తో ఇంటిగ్రేషన్‌ను అనుమతిస్తుంది. ఈ కాల్స్‌ను సమాంతరంగా లేదా ఒకదానికంటే మరొకదానికి అనుక్రమంగా చేయవచ్చు.
- *కోడ్ జనరేషన్* - ఈ మోడల్ పైథాన్, జావా, టైప్‌స్క్రిప్ట్ మరియు C++ కోడ్ ఉత్పత్తిలో మెరుగ్గా పనిచేస్తుంది.

### మిస్ట్రాల్ లార్జ్ 2 ఉపయోగించి RAG ఉదాహరణ

ఈ ఉదాహరణలో, మేము మిస్ట్రాల్ లార్జ్ 2 ఉపయోగించి టెక్ట్స్ డాక్యుమెంట్ మీద RAG ప్యాటర్న్ నడుపుతున్నాం. ప్రశ్న కొరియన్‌లో వ్రాయబడింది మరియు రచయిత కాలేజ్‌కి ముందే చేసిన కార్యకలాపాల గురించి అడుగుతుంది.

ఇది Cohere ఎంబెడ్డింగ్స్ మోడల్‌ను ఉపయోగించి టెక్ట్స్ డాక్యుమెంట్ మరియు ప్రశ్న యొక్క ఎంబెడ్డింగ్స్‌ని సృష్టిస్తుంది. ఈ నమూనా కోసం, faiss పైథాన్ ప్యాకేజీని వెక్టర్ స్టోర్‌గా ఉపయోగిస్తుంది.

మోడల్‌కు పంపిన ప్రాంప్ట్‌లో ప్రశ్నలు మరియు ప్రశ్నకు సమానమైన రిట్రీవ్ చేసిన భాగాలు ఉంటాయి. ఆ తరువాత మోడల్ సహజ భాషా ప్రతిస్పందనను అందిస్తుంది.

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
మిస్ట్రాల్ స్మాల్ మిస్ట్రాల్ కుటుంబంలోని మరో మోడల్, ప్రీమియర్/ఎంటర్‌ప్రైజ్ వర్గంలో ఉంటుంది. పేరుప్రకారం, ఈ మోడల్ ఒక చిన్న భాషా మోడల్ (SLM).

మిస్ట్రాల్ స్మాల్ ఉపయోగించడంలో ఉన్న ప్రయోజనాలు:
- మిస్ట్రాల్ LLMs వంటి మిస్ట్రాల్ లార్జ్ మరియు నేమోతో పోల్చితే ఖర్చు తగ్గింపు - 80% ధర తగ్గింపు
- తక్కువ లేటెన్సీ - మిస్ట్రాల్ LLMలతో పోల్చితే వేగవంతమైన స్పందన
- సౌలభ్యం - తక్కువ వనరులు అవసరమైన విభిన్న వాతావరణాలలో విస్తరణ సాధ్యం

మిస్ట్రాల్ స్మాల్ కోసం మంచి యాప్‌లు:
- సారాంశం, భావ విశ్లేషణ, అనువాదం వంటివి వంటి పాఠ్య ఆధారిత పనులు.
- అధిక తరచుదీసే అభ్యర్థనల అవసరమున్న అప్లికేషన్లు, దాని తక్కువ ధర కారణంగా
- సమీక్ష మరియు కోడ్ సూచనల వంటి తక్కువ లేటెన్సీ కోడ్ పనులు

## మిస్ట్రాల్ స్మాల్ మరియు మిస్ట్రాల్ లార్జ్ పోలిక

మిస్ట్రాల్ స్మాల్ మరియు లార్జ్ మధ్య లేటెన్సీ తేడాను చూపించడానికి కింది సెల్స్ నడపండి.

ప్రత్యేకించదగ్గ మార్పు 3-5 సెకన్ల మధ్య ఉంటుంది. ఒకే ప్రాంప్ట్‌పై స్పందన పొడవు మరియు శైలి కూడా గమనించండి.

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

ఈ పాఠంలో చర్చించిన రెండు మోడల్స్‌తో పోలిస్తే, మిస్ట్రాల్ నేమో మాత్రమే Apache2 లైసెన్సుతో ఉచిత మోడల్.

ఇది మిస్ట్రాల్ యొక్క మునుపటి ఓపెన్ సొర్సు LLM అయిన మిస్ట్రాల్ 7Bకి అప్గ్రేడ్‌గా భావించబడుతుంది.

నేమో మోడల్ కొన్ని అదనపు లక్షణాలు:

- *మరింత సమర్థవంతమైన టోకెనైజేషన్:* ఈ మోడల్ సాధారణంగా ఉపయోగించే tiktoken‌ కన్నా Tekken tokenizerను ఉపయోగిస్తాయి. ఇది మరిన్ని భాషలతో మరియు కోడ్‌తో మెరుగైన పనితీరును అందిస్తుంది.

- *ఫైనెట్యూనింగ్:* ఆధారమోడల్ ఫైనెట్యూనింగ్ కోసం అందుబాటులో ఉంటుంది. ఇది ఫైనెట్యూనింగ్ అవసరమయ్యే వినియోగ సందర్భాలకు మరింత సౌలభ్యం ఇస్తుంది.

- *నేటివ్ ఫంక్షన్ కాలింగ్* - మిస్ట్రాల్ లార్జ్‌లాగా, ఈ మోడల్ కూడా ఫంక్షన్ కాలింగ్‌పై శిక్షణ పొందింది. ఇది ఓపెన్ సొర్సులో మొదటి మోడల్స్‌లో ఒకటిగా అనన్యంగా చేస్తుంది.

### టోకెనైజర్స్ పోలిక

ఈ ఉదాహరణలో, మేము మిస్ట్రాల్ నేమో మరియు మిస్ట్రాల్ లార్జ్ మెక్కడి టోకెనైజేషన్ ఎలా నిర్వహిస్తుందో చూస్తాము.

రెండు ఉదాహరణలు ఒకే ప్రాంప్ట్ తీసుకుంటాయి కానీ నేమో మిస్ట్రాల్ లార్జ్ కంటే తక్కువ టోకెన్లను రిటర్న్ చేస్తుందని మీరు గమనిస్తారు.

```bash
pip install mistral-common
```

```python 
# కావలసిన ప్యాకేజీలను దిగుమతి చేసుకోండి:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# మిస్ట్రాల్ టోకనైజర్‌ని లోడ్ చేయండి

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

# టోకన్ల సంఖ్యను లెక్కించండి
print(len(tokens))
```

```python
# అవసరమైన ప్యాకేజీలను దిగుమతి చేయండి:
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

## తెలుసుకోవడం ఇక్కడే ఆగదు, ప్రయాణాన్ని కొనసాగించండి

ఈ పాఠం పూర్తయిన తరువాత, మా [సృష్టిశీల AI నేర్చుకునే సేకరణ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)ని పరిశీలించండి మరియు మీ సృష్టిశీల AI జ్ఞానాన్ని మరింత అభివృద్ధి చేసుకోండి!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**స్వీయాంఖ్యానం**:
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నా, ఆటోమేటెడ్ అనువాదాల్లో తప్పిదాలు లేదా అపదాలను కలిగి ఉండవచ్చు అని దయచేసి గమనించండి. స్థానిక భాషలో ఉన్న మౌలిక డాక్యుమెంట్‌ను అధికారిక మూలంగా పరిగణించాలి. ముఖ్య సమాచారం కోసం, వృత్తిపరమైన మానవ అనువాదాన్ని సిఫారసు చెయ్యబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా ভুল అసంకేతాల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->