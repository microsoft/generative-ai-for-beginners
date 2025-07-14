<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:25:13+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "ur"
}
-->

> "پائتھون ویب API کے لیے کوڈ تیار کریں"
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

پھر سے پرامپٹ چلانے پر ہمیں یہ نتیجہ ملتا ہے:

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

ان دونوں نتائج میں صرف معمولی فرق ہے۔ اس بار الٹ کریں، درجہ حرارت کو 0.9 پر سیٹ کرتے ہیں:

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

اور درجہ حرارت کی قیمت 0.9 کے ساتھ دوسری کوشش:

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

جیسا کہ آپ دیکھ سکتے ہیں، نتائج بہت مختلف ہو سکتے ہیں۔

> [!NOTE]
> یاد رکھیں، آپ آؤٹ پٹ کو مختلف بنانے کے لیے مزید پیرامیٹرز بھی تبدیل کر سکتے ہیں، جیسے top-k، top-p، repetition penalty، length penalty اور diversity penalty، لیکن یہ نصاب کے دائرہ کار سے باہر ہیں۔

## اچھی عادات

آپ بہت سی عادات اپنا سکتے ہیں تاکہ جو آپ چاہتے ہیں وہ حاصل کر سکیں۔ جوں جوں آپ پرامپٹنگ زیادہ استعمال کریں گے، آپ اپنی اپنی طرز تلاش کر لیں گے۔

ان تکنیکوں کے علاوہ جو ہم نے کور کی ہیں، LLM کو پرامپٹ کرتے وقت کچھ اچھی عادات کو مدنظر رکھنا ضروری ہے۔

یہاں کچھ اچھی عادات دی گئی ہیں جن پر غور کریں:

- **سیاق و سباق واضح کریں**۔ سیاق و سباق اہم ہے، جتنا زیادہ آپ ڈومین، موضوع وغیرہ واضح کریں گے، اتنا بہتر ہوگا۔
- آؤٹ پٹ کو محدود کریں۔ اگر آپ مخصوص تعداد میں آئٹمز یا مخصوص لمبائی چاہتے ہیں تو اسے واضح کریں۔
- **کیا اور کیسے دونوں واضح کریں**۔ یاد رکھیں کہ آپ جو چاہتے ہیں اور کیسے چاہتے ہیں دونوں کا ذکر کریں، مثلاً "Python Web API بنائیں جس میں routes products اور customers ہوں، اسے 3 فائلوں میں تقسیم کریں"۔
- **ٹیمپلیٹس استعمال کریں**۔ اکثر آپ اپنی کمپنی کے ڈیٹا کے ساتھ پرامپٹس کو بہتر بنانا چاہیں گے۔ اس کے لیے ٹیمپلیٹس استعمال کریں۔ ٹیمپلیٹس میں متغیرات ہو سکتے ہیں جنہیں آپ اصل ڈیٹا سے بدل سکتے ہیں۔
- **صحیح املا کریں**۔ LLM آپ کو درست جواب دے سکتا ہے، لیکن اگر آپ صحیح املا کریں گے تو بہتر جواب ملے گا۔

## اسائنمنٹ

یہاں Python میں کوڈ ہے جو Flask استعمال کرتے ہوئے ایک سادہ API بنانے کا طریقہ دکھاتا ہے:

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

GitHub Copilot یا ChatGPT جیسے AI اسسٹنٹ کا استعمال کریں اور "self-refine" تکنیک کو کوڈ بہتر بنانے کے لیے اپلائی کریں۔

## حل

براہ کرم اسائنمنٹ کو حل کرنے کی کوشش کریں اور کوڈ میں مناسب پرامپٹس شامل کریں۔

> [!TIP]
> ایک پرامپٹ بنائیں جس میں بہتری کی درخواست ہو، بہتری کی تعداد محدود کرنا اچھا خیال ہے۔ آپ مخصوص انداز میں بہتری بھی مانگ سکتے ہیں، مثلاً آرکیٹیکچر، کارکردگی، سیکیورٹی وغیرہ۔

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## علم کی جانچ

میں chain-of-thought prompting کیوں استعمال کروں؟ مجھے 1 درست جواب اور 2 غلط جوابات دکھائیں۔

1. LLM کو مسئلہ حل کرنا سکھانے کے لیے۔
1. B، LLM کو کوڈ میں غلطیاں تلاش کرنا سکھانے کے لیے۔
1. C، LLM کو مختلف حل پیش کرنے کی ہدایت دینے کے لیے۔

جواب: 1، کیونکہ chain-of-thought LLM کو مسئلہ حل کرنے کے لیے قدم بہ قدم طریقہ اور ملتے جلتے مسائل اور ان کے حل دکھانے کے بارے میں ہے۔

## 🚀 چیلنج

آپ نے ابھی اسائنمنٹ میں self-refine تکنیک استعمال کی ہے۔ کوئی بھی پروگرام جو آپ نے بنایا ہے لے کر سوچیں کہ آپ اس میں کیا بہتریاں کرنا چاہیں گے۔ اب self-refine تکنیک استعمال کرتے ہوئے تجویز کردہ تبدیلیاں اپلائی کریں۔ آپ کے خیال میں نتیجہ کیسا رہا، بہتر یا خراب؟

## شاندار کام! اپنی تعلیم جاری رکھیں

اس سبق کو مکمل کرنے کے بعد، ہمارے [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) کو دیکھیں تاکہ آپ اپنی Generative AI کی معلومات کو مزید بڑھا سکیں!

سبق 6 پر جائیں جہاں ہم Prompt Engineering کا استعمال کرتے ہوئے [text generation apps بنانے](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst) کا عمل کریں گے۔

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔