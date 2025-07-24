<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:15:16+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "de"
}
-->
# Entwicklung von Bildgenerierungsanwendungen

[![Entwicklung von Bildgenerierungsanwendungen](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.de.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMs können mehr als nur Text generieren. Es ist auch möglich, Bilder aus Textbeschreibungen zu erzeugen. Bilder als Modalität zu haben, kann in vielen Bereichen sehr nützlich sein, von MedTech, Architektur, Tourismus, Spieleentwicklung und mehr. In diesem Kapitel schauen wir uns die zwei beliebtesten Bildgenerierungsmodelle an: DALL-E und Midjourney.

## Einführung

In dieser Lektion behandeln wir:

- Bildgenerierung und warum sie nützlich ist.
- DALL-E und Midjourney: Was sie sind und wie sie funktionieren.
- Wie man eine Bildgenerierungsanwendung erstellt.

## Lernziele

Nach Abschluss dieser Lektion wirst du in der Lage sein:

- Eine Bildgenerierungsanwendung zu erstellen.
- Grenzen für deine Anwendung mit Metaprompts zu definieren.
- Mit DALL-E und Midjourney zu arbeiten.

## Warum eine Bildgenerierungsanwendung entwickeln?

Bildgenerierungsanwendungen sind eine großartige Möglichkeit, die Fähigkeiten von Generativer KI zu erkunden. Sie können beispielsweise verwendet werden für:

- **Bildbearbeitung und -synthese**. Du kannst Bilder für verschiedene Anwendungsfälle generieren, wie Bildbearbeitung und Bildsynthese.

- **Anwendung in verschiedenen Branchen**. Sie können auch genutzt werden, um Bilder für verschiedene Branchen zu erzeugen, wie MedTech, Tourismus, Spieleentwicklung und mehr.

## Szenario: Edu4All

Im Rahmen dieser Lektion arbeiten wir weiterhin mit unserem Startup Edu4All. Die Schüler erstellen Bilder für ihre Aufgaben. Welche Bilder genau, entscheiden die Schüler selbst – es könnten Illustrationen für ihr eigenes Märchen sein, ein neuer Charakter für ihre Geschichte oder eine Visualisierung ihrer Ideen und Konzepte.

So könnten die Schüler von Edu4All zum Beispiel Bilder generieren, wenn sie im Unterricht an Denkmälern arbeiten:

![Edu4All Startup, Unterricht zu Denkmälern, Eiffelturm](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.de.png)

mit einem Prompt wie

> "Hund neben dem Eiffelturm im frühen Morgenlicht"

## Was sind DALL-E und Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) und [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sind zwei der beliebtesten Bildgenerierungsmodelle, mit denen du Bilder anhand von Prompts erzeugen kannst.

### DALL-E

Beginnen wir mit DALL-E, einem Generativen KI-Modell, das Bilder aus Textbeschreibungen erzeugt.

> [DALL-E ist eine Kombination aus zwei Modellen, CLIP und diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** ist ein Modell, das Embeddings erzeugt, also numerische Darstellungen von Daten, aus Bildern und Text.

- **Diffused attention** ist ein Modell, das Bilder aus Embeddings generiert. DALL-E wurde mit einem Datensatz aus Bildern und Text trainiert und kann Bilder aus Textbeschreibungen erzeugen. Zum Beispiel kann DALL-E Bilder von einer Katze mit Hut oder einem Hund mit Irokesenschnitt generieren.

### Midjourney

Midjourney funktioniert ähnlich wie DALL-E und erzeugt Bilder aus Textprompts. Midjourney kann ebenfalls Bilder generieren, z. B. „eine Katze mit Hut“ oder „ein Hund mit Irokesenschnitt“.

![Von Midjourney generiertes Bild, mechanische Taube](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)  
_Bildquelle Wikipedia, Bild generiert von Midjourney_

## Wie funktionieren DALL-E und Midjourney?

Zuerst [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E ist ein Generatives KI-Modell, das auf der Transformer-Architektur basiert und einen _autoregressiven Transformer_ verwendet.

Ein _autoregressiver Transformer_ definiert, wie ein Modell Bilder aus Textbeschreibungen generiert: Es erzeugt Pixel für Pixel, wobei jeder neue Pixel auf den bereits generierten Pixeln basiert. Dabei durchläuft es mehrere Schichten in einem neuronalen Netzwerk, bis das Bild fertiggestellt ist.

Mit diesem Verfahren steuert DALL-E Attribute, Objekte, Eigenschaften und mehr im generierten Bild. DALL-E 2 und 3 bieten dabei noch mehr Kontrolle über das erzeugte Bild.

## Deine erste Bildgenerierungsanwendung erstellen

Was braucht man, um eine Bildgenerierungsanwendung zu bauen? Du benötigst folgende Bibliotheken:

- **python-dotenv**: Es wird dringend empfohlen, diese Bibliothek zu verwenden, um deine Geheimnisse in einer _.env_-Datei vom Code getrennt zu halten.
- **openai**: Diese Bibliothek nutzt du, um mit der OpenAI API zu interagieren.
- **pillow**: Zum Arbeiten mit Bildern in Python.
- **requests**: Um HTTP-Anfragen zu stellen.

1. Erstelle eine Datei _.env_ mit folgendem Inhalt:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Diese Informationen findest du im Azure-Portal für deine Ressource im Bereich „Keys and Endpoint“.

1. Sammle die oben genannten Bibliotheken in einer Datei namens _requirements.txt_ wie folgt:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Erstelle anschließend eine virtuelle Umgebung und installiere die Bibliotheken:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Für Windows verwende folgende Befehle, um die virtuelle Umgebung zu erstellen und zu aktivieren:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Füge folgenden Code in eine Datei namens _app.py_ ein:

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

Erklärung des Codes:

- Zuerst importieren wir die benötigten Bibliotheken, darunter die OpenAI-Bibliothek, dotenv, requests und Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Danach laden wir die Umgebungsvariablen aus der _.env_-Datei.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Anschließend setzen wir den Endpunkt, den Schlüssel für die OpenAI API, Version und Typ.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Danach generieren wir das Bild:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Der obige Code liefert ein JSON-Objekt mit der URL des generierten Bildes. Diese URL können wir nutzen, um das Bild herunterzuladen und zu speichern.

- Zum Schluss öffnen wir das Bild und zeigen es mit dem Standardbildbetrachter an:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Mehr Details zur Bildgenerierung

Schauen wir uns den Code zur Bildgenerierung genauer an:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** ist der Textprompt, der zur Bildgenerierung verwendet wird. In diesem Fall: „Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils“.
- **size** ist die Größe des generierten Bildes. Hier erzeugen wir ein Bild mit 1024x1024 Pixeln.
- **n** ist die Anzahl der generierten Bilder. Hier erzeugen wir zwei Bilder.
- **temperature** ist ein Parameter, der die Zufälligkeit der Ausgabe eines Generativen KI-Modells steuert. Der Wert liegt zwischen 0 und 1, wobei 0 eine deterministische Ausgabe bedeutet und 1 eine zufällige. Der Standardwert ist 0,7.

Es gibt noch weitere Möglichkeiten mit Bildern, die wir im nächsten Abschnitt behandeln.

## Zusätzliche Funktionen der Bildgenerierung

Du hast bisher gesehen, wie wir mit wenigen Zeilen Python-Code ein Bild generieren konnten. Es gibt jedoch noch mehr, was du mit Bildern machen kannst.

Du kannst außerdem:

- **Bearbeitungen durchführen**. Indem du ein bestehendes Bild, eine Maske und einen Prompt angibst, kannst du ein Bild verändern. Zum Beispiel kannst du einem Teil eines Bildes etwas hinzufügen. Stell dir unser Kaninchenbild vor: Du könntest dem Kaninchen einen Hut aufsetzen. Dazu gibst du das Bild, eine Maske (die den Bereich für die Änderung markiert) und einen Textprompt an, der beschreibt, was gemacht werden soll.

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

  Das Ausgangsbild enthält nur das Kaninchen, das Endbild zeigt das Kaninchen mit Hut.

- **Variationen erstellen**. Die Idee ist, ein bestehendes Bild zu nehmen und Variationen davon zu erzeugen. Um eine Variation zu erstellen, gibst du ein Bild und einen Textprompt an und nutzt Code wie diesen:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Hinweis: Dies wird nur von OpenAI unterstützt.

## Temperature

Temperature ist ein Parameter, der die Zufälligkeit der Ausgabe eines Generativen KI-Modells steuert. Der Wert liegt zwischen 0 und 1, wobei 0 eine deterministische Ausgabe bedeutet und 1 eine zufällige. Der Standardwert ist 0,7.

Schauen wir uns ein Beispiel an, wie Temperature wirkt, indem wir diesen Prompt zweimal ausführen:

> Prompt: "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Kaninchen auf Pferd mit Lutscher, Version 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.de.png)

Nun führen wir denselben Prompt noch einmal aus, um zu sehen, dass wir nicht zweimal dasselbe Bild erhalten:

![Generiertes Bild von Kaninchen auf Pferd](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.de.png)

Wie du siehst, sind die Bilder ähnlich, aber nicht identisch. Versuchen wir, den Temperature-Wert auf 0,1 zu setzen und schauen, was passiert:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Temperature ändern

Versuchen wir also, die Ausgabe deterministischer zu machen. Bei den zwei generierten Bildern sieht man, dass im ersten Bild ein Kaninchen zu sehen ist, im zweiten ein Pferd – die Bilder unterscheiden sich stark.

Ändern wir daher unseren Code und setzen die Temperature auf 0, so:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Wenn du diesen Code ausführst, erhältst du diese zwei Bilder:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.de.png)
- ![Temperature 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.de.png)

Hier sieht man deutlich, wie sich die Bilder stärker ähneln.

## Wie man Grenzen für die Anwendung mit Metaprompts definiert

Mit unserer Demo können wir bereits Bilder für unsere Kunden generieren. Allerdings müssen wir Grenzen für unsere Anwendung setzen.

Zum Beispiel wollen wir keine Bilder erzeugen, die nicht jugendfrei sind oder für Kinder ungeeignet.

Das erreichen wir mit _Metaprompts_. Metaprompts sind Textprompts, die verwendet werden, um die Ausgabe eines Generativen KI-Modells zu steuern. So können wir sicherstellen, dass die generierten Bilder jugendfrei oder kindgerecht sind.

### Wie funktioniert das?

Wie funktionieren Metaprompts?

Metaprompts sind Textprompts, die vor dem eigentlichen Textprompt stehen und die Ausgabe des Modells steuern. Sie werden in Anwendungen eingebettet, um die Ausgabe zu kontrollieren, indem sie den eigentlichen Prompt und den Metaprompt in einem einzigen Textprompt zusammenfassen.

Ein Beispiel für einen Metaprompt wäre:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Schauen wir uns nun an, wie wir Metaprompts in unserer Demo verwenden können.

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

Aus dem obigen Prompt siehst du, wie alle generierten Bilder den Metaprompt berücksichtigen.

## Aufgabe – Lass die Schüler aktiv werden

Wir haben Edu4All zu Beginn dieser Lektion vorgestellt. Jetzt ist es an der Zeit, die Schüler zu befähigen, Bilder für ihre Aufgaben zu generieren.

Die Schüler sollen Bilder mit Denkmälern für ihre Aufgaben erstellen. Welche Denkmäler genau, entscheiden die Schüler selbst. Sie werden aufgefordert, ihre Kreativität einzusetzen und die Denkmäler in verschiedenen Kontexten darzustellen.

## Lösung

Hier ist eine mögliche Lösung:

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

## Gute Arbeit! Setze dein Lernen fort

Nach Abschluss dieser Lektion schau dir unsere [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um dein Wissen über Generative KI weiter auszubauen!

Gehe weiter zu Lektion 10, in der wir uns anschauen, wie man [KI-Anwendungen mit Low-Code entwickelt](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.