# Рад са моделима Meta породице 

## Увод 

Ова лекција ће обухватити: 

- Истраживање два главна Meta модела породице - Llama 3.1 и Llama 3.2 
- Разумевање случајева употребе и сценарија за сваки модел 
- Пример кода који приказује јединствене карактеристике сваког модела 


## Meta породица модела 

У овој лекцији ћемо истражити 2 модела из Meta породице или "Llama Herd" - Llama 3.1 и Llama 3.2.

Ови модели долазе у различитим варијантама и доступни су у [Microsoft Foundry Models каталогу](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Напомена:** GitHub Models престаје са радом крајем јула 2026. Више детаља о коришћењу [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) за прављење прототипова са AI моделима.

Варијанте модела: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Напомена: Llama 3 је такође доступан у Microsoft Foundry Models али неће бити обрађен у овој лекцији*

## Llama 3.1 

Са 405 милијарди параметара, Llama 3.1 спада у категорију отворених LLM модела. 

Модел је надоградња претходног издања Llama 3 нудећи: 

- Већи контекстуални прозор - 128к токена уместо 8к токена 
- Већи максимални број токена за излаз - 4096 уместо 2048 
- Боља подршка за више језика - услед повећања броја токена за тренирање 

Ово омогућава Llama 3.1 да обрађује сложеније случајеве употребе приликом изградње GenAI апликација укључујући: 
- Нативно позивање функција - могућност позива спољних алата и функција ван LLM радног тока
- Боље RAG перформансе - због већег контекстуалног прозора 
- Синтетичка генерација података - могућност креирања ефикасних података за задатке као што је фино подешавање 

### Нативно позивање функција 

Llama 3.1 је фино подешен да буде ефикаснији у позивању функција или алата. Такође има два уграђена алата које модел може препознати да треба да користи на основу упита корисника. Та два алата су: 

- **Brave Search** - Може се користити за добијање најновијих информација као што је време вршењем претраге на вебу 
- **Wolfram Alpha** - Може се користити за сложеније математичке прорачуне тако да није потребно писати сопствене функције. 

Такође можете креирати своје прилагођене алате које LLM може позивати. 

У примеру кода испод: 

- Дефинишемо доступне алате (brave_search, wolfram_alpha) у системском упиту. 
- Слан је кориснички упит који пита за време у одређеном граду. 
- LLM ће одговорити позивом алату Brave Search који ће изгледати овако `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Напомена: Овај пример само прави позив алату, ако желите да добијете резултате, мораћете да направите бесплатан налог на Brave API страници и дефинишете саму функцију.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Узмите ове информације са странице "Преглед" вашег Microsoft Foundry пројекта
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

Иако је LLM, једно од ограничења Llama 3.1 је његов недостатак мултимодалности. То јест, немогућност коришћења различитих типова уноса као што су слике као упити и пружање одговора. Ова могућност је једна од главних карактеристика Llama 3.2. Ове карактеристике укључују и: 

- Мултимодалност - способност да се процењују и текстуални и сликовни упити 
- Варијације мале до средње величине (11B и 90B) - то пружа флексибилне опције за развој, 
- Само текстуалне варијације (1B и 3B) - омогућавају да модел буде развијен на уређајима са ивице / мобилним уређајима и пружају ниску латенцију 

Подршка мултимодалности представља велики корак у свету модела отвореног кода. Пример кода испод користи и слику и текстуални упит за добијање анализе слике од Llama 3.2 90B. 


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

# Узмите ове податке са странице „Преглед“ вашег Microsoft Foundry пројекта
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

## Учење овде не престаје, наставите путовање

Након завршетка ове лекције, погледајте нашу [Generative AI Learning колекцију](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) да наставите да унапређујете своје знање о генеративној вештачкој интелигенцији!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->