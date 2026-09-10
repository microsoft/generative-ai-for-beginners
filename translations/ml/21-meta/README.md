# മെറ്റ ഫാമിലി മോഡലുകളുമായി നിർമ്മാണം 

## പരിചയം 

ഈ പാഠം ഇതുവരെയുണ്ടാക്കും: 

- രണ്ട് പ്രധാന മെറ്റ ഫാമിലി മോഡലുകൾ പരിശോധിക്കുക - ല്ലാമ 3.1, ല്ലാമ 3.2 
- ഓരോ മോഡലിനും ഉള്ള ഉപയോഗ കേസുകളും ദൃശ്യവുമായുള്ള അറിവ് 
- ഓരോ മോഡലിന്റെയും വ്യത്യസ്ത സവിശേഷതകൾ ցույց കൊടുക്കുന്ന കോഡ് ഉദാഹരണം 


## മെറ്റ ഫാമിലി മോഡലുകൾ 

ഈ പാഠത്തിൽ, നാം മെറ്റ ഫാമിലി അല്ലെങ്കിൽ "ല്ലാമ ഹെർഡ്" ൽ നിന്നുള്ള 2 മോഡലുകൾ പരിശോധിക്കും - ല്ലാമ 3.1, ല്ലാമ 3.2.

ഈ മോഡലുകൾ വ്യത്യസ്ത വേരിയന്റുകളിലുണ്ട്, [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ൽ ലഭ്യമാണ്.

> **കുറിപ്പ്:** GitHub മോഡലുകൾ 2026 ജൂലൈ അവസാനം അവസാനിപ്പിക്കുന്നു. AI മോഡലുകളുമായി പ്രോട്ടോടൈപ്പ് ചെയ്യാൻ [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ഉപയോഗിക്കുന്നതിന് കൂടുതൽ വിശദാംശങ്ങൾ ഇവിടെ കാണുക.

മോഡൽ വേരിയന്റുകൾ: 
- ല്ലാമ 3.1 - 70B ഇൻസ്ട്രക്റ്റ് 
- ല്ലാമ 3.1 - 405B ഇൻസ്ട്രക്റ്റ് 
- ല്ലാമ 3.2 - 11B വിഷൻ ഇൻസ്ട്രക്റ്റ് 
- ല്ലാമ 3.2 - 90B വിഷൻ ഇൻസ്ട്രക്റ്റ് 

*കുറിപ്പ്: ല്ലാമ 3 മൈക്രോസോഫ്റ്റ് ഫൌണ്ട്രി മോഡലുകളിൽ ലഭ്യമാണ്, പക്ഷേ ഈ പാഠത്തിൽ ഉൾപ്പെടുന്നില്ല*

## ല്ലാമ 3.1 

405 ബില്ല്യൺ പാരാമീറ്ററുകളോടെ, ല്ലാമ 3.1 ഓപ്പൺ സോഴ്‌സ് LLM വിഭാഗത്തിൽപ്പെടുന്നത് ആണ്. 

ഈ മോഡൽ മുമ്പത്തെ റിലീസ് ല്ലാമ 3 നെ അപ്ഗ്രേഡ് ചെയ്യുന്നു: 

- വലിയ കണ്ടക്സ് വിൻഡോ - 128k ടോക്കണുകൾ എതിരെ 8k ടോക്കണുകൾ 
- വലിയ പരമാവധി ഔട്ട്‌പുട്ട് ടോക്കണുകൾ - 4096 എതിർ 2048 
- മെച്ചപ്പെട്ട ബഹുഭാഷാ പിന്തുണ - പരിശീലന ടോക്കണുകളുടെ വർധനവിന്റെ ഫലം 

ഇതുവഴി ല്ലാമ 3.1 ജനറേറ്റീവ് AI ആപ്ലിക്കേഷനുകൾക്ക് കൂടുതൽ സമുചിതമായ ഉപയോഗ കേസുകൾ കൈകാര്യം ചെയ്യാൻ കഴിയും, അവയിൽ: 
- നാട്ടിൻതള്ള പ്രവർത്തന വിളി - LLM പ്രവൃത്തി പ്രക്രിയയ്ക്ക് പുറത്തുള്ള പുറത്തുള്ള ഉപകരണങ്ങളും ഫങ്ഷനുകളും വിളിക്കാൻ കഴിയുന്ന കഴിവ്
- മെച്ചപ്പെട്ട RAG പെർഫോർമൻസ് - ഉയർന്ന കണ്ടക്സ് വിൻഡോ മൂലം 
- സിന്തറ്റിക് ഡാറ്റ ജനറേഷൻ - ഫൈൻ-ട്യൂണിംഗിന് വേണ്ടിയുള്ള ഫലപ്രദമായ ഡാറ്റ സൃഷ്ടിക്കാൻ കഴിവ് 

### നാട്ടിൻതള്ള പ്രവർത്തന വിളി 

ല്ലാമ 3.1 ഫങ്ഷൻ അല്ലെങ്കിൽ ടൂൾ വിളികൾ കൂടുതൽ ഫലപ്രദമാക്കാൻ ഫൈൻ-ട്യൂൺ ചെയ്‌തിരിക്കുന്നു. മോഡലിന് രണ്ട് ഇൻബിൽറ്റുൾ ടൂളുകൾ ഉണ്ട്, ഉപയോക്താവിന്റെ പ്രോസംബ് അടിസ്ഥാനമാക്കി ഉപയോഗിക്കേണ്ടതെന്ന് തിരിച്ചറിയാൻ കഴിയും. ഈ ടൂളുകൾ: 

- **Brave Search** - വെബ് സെർച്ച് നടത്തിക്കൊണ്ടു സമയബന്ധിത വിവരങ്ങൾ, പ്രധാനമായി കാലാവസ്ഥ പ്രാപ്തമാക്കാൻ ഉപയോഗിക്കുന്നു 
- **Wolfram Alpha** - കൂടുതൽ സങ്കീർണ്ണ ഗണിത കണക്കുകൾക്കായി ഉപയോഗിക്കുന്നു, സ്വന്തം ഫങ്ഷനുകൾ എഴുതേണ്ടതില്ല. 

നിങ്ങൾക്ക് നിങ്ങൾക്കായി കസ്റ്റം ടൂളുകൾ സൃഷ്ടിക്കാൻ കഴിയും, അവ LLM വിളിക്കാം. 

താഴെ കൊടുത്തിരിക്കുന്ന കോഡ് ഉദാഹരണത്തിൽ: 

- സിസ്റ്റം പ്രോസംബിൽ ലഭ്യമായ ടൂളുകൾ (brave_search, wolfram_alpha) നിർവ്വചിക്കുന്നു. 
- ഒരു യൂസർ പ്രോസംബ് അയയ്ക്കുന്നു, ഒരു പ്രത്യേക നഗരത്തിലെ കാലാവസ്ഥയെ കുറിച്ച് ചോദിക്കുന്നു. 
- LLM Brave Search ടൂൾ കാൾ ആയി പ്രതികരിക്കും, ഇത് ഇങ്ങനെ കാണിക്കും `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*കുറിപ്പ്: ഈ ഉദാഹരണം ടൂൾ કોલ് മാത്രം നടത്തുന്നു, ഫലങ്ങൾ ലഭിക്കാൻ Brave API പേജിൽ നിങ്ങൾക്ക് സൗജന്യ അക്കൗണ്ട് ഉണ്ടാക്കേണ്ടതും ഫങ്ഷൻ തന്നെ നിർവ്വചിക്കേണ്ടതുമുണ്ട്.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# മൈക്രോസോഫ്റ്റ് ഫൗണ്ട്രി പ്രോജക്ടിന്റെ "ഓവerview" പേജിൽ നിന്ന് ഇവ നേടുക
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

എൽഎൽഎം ആണെങ്കിലും, ല്ലാമ 3.1 ന്റെ ഒരു പരിമിതി ബഹുമാധ്യമതയുടെ അഭാവമാണ്. അതായത്, ചിത്രങ്ങൾ പോലുള്ള വിവിധ തരത്തിലുള്ള ഇൻപുട്ടുകൾ പ്രോസംബായി ഉപയോഗിക്കുകയും പ്രതികരിക്കുകയും ചെയ്യാൻ കഴിയാത്തത്. ഈ കഴിവ് ല്ലാമ 3.2 യുടെ മുഖ്യ സവിശേഷതയാണ്. ഇതിന് പുറമേയുള്ള സവിശേഷതകൾ: 

- ബഹുമാധ്യമത - ടെക്സ്റ്റും ചിത്ര പ്രോസംബുകളും വിലയിരുത്താൻ കഴിവ് 
- ചെറുതും മദ്ധ്യമാകുന്ന വലുപ്പ സാധ്യതകൾ (11B, 90B) - ഇതു വിന്യസിക്കുന്നതിൽ ലൈവറാണ്, 
- ടെക്സ്റ്റ് മാത്രം വേരിയന്റുകൾ (1B, 3B) - ഇത് മോഡൽ എഡ്ജ്/മൊബൈൽ ഉപകരണങ്ങളിലാണ് വിന്യാസം നടത്താനും കുറഞ്ഞ ഇടവേള നൽകാനും സഹായിക്കുന്നു 

ബഹുമാധ്യമ പിന്തുണ ഓപ്പൺ സോഴ്‌സ് മോഡലുകളുടെ ലോകത്ത് വലിയ മുന്നേറ്റമാണ്. താഴെ കൊടുത്തിരിക്കുന്ന കോഡ് ഉദാഹരണം ഒരു ചിത്രം കൂടാതെ ടെക്സ്റ്റ് പ്രോസംബ് സ്വീകരിച്ച് ല്ലാമ 3.2 90B നിൽ നിന്നുള്ള ചിത്ര വിശകലനം നേടുന്നു. 


### ല്ലാമ 3.2 ൽ ബഹുമാധ്യമ പിന്തുണ

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

# നിങ്ങളുടെ Microsoft Foundry പ്രോജക്ടിന്റെ "അവലോകനം" പേജിൽ നിന്ന് ഇത് الحصول ചെയ്യുക
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

ഈ പാഠം പൂർത്തിയാക്കിയശേഷം, മെഴുകു നിങ്ങളുടെ ജനറേറ്റീവ് AI നോളജ് മെച്ചപ്പെടുത്താൻ നമ്മുടെ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) കാണുക!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->