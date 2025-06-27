<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:07:18+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "id"
}
-->
# Kerangka Jaringan Saraf

Seperti yang telah kita pelajari, untuk dapat melatih jaringan saraf secara efisien kita perlu melakukan dua hal:

* Mengoperasikan tensor, misalnya mengalikan, menambah, dan menghitung beberapa fungsi seperti sigmoid atau softmax
* Menghitung gradien dari semua ekspresi, untuk melakukan optimasi penurunan gradien

Sementara perpustakaan `numpy` dapat melakukan bagian pertama, kita memerlukan beberapa mekanisme untuk menghitung gradien. Dalam kerangka kerja yang telah kita kembangkan di bagian sebelumnya, kita harus memprogram semua fungsi turunan secara manual di dalam metode `backward`, yang melakukan backpropagation. Idealnya, sebuah kerangka kerja harus memberi kita kesempatan untuk menghitung gradien dari *ekspresi apapun* yang dapat kita definisikan.

Hal penting lainnya adalah dapat melakukan komputasi pada GPU, atau unit komputasi khusus lainnya, seperti TPU. Pelatihan jaringan saraf dalam membutuhkan *banyak* komputasi, dan dapat memparalelkan komputasi tersebut pada GPU sangat penting.

> ✅ Istilah 'memparalelkan' berarti mendistribusikan komputasi ke beberapa perangkat.

Saat ini, dua kerangka jaringan saraf yang paling populer adalah: TensorFlow dan PyTorch. Keduanya menyediakan API tingkat rendah untuk beroperasi dengan tensor baik pada CPU maupun GPU. Di atas API tingkat rendah, ada juga API tingkat tinggi, yang disebut Keras dan PyTorch Lightning secara berturut-turut.

API Tingkat Rendah | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
API Tingkat Tinggi| Keras| Pytorch

**API tingkat rendah** dalam kedua kerangka memungkinkan Anda membangun apa yang disebut **graf komputasi**. Graf ini mendefinisikan bagaimana menghitung output (biasanya fungsi kerugian) dengan parameter input yang diberikan, dan dapat didorong untuk komputasi pada GPU, jika tersedia. Ada fungsi untuk membedakan graf komputasi ini dan menghitung gradien, yang kemudian dapat digunakan untuk mengoptimalkan parameter model.

**API tingkat tinggi** pada dasarnya menganggap jaringan saraf sebagai **urutan lapisan**, dan membuat konstruksi sebagian besar jaringan saraf menjadi lebih mudah. Melatih model biasanya memerlukan persiapan data dan kemudian memanggil fungsi `fit` untuk melakukan tugasnya.

API tingkat tinggi memungkinkan Anda membangun jaringan saraf tipikal dengan sangat cepat tanpa khawatir tentang banyak detail. Pada saat yang sama, API tingkat rendah menawarkan lebih banyak kontrol atas proses pelatihan, dan oleh karena itu sering digunakan dalam penelitian, ketika Anda berurusan dengan arsitektur jaringan saraf baru.

Penting juga untuk memahami bahwa Anda dapat menggunakan kedua API bersama-sama, misalnya Anda dapat mengembangkan arsitektur lapisan jaringan Anda sendiri menggunakan API tingkat rendah, dan kemudian menggunakannya di dalam jaringan yang lebih besar yang dibangun dan dilatih dengan API tingkat tinggi. Atau Anda dapat mendefinisikan jaringan menggunakan API tingkat tinggi sebagai urutan lapisan, dan kemudian menggunakan loop pelatihan tingkat rendah Anda sendiri untuk melakukan optimasi. Kedua API menggunakan konsep dasar yang sama, dan dirancang untuk bekerja dengan baik bersama.

## Pembelajaran

Dalam kursus ini, kami menawarkan sebagian besar konten baik untuk PyTorch maupun TensorFlow. Anda dapat memilih kerangka kerja yang Anda sukai dan hanya melalui notebook yang sesuai. Jika Anda tidak yakin kerangka kerja mana yang harus dipilih, bacalah beberapa diskusi di internet mengenai **PyTorch vs. TensorFlow**. Anda juga dapat melihat kedua kerangka kerja untuk mendapatkan pemahaman yang lebih baik.

Di mana mungkin, kami akan menggunakan API Tingkat Tinggi untuk kesederhanaan. Namun, kami percaya penting untuk memahami bagaimana jaringan saraf bekerja dari dasar, sehingga pada awalnya kami mulai dengan bekerja dengan API tingkat rendah dan tensor. Namun, jika Anda ingin memulai dengan cepat dan tidak ingin menghabiskan banyak waktu untuk mempelajari detail ini, Anda dapat melewati bagian tersebut dan langsung ke notebook API tingkat tinggi.

## ✍️ Latihan: Kerangka Kerja

Lanjutkan pembelajaran Anda di notebook berikut:

API Tingkat Rendah | Notebook TensorFlow+Keras | PyTorch
--------------|-------------------------------------|--------------------------------
API Tingkat Tinggi| Keras | *PyTorch Lightning*

Setelah menguasai kerangka kerja, mari kita ulas kembali konsep overfitting.

# Overfitting

Overfitting adalah konsep yang sangat penting dalam pembelajaran mesin, dan sangat penting untuk memahaminya dengan benar!

Pertimbangkan masalah berikut tentang mendekati 5 titik (diwakili oleh `x` pada grafik di bawah):

!linear | overfit
-------------------------|--------------------------
**Model Linear, 2 parameter** | **Model Non-linear, 7 parameter**
Kesalahan pelatihan = 5.3 | Kesalahan pelatihan = 0
Kesalahan validasi = 5.1 | Kesalahan validasi = 20

* Di sebelah kiri, kita melihat aproksimasi garis lurus yang baik. Karena jumlah parameter memadai, model mendapatkan ide di balik distribusi titik dengan benar.
* Di sebelah kanan, model terlalu kuat. Karena kita hanya memiliki 5 titik dan model memiliki 7 parameter, ia dapat menyesuaikan sedemikian rupa sehingga melewati semua titik, membuat kesalahan pelatihan menjadi 0. Namun, ini mencegah model memahami pola yang benar di balik data, sehingga kesalahan validasi sangat tinggi.

Sangat penting untuk mencapai keseimbangan yang tepat antara kekayaan model (jumlah parameter) dan jumlah sampel pelatihan.

## Mengapa overfitting terjadi

  * Tidak cukup data pelatihan
  * Model terlalu kuat
  * Terlalu banyak noise dalam data input

## Cara mendeteksi overfitting

Seperti yang Anda lihat dari grafik di atas, overfitting dapat dideteksi oleh kesalahan pelatihan yang sangat rendah, dan kesalahan validasi yang tinggi. Biasanya selama pelatihan kita akan melihat kesalahan pelatihan dan validasi mulai menurun, dan kemudian pada suatu titik kesalahan validasi mungkin berhenti menurun dan mulai naik. Ini akan menjadi tanda overfitting, dan indikator bahwa kita mungkin harus menghentikan pelatihan pada titik ini (atau setidaknya membuat snapshot dari model).

overfitting

## Cara mencegah overfitting

Jika Anda melihat bahwa overfitting terjadi, Anda dapat melakukan salah satu dari berikut ini:

 * Meningkatkan jumlah data pelatihan
 * Mengurangi kompleksitas model
 * Menggunakan beberapa teknik regularisasi, seperti Dropout, yang akan kita bahas nanti.

## Overfitting dan Bias-Variance Tradeoff

Overfitting sebenarnya adalah kasus dari masalah yang lebih umum dalam statistik yang disebut Bias-Variance Tradeoff. Jika kita mempertimbangkan sumber kesalahan yang mungkin dalam model kita, kita dapat melihat dua jenis kesalahan:

* **Kesalahan bias** disebabkan oleh algoritma kita yang tidak dapat menangkap hubungan antara data pelatihan dengan benar. Ini dapat terjadi karena model kita tidak cukup kuat (**underfitting**).
* **Kesalahan varians**, yang disebabkan oleh model yang memperkirakan noise dalam data input alih-alih hubungan yang berarti (**overfitting**).

Selama pelatihan, kesalahan bias menurun (karena model kita belajar untuk mendekati data), dan kesalahan varians meningkat. Penting untuk menghentikan pelatihan - baik secara manual (ketika kita mendeteksi overfitting) atau secara otomatis (dengan memperkenalkan regularisasi) - untuk mencegah overfitting.

## Kesimpulan

Dalam pelajaran ini, Anda mempelajari tentang perbedaan antara berbagai API untuk dua kerangka AI paling populer, TensorFlow dan PyTorch. Selain itu, Anda mempelajari tentang topik yang sangat penting, overfitting.

## 🚀 Tantangan

Dalam notebook yang menyertainya, Anda akan menemukan 'tugas' di bagian bawah; kerjakan notebook dan selesaikan tugas tersebut.

## Tinjauan & Studi Mandiri

Lakukan penelitian tentang topik berikut:

- TensorFlow
- PyTorch
- Overfitting

Tanyakan pada diri Anda pertanyaan berikut:

- Apa perbedaan antara TensorFlow dan PyTorch?
- Apa perbedaan antara overfitting dan underfitting?

## Tugas

Dalam laboratorium ini, Anda diminta untuk menyelesaikan dua masalah klasifikasi menggunakan jaringan yang sepenuhnya terhubung satu lapis dan multi-lapis menggunakan PyTorch atau TensorFlow.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan untuk menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.