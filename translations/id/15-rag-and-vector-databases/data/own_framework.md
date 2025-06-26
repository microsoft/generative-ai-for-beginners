<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:27:59+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "id"
}
-->
# Pengantar Jaringan Saraf. Perceptron Berlapis Ganda

Pada bagian sebelumnya, Anda telah mempelajari model jaringan saraf yang paling sederhana - perceptron satu lapis, sebuah model klasifikasi linear dua kelas.

Di bagian ini, kita akan memperluas model ini menjadi kerangka kerja yang lebih fleksibel, memungkinkan kita untuk:

* melakukan **klasifikasi multi-kelas** selain dua kelas
* menyelesaikan **masalah regresi** selain klasifikasi
* memisahkan kelas yang tidak dapat dipisahkan secara linear

Kita juga akan mengembangkan kerangka kerja modular kita sendiri dalam Python yang akan memungkinkan kita untuk membangun arsitektur jaringan saraf yang berbeda.

## Formalisasi Pembelajaran Mesin

Mari kita mulai dengan memformalisasi masalah Pembelajaran Mesin. Misalkan kita memiliki dataset pelatihan **X** dengan label **Y**, dan kita perlu membangun model *f* yang akan membuat prediksi paling akurat. Kualitas prediksi diukur dengan **fungsi kerugian** ℒ. Fungsi kerugian berikut sering digunakan:

* Untuk masalah regresi, ketika kita perlu memprediksi angka, kita dapat menggunakan **kesalahan absolut** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, atau **kesalahan kuadrat** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Untuk klasifikasi, kita menggunakan **kerugian 0-1** (yang pada dasarnya sama dengan **akurasi** model), atau **kerugian logistik**.

Untuk perceptron satu tingkat, fungsi *f* didefinisikan sebagai fungsi linear *f(x)=wx+b* (di sini *w* adalah matriks bobot, *x* adalah vektor fitur input, dan *b* adalah vektor bias). Untuk arsitektur jaringan saraf yang berbeda, fungsi ini dapat mengambil bentuk yang lebih kompleks.

> Dalam kasus klasifikasi, sering kali diinginkan untuk mendapatkan probabilitas kelas yang sesuai sebagai output jaringan. Untuk mengubah angka sembarang menjadi probabilitas (misalnya untuk menormalkan output), kita sering menggunakan fungsi **softmax** σ, dan fungsi *f* menjadi *f(x)=σ(wx+b)*

Dalam definisi *f* di atas, *w* dan *b* disebut **parameter** θ=⟨*w,b*⟩. Diberikan dataset ⟨**X**,**Y**⟩, kita dapat menghitung keseluruhan kesalahan pada seluruh dataset sebagai fungsi dari parameter θ.

> ✅ **Tujuan pelatihan jaringan saraf adalah meminimalkan kesalahan dengan memvariasikan parameter θ**

## Optimasi Penurunan Gradien

Ada metode optimasi fungsi yang terkenal yang disebut **penurunan gradien**. Idenya adalah kita dapat menghitung turunan (dalam kasus multi-dimensi disebut **gradien**) dari fungsi kerugian sehubungan dengan parameter, dan memvariasikan parameter sedemikian rupa sehingga kesalahan akan berkurang. Ini dapat diformalkan sebagai berikut:

* Inisialisasi parameter dengan beberapa nilai acak w<sup>(0)</sup>, b<sup>(0)</sup>
* Ulangi langkah berikut berkali-kali:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Selama pelatihan, langkah-langkah optimasi seharusnya dihitung dengan mempertimbangkan seluruh dataset (ingat bahwa kerugian dihitung sebagai jumlah melalui semua sampel pelatihan). Namun, dalam kehidupan nyata kita mengambil bagian kecil dari dataset yang disebut **minibatch**, dan menghitung gradien berdasarkan subset data. Karena subset diambil secara acak setiap kali, metode semacam itu disebut **penurunan gradien stokastik** (SGD).

## Perceptron Berlapis Ganda dan Backpropagation

Jaringan satu lapis, seperti yang telah kita lihat di atas, mampu mengklasifikasikan kelas yang dapat dipisahkan secara linear. Untuk membangun model yang lebih kaya, kita dapat menggabungkan beberapa lapisan jaringan. Secara matematis, ini berarti bahwa fungsi *f* akan memiliki bentuk yang lebih kompleks, dan akan dihitung dalam beberapa langkah:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Di sini, α adalah **fungsi aktivasi non-linear**, σ adalah fungsi softmax, dan parameter θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritma penurunan gradien akan tetap sama, tetapi akan lebih sulit untuk menghitung gradien. Berdasarkan aturan diferensiasi rantai, kita dapat menghitung turunan sebagai:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Aturan diferensiasi rantai digunakan untuk menghitung turunan dari fungsi kerugian terhadap parameter.

Perhatikan bahwa bagian paling kiri dari semua ekspresi tersebut adalah sama, dan dengan demikian kita dapat menghitung turunan secara efektif dimulai dari fungsi kerugian dan bergerak "mundur" melalui grafik komputasi. Oleh karena itu, metode pelatihan perceptron berlapis ganda disebut **backpropagation**, atau 'backprop'.

> TODO: kutipan gambar

> ✅ Kami akan membahas backprop dengan lebih detail dalam contoh notebook kami.

## Kesimpulan

Dalam pelajaran ini, kita telah membangun pustaka jaringan saraf kita sendiri, dan kita telah menggunakannya untuk tugas klasifikasi dua dimensi yang sederhana.

## 🚀 Tantangan

Dalam notebook yang menyertai, Anda akan mengimplementasikan kerangka kerja Anda sendiri untuk membangun dan melatih perceptron berlapis ganda. Anda akan dapat melihat secara detail bagaimana jaringan saraf modern beroperasi.

Lanjutkan ke notebook OwnFramework dan kerjakan.

## Tinjauan & Studi Mandiri

Backpropagation adalah algoritma umum yang digunakan dalam AI dan ML, layak untuk dipelajari lebih detail

## Tugas

Dalam lab ini, Anda diminta untuk menggunakan kerangka kerja yang Anda bangun dalam pelajaran ini untuk menyelesaikan klasifikasi digit tulisan tangan MNIST.

* Instruksi
* Notebook

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk mencapai akurasi, harap diingat bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.