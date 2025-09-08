<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:49:27+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "ms"
}
-->
# Pengenalan kepada Rangkaian Neural. Perceptron Berlapis-Lapis

Dalam bahagian sebelumnya, anda telah mempelajari model rangkaian neural yang paling mudah - perceptron satu lapisan, model klasifikasi linear dua kelas.

Dalam bahagian ini, kita akan mengembangkan model ini ke dalam rangka kerja yang lebih fleksibel, membolehkan kita untuk:

* melaksanakan **klasifikasi berbilang kelas** selain daripada dua kelas
* menyelesaikan **masalah regresi** selain daripada klasifikasi
* memisahkan kelas yang tidak boleh dipisahkan secara linear

Kita juga akan membangunkan rangka kerja modular kita sendiri dalam Python yang membolehkan kita membina pelbagai seni bina rangkaian neural.

## Formalisasi Pembelajaran Mesin

Mari kita mulakan dengan memformalkan masalah Pembelajaran Mesin. Anggap kita mempunyai set data latihan **X** dengan label **Y**, dan kita perlu membina model *f* yang akan membuat ramalan paling tepat. Kualiti ramalan diukur oleh **fungsi kerugian** ℒ. Fungsi kerugian berikut sering digunakan:

* Untuk masalah regresi, apabila kita perlu meramalkan nombor, kita boleh menggunakan **ralat mutlak** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, atau **ralat kuasa dua** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Untuk klasifikasi, kita menggunakan **kerugian 0-1** (yang pada dasarnya sama dengan **ketepatan** model), atau **kerugian logistik**.

Untuk perceptron satu lapisan, fungsi *f* ditakrifkan sebagai fungsi linear *f(x)=wx+b* (di sini *w* adalah matriks berat, *x* adalah vektor ciri input, dan *b* adalah vektor bias). Untuk seni bina rangkaian neural yang berbeza, fungsi ini boleh mengambil bentuk yang lebih kompleks.

> Dalam kes klasifikasi, sering kali diinginkan untuk mendapatkan kebarangkalian kelas yang sepadan sebagai output rangkaian. Untuk menukar nombor sewenang-wenangnya kepada kebarangkalian (contohnya untuk menormalkan output), kita sering menggunakan fungsi **softmax** σ, dan fungsi *f* menjadi *f(x)=σ(wx+b)*

Dalam definisi *f* di atas, *w* dan *b* dipanggil **parameter** θ=⟨*w,b*⟩. Diberikan set data ⟨**X**,**Y**⟩, kita boleh mengira jumlah ralat keseluruhan pada set data sebagai fungsi parameter θ.

> ✅ **Matlamat latihan rangkaian neural adalah untuk meminimumkan ralat dengan mengubah parameter θ**

## Pengoptimuman Kecerunan Menurun

Terdapat satu kaedah pengoptimuman fungsi yang terkenal dipanggil **kecerunan menurun**. Idea di sebaliknya adalah kita boleh mengira terbitan (dalam kes berbilang dimensi dipanggil **kecerunan**) fungsi kerugian berkenaan dengan parameter, dan mengubah parameter sedemikian rupa supaya ralat berkurang. Ini boleh diformalkan seperti berikut:

* Inisialisasi parameter dengan beberapa nilai rawak w<sup>(0)</sup>, b<sup>(0)</sup>
* Ulang langkah berikut berkali-kali:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Semasa latihan, langkah pengoptimuman sepatutnya dikira dengan mengambil kira keseluruhan set data (ingat bahawa kerugian dikira sebagai jumlah melalui semua sampel latihan). Namun, dalam kehidupan sebenar kita mengambil bahagian kecil set data yang dipanggil **minibatch**, dan mengira kecerunan berdasarkan subset data tersebut. Oleh kerana subset diambil secara rawak setiap kali, kaedah ini dipanggil **kecerunan menurun stokastik** (SGD).

## Perceptron Berlapis-Lapis dan Backpropagation

Rangkaian satu lapisan, seperti yang telah kita lihat di atas, mampu mengklasifikasikan kelas yang boleh dipisahkan secara linear. Untuk membina model yang lebih kaya, kita boleh menggabungkan beberapa lapisan rangkaian. Secara matematik, ini bermakna fungsi *f* akan mempunyai bentuk yang lebih kompleks, dan akan dikira dalam beberapa langkah:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Di sini, α adalah **fungsi pengaktifan bukan linear**, σ adalah fungsi softmax, dan parameter θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritma kecerunan menurun kekal sama, tetapi pengiraan kecerunan menjadi lebih sukar. Dengan menggunakan peraturan rantai pembezaan, kita boleh mengira terbitan seperti berikut:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Peraturan rantai pembezaan digunakan untuk mengira terbitan fungsi kerugian berkenaan dengan parameter.

Perhatikan bahawa bahagian paling kiri dalam semua ungkapan ini adalah sama, jadi kita boleh mengira terbitan dengan berkesan bermula dari fungsi kerugian dan bergerak "ke belakang" melalui graf pengiraan. Oleh itu, kaedah latihan perceptron berlapis-lapis dipanggil **backpropagation**, atau 'backprop'.



> TODO: image citation

> ✅ Kita akan membincangkan backprop dengan lebih terperinci dalam contoh notebook kita.  

## Kesimpulan

Dalam pelajaran ini, kita telah membina perpustakaan rangkaian neural kita sendiri, dan menggunakannya untuk tugasan klasifikasi dua dimensi yang mudah.

## 🚀 Cabaran

Dalam notebook yang disertakan, anda akan melaksanakan rangka kerja anda sendiri untuk membina dan melatih perceptron berlapis-lapis. Anda akan dapat melihat dengan lebih terperinci bagaimana rangkaian neural moden beroperasi.

Teruskan ke notebook OwnFramework dan ikuti langkah-langkahnya.



## Ulasan & Belajar Sendiri

Backpropagation adalah algoritma biasa yang digunakan dalam AI dan ML, patut dipelajari dengan lebih mendalam

## Tugasan

Dalam makmal ini, anda diminta menggunakan rangka kerja yang anda bina dalam pelajaran ini untuk menyelesaikan klasifikasi digit tulisan tangan MNIST.

* Arahan
* Notebook

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.