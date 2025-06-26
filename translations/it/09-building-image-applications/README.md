<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:18:44+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "it"
}
-->
# Costruire Applicazioni di Generazione di Immagini

C'è di più nei LLM rispetto alla generazione di testo. È anche possibile generare immagini da descrizioni testuali. Avere immagini come modalità può essere estremamente utile in numerosi settori come MedTech, architettura, turismo, sviluppo di giochi e altro ancora. In questo capitolo, esamineremo i due modelli di generazione di immagini più popolari, DALL-E e Midjourney.

## Introduzione

In questa lezione, copriremo:

- Generazione di immagini e perché è utile.
- DALL-E e Midjourney, cosa sono e come funzionano.
- Come costruire un'app di generazione di immagini.

## Obiettivi di apprendimento

Dopo aver completato questa lezione, sarai in grado di:

- Costruire un'applicazione di generazione di immagini.
- Definire i confini per la tua applicazione con meta prompt.
- Lavorare con DALL-E e Midjourney.

## Perché costruire un'applicazione di generazione di immagini?

Le applicazioni di generazione di immagini sono un ottimo modo per esplorare le capacità dell'Intelligenza Artificiale Generativa. Possono essere utilizzate, ad esempio, per:

- **Modifica e sintesi di immagini**. Puoi generare immagini per una varietà di casi d'uso, come la modifica e la sintesi di immagini.

- **Applicate a una varietà di settori**. Possono anche essere utilizzate per generare immagini per una varietà di settori come Medtech, Turismo, Sviluppo di giochi e altro.

## Scenario: Edu4All

Come parte di questa lezione, continueremo a lavorare con la nostra startup, Edu4All, in questa lezione. Gli studenti creeranno immagini per le loro valutazioni, esattamente quali immagini spetta agli studenti, ma potrebbero essere illustrazioni per la loro fiaba o creare un nuovo personaggio per la loro storia o aiutarli a visualizzare le loro idee e concetti.

Ecco cosa potrebbero generare gli studenti di Edu4All, ad esempio, se stanno lavorando in classe sui monumenti:

usando un prompt come

> "Cane accanto alla Torre Eiffel nella luce del sole del primo mattino"

## Cosa sono DALL-E e Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) e [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sono due dei modelli di generazione di immagini più popolari, ti permettono di usare prompt per generare immagini.

### DALL-E

Iniziamo con DALL-E, che è un modello di Intelligenza Artificiale Generativa che genera immagini da descrizioni testuali.

- **CLIP**, è un modello che genera embedding, che sono rappresentazioni numeriche di dati, da immagini e testo.

- **Attenzione diffusa**, è un modello che genera immagini dagli embedding. DALL-E è addestrato su un dataset di immagini e testo e può essere utilizzato per generare immagini da descrizioni testuali. Ad esempio, DALL-E può essere utilizzato per generare immagini di un gatto con un cappello, o di un cane con una cresta.

### Midjourney

Midjourney funziona in modo simile a DALL-E, genera immagini da prompt testuali. Midjourney, può anche essere utilizzato per generare immagini usando prompt come "un gatto con un cappello", o un "cane con una cresta".

## Come funzionano DALL-E e Midjourney

Prima, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E è un modello di Intelligenza Artificiale Generativa basato sull'architettura transformer con un _transformer autoregressivo_.

Un _transformer autoregressivo_ definisce come un modello genera immagini da descrizioni testuali, genera un pixel alla volta, e poi utilizza i pixel generati per generare il pixel successivo. Passando attraverso più livelli in una rete neurale, fino a quando l'immagine è completa.

Con questo processo, DALL-E, controlla attributi, oggetti, caratteristiche e altro nell'immagine che genera. Tuttavia, DALL-E 2 e 3 hanno più controllo sull'immagine generata.

## Costruire la tua prima applicazione di generazione di immagini

Allora cosa serve per costruire un'applicazione di generazione di immagini? Hai bisogno delle seguenti librerie:

- **python-dotenv**, si consiglia vivamente di utilizzare questa libreria per mantenere i tuoi segreti in un file _.env_ lontano dal codice.
- **openai**, questa libreria è quella che utilizzerai per interagire con l'API OpenAI.
- **pillow**, per lavorare con le immagini in Python.
- **requests**, per aiutarti a fare richieste HTTP.

1. Crea un file _.env_ con il seguente contenuto:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Trova queste informazioni nel portale di Azure per la tua risorsa nella sezione "Chiavi e Endpoint".

1. Raccogli le librerie sopra in un file chiamato _requirements.txt_ in questo modo:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Successivamente, crea un ambiente virtuale e installa le librerie:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Per Windows, usa i seguenti comandi per creare e attivare il tuo ambiente virtuale:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Aggiungi il seguente codice in un file chiamato _app.py_:

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

Spieghiamo questo codice:

- Per prima cosa, importiamo le librerie di cui abbiamo bisogno, inclusa la libreria OpenAI, la libreria dotenv, la libreria requests e la libreria Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Successivamente, carichiamo le variabili d'ambiente dal file _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Dopodiché, impostiamo l'endpoint, la chiave per l'API OpenAI, la versione e il tipo.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Successivamente, generiamo l'immagine:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Il codice sopra risponde con un oggetto JSON che contiene l'URL dell'immagine generata. Possiamo utilizzare l'URL per scaricare l'immagine e salvarla in un file.

- Infine, apriamo l'immagine e usiamo il visualizzatore di immagini standard per visualizzarla:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Maggiori dettagli sulla generazione dell'immagine

Esaminiamo il codice che genera l'immagine in modo più dettagliato:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, è il prompt testuale che viene utilizzato per generare l'immagine. In questo caso, stiamo usando il prompt "Coniglio su cavallo, con in mano un lecca-lecca, in un prato nebbioso dove crescono i narcisi".
- **size**, è la dimensione dell'immagine che viene generata. In questo caso, stiamo generando un'immagine di 1024x1024 pixel.
- **n**, è il numero di immagini che vengono generate. In questo caso, stiamo generando due immagini.
- **temperature**, è un parametro che controlla la casualità dell'output di un modello di Intelligenza Artificiale Generativa. La temperatura è un valore compreso tra 0 e 1 dove 0 significa che l'output è deterministico e 1 significa che l'output è casuale. Il valore predefinito è 0,7.

Ci sono più cose che puoi fare con le immagini che copriremo nella sezione successiva.

## Capacità aggiuntive della generazione di immagini

Finora hai visto come siamo stati in grado di generare un'immagine utilizzando poche righe in Python. Tuttavia, ci sono più cose che puoi fare con le immagini.

Puoi anche fare quanto segue:

- **Eseguire modifiche**. Fornendo un'immagine esistente, una maschera e un prompt, puoi alterare un'immagine. Ad esempio, puoi aggiungere qualcosa a una porzione di un'immagine. Immagina la nostra immagine del coniglio, puoi aggiungere un cappello al coniglio. Come lo faresti è fornendo l'immagine, una maschera (identificando la parte dell'area per il cambiamento) e un prompt testuale per dire cosa dovrebbe essere fatto.

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

  L'immagine di base conterrebbe solo il coniglio, ma l'immagine finale avrebbe il cappello sul coniglio.

- **Creare variazioni**. L'idea è che prendi un'immagine esistente e chiedi che vengano create delle variazioni. Per creare una variazione, fornisci un'immagine e un prompt testuale e il codice in questo modo:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Nota, questo è supportato solo su OpenAI

## Temperatura

La temperatura è un parametro che controlla la casualità dell'output di un modello di Intelligenza Artificiale Generativa. La temperatura è un valore compreso tra 0 e 1 dove 0 significa che l'output è deterministico e 1 significa che l'output è casuale. Il valore predefinito è 0,7.

Esaminiamo un esempio di come funziona la temperatura, eseguendo questo prompt due volte:

> Prompt: "Coniglio su cavallo, con in mano un lecca-lecca, in un prato nebbioso dove crescono i narcisi"

Ora eseguiamo lo stesso prompt solo per vedere che non otterremo la stessa immagine due volte:

Come puoi vedere, le immagini sono simili, ma non uguali. Proviamo a cambiare il valore della temperatura a 0,1 e vediamo cosa succede:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Cambiare la temperatura

Quindi proviamo a rendere la risposta più deterministica. Potremmo osservare dalle due immagini che abbiamo generato che nella prima immagine c'è un coniglio e nella seconda immagine c'è un cavallo, quindi le immagini variano notevolmente.

Quindi cambiamo il nostro codice e impostiamo la temperatura a 0, in questo modo:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Ora quando esegui questo codice, ottieni queste due immagini:

Qui puoi chiaramente vedere come le immagini si assomigliano di più.

## Come definire i confini per la tua applicazione con metaprompt

Con la nostra demo, possiamo già generare immagini per i nostri clienti. Tuttavia, dobbiamo creare alcuni confini per la nostra applicazione.

Ad esempio, non vogliamo generare immagini che non siano sicure per il lavoro, o che non siano appropriate per i bambini.

Possiamo farlo con i _metaprompt_. I metaprompt sono prompt testuali che vengono utilizzati per controllare l'output di un modello di Intelligenza Artificiale Generativa. Ad esempio, possiamo utilizzare i metaprompt per controllare l'output e garantire che le immagini generate siano sicure per il lavoro o appropriate per i bambini.

### Come funziona?

Ora, come funzionano i meta prompt?

I meta prompt sono prompt testuali che vengono utilizzati per controllare l'output di un modello di Intelligenza Artificiale Generativa, sono posizionati prima del prompt testuale e vengono utilizzati per controllare l'output del modello e incorporati nelle applicazioni per controllare l'output del modello. Incapsulando l'input del prompt e l'input del meta prompt in un unico prompt testuale.

Un esempio di un meta prompt sarebbe il seguente:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Ora, vediamo come possiamo utilizzare i meta prompt nella nostra demo.

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

Dal prompt sopra, puoi vedere come tutte le immagini create considerano il metaprompt.

## Compito - diamo potere agli studenti

Abbiamo introdotto Edu4All all'inizio di questa lezione. Ora è il momento di abilitare gli studenti a generare immagini per le loro valutazioni.

Gli studenti creeranno immagini per le loro valutazioni contenenti monumenti, esattamente quali monumenti spetta agli studenti. Gli studenti sono invitati a usare la loro creatività in questo compito per collocare questi monumenti in contesti diversi.

## Soluzione

Ecco una possibile soluzione:

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

## Ottimo lavoro! Continua il tuo apprendimento

Dopo aver completato questa lezione, dai un'occhiata alla nostra [collezione di apprendimento sull'Intelligenza Artificiale Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare le tue conoscenze sull'Intelligenza Artificiale Generativa!

Passa alla Lezione 10 dove vedremo come [costruire applicazioni AI con low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.