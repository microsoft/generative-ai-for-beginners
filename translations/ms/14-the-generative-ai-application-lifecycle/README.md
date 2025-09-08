<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "27a5347a5022d5ef0a72ab029b03526a",
  "translation_date": "2025-07-09T15:56:41+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "ms"
}
-->
[![Integrasi dengan pemanggilan fungsi](../../../translated_images/14-lesson-banner.066d74a31727ac121eeac06376a068a397d8e335281e63ce94130d11f516e46b.ms.png)](https://aka.ms/gen-ai-lesson14-gh?WT.mc_id=academic-105485-koreyst)

# Kitaran Hayat Aplikasi AI Generatif

Satu soalan penting bagi semua aplikasi AI ialah sejauh mana ciri AI itu relevan, kerana AI adalah bidang yang berkembang pesat. Untuk memastikan aplikasi anda kekal relevan, boleh dipercayai, dan kukuh, anda perlu memantau, menilai, dan memperbaikinya secara berterusan. Di sinilah kitaran hayat AI generatif memainkan peranan.

Kitaran hayat AI generatif adalah rangka kerja yang membimbing anda melalui peringkat membangunkan, melancarkan, dan menyelenggara aplikasi AI generatif. Ia membantu anda menetapkan matlamat, mengukur prestasi, mengenal pasti cabaran, dan melaksanakan penyelesaian. Ia juga membantu anda menyelaraskan aplikasi anda dengan piawaian etika dan undang-undang dalam domain dan pihak berkepentingan anda. Dengan mengikuti kitaran hayat AI generatif, anda boleh memastikan aplikasi anda sentiasa memberikan nilai dan memuaskan pengguna.

## Pengenalan

Dalam bab ini, anda akan:

- Memahami Peralihan Paradigma dari MLOps ke LLMOps  
- Kitaran Hayat LLM  
- Alat Kitaran Hayat  
- Pengukuran dan Penilaian Kitaran Hayat  

## Memahami Peralihan Paradigma dari MLOps ke LLMOps

LLM adalah alat baru dalam arsenal Kecerdasan Buatan, ia sangat berkuasa dalam tugas analisis dan penjanaan untuk aplikasi, namun kuasa ini membawa beberapa kesan dalam cara kita menyelaraskan tugas AI dan Pembelajaran Mesin Klasik.

Dengan ini, kita memerlukan Paradigma baru untuk menyesuaikan alat ini secara dinamik, dengan insentif yang betul. Kita boleh mengkategorikan aplikasi AI lama sebagai "ML Apps" dan aplikasi AI baru sebagai "GenAI Apps" atau hanya "AI Apps", mencerminkan teknologi dan teknik utama yang digunakan pada masa itu. Ini mengubah naratif kita dalam pelbagai cara, lihat perbandingan berikut.

![Perbandingan LLMOps vs. MLOps](../../../translated_images/01-llmops-shift.29bc933cb3bb0080a562e1655c0c719b71a72c3be6252d5c564b7f598987e602.ms.png)

Perhatikan bahawa dalam LLMOps, kita lebih fokus kepada Pembangun Aplikasi, menggunakan integrasi sebagai titik utama, menggunakan "Models-as-a-Service" dan memikirkan perkara berikut untuk metrik.

- Kualiti: Kualiti respons  
- Kerosakan: AI Bertanggungjawab  
- Kejujuran: Ketepatan respons (Masuk akal? Betul?)  
- Kos: Bajet penyelesaian  
- Latensi: Purata masa untuk respons token  

## Kitaran Hayat LLM

Pertama, untuk memahami kitaran hayat dan pengubahsuaian, perhatikan infografik berikut.

![Infografik LLMOps](../../../translated_images/02-llmops.70a942ead05a7645db740f68727d90160cb438ab71f0fb20548bc7fe5cad83ff.ms.png)

Seperti yang anda perhatikan, ini berbeza daripada Kitaran Hayat biasa dalam MLOps. LLM mempunyai banyak keperluan baru, seperti Prompting, teknik berbeza untuk meningkatkan kualiti (Fine-Tuning, RAG, Meta-Prompts), penilaian dan tanggungjawab berbeza dengan AI bertanggungjawab, dan akhirnya, metrik penilaian baru (Kualiti, Kerosakan, Kejujuran, Kos dan Latensi).

Sebagai contoh, lihat bagaimana kita berfikir. Menggunakan kejuruteraan prompt untuk bereksperimen dengan pelbagai LLM bagi meneroka kemungkinan untuk menguji sama ada Hipotesis mereka boleh betul.

Perlu diingat bahawa ini bukan linear, tetapi gelung yang terintegrasi, berulang dan dengan kitaran menyeluruh.

Bagaimana kita boleh meneroka langkah-langkah ini? Mari kita lihat dengan lebih terperinci bagaimana kita boleh membina kitaran hayat.

![Aliran Kerja LLMOps](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cfa886ed6ba04aa52a096a545e1bc44fa54d7d5983a7201892.ms.png)

Ini mungkin kelihatan agak rumit, mari fokus pada tiga langkah besar dahulu.

1. Ideasi/Penerokaan: Eksplorasi, di sini kita boleh meneroka mengikut keperluan perniagaan kita. Membuat prototaip, mencipta [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) dan menguji sama ada ia cukup cekap untuk Hipotesis kita.  
1. Pembinaan/Peningkatan: Pelaksanaan, sekarang, kita mula menilai untuk set data yang lebih besar, melaksanakan teknik seperti Fine-tuning dan RAG, untuk memeriksa ketahanan penyelesaian kita. Jika tidak, melaksanakan semula, menambah langkah baru dalam aliran atau menyusun semula data mungkin membantu. Selepas menguji aliran dan skala kita, jika ia berfungsi dan metrik kita memuaskan, ia sedia untuk langkah seterusnya.  
1. Pengoperasian: Integrasi, kini menambah Sistem Pemantauan dan Amaran ke dalam sistem, pelancaran dan integrasi aplikasi ke dalam Aplikasi kita.  

Kemudian, kita ada kitaran menyeluruh Pengurusan, yang memberi tumpuan kepada keselamatan, pematuhan dan tadbir urus.

Tahniah, kini aplikasi AI anda sudah sedia dan beroperasi. Untuk pengalaman praktikal, lihat [Demo Contoso Chat.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Sekarang, alat apa yang boleh kita gunakan?

## Alat Kitaran Hayat

Untuk alat, Microsoft menyediakan [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) dan [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) yang memudahkan dan menjadikan kitaran anda mudah dilaksanakan dan sedia digunakan.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) membolehkan anda menggunakan [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio adalah portal web yang membolehkan anda meneroka model, contoh dan alat. Mengurus sumber anda, aliran pembangunan UI dan pilihan SDK/CLI untuk pembangunan berasaskan kod.

![Kemungkinan Azure AI](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8b166e194928f057074843d1955177baf0f5b53d50d7b6153.ms.png)

Azure AI membolehkan anda menggunakan pelbagai sumber untuk mengurus operasi, perkhidmatan, projek, carian vektor dan keperluan pangkalan data anda.

![LLMOps dengan Azure AI](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf95420668e3464aae70d8b22275a744254e941dd5e73ae0d2.ms.png)

Membina, dari Proof-of-Concept (POC) hingga aplikasi skala besar dengan PromptFlow:

- Reka dan bina aplikasi dari VS Code, dengan alat visual dan fungsi  
- Uji dan laraskan aplikasi anda untuk AI berkualiti dengan mudah  
- Gunakan Azure AI Studio untuk Integrasi dan Iterasi dengan awan, Tolak dan Lancarkan untuk integrasi pantas  

![LLMOps dengan PromptFlow](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf4aa74db92a318b8cbbf4a608671f6b166216358d3203d8d4.ms.png)

## Hebat! Teruskan Pembelajaran Anda!

Hebat, kini pelajari lebih lanjut tentang bagaimana kita menyusun aplikasi untuk menggunakan konsep ini dengan [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), untuk melihat bagaimana Cloud Advocacy menambah konsep ini dalam demonstrasi. Untuk lebih banyak kandungan, tonton sesi pecahan [Ignite!](https://www.youtube.com/watch?v=DdOylyrTOWg)

Sekarang, lihat Pelajaran 15, untuk memahami bagaimana [Retrieval Augmented Generation dan Pangkalan Data Vektor](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) memberi impak kepada AI Generatif dan menjadikan Aplikasi lebih menarik!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.