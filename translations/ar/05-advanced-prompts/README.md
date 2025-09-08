<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:24:28+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "ar"
}
-->

> "توليد كود لواجهة برمجة تطبيقات ويب بلغة بايثون"
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

تشغيل الأمر مرة أخرى يعطينا هذه النتيجة:

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

هناك فرق بسيط جدًا بين هذين الناتجين. لنقم بالعكس هذه المرة، لنضبط قيمة temperature على 0.9:

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

والمحاولة الثانية عند قيمة temperature 0.9:

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

كما ترى، النتائج لا يمكن أن تكون أكثر تنوعًا.

> ملاحظة، هناك المزيد من المعاملات التي يمكنك تعديلها لتغيير الناتج، مثل top-k، top-p، عقوبة التكرار، عقوبة الطول وعقوبة التنوع، لكن هذه خارج نطاق هذا المنهج.

## ممارسات جيدة

هناك العديد من الممارسات التي يمكنك تطبيقها لمحاولة الحصول على ما تريد. ستجد أسلوبك الخاص مع تكرار استخدامك للأوامر.

بالإضافة إلى التقنيات التي تناولناها، هناك بعض الممارسات الجيدة التي يجب أخذها في الاعتبار عند توجيه الأوامر إلى نموذج اللغة الكبير.

إليك بعض الممارسات الجيدة التي يجب مراعاتها:

- **حدد السياق**. السياق مهم، كلما استطعت تحديده أكثر مثل المجال، الموضوع، إلخ، كان ذلك أفضل.
- حدد الناتج. إذا كنت تريد عددًا معينًا من العناصر أو طولًا معينًا، فحدد ذلك.
- **حدد ماذا وكيف**. تذكر أن تذكر ماذا تريد وكيف تريده، على سبيل المثال "أنشئ API ويب بلغة Python مع مسارات products و customers، وقسمه إلى 3 ملفات".
- **استخدم القوالب**. غالبًا ما سترغب في إثراء الأوامر ببيانات من شركتك. استخدم القوالب لذلك. يمكن أن تحتوي القوالب على متغيرات تستبدلها بالبيانات الفعلية.
- **اكتب بشكل صحيح**. قد يقدم لك نموذج اللغة الكبير ردًا صحيحًا، لكن إذا كتبت بشكل صحيح، ستحصل على رد أفضل.

## المهمة

إليك كود بلغة Python يوضح كيفية بناء API بسيط باستخدام Flask:

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

استخدم مساعدًا ذكيًا مثل GitHub Copilot أو ChatGPT وطبق تقنية "التحسين الذاتي" لتحسين الكود.

## الحل

حاول حل المهمة بإضافة أوامر مناسبة إلى الكود.

> [!TIP]
> صغ أمرًا تطلب فيه تحسين الكود، من الجيد تحديد عدد التحسينات. يمكنك أيضًا طلب تحسين بطريقة معينة، مثل الهيكلية، الأداء، الأمان، إلخ.

[الحل](../../../05-advanced-prompts/python/aoai-solution.py)

## اختبار المعرفة

لماذا أستخدم chain-of-thought prompting؟ أظهر لي ردًا صحيحًا واحدًا وردين غير صحيحين.

1. لتعليم نموذج اللغة الكبير كيفية حل مشكلة.
1. ب، لتعليم نموذج اللغة الكبير كيفية إيجاد الأخطاء في الكود.
1. ج، لإرشاد نموذج اللغة الكبير لتقديم حلول مختلفة.

الإجابة: 1، لأن chain-of-thought تدور حول إظهار كيفية حل المشكلة للنموذج من خلال تزويده بسلسلة من الخطوات، ومشاكل مشابهة وكيف تم حلها.

## 🚀 التحدي

لقد استخدمت للتو تقنية التحسين الذاتي في المهمة. خذ أي برنامج قمت ببنائه وفكر في التحسينات التي تود تطبيقها عليه. الآن استخدم تقنية التحسين الذاتي لتطبيق التغييرات المقترحة. ما رأيك في النتيجة، هل كانت أفضل أم أسوأ؟

## عمل رائع! واصل تعلمك

بعد إكمال هذا الدرس، اطلع على [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة تطوير معرفتك في الذكاء الاصطناعي التوليدي!

توجه إلى الدرس 6 حيث سنطبق معرفتنا في هندسة الأوامر من خلال [بناء تطبيقات توليد النصوص](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.