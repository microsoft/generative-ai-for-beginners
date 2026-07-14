# മിസ്ട്രാൽ മോഡലുകളുമായി നിർമ്മാണം 

## പരിചയം 

ഈ പാഠത്തിൽ ഉൾക്കൊള്ളുന്നത്: 
- വ്യത്യസ്ത മിസ്ട്രാൽ മോഡലുകളുടെ പഠനം 
- ഓരോ മോഡലിന്റെയും ഉപയോഗ കേസുകളും ഘടനകളും മനസിലാക്കൽ 
- ഓരോ മോഡലിന്റെയും പ്രത്യേകതകളെ കാണിക്കുന്ന കോഡ് സാമ്പിളുകൾ പരിശോധിക്കൽ. 

## മിസ്ട്രാൽ മോഡലുകൾ 

ഈ പാഠത്തിൽ നാം 3 വ്യത്യസ്ത മിസ്ട്രാൽ മോഡലുകൾ പരിശോധിക്കും: 
**മിസ്ട്രൽ ലാർജ്**, **മിസ്ട്രൽ സ്മോൾ** , **മിസ്ട്രൽ നീമോ**. 

ഈ മോഡലുകൾ Microsoft Foundry Modelsൽ സൗജന്യമായി ലഭ്യമാണ്. ഈ നോട്ട്‌ബുക്കിലെ കോഡ് ഈ മോഡലുകൾ ഉപയോഗിച്ച് പ്രവർത്തിക്കും.

> **കുറിപ്പ്:** GitHub മോഡലുകൾ ജൂലൈ 2026 അവസാനം വിരമിക്കുന്നു. AI മോഡലുകൾ ഉപയോഗിച്ച് പ്രോട്ടോടൈപ്പിങ് ചെയ്യുന്നതിനുള്ള കൂടുതൽ വിവരങ്ങൾ [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) വഴി ഇതുവരെ ലഭ്യമാണ്. 


## മിസ്ട്രാൽ ലാർജ് 2 (2407)
മിസ്ട്രൽ ലാർജ് 2 ഇപ്പോൾ മിസ്ട്രലിന്റെ ഫ്ലാഗ്ഷിപ്പ് മോഡലായും എന്റർപ്രൈസ് ഉപയോഗത്തിന് രൂപകൽപ്പന ചെയ്തതുമാണ്. 

ഈ മോഡൽ പ്ര(original) മിസ്ട്രൽ ലാർജിനേക്കാൾ അപ്‌ഗ്രേഡ് ചെയ്തത് ആണ്, നൽകുന്നത് 
-  കൂടുതൽ വലുപ്പത്തിലുള്ള കോൺടെക്സ്റ്റ് വിൻഡോ - 128k ൽ 32k എന്നത്  
-  ഗണിതവും കോഡിങ്ങ് ആവശ്യകതകളിലും മെച്ചപ്പെട്ട പ്രകടനം - ശരാശരി കൃത്യത 76.9% ബദൽ 60.4%  
-  വർധിച്ച ബഹുഭാഷ പ്രകടനം - ഇംഗ്ലീഷ്, ഫ്രഞ്ച്, ജർമ്മൻ, സ്പാനിഷ്, ഇറ്റേലിയൻ, പോർച്ചുഗീസ്, ഡച്ച്, റഷ്യൻ, ചൈനീസ്, ജാപ്പനീസ്, കൊറിയൻ, അറബി, ഹിന്ദി ഭാഷകൾ ഉൾപ്പെടെ. 

ഈ സവിശേഷതകളോടെ മിസ്ട്രൽ ലാർജ് മികച്ചതാണ്: 
- *രിഇട്രീവൽ ഓഗ്മെന്റഡ് ജനറേഷൻ (RAG)* - വലുതായ കോൺടെക്സ്റ്റ് വിൻഡോ മൂലം 
- *ഫംഗ്ഷൻ കോളിങ്* - ഈ മോഡലിന് സ്വാഭാവിക ഫംഗ്ഷൻ കോളിങ് ഉണ്ട്, ഇത് ബാഹ്യ ഉപകരണങ്ങളുമായി APIകളും സംയോജിപ്പിക്കാനുള്ള അവസരം നൽകുന്നു. ഈ കോളുകൾ പരസ്പരം സമാന്തരമായി അല്ലെങ്കിൽ ക്രമത്തിൽ നടത്താം.
- *കോഡ് ജനറേഷൻ* - ഈ മോഡൽ പൈത്തൺ, ജാവ, ടൈപ്പ്സ്ക്രിപ്റ്റ്, സി++ ജനറേഷനിൽ മികച്ചതാണ്. 

### മിസ്ട്രൽ ലാർജ് 2 ഉപയോഗിച്ച് RAG ഉദാഹരണം 

ഈ ഉദാഹരണത്തിൽ, മിസ്ട്രൽ ലാർജ് 2 ഉപയോഗിച്ച് ഒരു ടെക്സ്റ്റ് ഡോക്കുമെന്റിന്റെ മേൽ RAG പാറ്റേൺ ഓടിക്കുന്നു. ചോദ്യം കൊറിയൻ ഭാഷയിൽ എഴുതപ്പെട്ടിരിക്കുന്നു, കോളേജ് മുമ്പുള്ള എഴുത്തുകാരന്റെ പ്രവർത്തനങ്ങളെക്കുറിച്ചാണ്. 

ഇത് ടെക്സ്റ്റ് ഡോക്യുമെന്റിന്റെ കൂടാതെ ചോദ്യത്തിന്റെ എൻബെഡിംഗ് സൃഷ്ടിക്കാൻ Cohere Embeddings മോഡൽ ഉപയോഗിക്കുന്നു. ഈ സാമ്പിളിനായി faiss പൈത്തൺ പാക്കേജ് വെക്റ്റർ സ്റ്റോർ ആയി ഉപയോഗിക്കുന്നു. 

മോഡലിലേക്ക് അയക്കുന്ന പ്രോംപ്റ്റിൽ ചോദ്യങ്ങളുടെയും ചോദ്യത്തിന് സമാനമായ തിരികെ കണ്ടെത്തിയ ഭാഗങ്ങളുടെയും ഉൾപ്പെടുന്നു. മോഡൽ തുടർന്ന് സ്വാഭാവിക ഭാഷാ പ്രതികരണം നൽകുന്നു. 

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

# നിങ്ങളുടെ Microsoft Foundry പ്രോജക്ടിന്റെ "ഓവerview" പേജിൽ നിന്നും ഇത് ലഭിക്കുക
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # ദൂരം, സൂചിക
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

## മിസ്ട്രൽ സ്മോൾ 
മിസ്ട്രൽ സ്മോൾ മിസ്ട്രാൽ സീരീസിലെ മറ്റൊരു മോഡലാണ്, പ്രീമിയർ/എന്റർപ്രൈസ് വിഭാഗത്തിൽ വരുന്നത്. പേര് സൂചിപ്പിക്കുന്നത് പോലെ, ഇത് ഒരു ചെറു ഭാഷാ മോഡലാണ് (SLM). മിസ്ട്രൽ സ്മോൾ ഉപയോഗിക്കുന്ന പ്രധാന നേട്ടങ്ങൾ: 
- മിസ്ട്രൽ ലാർജ്, നീമോ പോലുള്ള വലിയ മോഡലുകളേക്കാൾ ചെലവ് ലാഭം - 80% വിലക്കുറവ് 
- കുറഞ്ഞ വൈകിപ്പ് - മിസ്ട്രൽ LLM കൾക്കാൾ വേഗത്തിലുള്ള പ്രതികരണം 
- റിസോഴ്സുകൾ കുറവോടെ വ്യത്യസ്ത പരിസരങ്ങളിൽ വിന്യസിക്കാൻ കഴിയും - കൂടുതൽ ലവചിതം 


മിസ്ട്രൽ സ്മോൾ നല്ലതാണ്: 
- സംഗ്രഹം, വികാര വിശകലനം, പരിഭാഷ തുടങ്ങിയ ടെക്സ്റ്റ് അടിസ്ഥാന പ്രവർത്തനങ്ങൾക്ക് 
- ചെലവ് കാര്യക്ഷമത കാരണം ആവർത്തിച്ച് അഭ്യർത്ഥനകൾ ഉണ്ടാകുന്ന പ്രയോഗങ്ങൾക്കു 
- കുറഞ്ഞ വൈകിപ്പുള്ള കോഡ് സംബന്ധിച്ച പ്രവർത്തനങ്ങൾ, റിവ്യൂ, നിർദ്ദേശങ്ങൾ. 

## മിസ്ട്രൽ സ്മോൾ ഉം മിസ്ട്രൽ ലാർജ് ഉം തമ്മിലുള്ള താരതമ്യം 

മിസ്ട്രൽ സ്മോൾ ഉം ലാർജ് ഉം തമ്മിലുള്ള വൈകിപ്പ് വ്യത്യാസം കാണിക്കാൻ താഴെയുള്ള സെല്ലുകൾ പ്രവർത്തിപ്പിക്കുക. 

പ്രതികരണ സമയങ്ങളിൽ 3-5 സെക്കൻഡിന്റെ വ്യത്യാസം നിങ്ങൾക്ക് കാണാം. ഒരേ പ്രോംപ്റ്റിൽ പ്രതികരണത്തിന്റെ നീളവും ശൈലിയും ശ്രദ്ധിക്കുക.  

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

## മിസ്ട്രൽ നീമോ

ഈ പാഠത്തിൽ ചർച്ച ചെയ്ത മറ്റു രണ്ട് മോഡലുകളെയും താരതമ്യപ്പെടുത്തുമ്പോൾ, മിസ്ട്രൽ നീമോ മാത്രമേ ആപ്പാച്ചെ 2 ലൈസൻസോടെ സൗജന്യ മോഡൽ ആയിരിക്കൂ. 

മിസ്ട്രൽ നീമോ, മിസ്ട്രലിന്റെ പ്രാഥമിക ഓപ്പൺ സോഴ്‌സ് LLM ആയ മിസ്ട്രൽ 7B ന്റെ അപ്‌ഗ്രേഡായി കണക്കാക്കപ്പെടുന്നു. 

നീമോ മോഡലിന്റെ മറ്റ് ചില സവിശേഷതകൾ: 

- *കൂടുതൽ കാര്യക്ഷമമായ ടോക്കൻവലൈസേഷൻ:* ഈ മോഡൽ സാധാരണയായി ഉപയോഗിക്കുന്ന tiktoken ന് പകരം Tekken tokenizer استعمالിക്കുന്നു. ഇതിലൂടെ കൂടുതൽ ഭാഷകൾക്കും കോഡിനും പെരുമാറ്റം മെച്ചപ്പെട്ടിരിക്കുന്നു. 

- *ഫിൻട്യൂണിംഗ്:* അടിസ്ഥാന മോഡൽ ഫിൻട്യൂണിംഗിനായി ലഭ്യമാണ്. ഇത് ഫിൻട്യൂണിംഗ് ആവശ്യമുള്ള ഉപയോഗ കേസുകൾക്കായി കൂടുതൽ സൗകര്യപ്രദമാക്കുന്നു. 

- *സ്വാഭാവിക ഫംഗ്ഷൻ കോളിങ്* - മിസ്ട്രൽ ലാർജിൽപോലെ, ഈ മോഡലും ഫംഗ്ഷൻ കോളിങിൽ പരിശീലനം ലഭിച്ചിട്ടുണ്ട്. ഇത് ആദ്യ ഓപ്പൺ സോഴ്‌സ് മോഡലുകളിൽ ഒന്ന് ആക്കുന്നു. 


### ടോക്കൻ വലൈസർമാരുടെ താരതമ്യം 

ഈ ഉദാഹരണത്തിൽ, മിസ്ട്രൽ നീമോ ടോക്കൻവലൈസേഷൻ മിസ്ട്രൽ ലാർജുമായി താരതമ്യം ചെയ്യാം. 

രണ്ട് സാമ്പിളുകളും ഒരേ പ്രോംപ്റ്റ് സ്വീಕರിക്കുന്നു, എന്നാൽ നീമോ മിസ്ട്രൽ ലാർജിനേക്കാൾ കുറവുള്ള ടോക്കണുകൾ തിരിച്ചു നൽകുമെന്ന് കാണണം. 

```bash
pip install mistral-common
```

```python 
# ആവശ്യമുള്ള പാക്കേജുകൾ ഇറക്കുമതി ചെയ്യുക:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# മിസ്‌ട്രാൾ ടോക്കനൈസർ ലോഡ് ചെയ്യുക

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# സന്ദേശങ്ങളുടെ പട്ടിക ടോക്കനൈസ് ചെയ്യുക
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

# ടോക്കൺകളുടെ എണ്ണം എണ്ണുക
print(len(tokens))
```

```python
# ആവശ്യമായ പാക്കേജ്‌സ് ഇറക്കുമതി ചെയ്യുക:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral ടോക്കിനൈസർ ലോഡ് ചെയ്യുക

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# സന്ദേശങ്ങളുടെ ലിസ്റ്റ് ടോക്കിനൈസ് ചെയ്യുക
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

# ടോക്കൺകളുടെ എണ്ണം എണ്ണുക
print(len(tokens))
```

## പഠനം ഇവിടെ അവസാനിക്കുക അല്ല, യാത്ര തുടരുക

ഈ പാഠം പൂർത്തിയാക്കിയതിന് ശേഷം, [ജനറേറ്റീവ് AI ലേണിംഗ് ശേഖരം](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) സന്ദർശിച്ചു നിങ്ങളുടെ ജനറേറ്റീവ് AI അറിവ് കൂടുതൽ ഉയർത്തുക!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->