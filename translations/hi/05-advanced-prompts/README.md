<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:28:14+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "hi"
}
-->

# Python वेब API के लिए कोड जनरेट करें

यह गाइड आपको Python में एक वेब API बनाने के लिए आवश्यक कोड जनरेट करने में मदद करेगा। हम Flask फ्रेमवर्क का उपयोग करेंगे क्योंकि यह हल्का और उपयोग में आसान है।

## आवश्यकताएँ

- Python 3.6 या उससे ऊपर
- Flask इंस्टॉल किया हुआ होना चाहिए (`pip install Flask`)

## बेसिक API सेटअप

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# एक सिंपल रूट जो "Hello, World!" रिटर्न करता है
@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
```

## GET रिक्वेस्ट हैंडल करना

```python
@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {
        "id": 1,
        "name": "Sample Item",
        "description": "यह एक नमूना डेटा है"
    }
    return jsonify(sample_data)
```

## POST रिक्वेस्ट हैंडल करना

```python
@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    # यहाँ आप डेटा को प्रोसेस कर सकते हैं
    return jsonify({"message": "डेटा प्राप्त हुआ", "received_data": data}), 201
```

## API चलाना

टर्मिनल में नीचे दिया गया कमांड चलाएं:

```bash
python app.py
```

यह आपका API लोकलहोस्ट पर `http://127.0.0.1:5000/` पर चलाएगा।

## निष्कर्ष

इस गाइड में हमने एक बेसिक Python वेब API कैसे बनाएं, इसके बारे में जाना। आप इसे अपनी जरूरत के अनुसार बढ़ा सकते हैं और अधिक जटिल फीचर्स जोड़ सकते हैं।
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

प्रॉम्प्ट को फिर से चलाने पर हमें यह परिणाम मिलता है:

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

इन दोनों आउटपुट्स में केवल एक छोटा सा अंतर है। इस बार इसके विपरीत करते हैं, तापमान को 0.9 सेट करते हैं:

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

और दूसरी बार 0.9 तापमान मान के साथ प्रयास:

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

जैसा कि आप देख सकते हैं, परिणाम काफी विविध हो सकते हैं।

> Note, कि आप आउटपुट को बदलने के लिए और भी कई पैरामीटर बदल सकते हैं, जैसे top-k, top-p, repetition penalty, length penalty और diversity penalty, लेकिन ये इस पाठ्यक्रम के दायरे से बाहर हैं।

## अच्छी प्रथाएँ

आप कई ऐसी प्रथाएँ अपना सकते हैं जिनसे आप अपनी इच्छित चीज़ प्राप्त कर सकें। जैसे-जैसे आप प्रॉम्प्टिंग का अधिक उपयोग करेंगे, आपको अपनी खुद की शैली मिल जाएगी।

हमने जिन तकनीकों को कवर किया है, उसके अलावा LLM को प्रॉम्प्ट करते समय कुछ अच्छी प्रथाएँ ध्यान में रखनी चाहिए।

यहाँ कुछ अच्छी प्रथाएँ दी गई हैं जिन्हें ध्यान में रखना चाहिए:

- **संदर्भ निर्दिष्ट करें**। संदर्भ महत्वपूर्ण होता है, जितना अधिक आप डोमेन, विषय आदि जैसे विवरण दे सकेंगे, उतना बेहतर होगा।
- आउटपुट को सीमित करें। यदि आप किसी विशिष्ट संख्या में आइटम या किसी निश्चित लंबाई चाहते हैं, तो इसे स्पष्ट करें।
- **क्या और कैसे दोनों निर्दिष्ट करें**। याद रखें कि आप जो चाहते हैं और उसे कैसे चाहते हैं, दोनों का उल्लेख करें, उदाहरण के लिए "Create a Python Web API with routes products and customers, divide it into 3 files"।
- **टेम्पलेट्स का उपयोग करें**। अक्सर, आप अपने प्रॉम्प्ट्स को अपनी कंपनी के डेटा से समृद्ध करना चाहेंगे। इसके लिए टेम्पलेट्स का उपयोग करें। टेम्पलेट्स में ऐसे वेरिएबल हो सकते हैं जिन्हें आप वास्तविक डेटा से बदल सकते हैं।
- **सही वर्तनी का प्रयोग करें**। LLM आपको सही उत्तर दे सकता है, लेकिन यदि आप सही वर्तनी का उपयोग करेंगे, तो आपको बेहतर उत्तर मिलेगा।

## असाइनमेंट

यहाँ Python में Flask का उपयोग करके एक सरल API बनाने का कोड दिया गया है:

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

GitHub Copilot या ChatGPT जैसे AI सहायक का उपयोग करें और "self-refine" तकनीक लागू करके कोड में सुधार करें।

## समाधान

कृपया कोड में उपयुक्त प्रॉम्प्ट जोड़कर असाइनमेंट को हल करने का प्रयास करें।

> [!TIP]
> सुधार के लिए प्रॉम्प्ट बनाएं, यह अच्छा होगा कि आप सुधारों की संख्या सीमित करें। आप इसे किसी विशेष तरीके से सुधारने के लिए भी कह सकते हैं, जैसे आर्किटेक्चर, प्रदर्शन, सुरक्षा आदि।

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## ज्ञान जांच

मैं chain-of-thought prompting क्यों उपयोग करूँ? मुझे 1 सही उत्तर और 2 गलत उत्तर दिखाएं।

1. LLM को समस्या हल करना सिखाने के लिए।
1. B, LLM को कोड में त्रुटियाँ खोजने के लिए सिखाने के लिए।
1. C, LLM को विभिन्न समाधान सुझाने के लिए निर्देशित करने के लिए।

उत्तर: 1, क्योंकि chain-of-thought LLM को समस्या हल करने के लिए चरण-दर-चरण प्रक्रिया और समान समस्याओं के समाधान दिखाने के बारे में है।

## 🚀 चुनौती

आपने असाइनमेंट में self-refine तकनीक का उपयोग किया। किसी भी प्रोग्राम को लें जो आपने बनाया है और सोचें कि आप उसमें कौन से सुधार करना चाहेंगे। अब self-refine तकनीक का उपयोग करके प्रस्तावित बदलाव लागू करें। आपको परिणाम कैसा लगा, बेहतर या खराब?

## शानदार काम! अपनी सीख जारी रखें

इस पाठ को पूरा करने के बाद, हमारे [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) को देखें और अपनी Generative AI की जानकारी को और बढ़ाएं!

अब Lesson 6 पर जाएं जहाँ हम Prompt Engineering का उपयोग करके [text generation apps बनाएंगे](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।