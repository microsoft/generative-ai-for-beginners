# മെറ്റാ ഫാമിലി മോഡലുകളുമായി നിർമ്മാണം

## പരിചയം

ഈ പാഠം ഉൾക്കൊള്ളുന്നതാണ്:

- രണ്ട് പ്രധാന മെറ്റാ ഫാമിലി മോഡലുകൾ - ല്ലാമ 3.1, ല്ലാമ 3.2 എന്നിവ പരിശോധിക്കൽ
- ഓരോ മോഡലിന്റെയും ഉപയോഗ കേസുകളും സാഹചര്യങ്ങളും മനസ്സിലാക്കൽ
- ഓരോ മോഡലിന്റെയും പ്രത്യേകതകൾ കാണിക്കുന്ന കോഡ് ഉദാഹരണം

## മെറ്റാ ഫാമിലി മോഡലുകൾ

ഈ പാഠത്തിൽ, മെറ്റാ ഫാമിലി അല്ലെങ്കിൽ "ല്ലാമ ഹെർഡ്" എന്നറിയപ്പെടുന്ന 2 മോഡലുകൾ പരിശോധിക്കും - ല്ലാമ 3.1, ല്ലാമ 3.2

ഈ മോഡലുകൾ വ്യത്യസ്ത വകഭേദങ്ങളിലായി ലഭ്യമാണ്, കൂടാതെ GitHub മോഡൽ മാർക്കറ്റ്പ്ലേസിൽ ലഭ്യമാണ്. GitHub മോഡലുകൾ ഉപയോഗിച്ച് [AI മോഡലുകളുമായി പ്രോട്ടോടൈപ്പ് ചെയ്യുന്നതിനെക്കുറിച്ച്](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) കൂടുതൽ വിവരങ്ങൾ ഇവിടെ കാണാം.

മോഡൽ വകഭേദങ്ങൾ:
- ല്ലാമ 3.1 - 70B ഇൻസ്ട്രക്റ്റ്
- ല്ലാമ 3.1 - 405B ഇൻസ്ട്രക്റ്റ്
- ല്ലാമ 3.2 - 11B വിഷൻ ഇൻസ്ട്രക്റ്റ്
- ല്ലാമ 3.2 - 90B വിഷൻ ഇൻസ്ട്രക്റ്റ്

*കുറിപ്പ്: ല്ലാമ 3 GitHub മോഡലുകളിൽ ലഭ്യമാണ്, പക്ഷേ ഈ പാഠത്തിൽ ഉൾപ്പെടുത്തുന്നില്ല*

## ല്ലാമ 3.1

405 ബില്യൺ പാരാമീറ്ററുകളുള്ള ല്ലാമ 3.1 ഓപ്പൺ സോഴ്‌സ് LLM വിഭാഗത്തിൽപ്പെടുന്നു.

മുൻപ് പുറത്തിറങ്ങിയ ല്ലാമ 3-ന്റെ അപ്ഗ്രേഡ് മോഡലാണ് ഇത്, ഇതിലൂടെ ലഭിക്കുന്നവ:

- വലിയ കോൺടെക്സ്റ്റ് വിൻഡോ - 128k ടോക്കൺസ് 8k ടോക്കൺസിനെ അപേക്ഷിച്ച്
- വലിയ മാക്സ് ഔട്ട്പുട്ട് ടോക്കൺസ് - 4096 2048-നെ അപേക്ഷിച്ച്
- മെച്ചപ്പെട്ട ബഹുഭാഷാ പിന്തുണ - പരിശീലന ടോക്കണുകളുടെ വർദ്ധനവിന്റെ ഫലമായി

ഇവ ല്ലാമ 3.1-ന് GenAI ആപ്ലിക്കേഷനുകൾ നിർമ്മിക്കുമ്പോൾ കൂടുതൽ സങ്കീർണ്ണമായ ഉപയോഗ കേസുകൾ കൈകാര്യം ചെയ്യാൻ സഹായിക്കുന്നു, ഉദാഹരണങ്ങൾ:

- നേറ്റീവ് ഫംഗ്ഷൻ കോളിംഗ് - LLM പ്രവാഹത്തിന് പുറത്തുള്ള ടൂളുകളും ഫംഗ്ഷനുകളും വിളിക്കാൻ കഴിവ്
- മെച്ചപ്പെട്ട RAG പ്രകടനം - ഉയർന്ന കോൺടെക്സ്റ്റ് വിൻഡോ കാരണം
- സിന്തറ്റിക് ഡാറ്റ ജനറേഷൻ - ഫൈൻ-ട്യൂണിംഗിനുള്ള ഫലപ്രദമായ ഡാറ്റ സൃഷ്ടിക്കാൻ കഴിവ്

### നേറ്റീവ് ഫംഗ്ഷൻ കോളിംഗ്

ല്ലാമ 3.1 ഫംഗ്ഷൻ അല്ലെങ്കിൽ ടൂൾ കോൾ ചെയ്യുന്നതിൽ കൂടുതൽ ഫലപ്രദമാക്കാൻ ഫൈൻ-ട്യൂൺ ചെയ്തിട്ടുണ്ട്. ഉപയോക്താവിന്റെ പ്രോംപ്റ്റ് അടിസ്ഥാനമാക്കി ഉപയോഗിക്കേണ്ട ടൂളുകൾ മോഡൽ തിരിച്ചറിയാൻ കഴിവുള്ള രണ്ട് ഇൻബിൽറ്റ് ടൂളുകളും ഉണ്ട്. അവ:

- **ബ്രേവ് സെർച്ച്** - വെബ് സെർച്ച് നടത്തിക്കൊണ്ട് കാലാവസ്ഥ പോലുള്ള പുതുക്കിയ വിവരങ്ങൾ ലഭിക്കാൻ ഉപയോഗിക്കാം
- **വോൾഫ്രാം ആൽഫ** - കൂടുതൽ സങ്കീർണ്ണ ഗണിത കണക്കുകൾക്കായി ഉപയോഗിക്കാം, അതിനാൽ നിങ്ങളുടെ സ്വന്തം ഫംഗ്ഷനുകൾ എഴുതേണ്ടതില്ല

നിങ്ങൾക്ക് നിങ്ങളുടെ സ്വന്തം കസ്റ്റം ടൂളുകളും സൃഷ്ടിക്കാം, LLM അവ വിളിക്കാം.

താഴെ കൊടുത്തിരിക്കുന്ന കോഡ് ഉദാഹരണത്തിൽ:

- സിസ്റ്റം പ്രോംപ്റ്റിൽ ലഭ്യമായ ടൂളുകൾ (brave_search, wolfram_alpha) നിർവചിക്കുന്നു.
- ഒരു നഗരത്തിലെ കാലാവസ്ഥയെക്കുറിച്ച് ചോദിക്കുന്ന ഉപയോക്തൃ പ്രോംപ്റ്റ് അയയ്ക്കുന്നു.
- LLM ബ്രേവ് സെർച്ച് ടൂൾ കോൾ ആയി പ്രതികരിക്കും, ഇത് ഇങ്ങനെ കാണപ്പെടും `<|python_tag|>brave_search.call(query="Stockholm weather")`

*കുറിപ്പ്: ഈ ഉദാഹരണം ടൂൾ കോൾ മാത്രമാണ് ചെയ്യുന്നത്, ഫലങ്ങൾ ലഭിക്കാൻ നിങ്ങൾക്ക് ബ്രേവ് API പേജിൽ ഒരു സൗജന്യ അക്കൗണ്ട് സൃഷ്ടിച്ച് ഫംഗ്ഷൻ നിർവചിക്കേണ്ടതുണ്ട്*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

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

LLM ആയിട്ടും, ല്ലാമ 3.1-ന് ഒരു പരിമിതിയാണ് മൾട്ടിമോഡാലിറ്റി. അതായത്, ചിത്രങ്ങൾ പോലുള്ള വ്യത്യസ്ത തരത്തിലുള്ള ഇൻപുട്ടുകൾ പ്രോംപ്റ്റുകളായി ഉപയോഗിച്ച് പ്രതികരണങ്ങൾ നൽകാൻ കഴിയുക. ഈ കഴിവ് ല്ലാമ 3.2-ന്റെ പ്രധാന സവിശേഷതകളിലൊന്നാണ്. ഈ സവിശേഷതകൾ ഉൾപ്പെടുന്നു:

- മൾട്ടിമോഡാലിറ്റി - ടെക്സ്റ്റും ചിത്ര പ്രോംപ്റ്റുകളും വിലയിരുത്താനുള്ള കഴിവ്
- ചെറിയ മുതൽ മധ്യവയസ്സുള്ള വകഭേദങ്ങൾ (11B, 90B) - ഇത് ലളിതമായ വിന്യാസ ഓപ്ഷനുകൾ നൽകുന്നു
- ടെക്സ്റ്റ് മാത്രം വകഭേദങ്ങൾ (1B, 3B) - ഇത് മോഡൽ എഡ്ജ് / മൊബൈൽ ഉപകരണങ്ങളിൽ വിന്യസിക്കാൻ അനുവദിക്കുകയും കുറഞ്ഞ ലാറ്റൻസി നൽകുകയും ചെയ്യുന്നു

മൾട്ടിമോഡൽ പിന്തുണ ഓപ്പൺ സോഴ്‌സ് മോഡലുകളുടെ ലോകത്ത് വലിയ മുന്നേറ്റമാണ്. താഴെ കൊടുത്തിരിക്കുന്ന കോഡ് ഉദാഹരണം ഒരു ചിത്രം കൂടാതെ ടെക്സ്റ്റ് പ്രോംപ്റ്റും ഉപയോഗിച്ച് ല്ലാമ 3.2 90B-ൽ നിന്നുള്ള ചിത്ര വിശകലനം നേടുന്നു.

### ല്ലാമ 3.2-യുമായി മൾട്ടിമോഡൽ പിന്തുണ

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

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
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

ഈ പാഠം പൂർത്തിയാക്കിയ ശേഷം, നമ്മുടെ [ജനറേറ്റീവ് AI പഠന ശേഖരം](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) പരിശോധിച്ച് നിങ്ങളുടെ ജനറേറ്റീവ് AI അറിവ് ഉയർത്താൻ തുടരണം!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖയാണ് പ്രാമാണികമായ ഉറവിടം എന്ന് പരിഗണിക്കേണ്ടതാണ്. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->