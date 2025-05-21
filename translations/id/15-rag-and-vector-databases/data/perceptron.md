<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T06:41:30+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "id"
}
-->
# Pengantar Jaringan Neural: Perceptron

Salah satu upaya pertama untuk mengimplementasikan sesuatu yang mirip dengan jaringan neural modern dilakukan oleh Frank Rosenblatt dari Cornell Aeronautical Laboratory pada tahun 1957. Ini adalah implementasi perangkat keras yang disebut "Mark-1", dirancang untuk mengenali bentuk geometris primitif, seperti segitiga, persegi, dan lingkaran.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Gambar dari Wikipedia

Gambar input diwakili oleh array fotocell 20x20, sehingga jaringan neural memiliki 400 input dan satu output biner. Jaringan sederhana ini mengandung satu neuron, yang juga disebut sebagai **unit logika ambang**. Bobot jaringan neural bertindak seperti potensiometer yang memerlukan penyesuaian manual selama fase pelatihan.

> ✅ Potensiometer adalah perangkat yang memungkinkan pengguna untuk menyesuaikan resistansi dari sebuah sirkuit.

> The New York Times menulis tentang perceptron pada saat itu: *embrio dari komputer elektronik yang [Angkatan Laut] harapkan akan dapat berjalan, berbicara, melihat, menulis, mereproduksi dirinya sendiri dan menyadari keberadaannya.*

## Model Perceptron

Misalkan kita memiliki N fitur dalam model kita, dalam hal ini vektor input akan menjadi vektor berukuran N. Perceptron adalah model **klasifikasi biner**, yaitu dapat membedakan antara dua kelas data input. Kita akan mengasumsikan bahwa untuk setiap vektor input x output dari perceptron kita akan menjadi +1 atau -1, tergantung pada kelasnya. Output akan dihitung menggunakan rumus:

y(x) = f(w<sup>T</sup>x)

di mana f adalah fungsi aktivasi langkah

## Melatih Perceptron

Untuk melatih perceptron, kita perlu menemukan vektor bobot w yang mengklasifikasikan sebagian besar nilai dengan benar, yaitu menghasilkan **kesalahan** terkecil. Kesalahan ini didefinisikan oleh **kriteria perceptron** dengan cara berikut:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

di mana:

* penjumlahan dilakukan pada titik data pelatihan i yang menghasilkan klasifikasi yang salah
* x<sub>i</sub> adalah data input, dan t<sub>i</sub> adalah -1 atau +1 untuk contoh negatif dan positif sesuai.

Kriteria ini dianggap sebagai fungsi dari bobot w, dan kita perlu meminimalkannya. Seringkali, metode yang disebut **gradient descent** digunakan, di mana kita memulai dengan beberapa bobot awal w<sup>(0)</sup>, dan kemudian pada setiap langkah memperbarui bobot sesuai dengan rumus:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Di sini η disebut sebagai **learning rate**, dan ∇E(w) menunjukkan **gradient** dari E. Setelah kita menghitung gradient, kita berakhir dengan

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritma dalam Python terlihat seperti ini:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## Kesimpulan

Dalam pelajaran ini, Anda telah mempelajari tentang perceptron, yang merupakan model klasifikasi biner, dan bagaimana melatihnya dengan menggunakan vektor bobot.

## 🚀 Tantangan

Jika Anda ingin mencoba membangun perceptron sendiri, coba lab ini di Microsoft Learn yang menggunakan Azure ML designer

## Tinjauan & Studi Mandiri

Untuk melihat bagaimana kita dapat menggunakan perceptron untuk memecahkan masalah mainan serta masalah nyata, dan untuk melanjutkan pembelajaran - pergi ke notebook Perceptron.

Berikut adalah artikel menarik tentang perceptron juga.

## Tugas

Dalam pelajaran ini, kita telah mengimplementasikan perceptron untuk tugas klasifikasi biner, dan kita telah menggunakannya untuk mengklasifikasikan antara dua digit tulisan tangan. Dalam lab ini, Anda diminta untuk memecahkan masalah klasifikasi digit sepenuhnya, yaitu menentukan digit mana yang paling mungkin sesuai dengan gambar yang diberikan.

* Instruksi
* Notebook

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan terjemahan yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi penting, disarankan untuk menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.