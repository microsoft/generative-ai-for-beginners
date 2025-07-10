<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:37:22+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "tl"
}
-->

# Paano Gumawa ng Code para sa isang Python Web API

Ang tutorial na ito ay magtuturo sa iyo kung paano gumawa ng isang simpleng Web API gamit ang Python.

## Mga Kinakailangan

Bago tayo magsimula, siguraduhing naka-install ang mga sumusunod:

- Python 3.6 o mas bago
- Flask library

## Pag-install ng Flask

Gamitin ang sumusunod na command para i-install ang Flask:

```bash
pip install Flask
```

## Paggawa ng Simpleng API

Narito ang isang halimbawa ng simpleng API na nagbabalik ng mensahe sa JSON format:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    # Ibalik ang simpleng mensahe bilang JSON
    return jsonify(message="Kamusta, mundo!")

if __name__ == '__main__':
    app.run(debug=True)
```

## Pagsubok ng API

Kapag tumakbo na ang server, bisitahin ang `http://localhost:5000/hello` gamit ang browser o Postman upang makita ang resulta.

## [!IMPORTANT] Tandaan

Siguraduhing hindi naka-enable ang debug mode sa production environment para sa seguridad.
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

Kapag pinaulit natin ang prompt, ito ang lumabas na resulta:

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

May maliit lang na pagkakaiba sa dalawang output na ito. Subukan naman natin ang kabaligtaran, itakda natin ang temperature sa 0.9:

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

at ito naman ang pangalawang pagtatangka gamit ang temperature na 0.9:

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

Makikita mo na sobrang iba-iba talaga ang mga resulta.

> Tandaan, may iba pang mga parameter na pwede mong baguhin para mag-iba ang output, tulad ng top-k, top-p, repetition penalty, length penalty, at diversity penalty pero hindi ito sakop ng kurikulum na ito.

## Magagandang Gawi

Maraming mga gawi ang pwede mong gawin para makuha ang gusto mo. Makikita mo ang sarili mong estilo habang mas ginagamit mo ang prompting.

Bukod sa mga teknik na natalakay natin, may ilang magagandang gawi na dapat isaalang-alang kapag nagpo-prompt sa isang LLM.

Narito ang ilang magagandang gawi na dapat tandaan:

- **Ibigay ang konteksto**. Mahalaga ang konteksto, mas marami kang maibibigay na detalye tulad ng domain, paksa, atbp., mas maganda.
- Limitahan ang output. Kung gusto mo ng tiyak na bilang ng mga item o tiyak na haba, sabihin mo ito.
- **Sabihin kung ano at paano**. Tandaan na banggitin kung ano ang gusto mo at kung paano mo ito gusto, halimbawa "Gumawa ng Python Web API na may mga ruta na products at customers, hatiin ito sa 3 files".
- **Gumamit ng mga template**. Madalas, gusto mong dagdagan ang iyong mga prompt ng data mula sa iyong kumpanya. Gamitin ang mga template para dito. Ang mga template ay maaaring may mga variable na papalitan mo ng totoong data.
- **Mag-spell nang tama**. Maaaring magbigay ang LLM ng tamang sagot kahit mali ang spelling mo, pero mas maganda ang sagot kapag tama ang spelling.

## Takdang-Aralin

Narito ang code sa Python na nagpapakita kung paano gumawa ng simpleng API gamit ang Flask:

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

Gamitin ang AI assistant tulad ng GitHub Copilot o ChatGPT at i-apply ang teknik na "self-refine" para pagandahin ang code.

## Solusyon

Subukan mong lutasin ang takdang-aralin sa pamamagitan ng pagdagdag ng angkop na mga prompt sa code.

> [!TIP]
> Gumawa ng prompt na hihilingin na pagandahin ito, magandang ideya na limitahan kung ilang pagbuti ang gagawin. Pwede mo ring hilingin na pagandahin ito sa isang partikular na aspeto, halimbawa arkitektura, performance, seguridad, atbp.

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## Pagsusulit sa Kaalaman

Bakit gagamitin ko ang chain-of-thought prompting? Ipakita sa akin ang 1 tamang sagot at 2 maling sagot.

1. Para turuan ang LLM kung paano lutasin ang isang problema.  
1. B, Para turuan ang LLM na hanapin ang mga error sa code.  
1. C, Para utusan ang LLM na mag-isip ng iba't ibang solusyon.

A: 1, dahil ang chain-of-thought ay tungkol sa pagpapakita sa LLM kung paano lutasin ang problema sa pamamagitan ng pagbibigay ng sunod-sunod na mga hakbang, at mga katulad na problema at kung paano ito nalutas.

## 🚀 Hamon

Kakatapos mo lang gamitin ang self-refine technique sa takdang-aralin. Pumili ng kahit anong programang ginawa mo at isipin kung anong mga pagbuti ang gusto mong gawin dito. Ngayon, gamitin ang self-refine technique para ipatupad ang mga mungkahing pagbabago. Ano sa tingin mo ang naging resulta, mas maganda o mas hindi maganda?

## Magaling! Ipagpatuloy ang Iyong Pag-aaral

Pagkatapos mong matapos ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para ipagpatuloy ang pag-level up ng iyong kaalaman sa Generative AI!

Pumunta sa Lesson 6 kung saan gagamitin natin ang ating kaalaman sa Prompt Engineering sa pamamagitan ng [paggawa ng mga text generation apps](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.