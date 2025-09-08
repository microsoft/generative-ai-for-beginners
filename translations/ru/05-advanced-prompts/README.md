<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:24:06+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "ru"
}
-->

> «Сгенерировать код для Python Web API»
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

Повторный запуск запроса даёт следующий результат:

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

Между этими двумя результатами лишь небольшая разница. Теперь сделаем наоборот — установим температуру на 0.9:

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

и второй запуск с температурой 0.9:

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

Как видите, результаты получились максимально разнообразными.

> Обратите внимание, что есть и другие параметры, которые можно менять для разнообразия вывода, такие как top-k, top-p, штраф за повторения, штраф за длину и штраф за разнообразие, но они выходят за рамки этой программы обучения.

## Хорошие практики

Существует множество приёмов, которые помогут получить желаемый результат. Со временем, по мере практики с запросами, вы найдёте свой собственный стиль.

Кроме рассмотренных техник, есть несколько хороших практик, которые стоит учитывать при работе с LLM.

Вот некоторые из них:

- **Указывайте контекст**. Контекст важен — чем больше вы уточните, например, домен, тему и т.д., тем лучше.
- Ограничивайте вывод. Если вам нужно определённое количество элементов или конкретная длина, обязательно укажите это.
- **Указывайте и что, и как**. Не забывайте говорить и что вы хотите, и как именно, например: «Создай Python Web API с маршрутами products и customers, раздели на 3 файла».
- **Используйте шаблоны**. Часто хочется обогатить запрос данными вашей компании. Для этого применяйте шаблоны. В шаблонах могут быть переменные, которые вы заменяете на реальные данные.
- **Пишите без ошибок**. LLM может дать правильный ответ, но если вы пишете грамотно, ответ будет лучше.

## Задание

Вот пример кода на Python, показывающий, как создать простой API с помощью Flask:

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

Используйте AI-помощника, например GitHub Copilot или ChatGPT, и примените технику «самоулучшения» (self-refine), чтобы улучшить этот код.

## Решение

Попробуйте решить задание, добавив подходящие запросы к коду.

> [!TIP]
> Сформулируйте запрос с просьбой улучшить код, желательно ограничить количество улучшений. Можно также попросить улучшить код в определённом направлении, например архитектура, производительность, безопасность и т.д.

[Решение](../../../05-advanced-prompts/python/aoai-solution.py)

## Проверка знаний

Зачем использовать chain-of-thought prompting? Приведите 1 правильный и 2 неправильных ответа.

1. Чтобы научить LLM решать задачу.
1. B, Чтобы научить LLM находить ошибки в коде.
1. C, Чтобы заставить LLM придумывать разные решения.

Ответ: 1, потому что chain-of-thought — это способ показать LLM, как решать задачу, предоставляя последовательность шагов и похожие задачи с их решениями.

## 🚀 Вызов

Вы только что применили технику самоулучшения в задании. Возьмите любую программу, которую вы написали, и подумайте, какие улучшения вы хотели бы в неё внести. Теперь примените технику самоулучшения, чтобы реализовать эти изменения. Как вы думаете, результат стал лучше или хуже?

## Отличная работа! Продолжайте обучение

После завершения этого урока ознакомьтесь с нашей [коллекцией по генеративному ИИ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжить развивать свои знания в области генеративного ИИ!

Перейдите к уроку 6, где мы применим знания по Prompt Engineering, [создавая приложения для генерации текста](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.