<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77a48a201447be19aa7560706d6f93a0",
  "translation_date": "2025-07-09T14:35:21+00:00",
  "source_file": "11-integrating-with-function-calling/README.md",
  "language_code": "sv"
}
-->
# Integrering med function calling

[![Integrating with function calling](../../../translated_images/11-lesson-banner.d78860d3e1f041e2c3426b1c052e1590738d2978db584a08efe1efbca299ed82.sv.png)](https://aka.ms/gen-ai-lesson11-gh?WT.mc_id=academic-105485-koreyst)

Du har lärt dig en hel del hittills i de tidigare lektionerna. Men vi kan förbättra oss ytterligare. Några saker vi kan ta itu med är hur vi kan få ett mer konsekvent svarformat för att göra det enklare att arbeta med svaret längre fram. Dessutom kanske vi vill lägga till data från andra källor för att ytterligare berika vår applikation.

De ovan nämnda problemen är vad detta kapitel syftar till att lösa.

## Introduktion

Den här lektionen kommer att täcka:

- Förklara vad function calling är och dess användningsområden.
- Skapa ett function call med Azure OpenAI.
- Hur man integrerar ett function call i en applikation.

## Lärandemål

I slutet av denna lektion kommer du att kunna:

- Förklara syftet med att använda function calling.
- Ställa in Function Call med Azure OpenAI Service.
- Designa effektiva function calls för din applikations användningsfall.

## Scenario: Förbättra vår chatbot med funktioner

För denna lektion vill vi bygga en funktion för vårt utbildningsstartup som låter användare använda en chatbot för att hitta tekniska kurser. Vi kommer att rekommendera kurser som passar deras kunskapsnivå, nuvarande roll och teknikintresse.

För att slutföra detta scenario kommer vi att använda en kombination av:

- `Azure OpenAI` för att skapa en chattupplevelse för användaren.
- `Microsoft Learn Catalog API` för att hjälpa användare att hitta kurser baserat på användarens förfrågan.
- `Function Calling` för att ta användarens fråga och skicka den till en funktion för att göra API-förfrågan.

För att komma igång, låt oss titta på varför vi skulle vilja använda function calling från början:

## Varför Function Calling

Innan function calling var svaren från en LLM ostrukturerade och inkonsekventa. Utvecklare var tvungna att skriva komplex valideringskod för att säkerställa att de kunde hantera varje variation av ett svar. Användare kunde inte få svar på frågor som "Vad är det aktuella vädret i Stockholm?". Detta berodde på att modellerna var begränsade till den tid då datan tränades.

Function Calling är en funktion i Azure OpenAI Service för att övervinna följande begränsningar:

- **Konsekvent svarformat**. Om vi kan kontrollera svarformatet bättre kan vi enklare integrera svaret vidare till andra system.
- **Extern data**. Möjlighet att använda data från andra källor i en applikation i ett chatt-sammanhang.

## Illustrera problemet genom ett scenario

> Vi rekommenderar att du använder [inkluderade notebook](../../../11-integrating-with-function-calling/python/aoai-assignment.ipynb) om du vill köra scenariot nedan. Du kan också bara läsa med medan vi försöker illustrera ett problem där funktioner kan hjälpa till att lösa problemet.

Låt oss titta på exemplet som illustrerar problemet med svarformatet:

Anta att vi vill skapa en databas med studentdata så att vi kan föreslå rätt kurs för dem. Nedan har vi två beskrivningar av studenter som är mycket lika i den data de innehåller.

1. Skapa en anslutning till vår Azure OpenAI-resurs:

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

   Nedan är lite Python-kod för att konfigurera vår anslutning till Azure OpenAI där vi sätter `api_type`, `api_base`, `api_version` och `api_key`.

1. Skapa två studentbeskrivningar med variablerna `student_1_description` och `student_2_description`.

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   Vi vill skicka ovanstående studentbeskrivningar till en LLM för att tolka datan. Denna data kan senare användas i vår applikation och skickas till ett API eller lagras i en databas.

1. Låt oss skapa två identiska prompts där vi instruerar LLM vad för information vi är intresserade av:

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

   Ovanstående prompts instruerar LLM att extrahera information och returnera svaret i JSON-format.

1. Efter att ha satt upp prompts och anslutningen till Azure OpenAI, skickar vi nu prompts till LLM genom att använda `openai.ChatCompletion`. Vi lagrar prompten i variabeln `messages` och tilldelar rollen `user`. Detta för att efterlikna ett meddelande från en användare som skrivs till en chatbot.

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

Nu kan vi skicka båda förfrågningarna till LLM och undersöka svaret vi får genom att hitta det så här `openai_response1['choices'][0]['message']['content']`.

1. Slutligen kan vi konvertera svaret till JSON-format genom att anropa `json.loads`:

   ```python
   # Loading the response as a JSON object
   json_response1 = json.loads(openai_response1.choices[0].message.content)
   json_response1
   ```

   Svar 1:

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   Svar 2:

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   Även om prompts är samma och beskrivningarna liknar varandra, ser vi att värdena för egenskapen `Grades` är formaterade olika, eftersom vi ibland kan få formatet `3.7` eller `3.7 GPA` till exempel.

   Detta resultat beror på att LLM tar emot ostrukturerad data i form av den skrivna prompten och returnerar också ostrukturerad data. Vi behöver ha ett strukturerat format så att vi vet vad vi kan förvänta oss när vi lagrar eller använder denna data.

Så hur löser vi då formateringsproblemet? Genom att använda function calling kan vi säkerställa att vi får strukturerad data tillbaka. När vi använder function calling, anropar eller kör LLM faktiskt inga funktioner. Istället skapar vi en struktur för LLM att följa i sina svar. Vi använder sedan dessa strukturerade svar för att veta vilken funktion som ska köras i våra applikationer.

![function flow](../../../translated_images/Function-Flow.083875364af4f4bb69bd6f6ed94096a836453183a71cf22388f50310ad6404de.sv.png)

Vi kan sedan ta det som returneras från funktionen och skicka tillbaka detta till LLM. LLM kommer då att svara med naturligt språk för att besvara användarens fråga.

## Användningsområden för function calls

Det finns många olika användningsområden där function calls kan förbättra din app, till exempel:

- **Anropa externa verktyg**. Chatbots är bra på att ge svar på frågor från användare. Genom att använda function calling kan chatbots använda meddelanden från användare för att utföra vissa uppgifter. Till exempel kan en student be chatboten att "Skicka ett mejl till min lärare och säg att jag behöver mer hjälp med detta ämne". Detta kan göra ett function call till `send_email(to: string, body: string)`

- **Skapa API- eller databasfrågor**. Användare kan hitta information med naturligt språk som konverteras till en formaterad fråga eller API-förfrågan. Ett exempel kan vara en lärare som frågar "Vilka är studenterna som slutförde senaste uppgiften" vilket kan anropa en funktion som heter `get_completed(student_name: string, assignment: int, current_status: string)`

- **Skapa strukturerad data**. Användare kan ta en textblock eller CSV och använda LLM för att extrahera viktig information från det. Till exempel kan en student konvertera en Wikipedia-artikel om fredsavtal för att skapa AI-flashcards. Detta kan göras med en funktion som heter `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)`

## Skapa ditt första function call

Processen för att skapa ett function call inkluderar 3 huvudsteg:

1. **Anropa** Chat Completions API med en lista av dina funktioner och ett användarmeddelande.
2. **Läsa** modellens svar för att utföra en åtgärd, t.ex. köra en funktion eller göra ett API-anrop.
3. **Göra** ett nytt anrop till Chat Completions API med svaret från din funktion för att använda den informationen för att skapa ett svar till användaren.

![LLM Flow](../../../translated_images/LLM-Flow.3285ed8caf4796d7343c02927f52c9d32df59e790f6e440568e2e951f6ffa5fd.sv.png)

### Steg 1 - skapa meddelanden

Det första steget är att skapa ett användarmeddelande. Detta kan tilldelas dynamiskt genom att ta värdet från en textinmatning eller så kan du tilldela ett värde här. Om detta är första gången du arbetar med Chat Completions API behöver vi definiera `role` och `content` i meddelandet.

`role` kan vara antingen `system` (skapa regler), `assistant` (modellen) eller `user` (slutanvändaren). För function calling kommer vi att tilldela detta som `user` och ett exempel på fråga.

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Genom att tilldela olika roller blir det tydligt för LLM om det är systemet som säger något eller användaren, vilket hjälper till att bygga en konversationshistorik som LLM kan bygga vidare på.

### Steg 2 - skapa funktioner

Nästa steg är att definiera en funktion och parametrarna för den funktionen. Vi kommer att använda bara en funktion här som heter `search_courses` men du kan skapa flera funktioner.

> **Important** : Funktioner inkluderas i systemmeddelandet till LLM och räknas mot det antal tokens du har tillgängligt.

Nedan skapar vi funktionerna som en array av objekt. Varje objekt är en funktion och har egenskaperna `name`, `description` och `parameters`:

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

Låt oss beskriva varje funktionsinstans mer i detalj nedan:

- `name` - Namnet på funktionen som vi vill att ska anropas.
- `description` - Detta är beskrivningen av hur funktionen fungerar. Här är det viktigt att vara specifik och tydlig.
- `parameters` - En lista av värden och format som du vill att modellen ska producera i sitt svar. Parametrarna består av objekt där objekten har följande egenskaper:
  1.  `type` - Datatypen som egenskaperna kommer att lagras i.
  1.  `properties` - Lista över specifika värden som modellen kommer att använda i sitt svar
      1. `name` - Nyckeln är namnet på egenskapen som modellen kommer att använda i sitt formaterade svar, till exempel `product`.
      1. `type` - Datatypen för denna egenskap, till exempel `string`.
      1. `description` - Beskrivning av den specifika egenskapen.

Det finns också en valfri egenskap `required` - obligatorisk egenskap för att function call ska kunna genomföras.

### Steg 3 - Göra function call

Efter att ha definierat en funktion behöver vi nu inkludera den i anropet till Chat Completion API. Vi gör detta genom att lägga till `functions` i förfrågan. I detta fall `functions=functions`.

Det finns också ett alternativ att sätta `function_call` till `auto`. Det betyder att vi låter LLM bestämma vilken funktion som ska anropas baserat på användarens meddelande istället för att tilldela det själva.

Här är lite kod nedan där vi anropar `ChatCompletion.create`, notera hur vi sätter `functions=functions` och `function_call="auto"` och därmed ger LLM valet när funktionerna vi tillhandahåller ska anropas:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

Svaret som kommer tillbaka ser nu ut så här:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

Här kan vi se hur funktionen `search_courses` anropades och med vilka argument, som listas i egenskapen `arguments` i JSON-svaret.

Slutsatsen är att LLM kunde hitta data som passar argumenten för funktionen eftersom den extraherade det från värdet som gavs till parametern `messages` i chat completion-anropet. Nedan är en påminnelse om värdet i `messages`:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Som du kan se extraherades `student`, `Azure` och `beginner` från `messages` och sattes som input till funktionen. Att använda funktioner på detta sätt är ett utmärkt sätt att extrahera information från en prompt men också att ge struktur till LLM och ha återanvändbar funktionalitet.

Nästa steg är att se hur vi kan använda detta i vår app.

## Integrera function calls i en applikation

Efter att vi har testat det formaterade svaret från LLM kan vi nu integrera detta i en applikation.

### Hantera flödet

För att integrera detta i vår applikation, låt oss ta följande steg:

1. Först gör vi anropet till OpenAI-tjänsterna och lagrar meddelandet i en variabel som heter `response_message`.

   ```python
   response_message = response.choices[0].message
   ```

1. Nu definierar vi funktionen som kommer att anropa Microsoft Learn API för att få en lista med kurser:

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

   Notera hur vi nu skapar en faktisk Python-funktion som mappar till funktionsnamnen som introducerades i variabeln `functions`. Vi gör också riktiga externa API-anrop för att hämta den data vi behöver. I detta fall går vi mot Microsoft Learn API för att söka efter utbildningsmoduler.

Okej, vi skapade variabeln `functions` och en motsvarande Python-funktion, hur berättar vi för LLM hur dessa två ska kopplas ihop så att vår Python-funktion anropas?

1. För att se om vi behöver anropa en Python-funktion måste vi titta i LLM-svaret och se om `function_call` är en del av det och anropa den angivna funktionen. Så här kan du göra den nämnda kontrollen nedan:

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

   Dessa tre rader säkerställer att vi extraherar funktionsnamnet, argumenten och gör anropet:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   Nedan är utskriften från att köra vår kod:

   **Output**

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

1. Nu skickar vi det uppdaterade meddelandet, `messages` till LLM så att vi kan få ett svar i naturligt språk istället för ett API-svar i JSON-format.

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

   **Output**

   ```python
   {
     "role": "assistant",
     "content": "I found some good courses for beginner students to learn Azure:\n\n1. [Describe concepts of cryptography] (https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n5. [Set up the Rust development environment](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\nYou can click on the links to access the courses."
   }

   ```

## Uppgift

För att fortsätta din inlärning av Azure OpenAI Function Calling kan du bygga:

- Fler parametrar för funktionen som kan hjälpa användare att hitta fler kurser.
- Skapa ett annat function call som tar mer information från användaren, som deras modersmål.
- Skapa felhantering när function call och/eller API-anrop inte returnerar några lämpliga kurser.
## Bra jobbat! Fortsätt resan

Efter att ha slutfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla dina kunskaper inom Generative AI!

Gå vidare till Lektion 12, där vi kommer att titta på hur man [designar UX för AI-applikationer](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.