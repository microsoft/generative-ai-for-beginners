<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:24:13+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "it"
}
-->
# Creare Applicazioni per la Generazione di Immagini

[![Creare Applicazioni per la Generazione di Immagini](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.it.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Gli LLM non servono solo per generare testo. È anche possibile creare immagini a partire da descrizioni testuali. Avere le immagini come modalità può essere molto utile in diversi ambiti, dalla MedTech, all’architettura, al turismo, allo sviluppo di videogiochi e altro ancora. In questo capitolo, esploreremo i due modelli di generazione di immagini più popolari, DALL-E e Midjourney.

## Introduzione

In questa lezione tratteremo:

- La generazione di immagini e perché è utile.
- DALL-E e Midjourney, cosa sono e come funzionano.
- Come costruire un’applicazione per la generazione di immagini.

## Obiettivi di Apprendimento

Al termine di questa lezione, sarai in grado di:

- Creare un’applicazione per la generazione di immagini.
- Definire i confini della tua applicazione con meta prompt.
- Lavorare con DALL-E e Midjourney.

## Perché creare un’applicazione per la generazione di immagini?

Le applicazioni per la generazione di immagini sono un ottimo modo per esplorare le potenzialità dell’Intelligenza Artificiale Generativa. Possono essere utilizzate, ad esempio, per:

- **Modifica e sintesi di immagini**. Puoi generare immagini per diversi casi d’uso, come la modifica o la sintesi di immagini.

- **Applicazioni in vari settori**. Possono anche essere impiegate per creare immagini in diversi settori come Medtech, Turismo, sviluppo di videogiochi e altro.

## Scenario: Edu4All

Come parte di questa lezione, continueremo a lavorare con la nostra startup, Edu4All. Gli studenti creeranno immagini per le loro valutazioni; quali immagini creare è a loro discrezione, potrebbero essere illustrazioni per una loro fiaba, un nuovo personaggio per la loro storia o aiutarli a visualizzare idee e concetti.

Ecco cosa potrebbero generare gli studenti di Edu4All, ad esempio se stanno lavorando in classe sui monumenti:

![Edu4All startup, classe sui monumenti, Torre Eiffel](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.it.png)

usando un prompt come

> "Cane accanto alla Torre Eiffel alla luce del sole del primo mattino"

## Che cosa sono DALL-E e Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) e [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sono due dei modelli di generazione di immagini più popolari, che permettono di usare prompt per generare immagini.

### DALL-E

Iniziamo con DALL-E, un modello di Intelligenza Artificiale Generativa che crea immagini a partire da descrizioni testuali.

> [DALL-E è una combinazione di due modelli, CLIP e diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** è un modello che genera embedding, ovvero rappresentazioni numeriche dei dati, da immagini e testo.

- **Diffused attention** è un modello che genera immagini a partire dagli embedding. DALL-E è addestrato su un dataset di immagini e testo e può essere usato per creare immagini da descrizioni testuali. Ad esempio, DALL-E può generare immagini di un gatto con un cappello o di un cane con un mohawk.

### Midjourney

Midjourney funziona in modo simile a DALL-E, genera immagini da prompt testuali. Midjourney può essere usato per creare immagini con prompt come “un gatto con un cappello” o “un cane con un mohawk”.

![Immagine generata da Midjourney, piccione meccanico](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)  
_Immagine da Wikipedia, generata da Midjourney_

## Come funzionano DALL-E e Midjourney

Prima, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E è un modello di Intelligenza Artificiale Generativa basato sull’architettura transformer con un _autoregressive transformer_.

Un _autoregressive transformer_ definisce come un modello genera immagini da descrizioni testuali, generando un pixel alla volta e usando i pixel generati per produrre il pixel successivo. Passa attraverso più livelli in una rete neurale, fino a completare l’immagine.

Con questo processo, DALL-E controlla attributi, oggetti, caratteristiche e altro nell’immagine che genera. Tuttavia, DALL-E 2 e 3 offrono un controllo maggiore sull’immagine generata.

## Costruire la tua prima applicazione per la generazione di immagini

Cosa serve per costruire un’applicazione per la generazione di immagini? Ti servono le seguenti librerie:

- **python-dotenv**, è altamente consigliato usare questa libreria per tenere i tuoi segreti in un file _.env_ separato dal codice.
- **openai**, questa libreria serve per interagire con l’API di OpenAI.
- **pillow**, per lavorare con le immagini in Python.
- **requests**, per aiutarti a fare richieste HTTP.

1. Crea un file _.env_ con il seguente contenuto:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Trova queste informazioni nel Portale Azure per la tua risorsa nella sezione "Keys and Endpoint".

1. Raccogli le librerie sopra in un file chiamato _requirements.txt_ così:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Poi, crea un ambiente virtuale e installa le librerie:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Per Windows, usa i seguenti comandi per creare e attivare l’ambiente virtuale:

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

- Prima importiamo le librerie necessarie, inclusa la libreria OpenAI, dotenv, requests e Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Poi carichiamo le variabili d’ambiente dal file _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Successivamente impostiamo endpoint, chiave per l’API OpenAI, versione e tipo.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Poi generiamo l’immagine:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Il codice sopra risponde con un oggetto JSON che contiene l’URL dell’immagine generata. Possiamo usare l’URL per scaricare l’immagine e salvarla su file.

- Infine, apriamo l’immagine e usiamo il visualizzatore standard per mostrarla:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Più dettagli sulla generazione dell’immagine

Vediamo il codice che genera l’immagine più nel dettaglio:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** è il testo usato per generare l’immagine. In questo caso, usiamo il prompt "Coniglio su un cavallo, che tiene un lecca-lecca, in un prato nebbioso dove crescono narcisi".
- **size** è la dimensione dell’immagine generata. Qui generiamo un’immagine di 1024x1024 pixel.
- **n** è il numero di immagini generate. Qui ne generiamo due.
- **temperature** è un parametro che controlla la casualità dell’output di un modello di Intelligenza Artificiale Generativa. La temperatura varia tra 0 e 1, dove 0 significa output deterministico e 1 output casuale. Il valore predefinito è 0.7.

Ci sono altre cose che puoi fare con le immagini, che vedremo nella sezione successiva.

## Capacità aggiuntive della generazione di immagini

Finora hai visto come generare un’immagine con poche righe di Python. Tuttavia, ci sono altre possibilità con le immagini.

Puoi anche:

- **Effettuare modifiche**. Fornendo un’immagine esistente, una maschera e un prompt, puoi modificare un’immagine. Ad esempio, puoi aggiungere qualcosa a una parte dell’immagine. Immagina la nostra immagine del coniglio, potresti aggiungere un cappello al coniglio. Per farlo, fornisci l’immagine, una maschera (che identifica la parte da modificare) e un prompt testuale che spiega cosa fare.

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

  L’immagine di base conterrebbe solo il coniglio, ma l’immagine finale avrebbe il cappello sul coniglio.

- **Creare variazioni**. L’idea è prendere un’immagine esistente e chiedere di creare variazioni. Per creare una variazione, fornisci un’immagine e un prompt testuale e un codice come questo:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Nota, questo è supportato solo su OpenAI

## Temperature

La temperatura è un parametro che controlla la casualità dell’output di un modello di Intelligenza Artificiale Generativa. La temperatura varia tra 0 e 1, dove 0 significa output deterministico e 1 output casuale. Il valore predefinito è 0.7.

Vediamo un esempio di come funziona la temperatura, eseguendo questo prompt due volte:

> Prompt: "Coniglio su un cavallo, che tiene un lecca-lecca, in un prato nebbioso dove crescono narcisi"

![Coniglio su un cavallo che tiene un lecca-lecca, versione 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.it.png)

Ora eseguiamo lo stesso prompt per vedere che non otterremo la stessa immagine due volte:

![Immagine generata di coniglio su cavallo](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.it.png)

Come vedi, le immagini sono simili, ma non identiche. Proviamo a cambiare il valore della temperatura a 0.1 e vediamo cosa succede:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Cambiare la temperatura

Proviamo a rendere la risposta più deterministica. Dalle due immagini generate, nella prima c’è un coniglio e nella seconda un cavallo, quindi le immagini variano molto.

Modifichiamo quindi il codice impostando la temperatura a 0, così:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Ora, eseguendo questo codice, ottieni queste due immagini:

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.it.png)
- ![Temperatura 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.it.png)

Qui si vede chiaramente come le immagini si somiglino molto di più.

## Come definire i confini della tua applicazione con i metaprompt

Con la nostra demo, possiamo già generare immagini per i nostri clienti. Tuttavia, dobbiamo creare dei limiti per la nostra applicazione.

Ad esempio, non vogliamo generare immagini non adatte al lavoro o inappropriate per i bambini.

Possiamo farlo con i _metaprompt_. I metaprompt sono prompt testuali usati per controllare l’output di un modello di Intelligenza Artificiale Generativa. Ad esempio, possiamo usare i metaprompt per garantire che le immagini generate siano sicure per il lavoro o adatte ai bambini.

### Come funziona?

Come funzionano i metaprompt?

I metaprompt sono prompt testuali usati per controllare l’output di un modello di Intelligenza Artificiale Generativa, vengono posizionati prima del prompt testuale e servono a controllare l’output del modello, integrandosi nelle applicazioni per gestire l’output. Racchiudono l’input del prompt e quello del metaprompt in un unico prompt testuale.

Un esempio di metaprompt potrebbe essere il seguente:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Ora vediamo come usare i metaprompt nella nostra demo.

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

Dal prompt sopra, puoi vedere come tutte le immagini generate tengano conto del metaprompt.

## Compito - abilitiamo gli studenti

Abbiamo introdotto Edu4All all’inizio di questa lezione. Ora è il momento di permettere agli studenti di generare immagini per le loro valutazioni.

Gli studenti creeranno immagini per le loro valutazioni contenenti monumenti, quali monumenti esattamente è a loro scelta. Gli studenti sono invitati a usare la loro creatività per collocare questi monumenti in contesti diversi.

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

## Ottimo lavoro! Continua a imparare

Dopo aver completato questa lezione, dai un’occhiata alla nostra [collezione di apprendimento sull’Intelligenza Artificiale Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare le tue conoscenze sull’IA Generativa!

Passa alla Lezione 10 dove vedremo come [creare applicazioni AI con low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.