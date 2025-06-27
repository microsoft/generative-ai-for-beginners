<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T13:07:55+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "id"
}
-->
# Dasar-dasar Teknik Penyusunan Prompt

## Pendahuluan
Modul ini mencakup konsep dan teknik penting untuk membuat prompt yang efektif dalam model AI generatif. Cara Anda menulis prompt ke LLM juga penting. Sebuah prompt yang dirancang dengan hati-hati dapat menghasilkan kualitas respons yang lebih baik. Tetapi apa sebenarnya arti istilah seperti _prompt_ dan _teknik penyusunan prompt_? Dan bagaimana saya dapat meningkatkan _input_ prompt yang saya kirim ke LLM? Ini adalah pertanyaan yang akan kita coba jawab dalam bab ini dan bab berikutnya.

AI Generatif mampu membuat konten baru (misalnya, teks, gambar, audio, kode, dll.) sebagai respons terhadap permintaan pengguna. Hal ini dicapai dengan menggunakan _Model Bahasa Besar_ seperti seri GPT ("Generative Pre-trained Transformer") dari OpenAI yang dilatih untuk menggunakan bahasa alami dan kode.

Pengguna sekarang dapat berinteraksi dengan model-model ini menggunakan paradigma yang sudah dikenal seperti chat, tanpa memerlukan keahlian teknis atau pelatihan. Model-model ini berbasis _prompt_ - pengguna mengirimkan input teks (prompt) dan mendapatkan respons AI (penyelesaian). Mereka kemudian dapat "mengobrol dengan AI" secara iteratif, dalam percakapan multi-putaran, memperbaiki prompt mereka hingga responsnya sesuai dengan harapan mereka.

"Prompt" kini menjadi antarmuka _pemrograman_ utama untuk aplikasi AI generatif, memberi tahu model apa yang harus dilakukan dan mempengaruhi kualitas respons yang dikembalikan. "Teknik Penyusunan Prompt" adalah bidang studi yang berkembang pesat yang berfokus pada _desain dan optimasi_ prompt untuk memberikan respons yang konsisten dan berkualitas dalam skala besar.

## Tujuan Pembelajaran

Dalam pelajaran ini, kita akan mempelajari apa itu Teknik Penyusunan Prompt, mengapa penting, dan bagaimana kita dapat membuat prompt yang lebih efektif untuk model dan tujuan aplikasi tertentu. Kita akan memahami konsep inti dan praktik terbaik untuk teknik penyusunan prompt - dan belajar tentang lingkungan "sandbox" Jupyter Notebooks interaktif di mana kita dapat melihat konsep-konsep ini diterapkan pada contoh nyata.

Pada akhir pelajaran ini kita akan dapat:

1. Menjelaskan apa itu teknik penyusunan prompt dan mengapa itu penting.
2. Mendeskripsikan komponen dari sebuah prompt dan bagaimana mereka digunakan.
3. Mempelajari praktik terbaik dan teknik untuk teknik penyusunan prompt.
4. Menerapkan teknik yang dipelajari ke contoh nyata, menggunakan endpoint OpenAI.

## Istilah Kunci

Teknik Penyusunan Prompt: Praktik merancang dan menyempurnakan input untuk membimbing model AI menuju menghasilkan output yang diinginkan.
Tokenisasi: Proses mengubah teks menjadi unit yang lebih kecil, disebut token, yang dapat dipahami dan diproses oleh model.
LLM yang Disetel dengan Instruksi: Model Bahasa Besar (LLM) yang telah disesuaikan dengan instruksi spesifik untuk meningkatkan akurasi dan relevansi respons mereka.

## Sandbox Pembelajaran

Teknik penyusunan prompt saat ini lebih merupakan seni daripada ilmu. Cara terbaik untuk meningkatkan intuisi kita tentangnya adalah dengan _berlatih lebih banyak_ dan mengadopsi pendekatan trial-and-error yang menggabungkan keahlian domain aplikasi dengan teknik yang direkomendasikan dan optimasi model-spesifik.

Jupyter Notebook yang menyertai pelajaran ini menyediakan lingkungan _sandbox_ di mana Anda dapat mencoba apa yang Anda pelajari - seiring berjalannya waktu atau sebagai bagian dari tantangan kode di akhir. Untuk menjalankan latihan, Anda akan memerlukan:

1. **Kunci API Azure OpenAI** - endpoint layanan untuk LLM yang dideploy.
2. **Python Runtime** - di mana Notebook dapat dieksekusi.
3. **Variabel Lingkungan Lokal** - _selesaikan langkah-langkah [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) sekarang untuk bersiap_.

Notebook ini dilengkapi dengan latihan _pemula_ - tetapi Anda didorong untuk menambahkan bagian _Markdown_ (deskripsi) dan _Kode_ (permintaan prompt) Anda sendiri untuk mencoba lebih banyak contoh atau ide - dan membangun intuisi Anda untuk desain prompt.

## Panduan Bergambar

Ingin mendapatkan gambaran besar tentang apa yang dibahas dalam pelajaran ini sebelum Anda mendalami? Lihat panduan bergambar ini, yang memberi Anda gambaran tentang topik utama yang dibahas dan poin penting untuk Anda pikirkan dalam setiap topik. Peta jalan pelajaran membawa Anda dari memahami konsep inti dan tantangan hingga mengatasinya dengan teknik dan praktik terbaik penyusunan prompt yang relevan. Perhatikan bahwa bagian "Teknik Lanjutan" dalam panduan ini merujuk pada konten yang dibahas dalam bab _berikutnya_ dari kurikulum ini.

## Startup Kami

Sekarang, mari kita bahas bagaimana _topik ini_ berhubungan dengan misi startup kami untuk [membawa inovasi AI ke pendidikan](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Kami ingin membangun aplikasi pembelajaran _personalized_ berbasis AI - jadi mari kita pikirkan bagaimana pengguna yang berbeda dari aplikasi kami mungkin "merancang" prompt:

- **Administrator** mungkin meminta AI untuk _menganalisis data kurikulum untuk mengidentifikasi celah dalam cakupan_. AI dapat merangkum hasil atau memvisualisasikannya dengan kode.
- **Pendidik** mungkin meminta AI untuk _menghasilkan rencana pelajaran untuk audiens dan topik tertentu_. AI dapat membangun rencana yang dipersonalisasi dalam format yang ditentukan.
- **Siswa** mungkin meminta AI untuk _mengajar mereka dalam mata pelajaran yang sulit_. AI sekarang dapat membimbing siswa dengan pelajaran, petunjuk & contoh yang disesuaikan dengan tingkat mereka.

Itu hanya sebagian kecil dari kemungkinan. Lihat [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - perpustakaan prompt sumber terbuka yang dikurasi oleh para ahli pendidikan - untuk mendapatkan gambaran yang lebih luas tentang kemungkinan-kemungkinan tersebut! _Cobalah menjalankan beberapa prompt tersebut di sandbox atau menggunakan OpenAI Playground untuk melihat apa yang terjadi!_

## Apa itu Teknik Penyusunan Prompt?

Kami memulai pelajaran ini dengan mendefinisikan **Teknik Penyusunan Prompt** sebagai proses _merancang dan mengoptimalkan_ input teks (prompt) untuk memberikan respons yang konsisten dan berkualitas (penyelesaian) untuk tujuan aplikasi dan model tertentu. Kita dapat menganggap ini sebagai proses 2 langkah:

- _merancang_ prompt awal untuk model dan tujuan tertentu
- _menyempurnakan_ prompt secara iteratif untuk meningkatkan kualitas respons

Ini adalah proses trial-and-error yang memerlukan intuisi dan upaya pengguna untuk mendapatkan hasil yang optimal. Jadi mengapa ini penting? Untuk menjawab pertanyaan itu, kita pertama-tama perlu memahami tiga konsep:

- _Tokenisasi_ = bagaimana model "melihat" prompt
- _Base LLMs_ = bagaimana model dasar "memproses" sebuah prompt
- _Instruction-Tuned LLMs_ = bagaimana model sekarang dapat melihat "tugas"

### Tokenisasi

LLM melihat prompt sebagai _urutan token_ di mana model yang berbeda (atau versi model) dapat men-tokenisasi prompt yang sama dengan cara yang berbeda. Karena LLM dilatih pada token (dan bukan pada teks mentah), cara prompt ditokenisasi memiliki dampak langsung pada kualitas respons yang dihasilkan.

Untuk mendapatkan intuisi tentang bagaimana tokenisasi bekerja, coba alat seperti [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) yang ditunjukkan di bawah ini. Salin prompt Anda - dan lihat bagaimana itu dikonversi menjadi token, perhatikan bagaimana karakter spasi dan tanda baca ditangani. Perhatikan bahwa contoh ini menunjukkan LLM yang lebih lama (GPT-3) - jadi mencoba ini dengan model yang lebih baru mungkin menghasilkan hasil yang berbeda.

### Konsep: Model Dasar

Setelah sebuah prompt ditokenisasi, fungsi utama dari ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (atau model Dasar) adalah memprediksi token dalam urutan tersebut. Karena LLM dilatih pada kumpulan data teks yang besar, mereka memiliki pemahaman yang baik tentang hubungan statistik antara token dan dapat membuat prediksi tersebut dengan percaya diri. Perhatikan bahwa mereka tidak memahami _makna_ kata-kata dalam prompt atau token; mereka hanya melihat pola yang dapat mereka "lengkapi" dengan prediksi berikutnya. Mereka dapat terus memprediksi urutan tersebut hingga dihentikan oleh intervensi pengguna atau beberapa kondisi yang telah ditetapkan sebelumnya.

Ingin melihat bagaimana penyelesaian berbasis prompt bekerja? Masukkan prompt di atas ke dalam Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) dengan pengaturan default. Sistem ini dikonfigurasi untuk memperlakukan prompt sebagai permintaan informasi - jadi Anda seharusnya melihat penyelesaian yang memenuhi konteks ini.

Tetapi bagaimana jika pengguna ingin melihat sesuatu yang spesifik yang memenuhi beberapa kriteria atau tujuan tugas? Di sinilah LLM yang _disetel dengan instruksi_ berperan.

### Konsep: LLM yang Disetel dengan Instruksi

Sebuah [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) dimulai dengan model dasar dan menyetelnya dengan contoh atau pasangan input/output (misalnya, "pesan" multi-putaran) yang dapat berisi instruksi yang jelas - dan respons dari AI mencoba mengikuti instruksi tersebut.

Ini menggunakan teknik seperti Pembelajaran Penguatan dengan Umpan Balik Manusia (RLHF) yang dapat melatih model untuk _mengikuti instruksi_ dan _belajar dari umpan balik_ sehingga menghasilkan respons yang lebih sesuai untuk aplikasi praktis dan lebih relevan dengan tujuan pengguna.

Mari kita coba - kunjungi kembali prompt di atas, tetapi sekarang ubah _pesan sistem_ untuk memberikan instruksi berikut sebagai konteks:

> _Ringkas konten yang Anda berikan untuk siswa kelas dua. Jaga agar hasilnya dalam satu paragraf dengan 3-5 poin._

Lihat bagaimana hasilnya sekarang disetel untuk mencerminkan tujuan dan format yang diinginkan? Seorang pendidik sekarang dapat langsung menggunakan respons ini dalam slide mereka untuk kelas tersebut.

## Mengapa kita membutuhkan Teknik Penyusunan Prompt?

Sekarang kita tahu bagaimana prompt diproses oleh LLM, mari kita bicarakan _mengapa_ kita membutuhkan teknik penyusunan prompt. Jawabannya terletak pada fakta bahwa LLM saat ini menghadapi sejumlah tantangan yang membuat _penyelesaian yang andal dan konsisten_ lebih sulit dicapai tanpa upaya dalam konstruksi dan optimasi prompt. Misalnya:

1. **Respons model bersifat stokastik.** _Prompt yang sama_ kemungkinan akan menghasilkan respons yang berbeda dengan model atau versi model yang berbeda. Dan mungkin bahkan menghasilkan hasil yang berbeda dengan _model yang sama_ pada waktu yang berbeda. _Teknik penyusunan prompt dapat membantu kita meminimalkan variasi ini dengan memberikan batasan yang lebih baik_.

1. **Model dapat membuat respons.** Model dilatih dengan kumpulan data yang _besar tetapi terbatas_, yang berarti mereka tidak memiliki pengetahuan tentang konsep di luar cakupan pelatihan tersebut. Akibatnya, mereka dapat menghasilkan penyelesaian yang tidak akurat, imajiner, atau langsung bertentangan dengan fakta yang diketahui. _Teknik penyusunan prompt membantu pengguna mengidentifikasi dan mengurangi fabrikasi semacam itu misalnya, dengan meminta AI untuk referensi atau penalaran_.

1. **Kemampuan model akan bervariasi.** Model yang lebih baru atau generasi model yang lebih baru akan memiliki kemampuan yang lebih kaya tetapi juga membawa keunikan dan pertukaran dalam biaya & kompleksitas. _Teknik penyusunan prompt dapat membantu kita mengembangkan praktik terbaik dan alur kerja yang mengabstraksi perbedaan dan beradaptasi dengan persyaratan spesifik model dengan cara yang dapat diskalakan dan mulus_.

Mari kita lihat ini dalam aksi di OpenAI atau Azure OpenAI Playground:

- Gunakan prompt yang sama dengan berbagai penyebaran LLM (misalnya, OpenAI, Azure OpenAI, Hugging Face) - apakah Anda melihat variasinya?
- Gunakan prompt yang sama berulang kali dengan penyebaran LLM yang _sama_ (misalnya, playground Azure OpenAI) - bagaimana variasi ini berbeda?

### Contoh Fabrikasi

Dalam kursus ini, kami menggunakan istilah **"fabrikasi"** untuk merujuk pada fenomena di mana LLM kadang-kadang menghasilkan informasi yang tidak benar secara faktual karena keterbatasan dalam pelatihan mereka atau kendala lainnya. Anda mungkin juga pernah mendengar ini disebut sebagai _"halusinasi"_ dalam artikel populer atau makalah penelitian. Namun, kami sangat merekomendasikan menggunakan istilah _"fabrikasi"_ sehingga kami tidak secara tidak sengaja memberikan sifat seperti manusia pada hasil yang didorong oleh mesin. Ini juga memperkuat [pedoman AI yang Bertanggung Jawab](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) dari perspektif terminologi, menghilangkan istilah yang juga dapat dianggap ofensif atau tidak inklusif dalam beberapa konteks.

Ingin mendapatkan gambaran tentang bagaimana fabrikasi bekerja? Pikirkan sebuah prompt yang menginstruksikan AI untuk menghasilkan konten untuk topik yang tidak ada (untuk memastikan itu tidak ditemukan dalam kumpulan data pelatihan). Misalnya - saya mencoba prompt ini:

> **Prompt:** buat rencana pelajaran tentang Perang Mars tahun 2076.

Pencarian web menunjukkan kepada saya bahwa ada akun fiksi (misalnya, serial televisi atau buku) tentang perang Mars - tetapi tidak ada yang terjadi pada tahun 2076. Akal sehat juga memberi tahu kita bahwa 2076 adalah _masa depan_ dan dengan demikian, tidak dapat dikaitkan dengan peristiwa nyata.

Jadi, apa yang terjadi ketika kita menjalankan prompt ini dengan penyedia LLM yang berbeda?

> **Respons 1**: OpenAI Playground (GPT-35)

> **Respons 2**: Azure OpenAI Playground (GPT-35)

> **Respons 3**: : Hugging Face Chat Playground (LLama-2)

Seperti yang diharapkan, setiap model (atau versi model) menghasilkan respons yang sedikit berbeda berkat perilaku stokastik dan variasi kemampuan model. Misalnya, satu model menargetkan audiens kelas 8 sementara yang lain menganggap siswa sekolah menengah. Namun ketiga model tersebut menghasilkan respons yang dapat meyakinkan pengguna yang tidak terinformasi bahwa peristiwa tersebut nyata.

Teknik penyusunan prompt seperti _metaprompting_ dan _konfigurasi suhu_ dapat mengurangi fabrikasi model hingga batas tertentu. Arsitektur _baru_ teknik penyusunan prompt juga menggabungkan alat dan teknik baru dengan mulus ke dalam aliran prompt, untuk mengurangi atau mengurangi beberapa efek ini.

## Studi Kasus: GitHub Copilot

Mari kita akhiri bagian ini dengan mendapatkan gambaran tentang bagaimana teknik penyusunan prompt digunakan dalam solusi dunia nyata dengan melihat satu Studi Kasus: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot adalah "Programmer Pasangan AI" Anda - ia mengubah prompt teks menjadi penyelesaian kode dan terintegrasi ke dalam lingkungan pengembangan Anda (misalnya, Visual Studio Code) untuk pengalaman pengguna yang mulus. Seperti yang didokumentasikan dalam rangkaian blog di bawah ini, versi paling awal didasarkan pada model OpenAI Codex - dengan insinyur yang dengan cepat menyadari perlunya menyetel model dan mengembangkan teknik penyusunan prompt yang lebih baik, untuk meningkatkan kualitas kode. Pada bulan Juli, mereka [meluncurkan model AI yang lebih baik yang melampaui Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) untuk saran yang lebih cepat.

Baca postingan dalam urutan, untuk mengikuti perjalanan pembelajaran mereka.

Anda juga dapat menjelajahi [blog Teknik](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) mereka untuk postingan lebih lanjut seperti [yang satu ini](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) yang menunjukkan bagaimana model dan teknik ini _diterapkan_ untuk mendorong aplikasi dunia nyata.

## Konstruksi Prompt

Kita telah melihat mengapa teknik penyusunan prompt penting - sekarang mari kita pahami bagaimana prompt _dibangun_ sehingga kita dapat mengevaluasi berbagai teknik untuk desain prompt yang lebih efektif.

### Prompt Dasar

Mari kita mulai dengan prompt dasar: input teks yang dikirimkan ke model tanpa konteks lain. Berikut adalah contoh - ketika kita mengirim beberapa kata pertama dari lagu kebangsaan AS ke [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) OpenAI, itu langsung _melengkapi_ respons dengan beberapa baris berikutnya, menggambarkan perilaku prediksi dasar.

| Prompt (Input)     | Penyelesaian (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Tampaknya Anda memulai lirik "The Star-Spangled Banner," lagu kebangsaan Amerika Serikat. Lirik lengkapnya adalah ... |

### Prompt Kompleks

Sekarang mari kita tambahkan konteks dan instruksi ke prompt dasar tersebut. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) memungkinkan kita membangun prompt kompleks sebagai kumpulan _pesan_ dengan:

- Pasangan input/output yang mencerminkan _input pengguna_ dan _respons asisten_.
- Pesan sistem yang menetapkan konteks untuk perilaku atau kepribadian asisten.

Permintaan sekarang dalam bentuk di bawah ini, di mana _tokenisasi_ secara efektif menangkap informasi relevan dari konteks dan percakapan. Sekarang, mengubah konteks sistem dapat berdampak besar pada kualitas penyelesaian, seperti input pengguna yang diberikan.

### Prompt Instruksi

Dalam contoh di atas, prompt pengguna adalah permintaan informasi sederhana yang dapat diartikan sebagai permintaan informasi. Dengan prompt _instruksi_, kita dapat menggunakan teks tersebut untuk menentukan tugas dengan lebih rinci, memberikan panduan yang lebih baik kepada
Akhirnya, nilai sebenarnya dari template terletak pada kemampuan untuk membuat dan menerbitkan _perpustakaan prompt_ untuk domain aplikasi vertikal - di mana template prompt kini dioptimalkan untuk mencerminkan konteks atau contoh spesifik aplikasi yang membuat respons lebih relevan dan akurat untuk audiens pengguna yang ditargetkan. Repositori [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) adalah contoh bagus dari pendekatan ini, yang mengkurasi perpustakaan prompt untuk domain pendidikan dengan penekanan pada tujuan utama seperti perencanaan pelajaran, desain kurikulum, bimbingan siswa, dll.

## Konten Pendukung

Jika kita berpikir tentang konstruksi prompt sebagai memiliki instruksi (tugas) dan target (konten utama), maka _konten sekunder_ adalah seperti konteks tambahan yang kita berikan untuk **mempengaruhi keluaran dengan cara tertentu**. Ini bisa berupa parameter penyesuaian, instruksi format, taksonomi topik, dll. yang dapat membantu model _menyesuaikan_ responsnya agar sesuai dengan tujuan atau harapan pengguna yang diinginkan.

Sebagai contoh: Diberikan katalog kursus dengan metadata yang luas (nama, deskripsi, tingkat, tag metadata, instruktur, dll.) pada semua kursus yang tersedia dalam kurikulum:

- kita bisa menentukan instruksi untuk "merangkum katalog kursus untuk Musim Gugur 2023"
- kita bisa menggunakan konten utama untuk memberikan beberapa contoh keluaran yang diinginkan
- kita bisa menggunakan konten sekunder untuk mengidentifikasi 5 "tag" teratas yang menarik.

Sekarang, model dapat memberikan ringkasan dalam format yang ditunjukkan oleh beberapa contoh - tetapi jika hasil memiliki beberapa tag, ia dapat memprioritaskan 5 tag yang diidentifikasi dalam konten sekunder.

---

## Praktik Terbaik dalam Prompting

Sekarang kita tahu bagaimana prompt dapat dikonstruksi, kita bisa mulai memikirkan bagaimana mendesainnya untuk mencerminkan praktik terbaik. Kita bisa memikirkan ini dalam dua bagian - memiliki _pola pikir_ yang tepat dan menerapkan _teknik_ yang tepat.

### Pola Pikir Rekayasa Prompt

Rekayasa Prompt adalah proses coba-coba, jadi ingat tiga faktor panduan yang luas:

1. **Pemahaman Domain Penting.** Akurasi dan relevansi respons adalah fungsi dari _domain_ di mana aplikasi atau pengguna tersebut beroperasi. Terapkan intuisi dan keahlian domain Anda untuk **menyesuaikan teknik** lebih lanjut. Misalnya, definisikan _kepribadian spesifik domain_ dalam prompt sistem Anda, atau gunakan _template spesifik domain_ dalam prompt pengguna Anda. Berikan konten sekunder yang mencerminkan konteks spesifik domain, atau gunakan _petunjuk dan contoh spesifik domain_ untuk membimbing model menuju pola penggunaan yang dikenal.

2. **Pemahaman Model Penting.** Kita tahu model bersifat stokastik secara alami. Tetapi implementasi model juga dapat bervariasi dalam hal dataset pelatihan yang mereka gunakan (pengetahuan yang telah dilatih), kemampuan yang mereka berikan (misalnya, melalui API atau SDK) dan jenis konten yang mereka optimalkan (misalnya, kode vs. gambar vs. teks). Pahami kekuatan dan keterbatasan model yang Anda gunakan, dan gunakan pengetahuan itu untuk _memprioritaskan tugas_ atau membangun _template khusus_ yang dioptimalkan untuk kemampuan model.

3. **Iterasi & Validasi Penting.** Model berkembang dengan cepat, begitu pula teknik untuk rekayasa prompt. Sebagai ahli domain, Anda mungkin memiliki konteks atau kriteria lain untuk aplikasi spesifik Anda, yang mungkin tidak berlaku untuk komunitas yang lebih luas. Gunakan alat & teknik rekayasa prompt untuk "memulai" konstruksi prompt, kemudian iterasi dan validasi hasil menggunakan intuisi dan keahlian domain Anda sendiri. Catat wawasan Anda dan buat **basis pengetahuan** (misalnya, perpustakaan prompt) yang dapat digunakan sebagai dasar baru oleh orang lain, untuk iterasi yang lebih cepat di masa depan.

## Praktik Terbaik

Sekarang mari kita lihat praktik terbaik umum yang direkomendasikan oleh praktisi [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) dan [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Apa                               | Mengapa                                                                                                                                                                                                                                               |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evaluasi model terbaru.           | Generasi model baru kemungkinan memiliki fitur dan kualitas yang lebih baik - tetapi mungkin juga menimbulkan biaya yang lebih tinggi. Evaluasi mereka untuk dampak, kemudian buat keputusan migrasi.                                                   |
| Pisahkan instruksi & konteks      | Periksa apakah model/penyedia Anda mendefinisikan _pembatas_ untuk membedakan instruksi, konten utama, dan konten sekunder dengan lebih jelas. Ini dapat membantu model menugaskan bobot lebih akurat ke token.                                      |
| Bersikap spesifik dan jelas       | Berikan lebih banyak detail tentang konteks yang diinginkan, hasil, panjang, format, gaya, dll. Ini akan meningkatkan kualitas dan konsistensi respons. Tangkap resep dalam template yang dapat digunakan kembali.                                    |
| Bersifat deskriptif, gunakan contoh | Model mungkin merespons lebih baik dengan pendekatan "show and tell". Mulailah dengan `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` nilai. Kembali ke [bagian Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) untuk belajar bagaimana.

### Selanjutnya, buka Jupyter Notebook

- Pilih kernel runtime. Jika menggunakan opsi 1 atau 2, cukup pilih kernel Python 3.10.x default yang disediakan oleh dev container.

Anda siap menjalankan latihan. Perhatikan bahwa tidak ada jawaban _benar dan salah_ di sini - hanya menjelajahi opsi melalui coba-coba dan membangun intuisi untuk apa yang bekerja untuk model dan domain aplikasi tertentu.

_Oleh karena itu tidak ada segmen Solusi Kode dalam pelajaran ini. Sebagai gantinya, Notebook akan memiliki sel Markdown berjudul "My Solution:" yang menunjukkan satu contoh keluaran untuk referensi._

## Pemeriksaan Pengetahuan

Mana dari berikut ini adalah prompt yang baik mengikuti beberapa praktik terbaik yang masuk akal?

1. Tunjukkan padaku gambar mobil merah
2. Tunjukkan padaku gambar mobil merah merek Volvo dan model XC90 diparkir di tepi tebing dengan matahari terbenam
3. Tunjukkan padaku gambar mobil merah merek Volvo dan model XC90

A: 2, itu adalah prompt terbaik karena memberikan detail tentang "apa" dan masuk ke spesifik (bukan hanya mobil mana saja tetapi merek dan model tertentu) dan juga menggambarkan pengaturan keseluruhan. 3 adalah yang terbaik berikutnya karena juga berisi banyak deskripsi.

## 🚀 Tantangan

Lihat apakah Anda bisa memanfaatkan teknik "cue" dengan prompt: Selesaikan kalimat "Tunjukkan padaku gambar mobil merah merek Volvo dan ". Apa yang direspons, dan bagaimana Anda akan memperbaikinya?

## Kerja Bagus! Lanjutkan Pembelajaran Anda

Ingin belajar lebih banyak tentang konsep Rekayasa Prompt yang berbeda? Kunjungi [halaman pembelajaran lanjutan](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk menemukan sumber daya hebat lainnya tentang topik ini.

Pergi ke Pelajaran 5 di mana kita akan melihat [teknik prompting lanjutan](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap disadari bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.