# Creating Advanced prompts

[![Creating Advanced Prompts](../../../translated_images/pcm/05-lesson-banner.522610fd4a2cd82d.webp)](https://youtu.be/BAjzkaCdRok?si=NmUIyRf7-cDgbjtt)

Mek we recall some tins we don learn for di previous chapter:

> Prompt _engineering_ na di process wey we **dey guide di model make e give better better answers** by gimme beta instructions or context.

Two steps dey for writing prompts: to build di prompt by gimme correct context, and _optimization_, how to improve di prompt small small.

For dis stage, we don understand some of di basic tins about how to write prompts, but we go need go deeper. For dis chapter, you go move from to dey try different prompts to sabi why one prompt better pass another. You go learn how to build prompts by some basic techniques wey fit work for any LLM.

## Introduction

For dis chapter, we go talk the following tins:

- Extend your knowledge of prompt engineering by applying different techniques to your prompts.
- Configuring your prompts to vary the output.

## Learning goals

After you finish dis lesson, you go fit:

- Use prompt engineering techniques wey go improve the results of your prompts.
- Perform prompting wey fit be varied or deterministic.

## Prompt engineering

Prompt engineering na di process of creating prompts wey go give the result wey you want. E no be just to write text prompt. Prompt engineering no be engineering discipline, e be set of techniques wey you fit use make you get wetin you want.

### An example of a prompt

Make we look one basic prompt like dis one:

> Generate 10 questions on geography.

For dis prompt, you dey apply different prompt techniques.

Make we break am down.

- **Context**, you talk sey e suppose be about "geography".
- **Limit di output**, you want make dem no pass 10 questions.

### Limitations of simple prompting

You fit no get di result wey you want. You go get your questions, but geography na big topic and e fit no be wetin you expect because:

- **Big topic**, you no sabi if e go be about countries, capitals, rivers and so on.
- **Format**, wetin if you want the questions make dem dey for special format?

You see, e get plenty things you gots consider when you dey create prompts.

So far, we don see one simple prompt example, but generative AI fit do well well to help different people for different roles and industries. Make we check some basic techniques next.

### Techniques for prompting

First, we gots know say prompting na _emergent_ property of LLM, meaning say dis one no be feature wey dey built inside model but na something wey we discover as we dey use di model.

E get some basic techniques we fit use for prompt LLM. Make we talk dem.

- **Zero-shot prompting**, dis be di simplest kind of prompting. Na one prompt wey dey ask LLM answer based on im training data alone.
- **Few-shot prompting**, dis kind prompting dey guide LLM by to give am 1 or more examples wey e fit use generate answer.
- **Chain-of-thought**, dis type of prompting dey tell LLM how to break problem into small steps.
- **Generated knowledge**, to improve prompt response, you fit give generated facts or knowledge alongside your prompt.
- **Least to most**, like chain-of-thought, dis technique dey about to break problem into steps and ask make e perform dem one by one.
- **Self-refine**, dis technique dey make LLM check im own output then improve am.
- **Maieutic prompting**. Wetin you want be to make sure say LLM answer correct so you go ask am to explain different parts of di answer. Dis na form of self-refine.

### Zero-shot prompting

Dis kind prompting easy, na just one prompt be dat. Dis technique na wetin most people dey use as dem dey start to learn about LLMs. Example:

- Prompt: "What is Algebra?"
- Answer: "Algebra na branch of mathematics wey study mathematical symbols and di rules for to handle these symbols."

### Few-shot prompting

Dis kind prompting dey help model by to give am few examples with di request. E get one prompt plus task-specific data. Example:

- Prompt: "Write poem for Shakespeare style. Here be some examples of Shakespearean sonnets:
  Sonnet 18: 'Shall I compare thee to a summer's day? Thou art more lovely and more temperate...'
  Sonnet 116: 'Let me not to the marriage of true minds Admit impediments. Love no be love Wey dey change when e see something new...'
  Sonnet 132: 'Thine eyes I love, and they, as pitying me, Knowing thy heart torment me with disdain,...'
  Now write sonnet about the beauty of the moon."
- Answer: "Upon the sky, the moon doth softly gleam, In silv'ry light wey dey cast im gentle grace,..."

Examples dey give LLM context, format or style wey you want. E dey help model sabi di task well and takeful generate better answers.

### Chain-of-thought

Chain-of-thought na interesting technique because e dey make LLM follow series of steps. Di idea be to teach LLM how to do something. Check di example, with and without chain-of-thought:

    - Prompt: "Alice get 5 apples, she throw 3 apples, she give 2 to Bob and Bob give one back, how many apples Alice get?"
    - Answer: 5

LLM talk 5, but e no correct. Correct answer na 1 apple (5 - 3 - 2 + 1 = 1).

How we go take teach LLM do am correct?

Make we try chain-of-thought. To apply chain-of-thought mean:

1. Give LLM similar example.
1. Show calculation and how to calculate am correct.
1. Give original prompt.

Example:

- Prompt: "Lisa get 7 apples, she throw 1 apple, she give 4 apples to Bart and Bart give one back:
  7 -1 = 6
  6 -4 = 2
  2 +1 = 3  
  Alice get 5 apples, she throw 3 apples, give 2 to Bob and Bob give one back, how many apples Alice get?"
  Answer: 1

You fit see say we write longer prompt with example, calculation then original prompt and we get correct answer 1.

Chain-of-thought na powerful technique.

### Generated knowledge

Many times when you want build prompt, you want use your own company data. You want part of prompt to come from your company and the other part be the actual prompt wey you want.

Example, if you dey insurance business, your prompt fit be like dis:

```text
{{company}}: {{company_name}}
{{products}}:
{{products_list}}
Please suggest an insurance given the following budget and requirements:
Budget: {{budget}}
Requirements: {{requirements}}
```

You see how the prompt dey built using template. For the template, e get variables, with `{{variable}}`, wey go replace with actual values from company API.

Example after variables don replace with your company content:

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

If you run dis prompt through LLM, e go give answer like dis:

```output
Given the budget and requirements, we suggest the following insurance package from ACME Insurance:
- Car, cheap, 500 USD
- Home, cheap, 600 USD
- Life, cheap, 100 USD
Total cost: $1,200 USD
```

As you see, e still suggest Life insurance wey e no suppose. Dis shows say we need optimize the prompt by to dey clearer wetin e fit allow. After some _trial and error_, we come up with dis prompt:

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

You fit see say adding _type_ and _cost_ plus using keyword _restrict_ dey help LLM sabi wetin we want.

Now, we get dis response:

```output
Given the budget and requirements, we suggest the Car, Cheap insurance product which costs 500 USD per month.
```

Point be say even though we dey use basic technique like _generated knowledge_, most times we gots to optimize prompt to get correct result.

### Least-to-most

Di idea for Least-to-most prompting be say to break big problem into small subproblems. Dat way e go help guide LLM how to "conquer" big problem. Example for data science you fit ask LLM to break problem like dis:

> Prompt: How to perform data science in 5 steps?

Your AI assistant go answer:

1. Collect data
1. Clean data
1. Analyze data
1. Plot data
1. Present data

### Self-refine, critique the results

With generative AIs and LLMs, you no fit trust di output. You gots verify am. After all, LLM just dey give wetin e think na wetin e go talk next, no be wetin correct. So, good idea be to ask LLM to critique imself, dat na di self-refine technique.

How e dey work na say you go do:

1. First prompt to ask LLM solve problem
1. LLM answer
1. You critique di answer and ask AI to improve
1. LLM answer again, this time e consider di critique and give better solutions

You fit repeat dis process as many times as you want.

Example with dis technique:

> Prompt: "Create Python Web API with routes products and customers"

AI Answer:

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

> Prompt: suggest 3 improvements of di code above

AI Answer:

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

You fit see say di AI response dey improve di first code based on critique.

### Maieutic prompting

Maieutic prompting similar to self-refine but e more be to ask LLM to explain im self. The goal be to reduce wahala for LLM output so e go get correct answer. Di workflow be:

1. Ask LLM question
1. For each part of answer, ask LLM explain am deeper.
1. If e get wahala, discard inconsistent parts.

Repeat 2 and 3 until you finish all parts and you satisfied.

Example prompt:

> prompt: How I fit create crisis plan to stop pandemic in 5 steps?
> LLM answer:

```text
1. Identify the risks
1. Identify the stakeholders
1. Identify the resources
1. Identify the actions
1. Identify the communication channels
```

E identify 5 steps, but how we fit know if e correct? Make we ask LLM to explain each step:

> prompt: Explain di first step well well, wetin be the risk for pandemic?

```text
The risks are the following:

- Loss of life
- Loss of business
- Loss of reputation
- Loss of customers
- Loss of employees
```

Now, we want sure say LLM correct so we ask am make e explain first risk well and hope e agree with previous answer:

> prompt: For Pandemic, which be biggest risk and why?

```text
The biggest risk is loss of life because it's the most important thing to protect.
```

> What are di two biggest risks in pandemic?

```text
The two biggest risks are loss of life and loss of business.
```

Now, LLM dey consistent and e mention "life" and "business" as top two risks. We fit continue next step and dey confident. But we no go just trust LLM blind, we gots verify the output always.

## Vary your output

LLMs no dey deterministic by nature, meaning say each time you run same prompt, result fit different. Try dis prompt:

> "Generate code for Python Web API"

```python
# Import di necessary modules
import flask
from flask import request, jsonify

# Create one Flask app
app = flask.Flask(__name__)

# Create one route for di API
@app.route('/api', methods=['GET'])
def api():
    # Collect di data from di request
    data = request.args

    # Work on di data
    result = process_data(data)

    # Return di result as JSON
    return jsonify(result)

# Function wey go process di data
def process_data(data):
    # Do sometin wit di data
    result = data + 1

    # Return di result
    return result

# Run di app
if __name__ == '__main__':
    app.run()

```

Run di same prompt again and you go see slight difference:

```python
#import di packages wey dem need
import flask
from flask import request, jsonify

#create di Flask app wey go run
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#create one list of books
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

#create one endpoint for di API
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Books API</h1>
<p>A prototype API for retrieving books.</p>'''

#create one endpoint wey go return all di books
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

#create one endpoint wey go return one book
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    #check if dem give ID as part of di URL
    #if ID dey, put am for one variable
    #if no ID dey, show error
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    #create one empty list for our results
    results = []

    #waka through di data, find results wey match di ID wey dem ask
    #IDs different one-one, but other fields fit get plenty results
    for book in books:
        if book['id'] == id:
            results.append(book)

    #use di jsonify function from Flask to change our list
    #Python dictionaries go JSON format
    return jsonify(results)

app.run()
```

> So, na problem be the varied output?

E depend on wetin you want do. If you need specific answer, e be problem. If you dey ok with varied output like "Generate any 3 questions on geography", then no wahala.

### Using temperature to vary your output

Ok, we don decide say we want limit output so e go be more predictable or deterministic. How we go take do am?

Temperature na value between 0 and 1, where 0 be most deterministic and 1 be most varied. Default na 0.7. Make we see wetin happen if we run same prompt twice with temperature 0.1:

> "Generate code for Python Web API"

```python
#import di libraries wey e need
import flask
from flask import request, jsonify

#create one instance of di Flask class
app = flask.Flask(__name__)

#create one endpoint for di API
@app.route('/api/v1/endpoint', methods=['GET'])
def api_endpoint():
    #collect di request data
    data = request.get_json()

    #process di data
    result = process_data(data)

    #return di result
    return jsonify(result)

#function wey go process di data
def process_data(data):
    #process di data
    result = {'result': 'success'}

    #return di result
    return result

#run di Flask app
if __name__ == '__main__':
    app.run()

```

Run prompt again give dis result:

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

Only small difference dey between outputs. Make we do opposite now, temperature 0.9:

```python
# Import di necessary libraries
import flask
from flask import request, jsonify

# Create one Flask app
app = flask.Flask(__name__)

# Create one route for di API
@app.route('/api', methods=['GET'])
def api_call():
    # Collect di data from di request
    data = request.args

    # Process di data
    result = process_data(data)

    # Return di result
    return jsonify(result)

# Function to process di data
def process_data(data):
    # Do something wit di data
    result = data + 1

    # Return di result
    return result

# Run di app
if __name__ == '__main__':
    app.run()

```

Second try with 0.9 temperature:

```python
import flask
from flask import request, jsonify

# make di Flask app
app = flask.Flask(__name__)
app.config['DEBUG'] = True

# make some test data
books = [
    {'id': 0, 'title': 'A Fire Upon The Deep', 'author': 'Vernor Vinge', 'first_sentence': 'The coldsleep itself was dreamless.', 'year_published': '1992'},
    {'id': 1, 'title': 'The Ones Who Walk Away From Omelas', 'author': 'Ursula K. Le Guin', 'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.', 'published': '1973'},
    {'id': 2, 'title': 'Dhalgren', 'author': 'Samuel R. Delany', 'first_sentence': 'to wound the autumnal city.', 'published': '1975'}
]

# make one endpoint
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to our book API!</h1>'''

@app.route('/api/v1/resources/books

```

You fit see say di results dey very varied.
> Note, say dem get more parameters wey you fit change to vary the output, like top-k, top-p, repetition penalty, length penalty and diversity penalty but these ones no dey inside the scope of this curriculum.

## Good practices

Plenty good practices dey wey you fit apply make you try get wetin you want. You go find your own style as you dey use prompting more and more.

For plus the techniques we don cover, some good practices dey wey you go fit consider when you dey prompt LLM.

Here be some good practices wey you fit consider:

- **Specify context**. Context matter, the more you fit specify like domain, topic, and so on, the better.
- Limit the output. If you want specific number of items or one correct length, specify am.
- **Specify both what and how**. Remember to yarn both wetin you want and how you want am, for example "Create a Python Web API with routes products and customers, divide am into 3 files".
- **Use templates**. Many times, you go want add more info to your prompts from your company. Use templates do am. Templates fit get variables wey you go fit change to actual data.
- **Spell correctly**. LLM fit give you correct answer, but if you spell correctly, you go get better response.

## Assignment

Here be code for Python wey show how to build simple API with Flask:

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

Use AI assistant like GitHub Copilot or ChatGPT and apply the "self-refine" technique to improve the code.

## Solution

Try solve the assignment by adding correct prompts to the code.

> [!TIP]
> Phrase prompt to ask am to improve, e dey better to limit how many improvements. You fit also ask to improve am one kind way, like architecture, performance, security, and so on.

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## Knowledge check

Why you go use chain-of-thought prompting? Show me 1 correct response and 2 wrong responses.

1. To teach the LLM how to solve problem.
1. B, To teach the LLM to find errors inside code.
1. C, To instruct LLM make e come up with different solutions.

A: 1, because chain-of-thought na to show LLM how e go solve problem by giving am series of steps, and similar problems and how dem solve am.

## 🚀 Challenge

You just use the self-refine technique for the assignment. Take any program wey you build and think wetin improvements you for like do for am. Now use the self-refine technique to apply the changes wey you come up with. How you see the result, better or worse?

## Great Work! Continue Your Learning

After you finish this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) make you continue to level up your Generative AI knowledge!

Go Lesson 6 where we go apply our Prompt Engineering knowledge by [building text generation apps](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->