[![Open Source Models](../../../translated_images/id/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Menyempurnakan Fine-Tuning LLM Anda

Menggunakan model bahasa besar untuk membangun aplikasi AI generatif menghadirkan tantangan baru. Masalah utama adalah memastikan kualitas respons (akurasi dan relevansi) dalam konten yang dihasilkan oleh model untuk permintaan pengguna tertentu. Dalam pelajaran sebelumnya, kita membahas teknik seperti rekayasa prompt dan generasi yang diperkuat dengan pengambilan yang mencoba menyelesaikan masalah dengan _memodifikasi input prompt_ pada model yang ada.

Dalam pelajaran hari ini, kita membahas teknik ketiga, **fine-tuning**, yang mencoba mengatasi tantangan ini dengan _melatih ulang model itu sendiri_ dengan data tambahan. Mari kita selami detailnya.

## Tujuan Pembelajaran

Pelajaran ini memperkenalkan konsep fine-tuning untuk model bahasa yang sudah dilatih sebelumnya, mengeksplorasi manfaat dan tantangan pendekatan ini, serta memberikan panduan kapan dan bagaimana menggunakan fine-tuning untuk meningkatkan kinerja model AI generatif Anda.

Pada akhir pelajaran ini, Anda harus dapat menjawab pertanyaan berikut:

- Apa itu fine-tuning untuk model bahasa?
- Kapan, dan mengapa, fine-tuning berguna?
- Bagaimana saya bisa melakukan fine-tuning pada model yang sudah dilatih sebelumnya?
- Apa saja keterbatasan dari fine-tuning?

Siap? Mari kita mulai.

## Panduan Bergambar

Ingin mendapatkan gambaran besar tentang apa yang akan kita bahas sebelum mendalaminya? Lihat panduan bergambar ini yang menjelaskan perjalanan pembelajaran untuk pelajaran ini—dari mempelajari konsep inti dan motivasi untuk fine-tuning, hingga memahami proses dan praktik terbaik untuk melaksanakan tugas fine-tuning. Ini adalah topik yang menarik untuk dijelajahi, jadi jangan lupa untuk memeriksa halaman [Resources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) untuk tautan tambahan yang mendukung perjalanan pembelajaran Anda secara mandiri!

![Panduan Bergambar untuk Fine Tuning Model Bahasa](../../../translated_images/id/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Apa itu fine-tuning untuk model bahasa?

Secara definisi, model bahasa besar dilatih _pre-trained_ pada sejumlah besar teks yang bersumber dari berbagai sumber termasuk internet. Seperti yang telah kita pelajari dalam pelajaran sebelumnya, kita memerlukan teknik seperti _prompt engineering_ dan _retrieval-augmented generation_ untuk meningkatkan kualitas respons model terhadap pertanyaan pengguna ("prompt").

Teknik rekayasa prompt yang populer melibatkan memberikan model lebih banyak panduan tentang apa yang diharapkan dalam respons, baik dengan menyediakan _instruksi_ (panduan eksplisit) atau _memberi beberapa contoh_ (panduan implisit). Ini disebut _few-shot learning_ tetapi memiliki dua keterbatasan:

- Batas token model dapat membatasi jumlah contoh yang dapat Anda berikan, dan mengurangi efektivitasnya.
- Biaya token model dapat membuatnya mahal untuk menambahkan contoh ke setiap prompt, dan membatasi fleksibilitas.

Fine-tuning adalah praktik umum dalam sistem pembelajaran mesin di mana kita mengambil model yang sudah dilatih sebelumnya dan melatih ulang dengan data baru untuk meningkatkan kinerjanya pada tugas spesifik. Dalam konteks model bahasa, kita dapat melakukan fine-tuning pada model yang sudah dilatih _dengan kumpulan contoh yang dikurasi untuk tugas atau domain aplikasi tertentu_ untuk membuat **model khusus** yang mungkin lebih akurat dan relevan untuk tugas atau domain tersebut. Manfaat tambahan dari fine-tuning adalah dapat mengurangi jumlah contoh yang diperlukan untuk few-shot learning—mengurangi penggunaan token dan biaya terkait.

## Kapan dan mengapa kita harus melakukan fine-tuning model?

Dalam _konteks ini_, ketika kita berbicara tentang fine-tuning, kita merujuk pada fine-tuning **terawasi** di mana pelatihan ulang dilakukan dengan **menambahkan data baru** yang tidak termasuk dalam dataset pelatihan asli. Ini berbeda dengan pendekatan fine-tuning tanpa pengawasan di mana model dilatih ulang pada data asli, tetapi dengan hyperparameter yang berbeda.

Hal utama yang perlu diingat adalah bahwa fine-tuning adalah teknik lanjutan yang memerlukan tingkat keahlian tertentu untuk mendapatkan hasil yang diinginkan. Jika dilakukan dengan salah, mungkin tidak memberikan peningkatan yang diharapkan, bahkan dapat menurunkan kinerja model untuk domain target Anda.

Jadi, sebelum Anda mempelajari "bagaimana" melakukan fine-tuning model bahasa, Anda perlu tahu "mengapa" Anda harus menempuh jalur ini, dan "kapan" memulai proses fine-tuning. Mulailah dengan menanyakan pertanyaan-pertanyaan ini pada diri Anda:

- **Kasus Penggunaan**: Apa _kasus penggunaan_ Anda untuk fine-tuning? Aspek apa dari model pre-trained saat ini yang ingin Anda tingkatkan?
- **Alternatif**: Apakah Anda sudah mencoba _teknik lain_ untuk mencapai hasil yang diinginkan? Gunakan ini untuk membuat baseline perbandingan.
  - Rekayasa prompt: Cobalah teknik seperti few-shot prompting dengan contoh respons prompt yang relevan. Evaluasi kualitas respons.
  - Retrieval Augmented Generation: Cobalah melengkapi prompt dengan hasil query yang diambil dengan mencari data Anda. Evaluasi kualitas respons.
- **Biaya**: Apakah Anda sudah mengidentifikasi biaya untuk fine-tuning?
  - Kemampuan tuning - apakah model pre-trained tersedia untuk fine-tuning?
  - Upaya - untuk menyiapkan data pelatihan, mengevaluasi & menyempurnakan model.
  - Komputasi - untuk menjalankan pekerjaan fine-tuning, dan menerapkan model yang sudah di-fine-tune
  - Data - akses ke contoh berkualitas cukup untuk dampak fine-tuning
- **Manfaat**: Apakah Anda sudah memastikan manfaat dari fine-tuning?
  - Kualitas - apakah model yang di-fine-tune mengungguli baseline?
  - Biaya - apakah ini mengurangi penggunaan token dengan menyederhanakan prompt?
  - Ekstensibilitas - dapatkah Anda menggunakan ulang model dasar untuk domain baru?

Dengan menjawab pertanyaan-pertanyaan ini, Anda harus dapat memutuskan apakah fine-tuning adalah pendekatan yang tepat untuk kasus penggunaan Anda. Idealnya, pendekatan ini hanya valid jika manfaatnya lebih besar daripada biayanya. Setelah Anda memutuskan untuk melanjutkan, saatnya memikirkan _bagaimana_ Anda dapat melakukan fine-tuning pada model yang sudah dilatih sebelumnya.

Ingin mendapatkan wawasan lebih tentang proses pengambilan keputusan? Tonton [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Bagaimana cara melakukan fine-tuning model pre-trained?

Untuk melakukan fine-tuning model pre-trained, Anda perlu memiliki:

- model pre-trained untuk di-fine-tune
- dataset untuk digunakan dalam fine-tuning
- lingkungan pelatihan untuk menjalankan pekerjaan fine-tuning
- lingkungan hosting untuk menerapkan model yang sudah di-fine-tune

## Fine-Tuning di Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) adalah tempat Anda melakukan fine-tuning, menerapkan, dan mengelola model khusus di Azure saat ini (menggabungkan apa yang dulu dikenal sebagai Azure OpenAI Studio dan Azure AI Studio). Sebelum memulai pekerjaan, ada baiknya memahami pilihan yang diberikan Foundry—dan praktik terbaik yang direkomendasikan platform. Di balik layar, Foundry menggunakan **LoRA (low-rank adaptation)** untuk melakukan fine-tuning model secara efisien, yang membuat pelatihan lebih cepat dan lebih terjangkau dibandingkan melatih ulang setiap bobot.

### Langkah 1: Pilih teknik pelatihan

Foundry mendukung tiga teknik fine-tuning. **Mulailah dengan SFT** - ini mencakup berbagai skenario paling luas.

| Teknik | Apa yang Dilakukan | Kapan Menggunakannya |
| --- | --- | --- |
| **Supervised Fine-Tuning (SFT)** | Melatih pada pasangan contoh input/output sehingga model belajar menghasilkan respons yang Anda inginkan. | Default untuk sebagian besar tugas: spesialisasi domain, kinerja tugas, gaya dan nada, mengikuti instruksi, dan adaptasi bahasa. |
| **Direct Preference Optimization (DPO)** | Belajar dari pasangan respons _lebih disukai vs. tidak disukai_ untuk menyelaraskan output dengan preferensi manusia. | Meningkatkan kualitas respons, keamanan, dan keselarasan ketika Anda memiliki umpan balik perbandingan. |
| **Reinforcement Fine-Tuning (RFT)** | Menggunakan sinyal penghargaan dari _penilai_ untuk mengoptimalkan perilaku kompleks dengan pembelajaran penguatan. | Domain objektif dan berat penalaran (matematika, kimia, fisika) dengan jawaban benar/salah yang jelas. Memerlukan keahlian ML lebih. |

### Langkah 2: Pilih tingkatan pelatihan

Foundry memungkinkan Anda memilih bagaimana dan di mana pelatihan dijalankan:

- **Standard** - melatih di wilayah sumber daya Anda dan menjamin residensi data. Gunakan saat data harus tetap di wilayah tertentu.
- **Global** - lebih murah dan cepat untuk antre dengan memanfaatkan kapasitas di luar wilayah Anda (data dan bobot disalin ke wilayah pelatihan). Pilihan bagus jika residensi data tidak menjadi persyaratan.
- **Developer** - biaya terendah, menggunakan kapasitas menganggur tanpa jaminan latensi/SLA (pekerjaan bisa dihentikan sementara dan dilanjutkan). Ideal untuk eksperimen.

### Langkah 3: Pilih model dasar

Model yang dapat di-fine-tune termasuk OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini`, dan `gpt-4.1-nano` (SFT; keluarga 4o/4.1 juga mendukung DPO), model reasoning `o4-mini` dan `gpt-5` (RFT), serta model open-source seperti `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct`, dan `gpt-oss-20b` (SFT pada sumber daya Foundry). Selalu periksa daftar [Fine-tuning models list](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) saat ini untuk metode, wilayah, dan ketersediaan yang didukung.

> Foundry menawarkan dua modalitas: **serverless** (harga berbasis konsumsi, tanpa kuota GPU untuk dikelola, OpenAI dan model terpilih) dan **managed compute** (bawa VM sendiri lewat Azure Machine Learning untuk jangkauan model terluas). Sebagian besar pengguna harus mulai dengan serverless.

### Praktik terbaik Foundry

- **Baseline dulu.** Ukur model dasar dengan rekayasa prompt dan RAG _sebelum_ melakukan fine-tuning, supaya Anda bisa membuktikan peningkatan.
- **Mulai kecil, lalu skala.** Mulai dengan 50-100 contoh berkualitas tinggi untuk memvalidasi pendekatan, lalu tingkatkan menjadi 500+ untuk produksi. Kualitas lebih penting daripada kuantitas - pangkas contoh berkualitas rendah.
- **Format data dengan benar.** File pelatihan dan validasi harus JSONL, UTF-8 **dengan BOM**, ukuran kurang dari 512 MB, menggunakan format pesan chat-completions. Selalu sertakan file validasi agar dapat memantau overfitting.
- **Pertahankan prompt sistem pelatihan saat inferensi.** Gunakan pesan sistem yang sama ketika memanggil model seperti saat pelatihan.
- **Evaluasi checkpoint - jangan langsung terapkan yang terakhir.** Foundry menyimpan tiga epoch terakhir sebagai checkpoint yang dapat diterapkan; pilih yang terbaik merepresentasikan generalisasi dengan memantau `train_loss` / `valid_loss` dan akurasi token.
- **Ukur biaya token bersama dengan kualitas** saat membandingkan model yang sudah di-fine-tune dengan baseline.
- **Iterasi dengan fine-tuning berkelanjutan.** Anda dapat melakukan fine-tuning ulang pada model yang sudah di-fine-tune dengan data baru (didukung untuk model OpenAI).
- **Perhatikan biaya hosting.** Model khusus yang diterapkan dikenakan biaya per jam, dan deployment yang tidak aktif dihapus setelah 15 hari - bersihkan yang tidak diperlukan.

Kerjakan panduan langkah demi langkah dalam [Customize a model with fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst), dan lihat panduan untuk [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) dan [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) saat Anda siap untuk teknik lainnya.

## Fine-Tuning Dalam Praktik

Sumber daya berikut menyediakan tutorial langkah demi langkah yang memandu Anda melalui contoh nyata pada model yang saat ini didukung dengan kumpulan data yang dikurasi. Untuk mengerjakannya, Anda memerlukan akun pada penyedia tertentu, serta akses ke model dan dataset terkait.

| Penyedia     | Tutorial                                                                                                                                                                       | Deskripsi                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [How to fine-tune chat models](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Pelajari cara melakukan fine-tuning model chat OpenAI terbaru untuk domain spesifik ("asisten resep") dengan menyiapkan data pelatihan, menjalankan pekerjaan fine-tuning, dan menggunakan model yang sudah di-fine-tune untuk inferensi.                                                                                                                                                                                                                                              |
| Microsoft Foundry | [Customize a model with fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Pelajari cara melakukan fine-tuning model yang saat ini didukung seperti `gpt-4.1-mini` **di Azure** dengan Microsoft Foundry: menyiapkan & mengunggah data pelatihan dan validasi, menjalankan pekerjaan fine-tuning, lalu menerapkan & menggunakan model baru.                                                                                                                                                                                                                                                                 |

| Hugging Face | [Fine-tuning LLMs dengan Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Postingan blog ini memandu Anda melakukan fine-tuning pada _open LLM_ (misal: `CodeLlama 7B`) menggunakan library [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) dengan [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) terbuka di Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fine-tuning LLMs dengan AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (atau AutoTrain Advanced) adalah library python yang dikembangkan oleh Hugging Face yang memungkinkan fine-tuning untuk banyak tugas berbeda termasuk fine-tuning LLM. AutoTrain adalah solusi tanpa kode dan fine-tuning dapat dilakukan di cloud Anda sendiri, di Hugging Face Spaces atau secara lokal. Mendukung baik GUI berbasis web, CLI, dan pelatihan melalui file konfigurasi yaml.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Fine-tuning LLMs dengan Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth adalah kerangka kerja open-source yang mendukung fine-tuning LLM dan reinforcement learning (RL). Unsloth mempermudah pelatihan lokal, evaluasi, dan penyebaran dengan [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) siap pakai. Juga mendukung text-to-speech (TTS), BERT, dan model multimodal. Untuk memulai, bacalah panduan langkah demi langkah mereka [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Tugas

Pilih salah satu tutorial di atas dan jalankan langkah-langkahnya. _Kami mungkin akan mereplikasi versi tutorial ini di Jupyter Notebooks di repo ini sebagai referensi saja. Silakan gunakan sumber asli secara langsung untuk mendapatkan versi terbaru_.

## Kerja Hebat! Lanjutkan Pembelajaran Anda.

Setelah menyelesaikan pelajaran ini, lihat koleksi kami [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan AI Generatif Anda!

Selamat!! Anda telah menyelesaikan pelajaran terakhir dari seri v2 untuk kursus ini! Jangan berhenti belajar dan membangun. \*\*Lihat halaman [RESOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) untuk daftar saran tambahan khusus untuk topik ini.

Seri pelajaran v1 kami juga telah diperbarui dengan lebih banyak tugas dan konsep. Jadi luangkan waktu sejenak untuk menyegarkan pengetahuan Anda - dan silakan [bagikan pertanyaan dan umpan balik Anda](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) untuk membantu kami memperbaiki pelajaran ini untuk komunitas.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->