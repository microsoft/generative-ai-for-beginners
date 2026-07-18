# Dasar-dasar Rekayasa Prompt

[![Dasar-dasar Rekayasa Prompt](../../../translated_images/id/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Pendahuluan
Modul ini membahas konsep dan teknik penting untuk membuat prompt yang efektif dalam model AI generatif. Cara Anda menulis prompt ke LLM juga penting. Prompt yang dirancang dengan cermat dapat menghasilkan kualitas respons yang lebih baik. Tapi apa sebenarnya arti istilah seperti _prompt_ dan _rekayasa prompt_? Dan bagaimana saya bisa meningkatkan _input_ prompt yang saya kirim ke LLM? Ini adalah pertanyaan yang akan kita coba jawab dalam bab ini dan bab berikutnya.

_Generative AI_ mampu menciptakan konten baru (misalnya, teks, gambar, audio, kode, dll.) sebagai respons atas permintaan pengguna. Ini dicapai menggunakan _Large Language Models_ seperti seri GPT OpenAI ("Generative Pre-trained Transformer") yang dilatih untuk menggunakan bahasa alami dan kode.

Pengguna sekarang dapat berinteraksi dengan model ini menggunakan paradigma yang familiar seperti chat, tanpa memerlukan keahlian teknis atau pelatihan. Model ini berbasis _prompt_ - pengguna mengirim input teks (prompt) dan mendapatkan respons AI (penyelesaian). Mereka kemudian bisa "ngobrol dengan AI" secara iteratif, dalam percakapan multi-giliran, menyempurnakan prompt mereka sampai responsnya sesuai dengan harapan.

"Prompt" kini menjadi antarmuka _pemrograman utama_ untuk aplikasi AI generatif, memberitahu model apa yang harus dilakukan dan memengaruhi kualitas respons yang dikembalikan. "Rekayasa Prompt" adalah bidang studi yang berkembang pesat yang fokus pada _desain dan optimasi_ prompt untuk memberikan respons yang konsisten dan berkualitas secara skala.

## Tujuan Pembelajaran

Dalam pelajaran ini, kita belajar apa itu Rekayasa Prompt, mengapa itu penting, dan bagaimana kita bisa membuat prompt yang lebih efektif untuk model dan tujuan aplikasi tertentu. Kita akan memahami konsep inti dan praktik terbaik dalam rekayasa prompt - serta belajar tentang lingkungan _sandbox_ interaktif Jupyter Notebooks di mana kita bisa melihat konsep-konsep ini diterapkan pada contoh nyata.

Pada akhir pelajaran ini kita akan bisa:

1. Menjelaskan apa itu rekayasa prompt dan mengapa itu penting.
2. Mendeskripsikan komponen dari sebuah prompt dan bagaimana penggunaannya.
3. Mempelajari praktik terbaik dan teknik rekayasa prompt.
4. Menerapkan teknik yang dipelajari pada contoh nyata, menggunakan endpoint OpenAI.

## Istilah Kunci

Rekayasa Prompt: Praktik merancang dan menyempurnakan input untuk mengarahkan model AI menghasilkan output yang diinginkan.
Tokenisasi: Proses mengubah teks menjadi unit lebih kecil, yang disebut token, yang dapat dipahami dan diproses oleh model.
Instruction-Tuned LLMs: Large Language Models (LLM) yang telah disesuaikan dengan instruksi spesifik untuk meningkatkan akurasi dan relevansi respons mereka.

## Sandbox Pembelajaran

Rekayasa prompt saat ini lebih merupakan seni daripada ilmu. Cara terbaik untuk meningkatkan intuisi kita adalah dengan _berlatih lebih banyak_ dan mengadopsi pendekatan coba-coba yang menggabungkan keahlian domain aplikasi dengan teknik yang direkomendasikan dan optimasi spesifik model.

Jupyter Notebook yang menyertai pelajaran ini menyediakan lingkungan _sandbox_ di mana Anda bisa mencoba apa yang Anda pelajari - saat belajar atau sebagai bagian dari tantangan kode di akhir. Untuk menjalankan latihan, Anda memerlukan:

1. **Kunci API Azure OpenAI** - endpoint layanan untuk LLM yang dideploy.
2. **Runtime Python** - tempat Notebook dapat dijalankan.
3. **Variabel Lingkungan Lokal** - _selesaikan langkah [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) sekarang untuk siap digunakan_.

Notebook ini dilengkapi dengan latihan _pemula_ - tetapi Anda dianjurkan untuk menambahkan bagian _Markdown_ (deskripsi) dan _Kode_ (permintaan prompt) Anda sendiri untuk mencoba lebih banyak contoh atau ide - dan membangun intuisi Anda untuk desain prompt.

## Panduan Bergambar

Ingin mendapatkan gambaran besar tentang apa yang dibahas pelajaran ini sebelum mulai? Lihat panduan bergambar ini, yang memberi Anda gambaran topik utama yang dibahas dan poin-poin penting yang perlu Anda pikirkan di masing-masing. Peta jalan pelajaran membawa Anda dari memahami konsep inti dan tantangan hingga mengatasinya dengan teknik rekayasa prompt yang relevan dan praktik terbaik. Perlu dicatat bagian "Teknik Lanjutan" pada panduan ini merujuk pada materi di bab _berikutnya_ dari kurikulum ini.

![Panduan Bergambar Rekayasa Prompt](../../../translated_images/id/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Startup Kami

Sekarang, mari kita bicarakan bagaimana _topik ini_ terkait dengan misi startup kami untuk [membawa inovasi AI ke pendidikan](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Kami ingin membangun aplikasi AI yang mendukung _pembelajaran personalisasi_ - jadi mari kita pikirkan bagaimana pengguna berbeda dari aplikasi kami mungkin "merancang" prompt:

- **Administrator** mungkin meminta AI untuk _menganalisis data kurikulum guna mengidentifikasi kekurangan cakupan_. AI dapat merangkum hasil atau memvisualisasikannya dengan kode.
- **Pendidik** mungkin meminta AI untuk _menghasilkan rencana pelajaran untuk audiens dan topik tertentu_. AI dapat membangun rencana personalisasi dalam format yang ditentukan.
- **Pelajar** mungkin meminta AI untuk _mengajarnya dalam subjek yang sulit_. AI sekarang dapat membimbing pelajar dengan pelajaran, petunjuk & contoh yang disesuaikan dengan tingkat mereka.

Itu baru permulaan. Lihat [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - perpustakaan prompt sumber terbuka yang dikurasi oleh para ahli pendidikan - untuk mendapatkan gambaran lebih luas tentang kemungkinan-kemungkinannya! _Cobalah menjalankan beberapa prompt di sandbox atau menggunakan OpenAI Playground untuk melihat apa yang terjadi!_

<!--
TEMPLATE PELAJARAN:
Unit ini harus membahas konsep inti #1.
Perkuat konsep dengan contoh dan referensi.

KONSEP #1:
Rekayasa Prompt.
Definisikan dan jelaskan mengapa diperlukan.
-->

## Apa itu Rekayasa Prompt?

Kami memulai pelajaran ini dengan mendefinisikan **Rekayasa Prompt** sebagai proses _merancang dan mengoptimalkan_ input teks (prompt) untuk memberikan respons (penyelesaian) yang konsisten dan berkualitas sesuai tujuan aplikasi dan model tertentu. Kita bisa memikirkan ini sebagai proses 2 langkah:

- _merancang_ prompt awal untuk model dan tujuan tertentu
- _menyempurnakan_ prompt secara iteratif untuk meningkatkan kualitas respons

Ini tentu merupakan proses coba-coba yang memerlukan intuisi dan usaha pengguna untuk memperoleh hasil optimal. Jadi mengapa penting? Untuk menjawabnya, kita harus memahami tiga konsep:

- _Tokenisasi_ = bagaimana model "melihat" prompt
- _Base LLMs_ = bagaimana model dasar "memproses" prompt
- _Instruction-Tuned LLMs_ = bagaimana model kini bisa "melihat tugas"

### Tokenisasi

LLM melihat prompt sebagai _urutan token_ di mana model berbeda (atau versi model) bisa men-tokenisasi prompt yang sama dengan cara berbeda. Karena LLM dilatih pada token (bukan teks mentah), cara prompt di-tokenisasi berdampak langsung pada kualitas respons yang dihasilkan.

Untuk mendapatkan intuisi tentang bagaimana tokenisasi bekerja, coba alat seperti [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) yang diperlihatkan di bawah. Salin prompt Anda - dan lihat bagaimana itu diubah menjadi token, perhatikan cara karakter spasi dan tanda baca ditangani. Perhatikan bahwa contoh ini menggunakan LLM lama (GPT-3) - jadi mencoba dengan model lebih baru mungkin memberi hasil berbeda.

![Tokenisasi](../../../translated_images/id/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Konsep: Model Dasar

Setelah prompt ditokenisasi, fungsi utama dari ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (atau model dasar) adalah memprediksi token berikutnya dalam urutan tersebut. Karena LLM dilatih dari dataset teks besar, mereka memiliki pemahaman statistik hubungan antar token dan dapat membuat prediksi tersebut dengan tingkat percaya diri tertentu. Catat bahwa mereka tidak memahami _makna_ kata dalam prompt atau token; mereka hanya melihat pola yang bisa "dilengkapi" dengan prediksi berikutnya. Mereka bisa terus memprediksi rangkaian hingga dihentikan oleh pengguna atau kondisi tertentu.

Ingin melihat bagaimana penyelesaian berbasis prompt bekerja? Masukkan prompt di atas ke [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) dengan pengaturan default. Sistem dikonfigurasi untuk memperlakukan prompt sebagai permintaan informasi - jadi Anda harus melihat penyelesaian yang sesuai konteks ini.

Tapi bagaimana jika pengguna ingin melihat sesuatu yang spesifik sesuai dengan kriteria atau tujuan tugas tertentu? Di sinilah LLM _instruction-tuned_ ikut berperan.

![Penyelesaian Chat Base LLM](../../../translated_images/id/04-playground-chat-base.65b76fcfde0caa67.webp)

### Konsep: Instruction Tuned LLMs

[Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) memulai dari model dasar dan menyetelnya secara halus menggunakan contoh atau pasangan input/output (misal, pesan "multi-turn") yang dapat mengandung instruksi jelas - dan respons AI mencoba mengikuti instruksi tersebut.

Ini menggunakan teknik seperti Reinforcement Learning with Human Feedback (RLHF) yang dapat melatih model untuk _mengikuti instruksi_ dan _belajar dari umpan balik_ sehingga menghasilkan respons yang lebih sesuai aplikasi praktis dan lebih relevan dengan tujuan pengguna.

Mari coba - kembali ke prompt di atas, tapi sekarang ubah _pesan sistem_ untuk menyediakan instruksi berikut sebagai konteks:

> _Ringkas konten yang disediakan untuk siswa kelas dua. Jaga hasil agar dalam satu paragraf dengan 3-5 poin peluru._

Lihat bagaimana hasil sekarang disesuaikan untuk mencerminkan tujuan dan format yang diinginkan? Seorang pendidik sekarang dapat langsung menggunakan respons ini dalam slide mereka untuk kelas tersebut.

![Penyelesaian Chat Instruction Tuned LLM](../../../translated_images/id/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Mengapa Kita Membutuhkan Rekayasa Prompt?

Sekarang kita tahu bagaimana prompt diproses oleh LLM, mari kita bahas _mengapa_ kita membutuhkan rekayasa prompt. Jawabannya terletak pada fakta bahwa LLM saat ini menghadirkan sejumlah tantangan yang membuat _penyelesaian yang dapat diandalkan dan konsisten_ lebih sulit dicapai tanpa upaya dalam konstruksi dan optimasi prompt. Misalnya:

1. **Respons model bersifat stokastik.** _Prompt yang sama_ kemungkinan akan menghasilkan respons berbeda dengan model atau versi model yang berbeda. Dan mungkin juga menghasilkan hasil berbeda dengan _model yang sama_ pada waktu berbeda. _Teknik rekayasa prompt dapat membantu meminimalkan variasi ini dengan menyediakan pembatas yang lebih baik_.

1. **Model dapat membuat respons palsu.** Model dilatih dengan dataset _besar tapi terbatas_, artinya mereka tidak punya pengetahuan tentang konsep di luar ruang lingkup pelatihan itu. Akibatnya, mereka bisa menghasilkan penyelesaian yang tidak akurat, imajiner, atau langsung bertentangan dengan fakta yang diketahui. _Teknik rekayasa prompt membantu pengguna mengidentifikasi dan mengurangi fabrikasi seperti ini misalnya dengan meminta AI untuk sitasi atau alasan_.

1. **Kemampuan model akan berbeda.** Model baru atau generasi model akan memiliki kemampuan lebih kaya tetapi juga membawa keunikan dan tradeoff dalam biaya & kompleksitas. _Rekayasa prompt dapat membantu kita mengembangkan praktik terbaik dan alur kerja yang mengabstraksi perbedaan dan menyesuaikan kebutuhan spesifik model secara skala dan mulus_.

Mari lihat ini dalam aksi di OpenAI atau Azure OpenAI Playground:

- Gunakan prompt yang sama dengan deployment LLM berbeda (misal, OpenAI, Azure OpenAI, Hugging Face) - apakah Anda melihat variasinya?
- Gunakan prompt yang sama berulang kali dengan deployment LLM _yang sama_ (misal, playground Azure OpenAI) - bagaimana variasi tersebut berbeda?

### Contoh Fabrikasi

Dalam kursus ini, kami menggunakan istilah **"fabrikasi"** untuk merujuk pada fenomena di mana LLM kadang-kadang menghasilkan informasi yang faktualnya salah karena keterbatasan dalam pelatihan atau kendala lain. Anda mungkin juga pernah mendengar ini disebut _"halusinasi"_ dalam artikel populer atau makalah penelitian. Namun, kami sangat menyarankan menggunakan istilah _"fabrikasi"_ agar kita tidak secara tidak sengaja mengantropomorfisasi perilaku dengan memberi sifat seperti manusia pada hasil mesin. Ini juga memperkuat [pedoman AI Bertanggung Jawab](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) dari perspektif terminologi, menghilangkan istilah yang mungkin dianggap ofensif atau tidak inklusif dalam konteks tertentu.

Ingin merasakan bagaimana fabrikasi bekerja? Pikirkan prompt yang memerintahkan AI untuk menghasilkan konten tentang topik yang tidak ada (agar tidak ditemukan dalam dataset pelatihan). Misalnya - saya mencoba prompt ini:

> **Prompt:** buat rencana pelajaran tentang Perang Mars tahun 2076.

Pencarian web menunjukkan ada kisah fiksi (misal, serial televisi atau buku) tentang perang di Mars - tetapi tidak ada yang tahun 2076. Akal sehat juga memberitahu kita bahwa 2076 _adalah masa depan_ sehingga tidak bisa dikaitkan dengan peristiwa nyata.


Jadi apa yang terjadi ketika kita menjalankan prompt ini dengan penyedia LLM yang berbeda?

> **Respon 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/id/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Respon 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/id/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Respon 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/id/04-fabrication-huggingchat.faf82a0a51278956.webp)

Seperti yang diharapkan, setiap model (atau versi model) menghasilkan respon yang sedikit berbeda berkat perilaku stokastik dan variasi kemampuan model. Misalnya, satu model menargetkan audiens kelas 8 sementara yang lain mengasumsikan siswa sekolah menengah. Tetapi ketiga model ini menghasilkan respon yang dapat meyakinkan pengguna yang tidak berpengetahuan bahwa kejadian tersebut nyata.

Teknik rekayasa prompt seperti _metaprompting_ dan _konfigurasi suhu_ dapat mengurangi fabrikasi model sampai batas tertentu. Arsitektur rekayasa prompt baru juga mengintegrasikan alat dan teknik baru secara mulus ke dalam alur prompt, untuk mengurangi atau mengatasi beberapa efek ini.

## Studi Kasus: GitHub Copilot

Mari kita tutup bagian ini dengan mendapatkan gambaran bagaimana rekayasa prompt digunakan dalam solusi dunia nyata dengan melihat satu Studi Kasus: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot adalah "AI Pair Programmer" Anda - ia mengubah prompt teks menjadi penyelesaian kode dan terintegrasi dalam lingkungan pengembangan Anda (misalnya, Visual Studio Code) untuk pengalaman pengguna yang mulus. Seperti yang didokumentasikan dalam rangkaian blog di bawah ini, versi awal didasarkan pada model OpenAI Codex - dengan para insinyur cepat menyadari kebutuhan untuk menyempurnakan model dan mengembangkan teknik rekayasa prompt yang lebih baik, untuk meningkatkan kualitas kode. Pada bulan Juli, mereka [memperkenalkan model AI yang ditingkatkan yang melampaui Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) untuk saran yang lebih cepat.

Bacalah postingan tersebut secara berurutan, untuk mengikuti perjalanan pembelajaran mereka.

- **Mei 2023** | [GitHub Copilot menjadi lebih baik dalam memahami kode Anda](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mei 2023** | [Di dalam GitHub: Bekerja dengan LLM di balik GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Cara menulis prompt yang lebih baik untuk GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot melampaui Codex dengan model AI yang ditingkatkan](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Panduan Developer untuk Rekayasa Prompt dan LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Cara membangun aplikasi LLM enterprise: Pelajaran dari GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Anda juga dapat menelusuri [blog Engineering mereka](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) untuk lebih banyak posting seperti [ini](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) yang menunjukkan bagaimana model dan teknik ini _diterapkan_ untuk menjalankan aplikasi dunia nyata.

---

<!--
TEMPLATE PELAJARAN:
Unit ini harus mencakup konsep inti #2.
Perkuat konsep dengan contoh dan referensi.

KONSEP #2:
Desain Prompt.
Diilustrasikan dengan contoh.
-->

## Konstruksi Prompt

Kita sudah melihat mengapa rekayasa prompt penting - sekarang mari kita pahami bagaimana prompt _dibangun_ supaya kita dapat mengevaluasi berbagai teknik untuk desain prompt yang lebih efektif.

### Prompt Dasar

Mari mulai dengan prompt dasar: input teks yang dikirim ke model tanpa konteks lain. Berikut contoh - ketika kita mengirim beberapa kata pertama dari lagu kebangsaan AS ke OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), ia langsung _melengkapi_ respon dengan beberapa baris berikutnya, menggambarkan perilaku prediksi dasar.

| Prompt (Input)     | Penyelesaian (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Sepertinya kamu memulai lirik "The Star-Spangled Banner," lagu kebangsaan Amerika Serikat. Lirik lengkapnya adalah ...                     |

### Prompt Kompleks

Sekarang mari tambahkan konteks dan instruksi ke prompt dasar itu. [Chat Completion API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) memungkinkan kita membangun prompt kompleks sebagai kumpulan _pesan_ dengan:

- Pasangan input/output yang mencerminkan input _user_ dan respon _assistant_.
- Pesan sistem yang menetapkan konteks untuk perilaku atau kepribadian asisten.

Permintaan sekarang dalam bentuk di bawah ini, di mana _tokenisasi_ secara efektif menangkap informasi relevan dari konteks dan percakapan. Sekarang, mengubah konteks sistem bisa berdampak sama besar pada kualitas penyelesaian, seperti input pengguna yang diberikan.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Prompt Instruksi

Dalam contoh di atas, prompt pengguna adalah kueri teks sederhana yang dapat diartikan sebagai permintaan informasi. Dengan prompt _instruksi_, kita bisa menggunakan teks itu untuk menetapkan tugas lebih detail, memberikan panduan yang lebih baik kepada AI. Berikut contohnya:

| Prompt (Input)                                                                                                                                                                                                                         | Penyelesaian (Output)                                                                                                        | Jenis Instruksi   |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :---------------- |
| Tuliskan deskripsi Perang Saudara                                                                                                                                                                                                   | _menghasilkan sebuah paragraf sederhana_                                                                                      | Sederhana        |
| Tuliskan deskripsi Perang Saudara. Berikan tanggal dan peristiwa kunci serta deskripsikan signifikansinya                                                                                                                            | _menghasilkan paragraf diikuti daftar tanggal peristiwa kunci dengan deskripsi_                                              | Kompleks         |
| Tuliskan deskripsi Perang Saudara dalam 1 paragraf. Berikan 3 poin peluru dengan tanggal kunci dan signifikansinya. Berikan 3 poin peluru lagi dengan tokoh sejarah kunci dan kontribusinya. Kembalikan output sebagai file JSON                    | _menghasilkan detail lebih luas dalam kotak teks, diformat sebagai JSON yang dapat Anda salin-tempel ke file dan validasi sesuai kebutuhan_ | Kompleks. Terformat. |

## Konten Utama

Dalam contoh di atas, prompt masih cukup terbuka, membiarkan LLM memutuskan bagian dataset pra-latihannya yang relevan. Dengan pola desain _konten utama_, teks input dibagi menjadi dua bagian:

- sebuah instruksi (tindakan)
- konten relevan (yang memengaruhi tindakan)

Berikut contoh di mana instruksinya adalah "ringkas ini dalam 2 kalimat".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Penyelesaian (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter adalah planet kelima dari Matahari dan yang terbesar di Tata Surya. Ia adalah raksasa gas dengan massa seper seribu dari Matahari, tetapi dua setengah kali massa semua planet lain dalam Tata Surya digabungkan. Jupiter adalah salah satu objek paling terang yang terlihat dengan mata telanjang di langit malam, dan telah dikenal oleh peradaban kuno sejak sebelum sejarah tercatat. Ia dinamai menurut dewa Romawi Jupiter.[19] Saat dilihat dari Bumi, Jupiter bisa cukup terang sehingga cahaya pantulannya dapat menghasilkan bayangan yang terlihat,[20] dan secara rata-rata adalah objek alami ketiga paling terang di langit malam setelah Bulan dan Venus. <br/> **Ringkas ini dalam 2 kalimat pendek** | Jupiter, planet kelima dari Matahari, adalah yang terbesar di Tata Surya dan dikenal sebagai salah satu objek paling terang di langit malam. Dinamai menurut dewa Romawi Jupiter, ia adalah raksasa gas dengan massa dua setengah kali semua planet lain dalam Tata Surya digabungkan. |

Segment konten utama dapat digunakan dengan berbagai cara untuk menjalankan instruksi yang lebih efektif:

- **Contoh** - alih-alih memberi tahu model apa yang harus dilakukan dengan instruksi eksplisit, berikan contoh apa yang harus dilakukan dan biarkan ia menyimpulkan pola.
- **Isyarat** - ikuti instruksi dengan sebuah "isyarat" yang memicu penyelesaian, mengarahkan model ke respon yang lebih relevan.
- **Template** - ini adalah 'resep' yang dapat diulang untuk prompt dengan placeholder (variabel) yang bisa disesuaikan dengan data untuk kasus penggunaan spesifik.

Mari kita jelajahi ini dalam praktek.

### Menggunakan Contoh

Ini adalah pendekatan di mana Anda menggunakan konten utama untuk "memberi makan model" beberapa contoh output yang diinginkan untuk sebuah instruksi tertentu, dan membiarkannya menyimpulkan pola untuk output yang diinginkan. Berdasarkan jumlah contoh yang diberikan, kita dapat memiliki zero-shot prompting, one-shot prompting, few-shot prompting, dll.

Prompt sekarang terdiri dari tiga komponen:

- Deskripsi tugas
- Beberapa contoh output yang diinginkan
- Awal contoh baru (yang menjadi deskripsi tugas implisit)

| Jenis Pembelajaran | Prompt (Input)                                                                                                                                        | Penyelesaian (Output)            |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------- |
| Zero-shot     | "The Sun is Shining". Terjemahkan ke dalam bahasa Spanyol                                                                                           | "El Sol está brillando".         |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso".      |
| Few-shot      | Pemain berlari mengelilingi base => Baseball <br/> Pemain melakukan ace => Tenis <br/> Pemain memukul enam => Kriket <br/> Pemain melakukan slam-dunk =>   | Bola Basket                     |
|               |                                                                                                                                                       |                                 |

Perhatikan bagaimana kita harus memberikan instruksi eksplisit ("Terjemahkan ke dalam bahasa Spanyol") dalam zero-shot prompting, tetapi itu tersirat dalam contoh one-shot prompting. Contoh few-shot menunjukkan bagaimana menambahkan lebih banyak contoh memungkinkan model membuat inferensi yang lebih akurat tanpa tambahan instruksi.

### Isyarat Prompt

Teknik lain untuk menggunakan konten utama adalah memberikan _isyarat_ daripada contoh. Dalam hal ini, kita memberi model dorongan ke arah yang benar dengan _memulainya_ menggunakan cuplikan yang mencerminkan format respon yang diinginkan. Model kemudian "mengambil isyarat" untuk melanjutkan sesuai itu.

| Jumlah Isyarat | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Penyelesaian (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter adalah planet kelima dari Matahari dan yang terbesar di Tata Surya. Ia adalah raksasa gas dengan massa seper seribu dari Matahari, tetapi dua setengah kali massa semua planet lain dalam Tata Surya digabungkan. Jupiter adalah salah satu objek paling terang yang terlihat dengan mata telanjang di langit malam, dan telah dikenal oleh peradaban kuno sejak sebelum sejarah tercatat. <br/>**Ringkas Ini**                                       | Jupiter adalah planet terbesar di Tata Surya kita dan yang kelima dari Matahari. Ia adalah raksasa gas dengan massa 1/1000 dari Matahari, tapi lebih berat dari semua planet lain digabungkan. Peradaban kuno sudah lama mengetahui Jupiter dan ia mudah terlihat di langit malam. |
| 1              | Jupiter adalah planet kelima dari Matahari dan yang terbesar di Tata Surya. Ia adalah raksasa gas dengan massa seper seribu dari Matahari, tetapi dua setengah kali massa semua planet lain dalam Tata Surya digabungkan. Jupiter adalah salah satu objek paling terang yang terlihat dengan mata telanjang di langit malam, dan telah dikenal oleh peradaban kuno sejak sebelum sejarah tercatat. <br/>**Ringkas Ini** <br/> Apa yang kita pelajari adalah bahwa Jupiter | adalah planet kelima dari Matahari dan yang terbesar di Tata Surya. Ia adalah raksasa gas dengan massa seper seribu dari Matahari, tetapi dua setengah kali keseluruhan planet lain digabungkan. Ia mudah terlihat dengan mata telanjang dan telah dikenal sejak zaman kuno.          |

| 2              | Jupiter adalah planet kelima dari Matahari dan yang terbesar di Tata Surya. Ini adalah raksasa gas dengan massa seper seribu dari Matahari, tetapi dua setengah kali dari semua planet lain di Tata Surya secara gabungan. Jupiter adalah salah satu objek paling terang yang terlihat dengan mata telanjang di langit malam, dan telah dikenal oleh peradaban kuno sejak sebelum sejarah tercatat. <br/>**Ringkas Ini** <br/> 3 Fakta Teratas yang Kami Pelajari:         | 1. Jupiter adalah planet kelima dari Matahari dan yang terbesar di Tata Surya. <br/> 2. Ini adalah raksasa gas dengan massa seper seribu dari Matahari...<br/> 3. Jupiter telah terlihat dengan mata telanjang sejak zaman kuno ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Template Prompt

Template prompt adalah _resep yang sudah ditentukan sebelumnya untuk prompt_ yang dapat disimpan dan digunakan kembali sesuai kebutuhan, untuk mendorong pengalaman pengguna yang lebih konsisten dalam skala besar. Dalam bentuk paling sederhana, itu hanyalah kumpulan contoh prompt seperti [yang satu dari OpenAI ini](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) yang menyediakan komponen prompt interaktif (pesan pengguna dan sistem) serta format permintaan yang digerakkan oleh API - untuk mendukung penggunaan ulang.

Dalam bentuk yang lebih kompleks seperti [contoh ini dari LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) ini berisi _placeholder_ yang dapat diganti dengan data dari berbagai sumber (input pengguna, konteks sistem, sumber data eksternal dll.) untuk menghasilkan prompt secara dinamis. Ini memungkinkan kami membuat perpustakaan prompt yang dapat digunakan kembali yang dapat digunakan untuk mendorong pengalaman pengguna yang konsisten **secara programatik** dalam skala besar.

Akhirnya, nilai sebenarnya dari template terletak pada kemampuan untuk membuat dan menerbitkan _perpustakaan prompt_ untuk domain aplikasi vertikal - di mana template prompt kini _dioptimalkan_ untuk mencerminkan konteks atau contoh khusus aplikasi yang membuat respons lebih relevan dan akurat untuk audiens pengguna yang ditargetkan. Repositori [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) adalah contoh bagus dari pendekatan ini, mengkurasi perpustakaan prompt untuk domain pendidikan dengan penekanan pada tujuan utama seperti perencanaan pelajaran, desain kurikulum, bimbingan siswa dll.

## Konten Pendukung

Jika kita menganggap konstruksi prompt terdiri dari instruksi (tugas) dan target (konten utama), maka _konten sekunder_ seperti konteks tambahan yang kita berikan untuk **mempengaruhi keluaran dengan cara tertentu**. Ini bisa berupa parameter pengaturan, instruksi format, taksonomi topik dll. yang dapat membantu model _menyesuaikan_ responsnya agar sesuai dengan tujuan atau ekspektasi pengguna yang diinginkan.

Contohnya: Diberikan katalog kursus dengan metadata ekstensif (nama, deskripsi, level, tag metadata, instruktur dll.) pada semua kursus yang tersedia dalam kurikulum:

- kita dapat mendefinisikan instruksi untuk "merangkum katalog kursus untuk Musim Gugur 2023"
- kita dapat menggunakan konten utama untuk memberikan beberapa contoh keluaran yang diinginkan
- kita dapat menggunakan konten sekunder untuk mengidentifikasi 5 "tag" teratas yang diminati.

Sekarang, model dapat memberikan ringkasan dalam format yang ditunjukkan oleh beberapa contoh itu - tetapi jika hasilnya memiliki banyak tag, dapat memprioritaskan 5 tag yang telah diidentifikasi dalam konten sekunder.

---

<!--
TEMPLATE PELAJARAN:
Unit ini harus mencakup konsep inti #1.
Perkuat konsep dengan contoh dan referensi.

KONSEP #3:
Teknik Prompt Engineering.
Apa saja teknik dasar untuk rekayasa prompt?
Ilustrasikan dengan beberapa latihan.
-->

## Praktik Terbaik dalam Prompting

Sekarang setelah kita tahu bagaimana prompt dapat _dibuat_, kita dapat mulai memikirkan bagaimana _merancang_ mereka agar mencerminkan praktik terbaik. Kita dapat memikirkannya dalam dua bagian - memiliki _pola pikir_ yang tepat dan menerapkan _teknik_ yang benar.

### Pola Pikir Prompt Engineering

Prompt Engineering adalah proses coba-coba jadi ingatlah tiga faktor panduan utama ini:

1. **Pemahaman Domain Penting.** Akurasi dan relevansi respons adalah fungsi dari _domain_ tempat aplikasi atau pengguna itu beroperasi. Terapkan intuisi dan keahlian domain Anda untuk **menyesuaikan teknik** lebih jauh. Misalnya, definisikan _kepribadian spesifik domain_ dalam prompt sistem Anda, atau gunakan _template spesifik domain_ dalam prompt pengguna Anda. Berikan konten sekunder yang mencerminkan konteks spesifik domain, atau gunakan _isyarat dan contoh spesifik domain_ untuk membimbing model ke pola penggunaan yang familiar.

2. **Pemahaman Model Penting.** Kita tahu model bersifat stokastik secara alami. Tetapi implementasi model juga dapat bervariasi dalam hal dataset pelatihan yang digunakannya (pengetahuan pra-pelatihan), kemampuan yang disediakan (mis., melalui API atau SDK) dan jenis konten yang dioptimalkannya (mis., kode vs. gambar vs. teks). Pahami kekuatan dan keterbatasan model yang Anda gunakan, dan gunakan pengetahuan itu untuk _memprioritaskan tugas_ atau membangun _template khusus_ yang dioptimalkan untuk kemampuan model tersebut.

3. **Iterasi & Validasi Penting.** Model berkembang dengan cepat, demikian juga teknik untuk rekayasa prompt. Sebagai ahli domain, Anda mungkin memiliki konteks atau kriteria lain untuk aplikasi _Anda_ yang tidak berlaku untuk komunitas yang lebih luas. Gunakan alat & teknik rekayasa prompt untuk "memulai cepat" pembuatan prompt, lalu iterasi dan validasi hasilnya menggunakan intuisi dan keahlian domain Anda sendiri. Catat wawasan Anda dan buat **basis pengetahuan** (mis., perpustakaan prompt) yang dapat digunakan sebagai baseline baru oleh orang lain, untuk iterasi lebih cepat di masa mendatang.

## Praktik Terbaik

Sekarang mari lihat praktik terbaik umum yang dianjurkan oleh [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) dan praktisi [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Apa                              | Mengapa                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evaluasi model terbaru.       | Generasi model baru kemungkinan memiliki fitur dan kualitas yang lebih baik - tetapi mungkin juga menimbulkan biaya lebih tinggi. Evaluasi dampaknya, lalu buat keputusan migrasi.                                                                                |
| Pisahkan instruksi & konteks   | Periksa apakah model/penyedia Anda mendefinisikan _pembatas_ untuk membedakan instruksi, konten utama dan sekunder lebih jelas. Ini dapat membantu model memberi bobot token dengan lebih akurat.                                                         |
| Jadilah spesifik dan jelas             | Berikan lebih banyak detail tentang konteks, hasil, panjang, format, gaya yang diinginkan dll. Ini akan meningkatkan kualitas dan konsistensi respons. Tangkap resep dalam template yang dapat digunakan kembali.                                                          |
| Jadilah deskriptif, gunakan contoh      | Model mungkin merespons lebih baik dengan pendekatan "tunjukkan dan ceritakan". Mulailah dengan pendekatan `zero-shot` di mana Anda memberi instruksi (tetapi tanpa contoh) lalu coba `few-shot` sebagai penyempurnaan, memberikan beberapa contoh keluaran yang diinginkan. Gunakan analogi. |
| Gunakan isyarat untuk memulai penyelesaian | Dorong model ke hasil yang diinginkan dengan memberinya beberapa kata atau frasa pembuka yang dapat digunakan sebagai titik awal dalam respons.                                                                                                               |
| Gandakan                       | Kadang Anda perlu mengulangi instruksi kepada model. Beri instruksi sebelum dan setelah konten utama Anda, gunakan instruksi dan isyarat, dll. Iterasi & validasi untuk melihat apa yang berhasil.                                                         |
| Urutan Penting                     | Urutan informasi yang Anda sajikan ke model dapat memengaruhi keluaran, bahkan dalam contoh pembelajaran, berkat bias terbaru (recency bias). Coba berbagai opsi untuk melihat mana yang paling efektif.                                                               |
| Beri model “jalan keluar”           | Beri model respons penyelesaian _cadangan_ yang dapat diberikan jika tidak dapat menyelesaikan tugas karena alasan apa pun. Ini dapat mengurangi kemungkinan model menghasilkan respons yang salah atau dibuat-buat.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Seperti pada praktik terbaik lainnya, ingat bahwa _hasil Anda bisa berbeda_ berdasarkan model, tugas dan domain. Gunakan ini sebagai titik awal, dan iterasi untuk menemukan apa yang terbaik untuk Anda. Terus evaluasi ulang proses rekayasa prompt Anda saat model dan alat baru tersedia, dengan fokus pada skalabilitas proses dan kualitas respons.

<!--
TEMPLATE PELAJARAN:
Unit ini harus menyediakan tantangan kode jika relevan

TANTANGAN:
Tautkan ke Jupyter Notebook dengan hanya komentar kode dalam instruksi (bagian kode kosong).

SOLUSI:
Tautkan ke salinan Notebook tersebut dengan prompt diisi dan dijalankan, menunjukkan satu contoh keluaran.
-->

## Tugas

Selamat! Anda telah sampai di akhir pelajaran! Saatnya menguji beberapa konsep dan teknik dengan contoh nyata!

Untuk tugas kita, kita akan menggunakan Jupyter Notebook dengan latihan yang dapat Anda selesaikan secara interaktif. Anda juga dapat memperluas Notebook dengan sel Markdown dan Kode Anda sendiri untuk mengeksplorasi ide dan teknik secara mandiri.

### Untuk memulai, buat fork repo, lalu

- (Direkomendasikan) Luncurkan GitHub Codespaces
- (Alternatif) Salin repo ke perangkat lokal Anda dan gunakan dengan Docker Desktop
- (Alternatif) Buka Notebook dengan lingkungan runtime Notebook pilihan Anda.

### Selanjutnya, konfigurasikan variabel lingkungan Anda

- Salin file `.env.copy` di root repo ke `.env` dan isi nilai `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` dan `AZURE_OPENAI_DEPLOYMENT`. Kembali ke bagian [Learning Sandbox](#sandbox-pembelajaran) untuk belajar caranya.

### Selanjutnya, buka Jupyter Notebook

- Pilih kernel runtime. Jika menggunakan opsi 1 atau 2, cukup pilih kernel Python 3.10.x default yang disediakan oleh dev container.

Anda siap menjalankan latihannya. Perlu dicatat bahwa di sini tidak ada jawaban _benar atau salah_ - hanya eksplorasi opsi dengan coba-coba dan membangun intuisi untuk apa yang bekerja untuk model dan domain aplikasi tertentu.

_Untuk alasan ini tidak ada segmen Solusi Kode dalam pelajaran ini. Sebagai gantinya, Notebook akan memiliki sel Markdown berjudul "My Solution:" yang menunjukkan satu contoh keluaran sebagai referensi._

 <!--
TEMPLATE PELAJARAN:
Bungkus bagian ini dengan ringkasan dan sumber daya untuk pembelajaran mandiri.
-->

## Pemeriksaan Pengetahuan

Mana dari berikut ini adalah prompt yang baik mengikuti beberapa praktik terbaik yang masuk akal?

1. Tunjukkan saya gambar mobil merah
2. Tunjukkan saya gambar mobil merah merk Volvo dan model XC90 diparkir di tepi tebing dengan matahari terbenam
3. Tunjukkan saya gambar mobil merah merk Volvo dan model XC90

A: 2, itu adalah prompt terbaik karena memberikan detail tentang "apa" dan masuk ke spesifik (bukan sembarang mobil tapi merek dan model tertentu) dan juga menggambarkan latar secara keseluruhan. 3 adalah yang terbaik berikutnya karena juga mengandung banyak deskripsi.

## 🚀 Tantangan

Cobalah gunakan teknik "isyarat" dengan prompt: Lengkapi kalimat "Tunjukkan saya gambar mobil merah merk Volvo dan ". Apa responsnya, dan bagaimana Anda akan memperbaikinya?

## Kerja Bagus! Lanjutkan Pembelajaran Anda

Ingin belajar lebih banyak tentang konsep Prompt Engineering? Pergi ke [halaman pembelajaran lanjutan](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk menemukan sumber daya hebat lainnya tentang topik ini.

Arahkan ke Pelajaran 5 di mana kita akan melihat [teknik prompt tingkat lanjut](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->