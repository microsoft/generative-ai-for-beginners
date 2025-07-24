<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:33:36+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "sv"
}
-->

> "Generera kod för ett Python Web API"
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

Att köra prompten igen ger oss detta resultat:

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

Det är bara en liten skillnad mellan dessa två resultat. Låt oss göra tvärtom den här gången, vi sätter temperaturen till 0,9:

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

och det andra försöket med temperaturvärdet 0,9:

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

Som du kan se kunde resultaten inte vara mer varierande.

> Note, att det finns fler parametrar du kan ändra för att variera resultatet, som top-k, top-p, repetition penalty, length penalty och diversity penalty, men dessa ligger utanför detta kursinnehåll.

## Bra metoder

Det finns många metoder du kan använda för att försöka få det du vill ha. Du kommer att hitta din egen stil ju mer du använder prompting.

Utöver de tekniker vi har gått igenom finns det några bra metoder att tänka på när du promptar en LLM.

Här är några bra metoder att överväga:

- **Specificera kontext**. Kontext är viktigt, ju mer du kan specificera som domän, ämne osv. desto bättre.
- Begränsa outputen. Om du vill ha ett specifikt antal objekt eller en viss längd, specificera det.
- **Specificera både vad och hur**. Kom ihåg att nämna både vad du vill ha och hur du vill ha det, till exempel "Skapa en Python Web API med rutterna products och customers, dela upp den i 3 filer".
- **Använd mallar**. Ofta vill du berika dina prompts med data från ditt företag. Använd mallar för detta. Mallar kan ha variabler som du ersätter med faktisk data.
- **Stava rätt**. LLMs kan ge dig ett korrekt svar, men om du stavar rätt får du ett bättre svar.

## Uppgift

Här är kod i Python som visar hur man bygger en enkel API med Flask:

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

Använd en AI-assistent som GitHub Copilot eller ChatGPT och tillämpa "self-refine"-tekniken för att förbättra koden.

## Lösning

Försök att lösa uppgiften genom att lägga till lämpliga prompts till koden.

> [!TIP]
> Formulera en prompt för att be om förbättringar, det är en bra idé att begränsa hur många förbättringar. Du kan också be om förbättringar på ett visst sätt, till exempel arkitektur, prestanda, säkerhet osv.

[Lösning](../../../05-advanced-prompts/python/aoai-solution.py)

## Kunskapskontroll

Varför skulle jag använda chain-of-thought prompting? Visa mig 1 korrekt svar och 2 felaktiga svar.

1. För att lära LLM hur man löser ett problem.  
1. B, För att lära LLM att hitta fel i kod.  
1. C, För att instruera LLM att komma på olika lösningar.

A: 1, eftersom chain-of-thought handlar om att visa LLM hur man löser ett problem genom att ge den en serie steg, och liknande problem och hur de löstes.

## 🚀 Utmaning

Du använde precis self-refine-tekniken i uppgiften. Ta vilket program du än byggt och fundera på vilka förbättringar du skulle vilja göra. Använd sedan self-refine-tekniken för att genomföra de föreslagna ändringarna. Vad tyckte du om resultatet, bättre eller sämre?

## Bra jobbat! Fortsätt din lärande

Efter att ha slutfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla dina kunskaper inom Generative AI!

Gå vidare till Lektion 6 där vi kommer att tillämpa vår kunskap om Prompt Engineering genom att [bygga appar för textgenerering](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.