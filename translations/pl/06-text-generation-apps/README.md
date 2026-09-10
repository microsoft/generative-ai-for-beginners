# Tworzenie aplikacji do generowania tekstu

[![Tworzenie aplikacji do generowania tekstu](../../../translated_images/pl/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_

Do tej pory widziałeś w tym programie, że istnieją podstawowe pojęcia, takie jak podpowiedzi (prompts) oraz całe zagadnienie zwane "inżynierią podpowiedzi". Wiele narzędzi, z którymi możesz się komunikować, jak ChatGPT, Office 365, Microsoft Power Platform i inne, wspiera cię w korzystaniu z podpowiedzi, aby osiągnąć cel.

Aby dodać takie doświadczenie do aplikacji, musisz zrozumieć takie pojęcia jak podpowiedzi, odpowiedzi oraz wybrać bibliotekę do współpracy. Dokładnie tego nauczysz się w tym rozdziale.

## Wprowadzenie

W tym rozdziale:

- Poznasz bibliotekę openai i jej podstawowe pojęcia.
- Zbudujesz aplikację do generowania tekstu przy użyciu openai.
- Zrozumiesz jak używać pojęć takich jak prompt, temperatura i tokeny do tworzenia aplikacji generujących tekst.

## Cele nauki

Po zakończeniu tej lekcji będziesz potrafił:

- Wyjaśnić, czym jest aplikacja do generowania tekstu.
- Zbudować aplikację do generowania tekstu za pomocą openai.
- Skonfigurować swoją aplikację tak, aby korzystała z większej lub mniejszej liczby tokenów oraz zmieniać temperaturę, dla uzyskania zróżnicowanych wyników.

## Czym jest aplikacja do generowania tekstu?

Zazwyczaj gdy tworzysz aplikację, ma ona jakiś interfejs, na przykład taki:

- Komendowy. Aplikacje konsolowe to typowe aplikacje, w których wpisujesz polecenie, a aplikacja wykonuje zadanie. Na przykład, `git` jest aplikacją opartą na poleceniach.
- Interfejs użytkownika (UI). Niektóre aplikacje mają graficzne interfejsy użytkownika (GUI), gdzie klikasz przyciski, wpisujesz tekst, wybierasz opcje i więcej.

### Aplikacje konsolowe i UI mają ograniczenia

Porównaj to do aplikacji opartej na poleceniach, gdzie wpisujesz polecenie:

- **To jest ograniczone**. Nie możesz wpisywać dowolnych poleceń, tylko te, które aplikacja obsługuje.
- **Specyficzne dla języka**. Niektóre aplikacje obsługują wiele języków, ale domyślnie aplikacja jest zbudowana pod konkretny język, nawet jeśli możesz dodać więcej języków.

### Zalety aplikacji do generowania tekstu

Czym więc różni się aplikacja do generowania tekstu?

W aplikacji generującej tekst masz więcej elastyczności, nie jesteś ograniczony do zestawu poleceń lub konkretnego języka wejściowego. Zamiast tego możesz używać języka naturalnego do interakcji z aplikacją. Kolejną zaletą jest to, że już pracujesz z źródłem danych trenowanym na ogromnym korpusie informacji, podczas gdy tradycyjna aplikacja może być ograniczona do tego, co jest w bazie danych.

### Co mogę stworzyć z aplikacją do generowania tekstu?

Możesz zbudować wiele rzeczy. Na przykład:

- **Chatbota**. Chatbot odpowiadający na pytania dotyczące tematów, na przykład twojej firmy i jej produktów, może być dobrym pomysłem.
- **Pomocnika**. LLM świetnie radzi sobie z takimi zadaniami jak streszczanie tekstu, uzyskiwanie wniosków z tekstu, generowanie tekstów typu CV i inne.
- **Asystenta kodu**. W zależności od używanego modelu językowego, możesz stworzyć asystenta kodu pomagającego pisać kod. Na przykład, możesz użyć produktów takich jak GitHub Copilot oraz ChatGPT, które pomagają pisać kod.

## Jak zacząć?

Musisz znaleźć sposób na integrację z LLM, co zwykle sprowadza się do dwóch podejść:

- Użycie API. Tutaj tworzysz zapytania sieciowe z twoją podpowiedzią i otrzymujesz wygenerowany tekst.
- Użycie biblioteki. Biblioteki pomagają enkapsulować wywołania API i ułatwiają ich użycie.

## Biblioteki/SDK

Istnieje kilka znanych bibliotek do pracy z LLM, takich jak:

- **openai**, ta biblioteka ułatwia połączenie z modelem i wysyłanie podpowiedzi.

Następnie są biblioteki działające na wyższym poziomie, takie jak:

- **Langchain**. Langchain jest znany i obsługuje Pythona.
- **Semantic Kernel**. Semantic Kernel to biblioteka Microsoftu obsługująca języki C#, Python oraz Java.

## Pierwsza aplikacja z użyciem openai

Zobaczmy, jak zbudować naszą pierwszą aplikację, jakie biblioteki są potrzebne, ile to zajmuje i tak dalej.

### Instalacja openai

Istnieje wiele bibliotek do interakcji z OpenAI lub Azure OpenAI. Można używać różnych języków programowania, takich jak C#, Python, JavaScript, Java i więcej. My wybraliśmy bibliotekę `openai` w Pythonie, więc użyjemy `pip`, aby ją zainstalować.

```bash
pip install openai
```

### Utwórz zasób

Wykonaj następujące kroki:

- Załóż konto na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Uzyskaj dostęp do Azure OpenAI. Wejdź na [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) i złóż wniosek o dostęp.

  > [!NOTE]
  > W momencie pisania, konieczne jest złożenie wniosku o dostęp do Azure OpenAI.

- Zainstaluj Pythona <https://www.python.org/>
- Utwórz zasób Azure OpenAI Service. Zobacz ten poradnik, jak [utworzyć zasób](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Znajdź klucz API i punkt końcowy

W tym momencie musisz powiedzieć swojej bibliotece `openai`, którego klucza API używać. Aby znaleźć klucz API, przejdź do sekcji "Klucze i punkt końcowy" zasobu Azure OpenAI i skopiuj wartość "Klucz 1".

![Klucze i punkt końcowy zasobu w Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Teraz, gdy masz skopiowaną tę informację, wskażemy bibliotekom, aby z niej korzystały.

> [!NOTE]
> Warto oddzielić swój klucz API od kodu. Można to zrobić za pomocą zmiennych środowiskowych.
>
> - Ustaw zmienną środowiskową `OPENAI_API_KEY` na swój klucz API.
>   `export OPENAI_API_KEY='sk-...'`

### Konfiguracja Azure

Jeśli używasz Azure OpenAI (obecnie część Microsoft Foundry), oto jak skonfigurować ustawienia. Używamy standardowego klienta `OpenAI` skierowanego do punktu końcowego Azure OpenAI `/openai/v1/`, który działa z Responses API i nie wymaga `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Powyżej ustawiamy:

- `api_key`, jest to twój klucz API znaleziony w portalu Azure lub Microsoft Foundry.
- `base_url`, to Twój punkt końcowy zasobu Foundry z dodanym `/openai/v1/`. Stabilny punkt końcowy v1 działa zarówno z OpenAI, jak i Azure OpenAI bez potrzeby zarządzania `api_version`.

> [!NOTE] > `os.environ` odczytuje zmienne środowiskowe. Możesz go użyć do odczytu zmiennych środowiskowych, takich jak `AZURE_OPENAI_API_KEY` i `AZURE_OPENAI_ENDPOINT`. Ustaw te zmienne środowiskowe w terminalu lub za pomocą biblioteki takiej jak `dotenv`.

## Generowanie tekstu

Sposobem na generowanie tekstu jest użycie Responses API poprzez metodę `responses.create`. Oto przykład:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # to jest nazwa wdrożenia twojego modelu
    input=prompt,
    store=False,
)
print(response.output_text)
```

W powyższym kodzie tworzymy odpowiedź i przekazujemy model, który chcemy użyć oraz podpowiedź (prompt). Następnie wypisujemy wygenerowany tekst przez `response.output_text`.

### Konwersacje wieloetapowe

Responses API dobrze nadaje się zarówno do generowania tekstu jednokrotnego, jak i do wieloetapowych chatbotów – podajesz listę wiadomości w `input` aby zbudować rozmowę:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Więcej o tej funkcjonalności w nadchodzącym rozdziale.

## Ćwiczenie - twoja pierwsza aplikacja do generowania tekstu

Teraz, gdy nauczyliśmy się jak skonfigurować i ustawić openai, czas zbudować twoją pierwszą aplikację do generowania tekstu. Aby to zrobić, wykonaj następujące kroki:

1. Utwórz środowisko wirtualne i zainstaluj openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jeśli używasz Windows, wpisz `venv\Scripts\activate` zamiast `source venv/bin/activate`.

   > [!NOTE]
   > Znajdź swój klucz Azure OpenAI przechodząc na [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), wyszukaj `Open AI`, wybierz zasób `Open AI` i następnie `Keys and Endpoint`, skopiuj wartość `Key 1`.

1. Utwórz plik _app.py_ i wpisz w nim poniższy kod:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # dodaj swój kod do ukończenia
   prompt = "Complete the following: Once upon a time there was a"

   # wykonaj żądanie za pomocą API Odpowiedzi
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # wydrukuj odpowiedź
   print(response.output_text)
   ```

   > [!NOTE]
   > Jeśli używasz zwykłego OpenAI (nie Azure), użyj `client = OpenAI(api_key="<wstaw swój klucz OpenAI>")` (bez `base_url`) i podaj nazwę modelu, np. `gpt-5-mini` zamiast nazwy wdrożenia.

   Powinieneś zobaczyć wynik podobny do tego:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Różne typy podpowiedzi do różnych zastosowań

Teraz widzisz, jak generować tekst z użyciem podpowiedzi. Masz nawet działający program, który możesz modyfikować i zmieniać, by generować różne typy tekstów.

Podpowiedzi można używać do najróżniejszych zadań. Na przykład:

- **Generowanie danego typu tekstu**. Na przykład, możesz wygenerować wiersz, pytania do quizu itp.
- **Wyszukiwanie informacji**. Możesz używać podpowiedzi, by szukać informacji, jak w przykładzie 'Co oznacza CORS w tworzeniu stron?'
- **Generowanie kodu**. Możesz generować kod, na przykład napisać wyrażenie regularne do walidacji adresów e-mail lub nawet całe programy, np. aplikację webową.

## Bardziej praktyczny przykład: generator przepisów

Wyobraź sobie, że masz w domu składniki i chcesz coś ugotować. Do tego potrzebujesz przepisu. Możesz użyć wyszukiwarki lub LLM do tego celu.

Możesz napisać podpowiedź tak:

> "Pokaż mi 5 przepisów na potrawę z następujących składników: kurczak, ziemniaki i marchew. Dla każdego przepisu wypisz wszystkie użyte składniki"

Na powyższą podpowiedź możesz otrzymać odpowiedź podobną do:

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

To świetny wynik, wiem, co ugotować. Na tym etapie przydatne mogą być:

- Filtrowanie składników, których nie lubię lub na które jestem uczulony.
- Sporządzenie listy zakupów, jeśli nie mam wszystkich składników w domu.

Dla powyższych przypadków dodajmy kolejną podpowiedź:

> "Proszę usuń przepisy z czosnkiem, bo jestem uczulony i zamień je na coś innego. Proszę też wygeneruj listę zakupów dla tych przepisów, biorąc pod uwagę, że mam już w domu kurczaka, ziemniaki i marchew."

Teraz masz nowy wynik, mianowicie:

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

To twoje pięć przepisów, bez wymienionego czosnku, oraz lista zakupów uwzględniająca to, co masz w domu.

## Ćwiczenie - zbuduj generator przepisów

Po rozegraniu scenariusza napiszmy kod odpowiadający pokazanej sytuacji. Aby to zrobić, wykonaj następujące kroki:

1. Użyj istniejącego pliku _app.py_ jako punktu wyjścia
1. Znajdź zmienną `prompt` i zmień jej kod na następujący:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Jeśli teraz uruchomisz kod, powinieneś zobaczyć wynik podobny do:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > UWAGA, Twój LLM jest niedeterministyczny, więc możesz otrzymać różne wyniki za każdym razem, gdy uruchomisz program.

   Świetnie, zobaczmy, jak można to ulepszyć. Aby to zrobić, chcemy, by kod był elastyczny, tak aby składniki i liczba przepisów mogły być zmieniane.

1. Zmień kod w następujący sposób:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # wstaw liczbę przepisów do podpowiedzi i składników
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Wywołanie testowe kodu może wyglądać tak:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Ulepszenie przez dodanie filtra i listy zakupów

Mamy teraz działającą aplikację, która potrafi generować przepisy i jest elastyczna, ponieważ zależy od danych wejściowych użytkownika, zarówno liczby przepisów, jak i używanych składników.

Aby ulepszyć ją dalej, chcemy dodać:

- **Filtrowanie składników**. Chcemy móc filtrować składniki, których nie lubimy lub na które mamy uczulenie. Aby to osiągnąć, możemy edytować istniejącą podpowiedź i dodać warunek filtru na jej końcu, tak jak poniżej:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Powyżej dodaliśmy `{filter}` na końcu podpowiedzi i także przechwytujemy wartość filtru od użytkownika.

  Przykładowe uruchomienie programu może teraz wyglądać tak:

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

  Jak widzisz, przepisy zawierające mleko zostały odfiltrowane. Jednak jeśli masz nietolerancję laktozy, możesz chcieć również odfiltrować przepisy z serem, dlatego ważne jest jasne określenie.


- **Stwórz listę zakupów**. Chcemy stworzyć listę zakupów, biorąc pod uwagę to, co już mamy w domu.

  Dla tej funkcjonalności możemy spróbować rozwiązać wszystko w jednym promptcie lub podzielić to na dwa promptty. Spróbujmy podejścia drugiego. Tutaj sugerujemy dodanie dodatkowego promptu, ale aby to zadziałało, musimy dodać wynik pierwszego promptu jako kontekst do drugiego promptu.

  Zlokalizuj część w kodzie, która wyświetla wynik z pierwszego promptu i dodaj poniższy kod poniżej:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # wydrukuj odpowiedź
  print("Shopping list:")
  print(response.output_text)
  ```

  Zwróć uwagę na następujące rzeczy:

  1. Tworzymy nowy prompt, dodając wynik z pierwszego promptu do nowego promptu:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Wykonujemy nowe zapytanie, ale również uwzględniając liczbę tokenów, o które prosiliśmy w pierwszym promptcie, więc tym razem ustawiamy `max_output_tokens` na 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Testując ten kod, otrzymujemy następujące wyjście:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Ulepsz swój setup

To, co mamy do tej pory, to kod, który działa, ale są pewne poprawki, które powinniśmy wprowadzić, aby go jeszcze ulepszyć. Oto kilka rzeczy, które powinniśmy zrobić:

- **Oddziel sekrety od kodu**, np. klucz API. Sekrety nie powinny znajdować się w kodzie i powinny być przechowywane w bezpiecznym miejscu. Aby oddzielić sekrety od kodu, możemy użyć zmiennych środowiskowych oraz bibliotek takich jak `python-dotenv`, które ładują je z pliku. Oto jak to mogłoby wyglądać w kodzie:

  1. Utwórz plik `.env` z następującą zawartością:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Uwaga, dla Azure OpenAI w Microsoft Foundry musisz zamiast tego ustawić następujące zmienne środowiskowe:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     W kodzie zmienne środowiskowe ładujesz w ten sposób:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Kilka słów o długości tokenów**. Powinniśmy rozważyć, ile tokenów potrzeba, aby wygenerować pożądany tekst. Tokeny kosztują, więc tam, gdzie to możliwe, powinniśmy starać się oszczędzać ich ilość. Na przykład, czy możemy sformułować prompt w taki sposób, aby użyć mniej tokenów?

  Aby zmienić liczbę używanych tokenów, możesz użyć parametru `max_output_tokens`. Na przykład, jeśli chcesz użyć 100 tokenów, zrób tak:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Eksperymentowanie z temperaturą**. Temperatura to coś, o czym dotąd nie wspomnieliśmy, ale to ważny kontekst dla działania naszego programu. Im wyższa wartość temperatury, tym bardziej losowy będzie rezultat wyjściowy. Natomiast im niższa wartość temperatury, tym bardziej przewidywalny będzie rezultat. Zastanów się, czy chcesz, aby twój wynik był zróżnicowany, czy nie.

  Aby zmienić temperaturę, możesz użyć parametru `temperature`. Na przykład, jeśli chcesz zastosować temperaturę 0,5, zrób tak:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Uwaga, im bliżej 1.0, tym bardziej zróżnicowany jest wynik.

- **Modele rozumowania nie używają `temperature`**. To ważna zmiana na 2026 rok. Aktualne, niewycofane modele w Microsoft Foundry to **modele rozumowania** (rodzina GPT-5, seria o) - i one **nie wspierają `temperature` ani `top_p`** (ani `max_tokens`; używaj `max_output_tokens`). Jeśli wyślesz `temperature` do `gpt-5-mini`, otrzymasz błąd "parameter not supported". Aby wypróbować powyższy przykład z temperaturą, skieruj zapytanie do modelu, który wciąż wspiera kontrolę próbkowania - na przykład do otwartego modelu **Llama** takiego jak `Llama-3.3-70B-Instruct` z [katalogu modeli Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), wywoływanego przez punkt końcowy Foundry Models / Azure AI Inference (tak samo jak próbki `githubmodels-*`). W przypadku modeli rozumowania jak GPT-5, sterowanie wynikiem odbywa się inaczej:
  - **Inżynieria promptów** - jasne instrukcje, przykłady i ustrukturyzowany wynik (zobacz lekcję [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) zastępują działanie pokręteł do próbkowania.
  - **Kontrole rozumowania** - parametry takie jak wysiłek rozumowania/werbalność wymieniają głębokość rozumowania na opóźnienie i koszt.

  W skrócie: `temperature`/`top_p` są nadal ważne w wielu modelach (Llama, Mistral, Phi oraz rodzina GPT-4.x - chociaż GPT-4.x jest wycofywany), ale kierunkiem rozwoju jest inżynieria promptów + kontrola rozumowania w modelach rozumowania jak GPT-5.

## Zadanie

Na to zadanie możesz wybrać, co zbudujesz.

Oto kilka sugestii:

- Dopracuj aplikację generatora przepisów, aby jeszcze ją ulepszyć. Eksperymentuj z wartościami temperatury i promptami, aby zobaczyć, co uda ci się wymyślić.
- Zbuduj "towarzysza nauki". Ta aplikacja powinna potrafić odpowiadać na pytania o dany temat, na przykład Python, możesz mieć prompt "Co to jest dany temat w Pythonie?", albo prompt "Pokaż mi kod na dany temat" itd.
- Bot historyczny, ożyw historię, nakaz botowi grać określoną postać historyczną i zadawaj mu pytania o jej życie i czasy.

## Rozwiązanie

### Towarzysz nauki

Poniżej jest prompt startowy, zobacz, jak możesz go użyć i dostosować do swoich potrzeb.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot historyczny

Oto kilka promptów, których możesz użyć:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Sprawdzenie wiedzy

Co robi parametr temperatura?

1. Kontroluje, jak losowy jest wynik wyjściowy.
1. Kontroluje, jak długa jest odpowiedź.
1. Kontroluje, ile tokenów jest używanych.

## 🚀 Wyzwanie

Podczas wykonywania zadania, spróbuj różnych wartości temperatury: ustaw 0, 0,5 i 1. Pamiętaj, że 0 to najmniej zróżnicowany wynik, a 1 to najbardziej. Która wartość działa najlepiej w twojej aplikacji?

## Świetna robota! Kontynuuj naukę

Po ukończeniu tej lekcji sprawdź naszą [kolekcję do nauki Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę na temat Sztucznej Inteligencji generatywnej!

Przejdź do Lekcji 7, gdzie omówimy, jak [budować aplikacje czatowe](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->