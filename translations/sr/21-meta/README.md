# Прављење са Мета породичним моделима 

## Увод 

Ова лекција ће обухватити: 

- Истраживање два главна Мета породична модела - Llama 3.1 и Llama 3.2 
- Разумевање случајева употребе и сценарија за сваки модел 
- Пример кода који показује јединствене карактеристике сваког модела 


## Мета породица модела 

У овој лекцији ћемо проучити 2 модела из Мета породице или "Llama Herd" - Llama 3.1 и Llama 3.2.

Ови модели долазе у различитим варијантама и доступни су у [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Напомена:** GitHub Models се укида крајем јула 2026. Више детаља о коришћењу [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) за прототипирање са AI моделима можете пронаћи овде.

Варијанте модела: 
- Llama 3.1 - 70B Инструкт 
- Llama 3.1 - 405B Инструкт 
- Llama 3.2 - 11B Vision Инструкт 
- Llama 3.2 - 90B Vision Инструкт 

*Напомена: Llama 3 је такође доступан у Microsoft Foundry Models али неће бити обрађен у овој лекцији*

## Llama 3.1 

Са 405 милијарди параметара, Llama 3.1 спада у категорију отворених LLM модела. 

Модел је надоградња у односу на ранији издање Llama 3 нудећи: 

- Већи контекстни прозор - 128к токена у поређењу са 8к токена 
- Већи Максимални број излазних токена - 4096 уместо 2048 
- Боља мултилингвистичка подршка - због повећања броја токена за обуку 

Ово омогућава Llama 3.1 да решава сложеније случајеве употребе при изради GenAI апликација укључујући: 
- Нативно позивање функција - могућност позива спољних алата и функција изван LLM радног тока
- Боље RAG перформансе - због већег контекстног прозора 
- Генерација синтетичких података - могућност креирања ефикасних података за задатке као што је фино подешавање 

### Нативно позивање функција 

Llama 3.1 је фино подешен да буде ефикаснији у прављењу позива функцијама или алатима. Такође има два уграђена алата која модел може препознати као неопходна за употребу на основу упита корисника. Тим алатима су: 

- **Brave Search** - Може се користити за добијање најсвежијих информација попут времена обављањем претраге веба 
- **Wolfram Alpha** - Може се користити за сложеније математичке прорачуне тако да није потребно писати сопствене функције. 

Такође можете креирати своје прилагођене алате које LLM може позивати. 

У примеру кода испод: 

- Дефинишемо доступне алате (brave_search, wolfram_alpha) у системској поруци. 
- Слањем корисничког упита који пита о времену у одређеном граду. 
- LLM ће одговорити позивом алата ка Brave Search алату који ће изгледати овако `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Напомена: Овај пример само прави позив алату, ако желите да добијете резултате, потребно је да направите бесплатни налог на Brave API страници и дефинишете саму функцију.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Узмите ове из странице „Преглед“ вашег Microsoft Foundry пројекта
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

Иако је LLM, једно ограничење Llama 3.1 је његов недостатак мултимодалности. То јест, неспособност коришћења различитих типова улазних података као што су слике као упити и пружање одговора. Ова способност је једна од главних карактеристика Llama 3.2. Ове карактеристике такође укључују: 

- Мултимодалност - има способност да оцени и текстуалне и сликовне упите 
- Варијације мале до средње величине (11B и 90B) - ово пружа флексибилне опције за имплементацију, 
- Варијације само за текст (1B и 3B) - ово омогућава моделу да се имплементира на уређајима краја мреже / мобилним уређајима и пружа ниску латенцију 

Подршка мултимодалности представља велики корак у свету отворених модела. Пример кода испод узима и слику и текстуални упит за добијање анализе слике од Llama 3.2 90B. 


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

# Узмите ово са странице "Преглед" вашег Microsoft Foundry пројекта
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

## Учивање овде не престаје, наставите путовање

Након завршетка ове лекције, погледајте нашу [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) да бисте наставили да унапређујете своје знање о генеративној вештачкој интелигенцији!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->