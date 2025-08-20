<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:37:48+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "sw"
}
-->

# Tengeneza msimbo kwa ajili ya Python Web API

Katika mwongozo huu, tutakuonyesha jinsi ya kuunda API ya wavuti kwa kutumia Python. API hii itaruhusu mawasiliano kati ya programu mbalimbali kupitia mtandao.

## Hatua za Kuanzisha

1. **Sakinisha maktaba zinazohitajika**  
   Hakikisha umeweka maktaba kama `Flask` au `FastAPI` kwa kutumia pip.

2. **Unda faili la msimbo**  
   Tengeneza faili mpya la Python, kwa mfano `app.py`, ambapo utaunda API yako.

3. **Andika msimbo wa API**  
   Tumia maktaba ulizoweka kuandika njia za API zinazoshughulikia maombi ya HTTP kama GET, POST, PUT, na DELETE.

## Mfano wa Msimbo

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Hifadhi data za mfano
data = []

@app.route('/items', methods=['GET'])
def get_items():
    # Rudisha orodha ya vitu
    return jsonify(data)

@app.route('/items', methods=['POST'])
def add_item():
    # Ongeza kipengee kipya kwenye data
    item = request.json
    data.append(item)
    return jsonify(item), 201

if __name__ == '__main__':
    app.run(debug=True)
```

## Vidokezo Muhimu

- [!TIP] Hakikisha API yako ina usalama wa kutosha kama uthibitishaji na idhini.
- [!IMPORTANT] Tumia `debug=True` tu wakati wa maendeleo, si katika mazingira ya uzalishaji.
- [!WARNING] Usihifadhi data nyeti moja kwa moja kwenye API bila usimbaji fiche.

Kwa kufuata mwongozo huu, utaweza kuunda API ya wavuti yenye ufanisi kwa kutumia Python.
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

Kukimbia prompt tena kunatupa matokeo haya:

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

Kuna tofauti ndogo sana kati ya matokeo haya mawili. Sasa tufanye kinyume, tutaweka joto (temperature) kuwa 0.9:

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

na jaribio la pili kwa joto 0.9:

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

Kama unavyoona, matokeo hayawezi kuwa tofauti zaidi.

> Note, kwamba kuna vigezo vingine zaidi unaweza kubadilisha ili kubadilisha matokeo, kama top-k, top-p, adhabu ya kurudia, adhabu ya urefu na adhabu ya utofauti lakini haya yako nje ya muktadha wa mtaala huu.

## Mazoezi mazuri

Kuna mazoezi mengi unaweza kutumia ili kupata unachotaka. Utapata mtindo wako mwenyewe unapotumia prompting zaidi na zaidi.

Mbali na mbinu tulizozifunua, kuna mazoezi mazuri ya kuzingatia unapotumia LLM.

Hapa kuna mazoezi mazuri ya kuzingatia:

- **Taja muktadha**. Muktadha ni muhimu, kadri unavyoweza kuelezea zaidi kama eneo, mada, n.k. ndivyo bora.
- Punguza matokeo. Ikiwa unataka idadi maalum ya vitu au urefu maalum, taja hilo.
- **Taja kile na jinsi**. Kumbuka kutaja kile unachotaka na jinsi unavyotaka, kwa mfano "Tengeneza Python Web API yenye routes products na customers, igawanye katika mafaili 3".
- **Tumia templates**. Mara nyingi, utataka kuongeza data ya kampuni yako kwenye prompts zako. Tumia templates kufanya hivyo. Templates zinaweza kuwa na variables unazobadilisha na data halisi.
- **Taja maneno kwa usahihi**. LLM zinaweza kutoa jibu sahihi, lakini ukitaja maneno kwa usahihi, utapata jibu bora zaidi.

## Kazi ya nyumbani

Hapa kuna msimbo wa Python unaoonyesha jinsi ya kujenga API rahisi kwa kutumia Flask:

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

Tumia msaidizi wa AI kama GitHub Copilot au ChatGPT na tumia mbinu ya "self-refine" kuboresha msimbo.

## Suluhisho

Tafadhali jaribu kutatua kazi ya nyumbani kwa kuongeza prompts zinazofaa kwenye msimbo.

> [!TIP]
> Andika prompt ya kuomba iboreshe, ni wazo zuri kupunguza idadi ya maboresho. Pia unaweza kuomba iboreshe kwa njia fulani, kwa mfano usanifu, utendaji, usalama, n.k.

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## Kagua maarifa

Kwa nini ningetumia chain-of-thought prompting? Nionyeshe jibu 1 sahihi na majibu 2 yasiyo sahihi.

1. Kufundisha LLM jinsi ya kutatua tatizo.
1. B, Kufundisha LLM kutambua makosa kwenye msimbo.
1. C, Kuelekeza LLM kuja na suluhisho tofauti.

J: 1, kwa sababu chain-of-thought ni kuhusu kuonyesha LLM jinsi ya kutatua tatizo kwa kumpa hatua mfululizo, na matatizo yanayofanana na jinsi yalivyotatuliwa.

## 🚀 Changamoto

Umetumia mbinu ya self-refine kwenye kazi ya nyumbani. Chukua programu yoyote uliyotengeneza na fikiria maboresho unayopenda kuifanya. Sasa tumia mbinu ya self-refine kutekeleza mabadiliko yaliyopendekezwa. Umefikiri matokeo ni bora au mabaya?

## Kazi Nzuri! Endelea Kujifunza

Baada ya kumaliza somo hili, angalia [Mkusanyiko wetu wa Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza maarifa yako ya AI ya Kizazi!

Nenda kwenye Somo la 6 ambapo tutatumia maarifa yetu ya Prompt Engineering kwa [kujenga programu za kizazi cha maandishi](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.