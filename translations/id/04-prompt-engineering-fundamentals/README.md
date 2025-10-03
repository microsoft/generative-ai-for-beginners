<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8b3cb38518cf4fe7714d2f5e74dfa3eb",
  "translation_date": "2025-10-03T09:57:10+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "id"
}
-->
# Dasar-Dasar Rekayasa Prompt

[![Dasar-Dasar Rekayasa Prompt](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.id.png)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Pendahuluan
Modul ini mencakup konsep dan teknik penting untuk membuat prompt yang efektif dalam model AI generatif. Cara Anda menulis prompt untuk LLM juga berpengaruh. Prompt yang dirancang dengan hati-hati dapat menghasilkan respons yang lebih berkualitas. Tapi apa sebenarnya istilah seperti _prompt_ dan _rekayasa prompt_ itu? Dan bagaimana cara meningkatkan _input prompt_ yang dikirim ke LLM? Pertanyaan-pertanyaan ini akan kita coba jawab dalam bab ini dan bab berikutnya.

_AI generatif_ mampu menciptakan konten baru (misalnya, teks, gambar, audio, kode, dll.) sebagai respons terhadap permintaan pengguna. Hal ini dicapai dengan menggunakan _Model Bahasa Besar_ seperti seri GPT ("Generative Pre-trained Transformer") dari OpenAI yang dilatih untuk menggunakan bahasa alami dan kode.

Pengguna kini dapat berinteraksi dengan model-model ini menggunakan paradigma yang sudah dikenal seperti obrolan, tanpa memerlukan keahlian teknis atau pelatihan. Model-model ini berbasis _prompt_ - pengguna mengirimkan input teks (prompt) dan mendapatkan respons AI (penyelesaian). Mereka kemudian dapat "mengobrol dengan AI" secara iteratif, dalam percakapan multi-putaran, menyempurnakan prompt mereka hingga respons sesuai dengan harapan.

"Prompt" kini menjadi antarmuka _pemrograman utama_ untuk aplikasi AI generatif, memberi tahu model apa yang harus dilakukan dan memengaruhi kualitas respons yang dikembalikan. "Rekayasa Prompt" adalah bidang studi yang berkembang pesat yang berfokus pada _desain dan optimasi_ prompt untuk menghasilkan respons yang konsisten dan berkualitas dalam skala besar.

## Tujuan Pembelajaran

Dalam pelajaran ini, kita akan mempelajari apa itu Rekayasa Prompt, mengapa hal itu penting, dan bagaimana kita dapat membuat prompt yang lebih efektif untuk model dan tujuan aplikasi tertentu. Kita akan memahami konsep inti dan praktik terbaik untuk rekayasa prompt - serta mempelajari lingkungan "sandbox" interaktif Jupyter Notebooks di mana kita dapat melihat konsep-konsep ini diterapkan pada contoh nyata.

Pada akhir pelajaran ini, kita akan dapat:

1. Menjelaskan apa itu rekayasa prompt dan mengapa hal itu penting.
2. Mendeskripsikan komponen-komponen dari sebuah prompt dan bagaimana mereka digunakan.
3. Mempelajari praktik terbaik dan teknik untuk rekayasa prompt.
4. Menerapkan teknik yang dipelajari pada contoh nyata, menggunakan endpoint OpenAI.

## Istilah Kunci

Rekayasa Prompt: Praktik merancang dan menyempurnakan input untuk membimbing model AI agar menghasilkan output yang diinginkan.  
Tokenisasi: Proses mengubah teks menjadi unit-unit kecil, yang disebut token, yang dapat dipahami dan diproses oleh model.  
LLM yang Disetel Instruksi: Model Bahasa Besar (LLM) yang telah disetel dengan instruksi spesifik untuk meningkatkan akurasi dan relevansi responsnya.

## Sandbox Pembelajaran

Rekayasa prompt saat ini lebih merupakan seni daripada ilmu. Cara terbaik untuk meningkatkan intuisi kita tentang hal ini adalah dengan _berlatih lebih banyak_ dan mengadopsi pendekatan coba-coba yang menggabungkan keahlian domain aplikasi dengan teknik yang direkomendasikan dan optimasi spesifik model.

Notebook Jupyter yang menyertai pelajaran ini menyediakan lingkungan _sandbox_ di mana Anda dapat mencoba apa yang Anda pelajari - baik saat Anda belajar maupun sebagai bagian dari tantangan kode di akhir. Untuk menjalankan latihan, Anda akan membutuhkan:

1. **Kunci API Azure OpenAI** - endpoint layanan untuk LLM yang telah diterapkan.  
2. **Runtime Python** - tempat Notebook dapat dijalankan.  
3. **Variabel Lingkungan Lokal** - _selesaikan langkah-langkah [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) sekarang untuk bersiap_.  

Notebook ini dilengkapi dengan latihan _pemula_ - tetapi Anda didorong untuk menambahkan bagian _Markdown_ (deskripsi) dan _Kode_ (permintaan prompt) Anda sendiri untuk mencoba lebih banyak contoh atau ide - dan membangun intuisi Anda untuk desain prompt.

## Panduan Bergambar

Ingin mendapatkan gambaran besar tentang apa yang dibahas dalam pelajaran ini sebelum Anda mendalami? Lihat panduan bergambar ini, yang memberikan gambaran tentang topik utama yang dibahas dan poin-poin penting untuk Anda pikirkan di setiap bagian. Peta jalan pelajaran membawa Anda dari memahami konsep inti dan tantangan hingga mengatasinya dengan teknik rekayasa prompt dan praktik terbaik yang relevan. Perhatikan bahwa bagian "Teknik Lanjutan" dalam panduan ini merujuk pada konten yang dibahas dalam bab _berikutnya_ dari kurikulum ini.

![Panduan Bergambar untuk Rekayasa Prompt](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.id.png)

## Startup Kami

Sekarang, mari kita bahas bagaimana _topik ini_ berkaitan dengan misi startup kami untuk [membawa inovasi AI ke pendidikan](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Kami ingin membangun aplikasi pembelajaran _personalized_ yang didukung AI - jadi mari kita pikirkan bagaimana pengguna yang berbeda dari aplikasi kami mungkin "merancang" prompt:

- **Administrator** mungkin meminta AI untuk _menganalisis data kurikulum untuk mengidentifikasi kekurangan dalam cakupan_. AI dapat merangkum hasil atau memvisualisasikannya dengan kode.  
- **Pendidik** mungkin meminta AI untuk _menghasilkan rencana pelajaran untuk audiens dan topik tertentu_. AI dapat membuat rencana yang dipersonalisasi dalam format yang ditentukan.  
- **Siswa** mungkin meminta AI untuk _mengajari mereka dalam mata pelajaran yang sulit_. AI sekarang dapat membimbing siswa dengan pelajaran, petunjuk, & contoh yang disesuaikan dengan tingkat mereka.  

Itu hanya sebagian kecil dari kemungkinannya. Lihat [Prompts Untuk Pendidikan](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - perpustakaan prompt sumber terbuka yang dikurasi oleh para ahli pendidikan - untuk mendapatkan gambaran yang lebih luas tentang kemungkinan-kemungkinannya! _Cobalah menjalankan beberapa prompt tersebut di sandbox atau menggunakan OpenAI Playground untuk melihat apa yang terjadi!_

<!--
TEMPLATE PELAJARAN:
Unit ini harus mencakup konsep inti #1.
Perkuat konsep dengan contoh dan referensi.

KONSEP #1:
Rekayasa Prompt.
Definisikan dan jelaskan mengapa hal itu diperlukan.
-->

## Apa itu Rekayasa Prompt?

Kami memulai pelajaran ini dengan mendefinisikan **Rekayasa Prompt** sebagai proses _merancang dan mengoptimalkan_ input teks (prompt) untuk menghasilkan respons yang konsisten dan berkualitas (penyelesaian) untuk tujuan aplikasi dan model tertentu. Kita dapat memikirkan ini sebagai proses 2 langkah:

- _merancang_ prompt awal untuk model dan tujuan tertentu  
- _menyempurnakan_ prompt secara iteratif untuk meningkatkan kualitas respons  

Ini adalah proses coba-coba yang memerlukan intuisi dan usaha pengguna untuk mendapatkan hasil yang optimal. Jadi mengapa ini penting? Untuk menjawab pertanyaan itu, kita pertama-tama perlu memahami tiga konsep:

- _Tokenisasi_ = bagaimana model "melihat" prompt  
- _Base LLMs_ = bagaimana model dasar "memproses" prompt  
- _LLM yang Disetel Instruksi_ = bagaimana model sekarang dapat melihat "tugas"  

### Tokenisasi

LLM melihat prompt sebagai _urutan token_ di mana model yang berbeda (atau versi model) dapat melakukan tokenisasi pada prompt yang sama dengan cara yang berbeda. Karena LLM dilatih pada token (dan bukan pada teks mentah), cara prompt ditokenisasi memiliki dampak langsung pada kualitas respons yang dihasilkan.

Untuk mendapatkan intuisi tentang bagaimana tokenisasi bekerja, coba alat seperti [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) yang ditunjukkan di bawah ini. Salin prompt Anda - dan lihat bagaimana itu diubah menjadi token, perhatikan bagaimana karakter spasi dan tanda baca ditangani. Perhatikan bahwa contoh ini menunjukkan LLM yang lebih lama (GPT-3) - jadi mencoba ini dengan model yang lebih baru mungkin menghasilkan hasil yang berbeda.

![Tokenisasi](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.id.png)

### Konsep: Model Dasar

Setelah prompt ditokenisasi, fungsi utama ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (atau model dasar) adalah memprediksi token dalam urutan tersebut. Karena LLM dilatih pada dataset teks yang sangat besar, mereka memiliki pemahaman yang baik tentang hubungan statistik antar token dan dapat membuat prediksi tersebut dengan tingkat kepercayaan tertentu. Perhatikan bahwa mereka tidak memahami _makna_ kata-kata dalam prompt atau token; mereka hanya melihat pola yang dapat mereka "lengkapi" dengan prediksi berikutnya. Mereka dapat terus memprediksi urutan hingga dihentikan oleh intervensi pengguna atau kondisi yang telah ditetapkan sebelumnya.

Ingin melihat bagaimana penyelesaian berbasis prompt bekerja? Masukkan prompt di atas ke dalam [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) Azure OpenAI Studio dengan pengaturan default. Sistem dikonfigurasi untuk memperlakukan prompt sebagai permintaan informasi - jadi Anda harus melihat penyelesaian yang memenuhi konteks ini.

Tapi bagaimana jika pengguna ingin melihat sesuatu yang spesifik yang memenuhi beberapa kriteria atau tujuan tugas? Di sinilah _LLM yang disetel instruksi_ masuk ke dalam gambar.

![Penyelesaian Obrolan Base LLM](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.id.png)

### Konsep: LLM yang Disetel Instruksi

[LLM yang Disetel Instruksi](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) dimulai dengan model dasar dan menyetelnya dengan contoh atau pasangan input/output (misalnya, "pesan" multi-putaran) yang dapat berisi instruksi yang jelas - dan respons dari AI mencoba mengikuti instruksi tersebut.

Ini menggunakan teknik seperti Reinforcement Learning with Human Feedback (RLHF) yang dapat melatih model untuk _mengikuti instruksi_ dan _belajar dari umpan balik_ sehingga menghasilkan respons yang lebih sesuai untuk aplikasi praktis dan lebih relevan dengan tujuan pengguna.

Mari kita coba - kunjungi kembali prompt di atas, tetapi sekarang ubah _pesan sistem_ untuk memberikan instruksi berikut sebagai konteks:

> _Ringkas konten yang Anda diberikan untuk siswa kelas dua. Batasi hasilnya menjadi satu paragraf dengan 3-5 poin utama._

Lihat bagaimana hasilnya sekarang disetel untuk mencerminkan tujuan dan format yang diinginkan? Seorang pendidik sekarang dapat langsung menggunakan respons ini dalam slide untuk kelas tersebut.

![Penyelesaian Obrolan LLM yang Disetel Instruksi](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.id.png)

## Mengapa kita membutuhkan Rekayasa Prompt?

Sekarang kita tahu bagaimana prompt diproses oleh LLM, mari kita bahas _mengapa_ kita membutuhkan rekayasa prompt. Jawabannya terletak pada fakta bahwa LLM saat ini menghadirkan sejumlah tantangan yang membuat _penyelesaian yang andal dan konsisten_ lebih sulit dicapai tanpa usaha dalam konstruksi dan optimasi prompt. Misalnya:

1. **Respons model bersifat stokastik.** _Prompt yang sama_ kemungkinan akan menghasilkan respons yang berbeda dengan model atau versi model yang berbeda. Dan bahkan mungkin menghasilkan hasil yang berbeda dengan _model yang sama_ pada waktu yang berbeda. _Teknik rekayasa prompt dapat membantu kita meminimalkan variasi ini dengan menyediakan batasan yang lebih baik_.  

1. **Model dapat membuat respons fiktif.** Model dilatih dengan dataset yang _besar tetapi terbatas_, yang berarti mereka tidak memiliki pengetahuan tentang konsep di luar cakupan pelatihan tersebut. Akibatnya, mereka dapat menghasilkan penyelesaian yang tidak akurat, imajiner, atau langsung bertentangan dengan fakta yang diketahui. _Teknik rekayasa prompt membantu pengguna mengidentifikasi dan mengurangi fabrikasi semacam itu, misalnya dengan meminta AI untuk memberikan kutipan atau alasan_.  

1. **Kemampuan model akan bervariasi.** Model yang lebih baru atau generasi model akan memiliki kemampuan yang lebih kaya tetapi juga membawa keunikan dan trade-off dalam biaya & kompleksitas. _Rekayasa prompt dapat membantu kita mengembangkan praktik terbaik dan alur kerja yang mengabstraksi perbedaan dan beradaptasi dengan persyaratan spesifik model dengan cara yang skalabel dan mulus_.  

Mari kita lihat ini dalam aksi di OpenAI atau Azure OpenAI Playground:

- Gunakan prompt yang sama dengan penerapan LLM yang berbeda (misalnya, OpenAI, Azure OpenAI, Hugging Face) - apakah Anda melihat variasinya?  
- Gunakan prompt yang sama berulang kali dengan penerapan LLM _yang sama_ (misalnya, playground Azure OpenAI) - bagaimana variasi ini berbeda?  

### Contoh Fabrikasi

Dalam kursus ini, kami menggunakan istilah **"fabrikasi"** untuk merujuk pada fenomena di mana LLM kadang-kadang menghasilkan informasi yang tidak faktual karena keterbatasan dalam pelatihannya atau kendala lainnya. Anda mungkin juga pernah mendengar ini disebut sebagai _"halusinasi"_ dalam artikel populer atau makalah penelitian. Namun, kami sangat merekomendasikan menggunakan istilah _"fabrikasi"_ agar kita tidak secara tidak sengaja mengatributkan sifat manusia kepada hasil yang digerakkan oleh mesin. Ini juga memperkuat [pedoman AI yang Bertanggung Jawab](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) dari perspektif terminologi, menghilangkan istilah yang mungkin dianggap ofensif atau tidak inklusif dalam beberapa konteks.

Ingin mendapatkan gambaran tentang bagaimana fabrikasi bekerja? Pikirkan sebuah prompt yang menginstruksikan AI untuk menghasilkan konten untuk topik yang tidak ada (untuk memastikan itu tidak ditemukan dalam dataset pelatihan). Misalnya - saya mencoba prompt ini:

> **Prompt:** buat rencana pelajaran tentang Perang Mars tahun 2076.
Sebuah pencarian web menunjukkan bahwa ada kisah fiksi (misalnya, serial televisi atau buku) tentang perang di Mars - tetapi tidak ada yang terjadi pada tahun 2076. Logika sederhana juga memberi tahu kita bahwa tahun 2076 adalah _masa depan_ dan karenanya tidak dapat dikaitkan dengan peristiwa nyata.

Jadi, apa yang terjadi ketika kita menjalankan prompt ini dengan penyedia LLM yang berbeda?

> **Respons 1**: OpenAI Playground (GPT-35)

![Respons 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.id.png)

> **Respons 2**: Azure OpenAI Playground (GPT-35)

![Respons 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.id.png)

> **Respons 3**: Hugging Face Chat Playground (LLama-2)

![Respons 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.id.png)

Seperti yang diharapkan, setiap model (atau versi model) menghasilkan respons yang sedikit berbeda berkat perilaku stokastik dan variasi kemampuan model. Misalnya, satu model menargetkan audiens kelas 8 sementara yang lain mengasumsikan siswa sekolah menengah. Namun, ketiga model tersebut menghasilkan respons yang dapat meyakinkan pengguna yang tidak tahu bahwa peristiwa tersebut nyata.

Teknik rekayasa prompt seperti _metaprompting_ dan _konfigurasi suhu_ dapat mengurangi fabrikasi model hingga tingkat tertentu. Arsitektur rekayasa prompt baru juga mengintegrasikan alat dan teknik baru secara mulus ke dalam alur prompt, untuk mengurangi atau memitigasi beberapa efek ini.

## Studi Kasus: GitHub Copilot

Mari kita akhiri bagian ini dengan memahami bagaimana rekayasa prompt digunakan dalam solusi dunia nyata dengan melihat satu Studi Kasus: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot adalah "AI Pair Programmer" Anda - ia mengubah prompt teks menjadi pelengkapan kode dan diintegrasikan ke dalam lingkungan pengembangan Anda (misalnya, Visual Studio Code) untuk pengalaman pengguna yang mulus. Seperti yang didokumentasikan dalam serangkaian blog di bawah ini, versi awalnya didasarkan pada model OpenAI Codex - dengan para insinyur segera menyadari perlunya menyempurnakan model dan mengembangkan teknik rekayasa prompt yang lebih baik untuk meningkatkan kualitas kode. Pada bulan Juli, mereka [meluncurkan model AI yang lebih baik yang melampaui Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) untuk saran yang lebih cepat.

Baca postingan secara berurutan untuk mengikuti perjalanan pembelajaran mereka.

- **Mei 2023** | [GitHub Copilot Semakin Baik dalam Memahami Kode Anda](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mei 2023** | [Di Dalam GitHub: Bekerja dengan LLM di Balik GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Cara Menulis Prompt yang Lebih Baik untuk GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot Melampaui Codex dengan Model AI yang Lebih Baik](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Panduan Pengembang untuk Rekayasa Prompt dan LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Cara Membangun Aplikasi LLM Perusahaan: Pelajaran dari GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Anda juga dapat menjelajahi [blog Teknik mereka](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) untuk lebih banyak postingan seperti [yang satu ini](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) yang menunjukkan bagaimana model dan teknik ini _diterapkan_ untuk mendorong aplikasi dunia nyata.

---

## Konstruksi Prompt

Kita telah melihat mengapa rekayasa prompt itu penting - sekarang mari kita pahami bagaimana prompt _dibangun_ sehingga kita dapat mengevaluasi berbagai teknik untuk desain prompt yang lebih efektif.

### Prompt Dasar

Mari kita mulai dengan prompt dasar: input teks yang dikirim ke model tanpa konteks lain. Berikut adalah contohnya - ketika kita mengirim beberapa kata pertama dari lagu kebangsaan AS ke [API Completion](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) OpenAI, model langsung _melengkapi_ respons dengan beberapa baris berikutnya, menggambarkan perilaku prediksi dasar.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Sepertinya Anda sedang memulai lirik "The Star-Spangled Banner," lagu kebangsaan Amerika Serikat. Lirik lengkapnya adalah ...              |

### Prompt Kompleks

Sekarang mari kita tambahkan konteks dan instruksi ke prompt dasar tersebut. [API Chat Completion](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) memungkinkan kita membangun prompt kompleks sebagai kumpulan _pesan_ dengan:

- Pasangan input/output yang mencerminkan input _pengguna_ dan respons _asisten_.
- Pesan sistem yang menetapkan konteks untuk perilaku atau kepribadian asisten.

Permintaan sekarang berbentuk seperti di bawah ini, di mana _tokenisasi_ secara efektif menangkap informasi relevan dari konteks dan percakapan. Sekarang, mengubah konteks sistem bisa sama berdampaknya pada kualitas pelengkapan, seperti input pengguna yang diberikan.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Prompt Instruksi

Dalam contoh di atas, prompt pengguna adalah kueri teks sederhana yang dapat diinterpretasikan sebagai permintaan informasi. Dengan prompt _instruksi_, kita dapat menggunakan teks tersebut untuk menentukan tugas secara lebih rinci, memberikan panduan yang lebih baik kepada AI. Berikut adalah contohnya:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Jenis Instruksi     |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Tuliskan deskripsi tentang Perang Saudara                                                                                                                                                                                              | _mengembalikan paragraf sederhana_                                                                                        | Sederhana           |
| Tuliskan deskripsi tentang Perang Saudara. Sertakan tanggal dan peristiwa penting serta jelaskan signifikansinya                                                                                                                       | _mengembalikan paragraf diikuti dengan daftar tanggal peristiwa penting beserta deskripsinya_                              | Kompleks            |
| Tuliskan deskripsi tentang Perang Saudara dalam 1 paragraf. Sertakan 3 poin penting dengan tanggal dan signifikansinya. Sertakan 3 poin lagi dengan tokoh sejarah penting dan kontribusinya. Kembalikan output dalam format file JSON. | _mengembalikan detail lebih ekstensif dalam kotak teks, diformat sebagai JSON yang dapat Anda salin-tempel ke file dan validasi sesuai kebutuhan_ | Kompleks. Terformat.|

## Konten Utama

Dalam contoh di atas, prompt masih cukup terbuka, memungkinkan LLM memutuskan bagian mana dari dataset pra-latihannya yang relevan. Dengan pola desain _konten utama_, teks input dibagi menjadi dua bagian:

- instruksi (aksi)
- konten relevan (yang memengaruhi aksi)

Berikut adalah contoh di mana instruksinya adalah "ringkas ini dalam 2 kalimat".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter adalah planet kelima dari Matahari dan yang terbesar di Tata Surya. Ini adalah raksasa gas dengan massa seperseribu dari Matahari, tetapi dua setengah kali dari semua planet lain di Tata Surya digabungkan. Jupiter adalah salah satu objek paling terang yang terlihat dengan mata telanjang di langit malam, dan telah dikenal oleh peradaban kuno sejak sebelum sejarah tercatat. Ia dinamai sesuai dengan dewa Romawi Jupiter.[19] Ketika dilihat dari Bumi, Jupiter bisa cukup terang sehingga cahayanya yang dipantulkan dapat menghasilkan bayangan yang terlihat,[20] dan rata-rata merupakan objek alami ketiga paling terang di langit malam setelah Bulan dan Venus. <br/> **Ringkas ini dalam 2 kalimat pendek** | Jupiter, planet kelima dari Matahari, adalah yang terbesar di Tata Surya dan dikenal sebagai salah satu objek paling terang di langit malam. Dinamai sesuai dengan dewa Romawi Jupiter, ia adalah raksasa gas dengan massa dua setengah kali dari semua planet lain di Tata Surya digabungkan. |

Segmen konten utama dapat digunakan dengan berbagai cara untuk mendorong instruksi yang lebih efektif:

- **Contoh** - alih-alih memberi tahu model apa yang harus dilakukan dengan instruksi eksplisit, berikan contoh tentang apa yang harus dilakukan dan biarkan model menyimpulkan pola.
- **Petunjuk** - ikuti instruksi dengan "petunjuk" yang memulai pelengkapan, membimbing model menuju respons yang lebih relevan.
- **Template** - ini adalah 'resep' yang dapat diulang untuk prompt dengan placeholder (variabel) yang dapat disesuaikan dengan data untuk kasus penggunaan tertentu.

Mari kita eksplorasi ini dalam aksi.

### Menggunakan Contoh

Ini adalah pendekatan di mana Anda menggunakan konten utama untuk "memberi makan model" beberapa contoh output yang diinginkan untuk instruksi tertentu, dan biarkan model menyimpulkan pola untuk output yang diinginkan. Berdasarkan jumlah contoh yang diberikan, kita dapat memiliki zero-shot prompting, one-shot prompting, few-shot prompting, dll.

Prompt sekarang terdiri dari tiga komponen:

- Deskripsi tugas
- Beberapa contoh output yang diinginkan
- Awal dari contoh baru (yang menjadi deskripsi tugas implisit)

| Jenis Pembelajaran | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot          | "The Sun is Shining". Terjemahkan ke Bahasa Spanyol                                                                                                  | "El Sol está brillando".    |
| One-shot           | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot           | Pemain berlari di base => Baseball <br/> Pemain memukul ace => Tenis <br/> Pemain memukul enam => Kriket <br/> Pemain melakukan slam-dunk =>          | Basket                      |
|                    |                                                                                                                                                       |                             |

Perhatikan bagaimana kita harus memberikan instruksi eksplisit ("Terjemahkan ke Bahasa Spanyol") dalam zero-shot prompting, tetapi itu disimpulkan dalam contoh one-shot prompting. Contoh few-shot menunjukkan bagaimana menambahkan lebih banyak contoh memungkinkan model membuat inferensi yang lebih akurat tanpa instruksi tambahan.

### Petunjuk Prompt

Teknik lain untuk menggunakan konten utama adalah memberikan _petunjuk_ daripada contoh. Dalam kasus ini, kita memberikan model dorongan ke arah yang benar dengan _memulainya_ dengan cuplikan yang mencerminkan format respons yang diinginkan. Model kemudian "mengambil petunjuk" untuk melanjutkan dalam arah tersebut.

| Jumlah Petunjuk | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter adalah planet kelima dari Matahari dan yang terbesar di Tata Surya. Ini adalah raksasa gas dengan massa seperseribu dari Matahari, tetapi dua setengah kali dari semua planet lain di Tata Surya digabungkan. Jupiter adalah salah satu objek paling terang yang terlihat dengan mata telanjang di langit malam, dan telah dikenal oleh peradaban kuno sejak sebelum sejarah tercatat. <br/>**Ringkas Ini**                                       | Jupiter adalah planet terbesar di Tata Surya dan yang kelima dari Matahari. Ini adalah raksasa gas dengan massa 1/1000 dari Matahari, tetapi lebih berat daripada semua planet lain digabungkan. Peradaban kuno telah lama mengetahui tentang Jupiter, dan ia mudah terlihat di langit malam. |
| 1              | Jupiter adalah planet kelima dari Matahari dan yang terbesar di Tata Surya. Ini adalah raksasa gas dengan massa seperseribu dari Matahari, tetapi dua setengah kali lebih besar dari gabungan semua planet lain di Tata Surya. Jupiter adalah salah satu objek paling terang yang terlihat dengan mata telanjang di langit malam, dan telah dikenal oleh peradaban kuno sejak sebelum sejarah tercatat. <br/>**Ringkas Ini** <br/> Yang kita pelajari adalah bahwa Jupiter | adalah planet kelima dari Matahari dan yang terbesar di Tata Surya. Ini adalah raksasa gas dengan massa seperseribu dari Matahari, tetapi dua setengah kali lebih besar dari gabungan semua planet lain. Jupiter mudah terlihat dengan mata telanjang dan telah dikenal sejak zaman kuno.                        |
| 2              | Jupiter adalah planet kelima dari Matahari dan yang terbesar di Tata Surya. Ini adalah raksasa gas dengan massa seperseribu dari Matahari, tetapi dua setengah kali lebih besar dari gabungan semua planet lain di Tata Surya. Jupiter adalah salah satu objek paling terang yang terlihat dengan mata telanjang di langit malam, dan telah dikenal oleh peradaban kuno sejak sebelum sejarah tercatat. <br/>**Ringkas Ini** <br/> 3 Fakta Utama yang Kita Pelajari:         | 1. Jupiter adalah planet kelima dari Matahari dan yang terbesar di Tata Surya. <br/> 2. Ini adalah raksasa gas dengan massa seperseribu dari Matahari...<br/> 3. Jupiter telah terlihat dengan mata telanjang sejak zaman kuno ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Template Prompt

Template prompt adalah _resep yang telah ditentukan untuk sebuah prompt_ yang dapat disimpan dan digunakan kembali sesuai kebutuhan, untuk mendorong pengalaman pengguna yang lebih konsisten dalam skala besar. Dalam bentuknya yang paling sederhana, ini hanyalah kumpulan contoh prompt seperti [contoh dari OpenAI ini](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst) yang menyediakan komponen prompt interaktif (pesan pengguna dan sistem) serta format permintaan berbasis API - untuk mendukung penggunaan ulang.

Dalam bentuknya yang lebih kompleks seperti [contoh dari LangChain ini](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), template ini berisi _placeholder_ yang dapat diganti dengan data dari berbagai sumber (input pengguna, konteks sistem, sumber data eksternal, dll.) untuk menghasilkan prompt secara dinamis. Hal ini memungkinkan kita untuk membuat pustaka prompt yang dapat digunakan kembali untuk mendorong pengalaman pengguna yang konsisten **secara programatik** dalam skala besar.

Akhirnya, nilai nyata dari template terletak pada kemampuan untuk membuat dan menerbitkan _pustaka prompt_ untuk domain aplikasi vertikal - di mana template prompt sekarang _dioptimalkan_ untuk mencerminkan konteks atau contoh spesifik aplikasi yang membuat respons lebih relevan dan akurat untuk audiens pengguna yang ditargetkan. Repositori [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) adalah contoh yang bagus dari pendekatan ini, mengkurasi pustaka prompt untuk domain pendidikan dengan penekanan pada tujuan utama seperti perencanaan pelajaran, desain kurikulum, bimbingan siswa, dll.

## Konten Pendukung

Jika kita memikirkan konstruksi prompt sebagai memiliki instruksi (tugas) dan target (konten utama), maka _konten sekunder_ adalah seperti konteks tambahan yang kita berikan untuk **mempengaruhi output dengan cara tertentu**. Ini bisa berupa parameter penyetelan, instruksi format, taksonomi topik, dll. yang dapat membantu model _menyesuaikan_ responsnya agar sesuai dengan tujuan atau harapan pengguna yang diinginkan.

Sebagai contoh: Diberikan katalog kursus dengan metadata yang luas (nama, deskripsi, tingkat, tag metadata, instruktur, dll.) tentang semua kursus yang tersedia dalam kurikulum:

- kita dapat mendefinisikan instruksi untuk "meringkas katalog kursus untuk Musim Gugur 2023"
- kita dapat menggunakan konten utama untuk memberikan beberapa contoh output yang diinginkan
- kita dapat menggunakan konten sekunder untuk mengidentifikasi 5 "tag" teratas yang diminati.

Sekarang, model dapat memberikan ringkasan dalam format yang ditunjukkan oleh beberapa contoh - tetapi jika hasil memiliki beberapa tag, model dapat memprioritaskan 5 tag yang diidentifikasi dalam konten sekunder.

---

<!--
TEMPLATE PELAJARAN:
Unit ini harus mencakup konsep inti #1.
Perkuat konsep dengan contoh dan referensi.

KONSEP #3:
Teknik Rekayasa Prompt.
Apa saja teknik dasar untuk rekayasa prompt?
Ilustrasikan dengan beberapa latihan.
-->

## Praktik Terbaik dalam Prompting

Sekarang kita tahu bagaimana prompt dapat _dibangun_, kita dapat mulai memikirkan bagaimana _merancang_ mereka untuk mencerminkan praktik terbaik. Kita dapat memikirkan ini dalam dua bagian - memiliki _pola pikir_ yang tepat dan menerapkan _teknik_ yang tepat.

### Pola Pikir Rekayasa Prompt

Rekayasa Prompt adalah proses coba-coba, jadi ingat tiga faktor panduan utama:

1. **Pemahaman Domain Penting.** Akurasi dan relevansi respons adalah fungsi dari _domain_ di mana aplikasi atau pengguna tersebut beroperasi. Gunakan intuisi dan keahlian domain Anda untuk **menyesuaikan teknik** lebih lanjut. Misalnya, definisikan _kepribadian spesifik domain_ dalam prompt sistem Anda, atau gunakan _template spesifik domain_ dalam prompt pengguna Anda. Berikan konten sekunder yang mencerminkan konteks spesifik domain, atau gunakan _petunjuk dan contoh spesifik domain_ untuk membimbing model menuju pola penggunaan yang familiar.

2. **Pemahaman Model Penting.** Kita tahu model bersifat stokastik secara alami. Tetapi implementasi model juga dapat bervariasi dalam hal dataset pelatihan yang mereka gunakan (pengetahuan yang telah dilatih sebelumnya), kemampuan yang mereka sediakan (misalnya, melalui API atau SDK) dan jenis konten yang mereka optimalkan (misalnya, kode vs. gambar vs. teks). Pahami kekuatan dan keterbatasan model yang Anda gunakan, dan gunakan pengetahuan itu untuk _memprioritaskan tugas_ atau membangun _template yang disesuaikan_ yang dioptimalkan untuk kemampuan model.

3. **Iterasi & Validasi Penting.** Model berkembang dengan cepat, begitu juga teknik untuk rekayasa prompt. Sebagai ahli domain, Anda mungkin memiliki konteks atau kriteria lain untuk aplikasi spesifik _Anda_, yang mungkin tidak berlaku untuk komunitas yang lebih luas. Gunakan alat & teknik rekayasa prompt untuk "memulai" konstruksi prompt, lalu iterasi dan validasi hasil menggunakan intuisi dan keahlian domain Anda sendiri. Catat wawasan Anda dan buat **basis pengetahuan** (misalnya, pustaka prompt) yang dapat digunakan sebagai baseline baru oleh orang lain, untuk iterasi yang lebih cepat di masa depan.

## Praktik Terbaik

Sekarang mari kita lihat praktik terbaik umum yang direkomendasikan oleh [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) dan praktisi [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Apa                               | Mengapa                                                                                                                                                                                                                                               |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evaluasi model terbaru.           | Generasi model baru kemungkinan memiliki fitur dan kualitas yang lebih baik - tetapi mungkin juga menimbulkan biaya yang lebih tinggi. Evaluasi dampaknya, lalu buat keputusan migrasi.                                                               |
| Pisahkan instruksi & konteks      | Periksa apakah model/penyedia Anda mendefinisikan _pembatas_ untuk membedakan instruksi, konten utama, dan konten sekunder dengan lebih jelas. Ini dapat membantu model memberikan bobot lebih akurat pada token.                                       |
| Bersikap spesifik dan jelas       | Berikan lebih banyak detail tentang konteks, hasil, panjang, format, gaya, dll. yang diinginkan. Ini akan meningkatkan kualitas dan konsistensi respons. Tangkap resep dalam template yang dapat digunakan kembali.                                    |
| Bersifat deskriptif, gunakan contoh | Model mungkin merespons lebih baik dengan pendekatan "tunjukkan dan ceritakan". Mulailah dengan pendekatan `zero-shot` di mana Anda memberikan instruksi (tetapi tanpa contoh) lalu coba `few-shot` sebagai penyempurnaan, memberikan beberapa contoh output yang diinginkan. Gunakan analogi. |
| Gunakan petunjuk untuk memulai penyelesaian | Dorong model menuju hasil yang diinginkan dengan memberikan beberapa kata atau frasa awal yang dapat digunakan sebagai titik awal untuk respons.                                                                                                     |
| Ulangi                           | Kadang-kadang Anda mungkin perlu mengulang instruksi ke model. Berikan instruksi sebelum dan setelah konten utama Anda, gunakan instruksi dan petunjuk, dll. Iterasi & validasi untuk melihat apa yang berhasil.                                       |
| Urutan Penting                   | Urutan di mana Anda menyajikan informasi ke model dapat memengaruhi output, bahkan dalam contoh pembelajaran, berkat bias kebaruan. Coba berbagai opsi untuk melihat apa yang paling berhasil.                                                          |
| Berikan model "jalan keluar"     | Berikan respons penyelesaian _fallback_ ke model yang dapat diberikan jika tidak dapat menyelesaikan tugas karena alasan apa pun. Ini dapat mengurangi kemungkinan model menghasilkan respons palsu atau dibuat-buat.                                   |
|                                   |                                                                                                                                                                                                                                                       |

Seperti halnya praktik terbaik lainnya, ingat bahwa _hasil Anda mungkin berbeda_ tergantung pada model, tugas, dan domain. Gunakan ini sebagai titik awal, dan iterasi untuk menemukan apa yang paling berhasil untuk Anda. Terus evaluasi ulang proses rekayasa prompt Anda saat model dan alat baru tersedia, dengan fokus pada skalabilitas proses dan kualitas respons.

<!--
TEMPLATE PELAJARAN:
Unit ini harus menyediakan tantangan kode jika memungkinkan

TANTANGAN:
Tautkan ke Jupyter Notebook dengan hanya komentar kode dalam instruksi (bagian kode kosong).

SOLUSI:
Tautkan ke salinan Notebook tersebut dengan prompt diisi dan dijalankan, menunjukkan satu contoh.
-->

## Tugas

Selamat! Anda telah sampai di akhir pelajaran! Saatnya untuk menguji beberapa konsep dan teknik tersebut dengan contoh nyata!

Untuk tugas kita, kita akan menggunakan Jupyter Notebook dengan latihan yang dapat Anda selesaikan secara interaktif. Anda juga dapat memperluas Notebook dengan sel Markdown dan Kode Anda sendiri untuk mengeksplorasi ide dan teknik secara mandiri.

### Untuk memulai, fork repo, lalu

- (Direkomendasikan) Luncurkan GitHub Codespaces
- (Alternatif) Clone repo ke perangkat lokal Anda dan gunakan dengan Docker Desktop
- (Alternatif) Buka Notebook dengan lingkungan runtime Notebook pilihan Anda.

### Selanjutnya, konfigurasikan variabel lingkungan Anda

- Salin file `.env.copy` di root repo ke `.env` dan isi nilai `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, dan `AZURE_OPENAI_DEPLOYMENT`. Kembali ke [bagian Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) untuk mempelajari caranya.

### Selanjutnya, buka Jupyter Notebook

- Pilih kernel runtime. Jika menggunakan opsi 1 atau 2, cukup pilih kernel Python 3.10.x default yang disediakan oleh container pengembang.

Anda siap menjalankan latihan. Perhatikan bahwa tidak ada _jawaban benar dan salah_ di sini - hanya mengeksplorasi opsi melalui coba-coba dan membangun intuisi tentang apa yang berhasil untuk model dan domain aplikasi tertentu.

_Untuk alasan ini, tidak ada segmen Solusi Kode dalam pelajaran ini. Sebagai gantinya, Notebook akan memiliki sel Markdown berjudul "Solusi Saya:" yang menunjukkan satu contoh output untuk referensi._

 <!--
TEMPLATE PELAJARAN:
Bungkus bagian dengan ringkasan dan sumber daya untuk pembelajaran mandiri.
-->

## Pemeriksaan Pengetahuan

Manakah dari berikut ini yang merupakan prompt yang baik mengikuti beberapa praktik terbaik yang masuk akal?

1. Tunjukkan gambar mobil merah
2. Tunjukkan gambar mobil merah merek Volvo dan model XC90 yang diparkir di tepi tebing dengan matahari terbenam
3. Tunjukkan gambar mobil merah merek Volvo dan model XC90

A: 2, ini adalah prompt terbaik karena memberikan detail tentang "apa" dan masuk ke spesifik (bukan hanya mobil apa pun tetapi merek dan model tertentu) dan juga menggambarkan pengaturan keseluruhan. 3 adalah yang terbaik berikutnya karena juga berisi banyak deskripsi.

## 🚀 Tantangan

Coba gunakan teknik "petunjuk" dengan prompt: Lengkapi kalimat "Tunjukkan gambar mobil merah merek Volvo dan ". Apa yang direspons, dan bagaimana Anda akan meningkatkannya?

## Kerja Hebat! Lanjutkan Pembelajaran Anda

Ingin belajar lebih banyak tentang berbagai konsep Rekayasa Prompt? Kunjungi [halaman pembelajaran lanjutan](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk menemukan sumber daya hebat lainnya tentang topik ini.

Lanjutkan ke Pelajaran 5 di mana kita akan melihat [teknik prompting lanjutan](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.