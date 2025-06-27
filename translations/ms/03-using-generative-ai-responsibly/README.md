<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-06-25T11:29:09+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "ms"
}
-->
# Menggunakan AI Generatif Secara Bertanggungjawab

> _Klik imej di atas untuk menonton video pelajaran ini_

Mudah untuk terpesona dengan AI dan AI generatif khususnya, tetapi anda perlu mempertimbangkan bagaimana anda akan menggunakannya secara bertanggungjawab. Anda perlu memikirkan perkara seperti bagaimana memastikan hasilnya adil, tidak berbahaya dan banyak lagi. Bab ini bertujuan untuk memberikan konteks yang disebutkan, apa yang perlu dipertimbangkan, dan bagaimana mengambil langkah aktif untuk memperbaiki penggunaan AI anda.

## Pengenalan

Pelajaran ini akan merangkumi:

- Mengapa anda harus mengutamakan AI Bertanggungjawab ketika membina aplikasi AI Generatif.
- Prinsip utama AI Bertanggungjawab dan bagaimana ia berkaitan dengan AI Generatif.
- Bagaimana untuk melaksanakan prinsip AI Bertanggungjawab ini melalui strategi dan alatan.

## Matlamat Pembelajaran

Selepas menyelesaikan pelajaran ini, anda akan tahu:

- Kepentingan AI Bertanggungjawab ketika membina aplikasi AI Generatif.
- Bila untuk memikirkan dan menerapkan prinsip utama AI Bertanggungjawab ketika membina aplikasi AI Generatif.
- Alat dan strategi apa yang tersedia untuk anda untuk melaksanakan konsep AI Bertanggungjawab.

## Prinsip AI Bertanggungjawab

Keterujaan terhadap AI Generatif tidak pernah lebih tinggi. Keterujaan ini telah membawa banyak pemaju baru, perhatian, dan pembiayaan ke ruang ini. Walaupun ini sangat positif bagi sesiapa yang ingin membina produk dan syarikat menggunakan AI Generatif, adalah penting kita bertindak dengan bertanggungjawab.

Sepanjang kursus ini, kami memberi tumpuan kepada membina startup kami dan produk pendidikan AI kami. Kami akan menggunakan prinsip AI Bertanggungjawab: Keadilan, Inklusif, Kebolehpercayaan/Keselamatan, Keselamatan & Privasi, Ketelusan dan Akauntabiliti. Dengan prinsip-prinsip ini, kami akan meneroka bagaimana ia berkaitan dengan penggunaan AI Generatif dalam produk kami.

## Mengapa Anda Perlu Mengutamakan AI Bertanggungjawab

Apabila membina produk, mengambil pendekatan yang berpusatkan manusia dengan mengutamakan kepentingan terbaik pengguna anda membawa kepada hasil yang terbaik.

Keunikan AI Generatif adalah kuasanya untuk mencipta jawapan, maklumat, panduan, dan kandungan yang berguna untuk pengguna. Ini boleh dilakukan tanpa banyak langkah manual yang boleh membawa kepada hasil yang sangat mengagumkan. Tanpa perancangan dan strategi yang betul, ia juga boleh malangnya membawa kepada beberapa hasil yang berbahaya untuk pengguna anda, produk anda, dan masyarakat secara keseluruhan.

Mari kita lihat beberapa (tetapi tidak semua) hasil yang berpotensi berbahaya ini:

### Halusinasi

Halusinasi adalah istilah yang digunakan untuk menggambarkan apabila LLM menghasilkan kandungan yang sama ada benar-benar tidak masuk akal atau sesuatu yang kita tahu salah secara fakta berdasarkan sumber maklumat lain.

Mari kita ambil contoh kita membina ciri untuk startup kita yang membolehkan pelajar mengemukakan soalan sejarah kepada model. Seorang pelajar bertanya soalan `Who was the sole survivor of Titanic?`

Model menghasilkan jawapan seperti yang di bawah:

Ini adalah jawapan yang sangat yakin dan menyeluruh. Malangnya, ia tidak betul. Walaupun dengan sedikit penyelidikan, seseorang akan mendapati terdapat lebih daripada seorang yang terselamat dari bencana Titanic. Bagi seorang pelajar yang baru memulakan penyelidikan mengenai topik ini, jawapan ini boleh cukup meyakinkan untuk tidak dipersoalkan dan dianggap sebagai fakta. Akibatnya boleh membawa kepada sistem AI yang tidak boleh dipercayai dan memberi kesan negatif kepada reputasi startup kami.

Dengan setiap iterasi mana-mana LLM yang diberikan, kami telah melihat peningkatan prestasi dalam meminimumkan halusinasi. Walaupun dengan peningkatan ini, kami sebagai pembina aplikasi dan pengguna masih perlu sedar akan batasan ini.

### Kandungan Berbahaya

Kami telah meliputi dalam bahagian sebelumnya apabila LLM menghasilkan jawapan yang salah atau tidak masuk akal. Risiko lain yang perlu kita sedari adalah apabila model memberikan respons dengan kandungan yang berbahaya.

Kandungan berbahaya boleh didefinisikan sebagai:

- Memberikan arahan atau menggalakkan mencederakan diri sendiri atau mencederakan kumpulan tertentu.
- Kandungan yang membenci atau menghina.
- Membimbing merancang sebarang jenis serangan atau tindakan keganasan.
- Memberikan arahan tentang cara mencari kandungan haram atau melakukan tindakan haram.
- Memaparkan kandungan seksual eksplisit.

Untuk startup kami, kami ingin memastikan kami mempunyai alat dan strategi yang betul untuk menghalang kandungan jenis ini daripada dilihat oleh pelajar.

### Kekurangan Keadilan

Keadilan didefinisikan sebagai "memastikan bahawa sistem AI bebas dari bias dan diskriminasi dan bahawa mereka melayan semua orang secara adil dan sama rata." Dalam dunia AI Generatif, kami ingin memastikan bahawa pandangan dunia yang mengecualikan kumpulan yang terpinggir tidak diperkuat oleh output model.

Jenis output ini bukan sahaja merosakkan untuk membina pengalaman produk yang positif untuk pengguna kami, tetapi mereka juga menyebabkan kerosakan masyarakat yang lebih lanjut. Sebagai pembina aplikasi, kita harus sentiasa menjaga pangkalan pengguna yang luas dan pelbagai dalam fikiran ketika membina penyelesaian dengan AI Generatif.

## Bagaimana Menggunakan AI Generatif Secara Bertanggungjawab

Sekarang kita telah mengenal pasti kepentingan AI Generatif yang Bertanggungjawab, mari kita lihat 4 langkah yang boleh kita ambil untuk membina penyelesaian AI kita dengan bertanggungjawab:

### Mengukur Potensi Bahaya

Dalam ujian perisian, kita menguji tindakan yang dijangkakan pengguna pada aplikasi. Begitu juga, menguji set perintah yang pelbagai yang mungkin akan digunakan oleh pengguna adalah cara yang baik untuk mengukur potensi bahaya.

Oleh kerana startup kami sedang membina produk pendidikan, adalah baik untuk menyediakan senarai perintah berkaitan pendidikan. Ini boleh meliputi subjek tertentu, fakta sejarah, dan perintah tentang kehidupan pelajar.

### Mengurangkan Potensi Bahaya

Sekarang adalah masa untuk mencari cara di mana kita boleh menghalang atau menghadkan potensi bahaya yang disebabkan oleh model dan responsnya. Kita boleh melihat ini dalam 4 lapisan berbeza:

- **Model**. Memilih model yang betul untuk kes penggunaan yang betul. Model yang lebih besar dan lebih kompleks seperti GPT-4 boleh menyebabkan lebih banyak risiko kandungan berbahaya apabila digunakan untuk kes penggunaan yang lebih kecil dan lebih spesifik. Menggunakan data latihan anda untuk menyelaraskan juga mengurangkan risiko kandungan berbahaya.

- **Sistem Keselamatan**. Sistem keselamatan adalah set alat dan konfigurasi pada platform yang menyajikan model yang membantu mengurangkan bahaya. Contoh ini adalah sistem penapisan kandungan pada perkhidmatan Azure OpenAI. Sistem juga harus mengesan serangan jailbreak dan aktiviti yang tidak diingini seperti permintaan dari bot.

- **Metaprompt**. Metaprompt dan grounding adalah cara kita boleh mengarahkan atau menghadkan model berdasarkan tingkah laku dan maklumat tertentu. Ini boleh menggunakan input sistem untuk menentukan had tertentu model. Selain itu, menyediakan output yang lebih relevan dengan skop atau domain sistem.

Ia juga boleh menggunakan teknik seperti Retrieval Augmented Generation (RAG) untuk membuat model hanya menarik maklumat dari pilihan sumber yang dipercayai. Terdapat pelajaran kemudian dalam kursus ini untuk [membina aplikasi carian](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Pengalaman Pengguna**. Lapisan terakhir adalah di mana pengguna berinteraksi secara langsung dengan model melalui antara muka aplikasi kami dengan cara tertentu. Dengan cara ini kita boleh merancang UI/UX untuk menghadkan pengguna pada jenis input yang boleh mereka hantar kepada model serta teks atau imej yang dipaparkan kepada pengguna. Apabila menyebarkan aplikasi AI, kita juga harus telus tentang apa yang aplikasi AI Generatif kita boleh dan tidak boleh lakukan.

Kami mempunyai satu pelajaran khusus untuk [Mereka Bentuk UX untuk Aplikasi AI](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Menilai model**. Bekerja dengan LLM boleh mencabar kerana kita tidak selalu mempunyai kawalan ke atas data yang model dilatih. Walau bagaimanapun, kita harus sentiasa menilai prestasi dan output model. Masih penting untuk mengukur ketepatan model, keserupaan, kekukuhan, dan relevansi output. Ini membantu memberikan ketelusan dan kepercayaan kepada pemegang kepentingan dan pengguna.

### Mengendalikan Penyelesaian AI Generatif yang Bertanggungjawab

Membina amalan operasi di sekitar aplikasi AI anda adalah peringkat akhir. Ini termasuk bekerjasama dengan bahagian lain dari startup kami seperti Legal dan Security untuk memastikan kami mematuhi semua polisi peraturan. Sebelum pelancaran, kami juga ingin membina rancangan sekitar penghantaran, pengendalian insiden, dan rollback untuk mencegah sebarang bahaya kepada pengguna kami daripada berkembang.

## Alat

Walaupun kerja membangunkan penyelesaian AI Bertanggungjawab mungkin kelihatan seperti banyak, ia adalah kerja yang berbaloi. Ketika bidang AI Generatif berkembang, lebih banyak alat untuk membantu pembangun mengintegrasikan tanggungjawab dengan cekap ke dalam aliran kerja mereka akan matang. Sebagai contoh, [Keselamatan Kandungan Azure AI](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) boleh membantu mengesan kandungan dan imej yang berbahaya melalui permintaan API.

## Semakan Pengetahuan

Apakah beberapa perkara yang perlu anda ambil berat untuk memastikan penggunaan AI yang bertanggungjawab?

1. Bahawa jawapannya betul.
1. Penggunaan berbahaya, bahawa AI tidak digunakan untuk tujuan jenayah.
1. Memastikan AI bebas dari bias dan diskriminasi.

A: 2 dan 3 adalah betul. AI Bertanggungjawab membantu anda mempertimbangkan bagaimana untuk mengurangkan kesan berbahaya dan bias dan banyak lagi.

## 🚀 Cabaran

Baca tentang [Keselamatan Kandungan Azure AI](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) dan lihat apa yang boleh anda terapkan untuk penggunaan anda.

## Kerja Hebat, Teruskan Pembelajaran Anda

Selepas menyelesaikan pelajaran ini, lihat koleksi Pembelajaran AI Generatif kami untuk terus meningkatkan pengetahuan AI Generatif anda!

Pergi ke Pelajaran 4 di mana kita akan melihat [Asas Kejuruteraan Prompt](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.