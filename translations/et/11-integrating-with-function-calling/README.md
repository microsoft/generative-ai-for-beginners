<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77a48a201447be19aa7560706d6f93a0",
  "translation_date": "2025-10-11T11:21:44+00:00",
  "source_file": "11-integrating-with-function-calling/README.md",
  "language_code": "et"
}
-->
# Integreerimine funktsioonikutsumisega

[![Integreerimine funktsioonikutsumisega](../../../translated_images/11-lesson-banner.d78860d3e1f041e2c3426b1c052e1590738d2978db584a08efe1efbca299ed82.et.png)](https://aka.ms/gen-ai-lesson11-gh?WT.mc_id=academic-105485-koreyst)

Eelnevates tundides oled juba päris palju õppinud. Kuid alati on võimalus veelgi paremaks muutuda. Mõned asjad, mida saame parandada, on näiteks see, kuidas saada järjepidevamat vastusevormingut, et vastust oleks lihtsam hiljem kasutada. Samuti võiksime lisada andmeid teistest allikatest, et rikastada oma rakendust veelgi.

Need probleemid ongi selle peatüki fookuses.

## Sissejuhatus

Selles tunnis käsitletakse:

- Mis on funktsioonikutsumine ja selle kasutusjuhtumid.
- Funktsioonikutsumise loomine Azure OpenAI abil.
- Kuidas integreerida funktsioonikutsumist rakendusse.

## Õpieesmärgid

Selle tunni lõpuks oskad:

- Selgitada funktsioonikutsumise eesmärki.
- Seadistada funktsioonikutsumist Azure OpenAI teenuse abil.
- Kujundada tõhusaid funktsioonikutsumisi vastavalt oma rakenduse vajadustele.

## Stsenaarium: Meie vestlusroboti täiustamine funktsioonidega

Selles tunnis soovime luua funktsiooni meie haridusettevõtte jaoks, mis võimaldab kasutajatel vestlusroboti abil leida tehnilisi kursusi. Soovitame kursusi, mis sobivad nende oskuste tasemele, praegusele rollile ja huvipakkuvale tehnoloogiale.

Selle stsenaariumi täitmiseks kasutame kombinatsiooni:

- `Azure OpenAI`, et luua kasutajale vestluskogemus.
- `Microsoft Learn Catalog API`, et aidata kasutajatel leida kursusi vastavalt nende päringule.
- `Funktsioonikutsumine`, et võtta kasutaja päring ja saata see funktsioonile API päringu tegemiseks.

Alustuseks vaatame, miks me üldse tahaksime kasutada funktsioonikutsumist:

## Miks funktsioonikutsumine

Enne funktsioonikutsumist olid LLM-i (suured keelemudelid) vastused struktureerimata ja ebajärjekindlad. Arendajad pidid kirjutama keerulist valideerimiskoodi, et tagada iga vastuse variatsiooni käsitlemine. Kasutajad ei saanud vastuseid nagu "Mis on praegune ilm Stockholmis?". Seda seetõttu, et mudelid olid piiratud ajaga, mil andmed treeniti.

Funktsioonikutsumine on Azure OpenAI teenuse funktsioon, mis aitab ületada järgmisi piiranguid:

- **Järjepidev vastusevorming**. Kui suudame paremini kontrollida vastuse vormingut, saame vastuse hõlpsamini integreerida teistesse süsteemidesse.
- **Välised andmed**. Võimalus kasutada rakenduse teistest allikatest pärit andmeid vestluskontekstis.

## Probleemi illustreerimine stsenaariumi kaudu

> Soovitame kasutada [kaasasolevat märkmikku](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreyst), kui soovite allpool toodud stsenaariumi käivitada. Võite ka lihtsalt lugeda, kuna püüame illustreerida probleemi, kus funktsioonid võivad aidata lahendust leida.

Vaatame näidet, mis illustreerib vastuse vormingu probleemi:

Oletame, et soovime luua andmebaasi õpilaste andmetega, et saaksime neile soovitada sobivaid kursusi. Allpool on kaks õpilaste kirjeldust, mis on väga sarnased nende sisalduvate andmete poolest.

1. Loo ühendus meie Azure OpenAI ressursiga:

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

   Allpool on Python-kood, mis konfigureerib meie ühenduse Azure OpenAI-ga, kus määrame `api_type`, `api_base`, `api_version` ja `api_key`.

1. Loo kaks õpilaste kirjeldust, kasutades muutujaid `student_1_description` ja `student_2_description`.

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   Soovime saata ülaltoodud õpilaste kirjeldused LLM-ile, et andmeid analüüsida. Neid andmeid saab hiljem kasutada meie rakenduses, saata API-le või salvestada andmebaasi.

1. Loome kaks identset viipa, milles juhendame LLM-i, millist teavet me otsime:

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

   Ülaltoodud viipad juhendavad LLM-i teavet välja võtma ja vastust JSON-vormingus tagastama.

1. Pärast viipade ja Azure OpenAI ühenduse seadistamist saadame viipad LLM-ile, kasutades `openai.ChatCompletion`. Salvestame viiba muutujasse `messages` ja määrame rolliks `user`. See jäljendab kasutaja sõnumit, mis kirjutatakse vestlusrobotile.

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

Nüüd saame saata mõlemad päringud LLM-ile ja uurida vastust, mille saame, leides selle näiteks `openai_response1['choices'][0]['message']['content']`.

1. Lõpuks saame vastuse JSON-vormingusse teisendada, kutsudes `json.loads`:

   ```python
   # Loading the response as a JSON object
   json_response1 = json.loads(openai_response1.choices[0].message.content)
   json_response1
   ```

   Vastus 1:

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   Vastus 2:

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   Kuigi viipad on samad ja kirjeldused sarnased, näeme, et `Grades` omaduse väärtused on vormindatud erinevalt, näiteks `3.7` või `3.7 GPA`.

   See tulemus on tingitud sellest, et LLM võtab struktureerimata andmeid kirjaliku viiba kujul ja tagastab samuti struktureerimata andmeid. Meil on vaja struktureeritud vormingut, et teaksime, mida oodata andmete salvestamisel või kasutamisel.

Kuidas siis lahendada vormindamise probleemi? Funktsioonikutsumise abil saame tagada, et saame tagasi struktureeritud andmeid. Funktsioonikutsumist kasutades LLM tegelikult ei kutsu ega käivita ühtegi funktsiooni. Selle asemel loome LLM-ile struktuuri, mida vastustes järgida. Seejärel kasutame neid struktureeritud vastuseid, et teada, millist funktsiooni oma rakendustes käivitada.

![funktsiooni voog](../../../translated_images/Function-Flow.083875364af4f4bb69bd6f6ed94096a836453183a71cf22388f50310ad6404de.et.png)

Seejärel saame funktsioonist tagastatud andmed saata tagasi LLM-ile. LLM vastab seejärel loomulikus keeles, et vastata kasutaja päringule.

## Funktsioonikutsumise kasutusjuhtumid

Funktsioonikutsumine võib parandada teie rakendust mitmel viisil, näiteks:

- **Väliste tööriistade kutsumine**. Vestlusrobotid on suurepärased vastuste pakkumiseks kasutajate küsimustele. Funktsioonikutsumise abil saavad vestlusrobotid kasutada kasutajate sõnumeid teatud ülesannete täitmiseks. Näiteks võib õpilane paluda vestlusrobotil "Saada minu juhendajale e-kiri, et mul on vaja selle teemaga rohkem abi". See võib teha funktsioonikutsumise `send_email(to: string, body: string)`.

- **API või andmebaasi päringute loomine**. Kasutajad saavad leida teavet loomuliku keele abil, mis muudetakse vormindatud päringuks või API päringuks. Näiteks võib õpetaja küsida "Kes on õpilased, kes lõpetasid viimase ülesande", mis võib kutsuda funktsiooni nimega `get_completed(student_name: string, assignment: int, current_status: string)`.

- **Struktureeritud andmete loomine**. Kasutajad saavad võtta tekstiploki või CSV ja kasutada LLM-i, et sellest olulist teavet välja võtta. Näiteks võib õpilane teisendada Wikipedia artikli rahulepingutest AI mälukaartide loomiseks. Seda saab teha funktsiooni abil `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)`.

## Esimese funktsioonikutsumise loomine

Funktsioonikutsumise loomise protsess hõlmab kolme peamist sammu:

1. **Kutsumine** Chat Completions API-le koos funktsioonide loendi ja kasutaja sõnumiga.
2. **Lugemine** mudeli vastusest, et teha toiming, näiteks käivitada funktsioon või API päring.
3. **Teine** Chat Completions API kõne funktsiooni vastusega, et kasutada seda teavet kasutajale vastuse loomiseks.

![LLM voog](../../../translated_images/LLM-Flow.3285ed8caf4796d7343c02927f52c9d32df59e790f6e440568e2e951f6ffa5fd.et.png)

### Samm 1 - sõnumite loomine

Esimene samm on luua kasutaja sõnum. Selle saab dünaamiliselt määrata, võttes tekstisisendi väärtuse, või määrata väärtuse siin. Kui see on teie esimene kord töötada Chat Completions API-ga, peame määratlema sõnumi `role` ja `content`.

`Role` võib olla kas `system` (reeglite loomine), `assistant` (mudel) või `user` (lõppkasutaja). Funktsioonikutsumise jaoks määrame selle `user` ja näidisena küsimuse.

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Rollide määramisega tehakse LLM-ile selgeks, kas midagi ütleb süsteem või kasutaja, mis aitab luua vestluse ajalugu, millele LLM saab tugineda.

### Samm 2 - funktsioonide loomine

Järgmisena määratleme funktsiooni ja selle parameetrid. Kasutame siin ainult ühte funktsiooni nimega `search_courses`, kuid võite luua mitu funktsiooni.

> **Oluline**: Funktsioonid lisatakse LLM-i süsteemisõnumisse ja need arvestatakse teie saadaolevate tokenite hulka.

Allpool loome funktsioonid elementide massiivina. Iga element on funktsioon ja sellel on omadused `name`, `description` ja `parameters`:

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

Selgitame iga funktsiooni eksemplari üksikasjalikumalt allpool:

- `name` - Funktsiooni nimi, mida soovime kutsuda.
- `description` - Funktsiooni töö kirjeldus. Siin on oluline olla konkreetne ja selge.
- `parameters` - Väärtuste ja vormingu loend, mida soovite mudelil vastuses kasutada. Parameetrite massiiv koosneb elementidest, millel on järgmised omadused:
  1.  `type` - Omaduste andmetüüp, kuhu need salvestatakse.
  1.  `properties` - Spetsiifiliste väärtuste loend, mida mudel vastuses kasutab.
      1. `name` - Võti, mis on omaduse nimi, mida mudel kasutab vormindatud vastuses, näiteks `product`.
      1. `type` - Selle omaduse andmetüüp, näiteks `string`.
      1. `description` - Konkreetse omaduse kirjeldus.

Samuti on olemas valikuline omadus `required` - nõutav omadus funktsioonikutsumise lõpuleviimiseks.

### Samm 3 - Funktsioonikutsumise tegemine

Pärast funktsiooni määratlemist peame selle nüüd lisama Chat Completion API kõnesse. Teeme seda, lisades `functions` päringusse. Sel juhul `functions=functions`.

Samuti on võimalus määrata `function_call` väärtuseks `auto`. See tähendab, et laseme LLM-il otsustada, millist funktsiooni peaks kutsuma kasutaja sõnumi põhjal, selle asemel et ise määrata.

Allpool on kood, kus kutsume `ChatCompletion.create`, märkige, kuidas määrame `functions=functions` ja `function_call="auto"` ning anname seega LLM-ile valiku, millal kutsuda pakutud funktsioone:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

Tagastatud vastus näeb nüüd välja selline:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

Siin näeme, kuidas funktsiooni `search_courses` kutsuti ja milliste argumentidega, nagu on loetletud JSON-vastuse `arguments` omaduses.

LLM suutis leida andmed, mis sobivad funktsiooni argumentidega, kuna ta eraldas need väärtusest, mis anti `messages` parameetrile vestluse lõpetamise kõnes. Allpool on meeldetuletus `messages` väärtusest:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Nagu näete, eraldati `student`, `Azure` ja `beginner` `messages` väärtusest ja määrati funktsiooni sisendiks. Funktsioonide kasutamine sel viisil on suurepärane viis teabe eraldamiseks viibast, aga ka LLM-ile struktuuri pakkumiseks ja korduvkasutatava funktsionaalsuse loomiseks.

Järgmisena peame nägema, kuidas seda oma rakenduses kasutada.

## Funktsioonikutsumiste integreerimine rakendusse

Pärast LLM-i vormindatud vastuse testimist saame selle nüüd integreerida rakendusse.

### Voo haldamine

Selle rakendusse integreerimiseks teeme järgmised sammud:

1. Kõigepealt teeme kõne OpenAI teenustele ja salvestame sõnumi muutujasse `response_message`.

   ```python
   response_message = response.choices[0].message
   ```

1. Nüüd määratleme funktsiooni, mis kutsub Microsoft Learn API-d, et saada kursuste loend:

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

   Pange tähele, kuidas me nüüd loome tegeliku Python-funktsiooni, mis vastab `functions` muutujas tutvustatud funktsiooninimedele. Samuti teeme reaalseid väliseid API-kõnesid, et hankida vajalikke andmeid. Sel juhul pöördume Microsoft Learn API poole, et otsida koolitusmoduleid.

Ok, nii et me lõime `functions` muutujad ja vastava Python-funktsiooni, kuidas me ütleme LLM-ile, kuidas neid kahte omavahel siduda, et meie Python-funktsiooni kutsutaks?

1. Et näha, kas peame Python-funktsiooni kutsuma, peame vaatama LLM-i vastust ja kontrollima, kas `function_call` on osa sellest, ning kutsuma välja toodud funktsiooni. Allpool on näidatud, kuidas seda kontrolli teha:

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

   Need kolm rida tagavad, et eraldame funktsiooni nime, argumendid ja teeme kõne:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   Allpool on meie koodi käivitamise tulemus:

   **Väljund**

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

1. Nüüd saadame uuendatud sõnumi, `messages`, LLM-ile, et saada loomuliku keele vastus API JSON-vormingus vastuse asemel.

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

   **Väljund**

   ```python
   {
     "role": "assistant",
     "content": "I found some good courses for beginner students to learn Azure:\n\n1. [Describe concepts of cryptography] (https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n5. [Set up the Rust development environment](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\nYou can click on the links to access the courses."
   }

   ```

## Ülesanne

Azure OpenAI funktsioonikutsumise õppimise jätkamiseks saate luua:

- Rohkem funktsiooni parameetreid, mis aitavad õppijatel leida rohkem kursusi.
- Luua teise funktsioonikutsumise, mis võtab õppijalt rohkem teavet, näiteks tema emakeele.
- Loo veakäsitlus juhuks, kui funktsiooni või API päring ei tagasta sobivaid kursusi.

Vihje: Vaata [Learn API viitedokumentatsiooni](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) lehte, et näha, kuidas ja kus need andmed on saadaval.

## Suurepärane töö! Jätka teekonda

Pärast selle õppetunni lõpetamist tutvu meie [Generatiivse AI õppekollektsiooniga](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma Generatiivse AI teadmiste arendamist!

Liigu edasi 12. õppetundi, kus vaatame, kuidas [kujundada UX AI rakenduste jaoks](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.