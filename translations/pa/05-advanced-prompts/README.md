<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:30:09+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "pa"
}
-->

> "ਪਾਇਥਨ ਵੈੱਬ API ਲਈ ਕੋਡ ਬਣਾਓ"
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

ਪ੍ਰਾਂਪਟ ਨੂੰ ਦੁਬਾਰਾ ਚਲਾਉਣ ਨਾਲ ਸਾਨੂੰ ਇਹ ਨਤੀਜਾ ਮਿਲਦਾ ਹੈ:

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

ਇਨ੍ਹਾਂ ਦੋ ਨਤੀਜਿਆਂ ਵਿੱਚ ਸਿਰਫ਼ ਇੱਕ ਛੋਟਾ ਜਿਹਾ ਫਰਕ ਹੈ। ਇਸ ਵਾਰੀ ਉਲਟ ਕਰਦੇ ਹਾਂ, ਤਾਪਮਾਨ ਨੂੰ 0.9 ਤੇ ਸੈੱਟ ਕਰਦੇ ਹਾਂ:

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

ਅਤੇ ਦੂਜੀ ਕੋਸ਼ਿਸ਼ 0.9 ਤਾਪਮਾਨ ਮੁੱਲ ਨਾਲ:

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

ਜਿਵੇਂ ਤੁਸੀਂ ਵੇਖ ਸਕਦੇ ਹੋ, ਨਤੀਜੇ ਬਹੁਤ ਵੱਖ-ਵੱਖ ਹਨ।

> [!NOTE] ਯਾਦ ਰੱਖੋ, ਹੋਰ ਵੀ ਕਈ ਪੈਰਾਮੀਟਰ ਹਨ ਜਿਨ੍ਹਾਂ ਨੂੰ ਤੁਸੀਂ ਨਤੀਜੇ ਨੂੰ ਵੱਖਰਾ ਕਰਨ ਲਈ ਬਦਲ ਸਕਦੇ ਹੋ, ਜਿਵੇਂ top-k, top-p, repetition penalty, length penalty ਅਤੇ diversity penalty, ਪਰ ਇਹ ਸਾਰੇ ਇਸ ਕੋਰਸ ਦੇ ਦਾਇਰੇ ਤੋਂ ਬਾਹਰ ਹਨ।

## ਚੰਗੀਆਂ ਅਭਿਆਸਾਂ

ਤੁਸੀਂ ਬਹੁਤ ਸਾਰੇ ਅਭਿਆਸ ਅਪਣਾ ਸਕਦੇ ਹੋ ਤਾਂ ਜੋ ਤੁਸੀਂ ਜੋ ਚਾਹੁੰਦੇ ਹੋ ਉਹ ਪ੍ਰਾਪਤ ਕਰ ਸਕੋ। ਜਿਵੇਂ ਜਿਵੇਂ ਤੁਸੀਂ ਪ੍ਰਾਂਪਟਿੰਗ ਵੱਧ ਵਰਤੋਂਗੇ, ਆਪਣਾ ਅੰਦਾਜ਼ ਬਣ ਜਾਵੇਗਾ।

ਜੋ ਤਕਨੀਕਾਂ ਅਸੀਂ ਕਵਰ ਕੀਤੀਆਂ ਹਨ, ਉਨ੍ਹਾਂ ਦੇ ਨਾਲ ਨਾਲ ਕੁਝ ਚੰਗੀਆਂ ਅਭਿਆਸਾਂ ਵੀ ਹਨ ਜਿਨ੍ਹਾਂ ਨੂੰ LLM ਨੂੰ ਪ੍ਰਾਂਪਟ ਕਰਦੇ ਸਮੇਂ ਧਿਆਨ ਵਿੱਚ ਰੱਖਣਾ ਚਾਹੀਦਾ ਹੈ।

ਇੱਥੇ ਕੁਝ ਚੰਗੀਆਂ ਅਭਿਆਸਾਂ ਹਨ ਜੋ ਧਿਆਨ ਵਿੱਚ ਰੱਖਣ ਯੋਗ ਹਨ:

- **ਸੰਦਰਭ ਦੱਸੋ**। ਸੰਦਰਭ ਮਹੱਤਵਪੂਰਨ ਹੈ, ਜਿੰਨਾ ਜ਼ਿਆਦਾ ਤੁਸੀਂ ਦੱਸ ਸਕਦੇ ਹੋ ਜਿਵੇਂ ਡੋਮੇਨ, ਵਿਸ਼ਾ ਆਦਿ, ਉਨਾ ਹੀ ਵਧੀਆ।
- ਨਤੀਜੇ ਨੂੰ ਸੀਮਿਤ ਕਰੋ। ਜੇ ਤੁਸੀਂ ਕਿਸੇ ਖਾਸ ਗਿਣਤੀ ਜਾਂ ਲੰਬਾਈ ਦੀ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਇਸਨੂੰ ਸਪਸ਼ਟ ਕਰੋ।
- **ਕੀ ਅਤੇ ਕਿਵੇਂ ਦੋਹਾਂ ਦੱਸੋ**। ਯਾਦ ਰੱਖੋ ਕਿ ਤੁਸੀਂ ਜੋ ਚਾਹੁੰਦੇ ਹੋ ਅਤੇ ਕਿਵੇਂ ਚਾਹੁੰਦੇ ਹੋ, ਦੋਹਾਂ ਨੂੰ ਦੱਸੋ, ਉਦਾਹਰਨ ਵਜੋਂ "Python Web API ਬਣਾਓ ਜਿਸ ਵਿੱਚ routes products ਅਤੇ customers ਹਨ, ਇਸਨੂੰ 3 ਫਾਈਲਾਂ ਵਿੱਚ ਵੰਡੋ"।
- **ਟੈਮਪਲੇਟ ਵਰਤੋਂ**। ਅਕਸਰ, ਤੁਸੀਂ ਆਪਣੇ ਕੰਪਨੀ ਦੇ ਡੇਟਾ ਨਾਲ ਪ੍ਰਾਂਪਟ ਨੂੰ ਸੰਵਾਰਨਾ ਚਾਹੁੰਦੇ ਹੋ। ਇਸ ਲਈ ਟੈਮਪਲੇਟ ਵਰਤੋਂ। ਟੈਮਪਲੇਟ ਵਿੱਚ ਵੈਰੀਏਬਲ ਹੋ ਸਕਦੇ ਹਨ ਜਿਨ੍ਹਾਂ ਨੂੰ ਤੁਸੀਂ ਅਸਲੀ ਡੇਟਾ ਨਾਲ ਬਦਲ ਸਕਦੇ ਹੋ।
- **ਸਹੀ ਸਪੈਲਿੰਗ ਕਰੋ**। LLMs ਤੁਹਾਨੂੰ ਸਹੀ ਜਵਾਬ ਦੇ ਸਕਦੇ ਹਨ, ਪਰ ਜੇ ਤੁਸੀਂ ਸਹੀ ਸਪੈਲਿੰਗ ਕਰੋਗੇ ਤਾਂ ਜਵਾਬ ਹੋਰ ਵੀ ਵਧੀਆ ਮਿਲੇਗਾ।

## ਅਸਾਈਨਮੈਂਟ

ਇੱਥੇ Python ਵਿੱਚ ਕੋਡ ਦਿੱਤਾ ਗਿਆ ਹੈ ਜੋ Flask ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਸਧਾਰਣ API ਬਣਾਉਂਦਾ ਹੈ:

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

GitHub Copilot ਜਾਂ ChatGPT ਵਰਗੇ AI ਸਹਾਇਕ ਦੀ ਵਰਤੋਂ ਕਰੋ ਅਤੇ "self-refine" ਤਕਨੀਕ ਲਾਗੂ ਕਰਕੇ ਕੋਡ ਨੂੰ ਸੁਧਾਰੋ।

## ਹੱਲ

ਕਿਰਪਾ ਕਰਕੇ ਅਸਾਈਨਮੈਂਟ ਨੂੰ ਹੱਲ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ ਅਤੇ ਕੋਡ ਵਿੱਚ ਉਚਿਤ ਪ੍ਰਾਂਪਟ ਸ਼ਾਮਲ ਕਰੋ।

> [!TIP]
> ਸੁਧਾਰ ਕਰਨ ਲਈ ਪ੍ਰਾਂਪਟ ਬਣਾਓ, ਇਹ ਚੰਗੀ ਗੱਲ ਹੈ ਕਿ ਤੁਸੀਂ ਸੁਧਾਰਾਂ ਦੀ ਗਿਣਤੀ ਸੀਮਿਤ ਕਰੋ। ਤੁਸੀਂ ਕਿਸੇ ਖਾਸ ਤਰੀਕੇ ਨਾਲ ਸੁਧਾਰ ਕਰਨ ਲਈ ਵੀ ਕਹਿ ਸਕਦੇ ਹੋ, ਜਿਵੇਂ ਆਰਕੀਟੈਕਚਰ, ਪ੍ਰਦਰਸ਼ਨ, ਸੁਰੱਖਿਆ ਆਦਿ।

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## ਗਿਆਨ ਜਾਂਚ

ਮੈਂ chain-of-thought prompting ਕਿਉਂ ਵਰਤਾਂ? ਮੈਨੂੰ 1 ਸਹੀ ਜਵਾਬ ਅਤੇ 2 ਗਲਤ ਜਵਾਬ ਦਿਖਾਓ।

1. LLM ਨੂੰ ਸਮੱਸਿਆ ਹੱਲ ਕਰਨਾ ਸਿਖਾਉਣ ਲਈ।
1. B, LLM ਨੂੰ ਕੋਡ ਵਿੱਚ ਗਲਤੀਆਂ ਲੱਭਣ ਲਈ ਸਿਖਾਉਣ ਲਈ।
1. C, LLM ਨੂੰ ਵੱਖ-ਵੱਖ ਹੱਲ ਲੱਭਣ ਲਈ ਦਿਸ਼ਾ ਦੇਣ ਲਈ।

ਜਵਾਬ: 1, ਕਿਉਂਕਿ chain-of-thought LLM ਨੂੰ ਸਮੱਸਿਆ ਹੱਲ ਕਰਨ ਲਈ ਕਦਮ-ਦਰ-ਕਦਮ ਦਿਖਾਉਂਦਾ ਹੈ, ਅਤੇ ਸਮਾਨ ਸਮੱਸਿਆਵਾਂ ਅਤੇ ਉਹਨਾਂ ਦੇ ਹੱਲ ਵੀ ਦਿਖਾਉਂਦਾ ਹੈ।

## 🚀 ਚੈਲੈਂਜ

ਤੁਸੀਂ ਅਸਾਈਨਮੈਂਟ ਵਿੱਚ self-refine ਤਕਨੀਕ ਵਰਤੀ ਹੈ। ਕੋਈ ਵੀ ਪ੍ਰੋਗਰਾਮ ਜੋ ਤੁਸੀਂ ਬਣਾਇਆ ਹੈ, ਉਸ ਵਿੱਚ ਤੁਸੀਂ ਕਿਹੜੇ ਸੁਧਾਰ ਲਿਆਉਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਸੋਚੋ। ਹੁਣ self-refine ਤਕਨੀਕ ਵਰਤ ਕੇ ਉਹ ਸੁਧਾਰ ਲਾਗੂ ਕਰੋ। ਤੁਹਾਡੇ ਖਿਆਲ ਵਿੱਚ ਨਤੀਜਾ ਕਿਵੇਂ ਰਿਹਾ, ਵਧੀਆ ਜਾਂ ਖਰਾਬ?

## ਸ਼ਾਬਾਸ਼! ਆਪਣੀ ਸਿੱਖਿਆ ਜਾਰੀ ਰੱਖੋ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੇ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਵੇਖੋ ਤਾਂ ਜੋ ਤੁਸੀਂ ਆਪਣਾ Generative AI ਗਿਆਨ ਹੋਰ ਵਧਾ ਸਕੋ!

ਹੁਣ ਲੈਸਨ 6 ਵੱਲ ਜਾਓ ਜਿੱਥੇ ਅਸੀਂ Prompt Engineering ਦਾ ਗਿਆਨ ਲਾਗੂ ਕਰਦੇ ਹੋਏ [ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪਸ ਬਣਾਵਾਂਗੇ](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।