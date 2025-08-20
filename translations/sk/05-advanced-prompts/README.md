<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:39:11+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "sk"
}
-->

> "Generovať kód pre Python Web API"
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

Opätovné spustenie promptu nám prináša tento výsledok:

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

Medzi týmito dvoma výstupmi je len malý rozdiel. Teraz urobme opak, nastavme teplotu na 0,9:

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

Ako vidíte, výsledky sú oveľa rozmanitejšie.

> Note, že existuje viac parametrov, ktoré môžete meniť, aby ste ovplyvnili výstup, napríklad top-k, top-p, repetition penalty, length penalty a diversity penalty, ale tie presahujú rozsah tohto kurzu.

## Dobré praktiky

Existuje mnoho postupov, ktoré môžete použiť, aby ste dosiahli požadovaný výsledok. Postupne si vytvoríte vlastný štýl, ako budete promptovať čoraz viac.

Okrem techník, ktoré sme prebrali, je dobré zvážiť aj niektoré osvedčené postupy pri promptovaní LLM.

Tu je niekoľko dobrých praktík, ktoré stojí za to mať na pamäti:

- **Špecifikujte kontext**. Kontext je dôležitý, čím viac dokážete upresniť, napríklad doménu, tému a podobne, tým lepšie.
- Obmedzte výstup. Ak chcete konkrétny počet položiek alebo určitú dĺžku, uveďte to.
- **Uveďte čo aj ako**. Nezabudnite spomenúť, čo chcete a ako to chcete, napríklad „Vytvor Python Web API s routami products a customers, rozdeľ ho do 3 súborov“.
- **Používajte šablóny**. Často budete chcieť obohatiť svoje prompty o dáta z vašej firmy. Použite na to šablóny. Šablóny môžu obsahovať premenné, ktoré nahradíte skutočnými dátami.
- **Správne pravopisujte**. LLM vám môže dať správnu odpoveď, ale ak budete správne pravopisovať, dostanete lepšiu odpoveď.

## Zadanie

Tu je kód v Pythone, ktorý ukazuje, ako vytvoriť jednoduché API pomocou Flasku:

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

Použite AI asistenta ako GitHub Copilot alebo ChatGPT a aplikujte techniku „self-refine“ na vylepšenie kódu.

## Riešenie

Skúste vyriešiť zadanie tak, že pridáte vhodné prompty ku kódu.

> [!TIP]
> Formulujte prompt tak, aby ste požiadali o vylepšenie, je dobré obmedziť počet vylepšení. Môžete tiež požiadať o vylepšenie v konkrétnej oblasti, napríklad architektúra, výkon, bezpečnosť a podobne.

[Riešenie](../../../05-advanced-prompts/python/aoai-solution.py)

## Overenie vedomostí

Prečo by som použil chain-of-thought prompting? Ukáž mi 1 správnu odpoveď a 2 nesprávne odpovede.

1. Aby som naučil LLM, ako vyriešiť problém.  
1. B, Aby som naučil LLM hľadať chyby v kóde.  
1. C, Aby som inštruoval LLM, aby prišiel s rôznymi riešeniami.

A: 1, pretože chain-of-thought znamená ukázať LLM, ako vyriešiť problém poskytnutím série krokov a podobných problémov a ich riešení.

## 🚀 Výzva

Práve ste použili techniku self-refine v zadaní. Vezmite akýkoľvek program, ktorý ste vytvorili, a zvážte, aké vylepšenia by ste chceli aplikovať. Teraz použite techniku self-refine na zavedenie navrhovaných zmien. Ako ste hodnotili výsledok, lepší alebo horší?

## Skvelá práca! Pokračujte v učení

Po dokončení tejto lekcie si pozrite našu [kolekciu Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste ďalej rozvíjali svoje znalosti o Generatívnej AI!

Prejdite na Lekciu 6, kde využijeme naše znalosti Prompt Engineering na [vytváranie aplikácií na generovanie textu](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.