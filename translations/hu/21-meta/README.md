# Építés a Meta Család Modelleivel 

## Bevezetés 

Ez a lecke a következőket fogja lefedni: 

- A Meta család két fő modelljének felfedezése - Llama 3.1 és Llama 3.2 
- Minden modell felhasználási eseteinek és forgatókönyveinek megértése 
- Kódrészlet, amely bemutatja az egyedi jellemzőket minden modell esetében 


## A Meta Család Modelljei 

Ebben a leckében két modellt fedezünk fel a Meta családból vagy "Llama Herd"-ből - Llama 3.1 és Llama 3.2.

Ezek a modellek különféle változatokban érhetők el, és megtalálhatók a [Microsoft Foundry Models katalógusában](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Megjegyzés:** A GitHub Modellek 2026 júliusának végén megszűnik. További részletek a [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) használatáról az AI modellekkel való prototípus-készítéshez.

Modell Változatok: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Megjegyzés: A Llama 3 elérhető a Microsoft Foundry Models szolgáltatásban is, de ez a lecke nem foglalkozik vele*

## Llama 3.1 

A 405 milliárd paraméterrel rendelkező Llama 3.1 az open source nagyméretű nyelvi modellek kategóriájába tartozik. 

A modell az előző kiadás, a Llama 3 továbbfejlesztése, amely a következőket kínálja: 

- Nagyobb kontextusablak - 128k token a 8k token helyett 
- Nagyobb Maximális Kimeneti Tokenek száma - 4096 a 2048 helyett 
- Jobb többnyelvű támogatás - a megnövekedett tanító tokenek miatt 

Ezek lehetővé teszik, hogy a Llama 3.1 összetettebb feladatokat is kezeljen GenAI alkalmazások építése során, beleértve: 
- Natív funkcióhívás - a képesség arra, hogy külső eszközöket és funkciókat hívjon meg az LLM munkafolyamatán kívül
- Jobb RAG teljesítmény - a nagyobb kontextusablak miatt 
- Szintetikus adat generálása - a képesség hatékony adatokat előállítani finomhangolási feladatokhoz 

### Natív Funkcióhívás 

A Llama 3.1-et úgy hangolták finomra, hogy hatékonyabb legyen a funkció- vagy eszközhívásoknál. Két beépített eszközzel is rendelkezik, amelyeket a modell azonosítani tud, ha a felhasználó utasítása alapján azok használata szükséges. Ezek az eszközök: 

- **Brave Search** - Használható friss információk, például az időjárás lekérdezésére webes keresés végrehajtásával 
- **Wolfram Alpha** - Használható bonyolultabb matematikai számításokra, így nem szükséges saját függvényeket írni. 

Saját egyedi eszközöket is létrehozhatsz, amelyeket az LLM képes meghívni. 

A következő kódrészletben: 

- Meghatározzuk az elérhető eszközöket (brave_search, wolfram_alpha) a rendszerutasításban. 
- Küldünk egy felhasználói utasítást, amely megkérdezi egy adott város időjárását. 
- Az LLM válaszként egy eszközhívást fog generálni a Brave Search eszközhöz, ami így fog kinézni: `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Megjegyzés: Ez a példa csak az eszközhívást mutatja be, ha az eredményeket is meg szeretnéd kapni, ingyenes fiókot kell létrehoznod a Brave API oldalán, és definiálnod kell magát a függvényt.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Szerezd be ezeket a Microsoft Foundry projekted „Áttekintés” oldaláról
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

Noha az Llama 3.1 egy LLM, egy korlátja az, hogy nem támogatja a multimodalitást. Vagyis nem képes különböző típusú bemeneteket, például képeket használni utasításként, és válaszokat adni rájuk. Ez a képesség a Llama 3.2 egyik fő jellemzője. Ezek a jellemzők a következők: 

- Multimodalitás - képes értékelni mind szöveges, mind képi utasításokat 
- Kis és közepes méretű változatok (11B és 90B) - rugalmas telepítési lehetőségeket biztosítanak, 
- Csak szöveges változatok (1B és 3B) - lehetővé teszi a modell telepítését edge / mobil eszközökön, alacsony késleltetéssel 

A multimodális támogatás nagy előrelépést jelent az open source modellek világában. Az alábbi kódrészlet mind kép-, mind szöveges utasítást használva elemzést kér a Llama 3.2 90B modelltől. 


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

# Szerezze be ezeket a Microsoft Foundry projekt "Áttekintés" oldaláról
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

A lecke elvégzése után nézd meg a [Generatív AI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd a generatív AI ismereteidet!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->