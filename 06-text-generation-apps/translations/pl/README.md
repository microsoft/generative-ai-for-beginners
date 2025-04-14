# Budowanie Aplikacji Generujących Tekst

[![Budowanie Aplikacji Generujących Tekst](../../images/06-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(Kliknij powyższy obraz, aby obejrzeć wideo tej lekcji)_

Do tej pory w tym programie nauczania widziałeś, że istnieją podstawowe koncepcje, takie jak prompty, a nawet cała dyscyplina zwana "inżynierią promptów". Wiele narzędzi, z którymi możesz wchodzić w interakcję, takich jak ChatGPT, Office 365, Microsoft Power Platform i inne, wspiera korzystanie z promptów, aby coś osiągnąć.

Aby dodać takie doświadczenie do aplikacji, musisz zrozumieć koncepcje takie jak prompty, uzupełnienia (completions) i wybrać bibliotekę, z którą będziesz pracować. Właśnie tego nauczysz się w tym rozdziale.

## Wprowadzenie

W tym rozdziale:

- Poznasz bibliotekę openai i jej podstawowe koncepcje.
- Zbudujesz aplikację generującą tekst przy użyciu openai.
- Zrozumiesz, jak używać koncepcji takich jak prompt, temperatura i tokeny do budowania aplikacji generującej tekst.

## Cele nauki

Po zakończeniu tej lekcji będziesz w stanie:

- Wyjaśnić, czym jest aplikacja generująca tekst.
- Zbudować aplikację generującą tekst przy użyciu openai.
- Skonfigurować swoją aplikację, aby używała więcej lub mniej tokenów, a także zmienić temperaturę dla zróżnicowanego wyniku.

## Czym jest aplikacja generująca tekst?

Normalnie, gdy budujesz aplikację, ma ona jakiś rodzaj interfejsu, taki jak:

- Opartą na komendach. Aplikacje konsolowe to typowe aplikacje, w których wpisujesz komendę, a ona wykonuje zadanie. Na przykład `git` to aplikacja oparta na komendach.
- Interfejs użytkownika (UI). Niektóre aplikacje mają graficzne interfejsy użytkownika (GUI), gdzie klikasz przyciski, wprowadzasz tekst, wybierasz opcje i więcej.

### Aplikacje konsolowe i UI są ograniczone

Porównaj to z aplikacją opartą na komendach, gdzie wpisujesz komendę:

- **Jest ograniczona**. Nie możesz po prostu wpisać dowolnej komendy, tylko te, które aplikacja obsługuje.
- **Specyficzna dla języka**. Niektóre aplikacje obsługują wiele języków, ale domyślnie aplikacja jest zbudowana dla konkretnego języka, nawet jeśli możesz dodać obsługę większej liczby języków.

### Korzyści z aplikacji generujących tekst

Więc czym różni się aplikacja generująca tekst?

W aplikacji generującej tekst masz większą elastyczność, nie jesteś ograniczony do zestawu komend lub konkretnego języka wprowadzania. Zamiast tego możesz używać języka naturalnego do interakcji z aplikacją. Kolejną korzyścią jest to, że już wchodzisz w interakcję ze źródłem danych, które zostało wytrenowane na ogromnym korpusie informacji, podczas gdy tradycyjna aplikacja może być ograniczona do tego, co jest w bazie danych.

### Co mogę zbudować z aplikacją generującą tekst?

Jest wiele rzeczy, które możesz zbudować. Na przykład:

- **Chatbota**. Chatbot odpowiadający na pytania na tematy, takie jak Twoja firma i jej produkty, może być dobrym dopasowaniem.
- **Pomocnika**. LLM-y są świetne w rzeczach takich jak podsumowywanie tekstu, uzyskiwanie spostrzeżeń z tekstu, tworzenie tekstu, takiego jak CV i więcej.
- **Asystenta kodowania**. W zależności od używanego modelu językowego, możesz zbudować asystenta kodowania, który pomoże Ci pisać kod. Na przykład, możesz użyć produktu takiego jak GitHub Copilot, a także ChatGPT, aby pomóc Ci pisać kod.

## Jak mogę zacząć?

Cóż, musisz znaleźć sposób na integrację z LLM, co zwykle wiąże się z następującymi dwoma podejściami:

- Użyj API. Tutaj konstruujesz zapytania internetowe z Twoim promptem i otrzymujesz wygenerowany tekst z powrotem.
- Użyj biblioteki. Biblioteki pomagają enkapsulować wywołania API i ułatwiają ich użycie.

## Biblioteki/SDK

Istnieje kilka dobrze znanych bibliotek do pracy z LLM, takich jak:

- **openai**, ta biblioteka ułatwia połączenie z Twoim modelem i wysyłanie promptów.

Następnie są biblioteki, które działają na wyższym poziomie, takie jak:

- **Langchain**. Langchain jest dobrze znany i wspiera Pythona.
- **Semantic Kernel**. Semantic Kernel to biblioteka od Microsoftu wspierająca języki C#, Python i Java.

## Pierwsza aplikacja używająca openai

Zobaczmy, jak możemy zbudować naszą pierwszą aplikację, jakich bibliotek potrzebujemy, ile jest wymagane i tak dalej.

### Instalacja openai

Istnieje wiele bibliotek do interakcji z OpenAI lub Azure OpenAI. Możliwe jest używanie wielu języków programowania, takich jak C#, Python, JavaScript, Java i inne. Wybraliśmy użycie biblioteki `openai` w Pythonie, więc użyjemy `pip` do jej instalacji.

```bash
pip install openai
```

### Tworzenie zasobu

Musisz wykonać następujące kroki:

- Utwórz konto na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Uzyskaj dostęp do Azure OpenAI. Przejdź do [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) i poproś o dostęp.

  > [!NOTE]
  > W momencie pisania tego tekstu, musisz złożyć wniosek o dostęp do Azure OpenAI.

- Zainstaluj Pythona <https://www.python.org/>
- Utwórz zasób Azure OpenAI Service. Zobacz ten przewodnik, jak [utworzyć zasób](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Znajdź klucz API i endpoint

W tym momencie musisz powiedzieć swojej bibliotece `openai`, jakiego klucza API użyć. Aby znaleźć swój klucz API, przejdź do sekcji "Keys and Endpoint" swojego zasobu Azure OpenAI i skopiuj wartość "Key 1".

![Sekcja Keys and Endpoint zasobu w Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Teraz, gdy masz te informacje skopiowane, poinstruujmy biblioteki, aby ich używały.

> [!NOTE]
> Warto oddzielić klucz API od kodu. Możesz to zrobić, używając zmiennych środowiskowych.
>
> - Ustaw zmienną środowiskową `OPENAI_API_KEY` na swój klucz API.
>   `export OPENAI_API_KEY='sk-...'`

### Konfiguracja Azure

Jeśli używasz Azure OpenAI, oto jak ustawić konfigurację:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Powyżej ustawiamy:

- `api_type` na `azure`. To mówi bibliotece, aby używała Azure OpenAI, a nie OpenAI.
- `api_key`, to Twój klucz API znaleziony w Azure Portal.
- `api_version`, to wersja API, której chcesz użyć. W momencie pisania, najnowsza wersja to `2023-05-15`.
- `api_base`, to endpoint API. Możesz go znaleźć w Azure Portal obok klucza API.

> [!NOTE] > `os.getenv` to funkcja, która odczytuje zmienne środowiskowe. Możesz jej użyć do odczytania zmiennych środowiskowych, takich jak `OPENAI_API_KEY` i `API_BASE`. Ustaw te zmienne środowiskowe w terminalu lub używając biblioteki takiej jak `dotenv`.

## Generowanie tekstu

Sposób na generowanie tekstu to użycie klasy `Completion`. Oto przykład:

```python
prompt = "Uzupełnij następujące: Dawno, dawno temu był sobie"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

W powyższym kodzie tworzymy obiekt completion i przekazujemy model, którego chcemy użyć, oraz prompt. Następnie drukujemy wygenerowany tekst.

### Uzupełnienia czatu

Do tej pory widziałeś, jak używaliśmy `Completion` do generowania tekstu. Ale istnieje inna klasa o nazwie `ChatCompletion`, która bardziej nadaje się do chatbotów. Oto przykład jej użycia:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Więcej na temat tej funkcjonalności w nadchodzącym rozdziale.

## Ćwiczenie - twoja pierwsza aplikacja generująca tekst

Teraz, gdy nauczyliśmy się, jak skonfigurować i skonfigurować openai, nadszedł czas, aby zbudować twoją pierwszą aplikację generującą tekst. Aby zbudować swoją aplikację, wykonaj następujące kroki:

1. Utwórz wirtualne środowisko i zainstaluj openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jeśli używasz Windows, wpisz `venv\Scripts\activate` zamiast `source venv/bin/activate`.

   > [!NOTE]
   > Znajdź swój klucz Azure OpenAI, przechodząc do [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) i wyszukując `Open AI`, a następnie wybierz `Open AI resource`, a następnie wybierz `Keys and Endpoint` i skopiuj wartość `Key 1`.

1. Utwórz plik _app.py_ i nadaj mu następujący kod:

   ```python
   import openai

   openai.api_key = "<zastąp tę wartość swoim kluczem open ai lub kluczem Azure OpenAI>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint znaleziony w Azure Portal, gdzie jest Twój klucz API>"
   deployment_name = "<nazwa wdrożenia>"

   # dodaj swój kod uzupełnienia
   prompt = "Uzupełnij następujące: Dawno, dawno temu był sobie"
   messages = [{"role": "user", "content": prompt}]

   # zrób uzupełnienie
   completion = openai.chat.completions.create(model=deployment_name, messages=messages)

   # wydrukuj odpowiedź
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > Jeśli używasz Azure OpenAI, musisz ustawić `api_type` na `azure` i ustawić `api_key` na swój klucz Azure OpenAI.

   Powinieneś zobaczyć wynik podobny do następującego:

   ```output
    bardzo nieszczęśliwy _____.

   Dawno, dawno temu był sobie bardzo nieszczęśliwa syrenka.
   ```

## Różne rodzaje promptów do różnych rzeczy

Teraz widziałeś, jak generować tekst za pomocą promptu. Masz nawet działający program, który możesz modyfikować i zmieniać, aby generować różne rodzaje tekstu.

Prompty mogą być używane do różnego rodzaju zadań. Na przykład:

- **Generowanie rodzaju tekstu**. Na przykład, możesz generować wiersz, pytania do quizu itp.
- **Wyszukiwanie informacji**. Możesz używać promptów do szukania informacji, jak w następującym przykładzie 'Co oznacza CORS w rozwoju web?'.
- **Generowanie kodu**. Możesz używać promptów do generowania kodu, na przykład opracowania wyrażenia regularnego używanego do walidacji e-maili, a dlaczego nie wygenerować całego programu, takiego jak aplikacja internetowa?

## Bardziej praktyczny przypadek użycia: generator przepisów

Wyobraź sobie, że masz składniki w domu i chcesz coś ugotować. Do tego potrzebujesz przepisu. Jednym ze sposobów znalezienia przepisów jest użycie wyszukiwarki lub możesz użyć LLM, aby to zrobić.

Możesz napisać prompt w ten sposób:

> "Pokaż mi 5 przepisów na danie z następującymi składnikami: kurczak, ziemniaki i marchewki. Dla każdego przepisu wymień wszystkie użyte składniki"

Biorąc pod uwagę powyższy prompt, możesz otrzymać odpowiedź podobną do:

```output
1. Pieczony Kurczak z Warzywami:
Składniki:
- 4 udka z kurczaka
- 2 ziemniaki, pokrojone w kostkę
- 2 marchewki, pokrojone w kostkę
- 2 łyżki oliwy z oliwek
- 2 ząbki czosnku, posiekane
- 1 łyżeczka suszonego tymianku
- 1 łyżeczka suszonego oregano
- Sól i pieprz do smaku

2. Gulasz z Kurczaka i Ziemniaków:
Składniki:
- 2 łyżki oliwy z oliwek
- 1 cebula, posiekana
- 2 ząbki czosnku, posiekane
- 2 piersi z kurczaka, pokrojone w kostkę
- 2 ziemniaki, pokrojone w kostkę
- 2 marchewki, pokrojone w kostkę
- 1 łyżeczka suszonego oregano
- 1 łyżeczka suszonego tymianku
- 1 szklanka bulionu drobiowego
- Sól i pieprz do smaku

3. Zapiekanka z Kurczaka i Ziemniaków:
Składniki:
- 2 łyżki oliwy z oliwek
- 2 piersi z kurczaka, pokrojone w kostkę
- 2 ziemniaki, pokrojone w kostkę
- 2 marchewki, pokrojone w kostkę
- 1 cebula, posiekana
- 2 ząbki czosnku, posiekane
- 1 łyżeczka suszonego oregano
- 1 łyżeczka suszonego tymianku
- 1 szklanka bulionu drobiowego
- Sól i pieprz do smaku

4. Zupa z Kurczaka i Ziemniaków:
Składniki:
- 2 łyżki oliwy z oliwek
- 1 cebula, posiekana
- 2 ząbki czosnku, posiekane
- 2 piersi z kurczaka, pokrojone w kostkę
- 2 ziemniaki, pokrojone w kostkę
- 2 marchewki, pokrojone w kostkę
- 1 łyżeczka suszonego oregano
- 1 łyżeczka suszonego tymianku
- 4 szklanki bulionu drobiowego
- Sól i pieprz do smaku

5. Hash z Kurczaka i Ziemniaków:
Składniki:
- 2 łyżki oliwy z oliwek
- 2 piersi z kurczaka, pokrojone w kostkę
- 2 ziemniaki, pokrojone w kostkę
- 2 marchewki, pokrojone w kostkę
- 1 cebula, posiekana
- 2 ząbki czosnku, posiekane
- 1 łyżeczka suszonego oregano
```

Ten wynik jest świetny, wiem, co gotować. W tym momencie, jakie przydatne ulepszenia można wprowadzić:

- Filtrowanie składników, których nie lubię lub na które jestem uczulony.
- Stworzenie listy zakupów, w przypadku, gdy nie mam wszystkich składników w domu.

Dla powyższych przypadków, dodajmy dodatkowy prompt:

> "Proszę usunąć przepisy z czosnkiem, ponieważ jestem uczulony i zastąpić go czymś innym. Proszę także utworzyć listę zakupów dla przepisów, biorąc pod uwagę, że już mam kurczaka, ziemniaki i marchewki w domu."

Teraz masz nowy wynik, a mianowicie:

```output
1. Pieczony Kurczak z Warzywami:
Składniki:
- 4 udka z kurczaka
- 2 ziemniaki, pokrojone w kostkę
- 2 marchewki, pokrojone w kostkę
- 2 łyżki oliwy z oliwek
- 1 łyżeczka suszonego tymianku
- 1 łyżeczka suszonego oregano
- Sól i pieprz do smaku

2. Gulasz z Kurczaka i Ziemniaków:
Składniki:
- 2 łyżki oliwy z oliwek
- 1 cebula, posiekana
- 2 piersi z kurczaka, pokrojone w kostkę
- 2 ziemniaki, pokrojone w kostkę
- 2 marchewki, pokrojone w kostkę
- 1 łyżeczka suszonego oregano
- 1 łyżeczka suszonego tymianku
- 1 szklanka bulionu drobiowego
- Sól i pieprz do smaku

3. Zapiekanka z Kurczaka i Ziemniaków:
Składniki:
- 2 łyżki oliwy z oliwek
- 2 piersi z kurczaka, pokrojone w kostkę
- 2 ziemniaki, pokrojone w kostkę
- 2 marchewki, pokrojone w kostkę
- 1 cebula, posiekana
- 1 łyżeczka suszonego oregano
- 1 łyżeczka suszonego tymianku
- 1 szklanka bulionu drobiowego
- Sól i pieprz do smaku

4. Zupa z Kurczaka i Ziemniaków:
Składniki:
- 2 łyżki oliwy z oliwek
- 1 cebula, posiekana
- 2 piersi z kurczaka, pokrojone w kostkę
- 2 ziemniaki, pokrojone w kostkę
- 2 marchewki, pokrojone w kostkę
- 1 łyżeczka suszonego oregano
- 1 łyżeczka suszonego tymianku
- 4 szklanki bulionu drobiowego
- Sól i pieprz do smaku

5. Hash z Kurczaka i Ziemniaków:
Składniki:
- 2 łyżki oliwy z oliwek
- 2 piersi z kurczaka, pokrojone w kostkę
- 2 ziemniaki, pokrojone w kostkę
- 2 marchewki, pokrojone w kostkę
- 1 cebula, posiekana
- 1 łyżeczka suszonego oregano

Lista zakupów:
- Oliwa z oliwek
- Cebula
- Tymianek
- Oregano
- Sól
- Pieprz
```

To Twoje pięć przepisów, bez wspomnienia o czosnku, i masz również listę zakupów, biorąc pod uwagę to, co już masz w domu.

## Ćwiczenie - zbuduj generator przepisów

Teraz, gdy omówiliśmy scenariusz, napiszmy kod pasujący do zademonstrowanego scenariusza. Aby to zrobić, wykonaj następujące kroki:

1. Użyj istniejącego pliku _app.py_ jako punktu wyjścia
1. Znajdź zmienną `prompt` i zmień jej kod na następujący:

   ```python
   prompt = "Pokaż mi 5 przepisów na danie z następującymi składnikami: kurczak, ziemniaki i marchewki. Dla każdego przepisu wymień wszystkie użyte składniki"
   ```

   Jeśli teraz uruchomisz kod, powinieneś zobaczyć wynik podobny do:

   ```output
   -Gulasz z Kurczakiem i Ziemniakami: 3 łyżki oleju, 1 cebula, posiekana, 2 ząbki czosnku, posiekane, 1 marchew, obrana i posiekana, 1 ziemniak, obrany i posiekany, 1 liść laurowy, 1 gałązka tymianku, 1/2 łyżeczki soli, 1/4 łyżeczki czarnego pieprzu, 1 1/2 szklanki bulionu drobiowego, 1/2 szklanki suchego białego wina, 2 łyżki posiekanej świeżej pietruszki, 2 łyżki niesolonego masła, 1 1/2 funta udek z kurczaka bez kości i skóry, pokrojonych na kawałki 1-calowe
   -Pieczony Kurczak z Ziemniakami i Marchewkami: 3 łyżki oliwy z oliwek extra virgin, 1 łyżka musztardy Dijon, 1 łyżka posiekanego świeżego rozmarynu, 1 łyżka posiekanego świeżego tymianku, 4 ząbki czosnku, posiekane, 1 1/2 funta małych czerwonych ziemniaków, pokrojonych na ćwiartki, 1 1/2 funta marchewek, pokrojonych wzdłuż na ćwiartki, 1/2 łyżeczki soli, 1/4 łyżeczki czarnego pieprzu, 1 (4-funtowy) cały kurczak
   -Zapiekanka z Kurczaka, Ziemniaków i Marchewek: spray do gotowania, 1 duża cebula, posiekana, 2 ząbki czosnku, posiekane, 1 marchew, obrana i starta, 1 ziemniak, obrany i starty, 1/2 łyżeczki suszonych liści tymianku, 1/4 łyżeczki soli, 1/4 łyżeczki czarnego pieprzu, 2 szklanki bulionu drobiowego beztłuszczowego, o niskiej zawartości sodu, 1 szklanka mrożonego groszku, 1/4 szklanki mąki uniwersalnej, 1 szklanka mleka 2% o zredukowanej zawartości tłuszczu, 1/4 szklanki startego sera parmezan

   -Obiad z Kurczaka i Ziemniaków w Jednym Garnku: 2 łyżki oliwy z oliwek, 1 funt udek z kurczaka bez kości i skóry, pokrojonych na kawałki 1-calowe, 1 duża cebula, posiekana, 3 ząbki czosnku, posiekane, 1 marchew, obrana i posiekana, 1 ziemniak, obrany i posiekany, 1 liść laurowy, 1 gałązka tymianku, 1/2 łyżeczki soli, 1/4 łyżeczki czarnego pieprzu, 2 szklanki bulionu drobiowego, 1/2 szklanki suchego białego wina

   -Curry z Kurczaka, Ziemniaków i Marchewek: 1 łyżka oleju roślinnego, 1 duża cebula, posiekana, 2 ząbki czosnku, posiekane, 1 marchew, obrana i posiekana, 1 ziemniak, obrany i posiekany, 1 łyżeczka mielonej kolendry, 1 łyżeczka mielonego kuminu, 1/2 łyżeczki mielonej kurkumy, 1/2 łyżeczki mielonego imbiru, 1/4 łyżeczki pieprzu cayenne, 2 szklanki bulionu drobiowego, 1/2 szklanki suchego białego wina, 1 (15-uncjowa) puszka ciecierzycy, odsączona i przepłukana, 1/2 szklanki rodzynek, 1/2 szklanki posiekanej świeżej kolendry
   ```

   > UWAGA, Twój LLM jest niedeterministyczny, więc możesz otrzymać różne wyniki za każdym razem, gdy uruchomisz program.

   Świetnie, zobaczmy, jak możemy poprawić rzeczy. Aby poprawić rzeczy, chcemy upewnić się, że kod jest elastyczny, więc składniki i liczba przepisów mogą być poprawione i zmienione.

1. Zmieńmy kod w następujący sposób:

   ```python
   no_recipes = input("Liczba przepisów (na przykład, 5): ")

   ingredients = input("Lista składników (na przykład, kurczak, ziemniaki i marchewki): ")

   # interpolacja liczby przepisów do promptu i składników
   prompt = f"Pokaż mi {no_recipes} przepisów na danie z następującymi składnikami: {ingredients}. Dla każdego przepisu wymień wszystkie użyte składniki"
   ```

   Przetestowanie tego kodu mogłoby wyglądać tak:

   ```output
   Liczba przepisów (na przykład, 5): 3
   Lista składników (na przykład, kurczak, ziemniaki i marchewki): mleko,truskawki

   -Koktajl mleczny z truskawkami: mleko, truskawki, cukier, ekstrakt waniliowy, kostki lodu
   -Ciasto truskawkowe: mleko, mąka, proszek do pieczenia, cukier, sól, niesolone masło, truskawki, bita śmietana
   -Mleko truskawkowe: mleko, truskawki, cukier, ekstrakt waniliowy
   ```

### Ulepszenie przez dodanie filtra i listy zakupów

Mamy teraz działającą aplikację zdolną do produkowania przepisów i jest elastyczna, ponieważ opiera się na wejściach od użytkownika, zarówno co do liczby przepisów, jak i używanych składników.

Aby dalej ją ulepszyć, chcemy dodać następujące:

- **Filtrowanie składników**. Chcemy być w stanie filtrować składniki, których nie lubimy lub na które jesteśmy uczuleni. Aby to osiągnąć, możemy edytować nasz istniejący prompt i dodać warunek filtrowania na jego końcu, w ten sposób:

  ```python
  filter = input("Filtr (na przykład, wegetariański, wegański lub bezglutenowy): ")

  prompt = f"Pokaż mi {no_recipes} przepisów na danie z następującymi składnikami: {ingredients}. Dla każdego przepisu wymień wszystkie użyte składniki, bez {filter}"
  ```

  Powyżej, dodajemy `{filter}` na końcu promptu i przechwytujemy również wartość filtra od użytkownika.

  Przykładowe wejście przy uruchomieniu programu może teraz wyglądać tak:

  ```output
  Liczba przepisów (na przykład, 5): 3
  Lista składników (na przykład, kurczak, ziemniaki i marchewki): cebula,mleko
  Filtr (na przykład, wegetariański, wegański lub bezglutenowy): bez mleka

  1. Francuska Zupa Cebulowa

  Składniki:

  -1 duża cebula, pokrojona
  -3 szklanki bulionu wołowego
  -1 szklanka mleka
  -6 plastrów chleba francuskiego
  -1/4 szklanki startego sera parmezan
  -1 łyżka masła
  -1 łyżeczka suszonego tymianku
  -1/4 łyżeczki soli
  -1/4 łyżeczki czarnego pieprzu

  Instrukcje:

  1. W dużym garnku, podsmaż cebulę na maśle, aż się zezłoci.
  2. Dodaj bulion wołowy, mleko, tymianek, sól i pieprz. Doprowadź do wrzenia.
  3. Zmniejsz ogień i gotuj przez 10 minut.
  4. Umieść plastry chleba francuskiego na miseczkach do zupy.
  5. Nalej zupę na chleb.
  6. Posyp serem parmezan.

  2. Zupa Cebulowa i Ziemniaczana

  Składniki:

  -1 duża cebula, posiekana
  -2 szklanki ziemniaków, pokrojonych w kostkę
  -3 szklanki bulionu warzywnego
  -1 szklanka mleka
  -1/4 łyżeczki czarnego pieprzu

  Instrukcje:

  1. W dużym garnku, podsmaż cebulę na maśle, aż się zezłoci.
  2. Dodaj ziemniaki, bulion warzywny, mleko i pieprz. Doprowadź do wrzenia.
  3. Zmniejsz ogień i gotuj przez 10 minut.
  4. Podawaj gorącą.

  3. Kremowa Zupa Cebulowa

  Składniki:

  -1 duża cebula, posiekana
  -3 szklanki bulionu warzywnego
  -1 szklanka mleka
  -1/4 łyżeczki czarnego pieprzu
  -1/4 szklanki mąki uniwersalnej
  -1/2 szklanki startego sera parmezan

  Instrukcje:

  1. W dużym garnku, podsmaż cebulę na maśle, aż się zezłoci.
  2. Dodaj bulion warzywny, mleko i pieprz. Doprowadź do wrzenia.
  3. Zmniejsz ogień i gotuj przez 10 minut.
  4. W małej misce, wymieszaj mąkę i ser parmezan, aż będzie gładkie.
  5. Dodaj do zupy i gotuj przez dodatkowe 5 minut, lub aż zupa zgęstnieje.
  ```

  Jak widać, wszelkie przepisy z mlekiem zostały odfiltrowane. Ale jeśli jesteś nietolerancyjny na laktozę, możesz chcieć filtrować również przepisy z serem, więc istnieje potrzeba bycia jasnym.

- **Stworzenie listy zakupów**. Chcemy stworzyć listę zakupów, biorąc pod uwagę, co już mamy w domu.

  Dla tej funkcjonalności, moglibyśmy albo próbować rozwiązać wszystko w jednym prompcie, albo moglibyśmy podzielić to na dwa prompty. Spróbujmy tego drugiego podejścia. Tutaj sugerujemy dodanie dodatkowego promptu, ale aby to zadziałało, musimy dodać wynik poprzedniego promptu jako kontekst do późniejszego promptu.

  Znajdź część kodu, która drukuje wynik z pierwszego promptu i dodaj poniższy kod poniżej:

  ```python
  old_prompt_result = completion.choices[0].message.content
  prompt = "Utwórz listę zakupów dla wygenerowanych przepisów i proszę nie uwzględniaj składników, które już mam."

  new_prompt = f"{old_prompt_result} {prompt}"
  messages = [{"role": "user", "content": new_prompt}]
  completion = openai.Completion.create(engine=deployment_name, messages=messages, max_tokens=1200)

  # wydrukuj odpowiedź
  print("Lista zakupów:")
  print(completion.choices[0].message.content)
  ```

  Zwróć uwagę na następujące:

  1.  Konstruujemy nowy prompt, dodając wynik z pierwszego promptu do nowego promptu:

      ```python
      new_prompt = f"{old_prompt_result} {prompt}"
      ```

  1.  Robimy nowe żądanie, ale również biorąc pod uwagę liczbę tokenów, o które prosiliśmy w pierwszym prompcie, więc tym razem mówimy, że `max_tokens` to 1200.

           ```python
           completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
           ```

           Przeprowadzając ten kod, otrzymujemy teraz następujący wynik:

           ```output
           Liczba przepisów (na przykład, 5): 2
           Lista składników (na przykład, kurczak, ziemniaki i marchewki): jabłko,mąka
           Filtr (na przykład, wegetariański, wegański lub bezglutenowy): cukier


           -Placki jabłkowo-mączne: 1 szklanka mąki, 1/2 łyżeczki proszku do pieczenia, 1/2 łyżeczki sody oczyszczonej, 1/4 łyżeczki soli, 1 łyżka cukru, 1 jajko, 1 szklanka maślanki lub kwaśnego mleka, 1/4 szklanki roztopionego masła, 1 jabłko Granny Smith, obrane i starte
           -Frytki jabłkowe: 1-1/2 szklanki mąki, 1 łyżeczka proszku do pieczenia, 1/4 łyżeczki soli, 1/4 łyżeczki sody oczyszczonej, 1/4 łyżeczki gałki muszkatołowej, 1/4 łyżeczki cynamonu, 1/4 łyżeczki anyżu, 1/4 szklanki cukru, 1/4 szklanki tłuszczu roślinnego, 1/4 szklanki mleka, 1 jajko, 2 szklanki startych, obranych jabłek
           Lista zakupów:
           -Mąka, proszek do pieczenia, soda oczyszczona, sól, cukier, jajko, maślanka, masło, jabłko, gałka muszkatołowa, cynamon, anyż
           ```

      </code_block_to_apply_changes_from>

## Ulepszenie konfiguracji

To, co mamy do tej pory, to kod, który działa, ale jest kilka poprawek, które powinniśmy wprowadzić, aby dalej ulepszyć rzeczy. Niektóre rzeczy, które powinniśmy zrobić, to:

- **Oddzielenie sekretów od kodu**, takich jak klucz API. Sekrety nie należą do kodu i powinny być przechowywane w bezpiecznym miejscu. Aby oddzielić sekrety od kodu, możemy użyć zmiennych środowiskowych i bibliotek takich jak `python-dotenv` do ładowania ich z pliku. Oto jak to wyglądałoby w kodzie:

  1. Utwórz plik `.env` o następującej treści:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Uwaga, dla Azure, musisz ustawić następujące zmienne środowiskowe:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<zastąp>
     ```

     W kodzie, załadowałbyś zmienne środowiskowe w ten sposób:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Słowo o długości tokenów**. Powinniśmy rozważyć, ile tokenów potrzebujemy do wygenerowania tekstu, którego chcemy. Tokeny kosztują pieniądze, więc tam, gdzie to możliwe, powinniśmy starać się być ekonomicznymi z liczbą używanych tokenów. Na przykład, czy możemy sformułować prompt tak, abyśmy mogli użyć mniej tokenów?

  Aby zmienić używane tokeny, możesz użyć parametru `max_tokens`. Na przykład, jeśli chcesz użyć 100 tokenów, zrobiłbyś to:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Eksperymentowanie z temperaturą**. Temperatura to coś, o czym do tej pory nie wspomnieliśmy, ale jest ważnym kontekstem dla tego, jak działa nasz program. Im wyższa wartość temperatury, tym bardziej losowy będzie wynik. Odwrotnie, im niższa wartość temperatury, tym bardziej przewidywalny będzie wynik. Zastanów się, czy chcesz wariacji w swoim wyniku, czy nie.

  Aby zmienić temperaturę, możesz użyć parametru `temperature`. Na przykład, jeśli chcesz użyć temperatury 0,5, zrobiłbyś to:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Uwaga, im bliżej 1.0, tym bardziej zróżnicowany wynik.

## Zadanie

Dla tego zadania, możesz wybrać, co zbudować.

Oto kilka sugestii:

- Dostosuj aplikację generatora przepisów, aby dalej ją ulepszyć. Pobaw się wartościami temperatury i promptami, aby zobaczyć, co możesz wymyślić.
- Zbuduj "kumpla do nauki". Ta aplikacja powinna być w stanie odpowiadać na pytania na temat, na przykład Pythona, mógłbyś mieć prompty takie jak "Co to jest określony temat w Pythonie?", lub mógłbyś mieć prompt, który mówi, pokaż mi kod dla określonego tematu itp.
- Bot historyczny, ożyw historię, poinstruuj bota, aby odgrywał określoną postać historyczną i zadawaj mu pytania o jego życie i czasy.

## Rozwiązanie

### Kumpel do nauki

Poniżej znajduje się początkowy prompt, zobacz, jak możesz go użyć i dostosować do swoich upodobań.

```text
- "Jesteś ekspertem od języka Python

    Zaproponuj lekcję dla początkujących w Pythonie w następującym formacie:

    Format:
    - koncepcje:
    - krótkie wyjaśnienie lekcji:
    - ćwiczenie w kodzie z rozwiązaniami"
```

### Bot historyczny

Oto kilka promptów, których możesz użyć:

```text
- "Jesteś Abrahamem Lincolnem, powiedz mi o sobie w 3 zdaniach i odpowiedz używając gramatyki i słów, jakich Abraham by użył"
- "Jesteś Abrahamem Lincolnem, odpowiedz używając gramatyki i słów, jakich Abraham by użył:

   Opowiedz mi o swoich największych osiągnięciach, w 300 słowach"
```

## Sprawdzenie wiedzy

Co robi koncepcja temperatury?

1. Kontroluje, jak losowy jest wynik.
1. Kontroluje, jak duża jest odpowiedź.
1. Kontroluje, ile tokenów jest używanych.

## 🚀 Wyzwanie

Pracując nad zadaniem, spróbuj zmieniać temperaturę, spróbuj ustawić ją na 0, 0,5 i 1. Pamiętaj, że 0 jest najmniej zróżnicowane, a 1 najbardziej, jaka wartość działa najlepiej dla Twojej aplikacji?

## Świetna Praca! Kontynuuj Naukę

Po ukończeniu tej lekcji, sprawdź naszą [kolekcję materiałów edukacyjnych o Generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby nadal podnosić swoją wiedzę o Generatywnej AI!

Przejdź do Lekcji 7, gdzie przyjrzymy się, jak [budować aplikacje czatowe](../../../07-building-chat-applications/translations/pl/README.md?WT.mc_id=academic-105485-koreyst)!
