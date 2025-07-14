<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:40:58+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "hr"
}
-->

> "Generiraj kod za Python Web API"
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

Ponovno pokretanje prompta daje nam ovaj rezultat:

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

Razlika između ova dva izlaza je vrlo mala. Sada ćemo napraviti suprotno, postaviti temperaturu na 0.9:

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

i drugi pokušaj s temperaturom postavljenom na 0.9:

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

Kao što vidite, rezultati su znatno različiti.

> Note, da postoji još parametara koje možete mijenjati kako biste varirali izlaz, poput top-k, top-p, repetition penalty, length penalty i diversity penalty, ali oni nisu obuhvaćeni ovim kurikulumom.

## Dobre prakse

Postoji mnogo praksi koje možete primijeniti kako biste dobili željeni rezultat. S vremenom ćete razviti vlastiti stil kako budete sve više koristili promptove.

Osim tehnika koje smo obradili, postoje i neke dobre prakse koje treba uzeti u obzir pri promptanju LLM-a.

Evo nekoliko dobrih praksi koje treba razmotriti:

- **Navedite kontekst**. Kontekst je važan, što više možete specificirati poput domene, teme i slično, to bolje.
- Ograničite izlaz. Ako želite određeni broj stavki ili određenu duljinu, navedite to.
- **Navedite i što i kako**. Ne zaboravite spomenuti i što želite i kako to želite, na primjer "Napravi Python Web API s rutama products i customers, podijeli ga u 3 datoteke".
- **Koristite predloške**. Često ćete htjeti obogatiti svoje promptove podacima iz vaše tvrtke. Koristite predloške za to. Predlošci mogu imati varijable koje zamijenite stvarnim podacima.
- **Ispravno pišite**. LLM-ovi vam mogu dati točan odgovor, ali ako pravilno pišete, dobit ćete bolji odgovor.

## Zadatak

Evo koda u Pythonu koji pokazuje kako izgraditi jednostavan API koristeći Flask:

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

Koristite AI asistenta poput GitHub Copilota ili ChatGPT-a i primijenite tehniku "self-refine" za poboljšanje koda.

## Rješenje

Pokušajte riješiti zadatak dodavanjem odgovarajućih promptova u kod.

> [!TIP]
> Formulirajte prompt kojim tražite poboljšanja, dobro je ograničiti koliko poboljšanja želite. Također možete tražiti poboljšanja u određenom smjeru, na primjer arhitektura, performanse, sigurnost i slično.

[Rješenje](../../../05-advanced-prompts/python/aoai-solution.py)

## Provjera znanja

Zašto bih koristio chain-of-thought prompting? Pokaži mi 1 točan odgovor i 2 netočna odgovora.

1. Da naučim LLM kako riješiti problem.  
1. B, Da naučim LLM pronalaziti greške u kodu.  
1. C, Da uputim LLM da smisli različita rješenja.

A: 1, jer chain-of-thought znači pokazati LLM-u kako riješiti problem pružajući mu niz koraka, slične probleme i kako su oni riješeni.

## 🚀 Izazov

Upravo ste u zadatku koristili tehniku self-refine. Uzmite bilo koji program koji ste napravili i razmislite o poboljšanjima koja biste željeli primijeniti. Sada upotrijebite tehniku self-refine da primijenite predložene promjene. Kako vam se čini rezultat, bolji ili lošiji?

## Odličan posao! Nastavite s učenjem

Nakon što završite ovu lekciju, pogledajte našu [Generative AI Learning kolekciju](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) i nastavite podizati svoje znanje o Generativnoj AI!

Krenite na Lekciju 6 gdje ćemo primijeniti znanje o Prompt Engineeringu kroz [izradu aplikacija za generiranje teksta](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.