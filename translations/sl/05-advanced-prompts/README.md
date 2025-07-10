<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:41:22+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "sl"
}
-->

> "Generiraj kodo za Python spletni API"
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

Ponovno zagon poziva nam da rezultat:

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

Med tema dvema izhodoma je le majhna razlika. Tokrat naredimo nasprotno, nastavimo temperaturo na 0,9:

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

in drugi poskus z vrednostjo temperature 0,9:

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

Kot vidite, so rezultati lahko zelo različni.

> Opomba, obstaja še več parametrov, ki jih lahko spreminjate za raznolikost izhoda, kot so top-k, top-p, kazen za ponavljanje, kazen za dolžino in kazen za raznolikost, vendar ti niso del tega učnega načrta.

## Dobri postopki

Obstaja veliko pristopov, ki jih lahko uporabite, da dobite želeni rezultat. Sčasoma boste razvili svoj slog, ko boste več uporabljali pozive.

Poleg tehnik, ki smo jih obravnavali, je nekaj dobrih praks, ki jih je vredno upoštevati pri pozivanju LLM.

Tukaj je nekaj dobrih praks:

- **Določite kontekst**. Kontekst je pomemben, bolj ko ga lahko natančno opišete, na primer domeno, temo itd., bolje je.
- Omejite izhod. Če želite določen število elementov ali določeno dolžino, to jasno navedite.
- **Določite tako kaj kot kako**. Ne pozabite navesti, kaj želite in kako želite, na primer "Ustvari Python Web API z usmeritvami products in customers, razdeli ga v 3 datoteke".
- **Uporabljajte predloge**. Pogosto boste želeli obogatiti svoje pozive z podatki iz vašega podjetja. Za to uporabite predloge. Predloge lahko vsebujejo spremenljivke, ki jih nadomestite z dejanskimi podatki.
- **Pravilno črkujte**. LLM vam lahko da pravilen odgovor, a če pravilno črkujete, boste dobili še boljši odgovor.

## Naloga

Tukaj je koda v Pythonu, ki prikazuje, kako zgraditi preprost API z uporabo Flask:

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

Uporabite AI pomočnika, kot sta GitHub Copilot ali ChatGPT, in uporabite tehniko "self-refine" za izboljšanje kode.

## Rešitev

Poskusite rešiti nalogo tako, da dodate ustrezne pozive v kodo.

> [!TIP]
> Oblikujte poziv, ki prosi za izboljšave, dobro je omejiti število izboljšav. Prav tako lahko prosite za izboljšave na določen način, na primer arhitektura, zmogljivost, varnost itd.

[Rešitev](../../../05-advanced-prompts/python/aoai-solution.py)

## Preverjanje znanja

Zakaj bi uporabil chain-of-thought pozivanje? Pokaži mi 1 pravilen odgovor in 2 napačna odgovora.

1. Da naučim LLM, kako rešiti problem.  
1. B, Da naučim LLM, kako najti napake v kodi.  
1. C, Da navodim LLM, naj predlaga različne rešitve.

A: 1, ker chain-of-thought pomeni pokazati LLM, kako rešiti problem z naborom korakov in podobnimi problemi ter njihovimi rešitvami.

## 🚀 Izziv

Pravkar ste v nalogi uporabili tehniko self-refine. Vzemite katerikoli program, ki ste ga napisali, in premislite, katere izboljšave bi želeli uvesti. Nato uporabite tehniko self-refine, da izvedete predlagane spremembe. Kakšen je bil vaš vtis o rezultatu, boljši ali slabši?

## Odlično! Nadaljujte z učenjem

Po zaključku te lekcije si oglejte našo [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da še naprej nadgrajujete svoje znanje o Generativni AI!

Pojdite na Lekcijo 6, kjer bomo uporabili znanje o Prompt Engineering z [izdelavo aplikacij za generiranje besedila](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.