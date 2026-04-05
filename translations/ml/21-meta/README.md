# മെട ഫാമിലി മോഡലുകളുമായി നിർമ്മാണം

## പരിചയം

ഈ പാഠത്തിൽ പരിഗണിക്കുന്നത്:

- രണ്ട് പ്രധാന മെട ഫാമിലി മോഡലുകൾ - ല്ലാമ 3.1, ല്ലാമ 3.2 എന്നിവ പരിശോധിക്കുക
- ഓരോ മോഡലിന്റെയും ഉപയോഗാവശ്യങ്ങളും സാഹചര്യങ്ങളും മനസിലാക്കുക
- ഓരോ മോഡലിന്റെയും പ്രത്യേകതകൾ കാണിക്കുന്ന കോഡ് സാംപിൽ

## മെട ഫാമിലി മോഡലുകൾ

ഈ പാഠത്തിൽ, മെട ഫാമിലി അല്ലെങ്കിൽ "ല്ലാമ ഹേർഡ്" എന്ന 2 മോഡലുകൾ പരിഗണിക്കും - ല്ലാമ 3.1, ല്ലാമ 3.2.

ഈ മോഡലുകൾ വ്യത്യസ്ത വേരിയന്റുകളിൽ ലഭ്യമാണ് കൂടാതെ GitHub മോഡൽ മാർക്കറ്റ്പ്ലേസിൽ ലഭ്യമാണ്. GitHub മോഡലുകളുമായി ബന്ധപ്പെട്ട കൂടുതൽ വിവരങ്ങൾ [AI മോഡലുകളുമായി പ്രോട്ടോടൈപ്പിങ്](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) എന്ന ലിങ്കിൽ കാണാം.

മോഡൽ വേരിയന്റുകൾ:  
- ല്ലാമ 3.1 - 70B ഇൻസ്ട്രക്റ്റ്  
- ല്ലാമ 3.1 - 405B ഇൻസ്ട്രക്റ്റ്  
- ല്ലാമ 3.2 - 11B വിഷൻ ഇൻസ്ട്രക്റ്റ്  
- ല്ലാമ 3.2 - 90B വിഷൻ ഇൻസ്ട്രക്റ്റ്  

*കുറിപ്പ്: ല്ലാമ 3 GitHub മോഡലുകളിൽ ലഭ്യമാണ്, പക്ഷേ ഈ പാഠത്തിൽ ഉൾപ്പെടുത്തുന്നില്ല*

## ല്ലാമ 3.1

405 ബില്യൺ പാരാമീറ്ററുകളുള്ള ല്ലാമ 3.1 ഓപ്പൺ സോഴ്സ് LLM വിഭാഗത്തിൽപ്പെടുന്നു.

മുമ്പത്തെ ല്ലാമ 3 റിലീസിനെ അപേക്ഷിച്ച് ഈ മോഡലിന് ലഭിക്കുന്ന മെച്ചപ്പെടുത്തലുകൾ:

- വലിയ കോൺടെക്സ്റ്റ് വിൻഡോ - 128k ടോക്കൻസ് നിന്നു 8k ടോക്കൻസിലേക്ക്  
- വലുതായ പരമാവധി ഔട്ട്‌പുട്ട് ടോക്കൻ - 4096 vs 2048  
- മെച്ചപ്പെട്ട ബഹുഭാഷാ പിന്തുണ - പരിശീലന ടോക്കൻസിന്റെ വർധനവിന്റെ ഫലം  

ഇവ GenAI അപ্লിക്കേഷനുകൾ നിർമ്മിക്കുന്നപ്പോൾ മുന്നേറ്റമായി ല്ലാമ 3.1 നു സഹായകമായ കാര്യങ്ങൾ:

- ജന്മസിദ്ധ ഫംഗ്ഷൻ കോളിങ് - LLM പ്രക്രിയയ്‌ക്കു പുറത്ത് എക്സ്റ്റേണൽ ടൂളുകളും ഫംഗ്ഷനുകളും വിളിക്കാൻ കഴിയുന്നു
- മെച്ചപ്പെട്ട RAG പ്രകടനം - ഉയർന്ന കോൺടെക്സ്റ്റ് വിൻഡോയുടെ കാരണത്താൽ
- സിന്തറ്റിക് ഡാറ്റ ജനറേഷൻ - ഫൈൻ-ട്യൂണിംഗിനായി ഫലപ്രദമായ ഡാറ്റ സൃഷ്ടിക്കാൻ കഴിയും

### ജന്മസിദ്ധ ഫംഗ്ഷൻ കോളിങ്

ല്ലാമ 3.1 ഫംഗ്ഷനുകളും ടൂളുകളും വിളിക്കാൻ കൂടുതൽ ഫലപ്രദമാക്കാൻ ഫൈൻ-ട്യൂൺ ചെയ്‌തിരിക്കുന്നു. ഉപയോക്താവിന്റെ പ്രോമ്പ്റ്റിനെ അടിസ്ഥാനമാക്കി ഉപയോഗിക്കേണ്ട ടൂളുകൾ തിരിച്ചറിയാൻ മോഡലിന് ഉള്ളില്‍ രണ്ട് ടൂളുകൾ ഉൾപ്പെടുത്തിയിട്ടുണ്ട്. ആ ടൂളുകൾ:

- **ബ്രാവി സെർച്ച്** - വെബ് സെർച്ച് നടത്തി കാലാവസ്ഥ പോലുള്ള പുതുക്കപ്പെട്ട വിവരങ്ങൾ കിട്ടാൻ ഉപയോഗിക്കുന്നു  
- **വോൾഫ്രാം ആൽഫ** - കൂടുതൽ സങ്കീർണ്ണമായ ഗണിത കണക്കുകൂട്ടലുകൾക്കായി, സ്വയം ഫംഗ്ഷനുകൾ എഴുതേണ്ടതില്ല  

നിങ്ങൾക്ക് നിങ്ങളുടെ സ്വന്തം കസ്റ്റം ടൂളുകളും സൃഷ്ടിക്കാം, LLM ഈ ടൂളുകൾ വിളിക്കാനാകും.

താഴെ കാണുന്ന കോഡ് ഉദാഹരണത്തിൽ:

- ലഭ്യമായ ടൂളുകൾ (brave_search, wolfram_alpha) സിസ്റ്റം പ്രോമ്പ്റ്റിൽ നിർവചിക്കപ്പെടുന്നു.  
- ഒരു പ്രത്യേക നഗരത്തിലെ കാലാവസ്ഥയെക്കുറിച്ച് ചോദിക്കുന്ന ഉപയോക്തൃ പ്രോമ്പ്റ്റ് അയയ്ക്കുന്നു.  
- LLM ബ്രാവി സെർച്ച് ടൂളിനെ വിളിക്കുന്ന `<|python_tag|>brave_search.call(query="Stockholm weather")` എന്ന രീതിയിൽ മറുപടി നൽകുന്നുണ്ട്.  

*കുറിപ്പ്: ഉദാഹരണത്തിൽ ടൂൾ കോൾ മാത്രമാണ് കാണിക്കുന്നത്; ഫലങ്ങൾ എടുക്കാൻ ബ്രാവി API പേജിൽ സൗജന്യ അക്കൗണ്ട് തുറന്ന് ഫംഗ്ഷൻ നിർവചിക്കണം.*

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

LLM ആയതിനാൽ, ല്ലാമ 3.1 ന്റെ ഒരു പരിമിതിയാണ് മൾട്ടിമോടാലിറ്റി ഇല്ലായ്മ. അഥവാ, ചിത്രങ്ങൾ പോലുള്ള വ്യത്യസ്ത തരം ഇൻപുട്ടുകൾ പ്രോമ്പ്റ്റായി ഉപയോഗിച്ച് പ്രതികരണങ്ങൾ നൽകാൻ കഴിയാത്തത്. ഇത് ല്ലാമ 3.2 ന്റെ പ്രധാന സവിശേഷതകളിലൊന്നാണ്. ഈ സവിശേഷതകളും ഉൾക്കൊള്ളുന്നു:

- മൾട്ടിമോടാലിറ്റി - ടെകസ്റ്റ്, ഇമേജ് പ്രോമ്പ്റ്റുകൾ വിലയിരുത്താനാകുന്നു  
- ചെറിയ മുതൽ മധ്യമ തോതിലുള്ള വേരിയന്റുകൾ (11B, 90B) - സൗകര്യപ്രദമായ വിന്യസമാക്കൽ ഓപ്ഷനുകൾ  
- ടെക്സ്റ്റ് മാത്രം വേരിയന്റുകൾ (1B, 3B) - എഡ്ജ് / മൊബൈൽ ഉപകരണങ്ങളിൽ വിന്യസിയ്ക്കാനും കുറവ് ലാറ്റൻസിയും

മൾട്ടിമോടൽ പിന്തുണ ഓപ്പൺ സോഴ്സ് മോഡലുകളുടെ ലോകത്ത് വലിയ മുന്നേറ്റമാണിത്. താഴെയുള്ള കോഡിൽ ഒരു ചിത്രം കൂടാതെ ടെക്സ്റ്റ് പ്രോമ്പ്റ്റും നൽകുന്നു; ല്ലാമ 3.2 90B ചിത്രത്തിന്റെ വിശകലനം നൽകുന്നു.

### ല്ലാമ 3.2 യോടുള്ള മൾട്ടിമോടൽ പിന്തുണ

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

ഈ പാഠം പൂർത്തിയാക്കിയതിന് ശേഷം നമ്മുടെ [ജനറേറ്റീവ് AI ലർണിംഗ് ശേഖരം](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) പരിശോധിച്ച് നിങ്ങളുടെ ജനറേറ്റീവ് AI വിജ്ഞാനം വർധിപ്പിക്കാൻ തുടരുക!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസാധുത**:  
ഈ രേഖ AI വിവര്‍ത്തന സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവര്‍ത്തനം ചെയ്തിരിക്കുകയാണ്. ഞങ്ങള്‍ ശരിയായ വിവര്‍ത്തനം ഉറപ്പാക്കാന്‍ ശ്രമിക്കുന്നതിനിടയിലും, ഓട്ടോമാറ്റഡ് വിവര്‍ത്തനങ്ങളില്‍ പിശകുകള്‍ അല്ലെങ്കില്‍ അപൂര്‍ണ്ണതകള്‍ ഉണ്ടാകാമെന്നുള്ളത് മനസ്സിലാക്കേണ്ടതാണ്. സ്രോതസ്സ് ഭാഷയിലുള്ള പ്രഥമ രേഖ യഥാര്‍ഥവും അവകാശമുള്ളതുമായ സ്രോതസ്സ് ആയി കണക്കാക്കപ്പെടണം. ഗുരുതരമുള്ള വിവരങ്ങള്‍ക്കായി വിദഗ്ധ മനുഷ്യ വിവര്‍ത്തനം നിര്‍ദേശിക്കുന്നു. ഈ വിവര്‍ത്തനത്തിന്റെ ഉപയോഗത്തില്‍ നിന്നു ഉണ്ടായിട്ടുള്ള തെറ്റിദ്ധാരണകള്‍ക്ക് ഞങ്ങള്‍ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->