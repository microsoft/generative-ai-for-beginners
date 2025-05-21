<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T10:29:20+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "pl"
}
-->
# Budowanie aplikacji do generowania obrazów

Istnieje więcej możliwości LLM niż tylko generowanie tekstu. Możliwe jest także generowanie obrazów na podstawie opisów tekstowych. Posiadanie obrazów jako modalności może być niezwykle przydatne w wielu dziedzinach, takich jak MedTech, architektura, turystyka, rozwój gier i inne. W tym rozdziale przyjrzymy się dwóm najpopularniejszym modelom generowania obrazów, DALL-E i Midjourney.

## Wprowadzenie

W tej lekcji omówimy:

- Generowanie obrazów i dlaczego jest przydatne.
- DALL-E i Midjourney, czym są i jak działają.
- Jak zbudować aplikację do generowania obrazów.

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Zbudować aplikację do generowania obrazów.
- Określić granice dla swojej aplikacji za pomocą meta promptów.
- Pracować z DALL-E i Midjourney.

## Dlaczego budować aplikację do generowania obrazów?

Aplikacje do generowania obrazów to świetny sposób na eksplorację możliwości Generative AI. Mogą być używane na przykład do:

- **Edycji i syntezy obrazów**. Możesz generować obrazy dla różnych zastosowań, takich jak edycja obrazów i synteza obrazów.

- **Zastosowanie w różnych branżach**. Mogą być również używane do generowania obrazów dla różnych branż, takich jak Medtech, turystyka, rozwój gier i inne.

## Scenariusz: Edu4All

W ramach tej lekcji będziemy kontynuować pracę z naszym startupem, Edu4All. Studenci będą tworzyć obrazy do swoich ocen, dokładnie jakie obrazy, zależy od nich, ale mogą to być ilustracje do ich własnej bajki, stworzenie nowej postaci do swojej opowieści lub pomoc w wizualizacji ich pomysłów i koncepcji.

Oto, co studenci Edu4All mogliby wygenerować, na przykład, gdy pracują na zajęciach nad zabytkami:

przy użyciu promptu takiego jak

> "Pies obok Wieży Eiffla w porannym świetle"

## Czym są DALL-E i Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) i [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) to dwa z najpopularniejszych modeli generowania obrazów, które pozwalają na użycie promptów do generowania obrazów.

### DALL-E

Zacznijmy od DALL-E, który jest modelem Generative AI generującym obrazy na podstawie opisów tekstowych.

- **CLIP**, to model generujący osadzenia, które są numerycznymi reprezentacjami danych, z obrazów i tekstu.

- **Rozproszona uwaga**, to model generujący obrazy z osadzeń. DALL-E jest szkolony na zbiorze danych z obrazami i tekstem i może być używany do generowania obrazów z opisów tekstowych. Na przykład, DALL-E może być używany do generowania obrazów kota w kapeluszu lub psa z irokezem.

### Midjourney

Midjourney działa podobnie do DALL-E, generuje obrazy z tekstowych promptów. Midjourney może być również używany do generowania obrazów przy użyciu promptów takich jak „kot w kapeluszu” lub „pies z irokezem”.

## Jak działają DALL-E i Midjourney

Najpierw [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E to model Generative AI oparty na architekturze transformera z _autoregresyjnym transformerem_.

_Autoregresyjny transformer_ definiuje, jak model generuje obrazy z opisów tekstowych, generując jeden piksel na raz, a następnie używa wygenerowanych pikseli do generowania kolejnego piksela. Przechodzi przez wiele warstw w sieci neuronowej, aż obraz jest kompletny.

Dzięki temu procesowi DALL-E kontroluje atrybuty, obiekty, cechy i inne w generowanym obrazie. Jednak DALL-E 2 i 3 mają większą kontrolę nad generowanym obrazem.

## Budowanie pierwszej aplikacji do generowania obrazów

Co jest potrzebne, aby zbudować aplikację do generowania obrazów? Potrzebujesz następujących bibliotek:

- **python-dotenv**, zaleca się użycie tej biblioteki do przechowywania tajnych danych w pliku _.env_ z dala od kodu.
- **openai**, ta biblioteka jest tym, czego użyjesz do interakcji z OpenAI API.
- **pillow**, do pracy z obrazami w Pythonie.
- **requests**, aby pomóc w wykonywaniu żądań HTTP.

1. Utwórz plik _.env_ z następującą zawartością:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Znajdź te informacje w Azure Portal dla swojego zasobu w sekcji "Keys and Endpoint".

1. Zbierz powyższe biblioteki w pliku _requirements.txt_ w następujący sposób:

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

   Dla Windows, użyj następujących poleceń, aby utworzyć i aktywować wirtualne środowisko:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Dodaj następujący kod w pliku _app.py_:

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

- Po tym ustawiamy endpoint, klucz dla OpenAI API, wersję i typ.

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

  Powyższy kod odpowiada obiektem JSON, który zawiera URL wygenerowanego obrazu. Możemy użyć URL, aby pobrać obraz i zapisać go do pliku.

- Na koniec otwieramy obraz i używamy standardowego przeglądarki obrazów, aby go wyświetlić:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Więcej szczegółów na temat generowania obrazu

Przyjrzyjmy się kodowi, który generuje obraz w większych szczegółach:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, to tekstowy prompt używany do generowania obrazu. W tym przypadku używamy promptu "Królik na koniu, trzymający lizaka, na mglistym polu, gdzie rosną żonkile".
- **size**, to rozmiar generowanego obrazu. W tym przypadku generujemy obraz o wymiarach 1024x1024 pikseli.
- **n**, to liczba generowanych obrazów. W tym przypadku generujemy dwa obrazy.
- **temperature**, to parametr kontrolujący losowość wyniku modelu Generative AI. Temperatura to wartość między 0 a 1, gdzie 0 oznacza, że wynik jest deterministyczny, a 1 oznacza, że wynik jest losowy. Domyślna wartość to 0.7.

Jest więcej rzeczy, które możesz zrobić z obrazami, które omówimy w następnej sekcji.

## Dodatkowe możliwości generowania obrazów

Jak dotąd widziałeś, jak udało nam się wygenerować obraz za pomocą kilku linii kodu w Pythonie. Jednak istnieje więcej rzeczy, które można zrobić z obrazami.

Możesz również wykonać następujące czynności:

- **Wykonywanie edycji**. Dostarczając istniejący obraz, maskę i prompt, możesz zmienić obraz. Na przykład możesz dodać coś do części obrazu. Wyobraź sobie nasz obraz królika, możesz dodać kapelusz na królika. Jak to zrobić, to dostarczenie obrazu, maski (identyfikującej część obszaru do zmiany) i tekstowego promptu, aby powiedzieć, co należy zrobić.

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

  Podstawowy obraz zawierałby tylko królika, ale ostateczny obraz miałby kapelusz na królika.

- **Tworzenie wariacji**. Idea polega na tym, że bierzesz istniejący obraz i prosisz o stworzenie wariacji. Aby stworzyć wariację, dostarczasz obraz i tekstowy prompt oraz kod, jak poniżej:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Uwaga, jest to obsługiwane tylko na OpenAI

## Temperatura

Temperatura to parametr kontrolujący losowość wyniku modelu Generative AI. Temperatura to wartość między 0 a 1, gdzie 0 oznacza, że wynik jest deterministyczny, a 1 oznacza, że wynik jest losowy. Domyślna wartość to 0.7.

Przyjrzyjmy się przykładzie działania temperatury, uruchamiając ten prompt dwa razy:

> Prompt : "Królik na koniu, trzymający lizaka, na mglistym polu, gdzie rosną żonkile"

Teraz uruchommy ten sam prompt, aby zobaczyć, że nie otrzymamy dwa razy tego samego obrazu:

Jak widać, obrazy są podobne, ale nie takie same. Spróbujmy zmienić wartość temperatury na 0.1 i zobaczyć, co się stanie:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Zmiana temperatury

Spróbujmy więc, aby odpowiedź była bardziej deterministyczna. Mogliśmy zaobserwować z dwóch wygenerowanych obrazów, że na pierwszym obrazie jest królik, a na drugim koniu, więc obrazy znacznie się różnią.

Zmieńmy więc nasz kod i ustawmy temperaturę na 0, jak poniżej:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Teraz, gdy uruchomisz ten kod, otrzymasz te dwa obrazy:

Tutaj wyraźnie widać, jak obrazy bardziej się do siebie upodabniają.

## Jak zdefiniować granice dla swojej aplikacji za pomocą metapromptów

Dzięki naszemu demo możemy już generować obrazy dla naszych klientów. Musimy jednak stworzyć pewne granice dla naszej aplikacji.

Na przykład nie chcemy generować obrazów, które nie są odpowiednie do pracy, ani nieodpowiednie dla dzieci.

Możemy to zrobić za pomocą _metapromptów_. Metaprompty to tekstowe prompty używane do kontrolowania wyniku modelu Generative AI. Na przykład, możemy użyć metapromptów do kontrolowania wyniku i zapewnienia, że generowane obrazy są odpowiednie do pracy lub odpowiednie dla dzieci.

### Jak to działa?

Jak działają meta prompty?

Meta prompty to tekstowe prompty używane do kontrolowania wyniku modelu Generative AI, są umieszczane przed promptem tekstowym i służą do kontrolowania wyniku modelu oraz osadzane w aplikacjach w celu kontrolowania wyniku modelu. Enkapsulują wejście promptu i wejście meta promptu w jednym promptu tekstowym.

Jednym z przykładów meta promptu byłby następujący:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Teraz zobaczmy, jak możemy użyć meta promptów w naszym demo.

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

Z powyższego promptu można zobaczyć, jak wszystkie tworzone obrazy uwzględniają metaprompt.

## Zadanie - umożliwmy studentom

Na początku tej lekcji przedstawiliśmy Edu4All. Teraz nadszedł czas, aby umożliwić studentom generowanie obrazów do ich ocen.

Studenci będą tworzyć obrazy do swoich ocen zawierające zabytki, dokładnie jakie zabytki, zależy od studentów. Studenci są proszeni o wykorzystanie swojej kreatywności w tym zadaniu, aby umieścić te zabytki w różnych kontekstach.

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

prompt = f"""{metaprompt}
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

Po ukończeniu tej lekcji sprawdź naszą [kolekcję nauki o Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby kontynuować pogłębianie wiedzy o Generative AI!

Przejdź do Lekcji 10, gdzie przyjrzymy się, jak [budować aplikacje AI z użyciem niskiego kodu](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się o dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zalecane jest profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.