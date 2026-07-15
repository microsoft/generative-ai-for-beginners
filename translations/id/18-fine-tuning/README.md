[![Open Source Models](../../../translated_images/id/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Menyesuaikan LLM Anda

Menggunakan model bahasa besar untuk membangun aplikasi AI generatif menghadirkan tantangan baru. Masalah utama adalah memastikan kualitas respons (akurasi dan relevansi) dalam konten yang dihasilkan oleh model untuk permintaan pengguna tertentu. Dalam pelajaran sebelumnya, kami membahas teknik seperti rekayasa prompt dan generasi yang diperkuat pengambilan yang mencoba menyelesaikan masalah dengan _mengubah input prompt_ pada model yang ada.

Dalam pelajaran hari ini, kita membahas teknik ketiga, **penyesuaian (fine-tuning)**, yang mencoba mengatasi tantangan dengan _melatih ulang model itu sendiri_ dengan data tambahan. Mari kita selami detailnya.

## Tujuan Pembelajaran

Pelajaran ini memperkenalkan konsep penyesuaian untuk model bahasa yang sudah dilatih sebelumnya, mengeksplorasi manfaat dan tantangan pendekatan ini, serta memberikan panduan kapan dan bagaimana menggunakan penyesuaian untuk meningkatkan kinerja model AI generatif Anda.

Pada akhir pelajaran ini, Anda harus dapat menjawab pertanyaan berikut:

- Apa itu penyesuaian untuk model bahasa?
- Kapan, dan mengapa, penyesuaian berguna?
- Bagaimana saya dapat menyesuaikan model yang sudah dilatih sebelumnya?
- Apa batasan penyesuaian?

Siap? Mari kita mulai.

## Panduan Bergambar

Ingin mendapatkan gambaran besar tentang apa yang akan kita bahas sebelum kita masuk lebih dalam? Lihat panduan bergambar ini yang menjelaskan perjalanan pembelajaran untuk pelajaran ini - dari mempelajari konsep inti dan motivasi untuk penyesuaian, hingga memahami proses dan praktik terbaik untuk menjalankan tugas penyesuaian. Ini adalah topik menarik untuk dijelajahi, jadi jangan lupa untuk mengunjungi halaman [Sumber Daya](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) untuk tautan tambahan yang mendukung perjalanan pembelajaran mandiri Anda!

![Panduan Bergambar untuk Menyesuaikan Model Bahasa](../../../translated_images/id/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Apa itu penyesuaian untuk model bahasa?

Secara definisi, model bahasa besar _dilatih sebelumnya_ pada sejumlah besar teks yang bersumber dari berbagai sumber termasuk internet. Seperti yang telah kita pelajari dalam pelajaran sebelumnya, kita memerlukan teknik seperti _rekayasa prompt_ dan _generasi yang diperkuat pengambilan_ untuk meningkatkan kualitas respons model terhadap pertanyaan pengguna ("prompt").

Teknik rekayasa prompt yang populer melibatkan memberikan model panduan lebih tentang apa yang diharapkan dalam respons baik dengan memberikan _instruksi_ (panduan eksplisit) atau _memberikan beberapa contoh_ (panduan implisit). Ini disebut _few-shot learning_ tetapi memiliki dua keterbatasan:

- Batas token model dapat membatasi jumlah contoh yang dapat Anda berikan, dan membatasi efektivitasnya.
- Biaya token model dapat membuatnya mahal untuk menambahkan contoh ke setiap prompt, dan membatasi fleksibilitas.

Penyesuaian adalah praktik umum dalam sistem pembelajaran mesin di mana kita mengambil model yang sudah dilatih sebelumnya dan melatih ulang dengan data baru untuk meningkatkan kinerjanya pada tugas tertentu. Dalam konteks model bahasa, kita dapat menyesuaikan model yang sudah dilatih sebelumnya _dengan kumpulan contoh yang dikurasi untuk tugas atau domain aplikasi tertentu_ untuk membuat **model khusus** yang mungkin lebih akurat dan relevan untuk tugas atau domain spesifik tersebut. Manfaat sampingan dari penyesuaian adalah dapat mengurangi jumlah contoh yang dibutuhkan untuk pembelajaran few-shot - mengurangi penggunaan token dan biaya terkait.

## Kapan dan mengapa kita harus menyesuaikan model?

Dalam _konteks ini_, saat kita berbicara tentang penyesuaian, kita merujuk pada penyesuaian **terawasi** dimana pelatihan ulang dilakukan dengan **menambahkan data baru** yang bukan bagian dari dataset pelatihan asli. Ini berbeda dari pendekatan penyesuaian tanpa pengawasan di mana model dilatih ulang pada data asli, tetapi dengan hyperparameter yang berbeda.

Hal utama yang harus diingat adalah bahwa penyesuaian adalah teknik lanjutan yang memerlukan tingkat keahlian tertentu untuk mendapatkan hasil yang diinginkan. Jika dilakukan dengan tidak benar, mungkin tidak memberikan peningkatan yang diharapkan, bahkan dapat menurunkan kinerja model untuk domain yang Anda targetkan.

Jadi, sebelum Anda belajar "bagaimana" menyesuaikan model bahasa, Anda perlu tahu "mengapa" Anda harus mengambil jalur ini, dan "kapan" memulai proses penyesuaian. Mulailah dengan bertanya pada diri sendiri pertanyaan-pertanyaan ini:

- **Kasus Penggunaan**: Apa _kasus penggunaan_ Anda untuk penyesuaian? Aspek apa dari model yang sudah dilatih sebelumnya yang ingin Anda tingkatkan?
- **Alternatif**: Apakah Anda sudah mencoba _teknik lain_ untuk mencapai hasil yang diinginkan? Gunakan itu untuk membuat baseline perbandingan.
  - Rekayasa prompt: Coba teknik seperti few-shot prompting dengan contoh respons prompt yang relevan. Evaluasi kualitas respons.
  - Generasi yang Diperkuat Pengambilan: Coba tambahkan prompt dengan hasil pencarian dari data Anda. Evaluasi kualitas respons.
- **Biaya**: Apakah Anda sudah mengidentifikasi biaya untuk penyesuaian?
  - Kemampuan disesuaikan - apakah model yang sudah dilatih tersedia untuk penyesuaian?
  - Upaya - untuk menyiapkan data pelatihan, mengevaluasi & menyempurnakan model.
  - Komputasi - untuk menjalankan pekerjaan penyesuaian, dan menerapkan model yang sudah disesuaikan
  - Data - akses ke contoh berkualitas yang cukup untuk dampak penyesuaian
- **Manfaat**: Apakah Anda sudah mengonfirmasi manfaat penyesuaian?
  - Kualitas - apakah model yang disesuaikan mengungguli baseline?
  - Biaya - apakah mengurangi penggunaan token dengan menyederhanakan prompt?
  - Ekstensibilitas - apakah Anda dapat menggunakan kembali model dasar untuk domain baru?

Dengan menjawab pertanyaan-pertanyaan ini, Anda harus dapat memutuskan apakah penyesuaian adalah pendekatan yang tepat untuk kasus penggunaan Anda. Idealnya, pendekatan ini sah hanya jika manfaatnya lebih besar daripada biayanya. Setelah Anda memutuskan untuk melanjutkan, saatnya memikirkan _bagaimana_ Anda dapat menyesuaikan model yang sudah dilatih sebelumnya.

Ingin mendapatkan wawasan lebih tentang proses pengambilan keputusan? Tonton [Untuk menyesuaikan atau tidak menyesuaikan](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Bagaimana kita dapat menyesuaikan model yang sudah dilatih sebelumnya?

Untuk menyesuaikan model yang sudah dilatih sebelumnya, Anda perlu memiliki:

- model yang sudah dilatih sebelumnya untuk disesuaikan
- dataset yang digunakan untuk penyesuaian
- lingkungan pelatihan untuk menjalankan pekerjaan penyesuaian
- lingkungan hosting untuk menerapkan model yang sudah disesuaikan

## Penyesuaian dalam Praktek

> **Catatan:** `gpt-35-turbo` / `gpt-3.5-turbo`, yang dirujuk dalam beberapa tutorial di bawah, sudah tidak digunakan lagi untuk inferensi dan penyesuaian. Jika Anda memulai pekerjaan penyesuaian baru hari ini, tuju model yang saat ini didukung - misalnya `gpt-4o-mini` atau `gpt-4.1-mini`. Lihat [Daftar model penyesuaian](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) untuk kumpulan model penyesuaian saat ini. Konsep dan langkah dalam tutorial ini masih berlaku.

Sumber daya berikut menyediakan tutorial langkah demi langkah untuk membimbing Anda melalui contoh nyata menggunakan model terpilih dengan dataset yang dikurasi. Untuk mengerjakan tutorial ini, Anda membutuhkan akun pada penyedia tertentu, bersama akses ke model dan dataset yang relevan.

| Penyedia     | Tutorial                                                                                                                                                                       | Deskripsi                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Cara menyesuaikan model chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Pelajari cara menyesuaikan `gpt-35-turbo` untuk domain spesifik ("asisten resep") dengan menyiapkan data pelatihan, menjalankan pekerjaan penyesuaian, dan menggunakan model yang sudah disesuaikan untuk inferensi.                                                                                                                                                                                                                  |
| Azure OpenAI | [Tutorial penyesuaian GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Pelajari cara menyesuaikan model `gpt-35-turbo-0613` **di Azure** dengan langkah membuat & mengunggah data pelatihan, menjalankan pekerjaan penyesuaian. Terapkan & gunakan model baru.                                                                                                                                                                                                                                           |
| Hugging Face | [Menyesuaikan LLM dengan Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Postingan blog ini membimbing Anda menyesuaikan _open LLM_ (mis: `CodeLlama 7B`) menggunakan pustaka [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) dengan [dataset](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) terbuka di Hugging Face.                   |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Menyesuaikan LLM dengan AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (atau AutoTrain Advanced) adalah pustaka python yang dikembangkan oleh Hugging Face yang memungkinkan penyesuaian untuk berbagai tugas termasuk penyesuaian LLM. AutoTrain adalah solusi tanpa kode dan penyesuaian dapat dilakukan di cloud Anda sendiri, di Hugging Face Spaces atau lokal. Mendukung GUI berbasis web, CLI, dan pelatihan melalui file konfigurasi yaml.                                                                     |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Menyesuaikan LLM dengan Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth adalah kerangka kerja sumber terbuka yang mendukung penyesuaian LLM dan pembelajaran penguatan (RL). Unsloth mempermudah pelatihan lokal, evaluasi, dan penerapan dengan [notebook](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) siap pakai. Ini juga mendukung text-to-speech (TTS), BERT, dan model multimodal. Untuk memulai, baca panduan langkah demi langkah mereka [Panduan Menyesuaikan LLM](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Tugas

Pilih salah satu tutorial di atas dan jalani. _Kami mungkin mereplikasi versi tutorial ini dalam Jupyter Notebooks di repo ini hanya untuk referensi. Silakan gunakan sumber asli langsung untuk mendapatkan versi terbaru_.

## Kerja Bagus! Lanjutkan Pembelajaran Anda.

Setelah menyelesaikan pelajaran ini, lihat [koleksi Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif Anda!

Selamat!! Anda telah menyelesaikan pelajaran terakhir dari seri v2 untuk kursus ini! Jangan berhenti belajar dan membangun. \*\*Lihat halaman [SUMBER DAYA](RESOURCES.md?WT.mc_id=academic-105485-koreyst) untuk daftar saran tambahan hanya untuk topik ini.

Seri pelajaran v1 kami juga telah diperbarui dengan lebih banyak tugas dan konsep. Jadi luangkan waktu sejenak untuk menyegarkan pengetahuan Anda - dan silakan [bagikan pertanyaan dan umpan balik Anda](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) untuk membantu kami meningkatkan pelajaran ini bagi komunitas.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->