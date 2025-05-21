<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T06:41:44+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "ms"
}
-->
# Pengenalan kepada Rangkaian Neural: Perceptron

Salah satu percubaan pertama untuk melaksanakan sesuatu yang serupa dengan rangkaian neural moden telah dilakukan oleh Frank Rosenblatt dari Cornell Aeronautical Laboratory pada tahun 1957. Ia adalah pelaksanaan perkakasan yang dipanggil "Mark-1", direka untuk mengenali bentuk geometri primitif, seperti segitiga, segi empat dan bulatan.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Imej dari Wikipedia

Imej input diwakili oleh susunan fotocell 20x20, jadi rangkaian neural mempunyai 400 input dan satu output binari. Rangkaian mudah mengandungi satu neuron, juga dipanggil **unit logik ambang**. Berat rangkaian neural bertindak seperti potensiometer yang memerlukan pelarasan manual semasa fasa latihan.

> ✅ Potensiometer ialah peranti yang membolehkan pengguna melaraskan rintangan litar.

> The New York Times menulis tentang perceptron pada masa itu: *embrio komputer elektronik yang [Tentera Laut] jangkakan akan dapat berjalan, bercakap, melihat, menulis, membiak sendiri dan sedar akan kewujudannya.*

## Model Perceptron

Katakan kita mempunyai N ciri dalam model kita, dalam hal ini vektor input akan menjadi vektor bersaiz N. Perceptron ialah model **pengelasan binari**, iaitu ia boleh membezakan antara dua kelas data input. Kami akan mengandaikan bahawa untuk setiap vektor input x output perceptron kami akan sama ada +1 atau -1, bergantung pada kelas. Output akan dikira menggunakan formula:

y(x) = f(w<sup>T</sup>x)

di mana f ialah fungsi pengaktifan langkah

## Melatih Perceptron

Untuk melatih perceptron kita perlu mencari vektor berat w yang mengelaskan kebanyakan nilai dengan betul, iaitu menghasilkan **ralat** yang paling kecil. Ralat ini ditakrifkan oleh **kriteria perceptron** dengan cara berikut:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

di mana:

* jumlah diambil pada titik data latihan i yang mengakibatkan pengelasan salah
* x<sub>i</sub> ialah data input, dan t<sub>i</sub> sama ada -1 atau +1 untuk contoh negatif dan positif mengikut keperluan.

Kriteria ini dianggap sebagai fungsi berat w, dan kita perlu meminimumkannya. Selalunya, kaedah yang dipanggil **kecerunan menurun** digunakan, di mana kita bermula dengan beberapa berat awal w<sup>(0)</sup>, dan kemudian pada setiap langkah mengemas kini berat mengikut formula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Di sini η dipanggil **kadar pembelajaran**, dan ∇E(w) menandakan **kecerunan** E. Selepas kita mengira kecerunan, kita akan mendapat

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

Dalam pelajaran ini, anda telah belajar tentang perceptron, yang merupakan model pengelasan binari, dan cara melatihnya dengan menggunakan vektor berat.

## 🚀 Cabaran

Jika anda ingin mencuba membina perceptron anda sendiri, cuba makmal ini di Microsoft Learn yang menggunakan pereka Azure ML

## Kajian & Pembelajaran Kendiri

Untuk melihat bagaimana kita boleh menggunakan perceptron untuk menyelesaikan masalah mainan serta masalah kehidupan sebenar, dan untuk terus belajar - pergi ke buku nota Perceptron.

Berikut adalah artikel menarik tentang perceptrons juga.

## Tugasan

Dalam pelajaran ini, kami telah melaksanakan perceptron untuk tugas pengelasan binari, dan kami telah menggunakannya untuk mengelaskan antara dua digit tulisan tangan. Dalam makmal ini, anda diminta untuk menyelesaikan masalah pengelasan digit sepenuhnya, iaitu menentukan digit mana yang paling mungkin sepadan dengan imej yang diberikan.

* Arahan
* Buku nota

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.