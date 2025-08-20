<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:38:44+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "cs"
}
-->

> "Generovat kód pro Python Web API"
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

Opětovné spuštění promptu nám dává tento výsledek:

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

Mezi těmito dvěma výstupy je jen malý rozdíl. Tentokrát uděláme opak, nastavíme teplotu na 0,9:

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

a druhý pokus s hodnotou teploty 0,9:

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

Jak vidíte, výsledky jsou výrazně rozmanitější.

> Note, že existuje více parametrů, které můžete měnit pro variabilitu výstupu, jako top-k, top-p, repetition penalty, length penalty a diversity penalty, ale tyto nejsou součástí tohoto kurikula.

## Dobré postupy

Existuje mnoho postupů, které můžete použít, abyste získali to, co chcete. Svůj vlastní styl si najdete, jak budete prompting používat čím dál častěji.

Kromě technik, které jsme probrali, je dobré zvážit i některé osvědčené postupy při promptování LLM.

Zde je několik dobrých postupů, které stojí za zvážení:

- **Specifikujte kontext**. Kontext je důležitý, čím více můžete upřesnit, například doménu, téma atd., tím lépe.
- Omezte výstup. Pokud chcete konkrétní počet položek nebo určitou délku, uveďte to.
- **Specifikujte co i jak**. Nezapomeňte zmínit jak to, co chcete, tak i způsob, například „Vytvoř Python Web API s routami products a customers, rozděl ho do 3 souborů“.
- **Používejte šablony**. Často budete chtít obohatit své prompty o data z vaší firmy. Použijte k tomu šablony. Šablony mohou obsahovat proměnné, které nahradíte skutečnými daty.
- **Pište správně**. LLM vám může dát správnou odpověď, ale pokud budete psát správně, dostanete lepší odpověď.

## Zadání

Zde je kód v Pythonu, který ukazuje, jak vytvořit jednoduché API pomocí Flasku:

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

Použijte AI asistenta jako GitHub Copilot nebo ChatGPT a aplikujte techniku „self-refine“ pro vylepšení kódu.

## Řešení

Zkuste vyřešit zadání přidáním vhodných promptů ke kódu.

> [!TIP]
> Formulujte prompt tak, aby požadoval vylepšení, je dobré omezit počet vylepšení. Můžete také požádat o vylepšení v určité oblasti, například architektura, výkon, bezpečnost atd.

[Řešení](../../../05-advanced-prompts/python/aoai-solution.py)

## Kontrola znalostí

Proč bych použil chain-of-thought prompting? Ukažte mi 1 správnou odpověď a 2 nesprávné.

1. Abych naučil LLM, jak vyřešit problém.
1. B, Abych naučil LLM hledat chyby v kódu.
1. C, Abych instruoval LLM, aby přišel s různými řešeními.

A: 1, protože chain-of-thought znamená ukázat LLM, jak problém vyřešit, tím, že mu poskytneme sérii kroků a podobné problémy a jejich řešení.

## 🚀 Výzva

Právě jste v zadání použili techniku self-refine. Vezměte jakýkoli program, který jste vytvořili, a zamyslete se, jaká vylepšení byste na něm chtěli aplikovat. Nyní použijte techniku self-refine k provedení navrhovaných změn. Jaký byl podle vás výsledek, lepší nebo horší?

## Skvělá práce! Pokračujte ve vzdělávání

Po dokončení této lekce se podívejte na naši [kolekci Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kde můžete pokračovat ve zvyšování svých znalostí o Generative AI!

Přejděte do Lekce 6, kde využijeme naše znalosti Prompt Engineering tím, že [vytvoříme aplikace pro generování textu](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.