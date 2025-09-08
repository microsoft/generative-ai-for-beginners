<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:34:01+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "da"
}
-->

> "Generer kode til en Python Web API"
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

At køre prompten igen giver os dette resultat:

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

Der er kun en lille forskel mellem disse to output. Lad os gøre det modsatte denne gang, lad os sætte temperaturen til 0,9:

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

og det andet forsøg med temperaturen sat til 0,9:

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

Som du kan se, kunne resultaterne ikke være mere forskellige.

> Note, at der er flere parametre, du kan ændre for at variere outputtet, som top-k, top-p, repetition penalty, length penalty og diversity penalty, men disse ligger uden for rammerne af dette kursus.

## Gode fremgangsmåder

Der er mange metoder, du kan anvende for at prøve at få det, du ønsker. Du vil finde din egen stil, efterhånden som du bruger prompting mere og mere.

Ud over de teknikker, vi har gennemgået, er der nogle gode fremgangsmåder at overveje, når du prompt’er en LLM.

Her er nogle gode fremgangsmåder at tage i betragtning:

- **Angiv kontekst**. Kontekst er vigtigt, jo mere du kan specificere som domæne, emne osv., desto bedre.
- Begræns outputtet. Hvis du ønsker et bestemt antal elementer eller en bestemt længde, så angiv det.
- **Angiv både hvad og hvordan**. Husk at nævne både hvad du vil have, og hvordan du vil have det, for eksempel "Lav en Python Web API med ruterne products og customers, del den op i 3 filer".
- **Brug skabeloner**. Ofte vil du gerne berige dine prompts med data fra din virksomhed. Brug skabeloner til dette. Skabeloner kan have variabler, som du erstatter med faktiske data.
- **Stav korrekt**. LLM’er kan give dig et korrekt svar, men hvis du staver korrekt, får du et bedre svar.

## Opgave

Her er kode i Python, der viser, hvordan man bygger en simpel API med Flask:

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

Brug en AI-assistent som GitHub Copilot eller ChatGPT og anvend "self-refine"-teknikken til at forbedre koden.

## Løsning

Forsøg at løse opgaven ved at tilføje passende prompts til koden.

> [!TIP]
> Formuler en prompt, der beder om forbedring, det er en god idé at begrænse, hvor mange forbedringer der skal laves. Du kan også bede om forbedringer på en bestemt måde, for eksempel arkitektur, ydeevne, sikkerhed osv.

[Løsning](../../../05-advanced-prompts/python/aoai-solution.py)

## Videnstest

Hvorfor ville jeg bruge chain-of-thought prompting? Vis mig 1 korrekt svar og 2 forkerte svar.

1. For at lære LLM’en, hvordan man løser et problem.  
1. B, For at lære LLM’en at finde fejl i kode.  
1. C, For at instruere LLM’en i at komme med forskellige løsninger.

A: 1, fordi chain-of-thought handler om at vise LLM’en, hvordan man løser et problem ved at give den en række trin, og lignende problemer og hvordan de blev løst.

## 🚀 Udfordring

Du har netop brugt self-refine-teknikken i opgaven. Tag et hvilket som helst program, du har bygget, og overvej, hvilke forbedringer du gerne vil anvende på det. Brug nu self-refine-teknikken til at implementere de foreslåede ændringer. Hvad syntes du om resultatet, blev det bedre eller værre?

## Fantastisk arbejde! Fortsæt din læring

Efter at have gennemført denne lektion, kan du tjekke vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at udvikle din viden om Generativ AI!

Gå videre til Lektion 6, hvor vi vil anvende vores viden om Prompt Engineering ved at [bygge tekstgenereringsapps](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.