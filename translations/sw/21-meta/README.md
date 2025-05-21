<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:14:57+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "sw"
}
-->
# Kujenga na Mifano ya Familia ya Meta

## Utangulizi

Somo hili litaangazia:

- Kuchunguza mifano miwili kuu ya familia ya Meta - Llama 3.1 na Llama 3.2
- Kuelewa matumizi na hali za kila mfano
- Mfano wa msimbo kuonyesha sifa za kipekee za kila mfano

## Familia ya Mifano ya Meta

Katika somo hili, tutachunguza mifano 2 kutoka familia ya Meta au "Llama Herd" - Llama 3.1 na Llama 3.2

Mifano hii inakuja katika aina tofauti na inapatikana kwenye soko la mifano la GitHub. Hapa kuna maelezo zaidi kuhusu kutumia Mifano ya GitHub [kutengeneza prototipu na mifano ya AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Aina za Mfano:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Kumbuka: Llama 3 pia inapatikana kwenye Mifano ya GitHub lakini haitajadiliwa katika somo hili*

## Llama 3.1

Kwa Parameters Bilioni 405, Llama 3.1 inaingia katika kundi la LLM za chanzo wazi.

Mfano huu ni uboreshaji wa toleo la awali Llama 3 kwa kutoa:

- Dirisha kubwa la muktadha - alama 128k dhidi ya alama 8k
- Alama za Max Output kubwa - 4096 dhidi ya 2048
- Msaada bora wa lugha nyingi - kutokana na ongezeko la alama za mafunzo

Hii inawezesha Llama 3.1 kushughulikia matumizi magumu zaidi wakati wa kujenga programu za GenAI ikiwa ni pamoja na:
- Kupiga Simu za Kazi za Asili - uwezo wa kupiga simu za zana na kazi za nje ya mtiririko wa kazi wa LLM
- Utendaji Bora wa RAG - kutokana na dirisha kubwa la muktadha
- Uzalishaji wa Takwimu Bandia - uwezo wa kuunda data bora kwa kazi kama vile kurekebisha

### Kupiga Simu za Kazi za Asili

Llama 3.1 imeboreshwa kuwa bora zaidi katika kupiga simu za kazi au zana. Pia ina zana mbili zilizojengwa ndani ambazo mfano unaweza kutambua kama zinahitajika kutumika kulingana na agizo kutoka kwa mtumiaji. Zana hizi ni:

- **Brave Search** - Inaweza kutumika kupata taarifa za kisasa kama hali ya hewa kwa kufanya utafutaji wa wavuti
- **Wolfram Alpha** - Inaweza kutumika kwa mahesabu magumu zaidi ya kihisabati hivyo kuandika kazi zako mwenyewe hakuhitajiki.

Unaweza pia kuunda zana zako mwenyewe ambazo LLM inaweza kupiga simu.

Katika mfano wa msimbo hapa chini:

- Tunaelezea zana zinazopatikana (brave_search, wolfram_alpha) katika agizo la mfumo.
- Tuma agizo la mtumiaji linalouliza kuhusu hali ya hewa katika mji fulani.
- LLM itajibu kwa simu ya zana kwa zana ya Brave Search ambayo itaonekana kama hii `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Kumbuka: Mfano huu unafanya tu simu ya zana, kama ungependa kupata matokeo, utahitaji kuunda akaunti ya bure kwenye ukurasa wa API ya Brave na kuelezea kazi yenyewe*

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

Licha ya kuwa LLM, moja ya mipaka ambayo Llama 3.1 ina ni uwezo wa multimodality. Hii ni, kuwa na uwezo wa kutumia aina tofauti za ingizo kama picha kama maagizo na kutoa majibu. Uwezo huu ni moja ya sifa kuu za Llama 3.2. Sifa hizi pia zinajumuisha:

- Multimodality - ina uwezo wa kutathmini maagizo ya maandishi na picha
- Tofauti za ukubwa mdogo hadi wa kati (11B na 90B) - hii inatoa chaguzi za utekelezaji zinazobadilika,
- Tofauti za maandishi tu (1B na 3B) - hii inaruhusu mfano kutekelezwa kwenye vifaa vya pembeni / simu na kutoa ucheleweshaji mdogo

Msaada wa multimodal unawakilisha hatua kubwa katika ulimwengu wa mifano ya chanzo wazi. Mfano wa msimbo hapa chini unachukua picha na maandishi kama agizo kupata uchambuzi wa picha kutoka Llama 3.2 90B.

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

## Kujifunza hakuishii hapa, endelea na Safari

Baada ya kumaliza somo hili, angalia [mkusanyiko wetu wa Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuboresha ujuzi wako wa AI ya Kizazi!

**Kataa:**
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu. Hati asilia katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa habari muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.