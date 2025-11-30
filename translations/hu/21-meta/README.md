<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:12:34+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "hu"
}
-->
# Építés a Meta család modelljeivel

## Bevezetés

Ebben a leckében a következőkről lesz szó:

- A két fő Meta család modell felfedezése - Llama 3.1 és Llama 3.2
- Az egyes modellek használati eseteinek és helyzeteinek megértése
- Kódpélda, amely bemutatja az egyedi jellemzőket

## A Meta család modelljei

Ebben a leckében két modellt vizsgálunk meg a Meta családból, vagyis a "Llama Herd"-ből - Llama 3.1 és Llama 3.2

Ezek a modellek különböző változatokban érhetők el, és megtalálhatók a GitHub Model piacterén. További részletek a GitHub Modellek használatáról az [AI modellekkel való prototípus készítéshez](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modellváltozatok:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Megjegyzés: Llama 3 is elérhető a GitHub Modelleken, de ezt a leckét nem tárgyaljuk*

## Llama 3.1

A 405 milliárd paraméterével a Llama 3.1 az open source LLM kategóriába tartozik.

Ez a modell az előző, Llama 3-as verzió továbbfejlesztése, amely a következőket kínálja:

- Nagyobb kontextusablak - 128k token az 8k token helyett
- Nagyobb maximális kimeneti tokenek száma - 4096 az 2048 helyett
- Jobb többnyelvű támogatás - a megnövelt tanító tokenek miatt

Ezek lehetővé teszik, hogy a Llama 3.1 összetettebb feladatokat is kezeljen GenAI alkalmazások fejlesztésekor, például:
- Natív függvényhívás - külső eszközök és funkciók meghívásának képessége az LLM munkafolyamatán kívül
- Jobb RAG teljesítmény - a nagyobb kontextusablak miatt
- Szintetikus adatgenerálás - hatékony adatok létrehozása például finomhangoláshoz

### Natív függvényhívás

A Llama 3.1 finomhangolt, hogy hatékonyabban tudjon függvényeket vagy eszközöket hívni. Két beépített eszközt is tartalmaz, amelyeket a modell a felhasználói prompt alapján azonosítani tud, hogy használni kell őket. Ezek az eszközök:

- **Brave Search** - friss információk, például időjárás lekérdezésére alkalmas webes keresés segítségével
- **Wolfram Alpha** - összetettebb matematikai számításokhoz, így nem szükséges saját függvényeket írni

Saját egyedi eszközöket is létrehozhatsz, amelyeket az LLM hívhat.

Az alábbi kódpéldában:

- Meghatározzuk a rendelkezésre álló eszközöket (brave_search, wolfram_alpha) a rendszer promptban.
- Küldünk egy felhasználói promptot, amely egy adott város időjárására kérdez rá.
- Az LLM válasza egy eszközhívás lesz a Brave Search eszközhöz, ami így néz ki: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Megjegyzés: Ez a példa csak az eszközhívást mutatja be, ha az eredményeket is szeretnéd megkapni, ingyenes fiókot kell létrehoznod a Brave API oldalán, és definiálnod kell magát a függvényt*

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

Bár LLM-ről van szó, a Llama 3.1 egyik korlátja a multimodalitás hiánya. Ez azt jelenti, hogy nem képes különböző típusú bemeneteket, például képeket promptként használni és válaszokat adni rájuk. Ez a képesség a Llama 3.2 egyik fő jellemzője. További jellemzői:

- Multimodalitás - képes szöveges és képi promptokat is értékelni
- Kis- és közepes méretű változatok (11B és 90B) - rugalmas telepítési lehetőségeket kínál
- Csak szöveges változatok (1B és 3B) - lehetővé teszi a modell telepítését élőhelyi / mobil eszközökön, alacsony késleltetéssel

A multimodális támogatás nagy előrelépést jelent az open source modellek világában. Az alábbi kódpélda egy képet és egy szöveges promptot is használ, hogy a Llama 3.2 90B elemezze a képet.

### Multimodális támogatás a Llama 3.2-vel

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

## A tanulás itt nem ér véget, folytasd az utat

A lecke elvégzése után nézd meg a [Generatív AI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd a generatív AI ismereteidet!

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.