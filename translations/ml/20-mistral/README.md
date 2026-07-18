# മിസ്‌ട്രൽ മോഡലുകളുമായി നിർമ്മിക്കുന്നു

## പരിചയം

ഈ പാഠത്തിൽ ഉൾപ്പെടുന്നു:
- വിവിധ മിസ്‌ട്രൽ മോഡലുകൾ അന്വേഷിക്കുക
- ഓരോ മോഡലിന്റെയും ഉപയോഗകേസുകളും സാഹചര്യങ്ങളും മനസിലാക്കുക
- ഓരോ മോഡലിന്റെയും വ്യത്യസ്ത ഫീച്ചറുകൾ കാണിക്കുന്ന കോഡ് കാരാനാംശങ്ങൾ പരിശോധിക്കുക.

## മിസ്‌ട്രൽ മോഡലുകൾ

ഈ പാഠത്തിൽ, നാം 3 വിവിധ മിസ്‌ട്രൽ മോഡലുകൾ പരിചയപ്പെടുന്നു:
**മിസ്‌ട്രൽ ലാർജ്**, **മിസ്‌ട്രൽ സ്മോൾ**, **മിസ്‌ട്രൽ നീമോ**.

ఈ മോഡലുകളിൽ ഓരോന്നും [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ല്‍ സൗജന്യമായും ലഭ്യമാണ്. ഈ നോട്ട്ബുക്കിലെ കോഡ് ഈ മോഡലുകൾ ഉപയോഗിച്ച് പ്രവർത്തിക്കും.

> **കുറിപ്പ്:** GitHub മോഡലുകൾ 2026 ജൂലൈ അവസാനം റിട്ടയർ ചെയ്യുന്നു. [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ഉപയോഗിച്ച് AI മോഡലുകൾ പ്രോട്ടോടൈപ്പ് ചെയ്യാനുള്ള കൂടുതൽ വിവരങ്ങൾ ഇവിടെ.


## മിസ്‌ട്രൽ ലാർജ് 2 (2407)
മിസ്‌ട്രൽ ലാർജ് 2 നിലവിൽ മിസ്‌ട്രൽ സംരംഭത്തിലെ ഫ്ളാഗ്ഷിപ്പ് മോഡലാണ്, സംരംഭ ഉപയോഗത്തിനായി രൂപകല്‍പ്പന ചെയ്തിരിക്കുന്നു.

ഈ മോഡൽ ലഭ്യമാക്കുന്നതിലെ അപ്‌ഗ്രേഡുകൾ:
- വലുതായ കോൺടക്‌സ്‌റ്റ് വിൻഡോ - 128k വർക്കൊപ്പം 32k
- ഗണിതവും കോഡിങ്ങും ജോലികളിൽ മെച്ചപ്പെട്ട പ്രകടനം - ശരാശരി കൃത്യത 76.9% വർക്കൊപ്പം 60.4%
- വർദ്ധിച്ച മൾട്ടിലിംഗ്വൽ പ്രകടനം - ഭാഷകൾ: ഇംഗ്ലീഷ്, ഫ്രഞ്ച്, ജർമ്മൻ, സ്‌പാനിഷ്, ഇറ്റാലിയൻ, പോർച്ചുഗീസ്, ഡച്ച്, റഷ്യൻ, ചൈനീസ്, ജാപ്പനീസ്, കൊറിയൻ, അറബിക്, ഹിന്ദി.

ഈ ഫീച്ചറുകളുടെ സഹായത്തോടെ മിസ്‌ട്രൽ ലാർജ് മികച്ച ഉൽപ്പന്നങ്ങൾക്കായി:
- *രീറ്റ്രീവൽ ഓഗ്മെന്റഡ് ജനറേഷൻ (RAG)* - വലുതായ കോൺടക്‌സ്‌റ്റ് വിൻഡോ കാരണം
- *ഫംക്ഷൻ കോൾ* - ഈ മോഡലിന് നറേറ്റീവ് ഫംക്ഷൻ കോൾ കഴിവുണ്ട്, ഇത് ബാഹ്യ ടൂളുകളുമായി ഇന്റഗ്രേഷൻ അനുവദിക്കുന്നു. ഈ കോൾകൾ ഒരേസമയം അല്ലെങ്കിൽ പരമ്പരയായി നടത്താം.
- *കോഡ് ജനറേഷൻ* - പൈത്തൺ, ജാവ, ടൈപ്പ്‌സ്‌ക്രിപ്റ്റ്, C++ കോഡ് ജനറേഷൻ ഈ മോഡലിൽ അത്യുത്തമമാണ്.

### മിസ്‌ട്രൽ ലാർജ് 2 ഉപയോഗിച്ചുള്ള RAG ഉദാഹരണം

ഈ ഉദാഹരണത്തിൽ, നാം മിസ്‌ട്രൽ ലാർജ് 2 ഉപയോഗിച്ച് ഒരു ടെക്സ്റ്റ് ഡോക്യുമെന്റിന് മേൽ RAG മാതൃക പ്രവർത്തിപ്പിക്കുന്നു. ചോദ്യങ്ങൾ കൊറിയൻ ഭാഷയിൽ എഴുതപ്പെട്ടവയാണ്, കോളേജ് മുമ്പുള്ള എഴുത്തുകാരന്റെ പ്രവർത്തനങ്ങളെക്കുറിച്ചാണ് ചോദിക്കുന്നത്.

ടെക്സ്റ്റ് ഡോക്യുമെന്റിന്റെയും ചോദ്യത്തിന്റെയും എംബെഡിംഗുകൾ സൃഷ്‌ടിക്കാൻ കോഹിയർ എംബെഡിംഗ്സ് മോഡൽ ഉപയോഗിക്കുന്നു. ഈ സാമ്പിളിൽ ഫെയ്‌സ്സ് പൈത്തൺ പാക്കേജ് വെക്ടർ സ്റ്റോർ ആയി ഉപയോഗിക്കുന്നു.

മിസ്‌ട്രൽ മോഡലിന് അയക്കുന്ന പ്രോംപ്റ്റിൽ ചോദ്യങ്ങൾക്കും അവയ്ക്ക് സമാനമായ തിരിച്ചറിയപ്പെട്ട ഭാഗങ്ങളും ഉൾപ്പെടുന്നു. മോഡൽ പിന്നീട് സ്വാഭാവിക ഭാഷ പ്രതികരണം നൽകും.

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

# ഇത് നിങ്ങളുടെ Microsoft Foundry പ്രോജക്റ്റിന്റെ "അവലോകനം" പേജിൽ നിന്നും എടുത്തു.
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # ദൂരവും, സൂചികയും
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

## മിസ്‌ട്രൽ സ്മോൾ
മിസ്‌ട്രൽ സ്മോൾ, മിസ്‌ട്രൽ‌ പരിവാരത്തിലെ മറ്റൊരു പ്രീമിയർ/എന്റർപ്രൈസ് സ്റ്റാറ്റസിലുള്ള മോഡലാണ്. പേര് സൂചിപ്പിക്കുന്ന പോലെ, ഇത് ഒരു ചെറിയ ഭാഷാ മോഡലാണ് (SLM). മിസ്‌ട്രൽ സ്മോൾ ഉപയോഗിക്കുന്നതിന്റെ ആനുകൂല്യങ്ങൾ:
- മിസ്‌ട്രൽ ലാർജ്, നീമോ പോലുള്ള LLM-കളെ അപേക്ഷിച്ച് ചെലവ് ലാഭം - 80% വില താഴ്ച്ച
- കുറഞ്ഞ ലാറ്റൻസി - മിസ്‌ട്രൽ LLM-കളെക്കാൾ വേഗതയാർന്ന പ്രതികരണം
- കൂടുതൽ സാന്ദ്രതയുള്ള - കുറഞ്ഞ കൂടുതൽ റിസോഴ്‌സുകൾ ആവശ്യപ്പെട്ട് വിവിധ പരിസ്ഥിതികളിൽ വിന്യസിക്കാൻ കഴിയും


മിസ്‌ട്രൽ സ്മോൾ അനുയോജ്യമാണ്:
- സംഗ്രഹം, സന്റിമെന്റ് അനാലിസിസ്, ഭാഷാ പരിഭാഷ പോലുള്ള സ്വരൂപ കോണ്ടക്സ് പ്രവർത്തനങ്ങൾക്ക്
- നിരന്തരം അപേക്ഷകൾ വരുമ്പോൾ കുറഞ്ഞ ചെലവ് മൂലം ഉപയോഗിക്കാൻ
- നിരവധി ലാറ്റൻസി ആവശ്യമായ കോഡ് അകലനം, നിരീക്ഷണം, നിർദേശം

## മിസ്‌ട്രൽ സ്മോൾക്കും മിസ്‌ട്രൽ ലാർജിനും ഇടയിലുള്ള താരതമ്യം

മിസ്‌ട്രൽ സ്മോൾക്കും മിസ്‌ട്രൽ ലാർജിനും ഇടയിലുള്ള ലാറ്റൻസി വ്യത്യാസം കാണിക്കാൻ താഴെയുള്ള സെല്ലുകൾ പ്രവർത്തിപ്പിക്കുക.

സമാനമായ പ്രോംപ്റ്റിൽ പ്രതികരണ സമയങ്ങളിൽ 3-5 സെക്കന്റ് വ്യത്യാസം കാണാം. കൂടാതെ പ്രതികരണ ദൈർഘ്യവും ശൈലിയും ശ്രദ്ധിക്കുക.

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

## മിസ്‌ട്രൽ നീമോ

ഈ പാഠത്തിൽ വിശദീകരിച്ച മറ്റു രണ്ട് മോഡലുകളെ അപേക്ഷിച്ച്, മിസ്‌ട്രൽ നീമോ അപ്പാചെ2 ലൈസൻസ് ഉള്ള മാത്രമായ സൗജന്യ മോഡലാണ്.

മിസ്‌ട്രൽ നീമോ ആദ്യം പുറത്തുവന്ന മിസ്‌ട്രൽ ഓപ്പൺ സോഴ്സ് LLM ആയ മിസ്‌ട്രൽ 7B ന് ഒരു അപ്‌ഗ്രേഡായി കണക്കാക്കപ്പെടുന്നു.

നീമോ മോഡലിന്റെ മറ്റു ചില ഫീച്ചറുകൾ:

- *കൂടുതൽ കാര്യക്ഷമമായ ടോക്കണൈസേഷൻ:*  ഈ മോഡലിൽ പ്രചാരത്തിലായ ടിക്ടോക്കൻ പോലെ പകരം ടെക്കൻ ടോക്കണൈസർ ഉപയോഗിക്കുന്നു. ഇത് കൂടുതൽ ഭാഷകളും കോഡും മികച്ച പ്രകടനം നൽകാൻ സഹായിക്കുന്നു.

- *ഫൈനിട്യൂണിംഗ്:* അടിസ്ഥാന മോഡൽ ഫൈനിട്യൂണിംഗിന് ലഭ്യമാണ്. ഫൈനിട്യൂണിംഗ് ആവശ്യമായ ഉപയോഗകേസുകളിൽ കൂടുതൽ സൗകര്യം നൽകുന്നു.

- *നറേറ്റീവ് ഫംക്ഷൻ കോൾ* - മിസ്‌ട്രൽ ലാർജിന്റെ പോലെ, ഈ മോഡലും ഫംക്ഷൻ കോൾക്ക് പരിശീലനം നൽകിയിട്ടുണ്ട്. ഇത് ഓപ്പൺ സോഴ്സ് മോഡലുകളിൽ ഒന്നാമത്തെ മോഡലുകളിലൊന്നായി പ്രത്യേകം ശ്രദ്ധിക്കപ്പെടുന്നു.


### ടോക്കണൈസറുകള്ക്ക് ഇടയിലുള്ള താരതമ്യം

ഈ സാമ്പിളിൽ, മിസ്‌ട്രൽ നീമോ മിസ്‌ട്രൽ ലാർജുമായി താരതമ്യം ചെയ്യുമ്പോൾ ടോക്കണൈസിംഗ് എങ്ങനെ കൈകാര്യം ചെയ്യുന്നു എന്നു നോക്കാം.

രണ്ട് സാമ്പിളുകളും ഒരേ പ്രോംപ്റ്റ് സ്വീകരിച്ചാലും നീമോ കുറവ് ടോക്കണുകൾ മിസ്ട്രൽ ലാറ്ജിനെ അപേക്ഷിച്ച് നൽകുന്നു.

```bash
pip install mistral-common
```

```python 
# ആവശ്യമായ പേക്കേജുകൾ ഇറക്കുമതി ചെയ്യുക:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# മിസ്റ്റ്രാൽ ടോക്കനൈസർ ലോഡ് ചെയ്യുക

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# സന്ദേശങ്ങളുടെ പട്ടിക ടോക്കൻ ചെയ്യുക
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

# Mistral ടോക്കൻଇസർ ലോഡ് ചെയ്യുക

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# മെസേജുകളുടെ പട്ടിക ടോക്കന്‍ൈസ് ചെയ്യുക
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

## പഠനം ഇവിടെ അവസാനിക്കാൻ അല്ല, യാത്ര തുടരുമ്

ഈ പാഠം പൂർത്തിയാക്കിയതിനു ശേഷം, ഞങ്ങളുടെ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) കാണുക, നിങ്ങളുടെ ജെനെറേറ്റീവ് AI അറിവു ഉയർത്താൻ തുടരണormalize‍ഡ്!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->