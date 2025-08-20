<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:22:22+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "en"
}
-->

# Generate code for a Python Web API

This guide will help you create a simple Python Web API using the FastAPI framework.

## Prerequisites

- Python 3.7 or higher installed
- Basic knowledge of Python programming
- Familiarity with RESTful APIs

## Installation

First, install FastAPI and Uvicorn (an ASGI server) using pip:

```bash
pip install fastapi uvicorn
```

## Creating the API

Create a new Python file named `main.py` and add the following code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}
```

This code initializes a FastAPI app and defines a root endpoint that returns a simple JSON message.

## Running the API

Run the API server using Uvicorn with the following command:

```bash
uvicorn main:app --reload
```

The `--reload` flag enables auto-reload on code changes, which is useful during development.

## Testing the API

Open your browser and navigate to `http://127.0.0.1:8000/`. You should see the JSON response:

```json
{"message": "Hello World"}
```

## Interactive API Docs

FastAPI automatically generates interactive API documentation. You can access it at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Next Steps

- Add more endpoints with different HTTP methods (POST, PUT, DELETE)
- Implement request validation using Pydantic models
- Connect your API to a database for persistent storage

[!TIP]  
Explore the FastAPI official documentation for more advanced features and best practices.
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

Running the prompt again gives us this result:

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

There’s only a slight difference between these two outputs. Let’s try the opposite this time and set the temperature to 0.9:

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

and here’s the second attempt with the temperature set to 0.9:

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

As you can see, the results vary significantly.

> Note that there are additional parameters you can adjust to change the output, such as top-k, top-p, repetition penalty, length penalty, and diversity penalty, but these are beyond the scope of this curriculum.

## Good practices

There are many techniques you can use to try to get the results you want. You’ll develop your own style as you gain more experience with prompting.

In addition to the techniques we’ve covered, here are some good practices to keep in mind when prompting an LLM:

- **Specify context.** Context matters—the more you can specify, like domain, topic, etc., the better.
- Limit the output. If you want a specific number of items or a certain length, make sure to specify it.
- **Specify both what and how.** Remember to mention both what you want and how you want it, for example, “Create a Python Web API with routes for products and customers, divided into 3 files.”
- **Use templates.** Often, you’ll want to enrich your prompts with data from your company. Use templates for this. Templates can include variables that you replace with actual data.
- **Spell correctly.** LLMs might still provide a correct response, but spelling correctly will help you get a better response.

## Assignment

Here’s some Python code showing how to build a simple API using Flask:

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

Use an AI assistant like GitHub Copilot or ChatGPT and apply the “self-refine” technique to improve the code.

## Solution

Try to solve the assignment by adding appropriate prompts to the code.

> [!TIP]
> Phrase a prompt asking for improvements, and it’s a good idea to limit how many improvements you want. You can also ask for improvements in a specific area, such as architecture, performance, security, etc.

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## Knowledge check

Why would I use chain-of-thought prompting? Show me 1 correct response and 2 incorrect responses.

1. To teach the LLM how to solve a problem.  
1. B, To teach the LLM to find errors in code.  
1. C, To instruct the LLM to come up with different solutions.

A: 1, because chain-of-thought is about showing the LLM how to solve a problem by providing it with a series of steps, along with similar problems and how they were solved.

## 🚀 Challenge

You just used the self-refine technique in the assignment. Take any program you built and think about what improvements you would want to make. Now use the self-refine technique to apply those changes. What did you think of the result—better or worse?

## Great Work! Continue Your Learning

After completing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to keep advancing your Generative AI skills!

Head over to Lesson 6 where we will apply our knowledge of Prompt Engineering by [building text generation apps](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.