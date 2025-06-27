<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "27a5347a5022d5ef0a72ab029b03526a",
  "translation_date": "2025-06-25T22:07:16+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "id"
}
-->
[![Integrasi dengan pemanggilan fungsi](../../../translated_images/14-lesson-banner.066d74a31727ac121eeac06376a068a397d8e335281e63ce94130d11f516e46b.id.png)](https://aka.ms/gen-ai-lesson14-gh?WT.mc_id=academic-105485-koreyst)

# Siklus Hidup Aplikasi AI Generatif

Pertanyaan penting untuk semua aplikasi AI adalah relevansi fitur AI, karena AI adalah bidang yang berkembang pesat. Untuk memastikan aplikasi Anda tetap relevan, andal, dan kuat, Anda perlu memantau, mengevaluasi, dan memperbaikinya secara terus-menerus. Di sinilah siklus hidup AI generatif berperan.

Siklus hidup AI generatif adalah kerangka kerja yang memandu Anda melalui tahap pengembangan, penerapan, dan pemeliharaan aplikasi AI generatif. Ini membantu Anda mendefinisikan tujuan Anda, mengukur kinerja Anda, mengidentifikasi tantangan Anda, dan menerapkan solusi Anda. Ini juga membantu Anda menyelaraskan aplikasi Anda dengan standar etika dan hukum dari domain dan pemangku kepentingan Anda. Dengan mengikuti siklus hidup AI generatif, Anda dapat memastikan bahwa aplikasi Anda selalu memberikan nilai dan memuaskan pengguna Anda.

## Pendahuluan

Dalam bab ini, Anda akan:

- Memahami Pergeseran Paradigma dari MLOps ke LLMOps
- Siklus Hidup LLM
- Alat untuk Siklus Hidup
- Metode dan Evaluasi Siklus Hidup

## Memahami Pergeseran Paradigma dari MLOps ke LLMOps

LLM adalah alat baru dalam persenjataan Kecerdasan Buatan, sangat kuat dalam tugas analisis dan generasi untuk aplikasi, namun kekuatan ini memiliki beberapa konsekuensi dalam cara kita menyederhanakan tugas AI dan Pembelajaran Mesin Klasik.

Dengan ini, kita memerlukan Paradigma baru untuk menyesuaikan alat ini secara dinamis, dengan insentif yang tepat. Kita dapat mengkategorikan aplikasi AI lama sebagai "Aplikasi ML" dan Aplikasi AI baru sebagai "Aplikasi GenAI" atau hanya "Aplikasi AI", mencerminkan teknologi dan teknik utama yang digunakan saat itu. Ini mengubah narasi kita dalam berbagai cara, lihat perbandingan berikut.

![Perbandingan LLMOps vs. MLOps](../../../translated_images/01-llmops-shift.29bc933cb3bb0080a562e1655c0c719b71a72c3be6252d5c564b7f598987e602.id.png)

Perhatikan bahwa dalam LLMOps, kita lebih fokus pada Pengembang Aplikasi, menggunakan integrasi sebagai titik kunci, menggunakan "Model-as-a-Service" dan memikirkan poin-poin berikut untuk metrik.

- Kualitas: Kualitas respons
- Bahaya: AI yang bertanggung jawab
- Kejujuran: Ketepatan respons (Masuk akal? Apakah benar?)
- Biaya: Anggaran Solusi
- Latensi: Rata-rata waktu untuk respons token

## Siklus Hidup LLM

Pertama, untuk memahami siklus hidup dan modifikasinya, mari kita perhatikan infografis berikut.

![Infografis LLMOps](../../../translated_images/02-llmops.70a942ead05a7645db740f68727d90160cb438ab71f0fb20548bc7fe5cad83ff.id.png)

Seperti yang mungkin Anda perhatikan, ini berbeda dari Siklus Hidup biasa dari MLOps. LLM memiliki banyak persyaratan baru, seperti Prompting, teknik berbeda untuk meningkatkan kualitas (Fine-Tuning, RAG, Meta-Prompts), penilaian dan tanggung jawab yang berbeda dengan AI yang bertanggung jawab, terakhir, metrik evaluasi baru (Kualitas, Bahaya, Kejujuran, Biaya, dan Latensi).

Misalnya, lihat bagaimana kita beride. Menggunakan rekayasa prompt untuk bereksperimen dengan berbagai LLM untuk mengeksplorasi kemungkinan untuk menguji apakah Hipotesis mereka bisa benar.

Perhatikan bahwa ini tidak linier, tetapi terintegrasi dalam loop, iteratif dan dengan siklus keseluruhan.

Bagaimana kita bisa mengeksplorasi langkah-langkah tersebut? Mari kita rinci bagaimana kita bisa membangun siklus hidup.

![Alur Kerja LLMOps](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cfa886ed6ba04aa52a096a545e1bc44fa54d7d5983a7201892.id.png)

Ini mungkin terlihat agak rumit, mari kita fokus pada tiga langkah besar terlebih dahulu.

1. Ideasi/Eksplorasi: Eksplorasi, di sini kita dapat mengeksplorasi sesuai kebutuhan bisnis kita. Membuat prototipe, membuat [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) dan menguji apakah cukup efisien untuk Hipotesis kita.
2. Pembangunan/Peningkatan: Implementasi, sekarang, kita mulai mengevaluasi untuk kumpulan data yang lebih besar menerapkan teknik, seperti Fine-tuning dan RAG, untuk memeriksa kekuatan solusi kita. Jika tidak, mengimplementasikannya kembali, menambahkan langkah baru dalam alur kita atau merestrukturisasi data, mungkin bisa membantu. Setelah menguji alur dan skala kita, jika berhasil dan memeriksa Metrik kita, siap untuk langkah berikutnya.
3. Operasionalisasi: Integrasi, sekarang menambahkan Sistem Pemantauan dan Peringatan ke sistem kita, penerapan dan integrasi aplikasi ke Aplikasi kita.

Kemudian, kita memiliki siklus keseluruhan Manajemen, berfokus pada keamanan, kepatuhan, dan tata kelola.

Selamat, sekarang Anda memiliki Aplikasi AI Anda siap untuk digunakan dan operasional. Untuk pengalaman langsung, lihat [Demo Obrolan Contoso.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Sekarang, alat apa yang bisa kita gunakan?

## Alat untuk Siklus Hidup

Untuk Alat, Microsoft menyediakan [Platform AI Azure](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) dan [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) untuk memfasilitasi dan membuat siklus Anda mudah diimplementasikan dan siap digunakan.

[Platform AI Azure](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys), memungkinkan Anda menggunakan [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio adalah portal web yang memungkinkan Anda menjelajahi model, sampel, dan alat. Mengelola sumber daya Anda, alur pengembangan UI, dan opsi SDK/CLI untuk pengembangan Code-First.

![Kemungkinan AI Azure](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8b166e194928f057074843d1955177baf0f5b53d50d7b6153.id.png)

Azure AI, memungkinkan Anda menggunakan berbagai sumber daya, untuk mengelola operasi, layanan, proyek, pencarian vektor, dan kebutuhan basis data Anda.

![LLMOps dengan Azure AI](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf95420668e3464aae70d8b22275a744254e941dd5e73ae0d2.id.png)

Membangun, dari Proof-of-Concept(POC) hingga aplikasi skala besar dengan PromptFlow:

- Merancang dan Membangun aplikasi dari VS Code, dengan alat visual dan fungsional
- Menguji dan menyempurnakan aplikasi Anda untuk kualitas AI, dengan mudah.
- Gunakan Azure AI Studio untuk Mengintegrasikan dan Mengulangi dengan cloud, Mendorong dan Menerapkan untuk integrasi cepat.

![LLMOps dengan PromptFlow](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf4aa74db92a318b8cbbf4a608671f6b166216358d3203d8d4.id.png)

## Hebat! Lanjutkan Pembelajaran Anda!

Luar biasa, sekarang pelajari lebih lanjut tentang bagaimana kita menyusun aplikasi untuk menggunakan konsep dengan [Aplikasi Obrolan Contoso](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), untuk memeriksa bagaimana Cloud Advocacy menambahkan konsep-konsep tersebut dalam demonstrasi. Untuk konten lebih lanjut, lihat [sesi breakout Ignite!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Sekarang, lihat Pelajaran 15, untuk memahami bagaimana [Retrieval Augmented Generation dan Database Vektor](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) mempengaruhi AI Generatif dan membuat Aplikasi yang lebih menarik!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan terjemahan yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.