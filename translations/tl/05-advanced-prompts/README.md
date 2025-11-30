<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b2651fb16bcfbc62b8e518751ed90fdb",
  "translation_date": "2025-10-18T01:09:12+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "tl"
}
-->
# Paglikha ng Advanced na Prompt

[![Paglikha ng Advanced na Prompt](../../../translated_images/05-lesson-banner.522610fd4a2cd82dbed66bb7e6fe104ed6da172e085dbb4d9100b28dc73ed435.tl.png)](https://youtu.be/BAjzkaCdRok?si=NmUIyRf7-cDgbjtt)

Balikan natin ang ilang natutunan mula sa nakaraang kabanata:

> Ang _engineering_ ng prompt ay ang proseso kung saan **ginagabayan natin ang modelo patungo sa mas nauugnay na mga sagot** sa pamamagitan ng pagbibigay ng mas kapaki-pakinabang na mga tagubilin o konteksto.

May dalawang hakbang din sa pagsusulat ng mga prompt: ang pagbuo ng prompt, sa pamamagitan ng pagbibigay ng kaugnay na konteksto, at _optimization_, kung paano unti-unting mapapabuti ang prompt.

Sa puntong ito, mayroon na tayong pangunahing kaalaman kung paano magsulat ng mga prompt, ngunit kailangan nating mas palalimin pa. Sa kabanatang ito, mula sa pagsubok ng iba't ibang prompt, mauunawaan mo kung bakit mas mahusay ang isang prompt kaysa sa iba. Matututo kang bumuo ng mga prompt gamit ang ilang pangunahing teknik na maaaring gamitin sa anumang LLM.

## Panimula

Sa kabanatang ito, tatalakayin natin ang mga sumusunod na paksa:

- Palawakin ang iyong kaalaman sa prompt engineering sa pamamagitan ng paggamit ng iba't ibang teknik sa iyong mga prompt.
- I-configure ang iyong mga prompt upang mag-iba ang output.

## Mga Layunin sa Pag-aaral

Pagkatapos makumpleto ang araling ito, magagawa mong:

- Gamitin ang mga teknik sa prompt engineering na nagpapabuti sa resulta ng iyong mga prompt.
- Magsagawa ng prompting na maaaring mag-iba o deterministiko.

## Prompt Engineering

Ang prompt engineering ay ang proseso ng paglikha ng mga prompt na magbibigay ng ninanais na resulta. Hindi lamang ito tungkol sa simpleng pagsusulat ng text prompt. Ang prompt engineering ay hindi isang disiplina sa engineering, ito ay isang hanay ng mga teknik na maaari mong gamitin upang makuha ang ninanais na resulta.

### Halimbawa ng isang Prompt

Tingnan natin ang isang simpleng prompt tulad nito:

> Gumawa ng 10 tanong tungkol sa heograpiya.

Sa prompt na ito, aktwal kang gumagamit ng iba't ibang teknik sa prompt.

Suriin natin ito.

- **Konteksto**, tinukoy mo na ito ay tungkol sa "heograpiya".
- **Paglilimita sa output**, gusto mo ng hindi hihigit sa 10 tanong.

### Mga Limitasyon ng Simpleng Prompting

Maaaring makuha mo o hindi ang ninanais na resulta. Maaaring magawa ang mga tanong, ngunit ang heograpiya ay isang malawak na paksa at maaaring hindi mo makuha ang gusto mo dahil sa mga sumusunod na dahilan:

- **Malawak na paksa**, hindi mo alam kung ito ay tungkol sa mga bansa, kabisera, ilog, at iba pa.
- **Format**, paano kung gusto mong ang mga tanong ay naka-format sa isang tiyak na paraan?

Tulad ng nakikita mo, maraming dapat isaalang-alang sa paglikha ng mga prompt.

Sa ngayon, nakita natin ang isang simpleng halimbawa ng prompt, ngunit ang generative AI ay may kakayahang gumawa ng mas marami upang makatulong sa iba't ibang tungkulin at industriya. Tuklasin natin ang ilang pangunahing teknik sa susunod.

### Mga Teknik sa Prompting

Una, kailangan nating maunawaan na ang prompting ay isang _emergent_ na katangian ng isang LLM, ibig sabihin, hindi ito isang tampok na built-in sa modelo kundi isang bagay na natutuklasan natin habang ginagamit ang modelo.

May ilang pangunahing teknik na maaari nating gamitin sa pag-prompt sa isang LLM. Tuklasin natin ang mga ito.

- **Zero-shot prompting**, ito ang pinaka-basic na uri ng prompting. Isang simpleng prompt na humihiling ng sagot mula sa LLM batay lamang sa training data nito.
- **Few-shot prompting**, ang ganitong uri ng prompting ay ginagabayan ang LLM sa pamamagitan ng pagbibigay ng 1 o higit pang mga halimbawa na maaari nitong gamitin upang makabuo ng sagot.
- **Chain-of-thought**, ang ganitong uri ng prompting ay nagtuturo sa LLM kung paano hatiin ang isang problema sa mga hakbang.
- **Generated knowledge**, upang mapabuti ang sagot ng isang prompt, maaari kang magbigay ng mga nabuong impormasyon o kaalaman bilang karagdagan sa iyong prompt.
- **Least to most**, tulad ng chain-of-thought, ang teknik na ito ay tungkol sa paghahati ng isang problema sa serye ng mga hakbang at pagkatapos ay hilingin na isagawa ang mga hakbang na ito nang sunod-sunod.
- **Self-refine**, ang teknik na ito ay tungkol sa pag-critique sa output ng LLM at pagkatapos ay hilingin dito na mag-improve.
- **Maieutic prompting**, ang layunin dito ay tiyakin na tama ang sagot ng LLM at hilingin dito na ipaliwanag ang iba't ibang bahagi ng sagot. Ito ay isang uri ng self-refine.

### Zero-shot Prompting

Ang istilo ng prompting na ito ay napakasimple, binubuo ito ng isang prompt lamang. Ang teknik na ito ay marahil ang ginagamit mo habang nagsisimula kang matuto tungkol sa LLM. Narito ang isang halimbawa:

- Prompt: "Ano ang Algebra?"
- Sagot: "Ang Algebra ay isang sangay ng matematika na nag-aaral ng mga simbolo ng matematika at ang mga patakaran para sa pagmamanipula ng mga simbolong ito."

### Few-shot Prompting

Ang istilo ng prompting na ito ay tumutulong sa modelo sa pamamagitan ng pagbibigay ng ilang mga halimbawa kasama ang kahilingan. Binubuo ito ng isang prompt na may karagdagang task-specific na data. Narito ang isang halimbawa:

- Prompt: "Sumulat ng tula sa estilo ni Shakespeare. Narito ang ilang halimbawa ng mga soneto ni Shakespeare:
  Soneto 18: 'Ihahambing ba kita sa isang araw ng tag-init? Mas maganda ka at mas mahinahon...'
  Soneto 116: 'Huwag nating pigilan ang pagsasama ng tunay na isipan. Ang pag-ibig ay hindi pag-ibig na nagbabago kapag may pagbabago...'
  Soneto 132: 'Ang iyong mga mata ay mahal ko, at sila, na parang naaawa sa akin, Alam ang iyong puso na pinahihirapan ako ng paghamak,...'
  Ngayon, sumulat ng soneto tungkol sa kagandahan ng buwan."
- Sagot: "Sa kalangitan, ang buwan ay banayad na kumikislap, Sa pilak na liwanag na nagdadala ng kanyang banayad na biyaya,..."

Ang mga halimbawa ay nagbibigay sa LLM ng konteksto, format, o estilo ng ninanais na output. Tinutulungan nila ang modelo na maunawaan ang tiyak na gawain at makabuo ng mas tumpak at nauugnay na mga sagot.

### Chain-of-thought

Ang Chain-of-thought ay isang napaka-interesanteng teknik dahil ito ay tungkol sa pagdadala sa LLM sa pamamagitan ng serye ng mga hakbang. Ang ideya ay turuan ang LLM sa paraang nauunawaan nito kung paano gawin ang isang bagay. Isaalang-alang ang sumusunod na halimbawa, na may at walang chain-of-thought:

    - Prompt: "Si Alice ay may 5 mansanas, itinapon ang 3 mansanas, ibinigay ang 2 kay Bob at si Bob ay ibinalik ang isa, ilan ang mansanas ni Alice?"
    - Sagot: 5

Ang sagot ng LLM ay 5, na mali. Ang tamang sagot ay 1 mansanas, batay sa kalkulasyon (5 -3 -2 + 1 = 1).

Paano natin matuturuan ang LLM na gawin ito nang tama?

Subukan natin ang chain-of-thought. Ang paglalapat ng chain-of-thought ay nangangahulugan ng:

1. Magbigay ng katulad na halimbawa sa LLM.
1. Ipakita ang kalkulasyon, at kung paano ito kalkulahin nang tama.
1. Ibigay ang orihinal na prompt.

Narito kung paano:

- Prompt: "Si Lisa ay may 7 mansanas, itinapon ang 1 mansanas, ibinigay ang 4 mansanas kay Bart at si Bart ay ibinalik ang isa:
  7 -1 = 6
  6 -4 = 2
  2 +1 = 3  
  Si Alice ay may 5 mansanas, itinapon ang 3 mansanas, ibinigay ang 2 kay Bob at si Bob ay ibinalik ang isa, ilan ang mansanas ni Alice?"
  Sagot: 1

Pansinin kung paano tayo nagsusulat ng mas mahahabang prompt na may isa pang halimbawa, isang kalkulasyon, at pagkatapos ang orihinal na prompt, at nakarating tayo sa tamang sagot na 1.

Tulad ng nakikita mo, ang chain-of-thought ay isang napakalakas na teknik.

### Generated Knowledge

Maraming beses kapag gusto mong bumuo ng isang prompt, gusto mong gawin ito gamit ang data ng iyong sariling kumpanya. Gusto mong ang bahagi ng prompt ay mula sa kumpanya at ang isa pang bahagi ay ang aktwal na prompt na interesado ka.

Halimbawa, ganito ang maaaring hitsura ng iyong prompt kung ikaw ay nasa negosyo ng insurance:

```text
{{company}}: {{company_name}}
{{products}}:
{{products_list}}
Please suggest an insurance given the following budget and requirements:
Budget: {{budget}}
Requirements: {{requirements}}
```

Sa itaas, makikita mo kung paano binuo ang prompt gamit ang isang template. Sa template, mayroong ilang mga variable, na tinutukoy ng `{{variable}}`, na papalitan ng aktwal na mga halaga mula sa API ng kumpanya.

Narito ang isang halimbawa kung paano maaaring magmukha ang prompt kapag ang mga variable ay napalitan ng nilalaman mula sa iyong kumpanya:

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

Ang pagpapatakbo ng prompt na ito sa isang LLM ay magbibigay ng sagot tulad nito:

```output
Given the budget and requirements, we suggest the following insurance package from ACME Insurance:
- Car, cheap, 500 USD
- Home, cheap, 600 USD
- Life, cheap, 100 USD
Total cost: $1,200 USD
```

Tulad ng nakikita mo, nagmumungkahi din ito ng Life insurance, na hindi dapat. Ang resulta na ito ay indikasyon na kailangan nating i-optimize ang prompt sa pamamagitan ng pagbabago nito upang maging mas malinaw kung ano ang maaaring pahintulutan. Pagkatapos ng ilang _trial and error_, nakarating tayo sa sumusunod na prompt:

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

Pansinin kung paano ang pagdaragdag ng _type_ at _cost_ at paggamit din ng keyword na _restrict_ ay nakatulong sa LLM na maunawaan ang gusto natin.

Ngayon, nakukuha natin ang sumusunod na sagot:

```output
Given the budget and requirements, we suggest the Car, Cheap insurance product which costs 500 USD per month.
```

Ang punto ng halimbawang ito ay ipakita na kahit na gumagamit tayo ng isang pangunahing teknik tulad ng _generated knowledge_, kailangan pa rin nating i-optimize ang prompt sa karamihan ng mga kaso upang makuha ang ninanais na resulta.

### Least-to-most

Ang ideya ng Least-to-most prompting ay hatiin ang mas malaking problema sa mga subproblema. Sa ganitong paraan, tinutulungan mong gabayan ang LLM kung paano "malalampasan" ang mas malaking problema. Isang magandang halimbawa ay maaaring para sa data science kung saan maaari mong hilingin sa LLM na hatiin ang isang problema tulad nito:

> Prompt: Paano magsagawa ng data science sa 5 hakbang?

Ang sagot ng iyong AI assistant:

1. Kolektahin ang data
1. Linisin ang data
1. Suriin ang data
1. I-plot ang data
1. I-presenta ang data

### Self-refine, Critique ang mga Resulta

Sa generative AIs at LLMs, hindi mo maaaring pagkatiwalaan ang output. Kailangan mong i-verify ito. Pagkatapos ng lahat, ang LLM ay nagpe-presenta lamang ng kung ano ang susunod na pinaka-malamang na sasabihin, hindi kung ano ang tama. Kaya, isang magandang ideya ay hilingin sa LLM na i-critique ang sarili nito, na nagdadala sa atin sa teknik na self-refine.

Paano ito gumagana ay sundin mo ang mga sumusunod na hakbang:

1. Paunang prompt na humihiling sa LLM na lutasin ang isang problema
1. Sumagot ang LLM
1. I-critique mo ang sagot at hilingin sa AI na mag-improve
1. Sumagot ulit ang LLM, sa pagkakataong ito isinasaalang-alang ang critique at nagmumungkahi ng mga solusyon na naisip nito

Maaari mong ulitin ang prosesong ito nang maraming beses hangga't gusto mo.

Narito ang isang halimbawa gamit ang teknik na ito:

> Prompt: "Gumawa ng Python Web API na may mga ruta para sa mga produkto at mga customer"

Sagot ng AI:

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

> Prompt: Magmungkahi ng 3 pagpapabuti sa code sa itaas

Sagot ng AI:

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

Tulad ng nakikita mo, ang sagot ng AI sa itaas ay nagpapabuti sa unang iminungkahing code salamat sa pag-critique sa unang sagot.

### Maieutic Prompting

Ang Maieutic prompting ay isang teknik na katulad ng self-refine ngunit ito ay higit pa sa pagtatanong sa LLM na ipaliwanag ang sarili nito. Ang layunin ay bawasan ang mga inconsistency sa output ng LLM upang matiyak na nakarating ito sa tamang sagot. Ang workflow na dapat sundin ay:

1. Hilingin sa LLM na sagutin ang isang tanong
1. Para sa bawat bahagi ng sagot, hilingin sa LLM na ipaliwanag ito nang mas detalyado.
1. Kung may mga inconsistency, tanggalin ang mga bahagi na hindi tugma.

Ulitin ang 2 at 3 hanggang sa ma-review mo ang lahat ng bahagi at ikaw ay nasisiyahan sa sagot.

Narito ang isang halimbawa ng prompt:

> Prompt: Paano ako makakagawa ng crisis plan upang mabawasan ang epekto ng pandemya sa 5 hakbang?
> Sagot ng LLM:

```text
1. Identify the risks
1. Identify the stakeholders
1. Identify the resources
1. Identify the actions
1. Identify the communication channels
```

Nakilala nito ang 5 hakbang, ngunit maaari ba nating matukoy kung tama ito? Hilingin natin sa LLM na ipaliwanag ang bawat hakbang:

> Prompt: Ipaliwanag ang unang hakbang nang mas detalyado, ano ang mga panganib nang detalyado sa isang pandemya?

```text
The risks are the following:

- Loss of life
- Loss of business
- Loss of reputation
- Loss of customers
- Loss of employees
```

Sa puntong ito, gusto nating tiyakin na tama ang LLM kaya hilingin natin dito na ipaliwanag ang unang panganib nang mas detalyado at umaasa tayong ito ay tugma sa sagot sa itaas:

> Prompt: Sa isang pandemya, ano ang pinakamalaking panganib at bakit?

```text
The biggest risk is loss of life because it's the most important thing to protect.
```

> Ano ang dalawang pinakamalaking panganib sa isang pandemya?

```text
The two biggest risks are loss of life and loss of business.
```

Sa puntong ito, ang LLM ay consistent at binanggit ang "buhay" at "negosyo" bilang dalawang pinakamalaking panganib. Maaari na tayong magpatuloy sa susunod na hakbang at maging medyo kumpiyansa. Gayunpaman, hindi natin dapat basta-basta pagkatiwalaan ang LLM, dapat palaging i-verify ang output.

## Pag-iba ng Iyong Output

Ang mga LLM ay likas na hindi deterministiko, ibig sabihin, makakakuha ka ng iba't ibang resulta sa tuwing tatakbo ang parehong prompt. Subukan ang sumusunod na prompt halimbawa:

> "Gumawa ng code para sa isang Python Web API"

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

Ang pagpapatakbo ng parehong prompt muli ay nagbubunga ng bahagyang naiibang sagot:

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

> Kaya ba ang varied output ay problema?

Depende sa kung ano ang sinusubukan mong gawin. Kung gusto mo ng tiyak na sagot, ito ay problema. Kung ok ka sa varied output tulad ng "Gumawa ng anumang 3 tanong tungkol sa heograpiya", hindi ito problema.

### Paggamit ng Temperature para Iba-iba ang Output

Ok, kaya napagpasyahan natin na gusto nating limitahan ang output upang maging mas predictable, ibig sabihin mas deterministiko. Paano natin ito gagawin?

Ang temperature ay isang halaga sa pagitan ng 0 at 1, kung saan ang 0 ang pinaka-deterministiko at ang 1 ang pinaka-varied. Ang default na halaga ay 0.7. Tingnan natin kung ano ang mangyayari sa dalawang run ng parehong prompt na may temperature na nakatakda sa 0.1:

> "Gumawa ng code para sa isang Python Web API"

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

Ang pagpapatakbo ng prompt muli ay nagbibigay sa atin ng ganitong resulta:

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

Mayroon lamang maliit na pagkakaiba sa pagitan ng dalawang output na ito. Subukan natin ang kabaligtaran sa pagkakataong ito, itakda natin ang temperature sa 0.9:

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

at ang pangalawang pagtatangka sa 0.9 bilang halaga ng temperature:

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

Tulad ng nakikita mo, napaka-iba-iba ng mga resulta.

> Tandaan, may iba pang mga parameter na maaari mong baguhin upang maiba ang output, tulad ng top-k, top-p, repetition penalty, length penalty, at diversity penalty, ngunit ang mga ito ay hindi saklaw ng kurikulum na ito.

## Magandang Praktika

Maraming mga praktika ang maaari mong gamitin upang makuha ang nais mo. Matutuklasan mo ang iyong sariling estilo habang mas ginagamit mo ang prompting.

Bukod sa mga teknik na natalakay natin, may ilang magagandang praktika na dapat isaalang-alang kapag nagpo-prompt sa isang LLM.

Narito ang ilang magagandang praktika na dapat isaalang-alang:

- **Tukuyin ang konteksto**. Mahalaga ang konteksto, mas marami kang maibibigay na detalye tulad ng domain, paksa, atbp., mas maganda ang resulta.
- Limitahan ang output. Kung nais mo ng tiyak na bilang ng mga item o tiyak na haba, tukuyin ito.
- **Tukuyin ang ano at paano**. Tandaan na banggitin ang parehong kung ano ang gusto mo at kung paano mo ito nais, halimbawa "Gumawa ng Python Web API na may mga ruta para sa products at customers, hatiin ito sa 3 file".
- **Gumamit ng mga template**. Madalas, nais mong pagyamanin ang iyong mga prompt gamit ang data mula sa iyong kumpanya. Gumamit ng mga template para dito. Ang mga template ay maaaring may mga variable na papalitan mo ng aktwal na data.
- **Mag-spell nang tama**. Maaaring magbigay ang LLM ng tamang sagot, ngunit kung tama ang spelling mo, mas maganda ang sagot na makukuha mo.

## Takdang-Aralin

Narito ang code sa Python na nagpapakita kung paano bumuo ng simpleng API gamit ang Flask:

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

Gumamit ng AI assistant tulad ng GitHub Copilot o ChatGPT at gamitin ang "self-refine" na teknik upang mapabuti ang code.

## Solusyon

Subukang lutasin ang takdang-aralin sa pamamagitan ng pagdaragdag ng angkop na mga prompt sa code.

> [!TIP]
> Bumuo ng prompt upang hilingin na mapabuti ito, magandang ideya na limitahan kung gaano karaming mga pagpapabuti ang gagawin. Maaari mo ring hilingin na mapabuti ito sa isang tiyak na paraan, halimbawa sa arkitektura, performance, seguridad, atbp.

[Solusyon](../../../05-advanced-prompts/python/aoai-solution.py)

## Pagsusuri ng Kaalaman

Bakit ko gagamitin ang chain-of-thought prompting? Ipakita ang 1 tamang sagot at 2 maling sagot.

1. Upang turuan ang LLM kung paano lutasin ang isang problema.
1. B, Upang turuan ang LLM na maghanap ng mga error sa code.
1. C, Upang utusan ang LLM na magbigay ng iba't ibang solusyon.

A: 1, dahil ang chain-of-thought ay tungkol sa pagpapakita sa LLM kung paano lutasin ang isang problema sa pamamagitan ng pagbibigay ng serye ng mga hakbang, at mga katulad na problema at kung paano ito nalutas.

## 🚀 Hamon

Ginamit mo lang ang self-refine na teknik sa takdang-aralin. Kumuha ng anumang programang ginawa mo at isaalang-alang kung anong mga pagpapabuti ang nais mong ilapat dito. Ngayon gamitin ang self-refine na teknik upang ilapat ang mga iminungkahing pagbabago. Ano ang palagay mo sa resulta, mas maganda o mas pangit?

## Mahusay na Trabaho! Ipagpatuloy ang Iyong Pag-aaral

Matapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang patuloy na paunlarin ang iyong kaalaman sa Generative AI!

Pumunta sa Lesson 6 kung saan ilalapat natin ang ating kaalaman sa Prompt Engineering sa pamamagitan ng [pagbuo ng mga text generation apps](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.