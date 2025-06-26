<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-06-25T10:00:22+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "id"
}
-->
# Pengantar AI Generatif dan Model Bahasa Besar

_(Klik gambar di atas untuk menonton video dari pelajaran ini)_

AI Generatif adalah kecerdasan buatan yang mampu menghasilkan teks, gambar, dan jenis konten lainnya. Yang membuatnya menjadi teknologi fantastis adalah ia mendemokratisasi AI, siapa pun dapat menggunakannya hanya dengan prompt teks, sebuah kalimat yang ditulis dalam bahasa alami. Anda tidak perlu mempelajari bahasa seperti Java atau SQL untuk mencapai sesuatu yang berharga, yang Anda butuhkan hanyalah menggunakan bahasa Anda, nyatakan apa yang Anda inginkan dan keluarlah saran dari model AI. Aplikasi dan dampaknya sangat besar, Anda dapat menulis atau memahami laporan, menulis aplikasi, dan banyak lagi, semuanya dalam hitungan detik.

Dalam kurikulum ini, kita akan menjelajahi bagaimana startup kita memanfaatkan AI generatif untuk membuka skenario baru di dunia pendidikan dan bagaimana kita menangani tantangan yang tak terhindarkan terkait dengan implikasi sosial dari penerapannya dan keterbatasan teknologi.

## Pengantar

Pelajaran ini akan mencakup:

- Pengantar skenario bisnis: ide dan misi startup kita.
- AI Generatif dan bagaimana kita mencapai lanskap teknologi saat ini.
- Cara kerja internal model bahasa besar.
- Kemampuan utama dan kasus penggunaan praktis dari Model Bahasa Besar.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan memahami:

- Apa itu AI generatif dan bagaimana Model Bahasa Besar bekerja.
- Bagaimana Anda dapat memanfaatkan model bahasa besar untuk berbagai kasus penggunaan, dengan fokus pada skenario pendidikan.

## Skenario: startup pendidikan kita

Kecerdasan Buatan (AI) Generatif mewakili puncak teknologi AI, mendorong batasan dari apa yang dulunya dianggap mustahil. Model AI generatif memiliki beberapa kemampuan dan aplikasi, tetapi untuk kurikulum ini kita akan menjelajahi bagaimana ini merevolusi pendidikan melalui startup fiktif. Kita akan merujuk ke startup ini sebagai _startup kita_. Startup kita bekerja di bidang pendidikan dengan pernyataan misi yang ambisius:

> _meningkatkan aksesibilitas dalam pembelajaran, secara global, memastikan akses pendidikan yang setara dan memberikan pengalaman pembelajaran yang dipersonalisasi kepada setiap pelajar, sesuai kebutuhan mereka_.

Tim startup kita sadar bahwa kita tidak akan dapat mencapai tujuan ini tanpa memanfaatkan salah satu alat paling kuat di zaman modern – Model Bahasa Besar (LLM).

AI Generatif diharapkan dapat merevolusi cara kita belajar dan mengajar saat ini, dengan siswa memiliki guru virtual 24 jam sehari yang menyediakan sejumlah besar informasi dan contoh, dan guru dapat memanfaatkan alat inovatif untuk menilai siswa mereka dan memberikan umpan balik.

Untuk memulai, mari kita definisikan beberapa konsep dasar dan terminologi yang akan kita gunakan sepanjang kurikulum.

## Bagaimana kita mendapatkan AI Generatif?

Meskipun _hype_ luar biasa yang diciptakan baru-baru ini oleh pengumuman model AI generatif, teknologi ini telah dikembangkan selama beberapa dekade, dengan upaya penelitian pertama yang dimulai sejak tahun 60-an. Kita sekarang berada di titik di mana AI memiliki kemampuan kognitif manusia, seperti percakapan yang ditunjukkan oleh misalnya [OpenAI ChatGPT](https://openai.com/chatgpt) atau [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), yang juga menggunakan model GPT untuk pencarian web Bing.

Mundur sedikit, prototipe pertama AI terdiri dari chatbot yang diketik, mengandalkan basis pengetahuan yang diekstraksi dari sekelompok ahli dan diwakili ke dalam komputer. Jawaban dalam basis pengetahuan dipicu oleh kata kunci yang muncul dalam teks input. Namun, segera menjadi jelas bahwa pendekatan seperti itu, menggunakan chatbot yang diketik, tidak dapat diukur dengan baik.

### Pendekatan statistik untuk AI: Pembelajaran Mesin

Titik balik tiba pada tahun 90-an, dengan penerapan pendekatan statistik untuk analisis teks. Ini mengarah pada pengembangan algoritma baru – yang dikenal sebagai pembelajaran mesin – yang mampu mempelajari pola dari data tanpa diprogram secara eksplisit. Pendekatan ini memungkinkan mesin untuk mensimulasikan pemahaman bahasa manusia: model statistik dilatih pada pasangan teks-label, memungkinkan model untuk mengklasifikasikan teks input yang tidak dikenal dengan label yang telah ditentukan sebelumnya yang mewakili niat pesan.

### Jaringan saraf dan asisten virtual modern

Dalam beberapa tahun terakhir, evolusi teknologi perangkat keras, yang mampu menangani jumlah data yang lebih besar dan perhitungan yang lebih kompleks, mendorong penelitian dalam AI, yang mengarah pada pengembangan algoritma pembelajaran mesin canggih yang dikenal sebagai jaringan saraf atau algoritma pembelajaran mendalam.

Jaringan saraf (dan khususnya Jaringan Saraf Rekuren – RNN) secara signifikan meningkatkan pemrosesan bahasa alami, memungkinkan representasi makna teks dengan cara yang lebih bermakna, menghargai konteks kata dalam kalimat.

Inilah teknologi yang mendukung asisten virtual yang lahir pada dekade pertama abad baru, sangat mahir dalam menafsirkan bahasa manusia, mengidentifikasi kebutuhan, dan melakukan tindakan untuk memuaskannya – seperti menjawab dengan skrip yang telah ditentukan sebelumnya atau mengonsumsi layanan pihak ketiga.

### Hari ini, AI Generatif

Jadi begitulah cara kita sampai ke AI Generatif hari ini, yang dapat dilihat sebagai subset dari pembelajaran mendalam.

Setelah beberapa dekade penelitian di bidang AI, arsitektur model baru – yang disebut _Transformer_ – mengatasi batasan RNN, mampu menerima urutan teks yang jauh lebih panjang sebagai input. Transformer didasarkan pada mekanisme perhatian, memungkinkan model untuk memberikan bobot yang berbeda pada input yang diterimanya, ‘lebih memperhatikan’ di mana informasi paling relevan terkonsentrasi, terlepas dari urutannya dalam urutan teks.

Sebagian besar model AI generatif terbaru – juga dikenal sebagai Model Bahasa Besar (LLM), karena mereka bekerja dengan input dan output tekstual – memang didasarkan pada arsitektur ini. Yang menarik dari model-model ini – yang dilatih pada sejumlah besar data tanpa label dari berbagai sumber seperti buku, artikel, dan situs web – adalah bahwa mereka dapat disesuaikan dengan berbagai tugas dan menghasilkan teks yang benar secara tata bahasa dengan kesan kreativitas. Jadi, tidak hanya mereka secara luar biasa meningkatkan kapasitas mesin untuk ‘memahami’ teks input, tetapi mereka memungkinkan kapasitas mereka untuk menghasilkan respons asli dalam bahasa manusia.

## Bagaimana model bahasa besar bekerja?

Dalam bab berikutnya kita akan menjelajahi berbagai jenis model AI Generatif, tetapi untuk saat ini mari kita lihat bagaimana model bahasa besar bekerja, dengan fokus pada model OpenAI GPT (Generative Pre-trained Transformer).

- **Tokenizer, teks ke angka**: Model Bahasa Besar menerima teks sebagai input dan menghasilkan teks sebagai output. Namun, sebagai model statistik, mereka bekerja jauh lebih baik dengan angka daripada urutan teks. Itulah mengapa setiap input ke model diproses oleh tokenizer, sebelum digunakan oleh model inti. Token adalah potongan teks – terdiri dari sejumlah karakter variabel, jadi tugas utama tokenizer adalah membagi input menjadi array token. Kemudian, setiap token dipetakan dengan indeks token, yang merupakan pengkodean bilangan bulat dari potongan teks asli.

- **Memprediksi token output**: Diberikan n token sebagai input (dengan max n bervariasi dari satu model ke model lainnya), model dapat memprediksi satu token sebagai output. Token ini kemudian dimasukkan ke dalam input iterasi berikutnya, dalam pola jendela yang berkembang, memungkinkan pengalaman pengguna yang lebih baik untuk mendapatkan satu (atau beberapa) kalimat sebagai jawaban. Ini menjelaskan mengapa, jika Anda pernah bermain dengan ChatGPT, Anda mungkin memperhatikan bahwa terkadang terlihat seperti berhenti di tengah kalimat.

- **Proses seleksi, distribusi probabilitas**: Token output dipilih oleh model sesuai dengan probabilitas kemunculannya setelah urutan teks saat ini. Ini karena model memprediksi distribusi probabilitas atas semua ‘token berikutnya’ yang mungkin, dihitung berdasarkan pelatihannya. Namun, tidak selalu token dengan probabilitas tertinggi dipilih dari distribusi yang dihasilkan. Sebuah derajat kebetulan ditambahkan ke pilihan ini, dengan cara bahwa model bertindak dengan cara non-deterministik - kita tidak mendapatkan output yang persis sama untuk input yang sama. Derajat kebetulan ini ditambahkan untuk mensimulasikan proses berpikir kreatif dan dapat disesuaikan menggunakan parameter model yang disebut suhu.

## Bagaimana startup kita dapat memanfaatkan Model Bahasa Besar?

Sekarang kita memiliki pemahaman yang lebih baik tentang cara kerja internal model bahasa besar, mari kita lihat beberapa contoh praktis dari tugas paling umum yang dapat mereka lakukan dengan cukup baik, dengan pandangan pada skenario bisnis kita. Kita mengatakan bahwa kemampuan utama dari Model Bahasa Besar adalah _menghasilkan teks dari awal, dimulai dari input tekstual, yang ditulis dalam bahasa alami_.

Tetapi jenis input dan output tekstual apa?
Input dari model bahasa besar dikenal sebagai prompt, sementara output dikenal sebagai completion, istilah yang merujuk pada mekanisme model untuk menghasilkan token berikutnya untuk melengkapi input saat ini. Kita akan mendalami apa itu prompt dan bagaimana merancangnya dengan cara untuk mendapatkan hasil terbaik dari model kita. Tetapi untuk saat ini, mari kita katakan bahwa prompt dapat mencakup:

- Sebuah **instruksi** yang menentukan jenis output yang kita harapkan dari model. Instruksi ini terkadang mungkin menyertakan beberapa contoh atau beberapa data tambahan.

  1. Meringkas artikel, buku, ulasan produk, dan lainnya, bersama dengan ekstraksi wawasan dari data tidak terstruktur.
  
  2. Ide kreatif dan desain artikel, esai, tugas, atau lainnya.
  
- Sebuah **pertanyaan**, diajukan dalam bentuk percakapan dengan agen.

- Sebuah potongan **teks untuk melengkapi**, yang secara implisit adalah permintaan untuk bantuan menulis.

- Sebuah potongan **kode** bersama dengan permintaan untuk menjelaskan dan mendokumentasikannya, atau komentar yang meminta untuk menghasilkan potongan kode yang melakukan tugas tertentu.

Contoh-contoh di atas cukup sederhana dan tidak dimaksudkan untuk menjadi demonstrasi yang lengkap dari kemampuan Model Bahasa Besar. Mereka dimaksudkan untuk menunjukkan potensi penggunaan AI generatif, khususnya tetapi tidak terbatas pada konteks pendidikan.

Selain itu, output dari model AI generatif tidak sempurna dan terkadang kreativitas model dapat bekerja melawannya, menghasilkan output yang merupakan kombinasi kata-kata yang dapat ditafsirkan oleh pengguna manusia sebagai mistifikasi realitas, atau dapat menjadi ofensif. AI generatif tidak cerdas - setidaknya dalam definisi kecerdasan yang lebih komprehensif, termasuk penalaran kritis dan kreatif atau kecerdasan emosional; itu tidak deterministik, dan itu tidak dapat dipercaya, karena fabrikasi, seperti referensi yang salah, konten, dan pernyataan, mungkin digabungkan dengan informasi yang benar, dan disajikan dengan cara yang meyakinkan dan percaya diri. Dalam pelajaran berikutnya, kita akan menangani semua keterbatasan ini dan kita akan melihat apa yang dapat kita lakukan untuk menguranginya.

## Tugas

Tugas Anda adalah membaca lebih lanjut tentang [AI generatif](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) dan mencoba mengidentifikasi area di mana Anda akan menambahkan AI generatif hari ini yang belum memilikinya. Bagaimana dampaknya berbeda dari melakukannya dengan cara "lama", bisakah Anda melakukan sesuatu yang tidak bisa Anda lakukan sebelumnya, atau apakah Anda lebih cepat? Tulis ringkasan 300 kata tentang bagaimana tampilan startup AI impian Anda dan sertakan judul seperti "Masalah", "Bagaimana saya akan menggunakan AI", "Dampak" dan opsi rencana bisnis.

Jika Anda melakukan tugas ini, Anda bahkan mungkin siap untuk mendaftar ke inkubator Microsoft, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) kami menawarkan kredit untuk Azure, OpenAI, mentoring dan banyak lagi, cek!

## Cek Pengetahuan

Apa yang benar tentang model bahasa besar?

1. Anda mendapatkan respons yang persis sama setiap saat.
2. Melakukan semuanya dengan sempurna, hebat dalam menambahkan angka, menghasilkan kode yang berfungsi, dll.
3. Respons dapat bervariasi meskipun menggunakan prompt yang sama. Juga bagus dalam memberikan draf awal sesuatu, baik itu teks atau kode. Tetapi Anda perlu meningkatkan hasilnya.

A: 3, LLM bersifat non-deterministik, respons bervariasi, namun, Anda dapat mengontrol variansnya melalui pengaturan suhu. Anda juga tidak boleh mengharapkannya melakukan segalanya dengan sempurna, ia ada untuk melakukan pekerjaan berat untuk Anda yang sering kali berarti Anda mendapatkan upaya pertama yang baik pada sesuatu yang perlu Anda tingkatkan secara bertahap.

## Kerja Hebat! Lanjutkan Perjalanan

Setelah menyelesaikan pelajaran ini, lihat [koleksi Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif Anda!

Lanjutkan ke Pelajaran 2 di mana kita akan melihat bagaimana [menjelajahi dan membandingkan berbagai jenis LLM](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang penting, disarankan untuk menggunakan jasa penerjemah manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah penafsiran yang timbul dari penggunaan terjemahan ini.