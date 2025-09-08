<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:40:28+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "sr"
}
-->

# Генериши код за Python Web API

Овај водич ће вам показати како да аутоматски генеришете код за Python Web API користећи одговарајуће алате и библиотеке.

## Почетак

Прво, уверите се да имате инсталиран Python и потребне пакете као што су `Flask` или `FastAPI`.

```python
# Пример инсталације FastAPI и Uvicorn
pip install fastapi uvicorn
```

## Креирање основног API-а

Ево једноставног примера како да направите основни API користећи FastAPI:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Здраво, свет!"}
```

## Покретање сервера

Да бисте покренули сервер, користите следећу команду:

```bash
uvicorn main:app --reload
```

Ово ће покренути ваш API на `http://127.0.0.1:8000`.

## Додавање нових руте

Можете додати више руте за различите HTTP методе:

```python
@app.post("/items/")
async def create_item(item: dict):
    return {"item": item}
```

## Закључак

Креирање Python Web API-а је једноставно уз помоћ модерних алата као што су FastAPI и Flask. Ови алати вам омогућавају брз развој и лако одржавање ваших апликација.
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

Поново покретање упита даје нам овај резултат:

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

Постоји само мала разлика између ова два резултата. Хајде да овог пута урадимо супротно, подесимо температуру на 0.9:

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

и други покушај са температуром 0.9:

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

Као што видите, резултати не могу бити разноврснији.

> Note, да постоје још параметара које можете мењати да бисте добили различите резултате, као што су top-k, top-p, repetition penalty, length penalty и diversity penalty, али они нису обухваћени овим курикулумом.

## Добре праксе

Постоји много техника које можете применити да бисте добили оно што желите. Временом ћете развити свој стил како будете све више користили упите.

Поред техника које смо обрадили, постоје и неке добре праксе које треба узети у обзир када радите са LLM-ом.

Ево неколико добрих пракси које треба имати на уму:

- **Наведите контекст**. Контекст је важан, што више можете прецизирати као што су домен, тема и слично, то боље.
- Ограничите излаз. Ако желите одређен број ставки или одређену дужину, наведите то.
- **Наведите и шта и како**. Запамтите да поменете и шта желите и како то желите, на пример „Направи Python Web API са рутама products и customers, подели га у 3 фајла“.
- **Користите шаблоне**. Често ћете желети да обогатите своје упите подацима из ваше компаније. Користите шаблоне за то. Шаблони могу имати променљиве које замените стварним подацима.
- **Правописно пишите**. LLM-ови могу дати исправан одговор, али ако правилно пишете, добићете бољи одговор.

## Задатак

Ево кода у Python-у који показује како направити једноставан API користећи Flask:

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

Користите AI асистента као што су GitHub Copilot или ChatGPT и примените технику „самопобољшања“ да унапредите код.

## Решење

Покушајте да решите задатак тако што ћете додати одговарајуће упите у код.

> [!TIP]
> Формулишите упит да тражите побољшања, добро је ограничити колико побољшања желите. Такође можете тражити побољшања у одређеном смислу, на пример архитектура, перформансе, безбедност и слично.

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## Провера знања

Зашто бих користио chain-of-thought prompting? Прикажи ми 1 тачан и 2 нетачна одговора.

1. Да научим LLM како да реши проблем.
1. B, Да научим LLM да пронађе грешке у коду.
1. C, Да упутим LLM да смисли различита решења.

А: 1, јер chain-of-thought значи показати LLM-у како да реши проблем тако што му се да низ корака, као и слични проблеми и како су решени.

## 🚀 Изазов

Управо сте користили технику самопобољшања у задатку. Узмите било који програм који сте направили и размислите о побољшањима која бисте желели да примените. Сада употребите технику самопобољшања да примените предложене измене. Каквог сте мишљења о резултату, бољи или лошији?

## Одличан посао! Наставите са учењем

Након што завршите ову лекцију, погледајте нашу [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) да наставите да унапређујете своје знање о генеративној вештачкој интелигенцији!

Прелазите на Лекцију 6 где ћемо применити наше знање о Prompt Engineering-у правећи [апликације за генерисање текста](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.