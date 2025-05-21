<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T02:04:03+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "ms"
}
-->
# Rangka Kerja Rangkaian Neural

Seperti yang telah kita pelajari, untuk melatih rangkaian neural dengan cekap kita perlu melakukan dua perkara:

* Mengendalikan tensor, contohnya untuk mendarab, menambah, dan mengira beberapa fungsi seperti sigmoid atau softmax
* Mengira kecerunan semua ungkapan, untuk melakukan pengoptimuman gradient descent

Walaupun perpustakaan `numpy` boleh melakukan bahagian pertama, kita memerlukan mekanisme untuk mengira kecerunan. Dalam rangka kerja yang telah kita bangunkan dalam seksyen sebelumnya, kita terpaksa memprogram semua fungsi terbitan secara manual dalam kaedah `backward`, yang melakukan backpropagation. Idealnya, rangka kerja harus memberi kita peluang untuk mengira kecerunan bagi *mana-mana ungkapan* yang kita boleh definisikan.

Perkara penting lain adalah keupayaan untuk melakukan pengiraan pada GPU, atau mana-mana unit pengiraan khusus lain, seperti TPU. Latihan rangkaian neural dalam memerlukan *banyak* pengiraan, dan keupayaan untuk memparalelkan pengiraan tersebut pada GPU adalah sangat penting.

> ✅ Istilah 'parallelize' bermaksud untuk mengagihkan pengiraan ke atas beberapa peranti.

Pada masa ini, dua rangka kerja neural yang paling popular adalah: TensorFlow dan PyTorch. Kedua-duanya menyediakan API peringkat rendah untuk beroperasi dengan tensor pada kedua-dua CPU dan GPU. Di atas API peringkat rendah, terdapat juga API peringkat tinggi, dipanggil Keras dan PyTorch Lightning masing-masing.

API Peringkat Rendah | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
API Peringkat Tinggi| Keras| Pytorch

**API peringkat rendah** dalam kedua-dua rangka kerja membolehkan anda membina apa yang dipanggil **graf pengiraan**. Graf ini mentakrifkan cara mengira output (biasanya fungsi kehilangan) dengan parameter input yang diberikan, dan boleh dihantar untuk pengiraan pada GPU, jika ia tersedia. Terdapat fungsi untuk membezakan graf pengiraan ini dan mengira kecerunan, yang kemudian boleh digunakan untuk mengoptimumkan parameter model.

**API peringkat tinggi** secara amnya menganggap rangkaian neural sebagai **urutan lapisan**, dan memudahkan pembinaan kebanyakan rangkaian neural. Melatih model biasanya memerlukan penyediaan data dan kemudian memanggil fungsi `fit` untuk melakukan kerja tersebut.

API peringkat tinggi membolehkan anda membina rangkaian neural tipikal dengan cepat tanpa perlu risau tentang banyak butiran. Pada masa yang sama, API peringkat rendah menawarkan lebih banyak kawalan ke atas proses latihan, dan oleh itu ia banyak digunakan dalam penyelidikan, apabila anda berurusan dengan seni bina rangkaian neural baharu.

Adalah penting juga untuk memahami bahawa anda boleh menggunakan kedua-dua API bersama-sama, contohnya anda boleh membangunkan seni bina lapisan rangkaian anda sendiri menggunakan API peringkat rendah, dan kemudian menggunakannya dalam rangkaian yang lebih besar yang dibina dan dilatih dengan API peringkat tinggi. Atau anda boleh mentakrifkan rangkaian menggunakan API peringkat tinggi sebagai urutan lapisan, dan kemudian menggunakan gelung latihan peringkat rendah anda sendiri untuk melakukan pengoptimuman. Kedua-dua API menggunakan konsep asas yang sama, dan ia direka untuk berfungsi dengan baik bersama-sama.

## Pembelajaran

Dalam kursus ini, kami menawarkan kebanyakan kandungan untuk PyTorch dan TensorFlow. Anda boleh memilih rangka kerja pilihan anda dan hanya melalui buku nota yang sepadan. Jika anda tidak pasti rangka kerja mana yang hendak dipilih, baca beberapa perbincangan di internet mengenai **PyTorch vs. TensorFlow**. Anda juga boleh melihat kedua-dua rangka kerja untuk mendapatkan pemahaman yang lebih baik.

Di mana mungkin, kami akan menggunakan API Peringkat Tinggi untuk kesederhanaan. Walau bagaimanapun, kami percaya adalah penting untuk memahami cara rangkaian neural berfungsi dari bawah ke atas, oleh itu pada permulaan kami bermula dengan bekerja dengan API peringkat rendah dan tensor. Walau bagaimanapun, jika anda ingin memulakan dengan cepat dan tidak mahu menghabiskan banyak masa untuk mempelajari butiran ini, anda boleh melangkau perkara tersebut dan terus ke buku nota API peringkat tinggi.

## ✍️ Latihan: Rangka Kerja

Teruskan pembelajaran anda dalam buku nota berikut:

API Peringkat Rendah | Buku Nota TensorFlow+Keras | PyTorch
--------------|-------------------------------------|--------------------------------
API Peringkat Tinggi| Keras | *PyTorch Lightning*

Selepas menguasai rangka kerja, mari kita imbas kembali konsep overfitting.

# Overfitting

Overfitting adalah konsep yang sangat penting dalam pembelajaran mesin, dan sangat penting untuk memahaminya dengan betul!

Pertimbangkan masalah berikut untuk menghampiri 5 titik (diwakili oleh `x` pada graf di bawah):

!linear | overfit
-------------------------|--------------------------
**Model linear, 2 parameter** | **Model bukan linear, 7 parameter**
Ralat latihan = 5.3 | Ralat latihan = 0
Ralat validasi = 5.1 | Ralat validasi = 20

* Di sebelah kiri, kita melihat anggaran garis lurus yang baik. Oleh kerana bilangan parameter adalah mencukupi, model mendapat idea di sebalik taburan titik dengan betul.
* Di sebelah kanan, model terlalu berkuasa. Oleh kerana kita hanya mempunyai 5 titik dan model mempunyai 7 parameter, ia boleh menyesuaikan dengan cara sedemikian untuk melalui semua titik, menjadikan ralat latihan menjadi 0. Walau bagaimanapun, ini menghalang model daripada memahami corak yang betul di sebalik data, oleh itu ralat validasi adalah sangat tinggi.

Adalah sangat penting untuk mencapai keseimbangan yang betul antara kekayaan model (bilangan parameter) dan bilangan sampel latihan.

## Mengapa overfitting berlaku

  * Tidak cukup data latihan
  * Model terlalu berkuasa
  * Terlalu banyak bunyi dalam data input

## Cara mengesan overfitting

Seperti yang anda lihat dari graf di atas, overfitting boleh dikesan dengan ralat latihan yang sangat rendah, dan ralat validasi yang tinggi. Biasanya semasa latihan kita akan melihat kedua-dua ralat latihan dan validasi mula berkurangan, dan kemudian pada satu ketika ralat validasi mungkin berhenti berkurangan dan mula meningkat. Ini akan menjadi tanda overfitting, dan petunjuk bahawa kita mungkin harus menghentikan latihan pada ketika ini (atau sekurang-kurangnya membuat snapshot model).

overfitting

## Cara mencegah overfitting

Jika anda melihat bahawa overfitting berlaku, anda boleh melakukan salah satu daripada perkara berikut:

 * Tingkatkan jumlah data latihan
 * Kurangkan kerumitan model
 * Gunakan beberapa teknik regularisasi, seperti Dropout, yang akan kita pertimbangkan kemudian.

## Overfitting dan Bias-Variance Tradeoff

Overfitting sebenarnya adalah kes masalah yang lebih umum dalam statistik yang dipanggil Bias-Variance Tradeoff. Jika kita mempertimbangkan kemungkinan sumber ralat dalam model kita, kita boleh melihat dua jenis ralat:

* **Ralat bias** disebabkan oleh algoritma kita yang tidak dapat menangkap hubungan antara data latihan dengan betul. Ia boleh berlaku kerana model kita tidak cukup berkuasa (**underfitting**).
* **Ralat varians**, yang disebabkan oleh model menghampiri bunyi dalam data input dan bukannya hubungan yang bermakna (**overfitting**).

Semasa latihan, ralat bias berkurangan (kerana model kita belajar menghampiri data), dan ralat varians meningkat. Adalah penting untuk menghentikan latihan - sama ada secara manual (apabila kita mengesan overfitting) atau secara automatik (dengan memperkenalkan regularisasi) - untuk mencegah overfitting.

## Kesimpulan

Dalam pelajaran ini, anda telah belajar tentang perbezaan antara pelbagai API untuk dua rangka kerja AI yang paling popular, TensorFlow dan PyTorch. Selain itu, anda telah mempelajari topik yang sangat penting, overfitting.

## 🚀 Cabaran

Dalam buku nota yang disertakan, anda akan menemui 'tugas' di bahagian bawah; kerjakan buku nota dan lengkapkan tugas tersebut.

## Ulasan & Kajian Sendiri

Lakukan penyelidikan mengenai topik berikut:

- TensorFlow
- PyTorch
- Overfitting

Tanya diri anda soalan berikut:

- Apakah perbezaan antara TensorFlow dan PyTorch?
- Apakah perbezaan antara overfitting dan underfitting?

## Tugasan

Dalam makmal ini, anda diminta untuk menyelesaikan dua masalah pengelasan menggunakan rangkaian bersambung penuh satu dan berbilang lapisan menggunakan PyTorch atau TensorFlow.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber berwibawa. Untuk maklumat penting, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.