# Рад са Meta породичним моделима

## Увод

Овај час покрива:

- Истраживање два главна Meta породична модела - Llama 3.1 и Llama 3.2
- Разумевање примене и сценарија за сваки модел
- Примере кода који приказују јединствене карактеристике сваког модела

## Meta породица модела

У овом часу ћемо истражити 2 модела из Meta породице или „Llama Herd“ - Llama 3.1 и Llama 3.2.

Ови модели долазе у различитим варијантама и доступни су на GitHub Model marketplace-у. Ево више детаља о коришћењу GitHub модела за [прототипирање са AI моделима](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Варијанте модела:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Напомена: Llama 3 је такође доступан на GitHub Models, али неће бити обрађен у овом часу*

## Llama 3.1

Са 405 милијарди параметара, Llama 3.1 спада у категорију open source LLM модела.

Модел је надоградња ранијег издања Llama 3 нудећи:

- Већи контекстуални прозор - 128к токена уместо 8к токена
- Већи максимални број излазних токена - 4096 уместо 2048
- Боља мултилингвистичка подршка - због повећања броја токена у тренингу

Ово омогућава Llama 3.1 да руководи комплекснијим случајевима употребе приликом израде GenAI апликација укључујући:  
- Нативно позивање функција - могућност позивања спољних алата и функција ван LLM протока рада  
- Боље перформансе RAG-а - због већег контекстуалног прозора  
- Синтетичка генерација података - могућност креирања ефикасних података за задатке као што је финетјунинг  

### Нативно позивање функција

Llama 3.1 је фино подешен да буде ефикаснији у позивању функција или алата. Такође има два уграђена алата које модел може препознати да треба користити на основу корисничког упита. Ови алати су:

- **Brave Search** - Може се користити за добијање ажурираних информација као што је време путем веб претраге  
- **Wolfram Alpha** - Може се користити за сложене математичке прорачуне па није потребно писати своје функције  

Такође можете креирати своје прилагођене алате које LLM може позивати.

У примеру кода испод:

- Дефинишемо расположиве алате (brave_search, wolfram_alpha) у системском упиту.  
- Сламо кориснички упит који пита о времену у одређеном граду.  
- LLM ће одговорити позивом алата Brave Search који ће изгледати овако `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Напомена: Овај пример само позива алат, ако желите добити резултате, потребно је да креирате бесплатан налог на Brave API страници и дефинишете саму функцију.*

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

Иако је LLM, једно ограничење Llama 3.1 је недостатак мултимодалности. То јест, неспособност коришћења различитих типова улазних података као што су слике као упити и пружања одговора. Ова способност је једна од главних карактеристика Llama 3.2. Ове карактеристике укључују и:

- Мултимодалност - способност процене како текстуалних тако и сликовних упита  
- Варијације мале до средње величине (11B и 90B) - пружају флексибилне опције за имплементацију,  
- Само текстуалне варијације (1B и 3B) - омогућавају примену на edge / мобилним уређајима и обезбеђују ниску латенцију  

Подршка мултимодалности представља велики корак у свету open source модела. Пример кода испод узима као улаз и слику и текстуални упит да добије анализу слике од Llama 3.2 90B.

### Подршка мултимодалности са Llama 3.2

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

## Ученије овде не престаје, наставите путовање

Након завршетка овог часа, погледајте нашу [Generative AI Learning колекцију](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) да наставите усавршавање својих знања о генеративној вештачкој интелигенцији!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да превод буде прецизан, молимо имајте у виду да аутоматски преводи могу да садрже грешке или нетачности. Оригинални документ на његовом матерњем језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Не преузимамо одговорност за било каква неспоразуми или погрешне тумачења која могу произаћи из употребе овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->