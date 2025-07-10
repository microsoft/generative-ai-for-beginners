<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:36:32+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "id"
}
-->

# Menghasilkan kode untuk Python Web API

Dalam panduan ini, kita akan membahas cara membuat kode untuk sebuah Web API menggunakan Python. Web API memungkinkan aplikasi Anda berkomunikasi dengan aplikasi lain melalui protokol HTTP.

## Langkah 1: Pilih framework

Python memiliki beberapa framework populer untuk membangun Web API, seperti Flask, FastAPI, dan Django REST Framework. Pilih framework yang sesuai dengan kebutuhan proyek Anda.

## Langkah 2: Instalasi

Instal framework yang dipilih menggunakan pip. Contoh untuk FastAPI:

```bash
pip install fastapi uvicorn
```

## Langkah 3: Buat endpoint dasar

Buat file Python baru dan tulis kode berikut untuk membuat endpoint dasar:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

## Langkah 4: Jalankan server

Jalankan server menggunakan uvicorn:

```bash
uvicorn main:app --reload
```

Server akan berjalan di `http://127.0.0.1:8000`. Anda dapat mengakses endpoint root dan melihat respons JSON.

## Langkah 5: Tambahkan endpoint lain

Tambahkan endpoint lain sesuai kebutuhan API Anda, misalnya endpoint untuk mengambil data, menambah data, memperbarui, atau menghapus data.

## Tips

[!TIP]  
Gunakan dokumentasi otomatis yang disediakan FastAPI dengan membuka `http://127.0.0.1:8000/docs` untuk melihat dan menguji API Anda secara interaktif.

## Kesimpulan

Membangun Web API dengan Python cukup mudah dengan bantuan framework yang tepat. Mulailah dengan membuat endpoint sederhana dan kembangkan sesuai kebutuhan aplikasi Anda.
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

Menjalankan prompt lagi memberikan hasil berikut:

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

Hanya ada perbedaan kecil antara kedua output ini. Kali ini, mari kita lakukan sebaliknya, atur temperature ke 0.9:

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

dan percobaan kedua dengan nilai temperature 0.9:

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

Seperti yang Anda lihat, hasilnya sangat bervariasi.

> Note, ada lebih banyak parameter yang bisa Anda ubah untuk memvariasikan output, seperti top-k, top-p, repetition penalty, length penalty, dan diversity penalty, tapi ini di luar cakupan kurikulum ini.

## Praktik Baik

Ada banyak praktik yang bisa Anda terapkan untuk mencoba mendapatkan hasil yang diinginkan. Anda akan menemukan gaya Anda sendiri seiring semakin sering menggunakan prompting.

Selain teknik yang sudah kita bahas, ada beberapa praktik baik yang perlu dipertimbangkan saat melakukan prompting pada LLM.

Berikut beberapa praktik baik yang perlu diperhatikan:

- **Tentukan konteks**. Konteks itu penting, semakin spesifik seperti domain, topik, dan lain-lain, hasilnya akan semakin baik.
- Batasi output. Jika Anda menginginkan jumlah item tertentu atau panjang tertentu, sebutkan secara spesifik.
- **Tentukan apa dan bagaimana**. Ingat untuk menyebutkan apa yang Anda inginkan dan bagaimana Anda menginginkannya, misalnya "Buat Python Web API dengan route products dan customers, bagi menjadi 3 file".
- **Gunakan template**. Seringkali, Anda ingin memperkaya prompt dengan data dari perusahaan Anda. Gunakan template untuk ini. Template bisa memiliki variabel yang Anda ganti dengan data sebenarnya.
- **Eja dengan benar**. LLM mungkin memberikan jawaban yang benar, tapi jika Anda mengeja dengan benar, Anda akan mendapatkan respons yang lebih baik.

## Tugas

Berikut kode Python yang menunjukkan cara membuat API sederhana menggunakan Flask:

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

Gunakan asisten AI seperti GitHub Copilot atau ChatGPT dan terapkan teknik "self-refine" untuk memperbaiki kode tersebut.

## Solusi

Silakan coba selesaikan tugas dengan menambahkan prompt yang sesuai pada kode.

> [!TIP]
> Buatlah prompt yang meminta perbaikan, ada baiknya membatasi berapa banyak perbaikan yang diinginkan. Anda juga bisa meminta perbaikan dalam aspek tertentu, misalnya arsitektur, performa, keamanan, dll.

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## Pemeriksaan Pengetahuan

Mengapa saya menggunakan chain-of-thought prompting? Tunjukkan 1 jawaban yang benar dan 2 jawaban yang salah.

1. Untuk mengajarkan LLM cara menyelesaikan masalah.
1. B, Untuk mengajarkan LLM menemukan kesalahan dalam kode.
1. C, Untuk menginstruksikan LLM menghasilkan solusi yang berbeda.

A: 1, karena chain-of-thought adalah tentang menunjukkan kepada LLM bagaimana menyelesaikan masalah dengan memberikan serangkaian langkah, serta masalah serupa dan bagaimana cara menyelesaikannya.

## 🚀 Tantangan

Anda baru saja menggunakan teknik self-refine dalam tugas. Ambil program apa pun yang sudah Anda buat dan pikirkan perbaikan apa yang ingin Anda terapkan. Sekarang gunakan teknik self-refine untuk menerapkan perubahan yang diusulkan. Bagaimana menurut Anda hasilnya, lebih baik atau lebih buruk?

## Kerja Bagus! Lanjutkan Pembelajaran Anda

Setelah menyelesaikan pelajaran ini, lihat koleksi [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Generative AI Anda!

Lanjut ke Lesson 6 di mana kita akan menerapkan pengetahuan Prompt Engineering dengan [membangun aplikasi text generation](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.