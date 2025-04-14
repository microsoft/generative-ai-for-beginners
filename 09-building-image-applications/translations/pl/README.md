# Budowanie Aplikacji Generujących Obrazy

[![Budowanie Aplikacji Generujących Obrazy](../../images/09-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Duże Modele Językowe (LLM) oferują więcej niż tylko generowanie tekstu. Możliwe jest również generowanie obrazów na podstawie opisów tekstowych. Obrazy jako modalność mogą być niezwykle użyteczne w wielu dziedzinach, od technologii medycznych, architektury, turystyki, po tworzenie gier i wiele innych. W tym rozdziale przyjrzymy się dwóm najpopularniejszym modelom generowania obrazów: DALL-E i Midjourney.

## Wprowadzenie

W tej lekcji omówimy:

- Generowanie obrazów i dlaczego jest przydatne.
- DALL-E i Midjourney - czym są i jak działają.
- Jak zbudować aplikację generującą obrazy.

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafić:

- Zbudować aplikację generującą obrazy.
- Zdefiniować granice dla swojej aplikacji za pomocą metapromptów.
- Pracować z DALL-E i Midjourney.

## Dlaczego warto budować aplikację generującą obrazy?

Aplikacje generujące obrazy to świetny sposób na odkrywanie możliwości Generatywnej SI. Mogą być używane na przykład do:

- **Edycji i syntezy obrazów**. Możesz generować obrazy dla różnych przypadków użycia, takich jak edycja i synteza obrazów.

- **Zastosowań w różnych branżach**. Mogą być również używane do generowania obrazów dla różnych branż, takich jak technologie medyczne, turystyka, tworzenie gier i wiele innych.

## Scenariusz: Edu4All

W ramach tej lekcji będziemy kontynuować współpracę z naszym startupem Edu4All. Uczniowie będą tworzyć obrazy do swoich zadań - dokładnie jakie obrazy, zależy od uczniów, ale mogą to być ilustracje do własnej bajki, stworzenie nowej postaci do opowiadania lub wizualizacja ich pomysłów i koncepcji.

Oto co uczniowie Edu4All mogliby wygenerować, jeśli na przykład pracują na lekcji o zabytkach:

![Startup Edu4All, lekcja o zabytkach, Wieża Eiffla](../../images/startup.png?WT.mc_id=academic-105485-koreyst)

używając promptu w stylu:

> "Pies obok Wieży Eiffla we wczesnym porannym świetle słonecznym"

## Czym są DALL-E i Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) i [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) to dwa z najpopularniejszych modeli generowania obrazów, które pozwalają używać promptów tekstowych do tworzenia obrazów.

### DALL-E

Zacznijmy od DALL-E, który jest modelem Generatywnej SI generującym obrazy na podstawie opisów tekstowych.

> [DALL-E to połączenie dwóch modeli: CLIP i uwagi dyfuzyjnej (diffused attention)](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** to model, który generuje osadzenia (embeddings), czyli numeryczne reprezentacje danych, z obrazów i tekstu.

- **Uwaga dyfuzyjna** to model, który generuje obrazy z osadzeń. DALL-E jest trenowany na zbiorze danych zawierającym obrazy i tekst, i może być używany do generowania obrazów na podstawie opisów tekstowych. Na przykład, DALL-E może być używany do generowania obrazów kota w kapeluszu lub psa z irokezem.

### Midjourney

Midjourney działa podobnie do DALL-E, generując obrazy na podstawie promptów tekstowych. Midjourney również może być używany do generowania obrazów za pomocą promptów, takich jak "kot w kapeluszu" lub "pies z irokezem".

![Obraz wygenerowany przez Midjourney, mechaniczny gołąb](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Autor obrazu: Wikipedia, obraz wygenerowany przez Midjourney_

## Jak działają DALL-E i Midjourney

Najpierw [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E to model Generatywnej SI oparty na architekturze transformera z _autoregresyjnym transformerem_.

_Autoregresyjny transformer_ określa, w jaki sposób model generuje obrazy z opisów tekstowych - generuje jeden piksel na raz, a następnie wykorzystuje wygenerowane piksele do generowania następnego piksela. Przechodząc przez wiele warstw w sieci neuronowej, aż do ukończenia obrazu.

W tym procesie DALL-E kontroluje atrybuty, obiekty, charakterystykę i więcej w generowanym obrazie. Jednak DALL-E 2 i 3 mają większą kontrolę nad generowanym obrazem.

## Budowanie pierwszej aplikacji generującej obrazy

Co więc jest potrzebne do zbudowania aplikacji generującej obrazy? Potrzebujesz następujących bibliotek:

- **python-dotenv**, zdecydowanie zaleca się używanie tej biblioteki do przechowywania sekretów w pliku _.env_ z dala od kodu.
- **openai**, ta biblioteka będzie używana do interakcji z API OpenAI.
- **pillow**, do pracy z obrazami w Pythonie.
- **requests**, do wykonywania żądań HTTP.

1. Utwórz plik _.env_ o następującej zawartości:

   ```text
   AZURE_OPENAI_ENDPOINT=<twój endpoint>
   AZURE_OPENAI_API_KEY=<twój klucz>
   ```

   Znajdź te informacje w Azure Portal dla swojego zasobu w sekcji "Klucze i Endpoint".

1. Zbierz powyższe biblioteki w pliku o nazwie _requirements.txt_ w następujący sposób:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Następnie utwórz wirtualne środowisko i zainstaluj biblioteki:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   W przypadku Windows użyj następujących poleceń, aby utworzyć i aktywować wirtualne środowisko:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Dodaj następujący kod w pliku o nazwie _app.py_:

   ```python
   import openai
   import os
   import requests
   from PIL import Image
   import dotenv

   # import dotenv
   dotenv.load_dotenv()

   # Pobierz endpoint i klucz ze zmiennych środowiskowych
   openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
   openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

   # Przypisz wersję API (DALL-E jest obecnie obsługiwany tylko dla wersji API 2023-06-01-preview)
   openai.api_version = '2023-06-01-preview'
   openai.api_type = 'azure'


   try:
       # Utwórz obraz za pomocą API generowania obrazów
       generation_response = openai.Image.create(
           prompt='Królik na koniu, trzymający lizaka, na mglistej łące, gdzie rosną żonkile',    # Wprowadź tutaj swój tekst promptu
           size='1024x1024',
           n=2,
           temperature=0,
       )
       # Ustaw katalog dla przechowywanego obrazu
       image_dir = os.path.join(os.curdir, 'images')

       # Jeśli katalog nie istnieje, utwórz go
       if not os.path.isdir(image_dir):
           os.mkdir(image_dir)

       # Zainicjuj ścieżkę obrazu (uwaga: typ pliku powinien być png)
       image_path = os.path.join(image_dir, 'generated-image.png')

       # Pobierz wygenerowany obraz
       image_url = generation_response["data"][0]["url"]  # wyodrębnij URL obrazu z odpowiedzi
       generated_image = requests.get(image_url).content  # pobierz obraz
       with open(image_path, "wb") as image_file:
           image_file.write(generated_image)

       # Wyświetl obraz w domyślnej przeglądarce obrazów
       image = Image.open(image_path)
       image.show()

   # złap wyjątki
   except openai.InvalidRequestError as err:
       print(err)

   ```

Wyjaśnijmy ten kod:

- Najpierw importujemy potrzebne biblioteki, w tym bibliotekę OpenAI, bibliotekę dotenv, bibliotekę requests i bibliotekę Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Następnie ładujemy zmienne środowiskowe z pliku _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Po tym ustawiamy endpoint, klucz dla API OpenAI, wersję i typ.

  ```python
  # Pobierz endpoint i klucz ze zmiennych środowiskowych
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # dodaj wersję i typ, specyficzne dla Azure
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Następnie generujemy obraz:

  ```python
  # Utwórz obraz za pomocą API generowania obrazów
  generation_response = openai.Image.create(
      prompt='Królik na koniu, trzymający lizaka, na mglistej łące, gdzie rosną żonkile',    # Wprowadź tutaj swój tekst promptu
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Powyższy kod zwraca obiekt JSON, który zawiera URL wygenerowanego obrazu. Możemy użyć tego URL do pobrania obrazu i zapisania go do pliku.

- Na koniec otwieramy obraz i używamy standardowej przeglądarki obrazów do jego wyświetlenia:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Więcej szczegółów na temat generowania obrazów

Przyjrzyjmy się dokładniej kodowi, który generuje obraz:

```python
generation_response = openai.Image.create(
        prompt='Królik na koniu, trzymający lizaka, na mglistej łące, gdzie rosną żonkile',    # Wprowadź tutaj swój tekst promptu
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** to tekst promptu, który jest używany do generowania obrazu. W tym przypadku używamy promptu "Królik na koniu, trzymający lizaka, na mglistej łące, gdzie rosną żonkile".
- **size** to rozmiar generowanego obrazu. W tym przypadku generujemy obraz o wymiarach 1024x1024 pikseli.
- **n** to liczba generowanych obrazów. W tym przypadku generujemy dwa obrazy.
- **temperature** to parametr, który kontroluje losowość wyjścia modelu Generatywnej SI. Temperatura to wartość między 0 a 1, gdzie 0 oznacza, że wyjście jest deterministyczne, a 1 oznacza, że wyjście jest losowe. Domyślna wartość to 0,7.

Jest więcej rzeczy, które możesz zrobić z obrazami, które omówimy w następnej sekcji.

## Dodatkowe możliwości generowania obrazów

Do tej pory widziałeś, jak mogliśmy wygenerować obraz za pomocą kilku linii w Pythonie. Jednak jest więcej rzeczy, które możesz zrobić z obrazami.

Możesz również wykonać następujące czynności:

- **Przeprowadzać edycje**. Dostarczając istniejący obraz, maskę i prompt, możesz zmienić obraz. Na przykład, możesz dodać coś do części obrazu. Wyobraź sobie nasz obraz królika, możesz dodać kapelusz do królika. Możesz to zrobić, dostarczając obraz, maskę (identyfikującą część obszaru do zmiany) i tekstowy prompt mówiący, co należy zrobić.

  ```python
  response = openai.Image.create_edit(
    image=open("base_image.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="Obraz królika z kapeluszem na głowie.",
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  Obraz bazowy zawierałby tylko królika, ale końcowy obraz miałby kapelusz na głowie królika.

- **Tworzenie wariacji**. Idea polega na tym, że bierzesz istniejący obraz i prosisz o utworzenie jego wariacji. Aby utworzyć wariację, dostarczasz obraz i tekstowy prompt, a kod wygląda tak:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Uwaga, ta funkcja jest obsługiwana tylko przez OpenAI

## Temperatura

Temperatura to parametr, który kontroluje losowość wyjścia modelu Generatywnej SI. Temperatura to wartość między 0 a 1, gdzie 0 oznacza, że wyjście jest deterministyczne, a 1 oznacza, że wyjście jest losowe. Domyślna wartość to 0,7.

Spójrzmy na przykład, jak działa temperatura, uruchamiając ten prompt dwukrotnie:

> Prompt: "Królik na koniu, trzymający lizaka, na mglistej łące, gdzie rosną żonkile"

![Królik na koniu trzymający lizaka, wersja 1](../../images/v1-generated-image.png?WT.mc_id=academic-105485-koreyst)

Teraz uruchommy ten sam prompt jeszcze raz, żeby zobaczyć, że nie otrzymamy dwa razy tego samego obrazu:

![Wygenerowany obraz królika na koniu](../../images/v2-generated-image.png?WT.mc_id=academic-105485-koreyst)

Jak widać, obrazy są podobne, ale nie takie same. Spróbujmy zmienić wartość temperatury na 0,1 i zobaczmy, co się stanie:

```python
 generation_response = openai.Image.create(
        prompt='Królik na koniu, trzymający lizaka, na mglistej łące, gdzie rosną żonkile',    # Wprowadź tutaj swój tekst promptu
        size='1024x1024',
        n=2
    )
```

### Zmiana temperatury

Spróbujmy więc uczynić odpowiedź bardziej deterministyczną. Mogliśmy zaobserwować z dwóch wygenerowanych obrazów, że na pierwszym obrazie jest królik, a na drugim jest koń, więc obrazy znacznie się różnią.

Zmieńmy więc nasz kod i ustawmy temperaturę na 0, w następujący sposób:

```python
generation_response = openai.Image.create(
        prompt='Królik na koniu, trzymający lizaka, na mglistej łące, gdzie rosną żonkile',    # Wprowadź tutaj swój tekst promptu
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Teraz, gdy uruchomisz ten kod, otrzymasz te dwa obrazy:

- ![Temperatura 0, v1](../../images/v1-temp-generated-image.png?WT.mc_id=academic-105485-koreyst)
- ![Temperatura 0, v2](../../images/v2-temp-generated-image.png?WT.mc_id=academic-105485-koreyst)

Tutaj wyraźnie widać, jak obrazy są bardziej do siebie podobne.

## Jak definiować granice dla aplikacji za pomocą metapromptów

Dzięki naszemu demo możemy już generować obrazy dla naszych klientów. Jednak musimy stworzyć pewne granice dla naszej aplikacji.

Na przykład, nie chcemy generować obrazów, które nie są bezpieczne dla pracy lub nie są odpowiednie dla dzieci.

Możemy to zrobić za pomocą _metapromptów_. Metaprompty to tekstowe instrukcje używane do kontrolowania wyjścia modelu Generatywnej SI. Na przykład, możemy użyć metapromptów do kontrolowania wyjścia i zapewnienia, że generowane obrazy są bezpieczne dla pracy lub odpowiednie dla dzieci.

### Jak to działa?

Jak działają metaprompty?

Metaprompty to tekstowe instrukcje używane do kontrolowania wyjścia modelu Generatywnej SI, są umieszczane przed właściwym promptem tekstowym i służą do kontrolowania wyjścia modelu oraz są wbudowane w aplikacje, aby kontrolować wyjście modelu. Łączą wejściowy prompt i metaprompt w jeden tekstowy prompt.

Przykładem metapromptu może być:

```text
Jesteś asystentem projektanta, który tworzy obrazy dla dzieci.

Obraz musi być bezpieczny dla pracy i odpowiedni dla dzieci.

Obraz musi być kolorowy.

Obraz musi być w orientacji poziomej.

Obraz musi mieć proporcje 16:9.

Nie uwzględniaj żadnych danych wejściowych z poniższych, które nie są bezpieczne dla pracy lub odpowiednie dla dzieci.

(Dane wejściowe)

```

Teraz zobaczmy, jak możemy użyć metapromptów w naszym demo.

```python
disallow_list = "miecze, przemoc, krew, gore, nagość, treści seksualne, treści dla dorosłych, tematy dla dorosłych, język dla dorosłych, humor dla dorosłych, żarty dla dorosłych, sytuacje dla dorosłych, dla dorosłych"

meta_prompt =f"""Jesteś asystentem projektanta, który tworzy obrazy dla dzieci.

Obraz musi być bezpieczny dla pracy i odpowiedni dla dzieci.

Obraz musi być kolorowy.

Obraz musi być w orientacji poziomej.

Obraz musi mieć proporcje 16:9.

Nie uwzględniaj żadnych danych wejściowych z poniższych, które nie są bezpieczne dla pracy lub odpowiednie dla dzieci.
{disallow_list}
"""

prompt = f"{meta_prompt}
Utwórz obraz królika na koniu, trzymającego lizaka"

# TODO dodaj żądanie wygenerowania obrazu
```

Z powyższego promptu możesz zobaczyć, jak wszystkie tworzone obrazy uwzględniają metaprompt.

## Zadanie - umożliwmy uczniom tworzenie

Przedstawiliśmy Edu4All na początku tej lekcji. Teraz czas umożliwić uczniom generowanie obrazów do ich zadań.

Uczniowie będą tworzyć obrazy do swoich zadań zawierające zabytki - dokładnie jakie zabytki, zależy od uczniów. Uczniowie są proszeni o wykorzystanie swojej kreatywności w tym zadaniu, aby umieścić te zabytki w różnych kontekstach.

## Rozwiązanie

Oto jedno z możliwych rozwiązań:

```python
import openai
import os
import requests
from PIL import Image
import dotenv

# import dotenv
dotenv.load_dotenv()

# Pobierz endpoint i klucz ze zmiennych środowiskowych
openai.api_base = "<zastąp endpoint>"
openai.api_key = "<zastąp kluczem api>"

# Przypisz wersję API (DALL-E jest obecnie obsługiwany tylko dla wersji API 2023-06-01-preview)
openai.api_version = '2023-06-01-preview'
openai.api_type = 'azure'

disallow_list = "miecze, przemoc, krew, gore, nagość, treści seksualne, treści dla dorosłych, tematy dla dorosłych, język dla dorosłych, humor dla dorosłych, żarty dla dorosłych, sytuacje dla dorosłych, dla dorosłych"

meta_prompt = f"""Jesteś asystentem projektanta, który tworzy obrazy dla dzieci.

Obraz musi być bezpieczny dla pracy i odpowiedni dla dzieci.

Obraz musi być kolorowy.

Obraz musi być w orientacji poziomej.

Obraz musi mieć proporcje 16:9.

Nie uwzględniaj żadnych danych wejściowych z poniższych, które nie są bezpieczne dla pracy lub odpowiednie dla dzieci.
{disallow_list}"""

prompt = f"""{meta_prompt}
Wygeneruj obraz Łuku Triumfalnego w Paryżu, Francja, w wieczornym świetle, z małym dzieckiem trzymającym misia.
""""

try:
    # Utwórz obraz za pomocą API generowania obrazów
    generation_response = openai.Image.create(
        prompt=prompt,    # Wprowadź tutaj swój tekst promptu
        size='1024x1024',
        n=2,
        temperature=0,
    )
    # Ustaw katalog dla przechowywanego obrazu
    image_dir = os.path.join(os.curdir, 'images')

    # Jeśli katalog nie istnieje, utwórz go
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Zainicjuj ścieżkę obrazu (uwaga: typ pliku powinien być png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Pobierz wygenerowany obraz
    image_url = generation_response["data"][0]["url"]  # wyodrębnij URL obrazu z odpowiedzi
    generated_image = requests.get(image_url).content  # pobierz obraz
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Wyświetl obraz w domyślnej przeglądarce obrazów
    image = Image.open(image_path)
    image.show()

# złap wyjątki
except openai.InvalidRequestError as err:
    print(err)
```

## Świetna praca! Kontynuuj naukę

Po ukończeniu tej lekcji, sprawdź naszą [kolekcję materiałów edukacyjnych Generatywnej SI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej podnosić swoją wiedzę o Generatywnej SI!

Przejdź do Lekcji 10, gdzie przyjrzymy się [budowaniu aplikacji AI z wykorzystaniem narzędzi niskokodowych](../../../10-building-low-code-ai-applications/translations/pl/README.md?WT.mc_id=academic-105485-koreyst)
