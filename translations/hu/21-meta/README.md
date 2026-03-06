# Építés a Meta Család Modelljeivel 

## Bevezetés 

Ez a lecke a következőket fedi le: 

- A két fő Meta család modell felfedezése - Llama 3.1 és Llama 3.2 
- Az egyes modellek felhasználási eseteinek és forgatókönyveinek megértése 
- Kódpélda az egyes modellek egyedi jellemzőinek bemutatására 


## A Meta család modelljei 

Ebben a leckében két modellt fedezünk fel a Meta családból, vagyis a "Llama Herd"-ből - Llama 3.1 és Llama 3.2.

Ezek a modellek különböző változatokban érhetők el, és elérhetőek a GitHub Model piactéren. További részletek a GitHub Modellek használatáról az AI modellekkel történő [prototípuskészítéshez](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modell változatok: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Megjegyzés: A Llama 3 szintén elérhető a GitHub Modelleken, de ebben a leckében nem kerül tárgyalásra*

## Llama 3.1 

A 405 milliárd paraméterrel rendelkező Llama 3.1 az open source LLM kategóriába tartozik. 

A modell az előző kiadású Llama 3 továbbfejlesztése az alábbiak révén: 

- Nagyobb kontextus ablak - 128k token a 8k token helyett 
- Nagyobb maximális kimeneti token szám - 4096 a 2048 helyett 
- Jobb többnyelvű támogatás - a megnövelt tanító tokenek miatt 

Ezek lehetővé teszik a Llama 3.1 számára, hogy összetettebb feladatokat is kezeljen Generatív AI alkalmazások építésekor, beleértve: 
- Natív függvényhívást - a képesség külső eszközök és függvények meghívására az LLM munkafolyamatán kívül
- Jobb RAG teljesítményt - a nagyobb kontextus ablak miatt 
- Szintetikus adatgenerálást - a hatékony adatok létrehozásának képessége feladatokhoz, mint például az finomhangolás 

### Natív függvényhívás 

A Llama 3.1 finomhangolva lett annak érdekében, hogy hatékonyabban tudjon függvény- vagy eszközhívásokat végrehajtani. Két beépített eszköze is van, amelyeket a modell a felhasználótól érkező prompt alapján használni tud. Ezek az eszközök: 

- **Brave Search** - használható aktuális információk megszerzésére, például az időjárás lekérdezésére webes kereséssel 
- **Wolfram Alpha** - használható összetettebb matematikai számításokra, így nem szükséges saját függvényeket írni 

Ezen kívül egyedi, testreszabott eszközöket is létrehozhat, amelyeket az LLM hívhat. 

Az alábbi kódpéldában: 

- Definiáljuk a rendelkezésre álló eszközöket (brave_search, wolfram_alpha) a rendszer promptban. 
- Küldünk egy felhasználói promptot, amely egy bizonyos város időjárásáról kérdez. 
- Az LLM válasza egy eszközhívás lesz a Brave Search eszközre, amely így fog kinézni: `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Megjegyzés: Ez a példa csak az eszközhívást mutatja be, ha szeretné megkapni az eredményeket, akkor regisztrálnia kell egy ingyenes fiókot a Brave API oldalán, és definiálnia kell magát a függvényt.

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

Annak ellenére, hogy LLM, a Llama 3.1 egyik korlátja a multimodalitás hiánya. Ez azt jelenti, hogy nem képes különféle bemeneteket, például képeket promptként használni és válaszokat adni. Ez a képesség a Llama 3.2 egyik fő jellemzője. Ezek a jellemzők a következők: 

- Multimodalitás - képes értékelni mind szöveges, mind képi promtokat 
- Kis és közepes méretű változatok (11B és 90B) - rugalmas telepítési lehetőségeket kínál 
- Csak szöveges változatok (1B és 3B) - lehetővé teszi a modell élőhelyi / mobil eszközökön történő telepítését alacsony késleltetéssel 

A multimodális támogatás nagy előrelépést jelent a nyílt forráskódú modellek világában. Az alábbi kódpélda mind kép, mind szöveges promptot használ, hogy elemzést kapjunk a Llama 3.2 90B modelltől a képről. 


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

A lecke befejezése után nézd meg a [Generatív AI Tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább bővítsd generatív AI ismereteidet!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Nyilatkozat**:
Ezt a dokumentumot az [Co-op Translator](https://github.com/Azure/co-op-translator) mesterséges intelligencia alapú fordító szolgáltatással fordítottuk. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum anyanyelvű változata tekintendő hivatalos forrásnak. Fontos információk esetén javasolt profi, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->