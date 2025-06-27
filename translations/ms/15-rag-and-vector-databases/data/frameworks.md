<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:07:42+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "ms"
}
-->
# Rangka Kerja Rangkaian Neural

Seperti yang telah kita pelajari, untuk melatih rangkaian neural dengan cekap kita perlu melakukan dua perkara:

* Mengendalikan tensor, contohnya untuk mendarab, menambah, dan mengira beberapa fungsi seperti sigmoid atau softmax
* Mengira kecerunan semua ekspresi, untuk melakukan pengoptimuman penurunan kecerunan

Walaupun perpustakaan `numpy` boleh melakukan bahagian pertama, kita memerlukan mekanisme untuk mengira kecerunan. Dalam rangka kerja yang telah kita bangunkan dalam bahagian sebelumnya, kita perlu memprogramkan semua fungsi terbitan secara manual dalam kaedah `backward`, yang melakukan backpropagation. Idealnya, rangka kerja harus memberi kita peluang untuk mengira kecerunan *sebarang ekspresi* yang kita boleh definisikan.

Perkara penting lain adalah dapat melakukan pengiraan pada GPU, atau unit pengiraan khusus lain, seperti TPU. Latihan rangkaian neural yang mendalam memerlukan *banyak* pengiraan, dan dapat memparallelkan pengiraan tersebut pada GPU adalah sangat penting.

> ✅ Istilah 'parallelize' bermaksud untuk mengedarkan pengiraan ke atas pelbagai peranti.

Pada masa ini, dua rangka kerja neural yang paling popular ialah: TensorFlow dan PyTorch. Kedua-duanya menyediakan API peringkat rendah untuk beroperasi dengan tensor pada CPU dan GPU. Di atas API peringkat rendah, terdapat juga API peringkat tinggi, yang dipanggil Keras dan PyTorch Lightning masing-masing.

API Peringkat Rendah | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
API Peringkat Tinggi| Keras| Pytorch

**API peringkat rendah** dalam kedua-dua rangka kerja membolehkan anda membina **graf pengiraan** yang dipanggil. Graf ini menentukan bagaimana untuk mengira output (biasanya fungsi kerugian) dengan parameter input yang diberikan, dan boleh ditolak untuk pengiraan pada GPU, jika ia tersedia. Terdapat fungsi untuk membezakan graf pengiraan ini dan mengira kecerunan, yang kemudiannya boleh digunakan untuk mengoptimumkan parameter model.

**API peringkat tinggi** menganggap rangkaian neural sebagai **susunan lapisan**, dan membuat pembinaan kebanyakan rangkaian neural menjadi lebih mudah. Melatih model biasanya memerlukan penyediaan data dan kemudian memanggil fungsi `fit` untuk melakukan tugas tersebut.

API peringkat tinggi membolehkan anda membina rangkaian neural tipikal dengan cepat tanpa risau tentang banyak butiran. Pada masa yang sama, API peringkat rendah menawarkan lebih banyak kawalan ke atas proses latihan, dan oleh itu ia banyak digunakan dalam penyelidikan, apabila anda berurusan dengan seni bina rangkaian neural baru.

Ia juga penting untuk memahami bahawa anda boleh menggunakan kedua-dua API bersama-sama, contohnya anda boleh membangunkan seni bina lapisan rangkaian anda sendiri menggunakan API peringkat rendah, dan kemudian menggunakannya di dalam rangkaian yang lebih besar yang dibina dan dilatih dengan API peringkat tinggi. Atau anda boleh mentakrifkan rangkaian menggunakan API peringkat tinggi sebagai susunan lapisan, dan kemudian menggunakan gelung latihan peringkat rendah anda sendiri untuk melakukan pengoptimuman. Kedua-dua API menggunakan konsep asas yang sama, dan ia direka untuk berfungsi dengan baik bersama-sama.

## Pembelajaran

Dalam kursus ini, kami menawarkan kebanyakan kandungan untuk PyTorch dan TensorFlow. Anda boleh memilih rangka kerja pilihan anda dan hanya melalui buku nota yang berkaitan. Jika anda tidak pasti rangka kerja mana yang hendak dipilih, baca beberapa perbincangan di internet mengenai **PyTorch vs. TensorFlow**. Anda juga boleh melihat kedua-dua rangka kerja untuk mendapatkan pemahaman yang lebih baik.

Di mana boleh, kami akan menggunakan API Peringkat Tinggi untuk kesederhanaan. Walau bagaimanapun, kami percaya adalah penting untuk memahami bagaimana rangkaian neural berfungsi dari asas, oleh itu pada permulaan kami bermula dengan bekerja dengan API peringkat rendah dan tensor. Walau bagaimanapun, jika anda ingin bermula dengan cepat dan tidak mahu menghabiskan banyak masa untuk mempelajari butiran ini, anda boleh melangkau dan terus ke buku nota API peringkat tinggi.

## ✍️ Latihan: Rangka Kerja

Teruskan pembelajaran anda dalam buku nota berikut:

API Peringkat Rendah | Buku Nota TensorFlow+Keras | PyTorch
--------------|-------------------------------------|--------------------------------
API Peringkat Tinggi| Keras | *PyTorch Lightning*

Selepas menguasai rangka kerja, mari kita ulangi konsep overfitting.

# Overfitting

Overfitting adalah konsep yang sangat penting dalam pembelajaran mesin, dan sangat penting untuk mendapatkannya dengan betul!

Pertimbangkan masalah berikut untuk menganggar 5 titik (diwakili oleh `x` pada graf di bawah):

!linear | overfit
-------------------------|--------------------------
**Model Linear, 2 parameter** | **Model Bukan Linear, 7 parameter**
Ralat latihan = 5.3 | Ralat latihan = 0
Ralat pengesahan = 5.1 | Ralat pengesahan = 20

* Di sebelah kiri, kita melihat anggaran garis lurus yang baik. Kerana bilangan parameter adalah mencukupi, model mendapat idea di sebalik pengedaran titik dengan betul.
* Di sebelah kanan, model terlalu berkuasa. Kerana kita hanya mempunyai 5 titik dan model mempunyai 7 parameter, ia boleh menyesuaikan dengan cara yang melalui semua titik, menjadikan ralat latihan menjadi 0. Walau bagaimanapun, ini menghalang model daripada memahami pola yang betul di sebalik data, oleh itu ralat pengesahan adalah sangat tinggi.

Adalah sangat penting untuk mencapai keseimbangan yang betul antara kekayaan model (bilangan parameter) dan bilangan sampel latihan.

## Mengapa overfitting berlaku

  * Data latihan tidak mencukupi
  * Model terlalu berkuasa
  * Terlalu banyak bunyi dalam data input

## Cara mengesan overfitting

Seperti yang anda lihat dari graf di atas, overfitting boleh dikesan dengan ralat latihan yang sangat rendah, dan ralat pengesahan yang tinggi. Biasanya semasa latihan kita akan melihat kedua-dua ralat latihan dan pengesahan mula berkurangan, dan kemudian pada satu ketika ralat pengesahan mungkin berhenti berkurangan dan mula meningkat. Ini akan menjadi tanda overfitting, dan petunjuk bahawa kita mungkin harus berhenti latihan pada ketika ini (atau sekurang-kurangnya membuat snapshot model).

overfitting

## Cara mencegah overfitting

Jika anda dapat melihat bahawa overfitting berlaku, anda boleh melakukan salah satu perkara berikut:

 * Meningkatkan jumlah data latihan
 * Mengurangkan kerumitan model
 * Menggunakan beberapa teknik regularisasi, seperti Dropout, yang akan kita pertimbangkan kemudian.

## Overfitting dan Pertukaran Bias-Variance

Overfitting sebenarnya adalah kes masalah yang lebih umum dalam statistik yang dipanggil Pertukaran Bias-Variance. Jika kita mempertimbangkan sumber-sumber kesilapan yang mungkin dalam model kita, kita dapat melihat dua jenis kesilapan:

* **Kesilapan Bias** disebabkan oleh algoritma kita yang tidak dapat menangkap hubungan antara data latihan dengan betul. Ia boleh berpunca dari fakta bahawa model kita tidak cukup berkuasa (**underfitting**).
* **Kesilapan Varians**, yang disebabkan oleh model menganggar bunyi dalam data input daripada hubungan yang bermakna (**overfitting**).

Semasa latihan, kesilapan bias berkurangan (seperti model kita belajar menganggar data), dan kesilapan varians meningkat. Adalah penting untuk menghentikan latihan - sama ada secara manual (apabila kita mengesan overfitting) atau secara automatik (dengan memperkenalkan regularisasi) - untuk mencegah overfitting.

## Kesimpulan

Dalam pelajaran ini, anda telah mempelajari tentang perbezaan antara pelbagai API untuk dua rangka kerja AI yang paling popular, TensorFlow dan PyTorch. Di samping itu, anda telah mempelajari topik yang sangat penting, overfitting.

## 🚀 Cabaran

Dalam buku nota yang disertakan, anda akan menemui 'tugas' di bahagian bawah; bekerja melalui buku nota dan selesaikan tugas-tugas tersebut.

## Ulasan & Kajian Sendiri

Lakukan beberapa penyelidikan mengenai topik berikut:

- TensorFlow
- PyTorch
- Overfitting

Tanya diri anda soalan berikut:

- Apakah perbezaan antara TensorFlow dan PyTorch?
- Apakah perbezaan antara overfitting dan underfitting?

## Tugasan

Dalam makmal ini, anda diminta untuk menyelesaikan dua masalah klasifikasi menggunakan rangkaian yang bersambung sepenuhnya berlapis tunggal dan berbilang menggunakan PyTorch atau TensorFlow.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.