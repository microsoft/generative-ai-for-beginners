# Рад са моделима из породице Meta

## Увод

Ова лекција ће обухватити:

- Истраживање двa главнa модела из породице Meta - Llama 3.1 и Llama 3.2, као и тренутно доступне алтернативе коришћене у примерима кода (Llama 3.3 и Llama 4)
- Разумевање сценарија и случајева употребе за сваки модел
- Пример кода који приказује јединствене карактеристике сваког модела


## Породица Meta модела

У овој лекцији ћемо истражити 2 модела из породице Meta или "Llama Herd" - Llama 3.1 и Llama 3.2. Покретни примери кода користе Llama 3.3 и Llama 4, који су тренутно доступне алтернативе у каталогу Microsoft Foundry Models.

Ови модели долазе у различитим варијантама и доступни су у [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Напомена:** GitHub Models престаје са радом крајем јула 2026. Више детаља о коришћењу [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) за прототипизацију са AI моделима.

> **Напомена:** Конкретне верзије модела на којима је ова лекција првобитно базирана (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct) су од тада повучене из каталога Microsoft Foundry Models. Примери кода испод користе `Llama-3.3-70B-Instruct` и `Llama-4-Scout-17B-16E-Instruct` као тренутно доступне алтернативе у каталогу Microsoft Foundry Models, тако да и даље функционишу данас.

Варијанте модела (као што је првобитно објашњено у овој лекцији):
- Llama 3.1 - 70B Instruct (повучен)
- Llama 3.1 - 405B Instruct (повучен)
- Llama 3.2 - 11B Vision Instruct (повучен)
- Llama 3.2 - 90B Vision Instruct (повучен)

Тренутно доступне алтернативе коришћене у примерима кода:
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`)
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`)

*Напомена: Варијанте Llama 3 о којима је горе било речи задржане су из историјских разлога и више нису доступне у Microsoft Foundry Models.*

## Llama 3.1

Са 405 милијарди параметара, Llama 3.1 спада у категорију отворених LLM модела.

Модел је надоградња ранијег издања Llama 3 нудећи:

- Веће контекстно окно - 128k токена уместо 8k токена
- Већи максимални број излазних токена - 4096 уместо 2048
- Боља подршка за више језика - због повећања броја токена за тренирање

Ово омогућава Llama 3.1 да обрађује сложеније случајеве употребе у изградњи GenAI апликација укључујући:
- Нативно позивање функција - способност позивања екстерних алата и функција ван LLM радног тока
- Боље перформансе RAG-а - због већег контекстног окна
- Генерацију синтетичких података - способност креирања ефективних података за задатке као што је фино подешавање

### Нативно позивање функција

Llama 3.1 је фино подешен за ефикасније позивање функција или алата. Такође има два уграђена алата која модел може препознати да треба користити на основу корисничког упита. Ови алати су:

- **Brave Search** - Може се користити за добијање ажурираних информација као што је време вршећи веб претрагу
- **Wolfram Alpha** - Може се користити за комплексније математичке прорачуне тако да није потребно писање властитих функција.

Такође можете креирати своје прилагођене алате које LLM може позивати.

У примеру кода испод:

- Дефинишемо доступне алате (brave_search, wolfram_alpha) у системском упиту.
- Слањем корисничког упита који пита за време у одређеном граду.
- LLM ће одговорити позивом алата за Brave Search који ће изгледати овако `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Напомена: Овај пример само прави позив алату, ако желите да добијете резултате, потребно је да направите бесплатан налог на страници Brave API и дефинишете саму функцију.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Meta-Llama-3.1-405B-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-3.3-70B-Instruct, a currently available alternative, instead
model_name = "Llama-3.3-70B-Instruct"

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

Иако је LLM, једно ограничење Llama 3.1 је недостатак мултимодалности. То јест, неспособност коришћења различитих врста уноса као што су слике као упити и давање одговора. Ова способност је једна од главних карактеристика Llama 3.2. Ове функције укључују и:

- Мултимодалност - способност да се процене и текст и слике као упити
- Варијације малих до средњих величина (11B и 90B) - што пружа флексибилне опције за имплементацију,
- Само текстуалне варијације (1B и 3B) - омогућавају да се модел користи на ивичним/мобилним уређајима и пружају ниску латенцију

Подршка за мултимодалност представља велики помак у свету отворених модела. Пример кода испод узима и слику и текстуални упит за добијање анализе слике. Пошто је Llama 3.2 90B Vision Instruct повучен, пример користи `Llama-4-Scout-17B-16E-Instruct`, тренутно доступну нативно мултимодалну алтернативу.


### Мултимодална подршка са Llama 3.2

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

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Llama-3.2-90B-Vision-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-4-Scout-17B-16E-Instruct, a currently available natively multimodal alternative, instead
model_name = "Llama-4-Scout-17B-16E-Instruct"

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

## Учење се овде не зауставља, наставите путовање

Након завршетка ове лекције, погледајте нашу [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) како бисте наставили да развијате своје знање о генеративној вештачкој интелигенцији!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->