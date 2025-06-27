<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:35:51+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "bg"
}
-->
# Изграждане с модели от Meta семейството

## Въведение

Този урок ще обхване:

- Изследване на двата основни модела от Meta семейството - Llama 3.1 и Llama 3.2
- Разбиране на случаите на употреба и сценариите за всеки модел
- Примерен код, който показва уникалните характеристики на всеки модел

## Meta семейството от модели

В този урок ще разгледаме 2 модела от Meta семейството или "Llama стадо" - Llama 3.1 и Llama 3.2

Тези модели се предлагат в различни варианти и са налични на пазара за модели в GitHub. Ето повече информация за използването на GitHub модели за [прототипиране с AI модели](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Варианти на модела:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Забележка: Llama 3 също е наличен на GitHub модели, но няма да бъде разгледан в този урок*

## Llama 3.1

С 405 милиарда параметри, Llama 3.1 се вписва в категорията на отворените LLM.

Моделът е обновление на по-ранната версия Llama 3, като предлага:

- По-голям контекстен прозорец - 128k токени срещу 8k токени
- По-голям максимален брой изходни токени - 4096 срещу 2048
- По-добра многоезична поддръжка - поради увеличението на обучителните токени

Тези възможности позволяват на Llama 3.1 да се справя с по-сложни случаи на употреба при изграждане на GenAI приложения, включително:
- Извикване на родни функции - способността да извиква външни инструменти и функции извън работния процес на LLM
- По-добра RAG производителност - поради по-големия контекстен прозорец
- Генериране на синтетични данни - способността да създава ефективни данни за задачи като фино настройване

### Извикване на родни функции

Llama 3.1 е фино настроен да бъде по-ефективен при извършване на извиквания на функции или инструменти. Той също така има два вградени инструмента, които моделът може да идентифицира като необходими за използване въз основа на потребителския запит. Тези инструменти са:

- **Brave Search** - Може да се използва за получаване на актуална информация като времето чрез извършване на уеб търсене
- **Wolfram Alpha** - Може да се използва за по-сложни математически изчисления, така че не е необходимо да пишете собствени функции.

Можете също така да създадете собствени персонализирани инструменти, които LLM може да извика.

В примера с код по-долу:

- Дефинираме наличните инструменти (brave_search, wolfram_alpha) в системния запит.
- Изпращаме потребителски запит, който пита за времето в определен град.
- LLM ще отговори с извикване на инструмент към Brave Search, което ще изглежда така `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Забележка: Този пример само извършва извикването на инструмента, ако искате да получите резултатите, ще трябва да създадете безплатен акаунт на страницата на Brave API и да дефинирате самата функция*

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

Въпреки че е LLM, едно ограничение, което Llama 3.1 има, е мултимодалността. Тоест, способността да използва различни видове входни данни като изображения за запити и предоставяне на отговори. Тази способност е една от основните характеристики на Llama 3.2. Тези характеристики също включват:

- Мултимодалност - има способността да оценява както текстови, така и визуални запити
- Малки до средни размери (11B и 90B) - това осигурява гъвкави опции за разполагане,
- Само текстови вариации (1B и 3B) - това позволява моделът да бъде разположен на крайни / мобилни устройства и осигурява ниска латентност

Поддръжката на мултимодалност представлява голяма стъпка в света на отворените модели. Примерът с код по-долу използва както изображение, така и текстов запит, за да получи анализ на изображението от Llama 3.2 90B.

### Поддръжка на мултимодалност с Llama 3.2

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

## Обучението не спира тук, продължете пътуването

След завършване на този урок, разгледайте нашата [колекция за обучение по генеративен AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), за да продължите да повишавате знанията си за генеративния AI!

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Докато се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за недоразумения или неправилни интерпретации, възникнали от използването на този превод.