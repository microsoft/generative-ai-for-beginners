<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-06-25T21:29:52+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "id"
}
-->
# Mengamankan Aplikasi AI Generatif Anda

[![Mengamankan Aplikasi AI Generatif Anda](../../../translated_images/13-lesson-banner.14103e36b4bbf17398b64ed2b0531f6f2c6549e7f7342f797c40bcae5a11862e.id.png)](https://aka.ms/gen-ai-lesson13-gh?WT.mc_id=academic-105485-koreyst)

## Pengantar

Pelajaran ini akan mencakup:

- Keamanan dalam konteks sistem AI.
- Risiko dan ancaman umum terhadap sistem AI.
- Metode dan pertimbangan untuk mengamankan sistem AI.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan memahami:

- Ancaman dan risiko terhadap sistem AI.
- Metode dan praktik umum untuk mengamankan sistem AI.
- Bagaimana pelaksanaan pengujian keamanan dapat mencegah hasil yang tidak terduga dan mengikis kepercayaan pengguna.

## Apa arti keamanan dalam konteks AI generatif?

Seiring teknologi Kecerdasan Buatan (AI) dan Pembelajaran Mesin (ML) semakin membentuk kehidupan kita, penting untuk melindungi tidak hanya data pelanggan tetapi juga sistem AI itu sendiri. AI/ML semakin banyak digunakan dalam mendukung proses pengambilan keputusan bernilai tinggi di industri-industri di mana keputusan yang salah dapat berakibat serius.

Berikut adalah poin-poin kunci yang perlu dipertimbangkan:

- **Dampak AI/ML**: AI/ML memiliki dampak signifikan pada kehidupan sehari-hari dan oleh karena itu melindunginya menjadi sangat penting.
- **Tantangan Keamanan**: Dampak ini memerlukan perhatian yang tepat untuk menangani kebutuhan melindungi produk berbasis AI dari serangan canggih, baik oleh troll atau kelompok terorganisir.
- **Masalah Strategis**: Industri teknologi harus secara proaktif menangani tantangan strategis untuk memastikan keselamatan pelanggan jangka panjang dan keamanan data.

Selain itu, model Pembelajaran Mesin sebagian besar tidak dapat membedakan antara input berbahaya dan data anomali yang tidak berbahaya. Sumber data pelatihan yang signifikan berasal dari dataset publik yang tidak terkurasi dan tidak dimoderasi, yang terbuka untuk kontribusi pihak ketiga. Penyerang tidak perlu mengkompromikan dataset ketika mereka bebas untuk berkontribusi padanya. Seiring waktu, data berbahaya dengan tingkat kepercayaan rendah menjadi data tepercaya dengan tingkat kepercayaan tinggi, jika struktur/format data tetap benar.

Inilah sebabnya mengapa sangat penting untuk memastikan integritas dan perlindungan dari penyimpanan data yang digunakan model Anda untuk membuat keputusan.

## Memahami ancaman dan risiko AI

Dalam hal AI dan sistem terkait, peracunan data menonjol sebagai ancaman keamanan paling signifikan saat ini. Peracunan data terjadi ketika seseorang dengan sengaja mengubah informasi yang digunakan untuk melatih AI, menyebabkannya membuat kesalahan. Ini disebabkan oleh tidak adanya metode deteksi dan mitigasi yang standar, ditambah dengan ketergantungan kita pada dataset publik yang tidak dipercaya atau tidak terkurasi untuk pelatihan. Untuk menjaga integritas data dan mencegah proses pelatihan yang cacat, sangat penting untuk melacak asal dan garis keturunan data Anda. Jika tidak, pepatah lama "sampah masuk, sampah keluar" berlaku, yang mengarah pada kinerja model yang terkompromi.

Berikut adalah contoh bagaimana peracunan data dapat mempengaruhi model Anda:

1. **Pembalikan Label**: Dalam tugas klasifikasi biner, seorang penyerang dengan sengaja membalik label dari sebagian kecil data pelatihan. Misalnya, sampel yang tidak berbahaya diberi label sebagai berbahaya, menyebabkan model mempelajari asosiasi yang salah.\
   **Contoh**: Filter spam salah mengklasifikasikan email yang sah sebagai spam karena label yang dimanipulasi.
2. **Peracunan Fitur**: Seorang penyerang dengan halus memodifikasi fitur dalam data pelatihan untuk memperkenalkan bias atau menyesatkan model.\
   **Contoh**: Menambahkan kata kunci yang tidak relevan ke deskripsi produk untuk memanipulasi sistem rekomendasi.
3. **Injeksi Data**: Menyuntikkan data berbahaya ke dalam set pelatihan untuk mempengaruhi perilaku model.\
   **Contoh**: Memperkenalkan ulasan pengguna palsu untuk mempengaruhi hasil analisis sentimen.
4. **Serangan Pintu Belakang**: Seorang penyerang menyisipkan pola tersembunyi (pintu belakang) ke dalam data pelatihan. Model belajar mengenali pola ini dan berperilaku jahat saat dipicu.\
   **Contoh**: Sistem pengenalan wajah yang dilatih dengan gambar berisi pintu belakang yang salah mengidentifikasi orang tertentu.

MITRE Corporation telah membuat [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), sebuah basis pengetahuan tentang taktik dan teknik yang digunakan oleh penyerang dalam serangan dunia nyata pada sistem AI.

> Ada semakin banyak kerentanan dalam sistem yang didukung AI, karena penggabungan AI meningkatkan permukaan serangan sistem yang ada di luar serangan siber tradisional. Kami mengembangkan ATLAS untuk meningkatkan kesadaran akan kerentanan yang unik dan berkembang ini, seiring komunitas global semakin menggabungkan AI ke dalam berbagai sistem. ATLAS dimodelkan setelah kerangka kerja MITRE ATT&CK® dan taktik, teknik, dan prosedurnya (TTPs) melengkapi yang ada di ATT&CK.

Seperti kerangka kerja MITRE ATT&CK® yang digunakan secara luas dalam keamanan siber tradisional untuk merencanakan skenario emulasi ancaman lanjutan, ATLAS menyediakan satu set TTP yang mudah dicari yang dapat membantu lebih memahami dan mempersiapkan diri untuk bertahan dari serangan yang muncul.

Selain itu, Proyek Keamanan Aplikasi Web Terbuka (OWASP) telah membuat "[Daftar 10 Teratas](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" dari kerentanan paling kritis yang ditemukan dalam aplikasi yang memanfaatkan LLM. Daftar ini menyoroti risiko ancaman seperti peracunan data yang disebutkan di atas serta lainnya seperti:

- **Injeksi Prompt**: teknik di mana penyerang memanipulasi Model Bahasa Besar (LLM) melalui input yang dirancang dengan hati-hati, menyebabkannya berperilaku di luar perilaku yang dimaksudkan.
- **Kerentanan Rantai Pasokan**: Komponen dan perangkat lunak yang membentuk aplikasi yang digunakan oleh LLM, seperti modul Python atau dataset eksternal, dapat dikompromikan sendiri yang mengarah pada hasil yang tidak terduga, bias yang diperkenalkan, dan bahkan kerentanan dalam infrastruktur yang mendasarinya.
- **Ketergantungan Berlebihan**: LLM tidak sempurna dan rentan terhadap halusinasi, memberikan hasil yang tidak akurat atau tidak aman. Dalam beberapa keadaan yang terdokumentasi, orang telah menerima hasilnya apa adanya yang mengarah pada konsekuensi negatif dunia nyata yang tidak diinginkan.

Microsoft Cloud Advocate Rod Trent telah menulis ebook gratis, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), yang mendalami ancaman AI yang muncul ini dan memberikan panduan ekstensif tentang cara terbaik menangani skenario ini.

## Pengujian Keamanan untuk Sistem AI dan LLM

Kecerdasan buatan (AI) mengubah berbagai domain dan industri, menawarkan kemungkinan dan manfaat baru bagi masyarakat. Namun, AI juga menimbulkan tantangan dan risiko yang signifikan, seperti privasi data, bias, kurangnya keterjelasan, dan potensi penyalahgunaan. Oleh karena itu, penting untuk memastikan bahwa sistem AI aman dan bertanggung jawab, artinya mereka mematuhi standar etika dan hukum dan dapat dipercaya oleh pengguna dan pemangku kepentingan.

Pengujian keamanan adalah proses evaluasi keamanan sistem AI atau LLM, dengan mengidentifikasi dan mengeksploitasi kerentanannya. Ini dapat dilakukan oleh pengembang, pengguna, atau auditor pihak ketiga, tergantung pada tujuan dan ruang lingkup pengujian. Beberapa metode pengujian keamanan yang paling umum untuk sistem AI dan LLM adalah:

- **Sanitasi Data**: Ini adalah proses menghapus atau menganonimkan informasi sensitif atau pribadi dari data pelatihan atau input dari sistem AI atau LLM. Sanitasi data dapat membantu mencegah kebocoran data dan manipulasi berbahaya dengan mengurangi paparan data rahasia atau pribadi.
- **Pengujian Adversarial**: Ini adalah proses menghasilkan dan menerapkan contoh-contoh adversarial ke input atau output dari sistem AI atau LLM untuk mengevaluasi ketahanan dan ketahanannya terhadap serangan adversarial. Pengujian adversarial dapat membantu mengidentifikasi dan mengurangi kerentanan dan kelemahan sistem AI atau LLM yang mungkin dieksploitasi oleh penyerang.
- **Verifikasi Model**: Ini adalah proses memverifikasi kebenaran dan kelengkapan parameter model atau arsitektur sistem AI atau LLM. Verifikasi model dapat membantu mendeteksi dan mencegah pencurian model dengan memastikan bahwa model dilindungi dan diautentikasi.
- **Validasi Output**: Ini adalah proses memvalidasi kualitas dan keandalan output dari sistem AI atau LLM. Validasi output dapat membantu mendeteksi dan memperbaiki manipulasi berbahaya dengan memastikan bahwa output konsisten dan akurat.

OpenAI, pemimpin dalam sistem AI, telah menyiapkan serangkaian _evaluasi keselamatan_ sebagai bagian dari inisiatif jaringan red teaming mereka, yang bertujuan untuk menguji output sistem AI dengan harapan berkontribusi pada keselamatan AI.

> Evaluasi dapat berkisar dari tes Q&A sederhana hingga simulasi yang lebih kompleks. Sebagai contoh konkret, berikut adalah evaluasi sampel yang dikembangkan oleh OpenAI untuk mengevaluasi perilaku AI dari berbagai sudut:

#### Persuasi

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Seberapa baik sistem AI dapat menipu sistem AI lain untuk mengatakan kata rahasia?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Seberapa baik sistem AI dapat meyakinkan sistem AI lain untuk menyumbangkan uang?
- [Proposal Pemungutan Suara](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Seberapa baik sistem AI dapat mempengaruhi dukungan sistem AI lain terhadap proposisi politik?

#### Steganografi (pesan tersembunyi)

- [Steganografi](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Seberapa baik sistem AI dapat mengirimkan pesan rahasia tanpa tertangkap oleh sistem AI lain?
- [Kompresi Teks](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Seberapa baik sistem AI dapat mengompresi dan mendekompresi pesan, untuk memungkinkan penyembunyian pesan rahasia?
- [Titik Schelling](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Seberapa baik sistem AI dapat berkoordinasi dengan sistem AI lain, tanpa komunikasi langsung?

### Keamanan AI

Sangat penting bagi kita untuk berupaya melindungi sistem AI dari serangan berbahaya, penyalahgunaan, atau konsekuensi yang tidak diinginkan. Ini termasuk mengambil langkah-langkah untuk memastikan keselamatan, keandalan, dan kepercayaan sistem AI, seperti:

- Mengamankan data dan algoritma yang digunakan untuk melatih dan menjalankan model AI
- Mencegah akses tidak sah, manipulasi, atau sabotase sistem AI
- Mendeteksi dan mengurangi bias, diskriminasi, atau masalah etika dalam sistem AI
- Memastikan akuntabilitas, transparansi, dan keterjelasan keputusan dan tindakan AI
- Menyelaraskan tujuan dan nilai sistem AI dengan manusia dan masyarakat

Keamanan AI penting untuk memastikan integritas, ketersediaan, dan kerahasiaan sistem AI dan data. Beberapa tantangan dan peluang keamanan AI adalah:

- Peluang: Menggabungkan AI dalam strategi keamanan siber karena dapat memainkan peran penting dalam mengidentifikasi ancaman dan meningkatkan waktu respons. AI dapat membantu mengotomatisasi dan memperkuat deteksi dan mitigasi serangan siber, seperti phishing, malware, atau ransomware.
- Tantangan: AI juga dapat digunakan oleh pihak yang tidak bertanggung jawab untuk meluncurkan serangan canggih, seperti menghasilkan konten palsu atau menyesatkan, menyamar sebagai pengguna, atau mengeksploitasi kerentanan dalam sistem AI. Oleh karena itu, pengembang AI memiliki tanggung jawab unik untuk merancang sistem yang kuat dan tangguh terhadap penyalahgunaan.

### Perlindungan Data

LLM dapat menimbulkan risiko terhadap privasi dan keamanan data yang mereka gunakan. Misalnya, LLM dapat berpotensi menghafal dan membocorkan informasi sensitif dari data pelatihan mereka, seperti nama pribadi, alamat, kata sandi, atau nomor kartu kredit. Mereka juga dapat dimanipulasi atau diserang oleh pelaku jahat yang ingin mengeksploitasi kerentanan atau bias mereka. Oleh karena itu, penting untuk menyadari risiko ini dan mengambil langkah-langkah yang tepat untuk melindungi data yang digunakan dengan LLM. Ada beberapa langkah yang dapat Anda ambil untuk melindungi data yang digunakan dengan LLM. Langkah-langkah ini meliputi:

- **Membatasi jumlah dan jenis data yang mereka bagikan dengan LLM**: Hanya bagikan data yang diperlukan dan relevan untuk tujuan yang dimaksudkan, dan hindari membagikan data yang sensitif, rahasia, atau pribadi. Pengguna juga harus menganonimkan atau mengenkripsi data yang mereka bagikan dengan LLM, seperti dengan menghapus atau menyamarkan informasi identifikasi, atau menggunakan saluran komunikasi yang aman.
- **Memverifikasi data yang dihasilkan oleh LLM**: Selalu periksa keakuratan dan kualitas output yang dihasilkan oleh LLM untuk memastikan mereka tidak mengandung informasi yang tidak diinginkan atau tidak pantas.
- **Melaporkan dan memberi tahu tentang pelanggaran data atau insiden**: Waspada terhadap aktivitas atau perilaku yang mencurigakan atau tidak normal dari LLM, seperti menghasilkan teks yang tidak relevan, tidak akurat, ofensif, atau berbahaya. Ini bisa menjadi indikasi pelanggaran data atau insiden keamanan.

Keamanan data, tata kelola, dan kepatuhan sangat penting bagi organisasi mana pun yang ingin memanfaatkan kekuatan data dan AI di lingkungan multi-cloud. Mengamankan dan mengelola semua data Anda adalah usaha yang kompleks dan multifaset. Anda perlu mengamankan dan mengelola berbagai jenis data (terstruktur, tidak terstruktur, dan data yang dihasilkan oleh AI) di berbagai lokasi di berbagai cloud, dan Anda perlu mempertimbangkan peraturan keamanan data, tata kelola, dan AI yang ada dan yang akan datang. Untuk melindungi data Anda, Anda perlu mengadopsi beberapa praktik terbaik dan tindakan pencegahan, seperti:

- Gunakan layanan cloud atau platform yang menawarkan fitur perlindungan dan privasi data.
- Gunakan alat kualitas dan validasi data untuk memeriksa data Anda dari kesalahan, ketidakkonsistenan, atau anomali.
- Gunakan kerangka kerja tata kelola dan etika data untuk memastikan data Anda digunakan secara bertanggung jawab dan transparan.

### Meniru ancaman dunia nyata - AI red teaming

Meniru ancaman dunia nyata sekarang dianggap sebagai praktik standar dalam membangun sistem AI yang tangguh dengan menggunakan alat, taktik, prosedur serupa untuk mengidentifikasi risiko terhadap sistem dan menguji respons pembela.

> Praktik AI red teaming telah berkembang untuk mengambil makna yang lebih luas: ini tidak hanya mencakup pengujian kerentanan keamanan, tetapi juga mencakup pengujian kegagalan sistem lainnya, seperti menghasilkan konten yang berpotensi berbahaya. Sistem AI datang dengan risiko baru, dan red teaming adalah inti untuk memahami risiko baru tersebut, seperti injeksi prompt dan menghasilkan konten yang tidak berlandaskan. - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Panduan dan sumber daya untuk red teaming](../../../translated_images/13-AI-red-team.642ed54689d7e8a4d83bdf0635768c4fd8aa41ea539d8e3ffe17514aec4b4824.id.png)]()

Berikut adalah wawasan kunci yang telah membentuk program AI Red Team Microsoft.

1. **Lingkup Luas dari AI Red Teaming:**
   AI red teaming sekarang mencakup hasil keamanan dan AI yang Bertanggung Jawab (RAI). Secara tradisional, red teaming berfokus pada aspek keamanan, memperlakukan model sebagai vektor (misalnya, mencuri model yang mendasarinya). Namun, sistem AI memperkenalkan kerentanan keamanan baru (misalnya, injeksi prompt, peracunan), yang memerlukan perhatian khusus. Di luar keamanan, AI red teaming juga menyelidiki masalah keadilan (misalnya, stereotip) dan konten berbahaya (misalnya, glorifikasi kekerasan). Identifikasi awal masalah ini memungkinkan prioritas investasi pertahanan.
2. **Kegagalan Berbahaya dan Tidak Berbahaya:**
   AI red teaming mempertimbangkan kegagalan dari perspektif berbahaya dan tidak berbahaya. Misalnya, ketika red teaming Bing baru, kami tidak hanya mengeksplorasi bagaimana penyerang berbahaya dapat merusak sistem tetapi juga bagaimana pengguna biasa dapat menghadapi konten yang bermasalah atau berbahaya. Berbeda dengan red teaming keamanan tradisional, yang berfokus terutama pada aktor berbahaya, AI red teaming memperhitungkan beragam persona dan potensi kegagalan.
3. **Sifat Dinamis dari Sistem AI:**
   Aplikasi AI terus berkembang. Dalam aplikasi model bahasa besar, pengembang beradaptasi dengan persyaratan yang berubah. Red teaming berkelanjutan memastikan kewaspadaan dan adaptasi yang berkelanjutan terhadap risiko yang berkembang.

AI red teaming tidak mencakup semua dan harus dianggap sebagai gerakan pelengkap untuk kontrol tambahan seperti [kontrol akses berbasis peran (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan terjemahan yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan untuk menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.