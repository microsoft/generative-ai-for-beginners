<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:24:40+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "pl"
}
-->
# Tworzenie aplikacji do generowania obrazów

[![Tworzenie aplikacji do generowania obrazów](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.pl.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM to nie tylko generowanie tekstu. Możliwe jest także tworzenie obrazów na podstawie opisów tekstowych. Obrazy jako modalność mogą być bardzo przydatne w wielu dziedzinach, takich jak MedTech, architektura, turystyka, tworzenie gier i inne. W tym rozdziale przyjrzymy się dwóm najpopularniejszym modelom generowania obrazów: DALL-E i Midjourney.

## Wprowadzenie

W tej lekcji omówimy:

- Generowanie obrazów i dlaczego jest to przydatne.
- DALL-E i Midjourney, czym są i jak działają.
- Jak zbudować aplikację do generowania obrazów.

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

- Zbudować aplikację do generowania obrazów.
- Określić granice działania aplikacji za pomocą meta promptów.
- Pracować z DALL-E i Midjourney.

## Dlaczego warto tworzyć aplikację do generowania obrazów?

Aplikacje do generowania obrazów to świetny sposób na poznanie możliwości Generatywnej Sztucznej Inteligencji. Mogą być wykorzystywane na przykład do:

- **Edycji i syntezy obrazów**. Możesz generować obrazy do różnych zastosowań, takich jak edycja czy synteza obrazów.

- **Zastosowań w różnych branżach**. Mogą być też używane do tworzenia obrazów dla branż takich jak MedTech, turystyka, tworzenie gier i inne.

## Scenariusz: Edu4All

W ramach tej lekcji będziemy kontynuować pracę z naszym startupem Edu4All. Uczniowie będą tworzyć obrazy do swoich zadań – jakie dokładnie obrazy, to już ich wybór, mogą to być ilustracje do własnej bajki, stworzenie nowej postaci do historii lub pomoc w wizualizacji pomysłów i koncepcji.

Oto co uczniowie Edu4All mogliby wygenerować na przykład podczas pracy w klasie nad zabytkami:

![Startup Edu4All, lekcja o zabytkach, Wieża Eiffla](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.pl.png)

używając promptu:

> "Pies obok Wieży Eiffla w porannym świetle"

## Czym są DALL-E i Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) i [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) to dwa z najpopularniejszych modeli generowania obrazów, które pozwalają na tworzenie obrazów na podstawie promptów tekstowych.

### DALL-E

Zacznijmy od DALL-E, który jest modelem Generatywnej AI generującym obrazy na podstawie opisów tekstowych.

> [DALL-E to połączenie dwóch modeli, CLIP i diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** to model generujący embeddingi, czyli numeryczne reprezentacje danych, z obrazów i tekstu.

- **Diffused attention** to model generujący obrazy na podstawie embeddingów. DALL-E jest trenowany na zbiorze obrazów i tekstów i może tworzyć obrazy na podstawie opisów tekstowych. Na przykład, DALL-E może wygenerować obraz kota w kapeluszu lub psa z irokezem.

### Midjourney

Midjourney działa podobnie do DALL-E, generując obrazy na podstawie promptów tekstowych. Midjourney również może tworzyć obrazy na podstawie promptów takich jak „kot w kapeluszu” lub „pies z irokezem”.

![Obraz wygenerowany przez Midjourney, mechaniczny gołąb](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Źródło: Wikipedia, obraz wygenerowany przez Midjourney_

## Jak działają DALL-E i Midjourney

Najpierw [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E to model Generatywnej AI oparty na architekturze transformera z _autoregresyjnym transformerem_.

_Autoregresyjny transformer_ definiuje sposób, w jaki model generuje obrazy z opisów tekstowych – tworzy obraz piksel po pikselu, wykorzystując wygenerowane piksele do stworzenia kolejnych. Przechodzi przez wiele warstw w sieci neuronowej, aż obraz jest kompletny.

Dzięki temu procesowi DALL-E kontroluje atrybuty, obiekty, cechy i inne elementy obrazu, który generuje. Jednak DALL-E 2 i 3 oferują jeszcze większą kontrolę nad generowanym obrazem.

## Budowa pierwszej aplikacji do generowania obrazów

Co jest potrzebne, aby zbudować aplikację do generowania obrazów? Potrzebujesz następujących bibliotek:

- **python-dotenv** – zalecane jest użycie tej biblioteki, aby przechowywać sekrety w pliku _.env_ z dala od kodu.
- **openai** – ta biblioteka służy do komunikacji z API OpenAI.
- **pillow** – do pracy z obrazami w Pythonie.
- **requests** – do wykonywania zapytań HTTP.

1. Utwórz plik _.env_ z następującą zawartością:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Znajdź te informacje w Azure Portal dla swojego zasobu w sekcji "Keys and Endpoint".

1. Zbierz powyższe biblioteki w pliku _requirements.txt_ w ten sposób:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Następnie utwórz środowisko wirtualne i zainstaluj biblioteki:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Dla Windows użyj następujących poleceń, aby utworzyć i aktywować środowisko wirtualne:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Dodaj poniższy kod do pliku _app.py_:

   ```python
   import openai
   import os
   import requests
   from PIL import Image
   import dotenv

   # import dotenv
   dotenv.load_dotenv()

   # Get endpoint and key from environment variables
   openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
   openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

   # Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
   openai.api_version = '2023-06-01-preview'
   openai.api_type = 'azure'


   try:
       # Create an image by using the image generation API
       generation_response = openai.Image.create(
           prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
           size='1024x1024',
           n=2,
           temperature=0,
       )
       # Set the directory for the stored image
       image_dir = os.path.join(os.curdir, 'images')

       # If the directory doesn't exist, create it
       if not os.path.isdir(image_dir):
           os.mkdir(image_dir)

       # Initialize the image path (note the filetype should be png)
       image_path = os.path.join(image_dir, 'generated-image.png')

       # Retrieve the generated image
       image_url = generation_response["data"][0]["url"]  # extract image URL from response
       generated_image = requests.get(image_url).content  # download the image
       with open(image_path, "wb") as image_file:
           image_file.write(generated_image)

       # Display the image in the default image viewer
       image = Image.open(image_path)
       image.show()

   # catch exceptions
   except openai.InvalidRequestError as err:
       print(err)

   ```

Wyjaśnijmy ten kod:

- Najpierw importujemy potrzebne biblioteki, w tym OpenAI, dotenv, requests oraz Pillow.

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

- Potem ustawiamy endpoint, klucz do API OpenAI, wersję i typ.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Następnie generujemy obraz:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Powyższy kod zwraca obiekt JSON zawierający URL wygenerowanego obrazu. Możemy użyć tego URL, aby pobrać obraz i zapisać go do pliku.

- Na koniec otwieramy obraz i wyświetlamy go za pomocą standardowej przeglądarki obrazów:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Szczegóły dotyczące generowania obrazu

Przyjrzyjmy się dokładniej kodowi generującemu obraz:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** to tekstowy prompt używany do generowania obrazu. W tym przypadku jest to "Królik na koniu, trzymający lizaka, na mglistym łące, gdzie rosną żonkile".
- **size** to rozmiar generowanego obrazu. Tutaj generujemy obraz o wymiarach 1024x1024 pikseli.
- **n** to liczba generowanych obrazów. W tym przypadku generujemy dwa obrazy.
- **temperature** to parametr kontrolujący losowość wyjścia modelu Generatywnej AI. Temperatura to wartość od 0 do 1, gdzie 0 oznacza deterministyczne wyjście, a 1 – losowe. Domyślna wartość to 0.7.

W kolejnej sekcji omówimy więcej możliwości pracy z obrazami.

## Dodatkowe możliwości generowania obrazów

Jak widzieliśmy, udało się wygenerować obraz za pomocą kilku linijek kodu w Pythonie. Jednak możliwości jest znacznie więcej.

Możesz także:

- **Wykonywać edycje**. Dostarczając istniejący obraz, maskę i prompt, możesz zmienić obraz. Na przykład możesz dodać coś do części obrazu. Wyobraź sobie nasz obraz królika – możesz dodać mu kapelusz. Robisz to, podając obraz, maskę (wskazującą obszar do zmiany) oraz tekstowy prompt opisujący, co ma zostać zrobione.

  ```python
  response = openai.Image.create_edit(
    image=open("base_image.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="An image of a rabbit with a hat on its head.",
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  Obraz bazowy zawierałby tylko królika, a końcowy obraz miałby kapelusz na króliku.

- **Tworzyć wariacje**. Polega to na tym, że bierzesz istniejący obraz i prosisz o stworzenie wariacji. Aby to zrobić, podajesz obraz i prompt tekstowy oraz kod w ten sposób:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Uwaga, ta funkcja jest dostępna tylko w OpenAI

## Temperatura

Temperatura to parametr kontrolujący losowość wyjścia modelu Generatywnej AI. Wartość temperatury mieści się w przedziale od 0 do 1, gdzie 0 oznacza wyjście deterministyczne, a 1 – losowe. Domyślnie jest ustawiona na 0.7.

Spójrzmy na przykład działania temperatury, uruchamiając ten sam prompt dwukrotnie:

> Prompt: "Królik na koniu, trzymający lizaka, na mglistym łące, gdzie rosną żonkile"

![Królik na koniu trzymający lizaka, wersja 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.pl.png)

Teraz uruchommy ten sam prompt jeszcze raz, aby zobaczyć, że nie otrzymamy dokładnie tego samego obrazu:

![Wygenerowany obraz królika na koniu](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.pl.png)

Jak widać, obrazy są podobne, ale nie identyczne. Spróbujmy zmienić wartość temperatury na 0.1 i zobaczyć, co się stanie:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Zmiana temperatury

Spróbujmy więc uczynić odpowiedź bardziej deterministyczną. Z dwóch wygenerowanych obrazów widzimy, że na pierwszym jest królik, a na drugim koń, więc obrazy znacznie się różnią.

Zmieńmy więc nasz kod i ustawmy temperaturę na 0, tak:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Po uruchomieniu tego kodu otrzymasz te dwa obrazy:

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.pl.png)
- ![Temperatura 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.pl.png)

Tutaj wyraźnie widać, że obrazy są do siebie bardziej podobne.

## Jak definiować granice działania aplikacji za pomocą metapromptów

W naszej demonstracji możemy już generować obrazy dla klientów. Jednak musimy ustalić pewne granice działania aplikacji.

Na przykład, nie chcemy generować obrazów nieodpowiednich do pracy (NSFW) lub nieodpowiednich dla dzieci.

Możemy to zrobić za pomocą _metapromptów_. Metaprompt to tekstowy prompt używany do kontrolowania wyjścia modelu Generatywnej AI. Na przykład, możemy użyć metapromptów, aby zapewnić, że generowane obrazy są bezpieczne do pracy lub odpowiednie dla dzieci.

### Jak to działa?

Jak działają metaprompt?

Metaprompt to tekstowy prompt, który kontroluje wyjście modelu Generatywnej AI. Umieszcza się go przed właściwym promptem i służy do kontrolowania wyjścia modelu. Metaprompt jest osadzany w aplikacjach, aby kontrolować wyjście modelu, łącząc prompt i metaprompt w jeden tekstowy prompt.

Przykładem metaprompt może być następujący:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Zobaczmy teraz, jak możemy użyć metapromptów w naszej demonstracji.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt =f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"{meta_prompt}
Create an image of a bunny on a horse, holding a lollipop"

# TODO add request to generate image
```

Z powyższego promptu widać, że wszystkie generowane obrazy uwzględniają metaprompt.

## Zadanie – umożliwmy uczniom tworzenie obrazów

Przedstawiliśmy Edu4All na początku tej lekcji. Teraz czas umożliwić uczniom generowanie obrazów do ich zadań.

Uczniowie stworzą obrazy do swoich zadań zawierające zabytki – jakie dokładnie zabytki, to już ich wybór. Zadaniem uczniów jest wykorzystanie kreatywności, aby umieścić te zabytki w różnych kontekstach.

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

# Get endpoint and key from environment variables
openai.api_base = "<replace with endpoint>"
openai.api_key = "<replace with api key>"

# Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
openai.api_version = '2023-06-01-preview'
openai.api_type = 'azure'

disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}"""

prompt = f"""{meta_prompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = openai.Image.create(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response["data"][0]["url"]  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.InvalidRequestError as err:
    print(err)
```

## Świetna robota! Kontynuuj naukę

Po ukończeniu tej lekcji sprawdź naszą [kolekcję materiałów do nauki Generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę!

Przejdź do Lekcji 10, gdzie omówimy, jak [tworzyć aplikacje AI z użyciem low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.