# Kujenga Kwa Miundo ya Familia ya Meta

## Utangulizi

Somo hili litashughulikia:

- Kuchunguza miundo kuu miwili ya familia ya Meta - Llama 3.1 na Llama 3.2
- Kuelewa matumizi na matukio ya kila mfano
- Mfano wa msimbo kuonyesha sifa za kipekee za kila mfano

## Familia ya Miundo ya Meta

Katika somo hili, tutachunguza miundo 2 kutoka kwa familia ya Meta au "Llama Herd" - Llama 3.1 na Llama 3.2.

Miundo hii inakuja katika aina tofauti na inapatikana kwenye soko la GitHub Model. Hapa kuna maelezo zaidi juu ya kutumia GitHub Models ku [fanya majaribio na miundo ya AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Aina za Miundo:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Kumbuka: Llama 3 pia inapatikana kwenye GitHub Models lakini haitashughulikiwa katika somo hili*

## Llama 3.1

Kwa Parameta Bilioni 405, Llama 3.1 inaingia katika kundi la LLM za chanzo huria.

Mfano huu ni sasisho la toleo la awali Llama 3 kwa kutoa:

- Dirisha kubwa la muktadha - tokeni 128k dhidi ya tokeni 8k
- Max Output Tokens kubwa - 4096 dhidi ya 2048
- Msaada Bora wa Lugha Nyingi - kutokana na ongezeko la tokeni za mafunzo

Hizi zinamruhusu Llama 3.1 kushughulikia matumizi changamani zaidi wakati wa kujenga programu za GenAI ikiwemo:
- Kupiga Simu za Kazi Asilia - uwezo wa kupiga simu kwa zana na kazi za nje ya mtiririko wa LLM
- Utendaji Bora wa RAG - kutokana na dirisha kubwa la muktadha
- Uundaji wa Data Bandia - uwezo wa kuunda data yenye ufanisi kwa kazi kama vile kuboresha mafunzo

### Kupiga Simu za Kazi Asilia

Llama 3.1 imeboreshwa ili kuwa na ufanisi zaidi katika kupiga simu za kazi au zana. Pia ina zana mbili zilizojengewa ndani ambazo mfano unaweza kubaini zinahitaji kutumika kulingana na maelekezo kutoka kwa mtumiaji. Zana hizi ni:

- **Brave Search** - Inaweza kutumika kupata taarifa za hivi karibuni kama hali ya hewa kwa kufanya utafutaji wa wavuti
- **Wolfram Alpha** - Inaweza kutumika kwa hesabu tata za hisabati hivyo kuandika kazi zako mwenyewe si lazima.

Unaweza pia kuunda zana zako maalum ambazo LLM inaweza kuzipiga simu.

Katika mfano wa msimbo hapa chini:

- Tunaelezea zana zinazopatikana (brave_search, wolfram_alpha) katika maelekezo ya mfumo.
- Kutuma maelekezo ya mtumiaji yanayoulizia kuhusu hali ya hewa katika mji fulani.
- LLM itajibu kwa simu ya zana ya Brave Search ambayo itaonekana kama hii `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Kumbuka: Mfano huu unapiga simu ya zana tu, ikiwa ungependa kupata matokeo, utahitaji kuunda akaunti ya bure kwenye ukurasa wa Brave API na kufafanua kazi yenyewe.*

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

Licha ya kuwa LLM, moja ya kikomo cha Llama 3.1 ni ukosefu wa multimodality. Yaani, kushindwa kutumia aina tofauti za maingizo kama picha kama maelekezo na kutoa majibu. Uwezo huu ni moja ya sifa kuu za Llama 3.2. Sifa hizi pia ni pamoja na:

- Multimodality - ina uwezo wa kutathmini maelekezo ya maandishi na picha
- Aina ndogo hadi za kati (11B na 90B) - hii inatoa chaguzi za uanzishaji zinazoeleweka,
- Aina za maandishi tu (1B na 3B) - hii inaruhusu mfano kuwekwa kwenye vifaa vya edge / simu na kutoa ucheleweshaji mdogo

Msaada wa multimodal ni hatua kubwa katika ulimwengu wa miundo ya chanzo huria. Mfano wa msimbo hapa chini unachukua picha na maelekezo ya maandishi kupata uchambuzi wa picha kutoka Llama 3.2 90B.

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

## Kujifunza hakukomi hapa, endelea na safari

Baada ya kumaliza somo hili, angalia [Mkusanyiko wetu wa Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza ufahamu wako wa AI ya Kizazi!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiarifa**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi usahihi, tafadhali fahamu kwamba tafsiri za moja kwa moja zinaweza kuwa na makosa au ukosefu wa usahihi. Hati asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu na ya binadamu inapendekezwa. Hatuwezi kuwajibika kwa kutoelewana au tafsiri potofu zitokanazo na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->