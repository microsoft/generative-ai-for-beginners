<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:42:20+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "uk"
}
-->

> "Згенерувати код для Python Web API"
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

Повторний запуск запиту дає нам такий результат:

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

Між цими двома результатами лише невелика різниця. Тепер зробимо навпаки — встановимо temperature на 0.9:

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

і друга спроба з temperature 0.9:

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

Як бачите, результати дуже різняться.

> Note, що існує ще багато параметрів, які можна змінювати для варіації результату, наприклад top-k, top-p, repetition penalty, length penalty та diversity penalty, але вони виходять за межі цієї навчальної програми.

## Хороші практики

Існує багато практик, які можна застосувати, щоб отримати бажаний результат. Ви знайдете свій власний стиль, використовуючи prompting дедалі більше.

Окрім технік, які ми розглянули, є кілька хороших практик, які варто враховувати при роботі з LLM.

Ось деякі з них:

- **Вказуйте контекст**. Контекст має значення, чим більше ви зможете уточнити, наприклад домен, тему тощо — тим краще.
- Обмежуйте вихідні дані. Якщо вам потрібна конкретна кількість елементів або певна довжина, обов’язково вкажіть це.
- **Вказуйте і що, і як**. Не забувайте вказувати і що саме ви хочете, і як це має бути зроблено, наприклад: «Створіть Python Web API з маршрутами products і customers, розділіть його на 3 файли».
- **Використовуйте шаблони**. Часто ви захочете доповнити свої запити даними вашої компанії. Для цього використовуйте шаблони. Шаблони можуть містити змінні, які ви замінюєте на реальні дані.
- **Правильно пишіть**. LLM можуть надати правильну відповідь, але якщо ви правильно пишете, відповідь буде кращою.

## Завдання

Ось код на Python, який показує, як створити простий API за допомогою Flask:

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

Використайте AI-помічника, наприклад GitHub Copilot або ChatGPT, і застосуйте техніку «self-refine», щоб покращити код.

## Розв’язок

Спробуйте розв’язати завдання, додавши відповідні запити до коду.

> [!TIP]
> Сформулюйте запит на покращення, бажано обмежити кількість покращень. Також можна попросити покращити код у певному напрямку, наприклад архітектура, продуктивність, безпека тощо.

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## Перевірка знань

Навіщо використовувати chain-of-thought prompting? Наведіть 1 правильну відповідь і 2 неправильні.

1. Щоб навчити LLM розв’язувати проблему.
1. B, Щоб навчити LLM знаходити помилки в коді.
1. C, Щоб дати LLM завдання придумати різні рішення.

Відповідь: 1, тому що chain-of-thought полягає в тому, щоб показати LLM, як розв’язувати проблему, надаючи послідовність кроків і схожі проблеми з їх розв’язаннями.

## 🚀 Виклик

Ви щойно застосували техніку self-refine у завданні. Візьміть будь-яку програму, яку ви створили, і подумайте, які покращення ви хотіли б до неї застосувати. Тепер використайте техніку self-refine, щоб внести запропоновані зміни. Як ви вважаєте, результат став кращим чи гіршим?

## Чудова робота! Продовжуйте навчання

Після завершення цього уроку ознайомтеся з нашою [колекцією Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб продовжити підвищувати свої знання з генеративного ШІ!

Перейдіть до Уроку 6, де ми застосуємо знання з Prompt Engineering, [створюючи додатки для генерації тексту](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.