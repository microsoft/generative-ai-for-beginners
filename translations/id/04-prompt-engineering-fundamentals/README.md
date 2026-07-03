# Dasar-dasar Rekayasa Prompt

[![Dasar-dasar Rekayasa Prompt](../../../translated_images/id/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Pendahuluan
Modul ini membahas konsep dan teknik penting untuk membuat prompt yang efektif dalam model AI generatif. Cara Anda menulis prompt ke sebuah LLM juga penting. Prompt yang dirancang dengan cermat dapat menghasilkan respons dengan kualitas yang lebih baik. Namun apa sebenarnya arti istilah seperti _prompt_ dan _rekayasa prompt_? Dan bagaimana saya memperbaiki _input_ prompt yang saya kirim ke LLM? Ini adalah pertanyaan yang akan kita coba jawab dalam bab ini dan bab berikutnya.

_AI Generatif_ mampu menciptakan konten baru (misalnya, teks, gambar, audio, kode, dll.) sebagai tanggapan atas permintaan pengguna. AI ini mencapai hal tersebut dengan menggunakan _Large Language Models_ seperti seri GPT dari OpenAI ("Generative Pre-trained Transformer") yang dilatih untuk menggunakan bahasa alami dan kode.

Pengguna sekarang dapat berinteraksi dengan model-model ini menggunakan paradigma yang familiar seperti chat, tanpa memerlukan keahlian teknis atau pelatihan. Model-model tersebut _berbasis prompt_ - pengguna mengirim input teks (prompt) dan mendapatkan kembali tanggapan AI (completion). Mereka kemudian dapat "mengobrol dengan AI" secara berulang, dalam percakapan multi-giliran, memperbaiki prompt mereka hingga responsnya sesuai dengan yang diharapkan.

"Prompt" kini menjadi _antarmuka pemrograman_ utama untuk aplikasi AI generatif, memberitahu model apa yang harus dilakukan dan memengaruhi kualitas respons yang diberikan. "Rekayasa Prompt" adalah bidang studi yang berkembang pesat yang berfokus pada _desain dan optimasi_ prompt untuk menghasilkan respons yang konsisten dan berkualitas dalam skala besar.

## Tujuan Pembelajaran

Dalam pelajaran ini, kita akan mempelajari apa itu Rekayasa Prompt, mengapa hal itu penting, dan bagaimana kita dapat merancang prompt yang lebih efektif untuk model dan tujuan aplikasi tertentu. Kita akan memahami konsep inti dan praktik terbaik untuk rekayasa prompt - serta mempelajari lingkungan "sandbox" interaktif Jupyter Notebooks di mana kita dapat melihat konsep ini diterapkan pada contoh nyata.

Pada akhir pelajaran ini kita akan mampu:

1. Menjelaskan apa itu rekayasa prompt dan mengapa hal itu penting.
2. Menggambarkan komponen dari sebuah prompt dan bagaimana cara menggunakannya.
3. Mempelajari praktik terbaik dan teknik untuk rekayasa prompt.
4. Menerapkan teknik yang dipelajari pada contoh nyata, menggunakan endpoint OpenAI.

## Istilah Kunci

Rekayasa Prompt: Praktik merancang dan menyempurnakan input untuk mengarahkan model AI menghasilkan output yang diinginkan.  
Tokenisasi: Proses mengubah teks menjadi unit-unit kecil, disebut token, yang dapat dipahami dan diproses oleh model.  
Instruction-Tuned LLMs: Large Language Models (LLM) yang telah disesuaikan dengan instruksi spesifik untuk meningkatkan akurasi dan relevansi tanggapannya.

## Sandbox Pembelajaran

Rekayasa prompt saat ini lebih merupakan seni daripada sains. Cara terbaik untuk meningkatkan intuisi kita adalah dengan _berlatih lebih banyak_ dan menggunakan pendekatan coba-coba yang menggabungkan keahlian domain aplikasi dengan teknik yang direkomendasikan serta optimasi spesifik model.

Jupyter Notebook yang menyertai pelajaran ini menyediakan lingkungan _sandbox_ di mana Anda bisa mencoba apa yang Anda pelajari—secara langsung atau sebagai bagian dari tantangan kode di akhir. Untuk menjalankan latihan, Anda memerlukan:

1. **Kunci API Azure OpenAI** - endpoint layanan untuk LLM yang sudah dideploy.  
2. **Runtime Python** - tempat Notebook dapat dijalankan.  
3. **Variabel Lingkungan Lokal** - _selesaikan langkah-langkah [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) sekarang untuk siap digunakan_.

Notebook ini dilengkapi dengan latihan _pemula_ - namun Anda didorong untuk menambah bagian _Markdown_ (deskripsi) dan _Kode_ (permintaan prompt) sendiri untuk mencoba lebih banyak contoh atau ide - dan membangun intuisi Anda dalam desain prompt.

## Panduan Bergambar

Ingin melihat gambaran besar tentang apa yang akan dibahas dalam pelajaran ini sebelum mulai? Lihat panduan bergambar ini, yang memberikan Anda gambaran topik utama yang dibahas dan poin-poin kunci yang bisa Anda pikirkan di setiap bagian. Peta jalan pelajaran ini membawa Anda dari pemahaman konsep inti dan tantangan hingga mengatasinya dengan teknik dan praktik terbaik rekayasa prompt yang relevan. Perlu dicatat bahwa bagian "Teknik Lanjutan" dalam panduan ini merujuk pada konten yang dibahas dalam bab _berikutnya_ dari kurikulum ini.

![Panduan Bergambar Rekayasa Prompt](../../../translated_images/id/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Startup Kami

Sekarang, mari kita bahas bagaimana _topik ini_ terkait dengan misi startup kami untuk [membawa inovasi AI ke pendidikan](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Kami ingin membangun aplikasi berbasis AI untuk _pembelajaran yang dipersonalisasi_ - jadi mari kita pikirkan bagaimana berbagai pengguna aplikasi kami mungkin "merancang" prompt:

- **Administrator** mungkin meminta AI untuk _menganalisis data kurikulum guna mengidentifikasi kesenjangan materi_. AI dapat merangkum hasil atau memvisualisasikannya dengan kode.  
- **Pendidik** mungkin meminta AI untuk _menghasilkan rencana pelajaran untuk audiens dan topik tertentu_. AI dapat membuat rencana yang dipersonalisasi dalam format yang ditentukan.  
- **Siswa** mungkin meminta AI untuk _membimbing mereka dalam mata pelajaran sulit_. AI kini dapat membimbing siswa dengan pelajaran, petunjuk, dan contoh yang disesuaikan dengan tingkat mereka.

Itu hanya sebagian kecil dari kemungkinan. Lihat [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - perpustakaan prompt open-source yang dikurasi oleh para ahli pendidikan - untuk mendapatkan gambaran lebih luas tentang kemungkinannya! _Cobalah menjalankan beberapa prompt tersebut di sandbox atau menggunakan OpenAI Playground untuk melihat apa yang terjadi!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Apa itu Rekayasa Prompt?

Kita memulai pelajaran ini dengan mendefinisikan **Rekayasa Prompt** sebagai proses _merancang dan mengoptimalkan_ input teks (prompt) untuk menghasilkan respons (completion) yang konsisten dan berkualitas untuk tujuan aplikasi dan model tertentu. Kita bisa memandang ini sebagai proses dua langkah:

- _merancang_ prompt awal untuk model dan tujuan tertentu  
- _memperbaiki_ prompt secara iteratif untuk meningkatkan kualitas respons

Ini secara otomatis merupakan proses coba-coba yang membutuhkan intuisi pengguna dan usaha agar mendapatkan hasil optimal. Jadi mengapa ini penting? Untuk menjawab pertanyaan itu, kita harus memahami tiga konsep:

- _Tokenisasi_ = bagaimana model "melihat" prompt  
- _Base LLMs_ = bagaimana model dasar "memproses" sebuah prompt  
- _Instruction-Tuned LLMs_ = bagaimana model kini bisa "melihat tugas"

### Tokenisasi

LLM memandang prompt sebagai _urutan token_ di mana model berbeda (atau versi model yang berbeda) dapat melakukan tokenisasi prompt yang sama dengan cara berbeda. Karena LLM dilatih pada token (bukan teks mentah), cara prompt di-tokenisasi langsung memengaruhi kualitas respons yang dihasilkan.

Untuk mendapatkan intuisi tentang bagaimana tokenisasi bekerja, coba alat seperti [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) yang ditunjukkan di bawah ini. Salin prompt Anda - dan lihat bagaimana itu diubah menjadi token, perhatikan bagaimana karakter spasi dan tanda baca diperlakukan. Perlu diingat contoh ini menunjukkan LLM lama (GPT-3) - jadi mencoba dengan model yang lebih baru mungkin menghasilkan hasil berbeda.

![Tokenisasi](../../../translated_images/id/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Konsep: Model Dasar

Setelah prompt di-tokenisasi, fungsi utama dari ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (atau model dasar) adalah memprediksi token berikutnya dalam urutan itu. Karena LLM dilatih pada dataset teks besar, mereka memiliki pemahaman hubungan statistik antar token dan dapat membuat prediksi dengan keyakinan tertentu. Perlu dicatat mereka tidak memahami _makna_ kata dalam prompt atau token; mereka hanya melihat pola yang dapat mereka "selesaikan" dengan prediksi berikutnya. Mereka dapat melanjutkan memprediksi urutan sampai dihentikan oleh intervensi pengguna atau kondisi yang telah ditetapkan sebelumnya.

Ingin melihat bagaimana penyelesaian berbasis prompt bekerja? Masukkan prompt di atas ke Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) dengan pengaturan default. Sistem dikonfigurasi untuk memperlakukan prompt sebagai permintaan informasi - sehingga Anda harus melihat penyelesaian yang sesuai konteks ini.

Namun bagaimana jika pengguna ingin melihat sesuatu yang spesifik sesuai kriteria atau tujuan tugas? Di sinilah _instruction-tuned_ LLM masuk ke gambar.

![Penyelesaian Chat Base LLM](../../../translated_images/id/04-playground-chat-base.65b76fcfde0caa67.webp)

### Konsep: Instruction Tuned LLMs

[Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) memulai dengan model dasar dan menyempurnakannya dengan contoh atau pasangan input/output (misalnya, "pesan" multi-giliran) yang dapat berisi instruksi jelas - dan tanggapan AI berusaha mengikuti instruksi tersebut.

Ini menggunakan teknik seperti Reinforcement Learning with Human Feedback (RLHF) yang melatih model untuk _mengikuti instruksi_ dan _belajar dari umpan balik_ sehingga memberikan respons yang lebih sesuai dengan aplikasi praktis dan lebih relevan dengan tujuan pengguna.

Mari coba — ulangi prompt di atas, namun ubah _pesan sistem_ untuk memberikan instruksi berikut sebagai konteks:

> _Ringkas konten yang diberikan untuk siswa kelas dua SD. Simpan hasilnya dalam satu paragraf dengan 3-5 poin peluru._

Lihat bagaimana hasilnya kini disesuaikan untuk mencerminkan tujuan dan format yang diinginkan? Seorang pendidik kini dapat langsung menggunakan respons ini dalam slide untuk kelas tersebut.

![Penyelesaian Chat Instruction Tuned LLM](../../../translated_images/id/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Mengapa Kita Membutuhkan Rekayasa Prompt?

Sekarang kita tahu bagaimana prompt diproses oleh LLM, mari kita bahas _mengapa_ kita membutuhkan rekayasa prompt. Jawaban terletak pada fakta bahwa LLM saat ini menghadirkan sejumlah tantangan yang membuat _penyelesaian yang andal dan konsisten_ lebih sulit dicapai tanpa upaya dalam konstruksi dan optimasi prompt. Misalnya:

1. **Respons model bersifat stokastik.** _Prompt yang sama_ kemungkinan akan menghasilkan respons berbeda dengan model atau versi model yang berbeda. Dan bahkan dapat menghasilkan hasil berbeda dengan _model yang sama_ pada waktu berbeda. _Teknik rekayasa prompt dapat membantu meminimalkan variasi ini dengan memberikan pembatas yang lebih baik_.

1. **Model bisa membuat respons palsu.** Model dilatih dengan dataset _besar namun terbatas_, artinya mereka tidak memiliki pengetahuan tentang konsep di luar ruang lingkup pelatihan tersebut. Akibatnya, mereka dapat menghasilkan penyelesaian yang tidak akurat, imajinatif, atau bahkan bertentangan langsung dengan fakta yang diketahui. _Teknik rekayasa prompt membantu pengguna mengidentifikasi dan mengurangi kekeliruan semacam itu misalnya dengan meminta kutipan atau penalaran AI_.

1. **Kemampuan model akan berbeda.** Model atau generasi model yang lebih baru akan memiliki kemampuan lebih kaya namun juga membawa keunikan dan trade-off dalam biaya & kompleksitas. _Rekayasa prompt dapat membantu kita mengembangkan praktik terbaik dan alur kerja yang mengabstraksi perbedaan dan menyesuaikan dengan kebutuhan spesifik model secara skalabel dan mulus_.

Mari lihat ini dalam tindakan di OpenAI atau Azure OpenAI Playground:

- Gunakan prompt yang sama dengan berbagai deployment LLM (misalnya, OpenAI, Azure OpenAI, Hugging Face) - apakah Anda melihat variasinya?  
- Gunakan prompt yang sama berulang kali dengan deployment LLM _yang sama_ (misalnya, Azure OpenAI playground) - bagaimana variasi-variasi tersebut berbeda?

### Contoh Fabrications

Dalam kursus ini, kami menggunakan istilah **"fabrication"** untuk merujuk pada fenomena di mana LLM kadang menghasilkan informasi yang salah secara faktual karena keterbatasan dalam pelatihan atau kendala lain. Anda mungkin juga pernah mendengar istilah ini disebut _"halusinasi"_ dalam artikel populer atau makalah riset. Namun, kami sangat menyarankan menggunakan istilah _"fabrication"_ agar kita tidak secara tidak sengaja mengantropomorfisasi perilaku ini dengan mengaitkan sifat manusia ke hasil yang digerakkan mesin. Ini juga memperkuat pedoman [AI yang Bertanggung Jawab](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) dari perspektif terminologi, menghilangkan istilah yang bisa dianggap ofensif atau tidak inklusif dalam konteks tertentu.

Ingin memahami bagaimana fabrication bekerja? Pikirkan prompt yang menginstruksikan AI untuk membuat konten tentang topik yang tidak ada (untuk memastikan topik tersebut tidak ada dalam dataset pelatihan). Misalnya - saya mencoba prompt berikut:

> **Prompt:** buat rencana pelajaran tentang Perang Mars tahun 2076.
Pencarian web menunjukkan bahwa ada kisah fiksi (misalnya, serial televisi atau buku) tentang perang Mars - tetapi tidak ada di tahun 2076. Akal sehat juga memberi tahu kita bahwa 2076 adalah _di masa depan_ dan oleh karena itu, tidak dapat dikaitkan dengan peristiwa nyata.

Jadi apa yang terjadi ketika kita menjalankan prompt ini dengan penyedia LLM yang berbeda?

> **Respons 1**: OpenAI Playground (GPT-35)

![Respons 1](../../../translated_images/id/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Respons 2**: Azure OpenAI Playground (GPT-35)

![Respons 2](../../../translated_images/id/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Respons 3**: : Hugging Face Chat Playground (LLama-2)

![Respons 3](../../../translated_images/id/04-fabrication-huggingchat.faf82a0a51278956.webp)

Seperti yang diharapkan, setiap model (atau versi model) menghasilkan respons yang sedikit berbeda berkat perilaku stokastik dan variasi kemampuan model. Misalnya, satu model menargetkan audiens kelas 8 sedangkan model lainnya mengasumsikan seorang siswa sekolah menengah atas. Tetapi ketiga model tersebut menghasilkan respons yang dapat meyakinkan pengguna yang tidak berpengetahuan bahwa peristiwa tersebut nyata.

Teknik rekayasa prompt seperti _metaprompting_ dan _konfigurasi temperatur_ mungkin dapat mengurangi fabrikasi model sampai batas tertentu. Arsitektur rekayasa prompt _baru_ juga mengintegrasikan alat dan teknik baru secara mulus dalam alur prompt, untuk mengurangi atau memitigasi beberapa efek ini.

## Studi Kasus: GitHub Copilot

Mari kita tutup bagian ini dengan mendapatkan gambaran bagaimana rekayasa prompt digunakan dalam solusi dunia nyata dengan melihat satu Studi Kasus: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot adalah "Pasangan Pemrogram AI" Anda - ia mengubah prompt teks menjadi penyelesaian kode dan terintegrasi ke dalam lingkungan pengembangan Anda (misalnya, Visual Studio Code) untuk pengalaman pengguna yang mulus. Seperti yang didokumentasikan dalam serangkaian blog di bawah ini, versi awal didasarkan pada model OpenAI Codex - di mana para insinyur dengan cepat menyadari perlunya menyempurnakan model dan mengembangkan teknik rekayasa prompt yang lebih baik, untuk meningkatkan kualitas kode. Pada bulan Juli, mereka [meluncurkan model AI yang lebih baik yang melampaui Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) untuk saran yang lebih cepat.

Bacalah postingan-postingan tersebut secara berurutan, untuk mengikuti perjalanan pembelajaran mereka.

- **Mei 2023** | [GitHub Copilot Semakin Baik Memahami Kode Anda](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mei 2023** | [Di Dalam GitHub: Bekerja dengan LLM di Balik GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Cara Menulis Prompt Lebih Baik untuk GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot Melampaui Codex dengan Model AI yang Lebih Baik](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Panduan Pengembang untuk Rekayasa Prompt dan LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Cara Membangun Aplikasi LLM Perusahaan: Pelajaran dari GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Anda juga dapat menjelajahi [blog Teknik](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) mereka untuk lebih banyak postingan seperti [yang ini](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) yang menunjukkan bagaimana model dan teknik ini _diterapkan_ untuk menggerakkan aplikasi dunia nyata.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Konstruksi Prompt

Kita sudah melihat mengapa rekayasa prompt penting - sekarang mari kita pahami bagaimana prompt _dibangun_ sehingga kita bisa mengevaluasi berbagai teknik untuk desain prompt yang lebih efektif.

### Prompt Dasar

Mari mulai dengan prompt dasar: input teks yang dikirim ke model tanpa konteks lain. Berikut contoh - ketika kita mengirim beberapa kata pertama dari lagu kebangsaan AS ke OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) itu langsung _melengkapi_ respons dengan beberapa baris berikutnya, menggambarkan perilaku prediksi dasar.

| Prompt (Input)     | Penyelesaian (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Kedengarannya seperti Anda sedang memulai lirik "The Star-Spangled Banner," lagu kebangsaan Amerika Serikat. Lirik lengkapnya adalah ... |

### Prompt Kompleks

Sekarang mari kita tambahkan konteks dan instruksi ke prompt dasar itu. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) memungkinkan kita membangun prompt kompleks sebagai kumpulan _pesan_ dengan:

- Pasangan input/output yang mencerminkan input _pengguna_ dan respons _asisten_.
- Pesan sistem yang mengatur konteks untuk perilaku atau kepribadian asisten.

Permintaan sekarang dalam bentuk berikut, di mana _tokenisasi_ secara efektif menangkap informasi relevan dari konteks dan percakapan. Sekarang, mengubah konteks sistem bisa sama berpengaruhnya terhadap kualitas penyelesaian, seperti input pengguna yang diberikan.

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

Dalam contoh-contoh di atas, prompt pengguna adalah kueri teks sederhana yang dapat diartikan sebagai permintaan informasi. Dengan prompt _instruksi_, kita dapat menggunakan teks itu untuk menentukan tugas secara lebih rinci, memberikan panduan yang lebih baik kepada AI. Berikut contohnya:

| Prompt (Input)                                                                                                                                                                                                                         | Penyelesaian (Output)                                                                                                        | Jenis Instruksi     |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Tulis deskripsi Perang Saudara                                                                                                                                                                                                       | _mengembalikan paragraf sederhana_                                                                                          | Sederhana           |
| Tulis deskripsi Perang Saudara. Berikan tanggal dan peristiwa penting dan jelaskan signifikansinya                                                                                                                                    | _mengembalikan paragraf diikuti daftar tanggal peristiwa penting beserta deskripsinya_                                      | Kompleks            |
| Tulis deskripsi Perang Saudara dalam 1 paragraf. Berikan 3 poin peluru dengan tanggal penting dan signifikansinya. Berikan 3 poin peluru lagi dengan tokoh sejarah penting dan kontribusinya. Kembalikan hasil dalam format file JSON       | _mengembalikan detail lebih luas dalam kotak teks, diformat sebagai JSON yang dapat Anda salin-tempel ke file dan validasi sesuai kebutuhan_ | Kompleks. Terformat. |

## Konten Utama

Dalam contoh-contoh di atas, prompt masih cukup terbuka, membiarkan LLM memutuskan bagian mana dari dataset yang telah dipelajari yang relevan. Dengan pola desain _konten utama_, teks input dibagi menjadi dua bagian:

- instruksi (aksi)
- konten relevan (yang memengaruhi aksi)

Berikut contoh di mana instruksinya adalah "ringkas ini dalam 2 kalimat".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Penyelesaian (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter adalah planet kelima dari Matahari dan terbesar di Tata Surya. Ia adalah raksasa gas dengan massa seper seribu kali Massa Matahari, tetapi dua setengah kali massa semua planet lain di Tata Surya digabungkan. Jupiter adalah salah satu benda paling terang yang terlihat oleh mata telanjang di langit malam, dan telah dikenal oleh peradaban kuno sejak sebelum sejarah tercatat. Ia dinamai berdasarkan dewa Romawi Jupiter.[19] Ketika dilihat dari Bumi, Jupiter bisa cukup terang untuk cahaya pantulannya dapat menimbulkan bayangan yang terlihat,[20] dan rata-rata merupakan benda alami ketiga paling terang di langit malam setelah Bulan dan Venus. <br/> **Ringkas ini dalam 2 kalimat pendek** | Jupiter, planet kelima dari Matahari, adalah yang terbesar di Tata Surya dan dikenal sebagai salah satu benda paling terang di langit malam. Dinamai menurut dewa Romawi Jupiter, itu adalah raksasa gas dengan massa dua setengah kali massa semua planet lain di Tata Surya jika digabungkan. |

Segmen konten utama dapat digunakan dengan berbagai cara untuk memberikan instruksi yang lebih efektif:

- **Contoh** - alih-alih memberitahu model apa yang harus dilakukan dengan instruksi eksplisit, berikan contoh apa yang harus dilakukan dan biarkan model mengambil pola.
- **Isyarat** - ikuti instruksi dengan "isyarat" yang memberi pengarahan untuk penyelesaian, membimbing model ke respons yang lebih relevan.
- **Templat** - ini adalah 'resep' yang dapat diulangi untuk prompt dengan tempat-tempat penampung (variabel) yang dapat disesuaikan dengan data untuk kasus penggunaan tertentu.

Mari kita jelajahi ini dalam praktik.

### Menggunakan Contoh

Ini adalah pendekatan di mana Anda menggunakan konten utama untuk "memberi makan model" beberapa contoh output yang diinginkan untuk instruksi tertentu, dan membiarkannya mengambil pola untuk output yang diinginkan. Berdasarkan jumlah contoh yang diberikan, kita dapat memiliki zero-shot prompting, one-shot prompting, few-shot prompting dan sebagainya.

Prompt sekarang terdiri dari tiga komponen:

- Deskripsi tugas
- Beberapa contoh output yang diinginkan
- Awal contoh baru (yang menjadi deskripsi tugas implisit)

| Jenis Pembelajaran | Prompt (Input)                                                                                                                                        | Penyelesaian (Output)         |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------- |
| Zero-shot          | "The Sun is Shining". Terjemahkan ke Bahasa Spanyol                                                                                                  | "El Sol está brillando".      |
| One-shot           | "The Sun is Shining" => "El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso".   |
| Few-shot           | Pemain berlari di base => Baseball <br/> Pemain memukul ace => Tenis <br/> Pemain memukul enam => Kriket <br/> Pemain melakukan slam-dunk =>            | Basket                       |
|                    |                                                                                                                                                      |                              |

Perhatikan bagaimana kita harus memberikan instruksi eksplisit ("Terjemahkan ke Bahasa Spanyol") pada zero-shot prompting, tetapi instruksi itu berkembang menjadi implisit pada contoh one-shot prompting. Contoh few-shot menunjukkan bagaimana menambahkan lebih banyak contoh memungkinkan model membuat inferensi yang lebih akurat tanpa instruksi tambahan.

### Isyarat Prompt

Teknik lain untuk menggunakan konten utama adalah memberikan _isyarat_ daripada contoh. Dalam hal ini, kita memberikan model dorongan ke arah yang benar dengan _memulai_ dengan cuplikan yang mencerminkan format respons yang diinginkan. Model kemudian "mengambil isyarat" untuk melanjutkan dalam jalur itu.

| Jumlah Isyarat | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Penyelesaian (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter adalah planet kelima dari Matahari dan terbesar di Tata Surya. Ia adalah raksasa gas dengan massa seper seribu kali Massa Matahari, tetapi dua setengah kali massa semua planet lain di Tata Surya digabungkan. Jupiter adalah salah satu benda paling terang yang terlihat oleh mata telanjang di langit malam, dan telah dikenal oleh peradaban kuno sejak sebelum sejarah tercatat. <br/>**Ringkas Ini**                                       | Jupiter adalah planet terbesar di Tata Surya kita dan planet kelima dari Matahari. Ia adalah raksasa gas dengan massa 1/1000 dari Matahari, tetapi massanya lebih berat dari semua planet lain digabungkan. Peradaban kuno telah lama mengetahui keberadaan Jupiter, dan itu mudah terlihat di langit malam.. |
| 1              | Jupiter adalah planet kelima dari Matahari dan yang terbesar di Tata Surya. Ini adalah raksasa gas dengan massa sepertiga ribu massa Matahari, tetapi dua setengah kali massa semua planet lain di Tata Surya digabungkan. Jupiter adalah salah satu objek paling terang yang dapat dilihat dengan mata telanjang di langit malam, dan telah dikenal oleh peradaban kuno sejak sebelum sejarah tercatat. <br/>**Ringkas Ini** <br/> Apa yang kita pelajari adalah bahwa Jupiter | adalah planet kelima dari Matahari dan yang terbesar di Tata Surya. Ini adalah raksasa gas dengan massa sepertiga ribu massa Matahari, tetapi dua setengah kali massa semua planet lain digabungkan. Ini mudah terlihat dengan mata telanjang dan telah dikenal sejak zaman kuno.                        |
| 2              | Jupiter adalah planet kelima dari Matahari dan yang terbesar di Tata Surya. Ini adalah raksasa gas dengan massa sepertiga ribu massa Matahari, tetapi dua setengah kali massa semua planet lain di Tata Surya digabungkan. Jupiter adalah salah satu objek paling terang yang dapat dilihat dengan mata telanjang di langit malam, dan telah dikenal oleh peradaban kuno sejak sebelum sejarah tercatat. <br/>**Ringkas Ini** <br/> 3 Fakta Teratas yang Kami Pelajari:         | 1. Jupiter adalah planet kelima dari Matahari dan yang terbesar di Tata Surya. <br/> 2. Ini adalah raksasa gas dengan massa sepertiga ribu massa Matahari...<br/> 3. Jupiter telah terlihat dengan mata telanjang sejak zaman kuno ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt Templates

Template prompt adalah _resep pra-definisi untuk sebuah prompt_ yang dapat disimpan dan digunakan ulang sesuai kebutuhan, untuk menghasilkan pengalaman pengguna yang lebih konsisten dalam skala besar. Dalam bentuk paling sederhana, ini hanyalah kumpulan contoh prompt seperti [yang ini dari OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) yang menyediakan komponen prompt interaktif (pesan pengguna dan sistem) serta format permintaan yang digerakkan API - untuk mendukung penggunaan ulang.

Dalam bentuk yang lebih kompleks seperti [contoh ini dari LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) mengandung _placeholder_ yang dapat digantikan dengan data dari berbagai sumber (input pengguna, konteks sistem, sumber data eksternal, dll.) untuk menghasilkan prompt secara dinamis. Ini memungkinkan kita membuat perpustakaan prompt yang dapat digunakan ulang untuk menghasilkan pengalaman pengguna yang konsisten **secara programatik** dalam skala besar.

Akhirnya, nilai sebenarnya dari template adalah kemampuannya untuk membuat dan menerbitkan _perpustakaan prompt_ untuk domain aplikasi vertikal - di mana template prompt kini _dioptimalkan_ untuk merefleksikan konteks atau contoh khusus aplikasi yang membuat respons lebih relevan dan akurat bagi audiens pengguna yang ditargetkan. Repositori [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) adalah contoh bagus dari pendekatan ini, mengkurasi perpustakaan prompt untuk domain pendidikan dengan penekanan pada tujuan utama seperti perencanaan pelajaran, desain kurikulum, bimbingan siswa, dll.

## Supporting Content

Jika kita memandang konstruksi prompt sebagai memiliki instruksi (tugas) dan target (konten utama), maka _konten sekunder_ seperti konteks tambahan yang kita berikan untuk **mempengaruhi keluaran dengan cara tertentu**. Ini bisa berupa parameter penyetelan, instruksi format, taksonomi topik, dll. yang membantu model _menyesuaikan_ respons agar sesuai dengan tujuan atau ekspektasi pengguna yang diinginkan.

Misalnya: Diberikan katalog kursus dengan metadata ekstensif (nama, deskripsi, level, tag metadata, instruktur, dll.) pada semua kursus yang tersedia dalam kurikulum:

- kita dapat mendefinisikan instruksi untuk "membuat ringkasan katalog kursus untuk Fall 2023"
- kita dapat menggunakan konten utama untuk memberikan beberapa contoh keluaran yang diinginkan
- kita dapat menggunakan konten sekunder untuk mengidentifikasi 5 "tag" teratas yang menarik.

Kini, model dapat memberikan ringkasan dalam format yang ditunjukkan oleh beberapa contoh - tetapi jika suatu hasil memiliki banyak tag, model dapat memprioritaskan 5 tag yang diidentifikasi dalam konten sekunder.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #3:
Prompt Engineering Techniques.
What are some basic techniques for prompt engineering?
Illustrate it with some exercises.
-->

## Praktik Terbaik Prompting

Sekarang setelah kita tahu bagaimana prompt dapat _dibuat_, kita dapat mulai memikirkan bagaimana _merancang_ mereka agar sesuai dengan praktik terbaik. Kita dapat memikirkannya dalam dua bagian - memiliki _pola pikir_ yang tepat dan menerapkan _teknik_ yang benar.

### Pola Pikir Prompt Engineering

Prompt Engineering adalah proses coba-coba sehingga ingat tiga faktor panduan luas berikut:

1. **Pemahaman Domain Penting.** Akurasi dan relevansi respons adalah fungsi dari _domain_ tempat aplikasi atau pengguna itu berada. Terapkan intuisi dan keahlian domain Anda untuk **menyesuaikan teknik** lebih lanjut. Misalnya, definisikan _kepribadian khusus domain_ dalam prompt sistem Anda, atau gunakan _template khusus domain_ dalam prompt pengguna. Berikan konten sekunder yang mencerminkan konteks domain, atau gunakan _isyarat dan contoh khusus domain_ untuk mengarahkan model menuju pola penggunaan yang familiar.

2. **Pemahaman Model Penting.** Kita tahu model bersifat stokastik secara alami. Namun, implementasi model juga bisa berbeda berdasarkan dataset pelatihan yang digunakan (pengetahuan pra-latih), kemampuan yang disediakan (mis. melalui API atau SDK), dan jenis konten yang dioptimalkan (mis. kode vs gambar vs teks). Pahami kekuatan dan keterbatasan model yang Anda gunakan, dan gunakan pengetahuan itu untuk _memprioritaskan tugas_ atau membangun _template khusus_ yang dioptimalkan untuk kemampuan model tersebut.

3. **Iterasi & Validasi Penting.** Model berkembang cepat, begitu juga teknik prompt engineering. Sebagai ahli domain, Anda mungkin punya konteks atau kriteria khusus untuk _aplikasi_ Anda, yang mungkin tidak berlaku untuk komunitas luas. Gunakan alat & teknik prompt engineering untuk "memulai" konstruksi prompt, lalu iterasi dan validasi hasil menggunakan intuisi dan keahlian domain Anda. Rekam wawasan Anda dan buat **basis pengetahuan** (mis., perpustakaan prompt) yang dapat dipakai sebagai dasar baru oleh orang lain, mempercepat iterasi berikutnya.

## Praktik Terbaik

Sekarang mari kita lihat praktik terbaik umum yang direkomendasikan oleh praktisi [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) dan [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Apa                              | Mengapa                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evaluasi model terbaru.           | Generasi model baru kemungkinan memiliki fitur dan kualitas yang lebih baik - tapi mungkin juga memerlukan biaya lebih tinggi. Evaluasi dampaknya, lalu buat keputusan migrasi.                                                                     |
| Pisahkan instruksi & konteks     | Periksa apakah model/penyedia Anda mendefinisikan _delimiter_ untuk membedakan instruksi, konten utama dan konten sekunder dengan lebih jelas. Ini dapat membantu model memberikan bobot token dengan lebih akurat.                                   |
| Jadilah spesifik dan jelas        | Berikan lebih banyak detail tentang konteks, hasil, panjang, format, gaya yang diinginkan. Ini akan meningkatkan kualitas dan konsistensi respons. Simpan resep dalam template yang dapat digunakan ulang.                                            |
| Gunakan deskripsi dan contoh      | Model mungkin merespon lebih baik pada pendekatan "show and tell". Mulailah dengan pendekatan `zero-shot` dimana Anda memberi instruksi (tanpa contoh), lalu coba `few-shot` sebagai perbaikan, memberikan beberapa contoh keluaran. Gunakan analogi.     |
| Gunakan isyarat untuk memulai respon | Dorong model menuju hasil yang diinginkan dengan memberikan kata atau frasa pembuka yang bisa dipakai sebagai titik awal respons.                                                                                                                   |
| Ulangi jika perlu                 | Kadang Anda perlu mengulangi instruksi pada model. Beri instruksi sebelum dan sesudah konten utama, gunakan instruksi dan isyarat, dll. Iterasi & validasi untuk melihat apa yang berhasil.                                                             |
| Urutan Penting                   | Urutan penyajian informasi ke model dapat mempengaruhi keluaran, bahkan dalam contoh pembelajaran, berkat bias kebaruan. Cobalah opsi berbeda untuk melihat mana yang terbaik.                                                                        |
| Beri model “pilihan keluar”      | Beri model respons _fallback_ yang dapat diberikan jika model tidak dapat menyelesaikan tugas dengan alasan apapun. Ini mengurangi kemungkinan model menghasilkan respons palsu atau dibuat-buat.                                                    |
|                                 |                                                                                                                                                                                                                                                    |

Seperti semua praktik terbaik, ingat bahwa _hasil bisa berbeda-beda_ berdasarkan model, tugas, dan domain. Gunakan ini sebagai titik awal, dan iterasikan untuk menemukan apa yang terbaik untuk Anda. Selalu evaluasi ulang proses prompt engineering Anda saat model dan alat baru tersedia, dengan fokus pada skalabilitas proses dan kualitas respons.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Tugas

Selamat! Anda telah mencapai akhir pelajaran! Saatnya menguji beberapa konsep dan teknik tersebut dengan contoh nyata!

Untuk tugas ini, kita akan menggunakan Jupyter Notebook dengan latihan yang dapat Anda selesaikan secara interaktif. Anda juga dapat memperluas Notebook dengan sel Markdown dan Kode Anda sendiri untuk mengeksplorasi ide dan teknik secara mandiri.

### Untuk memulai, fork repo, lalu

- (Direkomendasikan) Jalankan GitHub Codespaces
- (Alternatif) Clone repo ke perangkat lokal Anda dan gunakan dengan Docker Desktop
- (Alternatif) Buka Notebook dengan lingkungan runtime Notebook pilihan Anda.

### Selanjutnya, konfigurasikan variabel lingkungan Anda

- Salin file `.env.copy` di root repo ke `.env` dan isi nilai `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` dan `AZURE_OPENAI_DEPLOYMENT`. Kembali ke [bagian Learning Sandbox](#sandbox-pembelajaran) untuk belajar caranya.

### Selanjutnya, buka Jupyter Notebook

- Pilih kernel runtime yang sesuai. Jika menggunakan opsi 1 atau 2, cukup pilih kernel Python 3.10.x default yang disediakan oleh container dev.

Anda siap menjalankan latihan. Perlu diingat bahwa tidak ada jawaban _benar dan salah_ di sini - hanya eksplorasi pilihan dengan coba-coba dan membangun intuisi tentang apa yang berhasil untuk model dan domain aplikasi tertentu.

_Untuk alasan ini tidak ada segmen Solusi Kode dalam pelajaran ini. Sebagai gantinya, Notebook akan memiliki sel Markdown berjudul "Solusi Saya:" yang menunjukkan satu contoh keluaran sebagai referensi._

 <!--
LESSON TEMPLATE:
Wrap the section with a summary and resources for self-guided learning.
-->

## Pemeriksaan Pengetahuan

Manakah prompt yang baik mengikuti beberapa praktik terbaik yang masuk akal?

1. Tunjukkan gambar mobil merah
2. Tunjukkan gambar mobil merah merk Volvo dan model XC90 diparkir di tepi tebing dengan matahari terbenam
3. Tunjukkan gambar mobil merah merk Volvo dan model XC90

A: 2, ini adalah prompt terbaik karena memberikan detail tentang "apa" dan masuk ke spesifik (bukan sembarang mobil tetapi merk dan model spesifik) dan juga mendeskripsikan latar keseluruhan. 3 adalah yang berikutnya terbaik karena juga mengandung banyak deskripsi.

## 🚀 Tantangan

Coba gunakan teknik "isyarat" dengan prompt: Lengkapi kalimat "Tunjukkan gambar mobil merah merk Volvo dan ". Apa yang model jawab, dan bagaimana Anda akan memperbaikinya?

## Kerja Bagus! Lanjutkan Pembelajaran Anda

Ingin belajar lebih banyak tentang berbagai konsep Prompt Engineering? Kunjungi [halaman pembelajaran lanjutan](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk menemukan sumber daya hebat lainnya tentang topik ini.

Lanjut ke Pelajaran 5 di mana kita akan membahas [teknik prompting lanjutan](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->