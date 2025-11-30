<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b2651fb16bcfbc62b8e518751ed90fdb",
  "translation_date": "2025-10-17T22:03:08+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "ro"
}
-->
# Crearea de prompturi avansate

[![Crearea de prompturi avansate](../../../translated_images/05-lesson-banner.522610fd4a2cd82dbed66bb7e6fe104ed6da172e085dbb4d9100b28dc73ed435.ro.png)](https://youtu.be/BAjzkaCdRok?si=NmUIyRf7-cDgbjtt)

Să recapitulăm câteva lucruri învățate în capitolul anterior:

> _Ingineria prompturilor_ este procesul prin care **ghidăm modelul către răspunsuri mai relevante** oferind instrucțiuni sau context mai utile.

Există, de asemenea, două etape în scrierea prompturilor: construirea promptului, prin furnizarea unui context relevant, și _optimizarea_, adică modul de îmbunătățire treptată a promptului.

Până acum, avem o înțelegere de bază despre cum să scriem prompturi, dar trebuie să aprofundăm. În acest capitol, vei trece de la testarea diferitelor prompturi la înțelegerea motivului pentru care un prompt este mai bun decât altul. Vei învăța cum să construiești prompturi urmând câteva tehnici de bază care pot fi aplicate oricărui LLM.

## Introducere

În acest capitol, vom acoperi următoarele subiecte:

- Extinderea cunoștințelor despre ingineria prompturilor prin aplicarea diferitelor tehnici la prompturile tale.
- Configurarea prompturilor pentru a varia rezultatul.

## Obiective de învățare

După finalizarea acestei lecții, vei putea:

- Aplica tehnici de inginerie a prompturilor care îmbunătățesc rezultatul prompturilor tale.
- Realiza prompturi care sunt fie variate, fie deterministe.

## Ingineria prompturilor

Ingineria prompturilor este procesul de creare a prompturilor care vor produce rezultatul dorit. Ingineria prompturilor înseamnă mai mult decât scrierea unui text prompt. Nu este o disciplină inginerească, ci mai degrabă un set de tehnici pe care le poți aplica pentru a obține rezultatul dorit.

### Un exemplu de prompt

Să luăm un prompt de bază, cum ar fi acesta:

> Generează 10 întrebări despre geografie.

În acest prompt, aplici de fapt un set de tehnici diferite de promptare.

Să analizăm acest lucru.

- **Context**, specifici că ar trebui să fie despre "geografie".
- **Limitarea rezultatului**, dorești să nu fie mai mult de 10 întrebări.

### Limitările prompturilor simple

Este posibil să obții sau nu rezultatul dorit. Îți vor fi generate întrebările, dar geografia este un subiect vast și este posibil să nu obții ceea ce dorești din următoarele motive:

- **Subiect vast**, nu știi dacă va fi despre țări, capitale, râuri și așa mai departe.
- **Format**, ce se întâmplă dacă doreai ca întrebările să fie formate într-un anumit mod?

După cum poți vedea, există multe de luat în considerare atunci când creezi prompturi.

Până acum, am văzut un exemplu de prompt simplu, dar AI generativă este capabilă de mult mai mult pentru a ajuta oamenii în diverse roluri și industrii. Să explorăm câteva tehnici de bază în continuare.

### Tehnici de promptare

Mai întâi, trebuie să înțelegem că promptarea este o proprietate _emergentă_ a unui LLM, ceea ce înseamnă că nu este o funcție încorporată în model, ci mai degrabă ceva ce descoperim pe măsură ce utilizăm modelul.

Există câteva tehnici de bază pe care le putem folosi pentru a prompta un LLM. Să le explorăm.

- **Promptare zero-shot**, aceasta este cea mai simplă formă de promptare. Este un singur prompt care solicită un răspuns de la LLM bazat exclusiv pe datele sale de antrenament.
- **Promptare few-shot**, acest tip de promptare ghidează LLM oferindu-i 1 sau mai multe exemple pe care se poate baza pentru a genera răspunsul.
- **Chain-of-thought**, acest tip de promptare îi spune LLM cum să descompună o problemă în pași.
- **Cunoștințe generate**, pentru a îmbunătăți răspunsul unui prompt, poți oferi fapte sau cunoștințe generate suplimentar promptului tău.
- **De la cel mai simplu la cel mai complex**, similar cu chain-of-thought, această tehnică presupune descompunerea unei probleme într-o serie de pași și apoi solicitarea ca acești pași să fie efectuați în ordine.
- **Auto-refinarea**, această tehnică presupune criticarea răspunsului LLM și apoi solicitarea îmbunătățirii acestuia.
- **Promptare maieutică**, aici dorești să te asiguri că răspunsul LLM este corect și îi ceri să explice diverse părți ale răspunsului. Aceasta este o formă de auto-refinare.

### Promptare zero-shot

Acest stil de promptare este foarte simplu, constă într-un singur prompt. Această tehnică este probabil ceea ce folosești pe măsură ce începi să înveți despre LLM-uri. Iată un exemplu:

- Prompt: "Ce este Algebra?"
- Răspuns: "Algebra este o ramură a matematicii care studiază simbolurile matematice și regulile pentru manipularea acestor simboluri."

### Promptare few-shot

Acest stil de promptare ajută modelul oferindu-i câteva exemple împreună cu cererea. Constă într-un singur prompt cu date suplimentare specifice sarcinii. Iată un exemplu:

- Prompt: "Scrie un poem în stilul lui Shakespeare. Iată câteva exemple de sonete shakespeariene:
  Sonetul 18: 'Să te compar cu o zi de vară? Ești mai frumos și mai temperat...'
  Sonetul 116: 'Să nu admit impedimente în căsătoria minților adevărate. Dragostea nu este dragoste care se schimbă când găsește schimbare...'
  Sonetul 132: 'Ochii tăi îi iubesc, și ei, ca și cum mă compătimesc, Știind că inima ta mă chinuie cu dispreț,...'
  Acum, scrie un sonet despre frumusețea lunii."
- Răspuns: "Pe cer, luna strălucește blând, În lumină argintie ce își aruncă grația,..."

Exemplele oferă LLM contextul, formatul sau stilul rezultatului dorit. Ele ajută modelul să înțeleagă sarcina specifică și să genereze răspunsuri mai precise și relevante.

### Chain-of-thought

Chain-of-thought este o tehnică foarte interesantă, deoarece presupune parcurgerea LLM printr-o serie de pași. Ideea este să instruiești LLM astfel încât să înțeleagă cum să facă ceva. Ia în considerare următorul exemplu, cu și fără chain-of-thought:

    - Prompt: "Alice are 5 mere, aruncă 3 mere, dă 2 lui Bob și Bob îi dă unul înapoi, câte mere are Alice?"
    - Răspuns: 5

LLM răspunde cu 5, ceea ce este incorect. Răspunsul corect este 1 măr, având în vedere calculul (5 -3 -2 + 1 = 1).

Cum putem învăța LLM să facă acest lucru corect?

Să încercăm chain-of-thought. Aplicarea chain-of-thought înseamnă:

1. Oferă LLM un exemplu similar.
1. Arată calculul și cum să-l calculeze corect.
1. Furnizează promptul original.

Iată cum:

- Prompt: "Lisa are 7 mere, aruncă 1 măr, dă 4 mere lui Bart și Bart îi dă unul înapoi:
  7 -1 = 6
  6 -4 = 2
  2 +1 = 3  
  Alice are 5 mere, aruncă 3 mere, dă 2 lui Bob și Bob îi dă unul înapoi, câte mere are Alice?"
  Răspuns: 1

Observă cum scriem prompturi substanțial mai lungi cu un alt exemplu, un calcul și apoi promptul original și ajungem la răspunsul corect 1.

După cum poți vedea, chain-of-thought este o tehnică foarte puternică.

### Cunoștințe generate

De multe ori, când dorești să construiești un prompt, vrei să o faci folosind datele propriei companii. Vrei ca o parte a promptului să fie din companie, iar cealaltă parte să fie promptul care te interesează.

Ca exemplu, iată cum poate arăta promptul tău dacă ești în domeniul asigurărilor:

```text
{{company}}: {{company_name}}
{{products}}:
{{products_list}}
Please suggest an insurance given the following budget and requirements:
Budget: {{budget}}
Requirements: {{requirements}}
```

Mai sus, vezi cum promptul este construit folosind un șablon. În șablon există un număr de variabile, notate cu `{{variable}}`, care vor fi înlocuite cu valori reale dintr-un API al companiei.

Iată un exemplu de cum ar putea arăta promptul odată ce variabilele au fost înlocuite cu conținut din compania ta:

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

Rularea acestui prompt printr-un LLM va produce un răspuns ca acesta:

```output
Given the budget and requirements, we suggest the following insurance package from ACME Insurance:
- Car, cheap, 500 USD
- Home, cheap, 600 USD
- Life, cheap, 100 USD
Total cost: $1,200 USD
```

După cum poți vedea, sugerează și asigurarea de viață, ceea ce nu ar trebui. Acest rezultat indică faptul că trebuie să optimizăm promptul schimbându-l pentru a fi mai clar în ceea ce permite. După câteva _încercări și erori_, ajungem la următorul prompt:

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

Observă cum adăugarea _tipului_ și _costului_ și utilizarea cuvântului cheie _restrict_ ajută LLM să înțeleagă ce dorim.

Acum obținem următorul răspuns:

```output
Given the budget and requirements, we suggest the Car, Cheap insurance product which costs 500 USD per month.
```

Scopul acestui exemplu a fost să arate că, deși folosim o tehnică de bază precum _cunoștințe generate_, tot trebuie să optimizăm promptul în majoritatea cazurilor pentru a obține rezultatul dorit.

### De la cel mai simplu la cel mai complex

Ideea cu promptarea de la cel mai simplu la cel mai complex este să descompui o problemă mai mare în subprobleme. În acest fel, ajuți LLM să "cucerească" problema mai mare. Un exemplu bun ar putea fi pentru știința datelor, unde poți cere LLM să împartă o problemă astfel:

> Prompt: Cum să faci știință a datelor în 5 pași?

Cu asistentul AI răspunzând astfel:

1. Colectarea datelor
1. Curățarea datelor
1. Analiza datelor
1. Vizualizarea datelor
1. Prezentarea datelor

### Auto-refinarea, criticarea rezultatelor

Cu AI generativă și LLM-uri, nu poți avea încredere în rezultat. Trebuie să-l verifici. La urma urmei, LLM doar îți prezintă ceea ce este cel mai probabil să spună în continuare, nu ceea ce este corect. Prin urmare, o idee bună este să ceri LLM să se critice singur, ceea ce ne duce la tehnica de auto-refinare.

Cum funcționează este că urmezi următorii pași:

1. Prompt inițial care cere LLM să rezolve o problemă
1. LLM răspunde
1. Critici răspunsul și ceri AI să-l îmbunătățească
1. LLM răspunde din nou, de data aceasta luând în considerare critica și sugerând soluții pe care le-a găsit

Poți repeta acest proces de câte ori dorești.

Iată un exemplu folosind această tehnică:

> Prompt: "Creează un API Web Python cu rute pentru produse și clienți"

Răspuns AI:

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

> Prompt: sugerează 3 îmbunătățiri ale codului de mai sus

Răspuns AI:

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

După cum poți vedea, răspunsul AI de mai sus îmbunătățește primul cod sugerat datorită criticării primului răspuns.

### Promptare maieutică

Promptarea maieutică este o tehnică similară cu auto-refinarea, dar este mai mult despre a cere LLM să se explice. Scopul este de a reduce inconsecvențele în rezultatul LLM pentru a te asigura că ajunge la răspunsul corect. Fluxul de lucru de urmat este:

1. Cere LLM să răspundă la o întrebare
1. Pentru fiecare parte a răspunsului, cere LLM să o explice mai în detaliu.
1. Dacă există inconsecvențe, elimină părțile care sunt inconsistente.

Repetă pașii 2 și 3 până când ai trecut prin toate părțile și ești mulțumit de răspuns.

Iată un exemplu de prompt:

> prompt: Cum pot crea un plan de criză pentru a atenua o pandemie în 5 pași?
> Răspuns LLM:

```text
1. Identify the risks
1. Identify the stakeholders
1. Identify the resources
1. Identify the actions
1. Identify the communication channels
```

A identificat 5 pași, dar putem determina dacă acest lucru este corect? Să cerem LLM să explice fiecare pas:

> prompt: Explică primul pas mai în detaliu, care sunt riscurile în detaliu ale unei pandemii?

```text
The risks are the following:

- Loss of life
- Loss of business
- Loss of reputation
- Loss of customers
- Loss of employees
```

În acest moment, dorim să ne asigurăm că LLM este corect, așa că îi cerem să explice primul risc mai în detaliu și sperăm că este consistent cu răspunsul de mai sus:

> prompt: Într-o pandemie, care este cel mai mare risc și de ce?

```text
The biggest risk is loss of life because it's the most important thing to protect.
```

> Care sunt cele două cele mai mari riscuri într-o pandemie?

```text
The two biggest risks are loss of life and loss of business.
```

În acest moment, LLM este consistent și menționează "viața" și "afacerea" ca fiind cele două riscuri principale. Putem continua la pasul următor și să ne simțim destul de încrezători. Totuși, nu ar trebui să avem încredere oarbă în LLM, ar trebui să verificăm întotdeauna rezultatul.

## Variază rezultatul

LLM-urile sunt prin natura lor nedeterministe, ceea ce înseamnă că vei obține rezultate diferite de fiecare dată când rulezi același prompt. Încearcă următorul prompt, de exemplu:

> "Generează cod pentru un API Web Python"

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

Rularea aceluiași prompt din nou generează un răspuns ușor diferit:

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

> Deci, este rezultatul variat o problemă?

Depinde de ceea ce încerci să faci. Dacă dorești un răspuns specific, atunci este o problemă. Dacă ești ok cu un rezultat variat, cum ar fi "Generează orice 3 întrebări despre geografie", atunci nu este o problemă.

### Utilizarea temperaturii pentru a varia rezultatul

Ok, deci am decis că vrem să limităm rezultatul pentru a fi mai previzibil, adică mai determinist. Cum facem asta?

Temperatura este o valoare între 0 și 1, unde 0 este cel mai determinist și 1 este cel mai variat. Valoarea implicită este 0.7. Să vedem ce se întâmplă cu două rulări ale aceluiași prompt cu temperatura setată la 0.1:

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

Există doar o mică diferență între aceste două rezultate. Să facem opusul de data aceasta, să setăm temperatura la 0.9:

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

și a doua încercare cu valoarea temperaturii setată la 0.9:

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

După cum puteți vedea, rezultatele nu ar putea fi mai variate.

> Rețineți că există mai mulți parametri pe care îi puteți modifica pentru a varia rezultatul, cum ar fi top-k, top-p, penalizarea repetării, penalizarea lungimii și penalizarea diversității, dar aceștia sunt în afara domeniului acestui curriculum.

## Practici bune

Există multe practici pe care le puteți aplica pentru a obține ceea ce doriți. Veți descoperi propriul stil pe măsură ce utilizați mai mult și mai mult tehnica de prompting.

Pe lângă tehnicile pe care le-am acoperit, există câteva practici bune de luat în considerare atunci când formulați cereri pentru un LLM.

Iată câteva practici bune de luat în considerare:

- **Specificați contextul**. Contextul contează, cu cât puteți specifica mai mult, cum ar fi domeniul, subiectul etc., cu atât mai bine.
- Limitați rezultatul. Dacă doriți un număr specific de elemente sau o lungime specifică, specificați acest lucru.
- **Specificați atât ce, cât și cum**. Amintiți-vă să menționați atât ce doriți, cât și cum doriți, de exemplu: "Creați o API Web Python cu rute pentru produse și clienți, împărțiți-o în 3 fișiere".
- **Utilizați șabloane**. Adesea, veți dori să îmbogățiți cererile cu date din compania dvs. Utilizați șabloane pentru a face acest lucru. Șabloanele pot avea variabile pe care le înlocuiți cu date reale.
- **Scrieți corect**. LLM-urile ar putea să vă ofere un răspuns corect, dar dacă scrieți corect, veți obține un răspuns mai bun.

## Temă

Iată un cod în Python care arată cum să construiți o API simplă folosind Flask:

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

Utilizați un asistent AI precum GitHub Copilot sau ChatGPT și aplicați tehnica "self-refine" pentru a îmbunătăți codul.

## Soluție

Vă rugăm să încercați să rezolvați tema adăugând cereri potrivite la cod.

> [!TIP]
> Formulați o cerere pentru a solicita îmbunătățiri, este o idee bună să limitați numărul de îmbunătățiri. De asemenea, puteți solicita îmbunătățiri într-un anumit mod, de exemplu arhitectură, performanță, securitate etc.

[Soluție](../../../05-advanced-prompts/python/aoai-solution.py)

## Verificare cunoștințe

De ce aș folosi prompting-ul de tip chain-of-thought? Arătați-mi 1 răspuns corect și 2 răspunsuri incorecte.

1. Pentru a învăța LLM-ul cum să rezolve o problemă.
1. B, Pentru a învăța LLM-ul să găsească erori în cod.
1. C, Pentru a instrui LLM-ul să vină cu soluții diferite.

A: 1, deoarece chain-of-thought se referă la a arăta LLM-ului cum să rezolve o problemă oferindu-i o serie de pași, și probleme similare și cum au fost rezolvate.

## 🚀 Provocare

Tocmai ați utilizat tehnica self-refine în temă. Luați orice program pe care l-ați construit și gândiți-vă la ce îmbunătățiri ați dori să aplicați. Acum utilizați tehnica self-refine pentru a aplica modificările propuse. Ce părere aveți despre rezultat, mai bun sau mai rău?

## Felicitări! Continuați să învățați

După ce ați finalizat această lecție, consultați [colecția noastră de învățare despre AI generativ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să vă dezvoltați cunoștințele despre AI generativ!

Mergeți la Lecția 6 unde vom aplica cunoștințele noastre despre Prompt Engineering [construind aplicații de generare de text](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.