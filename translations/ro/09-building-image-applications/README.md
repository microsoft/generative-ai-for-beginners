<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:23:41+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ro"
}
-->
# Construirea aplicațiilor de generare a imaginilor

Există mai mult la LLM-uri decât generarea de text. Este, de asemenea, posibil să generezi imagini din descrieri textuale. A avea imagini ca modalitate poate fi extrem de util în numeroase domenii, de la MedTech, arhitectură, turism, dezvoltare de jocuri și altele. În acest capitol, vom analiza cele două modele de generare a imaginilor cele mai populare, DALL-E și Midjourney.

## Introducere

În această lecție, vom acoperi:

- Generarea de imagini și de ce este utilă.
- DALL-E și Midjourney, ce sunt și cum funcționează.
- Cum să construiești o aplicație de generare a imaginilor.

## Obiective de învățare

După finalizarea acestei lecții, vei putea:

- Să construiești o aplicație de generare a imaginilor.
- Să definești limitele aplicației tale cu meta-propuneri.
- Să lucrezi cu DALL-E și Midjourney.

## De ce să construiești o aplicație de generare a imaginilor?

Aplicațiile de generare a imaginilor sunt o modalitate excelentă de a explora capacitățile AI Generativă. Ele pot fi utilizate, de exemplu, pentru:

- **Editare și sinteză de imagini**. Poți genera imagini pentru o varietate de cazuri de utilizare, cum ar fi editarea și sinteza imaginilor.

- **Aplicate în diverse industrii**. Pot fi, de asemenea, folosite pentru a genera imagini pentru diverse industrii precum Medtech, Turism, Dezvoltare de jocuri și altele.

## Scenariu: Edu4All

Ca parte a acestei lecții, vom continua să lucrăm cu startup-ul nostru, Edu4All. Studenții vor crea imagini pentru evaluările lor, exact ce imagini depinde de studenți, dar ar putea fi ilustrații pentru propriul lor basm sau crearea unui nou personaj pentru povestea lor sau să îi ajute să-și vizualizeze ideile și conceptele.

Iată ce ar putea genera studenții de la Edu4All, de exemplu, dacă lucrează în clasă la monumente:

folosind o propunere ca

> "Câine lângă Turnul Eiffel în lumina dimineții"

## Ce sunt DALL-E și Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) și [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sunt două dintre cele mai populare modele de generare a imaginilor, care îți permit să folosești propuneri pentru a genera imagini.

### DALL-E

Să începem cu DALL-E, care este un model AI Generativă ce generează imagini din descrieri textuale.

- **CLIP**, este un model care generează încorporări, care sunt reprezentări numerice ale datelor, din imagini și text.

- **Atenție difuză**, este un model care generează imagini din încorporări. DALL-E este antrenat pe un set de date de imagini și text și poate fi folosit pentru a genera imagini din descrieri textuale. De exemplu, DALL-E poate fi folosit pentru a genera imagini cu o pisică cu pălărie sau un câine cu mohawk.

### Midjourney

Midjourney funcționează într-un mod similar cu DALL-E, generând imagini din propuneri textuale. Midjourney poate fi, de asemenea, folosit pentru a genera imagini folosind propuneri precum „o pisică cu pălărie” sau „un câine cu mohawk”.

## Cum funcționează DALL-E și Midjourney

Mai întâi, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E este un model AI Generativă bazat pe arhitectura transformatoare cu un _transformator autoregresiv_.

Un _transformator autoregresiv_ definește cum un model generează imagini din descrieri textuale, generând un pixel pe rând, și apoi folosind pixelii generați pentru a genera următorul pixel. Trecând prin mai multe straturi într-o rețea neuronală, până când imaginea este completă.

Cu acest proces, DALL-E controlează atribute, obiecte, caracteristici și altele în imaginea generată. Totuși, DALL-E 2 și 3 au mai mult control asupra imaginii generate.

## Construirea primei tale aplicații de generare a imaginilor

Deci, ce este necesar pentru a construi o aplicație de generare a imaginilor? Ai nevoie de următoarele biblioteci:

- **python-dotenv**, este recomandat să folosești această bibliotecă pentru a păstra secretele într-un fișier _.env_ departe de cod.
- **openai**, această bibliotecă este ceea ce vei folosi pentru a interacționa cu API-ul OpenAI.
- **pillow**, pentru a lucra cu imagini în Python.
- **requests**, pentru a te ajuta să faci cereri HTTP.

1. Creează un fișier _.env_ cu următorul conținut:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Localizează aceste informații în Portalul Azure pentru resursa ta în secțiunea "Keys and Endpoint".

1. Colectează bibliotecile de mai sus într-un fișier numit _requirements.txt_ astfel:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Apoi, creează un mediu virtual și instalează bibliotecile:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Pentru Windows, folosește următoarele comenzi pentru a crea și activa mediul tău virtual:

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

Să explicăm acest cod:

- Mai întâi, importăm bibliotecile de care avem nevoie, inclusiv biblioteca OpenAI, biblioteca dotenv, biblioteca requests și biblioteca Pillow.

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

- După aceea, setăm endpoint-ul, cheia pentru API-ul OpenAI, versiunea și tipul.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Apoi, generăm imaginea:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Codul de mai sus răspunde cu un obiect JSON care conține URL-ul imaginii generate. Putem folosi URL-ul pentru a descărca imaginea și a o salva într-un fișier.

- În cele din urmă, deschidem imaginea și folosim vizualizatorul standard de imagini pentru a o afișa:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Mai multe detalii despre generarea imaginii

Să ne uităm la codul care generează imaginea în mai multe detalii:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, este propunerea text care este folosită pentru a genera imaginea. În acest caz, folosim propunerea "Iepuraș pe cal, ținând o acadea, pe un câmp cu ceață unde cresc narcise".
- **size**, este dimensiunea imaginii generate. În acest caz, generăm o imagine de 1024x1024 pixeli.
- **n**, este numărul de imagini generate. În acest caz, generăm două imagini.
- **temperature**, este un parametru care controlează aleatorietatea rezultatului unui model AI Generativă. Temperatura este o valoare între 0 și 1 unde 0 înseamnă că rezultatul este determinist și 1 înseamnă că rezultatul este aleatoriu. Valoarea implicită este 0.7.

Există mai multe lucruri pe care le poți face cu imaginile, pe care le vom acoperi în secțiunea următoare.

## Capacități suplimentare de generare a imaginilor

Până acum ai văzut cum am reușit să generăm o imagine folosind câteva linii de cod în Python. Totuși, există mai multe lucruri pe care le poți face cu imaginile.

Poți, de asemenea, să faci următoarele:

- **Realiza editări**. Prin furnizarea unei imagini existente, a unei măști și a unei propuneri, poți modifica o imagine. De exemplu, poți adăuga ceva într-o porțiune a unei imagini. Imaginează-ți imaginea noastră cu iepurașul, poți adăuga o pălărie iepurașului. Cum ai face asta este prin furnizarea imaginii, a unei măști (identificând partea din zonă pentru schimbare) și a unei propuneri textuale pentru a spune ce ar trebui făcut.

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

  Imaginea de bază ar conține doar iepurele, dar imaginea finală ar avea pălăria pe iepure.

- **Creează variații**. Ideea este că iei o imagine existentă și ceri să fie create variații. Pentru a crea o variație, furnizezi o imagine și o propunere textuală și codul astfel:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Notă, aceasta este suportată doar pe OpenAI

## Temperatura

Temperatura este un parametru care controlează aleatorietatea rezultatului unui model AI Generativă. Temperatura este o valoare între 0 și 1 unde 0 înseamnă că rezultatul este determinist și 1 înseamnă că rezultatul este aleatoriu. Valoarea implicită este 0.7.

Să ne uităm la un exemplu de cum funcționează temperatura, rulând această propunere de două ori:

> Propunere: "Iepuraș pe cal, ținând o acadea, pe un câmp cu ceață unde cresc narcise"

Acum să rulăm aceeași propunere doar pentru a vedea că nu vom obține aceeași imagine de două ori:

După cum poți vedea, imaginile sunt similare, dar nu aceleași. Să încercăm să schimbăm valoarea temperaturii la 0.1 și să vedem ce se întâmplă:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Schimbarea temperaturii

Așadar, să încercăm să facem răspunsul mai determinist. Am putea observa din cele două imagini generate că în prima imagine, există un iepuraș și în a doua imagine, există un cal, deci imaginile variază foarte mult.

Prin urmare, să ne schimbăm codul și să setăm temperatura la 0, astfel:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Acum când rulezi acest cod, obții aceste două imagini:

Aici poți vedea clar cum imaginile se aseamănă mai mult.

## Cum să definești limitele pentru aplicația ta cu metapropuneri

Cu demo-ul nostru, putem deja genera imagini pentru clienții noștri. Totuși, trebuie să creăm niște limite pentru aplicația noastră.

De exemplu, nu dorim să generăm imagini care nu sunt sigure pentru muncă sau care nu sunt adecvate pentru copii.

Putem face asta cu _metapropuneri_. Metapropunerile sunt propuneri textuale care sunt folosite pentru a controla rezultatul unui model AI Generativă. De exemplu, putem folosi metapropuneri pentru a controla rezultatul și a ne asigura că imaginile generate sunt sigure pentru muncă sau adecvate pentru copii.

### Cum funcționează?

Acum, cum funcționează metapropunerile?

Metapropunerile sunt propuneri textuale care sunt folosite pentru a controla rezultatul unui model AI Generativă, ele sunt poziționate înaintea propunerii textuale și sunt folosite pentru a controla rezultatul modelului și sunt încorporate în aplicații pentru a controla rezultatul modelului. Înglobând intrarea propunerii și intrarea metapropunerii într-o singură propunere textuală.

Un exemplu de metapropunere ar fi următorul:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Acum, să vedem cum putem folosi metapropunerile în demo-ul nostru.

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

Din propunerea de mai sus, poți vedea cum toate imaginile create iau în considerare metapropunerea.

## Temă - să îi ajutăm pe studenți

Am introdus Edu4All la începutul acestei lecții. Acum este momentul să îi ajutăm pe studenți să genereze imagini pentru evaluările lor.

Studenții vor crea imagini pentru evaluările lor care conțin monumente, exact ce monumente depinde de studenți. Studenții sunt rugați să-și folosească creativitatea în această sarcină pentru a plasa aceste monumente în diferite contexte.

## Soluție

Iată o soluție posibilă:

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

## Foarte bine! Continuă să înveți

După finalizarea acestei lecții, verifică [colecția noastră de învățare AI Generativă](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să-ți îmbunătățești cunoștințele despre AI Generativă!

Mergi la Lecția 10 unde vom analiza cum să [construiești aplicații AI cu cod redus](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Declinare**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să obținem acuratețe, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională umană. Nu suntem responsabili pentru neînțelegerile sau interpretările greșite care decurg din utilizarea acestei traduceri.