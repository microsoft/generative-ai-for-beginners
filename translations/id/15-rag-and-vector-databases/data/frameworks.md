<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:34:48+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "id"
}
-->
# Neural Network Frameworks

Seperti yang sudah kita pelajari, untuk dapat melatih neural network secara efisien kita perlu melakukan dua hal:

* Mengoperasikan tensor, misalnya mengalikan, menjumlahkan, dan menghitung beberapa fungsi seperti sigmoid atau softmax
* Menghitung gradien dari semua ekspresi, untuk melakukan optimisasi dengan gradient descent

Meskipun library `numpy` dapat melakukan bagian pertama, kita membutuhkan mekanisme untuk menghitung gradien. Dalam framework yang telah kita kembangkan di bagian sebelumnya, kita harus memprogram semua fungsi turunan secara manual di dalam metode `backward`, yang melakukan backpropagation. Idealnya, sebuah framework harus memberikan kesempatan untuk menghitung gradien dari *ekspresi apapun* yang bisa kita definisikan.

Hal penting lainnya adalah kemampuan melakukan komputasi di GPU, atau unit komputasi khusus lainnya, seperti TPU. Pelatihan deep neural network membutuhkan *banyak* komputasi, dan kemampuan untuk memparalelkan komputasi tersebut di GPU sangatlah penting.

> ✅ Istilah 'memparalelkan' berarti mendistribusikan komputasi ke beberapa perangkat.

Saat ini, dua framework neural network yang paling populer adalah: TensorFlow dan PyTorch. Keduanya menyediakan API tingkat rendah untuk mengoperasikan tensor di CPU maupun GPU. Di atas API tingkat rendah, juga ada API tingkat tinggi, yang disebut Keras dan PyTorch Lightning secara berurutan.

Low-Level API | TensorFlow | PyTorch  
--------------|-------------------------------|------------------------------  
High-level API| Keras | PyTorch

**API tingkat rendah** di kedua framework memungkinkan Anda membangun yang disebut **computational graphs**. Graph ini mendefinisikan bagaimana menghitung output (biasanya fungsi loss) dengan parameter input yang diberikan, dan dapat dijalankan di GPU jika tersedia. Ada fungsi untuk mendiferensiasi computational graph ini dan menghitung gradien, yang kemudian dapat digunakan untuk mengoptimalkan parameter model.

**API tingkat tinggi** lebih memandang neural network sebagai **rangkaian layer**, dan membuat konstruksi sebagian besar neural network menjadi jauh lebih mudah. Melatih model biasanya hanya perlu menyiapkan data dan kemudian memanggil fungsi `fit` untuk menjalankan proses pelatihan.

API tingkat tinggi memungkinkan Anda membangun neural network tipikal dengan cepat tanpa harus memikirkan banyak detail. Sementara itu, API tingkat rendah menawarkan kontrol lebih besar atas proses pelatihan, sehingga sering digunakan dalam riset, terutama saat Anda berhadapan dengan arsitektur neural network baru.

Penting juga untuk memahami bahwa Anda bisa menggunakan kedua API ini secara bersamaan, misalnya Anda bisa mengembangkan arsitektur layer jaringan Anda sendiri menggunakan API tingkat rendah, lalu menggunakannya di dalam jaringan yang lebih besar yang dibangun dan dilatih dengan API tingkat tinggi. Atau Anda bisa mendefinisikan jaringan menggunakan API tingkat tinggi sebagai rangkaian layer, lalu menggunakan loop pelatihan tingkat rendah Anda sendiri untuk melakukan optimisasi. Kedua API menggunakan konsep dasar yang sama, dan dirancang agar bisa bekerja dengan baik bersama.

## Pembelajaran

Dalam kursus ini, kami menyediakan sebagian besar konten untuk PyTorch dan TensorFlow. Anda bisa memilih framework yang Anda sukai dan hanya mengikuti notebook yang sesuai. Jika Anda belum yakin memilih framework mana, baca beberapa diskusi di internet mengenai **PyTorch vs. TensorFlow**. Anda juga bisa melihat kedua framework untuk mendapatkan pemahaman yang lebih baik.

Jika memungkinkan, kami akan menggunakan API Tingkat Tinggi untuk kesederhanaan. Namun, kami percaya penting untuk memahami cara kerja neural network dari dasar, sehingga di awal kita mulai dengan bekerja menggunakan API tingkat rendah dan tensor. Namun, jika Anda ingin cepat memulai dan tidak ingin menghabiskan banyak waktu mempelajari detail ini, Anda bisa melewati bagian tersebut dan langsung ke notebook API tingkat tinggi.

## ✍️ Latihan: Frameworks

Lanjutkan pembelajaran Anda di notebook berikut:

Low-Level API | TensorFlow+Keras Notebook | PyTorch  
--------------|-------------------------------|------------------------------  
High-level API| Keras | *PyTorch Lightning*

Setelah menguasai framework, mari kita ulas kembali konsep overfitting.

# Overfitting

Overfitting adalah konsep yang sangat penting dalam machine learning, dan sangat penting untuk memahaminya dengan benar!

Pertimbangkan masalah berikut dalam mengaproksimasi 5 titik (diwakili oleh `x` pada grafik di bawah):

!linear | overfit  
-------------------------|--------------------------  
**Model linear, 2 parameter** | **Model non-linear, 7 parameter**  
Error pelatihan = 5.3 | Error pelatihan = 0  
Error validasi = 5.1 | Error validasi = 20

* Di sebelah kiri, kita melihat aproksimasi garis lurus yang baik. Karena jumlah parameter cukup, model dapat menangkap pola distribusi titik dengan benar.  
* Di sebelah kanan, model terlalu kuat. Karena kita hanya memiliki 5 titik dan model memiliki 7 parameter, model dapat menyesuaikan sedemikian rupa sehingga melewati semua titik, membuat error pelatihan menjadi 0. Namun, ini membuat model gagal memahami pola yang benar di balik data, sehingga error validasi sangat tinggi.

Sangat penting untuk menemukan keseimbangan yang tepat antara kompleksitas model (jumlah parameter) dan jumlah sampel pelatihan.

## Mengapa overfitting terjadi

  * Data pelatihan tidak cukup banyak  
  * Model terlalu kompleks  
  * Terlalu banyak noise pada data input

## Cara mendeteksi overfitting

Seperti yang terlihat pada grafik di atas, overfitting dapat dideteksi dari error pelatihan yang sangat rendah, dan error validasi yang tinggi. Biasanya selama pelatihan kita akan melihat error pelatihan dan validasi sama-sama menurun, lalu pada titik tertentu error validasi mungkin berhenti menurun dan mulai naik. Ini adalah tanda overfitting, dan indikator bahwa kita sebaiknya menghentikan pelatihan pada titik ini (atau setidaknya membuat snapshot model).

overfitting

## Cara mencegah overfitting

Jika Anda melihat overfitting terjadi, Anda bisa melakukan salah satu hal berikut:

 * Menambah jumlah data pelatihan  
 * Mengurangi kompleksitas model  
 * Menggunakan teknik regularisasi, seperti Dropout, yang akan kita bahas nanti.

## Overfitting dan Bias-Variance Tradeoff

Overfitting sebenarnya adalah kasus dari masalah yang lebih umum dalam statistik yang disebut Bias-Variance Tradeoff. Jika kita melihat sumber kesalahan dalam model kita, kita dapat membedakan dua jenis kesalahan:

* **Bias error** disebabkan oleh algoritma kita yang tidak mampu menangkap hubungan dalam data pelatihan dengan benar. Ini bisa terjadi karena model kita tidak cukup kuat (**underfitting**).  
* **Variance error**, yang disebabkan oleh model yang mengaproksimasi noise dalam data input daripada hubungan yang bermakna (**overfitting**).

Selama pelatihan, bias error menurun (karena model belajar mengaproksimasi data), dan variance error meningkat. Penting untuk menghentikan pelatihan - baik secara manual (ketika kita mendeteksi overfitting) atau otomatis (dengan memperkenalkan regularisasi) - untuk mencegah overfitting.

## Kesimpulan

Dalam pelajaran ini, Anda telah belajar tentang perbedaan berbagai API untuk dua framework AI paling populer, TensorFlow dan PyTorch. Selain itu, Anda juga mempelajari topik yang sangat penting, yaitu overfitting.

## 🚀 Tantangan

Di notebook pendamping, Anda akan menemukan 'tugas' di bagian bawah; kerjakan notebook tersebut dan selesaikan tugas-tugasnya.

## Review & Belajar Mandiri

Lakukan riset tentang topik berikut:

- TensorFlow  
- PyTorch  
- Overfitting

Tanyakan pada diri Anda pertanyaan berikut:

- Apa perbedaan antara TensorFlow dan PyTorch?  
- Apa perbedaan antara overfitting dan underfitting?

## Tugas

Dalam lab ini, Anda diminta untuk menyelesaikan dua masalah klasifikasi menggunakan jaringan fully-connected satu dan multi-layer dengan PyTorch atau TensorFlow.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.