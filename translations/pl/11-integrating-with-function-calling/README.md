<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f6f84f9ef2d066cd25850cab93580a50",
  "translation_date": "2025-10-18T00:51:32+00:00",
  "source_file": "11-integrating-with-function-calling/README.md",
  "language_code": "pl"
}
-->
# Integracja z wywoływaniem funkcji

[![Integracja z wywoływaniem funkcji](../../../translated_images/11-lesson-banner.d78860d3e1f041e2c3426b1c052e1590738d2978db584a08efe1efbca299ed82.pl.png)](https://youtu.be/DgUdCLX8qYQ?si=f1ouQU5HQx6F8Gl2)

W poprzednich lekcjach nauczyłeś się już całkiem sporo. Jednak zawsze można coś poprawić. Możemy na przykład zadbać o bardziej spójny format odpowiedzi, aby ułatwić pracę z odpowiedzią w dalszych etapach. Możemy również dodać dane z innych źródeł, aby wzbogacić naszą aplikację.

Właśnie te problemy są tematem tego rozdziału.

## Wprowadzenie

W tej lekcji omówimy:

- Wyjaśnienie, czym jest wywoływanie funkcji i jakie ma zastosowania.
- Tworzenie wywołania funkcji za pomocą Azure OpenAI.
- Jak zintegrować wywołanie funkcji z aplikacją.

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Wyjaśnić cel korzystania z wywoływania funkcji.
- Skonfigurować wywołanie funkcji za pomocą usługi Azure OpenAI.
- Zaprojektować efektywne wywołania funkcji dla potrzeb swojej aplikacji.

## Scenariusz: Ulepszanie naszego chatbota za pomocą funkcji

W tej lekcji chcemy stworzyć funkcję dla naszego startupu edukacyjnego, która pozwoli użytkownikom korzystać z chatbota do wyszukiwania kursów technicznych. Będziemy rekomendować kursy, które pasują do ich poziomu umiejętności, obecnej roli i zainteresowań technologicznych.

Aby zrealizować ten scenariusz, użyjemy kombinacji:

- `Azure OpenAI`, aby stworzyć doświadczenie czatu dla użytkownika.
- `Microsoft Learn Catalog API`, aby pomóc użytkownikom znaleźć kursy na podstawie ich zapytań.
- `Wywoływanie funkcji`, aby przekształcić zapytanie użytkownika w wywołanie funkcji, które wykona żądanie do API.

Na początek przyjrzyjmy się, dlaczego w ogóle warto korzystać z wywoływania funkcji:

## Dlaczego wywoływanie funkcji

Przed wprowadzeniem wywoływania funkcji odpowiedzi z LLM były nieustrukturyzowane i niespójne. Programiści musieli pisać skomplikowany kod walidacyjny, aby obsłużyć różne warianty odpowiedzi. Użytkownicy nie mogli uzyskać odpowiedzi na pytania typu „Jaka jest obecnie pogoda w Sztokholmie?”. Wynikało to z ograniczeń modeli, które bazowały na danych, na których były trenowane.

Wywoływanie funkcji to funkcja usługi Azure OpenAI, która pozwala przezwyciężyć następujące ograniczenia:

- **Spójny format odpowiedzi**. Jeśli możemy lepiej kontrolować format odpowiedzi, łatwiej będzie nam zintegrować ją z innymi systemami.
- **Dane zewnętrzne**. Możliwość korzystania z danych z innych źródeł aplikacji w kontekście czatu.

## Ilustracja problemu na przykładzie scenariusza

> Zalecamy skorzystanie z [dołączonego notebooka](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreyst), jeśli chcesz uruchomić poniższy scenariusz. Możesz również po prostu przeczytać, ponieważ staramy się zilustrować problem, w którym funkcje mogą pomóc w jego rozwiązaniu.

Przyjrzyjmy się przykładowi, który ilustruje problem z formatem odpowiedzi:

Załóżmy, że chcemy stworzyć bazę danych danych studentów, aby móc sugerować im odpowiednie kursy. Poniżej mamy dwa opisy studentów, które są bardzo podobne pod względem zawartych danych.

1. Utwórz połączenie z naszym zasobem Azure OpenAI:

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

   Poniżej znajduje się kod w Pythonie do skonfigurowania naszego połączenia z Azure OpenAI, gdzie ustawiamy `api_type`, `api_base`, `api_version` i `api_key`.

1. Utwórz dwa opisy studentów, korzystając z zmiennych `student_1_description` i `student_2_description`.

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   Chcemy wysłać powyższe opisy studentów do LLM, aby przeanalizować dane. Te dane mogą być później użyte w naszej aplikacji, wysłane do API lub zapisane w bazie danych.

1. Utwórz dwa identyczne polecenia, w których instruujemy LLM, jakie informacje nas interesują:

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

   Powyższe polecenia instruują LLM, aby wyodrębnił informacje i zwrócił odpowiedź w formacie JSON.

1. Po skonfigurowaniu poleceń i połączenia z Azure OpenAI, wyślemy teraz polecenia do LLM, używając `openai.ChatCompletion`. Przechowujemy polecenie w zmiennej `messages` i przypisujemy rolę `user`. Ma to na celu symulację wiadomości od użytkownika napisanej do chatbota.

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

Teraz możemy wysłać oba żądania do LLM i zbadać otrzymaną odpowiedź, znajdując ją w `openai_response1['choices'][0]['message']['content']`.

1. Na koniec możemy przekonwertować odpowiedź na format JSON, wywołując `json.loads`:

   ```python
   # Loading the response as a JSON object
   json_response1 = json.loads(openai_response1.choices[0].message.content)
   json_response1
   ```

   Odpowiedź 1:

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   Odpowiedź 2:

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   Mimo że polecenia są takie same, a opisy podobne, widzimy, że wartości właściwości `Grades` są sformatowane inaczej, np. w formacie `3.7` lub `3.7 GPA`.

   Wynik ten wynika z faktu, że LLM przyjmuje nieustrukturyzowane dane w formie napisanego polecenia i zwraca również dane nieustrukturyzowane. Potrzebujemy mieć ustrukturyzowany format, aby wiedzieć, czego się spodziewać podczas przechowywania lub używania tych danych.

Jak więc rozwiązać problem formatowania? Korzystając z wywoływania funkcji, możemy upewnić się, że otrzymujemy dane ustrukturyzowane. Podczas korzystania z wywoływania funkcji LLM faktycznie nie wywołuje ani nie uruchamia żadnych funkcji. Zamiast tego tworzymy strukturę, której LLM ma przestrzegać w swoich odpowiedziach. Następnie używamy tych ustrukturyzowanych odpowiedzi, aby wiedzieć, jaką funkcję uruchomić w naszych aplikacjach.

![przepływ funkcji](../../../translated_images/Function-Flow.083875364af4f4bb69bd6f6ed94096a836453183a71cf22388f50310ad6404de.pl.png)

Możemy następnie wziąć to, co zwróci funkcja, i przesłać to z powrotem do LLM. LLM odpowie wtedy w języku naturalnym, aby odpowiedzieć na zapytanie użytkownika.

## Przykłady zastosowań wywoływania funkcji

Istnieje wiele różnych zastosowań, w których wywoływanie funkcji może poprawić działanie Twojej aplikacji, takich jak:

- **Wywoływanie narzędzi zewnętrznych**. Chatboty świetnie nadają się do udzielania odpowiedzi na pytania użytkowników. Korzystając z wywoływania funkcji, chatboty mogą używać wiadomości od użytkowników do wykonywania określonych zadań. Na przykład student może poprosić chatbota: „Wyślij e-mail do mojego wykładowcy z informacją, że potrzebuję więcej pomocy w tym temacie”. Może to wywołać funkcję `send_email(to: string, body: string)`.

- **Tworzenie zapytań do API lub bazy danych**. Użytkownicy mogą znaleźć informacje, korzystając z języka naturalnego, który zostanie przekształcony w sformatowane zapytanie lub żądanie API. Przykładem może być nauczyciel, który pyta: „Którzy studenci ukończyli ostatnie zadanie?”, co może wywołać funkcję `get_completed(student_name: string, assignment: int, current_status: string)`.

- **Tworzenie danych ustrukturyzowanych**. Użytkownicy mogą wziąć blok tekstu lub plik CSV i użyć LLM do wyodrębnienia z niego ważnych informacji. Na przykład student może przekształcić artykuł z Wikipedii o porozumieniach pokojowych w AI fiszki. Można to zrobić za pomocą funkcji `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)`.

## Tworzenie pierwszego wywołania funkcji

Proces tworzenia wywołania funkcji obejmuje 3 główne kroki:

1. **Wywołanie** API Chat Completions z listą funkcji i wiadomością użytkownika.
2. **Odczytanie** odpowiedzi modelu w celu wykonania akcji, np. wywołania funkcji lub żądania API.
3. **Wykonanie** kolejnego wywołania API Chat Completions z odpowiedzią z funkcji, aby wykorzystać te informacje do stworzenia odpowiedzi dla użytkownika.

![Przepływ LLM](../../../translated_images/LLM-Flow.3285ed8caf4796d7343c02927f52c9d32df59e790f6e440568e2e951f6ffa5fd.pl.png)

### Krok 1 - tworzenie wiadomości

Pierwszym krokiem jest stworzenie wiadomości użytkownika. Może być ona dynamicznie przypisana na podstawie wartości z pola tekstowego lub przypisana tutaj. Jeśli po raz pierwszy pracujesz z API Chat Completions, musimy zdefiniować `role` i `content` wiadomości.

`Role` może być `system` (tworzenie reguł), `assistant` (model) lub `user` (użytkownik końcowy). W przypadku wywoływania funkcji przypiszemy rolę jako `user` i podamy przykładowe pytanie.

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Przypisując różne role, LLM może rozróżnić, czy coś mówi system, czy użytkownik, co pomaga budować historię rozmowy, na której LLM może się opierać.

### Krok 2 - tworzenie funkcji

Następnie zdefiniujemy funkcję i jej parametry. Użyjemy tutaj tylko jednej funkcji o nazwie `search_courses`, ale możesz stworzyć wiele funkcji.

> **Ważne**: Funkcje są uwzględniane w wiadomości systemowej dla LLM i będą wliczane w dostępne tokeny.

Poniżej tworzymy funkcje jako tablicę elementów. Każdy element to funkcja i ma właściwości `name`, `description` i `parameters`:

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

Omówmy bardziej szczegółowo każdą instancję funkcji:

- `name` - Nazwa funkcji, którą chcemy wywołać.
- `description` - Opis działania funkcji. Ważne jest, aby był konkretny i jasny.
- `parameters` - Lista wartości i format, który model ma wygenerować w swojej odpowiedzi. Tablica parametrów składa się z elementów, gdzie elementy mają następujące właściwości:
  1.  `type` - Typ danych, w którym będą przechowywane właściwości.
  1.  `properties` - Lista konkretnych wartości, które model wykorzysta w swojej odpowiedzi.
      1. `name` - Klucz to nazwa właściwości, którą model wykorzysta w swojej sformatowanej odpowiedzi, np. `product`.
      1. `type` - Typ danych tej właściwości, np. `string`.
      1. `description` - Opis konkretnej właściwości.

Istnieje również opcjonalna właściwość `required` - wymagana właściwość, aby wywołanie funkcji zostało zakończone.

### Krok 3 - Wywołanie funkcji

Po zdefiniowaniu funkcji musimy teraz uwzględnić ją w wywołaniu API Chat Completion. Robimy to, dodając `functions` do żądania. W tym przypadku `functions=functions`.

Istnieje również opcja ustawienia `function_call` na `auto`. Oznacza to, że pozwolimy LLM zdecydować, która funkcja powinna zostać wywołana na podstawie wiadomości użytkownika, zamiast przypisywać ją samodzielnie.

Poniżej znajduje się kod, w którym wywołujemy `ChatCompletion.create`, zwróć uwagę, jak ustawiamy `functions=functions` i `function_call="auto"`, dając tym samym LLM możliwość wyboru, kiedy wywołać dostarczone funkcje:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

Odpowiedź zwrotna wygląda teraz tak:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

Tutaj widzimy, jak funkcja `search_courses` została wywołana i z jakimi argumentami, jak pokazano w właściwości `arguments` w odpowiedzi JSON.

Wniosek: LLM był w stanie znaleźć dane pasujące do argumentów funkcji, wyodrębniając je z wartości podanej do parametru `messages` w wywołaniu chat completion. Poniżej przypomnienie wartości `messages`:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Jak widać, `student`, `Azure` i `beginner` zostały wyodrębnione z `messages` i ustawione jako dane wejściowe dla funkcji. Korzystanie z funkcji w ten sposób to świetny sposób na wyodrębnianie informacji z polecenia, a także na dostarczanie struktury LLM i posiadanie funkcjonalności wielokrotnego użytku.

Teraz musimy zobaczyć, jak możemy to wykorzystać w naszej aplikacji.

## Integracja wywołań funkcji z aplikacją

Po przetestowaniu sformatowanej odpowiedzi z LLM możemy teraz zintegrować ją z aplikacją.

### Zarządzanie przepływem

Aby zintegrować to z naszą aplikacją, wykonajmy następujące kroki:

1. Najpierw wykonajmy wywołanie do usług OpenAI i zapiszmy wiadomość w zmiennej `response_message`.

   ```python
   response_message = response.choices[0].message
   ```

1. Teraz zdefiniujemy funkcję, która wywoła Microsoft Learn API, aby uzyskać listę kursów:

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

   Zwróć uwagę, jak teraz tworzymy rzeczywistą funkcję w Pythonie, która odpowiada nazwom funkcji wprowadzonym w zmiennej `functions`. Tworzymy również rzeczywiste zewnętrzne wywołania API, aby pobrać potrzebne dane. W tym przypadku korzystamy z Microsoft Learn API, aby wyszukać moduły szkoleniowe.

Ok, stworzyliśmy zmienne `functions` i odpowiadającą funkcję w Pythonie, jak powiedzieć LLM, jak je ze sobą powiązać, aby nasza funkcja w Pythonie została wywołana?

1. Aby sprawdzić, czy musimy wywołać funkcję w Pythonie, musimy zajrzeć do odpowiedzi LLM i sprawdzić, czy zawiera `function_call`, a następnie wywołać wskazaną funkcję. Oto jak można wykonać wspomnianą kontrolę poniżej:

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

   Te trzy linie zapewniają wyodrębnienie nazwy funkcji, argumentów i wykonanie wywołania:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   Poniżej znajduje się wynik uruchomienia naszego kodu:

   **Wynik**

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

1. Teraz wyślemy zaktualizowaną wiadomość, `messages`, do LLM, aby otrzymać odpowiedź w języku naturalnym zamiast odpowiedzi w formacie JSON API.

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

   **Wynik**

   ```python
   {
     "role": "assistant",
     "content": "I found some good courses for beginner students to learn Azure:\n\n1. [Describe concepts of cryptography] (https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n5. [Set up the Rust development environment](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\nYou can click on the links to access the courses."
   }

   ```

## Zadanie

Aby kontynuować naukę Azure OpenAI Function Calling, możesz stworzyć:

- Więcej parametrów funkcji, które mogą pomóc uczniom w znalezieniu odpowiednich kursów.
- Stworzyć kolejne wywołanie funkcji, które uwzględni więcej informacji o uczniu, takich jak jego język ojczysty.
- Utwórz obsługę błędów na wypadek, gdyby wywołanie funkcji i/lub API nie zwróciło żadnych odpowiednich kursów.

Wskazówka: Skorzystaj ze strony [Learn API reference documentation](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst), aby zobaczyć, jak i gdzie dostępne są te dane.

## Świetna robota! Kontynuuj podróż

Po ukończeniu tej lekcji, sprawdź naszą [kolekcję nauki o generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę na temat generatywnej AI!

Przejdź do Lekcji 12, gdzie przyjrzymy się, jak [projektować UX dla aplikacji AI](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.