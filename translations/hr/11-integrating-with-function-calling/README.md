<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f6f84f9ef2d066cd25850cab93580a50",
  "translation_date": "2025-10-18T01:30:07+00:00",
  "source_file": "11-integrating-with-function-calling/README.md",
  "language_code": "hr"
}
-->
# Integracija s pozivanjem funkcija

[![Integracija s pozivanjem funkcija](../../../translated_images/11-lesson-banner.d78860d3e1f041e2c3426b1c052e1590738d2978db584a08efe1efbca299ed82.hr.png)](https://youtu.be/DgUdCLX8qYQ?si=f1ouQU5HQx6F8Gl2)

Do sada ste naučili dosta toga u prethodnim lekcijama. Međutim, uvijek postoji prostor za poboljšanje. Neke od stvari koje možemo unaprijediti uključuju dobivanje dosljednijeg formata odgovora kako bi rad s odgovorima bio lakši u daljnjem procesu. Također, možda želimo dodati podatke iz drugih izvora kako bismo dodatno obogatili našu aplikaciju.

Ova lekcija bavi se upravo tim problemima.

## Uvod

Ova lekcija obuhvaća:

- Objašnjenje što je pozivanje funkcija i njegove primjene.
- Kreiranje poziva funkcije pomoću Azure OpenAI.
- Kako integrirati poziv funkcije u aplikaciju.

## Ciljevi učenja

Na kraju ove lekcije moći ćete:

- Objasniti svrhu korištenja pozivanja funkcija.
- Postaviti poziv funkcije koristeći Azure OpenAI Service.
- Dizajnirati učinkovite pozive funkcija za potrebe vaše aplikacije.

## Scenarij: Poboljšanje našeg chatbota pomoću funkcija

Za ovu lekciju želimo izraditi značajku za naš startup u obrazovanju koja omogućuje korisnicima da koriste chatbot za pronalaženje tehničkih tečajeva. Preporučit ćemo tečajeve koji odgovaraju njihovoj razini vještina, trenutnoj ulozi i interesima u tehnologiji.

Za dovršetak ovog scenarija koristit ćemo kombinaciju:

- `Azure OpenAI` za kreiranje chat iskustva za korisnika.
- `Microsoft Learn Catalog API` za pomoć korisnicima u pronalaženju tečajeva na temelju njihovih zahtjeva.
- `Pozivanje funkcija` za uzimanje korisničkog upita i slanje funkciji za izvršenje API zahtjeva.

Za početak, pogledajmo zašto bismo uopće koristili pozivanje funkcija:

## Zašto pozivanje funkcija

Prije pozivanja funkcija, odgovori od LLM-a bili su nestrukturirani i nedosljedni. Programeri su morali pisati složeni kod za validaciju kako bi osigurali da mogu obraditi svaku varijaciju odgovora. Korisnici nisu mogli dobiti odgovore poput "Kakvo je trenutno vrijeme u Stockholmu?". To je zato što su modeli bili ograničeni na podatke na kojima su trenirani.

Pozivanje funkcija je značajka Azure OpenAI Service koja prevladava sljedeća ograničenja:

- **Dosljedan format odgovora**. Ako možemo bolje kontrolirati format odgovora, lakše ćemo ga integrirati u druge sustave.
- **Vanjski podaci**. Mogućnost korištenja podataka iz drugih izvora aplikacije u kontekstu razgovora.

## Ilustracija problema kroz scenarij

> Preporučujemo da koristite [priloženu bilježnicu](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) ako želite pokrenuti dolje navedeni scenarij. Također možete samo čitati dalje jer pokušavamo ilustrirati problem gdje funkcije mogu pomoći u njegovom rješavanju.

Pogledajmo primjer koji ilustrira problem formata odgovora:

Recimo da želimo stvoriti bazu podataka o studentima kako bismo im mogli predložiti odgovarajući tečaj. Ispod imamo dva opisa studenata koji su vrlo slični u podacima koje sadrže.

1. Kreirajte vezu s našim Azure OpenAI resursom:

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

   Ispod je Python kod za konfiguriranje naše veze s Azure OpenAI gdje postavljamo `api_type`, `api_base`, `api_version` i `api_key`.

1. Kreiranje dva opisa studenata koristeći varijable `student_1_description` i `student_2_description`.

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   Želimo poslati gore navedene opise studenata LLM-u za parsiranje podataka. Ti podaci kasnije se mogu koristiti u našoj aplikaciji i slati API-ju ili pohranjivati u bazu podataka.

1. Kreirajmo dva identična upita u kojima instruiramo LLM o informacijama koje nas zanimaju:

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

   Gore navedeni upiti instruiraju LLM da izvuče informacije i vrati odgovor u JSON formatu.

1. Nakon postavljanja upita i veze s Azure OpenAI, sada ćemo poslati upite LLM-u koristeći `openai.ChatCompletion`. Pohranjujemo upit u varijablu `messages` i dodjeljujemo ulogu `user`. Ovo simulira poruku korisnika napisanu chatbotu.

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

Sada možemo poslati oba zahtjeva LLM-u i pregledati odgovor koji primimo pronalazeći ga ovako `openai_response1['choices'][0]['message']['content']`.

1. Na kraju, možemo pretvoriti odgovor u JSON format pozivom `json.loads`:

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

   Iako su upiti isti i opisi slični, vidimo da su vrijednosti svojstva `Grades` formatirane različito, jer ponekad dobijemo format `3.7` ili `3.7 GPA`, na primjer.

   Ovaj rezultat je posljedica toga što LLM uzima nestrukturirane podatke u obliku pisanog upita i također vraća nestrukturirane podatke. Potrebno nam je strukturirani format kako bismo znali što očekivati prilikom pohrane ili korištenja tih podataka.

Kako onda riješiti problem formatiranja? Korištenjem pozivanja funkcija možemo osigurati da dobijemo strukturirane podatke natrag. Kod korištenja pozivanja funkcija, LLM zapravo ne poziva ili izvršava funkcije. Umjesto toga, kreiramo strukturu koju LLM treba slijediti za svoje odgovore. Zatim koristimo te strukturirane odgovore kako bismo znali koju funkciju pokrenuti u našim aplikacijama.

![tok funkcije](../../../translated_images/Function-Flow.083875364af4f4bb69bd6f6ed94096a836453183a71cf22388f50310ad6404de.hr.png)

Možemo zatim uzeti ono što je vraćeno iz funkcije i poslati to natrag LLM-u. LLM će zatim odgovoriti koristeći prirodni jezik kako bi odgovorio na korisnički upit.

## Primjene pozivanja funkcija

Postoji mnogo različitih primjena gdje pozivanje funkcija može poboljšati vašu aplikaciju, poput:

- **Pozivanje vanjskih alata**. Chatbotovi su izvrsni u pružanju odgovora na pitanja korisnika. Korištenjem pozivanja funkcija, chatbotovi mogu koristiti poruke korisnika za izvršavanje određenih zadataka. Na primjer, student može zatražiti od chatbota: "Pošalji e-mail mom instruktoru da mi treba više pomoći s ovom temom". Ovo može pokrenuti poziv funkcije `send_email(to: string, body: string)`.

- **Kreiranje API ili upita za bazu podataka**. Korisnici mogu pronaći informacije koristeći prirodni jezik koji se pretvara u formatirani upit ili API zahtjev. Primjer ovoga može biti učitelj koji traži: "Tko su studenti koji su završili posljednji zadatak", što može pozvati funkciju nazvanu `get_completed(student_name: string, assignment: int, current_status: string)`.

- **Kreiranje strukturiranih podataka**. Korisnici mogu uzeti blok teksta ili CSV i koristiti LLM za izdvajanje važnih informacija iz njega. Na primjer, student može pretvoriti Wikipedia članak o mirovnim sporazumima kako bi stvorio AI kartice za učenje. Ovo se može učiniti korištenjem funkcije nazvane `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)`.

## Kreiranje vašeg prvog poziva funkcije

Proces kreiranja poziva funkcije uključuje 3 glavna koraka:

1. **Pozivanje** Chat Completions API-ja s popisom vaših funkcija i korisničkom porukom.
2. **Čitanje** odgovora modela za izvršenje akcije, tj. pokretanje funkcije ili API poziva.
3. **Ponovno pozivanje** Chat Completions API-ja s odgovorom vaše funkcije kako bi se taj odgovor iskoristio za kreiranje odgovora korisniku.

![LLM tok](../../../translated_images/LLM-Flow.3285ed8caf4796d7343c02927f52c9d32df59e790f6e440568e2e951f6ffa5fd.hr.png)

### Korak 1 - kreiranje poruka

Prvi korak je kreiranje korisničke poruke. Ovo se može dinamički dodijeliti uzimanjem vrijednosti tekstualnog unosa ili možete ovdje dodijeliti vrijednost. Ako prvi put radite s Chat Completions API-jem, trebamo definirati `role` i `content` poruke.

`Role` može biti `system` (kreiranje pravila), `assistant` (model) ili `user` (krajnji korisnik). Za pozivanje funkcija, dodijelit ćemo ovo kao `user` i primjer pitanja.

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Dodjeljivanjem različitih uloga, jasno je LLM-u je li sustav nešto rekao ili korisnik, što pomaže u izgradnji povijesti razgovora na kojoj LLM može graditi.

### Korak 2 - kreiranje funkcija

Sljedeće, definirat ćemo funkciju i parametre te funkcije. Koristit ćemo samo jednu funkciju ovdje nazvanu `search_courses`, ali možete kreirati više funkcija.

> **Važno**: Funkcije su uključene u sistemsku poruku LLM-u i bit će uključene u broj dostupnih tokena koje imate na raspolaganju.

Ispod kreiramo funkcije kao niz stavki. Svaka stavka je funkcija i ima svojstva `name`, `description` i `parameters`:

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

Pojasnimo svaku instancu funkcije detaljnije:

- `name` - Naziv funkcije koju želimo da se pozove.
- `description` - Ovo je opis kako funkcija radi. Ovdje je važno biti specifičan i jasan.
- `parameters` - Popis vrijednosti i formata koje želimo da model proizvede u svom odgovoru. Niz parametara sastoji se od stavki gdje stavke imaju sljedeća svojstva:
  1.  `type` - Tip podataka u kojem će svojstva biti pohranjena.
  1.  `properties` - Popis specifičnih vrijednosti koje će model koristiti za svoj odgovor.
      1. `name` - Ključ je naziv svojstva koje će model koristiti u svom formatiranom odgovoru, na primjer, `product`.
      1. `type` - Tip podataka ovog svojstva, na primjer, `string`.
      1. `description` - Opis specifičnog svojstva.

Postoji i opcionalno svojstvo `required` - obavezno svojstvo za dovršetak poziva funkcije.

### Korak 3 - Izvršenje poziva funkcije

Nakon definiranja funkcije, sada je trebamo uključiti u poziv Chat Completion API-ju. To radimo dodavanjem `functions` zahtjevu. U ovom slučaju `functions=functions`.

Postoji i opcija za postavljanje `function_call` na `auto`. To znači da ćemo dopustiti LLM-u da odluči koju funkciju treba pozvati na temelju korisničke poruke, umjesto da je sami dodjeljujemo.

Ispod je kod gdje pozivamo `ChatCompletion.create`, obratite pažnju kako postavljamo `functions=functions` i `function_call="auto"` te time dajemo LLM-u izbor kada pozvati funkcije koje mu pružamo:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

Odgovor koji dolazi sada izgleda ovako:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

Ovdje možemo vidjeti kako je funkcija `search_courses` pozvana i s kojim argumentima, kao što je navedeno u svojstvu `arguments` u JSON odgovoru.

Zaključak je da je LLM bio u mogućnosti pronaći podatke koji odgovaraju argumentima funkcije jer ih je izvukao iz vrijednosti pružene parametru `messages` u pozivu za završetak razgovora. Ispod je podsjetnik na vrijednost `messages`:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Kao što možete vidjeti, `student`, `Azure` i `beginner` su izvučeni iz `messages` i postavljeni kao ulaz funkciji. Korištenje funkcija na ovaj način je odličan način za izdvajanje informacija iz upita, ali i za pružanje strukture LLM-u i stvaranje funkcionalnosti koja se može ponovno koristiti.

Sljedeće, trebamo vidjeti kako to možemo koristiti u našoj aplikaciji.

## Integracija poziva funkcija u aplikaciju

Nakon što smo testirali formatirani odgovor od LLM-a, sada možemo integrirati ovo u aplikaciju.

### Upravljanje tokom

Za integraciju u našu aplikaciju, slijedimo sljedeće korake:

1. Prvo, napravimo poziv OpenAI uslugama i pohranimo poruku u varijablu nazvanu `response_message`.

   ```python
   response_message = response.choices[0].message
   ```

1. Sada ćemo definirati funkciju koja će pozvati Microsoft Learn API za dobivanje popisa tečajeva:

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

   Obratite pažnju kako sada kreiramo stvarnu Python funkciju koja se mapira na nazive funkcija uvedene u varijabli `functions`. Također, radimo stvarne vanjske API pozive kako bismo dohvatili potrebne podatke. U ovom slučaju, koristimo Microsoft Learn API za pretraživanje modula za obuku.

Ok, kreirali smo varijable `functions` i odgovarajuću Python funkciju, kako kažemo LLM-u kako ih međusobno povezati tako da se naša Python funkcija pozove?

1. Da bismo vidjeli trebamo li pozvati Python funkciju, trebamo pogledati odgovor LLM-a i vidjeti je li `function_call` dio njega te pozvati navedenu funkciju. Evo kako možete napraviti navedenu provjeru:

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

   Ove tri linije osiguravaju da izdvojimo naziv funkcije, argumente i izvršimo poziv:

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

1. Sada ćemo poslati ažuriranu poruku, `messages`, LLM-u kako bismo dobili odgovor u prirodnom jeziku umjesto API JSON formatiranog odgovora.

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

Za nastavak vašeg učenja o Azure OpenAI Function Calling možete izraditi:

- Više parametara funkcije koji bi mogli pomoći učenicima da pronađu više tečajeva.
- Kreirati drugi poziv funkcije koji uzima više informacija od učenika, poput njihovog materinjeg jezika.
- Kreirajte rukovanje pogreškama kada poziv funkcije i/ili API poziv ne vrati odgovarajuće tečajeve

Savjet: Pogledajte stranicu [Learn API referentna dokumentacija](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) kako biste vidjeli kako i gdje su ti podaci dostupni.

## Sjajan posao! Nastavite putovanje

Nakon završetka ove lekcije, pogledajte našu [Generative AI Learning kolekciju](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o generativnoj umjetnoj inteligenciji!

Prijeđite na Lekciju 12, gdje ćemo istražiti kako [dizajnirati UX za AI aplikacije](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.