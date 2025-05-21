<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:15:16+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "hu"
}
-->
# Építés a Meta család modelleivel

## Bevezetés

Ez a lecke az alábbiakat fogja tárgyalni:

- A Meta család két fő modelljének - Llama 3.1 és Llama 3.2 - felfedezése
- Az egyes modellek használati eseteinek és forgatókönyveinek megértése
- Kódminta, amely bemutatja az egyes modellek egyedi jellemzőit

## A Meta család modelljei

Ebben a leckében a Meta család vagy "Llama Nyáj" 2 modelljét fogjuk megvizsgálni - Llama 3.1 és Llama 3.2

Ezek a modellek különböző változatokban érhetők el, és elérhetők a GitHub Model piactéren. További részletek a GitHub Modellek használatáról a [prototípus készítése AI modellekkel](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) oldalon találhatók.

Modellváltozatok:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Megjegyzés: A Llama 3 is elérhető a GitHub Modellek között, de ebben a leckében nem foglalkozunk vele*

## Llama 3.1

A 405 milliárd paraméterrel a Llama 3.1 az open source LLM kategóriába tartozik.

A modell a korábbi Llama 3 kiadás továbbfejlesztése az alábbiakkal:

- Nagyobb kontextusablak - 128k token vs 8k token
- Nagyobb maximális kimeneti tokenek - 4096 vs 2048
- Jobb többnyelvű támogatás - a képzési tokenek növekedése miatt

Ezek lehetővé teszik a Llama 3.1 számára, hogy összetettebb használati eseteket kezeljen a GenAI alkalmazások építése során, beleértve:
- Natív funkcióhívás - a képesség, hogy külső eszközöket és funkciókat hívjon meg az LLM munkafolyamaton kívül
- Jobb RAG teljesítmény - a nagyobb kontextusablak miatt
- Szintetikus adatok generálása - a hatékony adatok létrehozásának képessége finomhangolási feladatokhoz

### Natív funkcióhívás

A Llama 3.1 finomhangolva lett, hogy hatékonyabb legyen a funkciók vagy eszközök hívásában. Két beépített eszközzel is rendelkezik, amelyeket a modell azonosíthat, hogy szükséges használni a felhasználó kérésének megfelelően. Ezek az eszközök:

- **Brave Search** - Használható aktuális információk, például az időjárás megszerzésére webes kereséssel
- **Wolfram Alpha** - Használható összetettebb matematikai számításokhoz, így nem szükséges saját funkciók írása.

Saját egyéni eszközöket is létrehozhat, amelyeket az LLM meghívhat.

Az alábbi kódpéldában:

- Meghatározzuk az elérhető eszközöket (brave_search, wolfram_alpha) a rendszer kérésben.
- Küldünk egy felhasználói kérést, amely egy bizonyos város időjárásáról kérdez.
- Az LLM válaszolni fog egy eszközhívással a Brave Search eszközre, amely így fog kinézni `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Megjegyzés: Ez a példa csak az eszközhívást végzi el, ha szeretné megkapni az eredményeket, létre kell hoznia egy ingyenes fiókot a Brave API oldalon és meghatározni a funkciót magát*

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

Bár a Llama 3.1 egy LLM, van egy korlátja a multimodalitásnak. Vagyis képes különböző típusú bemenetek, például képek használatára kérésként és válaszok biztosítására. Ez a képesség az egyik fő jellemzője a Llama 3.2-nek. Ezek a jellemzők a következőket is tartalmazzák:

- Multimodalitás - képes mind szöveg, mind kép kérdések értékelésére
- Kis és közepes méretű változatok (11B és 90B) - ez rugalmas telepítési lehetőségeket biztosít
- Csak szöveg változatok (1B és 3B) - ez lehetővé teszi a modell telepítését élvonalbeli / mobil eszközökre, és alacsony késleltetést biztosít

A multimodális támogatás nagy lépést jelent az open source modellek világában. Az alábbi kódpélda mind képet, mind szöveg kérdést használ, hogy elemzést kapjon a képről a Llama 3.2 90B-től.

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

## A tanulás itt nem áll meg, folytassa az utazást

A lecke befejezése után nézze meg a [Generatív AI Tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejlessze Generatív AI ismereteit!

**Felelősségkizárás**:  
Ezt a dokumentumot az [Co-op Translator](https://github.com/Azure/co-op-translator) mesterséges intelligencia fordítási szolgáltatás segítségével fordítottuk le. Bár igyekszünk a pontosságra törekedni, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.