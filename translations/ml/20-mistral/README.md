# മിസ്റ്റ്രൽ മോഡലുകളുമായി കെട്ടിപ്പടുക്കുന്നത്

## പരിചയം

ഈ പാഠത്തിൽ ചർച്ചചെയ്യുന്നത്:  
- വ്യത്യസ്ത മിസ്റ്റ്രൽ മോഡലുകളുടെ അന്വേഷണം  
- ഓരോ മോഡലിന്റെയും ഉപയോഗങ്ങൾക്കും സാഹചര്യങ്ങൾക്കും മനസിലാക്കൽ  
- ഓരോ മോഡലിന്റെയും പ്രത്യേകതകൾ കാണിക്കുന്ന കോഡ് സാമ്പിളുകൾ പരിശോധിക്കൽ.

## മിസ്റ്റ്രൽ മോഡലുകൾ

ഈ പാഠത്തിൽ, നാം 3 വ്യത്യസ്ത മിസ്റ്റ്രൽ മോഡലുകൾ അന്വേഷിക്കും:  
**മിസ്റ്റ്രൽ ലാർജ്**, **മിസ്റ്റ്രൽ സ്മാൾ** എന്നിവയും **മിസ്റ്റ്രൽ നെയ്മോ**യും.

ഈ മോഡലുകൾ എല്ലാം GitHub മോഡൽ വിപണിയിൽ സൗജന്യമായാണ് ലഭ്യമാകുന്നത്. ഈ നോട്ട്‌ബുക്കിലുള്ള കോഡ് ഈ മോഡലുകളെ ഉപയോഗിച്ച് പ്രവർത്തിപ്പിക്കും. GitHub മോഡലുകൾ ഉപയോഗിച്ച് [AI മോഡലുകളുമായി പ്രോട്ടോടൈപ്പിംഗ്](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) ചെയ്യുന്നതിനെ കുറിച്ച് കൂടുതൽ വിവരങ്ങൾ ചുവടെ കാണാം.

## മിസ്റ്റ്രൽ ലാർജ് 2 (2407)
മിസ്റ്റ്രൽ ലാർജ് 2 ഇപ്പോഴത്തെ മിസ്റ്റ്രലിന്റെ ഫ്ലാഗ്ഷിപ്പ് മോഡലാണ്, സംസ്ഥാപന ഉപയോഗത്തിനായി രൂപകൽപ്പന ചെയ്‌തിരിക്കുന്നു.

ഈ മോഡൽ യഥാർത്ഥ മിസ്റ്റ്രൽ ലാർജിനെ അപ്‌ഗ്രേഡ് ചെയ്തതാണ്, ഇതിൽ ഉൾപ്പെടുന്നത്:  
- വലുതായ കോൺടെക്‌സ്‌റ്റ് വിൻഡോ - 128k vs 32k  
- ഗണിതം, കോഡിംഗ് ടാസ്കുകളിൽ മികച്ച പ്രകടനം - ശരാശരി കൃത്യത 76.9% vs 60.4%  
- വർദ്ധിച്ചുള്ള ബഹുഭാഷ നിർവഹണം - ഇംഗ്ലീഷ്, ഫ്രഞ്ച്, ജർമ്മൻ, സ്‌പാനിഷ്, ഇറ്റാലിയൻ, പോർച്ചുഗീസ്, ഡച്ച്, റഷ്യൻ, ചൈനീസ്, ജാപ്പനീസ്, കൊറിയൻ, അറബിക്, ഹിന്ദി എന്നിവ ഉൾപ്പെടുന്നു.

ഈ സവിശേഷതകളോടെ, മിസ്റ്റ്രൽ ലാർജ് മികച്ചവയാണ്:  
- *റിട്രീവൽ ഓഗ്മെന്റഡ് ജനറേഷൻ (RAG)* - വലുതായ കോൺടെക്‌സ്‌റ്റ് വിൻഡോയ്ക്ക് സമർപ്പിച്ച്  
- *ഫങ്ഷൻ കോൾ ചെയ്യൽ* - ഈ മോഡലിൽ നേറ്റീവ് ഫങ്ഷൻ കോൾ ചെയ്യൽ ഉൾപ്പെടുത്തിയിരിക്കുന്നു, ഇത് ബാഹ്യ ടൂളുകൾക്കും API കളിലും ഇന്റഗ്രേഷനും സാധ്യമാക്കുന്നു. ഫങ്ഷൻ കോൾപ്പുകൾ സമാന്തരമോ അല്ലെങ്കിൽ അനുഭവക്രമത്തിൽ ഒന്ന് ശേഷം ഒന്ന് നടത്താം.  
- *കോഡ് ജനറേഷൻ* - പൈതൺ, ജാവ, ടൈപ്പ്സ്ക്രിപ്റ്റ്, C++ എന്നിവയിൽ ഈ മോഡൽ മികച്ചതാണ്.

### മിസ്റ്റ്രൽ ലാർജ് 2 ഉപയോഗിച്ച RAG ഉദാഹരണം

ഈ ഉദാഹരണത്തിൽ, മിസ്റ്റ്രൽ ലാർജ് 2 ഉപയോഗിച്ച് ഒരു ടെക്സ്റ്റ് ഡോക്യുമെന്റിൽ RAG പാറ്റേൺ പ്രവർത്തിപ്പിക്കുന്നു. ചോദ്യം കൊറിയൻ ഭാഷയിൽ എഴുതിയതാണ്, കോളേജ് മുൻപ് എഴുത്തുകാരന്റെ പ്രവർത്തനങ്ങളെക്കുറിച്ച് ചോദിക്കുന്നു.

ഇത് കോഹീർ എംബെഡിങ്ങ് മോഡൽ ഉപയോഗിച്ച് ടെക്സ്റ്റ് ഡോക്യുമെന്റിനും ചോദ്യത്തിനുമുള്ള എംബെഡിങ്ങുകൾ സൃഷ്‌ടിക്കുന്നു. ഈ സാമ്പിളിന് ഫയ്സ് പൈതൺ പാക്കേജ് വക്ടർ സ്റ്റോർ ആയി ഉപയോഗിക്കുന്നു.

മിസ്റ്റ്രൽ മോഡലിലേക്ക് അയയ്ക്കുന്ന പ്രോംപ്റ്റിൽ ചോദ്യവും ചോദ്യത്തോട് സമാനമായ തിരിച്ചുകിട്ടിയ ഭാഗങ്ങളും ഉൾപ്പെടുന്നു. മോഡൽ സ്വാഭാവിക ഭാഷാ പ്രതികരണം നൽകുന്നു.

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
  
## മിസ്റ്റ്രൽ സ്മാൾ  
മിസ്റ്റ്രൽ സ്മാൾ മിസ്റ്റ്രൽ കുടുംബത്തിലെ മറ്റൊരു മോഡൽ ആണ്, പ്രധാനമായും പ്രീമിയർ/സ്ഥാപന വിഭാഗത്തിൽ പെടുന്നത്. പേരിൽപോലെ, ഇത് ഒരു ചെറിയ ഭാഷ മോഡൽ (SLM) ആണ്. മിസ്റ്റ്രൽ സ്മാൾ ഉപയോഗിക്കുന്നതിന്റെ നേട്ടങ്ങൾ:  
- മിസ്റ്റ്രൽ LLMs പോലുള്ള മിസ്റ്റ്രൽ ലാർജിനും നെയ്മോക്കും შედിയിച്ച് ചെലവ് ലാഭം - 80% വില കുറവ്  
- കുറഞ്ഞ ലാറ്റൻസി - മിസ്റ്റ്രൽ LLMs നെപോലെ വേഗത്തിലുള്ള പ്രതികരണം  
- വൈവിധ്യമാർന്ന പരിസ്ഥിതികളിൽ കുറവ് വനംമാനദണ്ഡങ്ങളോടെ വിന്യസിക്കാനുള്ള സൗകര്യം.

മിസ്റ്റ്രൽ സ്മാൾ മികച്ചതാണ്:  
- ടെക്സ്റ്റ് അടിസ്ഥാനത്തിലുള്ള ടാസ്കുകൾ, ഉദാഹരണത്തിന് സംഗ്രഹം, സ്നേഹം വിശകലനം, പരിഭാഷ  
- കുറവായ ചെലവുമായി അനുബന്ധ സമ്പ്രേഷണങ്ങൾ ആവർത്തിക്കുകയും ചെയ്യുന്ന അപേക്ഷകൾ  
- കോഡ്ജോലികൾ പോലുള്ള കുറഞ്ഞ പ്രാതികമായ കോഡ് ടാസ്കുകൾ

## മിസ്റ്റ്രൽ സ്മാൾ, മിസ്റ്റ്രൽ ലാർജ് താരതമ്യം

മിസ്റ്റ്രൽ സ്മാൾ, ലാർജ് മോഡലുകൾക്കിടയിലെ ലാറ്റൻസി വ്യത്യാസം കാണാൻ താഴെയുള്ള സെല്ലുകൾ പ്രവർത്തിപ്പിക്കുക.

3-5 സെക്കൻഡ് പ്രതിരോധ വ്യത്യാസം കാണാം. അതുപോലെ, ഒരേ പ്രോംപ്റ്റ്ക് പ്രതികരണങ്ങളുടെ നീളം, ശൈലിയും ശ്രദ്ധിക്കുക.

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
  
## മിസ്റ്റ്രൽ നെയ്മോ

ഈ പാഠത്തിൽ ചർച്ചചെയ്ത മറ്റ് രണ്ട് മോഡലുകളുമായി താരതമ്യപ്പെടുത്തുമ്പോൾ, മിസ്റ്റ്രൽ നെയ്മോ മാത്രമേ ആപാച്ചി 2 ലൈസൻസ് ഉള്ള സൗജന്യ മോഡൽ ആയിരിക്കൂ.

ഇത് മുമ്പളുടെ മിസ്റ്റ്രൽ 7B എന്ന ഓപ്പൺ സോഴ്‌സ് LLM നെ അപ്‌ഗ്രേഡ് ചെയ്ത മോഡലായി കാണപ്പെടുന്നു.

നെയ്മോ മോഡലിന്റെ മറ്റ് ചില സവിശേഷതകൾ:  
- *കമ്പാക്ട് ടോക്കനൈസേഷൻ:* ഈ മോഡൽ tiktoken നും ബജറ്റ് കൂട്ടിലുള്ള ടെക്കൻ ടോക്കനൈസർ ഉപയോഗിക്കുന്നു. ഇതിലൂടെ കൂടുതൽ ഭാഷകളിലും കോഡിലും മെച്ചപ്പെട്ട പ്രകടനം ലഭ്യമാണ്.  
- *ഫൈന്ട്യൂൺ:* അടിസ്ഥാന മോഡൽ ഫൈന്ട്യൂണിംഗിന് ലഭ്യമാണ്. ഇത് തുടർച്ചയായ ആവശ്യകതകൾക്കായി കൂടുതൽ പ്രാപ്തിയും നിരവധി ഉപയോഗ സാഹചര്യങ്ങൾക്ക് സൗകര്യവും നൽകുന്നു.  
- *നെറ്റീവ് ഫങ്ഷൻ കോൾ:* മിസ്റ്റ്രൽ ലാർജിനെപ്പോലെ ഈ മോഡലും ഫങ്ഷൻ കോൾ പരിശീലനം ലഭിച്ചു. ഇത് തുറന്ന സ്രോതസ് മോഡലുകളിൽ ആദ്യങ്ങളിൽ ഒരുപടിയായ പ്രായോഗികമായ സവിശേഷതയാണ്.

### ടോക്കനൈസേഴ്സ് താരതമ്യം

ഈ സാമ്പിളിൽ, മിസ്റ്റ്രൽ നെയ്മോ മിസ്റ്റ്രൽ ലാർജുമായി ടോക്കനൈസേഷൻ എങ്ങനെ കൈകാര്യം ചെയ്യുന്നു എന്ന് കാണാം.

രണ്ട് സാമ്പിളുകളും ഒരേ പ്രോംപ്റ്റ് സ്വീകരിക്കുന്നു, എന്നാൽ നെയ്മോ മിസ്റ്റ്രൽ ലാർജിനേക്കാൾ കുറവ് ടോക്കനുകൾ തിരികെ നൽകുന്നത് കാണാം.

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

# മിസ്ട്രൽ ടോക്കനൈസർ ലോഡ് ചെയ്യുക

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

# മിസ്ട്രാൽ ടോക്കണൈസർ ലോഡ് ചെയ്യുക

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# സന്ദേശങ്ങളുടെ പട്ടിക ടോക്കണൈസ് ചെയ്യുക
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

# ടോക്കണുകളുടെ എണ്ണം എണ്ണം ചെയ്യുക
print(len(tokens))
```
  
## പഠനം ഇവിടെ അവസാനിക്കാപ്പോ, യാത്ര തുടർക്കൂ

ഈ പാഠം പൂര്‍ത്തിയാക്കിയതിന് ശേഷം, ഞങ്ങളുടെ [ജനറേറ്റീവ് AI പഠന ശേഖരം](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) പരിശോധിച്ച് നിങ്ങളുടെ ജനറേറ്റീവ് AI അറിവ് മെച്ചപ്പെടുത്തുക!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസംബന്ധിതശേഷിയ്ക്ക്**:  
ഈ പ്രമാണം [Co-op Translator](https://github.com/Azure/co-op-translator) എന്ന എഐ പരിഭാഷാ സേവനം ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. നമുക്കു nauwത്വത്തിനായി ശ്രമിക്കുന്നത് അതാണ്, എന്നിരുന്നാലും സ്വയംചാലിതമായ പരിഭാഷകൾ പിഴവുകളും അശുദ്ധികളും ഉൾക്കൊള്ളാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. പ്രമാണത്തിന്റെ മാതൃഭാഷയിലുള്ള ആധാരപ്രമാണം മാത്രമേ അദ്ധ്യക്ഷമായ ഉറവിടം ആയിരിക്കു്. നിർണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശിപാർശ ചെയ്യപ്പെടുന്നു. ഈ പരിഭാഷ ഉപയോഗിക്കുന്നതിനാൽ ഉണ്ടാകാവുന്ന ഏത് തർജ്ജമയില്ലാത്തതോ തെറ്റിദ്ധാരണയിലായതോ സംഭവങ്ങൾക്ക് ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->