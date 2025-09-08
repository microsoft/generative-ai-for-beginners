<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:23:43+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "de"
}
-->

> "Code für eine Python-Web-API generieren"
```python
#import necessary libraries
import flask
from flask import request, jsonify

#create an instance of the Flask class
app = flask.Flask(__name__)

#create an endpoint for the API
@app.route('/api/v1/endpoint', methods=['GET'])
def api_endpoint():
    #get the request data
    data = request.get_json()

    #process the data
    result = process_data(data)

    #return the result
    return jsonify(result)

#function to process the data
def process_data(data):
    #process the data
    result = {'result': 'success'}

    #return the result
    return result

#run the Flask app
if __name__ == '__main__':
    app.run()

```

Wenn wir den Prompt erneut ausführen, erhalten wir folgendes Ergebnis:

```python
#import necessary libraries
import flask
from flask import request, jsonify

#create a Flask app
app = flask.Flask(__name__)

#create a route for the API
@app.route('/api', methods=['GET'])
def api_call():
    #get the data from the request
    data = request.get_json()

    #process the data
    result = process_data(data)

    #return the result
    return jsonify(result)

#define the process_data function
def process_data(data):
    #do something with the data
    result = data + 1

    #return the result
    return result

#run the app
if __name__ == '__main__':
    app.run()

```

Zwischen diesen beiden Ausgaben gibt es nur einen kleinen Unterschied. Machen wir es diesmal andersherum und setzen die Temperatur auf 0,9:

```python
# Import necessary libraries
import flask
from flask import request, jsonify

# Create a Flask app
app = flask.Flask(__name__)

# Create a route for the API
@app.route('/api', methods=['GET'])
def api_call():
    # Get the data from the request
    data = request.args

    # Process the data
    result = process_data(data)

    # Return the result
    return jsonify(result)

# Function to process the data
def process_data(data):
    # Do something with the data
    result = data + 1

    # Return the result
    return result

# Run the app
if __name__ == '__main__':
    app.run()

```

und der zweite Versuch mit einer Temperatur von 0,9:

```python
import flask
from flask import request, jsonify

# create the Flask app
app = flask.Flask(__name__)
app.config['DEBUG'] = True

# create some test data
books = [
    {'id': 0, 'title': 'A Fire Upon The Deep', 'author': 'Vernor Vinge', 'first_sentence': 'The coldsleep itself was dreamless.', 'year_published': '1992'},
    {'id': 1, 'title': 'The Ones Who Walk Away From Omelas', 'author': 'Ursula K. Le Guin', 'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.', 'published': '1973'},
    {'id': 2, 'title': 'Dhalgren', 'author': 'Samuel R. Delany', 'first_sentence': 'to wound the autumnal city.', 'published': '1975'}
]

# create an endpoint
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to our book API!</h1>'''

@app.route('/api/v1/resources/books

```

Wie du sehen kannst, könnten die Ergebnisse nicht unterschiedlicher sein.

> Hinweis: Es gibt noch weitere Parameter, die du ändern kannst, um die Ausgabe zu variieren, wie top-k, top-p, repetition penalty, length penalty und diversity penalty, aber diese liegen außerhalb des Umfangs dieses Kurses.

## Gute Praktiken

Es gibt viele Methoden, die du anwenden kannst, um das gewünschte Ergebnis zu erzielen. Mit der Zeit wirst du deinen eigenen Stil beim Prompting entwickeln.

Zusätzlich zu den bisher behandelten Techniken gibt es einige gute Praktiken, die du beim Prompting eines LLM beachten solltest.

Hier sind einige gute Praktiken, die du berücksichtigen solltest:

- **Kontext angeben**. Kontext ist wichtig, je mehr du angeben kannst, wie z. B. Domäne, Thema usw., desto besser.
- Begrenze die Ausgabe. Wenn du eine bestimmte Anzahl von Elementen oder eine bestimmte Länge möchtest, gib das an.
- **Gib sowohl was als auch wie an**. Denk daran, sowohl zu sagen, was du möchtest, als auch wie du es möchtest, zum Beispiel: „Erstelle eine Python Web-API mit den Routen products und customers, aufgeteilt in 3 Dateien“.
- **Verwende Templates**. Oft möchtest du deine Prompts mit Daten aus deinem Unternehmen anreichern. Nutze Templates dafür. Templates können Variablen enthalten, die du mit echten Daten ersetzt.
- **Rechtschreibung beachten**. LLMs können dir zwar auch bei falscher Rechtschreibung eine Antwort geben, aber bei korrekter Rechtschreibung erhältst du bessere Ergebnisse.

## Aufgabe

Hier ist ein Python-Code, der zeigt, wie man eine einfache API mit Flask erstellt:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
```

Nutze einen KI-Assistenten wie GitHub Copilot oder ChatGPT und wende die „self-refine“-Technik an, um den Code zu verbessern.

## Lösung

Versuche, die Aufgabe zu lösen, indem du passende Prompts zum Code hinzufügst.

> [!TIP]
> Formuliere einen Prompt, der um Verbesserungen bittet. Es ist sinnvoll, die Anzahl der Verbesserungen zu begrenzen. Du kannst auch darum bitten, die Verbesserung in einem bestimmten Bereich vorzunehmen, z. B. Architektur, Performance, Sicherheit usw.

[Lösung](../../../05-advanced-prompts/python/aoai-solution.py)

## Wissensüberprüfung

Warum würde ich chain-of-thought prompting verwenden? Zeige mir 1 richtige Antwort und 2 falsche Antworten.

1. Um dem LLM beizubringen, wie man ein Problem löst.  
1. B, Um dem LLM beizubringen, Fehler im Code zu finden.  
1. C, Um das LLM anzuweisen, verschiedene Lösungen zu entwickeln.

A: 1, weil chain-of-thought darin besteht, dem LLM zu zeigen, wie man ein Problem löst, indem man ihm eine Reihe von Schritten und ähnliche Probleme mit deren Lösungen vorgibt.

## 🚀 Herausforderung

Du hast gerade die self-refine-Technik in der Aufgabe angewendet. Nimm ein beliebiges Programm, das du geschrieben hast, und überlege, welche Verbesserungen du daran vornehmen würdest. Wende nun die self-refine-Technik an, um die vorgeschlagenen Änderungen umzusetzen. Wie war dein Ergebnis, besser oder schlechter?

## Großartige Arbeit! Setze dein Lernen fort

Nachdem du diese Lektion abgeschlossen hast, schau dir unsere [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um dein Wissen über Generative KI weiter auszubauen!

Gehe zu Lektion 6, wo wir unser Wissen über Prompt Engineering anwenden, indem wir [Textgenerierungs-Apps erstellen](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst).

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.