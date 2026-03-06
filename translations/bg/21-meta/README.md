# Създаване с моделите от семейството Meta

## Въведение

Този урок ще обхване:

- Изследване на двата основни модела от семейството Meta - Llama 3.1 и Llama 3.2
- Разбиране на случаите на използване и сценариите за всеки модел
- Примерен код, показващ уникалните характеристики на всеки модел

## Семейството модели Meta

В този урок ще разгледаме 2 модела от семейството Meta или "Llama Herd" - Llama 3.1 и Llama 3.2.

Тези модели се предлагат в различни варианти и са достъпни на пазара за модели в GitHub. По-долу има повече подробности за използването на GitHub модели за [прототипиране с AI модели](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Варианти на модели:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Забележка: Llama 3 също е наличен в GitHub модели, но няма да бъде разглеждан в този урок*

## Llama 3.1

С 405 милиарда параметри, Llama 3.1 попада в категорията на отворени LLM.

Моделът е ъпгрейд на по-ранното издание Llama 3, като предлага:

- По-голям контекстен прозорец - 128к токена спрямо 8к токена
- По-голям Max Output Tokens - 4096 спрямо 2048
- По-добра многоезична поддръжка - благодарение на увеличеното количество токени за обучение

Тези подобрения позволяват на Llama 3.1 да се справя с по-сложни случаи на използване при изграждането на GenAI приложения, включително:
- Роден извикване на функции - възможност за извикване на външни инструменти и функции извън работния процес на LLM
- По-добра RAG ефективност - благодарение на по-големия контекстен прозорец
- Генериране на синтетични данни - възможност за създаване на ефективни данни за задачи като фино настройване

### Родено извикване на функции

Llama 3.1 е допълнително обучен да бъде по-ефективен при извикване на функции или инструменти. Той разполага и с два вградени инструмента, които моделът може да идентифицира като необходими за използване според подадения от потребителя въпрос. Тези инструменти са:

- **Brave Search** - може да се използва за получаване на актуална информация като прогнозата за времето чрез уеб търсене
- **Wolfram Alpha** - може да се използва за по-сложни математически изчисления, така че не е необходимо писане на собствени функции.

Можете също така да създадете свои собствени инструменти, които LLM може да извиква.

В примерния код по-долу:

- Дефинираме наличните инструменти (brave_search, wolfram_alpha) в системния промпт.
- Изпращаме въпрос от потребителя, който пита за времето в определен град.
- LLM ще отговори с извикване на инструмента Brave Search, което ще изглежда така: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Забележка: Този пример само извършва извикване на инструмента, ако желаете да получите резултатите, ще трябва да създадете безплатен акаунт на страницата на Brave API и да дефинирате самата функция.

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

Въпреки че е LLM, едно ограничение на Llama 3.1 е липсата на мултимодалност. Това е неспособността да се използват различни видове входни данни, като изображения, като промпти и да се дадат отговори. Тази възможност е една от основните характеристики на Llama 3.2. Тези характеристики включват също:

- Мултимодалност - има способността да оценява както текстови, така и изображенчески промпти
- Вариации в малък до среден размер (11B и 90B) - това осигурява гъвкави опции за внедряване,
- Вариации само с текст (1B и 3B) - това позволява да се внедри моделът на крайни/mobile устройства и осигурява ниска латентност

Поддръжката на мултимодалността представлява голяма крачка в света на отворените модели. Примерният код по-долу приема както изображение, така и текстов промпт, за да получи анализ на изображението от Llama 3.2 90B.

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

## Учението не спира тук, продължете пътуването

След като завършите този урок, разгледайте нашата [колекция за обучение в Генеративен AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), за да продължите да повишавате знанията си за Генеративен AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с използване на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->