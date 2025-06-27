<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77a48a201447be19aa7560706d6f93a0",
  "translation_date": "2025-06-25T20:00:49+00:00",
  "source_file": "11-integrating-with-function-calling/README.md",
  "language_code": "hu"
}
-->
# Integráció a függvényhívással

Megtanultál már elég sokat az előző leckék során. Azonban tovább tudunk fejlődni. Néhány dolog, amit megvizsgálhatunk, az, hogy hogyan kaphatunk egységesebb válaszformátumot, hogy könnyebben tudjunk dolgozni a válaszokkal a továbbiakban. Emellett esetleg szeretnénk más forrásokból származó adatokat hozzáadni, hogy tovább gazdagítsuk alkalmazásunkat.

A fent említett problémák azok, amelyeket ez a fejezet meg kíván oldani.

## Bevezetés

Ez a lecke lefedi:

- Magyarázat arra, hogy mi a függvényhívás és milyen felhasználási esetei vannak.
- Függvényhívás létrehozása az Azure OpenAI segítségével.
- Hogyan integráljuk a függvényhívást egy alkalmazásba.

## Tanulási célok

A lecke végére képes leszel:

- Magyarázni a függvényhívás használatának célját.
- Beállítani a függvényhívást az Azure OpenAI Szolgáltatás segítségével.
- Hatékony függvényhívásokat tervezni az alkalmazásod felhasználási eseteihez.

## Szcenárió: A chatbotunk javítása függvényekkel

Ebben a leckében egy funkciót szeretnénk építeni oktatási startupunk számára, amely lehetővé teszi a felhasználók számára, hogy egy chatbot segítségével technikai kurzusokat találjanak. Olyan kurzusokat fogunk ajánlani, amelyek megfelelnek a készségszintjüknek, jelenlegi szerepüknek és az érdeklődési technológiájuknak.

Ennek a szcenáriónak a megvalósításához a következőket fogjuk használni:

- `Azure OpenAI` a felhasználói chatélmény létrehozásához.
- `Microsoft Learn Catalog API` a felhasználók számára kurzusok kereséséhez a felhasználó kérésének alapján.
- `Function Calling` a felhasználói lekérdezés fogadására és egy függvényhez való küldésére, hogy API-kérést indítsunk.

Kezdjük azzal, hogy megvizsgáljuk, miért is szeretnénk függvényhívást használni:

## Miért függvényhívás

A függvényhívás előtt az LLM-ből érkező válaszok strukturálatlanok és következetlenek voltak. A fejlesztőknek bonyolult validációs kódot kellett írniuk, hogy biztosak legyenek benne, hogy képesek kezelni a válaszok minden variációját. A felhasználók nem tudtak olyan kérdésekre választ kapni, mint például "Mi a jelenlegi időjárás Stockholmban?". Ennek oka, hogy a modellek korlátozottak voltak az adatgyűjtés időpontjáig.

A függvényhívás az Azure OpenAI Szolgáltatás egyik funkciója, amely a következő korlátokat hivatott leküzdeni:

- **Konzisztens válaszformátum**. Ha jobban tudjuk kontrollálni a válaszformátumot, könnyebben integrálhatjuk a választ más rendszerekbe.
- **Külső adatok**. Képesség arra, hogy más forrásokból származó adatokat használjunk egy alkalmazásban chat kontextusban.

## A probléma illusztrálása egy szcenárión keresztül

> Javasoljuk, hogy használd a [mellékelt notebookot](../../../11-integrating-with-function-calling/python/aoai-assignment.ipynb), ha futtatni szeretnéd az alábbi szcenáriót. Az is elegendő, ha végigolvasod, ahogy próbáljuk illusztrálni egy problémát, amelyben a függvények segíthetnek megoldani a problémát.

Nézzük meg az példát, amely illusztrálja a válaszformátum problémát:

Tegyük fel, hogy szeretnénk létrehozni egy adatbázist a diákok adataival, hogy javasolni tudjuk nekik a megfelelő kurzust. Az alábbiakban két olyan diák leírását látjuk, amelyek nagyon hasonló adatokat tartalmaznak.

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

   Az alábbiakban néhány Python kód található az Azure OpenAI-hoz való kapcsolódás konfigurálására, ahol beállítjuk `api_type`, `api_base`, `api_version` and `api_key`.

1. Creating two student descriptions using variables `student_1_description` and `student_2_description`.

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   Szeretnénk elküldeni a fenti diák leírásokat egy LLM-nek, hogy elemezze az adatokat. Ezek az adatok később felhasználhatók lesznek az alkalmazásunkban, és elküldhetők egy API-hoz vagy tárolhatók egy adatbázisban.

1. Készítsünk két azonos promptot, amelyekben utasítjuk az LLM-et, hogy milyen információk érdekelnek minket:

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

   A fenti promptok utasítják az LLM-et, hogy információt nyerjen ki, és adja vissza a választ JSON formátumban.

1. A promptok és az Azure OpenAI kapcsolódás beállítása után most elküldjük a promptokat az LLM-nek az `openai.ChatCompletion`. We store the prompt in the `messages` variable and assign the role to `user` használatával. Ez utánozza a felhasználó által írt üzenetet egy chatbotnak.

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

Most elküldhetjük mindkét kérést az LLM-nek, és megvizsgálhatjuk a kapott választ, úgy hogy megtaláljuk `openai_response1['choices'][0]['message']['content']`.

1. Lastly, we can convert the response to JSON format by calling `json.loads`:

   ```python
   # Loading the response as a JSON object
   json_response1 = json.loads(openai_response1.choices[0].message.content)
   json_response1
   ```

   Válasz 1:

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   Válasz 2:

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   Annak ellenére, hogy a promptok ugyanazok és a leírások hasonlóak, látjuk az `Grades` property formatted differently, as we can sometimes get the format `3.7` or `3.7 GPA` for example.

   This result is because the LLM takes unstructured data in the form of the written prompt and returns also unstructured data. We need to have a structured format so that we know what to expect when storing or using this data

So how do we solve the formatting problem then? By using functional calling, we can make sure that we receive structured data back. When using function calling, the LLM does not actually call or run any functions. Instead, we create a structure for the LLM to follow for its responses. We then use those structured responses to know what function to run in our applications.

![function flow](../../../translated_images/Function-Flow.083875364af4f4bb69bd6f6ed94096a836453183a71cf22388f50310ad6404de.hu.png)

We can then take what is returned from the function and send this back to the LLM. The LLM will then respond using natural language to answer the user's query.

## Use Cases for using function calls

There are many different use cases where function calls can improve your app like:

- **Calling External Tools**. Chatbots are great at providing answers to questions from users. By using function calling, the chatbots can use messages from users to complete certain tasks. For example, a student can ask the chatbot to "Send an email to my instructor saying I need more assistance with this subject". This can make a function call to `send_email(to: string, body: string)`

- **Create API or Database Queries**. Users can find information using natural language that gets converted into a formatted query or API request. An example of this could be a teacher who requests "Who are the students that completed the last assignment" which could call a function named `get_completed(student_name: string, assignment: int, current_status: string)`

- **Creating Structured Data**. Users can take a block of text or CSV and use the LLM to extract important information from it. For example, a student can convert a Wikipedia article about peace agreements to create AI flashcards. This can be done by using a function called `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)`

## Creating Your First Function Call

The process of creating a function call includes 3 main steps:

1. **Calling** the Chat Completions API with a list of your functions and a user message.
2. **Reading** the model's response to perform an action i.e. execute a function or API Call.
3. **Making** another call to Chat Completions API with the response from your function to use that information to create a response to the user.

![LLM Flow](../../../translated_images/LLM-Flow.3285ed8caf4796d7343c02927f52c9d32df59e790f6e440568e2e951f6ffa5fd.hu.png)

### Step 1 - creating messages

The first step is to create a user message. This can be dynamically assigned by taking the value of a text input or you can assign a value here. If this is your first time working with the Chat Completions API, we need to define the `role` and the `content` of the message.

The `role` can be either `system` (creating rules), `assistant` (the model) or `user` (the end-user). For function calling, we will assign this as `user` és egy példakérdés értékeit.

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Különböző szerepek hozzárendelésével világossá válik az LLM számára, hogy a rendszer mond valamit vagy a felhasználó, ami segít építeni egy beszélgetési történetet, amire az LLM építhet.

### 2. lépés - függvények létrehozása

Ezután definiálunk egy függvényt és annak paramétereit. Csak egy függvényt fogunk itt használni, amit `search_courses` but you can create multiple functions.

> **Important** : Functions are included in the system message to the LLM and will be included in the amount of available tokens you have available.

Below, we create the functions as an array of items. Each item is a function and has properties `name`, `description` and `parameters`-nek hívunk:

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

Nézzük meg részletesebben az egyes függvény példányokat:

- `name` - The name of the function that we want to have called.
- `description` - This is the description of how the function works. Here it's important to be specific and clear.
- `parameters` - A list of values and format that you want the model to produce in its response. The parameters array consists of items where the items have the following properties:
  1.  `type` - The data type of the properties will be stored in.
  1.  `properties` - List of the specific values that the model will use for its response
      1. `name` - The key is the name of the property that the model will use in its formatted response, for example, `product`.
      1. `type` - The data type of this property, for example, `string`.
      1. `description` - Description of the specific property.

There's also an optional property `required` - required property for the function call to be completed.

### Step 3 - Making the function call

After defining a function, we now need to include it in the call to the Chat Completion API. We do this by adding `functions` to the request. In this case `functions=functions`.

There is also an option to set `function_call` to `auto`. This means we will let the LLM decide which function should be called based on the user message rather than assigning it ourselves.

Here's some code below where we call `ChatCompletion.create`, note how we set `functions=functions` and `function_call="auto"` és így adva az LLM-nek a választási lehetőséget, hogy mikor hívja meg a megadott függvényeket:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

A most visszakapott válasz így néz ki:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

Itt láthatjuk, hogyan hívja meg a `search_courses` was called and with what arguments, as listed in the `arguments` property in the JSON response.

The conclusion the LLM was able to find the data to fit the arguments of the function as it was extracting it from the value provided to the `messages` parameter in the chat completion call. Below is a reminder of the `messages` függvényt:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Ahogy láthatod, `student`, `Azure` and `beginner` was extracted from `messages` and set as input to the function. Using functions this way is a great way to extract information from a prompt but also to provide structure to the LLM and have reusable functionality.

Next, we need to see how we can use this in our app.

## Integrating Function Calls into an Application

After we have tested the formatted response from the LLM, we can now integrate this into an application.

### Managing the flow

To integrate this into our application, let's take the following steps:

1. First, let's make the call to the OpenAI services and store the message in a variable called `response_message`.

   ```python
   response_message = response.choices[0].message
   ```

1. Most definiáljuk azt a függvényt, amely hívja a Microsoft Learn API-t, hogy kapjunk egy listát a kurzusokról:

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

   Figyeld meg, hogy most egy valódi Python függvényt hozunk létre, amely a `functions` variable. We're also making real external API calls to fetch the data we need. In this case, we go against the Microsoft Learn API to search for training modules.

Ok, so we created `functions` variables and a corresponding Python function, how do we tell the LLM how to map these two together so our Python function is called?

1. To see if we need to call a Python function, we need to look into the LLM response and see if `function_call` függvénynévhez kapcsolódik, amely része annak és meghívja a megjelölt függvényt. Így teheted meg az alábbi ellenőrzést:

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

   Ez a három sor biztosítja, hogy kinyerjük a függvény nevét, az argumentumokat és meghívjuk a függvényt:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   Az alábbiakban látható a kódunk futtatásának kimenete:

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

1. Most elküldjük a frissített üzenetet, `messages` az LLM-nek, hogy természetes nyelvi választ kapjunk, ne pedig API JSON formátumú választ.

   ```python
   print("Messages in next request:")
   print(messages)
   print()

   second_response = client.chat.completions.create(
      messages=messages,
      model=deployment,
      function_call="auto",
      functions=functions,
      temperature=0
         )  # get a new response from GPT where it can see the function response


   print(second_response.choices[0].message)
   ```

   **Kimenet**

   ```python
   {
     "role": "assistant",
     "content": "I found some good courses for beginner students to learn Azure:\n\n1. [Describe concepts of cryptography] (https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n5. [Set up the Rust development environment](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\nYou can click on the links to access the courses."
   }

   ```

## Feladat

Az Azure OpenAI Függvényhívás további tanulásához építhetsz:

- Több paramétert a függvényhez, amelyek segíthetnek a tanulóknak több kurzust találni.
- Hozz létre egy másik függvényhívást, amely több információt vesz figyelembe a tanulótól, például az anyanyelvét.
- Hozz létre hibakezelést, amikor a függvényhívás és/vagy API hívás nem ad vissza megfelelő kurzusokat.

Tipp: Kövesd a [Learn API referencia dokumentáció](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) oldalt, hogy lásd, hogyan és hol érhetők el ezek az adatok.

## Remek munka! Folytasd az utat

A lecke befejezése után nézd meg a [Generatív AI Tanulási gyűjteményt](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd a Generatív AI tudásodat!

Lépj tovább a 12. leckére, ahol megvizsgáljuk, hogyan lehet [UX-t tervezni AI alkalmazásokhoz](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Jogi nyilatkozat**:  
Ezt a dokumentumot az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum az anyanyelvén tekinthető a hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás. Nem vállalunk felelősséget semmilyen félreértésért vagy félremagyarázásért, amely a fordítás használatából eredhet.