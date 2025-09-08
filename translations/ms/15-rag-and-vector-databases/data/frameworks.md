<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:35:03+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "ms"
}
-->
# Rangka Kerja Rangkaian Neural

Seperti yang telah kita pelajari, untuk dapat melatih rangkaian neural dengan cekap kita perlu melakukan dua perkara:

* Untuk mengendalikan tensor, contohnya untuk mendarab, menambah, dan mengira beberapa fungsi seperti sigmoid atau softmax
* Untuk mengira kecerunan bagi semua ungkapan, bagi melaksanakan pengoptimuman kecerunan menurun

Walaupun perpustakaan `numpy` boleh melakukan bahagian pertama, kita memerlukan mekanisme untuk mengira kecerunan. Dalam rangka kerja yang telah kita bangunkan dalam bahagian sebelum ini, kita terpaksa memprogram secara manual semua fungsi terbitan di dalam kaedah `backward`, yang melakukan backpropagation. Secara idealnya, rangka kerja harus memberi peluang untuk mengira kecerunan bagi *sebarang ungkapan* yang boleh kita definisikan.

Satu lagi perkara penting adalah keupayaan untuk melakukan pengiraan pada GPU, atau unit pengiraan khusus lain, seperti TPU. Latihan rangkaian neural yang mendalam memerlukan *banyak* pengiraan, dan keupayaan untuk memparalelkan pengiraan tersebut pada GPU adalah sangat penting.

> ✅ Istilah 'memparalelkan' bermaksud mengagihkan pengiraan ke atas pelbagai peranti.

Pada masa ini, dua rangka kerja neural yang paling popular adalah: TensorFlow dan PyTorch. Kedua-duanya menyediakan API tahap rendah untuk mengendalikan tensor pada CPU dan GPU. Di atas API tahap rendah, terdapat juga API tahap tinggi, yang dipanggil Keras dan PyTorch Lightning masing-masing.

API Tahap Rendah | TensorFlow | PyTorch  
-----------------|------------|---------  
API Tahap Tinggi | Keras      | PyTorch

**API Tahap Rendah** dalam kedua-dua rangka kerja membolehkan anda membina apa yang dipanggil **graf pengiraan**. Graf ini menentukan bagaimana untuk mengira output (biasanya fungsi kerugian) dengan parameter input yang diberikan, dan boleh dihantar untuk pengiraan pada GPU, jika tersedia. Terdapat fungsi untuk membeza graf pengiraan ini dan mengira kecerunan, yang kemudiannya boleh digunakan untuk mengoptimumkan parameter model.

**API Tahap Tinggi** menganggap rangkaian neural sebagai **urutan lapisan**, dan memudahkan pembinaan kebanyakan rangkaian neural. Melatih model biasanya memerlukan penyediaan data dan kemudian memanggil fungsi `fit` untuk menjalankan proses latihan.

API tahap tinggi membolehkan anda membina rangkaian neural biasa dengan cepat tanpa perlu risau tentang banyak butiran. Pada masa yang sama, API tahap rendah menawarkan kawalan lebih terhadap proses latihan, dan oleh itu ia banyak digunakan dalam penyelidikan, terutamanya apabila anda berurusan dengan seni bina rangkaian neural baru.

Adalah penting juga untuk memahami bahawa anda boleh menggunakan kedua-dua API bersama-sama, contohnya anda boleh membangunkan seni bina lapisan rangkaian anda sendiri menggunakan API tahap rendah, dan kemudian menggunakannya dalam rangkaian yang lebih besar yang dibina dan dilatih dengan API tahap tinggi. Atau anda boleh mentakrifkan rangkaian menggunakan API tahap tinggi sebagai urutan lapisan, dan kemudian menggunakan gelung latihan tahap rendah anda sendiri untuk melakukan pengoptimuman. Kedua-dua API menggunakan konsep asas yang sama, dan direka untuk berfungsi dengan baik bersama.

## Pembelajaran

Dalam kursus ini, kami menawarkan kebanyakan kandungan untuk PyTorch dan TensorFlow. Anda boleh memilih rangka kerja pilihan anda dan hanya mengikuti buku nota yang berkaitan. Jika anda tidak pasti rangka kerja mana yang hendak dipilih, baca beberapa perbincangan di internet mengenai **PyTorch vs. TensorFlow**. Anda juga boleh melihat kedua-dua rangka kerja untuk mendapatkan pemahaman yang lebih baik.

Di mana boleh, kami akan menggunakan API Tahap Tinggi untuk kesederhanaan. Namun, kami percaya adalah penting untuk memahami bagaimana rangkaian neural berfungsi dari asas, oleh itu pada permulaan kami bermula dengan bekerja menggunakan API tahap rendah dan tensor. Walau bagaimanapun, jika anda ingin bermula dengan cepat dan tidak mahu meluangkan banyak masa untuk mempelajari butiran ini, anda boleh langkau dan terus ke buku nota API tahap tinggi.

## ✍️ Latihan: Rangka Kerja

Teruskan pembelajaran anda dalam buku nota berikut:

API Tahap Rendah | Buku Nota TensorFlow+Keras | PyTorch  
-----------------|----------------------------|---------  
API Tahap Tinggi | Keras                      | *PyTorch Lightning*

Setelah menguasai rangka kerja, mari kita ulangkaji konsep overfitting.

# Overfitting

Overfitting adalah konsep yang sangat penting dalam pembelajaran mesin, dan sangat penting untuk memahaminya dengan betul!

Pertimbangkan masalah berikut untuk menganggar 5 titik (diwakili oleh `x` pada graf di bawah):

!linear | overfit  
-------------------------|--------------------------  
**Model linear, 2 parameter** | **Model bukan linear, 7 parameter**  
Ralat latihan = 5.3 | Ralat latihan = 0  
Ralat pengesahan = 5.1 | Ralat pengesahan = 20

* Di sebelah kiri, kita melihat anggaran garis lurus yang baik. Oleh kerana bilangan parameter adalah mencukupi, model dapat memahami taburan titik dengan betul.
* Di sebelah kanan, model terlalu kuat. Oleh kerana kita hanya mempunyai 5 titik dan model mempunyai 7 parameter, ia boleh menyesuaikan diri supaya melalui semua titik, menjadikan ralat latihan menjadi 0. Namun, ini menghalang model daripada memahami corak sebenar di sebalik data, oleh itu ralat pengesahan sangat tinggi.

Adalah sangat penting untuk mencari keseimbangan yang betul antara kekayaan model (bilangan parameter) dan bilangan sampel latihan.

## Mengapa overfitting berlaku

  * Data latihan tidak mencukupi
  * Model terlalu kuat
  * Terlalu banyak bunyi dalam data input

## Cara mengesan overfitting

Seperti yang anda lihat dari graf di atas, overfitting boleh dikesan dengan ralat latihan yang sangat rendah, dan ralat pengesahan yang tinggi. Biasanya semasa latihan kita akan melihat kedua-dua ralat latihan dan pengesahan mula menurun, dan kemudian pada satu ketika ralat pengesahan mungkin berhenti menurun dan mula meningkat. Ini adalah tanda overfitting, dan petunjuk bahawa kita mungkin perlu berhenti latihan pada titik ini (atau sekurang-kurangnya membuat salinan model).

overfitting

## Cara mencegah overfitting

Jika anda dapat melihat overfitting berlaku, anda boleh melakukan salah satu daripada berikut:

 * Tambah jumlah data latihan
 * Kurangkan kerumitan model
 * Gunakan teknik regularisasi, seperti Dropout, yang akan kita bincangkan kemudian.

## Overfitting dan Perdagangan Bias-Varians

Overfitting sebenarnya adalah kes masalah yang lebih umum dalam statistik yang dipanggil Perdagangan Bias-Varians. Jika kita pertimbangkan sumber ralat yang mungkin dalam model kita, kita boleh lihat dua jenis ralat:

* **Ralat bias** disebabkan oleh algoritma kita yang tidak dapat menangkap hubungan antara data latihan dengan betul. Ia boleh berlaku kerana model kita tidak cukup kuat (**underfitting**).
* **Ralat varians**, yang disebabkan oleh model menganggar bunyi dalam data input dan bukannya hubungan bermakna (**overfitting**).

Semasa latihan, ralat bias menurun (kerana model kita belajar menganggar data), dan ralat varians meningkat. Adalah penting untuk menghentikan latihan - sama ada secara manual (apabila kita mengesan overfitting) atau secara automatik (dengan memperkenalkan regularisasi) - untuk mengelakkan overfitting.

## Kesimpulan

Dalam pelajaran ini, anda telah belajar tentang perbezaan antara pelbagai API untuk dua rangka kerja AI yang paling popular, TensorFlow dan PyTorch. Selain itu, anda juga mempelajari topik yang sangat penting, iaitu overfitting.

## 🚀 Cabaran

Dalam buku nota yang disertakan, anda akan menemui 'tugasan' di bahagian bawah; selesaikan buku nota tersebut dan lengkapkan tugasan.

## Ulasan & Belajar Sendiri

Lakukan kajian mengenai topik berikut:

- TensorFlow  
- PyTorch  
- Overfitting

Tanya diri anda soalan berikut:

- Apakah perbezaan antara TensorFlow dan PyTorch?  
- Apakah perbezaan antara overfitting dan underfitting?

## Tugasan

Dalam makmal ini, anda diminta untuk menyelesaikan dua masalah klasifikasi menggunakan rangkaian bersambung penuh satu lapisan dan berbilang lapisan menggunakan PyTorch atau TensorFlow.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.