<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:16:27+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "bg"
}
-->
# Създаване с моделите от семейството Meta

## Въведение

Този урок ще обхване:

- Разглеждане на двата основни модела от семейството Meta - Llama 3.1 и Llama 3.2
- Разбиране на случаите на използване и сценариите за всеки модел
- Примерен код, който показва уникалните характеристики на всеки модел

## Семейството модели Meta

В този урок ще разгледаме 2 модела от семейството Meta или "стадото Llama" - Llama 3.1 и Llama 3.2.

Тези модели идват в различни варианти и са достъпни на пазара на модели в GitHub. Ето повече подробности за използването на моделите в GitHub за [прототипиране с AI модели](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Варианти на моделите:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Забележка: Llama 3 също е достъпен на моделите в GitHub, но няма да бъде разглеждан в този урок*

## Llama 3.1

С 405 милиарда параметри, Llama 3.1 се вписва в категорията на отворените източници LLM.

Моделът е надграждане на по-ранното издание Llama 3, като предлага:

- По-голям контекстен прозорец - 128k токена срещу 8k токена
- По-голям максимален брой изходни токени - 4096 срещу 2048
- По-добра многоезична поддръжка - поради увеличаване на обучителните токени

Това позволява на Llama 3.1 да се справя с по-сложни случаи на използване при създаване на приложения за GenAI, включително:
- Възможност за извикване на външни инструменти и функции извън работния поток на LLM
- По-добра производителност на RAG - поради по-високия контекстен прозорец
- Генериране на синтетични данни - способността да се създават ефективни данни за задачи като фино настройване

### Извикване на родни функции

Llama 3.1 е фино настроен да бъде по-ефективен при извикване на функции или инструменти. Той също така има два вградени инструмента, които моделът може да идентифицира като нуждаещи се от използване, въз основа на подкана от потребителя. Тези инструменти са:

- **Brave Search** - Може да се използва за получаване на актуална информация като времето чрез извършване на уеб търсене
- **Wolfram Alpha** - Може да се използва за по-сложни математически изчисления, така че писането на собствени функции не е необходимо.

Можете също така да създадете свои собствени персонализирани инструменти, които LLM може да извиква.

В примера за код по-долу:

- Определяме наличните инструменти (brave_search, wolfram_alpha) в системната подкана.
- Изпращаме потребителска подкана, която пита за времето в определен град.
- LLM ще отговори с извикване на инструмента Brave Search, което ще изглежда така `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Забележка: Този пример само извиква инструмента, ако искате да получите резултатите, ще трябва да създадете безплатен акаунт на страницата на Brave API и да определите самата функция*

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

Въпреки че е LLM, едно ограничение, което Llama 3.1 има, е мултимодалността. Тоест, способността да използва различни видове входни данни, като изображения като подкани и предоставяне на отговори. Тази способност е една от основните характеристики на Llama 3.2. Тези характеристики включват:

- Мултимодалност - има способността да оценява както текстови, така и изображенски подкани
- Малки до средни размери (11B и 90B) - това предоставя гъвкави опции за внедряване
- Само текстови варианти (1B и 3B) - това позволява моделът да бъде внедрен на edge / мобилни устройства и предоставя ниска латентност

Мултимодалната поддръжка представлява голяма стъпка в света на моделите с отворен код. Примерът за код по-долу взема както изображение, така и текстова подкана, за да получи анализ на изображението от Llama 3.2 90B.

### Мултимодална поддръжка с Llama 3.2

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

## Учението не спира тук, продължете пътешествието

След като завършите този урок, разгледайте нашата [колекция за обучение по Генеративен AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), за да продължите да развивате своите знания по Генеративен AI!

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на родния му език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни тълкувания, произтичащи от използването на този превод.