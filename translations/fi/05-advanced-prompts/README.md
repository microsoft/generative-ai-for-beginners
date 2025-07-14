<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:34:51+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "fi"
}
-->

> "Luo koodi Python-verkkopalvelulle"
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

Kun suoritat kehotteen uudelleen, saamme tämän tuloksen:

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

Näiden kahden tulosteen välillä on vain pieni ero. Tehdäänpä nyt päinvastoin, asetetaan lämpötila arvoksi 0,9:

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

ja toinen yritys lämpötilalla 0,9:

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

Kuten näet, tulokset eivät voisi olla enempää erilaisia.

> Huomaa, että voit muuttaa myös muita parametreja vaihtelevan tuloksen saamiseksi, kuten top-k, top-p, repetition penalty, length penalty ja diversity penalty, mutta nämä eivät kuulu tämän oppimateriaalin aihepiiriin.

## Hyviä käytäntöjä

On monia tapoja, joilla voit yrittää saada haluamasi tuloksen. Löydät oman tyylisi, kun käytät kehotteita yhä enemmän.

Tekniikoiden lisäksi, joita olemme käsitelleet, on hyvä ottaa huomioon myös joitakin hyviä käytäntöjä LLM:n kehotteiden laatimisessa.

Tässä muutamia hyviä käytäntöjä:

- **Määritä konteksti**. Kontekstilla on merkitystä, mitä tarkemmin voit määritellä esimerkiksi toimialan, aiheen jne., sitä parempi.
- Rajoita tulostetta. Jos haluat tietyn määrän kohteita tai tietyn pituisen vastauksen, mainitse se.
- **Määritä sekä mitä että miten**. Muista kertoa sekä mitä haluat että miten haluat sen, esimerkiksi "Luo Python Web API, jossa on reitit products ja customers, ja jaa se kolmeen tiedostoon".
- **Käytä malleja**. Usein haluat rikastaa kehotteitasi yrityksesi tiedoilla. Käytä malleja tähän. Mallit voivat sisältää muuttujia, jotka korvaat todellisilla tiedoilla.
- **Kirjoita oikein**. LLM voi antaa oikean vastauksen, mutta oikeinkirjoituksella saat paremman vastauksen.

## Tehtävä

Tässä on Python-koodi, joka näyttää, miten rakennetaan yksinkertainen API Flaskin avulla:

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

Käytä tekoälyavustajaa, kuten GitHub Copilotia tai ChatGPT:tä, ja sovella "self-refine" -tekniikkaa parantaaksesi koodia.

## Ratkaisu

Yritä ratkaista tehtävä lisäämällä sopivia kehotteita koodiin.

> [!TIP]
> Muotoile kehotteesi niin, että pyydät parannuksia, ja on hyvä rajoittaa parannusten määrää. Voit myös pyytää parannuksia tietyllä tavalla, esimerkiksi arkkitehtuuri, suorituskyky, turvallisuus jne.

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## Tietovisa

Miksi käyttäisin chain-of-thought -kehotteita? Näytä 1 oikea vastaus ja 2 väärää vastausta.

1. Opettaakseni LLM:lle, miten ratkaista ongelma.
1. B, Opettaakseni LLM:lle virheiden etsimistä koodista.
1. C, Ohjatakseni LLM:ää keksimään erilaisia ratkaisuja.

A: 1, koska chain-of-thought tarkoittaa, että näytetään LLM:lle, miten ongelma ratkaistaan antamalla sille sarja vaiheita sekä samankaltaisia ongelmia ja niiden ratkaisuja.

## 🚀 Haaste

Käytit juuri self-refine -tekniikkaa tehtävässä. Ota mikä tahansa ohjelma, jonka olet rakentanut, ja pohdi, mitä parannuksia haluaisit siihen tehdä. Käytä nyt self-refine -tekniikkaa ehdotettujen muutosten toteuttamiseen. Miltä lopputulos vaikutti, paremmalta vai huonommalta?

## Hienoa työtä! Jatka oppimista

Kun olet suorittanut tämän oppitunnin, tutustu [Generative AI Learning -kokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi Generative AI -osaamisesi kehittämistä!

Siirry oppitunnille 6, jossa sovellamme Prompt Engineering -taitojamme [rakentamalla tekstin generointisovelluksia](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.