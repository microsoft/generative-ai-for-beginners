<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T16:59:52+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "ms"
}
-->
# Pengenalan kepada Rangkaian Neural: Perceptron

Salah satu percubaan pertama untuk melaksanakan sesuatu yang serupa dengan rangkaian neural moden dilakukan oleh Frank Rosenblatt dari Cornell Aeronautical Laboratory pada tahun 1957. Ia adalah pelaksanaan perkakasan yang dipanggil "Mark-1", direka untuk mengenal pasti bentuk geometri primitif, seperti segitiga, segi empat dan bulatan.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Imej dari Wikipedia

Imej input diwakili oleh susunan fotosit 20x20, jadi rangkaian neural mempunyai 400 input dan satu output binari. Rangkaian ringkas mengandungi satu neuron, juga dipanggil **unit logik ambang**. Berat rangkaian neural bertindak seperti potensiometer yang memerlukan pelarasan manual semasa fasa latihan.

> ✅ Potensiometer adalah peranti yang membolehkan pengguna melaraskan rintangan dalam litar.

> The New York Times menulis tentang perceptron pada masa itu: *embrio komputer elektronik yang [Tentera Laut] jangka boleh berjalan, bercakap, melihat, menulis, membiak sendiri dan sedar akan kewujudannya.*

## Model Perceptron

Andaikan kita mempunyai N ciri dalam model kita, dalam kes ini vektor input adalah vektor bersaiz N. Perceptron adalah model **klasifikasi binari**, iaitu ia boleh membezakan antara dua kelas data input. Kita akan anggap bahawa untuk setiap vektor input x, output perceptron kita adalah sama ada +1 atau -1, bergantung pada kelas. Output akan dikira menggunakan formula:

y(x) = f(w<sup>T</sup>x)

di mana f adalah fungsi pengaktifan langkah

## Melatih Perceptron

Untuk melatih perceptron, kita perlu mencari vektor berat w yang mengklasifikasikan kebanyakan nilai dengan betul, iaitu menghasilkan **ralat** yang paling kecil. Ralat ini ditakrifkan oleh **kriteria perceptron** dengan cara berikut:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

di mana:

* jumlah diambil pada data latihan i yang menghasilkan klasifikasi yang salah
* x<sub>i</sub> adalah data input, dan t<sub>i</sub> adalah sama ada -1 atau +1 untuk contoh negatif dan positif masing-masing.

Kriteria ini dianggap sebagai fungsi berat w, dan kita perlu meminimumkannya. Selalunya, kaedah yang dipanggil **penurunan kecerunan** digunakan, di mana kita bermula dengan beberapa berat awal w<sup>(0)</sup>, dan kemudian pada setiap langkah mengemas kini berat mengikut formula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Di sini η adalah **kadar pembelajaran**, dan ∇E(w) menunjukkan **kecerunan** E. Selepas kita mengira kecerunan, kita akan mendapat

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritma dalam Python kelihatan seperti ini:

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

Dalam pelajaran ini, anda telah belajar tentang perceptron, yang merupakan model klasifikasi binari, dan bagaimana melatihnya menggunakan vektor berat.

## 🚀 Cabaran

Jika anda ingin mencuba membina perceptron anda sendiri, cuba makmal ini di Microsoft Learn yang menggunakan Azure ML designer


## Ulasan & Belajar Sendiri

Untuk melihat bagaimana kita boleh menggunakan perceptron untuk menyelesaikan masalah mainan serta masalah kehidupan sebenar, dan untuk terus belajar - pergi ke buku nota Perceptron.

Berikut adalah artikel menarik tentang perceptron juga.

## Tugasan

Dalam pelajaran ini, kita telah melaksanakan perceptron untuk tugasan klasifikasi binari, dan kita telah menggunakannya untuk mengklasifikasikan antara dua digit tulisan tangan. Dalam makmal ini, anda diminta untuk menyelesaikan masalah klasifikasi digit sepenuhnya, iaitu menentukan digit mana yang paling mungkin sepadan dengan imej yang diberikan.

* Arahan
* Buku nota

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.