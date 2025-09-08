<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:49:13+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "id"
}
-->
# Pengenalan Jaringan Syaraf Tiruan. Multi-Layered Perceptron

Pada bagian sebelumnya, Anda telah mempelajari model jaringan syaraf paling sederhana - perceptron satu lapis, sebuah model klasifikasi dua kelas linier.

Pada bagian ini kita akan mengembangkan model ini menjadi kerangka kerja yang lebih fleksibel, memungkinkan kita untuk:

* melakukan **klasifikasi multi-kelas** selain klasifikasi dua kelas
* menyelesaikan **masalah regresi** selain klasifikasi
* memisahkan kelas yang tidak dapat dipisahkan secara linier

Kita juga akan mengembangkan kerangka modular kita sendiri dalam Python yang memungkinkan kita membangun berbagai arsitektur jaringan syaraf.

## Formalisasi Pembelajaran Mesin

Mari kita mulai dengan memformalkan masalah Pembelajaran Mesin. Misalkan kita memiliki dataset pelatihan **X** dengan label **Y**, dan kita perlu membangun model *f* yang akan membuat prediksi paling akurat. Kualitas prediksi diukur dengan **fungsi Loss** ℒ. Fungsi loss berikut sering digunakan:

* Untuk masalah regresi, ketika kita perlu memprediksi sebuah angka, kita bisa menggunakan **absolute error** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, atau **squared error** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Untuk klasifikasi, kita menggunakan **0-1 loss** (yang pada dasarnya sama dengan **akurasi** model), atau **logistic loss**.

Untuk perceptron satu lapis, fungsi *f* didefinisikan sebagai fungsi linier *f(x)=wx+b* (di sini *w* adalah matriks bobot, *x* adalah vektor fitur input, dan *b* adalah vektor bias). Untuk arsitektur jaringan syaraf yang berbeda, fungsi ini bisa berbentuk lebih kompleks.

> Dalam kasus klasifikasi, seringkali diinginkan untuk mendapatkan probabilitas kelas yang sesuai sebagai output jaringan. Untuk mengubah angka sembarang menjadi probabilitas (misalnya untuk menormalkan output), kita sering menggunakan fungsi **softmax** σ, dan fungsi *f* menjadi *f(x)=σ(wx+b)*

Dalam definisi *f* di atas, *w* dan *b* disebut **parameter** θ=⟨*w,b*⟩. Diberikan dataset ⟨**X**,**Y**⟩, kita dapat menghitung total error pada seluruh dataset sebagai fungsi dari parameter θ.

> ✅ **Tujuan pelatihan jaringan syaraf adalah meminimalkan error dengan mengubah parameter θ**

## Optimasi Gradient Descent

Ada metode optimasi fungsi yang terkenal bernama **gradient descent**. Idenya adalah kita dapat menghitung turunan (dalam kasus multi-dimensi disebut **gradien**) dari fungsi loss terhadap parameter, dan mengubah parameter sedemikian rupa sehingga error akan berkurang. Ini dapat diformalkan sebagai berikut:

* Inisialisasi parameter dengan nilai acak w<sup>(0)</sup>, b<sup>(0)</sup>
* Ulangi langkah berikut berkali-kali:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Selama pelatihan, langkah optimasi seharusnya dihitung dengan mempertimbangkan seluruh dataset (ingat bahwa loss dihitung sebagai jumlah dari semua sampel pelatihan). Namun, dalam praktik kita mengambil sebagian kecil dataset yang disebut **minibatches**, dan menghitung gradien berdasarkan subset data tersebut. Karena subset diambil secara acak setiap kali, metode ini disebut **stochastic gradient descent** (SGD).

## Multi-Layered Perceptrons dan Backpropagation

Jaringan satu lapis, seperti yang telah kita lihat di atas, mampu mengklasifikasikan kelas yang dapat dipisahkan secara linier. Untuk membangun model yang lebih kaya, kita dapat menggabungkan beberapa lapisan jaringan. Secara matematis ini berarti fungsi *f* akan memiliki bentuk yang lebih kompleks, dan akan dihitung dalam beberapa langkah:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Di sini, α adalah **fungsi aktivasi non-linier**, σ adalah fungsi softmax, dan parameter θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritma gradient descent tetap sama, tetapi akan lebih sulit menghitung gradien. Dengan aturan rantai diferensiasi, kita dapat menghitung turunan sebagai:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Aturan rantai diferensiasi digunakan untuk menghitung turunan fungsi loss terhadap parameter.

Perhatikan bahwa bagian paling kiri dari semua ekspresi tersebut sama, sehingga kita dapat menghitung turunan secara efektif mulai dari fungsi loss dan berjalan "mundur" melalui grafik komputasi. Oleh karena itu metode pelatihan multi-layered perceptron disebut **backpropagation**, atau 'backprop'.



> TODO: image citation

> ✅ Kita akan membahas backprop dengan lebih detail dalam contoh notebook kita.  

## Kesimpulan

Dalam pelajaran ini, kita telah membangun perpustakaan jaringan syaraf kita sendiri, dan menggunakannya untuk tugas klasifikasi dua dimensi yang sederhana.

## 🚀 Tantangan

Dalam notebook pendamping, Anda akan mengimplementasikan kerangka kerja Anda sendiri untuk membangun dan melatih multi-layered perceptrons. Anda akan dapat melihat secara rinci bagaimana jaringan syaraf modern bekerja.

Lanjutkan ke notebook OwnFramework dan kerjakan di sana.



## Review & Belajar Mandiri

Backpropagation adalah algoritma umum yang digunakan dalam AI dan ML, layak untuk dipelajari lebih mendalam

## Tugas

Dalam lab ini, Anda diminta menggunakan kerangka kerja yang Anda bangun dalam pelajaran ini untuk menyelesaikan klasifikasi digit tulisan tangan MNIST.

* Instruksi
* Notebook

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.