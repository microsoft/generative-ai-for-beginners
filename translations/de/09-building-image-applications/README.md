<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T10:34:04+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "de"
}
-->
# Erstellung von Anwendungen zur Bildgenerierung

Es gibt mehr als nur Textgenerierung bei LLMs. Es ist auch möglich, Bilder aus Textbeschreibungen zu generieren. Bilder als Modalität zu haben, kann in vielen Bereichen wie MedTech, Architektur, Tourismus, Spieleentwicklung und mehr äußerst nützlich sein. In diesem Kapitel werden wir uns die beiden bekanntesten Bildgenerierungsmodelle, DALL-E und Midjourney, ansehen.

## Einführung

In dieser Lektion werden wir folgende Themen behandeln:

- Bildgenerierung und warum sie nützlich ist.
- DALL-E und Midjourney, was sie sind und wie sie funktionieren.
- Wie man eine Anwendung zur Bildgenerierung erstellt.

## Lernziele

Nach Abschluss dieser Lektion werden Sie in der Lage sein:

- Eine Anwendung zur Bildgenerierung zu erstellen.
- Grenzen für Ihre Anwendung mit Metaprompts zu definieren.
- Mit DALL-E und Midjourney zu arbeiten.

## Warum eine Anwendung zur Bildgenerierung erstellen?

Anwendungen zur Bildgenerierung sind eine großartige Möglichkeit, die Fähigkeiten von Generativer KI zu erkunden. Sie können beispielsweise verwendet werden für:

- **Bildbearbeitung und Synthese**. Sie können Bilder für verschiedene Anwendungsfälle generieren, wie zum Beispiel Bildbearbeitung und Bildsynthese.

- **Anwendung in verschiedenen Branchen**. Sie können auch verwendet werden, um Bilder für verschiedene Branchen wie MedTech, Tourismus, Spieleentwicklung und mehr zu generieren.

## Szenario: Edu4All

Im Rahmen dieser Lektion werden wir weiterhin mit unserem Startup Edu4All arbeiten. Die Schüler werden Bilder für ihre Bewertungen erstellen, welche Bilder genau, bleibt den Schülern überlassen. Sie könnten Illustrationen für ihr eigenes Märchen oder einen neuen Charakter für ihre Geschichte erstellen oder ihnen helfen, ihre Ideen und Konzepte zu visualisieren.

Hier ist ein Beispiel dafür, was Edu4All-Schüler generieren könnten, wenn sie im Unterricht an Denkmälern arbeiten:

![Edu4All Startup, Unterricht über Denkmäler, Eiffelturm](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.de.png)

mit einem Prompt wie

> "Hund neben dem Eiffelturm im frühen Morgenlicht"

## Was ist DALL-E und Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) und [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sind zwei der bekanntesten Bildgenerierungsmodelle, die es ermöglichen, mithilfe von Prompts Bilder zu generieren.

### DALL-E

Beginnen wir mit DALL-E, einem Generativen KI-Modell, das Bilder aus Textbeschreibungen generiert.

> [DALL-E ist eine Kombination aus zwei Modellen, CLIP und diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** ist ein Modell, das Einbettungen generiert, also numerische Darstellungen von Daten, aus Bildern und Text.

- **Diffused attention** ist ein Modell, das Bilder aus Einbettungen generiert. DALL-E ist auf einem Datensatz von Bildern und Text trainiert und kann verwendet werden, um Bilder aus Textbeschreibungen zu generieren. Zum Beispiel kann DALL-E verwendet werden, um Bilder von einer Katze mit Hut oder einem Hund mit Irokesen zu generieren.

### Midjourney

Midjourney funktioniert ähnlich wie DALL-E und generiert Bilder aus Text-Prompts. Midjourney kann auch verwendet werden, um Bilder mit Prompts wie „eine Katze mit Hut“ oder „ein Hund mit Irokesen“ zu generieren.

![Von Midjourney generiertes Bild, mechanische Taube](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Bildnachweis Wikipedia, Bild generiert von Midjourney_

## Wie funktionieren DALL-E und Midjourney?

Zuerst [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E ist ein Generatives KI-Modell basierend auf der Transformer-Architektur mit einem _autoregressiven Transformer_.

Ein _autoregressiver Transformer_ definiert, wie ein Modell Bilder aus Textbeschreibungen generiert. Es generiert ein Pixel nach dem anderen und verwendet die generierten Pixel, um das nächste Pixel zu generieren. Es durchläuft dabei mehrere Schichten in einem neuronalen Netzwerk, bis das Bild vollständig ist.

Mit diesem Prozess kontrolliert DALL-E Attribute, Objekte, Eigenschaften und mehr in dem Bild, das es generiert. DALL-E 2 und 3 haben jedoch mehr Kontrolle über das generierte Bild.

## Ihre erste Anwendung zur Bildgenerierung erstellen

Was braucht es also, um eine Anwendung zur Bildgenerierung zu erstellen? Sie benötigen folgende Bibliotheken:

- **python-dotenv**, es wird dringend empfohlen, diese Bibliothek zu verwenden, um Ihre Geheimnisse in einer _.env_-Datei fern vom Code zu speichern.
- **openai**, diese Bibliothek wird verwendet, um mit der OpenAI-API zu interagieren.
- **pillow**, um mit Bildern in Python zu arbeiten.
- **requests**, um HTTP-Anfragen zu stellen.

1. Erstellen Sie eine Datei _.env_ mit folgendem Inhalt:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Suchen Sie diese Informationen im Azure-Portal für Ihre Ressource im Abschnitt „Schlüssel und Endpunkt“.

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

- Schließlich öffnen wir das Bild und verwenden den Standardbildbetrachter, um es anzuzeigen:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Weitere Details zur Bildgenerierung

Lassen Sie uns den Code, der das Bild generiert, genauer betrachten:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** ist der Text-Prompt, der zur Generierung des Bildes verwendet wird. In diesem Fall verwenden wir den Prompt „Hase auf Pferd, hält einen Lutscher, auf einer nebligen Wiese, auf der Narzissen wachsen“.
- **size** ist die Größe des generierten Bildes. In diesem Fall generieren wir ein Bild mit einer Größe von 1024x1024 Pixeln.
- **n** ist die Anzahl der generierten Bilder. In diesem Fall generieren wir zwei Bilder.
- **temperature** ist ein Parameter, der die Zufälligkeit der Ausgabe eines Generativen KI-Modells steuert. Die Temperatur ist ein Wert zwischen 0 und 1, wobei 0 bedeutet, dass die Ausgabe deterministisch ist und 1 bedeutet, dass die Ausgabe zufällig ist. Der Standardwert ist 0,7.

Es gibt noch mehr, was Sie mit Bildern tun können, was wir im nächsten Abschnitt behandeln werden.

## Zusätzliche Fähigkeiten der Bildgenerierung

Sie haben bisher gesehen, wie wir mit wenigen Zeilen in Python ein Bild generieren konnten. Es gibt jedoch noch mehr, was Sie mit Bildern tun können.

Sie können auch Folgendes tun:

- **Bearbeitungen durchführen**. Indem Sie ein vorhandenes Bild, eine Maske und einen Prompt bereitstellen, können Sie ein Bild ändern. Zum Beispiel können Sie etwas zu einem Teil eines Bildes hinzufügen. Stellen Sie sich unser Hasenbild vor, Sie können dem Hasen einen Hut hinzufügen. Wie Sie das tun würden, ist, indem Sie das Bild, eine Maske (die den Bereich für die Änderung identifiziert) und einen Text-Prompt bereitstellen, der angibt, was getan werden soll.

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

- **Variationen erstellen**. Die Idee ist, dass Sie ein vorhandenes Bild nehmen und fragen, dass Variationen erstellt werden. Um eine Variation zu erstellen, geben Sie ein Bild und einen Text-Prompt an und verwenden Code wie folgt:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Hinweis: Dies wird nur auf OpenAI unterstützt

## Temperatur

Temperatur ist ein Parameter, der die Zufälligkeit der Ausgabe eines Generativen KI-Modells steuert. Die Temperatur ist ein Wert zwischen 0 und 1, wobei 0 bedeutet, dass die Ausgabe deterministisch ist und 1 bedeutet, dass die Ausgabe zufällig ist. Der Standardwert ist 0,7.

Lassen Sie uns ein Beispiel dafür betrachten, wie die Temperatur funktioniert, indem wir diesen Prompt zweimal ausführen:

> Prompt: „Hase auf Pferd, hält einen Lutscher, auf einer nebligen Wiese, auf der Narzissen wachsen“

![Hase auf einem Pferd, hält einen Lutscher, Version 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.de.png)

Nun lassen Sie uns denselben Prompt erneut ausführen, um zu sehen, dass wir nicht zweimal dasselbe Bild erhalten:

![Generiertes Bild von Hase auf Pferd](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.de.png)

Wie Sie sehen können, sind die Bilder ähnlich, aber nicht identisch. Lassen Sie uns versuchen, den Temperaturwert auf 0,1 zu ändern und sehen, was passiert:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Ändern der Temperatur

Versuchen wir also, die Antwort deterministischer zu machen. Wir konnten aus den beiden generierten Bildern beobachten, dass im ersten Bild ein Hase und im zweiten Bild ein Pferd zu sehen ist, sodass sich die Bilder stark unterscheiden.

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

- ![Temperatur 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.de.png)
- ![Temperatur 0, v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.de.png)

Hier können Sie deutlich sehen, wie sich die Bilder mehr ähneln.

## Wie man Grenzen für Ihre Anwendung mit Metaprompts definiert

Mit unserem Demo können wir bereits Bilder für unsere Kunden generieren. Wir müssen jedoch einige Grenzen für unsere Anwendung festlegen.

Zum Beispiel wollen wir keine Bilder generieren, die nicht sicher für die Arbeit sind oder die nicht für Kinder geeignet sind.

Wir können dies mit _Metaprompts_ tun. Metaprompts sind Text-Prompts, die verwendet werden, um die Ausgabe eines Generativen KI-Modells zu steuern. Zum Beispiel können wir Metaprompts verwenden, um die Ausgabe zu kontrollieren und sicherzustellen, dass die generierten Bilder sicher für die Arbeit oder für Kinder geeignet sind.

### Wie funktioniert das?

Wie funktionieren Metaprompts?

Metaprompts sind Text-Prompts, die verwendet werden, um die Ausgabe eines Generativen KI-Modells zu steuern. Sie werden vor dem Text-Prompt positioniert und verwendet, um die Ausgabe des Modells zu steuern und in Anwendungen eingebettet, um die Ausgabe des Modells zu steuern. Sie kapseln den Prompt-Eingang und den Metaprompt-Eingang in einem einzigen Text-Prompt.

Ein Beispiel für ein Metaprompt wäre das folgende:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Lassen Sie uns nun sehen, wie wir Metaprompts in unserem Demo verwenden können.

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

Aus dem obigen Prompt können Sie sehen, wie alle erstellten Bilder das Metaprompt berücksichtigen.

## Aufgabe - Lass uns die Schüler befähigen

Wir haben Edu4All zu Beginn dieser Lektion eingeführt. Jetzt ist es an der Zeit, die Schüler zu befähigen, Bilder für ihre Bewertungen zu generieren.

Die Schüler werden Bilder für ihre Bewertungen erstellen, die Denkmäler enthalten. Welche Denkmäler genau, bleibt den Schülern überlassen. Die Schüler werden gebeten, ihrer Kreativität bei dieser Aufgabe freien Lauf zu lassen und diese Denkmäler in verschiedene Kontexte zu setzen.

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

## Großartige Arbeit! Setzen Sie Ihr Lernen fort

Nach Abschluss dieser Lektion schauen Sie sich unsere [Generative AI Learning Collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über Generative KI weiter zu vertiefen!

Gehen Sie zu Lektion 10, wo wir uns ansehen, wie man [AI-Anwendungen mit Low-Code erstellt](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.