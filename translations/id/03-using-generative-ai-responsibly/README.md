<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d57fad773cbeb69c5dd62e65c34200d",
  "translation_date": "2025-10-17T20:44:12+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "id"
}
-->
# Menggunakan AI Generatif Secara Bertanggung Jawab

[![Menggunakan AI Generatif Secara Bertanggung Jawab](../../../translated_images/03-lesson-banner.1ed56067a452d97709d51f6cc8b6953918b2287132f4909ade2008c936cd4af9.id.png)](https://youtu.be/YOp-e1GjZdA?si=7Wv4wu3x44L1DCVj)

> _Klik gambar di atas untuk menonton video pelajaran ini_

AI, khususnya AI generatif, memang sangat menarik, tetapi Anda perlu mempertimbangkan bagaimana menggunakannya secara bertanggung jawab. Anda harus memikirkan cara memastikan outputnya adil, tidak berbahaya, dan lainnya. Bab ini bertujuan untuk memberikan konteks yang disebutkan, hal-hal yang perlu dipertimbangkan, dan langkah-langkah aktif yang dapat diambil untuk meningkatkan penggunaan AI Anda.

## Pendahuluan

Pelajaran ini akan membahas:

- Mengapa Anda harus memprioritaskan AI yang Bertanggung Jawab saat membangun aplikasi AI Generatif.
- Prinsip-prinsip inti AI yang Bertanggung Jawab dan bagaimana kaitannya dengan AI Generatif.
- Cara menerapkan prinsip-prinsip AI yang Bertanggung Jawab melalui strategi dan alat.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan mengetahui:

- Pentingnya AI yang Bertanggung Jawab saat membangun aplikasi AI Generatif.
- Kapan harus memikirkan dan menerapkan prinsip-prinsip inti AI yang Bertanggung Jawab saat membangun aplikasi AI Generatif.
- Alat dan strategi apa saja yang tersedia untuk menerapkan konsep AI yang Bertanggung Jawab.

## Prinsip AI yang Bertanggung Jawab

Antusiasme terhadap AI Generatif tidak pernah setinggi ini. Antusiasme ini telah menarik banyak pengembang baru, perhatian, dan pendanaan ke bidang ini. Meskipun ini sangat positif bagi siapa saja yang ingin membangun produk dan perusahaan menggunakan AI Generatif, penting juga untuk melangkah dengan penuh tanggung jawab.

Sepanjang kursus ini, kita akan fokus pada pembangunan startup dan produk pendidikan AI kita. Kita akan menggunakan prinsip-prinsip AI yang Bertanggung Jawab: Keadilan, Inklusivitas, Keandalan/Keamanan, Keamanan & Privasi, Transparansi, dan Akuntabilitas. Dengan prinsip-prinsip ini, kita akan mengeksplorasi bagaimana kaitannya dengan penggunaan AI Generatif dalam produk kita.

## Mengapa Anda Harus Memprioritaskan AI yang Bertanggung Jawab

Saat membangun produk, pendekatan yang berpusat pada manusia dengan mengutamakan kepentingan terbaik pengguna Anda akan menghasilkan hasil terbaik.

Keunikan AI Generatif adalah kemampuannya untuk menciptakan jawaban, informasi, panduan, dan konten yang bermanfaat bagi pengguna. Hal ini dapat dilakukan tanpa banyak langkah manual yang dapat menghasilkan hasil yang sangat mengesankan. Namun, tanpa perencanaan dan strategi yang tepat, hal ini juga dapat menyebabkan hasil yang merugikan bagi pengguna Anda, produk Anda, dan masyarakat secara keseluruhan.

Mari kita lihat beberapa (tetapi tidak semua) potensi hasil yang merugikan ini:

### Halusinasi

Halusinasi adalah istilah yang digunakan untuk menggambarkan ketika LLM menghasilkan konten yang sepenuhnya tidak masuk akal atau sesuatu yang kita tahu salah secara faktual berdasarkan sumber informasi lainnya.

Sebagai contoh, kita membangun fitur untuk startup kita yang memungkinkan siswa mengajukan pertanyaan sejarah kepada model. Seorang siswa bertanya, `Siapa satu-satunya yang selamat dari Titanic?`

Model menghasilkan jawaban seperti di bawah ini:

![Prompt mengatakan "Siapa satu-satunya yang selamat dari Titanic"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

> _(Sumber: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

Ini adalah jawaban yang sangat percaya diri dan mendetail. Sayangnya, jawaban ini salah. Bahkan dengan sedikit penelitian, seseorang akan menemukan bahwa ada lebih dari satu orang yang selamat dari bencana Titanic. Bagi seorang siswa yang baru mulai meneliti topik ini, jawaban ini bisa cukup meyakinkan untuk tidak dipertanyakan dan dianggap sebagai fakta. Konsekuensi dari hal ini dapat menyebabkan sistem AI menjadi tidak dapat diandalkan dan berdampak negatif pada reputasi startup kita.

Dengan setiap iterasi dari LLM tertentu, kita telah melihat peningkatan kinerja dalam meminimalkan halusinasi. Meskipun ada peningkatan ini, kita sebagai pembangun aplikasi dan pengguna tetap perlu menyadari keterbatasan ini.

### Konten Berbahaya

Kita telah membahas di bagian sebelumnya ketika LLM menghasilkan respons yang salah atau tidak masuk akal. Risiko lain yang perlu kita sadari adalah ketika model merespons dengan konten yang berbahaya.

Konten berbahaya dapat didefinisikan sebagai:

- Memberikan instruksi atau mendorong tindakan menyakiti diri sendiri atau kelompok tertentu.
- Konten yang penuh kebencian atau merendahkan.
- Membimbing perencanaan serangan atau tindakan kekerasan apa pun.
- Memberikan instruksi tentang cara menemukan konten ilegal atau melakukan tindakan ilegal.
- Menampilkan konten yang eksplisit secara seksual.

Untuk startup kita, kita ingin memastikan bahwa kita memiliki alat dan strategi yang tepat untuk mencegah jenis konten ini dilihat oleh siswa.

### Kurangnya Keadilan

Keadilan didefinisikan sebagai “memastikan bahwa sistem AI bebas dari bias dan diskriminasi serta memperlakukan semua orang secara adil dan setara.” Dalam dunia AI Generatif, kita ingin memastikan bahwa pandangan dunia yang eksklusif terhadap kelompok yang terpinggirkan tidak diperkuat oleh output model.

Jenis output ini tidak hanya merusak pengalaman produk yang positif bagi pengguna kita, tetapi juga menyebabkan kerugian sosial lebih lanjut. Sebagai pembangun aplikasi, kita harus selalu mempertimbangkan basis pengguna yang luas dan beragam saat membangun solusi dengan AI Generatif.

## Cara Menggunakan AI Generatif Secara Bertanggung Jawab

Sekarang kita telah mengidentifikasi pentingnya AI Generatif yang Bertanggung Jawab, mari kita lihat 4 langkah yang dapat kita ambil untuk membangun solusi AI kita secara bertanggung jawab:

![Siklus Mitigasi](../../../translated_images/mitigate-cycle.babcd5a5658e1775d5f2cb47f2ff305cca090400a72d98d0f9e57e9db5637c72.id.png)

### Mengukur Potensi Kerugian

Dalam pengujian perangkat lunak, kita menguji tindakan yang diharapkan dari pengguna pada aplikasi. Demikian pula, menguji serangkaian prompt yang beragam yang kemungkinan besar akan digunakan oleh pengguna adalah cara yang baik untuk mengukur potensi kerugian.

Karena startup kita sedang membangun produk pendidikan, akan baik untuk menyiapkan daftar prompt terkait pendidikan. Ini bisa mencakup subjek tertentu, fakta sejarah, dan prompt tentang kehidupan siswa.

### Mengurangi Potensi Kerugian

Sekarang saatnya menemukan cara di mana kita dapat mencegah atau membatasi potensi kerugian yang disebabkan oleh model dan responsnya. Kita dapat melihat ini dalam 4 lapisan berbeda:

![Lapisan Mitigasi](../../../translated_images/mitigation-layers.377215120b9a1159a8c3982c6bbcf41b6adf8c8fa04ce35cbaeeb13b4979cdfc.id.png)

- **Model**. Memilih model yang tepat untuk kasus penggunaan yang tepat. Model yang lebih besar dan lebih kompleks seperti GPT-4 dapat menimbulkan risiko konten berbahaya yang lebih besar ketika diterapkan pada kasus penggunaan yang lebih kecil dan lebih spesifik. Menggunakan data pelatihan Anda untuk fine-tuning juga mengurangi risiko konten berbahaya.

- **Sistem Keamanan**. Sistem keamanan adalah seperangkat alat dan konfigurasi pada platform yang melayani model yang membantu mengurangi kerugian. Contohnya adalah sistem penyaringan konten pada layanan Azure OpenAI. Sistem juga harus mendeteksi serangan jailbreak dan aktivitas yang tidak diinginkan seperti permintaan dari bot.

- **Metaprompt**. Metaprompt dan grounding adalah cara kita dapat mengarahkan atau membatasi model berdasarkan perilaku dan informasi tertentu. Ini bisa berupa penggunaan input sistem untuk mendefinisikan batasan tertentu dari model. Selain itu, memberikan output yang lebih relevan dengan cakupan atau domain sistem.

Ini juga bisa berupa penggunaan teknik seperti Retrieval Augmented Generation (RAG) untuk membuat model hanya mengambil informasi dari pilihan sumber yang terpercaya. Ada pelajaran nanti dalam kursus ini tentang [membangun aplikasi pencarian](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Pengalaman Pengguna**. Lapisan terakhir adalah tempat pengguna berinteraksi langsung dengan model melalui antarmuka aplikasi kita dengan cara tertentu. Dengan cara ini kita dapat merancang UI/UX untuk membatasi pengguna pada jenis input yang dapat mereka kirim ke model serta teks atau gambar yang ditampilkan kepada pengguna. Saat meluncurkan aplikasi AI, kita juga harus transparan tentang apa yang dapat dan tidak dapat dilakukan oleh aplikasi AI Generatif kita.

Kami memiliki pelajaran khusus tentang [Merancang UX untuk Aplikasi AI](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Evaluasi model**. Bekerja dengan LLM bisa menjadi tantangan karena kita tidak selalu memiliki kendali atas data yang digunakan untuk melatih model. Meskipun demikian, kita harus selalu mengevaluasi kinerja dan output model. Penting untuk mengukur akurasi, kesamaan, keterkaitan, dan relevansi output model. Hal ini membantu memberikan transparansi dan kepercayaan kepada pemangku kepentingan dan pengguna.

### Mengoperasikan solusi AI Generatif yang Bertanggung Jawab

Membangun praktik operasional di sekitar aplikasi AI Anda adalah tahap akhir. Ini mencakup bekerja sama dengan bagian lain dari startup kita seperti Legal dan Keamanan untuk memastikan kita mematuhi semua kebijakan regulasi. Sebelum meluncurkan, kita juga ingin membangun rencana seputar pengiriman, penanganan insiden, dan rollback untuk mencegah kerugian kepada pengguna kita.

## Alat

Meskipun pekerjaan mengembangkan solusi AI yang Bertanggung Jawab tampaknya banyak, ini adalah pekerjaan yang sangat berharga. Seiring berkembangnya area AI Generatif, semakin banyak alat untuk membantu pengembang mengintegrasikan tanggung jawab ke dalam alur kerja mereka secara efisien akan berkembang. Misalnya, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) dapat membantu mendeteksi konten dan gambar berbahaya melalui permintaan API.

## Uji Pengetahuan

Apa saja hal yang perlu Anda perhatikan untuk memastikan penggunaan AI yang bertanggung jawab?

1. Bahwa jawabannya benar.
1. Penggunaan yang berbahaya, bahwa AI tidak digunakan untuk tujuan kriminal.
1. Memastikan AI bebas dari bias dan diskriminasi.

A: 2 dan 3 benar. AI yang Bertanggung Jawab membantu Anda mempertimbangkan cara mengurangi efek berbahaya dan bias serta lainnya.

## 🚀 Tantangan

Pelajari lebih lanjut tentang [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) dan lihat apa yang dapat Anda adopsi untuk penggunaan Anda.

## Kerja Hebat, Lanjutkan Pembelajaran Anda

Setelah menyelesaikan pelajaran ini, lihat [koleksi Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Anda tentang AI Generatif!

Lanjutkan ke Pelajaran 4 di mana kita akan membahas [Dasar-dasar Teknik Prompt](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.