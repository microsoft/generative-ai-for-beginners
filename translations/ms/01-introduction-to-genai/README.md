<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-05-19T13:28:20+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "ms"
}
-->
# Pengenalan kepada AI Generatif dan Model Bahasa Besar

_(Klik imej di atas untuk menonton video pelajaran ini)_

AI generatif ialah kecerdasan buatan yang mampu menjana teks, imej dan jenis kandungan lain. Apa yang menjadikannya teknologi yang hebat ialah ia mendemokrasikan AI, sesiapa sahaja boleh menggunakannya dengan hanya satu arahan teks, satu ayat yang ditulis dalam bahasa semula jadi. Tidak perlu anda belajar bahasa seperti Java atau SQL untuk mencapai sesuatu yang berbaloi, semua yang anda perlukan ialah menggunakan bahasa anda, nyatakan apa yang anda mahu dan keluar cadangan daripada model AI. Aplikasi dan impak untuk ini adalah besar, anda menulis atau memahami laporan, menulis aplikasi dan banyak lagi, semuanya dalam masa beberapa saat.

Dalam kurikulum ini, kami akan meneroka bagaimana permulaan kami memanfaatkan AI generatif untuk membuka senario baharu dalam dunia pendidikan dan bagaimana kami menangani cabaran yang tidak dapat dielakkan yang dikaitkan dengan implikasi sosial aplikasinya dan had teknologi.

## Pengenalan

Pelajaran ini akan merangkumi:

- Pengenalan kepada senario perniagaan: idea dan misi permulaan kami.
- AI generatif dan bagaimana kami mendarat di landskap teknologi semasa.
- Kerja dalaman model bahasa besar.
- Keupayaan utama dan kes penggunaan praktikal Model Bahasa Besar.

## Matlamat Pembelajaran

Selepas melengkapkan pelajaran ini, anda akan memahami:

- Apa itu AI generatif dan bagaimana Model Bahasa Besar berfungsi.
- Bagaimana anda boleh memanfaatkan model bahasa besar untuk kes penggunaan yang berbeza, dengan tumpuan kepada senario pendidikan.

## Senario: permulaan pendidikan kami

Kecerdasan Buatan (AI) Generatif mewakili puncak teknologi AI, menolak sempadan apa yang pernah dianggap mustahil. Model AI generatif mempunyai beberapa keupayaan dan aplikasi, tetapi untuk kurikulum ini kami akan meneroka bagaimana ia merevolusikan pendidikan melalui permulaan fiksyen. Kami akan merujuk kepada permulaan ini sebagai _permulaan kami_. Permulaan kami bekerja dalam domain pendidikan dengan pernyataan misi yang bercita-cita tinggi

> _meningkatkan kebolehcapaian dalam pembelajaran, pada skala global, memastikan akses yang saksama kepada pendidikan dan menyediakan pengalaman pembelajaran yang diperibadikan kepada setiap pelajar, mengikut keperluan mereka_.

Pasukan permulaan kami sedar kami tidak akan dapat mencapai matlamat ini tanpa memanfaatkan salah satu alat paling berkuasa zaman moden – Model Bahasa Besar (LLM).

AI generatif dijangka merevolusikan cara kita belajar dan mengajar hari ini, dengan pelajar mempunyai guru maya yang tersedia 24 jam sehari yang menyediakan sejumlah besar maklumat dan contoh, dan guru dapat memanfaatkan alat inovatif untuk menilai pelajar mereka dan memberikan maklum balas.

Untuk bermula, mari kita tentukan beberapa konsep asas dan terminologi yang akan kita gunakan sepanjang kurikulum.

## Bagaimana kita mendapat AI Generatif?

Walaupun _hype_ luar biasa yang dicipta baru-baru ini oleh pengumuman model AI generatif, teknologi ini telah dibangunkan selama beberapa dekad, dengan usaha penyelidikan pertama bermula sejak tahun 60-an. Kita kini berada pada titik dengan AI yang mempunyai keupayaan kognitif manusia, seperti perbualan seperti yang ditunjukkan oleh contohnya [OpenAI ChatGPT](https://openai.com/chatgpt) atau [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), yang juga menggunakan model GPT untuk perbualan carian web Bing.

Mundur sedikit, prototaip pertama AI terdiri daripada chatbot yang ditaip, bergantung pada pangkalan pengetahuan yang diekstrak daripada sekumpulan pakar dan diwakili ke dalam komputer. Jawapan dalam pangkalan pengetahuan dicetuskan oleh kata kunci yang muncul dalam teks input. Walau bagaimanapun, tidak lama kemudian jelas bahawa pendekatan sedemikian, menggunakan chatbot yang ditaip, tidak dapat diskalakan dengan baik.

### Pendekatan statistik kepada AI: Pembelajaran Mesin

Titik perubahan tiba semasa tahun 90-an, dengan penggunaan pendekatan statistik untuk analisis teks. Ini membawa kepada pembangunan algoritma baharu – dikenali sebagai pembelajaran mesin – yang mampu mempelajari corak daripada data tanpa diprogramkan secara eksplisit. Pendekatan ini membolehkan mesin mensimulasikan pemahaman bahasa manusia: model statistik dilatih pada pasangan teks-label, membolehkan model mengklasifikasikan teks input yang tidak diketahui dengan label yang telah ditetapkan yang mewakili niat mesej.

### Rangkaian neural dan pembantu maya moden

Dalam beberapa tahun kebelakangan ini, evolusi teknologi perkakasan, yang mampu mengendalikan sejumlah besar data dan pengiraan yang lebih kompleks, menggalakkan penyelidikan dalam AI, membawa kepada pembangunan algoritma pembelajaran mesin lanjutan yang dikenali sebagai rangkaian neural atau algoritma pembelajaran mendalam.

Rangkaian neural (dan khususnya Rangkaian Neural Berulang – RNN) meningkatkan pemprosesan bahasa semula jadi dengan ketara, membolehkan perwakilan makna teks dengan cara yang lebih bermakna, menilai konteks perkataan dalam ayat.

Ini adalah teknologi yang menggerakkan pembantu maya yang lahir dalam dekad pertama abad baharu, sangat mahir dalam mentafsirkan bahasa manusia, mengenal pasti keperluan dan melakukan tindakan untuk memuaskannya – seperti menjawab dengan skrip yang telah ditetapkan atau menggunakan perkhidmatan pihak ketiga.

### Hari ini, AI Generatif

Begitulah cara kami sampai kepada AI Generatif hari ini, yang boleh dilihat sebagai subset pembelajaran mendalam.

Selepas beberapa dekad penyelidikan dalam bidang AI, seni bina model baharu – dipanggil _Transformer_ – mengatasi had RNN, dapat mendapatkan urutan teks yang lebih panjang sebagai input. Transformer adalah berdasarkan mekanisme perhatian, membolehkan model memberikan berat yang berbeza kepada input yang diterimanya, 'memberikan lebih perhatian' di mana maklumat yang paling relevan tertumpu, tanpa mengira susunannya dalam urutan teks.

Kebanyakan model AI generatif baru-baru ini – juga dikenali sebagai Model Bahasa Besar (LLM), kerana ia berfungsi dengan input dan output teks – sememangnya berdasarkan seni bina ini. Apa yang menarik tentang model ini – dilatih pada sejumlah besar data tidak berlabel daripada sumber pelbagai seperti buku, artikel dan laman web – ialah ia boleh disesuaikan dengan pelbagai tugas dan menjana teks yang betul secara tatabahasa dengan kelihatan kreatif. Jadi, bukan sahaja mereka sangat meningkatkan keupayaan mesin untuk 'memahami' teks input, tetapi mereka membolehkan keupayaan mereka untuk menjana respons asal dalam bahasa manusia.

## Bagaimana model bahasa besar berfungsi?

Dalam bab seterusnya kita akan meneroka jenis model AI Generatif yang berbeza, tetapi buat masa ini mari kita lihat bagaimana model bahasa besar berfungsi, dengan fokus pada model OpenAI GPT (Generative Pre-trained Transformer).

- **Penambah, teks kepada nombor**: Model Bahasa Besar menerima teks sebagai input dan menjana teks sebagai output. Walau bagaimanapun, sebagai model statistik, mereka bekerja lebih baik dengan nombor daripada urutan teks. Itulah sebabnya setiap input kepada model diproses oleh penambah, sebelum digunakan oleh model teras. Token ialah cebisan teks – terdiri daripada bilangan aksara yang berubah-ubah, jadi tugas utama penambah ialah membahagikan input kepada tatasusunan token. Kemudian, setiap token dipetakan dengan indeks token, yang merupakan pengekodan integer bagi cebisan teks asal.

- **Meramalkan token output**: Diberi n token sebagai input (dengan maksimum n berbeza dari satu model ke model yang lain), model dapat meramalkan satu token sebagai output. Token ini kemudian dimasukkan ke dalam input lelaran seterusnya, dalam corak tetingkap yang berkembang, membolehkan pengalaman pengguna yang lebih baik untuk mendapatkan satu (atau berbilang) ayat sebagai jawapan. Ini menjelaskan mengapa, jika anda pernah bermain dengan ChatGPT, anda mungkin perasan bahawa kadangkala ia kelihatan seperti berhenti di tengah-tengah ayat.

- **Proses pemilihan, taburan kebarangkalian**: Token output dipilih oleh model mengikut kebarangkalian ia berlaku selepas urutan teks semasa. Ini kerana model meramalkan taburan kebarangkalian ke atas semua 'token seterusnya' yang mungkin, dikira berdasarkan latihannya. Walau bagaimanapun, tidak selalu token dengan kebarangkalian tertinggi dipilih daripada taburan yang terhasil. Satu darjah rawak ditambah kepada pilihan ini, dengan cara model bertindak secara tidak deterministik - kita tidak mendapat output yang sama tepat untuk input yang sama. Darjah rawak ini ditambah untuk mensimulasikan proses pemikiran kreatif dan ia boleh ditala menggunakan parameter model yang dipanggil suhu.

## Bagaimana permulaan kami boleh memanfaatkan Model Bahasa Besar?

Sekarang kita mempunyai pemahaman yang lebih baik tentang kerja dalaman model bahasa besar, mari kita lihat beberapa contoh praktikal tugas yang paling biasa mereka boleh lakukan dengan baik, dengan mata kepada senario perniagaan kita. Kami berkata bahawa keupayaan utama Model Bahasa Besar ialah _menjana teks dari awal, bermula dari input teks, yang ditulis dalam bahasa semula jadi_.

Tetapi apakah jenis input dan output teks?
Input model bahasa besar dikenali sebagai arahan, manakala output dikenali sebagai penyelesaian, istilah yang merujuk kepada mekanisme model menjana token seterusnya untuk melengkapkan input semasa. Kami akan menyelidiki apa itu arahan dan cara mereka bentuknya dengan cara untuk mendapatkan yang terbaik daripada model kami. Tetapi buat masa ini, katakanlah arahan mungkin termasuk:

- **Arahan** yang menentukan jenis output yang kami jangkakan daripada model. Arahan ini kadangkala mungkin menggabungkan beberapa contoh atau beberapa data tambahan.

  1. Ringkasan artikel, buku, ulasan produk dan banyak lagi, bersama-sama dengan pengekstrakan pandangan daripada data tidak berstruktur.

  2. Ideasi kreatif dan reka bentuk artikel, esei, tugasan atau lebih.

- **Soalan**, ditanya dalam bentuk perbualan dengan ejen.

- Cebisan **teks untuk melengkapkan**, yang secara tersirat adalah permintaan untuk bantuan penulisan.

- Cebisan **kod** bersama-sama dengan permintaan untuk menerangkan dan mendokumentasikannya, atau ulasan yang meminta untuk menjana sekeping kod yang melaksanakan tugas tertentu.

Contoh di atas agak mudah dan tidak bertujuan untuk menjadi demonstrasi yang lengkap tentang keupayaan Model Bahasa Besar. Mereka bertujuan untuk menunjukkan potensi penggunaan AI generatif, khususnya tetapi tidak terhad kepada konteks pendidikan.

Selain itu, output model AI generatif tidak sempurna dan kadangkala kreativiti model boleh berfungsi melawannya, menghasilkan output yang merupakan gabungan perkataan yang boleh ditafsirkan oleh pengguna manusia sebagai pemalsuan realiti, atau ia boleh menjadi menyinggung perasaan. AI generatif tidak pintar - sekurang-kurangnya dalam definisi kecerdasan yang lebih komprehensif, termasuk penaakulan kritikal dan kreatif atau kecerdasan emosi; ia tidak deterministik, dan ia tidak boleh dipercayai, kerana fabrikasi, seperti rujukan yang salah, kandungan dan kenyataan, mungkin digabungkan dengan maklumat yang betul, dan dibentangkan dengan cara yang meyakinkan dan yakin. Dalam pelajaran berikut, kami akan menangani semua had ini dan kami akan melihat apa yang boleh kami lakukan untuk mengurangkannya.

## Tugasan

Tugasan anda ialah membaca lebih lanjut tentang [AI generatif](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) dan cuba mengenal pasti kawasan di mana anda akan menambah AI generatif hari ini yang tidak memilikinya. Bagaimana kesannya berbeza daripada melakukannya dengan cara "lama", bolehkah anda melakukan sesuatu yang anda tidak boleh lakukan sebelum ini, atau adakah anda lebih pantas? Tulis ringkasan 300 perkataan tentang bagaimana permulaan AI impian anda akan kelihatan dan sertakan tajuk seperti "Masalah", "Bagaimana saya akan menggunakan AI", "Impak" dan secara pilihan pelan perniagaan.

Jika anda melakukan tugas ini, anda mungkin bersedia untuk memohon kepada inkubator Microsoft, [Microsoft untuk Permulaan Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) kami menawarkan kredit untuk kedua-dua Azure, OpenAI, bimbingan dan banyak lagi, lihatlah!

## Semakan pengetahuan

Apa yang benar tentang model bahasa besar?

1. Anda mendapat respons yang sama tepat setiap kali.
1. Ia melakukan perkara dengan sempurna, hebat dalam menambah nombor, menghasilkan kod yang berfungsi dan sebagainya.
1. Respons mungkin berbeza walaupun menggunakan arahan yang sama. Ia juga bagus untuk memberi anda draf pertama sesuatu, sama ada teks atau kod. Tetapi anda perlu meningkatkan hasilnya.

A: 3, LLM adalah tidak deterministik, respons berbeza, walau bagaimanapun, anda boleh mengawal variansnya melalui tetapan suhu. Anda juga tidak sepatutnya mengharapkannya melakukan perkara dengan sempurna, ia ada di sini untuk melakukan kerja berat untuk anda yang selalunya bermakna anda mendapat percubaan pertama yang baik pada sesuatu yang perlu anda tingkatkan secara beransur-ansur.

## Kerja Hebat! Teruskan Perjalanan

Selepas melengkapkan pelajaran ini, lihat [koleksi Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif anda!

Pergi ke Pelajaran 2 di mana kami akan melihat bagaimana untuk [meneroka dan membandingkan jenis LLM yang berbeza](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.