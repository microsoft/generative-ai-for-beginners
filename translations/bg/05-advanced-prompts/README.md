<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:40:02+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "bg"
}
-->

> "Генериране на код за Python Web API"
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

Повторното изпълнение на подканата ни дава следния резултат:

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

Има само малка разлика между тези два изхода. Сега нека направим обратното, нека зададем температурата на 0.9:

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

и вторият опит с температура 0.9:

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

Както виждате, резултатите са много по-разнообразни.

> Note, че има и други параметри, които можете да променяте, за да варирате изхода, като top-k, top-p, repetition penalty, length penalty и diversity penalty, но те са извън обхвата на този курс.

## Добри практики

Има много практики, които можете да приложите, за да получите желаното. Ще откриете свой собствен стил с натрупването на опит в използването на подканите.

Освен техниките, които разгледахме, има и някои добри практики, които да имате предвид при работа с LLM.

Ето някои добри практики, които да обмислите:

- **Посочете контекст**. Контекстът е важен – колкото повече можете да уточните, като домейн, тема и т.н., толкова по-добре.
- Ограничете изхода. Ако искате конкретен брой елементи или определена дължина, уточнете го.
- **Посочете какво и как**. Не забравяйте да споменете както какво искате, така и как искате да бъде направено, например „Създай Python Web API с маршрути products и customers, разделено на 3 файла“.
- **Използвайте шаблони**. Често ще искате да обогатите подканите си с данни от вашата компания. Използвайте шаблони за това. Шаблоните могат да съдържат променливи, които заменяте с реални данни.
- **Пишете правилно**. LLM може да ви даде правилен отговор, но ако пишете правилно, ще получите по-добър отговор.

## Задача

Ето код на Python, показващ как да се създаде просто API с Flask:

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

Използвайте AI асистент като GitHub Copilot или ChatGPT и приложете техниката „self-refine“, за да подобрите кода.

## Решение

Опитайте се да решите задачата, като добавите подходящи подканващи фрази към кода.

> [!TIP]
> Формулирайте подканата така, че да поиска подобрение, добре е да ограничите броя на подобренията. Можете също да поискате подобрение в определена насока, например архитектура, производителност, сигурност и т.н.

[Решение](../../../05-advanced-prompts/python/aoai-solution.py)

## Проверка на знанията

Защо бих използвал chain-of-thought prompting? Покажете ми 1 правилен отговор и 2 грешни.

1. За да науча LLM как да решава проблем.
1. B, За да науча LLM да намира грешки в кода.
1. C, За да инструктирам LLM да предложи различни решения.

Отговор: 1, защото chain-of-thought е за показване на LLM как да решава проблем, като му предоставя серия от стъпки и подобни проблеми и как са били решени.

## 🚀 Предизвикателство

Току-що използвахте техниката self-refine в задачата. Вземете произволна програма, която сте създали, и помислете какви подобрения бихте искали да приложите. Сега използвайте техниката self-refine, за да приложите предложените промени. Какъв беше резултатът – по-добър или по-лош?

## Отлична работа! Продължете да учите

След като завършите този урок, разгледайте нашата [колекция за обучение по Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), за да продължите да развивате знанията си в областта на генеративния AI!

Отидете на Урок 6, където ще приложим знанията си по Prompt Engineering, като [създаваме приложения за генериране на текст](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.