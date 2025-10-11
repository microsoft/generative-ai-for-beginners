<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-10-11T11:37:17+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "et"
}
-->
# Täiustatud käskude loomine

[![Täiustatud käskude loomine](../../../translated_images/05-lesson-banner.522610fd4a2cd82dbed66bb7e6fe104ed6da172e085dbb4d9100b28dc73ed435.et.png)](https://aka.ms/gen-ai-lesson5-gh?WT.mc_id=academic-105485-koreyst?WT.mc_id=academic-105485-koreyst)

Tuletame meelde eelmises peatükis õpitut:

> Käskude _kujundamine_ on protsess, mille käigus me **suuname mudeli asjakohasemate vastuste poole**, pakkudes kasulikumaid juhiseid või konteksti.

Käskude kirjutamiseks on kaks sammu: esmalt käskude koostamine, pakkudes asjakohast konteksti, ja teiseks _optimeerimine_, kuidas käsku järk-järgult paremaks muuta.

Praeguseks oleme saanud põhilise arusaama käskude kirjutamisest, kuid peame minema sügavamale. Selles peatükis liigume erinevate käskude katsetamisest arusaamiseni, miks üks käsk on parem kui teine. Õpid, kuidas koostada käske, järgides mõningaid põhilisi tehnikaid, mida saab rakendada igale LLM-ile.

## Sissejuhatus

Selles peatükis käsitleme järgmisi teemasid:

- Laienda oma teadmisi käskude kujundamisest, rakendades erinevaid tehnikaid.
- Kohanda oma käske, et muuta väljundit.

## Õpieesmärgid

Pärast selle peatüki läbimist suudad:

- Rakendada käskude kujundamise tehnikaid, mis parandavad käskude tulemusi.
- Teostada käskude loomist, mis on kas varieeruv või deterministlik.

## Käskude kujundamine

Käskude kujundamine on protsess, mille käigus luuakse käske, mis annavad soovitud tulemuse. Käskude kujundamine ei tähenda ainult tekstilise käsu kirjutamist. Tegemist on pigem tehnikate kogumiga, mida saab rakendada soovitud tulemuse saavutamiseks.

### Käskude näide

Vaatame ühte lihtsat käsku:

> Loo 10 küsimust geograafia kohta.

Selles käsus rakendad tegelikult mitmeid erinevaid käskude kujundamise tehnikaid.

Lahkame seda.

- **Kontekst**, sa täpsustad, et see peaks olema "geograafia" kohta.
- **Väljundi piiramine**, sa soovid mitte rohkem kui 10 küsimust.

### Lihtsate käskude piirangud

Sa võid saada soovitud tulemuse, aga võib juhtuda, et saadud küsimused ei vasta ootustele, kuna:

- **Suur teema**, sa ei tea, kas küsimused puudutavad riike, pealinnu, jõgesid jne.
- **Formaat**, mis siis, kui sa soovid, et küsimused oleksid teatud viisil vormistatud?

Nagu näha, on käskude loomisel palju asju, mida arvestada.

Siiani oleme näinud lihtsa käsu näidet, kuid generatiivne tehisintellekt suudab palju rohkem aidata erinevates rollides ja tööstusharudes. Uurime järgmisi põhilisi tehnikaid.

### Käskude loomise tehnikad

Esmalt peame mõistma, et käskude loomine on LLM-i _emergentne_ omadus, mis tähendab, et see pole mudelisse sisse ehitatud funktsioon, vaid midagi, mida avastame mudelit kasutades.

LLM-i käskude loomiseks on mõned põhilised tehnikad. Uurime neid.

- **Nullnäidisega käskude loomine**, see on kõige lihtsam käskude loomise vorm. See on üksik käsk, mis palub LLM-il vastata ainult oma treeningandmete põhjal.
- **Mõnenäidisega käskude loomine**, see käskude loomise tüüp juhendab LLM-i, pakkudes 1 või rohkem näiteid, millele tuginedes mudel vastuse genereerib.
- **Mõttekäigu ahel**, see käskude loomise tüüp õpetab LLM-i, kuidas probleemi sammudeks jagada.
- **Genereeritud teadmised**, käskude vastuse parandamiseks saab lisaks käsule pakkuda genereeritud fakte või teadmisi.
- **Vähemast rohkemani**, nagu mõttekäigu ahel, on see tehnika seotud probleemi jagamisega sammudeks ja nende sammude järjestikuse täitmisega.
- **Iseparandus**, see tehnika seisneb LLM-i väljundi kriitilises hindamises ja selle parandamise palumises.
- **Maieutiline käskude loomine**, siin soovid tagada, et LLM-i vastus oleks korrektne, ja palud mudelil selgitada vastuse erinevaid osi. See on iseparanduse vorm.

### Nullnäidisega käskude loomine

See käskude loomise stiil on väga lihtne, see koosneb ühest käsust. Tõenäoliselt kasutad seda tehnikat, kui alles õpid LLM-e tundma. Näide:

- Käsk: "Mis on algebra?"
- Vastus: "Algebra on matemaatika haru, mis uurib matemaatilisi sümboleid ja nende manipuleerimise reegleid."

### Mõnenäidisega käskude loomine

See käskude loomise stiil aitab mudelit, pakkudes mõningaid näiteid koos päringuga. See koosneb ühest käsust koos täiendavate ülesandespetsiifiliste andmetega. Näide:

- Käsk: "Kirjuta luuletus Shakespeare'i stiilis. Siin on mõned näited Shakespeare'i sonettidest:
  Sonett 18: 'Kas ma võrdlen sind suvepäevaga? Sa oled armsam ja mõõdukam...'
  Sonett 116: 'Ärgu olgu tõeliste mõtete abielus takistusi. Armastus pole armastus, mis muutub, kui muutus leiab...'
  Sonett 132: 'Sinu silmi ma armastan, ja need, nagu halastades mind, Teades su südame piina, piinavad mind põlgusega,...'
  Nüüd kirjuta sonett kuu ilust."
- Vastus: "Taevasse kuu pehmelt särab, Hõbedases valguses, mis heidab oma õrna armu,..."

Näited annavad LLM-ile konteksti, formaadi või stiili soovitud väljundi jaoks. Need aitavad mudelil mõista konkreetset ülesannet ja genereerida täpsemaid ja asjakohasemaid vastuseid.

### Mõttekäigu ahel

Mõttekäigu ahel on väga huvitav tehnika, kuna see seisneb LLM-i juhendamises läbi sammude seeria. Idee on õpetada LLM-i, kuidas midagi teha. Vaatame järgmist näidet, ilma ja koos mõttekäigu ahelaga:

    - Käsk: "Alice'il on 5 õuna, ta viskab 3 õuna, annab 2 Bobile ja Bob annab ühe tagasi, mitu õuna on Alice'il?"
    - Vastus: 5

LLM vastab 5, mis on vale. Õige vastus on 1 õun, arvestades arvutust (5 -3 -2 + 1 = 1).

Kuidas saame õpetada LLM-i seda õigesti tegema?

Proovime mõttekäigu ahelat. Mõttekäigu ahela rakendamine tähendab:

1. Anna LLM-ile sarnane näide.
1. Näita arvutust ja kuidas seda õigesti arvutada.
1. Esita algne käsk.

Näide:

- Käsk: "Lisal on 7 õuna, ta viskab 1 õuna, annab 4 õuna Bartile ja Bart annab ühe tagasi:
  7 -1 = 6
  6 -4 = 2
  2 +1 = 3  
  Alice'il on 5 õuna, ta viskab 3 õuna, annab 2 Bobile ja Bob annab ühe tagasi, mitu õuna on Alice'il?"
  Vastus: 1

Pane tähele, kuidas kirjutame oluliselt pikema käsu, lisame teise näite, arvutuse ja seejärel algse käsu ning jõuame õige vastuseni 1.

Nagu näha, on mõttekäigu ahel väga võimas tehnika.

### Genereeritud teadmised

Sageli, kui soovid koostada käsku, tahad seda teha, kasutades oma ettevõtte andmeid. Osa käsust peaks tulema ettevõttest ja teine osa peaks olema tegelik käsk, mis sind huvitab.

Näiteks, kui oled kindlustusäris, võib sinu käsk välja näha selline:

```text
{{company}}: {{company_name}}
{{products}}:
{{products_list}}
Please suggest an insurance given the following budget and requirements:
Budget: {{budget}}
Requirements: {{requirements}}
```

Ülal näed, kuidas käsk on koostatud, kasutades malli. Mallis on mitmeid muutujaid, tähistatud `{{variable}}`, mis asendatakse tegelike väärtustega ettevõtte API-st.

Näide, kuidas käsk võib välja näha, kui muutujad on asendatud ettevõtte sisuga:

```text
Insurance company: ACME Insurance
Insurance products (cost per month):
- Car, cheap, 500 USD
- Car, expensive, 1100 USD
- Home, cheap, 600 USD
- Home, expensive, 1200 USD
- Life, cheap, 100 USD

Please suggest an insurance given the following budget and requirements:
Budget: $1000
Requirements: Car, Home, and Life insurance
```

Selle käsu LLM-i kaudu käivitamine annab vastuse nagu:

```output
Given the budget and requirements, we suggest the following insurance package from ACME Insurance:
- Car, cheap, 500 USD
- Home, cheap, 600 USD
- Life, cheap, 100 USD
Total cost: $1,200 USD
```

Nagu näha, soovitab see ka elukindlustust, mida see ei peaks. See tulemus viitab sellele, et peame käsku optimeerima, muutes selle selgemaks, mida see lubada võib. Pärast mõningast _katsetamist ja eksimist_ jõuame järgmise käsuni:

```text
Insurance company: ACME Insurance
Insurance products (cost per month):
- type: Car, cheap, cost: 500 USD
- type: Car, expensive, cost: 1100 USD
- type: Home, cheap, cost: 600 USD
- type: Home, expensive, cost: 1200 USD
- type: Life, cheap, cost: 100 USD

Please suggest an insurance given the following budget and requirements:
Budget: $1000 restrict choice to types: Car, Home
```

Pane tähele, kuidas _tüüp_ ja _maksumus_ lisamine ning märksõna _piiramine_ kasutamine aitavad LLM-il mõista, mida me tahame.

Nüüd saame järgmise vastuse:

```output
Given the budget and requirements, we suggest the Car, Cheap insurance product which costs 500 USD per month.
```

Selle näite eesmärk oli näidata, et isegi kui kasutame põhilist tehnikat nagu _genereeritud teadmised_, peame enamikul juhtudel käsku optimeerima, et saada soovitud tulemus.

### Vähemast rohkemani

Vähemast rohkemani käskude loomise idee seisneb suurema probleemi jagamises alamprobleemideks. Nii aitad LLM-il "vallutada" suurema probleemi. Hea näide võiks olla andmeteadus, kus saad paluda LLM-il probleemi jagada järgmiselt:

> Käsk: Kuidas teostada andmeteadust 5 sammuga?

Sinu AI assistent vastab:

1. Kogu andmed
1. Puhasta andmed
1. Analüüsi andmeid
1. Kujuta andmeid
1. Esita andmed

### Iseparandus, tulemuste kriitika

Generatiivsete tehisintellektide ja LLM-ide puhul ei saa väljundit usaldada. Sa pead seda kontrollima. Lõppude lõpuks esitab LLM sulle lihtsalt seda, mis on kõige tõenäolisem järgmisena öelda, mitte seda, mis on õige. Seetõttu on hea mõte paluda LLM-il ennast kritiseerida, mis viib meid iseparanduse tehnikani.

Kuidas see töötab:

1. Esmane käsk, mis palub LLM-il probleemi lahendada
1. LLM vastab
1. Sa kritiseerid vastust ja palud AI-l seda parandada
1. LLM vastab uuesti, seekord arvestades kriitikat ja pakkudes lahendusi, millele ta jõudis

Seda protsessi saab korrata nii palju kordi, kui soovid.

Näide selle tehnika kasutamisest:

> Käsk: "Loo Python Web API marsruutidega tooted ja kliendid"

AI vastus:

```python
import flask
app = Flask(__name__)

@app.route('/products')
def products():
    return 'Products'

@app.route('/customers')
def customers():
    return 'Customers'
```

> Käsk: soovita 3 parandust ülaltoodud koodile

AI vastus:

```text
Sure, here are three suggestions to improve the code:

Import the correct module: The first line should import Flask instead of flask. The correct import statement should be from flask import Flask.

Add a main function: Add a if __name__ == '__main__': block to the end of the file to run the application when the file is executed.

Use f-strings: Use f-strings to format the return statements in the route functions. For example, return 'Products' can be changed to return f'This is the {request.path} page'.
```

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/products')
def products():
    return f'This is the {request.path} page'

@app.route('/customers')
def customers():
    return f'This is the {request.path} page'

if __name__ == '__main__':
    app.run()
```

Nagu näha, parandab ülaltoodud AI vastus esimest soovitatud koodi tänu esimese vastuse kriitikale.

### Maieutiline käskude loomine

Maieutiline käskude loomine on tehnika, mis sarnaneb iseparandusega, kuid keskendub rohkem LLM-i vastuse selgitamisele. Eesmärk on vähendada LLM-i väljundi vastuolusid, et tagada õige vastus. Töövoog, mida järgida:

1. Palu LLM-il vastata küsimusele
1. Iga vastuse osa kohta palu LLM-il seda põhjalikumalt selgitada.
1. Kui esineb vastuolusid, hülga osad, mis on vastuolulised.

Korda samme 2 ja 3, kuni oled vastusega rahul.

Näide käsust:

> Käsk: Kuidas luua kriisiplaan pandeemia leevendamiseks 5 sammuga?
> LLM vastus:

```text
1. Identify the risks
1. Identify the stakeholders
1. Identify the resources
1. Identify the actions
1. Identify the communication channels
```

See tuvastab 5 sammu, kuid kas saame kindlaks teha, kas see on õige? Palume LLM-il iga sammu selgitada:

> Käsk: Selgita esimest sammu põhjalikumalt, millised on pandeemia riskid üksikasjalikult?

```text
The risks are the following:

- Loss of life
- Loss of business
- Loss of reputation
- Loss of customers
- Loss of employees
```

Sel hetkel tahame veenduda, et LLM on õige, seega palume tal selgitada esimest riski üksikasjalikumalt ja loodame, et see on ülaltoodud vastusega kooskõlas:

> Käsk: Pandeemia korral, mis on suurim risk ja miks?

```text
The biggest risk is loss of life because it's the most important thing to protect.
```

> Millised on kaks suurimat riski pandeemia korral?

```text
The two biggest risks are loss of life and loss of business.
```

Sel hetkel on LLM järjekindel ja mainib "elu" ja "äri" kui kahte suurimat riski. Nüüd saame liikuda järgmise sammu juurde ja olla üsna kindlad. Kuid me ei tohiks LLM-i pimesi usaldada, alati tuleks väljundit kontrollida.

## Muuda oma väljundit

LLM-id on oma olemuselt mitte-deterministlikud, mis tähendab, et saad iga kord sama käsku käivitades erinevaid tulemusi. Proovi näiteks järgmist käsku:

> "Genereeri kood Python Web API jaoks"

```python
# Import necessary modules
import flask
from flask import request, jsonify

# Create a Flask app
app = flask.Flask(__name__)

# Create a route for the API
@app.route('/api', methods=['GET'])
def api():
    # Get the data from the request
    data = request.args

    # Process the data
    result = process_data(data)

    # Return the result as JSON
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

Sama käsku uuesti käivitades genereeritakse veidi erinev vastus:

```python
#import necessary packages
import flask
from flask import request, jsonify

#create the Flask application
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#create a list of books
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

#create an endpoint for the API
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Books API</h1>
<p>A prototype API for retrieving books.</p>'''

#create an endpoint to return all books
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

#create an endpoint to return a single book
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    #check if an ID was provided as part of the URL
    #if ID is provided, assign it to a variable
    #if no ID is provided, display an error
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    #create an empty list for our results
    results = []

    #loop through the data and match results that fit the requested ID
    #IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    #use the jsonify function from Flask to convert our list of
    #Python dictionaries to the JSON format
    return jsonify(results)

app.run()
```

> Kas varieeruv väljund on probleem?

Sõltub sellest, mida sa üritad teha. Kui soovid konkreetset vastust, siis on see probleem. Kui oled rahul varieeruva väljundiga, nagu "Genereeri 3 küsimust geograafia kohta", siis pole see probleem.

### Temperatuuri kasutamine väljundi varieerimiseks

Oleme otsustanud, et soovime piirata väljundit, et see oleks ennustatavam, st deterministlikum. Kuidas seda teha?

Temperatuur on väärtus vahemikus 0 kuni 1, kus 0 on kõige deterministlikum ja 1 kõige varieeruvam. Vaikeväärtus on 0.7. Vaatame, mis juhtub, kui käivitame sama käsu kaks korda temperatuuriga 0.1:

> "Genereeri kood Python Web API jaoks"

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

Käsku uuesti käivitades saame järgmise tulemuse:

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

Nende kahe väljundi vahel on ainult väike erinevus. Proovime seekord vastupidist, määrame temperatuuri väärtuseks 0.9:

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

ja teine katse temperatuuriga 0.9:
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

Nagu näha, võivad tulemused olla väga erinevad.

> Pange tähele, et on veel parameetreid, mida saate muuta, et väljundit varieerida, nagu top-k, top-p, korduse karistus, pikkuse karistus ja mitmekesisuse karistus, kuid need jäävad selle õppekava ulatusest välja.

## Head tavad

On mitmeid praktikaid, mida saate rakendada, et saavutada soovitud tulemus. Oma stiili leiate, kui kasutate järjest rohkem suunamist.

Lisaks tehnikatele, mida oleme käsitlenud, on mõned head tavad, mida tasub LLM-i suunamisel arvestada.

Siin on mõned head tavad, mida kaaluda:

- **Määratlege kontekst**. Kontekst on oluline – mida rohkem saate määratleda, näiteks valdkond, teema jne, seda parem.
- Piirake väljundit. Kui soovite kindlat arvu üksusi või kindlat pikkust, täpsustage see.
- **Määratlege nii mida kui ka kuidas**. Ärge unustage mainida nii seda, mida soovite, kui ka seda, kuidas soovite, näiteks "Loo Python Web API marsruutidega products ja customers, jaga see 3 failiks".
- **Kasutage malle**. Sageli soovite rikastada oma suunamisi ettevõtte andmetega. Kasutage selleks malle. Mallides võivad olla muutujad, mida asendate tegelike andmetega.
- **Kirjutage õigesti**. LLM-id võivad anda teile õige vastuse, kuid kui kirjutate õigesti, saate parema vastuse.

## Ülesanne

Siin on Pythonis kirjutatud kood, mis näitab, kuidas luua lihtsat API-d Flaski abil:

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

Kasutage AI assistenti, nagu GitHub Copilot või ChatGPT, ja rakendage "self-refine" tehnikat koodi täiustamiseks.

## Lahendus

Proovige ülesannet lahendada, lisades koodile sobivaid suunamisi.

> [!TIP]
> Sõnastage suunamine, et paluda koodi täiustada; hea mõte on piirata, kui palju täiustusi tehakse. Samuti võite paluda täiustada seda teatud viisil, näiteks arhitektuuri, jõudluse, turvalisuse jne osas.

[Lahendus](../../../05-advanced-prompts/python/aoai-solution.py)

## Teadmiste kontroll

Miks ma kasutaksin chain-of-thought suunamist? Näidake mulle 1 õiget vastust ja 2 valet vastust.

1. Õpetada LLM-ile, kuidas probleemi lahendada.
1. B, Õpetada LLM-ile, kuidas leida vigu koodis.
1. C, Juhendada LLM-i leidma erinevaid lahendusi.

A: 1, sest chain-of-thought seisneb selles, et näidata LLM-ile, kuidas probleemi lahendada, pakkudes sellele sammude jada, sarnaseid probleeme ja nende lahendusi.

## 🚀 Väljakutse

Te just kasutasite ülesandes self-refine tehnikat. Võtke mõni programm, mille olete loonud, ja mõelge, milliseid täiustusi sooviksite sellele rakendada. Kasutage nüüd self-refine tehnikat, et kavandatud muudatused rakendada. Mis te arvate, kas tulemus oli parem või halvem?

## Suurepärane töö! Jätkake õppimist

Pärast selle õppetunni lõpetamist vaadake meie [Generatiivse AI õppekollektsiooni](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma generatiivse AI teadmiste arendamist!

Liikuge edasi 6. õppetundi, kus rakendame oma teadmisi suunamise inseneeriast, [luues tekstigeneratsiooni rakendusi](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst).

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.