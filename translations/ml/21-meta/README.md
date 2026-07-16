# മെറ്റാ കുടുംബ മോഡലുകളുമായി നിർമ്മാണം 

## പരിചയം 

ഈ പാഠം ഉൾക്കൊള്ളുന്നതാണ്: 

- രണ്ട് പ്രധാന മെറ്റാ കുടുംബ മോഡലുകൾ - ല്ലാമ 3.1 һәм ല്ലാമ 3.2-നെക്കുറിച്ച് അന്വേഷിക്കുക 
- ഓരോ മോഡലിനും പ്രയോഗങ്ങൾക്കും സാഹചര്യങ്ങൾക്കും മനസിലാക്കുക 
- ഓരോ മോഡലിന്റെയും പ്രത്യേക സവിശേഷതകൾ കാണിക്കാൻ കോഡ് ഉദാഹരണം 


## മെറ്റാ കുടുംബ മോഡലുകൾ 

ഈ പാഠത്തിൽ, നാം മെറ്റാ കുടുംബത്തിൽ നിന്നുള്ള 2 മോഡലുകൾ അല്ലെങ്കിൽ "ല്ലാമ ഹേര്‍ഡ്" - ല്ലാമ 3.1 և ല്ലാമ 3.2 പരിശോധിക്കും.

ഈ മോഡലുകൾ വ്യത്യസ്ത വകഭേദങ്ങളിൽ ലഭ്യമാണ്, കൂടാതെ [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ൽ ലഭ്യമാണ്.

> **ഗమనിക്കുക:** GitHub Models 2026 ജൂലൈ അവസാനം വിരമിക്കുന്നു. AI മോഡലുകളുമായി പ്രോട്ടോട്ടൈപ്പ് ചെയ്യുന്നതിനായി [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ഉപയോഗിക്കുന്നതിന്റെ കൂടുതൽ വിവരങ്ങൾ ഇവിടെ ലഭ്യമാണ്.

മോഡൽ വകഭേദങ്ങൾ: 
- ല്ലാമ 3.1 - 70B ഇൻസ്ട്രക്റ്റ് 
- ല്ലാമ 3.1 - 405B ഇൻസ്ട്രക്റ്റ് 
- ല്ലാമ 3.2 - 11B വിക്ഷേപ ഇൻസ്ട്രക്റ്റ് 
- ല്ലാമ 3.2 - 90B വിക്ഷേപ ഇൻസ്ട്രക്റ്റ് 

*ഗమనിക്കുക: ല്ലാമ 3 മൈക്രോസോഫ്റ്റ് ഫൗണ്ട്രി മോഡലുകളിലും ലഭ്യമാണ്, എന്നാൽ ഈ പാഠത്തിൽ ഉൾക്കൊള്ളിക്കപ്പെട്ടിട്ടില്ല*

## ല്ലാമ 3.1 

405 ബില്യൺ പാരാമീറ്ററുകളിൽ, ല്ലാമ 3.1 ഓപ്പൺ സോഴ്സ് LLM വിഭാഗത്തിൽപ്പെടുന്നു. 

മോഡൽ മുമ്പത്തെ റിലീസ് ല്ലാമ 3ന് ആപ്‌ഗ്രേഡ് ആയി ഇത് നൽകുന്നു: 

- കൂടുതൽ വലുതായ കോൺടെക്സ്റ്റ് വിൻഡോ - 128k ടോക്കൺകൾ 8k ടോക്കണുകൾക്ക് বদലായി 
- കൂടുതൽ പരമാവധി ഔട്ട്‌പുട്ട് ടോക്കൺ - 4096 2048ന് പകരം 
- മെച്ചപ്പെട്ട ബഹുഭാഷാ പിന്തുണ - പരിശീലന ടോക്കണുകളുടെ വർധനവിന്റെ കാരണം 

ഈ സവിശേഷതകൾ ല്ലാമ 3.1-നെ GenAI ആപ്ലിക്കേഷനുകൾ നിർമ്മിക്കുമ്പോൾ കൂടുതൽ സങ്കീർണ്ണമായ ഉപയോഗ കേസുകൾ കൈകാര്യം ചെയ്യാൻ അനുവദിക്കുന്നു: 
- നാറ്റീവ് ഫംഗ്ഷൻ കോളിംഗ് - LLM പ്രവൃത്തി പ്രക്രിയയ്ക്ക് പുറമെ ബാഹ്യ ടൂളുകളും ഫംഗ്ഷനുകളും വിളിക്കാൻ കഴിവ്
- മെച്ചപ്പെട്ട RAG പ്രകടനം - ഉയർന്ന കോൺടെക്സ്റ്റ് വിൻഡോയുടെ കാരണം 
- സിന്തറ്റിക് ഡേറ്റാ ജനറേഷൻ - ഫൈൻ-ട്യൂണിങ്ങിനുള്ള ഫലപ്രദമായ ഡേറ്റ സൃഷ്ടിക്കാനുള്ള കഴിവ് 

### നാറ്റീവ് ഫംഗ്ഷൻ കോളിംഗ് 

ല്ലാമ 3.1 ഫംഗ്ഷൻ അല്ലെങ്കിൽ ടൂൾ കോളുകൾ കൂടുതൽ ഫലപ്രദമാക്കാൻ ഫൈൻ-ട്യൂൺ ചെയ്തിട്ടുണ്ട്. ഉപയോഗക്കാരന്റെ പ്രാമ്പ്റ്റ് അടിസ്ഥാനമാക്കി മോഡൽ ഉപയോഗിക്കേണ്ട ടൂളുകൾ തിരിച്ചറിയാൻ രണ്ട് നിർമിത ടൂളുകൾ ഉണ്ട്. ഈ ടൂളുകൾ: 

- **ബ്രേവ്സർച്** - വെബ് സേർച്ചിലൂടെ കാലഘട്ട വിവരം പോലുള്ള ആധിക്യവിവരം ലഭിക്കാൻ ഉപയോഗിക്കാവുന്ന ടൂൾ 
- **വോൾഫ്രാം ആൽഫ** - കൂടുതൽ സങ്കീർണ്ണമായ ഗണിതക കണക്കുകൾക്കായി വമ്പൻ, നിങ്ങളുടെ സ്വന്തം ഫംഗ്ഷനുകൾ എഴുതാൻ ആവശ്യമില്ല 

നിങ്ങൾക്ക് നിങ്ങളുടെ സ്വന്തം കസ്റ്റം ടൂളുകളും സൃഷ്ടിക്കാം, LLM ആടെ കോളുകൾക്ക് കഴിയും. 

താഴെ കൊടുത്ത കോഡ് ഉദാഹരണത്തിൽ: 

- സിസ്റ്റം പ്രാമ്പ്റ്റിൽ ലഭ്യമായ ടൂളുകൾ (brave_search, wolfram_alpha) നിർവചിക്കുന്നു. 
- ഒരു പ്രത്യേക നഗരത്തിൽ കാലാവസ്ഥയെക്കുറിച്ച് ചോദിക്കുന്ന ഉപയോക്തൃ പ്രാമ്പ്റ്റ് അയയ്ക്കുന്നു. 
- LLM ബ്രേവ്സർച്ച് ടൂൾ കോളിങ്ങ് ചെയ്യുകയും ഇതുപോലെ കാണും `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*ഗమనിക്കുക: ഈ ഉദാഹരണം ടൂൾ കോളിംഗ് മാത്രം കാണിക്കുന്നു, ഫലങ്ങൾ നേടാൻ നിങ്ങൾക്ക് ബ്രേവ് API പേജിൽ ഫ്രീ അക്കൗണ്ട് സൃഷ്ടിച്ചുകൊണ്ട് ഫംഗ്ഷൻ നിർവചിക്കേണ്ടതാണ്.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# നിങ്ങളുടെ Microsoft Foundry പ്രൊജക്ടിന്റെ "അവലോകനം" പേജിൽ നിന്നു ഇത് നേടുക
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## ല്ലാമ 3.2 

LLM ആണെങ്കിലും, ല്ലാമ 3.1-ന്റെ ഒരു പരിധി ബഹുമാധ്യമ രീതിയില്ലായ്മയാണ്. അതായത്, ചിത്രങ്ങൾ പോലുള്ള വിവിധ തരത്തിലുള്ള ഇൻപുട്ടുകൾ പ്രാമ്പ്റ്റുകളായി ഉപയോഗിക്കുകയും പ്രതികരണങ്ങൾ നൽകുകയും ചെയ്യാനാകാത്തതാ. ഇത് ല്ലാമ 3.2-ന്റെ പ്രധാന സവിശേഷതകളിൽ ഒന്നാണ്. ഈ സവിശേഷതകൾ ഇതുകൂടിയുണ്ട്: 

- ബഹുമാധ്യമത - ടക്സ്റ്റും ചിത്ര പ്രാമ്പ്റ്റുകളും മൂല്യനിർണയം ചെയ്യാൻ കഴിയും 
- ചെറിയ മുതൽ മധ്യമ വലുപ്പം വകഭേദങ്ങൾ (11B and 90B) - ഫ്ലെക്സിബിൾ ഡിപ്ലോയ്മെന്റ് ഓപ്ഷനുകൾ നൽകുന്നു, 
- ടക്സ്റ്റ് മാത്രം വകഭേദങ്ങൾ (1B and 3B) - മോഡൽ എജ് / മൊബൈൽ ഡിവൈസുകളിൽ ഡിപ്ലോയ് ചെയ്‌തേക്കാം, കുറഞ്ഞ ദൈർഘ്യം നൽകുന്നു 

ബഹുമാധ്യമ പിന്തുണ ഓപ്പൺ സോഴ്സ് മോഡലുകളുടെ ലോകത്ത് വലിയ മൈൽസ്ടോൺ ആണ്. താഴെ നൽകിയ കോഡ് ഉദാഹരണം ഒരു ചിത്രം കൂടാതെ ടക്സ്റ്റ് പ്രാമ്പ്റ്റും ഉപയോഗിച്ച് ല്ലാമ 3.2 90B-നിന്ന് ചിത്രത്തിന്റെ വിശകലനം ലഭിക്കുന്നു. 


### ല്ലാമ 3.2-നോടു ചേർന്ന ബഹുമാധ്യമ പിന്തുണ

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

# നിങ്ങളുടെ Microsoft Foundry പ്രോജക്റ്റിന്റെ "ഓവർവ്യൂ" പേജിൽ നിന്ന് ഇവ എടുക്കുക
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## പഠനം ഇവിടെ അവസാനിക്കുന്നില്ല, യാത്ര തുടരുക

ഈ പാഠം പൂർത്തിയാക്കിയ ശേഷം, ഞങ്ങളുടെ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) പരിശോധിച്ച് നിങ്ങളുടെ Generative AI അറിവ് ഉയർത്താൻ തുടരണം!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->