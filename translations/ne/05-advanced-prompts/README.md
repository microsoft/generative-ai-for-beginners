<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:29:39+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "ne"
}
-->

> "Python वेब API को लागि कोड सिर्जना गर्नुहोस्"
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

फेरि प्रॉम्प्ट चलाउँदा हामीलाई यो नतिजा प्राप्त हुन्छ:

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

यी दुई नतिजाबीच सानो मात्र फरक छ। यसपटक उल्टो गरौं, तापक्रमलाई ०.९ मा सेट गरौं:

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

र दोस्रो प्रयास तापक्रम मान ०.९ मा:

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

जसरी देख्न सकिन्छ, नतिजाहरू धेरै फरक-फरक छन्।

> [!NOTE] त्यहाँ अरू धेरै प्यारामिटरहरू छन् जुन तपाईंले नतिजा फरक बनाउन परिवर्तन गर्न सक्नुहुन्छ, जस्तै top-k, top-p, repetition penalty, length penalty र diversity penalty तर यी यस पाठ्यक्रमको दायराभन्दा बाहिर छन्।

## राम्रो अभ्यासहरू

तपाईंले चाहेको नतिजा पाउन प्रयास गर्दा धेरै अभ्यासहरू लागू गर्न सक्नुहुन्छ। तपाईंले प्रॉम्प्टिङ बढी प्रयोग गर्दा आफ्नो शैली पत्ता लगाउनुहुनेछ।

हामीले समेटेका प्रविधिहरू बाहेक, LLM लाई प्रॉम्प्ट गर्दा विचार गर्नुपर्ने केही राम्रो अभ्यासहरू छन्।

यहाँ केही राम्रो अभ्यासहरू छन्:

- **सन्दर्भ स्पष्ट गर्नुहोस्**। सन्दर्भ महत्वपूर्ण हुन्छ, तपाईंले जति सक्नुहुन्छ डोमेन, विषय आदि जस्ता कुरा स्पष्ट गर्नुहोस्, उत्तम हुन्छ।
- नतिजा सीमित गर्नुहोस्। यदि तपाईंलाई निश्चित संख्या वा निश्चित लम्बाइको नतिजा चाहिन्छ भने, त्यसलाई स्पष्ट गर्नुहोस्।
- **के र कसरी दुवै स्पष्ट गर्नुहोस्**। तपाईंले के चाहनुहुन्छ र कसरी चाहनुहुन्छ दुवै उल्लेख गर्न नबिर्सनुहोस्, उदाहरणका लागि "routes products र customers सहित Python Web API बनाउनुहोस्, र यसलाई ३ फाइलमा विभाजन गर्नुहोस्"।
- **टेम्प्लेटहरू प्रयोग गर्नुहोस्**। प्रायः तपाईंले आफ्नो कम्पनीको डाटाबाट प्रॉम्प्टलाई समृद्ध बनाउन चाहनुहुन्छ। यसका लागि टेम्प्लेटहरू प्रयोग गर्नुहोस्। टेम्प्लेटहरूमा भेरिएबलहरू हुन्छन् जुन तपाईं वास्तविक डाटाले प्रतिस्थापन गर्नुहुन्छ।
- **सही वर्तनी प्रयोग गर्नुहोस्**। LLM ले सही जवाफ दिन सक्छ, तर तपाईंले सही वर्तनी प्रयोग गर्दा अझ राम्रो जवाफ पाउनुहुनेछ।

## कार्य

यहाँ Python मा Flask प्रयोग गरी सरल API कसरी बनाउने देखाइएको छ:

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

GitHub Copilot वा ChatGPT जस्ता AI सहायक प्रयोग गरी "self-refine" प्रविधि लागू गरेर कोड सुधार गर्नुहोस्।

## समाधान

कृपया उपयुक्त प्रॉम्प्टहरू थपेर कार्य समाधान गर्ने प्रयास गर्नुहोस्।

> [!TIP]
> सुधार गर्न प्रॉम्प्ट तयार पार्नुहोस्, सुधारहरूको संख्या सीमित गर्नु राम्रो हुन्छ। तपाईंले विशेष तरिकाले सुधार गर्न पनि भन्न सक्नुहुन्छ, जस्तै आर्किटेक्चर, प्रदर्शन, सुरक्षा आदि।

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## ज्ञान जाँच

म किन chain-of-thought प्रॉम्प्टिङ प्रयोग गर्ने? मलाई १ सही जवाफ र २ गलत जवाफ देखाउनुहोस्।

1. LLM लाई समस्या समाधान गर्ने तरिका सिकाउन।
1. B, LLM लाई कोडमा त्रुटि खोज्न सिकाउन।
1. C, LLM लाई विभिन्न समाधानहरू सोच्न निर्देशन दिन।

उत्तर: १, किनभने chain-of-thought भनेको LLM लाई समस्या समाधान गर्ने तरिका देखाउनु हो, जसमा चरणहरू र समान समस्याहरू कसरी समाधान गरियो भन्ने कुरा समावेश हुन्छ।

## 🚀 चुनौती

तपाईंले कार्यमा self-refine प्रविधि प्रयोग गर्नुभयो। तपाईंले बनाएको कुनै पनि प्रोग्राम लिएर त्यसमा के सुधारहरू गर्न चाहनुहुन्छ भनेर विचार गर्नुहोस्। अब self-refine प्रविधि प्रयोग गरी प्रस्तावित परिवर्तनहरू लागू गर्नुहोस्। तपाईंलाई नतिजा कस्तो लाग्यो, राम्रो कि नराम्रो?

## उत्कृष्ट काम! आफ्नो सिकाइ जारी राख्नुहोस्

यो पाठ पूरा गरेपछि, हाम्रो [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) हेर्नुहोस् र Generative AI को ज्ञान अझ बढाउनुहोस्!

अब Lesson 6 मा जानुहोस् जहाँ हामी Prompt Engineering को ज्ञान प्रयोग गरी [टेक्स्ट जेनेरेसन एपहरू बनाउने](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst) छौं।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।