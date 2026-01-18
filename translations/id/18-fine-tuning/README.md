<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3772dcd23a98e2010f53ce8b9c583631",
  "translation_date": "2026-01-18T18:38:59+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "id"
}
-->
[![Open Source Models](../../../../../translated_images/id/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Fine-Tuning Your LLM

Menggunakan model bahasa besar untuk membangun aplikasi AI generatif menghadirkan tantangan baru. Masalah utama adalah memastikan kualitas respons (akurasi dan relevansi) dalam konten yang dihasilkan oleh model untuk permintaan pengguna tertentu. Dalam pelajaran sebelumnya, kami membahas teknik seperti rekayasa prompt dan generasi yang diperkuat pengambilan yang mencoba menyelesaikan masalah dengan _memodifikasi input prompt_ pada model yang ada.

Dalam pelajaran hari ini, kami membahas teknik ketiga, **fine-tuning**, yang mencoba mengatasi tantangan dengan _melatih ulang model itu sendiri_ dengan data tambahan. Mari kita selami detailnya.

## Learning Objectives

Pelajaran ini memperkenalkan konsep fine-tuning untuk model bahasa pra-latih, mengeksplorasi manfaat dan tantangan pendekatan ini, dan memberikan panduan kapan dan bagaimana menggunakan fine-tuning untuk meningkatkan performa model AI generatif Anda.

Pada akhir pelajaran ini, Anda harus dapat menjawab pertanyaan berikut:

- Apa itu fine-tuning untuk model bahasa?
- Kapan, dan mengapa, fine-tuning berguna?
- Bagaimana saya dapat melakukan fine-tuning pada model pra-latih?
- Apa keterbatasan dari fine-tuning?

Siap? Mari mulai.

## Illustrated Guide

Ingin mendapatkan gambaran besar tentang apa yang akan kita bahas sebelum kita melanjutkan? Lihat panduan bergambar ini yang menggambarkan perjalanan pembelajaran untuk pelajaran ini - dari mempelajari konsep inti dan motivasi untuk fine-tuning, hingga memahami proses dan praktik terbaik dalam menjalankan tugas fine-tuning. Ini adalah topik yang menarik untuk dieksplorasi, jadi jangan lupa lihat halaman [Resources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) untuk tautan tambahan yang mendukung pembelajaran mandiri Anda!

![Illustrated Guide to Fine Tuning Language Models](../../../../../translated_images/id/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## What is fine-tuning for language models?

Menurut definisi, model bahasa besar _pra-latih_ pada sejumlah besar teks yang bersumber dari berbagai sumber termasuk internet. Seperti yang telah kita pelajari dalam pelajaran sebelumnya, kita memerlukan teknik seperti _rekayasa prompt_ dan _generasi yang diperkuat pengambilan_ untuk meningkatkan kualitas respons model terhadap pertanyaan pengguna ("prompt").

Teknik rekayasa prompt yang populer melibatkan memberikan model lebih banyak panduan tentang apa yang diharapkan dalam respons baik dengan memberikan _instruksi_ (panduan eksplisit) atau _memberikan beberapa contoh_ (panduan implisit). Ini disebut sebagai _few-shot learning_ namun memiliki dua keterbatasan:

- Batas token model dapat membatasi jumlah contoh yang dapat Anda berikan, dan membatasi efektivitasnya.
- Biaya token model dapat membuatnya mahal untuk menambahkan contoh pada setiap prompt, dan membatasi fleksibilitas.

Fine-tuning adalah praktik umum dalam sistem pembelajaran mesin dimana kita mengambil model pra-latih dan melatih ulang dengan data baru untuk meningkatkan performanya pada tugas tertentu. Dalam konteks model bahasa, kita dapat melakukan fine-tuning pada model pra-latih _dengan kumpulan contoh yang dikurasi untuk tugas atau domain aplikasi tertentu_ untuk membuat **model khusus** yang mungkin lebih akurat dan relevan untuk tugas atau domain tersebut. Manfaat tambahan dari fine-tuning adalah dapat mengurangi jumlah contoh yang dibutuhkan untuk few-shot learning - mengurangi penggunaan token dan biaya terkait.

## When and why should we fine-tune models?

Dalam _konteks ini_, ketika kita berbicara tentang fine-tuning, yang kita maksud adalah fine-tuning **terawasi** dimana pelatihan ulang dilakukan dengan **menambahkan data baru** yang tidak menjadi bagian dari dataset pelatihan asli. Ini berbeda dari pendekatan fine-tuning tak terawasi dimana model dilatih ulang pada data asli, namun dengan hyperparameter yang berbeda.

Hal utama yang perlu diingat adalah bahwa fine-tuning adalah teknik lanjutan yang membutuhkan tingkat keahlian tertentu untuk mendapatkan hasil yang diinginkan. Jika dilakukan dengan salah, mungkin tidak memberikan peningkatan yang diharapkan, bahkan dapat menurunkan performa model untuk domain yang Anda targetkan.

Jadi, sebelum Anda mempelajari "bagaimana" melakukan fine-tuning pada model bahasa, Anda perlu tahu "mengapa" Anda harus mengambil jalur ini, dan "kapan" memulai proses fine-tuning. Mulailah dengan bertanya pada diri sendiri pertanyaan ini:

- **Use Case**: Apa _kasus penggunaan_ Anda untuk fine-tuning? Aspek model pra-latih mana yang ingin Anda tingkatkan?
- **Alternatives**: Apakah Anda sudah mencoba _teknik lain_ untuk mencapai hasil yang diinginkan? Gunakan teknik tersebut untuk membuat baseline perbandingan.
  - Rekayasa prompt: Coba teknik seperti few-shot prompting dengan contoh respons prompt yang relevan. Evaluasi kualitas respons.
  - Generasi yang diperkuat pengambilan: Coba memperkuat prompt dengan hasil query yang diambil dari data Anda. Evaluasi kualitas respons.
- **Costs**: Apakah Anda sudah mengidentifikasi biaya untuk melakukan fine-tuning?
  - Kemampuan tunning - apakah model pra-latih tersedia untuk fine-tuning?
  - Upaya - untuk menyiapkan data pelatihan, mengevaluasi & menyempurnakan model.
  - Komputasi - untuk menjalankan tugas fine-tuning, dan menyebarkan model yang telah di-tuning
  - Data - akses ke contoh berkualitas cukup untuk berdampak pada fine-tuning
- **Benefits**: Apakah Anda sudah mengonfirmasi manfaat dari fine-tuning?
  - Kualitas - apakah model yang dituning memberikan performa lebih baik daripada baseline?
  - Biaya - apakah mengurangi penggunaan token dengan menyederhanakan prompt?
  - Ekstensibilitas - dapatkah Anda menggunakan ulang model dasar untuk domain baru?

Dengan menjawab pertanyaan ini, Anda seharusnya dapat memutuskan apakah fine-tuning adalah pendekatan yang tepat untuk kasus penggunaan Anda. Idealnya, pendekatan ini valid hanya jika manfaatnya melebihi biayanya. Setelah Anda memutuskan untuk melanjutkan, saatnya memikirkan _bagaimana_ cara melakukan fine-tuning pada model pra-latih.

Ingin mendapatkan lebih banyak wawasan mengenai proses pengambilan keputusan? Tonton [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## How can we fine-tune a pre-trained model?

Untuk melakukan fine-tuning pada model pra-latih, Anda perlu memiliki:

- model pra-latih untuk di-fine-tune
- dataset yang digunakan untuk fine-tuning
- lingkungan pelatihan untuk menjalankan tugas fine-tuning
- lingkungan hosting untuk menyebarkan model yang telah di-fine-tune

## Fine-Tuning In Action

Sumber daya berikut menyediakan tutorial langkah-demi-langkah untuk membimbing Anda melalui contoh nyata menggunakan model terpilih dengan dataset yang dikurasi. Untuk mengerjakan tutorial ini, Anda memerlukan akun pada penyedia spesifik, bersama akses ke model dan dataset yang relevan.

| Provider     | Tutorial                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [How to fine-tune chat models](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Pelajari cara fine-tune `gpt-35-turbo` untuk domain khusus ("asisten resep") dengan menyiapkan data pelatihan, menjalankan tugas fine-tuning, dan menggunakan model yang sudah di-fine-tune untuk inferensi.                                                                                                                                                                                                                          |
| Azure OpenAI | [GPT 3.5 Turbo fine-tuning tutorial](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Pelajari cara fine-tune model `gpt-35-turbo-0613` **di Azure** dengan melakukan langkah-langkah membuat & mengunggah data pelatihan, menjalankan tugas fine-tuning. Menyebarkan & menggunakan model baru.                                                                                                                                                                                                                             |
| Hugging Face | [Fine-tuning LLMs with Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Postingan blog ini membimbing Anda melakukan fine-tuning pada _LLM terbuka_ (contoh: `CodeLlama 7B`) menggunakan pustaka [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) dengan [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) terbuka di Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fine-tuning LLMs with AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (atau AutoTrain Advanced) adalah pustaka python yang dikembangkan oleh Hugging Face yang memungkinkan fine-tuning untuk banyak tugas berbeda termasuk fine-tuning LLM. AutoTrain adalah solusi tanpa kode dan fine-tuning dapat dilakukan di cloud Anda sendiri, di Hugging Face Spaces, atau secara lokal. Mendukung antarmuka GUI berbasis web, CLI, dan pelatihan via file konfigurasi yaml.                                         |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Fine-tuning LLMs with Unsloth](https://github.com/unslothai/unsloth)                                                         | Unsloth adalah kerangka kerja open-source yang mendukung fine-tuning LLM dan pembelajaran penguatan (RL). Unsloth mempermudah pelatihan lokal, evaluasi, dan penyebaran dengan [notebook](https://github.com/unslothai/notebooks) siap pakai. Mendukung juga teks-ke-suara (TTS), BERT, dan model multimodal. Untuk memulai, baca panduan [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                        |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Assignment

Pilih salah satu tutorial di atas dan kerjakan. _Kami mungkin akan mereplikasi versi tutorial ini dalam Jupyter Notebooks di repo ini hanya sebagai referensi. Silakan gunakan sumber asli secara langsung untuk mendapatkan versi terbaru_.

## Great Work! Continue Your Learning.

Setelah menyelesaikan pelajaran ini, lihat koleksi [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Generative AI Anda!

Selamat!! Anda telah menyelesaikan pelajaran terakhir dari seri v2 untuk kursus ini! Jangan berhenti belajar dan membangun. \*\*Lihat halaman [RESOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) untuk daftar saran tambahan hanya untuk topik ini.

Seri v1 pelajaran kami juga telah diperbarui dengan lebih banyak tugas dan konsep. Jadi luangkan waktu sebentar untuk menyegarkan pengetahuan Anda - dan mohon [bagikan pertanyaan dan umpan balik Anda](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) untuk membantu kami memperbaiki pelajaran ini bagi komunitas.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mendapatkan terjemahan yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->