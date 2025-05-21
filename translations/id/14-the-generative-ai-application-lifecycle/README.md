<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "27a5347a5022d5ef0a72ab029b03526a",
  "translation_date": "2025-05-19T23:31:41+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "id"
}
-->
[![Mengintegrasikan dengan pemanggilan fungsi](../../../translated_images/14-lesson-banner.0b85d0b37979269e80a18bb1e758e1ccca0a2195b426a0af666c8ad14aee60b0.id.png)](https://aka.ms/gen-ai-lesson14-gh?WT.mc_id=academic-105485-koreyst)

# Siklus Hidup Aplikasi AI Generatif

Pertanyaan penting untuk semua aplikasi AI adalah relevansi fitur AI, karena AI adalah bidang yang berkembang pesat, untuk memastikan aplikasi Anda tetap relevan, dapat diandalkan, dan kuat, Anda perlu memantau, mengevaluasi, dan meningkatkannya secara terus-menerus. Di sinilah siklus hidup AI generatif berperan.

Siklus hidup AI generatif adalah kerangka kerja yang membimbing Anda melalui tahap pengembangan, penerapan, dan pemeliharaan aplikasi AI generatif. Ini membantu Anda mendefinisikan tujuan Anda, mengukur kinerja Anda, mengidentifikasi tantangan Anda, dan menerapkan solusi Anda. Ini juga membantu Anda menyelaraskan aplikasi Anda dengan standar etika dan hukum dari domain Anda dan pemangku kepentingan Anda. Dengan mengikuti siklus hidup AI generatif, Anda dapat memastikan bahwa aplikasi Anda selalu memberikan nilai dan memuaskan pengguna Anda.

## Pengantar

Dalam bab ini, Anda akan:

- Memahami Perubahan Paradigma dari MLOps ke LLMOps
- Siklus Hidup LLM
- Alat Siklus Hidup
- Metrik dan Evaluasi Siklus Hidup

## Memahami Perubahan Paradigma dari MLOps ke LLMOps

LLM adalah alat baru dalam persenjataan Kecerdasan Buatan, mereka sangat kuat dalam tugas analisis dan generasi untuk aplikasi, namun kekuatan ini memiliki beberapa konsekuensi dalam cara kita menyederhanakan tugas AI dan Pembelajaran Mesin Klasik.

Dengan ini, kita memerlukan Paradigma baru untuk menyesuaikan alat ini secara dinamis, dengan insentif yang tepat. Kita dapat mengkategorikan aplikasi AI lama sebagai "Aplikasi ML" dan Aplikasi AI baru sebagai "Aplikasi GenAI" atau hanya "Aplikasi AI", mencerminkan teknologi dan teknik utama yang digunakan pada saat itu. Ini mengubah narasi kita dalam berbagai cara, lihat perbandingan berikut.

![Perbandingan LLMOps vs. MLOps](../../../translated_images/01-llmops-shift.82d7bf6eb2d98a01e35f234df654e9aa4ebec89792f274695a5da8dc3f388084.id.png)

Perhatikan bahwa dalam LLMOps, kita lebih fokus pada Pengembang Aplikasi, menggunakan integrasi sebagai poin kunci, menggunakan "Models-as-a-Service" dan memikirkan poin-poin berikut untuk metrik.

- Kualitas: Kualitas respons
- Bahaya: AI yang Bertanggung Jawab
- Kejujuran: Dasar respons (Masuk akal? Apakah benar?)
- Biaya: Anggaran solusi
- Latensi: Waktu rata-rata untuk respons token

## Siklus Hidup LLM

Pertama, untuk memahami siklus hidup dan modifikasinya, mari kita perhatikan infografis berikut.

![Infografis LLMOps](../../../translated_images/02-llmops.287de964b5ce9577678b7f053efb3a3c92adf0852c882c5bae94c11b7563e4db.id.png)

Seperti yang Anda perhatikan, ini berbeda dari Siklus Hidup biasa dari MLOps. LLM memiliki banyak persyaratan baru, seperti Prompting, teknik berbeda untuk meningkatkan kualitas (Fine-Tuning, RAG, Meta-Prompts), penilaian dan tanggung jawab berbeda dengan AI yang bertanggung jawab, terakhir, metrik evaluasi baru (Kualitas, Bahaya, Kejujuran, Biaya, dan Latensi).

Misalnya, lihat bagaimana kita mengideasi. Menggunakan rekayasa prompt untuk bereksperimen dengan berbagai LLM untuk mengeksplorasi kemungkinan untuk menguji apakah Hipotesis mereka bisa benar.

Perhatikan bahwa ini tidak linear, tetapi loop terintegrasi, iteratif, dan dengan siklus yang menyeluruh.

Bagaimana kita bisa mengeksplorasi langkah-langkah tersebut? Mari kita masuk ke detail tentang bagaimana kita bisa membangun siklus hidup.

![Alur Kerja LLMOps](../../../translated_images/03-llm-stage-flows.f3b87c210c1fe37084a7b7408877ff1688e2dc565694789820ec259e76d4ed05.id.png)

Ini mungkin terlihat sedikit rumit, mari kita fokus pada tiga langkah besar terlebih dahulu.

1. Mengideasi/Mengeksplorasi: Eksplorasi, di sini kita dapat mengeksplorasi sesuai dengan kebutuhan bisnis kita. Pembuatan prototipe, membuat [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) dan menguji apakah cukup efisien untuk Hipotesis kita.
1. Membangun/Meningkatkan: Implementasi, sekarang, kita mulai mengevaluasi untuk dataset yang lebih besar menerapkan teknik, seperti Fine-tuning dan RAG, untuk memeriksa ketahanan solusi kita. Jika tidak, menerapkannya kembali, menambahkan langkah baru dalam alur kita atau merestrukturisasi data, mungkin membantu. Setelah menguji alur kita dan skala kita, jika berhasil dan memeriksa Metrik kita, itu siap untuk langkah berikutnya.
1. Mengoperasionalkan: Integrasi, sekarang menambahkan Sistem Pemantauan dan Peringatan ke sistem kita, penerapan dan integrasi aplikasi ke Aplikasi kita.

Kemudian, kita memiliki siklus menyeluruh Manajemen, berfokus pada keamanan, kepatuhan, dan tata kelola.

Selamat, sekarang Anda memiliki Aplikasi AI yang siap digunakan dan operasional. Untuk pengalaman langsung, lihat [Demo Obrolan Contoso.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Sekarang, alat apa yang bisa kita gunakan?

## Alat Siklus Hidup

Untuk Alat, Microsoft menyediakan [Platform AI Azure](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) dan [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) memudahkan dan membuat siklus Anda mudah diimplementasikan dan siap digunakan.

[Platform AI Azure](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys), memungkinkan Anda menggunakan [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio adalah portal web yang memungkinkan Anda menjelajahi model, sampel, dan alat. Mengelola sumber daya Anda, alur pengembangan UI dan opsi SDK/CLI untuk pengembangan Code-First.

![Kemungkinan AI Azure](../../../translated_images/04-azure-ai-platform.bf903e8cdf00f73896d804bd8e6bea62f5280498c998271bd5629c1efa8b466f.id.png)

AI Azure, memungkinkan Anda menggunakan berbagai sumber daya, untuk mengelola operasi, layanan, proyek, pencarian vektor, dan kebutuhan basis data Anda.

![LLMOps dengan AI Azure](../../../translated_images/05-llm-azure-ai-prompt.dc29c0d74b1dd939f7c6cbf28b1fee54b9a846ba04d4068c40134e2627cb7232.id.png)

Membangun, dari Proof-of-Concept(POC) hingga aplikasi skala besar dengan PromptFlow:

- Merancang dan Membangun aplikasi dari VS Code, dengan alat visual dan fungsional
- Menguji dan menyempurnakan aplikasi Anda untuk AI berkualitas, dengan mudah.
- Gunakan Azure AI Studio untuk Mengintegrasikan dan Mengulangi dengan cloud, Push dan Deploy untuk integrasi cepat.

![LLMOps dengan PromptFlow](../../../translated_images/06-llm-promptflow.8f0a6fcbea793a042a3db89ca1db1aa8fd540526958c97b5e894748fb4a87edd.id.png)

## Hebat! Lanjutkan Pembelajaran Anda!

Luar biasa, sekarang pelajari lebih lanjut tentang bagaimana kita menyusun aplikasi untuk menggunakan konsep dengan [Aplikasi Obrolan Contoso](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), untuk melihat bagaimana Cloud Advocacy menambahkan konsep tersebut dalam demonstrasi. Untuk konten lebih lanjut, lihat [sesi breakout Ignite!](https://www.youtube.com/watch?v=DdOylyrTOWg)

Sekarang, lihat Pelajaran 15, untuk memahami bagaimana [Retrieval Augmented Generation dan Basis Data Vektor](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) mempengaruhi AI Generatif dan membuat Aplikasi lebih menarik!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap disadari bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi penting, disarankan untuk menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.