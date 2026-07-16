[![Integrasi dengan pemanggilan fungsi](../../../translated_images/id/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Siklus Hidup Aplikasi AI Generatif

Pertanyaan penting untuk semua aplikasi AI adalah relevansi fitur AI, karena AI adalah bidang yang berkembang pesat, untuk memastikan bahwa aplikasi Anda tetap relevan, andal, dan kuat, Anda perlu memantau, mengevaluasi, dan meningkatkannya secara terus-menerus. Di sinilah siklus hidup AI generatif berperan.

Siklus hidup AI generatif adalah kerangka kerja yang membimbing Anda melalui tahapan pengembangan, penerapan, dan pemeliharaan aplikasi AI generatif. Ini membantu Anda mendefinisikan tujuan, mengukur kinerja, mengidentifikasi tantangan, dan menerapkan solusi Anda. Ini juga membantu Anda menyelaraskan aplikasi Anda dengan standar etika dan hukum dari domain Anda dan para pemangku kepentingan. Dengan mengikuti siklus hidup AI generatif, Anda dapat memastikan bahwa aplikasi Anda selalu memberikan nilai dan memuaskan pengguna Anda.

## Pendahuluan

Dalam bab ini, Anda akan:

- Memahami Pergeseran Paradigma dari MLOps ke LLMOps
- Siklus Hidup LLM
- Perkakas Siklus Hidup
- Metrifikasi dan Evaluasi Siklus Hidup

## Memahami Pergeseran Paradigma dari MLOps ke LLMOps

LLM adalah alat baru dalam arsenal Kecerdasan Buatan, mereka sangat kuat dalam tugas analisis dan generasi untuk aplikasi, namun kekuatan ini memiliki konsekuensi bagaimana kita menyederhanakan tugas AI dan Pembelajaran Mesin Klasik.

Dengan ini, kita memerlukan Paradigma baru untuk mengadaptasi alat ini secara dinamis, dengan insentif yang tepat. Kita dapat mengkategorikan aplikasi AI lama sebagai "Aplikasi ML" dan aplikasi AI baru sebagai "Aplikasi GenAI" atau hanya "Aplikasi AI", mencerminkan teknologi dan teknik utama yang digunakan pada waktu itu. Ini menggeser narasi kita dalam beberapa cara, lihat perbandingan berikut.

![Perbandingan LLMOps vs. MLOps](../../../translated_images/id/01-llmops-shift.29bc933cb3bb0080.webp)

Perhatikan bahwa dalam LLMOps, kita lebih fokus pada Pengembang Aplikasi, menggunakan integrasi sebagai titik kunci, menggunakan "Model-sebagai-Layanan" dan memikirkan poin berikut untuk metrik.

- Kualitas: Kualitas respons
- Bahaya: AI yang bertanggung jawab
- Kejujuran: Keterpautan respons (Masuk akal? Apakah benar?)
- Biaya: Anggaran solusi
- Latensi: Waktu rata-rata untuk respons token

## Siklus Hidup LLM

Pertama, untuk memahami siklus hidup dan modifikasinya, perhatikan infografis berikut.

![Infografis LLMOps](../../../translated_images/id/02-llmops.70a942ead05a7645.webp)

Seperti yang Anda lihat, ini berbeda dari Siklus Hidup biasa pada MLOps. LLM memiliki banyak persyaratan baru, seperti Prompting, teknik berbeda untuk meningkatkan kualitas (Fine-Tuning, RAG, Meta-Prompts), penilaian dan tanggung jawab dengan AI yang bertanggung jawab, terakhir, metrik evaluasi baru (Kualitas, Bahaya, Kejujuran, Biaya dan Latensi).

Misalnya, perhatikan bagaimana kita berideasi. Menggunakan rekayasa prompt untuk bereksperimen dengan berbagai LLM untuk mengeksplorasi kemungkinan dan menguji apakah Hipotesis mereka bisa benar.

Perlu dicatat bahwa ini bukan linear, melainkan loop terintegrasi, iteratif dan dengan siklus menyeluruh.

Bagaimana kita bisa mengeksplorasi langkah-langkah tersebut? Mari kita masuk ke detail bagaimana kita bisa membangun siklus hidup.

![Alur Kerja LLMOps](../../../translated_images/id/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Ini mungkin terlihat agak rumit, mari fokus dulu pada tiga langkah besar.

1. Berideasi/Mengeksplorasi: Eksplorasi, di sini kami dapat mengeksplorasi sesuai kebutuhan bisnis kami. Prototyping, membuat [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) dan menguji apakah cukup efisien untuk Hipotesis kami.
1. Membangun/Meningkatkan: Implementasi, sekarang, kita mulai mengevaluasi untuk dataset yang lebih besar, menerapkan teknik seperti Fine-tuning dan RAG, untuk memeriksa kekokohan solusi kita. Jika tidak berhasil, mengimplementasikan ulang, menambahkan langkah baru dalam alur atau merestrukturisasi data mungkin membantu. Setelah menguji alur dan skala kita, jika berhasil dan metrik kita terpenuhi, siap untuk langkah berikutnya.
1. Mengoperasionalkan: Integrasi, sekarang menambahkan Sistem Pemantauan dan Peringatan ke sistem kita, penerapan dan integrasi aplikasi ke aplikasi kita.

Kemudian, kita memiliki siklus menyeluruh Manajemen, fokus pada keamanan, kepatuhan dan tata kelola.

Selamat, sekarang aplikasi AI Anda siap dijalankan dan beroperasi. Untuk pengalaman langsung, lihat [Demo Chat Contoso.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

Sekarang, alat apa yang bisa kita gunakan?

## Perkakas Siklus Hidup

Untuk Perkakas, Microsoft menyediakan [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) dan [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) yang memudahkan dan membuat siklus Anda mudah untuk diimplementasikan dan siap digunakan.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst), memungkinkan Anda menggunakan [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (sebelumnya Azure AI Studio) adalah portal web yang memungkinkan Anda mengeksplorasi model, contoh, dan alat, mengelola sumber daya Anda, dan menggunakan alur pengembangan UI serta opsi SDK/CLI untuk pengembangan Berbasis Kode.

![Kemungkinan Azure AI](../../../translated_images/id/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI, memungkinkan Anda menggunakan berbagai sumber daya, untuk mengelola operasi, layanan, proyek, pencarian vektor dan kebutuhan basis data Anda.

![LLMOps dengan Azure AI](../../../translated_images/id/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Membuat, dari Proof-of-Concept (POC) hingga aplikasi skala besar dengan PromptFlow:

- Merancang dan Membangun aplikasi dari VS Code, dengan alat visual dan fungsional
- Menguji dan menyempurnakan aplikasi Anda untuk AI berkualitas, dengan mudah.
- Gunakan Microsoft Foundry untuk Mengintegrasikan dan Mengulang dengan cloud, Dorong dan Terapkan untuk integrasi cepat.

![LLMOps dengan PromptFlow](../../../translated_images/id/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Hebat! Lanjutkan Pembelajaran Anda!

Luar biasa, sekarang pelajari lebih lanjut tentang bagaimana kami menyusun aplikasi untuk menggunakan konsep dengan [Aplikasi Chat Contoso](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), untuk melihat bagaimana Cloud Advocacy menambahkan konsep tersebut dalam demonstrasi. Untuk konten lebih lanjut, lihat [sesi breakout Ignite kami!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Sekarang, lihat Pelajaran 15, untuk memahami bagaimana [Retrieval Augmented Generation dan Basis Data Vektor](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) memengaruhi AI Generatif dan membuat Aplikasi lebih menarik!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->