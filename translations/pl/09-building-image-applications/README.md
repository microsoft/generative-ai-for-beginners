<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:42:01+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "pl"
}
-->
# Tworzenie aplikacji do generowania obrazów

[![Tworzenie aplikacji do generowania obrazów](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.pl.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Generowanie tekstu to nie jedyna funkcja LLM-ów. Możliwe jest również generowanie obrazów na podstawie opisów tekstowych. Obrazy jako modalność mogą być niezwykle przydatne w wielu dziedzinach, takich jak MedTech, architektura, turystyka, tworzenie gier i wiele innych. W tym rozdziale przyjrzymy się dwóm najpopularniejszym modelom generowania obrazów: DALL-E i Midjourney.

## Wprowadzenie

W tej lekcji omówimy:

- Generowanie obrazów i dlaczego jest przydatne.
- DALL-E i Midjourney: czym są i jak działają.
- Jak zbudować aplikację do generowania obrazów.

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Zbudować aplikację do generowania obrazów.
- Określić granice dla swojej aplikacji za pomocą meta promptów.
- Pracować z DALL-E i Midjourney.

## Dlaczego warto zbudować aplikację do generowania obrazów?

Aplikacje do generowania obrazów to świetny sposób na eksplorowanie możliwości generatywnej AI. Mogą być używane na przykład do:

- **Edycji i syntezy obrazów**. Możesz generować obrazy dla różnych zastosowań, takich jak edycja i synteza obrazów.

- **Zastosowania w różnych branżach**. Mogą być również używane do generowania obrazów dla różnych branż, takich jak MedTech, turystyka, tworzenie gier i wiele innych.

## Scenariusz: Edu4All

W ramach tej lekcji będziemy kontynuować pracę z naszym startupem Edu4All. Studenci będą tworzyć obrazy do swoich ocen. Jakie obrazy stworzą, zależy od nich, ale mogą to być ilustracje do ich własnej bajki, stworzenie nowej postaci do ich opowieści lub pomoc w wizualizacji ich pomysłów i koncepcji.

Oto przykład, co studenci Edu4All mogliby wygenerować, jeśli pracują w klasie nad zabytkami:

![Startup Edu4All, klasa o zabytkach, Wieża Eiffla](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.pl.png)

używając promptu takiego jak:

> "Pies obok Wieży Eiffla w porannym świetle słonecznym"

## Czym są DALL-E i Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) i [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) to dwa z najpopularniejszych modeli generowania obrazów, które pozwalają na użycie promptów do generowania obrazów.

### DALL-E

Zacznijmy od DALL-E, który jest modelem generatywnej AI generującym obrazy na podstawie opisów tekstowych.

> [DALL-E to połączenie dwóch modeli, CLIP i rozproszonej uwagi](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** to model generujący osadzenia, czyli numeryczne reprezentacje danych, z obrazów i tekstu.

- **Rozproszona uwaga** to model generujący obrazy z osadzeń. DALL-E jest trenowany na zbiorze danych obrazów i tekstów i może być używany do generowania obrazów na podstawie opisów tekstowych. Na przykład DALL-E może być używany do generowania obrazów kota w kapeluszu lub psa z irokezem.

### Midjourney

Midjourney działa podobnie do DALL-E, generując obrazy na podstawie promptów tekstowych. Midjourney może być również używany do generowania obrazów za pomocą promptów takich jak „kot w kapeluszu” lub „pies z irokezem”.

![Obraz wygenerowany przez Midjourney, mechaniczny gołąb](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Kredyt: Wikipedia, obraz wygenerowany przez Midjourney_

## Jak działają DALL-E i Midjourney

Najpierw [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E to model generatywnej AI oparty na architekturze transformera z _autoregresywnym transformerem_.

_Autoregresywny transformer_ definiuje, jak model generuje obrazy na podstawie opisów tekstowych, generując jeden piksel na raz, a następnie używając wygenerowanych pikseli do generowania kolejnego piksela. Proces ten przechodzi przez wiele warstw w sieci neuronowej, aż obraz zostanie ukończony.

Dzięki temu procesowi DALL-E kontroluje atrybuty, obiekty, cechy i inne elementy w generowanym obrazie. Jednak DALL-E 2 i 3 mają większą kontrolę nad generowanym obrazem.

## Tworzenie pierwszej aplikacji do generowania obrazów

Co jest potrzebne do stworzenia aplikacji do generowania obrazów? Potrzebujesz następujących bibliotek:

- **python-dotenv** – zaleca się użycie tej biblioteki do przechowywania tajnych danych w pliku _.env_ z dala od kodu.
- **openai** – biblioteka, której użyjesz do interakcji z API OpenAI.
- **pillow** – do pracy z obrazami w Pythonie.
- **requests** – do wykonywania żądań HTTP.

## Tworzenie i wdrażanie modelu Azure OpenAI

Jeśli jeszcze tego nie zrobiłeś, postępuj zgodnie z instrukcjami na stronie [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal), aby utworzyć zasób i model Azure OpenAI. Wybierz model DALL-E 3.

## Tworzenie aplikacji

1. Utwórz plik _.env_ z następującą zawartością:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Znajdź te informacje w portalu Azure OpenAI Foundry dla swojego zasobu w sekcji „Deployments”.

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

   Dla systemu Windows użyj następujących poleceń, aby utworzyć i aktywować wirtualne środowisko:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Dodaj następujący kod do pliku _app.py_:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # configure Azure OpenAI service client 
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
    try:
        # Create an image by using the image generation API
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Set the directory for the stored image
        image_dir = os.path.join(os.curdir, 'images')

        # If the directory doesn't exist, create it
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Initialize the image path (note the filetype should be png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Retrieve the generated image
        image_url = generation_response.data[0].url  # extract image URL from response
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

- Potem konfigurujemy klienta usługi Azure OpenAI.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Następnie generujemy obraz:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Powyższy kod odpowiada obiektem JSON zawierającym URL wygenerowanego obrazu. Możemy użyć tego URL-a do pobrania obrazu i zapisania go w pliku.

- Na końcu otwieramy obraz i używamy standardowego przeglądarki obrazów do jego wyświetlenia:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Szczegóły dotyczące generowania obrazu

Przyjrzyjmy się bliżej kodowi generującemu obraz:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** – tekstowy prompt używany do generowania obrazu. W tym przypadku używamy promptu „Królik na koniu, trzymający lizaka, na mglistym łące, gdzie rosną żonkile”.
- **size** – rozmiar generowanego obrazu. W tym przypadku generujemy obraz o rozmiarze 1024x1024 pikseli.
- **n** – liczba generowanych obrazów. W tym przypadku generujemy dwa obrazy.
- **temperature** – parametr kontrolujący losowość wyników modelu generatywnej AI. Temperatura to wartość między 0 a 1, gdzie 0 oznacza, że wynik jest deterministyczny, a 1 oznacza, że wynik jest losowy. Domyślna wartość to 0.7.

Istnieje więcej rzeczy, które można zrobić z obrazami, o czym opowiemy w następnej sekcji.

## Dodatkowe możliwości generowania obrazów

Jak dotąd widziałeś, jak można wygenerować obraz za pomocą kilku linijek kodu w Pythonie. Jednak istnieje więcej rzeczy, które można zrobić z obrazami.

Możesz również:

- **Wykonywać edycje**. Podając istniejący obraz, maskę i prompt, możesz zmieniać obraz. Na przykład możesz dodać coś do części obrazu. Wyobraź sobie nasz obraz królika – możesz dodać kapelusz królikowi. Jak to zrobić? Podając obraz, maskę (identyfikującą część obszaru do zmiany) i tekstowy prompt określający, co należy zrobić. 
> Uwaga: to nie jest obsługiwane w DALL-E 3.

Oto przykład użycia GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Obraz bazowy zawierałby tylko salon z basenem, ale ostateczny obraz miałby flaminga:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.pl.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.pl.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.pl.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Tworzyć wariacje**. Idea polega na tym, że bierzesz istniejący obraz i prosisz o stworzenie jego wariacji. Aby stworzyć wariację, podajesz obraz i tekstowy prompt oraz kod, jak poniżej:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Uwaga: to jest obsługiwane tylko w OpenAI.

## Temperatura

Temperatura to parametr kontrolujący losowość wyników modelu generatywnej AI. Temperatura to wartość między 0 a 1, gdzie 0 oznacza, że wynik jest deterministyczny, a 1 oznacza, że wynik jest losowy. Domyślna wartość to 0.7.

Przyjrzyjmy się przykładowi działania temperatury, uruchamiając ten prompt dwa razy:

> Prompt: „Królik na koniu, trzymający lizaka, na mglistym łące, gdzie rosną żonkile”

![Królik na koniu trzymający lizaka, wersja 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.pl.png)

Teraz uruchommy ten sam prompt, aby zobaczyć, że nie otrzymamy dwa razy tego samego obrazu:

![Wygenerowany obraz królika na koniu](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.pl.png)

Jak widać, obrazy są podobne, ale nie identyczne. Spróbujmy zmienić wartość temperatury na 0.1 i zobaczmy, co się stanie:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Zmiana temperatury

Spróbujmy więc uczynić odpowiedź bardziej deterministyczną. Możemy zauważyć, że w dwóch wygenerowanych obrazach w pierwszym jest królik, a w drugim koń, więc obrazy znacznie się różnią.

Zmieńmy więc nasz kod i ustawmy temperaturę na 0, jak poniżej:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Teraz, gdy uruchomisz ten kod, otrzymasz te dwa obrazy:

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.pl.png)
- ![Temperatura 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.pl.png)

Tutaj wyraźnie widać, że obrazy bardziej się do siebie upodabniają.

## Jak określić granice dla swojej aplikacji za pomocą meta promptów

Dzięki naszemu demo możemy już generować obrazy dla naszych klientów. Jednak musimy stworzyć pewne granice dla naszej aplikacji.

Na przykład nie chcemy generować obrazów, które nie są odpowiednie dla pracy lub które nie są odpowiednie dla dzieci.

Możemy to zrobić za pomocą _meta promptów_. Meta prompty to tekstowe prompty używane do kontrolowania wyników modelu generatywnej AI. Na przykład możemy użyć meta promptów do kontrolowania wyników i zapewnienia, że generowane obrazy są odpowiednie dla pracy lub dzieci.

### Jak to działa?

Jak działają meta prompty?

Meta prompty to tekstowe prompty używane do kontrolowania wyników modelu generatywnej AI. Są umieszczane przed promptem tekstowym i służą do kontrolowania wyników modelu oraz są wbudowane w aplikacje w celu kontrolowania wyników modelu. Łączą dane wejściowe promptu i meta promptu w jednym tekście promptu.

Przykład meta promptu może wyglądać następująco:

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

Z powyższego promptu widać, jak wszystkie tworzone obrazy uwzględniają meta prompt.

## Zadanie – umożliwienie studentom działania

Na początku tej lekcji wprowadziliśmy Edu4All. Teraz nadszedł czas, aby umożliwić studentom generowanie obrazów do ich ocen.

Studenci będą tworzyć obrazy do swoich ocen zawierających zabytki. Jakie zabytki wybiorą, zależy od nich. Studenci są proszeni o wykorzystanie swojej kreatywności w tym zadaniu, aby umieścić te zabytki w różnych kontekstach.

## Rozwiązanie

Oto jedno z możliwych rozwiązań:
```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-02-01"
  )


disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"""{meta_prompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = client.images.generate(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=1,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response.data[0].url  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.BadRequestError as err:
    print(err)
```

## Świetna robota! Kontynuuj naukę

Po ukończeniu tej lekcji, zajrzyj do naszej [kolekcji nauki o generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę na temat generatywnej AI!

Przejdź do Lekcji 10, gdzie dowiemy się, jak [tworzyć aplikacje AI za pomocą narzędzi low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.