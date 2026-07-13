# Erstellung von Bildgenerierungsanwendungen

[![Erstellung von Bildgenerierungsanwendungen](../../../translated_images/de/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLMs können mehr als nur Text generieren. Es ist auch möglich, Bilder aus Textbeschreibungen zu erzeugen. Bilder als Modalität können in verschiedenen Bereichen wie Medizintechnik, Architektur, Tourismus, Spieleentwicklung und mehr sehr nützlich sein. In diesem Kapitel betrachten wir die beiden beliebtesten Modelle zur Bildgenerierung, DALL-E und Midjourney.

## Einführung

In dieser Lektion behandeln wir:

- Bildgenerierung und warum sie nützlich ist.
- DALL-E und Midjourney, was sie sind und wie sie funktionieren.
- Wie man eine Anwendung zur Bildgenerierung erstellt.

## Lernziele

Nach Abschluss dieser Lektion wirst du in der Lage sein:

- Eine Anwendung zur Bildgenerierung zu erstellen.
- Grenzen für deine Anwendung mit Metaprompts festzulegen.
- Mit DALL-E und Midjourney zu arbeiten.

## Warum eine Bildgenerierungsanwendung erstellen?

Bildgenerierungsanwendungen sind eine großartige Möglichkeit, die Fähigkeiten von Generative AI zu erkunden. Sie können unter anderem genutzt werden für:

- **Bildbearbeitung und Synthese**. Du kannst Bilder für verschiedene Anwendungsfälle erzeugen, wie Bildbearbeitung und Bildsynthese.

- **Angewandt in verschiedenen Branchen**. Sie können auch verwendet werden, um Bilder für Branchen wie Medizintechnik, Tourismus, Spieleentwicklung und mehr zu generieren.

## Szenario: Edu4All

Im Rahmen dieser Lektion arbeiten wir weiter mit unserem Startup Edu4All. Die Schülerinnen und Schüler werden Bilder für ihre Beurteilungen erstellen, welche Bilder genau, bleibt ihnen überlassen, aber es könnten Illustrationen zu ihrem eigenen Märchen sein, eine neue Figur für ihre Geschichte oder Hilfe zur Visualisierung ihrer Ideen und Konzepte.

Hier ist ein Beispiel, was die Edu4All-Schüler erzeugen könnten, wenn sie im Unterricht an Denkmälern arbeiten:

![Edu4All Startup, Unterricht über Denkmäler, Eiffelturm](../../../translated_images/de/startup.94d6b79cc4bb3f5a.webp)

mit einem Prompt wie

> "Hund neben Eiffelturm im frühmorgendlichen Sonnenlicht"

## Was sind DALL-E und Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) und [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sind zwei der beliebtesten Modelle zur Bildgenerierung, die es dir erlauben, durch Prompts Bilder zu erzeugen.

### DALL-E

Beginnen wir mit DALL-E, einem generativen KI-Modell, das Bilder aus Textbeschreibungen erstellt.

> [DALL-E ist eine Kombination aus zwei Modellen, CLIP und diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** ist ein Modell, das Embeddings generiert, also numerische Darstellungen von Daten, aus Bildern und Text.

- **Diffused attention** ist ein Modell, das Bilder aus Embeddings erzeugt. DALL-E wurde auf einem Datensatz von Bildern und Text trainiert und kann verwendet werden, um Bilder aus Textbeschreibungen zu generieren. Zum Beispiel kann DALL-E Bilder von einer Katze mit Hut oder einem Hund mit Irokesenschnitt erzeugen.

### Midjourney

Midjourney funktioniert ähnlich wie DALL-E, es erzeugt Bilder aus Textprompts. Midjourney kann auch dazu verwendet werden, Bilder mit Prompts wie "eine Katze mit Hut" oder "ein Hund mit Irokesenschnitt" zu erzeugen.

![Bild generiert von Midjourney, mechanische Taube](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Bildquelle Wikipedia, Bild erzeugt von Midjourney_

## Wie funktionieren DALL-E und Midjourney

Zuerst zu [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E ist ein generatives KI-Modell basierend auf der Transformer-Architektur mit einem _autoregressiven Transformer_.

Ein _autoregressiver Transformer_ definiert, wie ein Modell Bilder aus Textbeschreibungen generiert: Es erzeugt ein Pixel nach dem anderen und verwendet die bereits erzeugten Pixel, um den nächsten Pixel zu generieren, wobei es durch mehrere Schichten eines neuronalen Netzwerks läuft, bis das Bild vollständig ist.

Mit diesem Prozess kontrolliert DALL-E Attribute, Objekte, Merkmale und mehr im generierten Bild. DALL-E 2 und 3 bieten jedoch noch mehr Kontrolle über das erzeugte Bild.

## Erstellen deiner ersten Bildgenerierungsanwendung

Was braucht man also, um eine Bildgenerierungsanwendung zu bauen? Du benötigst folgende Bibliotheken:

- **python-dotenv**, es wird dringend empfohlen, diese Bibliothek zu verwenden, um deine Geheimnisse in einer _.env_-Datei getrennt vom Code zu speichern.
- **openai**, diese Bibliothek benutzt du, um mit der OpenAI API zu interagieren.
- **pillow**, um mit Bildern in Python zu arbeiten.
- **requests**, um HTTP-Anfragen zu machen.

## Erstellen und Bereitstellen eines Azure OpenAI Modells

Falls noch nicht erledigt, folge den Anweisungen auf der Seite [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst),
um eine Azure OpenAI Ressource und ein Modell zu erstellen. Wähle **gpt-image-1** als Modell (das aktuelle Azure OpenAI Bildgenerierungsmodell; DALL-E 3 ist veraltet und für neue Deployments nicht mehr verfügbar).

## Die App erstellen

1. Erstelle eine Datei _.env_ mit folgendem Inhalt:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Diese Informationen findest du im Azure OpenAI Foundry Portal für deine Ressource unter "Deployments".

1. Sammle die oben genannten Bibliotheken in einer Datei namens _requirements.txt_ wie folgt:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Erstelle als nächstes eine virtuelle Umgebung und installiere die Bibliotheken:

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
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # Azure OpenAI-Dienstclient konfigurieren
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # Erstellen Sie ein Bild mit der Bildgenerierungs-API
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Legen Sie das Verzeichnis für das gespeicherte Bild fest
        image_dir = os.path.join(os.curdir, 'images')

        # Wenn das Verzeichnis nicht existiert, erstellen Sie es
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Initialisieren Sie den Bildpfad (achten Sie darauf, dass der Dateityp png sein sollte)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Abrufen des generierten Bildes
        image_url = generation_response.data[0].url  # Bild-URL aus der Antwort extrahieren
        generated_image = requests.get(image_url).content  # Bild herunterladen
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # Bild im Standardbildbetrachter anzeigen
        image = Image.open(image_path)
        image.show()

    # Ausnahmen abfangen
    except openai.BadRequestError as err:
        print(err)
   ```

Erklären wir diesen Code:

- Zuerst importieren wir die benötigten Bibliotheken, darunter die OpenAI-Bibliothek, die dotenv-Bibliothek, die requests-Bibliothek sowie die Pillow-Bibliothek.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Danach laden wir die Umgebungsvariablen aus der _.env_-Datei.

  ```python
  # dotenv importieren
  dotenv.load_dotenv()
  ```

- Anschließend konfigurieren wir den Azure OpenAI-Service-Client

  ```python
  # Endpoint und Schlüssel aus Umgebungsvariablen abrufen
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- Als nächstes erzeugen wir das Bild:

  ```python
  # Erstellen Sie ein Bild mit der Bildgenerierungs-API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Der obige Code antwortet mit einem JSON-Objekt, das die URL des erzeugten Bildes enthält. Wir können die URL nutzen, um das Bild herunterzuladen und in einer Datei zu speichern.

- Zuletzt öffnen wir das Bild und zeigen es mit dem Standardbildbetrachter an:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Mehr Details zur Bildgenerierung

Schauen wir uns den Code zur Bildgenerierung etwas genauer an:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** ist der Textprompt, mit dem das Bild erzeugt wird. In diesem Fall verwenden wir den Prompt "Hase auf Pferd, hält einen Lutscher, auf einer nebligen Wiese, auf der Narzissen wachsen".
- **size** ist die Größe des erzeugten Bildes. Hier generieren wir ein Bild mit 1024x1024 Pixeln.
- **n** ist die Anzahl der erzeugten Bilder. Hier erzeugen wir zwei Bilder.
- **temperature** ist ein Parameter, der die Zufälligkeit der Ausgabe eines Generativen KI-Modells steuert. Die Temperatur ist ein Wert zwischen 0 und 1, wobei 0 bedeutet, dass die Ausgabe deterministisch ist, und 1 bedeutet, dass die Ausgabe zufällig ist. Standardwert ist 0.7.

Es gibt weitere Dinge, die man mit Bildern machen kann, die wir im nächsten Abschnitt behandeln.

## Erweiterte Möglichkeiten der Bildgenerierung

Du hast bisher gesehen, wie man mit wenigen Zeilen Python-Code ein Bild erzeugen kann. Aber es gibt noch mehr, was man mit Bildern machen kann.

Du kannst auch Folgendes tun:

- **Bearbeitungen durchführen**. Indem du einem bestehenden Bild eine Maske und einen Prompt gibst, kannst du das Bild verändern. Zum Beispiel kannst du an einem Teil des Bildes etwas hinzufügen. Stell dir unser Hasenbild vor: Du könntest dem Hasen einen Hut aufsetzen. Dabei gibst du das Bild, eine Maske (die den Bereich für die Änderung angibt) und einen Textprompt an, der beschreibt, was geändert werden soll.
> Hinweis: Dies wird in DALL-E 3 nicht unterstützt.
 
Hier ist ein Beispiel mit GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Das Ausgangsbild würde nur die Lounge mit Pool enthalten, aber das Endbild zeigt einen Flamingo:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/de/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/de/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/de/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Variationen erzeugen**. Die Idee ist, dass du ein vorhandenes Bild nimmst und Variationen davon erzeugen lässt. Um eine Variation zu erstellen, gibst du ein Bild und einen Textprompt an und verwendest Code wie folgt:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > Hinweis: Dies wird nur vom DALL-E 2 Modell von OpenAI unterstützt, nicht vom gpt-image-1.

## Temperatur

Temperatur ist ein Parameter, der die Zufälligkeit der Ausgabe eines Generativen KI-Modells steuert. Die Temperatur ist ein Wert zwischen 0 und 1, wobei 0 bedeutet, dass die Ausgabe deterministisch ist, und 1 bedeutet, dass die Ausgabe zufällig ist. Der Standardwert ist 0.7.

Schauen wir uns ein Beispiel an, wie Temperatur funktioniert, indem wir den folgenden Prompt zweimal ausführen:

> Prompt : "Hase auf Pferd, hält einen Lutscher, auf einer nebligen Wiese, auf der Narzissen wachsen"

![Hase auf einem Pferd, hält einen Lutscher, Version 1](../../../translated_images/de/v1-generated-image.a295cfcffa3c13c2.webp)

Jetzt führen wir denselben Prompt nochmal aus, um zu zeigen, dass wir nicht zweimal dasselbe Bild bekommen:

![Generiertes Bild eines Hasen auf einem Pferd](../../../translated_images/de/v2-generated-image.33f55a3714efe61d.webp)

Wie du sehen kannst, sind die Bilder ähnlich, aber nicht identisch. Versuchen wir, den Temperaturwert auf 0.1 zu ändern und sehen, was passiert:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Geben Sie hier Ihren Eingabetext ein
        size='1024x1024',
        n=2
    )
```

### Änderung der Temperatur

Versuchen wir also, die Antwort deterministischer zu machen. Wir können aus den beiden Bildern, die wir erzeugt haben, beobachten, dass im ersten Bild ein Hase und im zweiten ein Pferd zu sehen ist, die Bilder also stark variieren.

Ändern wir deshalb unseren Code und setzen die Temperatur auf 0, so:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Geben Sie hier Ihren Eingabetext ein
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Wenn du diesen Code ausführst, erhältst du diese zwei Bilder:

- ![Temperatur 0, Version 1](../../../translated_images/de/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Temperatur 0, Version 2](../../../translated_images/de/v2-temp-generated-image.871d0c920dbfb0f1.webp)

Hier sieht man deutlich, wie die Bilder einander ähnlicher sind.

## Wie du Grenzen für deine Anwendung mit Metaprompts definierst

Mit unserer Demo können wir bereits Bilder für unsere Kunden generieren. Allerdings müssen wir Grenzen für unsere Anwendung setzen.

Zum Beispiel wollen wir keine Bilder generieren, die nicht jugendfrei sind oder für Kinder ungeeignet.

Das können wir mit _Metaprompts_ tun. Metaprompts sind Textprompts, die verwendet werden, um die Ausgabe eines generativen KI-Modells zu steuern. So können wir kontrollieren, dass die erzeugten Bilder jugendfrei oder für Kinder geeignet sind.

### Wie funktioniert das?

Wie funktionieren Metaprompts?

Metaprompts sind Textprompts, die vor dem eigentlichen Textprompt positioniert sind, um die Ausgabe des Modells zu steuern, und in Anwendungen eingebettet werden, um die Modelleingabe zu kontrollieren. Dabei werden die Eingabe des Prompts und des Metaprompts in einem einzigen Textprompt zusammengefasst.

Ein Beispiel für einen Metaprompt wäre folgender:

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

# TODO Anfrage zum Generieren eines Bildes hinzufügen
```

Aus dem obigen Prompt sieht man, wie alle erzeugten Bilder den Metaprompt berücksichtigen.

## Aufgabe – Lass die Schüler aktiv werden

Edu4All wurde am Anfang dieser Lektion eingeführt. Nun ist es Zeit, die Schülerinnen und Schüler zu befähigen, Bilder für ihre Beurteilungen zu generieren.


Die Schüler werden Bilder für ihre Bewertungen erstellen, die Denkmäler enthalten. Welche Denkmäler genau, bleibt den Schülern überlassen. Die Schüler werden aufgefordert, bei dieser Aufgabe ihre Kreativität einzusetzen, um diese Denkmäler in verschiedenen Kontexten zu platzieren.

## Lösung

Hier ist eine mögliche Lösung:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# Endpunkt und Schlüssel aus Umgebungsvariablen abrufen
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
    # Erstellen Sie ein Bild mit der API zur Bildgenerierung
    generation_response = client.images.generate(
        prompt=prompt,    # Geben Sie hier Ihren Aufforderungstext ein
        size='1024x1024',
        n=1,
    )
    # Setzen Sie das Verzeichnis für das gespeicherte Bild
    image_dir = os.path.join(os.curdir, 'images')

    # Falls das Verzeichnis nicht existiert, erstellen Sie es
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialisieren Sie den Bildpfad (beachten Sie, dass der Dateityp png sein sollte)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Abrufen des generierten Bildes
    image_url = generation_response.data[0].url  # Bild-URL aus der Antwort extrahieren
    generated_image = requests.get(image_url).content  # Laden Sie das Bild herunter
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Zeigen Sie das Bild im Standardbildbetrachter an
    image = Image.open(image_path)
    image.show()

# Ausnahmen abfangen
except openai.BadRequestError as err:
    print(err)
```

## Großartige Arbeit! Setzen Sie Ihr Lernen fort

Nach Abschluss dieser Lektion sehen Sie sich unsere [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über Generative KI weiter zu vertiefen!

Gehen Sie zu Lektion 10, wo wir uns ansehen, wie man [KI-Anwendungen mit Low-Code erstellt](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->