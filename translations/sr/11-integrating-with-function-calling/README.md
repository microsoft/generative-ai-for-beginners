<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77a48a201447be19aa7560706d6f93a0",
  "translation_date": "2025-05-19T21:39:01+00:00",
  "source_file": "11-integrating-with-function-calling/README.md",
  "language_code": "sr"
}
-->
# Integracija sa pozivanjem funkcija

Naučili ste dosta do sada u prethodnim lekcijama. Međutim, možemo još više poboljšati. Neke stvari koje možemo obraditi su kako možemo dobiti konzistentniji format odgovora kako bi bilo lakše raditi sa odgovorom nizvodno. Takođe, možda želimo dodati podatke iz drugih izvora kako bismo dodatno obogatili našu aplikaciju.

Gore navedeni problemi su ono što ovo poglavlje želi da reši.

## Uvod

Ova lekcija će pokriti:

- Objašnjenje šta je pozivanje funkcija i njegovi slučajevi korišćenja.
- Kreiranje poziva funkcije koristeći Azure OpenAI.
- Kako integrisati poziv funkcije u aplikaciju.

## Ciljevi učenja

Do kraja ove lekcije, moći ćete da:

- Objasnite svrhu korišćenja pozivanja funkcija.
- Postavite Poziv Funkcije koristeći Azure OpenAI Service.
- Dizajnirate efikasne pozive funkcija za slučaj korišćenja vaše aplikacije.

## Scenario: Poboljšanje našeg chatbota sa funkcijama

Za ovu lekciju, želimo da izgradimo funkciju za našu startup edukaciju koja omogućava korisnicima da koriste chatbot za pronalaženje tehničkih kurseva. Preporučićemo kurseve koji odgovaraju njihovom nivou veština, trenutnoj ulozi i tehnologiji koja ih interesuje.

Da bismo završili ovaj scenario, koristićemo kombinaciju:

- `Azure OpenAI` da kreiramo chat iskustvo za korisnika.
- `Microsoft Learn Catalog API` da pomognemo korisnicima da pronađu kurseve na osnovu zahteva korisnika.
- `Function Calling` da uzmemo upit korisnika i pošaljemo ga funkciji da napravi API zahtev.

Da bismo počeli, pogledajmo zašto bismo uopšte želeli da koristimo pozivanje funkcija:

## Zašto Pozivanje Funkcija

Pre pozivanja funkcija, odgovori iz LLM-a bili su nestrukturirani i nekonzistentni. Programeri su morali pisati složen kod za validaciju kako bi bili sigurni da mogu obraditi svaku varijaciju odgovora. Korisnici nisu mogli dobiti odgovore kao "Kakvo je trenutno vreme u Stokholmu?". To je zato što su modeli bili ograničeni na vreme kada su podaci bili obučeni.

Pozivanje funkcija je funkcija Azure OpenAI Service koja prevazilazi sledeće ograničenja:

- **Konzistentan format odgovora**. Ako možemo bolje kontrolisati format odgovora, možemo lakše integrisati odgovor nizvodno u druge sisteme.
- **Spoljni podaci**. Mogućnost korišćenja podataka iz drugih izvora aplikacije u kontekstu chata.

## Ilustracija problema kroz scenario

> Preporučujemo da koristite [priloženi notebook](../../../11-integrating-with-function-calling/python/aoai-assignment.ipynb) ako želite da pokrenete scenario ispod. Takođe možete samo čitati dalje dok pokušavamo da ilustrujemo problem gde funkcije mogu pomoći u rešavanju problema.

Pogledajmo primer koji ilustruje problem formata odgovora:

Recimo da želimo da kreiramo bazu podataka studentskih podataka kako bismo im mogli predložiti pravi kurs. Ispod imamo dva opisa studenata koji su veoma slični u podacima koje sadrže.

1. Kreirajte vezu sa našim Azure OpenAI resursom:

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

   Ispod je neki Python kod za konfigurisanje naše veze sa Azure OpenAI gde postavljamo `api_type`, `api_base`, `api_version` and `api_key`.

1. Creating two student descriptions using variables `student_1_description` and `student_2_description`.

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   Želimo da pošaljemo gore navedene studentske opise LLM-u da parsira podatke. Ovi podaci kasnije mogu biti korišćeni u našoj aplikaciji i poslati API-ju ili sačuvani u bazi podataka.

1. Kreirajmo dva identična podsticaja u kojima instruiramo LLM o informacijama koje nas interesuju:

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

   Gore navedeni podsticaji instruiraju LLM da izvuče informacije i vrati odgovor u JSON formatu.

1. Nakon postavljanja podsticaja i veze sa Azure OpenAI, sada ćemo poslati podsticaje LLM-u koristeći `openai.ChatCompletion`. We store the prompt in the `messages` variable and assign the role to `user`. Ovo je da imitira poruku od korisnika koja se piše chatbotu.

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

Sada možemo poslati oba zahteva LLM-u i ispitati odgovor koji dobijemo pronalazeći ga ovako `openai_response1['choices'][0]['message']['content']`.

1. Lastly, we can convert the response to JSON format by calling `json.loads`:

   ```python
   # Loading the response as a JSON object
   json_response1 = json.loads(openai_response1.choices[0].message.content)
   json_response1
   ```

   Odgovor 1:

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   Odgovor 2:

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   Iako su podsticaji isti, a opisi slični, vidimo vrednosti `Grades` property formatted differently, as we can sometimes get the format `3.7` or `3.7 GPA` for example.

   This result is because the LLM takes unstructured data in the form of the written prompt and returns also unstructured data. We need to have a structured format so that we know what to expect when storing or using this data

So how do we solve the formatting problem then? By using functional calling, we can make sure that we receive structured data back. When using function calling, the LLM does not actually call or run any functions. Instead, we create a structure for the LLM to follow for its responses. We then use those structured responses to know what function to run in our applications.

![function flow](../../../translated_images/Function-Flow.01a723a374f79e5856d9915c39e16c59fa2a00c113698b22a28e616224f407e1.sr.png)

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

![LLM Flow](../../../translated_images/LLM-Flow.7df9f166be50aa324705f2ccddc04a27cfc7b87e57b1fbe65eb534059a3b8b66.sr.png)

### Step 1 - creating messages

The first step is to create a user message. This can be dynamically assigned by taking the value of a text input or you can assign a value here. If this is your first time working with the Chat Completions API, we need to define the `role` and the `content` of the message.

The `role` can be either `system` (creating rules), `assistant` (the model) or `user` (the end-user). For function calling, we will assign this as `user` i primer pitanja.

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Dodeljivanjem različitih uloga, jasno je LLM-u da li sistem nešto govori ili korisnik, što pomaže u izgradnji istorije razgovora na kojoj LLM može graditi.

### Korak 2 - kreiranje funkcija

Sledeće, definišemo funkciju i parametre te funkcije. Koristićemo samo jednu funkciju ovde nazvanu `search_courses` but you can create multiple functions.

> **Important** : Functions are included in the system message to the LLM and will be included in the amount of available tokens you have available.

Below, we create the functions as an array of items. Each item is a function and has properties `name`, `description` and `parameters`:

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

Hajde da opišemo svaku instancu funkcije detaljnije ispod:

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

Here's some code below where we call `ChatCompletion.create`, note how we set `functions=functions` and `function_call="auto"` i time dajemo LLM-u izbor kada da pozove funkcije koje mu pružamo:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

Odgovor koji dolazi nazad sada izgleda ovako:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

Ovde možemo videti kako funkcija `search_courses` was called and with what arguments, as listed in the `arguments` property in the JSON response.

The conclusion the LLM was able to find the data to fit the arguments of the function as it was extracting it from the value provided to the `messages` parameter in the chat completion call. Below is a reminder of the `messages` vrednost:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Kao što vidite, `student`, `Azure` and `beginner` was extracted from `messages` and set as input to the function. Using functions this way is a great way to extract information from a prompt but also to provide structure to the LLM and have reusable functionality.

Next, we need to see how we can use this in our app.

## Integrating Function Calls into an Application

After we have tested the formatted response from the LLM, we can now integrate this into an application.

### Managing the flow

To integrate this into our application, let's take the following steps:

1. First, let's make the call to the OpenAI services and store the message in a variable called `response_message`.

   ```python
   response_message = response.choices[0].message
   ```

1. Sada ćemo definisati funkciju koja će pozvati Microsoft Learn API da dobije listu kurseva:

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

   Obratite pažnju kako sada kreiramo stvarnu Python funkciju koja se mapira na nazive funkcija uvedene u `functions` variable. We're also making real external API calls to fetch the data we need. In this case, we go against the Microsoft Learn API to search for training modules.

Ok, so we created `functions` variables and a corresponding Python function, how do we tell the LLM how to map these two together so our Python function is called?

1. To see if we need to call a Python function, we need to look into the LLM response and see if `function_call` je deo toga i poziva istaknutu funkciju. Evo kako možete napraviti pomenutu proveru ispod:

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

   Ove tri linije osiguravaju da izdvojimo naziv funkcije, argumente i napravimo poziv:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   Ispod je izlaz iz pokretanja našeg koda:

   **Izlaz**

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

1. Sada ćemo poslati ažuriranu poruku, `messages` LLM-u kako bismo mogli primiti odgovor u prirodnom jeziku umesto API JSON formatiranog odgovora.

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

   **Izlaz**

   ```python
   {
     "role": "assistant",
     "content": "I found some good courses for beginner students to learn Azure:\n\n1. [Describe concepts of cryptography] (https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n5. [Set up the Rust development environment](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\nYou can click on the links to access the courses."
   }

   ```

## Zadatak

Da biste nastavili svoje učenje o Azure OpenAI Pozivanju Funkcija možete izgraditi:

- Više parametara funkcije koji mogu pomoći učenicima da pronađu više kurseva.
- Kreirajte drugi poziv funkcije koji uzima više informacija od učenika kao što je njihov maternji jezik.
- Kreirajte rukovanje greškama kada poziv funkcije i/ili API poziv ne vrate odgovarajuće kurseve.

Saveti: Pratite stranicu [Learn API reference documentation](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) da vidite kako i gde su ti podaci dostupni.

## Odličan rad! Nastavite putovanje

Nakon završetka ove lekcije, pogledajte našu [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) da nastavite da unapređujete svoje znanje o Generativnoj AI!

Pređite na Lekciju 12, gde ćemo pogledati kako [dizajnirati UX za AI aplikacije](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да постигнемо тачност, молимо вас да будете свесни да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације, препоручује се професионални људски превод. Не сносимо одговорност за било каква погрешна схватања или погрешна тумачења која произилазе из коришћења овог превода.