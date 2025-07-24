<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:39:37+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "ro"
}
-->

> "Generează cod pentru un API Web Python"
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

Rularea promptului din nou ne oferă acest rezultat:

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

Există doar o mică diferență între aceste două rezultate. De data aceasta să facem opusul, să setăm temperatura la 0.9:

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

și a doua încercare cu temperatura setată la 0.9:

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

După cum vezi, rezultatele nu ar putea fi mai variate.

> Reține că există mai mulți parametri pe care îi poți modifica pentru a varia rezultatul, cum ar fi top-k, top-p, penalizarea repetării, penalizarea lungimii și penalizarea diversității, dar aceștia sunt în afara domeniului acestui curriculum.

## Practici bune

Există multe practici pe care le poți aplica pentru a obține ceea ce dorești. Îți vei găsi propriul stil pe măsură ce folosești prompting-ul tot mai mult.

Pe lângă tehnicile pe care le-am acoperit, există câteva practici bune de luat în considerare când faci prompting unui LLM.

Iată câteva practici bune de avut în vedere:

- **Specifică contextul**. Contextul contează, cu cât poți specifica mai mult, cum ar fi domeniul, subiectul etc., cu atât mai bine.
- Limitează rezultatul. Dacă dorești un număr specific de elemente sau o anumită lungime, specifică acest lucru.
- **Specifică atât ce, cât și cum**. Amintește să menționezi atât ce vrei, cât și cum vrei, de exemplu „Creează o API Web Python cu rutele products și customers, împarte-o în 3 fișiere”.
- **Folosește șabloane**. De multe ori, vei dori să îmbogățești prompturile cu date din compania ta. Folosește șabloane pentru asta. Șabloanele pot avea variabile pe care le înlocuiești cu date reale.
- **Ortografia corectă**. LLM-urile pot oferi un răspuns corect, dar dacă scrii corect, vei primi un răspuns mai bun.

## Tema

Iată un cod în Python care arată cum să construiești o API simplă folosind Flask:

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

Folosește un asistent AI precum GitHub Copilot sau ChatGPT și aplică tehnica „self-refine” pentru a îmbunătăți codul.

## Soluție

Încearcă să rezolvi tema adăugând prompturi potrivite în cod.

> [!TIP]
> Formulează un prompt prin care să ceri îmbunătățiri, este o idee bună să limitezi câte îmbunătățiri dorești. Poți cere și să fie îmbunătățit într-un anumit mod, de exemplu arhitectură, performanță, securitate etc.

[Soluție](../../../05-advanced-prompts/python/aoai-solution.py)

## Verificare cunoștințe

De ce aș folosi chain-of-thought prompting? Arată-mi 1 răspuns corect și 2 răspunsuri greșite.

1. Pentru a învăța LLM-ul cum să rezolve o problemă.  
1. B, Pentru a învăța LLM-ul să găsească erori în cod.  
1. C, Pentru a instrui LLM-ul să vină cu soluții diferite.

Răspuns: 1, pentru că chain-of-thought înseamnă să arăți LLM-ului cum să rezolve o problemă oferindu-i o serie de pași și probleme similare și modul în care au fost rezolvate.

## 🚀 Provocare

Tocmai ai folosit tehnica self-refine în temă. Ia orice program pe care l-ai construit și gândește-te ce îmbunătățiri ai vrea să aplici. Acum folosește tehnica self-refine pentru a aplica schimbările propuse. Cum ți s-a părut rezultatul, mai bun sau mai slab?

## Felicitări! Continuă să înveți

După ce ai terminat această lecție, aruncă o privire la colecția noastră [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a-ți continua dezvoltarea cunoștințelor despre Generative AI!

Mergi la Lecția 6 unde vom aplica cunoștințele despre Prompt Engineering prin [construirea de aplicații de generare text](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.