<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-05-19T14:45:47+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "id"
}
-->
# Menggunakan AI Generatif Secara Bertanggung Jawab

> _Klik gambar di atas untuk melihat video dari pelajaran ini_

Mudah untuk terpesona dengan AI dan AI generatif pada khususnya, tetapi Anda perlu mempertimbangkan bagaimana Anda akan menggunakannya dengan bertanggung jawab. Anda perlu mempertimbangkan hal-hal seperti bagaimana memastikan hasilnya adil, tidak berbahaya, dan lainnya. Bab ini bertujuan untuk memberikan konteks yang disebutkan, apa yang harus dipertimbangkan, dan bagaimana mengambil langkah aktif untuk meningkatkan penggunaan AI Anda.

## Pendahuluan

Pelajaran ini akan mencakup:

- Mengapa Anda harus memprioritaskan AI Bertanggung Jawab saat membangun aplikasi AI Generatif.
- Prinsip-prinsip inti AI Bertanggung Jawab dan bagaimana mereka berhubungan dengan AI Generatif.
- Cara menerapkan prinsip-prinsip AI Bertanggung Jawab ini melalui strategi dan alat.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan mengetahui:

- Pentingnya AI Bertanggung Jawab saat membangun aplikasi AI Generatif.
- Kapan harus memikirkan dan menerapkan prinsip-prinsip inti AI Bertanggung Jawab saat membangun aplikasi AI Generatif.
- Alat dan strategi apa yang tersedia bagi Anda untuk menerapkan konsep AI Bertanggung Jawab.

## Prinsip AI Bertanggung Jawab

Kegembiraan AI Generatif belum pernah setinggi ini. Kegembiraan ini telah membawa banyak pengembang baru, perhatian, dan pendanaan ke ruang ini. Meskipun ini sangat positif bagi siapa pun yang ingin membangun produk dan perusahaan menggunakan AI Generatif, penting juga untuk melanjutkan dengan bertanggung jawab.

Sepanjang kursus ini, kami berfokus pada membangun startup kami dan produk pendidikan AI kami. Kami akan menggunakan prinsip-prinsip AI Bertanggung Jawab: Keadilan, Inklusivitas, Keandalan/Keamanan, Keamanan & Privasi, Transparansi, dan Akuntabilitas. Dengan prinsip-prinsip ini, kami akan menjelajahi bagaimana mereka berhubungan dengan penggunaan AI Generatif dalam produk kami.

## Mengapa Anda Harus Memprioritaskan AI Bertanggung Jawab

Saat membangun produk, mengambil pendekatan yang berpusat pada manusia dengan menjaga kepentingan terbaik pengguna Anda menghasilkan hasil terbaik.

Keunikan AI Generatif adalah kemampuannya untuk menciptakan jawaban, informasi, panduan, dan konten yang bermanfaat bagi pengguna. Ini dapat dilakukan tanpa banyak langkah manual yang dapat menghasilkan hasil yang sangat mengesankan. Tanpa perencanaan dan strategi yang tepat, ini juga dapat sayangnya menyebabkan beberapa hasil berbahaya bagi pengguna Anda, produk Anda, dan masyarakat secara keseluruhan.

Mari kita lihat beberapa (tetapi tidak semua) dari hasil yang berpotensi berbahaya ini:

### Halusinasi

Halusinasi adalah istilah yang digunakan untuk menggambarkan ketika LLM menghasilkan konten yang sepenuhnya tidak masuk akal atau sesuatu yang kita tahu secara faktual salah berdasarkan sumber informasi lain.

Mari kita ambil contoh kita membangun fitur untuk startup kita yang memungkinkan siswa mengajukan pertanyaan sejarah kepada model. Seorang siswa mengajukan pertanyaan `Who was the sole survivor of Titanic?`

Model menghasilkan respons seperti yang di bawah ini:

Ini adalah jawaban yang sangat percaya diri dan menyeluruh. Sayangnya, itu salah. Bahkan dengan jumlah penelitian minimal, seseorang akan menemukan bahwa ada lebih dari satu korban selamat dari bencana Titanic. Bagi seorang siswa yang baru memulai penelitian tentang topik ini, jawaban ini bisa cukup meyakinkan untuk tidak dipertanyakan dan diperlakukan sebagai fakta. Konsekuensi dari ini dapat menyebabkan sistem AI menjadi tidak dapat diandalkan dan berdampak negatif pada reputasi startup kami.

Dengan setiap iterasi dari LLM tertentu, kami telah melihat peningkatan kinerja dalam meminimalkan halusinasi. Meskipun dengan peningkatan ini, kami sebagai pembangun aplikasi dan pengguna masih perlu menyadari keterbatasan ini.

### Konten Berbahaya

Kami membahas di bagian sebelumnya ketika LLM menghasilkan respons yang salah atau tidak masuk akal. Risiko lain yang perlu kita sadari adalah ketika model merespons dengan konten berbahaya.

Konten berbahaya dapat didefinisikan sebagai:

- Memberikan instruksi atau mendorong tindakan menyakiti diri sendiri atau kelompok tertentu.
- Konten yang penuh kebencian atau merendahkan.
- Membimbing perencanaan serangan atau tindakan kekerasan.
- Memberikan instruksi tentang cara menemukan konten ilegal atau melakukan tindakan ilegal.
- Menampilkan konten yang eksplisit secara seksual.

Untuk startup kami, kami ingin memastikan bahwa kami memiliki alat dan strategi yang tepat untuk mencegah jenis konten ini dilihat oleh siswa.

### Kurangnya Keadilan

Keadilan didefinisikan sebagai "memastikan bahwa sistem AI bebas dari bias dan diskriminasi dan bahwa mereka memperlakukan semua orang secara adil dan setara." Dalam dunia AI Generatif, kita ingin memastikan bahwa pandangan dunia yang eksklusif dari kelompok-kelompok yang terpinggirkan tidak diperkuat oleh keluaran model.

Jenis keluaran ini tidak hanya merusak pengalaman produk positif bagi pengguna kami, tetapi juga menyebabkan kerugian sosial lebih lanjut. Sebagai pembangun aplikasi, kita harus selalu menjaga basis pengguna yang luas dan beragam dalam pikiran saat membangun solusi dengan AI Generatif.

## Cara Menggunakan AI Generatif Secara Bertanggung Jawab

Sekarang kita telah mengidentifikasi pentingnya AI Generatif Bertanggung Jawab, mari kita lihat 4 langkah yang dapat kita ambil untuk membangun solusi AI kita secara bertanggung jawab:

### Mengukur Potensi Bahaya

Dalam pengujian perangkat lunak, kita menguji tindakan yang diharapkan dari pengguna pada aplikasi. Demikian pula, menguji serangkaian permintaan yang beragam yang kemungkinan besar akan digunakan oleh pengguna adalah cara yang baik untuk mengukur potensi bahaya.

Karena startup kami sedang membangun produk pendidikan, akan baik untuk mempersiapkan daftar permintaan terkait pendidikan. Ini bisa mencakup subjek tertentu, fakta sejarah, dan permintaan tentang kehidupan siswa.

### Mengurangi Potensi Bahaya

Sekarang saatnya menemukan cara di mana kita dapat mencegah atau membatasi potensi bahaya yang disebabkan oleh model dan responsnya. Kita dapat melihat ini dalam 4 lapisan berbeda:

- **Model**. Memilih model yang tepat untuk kasus penggunaan yang tepat. Model yang lebih besar dan lebih kompleks seperti GPT-4 dapat menyebabkan lebih banyak risiko konten berbahaya ketika diterapkan pada kasus penggunaan yang lebih kecil dan lebih spesifik. Menggunakan data pelatihan Anda untuk menyempurnakan juga mengurangi risiko konten berbahaya.

- **Sistem Keamanan**. Sistem keamanan adalah seperangkat alat dan konfigurasi pada platform yang melayani model yang membantu mengurangi bahaya. Contohnya adalah sistem penyaringan konten pada layanan Azure OpenAI. Sistem juga harus mendeteksi serangan jailbreak dan aktivitas yang tidak diinginkan seperti permintaan dari bot.

- **Metaprompt**. Metaprompts dan grounding adalah cara kita dapat mengarahkan atau membatasi model berdasarkan perilaku dan informasi tertentu. Ini bisa menggunakan input sistem untuk mendefinisikan batasan tertentu dari model. Selain itu, memberikan keluaran yang lebih relevan dengan ruang lingkup atau domain sistem.

Ini juga bisa menggunakan teknik seperti Retrieval Augmented Generation (RAG) untuk membuat model hanya menarik informasi dari sumber yang terpercaya. Ada pelajaran nanti dalam kursus ini untuk [membangun aplikasi pencarian](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Pengalaman Pengguna**. Lapisan terakhir adalah di mana pengguna berinteraksi langsung dengan model melalui antarmuka aplikasi kami dengan cara tertentu. Dengan cara ini kita dapat merancang UI/UX untuk membatasi pengguna pada jenis input yang dapat mereka kirim ke model serta teks atau gambar yang ditampilkan kepada pengguna. Saat menerapkan aplikasi AI, kita juga harus transparan tentang apa yang dapat dan tidak dapat dilakukan oleh aplikasi AI Generatif kami.

Kami memiliki seluruh pelajaran yang didedikasikan untuk [Merancang UX untuk Aplikasi AI](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Evaluasi model**. Bekerja dengan LLM bisa menjadi tantangan karena kita tidak selalu memiliki kendali atas data yang digunakan untuk melatih model. Terlepas dari itu, kita harus selalu mengevaluasi kinerja dan keluaran model. Masih penting untuk mengukur akurasi model, kesamaan, grounding, dan relevansi keluaran. Ini membantu memberikan transparansi dan kepercayaan kepada pemangku kepentingan dan pengguna.

### Mengoperasikan solusi AI Generatif yang Bertanggung Jawab

Membangun praktik operasional di sekitar aplikasi AI Anda adalah tahap akhir. Ini termasuk bekerja sama dengan bagian lain dari startup kami seperti Legal dan Keamanan untuk memastikan kami mematuhi semua kebijakan regulasi. Sebelum meluncurkan, kami juga ingin membangun rencana seputar pengiriman, penanganan insiden, dan rollback untuk mencegah kerugian bagi pengguna kami dari pertumbuhan.

## Alat

Meskipun pekerjaan mengembangkan solusi AI Bertanggung Jawab mungkin tampak banyak, ini adalah pekerjaan yang sangat berharga. Seiring pertumbuhan area AI Generatif, lebih banyak alat untuk membantu pengembang secara efisien mengintegrasikan tanggung jawab ke dalam alur kerja mereka akan matang. Misalnya, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) dapat membantu mendeteksi konten dan gambar berbahaya melalui permintaan API.

## Pemeriksaan Pengetahuan

Apa saja hal yang perlu Anda perhatikan untuk memastikan penggunaan AI yang bertanggung jawab?

1. Bahwa jawabannya benar.
1. Penggunaan yang berbahaya, bahwa AI tidak digunakan untuk tujuan kriminal.
1. Memastikan AI bebas dari bias dan diskriminasi.

A: 2 dan 3 benar. AI Bertanggung Jawab membantu Anda mempertimbangkan bagaimana mengurangi efek berbahaya dan bias dan lebih banyak lagi.

## 🚀 Tantangan

Baca tentang [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) dan lihat apa yang dapat Anda adopsi untuk penggunaan Anda.

## Kerja Hebat, Lanjutkan Pembelajaran Anda

Setelah menyelesaikan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif Anda!

Lanjutkan ke Pelajaran 4 di mana kita akan melihat [Dasar-dasar Rekayasa Prompt](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.