# Създаване с моделите от семейството Meta 

## Въведение 

В този урок ще разгледаме: 

- Изследване на двата основни модела от семейството Meta - Llama 3.1 и Llama 3.2 
- Разбиране на случаите на използване и сценариите за всеки модел 
- Примери с код, показващи уникалните характеристики на всеки модел 


## Семейство модели Meta 

В този урок ще разгледаме 2 модела от семейството Meta или "стадото Llama" - Llama 3.1 и Llama 3.2.

Тези модели идват в различни варианти и са налични в [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Забележка:** GitHub Models ще бъде прекратен в края на юли 2026 г. Ето повече подробности за използването на [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) за прототипиране с AI модели.

Варианти на моделите: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Забележка: Llama 3 също е наличен в Microsoft Foundry Models, но няма да бъде разглеждан в този урок*

## Llama 3.1 

С 405 милиарда параметри, Llama 3.1 попада в категорията на отворените LLM.

Моделът е надграждане на по-ранната версия Llama 3 като предлага: 

- По-голям контекстен прозорец - 128k токена срещу 8k токена 
- По-голям максимален брой изходни токени - 4096 срещу 2048 
- По-добра многоезична поддръжка - благодарение на увеличението в обучителните токени 

Това позволява на Llama 3.1 да обработва по-сложни случаи при създаване на GenAI приложения, включително: 
- Вградена поддръжка за извикване на функции - възможността за извикване на външни инструменти и функции извън работния процес на LLM
- По-добра RAG производителност - поради по-големия контекстен прозорец 
- Генериране на синтетични данни - възможността за създаване на ефективни данни за задачи като дообучение 

### Вградена поддръжка за извикване на функции 

Llama 3.1 е фино настроен да бъде по-ефективен при извикване на функции или инструменти. Той също така има два вградени инструмента, които моделът може да разпознае, че е необходимо да използва в зависимост от подадения от потребителя промпт. Тези инструменти са: 

- **Brave Search** - може да се използва за получаване на актуална информация като прогноза за времето чрез уеб търсене 
- **Wolfram Alpha** - може да се използва за по-сложни математически изчисления, така че не е необходимо да се пишат собствени функции. 

Можете също да създадете свои собствени персонализирани инструменти, които LLM може да извиква. 

В примерния код по-долу: 

- Дефинираме наличните инструменти (brave_search, wolfram_alpha) в системния промпт. 
- Изпращаме потребителски промпт, който пита за времето в определен град. 
- LLM ще отговори с извикване на инструмента Brave Search, което ще изглежда така `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Забележка: Този пример само извиква инструмента, ако искате да получите резултатите, ще трябва да създадете безплатен акаунт на страницата на Brave API и да дефинирате самата функция.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Вземете ги от страницата "Преглед" на вашия проект Microsoft Foundry
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

Въпреки че е LLM, едно ограничение на Llama 3.1 е липсата на мултимодалност. Това е неспособността да се използват различни видове входни данни като изображения за промпти и да се предоставят отговори. Тази възможност е една от основните характеристики на Llama 3.2. Тези характеристики включват също: 

- Мултимодалност - способност да оценява както текстови, така и визуални промпти 
- Малки до средни размери вариации (11B и 90B) - това осигурява гъвкави опции за внедряване
- Текстови вариации (1B и 3B) - това позволява моделът да бъде внедрен на крайни / мобилни устройства и осигурява ниска латентност 

Мултимодалната поддръжка представлява голяма стъпка в света на отворените модели. Примерният код по-долу приема както изображение, така и текстов промпт, за да получи анализ на изображението от Llama 3.2 90B. 


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

# Получете тези от страницата "Общ преглед" на вашия проект Microsoft Foundry
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

## Обучението не спира тук, продължете пътешествието

След завършване на този урок, разгледайте нашата [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), за да продължите да развивате знанията си в генериращия AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->