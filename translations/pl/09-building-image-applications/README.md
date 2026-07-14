# Budowanie aplikacji generujących obrazy

[![Budowanie aplikacji generujących obrazy](../../../translated_images/pl/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLM to nie tylko generowanie tekstu. Możliwe jest także generowanie obrazów na podstawie opisów tekstowych. Posiadanie obrazów jako modalności może być bardzo przydatne w wielu obszarach, od MedTech, architektury, turystyki, tworzenia gier i nie tylko. W tym rozdziale przyjrzymy się dwóm najpopularniejszym modelom generowania obrazów, DALL-E i Midjourney.

## Wprowadzenie

W tej lekcji omówimy:

- Generowanie obrazów i dlaczego jest to przydatne.
- Co to jest DALL-E i Midjourney oraz jak działają.
- Jak zbudować aplikację do generowania obrazów.

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

- Zbudować aplikację do generowania obrazów.
- Określić granice swojej aplikacji za pomocą meta-promptów.
- Pracować z DALL-E i Midjourney.

## Dlaczego budować aplikację do generowania obrazów?

Aplikacje generujące obrazy to świetny sposób na eksplorację możliwości generatywnej sztucznej inteligencji. Można je wykorzystać na przykład do:

- **Edycji i syntezy obrazów**. Możesz generować obrazy dla różnych zastosowań, takich jak edycja obrazów czy ich synteza.

- **Zastosowań w różnych branżach**. Można je również używać do generowania obrazów dla różnych sektorów jak medycyna, turystyka, tworzenie gier i inne.

## Scenariusz: Edu4All

W ramach tej lekcji kontynuujemy pracę z naszym startupem Edu4All. Studenci stworzą obrazy na swoje zadania; jakie to obrazy, zależy od nich, mogą to być ilustracje do własnej bajki, nowa postać do historii lub pomoc w wizualizacji ich pomysłów i koncepcji.

Oto przykładowe obrazy, które mogliby wygenerować uczniowie Edu4All, jeśli pracują w klasie nad zabytkami:

![Startup Edu4All, klasa o zabytkach, Wieża Eiffla](../../../translated_images/pl/startup.94d6b79cc4bb3f5a.webp)

używając promptu takiego jak

> "Pies obok Wieży Eiffla w porannym słońcu"

## Co to są DALL-E i Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) i [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) to dwa z najpopularniejszych modeli generowania obrazów, które pozwalają na generowanie obrazów na podstawie promptów.

### DALL-E

Zacznijmy od DALL-E, modelu generatywnej AI, który generuje obrazy z opisów tekstowych.

> [DALL-E to połączenie dwóch modeli, CLIP oraz diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** to model, który generuje osadzanie (embeddings), czyli numeryczne reprezentacje danych, z obrazów i tekstów.

- **Diffused attention** to model generujący obrazy na podstawie osadzeń. DALL-E jest trenowany na zbiorze danych obrazów i tekstów i może generować obrazy na bazie opisów tekstowych. Na przykład, DALL-E może generować obrazy kota w kapeluszu albo psa z irokezem.

### Midjourney

Midjourney działa podobnie do DALL-E, generuje obrazy na podstawie tekstowych promptów. Midjourney również może generować obrazy na podstawie promptów typu „kot w kapeluszu” lub „pies z irokezem”.

![Obraz wygenerowany przez Midjourney, mechaniczny gołąb](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Źródło: Wikipedia, obraz wygenerowany przez Midjourney_

## Jak działają DALL-E i Midjourney

Na początek [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E to model generatywnej AI oparty na architekturze transformera z _autoregresyjnym transformerem_.

_Autoregresyjny transformer_ określa sposób generowania obrazów z opisów tekstowych przez model, generuje pojedynczy piksel na raz, a następnie używa wygenerowanych pikseli do wygenerowania kolejnego piksela. Przechodzi przez wiele warstw sieci neuronowej, aż obraz zostanie ukończony.

Dzięki temu procesowi DALL-E kontroluje atrybuty, obiekty, cechy i wiele innych w generowanym obrazie. Jednak DALL-E 2 i 3 mają większą kontrolę nad generowanym obrazem.

## Budowanie pierwszej aplikacji generującej obrazy

Co jest potrzebne do zbudowania aplikacji generującej obrazy? Potrzebujesz następujących bibliotek:

- **python-dotenv** – zaleca się korzystanie z tej biblioteki, aby przechowywać swoje sekrety w pliku _.env_ z dala od kodu.
- **openai** – tej biblioteki użyjesz do interakcji z API OpenAI.
- **pillow** – do pracy z obrazami w Pythonie.
- **requests** – aby pomagać w wykonywaniu żądań HTTP.

## Utwórz i wdroż model Azure OpenAI

Jeśli jeszcze tego nie zrobiłeś, postępuj zgodnie z instrukcjami na stronie [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst),
aby utworzyć zasób i model Azure OpenAI. Wybierz model **gpt-image-1** (aktualny model generacji obrazów Azure OpenAI; DALL-E 3 jest przestarzały i nie jest już dostępny dla nowych wdrożeń).

## Utwórz aplikację

1. Utwórz plik _.env_ z następującą zawartością:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Znajdź te informacje na portalu Azure OpenAI Foundry dla swojego zasobu w sekcji "Deployments".

1. Zbierz powyższe biblioteki w pliku o nazwie _requirements.txt_ w następujący sposób:

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

   Dla Windows użyj następujących poleceń do utworzenia i aktywacji środowiska wirtualnego:

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
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # Skonfiguruj klienta usługi Azure OpenAI
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # Utwórz obraz za pomocą API do generowania obrazów
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Ustaw katalog dla zapisanego obrazu
        image_dir = os.path.join(os.curdir, 'images')

        # Jeśli katalog nie istnieje, utwórz go
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Zainicjalizuj ścieżkę do obrazu (uwaga, rozszerzenie pliku powinno być png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Pobierz wygenerowany obraz
        image_url = generation_response.data[0].url  # wyodrębnij URL obrazu z odpowiedzi
        generated_image = requests.get(image_url).content  # pobierz obraz
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # Wyświetl obraz w domyślnym przeglądarce obrazów
        image = Image.open(image_path)
        image.show()

    # przechwyć wyjątki
    except openai.BadRequestError as err:
        print(err)
   ```

Wyjaśnijmy ten kod:

- Najpierw importujemy potrzebne biblioteki, w tym bibliotekę OpenAI, bibliotekę dotenv, bibliotekę requests oraz bibliotekę Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Następnie ładujemy zmienne środowiskowe z pliku _.env_.

  ```python
  # importuj dotenv
  dotenv.load_dotenv()
  ```

- Po tym konfigurujemy klienta usługi Azure OpenAI 

  ```python
  # Pobierz punkt końcowy i klucz z zmiennych środowiskowych
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- Następnie generujemy obraz:

  ```python
  # Utwórz obraz za pomocą interfejsu API generowania obrazów
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

Kod powyżej odpowiada obiektem JSON, który zawiera URL wygenerowanego obrazu. Możemy użyć tego URL, aby pobrać obraz i zapisać go do pliku.

- Na końcu otwieramy obraz i używamy standardowej przeglądarki obrazów, aby go wyświetlić:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Więcej szczegółów na temat generowania obrazu

Przyjrzyjmy się dokładniej kodowi, który generuje obraz:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, to tekstowa wskazówka używana do generowania obrazu. W tym przypadku używamy promptu "Zajączek na koniu, trzymający lizaka, na mglistym łące, gdzie rosną żonkile".
- **size**, to rozmiar generowanego obrazu. W tym przypadku generujemy obraz o wymiarach 1024x1024 pikseli.
- **n**, to liczba generowanych obrazów. W tym przypadku generujemy dwa obrazy.
- **temperature**, to parametr kontrolujący losowość wyniku modelu Generative AI. Temperatura ma wartość między 0 a 1, gdzie 0 oznacza, że wynik jest deterministyczny, a 1 oznacza, że wynik jest losowy. Domyślna wartość to 0.7.

Istnieje więcej rzeczy, które możesz zrobić z obrazami, o czym dowiesz się w następnej sekcji.

## Dodatkowe możliwości generowania obrazów

Jak widziałeś do tej pory, mogliśmy wygenerować obraz za pomocą kilku linii w Pythonie. Jednak istnieją też inne możliwości pracy z obrazami.

Możesz także:

- **Wykonywać edycje**. Podając istniejący obraz, maskę i prompt, możesz zmienić obraz. Na przykład możesz dodać coś do części obrazu. Wyobraź sobie nasz obraz z zajączkiem, możesz dodać mu kapelusz. Robisz to, podając obraz, maskę (oznaczającą część, która ma zostać zmieniona) oraz tekstową wskazówkę, co powinno zostać zrobione. 
> Uwaga: nie jest to obsługiwane w DALL-E 3. 
 
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

  Bazowy obraz zawierałby tylko salon z basenem, ale końcowy obraz miałby flaminga:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/pl/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/pl/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/pl/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Tworzyć wariacje**. Chodzi o to, że bierzemy istniejący obraz i prosimy o utworzenie wariantów. Aby stworzyć wariację, dostarczasz obraz i tekstową wskazówkę i kod jak poniżej:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > Uwaga, jest to obsługiwane tylko w modelu OpenAI DALL-E 2, a nie w gpt-image-1

## Temperatura

Temperatura to parametr kontrolujący losowość wyniku modelu Generative AI. Temperatura ma wartość od 0 do 1, gdzie 0 oznacza wynik deterministyczny, a 1 oznacza wynik losowy. Domyślną wartością jest 0.7.

Przyjrzyjmy się przykładzie działania temperatury, wykonując ten prompt dwukrotnie:

> Prompt : "Zajączek na koniu, trzymający lizaka, na mglistym łące, gdzie rosną żonkile"

![Bunny on a horse holding a lollipop, version 1](../../../translated_images/pl/v1-generated-image.a295cfcffa3c13c2.webp)

Teraz uruchommy ten sam prompt jeszcze raz, aby zobaczyć, że nie otrzymamy takiego samego obrazu dwa razy:

![Generated image of bunny on horse](../../../translated_images/pl/v2-generated-image.33f55a3714efe61d.webp)

Jak widzisz, obrazy są podobne, ale nie identyczne. Spróbujmy zmienić wartość temperatury na 0.1 i zobaczyć, co się stanie:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Wprowadź tutaj tekst swojego promptu
        size='1024x1024',
        n=2
    )
```

### Zmiana temperatury

Spróbujmy więc uczynić odpowiedź bardziej deterministyczną. Możemy zauważyć na podstawie dwóch wygenerowanych obrazów, że na pierwszym jest zajączek, a na drugim koń, więc obrazy różnią się znacznie.

Zmieńmy więc nasz kod i ustawmy temperaturę na 0, w ten sposób:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Wprowadź tutaj tekst swojego promptu
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Teraz, gdy uruchomisz ten kod, otrzymasz te dwa obrazy:

- ![Temperature 0, v1](../../../translated_images/pl/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Temperature 0 , v2](../../../translated_images/pl/v2-temp-generated-image.871d0c920dbfb0f1.webp)

Tutaj wyraźnie widać, że obrazy bardziej do siebie podobają.

## Jak zdefiniować granice dla Twojej aplikacji za pomocą metapromptów

W naszym demo już możemy generować obrazy dla naszych klientów. Jednak musimy stworzyć pewne granice dla naszej aplikacji.

Na przykład, nie chcemy generować obrazów nieodpowiednich do pracy (NSFW) lub nieodpowiednich dla dzieci.

Możemy to zrobić za pomocą _metapromptów_. Metaprompt to tekstowa wskazówka służąca do kontrolowania wyniku modelu Generative AI. Możemy użyć metapromptów, aby kontrolować wynik i zapewnić, że generowane obrazy są bezpieczne do pracy lub odpowiednie dla dzieci.

### Jak to działa?

Jak więc działają metaprompt?

Metaprompt to tekstowe wskazówki używane do kontrolowania wyniku modelu Generative AI, umieszczane przed właściwym promptem i służące do kontrolowania wyniku modelu oraz wbudowywane w aplikacje, aby kontrolować wynik modelu. Metaprompt i prompt wejściowy są połączone w jeden tekstowy prompt.

Przykładem metapromptu może być następujący tekst:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Zobaczmy teraz, jak możemy używać metapromptów w naszym demo.

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

# DO ZROBIENIA dodaj żądanie do generowania obrazu
```

Z powyższego promptu widzisz, jak wszystkie tworzone obrazy uwzględniają metaprompt.

## Zadanie - ułatwmy uczniom

Na początku tej lekcji przedstawiliśmy Edu4All. Teraz czas umożliwić uczniom generowanie obrazów na potrzeby ich ocen.


Uczniowie stworzą obrazy do swoich ocen zawierające pomniki, a dokładnie jakie pomniki, to już decyzja uczniów. Uczniowie są proszeni o użycie swojej kreatywności w tym zadaniu, aby umieścić te pomniki w różnych kontekstach.

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

# Pobierz punkt końcowy i klucz z zmiennych środowiskowych
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-10-21"
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
"""

try:
    # Utwórz obraz za pomocą API generowania obrazów
    generation_response = client.images.generate(
        prompt=prompt,    # Wprowadź tutaj swój tekst promptu
        size='1024x1024',
        n=1,
    )
    # Ustaw katalog dla przechowywanego obrazu
    image_dir = os.path.join(os.curdir, 'images')

    # Jeśli katalog nie istnieje, utwórz go
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Zainicjuj ścieżkę obrazu (uwaga: typ pliku powinien być png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Pobierz wygenerowany obraz
    image_url = generation_response.data[0].url  # wyodrębnij URL obrazu z odpowiedzi
    generated_image = requests.get(image_url).content  # pobierz obraz
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Wyświetl obraz w domyślnym przeglądaczu obrazów
    image = Image.open(image_path)
    image.show()

# obsłuż wyjątki
except openai.BadRequestError as err:
    print(err)
```

## Świetna robota! Kontynuuj naukę

Po ukończeniu tej lekcji, sprawdź naszą [kolekcję nauki o sztucznej inteligencji generatywnej](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę o Generatywnej AI!

Przejdź do Lekcji 10, gdzie przyjrzymy się, jak [tworzyć aplikacje AI za pomocą niskokodowych narzędzi](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->