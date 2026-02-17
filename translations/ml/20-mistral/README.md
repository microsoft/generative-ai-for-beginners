# മിസ്ട്രാൽ മോഡലുകളുമായി നിർമ്മാണം

## പരിചയം

ഈ പാഠത്തിൽ ഉൾപ്പെടുന്നത്:  
- വ്യത്യസ്ത മിസ്ട്രാൽ മോഡലുകൾ പരിശോധിക്കൽ  
- ഓരോ മോഡലിന്റെയും ഉപയോഗ കേസുകളും സാഹചര്യങ്ങളും മനസ്സിലാക്കൽ  
- ഓരോ മോഡലിന്റെയും പ്രത്യേകതകൾ കാണിക്കുന്ന കോഡ് സാമ്പിളുകൾ.

## മിസ്ട്രാൽ മോഡലുകൾ

ഈ പാഠത്തിൽ, നാം 3 വ്യത്യസ്ത മിസ്ട്രാൽ മോഡലുകൾ പരിശോധിക്കും:  
**മിസ്ട്രാൽ ലാർജ്**, **മിസ്ട്രാൽ സ്മോൾ** மற்றும் **മിസ്ട്രാൽ നീമോ**.

ഈ മോഡലുകൾ ഓരോന്നും ഗിത്തബ് മോഡൽ മാർക്കറ്റ്പ്ലേസിൽ സൗജന്യമായി ലഭ്യമാണ്. ഈ നോട്ട്‌ബുക്കിലെ കോഡ് ഈ മോഡലുകൾ ഉപയോഗിച്ച് പ്രവർത്തിക്കും. ഗിത്തബ് മോഡലുകൾ ഉപയോഗിച്ച് [AI മോഡലുകളുമായി പ്രോട്ടോടൈപ്പിംഗ്](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) ചെയ്യുന്നതിനെക്കുറിച്ച് കൂടുതൽ വിവരങ്ങൾ ഇവിടെ ലഭ്യമാണ്.

## മിസ്ട്രാൽ ലാർജ് 2 (2407)  
മിസ്ട്രാൽ ലാർജ് 2 ഇപ്പോൾ മിസ്ട്രാലിന്റെ ഫ്ലാഗ്ഷിപ്പ് മോഡലാണ്, എന്റർപ്രൈസ് ഉപയോഗത്തിനായി രൂപകൽപ്പന ചെയ്തതാണ്.

മൂല മിസ്ട്രാൽ ലാർജിനെ അപ്ഗ്രേഡ് ചെയ്ത മോഡലാണ് ഇത്, താഴെപ്പറയുന്നവ നൽകുന്നു:  
- വലിയ കോൺടെക്സ്റ്റ് വിൻഡോ - 128k vs 32k  
- ഗണിതവും കോഡിങ്ങും സംബന്ധിച്ച ടാസ്കുകളിൽ മെച്ചപ്പെട്ട പ്രകടനം - ശരാശരി കൃത്യത 76.9% vs 60.4%  
- വർദ്ധിച്ച ബഹുഭാഷാ പ്രകടനം - ഇംഗ്ലീഷ്, ഫ്രഞ്ച്, ജർമ്മൻ, സ്പാനിഷ്, ഇറ്റാലിയൻ, പോർച്ചുഗീസ്, ഡച്ച്, റഷ്യൻ, ചൈനീസ്, ജാപ്പനീസ്, കൊറിയൻ, അറബിക്, ഹിന്ദി എന്നിവ ഉൾപ്പെടുന്നു.

ഈ സവിശേഷതകളോടെ, മിസ്ട്രാൽ ലാർജ് മികച്ചത്:  
- *റിട്രീവൽ ഓഗ്മെന്റഡ് ജനറേഷൻ (RAG)* - വലിയ കോൺടെക്സ്റ്റ് വിൻഡോ കാരണം  
- *ഫംഗ്ഷൻ കോളിംഗ്* - ഈ മോഡലിന് നേറ്റീവ് ഫംഗ്ഷൻ കോളിംഗ് ഉണ്ട്, ഇത് ബാഹ്യ ടൂളുകളും API കളുമായി ഇന്റഗ്രേഷൻ അനുവദിക്കുന്നു. കോൾസ് പരലൽ ആയി അല്ലെങ്കിൽ അനുക്രമത്തിൽ നടത്താം.  
- *കോഡ് ജനറേഷൻ* - പൈത്തൺ, ജാവ, ടൈപ്പ്സ്ക്രിപ്റ്റ്, C++ കോഡ് ജനറേഷനിൽ മികച്ച പ്രകടനം.

### മിസ്ട്രാൽ ലാർജ് 2 ഉപയോഗിച്ച് RAG ഉദാഹരണം

ഈ ഉദാഹരണത്തിൽ, മിസ്ട്രാൽ ലാർജ് 2 ഉപയോഗിച്ച് ഒരു ടെക്സ്റ്റ് ഡോക്യുമെന്റിൽ RAG പാറ്റേൺ പ്രവർത്തിപ്പിക്കുന്നു. ചോദ്യം കൊറിയൻ ഭാഷയിൽ എഴുതിയതാണ്, കോളേജിന് മുമ്പ് എഴുത്തുകാരൻ ചെയ്ത പ്രവർത്തനങ്ങളെക്കുറിച്ചാണ്.

ടെക്സ്റ്റ് ഡോക്യുമെന്റിന്റെയും ചോദ്യത്തിന്റെയും എംബെഡിംഗുകൾ സൃഷ്ടിക്കാൻ കോഹിയർ എംബെഡിംഗ്സ് മോഡൽ ഉപയോഗിക്കുന്നു. ഈ സാമ്പിളിൽ, വെക്ടർ സ്റ്റോർ ആയി ഫൈസ് പൈത്തൺ പാക്കേജ് ഉപയോഗിക്കുന്നു.

മിസ്ട്രാൽ മോഡലിലേക്ക് അയക്കുന്ന പ്രോംപ്റ്റിൽ ചോദ്യങ്ങളും ചോദ്യത്തിന് സമാനമായ റിട്രീവുചെയ്ത ഭാഗങ്ങളും ഉൾപ്പെടുന്നു. മോഡൽ പിന്നീട് സ്വാഭാവിക ഭാഷാ പ്രതികരണം നൽകുന്നു.

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
  
## മിസ്ട്രാൽ സ്മോൾ  
മിസ്ട്രാൽ സ്മോൾ മിസ്ട്രാൽ കുടുംബത്തിലെ മറ്റൊരു മോഡലാണ്, പ്രീമിയർ/എന്റർപ്രൈസ് വിഭാഗത്തിൽ. പേരുപോലെ, ഇത് ഒരു സ്മോൾ ലാംഗ്വേജ് മോഡലാണ് (SLM). മിസ്ട്രാൽ സ്മോൾ ഉപയോഗിക്കുന്നതിന്റെ ഗുണങ്ങൾ:  
- മിസ്ട്രാൽ ലാർജ്, നീമോ പോലുള്ള LLM കളെ അപേക്ഷിച്ച് ചെലവ് ലാഭം - 80% വില കുറവ്  
- കുറഞ്ഞ ലാറ്റൻസി - മിസ്ട്രാൽ LLM കളെ അപേക്ഷിച്ച് വേഗത്തിലുള്ള പ്രതികരണം  
- ഫ്ലെക്സിബിൾ - ആവശ്യമായ റിസോഴ്‌സുകളിൽ കുറവ് നിയന്ത്രണങ്ങളോടെ വ്യത്യസ്ത പരിസ്ഥിതികളിൽ വിന്യസിക്കാവുന്നതാണ്.

മിസ്ട്രാൽ സ്മോൾ മികച്ചത്:  
- സംഗ്രഹണം, സന്റിമെന്റ് അനാലിസിസ്, വിവർത്തനം പോലുള്ള ടെക്സ്റ്റ് അടിസ്ഥാനത്തിലുള്ള ടാസ്കുകൾ  
- ചെലവ് കാര്യക്ഷമത കാരണം ആവർത്തിച്ച് അഭ്യർത്ഥനകൾ ഉണ്ടാകുന്ന ആപ്ലിക്കേഷനുകൾ  
- റിവ്യൂ, കോഡ് നിർദ്ദേശങ്ങൾ പോലുള്ള കുറഞ്ഞ ലാറ്റൻസി കോഡ് ടാസ്കുകൾ

## മിസ്ട്രാൽ സ്മോൾ, മിസ്ട്രാൽ ലാർജ് താരതമ്യം

മിസ്ട്രാൽ സ്മോൾ, ലാർജ് എന്നിവിടയിലെ ലാറ്റൻസി വ്യത്യാസം കാണാൻ താഴെ കൊടുത്ത സെല്ലുകൾ പ്രവർത്തിപ്പിക്കുക.

3-5 സെക്കൻഡ് വ്യത്യാസം പ്രതികരണ സമയങ്ങളിൽ കാണാം. ഒരേ പ്രോംപ്റ്റിൽ പ്രതികരണ ദൈർഘ്യവും ശൈലിയും ശ്രദ്ധിക്കുക.

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
  
## മിസ്ട്രാൽ നീമോ

ഈ പാഠത്തിൽ ചർച്ച ചെയ്ത മറ്റൊരു രണ്ട് മോഡലുകളുമായി താരതമ്യപ്പെടുത്തുമ്പോൾ, മിസ്ട്രാൽ നീമോ മാത്രമാണ് ആപാച്ചെ2 ലൈസൻസോടെ സൗജന്യ മോഡൽ.

മിസ്ട്രാലിന്റെ മുൻപ് പുറത്തിറങ്ങിയ ഓപ്പൺ സോഴ്‌സ് LLM ആയ മിസ്ട്രാൽ 7B ന്റെ അപ്ഗ്രേഡായി ഇത് കണക്കാക്കപ്പെടുന്നു.

നീമോ മോഡലിന്റെ മറ്റ് ചില സവിശേഷതകൾ:  

- *കൂടുതൽ കാര്യക്ഷമമായ ടോക്കനൈസേഷൻ:* ഈ മോഡൽ സാധാരണയായി ഉപയോഗിക്കുന്ന ടിക്ടോക്കൺ പകരം ടെക്കൻ ടോക്കനൈസർ ഉപയോഗിക്കുന്നു. ഇത് കൂടുതൽ ഭാഷകളിലും കോഡിലും മെച്ചപ്പെട്ട പ്രകടനം നൽകുന്നു.

- *ഫൈൻട്യൂണിംഗ്:* അടിസ്ഥാന മോഡൽ ഫൈൻട്യൂണിംഗിന് ലഭ്യമാണ്. ഫൈൻട്യൂണിംഗ് ആവശ്യമായ ഉപയോഗ കേസുകൾക്കായി കൂടുതൽ ഫ്ലെക്സിബിലിറ്റി നൽകുന്നു.

- *നേറ്റീവ് ഫംഗ്ഷൻ കോളിംഗ്* - മിസ്ട്രാൽ ലാർജിനുപോലെ, ഈ മോഡലും ഫംഗ്ഷൻ കോളിംഗിൽ പരിശീലനം നേടിയതാണ്. ഇത് ആദ്യത്തെ ഓപ്പൺ സോഴ്‌സ് മോഡലുകളിൽ ഒന്നായി അതിനെ വ്യത്യസ്തമാക്കുന്നു.

### ടോക്കനൈസറുകൾ താരതമ്യം

ഈ സാമ്പിളിൽ, മിസ്ട്രാൽ നീമോ മിസ്ട്രാൽ ലാർജിനോട് താരതമ്യം ചെയ്യുമ്പോൾ ടോക്കനൈസേഷൻ എങ്ങനെ കൈകാര്യം ചെയ്യുന്നു എന്ന് നോക്കാം.

രണ്ടു സാമ്പിളുകളും ഒരേ പ്രോംപ്റ്റ് സ്വീകരിക്കുന്നു, പക്ഷേ നീമോ മിസ്ട്രാൽ ലാർജിനെ അപേക്ഷിച്ച് കുറവ് ടോക്കണുകൾ തിരികെ നൽകും.

```bash
pip install mistral-common
```
  
```python 
# ആവശ്യമായ പാക്കേജുകൾ ഇറക്കുമതി ചെയ്യുക:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral ടോക്കനൈസർ ലോഡ് ചെയ്യുക

model_name = "open-mistral-nemo	"

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

# ടോക്കണുകളുടെ എണ്ണം എണ്ണുക
print(len(tokens))
```
  
```python
# ആവശ്യമായ പാക്കേജുകൾ ഇറക്കുമതി ചെയ്യുക:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral ടോക്കനൈസർ ലോഡ് ചെയ്യുക

model_name = "mistral-large-latest"

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

# ടോക്കണുകളുടെ എണ്ണം എണ്ണുക
print(len(tokens))
```
  
## പഠനം ഇവിടെ അവസാനിക്കുന്നില്ല, യാത്ര തുടരുക

ഈ പാഠം പൂർത്തിയാക്കിയ ശേഷം, നമ്മുടെ [ജനറേറ്റീവ് AI പഠന ശേഖരം](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) പരിശോധിച്ച് നിങ്ങളുടെ ജനറേറ്റീവ് AI അറിവ് ഉയർത്തുക!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖയാണ് പ്രാമാണികമായ ഉറവിടം എന്ന് പരിഗണിക്കേണ്ടതാണ്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->