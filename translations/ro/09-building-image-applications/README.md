# Construirea aplicațiilor de generare a imaginilor

[![Construirea aplicațiilor de generare a imaginilor](../../../translated_images/ro/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLM-urile nu sunt doar pentru generarea de text. De asemenea, este posibil să generezi imagini din descrieri textuale. Având imaginile ca modalitate poate fi extrem de util în numeroase domenii, de la MedTech, arhitectură, turism, dezvoltare de jocuri și altele. În acest capitol, vom analiza cele două modele de generare a imaginilor cele mai populare, DALL-E și Midjourney.

## Introducere

În această lecție, vom acoperi:

- Generarea imaginilor și de ce este utilă.
- DALL-E și Midjourney, ce sunt și cum funcționează.
- Cum ai construi o aplicație de generare a imaginilor.

## Obiective de învățare

După ce vei finaliza această lecție, vei putea să:

- Construiești o aplicație de generare a imaginilor.
- Definesti limitele aplicației tale cu metaprompts.
- Lucrezi cu DALL-E și Midjourney.

## De ce să construiești o aplicație de generare a imaginilor?

Aplicațiile de generare a imaginilor sunt o modalitate excelentă de a explora capacitățile AI Generativ. Pot fi folosite, de exemplu, pentru:

- **Editarea și sinteza imaginilor**. Poți genera imagini pentru diverse cazuri de utilizare, cum ar fi editarea imaginilor și sinteza imaginilor.

- **Aplicate într-o varietate de industrii**. Ele pot fi folosite și pentru generarea de imagini pentru diverse industrii precum MedTech, Turism, Dezvoltare de jocuri și altele.

## Scenariu: Edu4All

Ca parte a acestei lecții, vom continua să lucrăm cu startup-ul nostru, Edu4All, în această lecție. Elevii vor crea imagini pentru evaluările lor, exact ce fel de imagini este la alegerea elevilor, dar ar putea fi ilustrații pentru propriul lor basm sau pentru a crea un personaj nou pentru povestea lor sau pentru a-i ajuta să-și vizualizeze ideile și conceptele.

Iată ce ar putea genera elevii Edu4All, de exemplu dacă lucrează în clasă pe monumente:

![Startup Edu4All, clasă pe monumente, Turnul Eiffel](../../../translated_images/ro/startup.94d6b79cc4bb3f5a.webp)

folosind un prompt precum

> "Câine lângă Turnul Eiffel în lumina dimineții"

## Ce sunt DALL-E și Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) și [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sunt două dintre cele mai populare modele de generare a imaginilor, ele îți permit să folosești prompturi pentru a genera imagini.

### DALL-E

Să începem cu DALL-E, care este un model AI generativ ce generează imagini din descrieri textuale.

> [DALL-E este o combinație a două modele, CLIP și atenția difuză](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, este un model care generează embeddinguri, care sunt reprezentări numerice ale datelor, din imagini și text.

- **Atenția difuză**, este un model care generează imagini din embeddinguri. DALL-E este antrenat pe un set de date cu imagini și text și poate fi folosit pentru a genera imagini din descrieri textuale. De exemplu, DALL-E poate fi folosit pentru a genera imagini cu o pisică cu pălărie, sau un câine cu mohawk.

### Midjourney

Midjourney funcționează într-un mod similar cu DALL-E, generează imagini pornind de la prompturi text. Midjourney poate fi de asemenea folosit pentru a genera imagini folosind prompturi ca “o pisică cu pălărie”, sau un “câine cu mohawk”.

![Imagine generată de Midjourney, porumbel mecanic](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Imagine credit Wikipedia, imagine generată de Midjourney_

## Cum funcționează DALL-E și Midjourney

Mai întâi, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E este un model AI generativ bazat pe arhitectura transformer cu un _transformer autoregresiv_.

Un _transformer autoregresiv_ definește modul în care un model generează imagini din descrieri textuale, generează un pixel pe rând, apoi folosește pixelii generați pentru a genera următorul pixel. Trecând prin multiple straturi într-o rețea neurală, până când imaginea este completă.

Prin acest proces, DALL-E controlează atribute, obiecte, caracteristici și altele în imaginea pe care o generează. Totuși, DALL-E 2 și 3 au control mai mare asupra imaginii generate.

## Construiește-ți prima aplicație de generare a imaginilor

Deci, ce este nevoie pentru a construi o aplicație de generare a imaginilor? Ai nevoie de următoarele biblioteci:

- **python-dotenv**, este recomandat să folosești această bibliotecă pentru a-ți păstra secretele într-un fișier _.env_ departe de cod.
- **openai**, această bibliotecă este ce vei folosi pentru a interacționa cu API-ul OpenAI.
- **pillow**, pentru a lucra cu imagini în Python.
- **requests**, pentru a te ajuta să faci cereri HTTP.

## Creează și implementează un model Azure OpenAI

Dacă nu ai făcut deja, urmează instrucțiunile de pe pagina [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)
pentru a crea un serviciu și model Azure OpenAI. Selectează **gpt-image-1** ca model (modelul actual Azure OpenAI pentru generarea imaginilor; DALL-E 3 este moștenire și nu mai este disponibil pentru implementări noi).

## Creează aplicația

1. Creează un fișier _.env_ cu următorul conținut:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Găsește aceste informații în portalul Azure OpenAI Foundry pentru resursa ta în secțiunea "Deployments".

1. Adună bibliotecile de mai sus într-un fișier numit _requirements.txt_ astfel:

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

   Pentru Windows, folosește comenzile următoare pentru a crea și activa mediul virtual:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Adaugă următorul cod în fișierul numit _app.py_:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # importă dotenv
    dotenv.load_dotenv()
    
    # Configurează clientul serviciului Azure OpenAI
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # Creează o imagine folosind API-ul de generare a imaginilor
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Setează directorul pentru imaginea stocată
        image_dir = os.path.join(os.curdir, 'images')

        # Dacă directorul nu există, creează-l
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Initializează calea imaginii (reține că tipul fișierului trebuie să fie png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Preia imaginea generată
        image_url = generation_response.data[0].url  # extrage URL-ul imaginii din răspuns
        generated_image = requests.get(image_url).content  # descarcă imaginea
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # Afișează imaginea în vizualizatorul implicit de imagini
        image = Image.open(image_path)
        image.show()

    # prinde excepțiile
    except openai.BadRequestError as err:
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

- După aceea, configurăm clientul serviciului Azure OpenAI 

  ```python
  # Obțineți endpoint-ul și cheia din variabilele de mediu
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- Urmează generarea imaginii:

  ```python
  # Creează o imagine folosind API-ul de generare a imaginilor
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

Să analizăm codul care generează imaginea mai în detaliu:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, este promptul text folosit pentru a genera imaginea. În acest caz, folosim promptul "Iepuraș pe cal, ținând un acadea, pe o pajiște ceațoasă unde cresc narcise".
- **size**, este dimensiunea imaginii generate. În acest caz, generăm o imagine de 1024x1024 pixeli.
- **n**, este numărul de imagini generate. În acest caz, generăm două imagini.
- **temperature**, este un parametru care controlează aleatorietatea ieșirii unui model AI generativ. Temperatura este o valoare între 0 și 1 unde 0 înseamnă că ieșirea este deterministă, iar 1 înseamnă că ieșirea este aleatorie. Valoarea implicită este 0.7.

Mai sunt și alte lucruri pe care le poți face cu imaginile și pe care le vom acoperi în secțiunea următoare.

## Capacități suplimentare ale generării imaginilor

Ai văzut până acum cum am putut genera o imagine folosind câteva linii în Python. Totuși, mai există și alte lucruri pe care le poți face cu imaginile.

Poți face, de asemenea, următoarele:

- **Efectuarea de modificări**. Furnizând o imagine existentă, o mască și un prompt, poți modifica o imagine. De exemplu, poți adăuga ceva într-o porțiune din imagine. Imaginează-ți imaginea noastră cu iepurașul, poți adăuga o pălărie iepurașului. Cum faci asta este oferind imaginea, o mască (identificând zona pentru schimbare) și un prompt text pentru a specifica ce trebuie făcut.
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
  <img src="../../../translated_images/ro/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ro/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ro/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Crearea de variații**. Ideea este să iei o imagine existentă și să ceri crearea de variații. Pentru a crea o variație, oferi o imagine și un prompt text și scrii cod astfel:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > Notă, acest lucru este suportat doar pe modelul DALL-E 2 de la OpenAI, nu pe gpt-image-1

## Temperatura

Temperatura este un parametru care controlează aleatorietatea ieșirii unui model AI generativ. Temperatura este o valoare între 0 și 1 unde 0 înseamnă că ieșirea este deterministă, iar 1 înseamnă că ieșirea este aleatorie. Valoarea implicită este 0.7.

Să privim un exemplu despre cum funcționează temperatura, rulând acest prompt de două ori:

> Prompt : "Iepuraș pe cal, ținând un acadea, pe o pajiște ceațoasă unde cresc narcise"

![Iepuraș pe un cal ținând un acadea, versiunea 1](../../../translated_images/ro/v1-generated-image.a295cfcffa3c13c2.webp)

Acum să rulăm același prompt doar ca să vedem că nu vom obține aceeași imagine de două ori:

![Imagine generată cu iepuraș pe cal](../../../translated_images/ro/v2-generated-image.33f55a3714efe61d.webp)

După cum vezi, imaginile sunt similare, dar nu identice. Hai să încercăm să schimbăm valoarea temperaturii la 0.1 și să vedem ce se întâmplă:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Introduceți textul solicitării aici
        size='1024x1024',
        n=2
    )
```

### Schimbarea temperaturii

Deci să încercăm să facem răspunsul mai determinist. Am putea observa din cele două imagini generate că în prima imagine este un iepuraș iar în a doua este un cal, deci imaginile variază mult.

Așadar, să schimbăm codul nostru și să setăm temperatura la 0, astfel:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Introduceți textul solicitării aici
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Acum când rulezi acest cod, vei obține aceste două imagini:

- ![Temperatura 0, v1](../../../translated_images/ro/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Temperatura 0 , v2](../../../translated_images/ro/v2-temp-generated-image.871d0c920dbfb0f1.webp)

Aici poți vedea clar cum imaginile seamănă mult mai mult între ele.

## Cum să definești limite pentru aplicația ta cu metaprompturi

Cu demonstrația noastră, putem deja genera imagini pentru clienții noștri. Totuși, trebuie să creăm anumite limite pentru aplicația noastră.

De exemplu, nu vrem să generăm imagini care nu sunt sigure pentru muncă, sau care nu sunt potrivite pentru copii.

Putem face asta cu _metaprompturi_. Metaprompturile sunt prompturi text folosite pentru a controla ieșirea unui model AI generativ. De exemplu, putem folosi metaprompturi pentru a controla ieșirea și a asigura că imaginile generate sunt sigure pentru muncă sau potrivite pentru copii.

### Cum funcționează?

Acum, cum funcționează metaprompturile?

Metaprompturile sunt prompturi text folosite pentru a controla ieșirea unui model AI generativ, ele sunt poziționate înaintea promptului text și sunt folosite pentru a controla ieșirea modelului și încorporate în aplicații pentru a controla ieșirea modelului. Încapsulând promptul de intrare și metapromptul într-un singur prompt text.

Un exemplu de metaprompt ar fi următorul:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Acum, să vedem cum putem folosi metaprompturile în demonstrația noastră.

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

# TODO adăugați cererea pentru a genera imaginea
```

Din promptul de mai sus, poți vedea cum toate imaginile create iau în considerare metapromptul.

## Tema - să dăm posibilitatea elevilor

Am introdus Edu4All la începutul acestei lecții. Acum e timpul să dăm posibilitatea elevilor să genereze imagini pentru evaluările lor.


Elevii vor crea imagini pentru evaluările lor care conțin monumente, ce monumente exact vor fi alese de elevi. Se cere elevilor să folosească creativitatea în această sarcină pentru a plasa aceste monumente în contexte diferite.

## Soluție

Iată o soluție posibilă:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# Obțineți endpoint-ul și cheia din variabilele de mediu
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
    # Creați o imagine folosind API-ul de generare a imaginilor
    generation_response = client.images.generate(
        prompt=prompt,    # Introduceți aici textul promptului dvs.
        size='1024x1024',
        n=1,
    )
    # Setați directorul pentru imaginea stocată
    image_dir = os.path.join(os.curdir, 'images')

    # Dacă directorul nu există, creați-l
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Inițializați calea imaginii (rețineți că tipul fișierului ar trebui să fie png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Recuperați imaginea generată
    image_url = generation_response.data[0].url  # extrageți URL-ul imaginii din răspuns
    generated_image = requests.get(image_url).content  # descărcați imaginea
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Afișați imaginea în vizualizatorul de imagini implicit
    image = Image.open(image_path)
    image.show()

# prinde excepțiile
except openai.BadRequestError as err:
    print(err)
```

## Lucru excelent! Continuă să înveți

După ce finalizezi această lecție, consultă colecția noastră [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a-ți continua dezvoltarea cunoștințelor despre Generative AI!

Mergi la Lecția 10 unde vom vedea cum să [construim aplicații AI cu low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->