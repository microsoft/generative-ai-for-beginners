<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:34:26+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "sw"
}
-->
# Kujenga Kwa Kutumia Miundo ya Familia ya Meta

## Utangulizi

Somo hili litashughulikia:

- Kuchunguza miundo miwili mikuu ya familia ya Meta - Llama 3.1 na Llama 3.2
- Kuelewa matumizi na hali za kila mfano
- Mfano wa msimbo kuonyesha vipengele vya kipekee vya kila mfano

## Familia ya Miundo ya Meta

Katika somo hili, tutachunguza miundo miwili kutoka familia ya Meta au "Herd ya Llama" - Llama 3.1 na Llama 3.2

Miundo hii inakuja katika tofauti mbalimbali na inapatikana kwenye soko la GitHub Model. Hapa kuna maelezo zaidi kuhusu kutumia GitHub Models ku [unda mfano na AI models](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Tofauti za Mfano:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Kumbuka: Llama 3 pia inapatikana kwenye GitHub Models lakini haitashughulikiwa katika somo hili*

## Llama 3.1

Kwa vigezo Bilioni 405, Llama 3.1 inafaa katika jamii ya LLM ya chanzo wazi.

Mfano huu ni uboreshaji wa toleo la awali Llama 3 kwa kutoa:

- Dirisha kubwa la muktadha - ishara 128k dhidi ya ishara 8k
- Ishara za Matokeo ya Juu Zaidi - 4096 dhidi ya 2048
- Usaidizi Bora wa Lugha Mbalimbali - kutokana na ongezeko la ishara za mafunzo

Hii inaruhusu Llama 3.1 kushughulikia kesi ngumu zaidi za matumizi wakati wa kujenga programu za GenAI ikiwa ni pamoja na:
- Kuita Kazi za Asili - uwezo wa kuita zana na kazi za nje nje ya mchakato wa LLM
- Utendaji Bora wa RAG - kutokana na dirisha la muktadha mkubwa
- Uzalishaji wa Data Bandia - uwezo wa kuunda data madhubuti kwa kazi kama vile kurekebisha

### Kuita Kazi za Asili

Llama 3.1 imeboreshwa kuwa bora zaidi katika kufanya miito ya kazi au zana. Pia ina zana mbili zilizojengwa ndani ambazo mfano unaweza kutambua kama zinahitaji kutumiwa kulingana na maelekezo kutoka kwa mtumiaji. Zana hizi ni:

- **Brave Search** - Inaweza kutumika kupata habari za sasa kama hali ya hewa kwa kufanya utafutaji wa mtandao
- **Wolfram Alpha** - Inaweza kutumika kwa mahesabu ya hisabati changamano zaidi hivyo kuandika kazi zako mwenyewe hakuhitajiki.

Unaweza pia kuunda zana zako maalum ambazo LLM inaweza kuita.

Katika mfano wa msimbo hapa chini:

- Tunaelezea zana zinazopatikana (brave_search, wolfram_alpha) katika maelekezo ya mfumo.
- Tuma maelekezo ya mtumiaji yanayouliza kuhusu hali ya hewa katika jiji fulani.
- LLM itajibu kwa kuita zana ya Brave Search ambayo itaonekana kama hii `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Kumbuka: Mfano huu unafanya tu mwito wa zana, ikiwa ungependa kupata matokeo, utahitaji kuunda akaunti ya bure kwenye ukurasa wa Brave API na kufafanua kazi yenyewe*

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

Licha ya kuwa LLM, moja ya vikwazo ambavyo Llama 3.1 ina ni uwezo wa kutumia njia nyingi. Yaani, kuwa na uwezo wa kutumia aina tofauti za pembejeo kama vile picha kama maelekezo na kutoa majibu. Uwezo huu ni moja ya sifa kuu za Llama 3.2. Vipengele hivi pia ni pamoja na:

- Uwezo wa kutumia njia nyingi - ina uwezo wa kutathmini maelekezo ya maandishi na picha
- Tofauti za ukubwa wa Kati hadi Ndogo (11B na 90B) - hii inatoa chaguzi za kubadilika za kupeleka,
- Tofauti za maandishi pekee (1B na 3B) - hii inaruhusu mfano kupelekwa kwenye vifaa vya pembeni / simu na kutoa ucheleweshaji mdogo

Msaada wa kutumia njia nyingi unawakilisha hatua kubwa katika ulimwengu wa miundo ya chanzo wazi. Mfano wa msimbo hapa chini unachukua picha na maelekezo ya maandishi kupata uchambuzi wa picha kutoka Llama 3.2 90B.

### Msaada wa Kutumia Njia Nyingi na Llama 3.2

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

Baada ya kukamilisha somo hili, angalia [Mkusanyiko wa Kujifunza wa AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuboresha maarifa yako ya AI ya Kizazi!

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au kutafsiri vibaya kunakotokana na matumizi ya tafsiri hii.