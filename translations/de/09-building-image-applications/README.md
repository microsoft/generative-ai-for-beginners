<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:03:37+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "de"
}
-->
# Erstellung von Anwendungen zur Bildgenerierung

Es gibt mehr bei LLMs als nur Textgenerierung. Es ist auch möglich, Bilder aus Textbeschreibungen zu erzeugen. Bilder als Modalität können in vielen Bereichen sehr nützlich sein, von MedTech über Architektur, Tourismus, Spieleentwicklung und mehr. In diesem Kapitel werden wir uns die beiden bekanntesten Modelle zur Bildgenerierung, DALL-E und Midjourney, ansehen.

## Einführung

In dieser Lektion werden wir behandeln:

- Bildgenerierung und warum sie nützlich ist.
- DALL-E und Midjourney, was sie sind und wie sie funktionieren.
- Wie man eine Anwendung zur Bildgenerierung erstellt.

## Lernziele

Nach Abschluss dieser Lektion werden Sie in der Lage sein:

- Eine Anwendung zur Bildgenerierung zu erstellen.
- Grenzen für Ihre Anwendung mit Metaprompts zu definieren.
- Mit DALL-E und Midjourney zu arbeiten.

## Warum eine Anwendung zur Bildgenerierung erstellen?

Anwendungen zur Bildgenerierung sind eine großartige Möglichkeit, die Fähigkeiten der generativen KI zu erkunden. Sie können beispielsweise für Folgendes verwendet werden:

- **Bildbearbeitung und -synthese**. Sie können Bilder für eine Vielzahl von Anwendungsfällen erzeugen, wie z.B. Bildbearbeitung und Bildsynthese.

- **Anwendung in verschiedenen Branchen**. Sie können auch zur Erzeugung von Bildern für verschiedene Branchen wie MedTech, Tourismus, Spieleentwicklung und mehr verwendet werden.

## Szenario: Edu4All

Im Rahmen dieser Lektion werden wir weiterhin mit unserem Startup, Edu4All, arbeiten. Die Schüler werden Bilder für ihre Aufgaben erstellen, welche Bilder genau ist den Schülern überlassen, aber sie könnten Illustrationen für ihr eigenes Märchen sein oder einen neuen Charakter für ihre Geschichte erschaffen oder ihnen helfen, ihre Ideen und Konzepte zu visualisieren.

Hier ist ein Beispiel dafür, was Edu4Alls Schüler generieren könnten, wenn sie im Unterricht an Denkmälern arbeiten:

![Edu4All Startup, Unterricht über Denkmäler, Eiffelturm](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.de.png)

mit einem Prompt wie

> "Hund neben dem Eiffelturm im frühen Morgenlicht"

## Was sind DALL-E und Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) und [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sind zwei der bekanntesten Modelle zur Bildgenerierung, die es ermöglichen, Bilder mithilfe von Prompts zu erzeugen.

### DALL-E

Beginnen wir mit DALL-E, einem generativen KI-Modell, das Bilder aus Textbeschreibungen generiert.

> [DALL-E ist eine Kombination aus zwei Modellen, CLIP und diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** ist ein Modell, das Einbettungen generiert, die numerische Darstellungen von Daten aus Bildern und Texten sind.

- **Diffused attention** ist ein Modell, das Bilder aus Einbettungen generiert. DALL-E ist auf einem Datensatz von Bildern und Texten trainiert und kann verwendet werden, um Bilder aus Textbeschreibungen zu generieren. Zum Beispiel kann DALL-E verwendet werden, um Bilder von einer Katze im Hut oder einem Hund mit einem Irokesenschnitt zu generieren.

### Midjourney

Midjourney funktioniert ähnlich wie DALL-E, es generiert Bilder aus Textprompts. Midjourney kann ebenfalls verwendet werden, um Bilder mit Prompts wie „eine Katze im Hut“ oder „ein Hund mit einem Irokesenschnitt“ zu generieren.

![Bild generiert von Midjourney, mechanische Taube](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Bildquelle Wikipedia, Bild generiert von Midjourney_

## Wie funktionieren DALL-E und Midjourney

Zuerst [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E ist ein generatives KI-Modell basierend auf der Transformer-Architektur mit einem _autoregressiven Transformer_.

Ein _autoregressiver Transformer_ definiert, wie ein Modell Bilder aus Textbeschreibungen generiert, es generiert einen Pixel nach dem anderen und verwendet dann die generierten Pixel, um den nächsten Pixel zu generieren. Dabei durchläuft es mehrere Schichten in einem neuronalen Netzwerk, bis das Bild vollständig ist.

Mit diesem Prozess kontrolliert DALL-E Attribute, Objekte, Merkmale und mehr im generierten Bild. DALL-E 2 und 3 haben jedoch mehr Kontrolle über das generierte Bild.

## Erstellung Ihrer ersten Anwendung zur Bildgenerierung

Was braucht es also, um eine Anwendung zur Bildgenerierung zu erstellen? Sie benötigen die folgenden Bibliotheken:

- **python-dotenv**, es wird dringend empfohlen, diese Bibliothek zu verwenden, um Ihre Geheimnisse in einer _.env_-Datei vom Code fernzuhalten.
- **openai**, diese Bibliothek wird verwendet, um mit der OpenAI-API zu interagieren.
- **pillow**, um mit Bildern in Python zu arbeiten.
- **requests**, um Ihnen bei der Erstellung von HTTP-Anfragen zu helfen.

1. Erstellen Sie eine Datei _.env_ mit folgendem Inhalt:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Finden Sie diese Informationen im Azure-Portal für Ihre Ressource im Abschnitt "Schlüssel und Endpunkt".

1. Sammeln Sie die oben genannten Bibliotheken in einer Datei namens _requirements.txt_ wie folgt:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Erstellen Sie als Nächstes eine virtuelle Umgebung und installieren Sie die Bibliotheken:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Für Windows verwenden Sie die folgenden Befehle, um Ihre virtuelle Umgebung zu erstellen und zu aktivieren:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Fügen Sie den folgenden Code in eine Datei namens _app.py_ ein:

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

Lassen Sie uns diesen Code erklären:

- Zuerst importieren wir die benötigten Bibliotheken, einschließlich der OpenAI-Bibliothek, der dotenv-Bibliothek, der requests-Bibliothek und der Pillow-Bibliothek.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Als Nächstes laden wir die Umgebungsvariablen aus der _.env_-Datei.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Danach setzen wir den Endpunkt, den Schlüssel für die OpenAI-API, die Version und den Typ.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Als Nächstes generieren wir das Bild:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Der obige Code antwortet mit einem JSON-Objekt, das die URL des generierten Bildes enthält. Wir können die URL verwenden, um das Bild herunterzuladen und in einer Datei zu speichern.

- Schließlich öffnen wir das Bild und verwenden den Standard-Bildbetrachter, um es anzuzeigen:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Weitere Details zur Bildgenerierung

Schauen wir uns den Code, der das Bild generiert, genauer an:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, ist der Textprompt, der verwendet wird, um das Bild zu generieren. In diesem Fall verwenden wir den Prompt "Hase auf Pferd, der einen Lutscher hält, auf einer nebligen Wiese, auf der Narzissen wachsen".
- **size**, ist die Größe des generierten Bildes. In diesem Fall generieren wir ein Bild, das 1024x1024 Pixel groß ist.
- **n**, ist die Anzahl der generierten Bilder. In diesem Fall generieren wir zwei Bilder.
- **temperature**, ist ein Parameter, der die Zufälligkeit der Ausgabe eines generativen KI-Modells steuert. Die Temperatur ist ein Wert zwischen 0 und 1, wobei 0 bedeutet, dass die Ausgabe deterministisch ist und 1 bedeutet, dass die Ausgabe zufällig ist. Der Standardwert ist 0,7.

Es gibt mehr Dinge, die Sie mit Bildern tun können, die wir im nächsten Abschnitt behandeln werden.

## Zusätzliche Fähigkeiten der Bildgenerierung

Sie haben bisher gesehen, wie wir in Python mit nur wenigen Zeilen ein Bild generieren konnten. Es gibt jedoch mehr Dinge, die Sie mit Bildern tun können.

Sie können auch Folgendes tun:

- **Bearbeitungen durchführen**. Indem Sie ein vorhandenes Bild, eine Maske und einen Prompt bereitstellen, können Sie ein Bild ändern. Zum Beispiel können Sie etwas zu einem Teil eines Bildes hinzufügen. Stellen Sie sich unser Hasenbild vor, Sie können dem Hasen einen Hut hinzufügen. Wie Sie das tun würden, ist, indem Sie das Bild, eine Maske (die den Bereich für die Änderung identifiziert) und einen Textprompt bereitstellen, um zu sagen, was getan werden soll.

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

  Das Basisbild würde nur den Hasen enthalten, aber das endgültige Bild hätte den Hut auf dem Hasen.

- **Variationen erstellen**. Die Idee ist, dass Sie ein vorhandenes Bild nehmen und verlangen, dass Variationen erstellt werden. Um eine Variation zu erstellen, geben Sie ein Bild und einen Textprompt an und verwenden Code wie folgt:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Hinweis, dies wird nur von OpenAI unterstützt

## Temperatur

Die Temperatur ist ein Parameter, der die Zufälligkeit der Ausgabe eines generativen KI-Modells steuert. Die Temperatur ist ein Wert zwischen 0 und 1, wobei 0 bedeutet, dass die Ausgabe deterministisch ist und 1 bedeutet, dass die Ausgabe zufällig ist. Der Standardwert ist 0,7.

Schauen wir uns ein Beispiel an, wie die Temperatur funktioniert, indem wir diesen Prompt zweimal ausführen:

> Prompt : "Hase auf Pferd, der einen Lutscher hält, auf einer nebligen Wiese, auf der Narzissen wachsen"

![Hase auf einem Pferd, der einen Lutscher hält, Version 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.de.png)

Jetzt lassen Sie uns denselben Prompt erneut ausführen, um zu sehen, dass wir nicht zweimal dasselbe Bild erhalten:

![Generiertes Bild eines Hasen auf einem Pferd](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.de.png)

Wie Sie sehen können, sind die Bilder ähnlich, aber nicht identisch. Lassen Sie uns versuchen, den Temperaturwert auf 0,1 zu ändern und sehen, was passiert:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Ändern der Temperatur

Versuchen wir also, die Antwort deterministischer zu gestalten. Wir konnten aus den beiden generierten Bildern beobachten, dass im ersten Bild ein Hase und im zweiten Bild ein Pferd zu sehen ist, sodass sich die Bilder stark unterscheiden.

Lassen Sie uns daher unseren Code ändern und die Temperatur auf 0 setzen, wie folgt:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Wenn Sie diesen Code jetzt ausführen, erhalten Sie diese beiden Bilder:

- ![Temperatur 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.de.png)
- ![Temperatur 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.de.png)

Hier können Sie deutlich sehen, wie sich die Bilder einander mehr ähneln.

## Wie man Grenzen für Ihre Anwendung mit Metaprompts definiert

Mit unserer Demo können wir bereits Bilder für unsere Kunden generieren. Wir müssen jedoch einige Grenzen für unsere Anwendung schaffen.

Zum Beispiel möchten wir keine Bilder generieren, die nicht sicher für die Arbeit sind oder die nicht für Kinder geeignet sind.

Das können wir mit _Metaprompts_ tun. Metaprompts sind Textprompts, die verwendet werden, um die Ausgabe eines generativen KI-Modells zu steuern. Zum Beispiel können wir Metaprompts verwenden, um die Ausgabe zu steuern und sicherzustellen, dass die generierten Bilder sicher für die Arbeit sind oder für Kinder geeignet sind.

### Wie funktioniert es?

Wie funktionieren Metaprompts?

Metaprompts sind Textprompts, die verwendet werden, um die Ausgabe eines generativen KI-Modells zu steuern, sie werden vor dem Textprompt positioniert und verwendet, um die Ausgabe des Modells zu steuern und in Anwendungen eingebettet, um die Ausgabe des Modells zu steuern. Sie kapseln den Prompt-Input und den Metaprompt-Input in einem einzigen Textprompt ein.

Ein Beispiel für einen Metaprompt wäre das folgende:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Sehen wir uns nun an, wie wir Metaprompts in unserer Demo verwenden können.

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

Aus dem obigen Prompt können Sie sehen, wie alle erstellten Bilder den Metaprompt berücksichtigen.

## Aufgabe - Lass uns die Schüler befähigen

Wir haben Edu4All zu Beginn dieser Lektion vorgestellt. Jetzt ist es an der Zeit, den Schülern zu ermöglichen, Bilder für ihre Aufgaben zu generieren.

Die Schüler werden Bilder für ihre Aufgaben mit Denkmälern erstellen, welche Denkmäler genau ist den Schülern überlassen. Die Schüler werden aufgefordert, bei dieser Aufgabe ihre Kreativität einzusetzen, um diese Denkmäler in verschiedenen Kontexten zu platzieren.

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

## Gute Arbeit! Setzen Sie Ihr Lernen fort

Nach Abschluss dieser Lektion, schauen Sie sich unsere [Generative AI Learning Collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über generative KI weiter zu vertiefen!

Gehen Sie zu Lektion 10, wo wir uns ansehen, wie man [KI-Anwendungen mit wenig Code erstellt](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.