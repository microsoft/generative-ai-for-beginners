<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:36:56+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "ms"
}
-->

> "Hasilkan kod untuk API Web Python"
Menjalankan arahan sekali lagi memberikan kita hasil ini:

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

Hanya terdapat perbezaan kecil antara kedua-dua output ini. Kali ini, mari kita lakukan sebaliknya, tetapkan suhu kepada 0.9:

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

dan cubaan kedua pada nilai suhu 0.9:

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

Seperti yang anda lihat, hasilnya sangat berbeza-beza.

> Note, that there are more parameters you can change to vary the output, like top-k, top-p, repetition penalty, length penalty and diversity penalty but these are outside the scope of this curriculum.

## Amalan Baik

Terdapat banyak amalan yang boleh anda gunakan untuk cuba mendapatkan apa yang anda mahukan. Anda akan menemui gaya anda sendiri apabila anda semakin kerap menggunakan arahan.

Selain daripada teknik yang telah kita bincangkan, terdapat beberapa amalan baik yang perlu dipertimbangkan apabila memberi arahan kepada LLM.

Berikut adalah beberapa amalan baik yang perlu dipertimbangkan:

- **Nyatakan konteks**. Konteks adalah penting, lebih banyak anda boleh nyatakan seperti domain, topik, dan sebagainya, lebih baik.
- Hadkan output. Jika anda mahukan bilangan item tertentu atau panjang tertentu, nyatakan ia.
- **Nyatakan apa dan bagaimana**. Ingat untuk menyebut kedua-dua apa yang anda mahu dan bagaimana anda mahu ia, contohnya "Bina API Web Python dengan laluan products dan customers, bahagikan kepada 3 fail".
- **Gunakan templat**. Selalunya, anda akan mahu memperkayakan arahan anda dengan data dari syarikat anda. Gunakan templat untuk melakukan ini. Templat boleh mempunyai pembolehubah yang anda gantikan dengan data sebenar.
- **Eja dengan betul**. LLM mungkin memberikan jawapan yang betul, tetapi jika anda mengeja dengan betul, anda akan mendapat jawapan yang lebih baik.

## Tugasan

Berikut adalah kod dalam Python yang menunjukkan cara membina API ringkas menggunakan Flask:

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

Gunakan pembantu AI seperti GitHub Copilot atau ChatGPT dan gunakan teknik "self-refine" untuk memperbaiki kod tersebut.

## Penyelesaian

Sila cuba selesaikan tugasan dengan menambah arahan yang sesuai pada kod.

> [!TIP]
> Rangka ayat arahan untuk meminta penambahbaikan, adalah idea yang baik untuk mengehadkan berapa banyak penambahbaikan. Anda juga boleh minta untuk memperbaikinya dalam cara tertentu, contohnya seni bina, prestasi, keselamatan, dan sebagainya.

[Penyelesaian](../../../05-advanced-prompts/python/aoai-solution.py)

## Semakan Pengetahuan

Mengapa saya perlu menggunakan chain-of-thought prompting? Tunjukkan 1 jawapan betul dan 2 jawapan salah.

1. Untuk mengajar LLM cara menyelesaikan masalah.
1. B, Untuk mengajar LLM mencari kesilapan dalam kod.
1. C, Untuk mengarahkan LLM menghasilkan pelbagai penyelesaian.

A: 1, kerana chain-of-thought adalah tentang menunjukkan kepada LLM cara menyelesaikan masalah dengan memberikan satu siri langkah, dan masalah serupa serta cara ia diselesaikan.

## 🚀 Cabaran

Anda baru sahaja menggunakan teknik self-refine dalam tugasan. Ambil mana-mana program yang anda bina dan fikirkan penambahbaikan apa yang anda ingin lakukan. Sekarang gunakan teknik self-refine untuk melaksanakan perubahan yang dicadangkan. Apakah pendapat anda tentang hasilnya, lebih baik atau lebih teruk?

## Kerja Hebat! Teruskan Pembelajaran Anda

Selepas menamatkan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif anda!

Teruskan ke Pelajaran 6 di mana kita akan menggunakan pengetahuan Prompt Engineering dengan [membina aplikasi penjanaan teks](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.