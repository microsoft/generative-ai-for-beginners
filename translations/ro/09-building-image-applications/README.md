<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:55:31+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ro"
}
-->
# Construirea aplicațiilor de generare de imagini

[![Construirea aplicațiilor de generare de imagini](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ro.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM-urile nu se limitează doar la generarea de text. Este posibil să generăm imagini din descrieri textuale. Utilizarea imaginilor ca modalitate poate fi extrem de utilă în diverse domenii, cum ar fi MedTech, arhitectură, turism, dezvoltarea de jocuri și altele. În acest capitol, vom analiza cele mai populare modele de generare de imagini, DALL-E și Midjourney.

## Introducere

În această lecție, vom acoperi:

- Generarea de imagini și utilitatea acesteia.
- DALL-E și Midjourney: ce sunt și cum funcționează.
- Cum să construiești o aplicație de generare de imagini.

## Obiective de învățare

După finalizarea acestei lecții, vei putea:

- Să construiești o aplicație de generare de imagini.
- Să definești limite pentru aplicația ta folosind meta-prompts.
- Să lucrezi cu DALL-E și Midjourney.

## De ce să construiești o aplicație de generare de imagini?

Aplicațiile de generare de imagini sunt o modalitate excelentă de a explora capacitățile AI generativă. Acestea pot fi utilizate, de exemplu, pentru:

- **Editare și sinteză de imagini**. Poți genera imagini pentru diverse utilizări, cum ar fi editarea și sinteza de imagini.

- **Aplicare în diverse industrii**. Ele pot fi utilizate pentru a genera imagini în diverse industrii, cum ar fi MedTech, turism, dezvoltarea de jocuri și altele.

## Scenariu: Edu4All

Ca parte a acestei lecții, vom continua să lucrăm cu startup-ul nostru, Edu4All. Studenții vor crea imagini pentru evaluările lor; ce imagini vor crea depinde de ei, dar acestea ar putea fi ilustrații pentru propriile povești sau crearea unui nou personaj pentru povestea lor, sau îi pot ajuta să-și vizualizeze ideile și conceptele.

Iată ce ar putea genera studenții Edu4All, de exemplu, dacă lucrează în clasă la monumente:

![Startup Edu4All, clasă despre monumente, Turnul Eiffel](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ro.png)

folosind un prompt precum:

> "Câine lângă Turnul Eiffel în lumina dimineții"

## Ce sunt DALL-E și Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) și [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sunt două dintre cele mai populare modele de generare de imagini, care permit utilizarea prompturilor pentru a genera imagini.

### DALL-E

Să începem cu DALL-E, care este un model AI generativ ce generează imagini din descrieri textuale.

> [DALL-E este o combinație între două modele, CLIP și atenția difuză](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** este un model care generează embeddings, reprezentări numerice ale datelor, din imagini și text.

- **Atenția difuză** este un model care generează imagini din embeddings. DALL-E este antrenat pe un set de date de imagini și text și poate fi utilizat pentru a genera imagini din descrieri textuale. De exemplu, DALL-E poate fi utilizat pentru a genera imagini cu o pisică într-o pălărie sau un câine cu un mohawk.

### Midjourney

Midjourney funcționează într-un mod similar cu DALL-E, generând imagini din prompturi textuale. Midjourney poate fi utilizat pentru a genera imagini folosind prompturi precum „o pisică într-o pălărie” sau „un câine cu un mohawk”.

![Imagine generată de Midjourney, porumbel mecanic](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Credit imagine Wikipedia, imagine generată de Midjourney_

## Cum funcționează DALL-E și Midjourney

Mai întâi, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E este un model AI generativ bazat pe arhitectura transformer cu un _transformer autoregresiv_.

Un _transformer autoregresiv_ definește modul în care un model generează imagini din descrieri textuale, generând un pixel pe rând și utilizând pixelii generați pentru a genera următorul pixel. Procesul trece prin mai multe straturi ale unei rețele neuronale, până când imaginea este completă.

Prin acest proces, DALL-E controlează atributele, obiectele, caracteristicile și altele în imaginea generată. Totuși, DALL-E 2 și 3 oferă un control mai mare asupra imaginii generate.

## Construirea primei tale aplicații de generare de imagini

Ce este necesar pentru a construi o aplicație de generare de imagini? Ai nevoie de următoarele biblioteci:

- **python-dotenv**, este recomandat să folosești această bibliotecă pentru a păstra secretele într-un fișier _.env_ separat de cod.
- **openai**, această bibliotecă este utilizată pentru a interacționa cu API-ul OpenAI.
- **pillow**, pentru a lucra cu imagini în Python.
- **requests**, pentru a te ajuta să faci cereri HTTP.

## Crearea și implementarea unui model Azure OpenAI

Dacă nu ai făcut deja acest lucru, urmează instrucțiunile de pe pagina [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) pentru a crea o resursă și un model Azure OpenAI. Selectează DALL-E 3 ca model.

## Crearea aplicației

1. Creează un fișier _.env_ cu următorul conținut:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Localizează aceste informații în portalul Azure OpenAI Foundry pentru resursa ta, în secțiunea „Deployments”.

1. Adună bibliotecile de mai sus într-un fișier numit _requirements.txt_ astfel:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Creează un mediu virtual și instalează bibliotecile:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Pentru Windows, folosește următoarele comenzi pentru a crea și activa mediul virtual:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Adaugă următorul cod într-un fișier numit _app.py_:

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

Să explicăm acest cod:

- Mai întâi, importăm bibliotecile necesare, inclusiv biblioteca OpenAI, biblioteca dotenv, biblioteca requests și biblioteca Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Apoi, încărcăm variabilele de mediu din fișierul _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- După aceea, configurăm clientul serviciului Azure OpenAI.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Următorul pas este generarea imaginii:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Codul de mai sus răspunde cu un obiect JSON care conține URL-ul imaginii generate. Putem folosi URL-ul pentru a descărca imaginea și a o salva într-un fișier.

- În final, deschidem imaginea și folosim vizualizatorul standard de imagini pentru a o afișa:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Mai multe detalii despre generarea imaginii

Să analizăm codul care generează imaginea în detaliu:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, este promptul textual utilizat pentru a genera imaginea. În acest caz, folosim promptul „Iepure pe cal, ținând o acadea, pe o pajiște cețoasă unde cresc narcise”.
- **size**, este dimensiunea imaginii generate. În acest caz, generăm o imagine de 1024x1024 pixeli.
- **n**, este numărul de imagini generate. În acest caz, generăm două imagini.
- **temperature**, este un parametru care controlează aleatorietatea rezultatului unui model AI generativ. Temperatura este o valoare între 0 și 1, unde 0 înseamnă că rezultatul este determinist, iar 1 înseamnă că rezultatul este aleatoriu. Valoarea implicită este 0.7.

Există mai multe lucruri pe care le poți face cu imaginile, pe care le vom acoperi în secțiunea următoare.

## Capacități suplimentare ale generării de imagini

Până acum, ai văzut cum am reușit să generăm o imagine folosind câteva linii de cod în Python. Totuși, există mai multe lucruri pe care le poți face cu imaginile.

De asemenea, poți:

- **Efectua modificări**. Prin furnizarea unei imagini existente, a unei măști și a unui prompt, poți modifica o imagine. De exemplu, poți adăuga ceva într-o porțiune a imaginii. Imaginează-ți imaginea noastră cu iepurele; poți adăuga o pălărie iepurelui. Cum faci acest lucru? Furnizând imaginea, o mască (identificând partea zonei pentru schimbare) și un prompt textual care să descrie ce trebuie făcut.
> Notă: acest lucru nu este suportat în DALL-E 3.

Iată un exemplu folosind GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Imaginea de bază ar conține doar lounge-ul cu piscină, dar imaginea finală ar avea un flamingo:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.ro.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.ro.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.ro.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Crea variații**. Ideea este să iei o imagine existentă și să ceri să fie create variații. Pentru a crea o variație, furnizezi o imagine și un prompt textual și codul astfel:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Notă: acest lucru este suportat doar pe OpenAI.

## Temperatura

Temperatura este un parametru care controlează aleatorietatea rezultatului unui model AI generativ. Temperatura este o valoare între 0 și 1, unde 0 înseamnă că rezultatul este determinist, iar 1 înseamnă că rezultatul este aleatoriu. Valoarea implicită este 0.7.

Să analizăm un exemplu despre cum funcționează temperatura, rulând acest prompt de două ori:

> Prompt: „Iepure pe cal, ținând o acadea, pe o pajiște cețoasă unde cresc narcise”

![Iepure pe cal ținând o acadea, versiunea 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ro.png)

Acum să rulăm același prompt pentru a vedea că nu vom obține aceeași imagine de două ori:

![Imagine generată cu iepure pe cal](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ro.png)

După cum poți vedea, imaginile sunt similare, dar nu identice. Să încercăm să schimbăm valoarea temperaturii la 0.1 și să vedem ce se întâmplă:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Schimbarea temperaturii

Să încercăm să facem răspunsul mai determinist. Am putut observa din cele două imagini generate că în prima imagine există un iepure, iar în a doua imagine există un cal, deci imaginile variază semnificativ.

Să schimbăm, așadar, codul nostru și să setăm temperatura la 0, astfel:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Acum, când rulezi acest cod, obții aceste două imagini:

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ro.png)
- ![Temperatura 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ro.png)

Aici poți vedea clar cum imaginile se aseamănă mai mult.

## Cum să definești limite pentru aplicația ta folosind meta-prompts

Cu demo-ul nostru, putem deja genera imagini pentru clienții noștri. Totuși, trebuie să creăm niște limite pentru aplicația noastră.

De exemplu, nu dorim să generăm imagini care nu sunt potrivite pentru locul de muncă sau care nu sunt adecvate pentru copii.

Putem face acest lucru cu _meta-prompts_. Meta-prompts sunt prompturi textuale utilizate pentru a controla rezultatul unui model AI generativ. De exemplu, putem folosi meta-prompts pentru a controla rezultatul și a ne asigura că imaginile generate sunt potrivite pentru locul de muncă sau adecvate pentru copii.

### Cum funcționează?

Cum funcționează meta-prompts?

Meta-prompts sunt prompturi textuale utilizate pentru a controla rezultatul unui model AI generativ; ele sunt poziționate înaintea promptului textual și sunt utilizate pentru a controla rezultatul modelului, fiind încorporate în aplicații pentru a controla rezultatul modelului. Ele encapsulează inputul promptului și inputul meta-promptului într-un singur prompt textual.

Un exemplu de meta-prompt ar fi următorul:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Acum, să vedem cum putem folosi meta-prompts în demo-ul nostru.

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

Din promptul de mai sus, poți vedea cum toate imaginile create iau în considerare meta-promptul.

## Sarcină - să activăm studenții

Am introdus Edu4All la începutul acestei lecții. Acum este momentul să activăm studenții pentru a genera imagini pentru evaluările lor.

Studenții vor crea imagini pentru evaluările lor care conțin monumente; exact ce monumente vor alege depinde de studenți. Studenții sunt rugați să-și folosească creativitatea în această sarcină pentru a plasa aceste monumente în contexte diferite.

## Soluție

Iată o posibilă soluție:
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

## Felicitări! Continuă să înveți

După ce ai finalizat această lecție, explorează [colecția noastră de învățare despre AI generativă](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a-ți aprofunda cunoștințele despre AI generativă!

Mergi la Lecția 10, unde vom analiza cum să [construim aplicații AI cu cod redus](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.