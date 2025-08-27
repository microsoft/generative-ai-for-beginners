<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-08-25T12:30:47+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "lt"
}
-->

> "Generuokite kodą Python internetinei API"
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

Pakartotinai paleidus užklausą, gauname tokį rezultatą:

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

Tarp šių dviejų rezultatų yra tik labai nedidelis skirtumas. Dabar padarykime priešingai – nustatykime temperature reikšmę į 0.9:

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

ir antras bandymas su temperature reikšme 0.9:

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

Kaip matote, rezultatai gali būti labai skirtingi.

> Atkreipkite dėmesį, kad yra ir daugiau parametrų, kuriuos galite keisti norėdami gauti įvairesnius rezultatus, pavyzdžiui, top-k, top-p, repetition penalty, length penalty ir diversity penalty, tačiau jie neaptariami šioje mokymų programoje.

## Geros praktikos

Yra daug praktikų, kurias galite taikyti norėdami gauti norimą rezultatą. Naudodami promptus vis dažniau, atrasite savo stilių.

Be jau aptartų technikų, yra keletas gerų praktikų, kurias verta prisiminti dirbant su LLM.

Štai keletas gerų praktikų:

- **Nurodykite kontekstą**. Kontekstas svarbus – kuo tiksliau nurodysite sritį, temą ir pan., tuo geriau.
- Apribokite rezultatą. Jei norite tam tikro elementų skaičiaus ar ilgio, nurodykite tai.
- **Nurodykite, ką ir kaip**. Nepamirškite paminėti tiek, ko norite, tiek kaip norite, pavyzdžiui: „Sukurk Python Web API su maršrutais products ir customers, padalink į 3 failus“.
- **Naudokite šablonus**. Dažnai norėsite papildyti savo promptus įmonės duomenimis. Tam naudokite šablonus. Šablonuose gali būti kintamųjų, kuriuos pakeisite tikrais duomenimis.
- **Rašykite taisyklingai**. LLM gali pateikti teisingą atsakymą, bet jei rašysite taisyklingai, atsakymas bus geresnis.

## Užduotis

Štai Python kodas, rodantis, kaip sukurti paprastą API naudojant Flask:

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

Naudokite AI asistentą, pvz., GitHub Copilot ar ChatGPT, ir pritaikykite „self-refine“ techniką, kad patobulintumėte kodą.

## Sprendimas

Pabandykite išspręsti užduotį, pridėdami tinkamus promptus prie kodo.

> [!TIP]
> Suformuluokite promptą, kuriame paprašytumėte patobulinti kodą – verta nurodyti, kiek patobulinimų norite. Taip pat galite paprašyti patobulinti tam tikru aspektu, pavyzdžiui, architektūros, našumo, saugumo ir pan.

[Sprendimas](../../../05-advanced-prompts/python/aoai-solution.py)

## Žinių patikrinimas

Kodėl verta naudoti chain-of-thought promptus? Pateikite 1 teisingą ir 2 neteisingus atsakymus.

1. Norint parodyti LLM, kaip spręsti užduotį.
1. B, Norint išmokyti LLM rasti klaidas kode.
1. C, Norint nurodyti LLM sugalvoti skirtingus sprendimus.

A: 1, nes chain-of-thought esmė – parodyti LLM, kaip spręsti užduotį, pateikiant veiksmų seką, panašias užduotis ir jų sprendimo būdus.

## 🚀 Iššūkis

Užduotyje jau naudojote self-refine techniką. Paimkite bet kurią savo sukurtą programą ir pagalvokite, kokius patobulinimus norėtumėte joje pritaikyti. Dabar naudokite self-refine techniką, kad įgyvendintumėte siūlomus pakeitimus. Kaip manote, ar rezultatas tapo geresnis, ar blogesnis?

## Puikus darbas! Tęskite mokymąsi

Baigę šią pamoką, apsilankykite mūsų [Generatyvaus DI mokymosi kolekcijoje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau gilintumėte žinias apie generatyvųjį DI!

Eikite į 6 pamoką, kurioje pritaikysime promptų inžinerijos žinias [kurdami teksto generavimo programas](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbios informacijos atveju rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretavimą, kilusį dėl šio vertimo naudojimo.