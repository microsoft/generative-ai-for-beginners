<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:12:23+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "sw"
}
-->
# Kujenga Kwa Modeli za Familia ya Meta

## Utangulizi

Somo hili litajumuisha:

- Kuchunguza modeli kuu mbili za familia ya Meta - Llama 3.1 na Llama 3.2  
- Kuelewa matumizi na hali za kila modeli  
- Mfano wa msimbo unaoonyesha sifa za kipekee za kila modeli  

## Familia ya Modeli za Meta

Katika somo hili, tutachunguza modeli 2 kutoka familia ya Meta au "Llama Herd" - Llama 3.1 na Llama 3.2

Modeli hizi zinakuja katika aina tofauti na zinapatikana kwenye soko la Modeli la GitHub. Hapa kuna maelezo zaidi kuhusu kutumia Modeli za GitHub kwa [kufanya majaribio na modeli za AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Aina za Modeli:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Note: Llama 3 pia inapatikana kwenye Modeli za GitHub lakini haitajadiliwa katika somo hili*

## Llama 3.1

Kwa Parameta Bilioni 405, Llama 3.1 inaingia katika kundi la LLM za chanzo huria.

Modeli hii ni toleo lililoboreshwa la Llama 3 lililotanguliwa kwa kutoa:

- Dirisha kubwa la muktadha - tokeni 128k dhidi ya tokeni 8k  
- Idadi kubwa zaidi ya Tokeni za Matokeo - 4096 dhidi ya 2048  
- Msaada bora wa Lugha Nyingi - kutokana na ongezeko la tokeni za mafunzo  

Hii inamwezesha Llama 3.1 kushughulikia matumizi magumu zaidi wakati wa kujenga programu za GenAI ikijumuisha:  
- Kupiga Simu za Kazi za Asili - uwezo wa kupiga simu kwa zana na kazi za nje ya mtiririko wa LLM  
- Utendaji Bora wa RAG - kutokana na dirisha kubwa la muktadha  
- Uundaji wa Data Bandia - uwezo wa kuunda data yenye ufanisi kwa kazi kama vile kufinyangwa  

### Kupiga Simu za Kazi za Asili

Llama 3.1 imeboreshwa ili iwe na ufanisi zaidi katika kupiga simu za kazi au zana. Pia ina zana mbili zilizojengwa ndani ambazo modeli inaweza kutambua zinahitajika kutumika kulingana na maelekezo kutoka kwa mtumiaji. Zana hizi ni:

- **Brave Search** - Inaweza kutumika kupata taarifa za hivi karibuni kama hali ya hewa kwa kufanya utafutaji mtandaoni  
- **Wolfram Alpha** - Inaweza kutumika kwa mahesabu magumu zaidi ya hisabati hivyo kuandika kazi zako mwenyewe si lazima  

Unaweza pia kuunda zana zako maalum ambazo LLM inaweza kupiga simu.

Katika mfano wa msimbo hapa chini:

- Tunaeleza zana zinazopatikana (brave_search, wolfram_alpha) katika maelekezo ya mfumo.  
- Tunatuma maelekezo ya mtumiaji yanayouliza kuhusu hali ya hewa katika mji fulani.  
- LLM itajibu kwa kupiga simu ya zana kwa Brave Search ambayo itaonekana kama hii `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*Note: Mfano huu unafanya tu simu ya zana, ikiwa ungependa kupata matokeo, utahitaji kuunda akaunti ya bure kwenye ukurasa wa Brave API na kufafanua kazi yenyewe*  

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

## Llama 3.2

Licha ya kuwa LLM, kizuizi kimoja ambacho Llama 3.1 kina ni uwezo wa kutumia aina tofauti za pembejeo kama picha kama maelekezo na kutoa majibu. Uwezo huu ni mojawapo ya sifa kuu za Llama 3.2. Sifa hizi pia ni pamoja na:

- Multimodality - ina uwezo wa kutathmini maelekezo ya maandishi na picha  
- Aina ndogo hadi za kati (11B na 90B) - hii hutoa chaguzi za usambazaji zinazobadilika,  
- Aina za maandishi tu (1B na 3B) - hii inaruhusu modeli kusambazwa kwenye vifaa vya edge / simu na hutoa ucheleweshaji mdogo  

Msaada wa multimodal ni hatua kubwa katika ulimwengu wa modeli za chanzo huria. Mfano wa msimbo hapa chini unachukua picha na maelekezo ya maandishi kupata uchambuzi wa picha kutoka Llama 3.2 90B.

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

## Kujifunza hakukomi hapa, endelea Safari

Baada ya kumaliza somo hili, angalia [Mkusanyiko wetu wa Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza ujuzi wako wa AI ya Kizazi!

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.