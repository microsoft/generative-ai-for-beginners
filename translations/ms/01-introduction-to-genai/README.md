<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-06-25T10:01:04+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "ms"
}
-->
# Pengenalan kepada Generative AI dan Model Bahasa Besar

_(Klik imej di atas untuk menonton video pelajaran ini)_

Generative AI adalah kecerdasan buatan yang mampu menjana teks, imej dan jenis kandungan lain. Apa yang menjadikannya teknologi yang hebat ialah ia mendemokrasikan AI, sesiapa sahaja boleh menggunakannya dengan hanya arahan teks, satu ayat yang ditulis dalam bahasa semula jadi. Anda tidak perlu belajar bahasa seperti Java atau SQL untuk mencapai sesuatu yang berharga, yang anda perlukan hanyalah menggunakan bahasa anda, nyatakan apa yang anda mahukan dan keluar cadangan daripada model AI. Aplikasi dan kesannya adalah besar, anda menulis atau memahami laporan, menulis aplikasi dan banyak lagi, semuanya dalam beberapa saat.

Dalam kurikulum ini, kami akan meneroka bagaimana permulaan kami memanfaatkan generative AI untuk membuka senario baharu dalam dunia pendidikan dan bagaimana kami menangani cabaran yang tidak dapat dielakkan yang berkaitan dengan implikasi sosial aplikasinya dan had teknologi.

## Pengenalan

Pelajaran ini akan merangkumi:

- Pengenalan kepada senario perniagaan: idea dan misi permulaan kami.
- Generative AI dan bagaimana kita sampai ke landskap teknologi semasa.
- Cara kerja dalaman model bahasa besar.
- Keupayaan utama dan kes penggunaan praktikal Model Bahasa Besar.

## Matlamat Pembelajaran

Selepas melengkapkan pelajaran ini, anda akan memahami:

- Apa itu generative AI dan bagaimana Model Bahasa Besar berfungsi.
- Bagaimana anda boleh memanfaatkan model bahasa besar untuk kes penggunaan yang berbeza, dengan fokus pada senario pendidikan.

## Senario: permulaan pendidikan kami

Kecerdasan Buatan Generatif (AI) mewakili puncak teknologi AI, mendorong sempadan apa yang pernah dianggap mustahil. Model AI generatif mempunyai beberapa keupayaan dan aplikasi, tetapi untuk kurikulum ini kami akan meneroka bagaimana ia merevolusikan pendidikan melalui permulaan fiksyen. Kami akan merujuk kepada permulaan ini sebagai _permulaan kami_. Permulaan kami bekerja dalam domain pendidikan dengan pernyataan misi yang bercita-cita tinggi

> _meningkatkan kebolehcapaian dalam pembelajaran, pada skala global, memastikan akses pendidikan yang saksama dan menyediakan pengalaman pembelajaran yang diperibadikan kepada setiap pelajar, mengikut keperluan mereka_.

Pasukan permulaan kami sedar bahawa kami tidak akan dapat mencapai matlamat ini tanpa memanfaatkan salah satu alat paling berkuasa pada zaman moden – Model Bahasa Besar (LLM).

Generative AI dijangka merevolusikan cara kita belajar dan mengajar hari ini, dengan pelajar mempunyai guru maya yang tersedia 24 jam sehari yang menyediakan sejumlah besar maklumat dan contoh, dan guru dapat memanfaatkan alat inovatif untuk menilai pelajar mereka dan memberikan maklum balas.

Untuk memulakan, mari kita tentukan beberapa konsep dan istilah asas yang akan kita gunakan sepanjang kurikulum.

## Bagaimana kita mendapatkan Generative AI?

Walaupun _hype_ luar biasa yang dicipta baru-baru ini oleh pengumuman model AI generatif, teknologi ini telah berdekad-dekad dalam pembikinan, dengan usaha penyelidikan pertama bermula pada tahun 60-an. Kami kini berada pada tahap dengan AI yang mempunyai keupayaan kognitif manusia, seperti perbualan seperti yang ditunjukkan oleh contohnya [OpenAI ChatGPT](https://openai.com/chatgpt) atau [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), yang juga menggunakan model GPT untuk carian web perbualan Bing.

Melangkah ke belakang sedikit, prototaip AI yang paling awal terdiri daripada chatbot yang ditaip, bergantung pada pangkalan pengetahuan yang diekstrak daripada sekumpulan pakar dan diwakili ke dalam komputer. Jawapan dalam pangkalan pengetahuan dicetuskan oleh kata kunci yang muncul dalam teks input.
Walau bagaimanapun, ia tidak lama kemudian menjadi jelas bahawa pendekatan sedemikian, menggunakan chatbot yang ditaip, tidak berskala dengan baik.

### Pendekatan statistik kepada AI: Pembelajaran Mesin

Titik perubahan tiba pada tahun 90-an, dengan penerapan pendekatan statistik kepada analisis teks. Ini membawa kepada pembangunan algoritma baharu – dikenali sebagai pembelajaran mesin – yang mampu mempelajari corak daripada data tanpa diprogramkan secara eksplisit. Pendekatan ini membolehkan mesin mensimulasikan pemahaman bahasa manusia: model statistik dilatih pada pasangan teks-label, membolehkan model mengklasifikasikan teks input yang tidak diketahui dengan label yang telah ditetapkan yang mewakili niat mesej.

### Rangkaian neural dan pembantu maya moden

Dalam beberapa tahun kebelakangan ini, evolusi teknologi perkakasan, yang mampu mengendalikan sejumlah besar data dan pengiraan yang lebih kompleks, menggalakkan penyelidikan dalam AI, membawa kepada pembangunan algoritma pembelajaran mesin lanjutan yang dikenali sebagai rangkaian neural atau algoritma pembelajaran mendalam.

Rangkaian neural (dan khususnya Rangkaian Neural Berulang – RNN) meningkatkan pemprosesan bahasa semula jadi dengan ketara, membolehkan perwakilan makna teks dengan cara yang lebih bermakna, menilai konteks perkataan dalam ayat.

Ini adalah teknologi yang menggerakkan pembantu maya yang lahir pada dekad pertama abad baru, sangat mahir dalam mentafsir bahasa manusia, mengenal pasti keperluan, dan melaksanakan tindakan untuk memuaskannya – seperti menjawab dengan skrip yang telah ditetapkan atau menggunakan perkhidmatan pihak ketiga.

### Hari ini, Generative AI

Jadi begitulah cara kita sampai ke Generative AI hari ini, yang boleh dilihat sebagai subset pembelajaran mendalam.

Selepas berdekad-dekad penyelidikan dalam bidang AI, seni bina model baharu – yang dipanggil _Transformer_ – mengatasi had RNN, yang mampu mendapatkan urutan teks yang lebih panjang sebagai input. Transformers adalah berdasarkan mekanisme perhatian, membolehkan model memberikan berat yang berbeza kepada input yang diterimanya, 'memberi lebih perhatian' di mana maklumat yang paling relevan tertumpu, tanpa mengira susunannya dalam urutan teks.

Kebanyakan model AI generatif baru-baru ini – juga dikenali sebagai Model Bahasa Besar (LLM), kerana ia bekerja dengan input dan output teks – sememangnya berdasarkan seni bina ini. Apa yang menarik tentang model ini – dilatih pada sejumlah besar data tanpa label dari sumber yang pelbagai seperti buku, artikel dan laman web – ialah ia boleh disesuaikan dengan pelbagai jenis tugas dan menjana teks yang betul secara tatabahasa dengan semblance of creativity. Jadi, bukan sahaja mereka meningkatkan keupayaan mesin untuk 'memahami' teks input, tetapi mereka membolehkan keupayaan mereka untuk menjana respons asal dalam bahasa manusia.

## Bagaimana model bahasa besar berfungsi?

Dalam bab seterusnya kita akan meneroka pelbagai jenis model AI Generatif, tetapi buat masa ini mari kita lihat bagaimana model bahasa besar berfungsi, dengan fokus pada model OpenAI GPT (Generative Pre-trained Transformer).

- **Tokenizer, teks kepada nombor**: Model Bahasa Besar menerima teks sebagai input dan menjana teks sebagai output. Walau bagaimanapun, sebagai model statistik, mereka bekerja dengan lebih baik dengan nombor daripada urutan teks. Itulah sebabnya setiap input kepada model diproses oleh tokenizer, sebelum digunakan oleh model teras. Token adalah sebahagian daripada teks – terdiri daripada bilangan aksara yang berubah-ubah, jadi tugas utama tokenizer ialah membahagikan input kepada array token. Kemudian, setiap token dipetakan dengan indeks token, yang merupakan pengekodan integer bagi bahagian teks asal.

- **Meramal token output**: Diberikan n token sebagai input (dengan maksimum n berbeza dari satu model ke model lain), model dapat meramal satu token sebagai output. Token ini kemudian dimasukkan ke dalam input iterasi seterusnya, dalam corak tetingkap yang berkembang, membolehkan pengalaman pengguna yang lebih baik untuk mendapatkan satu (atau berbilang) ayat sebagai jawapan. Ini menjelaskan mengapa, jika anda pernah bermain dengan ChatGPT, anda mungkin perasan bahawa kadangkala ia kelihatan seperti berhenti di tengah-tengah ayat.

- **Proses pemilihan, taburan kebarangkalian**: Token output dipilih oleh model mengikut kebarangkalian ia berlaku selepas urutan teks semasa. Ini kerana model meramal taburan kebarangkalian ke atas semua 'token seterusnya' yang mungkin, dikira berdasarkan latihannya. Walau bagaimanapun, tidak selalu token dengan kebarangkalian tertinggi dipilih daripada taburan yang terhasil. Tahap rawak ditambah kepada pilihan ini, dengan cara model bertindak secara tidak deterministik - kita tidak mendapat output yang sama untuk input yang sama. Tahap rawak ini ditambah untuk mensimulasikan proses pemikiran kreatif dan ia boleh diselaraskan menggunakan parameter model yang dipanggil suhu.

## Bagaimana permulaan kami boleh memanfaatkan Model Bahasa Besar?

Sekarang kita mempunyai pemahaman yang lebih baik tentang cara kerja dalaman model bahasa besar, mari kita lihat beberapa contoh praktikal tugas paling biasa yang boleh mereka lakukan dengan baik, dengan mata kepada senario perniagaan kami. Kami mengatakan bahawa keupayaan utama Model Bahasa Besar ialah _menjana teks dari awal, bermula dari input teks, yang ditulis dalam bahasa semula jadi_.

Tetapi apakah jenis input dan output teks?
Input model bahasa besar dikenali sebagai prompt, manakala output dikenali sebagai completion, istilah yang merujuk kepada mekanisme model untuk menjana token seterusnya untuk melengkapkan input semasa. Kami akan mendalami apa itu prompt dan cara mereka bentuknya dengan cara untuk mendapatkan hasil terbaik daripada model kami. Tetapi buat masa ini, katakan sahaja bahawa prompt mungkin termasuk:

- Arahan yang menentukan jenis output yang kami jangkakan daripada model. Arahan ini kadangkala mungkin mengandungi beberapa contoh atau beberapa data tambahan.

  1. Ringkasan artikel, buku, ulasan produk dan banyak lagi, bersama-sama dengan pengekstrakan pandangan daripada data tidak berstruktur.

  2. Ideasi kreatif dan reka bentuk artikel, esei, tugasan atau lebih.

- Soalan, ditanya dalam bentuk perbualan dengan ejen.

- Sebahagian teks untuk dilengkapkan, yang secara tersirat adalah permintaan untuk bantuan penulisan.

- Sebahagian kod bersama-sama dengan permintaan untuk menerangkan dan mendokumentasikannya, atau komen yang meminta untuk menjana sepotong kod yang melaksanakan tugas tertentu.

Contoh di atas agak mudah dan tidak bertujuan untuk menjadi demonstrasi lengkap keupayaan Model Bahasa Besar. Mereka bertujuan untuk menunjukkan potensi menggunakan generative AI, khususnya tetapi tidak terhad kepada konteks pendidikan.

Juga, output model AI generatif tidak sempurna dan kadangkala kreativiti model boleh menentangnya, menghasilkan output yang merupakan gabungan perkataan yang boleh ditafsirkan oleh pengguna manusia sebagai penyamaran realiti, atau ia boleh menyinggung perasaan. Generative AI tidak pintar - sekurang-kurangnya dalam definisi kecerdasan yang lebih komprehensif, termasuk penaakulan kritikal dan kreatif atau kecerdasan emosi; ia tidak deterministik, dan ia tidak boleh dipercayai, kerana fabrikasi, seperti rujukan yang salah, kandungan, dan kenyataan, mungkin digabungkan dengan maklumat yang betul, dan dibentangkan dengan cara yang meyakinkan dan yakin. Dalam pelajaran berikut, kami akan menangani semua batasan ini dan kami akan melihat apa yang boleh kami lakukan untuk mengurangkannya.

## Tugasan

Tugasan anda ialah membaca lebih lanjut mengenai [generative AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) dan cuba mengenal pasti kawasan di mana anda ingin menambah generative AI hari ini yang belum memilikinya. Bagaimana impaknya akan berbeza daripada melakukannya dengan cara "lama", bolehkah anda melakukan sesuatu yang tidak boleh anda lakukan sebelum ini, atau adakah anda lebih cepat? Tulis ringkasan 300 perkataan tentang bagaimana permulaan AI impian anda akan kelihatan dan sertakan tajuk seperti "Masalah", "Bagaimana saya akan menggunakan AI", "Kesan" dan secara opsional rancangan perniagaan.

Jika anda melakukan tugasan ini, anda mungkin bersedia untuk memohon kepada inkubator Microsoft, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) kami menawarkan kredit untuk kedua-dua Azure, OpenAI, mentoring dan banyak lagi, lihatlah!

## Semakan Pengetahuan

Apa yang benar tentang model bahasa besar?

1. Anda mendapat respons yang sama setiap kali.
2. Ia melakukan perkara dengan sempurna, hebat dalam menambah nombor, menghasilkan kod berfungsi dll.
3. Respons mungkin berbeza walaupun menggunakan prompt yang sama. Ia juga hebat dalam memberikan anda draf pertama sesuatu, sama ada teks atau kod. Tetapi anda perlu memperbaiki hasilnya.

A: 3, LLM adalah tidak deterministik, respons berbeza, walau bagaimanapun, anda boleh mengawal variansnya melalui tetapan suhu. Anda juga tidak sepatutnya mengharapkannya melakukan perkara dengan sempurna, ia di sini untuk melakukan kerja berat untuk anda yang selalunya bermaksud anda mendapat percubaan pertama yang baik pada sesuatu yang anda perlu perbaiki secara beransur-ansur.

## Kerja Bagus! Teruskan Perjalanan

Selepas melengkapkan pelajaran ini, lihat [Koleksi Pembelajaran Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Generative AI anda!

Pergi ke Pelajaran 2 di mana kita akan melihat bagaimana untuk [meneroka dan membandingkan jenis LLM yang berbeza](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.