<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:27:49+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "ko"
}
-->

> "파이썬 웹 API용 코드 생성하기"
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

프롬프트를 다시 실행하면 다음과 같은 결과가 나옵니다:

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

이 두 출력물 사이에는 아주 작은 차이만 있습니다. 이번에는 반대로 해보겠습니다. 온도를 0.9로 설정해 봅시다:

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

그리고 온도 값을 0.9로 설정한 두 번째 시도 결과입니다:

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

보시다시피 결과가 훨씬 다양해졌습니다.

> Note, 출력 변화를 위해 top-k, top-p, repetition penalty, length penalty, diversity penalty 같은 더 많은 매개변수를 조정할 수 있지만, 이들은 이 커리큘럼의 범위를 벗어납니다.

## 좋은 실천 방법

원하는 결과를 얻기 위해 적용할 수 있는 다양한 방법들이 있습니다. 프롬프트를 더 많이 사용하면서 자신만의 스타일을 찾게 될 것입니다.

지금까지 다룬 기법들 외에도, LLM에 프롬프트를 작성할 때 고려할 만한 좋은 실천 방법들이 있습니다.

다음은 고려해볼 만한 좋은 실천 방법들입니다:

- **맥락을 명확히 하세요**. 맥락이 중요합니다. 도메인, 주제 등 가능한 한 구체적으로 명시할수록 좋습니다.
- 출력 범위를 제한하세요. 특정 개수의 항목이나 특정 길이를 원한다면 명확히 지정하세요.
- **무엇을 원하는지와 어떻게 원하는지를 모두 명시하세요**. 예를 들어 "products와 customers 라우트를 가진 Python Web API를 만들고, 3개의 파일로 나누어라"처럼 원하는 것과 방식을 함께 언급하세요.
- **템플릿을 활용하세요**. 종종 회사의 데이터를 활용해 프롬프트를 풍부하게 만들고 싶을 때가 있습니다. 템플릿을 사용하면 변수에 실제 데이터를 넣어 쉽게 적용할 수 있습니다.
- **맞춤법을 정확히 하세요**. LLM이 올바른 답변을 줄 수 있지만, 맞춤법이 정확할수록 더 좋은 답변을 받을 수 있습니다.

## 과제

다음은 Flask를 사용해 간단한 API를 만드는 Python 코드입니다:

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

GitHub Copilot이나 ChatGPT 같은 AI 어시스턴트를 사용해 "self-refine" 기법을 적용하여 코드를 개선해 보세요.

## 해답

적절한 프롬프트를 코드에 추가하여 과제를 해결해 보세요.

> [!TIP]
> 개선을 요청하는 프롬프트를 작성할 때는 개선 횟수를 제한하는 것이 좋습니다. 또한 아키텍처, 성능, 보안 등 특정 측면에서 개선을 요청할 수도 있습니다.

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## 지식 점검

왜 chain-of-thought 프롬프트를 사용하나요? 올바른 답변 1개와 틀린 답변 2개를 보여주세요.

1. 문제 해결 방법을 LLM에 가르치기 위해서입니다.  
1. B, LLM에게 코드의 오류를 찾도록 가르치기 위해서입니다.  
1. C, LLM에게 다양한 해결책을 생각해내도록 지시하기 위해서입니다.

A: 1번이 맞습니다. chain-of-thought는 LLM에게 문제를 해결하는 방법을 단계별로 보여주고, 유사한 문제와 해결 과정을 제공하는 방식입니다.

## 🚀 도전 과제

과제에서 self-refine 기법을 사용해 보았습니다. 자신이 만든 프로그램 중 하나를 선택해 어떤 개선을 적용할지 생각해 보세요. 그리고 self-refine 기법을 사용해 제안한 변경사항을 적용해 보세요. 결과는 어땠나요? 더 나아졌나요, 아니면 나빠졌나요?

## 훌륭합니다! 학습을 계속하세요

이 수업을 마친 후에는 [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성 AI 지식을 계속 향상시키세요!

다음 6강에서는 프롬프트 엔지니어링 지식을 활용해 [텍스트 생성 앱을 만드는 방법](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)을 배웁니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.