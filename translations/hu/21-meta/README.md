<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:34:43+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "hu"
}
-->
# Építkezés a Meta család modelleivel

## Bevezetés

Ez a lecke a következőket fogja tárgyalni:

- A Meta család két fő modelljének, a Llama 3.1 és Llama 3.2 felfedezése
- Az egyes modellek felhasználási eseteinek és forgatókönyveinek megértése
- Kódrészlet, amely bemutatja az egyes modellek egyedi jellemzőit

## A Meta család modelljei

Ebben a leckében a Meta család vagy "Llama csorda" 2 modelljét fogjuk felfedezni - Llama 3.1 és Llama 3.2.

Ezek a modellek különböző változatokban érhetők el, és megtalálhatók a GitHub Model piactéren. További részletek a GitHub Modellek használatáról az [AI modellekkel való prototípus készítéshez](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modellváltozatok:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Megjegyzés: A Llama 3 is elérhető a GitHub Modellek között, de ebben a leckében nem foglalkozunk vele.*

## Llama 3.1

A 405 milliárd paraméterrel a Llama 3.1 az open source LLM kategóriába tartozik.

A modell a korábbi Llama 3 kiadás frissítése az alábbiakkal:

- Nagyobb kontextusablak - 128k token vs 8k token
- Nagyobb maximális kimeneti tokenek - 4096 vs 2048
- Jobb többnyelvű támogatás - a tanulási tokenek számának növekedése miatt

Ezek lehetővé teszik a Llama 3.1 számára, hogy összetettebb felhasználási eseteket kezeljen a GenAI alkalmazások építése során, beleértve:
- Natív funkcióhívás - külső eszközök és funkciók hívásának képessége az LLM munkafolyamatán kívül
- Jobb RAG teljesítmény - a magasabb kontextusablak miatt
- Szintetikus adatgenerálás - hatékony adatok létrehozásának képessége például finomhangoláshoz

### Natív funkcióhívás

A Llama 3.1-t finomhangolták, hogy hatékonyabb legyen a funkció- vagy eszközhívásokban. Két beépített eszközzel is rendelkezik, amelyeket a modell azonosíthat a felhasználói kérés alapján, hogy használni kell őket. Ezek az eszközök:

- **Brave Search** - Használható naprakész információk, például időjárás lekérdezésére webes keresésen keresztül
- **Wolfram Alpha** - Bonyolultabb matematikai számításokhoz használható, így nem szükséges saját funkciókat írni.

Saját egyedi eszközöket is létrehozhat, amelyeket az LLM hívhat.

Az alábbi kódrészletben:

- Meghatározzuk az elérhető eszközöket (brave_search, wolfram_alpha) a rendszer kérésben.
- Küldünk egy felhasználói kérést, amely egy bizonyos város időjárásáról érdeklődik.
- Az LLM válaszolni fog egy eszközhívással a Brave Search eszköz felé, amely így fog kinézni: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Megjegyzés: Ez a példa csak az eszközhívást hajtja végre, ha szeretné megkapni az eredményeket, létre kell hoznia egy ingyenes fiókot a Brave API oldalon, és meg kell határoznia magát a funkciót.*

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

Bár LLM-ről van szó, a Llama 3.1 egyik korlátja a multimodalitás. Vagyis az a képesség, hogy különböző típusú bemeneteket, például képeket is használjon kérésként, és válaszokat adjon. Ez a képesség a Llama 3.2 egyik fő jellemzője. Ezek a jellemzők a következőket is magukban foglalják:

- Multimodalitás - képes mind szöveges, mind képi kéréseket értékelni
- Kis- és közepes méretű változatok (11B és 90B) - ez rugalmas telepítési lehetőségeket biztosít
- Csak szöveges változatok (1B és 3B) - ez lehetővé teszi a modell telepítését élő / mobil eszközökre és alacsony késleltetést biztosít

A multimodális támogatás nagy lépést jelent az open source modellek világában. Az alábbi kódrészlet mind képi, mind szöveges kérést használ, hogy elemzést kapjon a képről a Llama 3.2 90B-től.

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

## A tanulás nem áll meg itt, folytassa az utazást

A lecke befejezése után tekintse meg [Generatív AI Tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejlessze generatív AI ismereteit!

**Felelősségi nyilatkozat**:  
Ezt a dokumentumot az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt a professzionális emberi fordítás igénybevétele. Nem vállalunk felelősséget semmilyen félreértésért vagy félremagyarázásért, amely a fordítás használatából ered.