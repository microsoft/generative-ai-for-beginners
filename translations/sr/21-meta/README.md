<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:36:09+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "sr"
}
-->
# Изградња са моделима породице Мета

## Увод

Ова лекција ће покрити:

- Истраживање два главна модела породице Мета - Лама 3.1 и Лама 3.2
- Разумевање случајева употребе и сценарија за сваки модел
- Пример кода који показује јединствене карактеристике сваког модела

## Породица модела Мета

У овој лекцији ћемо истражити 2 модела из породице Мета или "стада Лама" - Лама 3.1 и Лама 3.2

Ови модели долазе у различитим варијантама и доступни су на тржишту модела на ГитХабу. Овде су детаљи о коришћењу ГитХаб модела за [прототиписање са AI моделима](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Варијанте модела:
- Лама 3.1 - 70Б Инструкт
- Лама 3.1 - 405Б Инструкт
- Лама 3.2 - 11Б Визија Инструкт
- Лама 3.2 - 90Б Визија Инструкт

*Напомена: Лама 3 је такође доступна на ГитХаб моделима, али неће бити покривена у овој лекцији*

## Лама 3.1

Са 405 милијарди параметара, Лама 3.1 се уклапа у категорију отвореног кода LLM.

Модел је надоградња претходног издања Лама 3, нудећи:

- Већи прозор контекста - 128k токена наспрам 8k токена
- Већи максимални излазни токени - 4096 наспрам 2048
- Боља подршка за више језика - због повећања броја токена за обуку

Ово омогућава Лами 3.1 да обради сложеније случајеве употребе при изградњи GenAI апликација, укључујући:
- Позивање изворних функција - могућност позивања спољних алата и функција ван LLM радног процеса
- Бољи RAG перформанси - због већег прозора контекста
- Генерација синтетичких података - могућност креирања ефикасних података за задатке као што је фино подешавање

### Позивање изворних функција

Лама 3.1 је фино подешена да буде ефикаснија у прављењу позива функција или алата. Такође има два уграђена алата које модел може идентификовати као потребне за употребу на основу корисничког упита. Ови алати су:

- **Brave Search** - Може се користити за добијање актуелних информација као што је временска прогноза путем веб претраге
- **Wolfram Alpha** - Може се користити за сложеније математичке прорачуне тако да писање сопствених функција није потребно.

Такође можете креирати сопствене прилагођене алате које LLM може позвати.

У примеру кода испод:

- Дефинишемо доступне алате (brave_search, wolfram_alpha) у системском упиту.
- Пошаљите кориснички упит који пита о времену у одређеном граду.
- LLM ће одговорити позивом алата Brave Search који ће изгледати овако `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Напомена: Овај пример само прави позив алата, ако желите да добијете резултате, потребно је да креирате бесплатан налог на Brave API страници и дефинишете саму функцију`

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

## Лама 3.2

Иако је LLM, једно ограничење које Лама 3.1 има је мултимодалност. То јест, способност коришћења различитих типова уноса као што су слике као упити и пружање одговора. Ова способност је једна од главних карактеристика Ламе 3.2. Ове карактеристике такође укључују:

- Мултимодалност - има способност процене и текстуалних и сликовних упита
- Варијације малих до средњих величина (11Б и 90Б) - ово пружа флексибилне опције за примену,
- Варијације само текста (1Б и 3Б) - ово омогућава моделу да се примени на edge / мобилним уређајима и пружа ниску латенцију

Подршка за мултимодалност представља велики корак у свету модела отвореног кода. Пример кода испод узима и сликовни и текстуални упит да би добио анализу слике од Ламе 3.2 90Б.

### Подршка за мултимодалност са Лама 3.2

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

## Учење се овде не завршава, наставите путовање

Након завршетка ове лекције, погледајте нашу [Generative AI Learning колекцију](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) да наставите да унапређујете своје знање о Generative AI!

**Одрицање од одговорности**:  
Овај документ је преведен користећи AI услугу превођења [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да будете свесни да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације, препоручује се професионални превод од стране људи. Нисмо одговорни за било каква погрешна разумевања или интерпретације које произилазе из употребе овог превода.