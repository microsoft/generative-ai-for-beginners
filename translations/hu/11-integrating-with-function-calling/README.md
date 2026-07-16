# Integráció függvényhívással

[![Integráció függvényhívással](../../../translated_images/hu/11-lesson-banner.d78860d3e1f041e2.webp)](https://youtu.be/DgUdCLX8qYQ?si=f1ouQU5HQx6F8Gl2)

Eddig meglehetősen sokat tanultál a korábbi leckékben. Azonban tovább tudunk fejlődni. Néhány dolgot érinthetünk, mint például hogy hogyan érhetünk el következetesebb válaszformátumot, hogy könnyebbé tegyük a válasz feldolgozását később. Emellett szeretnénk adatokat hozzáadni más forrásokból, hogy még gazdagabbá tegyük az alkalmazásunkat.

A fent említett problémákat ez a fejezet kívánja megoldani.

## Bevezetés

Ez a lecke a következőket tárgyalja:

- Megmagyarázza, mi az a függvényhívás és milyen esetekben használjuk.
- Függvényhívás létrehozása Azure OpenAI használatával.
- Hogyan integráljunk egy függvényhívást egy alkalmazásba.

## Tanulási célok

A lecke végére képes leszel:

- Megmagyarázni a függvényhívás használatának célját.
- Beállítani a Függvényhívást az Azure OpenAI Szolgáltatás használatával.
- Hatékony függvényhívásokat tervezni az alkalmazás felhasználási esetére.

## Forgatókönyv: Chatbotunk fejlesztése funkciókkal

Ebben a leckében egy olyan funkciót szeretnénk építeni oktatási startupunk számára, amely lehetővé teszi a felhasználóknak, hogy chatbot segítségével technikai kurzusokat találjanak. Olyan kurzusokat ajánlunk, amelyek megfelelnek a készségszintjüknek, aktuális szerepüknek és érdeklődési technológiájuknak.

Ehhez a forgatókönyvhöz a következő kombinációt fogjuk használni:

- `Azure OpenAI` a chat élmény létrehozásához a felhasználó számára.
- `Microsoft Learn Catalog API`, hogy segítsen a felhasználóknak megtalálni a kéréseiknek megfelelő kurzusokat.
- `Függvényhívás` a felhasználói lekérdezés átvételéhez és egy függvényhez küldéséhez az API kéréshez.

Kezdjük azzal, hogy megnézzük, miért is érdemes először használni a függvényhívást:

## Miért Függvényhívás

A függvényhívás előtt az LLM-ek válaszai strukturálatlanok és következetlenek voltak. A fejlesztőknek bonyolult validációs kódokat kellett írniuk, hogy minden válaszvariációt kezelni tudjanak. A felhasználók nem kaphattak válaszokat például arra, hogy "Mi a jelenlegi időjárás Stockholmban?". Ennek oka, hogy a modellek csak a tanított adatok időpontjáig voltak korlátozva.

A függvényhívás az Azure OpenAI Szolgáltatás egy funkciója, amellyel a következő korlátokat hidalhatjuk át:

- **Következetes válaszformátum**. Ha jobban tudjuk kontrollálni a válasz formátumát, könnyebben integrálhatjuk azt más rendszerekbe.
- **Külső adatok**. Képesség arra, hogy az alkalmazás más forrásaiból származó adatokat használjunk chat kontextusban.

## A probléma szemléltetése egy példán keresztül

> Javasoljuk, hogy használd a [mellékelt notebookot](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreyst), ha szeretnéd lefuttatni az alábbi forgatókönyvet. De egyszerűen olvashatod is, miközben megpróbálunk egy problémát bemutatni, amelyen a függvények segíthetnek.

Nézzük meg egy példát, amely illusztrálja a válasz formátum problémáját:

Tegyük fel, hogy szeretnénk létrehozni egy diákadatbázist, hogy megfelelő kurzust javasoljunk nekik. Lent két diák leírása található, amelyek nagyon hasonló adatokat tartalmaznak.

1. Hozz létre kapcsolatot az Azure OpenAI erőforrásunkhoz:

   ```python
   import os
   import json
   from openai import OpenAI
   from dotenv import load_dotenv
   load_dotenv()

   # A Responses API az Azure OpenAI (Microsoft Foundry) v1 végpontjáról szolgál ki,
   # ezért az OpenAI klienst a <your-endpoint>/openai/v1/ címre irányítjuk.
   endpoint = os.environ['AZURE_OPENAI_ENDPOINT']
   client = OpenAI(
   api_key=os.environ['AZURE_OPENAI_API_KEY'],
   base_url=f"{endpoint.rstrip('/')}/openai/v1/",
   )

   deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']
   ```

   Az alábbi Python kód az Azure OpenAI-hoz való kapcsolat konfigurálására szolgál. Mivel az v1 végpontot használjuk, csak az `api_key` és a `base_url` beállítása szükséges (nem kell `api_version`).

1. Két diák leírásának létrehozása a `student_1_description` és `student_2_description` változókban.

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   A fent említett diákleírásokat az LLM-nek küldjük feldolgozásra. Ezek az adatok később használhatók az alkalmazásban, API-nak küldhetők vagy adatbázisban tárolhatók.

1. Készítsünk két azonos promptot, melyekben utasítjuk az LLM-et, hogy milyen információkra vagyunk kíváncsiak:

   ```python
   prompt1 = f'''
   Please extract the following information from the given text and return it as a JSON object:

   name
   major
   school
   grades
   club

   This is the body of text to extract the information from:
   {student_1_description}
   '''

   prompt2 = f'''
   Please extract the following information from the given text and return it as a JSON object:

   name
   major
   school
   grades
   club

   This is the body of text to extract the information from:
   {student_2_description}
   '''
   ```

   A fenti promptok utasítják az LLM-et, hogy az információkat dolgozza fel, és JSON formátumban adja vissza a választ.

1. A promptok és a kapcsolat beállítása után a `client.responses.create` metódussal elküldjük a promptokat az LLM-nek. A promptot az `input` változóba tesszük, szerepként `user`-t adva, hogy utánozzuk egy felhasználói üzenetet a chatbotban.

   ```python
   # válasz az első promptból
   openai_response1 = client.responses.create(
   model=deployment,
   input = [{'role': 'user', 'content': prompt1}],
   store=False,
   )
   openai_response1.output_text

   # válasz a második promptból
   openai_response2 = client.responses.create(
   model=deployment,
   input = [{'role': 'user', 'content': prompt2}],
   store=False,
   )
   openai_response2.output_text
   ```

Most elküldhetjük mindkét kérést az LLM-nek és megvizsgálhatjuk a választ, például így: `openai_response1.output_text`.

1. Végül alakítsuk át a választ JSON formátummá a `json.loads` hívásával:

   ```python
   # A válasz betöltése JSON objektumként
   json_response1 = json.loads(openai_response1.output_text)
   json_response1
   ```

   1. válasz:

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   2. válasz:

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   Bár a promptok ugyanazok és a leírások is hasonlóak, a `Grades` tulajdonság értékei eltérően vannak formázva, néha például `3.7`, máskor `3.7 GPA`.

   Ez azért van, mert az LLM a strukturálatlan adatokról (a megírt prompt formájában) strukturálatlan adatokat ad vissza. Szükségünk van egy strukturált formátumra, hogy tudjuk, mire számítsunk az adat tárolásakor vagy használatakor.

Hogyan oldjuk meg tehát a formázási problémákat? A függvényhívás használatával biztosak lehetünk benne, hogy visszakapjuk a strukturált adatot. A függvényhívásnál az LLM valójában nem hív meg vagy futtat függvényeket. Ehelyett létrehozunk egy struktúrát, amelyet az LLM követni fog a válaszai során. Ezekből a strukturált válaszokból tudjuk, hogy melyik függvényt hajtsuk végre az alkalmazásban.

![function flow](../../../translated_images/hu/Function-Flow.083875364af4f4bb.webp)

Ezt követően a függvénytől kapott eredményt visszaküldjük az LLM-nek, amely természetes nyelven válaszol a felhasználói kérdésre.

## Függvényhívási esetek

Számos esetben javíthatják az alkalmazásodat a függvényhívások, például:

- **Külső eszközök hívása**. A chatbotok kiválóak a felhasználók kérdéseinek megválaszolásában. A függvényhívás használatával a chatbotok képesek bizonyos feladatokat elvégezni a felhasználói üzenetek alapján. Például egy diák megkérheti a chatbotot, hogy "Küldj egy emailt az oktatómnak, hogy segítségre van szükségem ebben a témában". Ez egy olyan függvényhíváshoz vezethet, mint `send_email(to: string, body: string)`.

- **API vagy adatbázis lekérdezések készítése**. A felhasználók természetes nyelven kereshetnek információt, amelyet a rendszer formázott lekérdezéssé vagy API kérésé alakít. Például egy tanár megkérdezheti, "Kik azok a diákok, akik teljesítették az utolsó feladatot", és ez egy `get_completed(student_name: string, assignment: int, current_status: string)` nevű függvényt hívhat meg.

- **Strukturált adat létrehozása**. A felhasználók szövegrészeket vagy CSV adatokat adhatnak meg, amelyből az LLM fontos információkat von ki. Például egy diák átalakíthat egy Wikipedia cikket a békemegállapodásokról AI-alapú tanulókártyák létrehozásához. Ez egy olyan függvényhívással történhet, mint `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)`.

## Első függvényhívás létrehozása

A függvényhívás létrehozásának folyamata három fő lépésből áll:

1. **Hívás** a Responses API-nak egy függvények listájával (eszközökkel) és egy felhasználói üzenettel.
2. **A modell válaszának elolvasása**, hogy egy művelet végrehajtásához – például egy függvény vagy API hívás indításához – döntést hozzunk.
3. **Egy másik hívás végrehajtása** a Responses API-nak a függvény válaszával, hogy az alapján választ adjunk a felhasználónak.

![LLM Flow](../../../translated_images/hu/LLM-Flow.3285ed8caf4796d7.webp)

### 1. lépés – üzenetek létrehozása

Az első lépés egy felhasználói üzenet létrehozása. Ezt dinamikusan is hozzárendelhetjük egy szövegbeviteli érték alapján, vagy itt is megadhatjuk. Ha először használjuk a Responses API-t, meg kell adnunk az `role` és a `content` értékeket.

A `role` lehet `system` (szabályokat hoz létre), `assistant` (a modell) vagy `user` (a végfelhasználó). Függvényhívás esetén `user` szerepkört adunk, egy kérdéssel példaként.

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

A különböző szerepkörök hozzárendelésével tisztázzuk az LLM számára, hogy a rendszer vagy a felhasználó mond-e valamit, ami segít a párbeszéd előzmények építésében.

### 2. lépés – függvények létrehozása

Ezután definiálunk egy függvényt és a paramétereit. Itt csak egy függvényt használunk, `search_courses` néven, de több függvényt is létrehozhatsz.

> **Fontos** : A függvények benne vannak a rendszerüzenetben az LLM-nek, és beleszámítanak az elérhető tokenek mennyiségébe.

Lent egy tömböt hozunk létre, amelyben minden elem egy eszköz a flat Responses API formátumában, a következő tulajdonságokkal: `type`, `name`, `description` és `parameters`:

```python
functions = [
   {
      "type":"function",
      "name":"search_courses",
      "description":"Retrieves courses from the search index based on the parameters provided",
      "parameters":{
         "type":"object",
         "properties":{
            "role":{
               "type":"string",
               "description":"The role of the learner (i.e. developer, data scientist, student, etc.)"
            },
            "product":{
               "type":"string",
               "description":"The product that the lesson is covering (i.e. Azure, Power BI, etc.)"
            },
            "level":{
               "type":"string",
               "description":"The level of experience the learner has prior to taking the course (i.e. beginner, intermediate, advanced)"
            }
         },
         "required":[
            "role"
         ]
      }
   }
]
```

Íme az egyes függvények részletesebb leírása:

- `name` - A függvény neve, amelyet hívni akarunk.
- `description` - A függvény működésének leírása. Itt fontos, hogy pontos és világos legyen.
- `parameters` - Egy lista azoknak az értékeknek és formátumoknak, amelyeket a modell válaszként előállít. A `parameters` lista elemei a következő tulajdonságokkal rendelkeznek:
  1. `type` - Az adattípus, amelybe az értékek kerülnek.
  1. `properties` - A pontos értékek listája, amelyeket a modell a válaszában használ.
      1. `name` - Az adott tulajdonság neve, amelyet a modell a formázott válaszban használ, pl. `product`.
      1. `type` - A tulajdonság adattípusa, például `string`.
      1. `description` - A konkrét tulajdonság leírása.

Opcionálisan szerepelhet egy `required` tulajdonság is – ez megadja, mely mezők kötelezőek a függvényhívás sikeréhez.

### 3. lépés – a függvényhívás megvalósítása

A függvény definiálása után be kell építenünk a hívásba a Responses API felé az `tools` beállítást, amelyre `tools=functions` értéket adunk.

Opcióként beállíthatjuk a `tool_choice` értékét `auto`-ra, így az LLM döntheti el, mikor hívja meg a függvényeket a felhasználói üzenet alapján, nem nekünk kell kijelölni.

Lent egy példa kód, amelyben a `client.responses.create` metódust hívjuk meg, `tools=functions` és `tool_choice="auto"` beállítással, így az LLM maga dönt, mikor hívja meg a megadott függvényeket:

```python
response = client.responses.create(model=deployment,
                                        input=messages,
                                        tools=functions,
                                        tool_choice="auto",
                                        store=False)

print(response.output)
```

A válaszban most megjelenik a `function_call` elem a `response.output` részen, így néz ki:

```json
{
  "type": "function_call",
  "name": "search_courses",
  "call_id": "call_abc123",
  "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
}
```

Itt látható, hogy a `search_courses` függvény lett meghívva, és milyen argumentumokkal, amelyek a JSON válasz `arguments` tulajdonságában találhatók.

Az következtetés, hogy az LLM megtalálta az adatokat az argumentumokhoz, mivel azokat az `input` paraméter értékéből vonta ki a Responses API hívásában. Lent láthatod a `messages` változó értékét:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Ahogy látod, a `student`, `Azure` és `beginner` értékeket kivonta a `messages`-ból és bemeneti paraméterként átadta a függvénynek. A függvények ilyen használata nagyszerű módja annak, hogy információt nyerjünk ki egy promptból, valamint hogy az LLM számára struktúrát biztosítsunk és újrafelhasználható funkciókat hozzunk létre.

Most nézzük meg, hogyan használhatjuk ezt az alkalmazásunkban.

## Függvényhívások integrálása egy alkalmazásba

Miután teszteltük az LLM által formázott választ, integrálhatjuk az alkalmazásba.

### A folyamat kezelése

Az alkalmazásba integrálás lépései:

1. Először hívjuk meg az OpenAI szolgáltatásokat, és vonjuk ki a függvényhívásokat tartalmazó elemeket a válasz `output` részéből.

   ```python
   response_items = response.output
   tool_calls = [item for item in response_items if item.type == "function_call"]
   ```

1. Most definiáljuk azt a függvényt, amely a Microsoft Learn API-t hívja meg a kurzusok listájának lekéréséhez:

   ```python
   import requests

   def search_courses(role, product, level):
     url = "https://learn.microsoft.com/api/catalog/"
     params = {
        "role": role,
        "product": product,
        "level": level
     }
     response = requests.get(url, params=params)
     modules = response.json()["modules"]
     results = []
     for module in modules[:5]:
        title = module["title"]
        url = module["url"]
        results.append({"title": title, "url": url})
     return str(results)
   ```

   Figyeld meg, hogy egy valódi Python függvényt hozunk létre, amely megfelel a `functions` változóban definiált függvényeknek. Továbbá valós külső API hívásokat hajtunk végre az adatok lekéréséhez. Ebben az esetben a Microsoft Learn API-t használjuk az oktatási modulok keresésére.

Oké, létrehoztuk a `functions` változókat és a megfelelő Python függvényt, hogyan mondjuk meg az LLM-nek, hogy ezeket hogyan kösse össze, hogy a Python függvényünket hívja meg?

1. Ahhoz, hogy lássuk, meg kell-e hívnunk egy Python függvényt, meg kell néznünk az LLM válaszát, hogy van-e benne `function_call` rész, és ha igen, akkor meghívjuk a megjelölt függvényt. Íme, hogyan végezheted el ezt az ellenőrzést:

   ```python
   # Ellenőrizze, hogy a modell szeretne-e függvényt hívni
   if tool_calls:
    for tool_call in tool_calls:
     print("Recommended Function call:")
     print(tool_call.name)
     print()

     # Hívja meg a függvényt.
     function_name = tool_call.name

     available_functions = {
             "search_courses": search_courses,
     }
     function_to_call = available_functions[function_name]

     function_args = json.loads(tool_call.arguments)
     function_response = function_to_call(**function_args)

     print("Output of function call:")
     print(function_response)
     print(type(function_response))

     # Adja hozzá a függvényhívást és annak eredményét a beszélgetéshez.
     # A modell function_call elemét a kimenet előtt kell hozzáfűzni.
     messages.append(tool_call)  # a segéd function_call eleme
     messages.append( # a függvény eredménye
         {
             "type": "function_call_output",
             "call_id": tool_call.call_id,
             "output": function_response,
         }
     )
   ```

   Ez a három sor biztosítja, hogy kivonjuk a függvény nevét, az argumentumokat és végrehajtjuk a hívást:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(tool_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   Lent a kód futtatásának eredménye látható:

**Kimenet**

   ```Recommended Function call:
   {
     "name": "search_courses",
     "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
   }

   Output of function call:
   [{'title': 'Describe concepts of cryptography', 'url': 'https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?
   WT.mc_id=api_CatalogApi'}, {'title': 'Introduction to audio classification with TensorFlow', 'url': 'https://learn.microsoft.com/en-
   us/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi'}, {'title': 'Design a Performant Data Model in Azure SQL
   Database with Azure Data Studio', 'url': 'https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?
   WT.mc_id=api_CatalogApi'}, {'title': 'Getting started with the Microsoft Cloud Adoption Framework for Azure', 'url':
   'https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi'}, {'title': 'Set up the
   Rust development environment', 'url': 'https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi'}]
   <class 'str'>
   ```

1. Most elküldjük a frissített `messages` üzenetet az LLM-nek, hogy természetes nyelvű választ kapjunk egy API JSON formátumú helyett.

   ```python
   print("Messages in next request:")
   print(messages)
   print()

   second_response = client.responses.create(
      input=messages,
      model=deployment,
      tool_choice="auto",
      tools=functions,
      temperature=0,
      store=False,
         )  # szerezzen egy új választ a modelltől, ahol láthatja a függvény választ


   print(second_response.output_text)
   ```

**Kimenet**

   ```text
   I found some good courses for beginner students to learn Azure:

   1. [Describe concepts of cryptography](https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)
   2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)
   3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)
   4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)
   5. [Set up the Rust development environment](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)

   You can click on the links to access the courses.
   ```

## Feladat

Az Azure OpenAI Function Calling tanulás folytatásához építhetsz:

- Több paramétert a függvényhez, amely segíthet a tanulóknak még több kurzus megtalálásában.

- Hozz létre egy másik függvényhívást, amely több információt vesz fel a tanulótól, például az anyanyelvét
- Hozz létre hibakezelést arra az esetre, ha a függvényhívás és/vagy az API hívás nem ad vissza megfelelő tanfolyamokat

Tipp: Kövesd a [Learn API referencia dokumentációját](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst), hogy lásd, hogyan és hol érhető el ez az adat.

## Nagyszerű munka! Folytasd az utat

A lecke befejezése után nézd meg a [Generative AI Learning gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd a Generatív AI tudásodat!

Lépj tovább a 12. leckéhez, ahol megnézzük, hogyan lehet [UX-et tervezni AI alkalmazásokhoz](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->