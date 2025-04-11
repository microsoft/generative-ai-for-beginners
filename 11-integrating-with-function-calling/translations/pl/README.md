# Integracja z wywołaniami funkcji

[![Integracja z wywołaniami funkcji](../../images/11-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson11-gh?WT.mc_id=academic-105485-koreyst)

W poprzednich lekcjach nauczyłeś się już całkiem sporo. Jednak możemy jeszcze ulepszyć nasze podejście. Możemy skupić się na tym, jak uzyskać bardziej spójny format odpowiedzi, aby ułatwić pracę z odpowiedzią w dalszych etapach. Ponadto możemy chcieć dodać dane z innych źródeł, aby dodatkowo wzbogacić naszą aplikację.

Powyższe problemy są właśnie tym, co ten rozdział ma na celu rozwiązać.

## Wprowadzenie

Ta lekcja obejmie:

- Wyjaśnienie czym jest wywoływanie funkcji i jego przypadki użycia.
- Tworzenie wywołania funkcji przy użyciu Azure OpenAI.
- Jak zintegrować wywołanie funkcji w aplikacji.

## Cele Nauki

Po zakończeniu tej lekcji będziesz potrafił:

- Wyjaśnić cel używania wywołań funkcji.
- Skonfigurować wywołanie funkcji przy użyciu Azure OpenAI Service.
- Projektować efektywne wywołania funkcji dla przypadków użycia Twojej aplikacji.

## Scenariusz: Ulepszanie naszego chatbota za pomocą funkcji

W tej lekcji chcemy zbudować funkcję dla naszego startupu edukacyjnego, która pozwoli użytkownikom korzystać z chatbota do znajdowania kursów technicznych. Będziemy polecać kursy, które pasują do ich poziomu umiejętności, aktualnej roli i interesującej ich technologii.

Aby ukończyć ten scenariusz, będziemy korzystać z kombinacji:

- `Azure OpenAI` do stworzenia doświadczenia czatu dla użytkownika.
- `Microsoft Learn Catalog API` do pomocy użytkownikom w znalezieniu kursów na podstawie ich zapytań.
- `Wywołania funkcji` do przyjęcia zapytania użytkownika i wysłania go do funkcji w celu wykonania żądania API.

Aby zacząć, przyjrzyjmy się, dlaczego w ogóle chcielibyśmy używać wywołań funkcji:

## Dlaczego Wywołania Funkcji

Przed wywołaniami funkcji, odpowiedzi z LLM były nieustrukturyzowane i niespójne. Programiści musieli pisać złożony kod walidacji, aby upewnić się, że są w stanie obsłużyć każdą odmianę odpowiedzi. Użytkownicy nie mogli otrzymać odpowiedzi na pytania takie jak "Jaka jest aktualna pogoda w Sztokholmie?". Działo się tak, ponieważ modele były ograniczone do danych, na których były trenowane.

Wywołanie funkcji to funkcja usługi Azure OpenAI, która pozwala przezwyciężyć następujące ograniczenia:

- **Spójny format odpowiedzi**. Jeśli możemy lepiej kontrolować format odpowiedzi, możemy łatwiej zintegrować odpowiedź w dalszych etapach z innymi systemami.
- **Zewnętrzne dane**. Możliwość wykorzystania danych z innych źródeł aplikacji w kontekście czatu.

## Ilustracja problemu na podstawie scenariusza

> Zalecamy skorzystanie z [dołączonego notebooka](../../python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreyst), jeśli chcesz uruchomić poniższy scenariusz. Możesz też po prostu czytać dalej, ponieważ staramy się zilustrować problem, w rozwiązaniu którego mogą pomóc funkcje.

Przyjrzyjmy się przykładowi, który ilustruje problem z formatem odpowiedzi:

Powiedzmy, że chcemy stworzyć bazę danych z danymi studentów, abyśmy mogli zasugerować im odpowiedni kurs. Poniżej mamy dwa opisy studentów, które są bardzo podobne pod względem zawartych danych.

1. Tworzenie połączenia z naszym zasobem Azure OpenAI:

   ```python
   import os
   import json
   from openai import AzureOpenAI
   from dotenv import load_dotenv
   load_dotenv()

   client = AzureOpenAI(
   api_key=os.environ['AZURE_OPENAI_API_KEY'],  # to jest również wartość domyślna, można ją pominąć
   api_version = "2023-07-01-preview"
   )

   deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']
   ```

   Powyżej znajduje się kod Pythona do konfiguracji naszego połączenia z Azure OpenAI, gdzie ustawiamy `api_type`, `api_base`, `api_version` i `api_key`.

1. Tworzenie dwóch opisów studentów przy użyciu zmiennych `student_1_description` i `student_2_description`.

   ```python
   student_1_description="Emily Johnson jest studentką drugiego roku informatyki na Uniwersytecie Duke. Ma średnią ocen 3,7. Emily jest aktywną członkinią uniwersyteckiego Klubu Szachowego i Drużyny Debat. Ma nadzieję na karierę w inżynierii oprogramowania po ukończeniu studiów."

   student_2_description = "Michael Lee jest studentem drugiego roku informatyki na Uniwersytecie Stanford. Ma średnią ocen 3,8. Michael znany jest ze swoich umiejętności programistycznych i jest aktywnym członkiem uniwersyteckiego Klubu Robotyki. Ma nadzieję na karierę w sztucznej inteligencji po ukończeniu studiów."
   ```

   Chcemy wysłać powyższe opisy studentów do LLM, aby przeanalizować dane. Te dane mogą być później wykorzystane w naszej aplikacji i wysłane do API lub przechowywane w bazie danych.

1. Stwórzmy dwa identyczne prompty, w których instruujemy LLM, jakie informacje nas interesują:

   ```python
   prompt1 = f'''
   Proszę wyodrębnić następujące informacje z podanego tekstu i zwrócić je jako obiekt JSON:

   name
   major
   school
   grades
   club

   Poniżej znajduje się tekst, z którego należy wyodrębnić informacje:
   {student_1_description}
   '''

   prompt2 = f'''
   Proszę wyodrębnić następujące informacje z podanego tekstu i zwrócić je jako obiekt JSON:

   name
   major
   school
   grades
   club

   Poniżej znajduje się tekst, z którego należy wyodrębnić informacje:
   {student_2_description}
   '''
   ```

   Powyższe prompty instruują LLM, aby wyodrębnił informacje i zwrócił odpowiedź w formacie JSON.

1. Po skonfigurowaniu promptów i połączenia z Azure OpenAI, wyślemy teraz prompty do LLM za pomocą `openai.ChatCompletion`. Zapisujemy prompt w zmiennej `messages` i przypisujemy rolę do `user`. Ma to na celu naśladowanie wiadomości od użytkownika pisanej do chatbota.

   ```python
   # odpowiedź na pierwszy prompt
   openai_response1 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt1}]
   )
   openai_response1.choices[0].message.content

   # odpowiedź na drugi prompt
   openai_response2 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt2}]
   )
   openai_response2.choices[0].message.content
   ```

Teraz możemy wysłać oba zapytania do LLM i zbadać otrzymaną odpowiedź, znajdując ją w ten sposób: `openai_response1['choices'][0]['message']['content']`.

1. Na koniec możemy przekonwertować odpowiedź na format JSON, wywołując `json.loads`:

   ```python
   # Wczytywanie odpowiedzi jako obiektu JSON
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

   Chociaż prompty są takie same, a opisy są podobne, widzimy wartości właściwości `Grades` sformatowane inaczej, ponieważ czasami możemy otrzymać format `3.7` lub `3.7 GPA`.

   Wynik ten wynika z faktu, że LLM przyjmuje nieustrukturyzowane dane w formie pisanego promptu i również zwraca nieustrukturyzowane dane. Potrzebujemy ustrukturyzowanego formatu, abyśmy wiedzieli, czego się spodziewać przy przechowywaniu lub używaniu tych danych.

Jak więc rozwiązać problem z formatowaniem? Używając wywołania funkcji, możemy upewnić się, że otrzymamy ustrukturyzowane dane. Podczas korzystania z wywołania funkcji, LLM nie wywołuje ani nie uruchamia żadnych funkcji. Zamiast tego tworzymy strukturę, którą LLM ma naśladować w swoich odpowiedziach. Następnie używamy tych ustrukturyzowanych odpowiedzi, aby wiedzieć, jaką funkcję uruchomić w naszych aplikacjach.

![function flow](../../images/Function-Flow.png?WT.mc_id=academic-105485-koreyst)

Możemy następnie wziąć to, co zwraca funkcja i wysłać to z powrotem do LLM. LLM odpowie następnie używając języka naturalnego, aby odpowiedzieć na zapytanie użytkownika.

## Przypadki użycia wywołań funkcji

Istnieje wiele różnych przypadków użycia, w których wywołania funkcji mogą ulepszyć Twoją aplikację, takich jak:

- **Wywoływanie zewnętrznych narzędzi**. Chatboty są świetne w udzielaniu odpowiedzi na pytania użytkowników. Korzystając z wywołania funkcji, chatboty mogą używać wiadomości od użytkowników do wykonywania określonych zadań. Na przykład, student może poprosić chatbota o "Wysłanie e-maila do mojego instruktora z informacją, że potrzebuję więcej pomocy z tym tematem". Może to wywołać funkcję `send_email(to: string, body: string)`

- **Tworzenie zapytań API lub bazy danych**. Użytkownicy mogą znaleźć informacje używając języka naturalnego, który zostaje przekształcony w sformatowane zapytanie lub żądanie API. Przykładem może być nauczyciel, który prosi o "Kto są studenci, którzy ukończyli ostatnie zadanie", co może wywołać funkcję o nazwie `get_completed(student_name: string, assignment: int, current_status: string)`

- **Tworzenie ustrukturyzowanych danych**. Użytkownicy mogą wziąć blok tekstu lub CSV i użyć LLM do wyodrębnienia ważnych informacji z niego. Na przykład, student może przekonwertować artykuł z Wikipedii o porozumieniach pokojowych, aby stworzyć fiszki AI. Można to zrobić za pomocą funkcji o nazwie `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)`

## Tworzenie Pierwszego Wywołania Funkcji

Proces tworzenia wywołania funkcji obejmuje 3 główne kroki:

1. **Wywołanie** API Chat Completions z listą Twoich funkcji i wiadomością użytkownika.
2. **Odczytanie** odpowiedzi modelu w celu wykonania działania, tj. wykonania funkcji lub wywołania API.
3. **Wykonanie** kolejnego wywołania API Chat Completions z odpowiedzią z Twojej funkcji, aby użyć tych informacji do stworzenia odpowiedzi dla użytkownika.

![LLM Flow](../../images/LLM-Flow.png?WT.mc_id=academic-105485-koreyst)

### Krok 1 - tworzenie wiadomości

Pierwszym krokiem jest utworzenie wiadomości użytkownika. Może to być dynamicznie przypisane przez pobranie wartości wejściowej tekstowej lub możesz przypisać wartość tutaj. Jeśli jest to Twój pierwszy raz pracy z API Chat Completions, musimy zdefiniować `role` i `content` wiadomości.

`role` może być albo `system` (tworzenie reguł), `assistant` (model) lub `user` (użytkownik końcowy). W przypadku wywołania funkcji przypiszemy to jako `user` i przykładowe pytanie.

```python
messages= [ {"role": "user", "content": "Znajdź mi dobry kurs dla początkującego studenta do nauki Azure."} ]
```

Przypisując różne role, LLM ma jasność, czy to system coś mówi, czy użytkownik, co pomaga budować historię konwersacji, na której LLM może bazować.

### Krok 2 - tworzenie funkcji

Następnie zdefiniujemy funkcję i jej parametry. Użyjemy tutaj tylko jednej funkcji o nazwie `search_courses`, ale możesz utworzyć wiele funkcji.

> **Ważne**: Funkcje są zawarte w wiadomości systemowej do LLM i będą wliczane w ilość dostępnych tokenów, które masz do dyspozycji.

Poniżej tworzymy funkcje jako tablicę elementów. Każdy element jest funkcją i ma właściwości `name`, `description` i `parameters`:

```python
functions = [
   {
      "name":"search_courses",
      "description":"Pobiera kursy z indeksu wyszukiwania na podstawie dostarczonych parametrów",
      "parameters":{
         "type":"object",
         "properties":{
            "role":{
               "type":"string",
               "description":"Rola uczącego się (np. developer, data scientist, student, itp.)"
            },
            "product":{
               "type":"string",
               "description":"Produkt, którego dotyczy lekcja (np. Azure, Power BI, itp.)"
            },
            "level":{
               "type":"string",
               "description":"Poziom doświadczenia, jaki posiada uczący się przed przystąpieniem do kursu (np. beginner, intermediate, advanced)"
            }
         },
         "required":[
            "role"
         ]
      }
   }
]
```

Opiszmy bardziej szczegółowo każdą instancję funkcji poniżej:

- `name` - Nazwa funkcji, którą chcemy wywołać.
- `description` - Jest to opis działania funkcji. Tutaj ważne jest, aby być konkretnym i jasnym.
- `parameters` - Lista wartości i format, które chcesz, aby model wyprodukował w swojej odpowiedzi. Tablica parametrów składa się z elementów, gdzie elementy mają następujące właściwości:
  1.  `type` - Typ danych, w którym będą przechowywane właściwości.
  1.  `properties` - Lista określonych wartości, które model wykorzysta w swojej odpowiedzi
      1. `name` - Klucz to nazwa właściwości, którą model użyje w swojej sformatowanej odpowiedzi, na przykład `product`.
      1. `type` - Typ danych tej właściwości, na przykład `string`.
      1. `description` - Opis konkretnej właściwości.

Istnieje również opcjonalna właściwość `required` - wymagana właściwość do ukończenia wywołania funkcji.

### Krok 3 - Wykonanie wywołania funkcji

Po zdefiniowaniu funkcji, musimy teraz uwzględnić ją w wywołaniu API Chat Completion. Robimy to dodając `functions` do żądania. W tym przypadku `functions=functions`.

Istnieje również opcja ustawienia `function_call` na `auto`. Oznacza to, że pozwolimy LLM zdecydować, która funkcja powinna być wywołana na podstawie wiadomości użytkownika, zamiast przypisywać ją samodzielnie.

Oto kod poniżej, w którym wywołujemy `ChatCompletion.create`, zauważ, jak ustawiamy `functions=functions` i `function_call="auto"`, dając tym samym LLM wybór, kiedy wywołać funkcje, które mu dostarczamy:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

Zwracana odpowiedź wygląda teraz tak:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

Tutaj możemy zobaczyć, jak funkcja `search_courses` została wywołana i z jakimi argumentami, wymienionymi we właściwości `arguments` w odpowiedzi JSON.

LLM był w stanie znaleźć dane pasujące do argumentów funkcji, ponieważ wyodrębnił je z wartości dostarczonej do parametru `messages` w wywołaniu chat completion. Poniżej przypomnienie wartości `messages`:

```python
messages= [ {"role": "user", "content": "Znajdź mi dobry kurs dla początkującego studenta do nauki Azure."} ]
```

Jak widzisz, `student`, `Azure` i `beginner` zostały wyodrębnione z `messages` i ustawione jako dane wejściowe do funkcji. Używanie funkcji w ten sposób to świetny sposób na wyodrębnianie informacji z promptu, ale także do zapewnienia struktury dla LLM i posiadania funkcjonalności wielokrotnego użytku.

Następnie musimy zobaczyć, jak możemy to wykorzystać w naszej aplikacji.

## Integracja Wywołań Funkcji w Aplikacji

Po przetestowaniu sformatowanej odpowiedzi z LLM, możemy teraz zintegrować to z aplikacją.

### Zarządzanie przepływem

Aby zintegrować to z naszą aplikacją, wykonajmy następujące kroki:

1. Najpierw wykonajmy wywołanie do usług OpenAI i zapiszmy wiadomość w zmiennej o nazwie `response_message`.

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

   Zauważ, jak teraz tworzymy rzeczywistą funkcję Pythona, która mapuje się na nazwy funkcji wprowadzone w zmiennej `functions`. Wykonujemy również rzeczywiste zewnętrzne wywołania API w celu pobrania potrzebnych danych. W tym przypadku korzystamy z Microsoft Learn API, aby wyszukać moduły szkoleniowe.

Ok, więc stworzyliśmy zmienne `functions` i odpowiadającą im funkcję Pythona, jak powiedzieć LLM, jak mapować te dwie rzeczy, aby nasza funkcja Pythona została wywołana?

1. Aby zobaczyć, czy potrzebujemy wywołać funkcję Pythona, musimy zajrzeć do odpowiedzi LLM i sprawdzić, czy `function_call` jest jej częścią i wywołać wskazaną funkcję. Oto jak można dokonać wspomnianego sprawdzenia poniżej:

   ```python
   # Sprawdź, czy model chce wywołać funkcję
   if response_message.function_call.name:
    print("Zalecane wywołanie funkcji:")
    print(response_message.function_call.name)
    print()

    # Wywołaj funkcję.
    function_name = response_message.function_call.name

    available_functions = {
            "search_courses": search_courses,
    }
    function_to_call = available_functions[function_name]

    function_args = json.loads(response_message.function_call.arguments)
    function_response = function_to_call(**function_args)

    print("Wynik wywołania funkcji:")
    print(function_response)
    print(type(function_response))


    # Dodaj odpowiedź asystenta i odpowiedź funkcji do wiadomości
    messages.append( # dodawanie odpowiedzi asystenta do wiadomości
        {
            "role": response_message.role,
            "function_call": {
                "name": function_name,
                "arguments": response_message.function_call.arguments,
            },
            "content": None
        }
    )
    messages.append( # dodawanie odpowiedzi funkcji do wiadomości
        {
            "role": "function",
            "name": function_name,
            "content":function_response,
        }
    )
   ```

   Te trzy linie zapewniają, że wyodrębniamy nazwę funkcji, argumenty i wykonujemy wywołanie:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   Poniżej znajduje się wynik uruchomienia naszego kodu:

   **Wynik**

   ```Zalecane wywołanie funkcji:
   {
     "name": "search_courses",
     "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
   }

   Wynik wywołania funkcji:
   [{'title': 'Describe concepts of cryptography', 'url': 'https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?
   WT.mc_id=api_CatalogApi'}, {'title': 'Introduction to audio classification with TensorFlow', 'url': 'https://learn.microsoft.com/en-
   us/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi'}, {'title': 'Design a Performant Data Model in Azure SQL
   Database with Azure Data Studio', 'url': 'https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?
   WT.mc_id=api_CatalogApi'}, {'title': 'Getting started with the Microsoft Cloud Adoption Framework for Azure', 'url':
   'https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi'}, {'title': 'Set up the
   Rust development environment', 'url': 'https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi'}]
   <class 'str'>
   ```

1. Teraz wyślemy zaktualizowaną wiadomość `messages` do LLM, abyśmy mogli otrzymać odpowiedź w języku naturalnym zamiast odpowiedzi w formacie JSON API.

   ```python
   print("Wiadomości w następnym żądaniu:")
   print(messages)
   print()

   second_response = client.chat.completions.create(
      messages=messages,
      model=deployment,
      function_call="auto",
      functions=functions,
      temperature=0
         )  # uzyskaj nową odpowiedź od GPT, gdzie może zobaczyć odpowiedź funkcji


   print(second_response.choices[0].message)
   ```

   **Wynik**

   ```python
   {
     "role": "assistant",
     "content": "Znalazłem kilka dobrych kursów dla początkujących studentów do nauki Azure:\n\n1. [Describe concepts of cryptography] (https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n5. [Set up the Rust development environment](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\nMożesz kliknąć na linki, aby uzyskać dostęp do kursów."
   }

   ```

## Zadanie

Aby kontynuować naukę o wywoływaniu funkcji Azure OpenAI, możesz zbudować:

- Więcej parametrów funkcji, które mogą pomóc uczącym się znaleźć więcej kursów.
- Stworzyć inne wywołanie funkcji, które pobiera więcej informacji od uczącego się, takich jak ich język ojczysty.
- Stworzyć obsługę błędów, gdy wywołanie funkcji i/lub API nie zwraca żadnych odpowiednich kursów.

Wskazówka: Zapoznaj się ze [stroną dokumentacji referencyjnej API Learn](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst), aby zobaczyć jak i gdzie te dane są dostępne.

## Świetna praca! Kontynuuj podróż

Po ukończeniu tej lekcji sprawdź naszą [Kolekcję nauki Generatywnej SI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej podnosić swoją wiedzę na temat Generatywnej SI!

Przejdź do Lekcji 12, gdzie przyjrzymy się, jak [projektować UX dla aplikacji SI](../../../12-designing-ux-for-ai-applications/translations/pl/README.md?WT.mc_id=academic-105485-koreyst)!
