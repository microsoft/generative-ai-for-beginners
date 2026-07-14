# Kujenga Kwa Mfumo wa Familia ya Meta 

## Utangulizi 

Somo hili litajumuisha: 

- Kuchunguza mifano miwili kuu ya familia ya Meta - Llama 3.1 na Llama 3.2 
- Kuelewa matumizi na matukio ya kila mfano 
- Sampuli ya msimbo kuonyesha sifa za kipekee za kila mfano 


## Familia ya Mifano ya Meta 

Katika somo hili, tutachunguza mifano 2 kutoka kwa familia ya Meta au "Kundi la Llama" - Llama 3.1 na Llama 3.2.

Mifano hii inakuja kwa aina tofauti na inapatikana katika [Katalogi ya Mifano ya Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Kumbuka:** GitHub Models inakoma kufanikisha mwishoni mwa Julai 2026. Hapa kuna maelezo zaidi ya kutumia [Mifano ya Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) kuunda mfano na mifano ya AI.

Aina za Mfano: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Kumbuka: Llama 3 pia inapatikana katika Mifano ya Microsoft Foundry lakini haitajadiliwa katika somo hili*

## Llama 3.1 

Kwa Paramita Bilioni 405, Llama 3.1 inaingia katika kundi la LLM za chanzo huria. 

Mfano huu ni sasisho la toleo la awali la Llama 3 kwa kutoa: 

- Dirisha kubwa la muktadha - tokeni 128k dhidi ya tokeni 8k 
- Idadi kubwa ya Max Output Tokens - 4096 dhidi ya 2048 
- Msaada bora wa lugha mbalimbali - kwa sababu ya kuongezeka kwa tokeni za mafunzo 

Hii inaruhusu Llama 3.1 kushughulikia matumizi magumu zaidi wakati wa kujenga programu za GenAI ikiwa ni pamoja na: 
- Kupiga simu za Kifunction asilia - uwezo wa kuitisha zana za nje na kazi nje ya mtiririko wa LLM
- Utendaji Bora wa RAG - kutokana na dirisha kubwa zaidi la muktadha 
- Uundaji wa Data ya Syntetiki - uwezo wa kuunda data bora kwa kazi kama vile kufinywa 

### Kupiga Simu Kifunction Asilia 

Llama 3.1 imesanifiwa tena ili kuwa na ufanisi zaidi katika kupiga simu za kifunction au zana. Pia ina zana mbili zilizojengwa ndani ambazo mfano unaweza kubaini zinahitaji kutumiwa kulingana na ombi la mtumiaji. Zana hizi ni: 

- **Brave Search** - Inaweza kutumika kupata habari za hivi karibuni kama hali ya hewa kwa kufanya utafutaji wa wavuti 
- **Wolfram Alpha** - Inaweza kutumika kwa mahesabu magumu zaidi ya kihisabati hivyo kuandika kazi zako mwenyewe si lazima. 

Pia unaweza kuunda zana zako za kawaida ambazo LLM inaweza kuitisha. 

Katika mfano wa msimbo chini: 

- Tunateua zana zinazopatikana (brave_search, wolfram_alpha) katika onyo la mfumo. 
- Tuma ombi la mtumiaji linalouliza kuhusu hali ya hewa katika mji fulani. 
- LLM itajibu kwa simu ya zana kwa zana ya Brave Search ambayo itaonekana kama hii `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Kumbuka: Mfano huu unafanya simu tu ya zana, kama unataka kupata matokeo, utahitaji kujisajili bure kwenye ukurasa wa Brave API na kufafanua kifunction yenyewe.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Pata hizi kutoka ukurasa wa "Muhtasari" wa mradi wako wa Microsoft Foundry
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

## Llama 3.2 

Licha ya kuwa LLM, kizuizi kimoja cha Llama 3.1 ni ukosefu wa multimodality. Yaani, kutoweza kutumia aina tofauti za ingizo kama picha kama mateke na kutoa majibu. Uwezo huu ni mojawapo ya sifa kuu za Llama 3.2. Sifa hizi pia zinajumuisha: 

- Multimodality - ina uwezo wa kutathmini mateke ya maandishi na picha 
- Aina ndogo hadi za kati (11B na 90B) - hii inatoa chaguzi flexible za ueneaji, 
- Aina za maandishi tu (1B na 3B) - hii inaruhusu mfano kuenezwa kwenye vifaa vya edge / simu na kutoa ucheleweshaji mdogo 

Msaada wa multimodal ni hatua kubwa katika dunia ya mifano ya chanzo huria. Mfano wa msimbo chini unatumia picha na kufanya tahmini ya picha kutoka Llama 3.2 90B. 


### Msaada wa Multimodal na Llama 3.2

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

# Pata haya kutoka kwenye ukurasa wa "Muhtasari" wa mradi wako wa Microsoft Foundry
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

## Kujifunza hakukomi hapa, endelea safari

Baada ya kumaliza somo hili, angalia [Mkusanyiko wetu wa Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza ujuzi wako wa AI ya Kizazi!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->