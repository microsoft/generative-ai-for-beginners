# Kujenga Kwa Matoleo ya Familia ya Meta 

## Utangulizi 

Somo hili litahusu: 

- Kuchunguza matoleo mawili makuu ya familia ya Meta - Llama 3.1 na Llama 3.2 
- Kuelewa matumizi na matukio ya kila mfano 
- Mfano wa msimbo kuonyesha sifa za kipekee za kila mfano 


## Familia ya Meta ya Modeli 

Katika somo hili, tutachunguza modeli 2 kutoka familia ya Meta au "Kundi la Llama" - Llama 3.1 na Llama 3.2.

Modeli hizi zinapatikana katika matoleo tofauti na zinapatikana katika [Katalogi ya Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Kumbuka:** GitHub Models itatupwa mwisho wa Julai 2026. Hapa kuna maelezo zaidi juu ya kutumia [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) kujaribu modeli za AI.

Matoleo ya Modeli: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Kumbuka: Llama 3 pia inapatikana katika Microsoft Foundry Models lakini haitashughulikiwa katika somo hili*

## Llama 3.1 

Kwa Parameters Bilioni 405, Llama 3.1 inaingia katika kundi la LLM la chanzo wazi. 

Mfano huu ni sasisho la toleo la awali la Llama 3 kwa kutoa: 

- Dirisha kubwa la muktadha - tokeni 128k dhidi ya tokeni 8k 
- Idadi kubwa zaidi ya Tokeni za Matokeo - 4096 dhidi ya 2048 
- Usaidizi bora wa Lugha Nyingi - kutokana na kuongezeka kwa tokeni za mafunzo 

Hii inamwezesha Llama 3.1 kushughulikia matumizi tata zaidi wakati wa kujenga programu za GenAI ikiwa ni pamoja na: 
- Kufanya Simu za Vitendo vya Asili - uwezo wa kuita zana na vitendo nje ya mtiririko wa LLM
- Utendaji Bora wa RAG - kutokana na dirisha kubwa la muktadha 
- Uundaji wa Data za Synthetiki - uwezo wa kuunda data madhubuti kwa kazi kama vile kurekebisha mafunzo 

### Kufanya Simu za Vitendo vya Asili 

Llama 3.1 imeboreshwa kuwa na ufanisi zaidi katika kuita vitendo au zana. Pia ina zana mbili zilizojengewa ndani ambazo mfano unaweza kubaini zinahitajika kutumiwa kulingana na ombi kutoka kwa mtumiaji. Zana hizi ni: 

- **Brave Search** - Inaweza kutumika kupata taarifa za hivi punde kama hali ya hewa kwa kufanya utafutaji mtandaoni 
- **Wolfram Alpha** - Inaweza kutumika kwa hesabu tata za kihisabati kwa hivyo sio lazima uandike vitendo vyako mwenyewe. 

Unaweza pia kuunda zana zako binafsi ambazo LLM inaweza kuita. 

Katika mfano wa msimbo ufuatao: 

- Tunataja zana zinazopatikana (brave_search, wolfram_alpha) katika ombi la mfumo. 
- Tuma ombi la mtumiaji linalouliza kuhusu hali ya hewa katika mji fulani. 
- LLM itajibu kwa simu ya zana kwa zana ya Brave Search ambayo itaonekana kama hii `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Kumbuka: Mfano huu hufanya simu ya zana tu, ikiwa ungependa kupata matokeo, utahitaji kuunda akaunti bure kwenye ukurasa wa API wa Brave na ueleze vitendo yenyewe.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Pata haya kutoka kwenye ukurasa wa "Muhtasari" wa mradi wako wa Microsoft Foundry
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

Licha ya kuwa LLM, ukosefu mmoja wa Llama 3.1 ni kutokuwa na multimodality. Yaani, kushindwa kutumia aina mbalimbali za pembejeo kama picha kama mabango na kutoa majibu. Uwezo huu ni moja ya sifa kuu za Llama 3.2. Sifa hizi pia ni pamoja na: 

- Multimodality - ina uwezo wa kutathmini mabango ya maandishi na picha 
- Tofauti za ukubwa mdogo hadi wa wastani (11B na 90B) - hii inatoa chaguo zinazobadilika za usambazaji, 
- Tofauti za maandishi pekee (1B na 3B) - hii inaruhusu mfano kuwekwa katika vifaa vya edge / simu na huleta ucheleweshaji mdogo 

Usaidizi wa multimodal ni hatua kubwa katika dunia ya modeli za chanzo wazi. Mfano wa msimbo ufuatao unachukua picha na ombi la maandishi ili kupata uchambuzi wa picha kutoka Llama 3.2 90B. 


### Usaidizi wa Multimodal na Llama 3.2

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

## Kujifunza haikuishii hapa, endelea safari

Baada ya kumaliza somo hili, angalia [Mkusanyiko wa Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza maarifa yako ya AI ya Kizazi!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->