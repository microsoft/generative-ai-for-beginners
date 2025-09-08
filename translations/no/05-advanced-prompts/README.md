<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:34:26+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "no"
}
-->

> "Generer kode for en Python Web-API"
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

Å kjøre prompten på nytt gir oss dette resultatet:

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

Det er bare en liten forskjell mellom disse to resultatene. La oss gjøre det motsatte denne gangen, la oss sette temperaturen til 0,9:

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

og det andre forsøket med temperaturverdien 0,9:

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

Som du kan se, kunne ikke resultatene vært mer varierte.

> Merk at det finnes flere parametere du kan endre for å variere output, som top-k, top-p, repetition penalty, length penalty og diversity penalty, men disse ligger utenfor omfanget av dette kurset.

## Gode praksiser

Det finnes mange metoder du kan bruke for å prøve å få det du ønsker. Du vil finne din egen stil etter hvert som du bruker prompting mer og mer.

I tillegg til teknikkene vi har gått gjennom, finnes det noen gode praksiser å tenke på når du prompt-er en LLM.

Her er noen gode praksiser å vurdere:

- **Spesifiser kontekst**. Kontekst er viktig, jo mer du kan spesifisere som domene, tema osv., desto bedre.
- Begrens output. Hvis du ønsker et bestemt antall elementer eller en bestemt lengde, spesifiser det.
- **Spesifiser både hva og hvordan**. Husk å nevne både hva du vil ha og hvordan du vil ha det, for eksempel "Lag en Python Web API med rutene products og customers, del den opp i 3 filer".
- **Bruk maler**. Ofte vil du berike promptene dine med data fra selskapet ditt. Bruk maler for å gjøre dette. Maler kan ha variabler som du erstatter med faktiske data.
- **Stav riktig**. LLM-er kan gi deg et korrekt svar, men hvis du staver riktig, får du et bedre svar.

## Oppgave

Her er kode i Python som viser hvordan man bygger en enkel API med Flask:

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

Bruk en AI-assistent som GitHub Copilot eller ChatGPT og bruk "self-refine"-teknikken for å forbedre koden.

## Løsning

Prøv å løse oppgaven ved å legge til passende prompts i koden.

> [!TIP]
> Formuler en prompt for å be om forbedring, det er lurt å begrense hvor mange forbedringer. Du kan også be om forbedring på en bestemt måte, for eksempel arkitektur, ytelse, sikkerhet osv.

[Løsning](../../../05-advanced-prompts/python/aoai-solution.py)

## Kunnskapssjekk

Hvorfor ville jeg brukt chain-of-thought prompting? Vis meg 1 korrekt svar og 2 feil svar.

1. For å lære LLM hvordan man løser et problem.  
1. B, For å lære LLM å finne feil i kode.  
1. C, For å instruere LLM til å komme opp med forskjellige løsninger.

A: 1, fordi chain-of-thought handler om å vise LLM hvordan man løser et problem ved å gi den en serie steg, og lignende problemer og hvordan de ble løst.

## 🚀 Utfordring

Du brukte nettopp self-refine-teknikken i oppgaven. Ta et hvilket som helst program du har laget og vurder hvilke forbedringer du ønsker å gjøre. Bruk nå self-refine-teknikken for å gjennomføre de foreslåtte endringene. Hva syntes du om resultatet, bedre eller verre?

## Flott jobbet! Fortsett læringen din

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å utvikle din kunnskap om Generativ AI!

Gå videre til Leksjon 6 hvor vi vil bruke kunnskapen vår om Prompt Engineering ved å [bygge tekstgenereringsapper](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.