<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f6f84f9ef2d066cd25850cab93580a50",
  "translation_date": "2025-10-17T21:24:40+00:00",
  "source_file": "11-integrating-with-function-calling/README.md",
  "language_code": "hu"
}
-->
# Funkcióhívás integrálása

[![Funkcióhívás integrálása](../../../translated_images/11-lesson-banner.d78860d3e1f041e2c3426b1c052e1590738d2978db584a08efe1efbca299ed82.hu.png)](https://youtu.be/DgUdCLX8qYQ?si=f1ouQU5HQx6F8Gl2)

Az előző leckék során már sok mindent megtanultál. Azonban még tovább fejleszthetjük a tudásunkat. Néhány dolog, amit érdemes megvizsgálni, hogy hogyan érhetünk el egységesebb válaszformátumot, amely megkönnyíti a válaszok további feldolgozását. Emellett érdemes lehet más forrásokból származó adatokat is hozzáadni, hogy gazdagítsuk az alkalmazásunkat.

Ez a fejezet a fent említett problémák megoldására összpontosít.

## Bevezetés

Ebben a leckében szó lesz:

- A funkcióhívás fogalmáról és felhasználási területeiről.
- Funkcióhívás létrehozásáról az Azure OpenAI segítségével.
- A funkcióhívás integrálásáról egy alkalmazásba.

## Tanulási célok

A lecke végére képes leszel:

- Megmagyarázni, miért érdemes funkcióhívást használni.
- Beállítani a funkcióhívást az Azure OpenAI szolgáltatásban.
- Hatékony funkcióhívásokat tervezni az alkalmazásod céljainak megfelelően.

## Szenárió: Chatbotunk fejlesztése funkciókkal

Ebben a leckében egy olyan funkciót szeretnénk létrehozni oktatási startupunk számára, amely lehetővé teszi a felhasználók számára, hogy egy chatbot segítségével technikai kurzusokat találjanak. Olyan kurzusokat fogunk ajánlani, amelyek megfelelnek a felhasználók képességeinek, jelenlegi szerepkörüknek és érdeklődési technológiájuknak.

A szenárió megvalósításához az alábbiakat fogjuk kombinálni:

- `Azure OpenAI`, hogy chatélményt hozzunk létre a felhasználók számára.
- `Microsoft Learn Catalog API`, hogy segítsünk a felhasználóknak megtalálni a számukra megfelelő kurzusokat.
- `Funkcióhívás`, amely a felhasználó kérését egy funkcióhoz továbbítja, hogy API-kérést generáljon.

Kezdjük azzal, hogy megvizsgáljuk, miért érdemes egyáltalán funkcióhívást használni:

## Miért érdemes funkcióhívást használni?

A funkcióhívás előtt az LLM-ek válaszai strukturálatlanok és következetlenek voltak. A fejlesztőknek bonyolult validációs kódokat kellett írniuk, hogy kezelni tudják a válaszok különböző variációit. A felhasználók nem kaphattak olyan válaszokat, mint például "Mi az aktuális időjárás Stockholmban?". Ennek oka, hogy a modellek korlátozottak voltak az adatok tanítási idejére.

A funkcióhívás az Azure OpenAI szolgáltatás egyik funkciója, amely a következő korlátokat hivatott leküzdeni:

- **Következetes válaszformátum**. Ha jobban tudjuk kontrollálni a válaszformátumot, könnyebben integrálhatjuk a választ más rendszerekbe.
- **Külső adatok**. Lehetőség arra, hogy egy alkalmazás más forrásból származó adatait használjuk egy chatkörnyezetben.

## A probléma szemléltetése egy példán keresztül

> Javasoljuk, hogy használd a [mellékelt notebookot](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreyst), ha futtatni szeretnéd az alábbi példát. Azonban olvashatod is, mivel a célunk az, hogy bemutassuk, hogyan segíthetnek a funkciók a probléma megoldásában.

Nézzük meg egy példát, amely bemutatja a válaszformátum problémáját:

Tegyük fel, hogy szeretnénk létrehozni egy adatbázist a diákok adataival, hogy megfelelő kurzusokat ajánlhassunk nekik. Az alábbiakban két diák leírását látjuk, amelyek nagyon hasonló adatokat tartalmaznak.

1. Kapcsolat létrehozása az Azure OpenAI erőforrásunkkal:

   ```python
   import os
   import json
   from openai import AzureOpenAI
   from dotenv import load_dotenv
   load_dotenv()

   client = AzureOpenAI(
   api_key=os.environ['AZURE_OPENAI_API_KEY'],  # this is also the default, it can be omitted
   api_version = "2023-07-01-preview"
   )

   deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']
   ```

   Az alábbi Python kód konfigurálja az Azure OpenAI-hoz való kapcsolatot, ahol beállítjuk az `api_type`, `api_base`, `api_version` és `api_key` értékeket.

1. Két diák leírásának létrehozása a `student_1_description` és `student_2_description` változók használatával.

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   Az előző diákleírásokat elküldjük egy LLM-nek, hogy elemezze az adatokat. Ezeket az adatokat később felhasználhatjuk az alkalmazásunkban, API-n keresztül továbbíthatjuk vagy adatbázisban tárolhatjuk.

1. Hozzunk létre két azonos promptot, amelyekben utasítjuk az LLM-et, hogy milyen információt szeretnénk kinyerni:

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

   Az előző promptok utasítják az LLM-et, hogy információt nyerjen ki, és JSON formátumban adja vissza a választ.

1. Miután beállítottuk a promptokat és az Azure OpenAI-hoz való kapcsolatot, elküldjük a promptokat az LLM-nek az `openai.ChatCompletion` használatával. A promptot a `messages` változóban tároljuk, és a szerepet `user`-ként adjuk meg. Ez azt szimulálja, mintha egy felhasználó írna üzenetet egy chatbotnak.

   ```python
   # response from prompt one
   openai_response1 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt1}]
   )
   openai_response1.choices[0].message.content

   # response from prompt two
   openai_response2 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt2}]
   )
   openai_response2.choices[0].message.content
   ```

Most elküldhetjük mindkét kérést az LLM-nek, és megvizsgálhatjuk a kapott választ, például így: `openai_response1['choices'][0]['message']['content']`.

1. Végül a választ JSON formátumba konvertálhatjuk a `json.loads` hívásával:

   ```python
   # Loading the response as a JSON object
   json_response1 = json.loads(openai_response1.choices[0].message.content)
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

   Annak ellenére, hogy a promptok azonosak és a leírások hasonlóak, a `Grades` tulajdonság értékei eltérő formátumban jelennek meg, például `3.7` vagy `3.7 GPA`.

   Ez az eredmény azért van, mert az LLM strukturálatlan adatokat kap a megírt prompt formájában, és szintén strukturálatlan adatokat ad vissza. Szükségünk van egy strukturált formátumra, hogy tudjuk, mire számíthatunk az adatok tárolásakor vagy felhasználásakor.

Hogyan oldhatjuk meg tehát a formázási problémát? A funkcióhívás használatával biztosíthatjuk, hogy strukturált adatokat kapjunk vissza. A funkcióhívás során az LLM valójában nem hív meg vagy futtat semmilyen funkciót. Ehelyett létrehozunk egy struktúrát, amelyet az LLM követ a válaszai során. Ezután ezeket a strukturált válaszokat használjuk fel annak eldöntésére, hogy milyen funkciót futtassunk az alkalmazásainkban.

![function flow](../../../translated_images/Function-Flow.083875364af4f4bb69bd6f6ed94096a836453183a71cf22388f50310ad6404de.hu.png)

Ezután a funkcióból visszakapott adatokat elküldhetjük az LLM-nek, amely természetes nyelven válaszol a felhasználó kérdésére.

## Funkcióhívások felhasználási területei

Számos különböző felhasználási terület létezik, ahol a funkcióhívások javíthatják az alkalmazásodat, például:

- **Külső eszközök hívása**. A chatbotok kiválóan alkalmasak arra, hogy válaszokat adjanak a felhasználók kérdéseire. A funkcióhívások használatával a chatbotok a felhasználók üzeneteit felhasználva bizonyos feladatokat is elvégezhetnek. Például egy diák kérheti a chatbotot, hogy "Küldjön egy e-mailt az oktatómnak, hogy több segítségre van szükségem ebben a témában". Ez egy `send_email(to: string, body: string)` nevű funkcióhívást generálhat.

- **API vagy adatbázis lekérdezések létrehozása**. A felhasználók természetes nyelven kereshetnek információkat, amelyeket formázott lekérdezéssé vagy API-kéréssé alakítunk. Például egy tanár kérheti, hogy "Kik azok a diákok, akik befejezték az utolsó feladatot", amely egy `get_completed(student_name: string, assignment: int, current_status: string)` nevű funkciót hívhat meg.

- **Strukturált adatok létrehozása**. A felhasználók egy szöveges blokkot vagy CSV-t használhatnak, és az LLM segítségével kinyerhetik belőle a fontos információkat. Például egy diák egy békeszerződésekről szóló Wikipédia-cikket átalakíthat AI flashcardokká. Ez egy `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)` nevű funkcióval valósítható meg.

## Az első funkcióhívás létrehozása

A funkcióhívás létrehozásának folyamata három fő lépésből áll:

1. **Hívás** a Chat Completions API-hoz a funkciók listájával és egy felhasználói üzenettel.
2. **Olvasás** a modell válaszából, hogy végrehajtsunk egy műveletet, például egy funkciót vagy API-hívást.
3. **Újabb hívás** a Chat Completions API-hoz a funkció válaszával, hogy ezt az információt felhasználva válaszoljunk a felhasználónak.

![LLM Flow](../../../translated_images/LLM-Flow.3285ed8caf4796d7343c02927f52c9d32df59e790f6e440568e2e951f6ffa5fd.hu.png)

### 1. lépés - üzenetek létrehozása

Az első lépés egy felhasználói üzenet létrehozása. Ez dinamikusan hozzárendelhető egy szövegbeviteli értékhez, vagy itt is megadható. Ha először dolgozol a Chat Completions API-val, meg kell határoznunk az üzenet `role` és `content` értékét.

A `role` lehet `system` (szabályok létrehozása), `assistant` (a modell) vagy `user` (a végfelhasználó). A funkcióhívás esetében ezt `user`-ként fogjuk megadni, és egy példa kérdést.

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

A különböző szerepek hozzárendelésével egyértelművé válik az LLM számára, hogy a rendszer vagy a felhasználó mond valamit, ami segít egy beszélgetési előzményt létrehozni, amelyre az LLM építhet.

### 2. lépés - funkciók létrehozása

Ezután definiálunk egy funkciót és annak paramétereit. Itt csak egy funkciót fogunk használni, amelynek neve `search_courses`, de több funkciót is létrehozhatsz.

> **Fontos**: A funkciók az LLM rendszerüzenetébe kerülnek, és beleszámítanak az elérhető tokenek számába.

Az alábbiakban létrehozzuk a funkciókat elemek tömbjeként. Minden elem egy funkció, amelynek tulajdonságai: `name`, `description` és `parameters`:

```python
functions = [
   {
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

Nézzük meg részletesebben az egyes funkciókat:

- `name` - A funkció neve, amelyet meg szeretnénk hívni.
- `description` - A funkció működésének leírása. Fontos, hogy specifikus és egyértelmű legyen.
- `parameters` - Az értékek és formátumok listája, amelyeket a modell a válaszában használni fog. A paraméterek tömbje elemekből áll, amelyek a következő tulajdonságokkal rendelkeznek:
  1.  `type` - Az adatok típusa, amelyben a tulajdonságok tárolva lesznek.
  1.  `properties` - Az értékek listája, amelyeket a modell a válaszában használni fog.
      1. `name` - A kulcs neve, amelyet a modell a válaszában használ, például `product`.
      1. `type` - A tulajdonság adattípusa, például `string`.
      1. `description` - A konkrét tulajdonság leírása.

Van egy opcionális `required` tulajdonság is - a funkcióhívás befejezéséhez szükséges tulajdonság.

### 3. lépés - A funkcióhívás végrehajtása

Miután definiáltuk a funkciót, most hozzá kell adnunk a Chat Completion API hívásához. Ezt úgy tesszük meg, hogy hozzáadjuk a `functions` értéket a kéréshez. Ebben az esetben `functions=functions`.

Van egy lehetőség arra is, hogy a `function_call` értékét `auto`-ra állítsuk. Ez azt jelenti, hogy az LLM dönti el, melyik funkciót kell meghívni a felhasználói üzenet alapján, ahelyett hogy mi rendelnénk hozzá.

Az alábbi kódban látható, hogyan hívjuk meg a `ChatCompletion.create`-t, megjegyezve, hogy beállítjuk a `functions=functions` és `function_call="auto"` értékeket, ezzel lehetőséget adva az LLM-nek, hogy eldöntse, mikor hívja meg az általunk biztosított funkciókat:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

A visszaérkező válasz így néz ki:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

Itt láthatjuk, hogy a `search_courses` funkciót hívták meg, és milyen argumentumokkal, amelyeket az `arguments` tulajdonságban találunk a JSON válaszban.

Az LLM képes volt megtalálni az adatokat, amelyek megfelelnek a funkció argumentumainak, mivel azokat a `messages` paraméter értékéből nyerte ki a chat completion hívás során. Az alábbiakban emlékeztetőül a `messages` értéke:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Amint látható, a `student`, `Azure` és `beginner` értékeket a `messages`-ből nyerte ki, és bemeneti adatként állította be a funkcióhoz. A funkciók ilyen módon történő használata nagyszerű módja annak, hogy információt nyerjünk ki egy promptból, valamint hogy strukturált formát biztosítsunk az LLM-nek és újrahasznosítható funkciókat hozzunk létre.

Most nézzük meg, hogyan integrálhatjuk ezt az alkalmazásunkba.

## Funkcióhívások integrálása egy alkalmazásba

Miután teszteltük az LLM formázott válaszát, most integrálhatjuk ezt az alkalmazásunkba.

### A folyamat kezelése

Az alkalmazásba való integráláshoz kövessük az alábbi lépéseket:

1. Először hívjuk meg az OpenAI szolgáltatásokat, és tároljuk az üzenetet egy `response_message` nevű változóban.

   ```python
   response_message = response.choices[0].message
   ```

1. Most definiáljuk azt a funkciót, amely a Microsoft Learn API-t hívja meg, hogy kurzusokat keressen:

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

   Figyeld meg, hogy most egy valódi Python funkciót hozunk létre, amely megfelel a `functions` változóban bevezetett funkcióneveknek. Valódi külső API-hívásokat is végrehajtunk, hogy megszerezzük a szükséges adatokat. Ebben az esetben a Microsoft Learn API-t használjuk, hogy képzési modulokat keressünk.

Oké, létrehoztuk a `functions` változókat és a megfelelő Python funkciót, hogyan mondjuk meg az LLM-nek, hogy hogyan kapcsolja össze ezeket, hogy a Python funkciónk meghívásra kerüljön?

1. Annak megállapításához, hogy szükséges-e Python funkciót hívni, meg kell vizsgálnunk az LLM válaszát, és ellenőriznünk kell, hogy tartalmazza-e a `function_call` értéket, majd meghívni a megadott funkciót. Az alábbiakban látható, hogyan végezhetjük el az említett ellenőrzést:

   ```python
   # Check if the model wants to call a function
   if response_message.function_call.name:
    print("Recommended Function call:")
    print(response_message.function_call.name)
    print()

    # Call the function.
    function_name = response_message.function_call.name

    available_functions = {
            "search_courses": search_courses,
    }
    function_to_call = available_functions[function_name]

    function_args = json.loads(response_message.function_call.arguments)
    function_response = function_to_call(**function_args)

    print("Output of function call:")
    print(function_response)
    print(type(function_response))


    # Add the assistant response and function response to the messages
    messages.append( # adding assistant response to messages
        {
            "role": response_message.role,
            "function_call": {
                "name": function_name,
                "arguments": response_message.function_call.arguments,
            },
            "content": None
        }
    )
    messages.append( # adding function response to messages
        {
            "role": "function",
            "name": function_name,
            "content":function_response,
        }
    )
   ```

   Ez a három sor biztosítja, hogy kinyerjük a funkció nevét, az argumentumokat
- Hozz létre hibakezelést arra az esetre, ha a függvényhívás és/vagy az API-hívás nem ad vissza megfelelő kurzusokat.

Tipp: Nézd meg a [Learn API referencia dokumentáció](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) oldalát, hogy lásd, hogyan és hol érhető el ez az adat.

## Szép munka! Folytasd az utazást

A lecke befejezése után nézd meg a [Generatív AI tanulási gyűjteményt](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd a Generatív AI tudásodat!

Lépj tovább a 12. leckére, ahol azt fogjuk megvizsgálni, hogyan lehet [UX-et tervezni AI alkalmazásokhoz](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.