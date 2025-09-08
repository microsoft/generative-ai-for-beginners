<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:13:35+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "sr"
}
-->
# Рад са моделима из Meta породице

## Увод

Овај час ће обухватити:

- Истраживање два главна Meta породична модела - Llama 3.1 и Llama 3.2
- Разумевање случајева употребе и сценарија за сваки модел
- Пример кода који показује јединствене карактеристике сваког модела

## Meta породица модела

У овом часу ћемо истражити 2 модела из Meta породице или „Llama Herd“ - Llama 3.1 и Llama 3.2

Ови модели долазе у различитим варијантама и доступни су на GitHub Model marketplace-у. Ево више детаља о коришћењу GitHub модела за [прототиповање са AI моделима](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Варијанте модела:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Напомена: Llama 3 је такође доступан на GitHub Models али неће бити обрађен у овом часу*

## Llama 3.1

Са 405 милијарди параметара, Llama 3.1 спада у категорију отворених LLM модела.

Овај модел је надоградња раније верзије Llama 3 и нуди:

- Веће контекстно окно - 128k токена уместо 8k токена
- Већи максимални број излазних токена - 4096 уместо 2048
- Бољу подршку за више језика - захваљујући повећаном броју токена у тренингу

Ово омогућава Llama 3.1 да се носи са сложенијим случајевима употребе приликом израде GenAI апликација, укључујући:
- Native Function Calling - могућност позивања спољних алата и функција ван LLM радног тока
- Боље RAG перформансе - захваљујући већем контекстном окну
- Генерисање синтетичких података - могућност креирања ефикасних података за задатке као што је фино подешавање

### Native Function Calling

Llama 3.1 је фино подешен да буде ефикаснији у позивању функција или алата. Такође има два уграђена алата која модел може препознати као потребна за коришћење на основу упита корисника. Та два алата су:

- **Brave Search** - може се користити за добијање ажурираних информација као што је време, путем претраге на вебу
- **Wolfram Alpha** - може се користити за сложеније математичке прорачуне, тако да није потребно писати своје функције

Такође можете креирати своје прилагођене алате које LLM може позивати.

У примеру кода испод:

- Дефинишемо доступне алате (brave_search, wolfram_alpha) у системском упиту.
- Слањем корисничког упита који пита за време у одређеном граду.
- LLM ће одговорити позивом алата Brave Search који ће изгледати овако `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Напомена: Овај пример само прави позив алата, ако желите да добијете резултате, потребно је да направите бесплатан налог на Brave API страници и дефинишете саму функцију*

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

Иако је LLM, једно ограничење Llama 3.1 је мултимодалност. То значи могућност коришћења различитих типова улаза као што су слике као упити и пружање одговора. Ова способност је једна од главних карактеристика Llama 3.2. Ове карактеристике укључују и:

- Мултимодалност - способност да обрађује и текстуалне и сликовне упите
- Варијанте мале и средње величине (11B и 90B) - пружају флексибилне опције за имплементацију
- Варијанте само за текст (1B и 3B) - омогућавају покретање модела на edge / мобилним уређајима и пружају ниску латенцију

Подршка мултимодалности представља велики корак у свету отворених модела. Пример кода испод користи и слику и текстуални упит да добије анализу слике од Llama 3.2 90B.

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

## Учење овде не престаје, наставите путовање

Након завршетка овог часа, погледајте нашу [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) да наставите да унапређујете своје знање о генеративној вештачкој интелигенцији!

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.