<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b9d32511b27373a1b21b5789d4fda057",
  "translation_date": "2025-10-17T20:46:52+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "id"
}
-->
[![Mengintegrasikan dengan pemanggilan fungsi](../../../translated_images/14-lesson-banner.066d74a31727ac121eeac06376a068a397d8e335281e63ce94130d11f516e46b.id.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Siklus Hidup Aplikasi AI Generatif

Pertanyaan penting untuk semua aplikasi AI adalah relevansi fitur AI, karena AI adalah bidang yang berkembang pesat. Untuk memastikan aplikasi Anda tetap relevan, andal, dan tangguh, Anda perlu memantau, mengevaluasi, dan meningkatkannya secara terus-menerus. Di sinilah siklus hidup AI generatif berperan.

Siklus hidup AI generatif adalah kerangka kerja yang membimbing Anda melalui tahap-tahap pengembangan, penerapan, dan pemeliharaan aplikasi AI generatif. Kerangka ini membantu Anda mendefinisikan tujuan, mengukur kinerja, mengidentifikasi tantangan, dan menerapkan solusi. Selain itu, kerangka ini membantu Anda menyelaraskan aplikasi dengan standar etika dan hukum di bidang Anda serta para pemangku kepentingan. Dengan mengikuti siklus hidup AI generatif, Anda dapat memastikan bahwa aplikasi Anda selalu memberikan nilai dan memenuhi kebutuhan pengguna.

## Pendahuluan

Dalam bab ini, Anda akan:

- Memahami Perubahan Paradigma dari MLOps ke LLMOps
- Siklus Hidup LLM
- Alat untuk Siklus Hidup
- Metrifikasi dan Evaluasi Siklus Hidup

## Memahami Perubahan Paradigma dari MLOps ke LLMOps

LLM adalah alat baru dalam dunia Kecerdasan Buatan, yang sangat kuat dalam tugas analisis dan generasi untuk aplikasi. Namun, kekuatan ini memiliki konsekuensi dalam cara kita menyederhanakan tugas AI dan Pembelajaran Mesin Klasik.

Dengan ini, kita memerlukan Paradigma baru untuk menyesuaikan alat ini secara dinamis, dengan insentif yang tepat. Kita dapat mengkategorikan aplikasi AI lama sebagai "Aplikasi ML" dan aplikasi AI baru sebagai "Aplikasi GenAI" atau hanya "Aplikasi AI", mencerminkan teknologi dan teknik utama yang digunakan pada saat itu. Perubahan ini menggeser narasi kita dalam berbagai cara, lihat perbandingan berikut.

![Perbandingan LLMOps vs. MLOps](../../../translated_images/01-llmops-shift.29bc933cb3bb0080a562e1655c0c719b71a72c3be6252d5c564b7f598987e602.id.png)

Perhatikan bahwa dalam LLMOps, kita lebih fokus pada Pengembang Aplikasi, menggunakan integrasi sebagai poin utama, menggunakan "Model-sebagai-Layanan" dan memikirkan poin-poin berikut untuk metrik.

- Kualitas: Kualitas respons
- Bahaya: AI yang bertanggung jawab
- Kejujuran: Dasar respons (Masuk akal? Apakah benar?)
- Biaya: Anggaran solusi
- Latensi: Waktu rata-rata untuk respons token

## Siklus Hidup LLM

Pertama, untuk memahami siklus hidup dan modifikasinya, mari kita perhatikan infografis berikut.

![Infografis LLMOps](../../../translated_images/02-llmops.70a942ead05a7645db740f68727d90160cb438ab71f0fb20548bc7fe5cad83ff.id.png)

Seperti yang Anda lihat, ini berbeda dari siklus hidup biasa dalam MLOps. LLM memiliki banyak persyaratan baru, seperti Prompting, teknik berbeda untuk meningkatkan kualitas (Fine-Tuning, RAG, Meta-Prompts), penilaian dan tanggung jawab dengan AI yang bertanggung jawab, serta metrik evaluasi baru (Kualitas, Bahaya, Kejujuran, Biaya, dan Latensi).

Sebagai contoh, perhatikan bagaimana kita mengembangkan ide. Menggunakan teknik prompt engineering untuk bereksperimen dengan berbagai LLM guna mengeksplorasi kemungkinan dan menguji apakah hipotesis mereka dapat benar.

Perlu dicatat bahwa ini bukan proses linear, melainkan loop terintegrasi, iteratif, dan dengan siklus yang menyeluruh.

Bagaimana kita bisa mengeksplorasi langkah-langkah tersebut? Mari kita bahas secara detail bagaimana kita bisa membangun siklus hidup.

![Alur Kerja LLMOps](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cfa886ed6ba04aa52a096a545e1bc44fa54d7d5983a7201892.id.png)

Ini mungkin terlihat agak rumit, mari kita fokus pada tiga langkah besar terlebih dahulu.

1. Mengembangkan Ide/Mengeksplorasi: Eksplorasi, di sini kita dapat mengeksplorasi sesuai kebutuhan bisnis kita. Membuat prototipe, menciptakan [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) dan menguji apakah cukup efisien untuk hipotesis kita.
2. Membangun/Meningkatkan: Implementasi, sekarang kita mulai mengevaluasi dataset yang lebih besar, menerapkan teknik seperti Fine-tuning dan RAG untuk memeriksa ketangguhan solusi kita. Jika tidak berhasil, kita dapat mengimplementasikan ulang, menambahkan langkah baru dalam alur kita, atau merestrukturisasi data. Setelah menguji alur dan skala kita, jika berhasil dan memenuhi metrik kita, maka siap untuk langkah berikutnya.
3. Mengoperasionalkan: Integrasi, sekarang menambahkan sistem pemantauan dan peringatan ke sistem kita, penerapan, dan integrasi aplikasi ke dalam aplikasi kita.

Kemudian, kita memiliki siklus menyeluruh tentang Manajemen, yang berfokus pada keamanan, kepatuhan, dan tata kelola.

Selamat, sekarang aplikasi AI Anda siap digunakan dan dioperasikan. Untuk pengalaman langsung, lihat [Demo Contoso Chat.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Sekarang, alat apa yang bisa kita gunakan?

## Alat untuk Siklus Hidup

Untuk alat, Microsoft menyediakan [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) dan [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) untuk mempermudah implementasi siklus Anda dan siap digunakan.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) memungkinkan Anda menggunakan [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio adalah portal web yang memungkinkan Anda mengeksplorasi model, sampel, dan alat. Mengelola sumber daya Anda, alur pengembangan UI, dan opsi SDK/CLI untuk pengembangan berbasis kode.

![Kemungkinan Azure AI](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8b166e194928f057074843d1955177baf0f5b53d50d7b6153.id.png)

Azure AI memungkinkan Anda menggunakan berbagai sumber daya untuk mengelola operasi, layanan, proyek, pencarian vektor, dan kebutuhan basis data Anda.

![LLMOps dengan Azure AI](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf95420668e3464aae70d8b22275a744254e941dd5e73ae0d2.id.png)

Bangun, dari Proof-of-Concept (POC) hingga aplikasi skala besar dengan PromptFlow:

- Desain dan Bangun aplikasi dari VS Code, dengan alat visual dan fungsional
- Uji dan sesuaikan aplikasi Anda untuk kualitas AI dengan mudah.
- Gunakan Azure AI Studio untuk mengintegrasikan dan mengiterasi dengan cloud, Push dan Deploy untuk integrasi cepat.

![LLMOps dengan PromptFlow](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf4aa74db92a318b8cbbf4a608671f6b166216358d3203d8d4.id.png)

## Hebat! Lanjutkan Pembelajaran Anda!

Luar biasa, sekarang pelajari lebih lanjut tentang bagaimana kita menyusun aplikasi untuk menggunakan konsep-konsep tersebut dengan [Aplikasi Contoso Chat](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), untuk melihat bagaimana Cloud Advocacy menambahkan konsep-konsep tersebut dalam demonstrasi. Untuk konten lebih lanjut, lihat [sesi breakout Ignite!](https://www.youtube.com/watch?v=DdOylyrTOWg)

Sekarang, lihat Pelajaran 15, untuk memahami bagaimana [Retrieval Augmented Generation dan Basis Data Vektor](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) memengaruhi AI Generatif dan membuat aplikasi lebih menarik!

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.