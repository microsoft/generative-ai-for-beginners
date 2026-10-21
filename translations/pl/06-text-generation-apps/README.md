# Tworzenie aplikacji do generowania tekstu

[![Tworzenie aplikacji do generowania tekstu](../../../translated_images/pl/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Kliknij powyższy obraz, aby obejrzeć film z tej lekcji)_

Do tej pory w tym programie nauczania widziałeś, że istnieją podstawowe pojęcia, takie jak prompt i nawet cała dziedzina zwana "inżynierią promptów". Wiele narzędzi, z którymi możesz się komunikować, takich jak ChatGPT, Office 365, Microsoft Power Platform i inne, wspiera używanie promptów do wykonania czegoś.

Aby dodać takie doświadczenie do aplikacji, musisz zrozumieć pojęcia takie jak prompt, completions (uzupełnienia) i wybrać bibliotekę do pracy. Dokładnie tego nauczysz się w tym rozdziale.

## Wprowadzenie

W tym rozdziale dowiesz się:

- Poznasz bibliotekę openai i jej podstawowe pojęcia.
- Zbudujesz aplikację do generowania tekstu wykorzystując openai.
- Zrozumiesz, jak używać pojęć takich jak prompt, temperatura i tokeny do tworzenia aplikacji generującej tekst.

## Cele nauki

Pod koniec tej lekcji będziesz potrafił:

- Wyjaśnić, czym jest aplikacja do generowania tekstu.
- Zbudować aplikację do generowania tekstu używając openai.
- Skonfigurować aplikację, aby używała więcej lub mniej tokenów oraz zmieniać temperaturę, dla uzyskania różnorodnych wyników.

## Co to jest aplikacja do generowania tekstu?

Zwykle, gdy tworzysz aplikację, ma ona pewien interfejs, na przykład taki jak poniżej:

- Opierający się na poleceniach. Aplikacje konsolowe to typowe aplikacje, gdzie wpisujesz polecenie, a ono wykonuje zadanie. Na przykład `git` to aplikacja oparta na poleceniach.
- Interfejs użytkownika (UI). Niektóre aplikacje mają graficzne interfejsy użytkownika (GUI), gdzie klikasz przyciski, wpisujesz tekst, wybierasz opcje i więcej.

### Aplikacje konsolowe i UI są ograniczone

Porównaj to z aplikacją opartą na poleceniu, gdzie wpisujesz komendę:

- **To jest ograniczone**. Nie możesz wpisać dowolnego polecenia, tylko te, które aplikacja obsługuje.
- **Specyficzne dla języka**. Niektóre aplikacje obsługują wiele języków, ale domyślnie aplikacja jest zbudowana dla konkretnego języka, nawet jeśli można dodać więcej języków.

### Zalety aplikacji do generowania tekstu

Czym więc różni się aplikacja do generowania tekstu?

W aplikacji do generowania tekstu masz więcej elastyczności, nie jesteś ograniczony do zestawu poleceń ani do konkretnego języka wejściowego. Możesz używać naturalnego języka do interakcji z aplikacją. Kolejną korzyścią jest to, że już korzystasz z źródła danych, które zostało wytrenowane na ogromnym korpusie informacji, podczas gdy tradycyjna aplikacja może mieć ograniczenia co do zawartości bazy danych.

### Co można stworzyć za pomocą aplikacji do generowania tekstu?

Można zbudować wiele rzeczy. Na przykład:

- **Chatbot**. Chatbot odpowiadający na pytania na temat takich tematów jak twoja firma i jej produkty może być dobrym wyborem.
- **Pomocnik**. Duże modele językowe (LLM) świetnie radzą sobie z zadaniami takimi jak podsumowywanie tekstów, uzyskiwanie wglądu z tekstów, tworzenie tekstów typu CV i wiele innych.
- **Asystent kodu**. W zależności od modelu językowego, którego używasz, możesz zbudować asystenta kodu, który pomoże ci pisać kod. Na przykład możesz używać produktów takich jak GitHub Copilot oraz ChatGPT, aby pomóc w pisaniu kodu.

## Jak zacząć?

Musisz znaleźć sposób na integrację z dużym modelem językowym (LLM), co zwykle oznacza dwie metody:

- Korzystać z API. Tutaj tworzy się zapytania sieciowe z twoim promptem i otrzymujesz wygenerowany tekst w odpowiedzi.
- Korzystać z biblioteki. Biblioteki ułatwiają wywoływanie API i sprawiają, że są prostsze w użyciu.

## Biblioteki/SDK

Istnieje kilka dobrze znanych bibliotek do pracy z LLM, takich jak:

- **openai**, ta biblioteka ułatwia połączenie z Twoim modelem i wysyłanie promptów.

Następnie są biblioteki działające na wyższym poziomie, takie jak:

- **Langchain**. Langchain jest dobrze znanym narzędziem i wspiera Python.
- **Semantic Kernel**. Semantic Kernel to biblioteka Microsoftu wspierająca języki C#, Python i Java.

## Pierwsza aplikacja korzystająca z openai

Zobaczmy, jak zbudować naszą pierwszą aplikację, jakich bibliotek potrzebujemy, ile to wymaga i tak dalej.

### Instalacja openai

Istnieje wiele bibliotek do interakcji z OpenAI lub Azure OpenAI. Można używać wielu języków programowania takich jak C#, Python, JavaScript, Java i więcej. My wybraliśmy bibliotekę `openai` dla Pythona, więc użyjemy `pip` do jej instalacji.

```bash
pip install openai
```

### Utwórz zasób

Musisz wykonać następujące kroki:

- Utwórz konto na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Uzyskaj dostęp do Azure OpenAI. Przejdź do [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) i złóż wniosek o dostęp.

  > [!NOTE]
  > W momencie pisania tego tekstu, aby korzystać z Azure OpenAI, trzeba złożyć wniosek o dostęp.

- Zainstaluj Pythona <https://www.python.org/>
- Utworzyłeś zasób Azure OpenAI Service. Zobacz ten przewodnik, jak [utworzyć zasób](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Znajdź klucz API i punkt końcowy

Na tym etapie musisz podać swojej bibliotece `openai`, jaki klucz API ma używać. Aby znaleźć swój klucz API, przejdź do sekcji "Keys and Endpoint" w zasobie Azure OpenAI i skopiuj wartość "Key 1".

![Klucze i punkt końcowy zasobu w Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Gdy już skopiujesz te informacje, poinstruuj biblioteki, aby ich używały.

> [!NOTE]
> Warto oddzielić swój klucz API od kodu. Możesz to zrobić, używając zmiennych środowiskowych.
>
> - Ustaw zmienną środowiskową `OPENAI_API_KEY` na swój klucz API.
>   `export OPENAI_API_KEY='sk-...'`

### Konfiguracja Azure

Jeśli używasz Azure OpenAI (obecnie w Microsoft Foundry), tak konfigurujesz ustawienia. Używamy standardowego klienta `OpenAI` skierowanego na punkt końcowy Azure OpenAI `/openai/v1/`, który działa z Responses API i nie wymaga `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Powyżej ustawiamy następujące:

- `api_key`, to Twój klucz API znaleziony w Azure Portal lub w portalu Microsoft Foundry.
- `base_url`, to punkt końcowy zasobu Foundry z dołączonym `/openai/v1/`. Stabilny punkt końcowy v1 działa w OpenAI i Azure OpenAI bez zarządzania `api_version`.

> [!NOTE] > `os.environ` odczytuje zmienne środowiskowe. Możesz jej użyć do odczytywania zmiennych środowiskowych takich jak `AZURE_OPENAI_API_KEY` i `AZURE_OPENAI_ENDPOINT`. Ustaw te zmienne środowiskowe w terminalu lub użyj biblioteki takiej jak `dotenv`.

## Generowanie tekstu

Aby generować tekst, używamy Responses API poprzez metodę `responses.create`. Oto przykład:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

W powyższym kodzie tworzymy odpowiedź, przekazujemy model, którego chcemy użyć oraz prompt. Następnie drukujemy wygenerowany tekst za pomocą `response.output_text`.

### Konwersacje wieloetapowe

Responses API jest dobrze dopasowane zarówno do generowania tekstu jednokrokowego, jak i wieloetapowych chatbotów – dostarczasz listę wiadomości w `input`, aby budować rozmowę:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Więcej o tej funkcjonalności w nadchodzącym rozdziale.

## Ćwiczenie – twoja pierwsza aplikacja do generowania tekstu

Teraz, gdy nauczyliśmy się jak konfigurować openai, czas zbudować twoją pierwszą aplikację do generowania tekstu. Wykonaj te kroki:

1. Utwórz środowisko wirtualne i zainstaluj openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jeśli używasz Windows, wpisz `venv\Scripts\activate` zamiast `source venv/bin/activate`.

   > [!NOTE]
   > Znajdź swój klucz Azure OpenAI, przechodząc do [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) i wyszukując `Open AI`, wybierz `Open AI resource`, potem wybierz `Keys and Endpoint` i skopiuj wartość `Key 1`.

1. Utwórz plik _app.py_ i wklej w nim następujący kod:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make a request using the Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # print response
   print(response.output_text)
   ```

   > [!NOTE]
   > Jeśli używasz zwykłego OpenAI (nie Azure), użyj `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (bez `base_url`) i przekaż nazwę modelu, na przykład `gpt-5-mini`, zamiast nazwy deploymentu.

   Powinieneś zobaczyć wynik podobny do poniższego:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Różne typy promptów, dla różnych zadań

Teraz widzisz, jak generować tekst za pomocą promptu. Masz nawet program działający, który możesz modyfikować, by generował różne typy tekstu.

Promptów można używać do wielu zadań. Na przykład:

- **Generowanie rodzaju tekstu**. Na przykład możesz wygenerować wiersz, pytania do quizu itd.
- **Wyszukiwanie informacji**. Możesz używać promptów do wyszukiwania informacji, na przykład zapytanie „Co oznacza CORS w rozwoju stron internetowych?”.
- **Generowanie kodu**. Możesz używać promptów do generowania kodu, na przykład tworzenia wyrażenia regularnego do walidacji emaili albo generowania całej aplikacji, np. aplikacji webowej.

## Bardziej praktyczny przypadek użycia: generator przepisów

Wyobraź sobie, że masz w domu składniki i chcesz coś ugotować. Do tego potrzebujesz przepisu. Możesz skorzystać z wyszukiwarki lub użyć dużego modelu językowego (LLM).

Możesz napisać prompt w ten sposób:

> "Pokaż mi 5 przepisów na danie ze składników: kurczak, ziemniaki i marchew. Dla każdego przepisu wypisz wszystkie użyte składniki."

Na ten prompt możesz otrzymać odpowiedź podobną do:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

To świetny wynik, wiem, co ugotować. Przydałyby się teraz ulepszenia takie jak:

- Filtrowanie składników, których nie lubię lub na które jestem uczulony.
- Wygenerowanie listy zakupów na wypadek, gdybym nie miał wszystkich składników w domu.

Na powyższe potrzeby dodajmy dodatkowy prompt:

> "Usuń proszę przepisy z czosnkiem, ponieważ jestem uczulony i zastąp go czymś innym. Proszę również o wygenerowanie listy zakupów na te przepisy, uwzględniając, że mam już w domu kurczaka, ziemniaki i marchew."

Otrzymasz teraz następujący efekt:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```

To twoje pięć przepisów, bez czosnku, a także lista zakupów z uwzględnieniem składników, które masz w domu.

## Ćwiczenie – zbuduj generator przepisów

Po odegraniu scenariusza, napiszmy kod realizujący ten scenariusz. Wykonaj następujące kroki:

1. Użyj istniejącego pliku _app.py_ jako punktu wyjścia.
1. Znajdź zmienną `prompt` i zmień jej kod na następujący:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Jeśli uruchomisz teraz ten kod, powinieneś otrzymać wynik podobny do:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > UWAGA, twój LLM działa niedeterministycznie, więc możesz za każdym razem uzyskiwać różne wyniki.

   Świetnie, zobaczmy, jak możemy to poprawić. Aby ulepszyć aplikację, chcemy, aby była elastyczna, aby można było wprowadzać i zmieniać liczbę przepisów oraz składniki.

1. Zmieńmy kod w następujący sposób:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Kod testowy może wyglądać tak:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Ulepszenie przez dodanie filtra i listy zakupów

Teraz mamy działającą aplikację zdolną generować przepisy i jest elastyczna, ponieważ opiera się na danych wejściowych użytkownika, zarówno liczbie przepisów, jak i używanych składnikach.

Aby to udoskonalić, chcemy dodać:

- **Filtrowanie składników**. Chcemy móc filtrować składniki, których nie lubimy lub na które jesteśmy uczuleni. Aby to zrobić, możemy edytować nasz prompt i dodać na końcu warunek filtra w taki sposób:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Tutaj dodajemy `{filter}` na koniec promptu i także pobieramy wartość filtra od użytkownika.

  Przykładowe wejście przy uruchomieniu programu może wyglądać tak:

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

  Jak widzisz, wszystkie przepisy zawierające mleko zostały odfiltrowane. Ale jeśli jesteś nietolerancyjny na laktozę, możesz chcieć odfiltrować też przepisy z serem, więc trzeba to jasno określić.

- **Generowanie listy zakupów**. Chcemy wygenerować listę zakupów, biorąc pod uwagę składniki, które już mamy w domu.

  W tej funkcjonalności możemy spróbować rozwiązać wszystko w jednym prompt lub rozdzielić na dwa prompt. Spróbujmy drugiego podejścia. Proponujemy dodać dodatkowy prompt, ale aby to zadziałało, musimy przekazać wynik pierwszego promptu jako kontekst do drugiego.

  Znajdź w kodzie miejsce, gdzie wyświetlany jest wynik pierwszego promptu i dodaj poniższy kod poniżej:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Zwróć uwagę na następujące:

  1. Tworzymy nowy prompt, dodając wynik z pierwszego promptu do nowego promptu:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Wywołujemy nowe żądanie, ale także biorąc pod uwagę liczbę tokenów z pierwszego promptu, więc tym razem ustawiamy `max_output_tokens` na 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Testując ten kod, uzyskamy następujący wynik:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Ulepsz swoją konfigurację

To, co mamy do tej pory, to działający kod, ale są pewne zmiany, które powinniśmy wprowadzić, aby jeszcze bardziej ulepszyć sprawy. Oto kilka rzeczy, które powinniśmy zrobić:

- **Oddziel tajemnice od kodu**, takich jak klucz API. Tajemnice nie powinny znajdować się w kodzie i powinny być przechowywane w bezpiecznym miejscu. Aby oddzielić tajemnice od kodu, możemy użyć zmiennych środowiskowych oraz bibliotek takich jak `python-dotenv` do wczytywania ich z pliku. Oto jak to może wyglądać w kodzie:

  1. Utwórz plik `.env` z następującą zawartością:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Uwaga, dla Azure OpenAI w Microsoft Foundry zamiast tego należy ustawić następujące zmienne środowiskowe:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     W kodzie zmienne środowiskowe załadujesz w następujący sposób:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Kilka słów na temat długości tokenów**. Powinniśmy rozważyć, ile tokenów potrzebujemy, aby wygenerować pożądany tekst. Tokeny kosztują, więc tam, gdzie to możliwe, powinniśmy starać się oszczędzać liczbę używanych tokenów. Na przykład, czy możemy sformułować zapytanie tak, aby użyć mniej tokenów?

  Aby zmienić liczbę używanych tokenów, możesz użyć parametru `max_output_tokens`. Na przykład, jeśli chcesz użyć 100 tokenów, zrobisz to tak:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Eksperymentowanie z temperaturą**. Temperatura to coś, o czym dotychczas nie wspominaliśmy, a jest to ważny kontekst tego, jak działa nasz program. Im wyższa wartość temperatury, tym bardziej losowy będzie wynik. Natomiast im niższa wartość, tym bardziej przewidywalny będzie wynik. Zastanów się, czy chcesz mieć zmienność w swoim wyniku, czy nie.

  Aby zmienić temperaturę, możesz użyć parametru `temperature`. Na przykład, jeśli chcesz użyć temperatury 0,5, zrobisz to tak:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Uwaga, im bliżej 1.0, tym bardziej zróżnicowany jest wynik.

- **Modele rozumowania nie używają `temperature`**. To ważna zmiana na rok 2026. Obecne, nieprzestarzałe modele w Microsoft Foundry to **modele rozumowania** (rodzina GPT-5, seria o) - i **nie obsługują `temperature` ani `top_p`** (ani `max_tokens`; użyj `max_output_tokens`). Jeśli wyślesz `temperature` do `gpt-5-mini`, otrzymasz błąd "parameter not supported". Aby więc wypróbować powyższy przykład z temperaturą, wskaż model, który nadal obsługuje kontrolki próbkowania - na przykład otwarty model **Llama** taki jak `Llama-3.3-70B-Instruct` z [katalogu modeli Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), wywoływany poprzez punkt końcowy Foundry Models / Azure AI Inference (tak samo jak próbki `githubmodels-*`). Dla modeli rozumowania, takich jak GPT-5, kierujesz wyniki inaczej:
  - **Inżynieria podpowiedzi** - jasne instrukcje, przykłady i uporządkowany output (zobacz lekcję [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) zastępują to, co kiedyś robiły pokrętła próbkowania.
  - **Kontrole rozumowania** - parametry takie jak wysiłek rozumowania/werbalność balansują głębokość rozumowania z latencją i kosztami.

  W skrócie: `temperature`/`top_p` nadal są ważne dla wielu modeli (Llama, Mistral, Phi oraz rodzina GPT-4.x - chociaż GPT-4.x jest przestarzały), ale przyszłość to inżynieria podpowiedzi + kontrole rozumowania dla modeli rozumowania takich jak GPT-5.

## Zadanie

W tym zadaniu możesz wybrać, co zbudować.

Oto kilka propozycji:

- Popraw generator przepisów, aby jeszcze bardziej go ulepszyć. Eksperymentuj z wartościami temperatury i podpowiedziami, aby zobaczyć, co możesz stworzyć.
- Zbuduj "kolegę do nauki". Ta aplikacja powinna umieć odpowiadać na pytania na dany temat, na przykład Python; możesz mieć podpowiedzi takie jak "Czym jest dany temat w Pythonie?" lub możesz mieć podpowiedź "pokaż mi kod dotyczący danego tematu" itp.
- Bot historyczny, ożyw historię, poleć botowi odgrywać postać historyczną i zadawaj pytania dotyczące jego życia i czasów.

## Rozwiązanie

### Kolega do nauki

Poniżej znajduje się przykładowa podpowiedź startowa, zobacz, jak możesz jej użyć i dopasować do swoich potrzeb.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot historyczny

Oto kilka podpowiedzi, których możesz użyć:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Sprawdzenie wiedzy

Co robi parametr temperatura?

1. Kontroluje, jak losowy jest wynik.
1. Kontroluje, jak duża jest odpowiedź.
1. Kontroluje, ile tokenów jest używanych.

## 🚀 Wyzwanie

Pracując nad zadaniem, spróbuj zmieniać temperaturę, ustaw ją na 0, 0.5 i 1. Pamiętaj, że 0 oznacza najmniejszą zmienność, a 1 największą. Jaka wartość działa najlepiej dla Twojej aplikacji?

## Świetna robota! Kontynuuj naukę

Po ukończeniu tej lekcji sprawdź naszą [kolekcję nauki Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej poszerzać swoją wiedzę o Generative AI!

Przejdź do Lekcji 7, gdzie zobaczymy, jak [tworzyć aplikacje czatu](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->