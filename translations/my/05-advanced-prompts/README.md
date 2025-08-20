<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:41:50+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "my"
}
-->

> "Python Web API အတွက် ကုဒ်ထုတ်ပေးပါ"
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

prompt ကို ထပ်မံ chạy လုပ်တဲ့အခါ ရလာတဲ့ရလဒ်က ဒီလိုဖြစ်ပါတယ်။

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

ဒီ output နှစ်ခုကြားမှာ အနည်းငယ်သာကွာခြားချက်ရှိပါတယ်။ ဒီတစ်ခါမှာတော့ အနောက်ဘက်ကိုလုပ်ကြည့်ပါစို့၊ temperature ကို 0.9 သတ်မှတ်ကြည့်မယ်။

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

နောက်တစ်ကြိမ် temperature 0.9 နဲ့ ပြန်လုပ်ကြည့်တာက ဒီလိုဖြစ်ပါတယ်။

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

မြင်ရသလို ရလဒ်တွေက အမျိုးမျိုးကွဲပြားမှုများစွာရှိပါတယ်။

> Note, output ကို မတူညီအောင်ပြောင်းလဲဖို့ top-k, top-p, repetition penalty, length penalty, diversity penalty စတဲ့ parameter တွေကိုလည်းပြောင်းလဲနိုင်ပါတယ်၊ ဒါပေမယ့် ဒီသင်ခန်းစာမှာတော့ မပါဝင်ပါ။

## ကောင်းမွန်တဲ့ လေ့လာမှုနည်းလမ်းများ

သင်လိုချင်တာရဖို့ ကြိုးစားတဲ့အခါ အသုံးပြုနိုင်တဲ့ လေ့လာမှုနည်းလမ်းများ များစွာရှိပါတယ်။ prompt ကို မကြာခဏအသုံးပြုသလို သင့်ကိုယ်ပိုင်စတိုင်ကို ရှာတွေ့မှာဖြစ်ပါတယ်။

ကျွန်တော်တို့ လေ့လာခဲ့တဲ့ နည်းလမ်းတွေ အပြင် LLM ကို prompt ပေးတဲ့အခါ စဉ်းစားသင့်တဲ့ ကောင်းမွန်တဲ့ လေ့လာမှုနည်းလမ်းတွေ ရှိပါတယ်။

အောက်ပါကောင်းမွန်တဲ့ လေ့လာမှုနည်းလမ်းများကို စဉ်းစားကြည့်ပါ။

- **Context ကို သတ်မှတ်ပါ။** Context က အရေးကြီးပါတယ်၊ domain, topic စသဖြင့် သတ်မှတ်နိုင်သမျှ ပိုသေချာသင့်ပါတယ်။
- Output ကို ကန့်သတ်ပါ။ အကြောင်းအရာအရေအတွက် သို့မဟုတ် အရှည်အတိုင်း သတ်မှတ်ချင်ရင် သတ်မှတ်ပါ။
- **ဘာလိုချင်သလဲ၊ ဘယ်လိုလိုချင်သလဲ နှစ်ခုလုံးကို သတ်မှတ်ပါ။** ဥပမာ "products နဲ့ customers ဆိုတဲ့ routes တွေပါဝင်တဲ့ Python Web API တစ်ခု ဖန်တီးပါ၊ ဖိုင် ၃ ဖိုင်ခွဲပါ" ဆိုပြီး ပြောပါ။
- **Template များကို အသုံးပြုပါ။** မကြာခဏ သင့်ကုမ္ပဏီရဲ့ ဒေတာနဲ့ prompt တွေကို ပိုမိုတိုးတက်အောင်လုပ်ချင်မှာဖြစ်ပါတယ်။ Template တွေမှာ variable တွေ ပါနိုင်ပြီး အဲဒီ variable တွေကို အမှန်တကယ်ရှိတဲ့ ဒေတာနဲ့ အစားထိုးနိုင်ပါတယ်။
- **စာလုံးပေါင်းမှန်စွာ ရေးပါ။** LLM တွေက မှန်ကန်တဲ့ဖြေကြားချက်ပေးနိုင်ပေမယ့် စာလုံးပေါင်းမှန်စွာရေးရင် ပိုကောင်းတဲ့ဖြေကြားချက်ရမှာ ဖြစ်ပါတယ်။

## လေ့ကျင့်ခန်း

Flask ကို အသုံးပြုပြီး ရိုးရှင်းတဲ့ API တစ်ခု ဖန်တီးနည်းကို Python ကုဒ်နမူနာဖြင့် ပြပါ။

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

GitHub Copilot သို့မဟုတ် ChatGPT ကဲ့သို့ AI အကူအညီတစ်ခုကို အသုံးပြုပြီး "self-refine" နည်းလမ်းကို အသုံးပြုကာ ကုဒ်ကို တိုးတက်အောင် ပြုပြင်ပါ။

## ဖြေရှင်းချက်

သင့်အနေနဲ့ ကုဒ်ထဲမှာ သင့်တော်တဲ့ prompt တွေ ထည့်သွင်းပြီး လေ့ကျင့်ခန်းကို ဖြေရှင်းကြည့်ပါ။

> [!TIP]
> တိုးတက်အောင် ပြုလုပ်ဖို့ prompt တစ်ခု ဖန်တီးပါ၊ တိုးတက်မှု အရေအတွက်ကို ကန့်သတ်ဖို့ကောင်းပါတယ်။ architecture, performance, security စသဖြင့် တိုးတက်စေချင်တဲ့ နည်းလမ်းတစ်ခုအတိုင်းလည်း တောင်းဆိုနိုင်ပါတယ်။

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## အသိပညာ စစ်ဆေးခြင်း

chain-of-thought prompting ကို ဘာကြောင့် အသုံးပြုမလဲ? မှန်ကန်တဲ့ဖြေကြားချက် ၁ ခုနဲ့ မှားယွင်းတဲ့ဖြေကြားချက် ၂ ခု ပြပါ။

1. LLM ကို ပြဿနာဖြေရှင်းနည်း သင်ပေးဖို့။
1. B, LLM ကို ကုဒ်အမှားတွေ ရှာဖွေဖို့ သင်ပေးဖို့။
1. C, LLM ကို မတူညီတဲ့ ဖြေရှင်းနည်းတွေ ထုတ်ဖော်ဖို့ ညွှန်ကြားဖို့။

A: 1, chain-of-thought က LLM ကို ပြဿနာဖြေရှင်းနည်းကို အဆင့်ဆင့်နဲ့ ပြသပေးခြင်း၊ ဆင်တူပြဿနာတွေနဲ့ ဖြေရှင်းနည်းတွေကို ပြသပေးခြင်း ဖြစ်ပါတယ်။

## 🚀 စိန်ခေါ်မှု

လေ့ကျင့်ခန်းမှာ self-refine နည်းလမ်းကို အသုံးပြုပြီးသားဖြစ်ပါတယ်။ သင်ဖန်တီးထားတဲ့ အစီအစဉ်တစ်ခုကို ယူပြီး ဘယ်လိုတိုးတက်မှုတွေ လုပ်ချင်မလဲ စဉ်းစားပါ။ အခုတော့ self-refine နည်းလမ်းကို အသုံးပြုပြီး အဆိုပြုထားတဲ့ ပြင်ဆင်မှုတွေကို လုပ်ဆောင်ပါ။ ရလဒ်ကို ဘယ်လိုထင်ပါသလဲ၊ ပိုကောင်းသလား၊ ပိုမကောင်းသလား?

## အလွန်ကောင်းပါတယ်! သင်ယူမှုကို ဆက်လက်လုပ်ဆောင်ပါ

ဒီသင်ခန်းစာပြီးဆုံးပြီးနောက် [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ရှုပြီး Generative AI အသိပညာကို ပိုမိုမြှင့်တင်ပါ။

Lesson 6 ကို သွားပါ၊ ဒီမှာတော့ Prompt Engineering အသိပညာကို အသုံးပြုပြီး [စာသားထုတ်လုပ်မှု အက်ပ်များ ဖန်တီးခြင်း](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst) ကို လေ့လာမှာ ဖြစ်ပါတယ်။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းသည် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ပညာရှင်များ၏ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။