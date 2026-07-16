[![Mengintegrasikan dengan fungsi pemanggilan](../../../translated_images/ms/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Kitaran Hayat Aplikasi AI Generatif

Soalan penting untuk semua aplikasi AI adalah kaitan ciri AI, kerana AI adalah bidang yang berkembang pesat, untuk memastikan aplikasi anda kekal relevan, boleh dipercayai, dan mantap, anda perlu memantau, menilai, dan memperbaikinya secara berterusan. Di sinilah kitaran hayat AI generatif masuk.

Kitaran hayat AI generatif adalah rangka kerja yang membimbing anda melalui peringkat membangunkan, melancarkan, dan menyelenggara aplikasi AI generatif. Ia membantu anda untuk mentakrifkan matlamat anda, mengukur prestasi anda, mengenal pasti cabaran anda, dan melaksanakan penyelesaian anda. Ia juga membantu anda menyelaraskan aplikasi anda dengan piawaian etika dan undang-undang dalam domain anda serta para pemegang kepentingan anda. Dengan mengikuti kitaran hayat AI generatif, anda boleh memastikan aplikasi anda sentiasa memberikan nilai dan memuaskan pengguna anda.

## Pengenalan

Dalam bab ini, anda akan:

- Memahami Peralihan Paradigma dari MLOps ke LLMOps
- Kitaran Hayat LLM
- Alat Kitaran Hayat
- Metrifikasi dan Penilaian Kitaran Hayat

## Memahami Peralihan Paradigma dari MLOps ke LLMOps

LLM adalah alat baru dalam arsenal Kecerdasan Buatan, mereka amat berkuasa dalam tugas analisis dan penjanaan untuk aplikasi, namun kuasa ini mempunyai beberapa akibat dalam cara kita melancarkan tugas AI dan Pembelajaran Mesin Klasik.

Dengan ini, kita memerlukan Paradigma baru untuk menyesuaikan alat ini secara dinamik, dengan insentif yang betul. Kita boleh mengkategorikan aplikasi AI lama sebagai "Aplikasi ML" dan aplikasi AI baru sebagai "Aplikasi GenAI" atau hanya "Aplikasi AI", mencerminkan teknologi dan teknik arus perdana yang digunakan pada masa itu. Ini mengalihkan naratif kita dalam pelbagai cara, lihat perbandingan berikut.

![Perbandingan LLMOps vs. MLOps](../../../translated_images/ms/01-llmops-shift.29bc933cb3bb0080.webp)

Perhatikan bahawa dalam LLMOps, kita lebih fokus kepada Pembangun Aplikasi, menggunakan integrasi sebagai titik utama, menggunakan "Model-sebagai-Perkhidmatan" dan berfikir dalam perkara berikut untuk metrik.

- Kualiti: Kualiti respons
- Kerosakan: AI Bertanggungjawab
- Kejujuran: Keterasasan respons (Adakah masuk akal? Adakah ia betul?)
- Kos: Bajet penyelesaian
- Latensi: Purata masa untuk respons token

## Kitaran Hayat LLM

Pertama, untuk memahami kitaran hayat dan pengubahsuaian, perhatikan infografik seterusnya.

![Infografik LLMOps](../../../translated_images/ms/02-llmops.70a942ead05a7645.webp)

Seperti yang mungkin anda perhatikan, ini berbeza dari Kitaran Hayat biasa dari MLOps. LLM mempunyai banyak keperluan baru, seperti Prompting, teknik berbeza untuk memperbaiki kualiti (Fine-Tuning, RAG, Meta-Prompts), penilaian dan tanggungjawab berbeza dengan AI bertanggungjawab, akhirnya, metrik penilaian baru (Kualiti, Kerosakan, Kejujuran, Kos dan Latensi).

Sebagai contoh, lihat bagaimana kita berideasi. Menggunakan kejuruteraan prompt untuk bereksperimen dengan pelbagai LLM untuk meneroka kemungkinan menguji jika Hipotesis mereka boleh betul.

Perhatikan bahawa ini bukan linear, tetapi gelung terintegrasi, berulang dan dengan kitaran besar yang menyeluruh.

Bagaimana kita boleh meneroka langkah-langkah itu? Mari kita selami secara terperinci bagaimana kita boleh membina kitaran hayat.

![Alir Kerja LLMOps](../../../translated_images/ms/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Ini mungkin kelihatan agak rumit, mari kita fokus pada tiga langkah besar dahulu.

1. Berideasi/Meneroka: Eksplorasi, di sini kita boleh meneroka mengikut keperluan perniagaan kita. Membuat prototaip, mencipta [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) dan menguji jika ia cukup cekap untuk Hipotesis kita.
1. Membina/Memperbaiki: Pelaksanaan, sekarang, kita mula menilai untuk set data yang lebih besar menggunakan teknik seperti Fine-tuning dan RAG untuk memeriksa ketahanan penyelesaian kita. Jika tidak, pelaksanaan semula, menambah langkah baru dalam aliran kita atau menyusun semula data mungkin membantu. Selepas menguji aliran dan skala kita, jika ia berfungsi dan memeriksa Metrik kita, ia sedia untuk langkah seterusnya.
1. Pengoperasian: Integrasi, kini menambah Sistem Pemantauan dan Amaran ke sistem kita, pelaksanaan dan integrasi aplikasi ke Aplikasi kita.

Kemudian, kita mempunyai kitaran besar Pengurusan, memberi tumpuan pada keselamatan, pematuhan dan tadbir urus.

Tahniah, kini anda mempunyai Aplikasi AI anda yang sedia digunakan dan beroperasi. Untuk pengalaman praktikal, lihat pada [Demo Sembang Contoso.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

Sekarang, alat apa yang boleh kita gunakan?

## Alat Kitaran Hayat

Untuk Alat, Microsoft menyediakan [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) dan [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) memudahkan dan menjadikan kitaran anda mudah untuk dilaksanakan dan sedia digunakan.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) membolehkan anda menggunakan [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (dahulu Azure AI Studio) adalah portal web yang membenarkan anda meneroka model, sampel dan alat, mengurus sumber anda, dan menggunakan aliran pembangunan UI serta pilihan SDK/CLI untuk pembangunan Kod-Pertama.

![Kemungkinan Azure AI](../../../translated_images/ms/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI membolehkan anda menggunakan pelbagai sumber untuk mengurus operasi, perkhidmatan, projek, carian vektor dan keperluan pangkalan data.

![LLMOps dengan Azure AI](../../../translated_images/ms/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Membina, dari Proof-of-Concept(POC) hingga aplikasi skala besar dengan PromptFlow:

- Reka dan Bina aplikasi dari VS Code, dengan alat visual dan fungsional
- Uji dan haluskan aplikasi anda untuk AI berkualiti, dengan mudah.
- Gunakan Microsoft Foundry untuk Integrasi dan Iterasi dengan awan, Dorong dan Lancarkan untuk integrasi cepat.

![LLMOps dengan PromptFlow](../../../translated_images/ms/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Hebat! Teruskan Pembelajaran anda!

Hebat, kini pelajari lebih lanjut tentang bagaimana kita menyusun aplikasi untuk menggunakan konsep dengan [Aplikasi Sembang Contoso](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), untuk melihat bagaimana Advocasi Awan menambah konsep-konsep tersebut dalam demonstrasi. Untuk lebih banyak kandungan, lihat sesi pecahan [Ignite!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Kini, lihat Pelajaran 15, untuk memahami bagaimana [Penjanaan Diperkuatkan Pemulihan dan Pangkalan Data Vektor](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) memberi impak kepada AI Generatif dan untuk membuat Aplikasi yang lebih menarik!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->