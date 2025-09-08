<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T16:59:41+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "id"
}
-->
# Pengenalan Jaringan Syaraf Tiruan: Perceptron

Salah satu upaya pertama untuk mengimplementasikan sesuatu yang mirip dengan jaringan syaraf modern dilakukan oleh Frank Rosenblatt dari Cornell Aeronautical Laboratory pada tahun 1957. Ini adalah implementasi perangkat keras yang disebut "Mark-1", dirancang untuk mengenali bentuk geometris primitif, seperti segitiga, persegi, dan lingkaran.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Gambar dari Wikipedia

Gambar input direpresentasikan oleh array fotocell 20x20, sehingga jaringan syaraf memiliki 400 input dan satu output biner. Jaringan sederhana ini hanya terdiri dari satu neuron, yang juga disebut **threshold logic unit**. Bobot jaringan syaraf berfungsi seperti potensiometer yang perlu disesuaikan secara manual selama fase pelatihan.

> ✅ Potensiometer adalah perangkat yang memungkinkan pengguna mengatur resistansi sebuah rangkaian.

> The New York Times menulis tentang perceptron pada masa itu: *embrio dari komputer elektronik yang [Angkatan Laut] harapkan dapat berjalan, berbicara, melihat, menulis, mereproduksi dirinya sendiri, dan menyadari keberadaannya.*

## Model Perceptron

Misalkan kita memiliki N fitur dalam model kita, sehingga vektor input adalah vektor berukuran N. Perceptron adalah model **klasifikasi biner**, artinya dapat membedakan antara dua kelas data input. Kita asumsikan bahwa untuk setiap vektor input x, output perceptron kita adalah +1 atau -1, tergantung kelasnya. Output dihitung menggunakan rumus:

y(x) = f(w<sup>T</sup>x)

di mana f adalah fungsi aktivasi step

## Melatih Perceptron

Untuk melatih perceptron, kita perlu mencari vektor bobot w yang mengklasifikasikan sebagian besar nilai dengan benar, yaitu menghasilkan **error** terkecil. Error ini didefinisikan oleh **kriteria perceptron** sebagai berikut:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

di mana:

* jumlah diambil dari data pelatihan i yang menghasilkan klasifikasi salah
* x<sub>i</sub> adalah data input, dan t<sub>i</sub> adalah -1 atau +1 untuk contoh negatif dan positif secara berurutan.

Kriteria ini dianggap sebagai fungsi dari bobot w, dan kita perlu meminimalkannya. Seringkali, metode yang digunakan adalah **gradient descent**, di mana kita mulai dengan bobot awal w<sup>(0)</sup>, lalu pada setiap langkah memperbarui bobot sesuai rumus:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Di sini η adalah **learning rate**, dan ∇E(w) adalah **gradien** dari E. Setelah menghitung gradien, kita mendapatkan

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

Dalam pelajaran ini, Anda belajar tentang perceptron, yang merupakan model klasifikasi biner, dan bagaimana melatihnya menggunakan vektor bobot.

## 🚀 Tantangan

Jika Anda ingin mencoba membangun perceptron sendiri, coba lab ini di Microsoft Learn yang menggunakan Azure ML designer


## Review & Belajar Mandiri

Untuk melihat bagaimana kita dapat menggunakan perceptron untuk menyelesaikan masalah main-main maupun masalah nyata, dan untuk melanjutkan pembelajaran - kunjungi notebook Perceptron.

Berikut artikel menarik tentang perceptron juga.

## Tugas

Dalam pelajaran ini, kita telah mengimplementasikan perceptron untuk tugas klasifikasi biner, dan menggunakannya untuk mengklasifikasikan dua digit tulisan tangan. Dalam lab ini, Anda diminta untuk menyelesaikan masalah klasifikasi digit secara keseluruhan, yaitu menentukan digit mana yang paling mungkin sesuai dengan gambar yang diberikan.

* Instruksi
* Notebook

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.