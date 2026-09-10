# Építés a Meta család modelleivel 

## Bevezetés 

Ez a lecke a következőket fogja lefedni: 

- A két fő Meta család modell felfedezése - Llama 3.1 és Llama 3.2 
- Mindkét modell felhasználási eseteinek és szcenárióinak megértése 
- Kódpélda, amely bemutatja mindkét modell egyedi jellemzőit 


## A Meta család modelljei 

Ebben a leckében két modellt fogunk felfedezni a Meta családból, azaz a "Llama Herd"-ból – Llama 3.1 és Llama 3.2.

Ezek a modellek különböző variánsokban érhetők el, és megtalálhatók a [Microsoft Foundry Models katalógusában](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Megjegyzés:** A GitHub Models 2026 júliusának végén megszűnik. Itt további részleteket talál a [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) használatáról az AI modellekkel való prototípuskészítéshez.

Modellváltozatok: 
- Llama 3.1 - 70B Instruktív 
- Llama 3.1 - 405B Instruktív 
- Llama 3.2 - 11B Vision Instruktív 
- Llama 3.2 - 90B Vision Instruktív 

*Megjegyzés: A Llama 3 szintén elérhető a Microsoft Foundry Modelseiben, de ez a lecke nem foglalkozik vele*

## Llama 3.1 

A 405 milliárd paraméterével a Llama 3.1 az open source nagyméretű nyelvi modellek (LLM) kategóriájába tartozik. 

A modell fejlesztés a korábbi Llama 3 kiadáshoz képest, az alábbiakat kínálja: 

- Nagyobb kontextusablak - 128k token vs 8k token 
- Nagyobb maximális kimeneti tokenek száma - 4096 vs 2048 
- Jobb többnyelvű támogatás - a megnövelt tanító token mennyiség miatt 

Ezek lehetővé teszik, hogy a Llama 3.1 összetettebb feladatokat kezeljen GenAI alkalmazások fejlesztésekor, beleértve: 
- Natív függvényhívás - a képesség külső eszközök és függvények meghívására az LLM munkafolyamatán kívül
- Jobb RAG teljesítmény - a nagyobb kontextusablak miatt 
- Szintetikus adat generálás - hatékony adatok létrehozásának képessége olyan feladatokhoz, mint a finomhangolás 

### Natív függvényhívás 

A Llama 3.1 finomhangoltabb, hogy hatékonyabban hívhasson meg függvényeket vagy eszközöket. Két beépített eszközt is tartalmaz, amelyeket a modell azonosítani tud, hogy a felhasználói prompt alapján használnia kell. Ezek az eszközök: 

- **Brave Search** - használható az aktuális információkhoz, például az időjárás lekérdezéséhez, webes keresést végezve 
- **Wolfram Alpha** - összetettebb matematikai számításokra használható, így nem szükséges saját függvények írása. 

Saját egyéni eszközöket is létrehozhatsz, amelyeket az LLM hívhat. 

Az alábbi kódpéldában: 

- Meghatározzuk a rendelkezésre álló eszközöket (brave_search, wolfram_alpha) a rendszerpromptban. 
- Küldünk egy felhasználói promptot, amely az időjárásról kérdez egy adott városban. 
- Az LLM válasza egy eszközhívás lesz a Brave Search eszközre, amely így néz ki: `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Megjegyzés: Ez a példa csak az eszközhívást hajtja végre, ha az eredményeket is szeretnéd megkapni, ingyenes fiókot kell létrehoznod a Brave API oldalon, és magát a függvényt is definiálnod kell.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Ezeket a Microsoft Foundry projekted „Áttekintés” oldaláról szerezd be
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

Habár LLM, a Llama 3.1 egy korlátja, hogy nincs multimodális képessége. Ez azt jelenti, hogy nem képes különböző típusú bemeneteket használni, például képeket promptként, és választ adni rájuk. Ez a képesség a Llama 3.2 egyik fő jellemzője. Ezek a jellemzők a következők is: 

- Multimodalitás - képes mind szöveg, mind kép promptokat értékelni 
- Kicsi és közepes méretű változatok (11B és 90B) - rugalmas telepítési lehetőségeket biztosítanak, 
- Csak szöveges változatok (1B és 3B) - lehetővé teszi a modell telepítését élvonalbeli / mobil eszközökön és alacsony késleltetést biztosít 

A multimodális támogatás nagy előrelépést jelent a nyílt forráskódú modellek világában. Az alábbi kódpélda egy képet és szöveges promptot is használ, hogy elemzést kapjunk a Llama 3.2 90B-től a képről. 


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

# Szerezd be ezeket a Microsoft Foundry projekted „Áttekintés” oldaláról
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

## A tanulás itt nem áll meg, folytasd az utat

A lecke befejeztével tekintsd meg [Generatív AI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy folytasd a Generatív AI ismereteid fejlesztését!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->