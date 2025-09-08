<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:33:12+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "th"
}
-->

> "สร้างโค้ดสำหรับ Python Web API"
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

การรัน prompt อีกครั้งให้ผลลัพธ์ดังนี้:

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

ผลลัพธ์ทั้งสองนี้มีความแตกต่างกันเพียงเล็กน้อย คราวนี้ลองทำในทางตรงกันข้าม โดยตั้งค่า temperature เป็น 0.9:

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

และการลองครั้งที่สองโดยใช้ค่า temperature 0.9:

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

อย่างที่เห็น ผลลัพธ์มีความหลากหลายอย่างมาก

> Note, that there are more parameters you can change to vary the output, like top-k, top-p, repetition penalty, length penalty and diversity penalty but these are outside the scope of this curriculum.

## แนวปฏิบัติที่ดี

มีแนวทางมากมายที่คุณสามารถใช้เพื่อพยายามให้ได้ผลลัพธ์ตามที่ต้องการ คุณจะค้นพบสไตล์ของตัวเองเมื่อใช้ prompting บ่อยขึ้นเรื่อยๆ

นอกจากเทคนิคที่เราได้กล่าวถึงแล้ว ยังมีแนวปฏิบัติที่ดีบางอย่างที่ควรพิจารณาเมื่อทำ prompting กับ LLM

นี่คือแนวปฏิบัติที่ดีที่ควรพิจารณา:

- **ระบุบริบท** บริบทมีความสำคัญ ยิ่งคุณระบุได้มาก เช่น ด้านความรู้ หัวข้อ ฯลฯ ยิ่งดี
- จำกัดผลลัพธ์ หากคุณต้องการจำนวนรายการหรือความยาวที่เจาะจง ให้ระบุไว้
- **ระบุทั้งสิ่งที่ต้องการและวิธีการ** จำไว้ว่าต้องบอกทั้งสิ่งที่ต้องการและวิธีการ เช่น "สร้าง Python Web API ที่มี routes สำหรับ products และ customers แบ่งเป็น 3 ไฟล์"
- **ใช้เทมเพลต** บ่อยครั้งคุณจะต้องเสริม prompt ด้วยข้อมูลจากบริษัทของคุณ ใช้เทมเพลตเพื่อทำสิ่งนี้ เทมเพลตสามารถมีตัวแปรที่คุณแทนที่ด้วยข้อมูลจริง
- **สะกดให้ถูกต้อง** LLM อาจให้คำตอบที่ถูกต้อง แต่ถ้าคุณสะกดถูกต้อง คุณจะได้คำตอบที่ดียิ่งขึ้น

## การบ้าน

นี่คือโค้ด Python ที่แสดงวิธีสร้าง API ง่ายๆ โดยใช้ Flask:

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

ใช้ผู้ช่วย AI เช่น GitHub Copilot หรือ ChatGPT และใช้เทคนิค "self-refine" เพื่อปรับปรุงโค้ดนี้

## ตัวอย่างคำตอบ

โปรดลองแก้โจทย์โดยเพิ่ม prompt ที่เหมาะสมลงในโค้ด

> [!TIP]
> ตั้งคำถามเพื่อขอให้ปรับปรุงโค้ด ควรจำกัดจำนวนการปรับปรุงที่ต้องการ คุณยังสามารถขอให้ปรับปรุงในด้านใดด้านหนึ่ง เช่น สถาปัตยกรรม ประสิทธิภาพ ความปลอดภัย ฯลฯ

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## ตรวจสอบความเข้าใจ

ทำไมจึงควรใช้ chain-of-thought prompting? ยกตัวอย่างคำตอบที่ถูกต้อง 1 ข้อ และคำตอบที่ผิด 2 ข้อ

1. เพื่อสอน LLM วิธีแก้ปัญหา
1. B, เพื่อสอน LLM ให้หาข้อผิดพลาดในโค้ด
1. C, เพื่อสั่งให้ LLM คิดหาวิธีแก้ปัญหาหลายๆ แบบ

คำตอบ: 1 เพราะ chain-of-thought คือการแสดงให้ LLM เห็นวิธีแก้ปัญหาโดยให้ขั้นตอนต่างๆ และปัญหาที่คล้ายกันพร้อมวิธีแก้

## 🚀 ความท้าทาย

คุณเพิ่งใช้เทคนิค self-refine ในการบ้าน ลองนำโปรแกรมที่คุณเขียนขึ้นมาสักโปรแกรมหนึ่ง แล้วพิจารณาว่าคุณอยากปรับปรุงอะไรบ้าง จากนั้นใช้เทคนิค self-refine เพื่อปรับเปลี่ยนตามที่เสนอ ผลลัพธ์เป็นอย่างไร ดีขึ้นหรือแย่ลง?

## ทำได้ดีมาก! เรียนรู้ต่อไป

หลังจากจบบทเรียนนี้แล้ว ลองดู [คอลเลกชันการเรียนรู้ Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) เพื่อพัฒนาความรู้ด้าน Generative AI ของคุณต่อไป!

ไปที่บทเรียนที่ 6 ซึ่งเราจะนำความรู้เรื่อง Prompt Engineering ไปใช้โดยการ [สร้างแอปพลิเคชันสร้างข้อความ](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้