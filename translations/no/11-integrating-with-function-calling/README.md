<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f6f84f9ef2d066cd25850cab93580a50",
  "translation_date": "2025-10-17T19:18:53+00:00",
  "source_file": "11-integrating-with-function-calling/README.md",
  "language_code": "no"
}
-->
# Integrering med funksjonskall

[![Integrering med funksjonskall](../../../translated_images/11-lesson-banner.d78860d3e1f041e2c3426b1c052e1590738d2978db584a08efe1efbca299ed82.no.png)](https://youtu.be/DgUdCLX8qYQ?si=f1ouQU5HQx6F8Gl2)

Du har lært en god del så langt i de tidligere leksjonene. Men vi kan fortsatt forbedre oss. Noen ting vi kan ta tak i er hvordan vi kan få et mer konsistent responsformat for å gjøre det enklere å jobbe med responsen videre. I tillegg kan vi ønske å legge til data fra andre kilder for å berike applikasjonen vår ytterligere.

Problemene nevnt ovenfor er det denne leksjonen tar sikte på å løse.

## Introduksjon

Denne leksjonen vil dekke:

- Forklare hva funksjonskall er og bruksområdene.
- Opprette et funksjonskall ved hjelp av Azure OpenAI.
- Hvordan integrere et funksjonskall i en applikasjon.

## Læringsmål

Ved slutten av denne leksjonen vil du kunne:

- Forklare hensikten med å bruke funksjonskall.
- Sette opp funksjonskall ved hjelp av Azure OpenAI Service.
- Designe effektive funksjonskall for din applikasjons bruksområde.

## Scenario: Forbedre chatboten vår med funksjoner

I denne leksjonen ønsker vi å bygge en funksjon for vår utdanningsstartup som lar brukere bruke en chatbot for å finne tekniske kurs. Vi vil anbefale kurs som passer deres ferdighetsnivå, nåværende rolle og teknologi de er interessert i.

For å fullføre dette scenariet vil vi bruke en kombinasjon av:

- `Azure OpenAI` for å skape en chatteopplevelse for brukeren.
- `Microsoft Learn Catalog API` for å hjelpe brukere med å finne kurs basert på deres forespørsel.
- `Funksjonskall` for å ta brukerens forespørsel og sende den til en funksjon for å gjøre API-forespørselen.

For å komme i gang, la oss se på hvorfor vi i det hele tatt vil bruke funksjonskall:

## Hvorfor funksjonskall

Før funksjonskall var svar fra en LLM ustrukturerte og inkonsistente. Utviklere måtte skrive kompleks valideringskode for å sikre at de kunne håndtere hver variasjon av et svar. Brukere kunne ikke få svar som "Hva er været i Stockholm akkurat nå?". Dette er fordi modeller var begrenset til tiden dataene ble trent på.

Funksjonskall er en funksjon i Azure OpenAI Service som overkommer følgende begrensninger:

- **Konsistent responsformat**. Hvis vi kan kontrollere responsformatet bedre, kan vi enklere integrere responsen videre til andre systemer.
- **Eksterne data**. Mulighet til å bruke data fra andre kilder i en applikasjon i en chatte-kontekst.

## Illustrere problemet gjennom et scenario

> Vi anbefaler deg å bruke [den inkluderte notatboken](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) hvis du ønsker å kjøre scenariet nedenfor. Du kan også bare lese videre, da vi prøver å illustrere et problem hvor funksjoner kan hjelpe med å løse det.

La oss se på et eksempel som illustrerer problemet med responsformat:

La oss si at vi ønsker å opprette en database med studentdata slik at vi kan foreslå riktig kurs til dem. Nedenfor har vi to beskrivelser av studenter som er veldig like i dataene de inneholder.

1. Opprett en tilkobling til vår Azure OpenAI-ressurs:

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

   Nedenfor er litt Python-kode for å konfigurere vår tilkobling til Azure OpenAI hvor vi setter `api_type`, `api_base`, `api_version` og `api_key`.

1. Opprett to studentbeskrivelser ved hjelp av variablene `student_1_description` og `student_2_description`.

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   Vi ønsker å sende de ovennevnte studentbeskrivelsene til en LLM for å analysere dataene. Disse dataene kan senere brukes i vår applikasjon og sendes til et API eller lagres i en database.

1. La oss opprette to identiske oppfordringer der vi instruerer LLM om hvilken informasjon vi er interessert i:

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

   De ovennevnte oppfordringene instruerer LLM om å trekke ut informasjon og returnere responsen i JSON-format.

1. Etter å ha satt opp oppfordringene og tilkoblingen til Azure OpenAI, vil vi nå sende oppfordringene til LLM ved å bruke `openai.ChatCompletion`. Vi lagrer oppfordringen i variabelen `messages` og tildeler rollen `user`. Dette er for å etterligne en melding fra en bruker som skrives til en chatbot.

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

Nå kan vi sende begge forespørslene til LLM og undersøke responsen vi mottar ved å finne den slik: `openai_response1['choices'][0]['message']['content']`.

1. Til slutt kan vi konvertere responsen til JSON-format ved å kalle `json.loads`:

   ```python
   # Loading the response as a JSON object
   json_response1 = json.loads(openai_response1.choices[0].message.content)
   json_response1
   ```

   Respons 1:

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   Respons 2:

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   Selv om oppfordringene er de samme og beskrivelsene er like, ser vi verdier for `Grades`-egenskapen formatert forskjellig, da vi noen ganger kan få formatet `3.7` eller `3.7 GPA` for eksempel.

   Dette resultatet skyldes at LLM tar ustrukturert data i form av den skrevne oppfordringen og returnerer også ustrukturert data. Vi trenger å ha et strukturert format slik at vi vet hva vi kan forvente når vi lagrer eller bruker disse dataene.

Så hvordan løser vi formateringsproblemet da? Ved å bruke funksjonskall kan vi sørge for at vi får strukturert data tilbake. Når vi bruker funksjonskall, kaller eller kjører LLM faktisk ikke noen funksjoner. I stedet oppretter vi en struktur for LLM å følge for sine svar. Vi bruker deretter disse strukturerte svarene for å vite hvilken funksjon vi skal kjøre i våre applikasjoner.

![funksjonsflyt](../../../translated_images/Function-Flow.083875364af4f4bb69bd6f6ed94096a836453183a71cf22388f50310ad6404de.no.png)

Vi kan deretter ta det som returneres fra funksjonen og sende dette tilbake til LLM. LLM vil deretter svare ved å bruke naturlig språk for å besvare brukerens forespørsel.

## Bruksområder for funksjonskall

Det finnes mange forskjellige bruksområder hvor funksjonskall kan forbedre appen din, som:

- **Kalle eksterne verktøy**. Chatbots er gode til å gi svar på spørsmål fra brukere. Ved å bruke funksjonskall kan chatbotene bruke meldinger fra brukere til å utføre visse oppgaver. For eksempel kan en student be chatboten om å "Send en e-post til min instruktør og si at jeg trenger mer hjelp med dette emnet". Dette kan gjøre et funksjonskall til `send_email(to: string, body: string)`.

- **Opprette API- eller databaseforespørsler**. Brukere kan finne informasjon ved hjelp av naturlig språk som blir konvertert til en formatert forespørsel eller API-forespørsel. Et eksempel på dette kan være en lærer som spør "Hvem er studentene som fullførte den siste oppgaven" som kan kalle en funksjon kalt `get_completed(student_name: string, assignment: int, current_status: string)`.

- **Opprette strukturert data**. Brukere kan ta en tekstblokk eller CSV og bruke LLM til å trekke ut viktig informasjon fra den. For eksempel kan en student konvertere en Wikipedia-artikkel om fredsavtaler til å lage AI-flashkort. Dette kan gjøres ved å bruke en funksjon kalt `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)`.

## Opprette ditt første funksjonskall

Prosessen med å opprette et funksjonskall inkluderer 3 hovedtrinn:

1. **Kalle** Chat Completions API med en liste over dine funksjoner og en brukermelding.
2. **Lese** modellens respons for å utføre en handling, dvs. kjøre en funksjon eller API-forespørsel.
3. **Gjøre** en ny samtale til Chat Completions API med responsen fra funksjonen din for å bruke den informasjonen til å lage et svar til brukeren.

![LLM-flyt](../../../translated_images/LLM-Flow.3285ed8caf4796d7343c02927f52c9d32df59e790f6e440568e2e951f6ffa5fd.no.png)

### Trinn 1 - opprette meldinger

Det første trinnet er å opprette en brukermelding. Dette kan dynamisk tildeles ved å ta verdien av et tekstfelt, eller du kan tildele en verdi her. Hvis dette er første gang du jobber med Chat Completions API, må vi definere `role` og `content` for meldingen.

`Role` kan enten være `system` (opprette regler), `assistant` (modellen) eller `user` (sluttbrukeren). For funksjonskall vil vi tildele dette som `user` og et eksempelspørsmål.

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Ved å tildele forskjellige roller blir det tydelig for LLM om det er systemet som sier noe eller brukeren, noe som hjelper med å bygge en samtalehistorikk som LLM kan bygge videre på.

### Trinn 2 - opprette funksjoner

Deretter vil vi definere en funksjon og parameterne til den funksjonen. Vi vil bruke bare én funksjon her kalt `search_courses`, men du kan opprette flere funksjoner.

> **Viktig**: Funksjoner er inkludert i systemmeldingen til LLM og vil bli inkludert i antall tilgjengelige tokens du har tilgjengelig.

Nedenfor oppretter vi funksjonene som en liste med elementer. Hvert element er en funksjon og har egenskapene `name`, `description` og `parameters`:

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

La oss beskrive hver funksjonsinstans mer detaljert nedenfor:

- `name` - Navnet på funksjonen vi ønsker å kalle.
- `description` - Dette er beskrivelsen av hvordan funksjonen fungerer. Her er det viktig å være spesifikk og tydelig.
- `parameters` - En liste over verdier og format som du ønsker at modellen skal produsere i sitt svar. Parameters-listen består av elementer der elementene har følgende egenskaper:
  1.  `type` - Datatypen egenskapene vil bli lagret i.
  1.  `properties` - Liste over de spesifikke verdiene som modellen vil bruke for sitt svar.
      1. `name` - Nøkkelen er navnet på egenskapen som modellen vil bruke i sitt formaterte svar, for eksempel `product`.
      1. `type` - Datatypen til denne egenskapen, for eksempel `string`.
      1. `description` - Beskrivelse av den spesifikke egenskapen.

Det finnes også en valgfri egenskap `required` - nødvendig egenskap for at funksjonskallet skal fullføres.

### Trinn 3 - Gjøre funksjonskallet

Etter å ha definert en funksjon, må vi nå inkludere den i samtalen til Chat Completion API. Vi gjør dette ved å legge til `functions` i forespørselen. I dette tilfellet `functions=functions`.

Det er også et alternativ å sette `function_call` til `auto`. Dette betyr at vi lar LLM bestemme hvilken funksjon som skal kalles basert på brukermeldingen i stedet for å tildele det selv.

Her er litt kode nedenfor hvor vi kaller `ChatCompletion.create`, merk hvordan vi setter `functions=functions` og `function_call="auto"` og dermed gir LLM valget om når funksjonene vi gir skal kalles:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

Responsen som kommer tilbake ser nå slik ut:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

Her kan vi se hvordan funksjonen `search_courses` ble kalt og med hvilke argumenter, som oppført i `arguments`-egenskapen i JSON-responsen.

Konklusjonen er at LLM var i stand til å finne dataene som passet til argumentene til funksjonen ved å trekke dem ut fra verdien gitt til `messages`-parameteren i samtalekallet. Nedenfor er en påminnelse om verdien til `messages`:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Som du kan se, ble `student`, `Azure` og `beginner` trukket ut fra `messages` og satt som input til funksjonen. Å bruke funksjoner på denne måten er en flott måte å trekke ut informasjon fra en oppfordring, men også å gi struktur til LLM og ha gjenbrukbar funksjonalitet.

Neste steg er å se hvordan vi kan bruke dette i vår app.

## Integrere funksjonskall i en applikasjon

Etter at vi har testet det formaterte svaret fra LLM, kan vi nå integrere dette i en applikasjon.

### Administrere flyten

For å integrere dette i vår applikasjon, la oss ta følgende steg:

1. Først, la oss gjøre samtalen til OpenAI-tjenestene og lagre meldingen i en variabel kalt `response_message`.

   ```python
   response_message = response.choices[0].message
   ```

1. Nå vil vi definere funksjonen som vil kalle Microsoft Learn API for å få en liste over kurs:

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

   Merk hvordan vi nå oppretter en faktisk Python-funksjon som samsvarer med funksjonsnavnene introdusert i `functions`-variabelen. Vi gjør også reelle eksterne API-kall for å hente dataene vi trenger. I dette tilfellet går vi mot Microsoft Learn API for å søke etter opplæringsmoduler.

Ok, så vi opprettet `functions`-variabler og en tilsvarende Python-funksjon, hvordan forteller vi LLM hvordan disse to skal kobles sammen slik at vår Python-funksjon blir kalt?

1. For å se om vi trenger å kalle en Python-funksjon, må vi se inn i LLM-responsen og se om `function_call` er en del av den og kalle den angitte funksjonen. Her er hvordan du kan gjøre den nevnte sjekken nedenfor:

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

   Disse tre linjene sikrer at vi trekker ut funksjonsnavnet, argumentene og gjør kallet:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   Nedenfor er output fra å kjøre koden vår:

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

1. Nå vil vi sende den oppdaterte meldingen, `messages`, til LLM slik at vi kan motta et naturlig språk-svar i stedet for en API JSON-formatert respons.

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

## Oppgave

For å fortsette læringen din om Azure OpenAI Funksjonskall kan du bygge:

- Flere parametere for funksjonen som kan hjelpe lærere med å finne flere kurs.
- Opprette et annet funksjonskall som tar mer informasjon fra læreren, som deres morsmål.
- Opprett feilhåndtering når funksjonskallet og/eller API-kallet ikke returnerer noen passende kurs

Hint: Følg siden [Learn API referansedokumentasjon](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) for å se hvordan og hvor disse dataene er tilgjengelige.

## Flott arbeid! Fortsett reisen

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning-samling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å utvikle din kunnskap om Generativ AI!

Gå videre til Leksjon 12, hvor vi skal se på hvordan man [designer UX for AI-applikasjoner](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.