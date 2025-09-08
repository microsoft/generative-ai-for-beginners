<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:29:12+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "mr"
}
-->

> "Python वेब API साठी कोड तयार करा"
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

पुन्हा प्रॉम्प्ट चालविल्यावर आपल्याला हा परिणाम मिळतो:

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

या दोन आउटपुटमध्ये फक्त थोडासा फरक आहे. यावेळी उलट करूया, तापमान 0.9 वर सेट करूया:

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

आणि तापमान मूल्य 0.9 वर दुसऱ्या प्रयत्नाचा परिणाम:

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

जसे तुम्ही पाहू शकता, परिणाम खूपच वेगवेगळे आहेत.

> लक्षात ठेवा, आउटपुट वेगळे करण्यासाठी तुम्ही अजूनही अनेक पॅरामीटर्स बदलू शकता, जसे की top-k, top-p, repetition penalty, length penalty आणि diversity penalty, पण हे या अभ्यासक्रमाच्या व्याप्तीबाहेर आहेत.

## चांगल्या पद्धती

तुम्हाला हवे ते मिळवण्यासाठी तुम्ही अनेक पद्धती वापरू शकता. तुम्ही जितका जास्त प्रॉम्प्टिंग वापराल तितका तुमचा स्वतःचा स्टाईल तयार होईल.

आम्ही ज्या तंत्रांचा आढावा घेतला आहे त्याशिवाय, LLM ला प्रॉम्प्ट करताना काही चांगल्या पद्धती लक्षात ठेवाव्यात.

येथे काही चांगल्या पद्धती दिल्या आहेत:

- **संदर्भ स्पष्ट करा**. संदर्भ महत्त्वाचा आहे, तुम्ही जितका अधिक डोमेन, विषय इत्यादी स्पष्ट कराल तितके चांगले.
- आउटपुट मर्यादित करा. जर तुम्हाला विशिष्ट आयटम्सची संख्या किंवा विशिष्ट लांबी हवी असेल तर ती नमूद करा.
- **काय आणि कसे दोन्ही नमूद करा**. तुम्हाला काय हवे आहे आणि ते कसे हवे आहे हे दोन्ही सांगणे आवश्यक आहे, उदाहरणार्थ "Create a Python Web API with routes products and customers, divide it into 3 files".
- **टेम्पलेट्स वापरा**. अनेकदा तुम्हाला तुमच्या कंपनीच्या डेटाने प्रॉम्प्ट समृद्ध करायचे असतात. यासाठी टेम्पलेट्स वापरा. टेम्पलेट्समध्ये अशा व्हेरिएबल्स असू शकतात ज्यांना तुम्ही प्रत्यक्ष डेटाने बदलू शकता.
- **योग्य स्पेलिंग वापरा**. LLM तुम्हाला बरोबर उत्तर देऊ शकते, पण जर तुम्ही योग्य स्पेलिंग वापराल तर उत्तम उत्तर मिळेल.

## असाइनमेंट

Flask वापरून साधी API कशी तयार करायची हे दाखवणारा Python कोड येथे आहे:

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

GitHub Copilot किंवा ChatGPT सारखा AI सहाय्यक वापरा आणि "self-refine" तंत्र वापरून कोड सुधारण्याचा प्रयत्न करा.

## समाधान

कृपया योग्य प्रॉम्प्ट्स कोडमध्ये जोडून असाइनमेंट सोडवण्याचा प्रयत्न करा.

> [!TIP]
> सुधारणा करण्यासाठी प्रॉम्प्ट तयार करा, सुधारणा किती करायच्या याची मर्यादा ठेवा. तुम्ही विशिष्ट प्रकारे सुधारणा करण्यासही सांगू शकता, उदाहरणार्थ आर्किटेक्चर, कार्यक्षमता, सुरक्षा इत्यादी.

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## ज्ञान तपासणी

मी chain-of-thought prompting का वापरू? मला 1 बरोबर उत्तर आणि 2 चुकीची उत्तरे दाखवा.

1. LLM ला समस्या सोडवायला शिकवण्यासाठी.
1. B, LLM ला कोडमधील चुका शोधायला शिकवण्यासाठी.
1. C, LLM ला वेगवेगळे उपाय सुचवायला सांगण्यासाठी.

उत्तर: 1, कारण chain-of-thought म्हणजे LLM ला समस्या सोडवण्याचे पाऊल-दर-पाऊल मार्ग दाखवणे, तसेच त्याच्यासारख्या समस्या आणि त्यांचे निराकरण कसे झाले हे समजावणे.

## 🚀 आव्हान

तुम्ही असाइनमेंटमध्ये self-refine तंत्र वापरले आहे. तुम्ही तयार केलेल्या कोणत्याही प्रोग्राममध्ये तुम्हाला कोणत्या सुधारणा करायच्या आहेत हे विचार करा. नंतर self-refine तंत्र वापरून प्रस्तावित बदल करा. तुम्हाला निकाल कसा वाटला, चांगला की वाईट?

## छान काम! तुमचे शिक्षण सुरू ठेवा

हा धडा पूर्ण केल्यानंतर, आमच्या [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) मध्ये जाऊन तुमचे Generative AI ज्ञान अधिक वाढवा!

पुढील धडा 6 मध्ये चला जिथे आपण Prompt Engineering चा वापर करून [टेक्स्ट जनरेशन अॅप्स तयार करू](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.