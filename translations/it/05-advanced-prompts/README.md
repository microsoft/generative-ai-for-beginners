<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:31:19+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "it"
}
-->

> "Genera codice per una Web API in Python"
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

Eseguire di nuovo il prompt ci dà questo risultato:

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

C’è solo una piccola differenza tra questi due output. Facciamo il contrario questa volta, impostiamo la temperatura a 0.9:

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

e il secondo tentativo con temperatura 0.9:

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

Come puoi vedere, i risultati non potrebbero essere più diversi.

> Nota che ci sono altri parametri che puoi modificare per variare l’output, come top-k, top-p, repetition penalty, length penalty e diversity penalty, ma questi esulano dallo scopo di questo corso.

## Buone pratiche

Ci sono molte pratiche che puoi applicare per cercare di ottenere ciò che desideri. Troverai il tuo stile man mano che userai il prompting sempre di più.

Oltre alle tecniche che abbiamo trattato, ci sono alcune buone pratiche da considerare quando si fa prompting a un LLM.

Ecco alcune buone pratiche da tenere a mente:

- **Specifica il contesto**. Il contesto è importante, più riesci a specificare come dominio, argomento, ecc., meglio è.
- Limita l’output. Se vuoi un numero specifico di elementi o una lunghezza precisa, specifica questo.
- **Specifica sia cosa che come**. Ricorda di indicare sia cosa vuoi che come lo vuoi, per esempio “Crea una Web API Python con le rotte products e customers, dividila in 3 file”.
- **Usa template**. Spesso vorrai arricchire i tuoi prompt con dati della tua azienda. Usa template per farlo. I template possono avere variabili che sostituisci con dati reali.
- **Scrivi correttamente**. Gli LLM potrebbero darti una risposta corretta, ma se scrivi correttamente otterrai una risposta migliore.

## Compito

Ecco un codice in Python che mostra come costruire una semplice API usando Flask:

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

Usa un assistente AI come GitHub Copilot o ChatGPT e applica la tecnica del “self-refine” per migliorare il codice.

## Soluzione

Prova a risolvere il compito aggiungendo prompt adeguati al codice.

> [!TIP]
> Formula un prompt per chiedere di migliorare, è una buona idea limitare il numero di miglioramenti. Puoi anche chiedere di migliorarlo in un certo modo, per esempio architettura, performance, sicurezza, ecc.

[Soluzione](../../../05-advanced-prompts/python/aoai-solution.py)

## Verifica delle conoscenze

Perché userei il chain-of-thought prompting? Mostrami 1 risposta corretta e 2 risposte errate.

1. Per insegnare all’LLM come risolvere un problema.  
1. B, Per insegnare all’LLM a trovare errori nel codice.  
1. C, Per istruire l’LLM a proporre soluzioni diverse.

A: 1, perché il chain-of-thought consiste nel mostrare all’LLM come risolvere un problema fornendogli una serie di passaggi, problemi simili e come sono stati risolti.

## 🚀 Sfida

Hai appena usato la tecnica del self-refine nel compito. Prendi un qualsiasi programma che hai creato e considera quali miglioramenti vorresti applicargli. Ora usa la tecnica del self-refine per applicare i cambiamenti proposti. Cosa pensi del risultato, migliore o peggiore?

## Ottimo lavoro! Continua a imparare

Dopo aver completato questa lezione, dai un’occhiata alla nostra [collezione di apprendimento su Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare le tue conoscenze sull’AI generativa!

Passa alla Lezione 6 dove applicheremo le nostre conoscenze di Prompt Engineering [costruendo app per la generazione di testo](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.