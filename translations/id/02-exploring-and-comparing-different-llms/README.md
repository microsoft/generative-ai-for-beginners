# Menjelajahi dan membandingkan berbagai LLM

[![Menjelajahi dan membandingkan berbagai LLM](../../../translated_images/id/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Klik gambar di atas untuk menonton video pelajaran ini_

Dengan pelajaran sebelumnya, kita telah melihat bagaimana Generative AI mengubah lanskap teknologi, bagaimana Large Language Models (LLM) bekerja dan bagaimana sebuah bisnis - seperti startup kita - dapat menerapkannya pada kasus penggunaan mereka dan berkembang! Dalam bab ini, kita akan membandingkan dan membedakan berbagai jenis large language models (LLM) untuk memahami kelebihan dan kekurangannya.

Langkah selanjutnya dalam perjalanan startup kita adalah menjelajahi lanskap LLM saat ini dan memahami mana yang cocok untuk kasus penggunaan kita.

## Pendahuluan

Pelajaran ini akan membahas:

- Berbagai jenis LLM dalam lanskap saat ini.
- Menguji, mengiterasi, dan membandingkan model berbeda untuk kasus penggunaan Anda di Azure.
- Cara menerapkan sebuah LLM.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan mampu:

- Memilih model yang tepat untuk kasus penggunaan Anda.
- Memahami cara menguji, mengiterasi, dan meningkatkan performa model Anda.
- Mengetahui bagaimana bisnis menerapkan model.

## Memahami berbagai jenis LLM

LLM dapat memiliki beberapa kategori berdasarkan arsitektur, data pelatihan, dan kasus penggunaan mereka. Memahami perbedaan ini akan membantu startup kita memilih model yang tepat untuk situasi tersebut, dan memahami bagaimana menguji, mengiterasi, dan meningkatkan performa.

Ada banyak jenis model LLM yang berbeda, pilihan model Anda tergantung pada apa yang Anda tuju untuk menggunakannya, data Anda, berapa banyak Anda siap membayar, dan lainnya.

Tergantung apakah Anda ingin menggunakan model untuk teks, audio, video, generasi gambar, dan sebagainya, Anda mungkin memilih tipe model yang berbeda.

- **Pengakuan audio dan suara**. Model gaya Whisper masih berguna sebagai model pengenal suara tujuan umum, tapi pilihan produksi sekarang juga mencakup model suara-ke-teks terbaru seperti `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, dan varian diarization. Evaluasi cakupan bahasa, diarization, dukungan waktu nyata, latensi, dan biaya untuk skenario Anda. Pelajari lebih lanjut di [dokumentasi OpenAI speech-to-text](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Generasi gambar**. DALL-E dan Midjourney adalah opsi generasi gambar yang terkenal, tapi API gambar OpenAI saat ini berfokus pada model GPT Image seperti `gpt-image-2`, sementara Stable Diffusion, Imagen, Flux, dan keluarga model lainnya juga merupakan pilihan umum. Bandingkan kepatuhan terhadap perintah, dukungan penyuntingan, kontrol gaya, persyaratan keamanan, dan lisensi. Pelajari lebih lanjut di [panduan generasi gambar OpenAI](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) dan Bab 9 dari kurikulum ini.

- **Generasi teks**. Model teks kini mencakup model frontier, model penalaran, model kecil berlatensi rendah, dan model open-weight. Contoh saat ini termasuk model OpenAI GPT-5.x, model Anthropic Claude 4.x, model Google Gemini 3.x, model Meta Llama 4, dan model Mistral. Jangan memilih hanya berdasarkan tanggal rilis atau harga; bandingkan kualitas tugas, latensi, jendela konteks, penggunaan alat, perilaku keamanan, ketersediaan regional, dan biaya total. [Katalog model Microsoft Foundry](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) adalah tempat yang baik untuk membandingkan model yang tersedia di Azure.

- **Multi-modalitas**. Banyak model saat ini dapat memproses lebih dari teks. Beberapa menerima input gambar, audio, atau video; beberapa dapat memanggil alat; dan model khusus dapat menghasilkan gambar, audio, atau video. Misalnya, model OpenAI saat ini mendukung input teks dan gambar, model Gemini dapat mendukung input teks, kode, gambar, audio, dan video tergantung varian, dan Llama 4 Scout serta Maverick adalah model open-weight natively multimodal. Selalu periksa kartu model masing-masing untuk modalitas input dan output yang didukung sebelum membangun alur kerja di sekitarnya.

Memilih model berarti Anda mendapatkan beberapa kemampuan dasar, yang mungkin tidak cukup. Seringkali Anda memiliki data spesifik perusahaan yang harus Anda sampaikan ke LLM. Ada beberapa cara berbeda untuk mendekati hal tersebut, akan dibahas lebih lanjut di bagian berikutnya.

### Foundation Models versus LLMs

Istilah Foundation Model [dicetuskan oleh peneliti Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) dan didefinisikan sebagai model AI yang memenuhi beberapa kriteria, seperti:

- **Dilatih menggunakan pembelajaran tanpa pengawasan atau pembelajaran mandiri (self-supervised)**, artinya mereka dilatih pada data multi-modal tanpa label, dan tidak memerlukan anotasi atau pelabelan manusia untuk proses pelatihannya.
- **Mereka adalah model yang sangat besar**, berdasarkan jaringan saraf yang sangat dalam yang dilatih pada miliaran parameter.
- **Umumnya ditujukan untuk menjadi ‘fondasi’ bagi model lain**, artinya mereka bisa digunakan sebagai titik awal bagi model lain yang dibangun di atasnya, yang dapat dilakukan dengan fine-tuning.

![Foundation Models versus LLMs](../../../translated_images/id/FoundationModel.e4859dbb7a825c94.webp)

Sumber gambar: [Panduan Esensial untuk Foundation Models dan Large Language Models | oleh Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Untuk memperjelas perbedaan ini, mari ambil ChatGPT sebagai contoh historis. Versi awal ChatGPT menggunakan GPT-3.5 sebagai foundation model. OpenAI kemudian menggunakan data khusus chat dan teknik alignment untuk membuat versi yang disesuaikan yang performanya lebih baik dalam skenario percakapan, seperti chatbot. Layanan AI modern sering mengalihkan antara beberapa varian model, sehingga nama layanan dan nama model yang mendasari tidak selalu sama.

![Foundation Model](../../../translated_images/id/Multimodal.2c389c6439e0fc51.webp)

Sumber gambar: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Open-Weight/Open-Source versus Proprietary Models

Cara lain untuk mengkategorikan LLM adalah apakah mereka open-weight, open-source, atau proprietary.

Model open-source dan open-weight membuat artefak model tersedia untuk inspeksi, unduhan, atau kustomisasi, tetapi lisensinya berbeda-beda. Beberapa sepenuhnya open source, sementara lainnya adalah model open-weight dengan pembatasan penggunaan. Mereka berguna ketika sebuah bisnis membutuhkan kontrol lebih terhadap penerapan, lokasi data, biaya, atau kustomisasi. Namun, tim masih perlu meninjau ketentuan lisensi, biaya penyajian, pemeliharaan, pembaruan keamanan, dan kualitas evaluasi sebelum menggunakannya dalam produksi. Contohnya termasuk [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), beberapa [model Mistral](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst), dan banyak model yang dihosting di [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Model proprietary dimiliki dan dihosting oleh penyedia. Model ini sering dioptimalkan untuk penggunaan produksi terkelola dan dapat menawarkan dukungan kuat, sistem keamanan, integrasi alat, dan skala. Namun, pelanggan biasanya tidak dapat memeriksa atau mengubah bobot model, dan mereka harus meninjau ketentuan penyedia tentang privasi, retensi, kepatuhan, dan penggunaan yang dapat diterima. Contohnya termasuk [model OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst), dan [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Embedding versus generasi Gambar versus Generasi Teks dan Kode

LLM juga dapat dikategorikan berdasarkan output yang mereka hasilkan.

Embedding adalah sekumpulan model yang dapat mengubah teks menjadi bentuk numerik, disebut embedding, yang merupakan representasi numerik dari teks input. Embedding memudahkan mesin memahami hubungan antara kata atau kalimat dan dapat digunakan sebagai input oleh model lain, seperti model klasifikasi, atau model klaster yang memiliki performa lebih baik pada data numerik. Model embedding sering digunakan untuk transfer learning, di mana sebuah model dibuat untuk tugas pengganti yang memiliki banyak data, dan bobot model (embedding) digunakan kembali untuk tugas hilir lainnya. Contoh kategori ini adalah [embedding OpenAI](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/id/Embedding.c3708fe988ccf760.webp)

Model generasi gambar adalah model yang menghasilkan gambar. Model ini sering digunakan untuk penyuntingan gambar, sintesis gambar, dan terjemahan gambar. Model generasi gambar biasanya dilatih pada dataset besar gambar, seperti [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), dan dapat digunakan untuk menghasilkan gambar baru atau menyunting gambar yang ada dengan teknik inpainting, super-resolution, dan kolorisasi. Contohnya termasuk [model GPT Image](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [model Stable Diffusion](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst), dan model Imagen.

![Generasi gambar](../../../translated_images/id/Image.349c080266a763fd.webp)

Model generasi teks dan kode adalah model yang menghasilkan teks atau kode. Model ini sering digunakan untuk ringkasan teks, terjemahan, dan menjawab pertanyaan. Model generasi teks biasanya dilatih pada dataset besar teks, seperti [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), dan dapat digunakan untuk menghasilkan teks baru atau menjawab pertanyaan. Model generasi kode, seperti [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), biasanya dilatih pada dataset besar kode, seperti GitHub, dan dapat digunakan untuk menghasilkan kode baru atau memperbaiki bug dalam kode yang ada.

![Generasi teks dan kode](../../../translated_images/id/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder versus Decoder-only

Untuk membicarakan berbagai jenis arsitektur LLM, mari gunakan analogi.

Bayangkan manajer Anda memberi tugas untuk membuat kuis untuk murid-murid. Anda memiliki dua rekan; satu mengawasi pembuatan konten dan yang lain mengawasi peninjauan konten tersebut.

Pembuat konten seperti model decoder-only: mereka dapat melihat topik, melihat apa yang sudah Anda tulis, lalu melanjutkan menghasilkan konten berdasarkan konteks itu. Mereka sangat baik dalam menulis konten yang menarik dan informatif, tetapi tidak selalu menjadi pilihan terbaik ketika tugasnya hanya mengklasifikasi, mengambil, atau mengenkode informasi. Contoh keluarga model decoder-only termasuk GPT dan model Llama.

Peninjau seperti model Encoder only, mereka melihat kursus yang ditulis dan jawabannya, memperhatikan hubungan antar keduanya dan memahami konteks, tetapi mereka tidak baik dalam menghasilkan konten. Contoh model Encoder only adalah BERT.

Bayangkan kita juga punya seseorang yang dapat membuat dan meninjau kuis, ini adalah model Encoder-Decoder. Contohnya adalah BART dan T5.

### Service versus Model

Sekarang, mari kita bicarakan perbedaan antara layanan dan model. Layanan adalah produk yang ditawarkan oleh Penyedia Layanan Cloud, dan sering merupakan kombinasi dari model, data, dan komponen lainnya. Model adalah komponen inti dari layanan, dan biasanya merupakan foundation model, seperti LLM.

Layanan sering dioptimalkan untuk penggunaan produksi dan seringkali lebih mudah digunakan daripada model, melalui antarmuka pengguna grafis. Namun, layanan tidak selalu tersedia gratis, dan mungkin memerlukan langganan atau pembayaran untuk digunakan, sebagai imbalan untuk memanfaatkan peralatan dan sumber daya pemilik layanan, mengoptimalkan pengeluaran dan skala dengan mudah. Contoh layanan adalah [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-foundry/openai/overview?WT.mc_id=academic-105485-koreyst), yang menawarkan rencana tarif bayar sesuai penggunaan, artinya pengguna dikenakan biaya proporsional dengan seberapa banyak mereka menggunakan layanan. Azure OpenAI Service juga menawarkan keamanan tingkat perusahaan dan kerangka AI yang bertanggung jawab di atas kemampuan model.

Model adalah artefak jaringan neural: parameter, bobot, arsitektur, tokenizer, dan konfigurasi pendukungnya. Menjalankan model secara lokal atau di lingkungan privat memerlukan perangkat keras yang cocok, infrastruktur penyajian, pemantauan, dan lisensi open-source/open-weight yang kompatibel atau lisensi komersial. Model open-weight seperti Llama 4 atau model Mistral dapat dihosting sendiri, tetapi mereka tetap memerlukan daya komputasi dan keahlian operasional.

## Cara menguji dan mengiterasi dengan model berbeda untuk memahami performa di Azure


Setelah tim kami menjelajahi lanskap LLM saat ini dan mengidentifikasi beberapa kandidat yang baik untuk skenario mereka, langkah selanjutnya adalah mengujinya pada data mereka dan pada beban kerja mereka. Ini adalah proses iteratif, dilakukan melalui eksperimen dan pengukuran.
Sebagian besar model yang kami sebutkan di paragraf sebelumnya (model OpenAI, model open-weight seperti Llama 4 dan Mistral, dan model Hugging Face) tersedia di [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), sebelumnya Azure AI Studio/Azure AI Foundry, adalah platform Azure terpadu untuk membangun aplikasi dan agen AI. Ini membantu pengembang mengelola siklus hidup mulai dari eksperimen dan evaluasi hingga penerapan, pemantauan, dan tata kelola. Katalog model di Microsoft Foundry memungkinkan pengguna untuk:

- Menemukan model dasar yang diminati dalam katalog, termasuk model yang dijual oleh Azure dan model dari mitra serta penyedia komunitas. Pengguna dapat memfilter berdasarkan tugas, penyedia, lisensi, opsi penerapan, atau nama.

![Model catalog](../../../translated_images/id/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Meninjau kartu model, termasuk deskripsi rinci tentang penggunaan yang dimaksudkan dan data pelatihan, contoh kode, serta hasil evaluasi pada perpustakaan evaluasi internal.

![Model card](../../../translated_images/id/ModelCard.598051692c6e400d.webp)

- Membandingkan tolok ukur di antara model dan dataset yang tersedia di industri untuk menilai mana yang memenuhi skenario bisnis, melalui panel [Model Benchmarks](https://learn.microsoft.com/azure/ai-foundry/concepts/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Model benchmarks](../../../translated_images/id/ModelBenchmarks.254cb20fbd06c03a.webp)

- Melakukan fine-tune pada model yang didukung dengan data pelatihan kustom untuk meningkatkan kinerja model pada beban kerja tertentu, memanfaatkan kemampuan eksperimen dan pelacakan Microsoft Foundry.

![Model fine-tuning](../../../translated_images/id/FineTuning.aac48f07142e36fd.webp)

- Menerapkan model pre-trained asli atau versi yang telah di-fine-tune ke endpoint inferensi real-time jarak jauh, menggunakan opsi komputasi terkelola atau penerapan tanpa server, agar aplikasi dapat mengonsumsinya.

![Model deployment](../../../translated_images/id/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Tidak semua model dalam katalog saat ini tersedia untuk fine-tuning dan/atau penerapan pay-as-you-go. Periksa kartu model untuk detail tentang kemampuan dan keterbatasan model.

## Meningkatkan hasil LLM

Kami telah menjelajahi dengan tim startup kami berbagai jenis LLM dan sebuah platform cloud (Microsoft Foundry) yang memungkinkan kami membandingkan berbagai model, mengevaluasi mereka dengan data uji, meningkatkan kinerja, dan menerapkannya pada endpoint inferensi.

Tetapi kapan mereka harus mempertimbangkan fine-tuning model dibanding menggunakan model yang sudah dilatih sebelumnya? Apakah ada pendekatan lain untuk meningkatkan kinerja model pada beban kerja tertentu?

Ada beberapa pendekatan yang dapat digunakan bisnis untuk mendapatkan hasil yang mereka butuhkan dari sebuah LLM. Anda dapat memilih berbagai jenis model dengan tingkat pelatihan yang berbeda saat menerapkan LLM di produksi, dengan tingkat kompleksitas, biaya, dan kualitas yang berbeda. Berikut beberapa pendekatan berbeda:

- **Prompt engineering dengan konteks**. Idenya adalah menyediakan konteks yang cukup saat Anda mem-prompt agar Anda mendapatkan respons yang Anda butuhkan.

- **Retrieval Augmented Generation, RAG**. Data Anda mungkin ada di database atau endpoint web misalnya, untuk memastikan data ini, atau subsetnya, termasuk pada saat melakukan prompt, Anda dapat mengambil data relevan tersebut dan menjadikannya bagian dari prompt pengguna.

- **Model yang di-fine-tune**. Di sini, Anda melatih model lebih lanjut dengan data Anda sendiri yang membuat model menjadi lebih tepat dan responsif terhadap kebutuhan Anda, namun mungkin biayanya tinggi.

![LLMs deployment](../../../translated_images/id/Deploy.18b2d27412ec8c02.webp)

Sumber gambar: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt Engineering dengan Konteks

LLM yang sudah dilatih sebelumnya bekerja sangat baik pada tugas bahasa alami yang digeneralisasi, bahkan dengan hanya memanggilnya dengan prompt singkat, seperti sebuah kalimat untuk dilengkapi atau sebuah pertanyaan – yang disebut pembelajaran “zero-shot”.

Namun, semakin pengguna bisa membingkai pertanyaan mereka, dengan permintaan rinci dan contoh – Konteks – maka jawaban akan semakin akurat dan sesuai dengan harapan pengguna. Dalam kasus ini, disebut pembelajaran “one-shot” jika prompt hanya mencakup satu contoh dan “few shot learning” jika mencakup beberapa contoh.
Prompt engineering dengan konteks adalah pendekatan yang paling hemat biaya untuk memulai.

### Retrieval Augmented Generation (RAG)

LLM memiliki keterbatasan bahwa mereka hanya dapat menggunakan data yang telah dipakai selama proses pelatihannya untuk menghasilkan jawaban. Ini berarti mereka tidak tahu apa pun tentang fakta yang terjadi setelah proses pelatihan, dan mereka tidak dapat mengakses informasi non-publik (seperti data perusahaan).
Ini dapat diatasi melalui RAG, teknik yang menambah prompt dengan data eksternal dalam bentuk potongan dokumen, dengan memperhatikan batas panjang prompt. Ini didukung oleh alat database vektor (seperti [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) yang mengambil potongan yang berguna dari berbagai sumber data yang telah ditentukan dan menambahkannya ke Konteks prompt.

Teknik ini sangat membantu saat sebuah bisnis tidak memiliki cukup data, waktu, atau sumber daya untuk melakukan fine-tune pada LLM, tapi masih ingin meningkatkan kinerja pada beban kerja tertentu dan mengurangi risiko jawaban yang halusinasi, ketinggalan zaman, atau tidak didukung.

### Model yang di-fine-tune

Fine-tuning adalah proses yang memanfaatkan transfer learning untuk ‘mengadaptasi’ model ke tugas hilir atau untuk memecahkan masalah tertentu. Berbeda dengan few-shot learning dan RAG, ini menghasilkan model baru yang dibuat, dengan bobot dan bias yang diperbarui. Ini memerlukan satu set contoh pelatihan yang terdiri dari input tunggal (prompt) dan output terkaitnya (penyelesaian).
Ini adalah pendekatan yang disukai jika:

- **Menggunakan model spesifik tugas yang lebih kecil**. Bisnis ingin melakukan fine-tune pada model kecil untuk tugas sempit daripada berulang kali mem-prompt model frontier yang lebih besar, menghasilkan solusi yang lebih hemat biaya dan lebih cepat.

- **Mempertimbangkan latensi**. Latensi penting untuk kasus penggunaan tertentu, sehingga tidak mungkin menggunakan prompt yang sangat panjang atau jumlah contoh yang harus dipelajari model tidak cocok dengan batas panjang prompt.

- **Mengadaptasi perilaku stabil**. Bisnis memiliki banyak contoh berkualitas tinggi dan ingin model secara konsisten mengikuti pola tugas, format keluaran, nada, atau gaya domain-spesifik. Jika masalah utama adalah fakta terkini atau pengetahuan pribadi yang sering berubah, gunakan RAG alih-alih hanya mengandalkan fine-tuning.

### Model yang dilatih

Melatih LLM dari awal tanpa diragukan lagi adalah pendekatan yang paling sulit dan paling kompleks untuk diterapkan, memerlukan jumlah data yang sangat besar, sumber daya yang terampil, dan kekuatan komputasi yang sesuai. Opsi ini harus dipertimbangkan hanya dalam skenario di mana bisnis memiliki kasus penggunaan domain-spesifik dan jumlah besar data yang berorientasi domain.

## Pemeriksaan Pengetahuan

Apa pendekatan yang baik untuk meningkatkan hasil penyelesaian LLM?

1. Prompt engineering dengan konteks
1. RAG
1. Model yang di-fine-tune

A: Ketiganya bisa membantu. Mulailah dengan prompt engineering dan konteks untuk perbaikan cepat, dan gunakan RAG ketika model membutuhkan fakta terkini atau data bisnis pribadi. Pilih fine-tuning ketika Anda memiliki cukup contoh berkualitas tinggi dan membutuhkan model untuk secara konsisten mengikuti pola tugas, format, nada, atau domain.

## 🚀 Tantangan

Pelajari lebih lanjut bagaimana Anda dapat [menggunakan RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) untuk bisnis Anda.

## Kerja Bagus, Lanjutkan Belajar Anda

Setelah menyelesaikan pelajaran ini, lihat koleksi [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif Anda!

Lanjutkan ke Pelajaran 3 di mana kita akan melihat bagaimana [membangun dengan Generative AI secara Bertanggung Jawab](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->