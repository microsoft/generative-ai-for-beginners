# Създаване с модели от фамилията Meta 

## Въведение 

Този урок ще обхване: 

- Изследване на двата основни модела от фамилията Meta - Llama 3.1 и Llama 3.2, плюс наличните в момента алтернативи използвани в примерите за код (Llama 3.3 и Llama 4) 
- Разбиране на употребите и сценарии за всеки модел 
- Пример за код, показващ уникалните характеристики на всеки модел 


## Фамилията модели Meta 

В този урок ще разгледаме 2 модела от фамилията Meta или „Роякът Llama“ - Llama 3.1 и Llama 3.2. Изпълнимите примери за код използват Llama 3.3 и Llama 4, които в момента са налични алтернативи в каталога на Microsoft Foundry Models.

Тези модели идват в различни варианти и са налични в [каталога на Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Забележка:** GitHub Models се изключва в края на юли 2026 г. Ето повече подробности за използване на [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) за прототипиране с AI модели.

> **Забележка:** Конкретните версии на моделите, на които този урок първоначално е базиран (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct), вече са изтеглени от каталога на Microsoft Foundry Models. Примерите за код по-долу използват `Llama-3.3-70B-Instruct` и `Llama-4-Scout-17B-16E-Instruct` като налични в момента алтернативи в каталога на Microsoft Foundry Models, затова те все още работят.

Варианти на моделите (както са разгледани първоначално в този урок): 
- Llama 3.1 - 70B Instruct (изтеглен) 
- Llama 3.1 - 405B Instruct (изтеглен) 
- Llama 3.2 - 11B Vision Instruct (изтеглен) 
- Llama 3.2 - 90B Vision Instruct (изтеглен) 

В момента налични алтернативи, използвани в примерите за код: 
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`) 
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`) 

*Забележка: Вариантите на Llama 3, обсъдени по-горе, са запазени за исторически контекст и вече не са налични в Microsoft Foundry Models.*

## Llama 3.1 

С 405 милиарда параметри Llama 3.1 се вписва в категорията отворен код LLM. 

Моделът е ъпгрейд на по-ранното издание Llama 3, като предлага: 

- По-голям контекстен прозорец - 128k токена срещу 8k токена 
- По-голям максимален брой токени за изход - 4096 срещу 2048 
- По-добра многоезична поддръжка - поради увеличението на тренировъчните токени 

Това позволява на Llama 3.1 да обработва по-сложни случаи на употреба при създаване на приложения с генеративен ИИ, включително: 
- Вградено извикване на функции - възможност за извикване на външни инструменти и функции извън работния поток на LLM 
- По-добра производителност при RAG - поради по-големия контекстен прозорец 
- Синтетично генериране на данни - възможност за създаване на ефективни данни за задачи като допълнително обучение 

### Вградено извикване на функции 

Llama 3.1 е дообучен да бъде по-ефективен при извикване на функции или инструменти. Той също така има два вградени инструмента, които моделът може да определи, че трябва да се използват на база на подадената подсказка от потребителя. Тези инструменти са: 

- **Brave Search** - може да се използва за получаване на актуална информация като времето чрез уеб търсене 
- **Wolfram Alpha** - може да се използва за по-сложни математически изчисления, така че не е необходимо писане на собствени функции. 

Можете също да създавате свои собствени инструменти, които LLM може да извиква. 

В примера за код по-долу: 

- Дефинираме достъпните инструменти (brave_search, wolfram_alpha) в системната подсказка. 
- Изпращаме потребителска подсказка, която пита за времето в определен град. 
- LLM ще отговори с извикване на инструмента Brave Search, което ще изглежда така `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Забележка: Този пример само извършва извикването на инструмента, ако желаете да получите резултатите, ще трябва да създадете безплатен акаунт на страницата за Brave API и да дефинирате самата функция.

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

Въпреки че е LLM, едно ограничение на Llama 3.1 е липсата на мултимодалност. Това означава невъзможност за използване на различни типове входни данни като изображения като подсказки и предоставяне на отговори. Тази способност е една от основните характеристики на Llama 3.2. Другите характеристики включват: 

- Мултимодалност - има възможност да оценява както текстови, така и визуални подсказки 
- Вариации с малък до среден размер (11B и 90B) - осигурява гъвкави възможности за внедряване, 
- Вариации само с текст (1B и 3B) - позволява на модела да бъде внедрен на edge / мобилни устройства и осигурява ниска латентност 

Поддръжката на мултимодалност представлява голяма крачка в света на моделите с отворен код. Примерът за код по-долу приема както изображение, така и текстова подсказка за получаване на анализ на изображението. Тъй като Llama 3.2 90B Vision Instruct е изтеглен, примерът използва `Llama-4-Scout-17B-16E-Instruct`, в момента налична нативно мултимодална алтернатива. 


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

## Обучението не спира тук, продължете пътешествието

След като завършите този урок, разгледайте нашата [колекция за учене на Генеративен AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), за да продължите да развивате своите знания за Генеративен AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->