<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-06-25T11:28:42+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "id"
}
-->
# Menggunakan AI Generatif dengan Bertanggung Jawab

> _Klik gambar di atas untuk menonton video pelajaran ini_

Mudah untuk terpesona dengan AI, terutama AI generatif, tetapi Anda perlu mempertimbangkan bagaimana menggunakannya dengan bertanggung jawab. Anda perlu mempertimbangkan hal-hal seperti bagaimana memastikan outputnya adil, tidak berbahaya, dan lainnya. Bab ini bertujuan memberikan konteks yang disebutkan, apa yang harus dipertimbangkan, dan bagaimana mengambil langkah aktif untuk meningkatkan penggunaan AI Anda.

## Pengantar

Pelajaran ini akan mencakup:

- Mengapa Anda harus memprioritaskan AI yang Bertanggung Jawab saat membangun aplikasi AI Generatif.
- Prinsip-prinsip inti dari AI yang Bertanggung Jawab dan bagaimana mereka terkait dengan AI Generatif.
- Bagaimana menerapkan prinsip-prinsip AI yang Bertanggung Jawab melalui strategi dan alat.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan mengetahui:

- Pentingnya AI yang Bertanggung Jawab saat membangun aplikasi AI Generatif.
- Kapan harus memikirkan dan menerapkan prinsip-prinsip inti AI yang Bertanggung Jawab saat membangun aplikasi AI Generatif.
- Alat dan strategi apa yang tersedia bagi Anda untuk menerapkan konsep AI yang Bertanggung Jawab.

## Prinsip AI yang Bertanggung Jawab

Kegembiraan tentang AI Generatif belum pernah setinggi ini. Kegembiraan ini telah menarik banyak pengembang baru, perhatian, dan pendanaan ke bidang ini. Meskipun ini sangat positif bagi siapa pun yang ingin membangun produk dan perusahaan menggunakan AI Generatif, penting juga untuk melangkah dengan bertanggung jawab.

Sepanjang kursus ini, kami berfokus pada membangun startup kami dan produk pendidikan AI kami. Kami akan menggunakan prinsip-prinsip AI yang Bertanggung Jawab: Keadilan, Inklusivitas, Keandalan/Keamanan, Keamanan & Privasi, Transparansi, dan Akuntabilitas. Dengan prinsip-prinsip ini, kami akan menjelajahi bagaimana mereka terkait dengan penggunaan AI Generatif dalam produk kami.

## Mengapa Anda Harus Memprioritaskan AI yang Bertanggung Jawab

Saat membangun produk, mengambil pendekatan berpusat pada manusia dengan mempertimbangkan kepentingan terbaik pengguna Anda menghasilkan hasil terbaik.

Keunikan AI Generatif adalah kekuatannya untuk menciptakan jawaban, informasi, panduan, dan konten yang bermanfaat bagi pengguna. Ini dapat dilakukan tanpa banyak langkah manual yang dapat menghasilkan hasil yang sangat mengesankan. Tanpa perencanaan dan strategi yang tepat, ini juga dapat menyebabkan hasil yang merugikan bagi pengguna Anda, produk Anda, dan masyarakat secara keseluruhan.

Mari kita lihat beberapa (tetapi tidak semua) hasil yang berpotensi merugikan ini:

### Halusinasi

Halusinasi adalah istilah yang digunakan untuk menggambarkan ketika LLM menghasilkan konten yang sepenuhnya tidak masuk akal atau sesuatu yang kita tahu secara faktual salah berdasarkan sumber informasi lainnya.

Mari kita ambil contoh kita membangun fitur untuk startup kita yang memungkinkan siswa mengajukan pertanyaan sejarah kepada model. Seorang siswa mengajukan pertanyaan `Who was the sole survivor of Titanic?`

Model menghasilkan respons seperti yang di bawah ini:

Ini adalah jawaban yang sangat percaya diri dan menyeluruh. Sayangnya, ini salah. Bahkan dengan sedikit penelitian, seseorang akan menemukan bahwa ada lebih dari satu penyintas dari bencana Titanic. Bagi seorang siswa yang baru memulai penelitian tentang topik ini, jawaban ini dapat cukup meyakinkan untuk tidak dipertanyakan dan diperlakukan sebagai fakta. Konsekuensi dari ini dapat menyebabkan sistem AI menjadi tidak dapat diandalkan dan berdampak negatif pada reputasi startup kami.

Dengan setiap iterasi dari LLM yang diberikan, kami telah melihat peningkatan kinerja dalam meminimalkan halusinasi. Bahkan dengan peningkatan ini, kami sebagai pembangun aplikasi dan pengguna tetap perlu menyadari keterbatasan ini.

### Konten Berbahaya

Kami telah membahas di bagian sebelumnya ketika LLM menghasilkan respons yang salah atau tidak masuk akal. Risiko lain yang perlu kita sadari adalah ketika model merespons dengan konten berbahaya.

Konten berbahaya dapat didefinisikan sebagai:

- Memberikan instruksi atau mendorong tindakan menyakiti diri sendiri atau kelompok tertentu.
- Konten yang penuh kebencian atau merendahkan.
- Membimbing perencanaan serangan atau tindakan kekerasan apa pun.
- Memberikan instruksi tentang cara menemukan konten ilegal atau melakukan tindakan ilegal.
- Menampilkan konten seksual eksplisit.

Untuk startup kami, kami ingin memastikan bahwa kami memiliki alat dan strategi yang tepat untuk mencegah jenis konten ini dilihat oleh siswa.

### Kurangnya Keadilan

Keadilan didefinisikan sebagai “memastikan bahwa sistem AI bebas dari bias dan diskriminasi dan memperlakukan semua orang dengan adil dan setara.” Dalam dunia AI Generatif, kami ingin memastikan bahwa pandangan dunia eksklusif dari kelompok yang terpinggirkan tidak diperkuat oleh output model.

Jenis output ini tidak hanya merusak pengalaman produk positif bagi pengguna kami, tetapi juga menyebabkan kerugian sosial lebih lanjut. Sebagai pembangun aplikasi, kita harus selalu mempertimbangkan basis pengguna yang luas dan beragam saat membangun solusi dengan AI Generatif.

## Cara Menggunakan AI Generatif dengan Bertanggung Jawab

Sekarang kita telah mengidentifikasi pentingnya AI Generatif yang Bertanggung Jawab, mari kita lihat 4 langkah yang dapat kita ambil untuk membangun solusi AI kita dengan bertanggung jawab:

### Ukur Potensi Kerugian

Dalam pengujian perangkat lunak, kita menguji tindakan yang diharapkan dari pengguna pada aplikasi. Demikian pula, menguji berbagai prompt yang paling mungkin digunakan oleh pengguna adalah cara yang baik untuk mengukur potensi kerugian.

Karena startup kami sedang membangun produk pendidikan, akan baik untuk menyiapkan daftar prompt terkait pendidikan. Ini bisa mencakup subjek tertentu, fakta sejarah, dan prompt tentang kehidupan siswa.

### Mitigasi Potensi Kerugian

Sekarang saatnya menemukan cara di mana kita dapat mencegah atau membatasi potensi kerugian yang disebabkan oleh model dan responsnya. Kita dapat melihat ini dalam 4 lapisan berbeda:

- **Model**. Memilih model yang tepat untuk kasus penggunaan yang tepat. Model yang lebih besar dan lebih kompleks seperti GPT-4 dapat menyebabkan risiko konten berbahaya lebih besar ketika diterapkan pada kasus penggunaan yang lebih kecil dan lebih spesifik. Menggunakan data pelatihan Anda untuk menyempurnakan juga mengurangi risiko konten berbahaya.

- **Sistem Keamanan**. Sistem keamanan adalah serangkaian alat dan konfigurasi pada platform yang melayani model yang membantu mengurangi kerugian. Contohnya adalah sistem penyaringan konten pada layanan Azure OpenAI. Sistem juga harus mendeteksi serangan jailbreak dan aktivitas yang tidak diinginkan seperti permintaan dari bot.

- **Metaprompt**. Metaprompt dan grounding adalah cara kita dapat mengarahkan atau membatasi model berdasarkan perilaku dan informasi tertentu. Ini bisa menggunakan input sistem untuk mendefinisikan batas tertentu dari model. Selain itu, memberikan output yang lebih relevan dengan cakupan atau domain sistem.

Ini juga bisa menggunakan teknik seperti Retrieval Augmented Generation (RAG) untuk membuat model hanya menarik informasi dari pilihan sumber terpercaya. Ada pelajaran nanti dalam kursus ini untuk [membangun aplikasi pencarian](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Pengalaman Pengguna**. Lapisan terakhir adalah tempat pengguna berinteraksi langsung dengan model melalui antarmuka aplikasi kami dengan cara tertentu. Dengan cara ini kita dapat merancang UI/UX untuk membatasi pengguna pada jenis input yang dapat mereka kirim ke model serta teks atau gambar yang ditampilkan kepada pengguna. Saat menerapkan aplikasi AI, kita juga harus transparan tentang apa yang dapat dan tidak dapat dilakukan oleh aplikasi AI Generatif kita.

Kami memiliki pelajaran khusus untuk [Merancang UX untuk Aplikasi AI](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Evaluasi model**. Bekerja dengan LLM bisa menjadi tantangan karena kita tidak selalu memiliki kontrol atas data yang digunakan untuk melatih model. Meskipun demikian, kita harus selalu mengevaluasi kinerja dan output model. Penting untuk mengukur akurasi, kesamaan, keterkaitan, dan relevansi output model. Ini membantu memberikan transparansi dan kepercayaan kepada pemangku kepentingan dan pengguna.

### Mengoperasikan solusi AI Generatif yang Bertanggung Jawab

Membangun praktik operasional di sekitar aplikasi AI Anda adalah tahap akhir. Ini termasuk bermitra dengan bagian lain dari startup kami seperti Legal dan Keamanan untuk memastikan kami mematuhi semua kebijakan regulasi. Sebelum meluncurkan, kami juga ingin membangun rencana di sekitar pengiriman, menangani insiden, dan rollback untuk mencegah kerugian bagi pengguna kami dari pertumbuhan.

## Alat

Meskipun pekerjaan mengembangkan solusi AI yang Bertanggung Jawab mungkin tampak banyak, itu adalah pekerjaan yang sepadan dengan usaha. Seiring pertumbuhan area AI Generatif, lebih banyak alat untuk membantu pengembang mengintegrasikan tanggung jawab dengan efisien ke dalam alur kerja mereka akan matang. Misalnya, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) dapat membantu mendeteksi konten dan gambar berbahaya melalui permintaan API.

## Uji Pengetahuan

Apa saja hal yang perlu Anda perhatikan untuk memastikan penggunaan AI yang bertanggung jawab?

1. Bahwa jawabannya benar.
1. Penggunaan yang berbahaya, bahwa AI tidak digunakan untuk tujuan kriminal.
1. Memastikan AI bebas dari bias dan diskriminasi.

A: 2 dan 3 benar. AI yang Bertanggung Jawab membantu Anda mempertimbangkan bagaimana mengurangi efek berbahaya dan bias dan lebih banyak lagi.

## 🚀 Tantangan

Baca tentang [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) dan lihat apa yang dapat Anda adopsi untuk penggunaan Anda.

## Kerja Hebat, Lanjutkan Pembelajaran Anda

Setelah menyelesaikan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif Anda!

Lanjutkan ke Pelajaran 4 di mana kita akan melihat [Dasar-dasar Teknik Pembuatan Prompt](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk mencapai akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.