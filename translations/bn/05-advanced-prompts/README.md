<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:28:43+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "bn"
}
-->

> "পাইথন ওয়েব এপিআই-এর জন্য কোড তৈরি করুন"
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

আবার প্রম্পট চালালে আমরা এই ফলাফল পাই:

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

এই দুই আউটপুটের মধ্যে খুব সামান্য পার্থক্য আছে। এবার উল্টোটা করি, তাপমাত্রা ০.৯ সেট করি:

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

এবং তাপমাত্রা মান ০.৯ দিয়ে দ্বিতীয় চেষ্টা:

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

আপনি দেখতে পাচ্ছেন, ফলাফলগুলো অনেক বেশি বৈচিত্র্যময় হয়েছে।

> Note, যে আরও অনেক প্যারামিটার আছে যেগুলো পরিবর্তন করে আউটপুট ভিন্ন করা যায়, যেমন top-k, top-p, repetition penalty, length penalty এবং diversity penalty, কিন্তু এগুলো এই পাঠ্যক্রমের আওতার বাইরে।

## ভালো অভ্যাস

আপনি অনেক ধরনের অভ্যাস প্রয়োগ করতে পারেন যা আপনার কাঙ্ক্ষিত ফলাফল পেতে সাহায্য করবে। যত বেশি প্রম্পট ব্যবহার করবেন, ততই আপনার নিজস্ব স্টাইল তৈরি হবে।

আমরা যেসব কৌশল আলোচনা করেছি তার পাশাপাশি, LLM-কে প্রম্পট করার সময় কিছু ভালো অভ্যাস বিবেচনা করা উচিত।

এখানে কিছু ভালো অভ্যাস দেওয়া হলো:

- **প্রসঙ্গ নির্দিষ্ট করুন**। প্রসঙ্গ গুরুত্বপূর্ণ, আপনি যত বেশি নির্দিষ্ট করতে পারবেন যেমন ডোমেইন, বিষয় ইত্যাদি, ততই ভালো।
- আউটপুট সীমাবদ্ধ করুন। যদি নির্দিষ্ট সংখ্যক আইটেম বা নির্দিষ্ট দৈর্ঘ্যের আউটপুট চান, তা স্পষ্ট করুন।
- **কি এবং কিভাবে উভয়ই নির্দিষ্ট করুন**। মনে রাখবেন কি চান এবং কিভাবে চান উভয়ই উল্লেখ করতে হবে, যেমন "Create a Python Web API with routes products and customers, divide it into 3 files"।
- **টেমপ্লেট ব্যবহার করুন**। প্রায়ই আপনি আপনার কোম্পানির ডেটা দিয়ে প্রম্পট সমৃদ্ধ করতে চাইবেন। এর জন্য টেমপ্লেট ব্যবহার করুন। টেমপ্লেটে ভেরিয়েবল থাকতে পারে যেগুলো আপনি আসল ডেটা দিয়ে প্রতিস্থাপন করবেন।
- **সঠিক বানান ব্যবহার করুন**। LLM সঠিক উত্তর দিতে পারে, কিন্তু সঠিক বানান ব্যবহার করলে আরও ভালো উত্তর পাবেন।

## অ্যাসাইনমেন্ট

এখানে Python-এ Flask ব্যবহার করে একটি সহজ API তৈরি করার কোড দেওয়া হলো:

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

GitHub Copilot বা ChatGPT-এর মতো AI সহকারী ব্যবহার করে "self-refine" কৌশল প্রয়োগ করে কোডটি উন্নত করুন।

## সমাধান

কোডে উপযুক্ত প্রম্পট যোগ করে অ্যাসাইনমেন্টটি সমাধান করার চেষ্টা করুন।

> [!TIP]
> উন্নতির জন্য একটি প্রম্পট তৈরি করুন, কতগুলো উন্নতি করতে চান তা সীমাবদ্ধ করা ভালো। আপনি নির্দিষ্ট কোনো দিক যেমন আর্কিটেকচার, পারফরম্যান্স, সিকিউরিটি ইত্যাদি উন্নত করার জন্যও বলতে পারেন।

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## জ্ঞান যাচাই

কেন আমি chain-of-thought prompting ব্যবহার করব? আমাকে ১টি সঠিক উত্তর এবং ২টি ভুল উত্তর দেখাও।

1. LLM-কে একটি সমস্যা সমাধান করতে শেখানোর জন্য।
1. B, LLM-কে কোডে ত্রুটি খুঁজে বের করতে শেখানোর জন্য।
1. C, LLM-কে বিভিন্ন সমাধান বের করতে নির্দেশ দেওয়ার জন্য।

উত্তর: ১, কারণ chain-of-thought হলো LLM-কে ধাপে ধাপে সমস্যা সমাধানের পদ্ধতি দেখানো, এবং একই ধরনের সমস্যা ও সেগুলো কিভাবে সমাধান করা হয়েছে তা শেখানো।

## 🚀 চ্যালেঞ্জ

আপনি অ্যাসাইনমেন্টে self-refine কৌশল ব্যবহার করেছেন। আপনি যেকোনো প্রোগ্রাম নিয়ে ভাবুন, সেখানে আপনি কী কী উন্নতি করতে চান। এখন self-refine কৌশল ব্যবহার করে প্রস্তাবিত পরিবর্তনগুলো প্রয়োগ করুন। আপনার মনে হলো ফলাফল কেমন হলো, ভালো না খারাপ?

## অসাধারণ কাজ! আপনার শেখা চালিয়ে যান

এই পাঠ শেষ করার পর, আমাদের [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন এবং আপনার Generative AI জ্ঞান আরও উন্নত করুন!

Lesson 6-এ যান যেখানে আমরা Prompt Engineering-এর জ্ঞান প্রয়োগ করে [text generation apps তৈরি করব](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।