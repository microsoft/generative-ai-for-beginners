<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:28:20+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "ms"
}
-->
# Pengenalan kepada Rangkaian Neural. Perceptron Berlapis-Lapis

Dalam bahagian sebelum ini, anda telah mempelajari tentang model rangkaian neural yang paling mudah - perceptron satu lapis, model klasifikasi linear dua kelas.

Dalam bahagian ini, kita akan mengembangkan model ini ke dalam kerangka yang lebih fleksibel, membolehkan kita:

* melakukan **klasifikasi pelbagai kelas** selain dua kelas
* menyelesaikan **masalah regresi** selain klasifikasi
* memisahkan kelas yang tidak boleh dipisahkan secara linear

Kita juga akan membangunkan kerangka modular kita sendiri dalam Python yang akan membolehkan kita membina pelbagai seni bina rangkaian neural.

## Formalisasi Pembelajaran Mesin

Mari kita mulakan dengan memformalkan masalah Pembelajaran Mesin. Katakan kita mempunyai dataset latihan **X** dengan label **Y**, dan kita perlu membina model *f* yang akan membuat ramalan paling tepat. Kualiti ramalan diukur dengan **fungsi Kehilangan** ℒ. Fungsi kehilangan berikut sering digunakan:

* Untuk masalah regresi, apabila kita perlu meramalkan nombor, kita boleh menggunakan **kesalahan mutlak** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, atau **kesalahan kuasa dua** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Untuk klasifikasi, kita menggunakan **kehilangan 0-1** (yang pada dasarnya sama dengan **ketepatan** model), atau **kehilangan logistik**.

Untuk perceptron satu lapis, fungsi *f* ditakrifkan sebagai fungsi linear *f(x)=wx+b* (di sini *w* adalah matriks berat, *x* adalah vektor ciri input, dan *b* adalah vektor bias). Untuk pelbagai seni bina rangkaian neural, fungsi ini boleh mengambil bentuk yang lebih kompleks.

> Dalam kes klasifikasi, sering diinginkan untuk mendapatkan kebarangkalian kelas yang sepadan sebagai output rangkaian. Untuk menukar nombor sewenang-wenangnya kepada kebarangkalian (cth. untuk menormalkan output), kita sering menggunakan fungsi **softmax** σ, dan fungsi *f* menjadi *f(x)=σ(wx+b)*

Dalam definisi *f* di atas, *w* dan *b* dipanggil **parameter** θ=⟨*w,b*⟩. Diberikan dataset ⟨**X**,**Y**⟩, kita boleh mengira kesalahan keseluruhan pada keseluruhan dataset sebagai fungsi parameter θ.

> ✅ **Matlamat latihan rangkaian neural adalah untuk meminimumkan kesalahan dengan mengubah parameter θ**

## Pengoptimuman Penurunan Kecerunan

Terdapat kaedah pengoptimuman fungsi yang terkenal yang dipanggil **penurunan kecerunan**. Idea di sini ialah kita boleh mengira terbitan (dalam kes berbilang dimensi dipanggil **kecerunan**) fungsi kehilangan berkenaan dengan parameter, dan mengubah parameter sedemikian rupa supaya kesalahan akan berkurang. Ini boleh diformalkan seperti berikut:

* Inisialisasi parameter dengan beberapa nilai rawak w<sup>(0)</sup>, b<sup>(0)</sup>
* Ulang langkah berikut berkali-kali:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Semasa latihan, langkah pengoptimuman sepatutnya dikira dengan mempertimbangkan keseluruhan dataset (ingat bahawa kehilangan dikira sebagai jumlah melalui semua sampel latihan). Walau bagaimanapun, dalam kehidupan sebenar kita mengambil bahagian kecil daripada dataset yang dipanggil **minibatches**, dan mengira kecerunan berdasarkan subset data. Oleh kerana subset diambil secara rawak setiap kali, kaedah sedemikian dipanggil **penurunan kecerunan stokastik** (SGD).

## Perceptron Berlapis-Lapis dan Penyebaran Balik

Rangkaian satu lapis, seperti yang telah kita lihat di atas, mampu mengklasifikasikan kelas yang boleh dipisahkan secara linear. Untuk membina model yang lebih kaya, kita boleh menggabungkan beberapa lapisan rangkaian. Secara matematik, ini bermaksud bahawa fungsi *f* akan mempunyai bentuk yang lebih kompleks, dan akan dikira dalam beberapa langkah:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Di sini, α adalah **fungsi pengaktifan tidak linear**, σ adalah fungsi softmax, dan parameter θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>

Algoritma penurunan kecerunan akan tetap sama, tetapi ia akan menjadi lebih sukar untuk mengira kecerunan. Diberikan peraturan pembezaan rantai, kita boleh mengira terbitan sebagai:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Peraturan pembezaan rantai digunakan untuk mengira terbitan fungsi kehilangan berkenaan dengan parameter.

Perhatikan bahawa bahagian paling kiri bagi semua ungkapan tersebut adalah sama, dan oleh itu kita boleh mengira terbitan secara efektif bermula dari fungsi kehilangan dan pergi "ke belakang" melalui graf pengiraan. Oleh itu, kaedah latihan perceptron berlapis-lapis dipanggil **penyebaran balik**, atau 'backprop'.



> TODO: citasi imej

> ✅ Kami akan membincangkan penyebaran balik dengan lebih terperinci dalam contoh buku nota kami.

## Kesimpulan

Dalam pelajaran ini, kami telah membina perpustakaan rangkaian neural kami sendiri, dan kami telah menggunakannya untuk tugas klasifikasi dua dimensi yang mudah.

## 🚀 Cabaran

Dalam buku nota yang disertakan, anda akan melaksanakan kerangka kerja anda sendiri untuk membina dan melatih perceptron berlapis-lapis. Anda akan dapat melihat secara terperinci bagaimana rangkaian neural moden beroperasi.

Teruskan ke buku nota OwnFramework dan kerjakanlah.

## Ulasan & Kajian Kendiri

Penyebaran balik adalah algoritma biasa yang digunakan dalam AI dan ML, berbaloi untuk dikaji dengan lebih mendalam.

## Tugasan

Dalam makmal ini, anda diminta menggunakan kerangka kerja yang anda bina dalam pelajaran ini untuk menyelesaikan klasifikasi digit tulisan tangan MNIST.

* Arahan
* Buku nota

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.