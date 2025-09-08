<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:35:19+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "nl"
}
-->

# Code genereren voor een Python Web API

In deze gids leer je hoe je code genereert voor een Python Web API met behulp van verschillende tools en frameworks.

## Vereisten

- Python 3.7 of hoger
- Een webframework zoals Flask of FastAPI
- Een HTTP-client zoals requests (voor testen)

## Stappen

1. **Projectstructuur opzetten**

   Maak een nieuwe map aan voor je project en initialiseer een virtuele omgeving:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Op Windows gebruik: venv\Scripts\activate
   ```

2. **Benodigde pakketten installeren**

   Installeer Flask of FastAPI en andere benodigde pakketten:

   ```bash
   pip install fastapi uvicorn
   ```

3. **Eenvoudige API maken**

   Maak een bestand `main.py` aan en voeg de volgende code toe:

   ```python
   from fastapi import FastAPI

   app = FastAPI()

   @app.get("/")
   async def read_root():
       return {"message": "Hallo Wereld"}
   ```

4. **API starten**

   Start de server met:

   ```bash
   uvicorn main:app --reload
   ```

5. **API testen**

   Open je browser en ga naar `http://127.0.0.1:8000/` om de API te testen.

## Tips

- [!TIP] Gebruik `uvicorn` met de `--reload` optie tijdens ontwikkeling om automatisch herstarten te activeren.
- [!IMPORTANT] Zorg ervoor dat je API endpoints duidelijk en consistent zijn.
- [!WARNING] Vermijd het hardcoderen van gevoelige informatie in je code.

## Volgende stappen

- Voeg meer endpoints toe voor CRUD-operaties.
- Implementeer authenticatie en autorisatie.
- Schrijf unittests voor je API.
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

De prompt opnieuw uitvoeren geeft ons dit resultaat:

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

Er is maar een klein verschil tussen deze twee outputs. Laten we het deze keer andersom doen en de temperatuur op 0,9 zetten:

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

en de tweede poging met een temperatuurwaarde van 0,9:

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

Zoals je ziet, kunnen de resultaten niet meer van elkaar verschillen.

> Let op, er zijn nog meer parameters die je kunt aanpassen om de output te variëren, zoals top-k, top-p, repetition penalty, length penalty en diversity penalty, maar deze vallen buiten de scope van deze cursus.

## Goede praktijken

Er zijn veel methodes die je kunt toepassen om te proberen te krijgen wat je wilt. Naarmate je meer met prompting werkt, ontwikkel je je eigen stijl.

Naast de technieken die we hebben behandeld, zijn er enkele goede praktijken om rekening mee te houden bij het prompten van een LLM.

Hier zijn een aantal goede praktijken om te overwegen:

- **Specificeer de context**. Context is belangrijk, hoe meer je kunt specificeren zoals domein, onderwerp, etc., hoe beter.
- Beperk de output. Als je een specifiek aantal items of een bepaalde lengte wilt, geef dat dan aan.
- **Specificeer zowel wat als hoe**. Vergeet niet te vermelden wat je wilt en hoe je het wilt, bijvoorbeeld "Maak een Python Web API met routes products en customers, verdeel het in 3 bestanden".
- **Gebruik templates**. Vaak wil je je prompts verrijken met data uit je bedrijf. Gebruik templates om dit te doen. Templates kunnen variabelen bevatten die je vervangt door echte data.
- **Spel correct**. LLMs kunnen je een correct antwoord geven, maar als je correct spelt, krijg je een beter antwoord.

## Opdracht

Hier is code in Python die laat zien hoe je een eenvoudige API bouwt met Flask:

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

Gebruik een AI-assistent zoals GitHub Copilot of ChatGPT en pas de "self-refine" techniek toe om de code te verbeteren.

## Oplossing

Probeer de opdracht op te lossen door geschikte prompts aan de code toe te voegen.

> [!TIP]
> Formuleer een prompt om te vragen om verbetering, het is een goed idee om te beperken hoeveel verbeteringen je wilt. Je kunt ook vragen om verbetering op een bepaald vlak, bijvoorbeeld architectuur, performance, beveiliging, etc.

[Oplossing](../../../05-advanced-prompts/python/aoai-solution.py)

## Kennischeck

Waarom zou ik chain-of-thought prompting gebruiken? Laat me 1 correct antwoord en 2 onjuiste antwoorden zien.

1. Om de LLM te leren hoe een probleem op te lossen.  
1. B, Om de LLM te leren fouten in code te vinden.  
1. C, Om de LLM aan te sturen om met verschillende oplossingen te komen.

A: 1, omdat chain-of-thought gaat over het laten zien aan de LLM hoe een probleem op te lossen door het een reeks stappen te geven, en vergelijkbare problemen en hoe die zijn opgelost.

## 🚀 Uitdaging

Je hebt zojuist de self-refine techniek gebruikt in de opdracht. Pak een programma dat je hebt gebouwd en bedenk welke verbeteringen je erop zou willen toepassen. Gebruik nu de self-refine techniek om de voorgestelde wijzigingen door te voeren. Wat vond je van het resultaat, beter of slechter?

## Goed gedaan! Ga door met leren

Na het afronden van deze les, bekijk onze [Generative AI Learning collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis van Generative AI verder te vergroten!

Ga door naar Les 6 waar we onze kennis van Prompt Engineering toepassen door [tekstgeneratie-apps te bouwen](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.