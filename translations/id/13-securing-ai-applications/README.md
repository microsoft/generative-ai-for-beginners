<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2faf8ee7a0b851efa647a19788f1e5b",
  "translation_date": "2025-10-17T20:43:37+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "id"
}
-->
# Mengamankan Aplikasi AI Generatif Anda

[![Mengamankan Aplikasi AI Generatif Anda](../../../translated_images/13-lesson-banner.14103e36b4bbf17398b64ed2b0531f6f2c6549e7f7342f797c40bcae5a11862e.id.png)](https://youtu.be/m0vXwsx5DNg?si=TYkr936GMKz15K0L)

## Pendahuluan

Pelajaran ini akan membahas:

- Keamanan dalam konteks sistem AI.
- Risiko dan ancaman umum terhadap sistem AI.
- Metode dan pertimbangan untuk mengamankan sistem AI.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan memahami:

- Ancaman dan risiko terhadap sistem AI.
- Metode dan praktik umum untuk mengamankan sistem AI.
- Bagaimana pengujian keamanan dapat mencegah hasil yang tidak diinginkan dan mengurangi hilangnya kepercayaan pengguna.

## Apa arti keamanan dalam konteks AI generatif?

Seiring teknologi Kecerdasan Buatan (AI) dan Pembelajaran Mesin (ML) semakin memengaruhi kehidupan kita, sangat penting untuk melindungi tidak hanya data pelanggan tetapi juga sistem AI itu sendiri. AI/ML semakin banyak digunakan untuk mendukung proses pengambilan keputusan bernilai tinggi di industri di mana keputusan yang salah dapat mengakibatkan konsekuensi serius.

Berikut adalah poin-poin penting yang perlu dipertimbangkan:

- **Dampak AI/ML**: AI/ML memiliki dampak signifikan pada kehidupan sehari-hari, sehingga melindunginya menjadi hal yang sangat penting.
- **Tantangan Keamanan**: Dampak yang dimiliki AI/ML memerlukan perhatian yang tepat untuk mengatasi kebutuhan melindungi produk berbasis AI dari serangan canggih, baik oleh troll maupun kelompok terorganisir.
- **Masalah Strategis**: Industri teknologi harus secara proaktif mengatasi tantangan strategis untuk memastikan keselamatan pelanggan jangka panjang dan keamanan data.

Selain itu, model Pembelajaran Mesin sebagian besar tidak mampu membedakan antara input berbahaya dan data anomali yang tidak berbahaya. Sumber data pelatihan yang signifikan berasal dari dataset publik yang tidak terkurasi dan tidak dimoderasi, yang terbuka untuk kontribusi pihak ketiga. Penyerang tidak perlu merusak dataset jika mereka bebas untuk berkontribusi padanya. Seiring waktu, data berbahaya dengan tingkat kepercayaan rendah dapat menjadi data yang dipercaya dengan tingkat kepercayaan tinggi, jika struktur/format data tetap benar.

Inilah mengapa sangat penting untuk memastikan integritas dan perlindungan penyimpanan data yang digunakan model Anda untuk membuat keputusan.

## Memahami ancaman dan risiko AI

Dalam hal AI dan sistem terkait, peracunan data adalah ancaman keamanan yang paling signifikan saat ini. Peracunan data terjadi ketika seseorang dengan sengaja mengubah informasi yang digunakan untuk melatih AI, sehingga menyebabkan AI membuat kesalahan. Hal ini disebabkan oleh tidak adanya metode deteksi dan mitigasi yang standar, ditambah dengan ketergantungan kita pada dataset publik yang tidak terpercaya atau tidak terkurasi untuk pelatihan. Untuk menjaga integritas data dan mencegah proses pelatihan yang cacat, sangat penting untuk melacak asal dan garis keturunan data Anda. Jika tidak, pepatah lama "sampah masuk, sampah keluar" akan berlaku, yang mengakibatkan kinerja model yang terganggu.

Berikut adalah contoh bagaimana peracunan data dapat memengaruhi model Anda:

1. **Label Flipping**: Dalam tugas klasifikasi biner, pelaku dengan sengaja membalik label dari sebagian kecil data pelatihan. Misalnya, sampel yang tidak berbahaya diberi label sebagai berbahaya, sehingga model mempelajari asosiasi yang salah.\
   **Contoh**: Filter spam yang salah mengklasifikasikan email yang sah sebagai spam karena label yang dimanipulasi.
2. **Feature Poisoning**: Penyerang secara halus memodifikasi fitur dalam data pelatihan untuk memperkenalkan bias atau menyesatkan model.\
   **Contoh**: Menambahkan kata kunci yang tidak relevan ke deskripsi produk untuk memanipulasi sistem rekomendasi.
3. **Data Injection**: Menyuntikkan data berbahaya ke dalam set pelatihan untuk memengaruhi perilaku model.\
   **Contoh**: Memasukkan ulasan pengguna palsu untuk memengaruhi hasil analisis sentimen.
4. **Serangan Backdoor**: Pelaku menyisipkan pola tersembunyi (backdoor) ke dalam data pelatihan. Model belajar mengenali pola ini dan berperilaku jahat saat dipicu.\
   **Contoh**: Sistem pengenalan wajah yang dilatih dengan gambar yang memiliki backdoor sehingga salah mengidentifikasi orang tertentu.

MITRE Corporation telah membuat [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), sebuah basis pengetahuan tentang taktik dan teknik yang digunakan oleh pelaku dalam serangan nyata terhadap sistem AI.

> Ada semakin banyak kerentanan dalam sistem yang didukung AI, karena penggabungan AI meningkatkan permukaan serangan dari sistem yang ada di luar serangan siber tradisional. Kami mengembangkan ATLAS untuk meningkatkan kesadaran akan kerentanan unik dan yang terus berkembang ini, karena komunitas global semakin mengintegrasikan AI ke dalam berbagai sistem. ATLAS dimodelkan setelah kerangka kerja MITRE ATT&CK® dan taktik, teknik, dan prosedur (TTP) yang dimilikinya melengkapi yang ada di ATT&CK.

Seperti halnya kerangka kerja MITRE ATT&CK®, yang banyak digunakan dalam keamanan siber tradisional untuk merencanakan skenario emulasi ancaman tingkat lanjut, ATLAS menyediakan kumpulan TTP yang mudah dicari yang dapat membantu memahami dan mempersiapkan diri untuk menghadapi serangan yang muncul.

Selain itu, Open Web Application Security Project (OWASP) telah membuat "[Daftar 10 Teratas](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" dari kerentanan paling kritis yang ditemukan dalam aplikasi yang menggunakan LLM. Daftar ini menyoroti risiko ancaman seperti peracunan data yang disebutkan sebelumnya, bersama dengan ancaman lainnya seperti:

- **Prompt Injection**: teknik di mana penyerang memanipulasi Model Bahasa Besar (LLM) melalui input yang dirancang dengan hati-hati, menyebabkan model berperilaku di luar perilaku yang dimaksudkan.
- **Kerentanan Rantai Pasokan**: Komponen dan perangkat lunak yang membentuk aplikasi yang digunakan oleh LLM, seperti modul Python atau dataset eksternal, dapat dikompromikan sehingga menghasilkan hasil yang tidak terduga, bias yang diperkenalkan, dan bahkan kerentanan dalam infrastruktur dasar.
- **Ketergantungan Berlebihan**: LLM rentan terhadap kesalahan dan sering kali memberikan hasil yang tidak akurat atau tidak aman. Dalam beberapa kasus yang terdokumentasi, orang menerima hasil tersebut begitu saja, yang menyebabkan konsekuensi negatif di dunia nyata.

Microsoft Cloud Advocate Rod Trent telah menulis ebook gratis, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), yang membahas secara mendalam ancaman AI yang muncul dan memberikan panduan luas tentang cara terbaik menghadapi skenario ini.

## Pengujian Keamanan untuk Sistem AI dan LLM

Kecerdasan buatan (AI) sedang mengubah berbagai domain dan industri, menawarkan kemungkinan dan manfaat baru bagi masyarakat. Namun, AI juga menghadirkan tantangan dan risiko yang signifikan, seperti privasi data, bias, kurangnya penjelasan, dan potensi penyalahgunaan. Oleh karena itu, sangat penting untuk memastikan bahwa sistem AI aman dan bertanggung jawab, yang berarti bahwa mereka mematuhi standar etika dan hukum serta dapat dipercaya oleh pengguna dan pemangku kepentingan.

Pengujian keamanan adalah proses mengevaluasi keamanan sistem AI atau LLM, dengan mengidentifikasi dan mengeksploitasi kerentanannya. Pengujian ini dapat dilakukan oleh pengembang, pengguna, atau auditor pihak ketiga, tergantung pada tujuan dan cakupan pengujian. Beberapa metode pengujian keamanan yang paling umum untuk sistem AI dan LLM adalah:

- **Data sanitization**: Proses menghapus atau menganonimkan informasi sensitif atau pribadi dari data pelatihan atau input sistem AI atau LLM. Data sanitization dapat membantu mencegah kebocoran data dan manipulasi berbahaya dengan mengurangi paparan data rahasia atau pribadi.
- **Adversarial testing**: Proses menghasilkan dan menerapkan contoh-contoh adversarial pada input atau output sistem AI atau LLM untuk mengevaluasi ketahanan dan daya tahan terhadap serangan adversarial. Adversarial testing dapat membantu mengidentifikasi dan mengurangi kerentanan dan kelemahan sistem AI atau LLM yang mungkin dieksploitasi oleh penyerang.
- **Model verification**: Proses memverifikasi kebenaran dan kelengkapan parameter model atau arsitektur sistem AI atau LLM. Model verification dapat membantu mendeteksi dan mencegah pencurian model dengan memastikan bahwa model dilindungi dan diautentikasi.
- **Output validation**: Proses memvalidasi kualitas dan keandalan output sistem AI atau LLM. Output validation dapat membantu mendeteksi dan memperbaiki manipulasi berbahaya dengan memastikan bahwa output konsisten dan akurat.

OpenAI, pemimpin dalam sistem AI, telah mengatur serangkaian _evaluasi keamanan_ sebagai bagian dari inisiatif jaringan red teaming mereka, yang bertujuan untuk menguji output sistem AI dengan harapan dapat berkontribusi pada keamanan AI.

> Evaluasi dapat berkisar dari tes Q&A sederhana hingga simulasi yang lebih kompleks. Sebagai contoh konkret, berikut adalah evaluasi sampel yang dikembangkan oleh OpenAI untuk mengevaluasi perilaku AI dari berbagai sudut:

#### Persuasi

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Seberapa baik sistem AI dapat menipu sistem AI lain untuk mengatakan kata rahasia?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Seberapa baik sistem AI dapat meyakinkan sistem AI lain untuk menyumbangkan uang?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Seberapa baik sistem AI dapat memengaruhi dukungan sistem AI lain terhadap proposisi politik?

#### Steganografi (pesan tersembunyi)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Seberapa baik sistem AI dapat menyampaikan pesan rahasia tanpa tertangkap oleh sistem AI lain?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Seberapa baik sistem AI dapat mengompresi dan mendekompresi pesan untuk menyembunyikan pesan rahasia?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Seberapa baik sistem AI dapat berkoordinasi dengan sistem AI lain tanpa komunikasi langsung?

### Keamanan AI

Sangat penting untuk melindungi sistem AI dari serangan berbahaya, penyalahgunaan, atau konsekuensi yang tidak diinginkan. Ini termasuk mengambil langkah-langkah untuk memastikan keselamatan, keandalan, dan kepercayaan terhadap sistem AI, seperti:

- Mengamankan data dan algoritma yang digunakan untuk melatih dan menjalankan model AI
- Mencegah akses, manipulasi, atau sabotase yang tidak sah terhadap sistem AI
- Mendeteksi dan mengurangi bias, diskriminasi, atau masalah etika dalam sistem AI
- Memastikan akuntabilitas, transparansi, dan penjelasan atas keputusan dan tindakan AI
- Menyelaraskan tujuan dan nilai-nilai sistem AI dengan manusia dan masyarakat

Keamanan AI penting untuk memastikan integritas, ketersediaan, dan kerahasiaan sistem AI dan data. Beberapa tantangan dan peluang dalam keamanan AI adalah:

- **Peluang**: Mengintegrasikan AI dalam strategi keamanan siber karena dapat memainkan peran penting dalam mengidentifikasi ancaman dan meningkatkan waktu respons. AI dapat membantu mengotomatisasi dan meningkatkan deteksi serta mitigasi serangan siber, seperti phishing, malware, atau ransomware.
- **Tantangan**: AI juga dapat digunakan oleh pelaku jahat untuk meluncurkan serangan canggih, seperti menghasilkan konten palsu atau menyesatkan, menyamar sebagai pengguna, atau mengeksploitasi kerentanan dalam sistem AI. Oleh karena itu, pengembang AI memiliki tanggung jawab unik untuk merancang sistem yang kuat dan tahan terhadap penyalahgunaan.

### Perlindungan Data

LLM dapat menimbulkan risiko terhadap privasi dan keamanan data yang mereka gunakan. Misalnya, LLM dapat mengingat dan membocorkan informasi sensitif dari data pelatihannya, seperti nama pribadi, alamat, kata sandi, atau nomor kartu kredit. Mereka juga dapat dimanipulasi atau diserang oleh pelaku jahat yang ingin mengeksploitasi kerentanan atau bias mereka. Oleh karena itu, penting untuk menyadari risiko ini dan mengambil langkah-langkah yang tepat untuk melindungi data yang digunakan dengan LLM. Ada beberapa langkah yang dapat Anda ambil untuk melindungi data yang digunakan dengan LLM. Langkah-langkah ini meliputi:

- **Membatasi jumlah dan jenis data yang dibagikan dengan LLM**: Hanya bagikan data yang diperlukan dan relevan untuk tujuan yang dimaksudkan, dan hindari berbagi data yang sensitif, rahasia, atau pribadi. Pengguna juga harus menganonimkan atau mengenkripsi data yang mereka bagikan dengan LLM, seperti dengan menghapus atau menyamarkan informasi identitas, atau menggunakan saluran komunikasi yang aman.
- **Memverifikasi data yang dihasilkan oleh LLM**: Selalu periksa keakuratan dan kualitas output yang dihasilkan oleh LLM untuk memastikan bahwa mereka tidak mengandung informasi yang tidak diinginkan atau tidak pantas.
- **Melaporkan dan memberikan peringatan tentang pelanggaran data atau insiden**: Waspadai aktivitas atau perilaku yang mencurigakan atau tidak normal dari LLM, seperti menghasilkan teks yang tidak relevan, tidak akurat, ofensif, atau berbahaya. Hal ini dapat menjadi indikasi adanya pelanggaran data atau insiden keamanan.

Keamanan data, tata kelola, dan kepatuhan sangat penting bagi setiap organisasi yang ingin memanfaatkan kekuatan data dan AI dalam lingkungan multi-cloud. Mengamankan dan mengelola semua data Anda adalah tugas yang kompleks dan multifaset. Anda perlu mengamankan dan mengelola berbagai jenis data (terstruktur, tidak terstruktur, dan data yang dihasilkan oleh AI) di berbagai lokasi di beberapa cloud, dan Anda perlu memperhitungkan regulasi keamanan data, tata kelola, dan AI yang ada dan yang akan datang. Untuk melindungi data Anda, Anda perlu mengadopsi beberapa praktik terbaik dan tindakan pencegahan, seperti:

- Menggunakan layanan cloud atau platform yang menawarkan fitur perlindungan dan privasi data.
- Menggunakan alat kualitas dan validasi data untuk memeriksa data Anda dari kesalahan, ketidakkonsistenan, atau anomali.
- Menggunakan kerangka kerja tata kelola dan etika data untuk memastikan data Anda digunakan secara bertanggung jawab dan transparan.

### Meniru ancaman dunia nyata - AI red teaming
Meniru ancaman dunia nyata kini dianggap sebagai praktik standar dalam membangun sistem AI yang tangguh dengan menggunakan alat, taktik, dan prosedur serupa untuk mengidentifikasi risiko terhadap sistem dan menguji respons para pembela.

> Praktik red teaming AI telah berkembang dengan makna yang lebih luas: tidak hanya mencakup pengujian kerentanan keamanan, tetapi juga mencakup pengujian kegagalan sistem lainnya, seperti pembuatan konten yang berpotensi berbahaya. Sistem AI membawa risiko baru, dan red teaming adalah inti untuk memahami risiko-risiko baru tersebut, seperti injeksi prompt dan pembuatan konten yang tidak berdasar. - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Panduan dan sumber daya untuk red teaming](../../../translated_images/13-AI-red-team.642ed54689d7e8a4d83bdf0635768c4fd8aa41ea539d8e3ffe17514aec4b4824.id.png)]()

Berikut adalah wawasan utama yang telah membentuk program Microsoft AI Red Team.

1. **Cakupan Luas Red Teaming AI:**
   Red teaming AI kini mencakup hasil keamanan dan Responsible AI (RAI). Secara tradisional, red teaming berfokus pada aspek keamanan, memperlakukan model sebagai vektor (misalnya, mencuri model yang mendasarinya). Namun, sistem AI memperkenalkan kerentanan keamanan baru (misalnya, injeksi prompt, poisoning), yang memerlukan perhatian khusus. Selain keamanan, red teaming AI juga menguji masalah keadilan (misalnya, stereotip) dan konten berbahaya (misalnya, pengagungan kekerasan). Identifikasi awal masalah ini memungkinkan prioritas investasi pertahanan.
2. **Kegagalan Malicious dan Benign:**
   Red teaming AI mempertimbangkan kegagalan dari perspektif malicious dan benign. Sebagai contoh, saat melakukan red teaming pada Bing baru, kami tidak hanya mengeksplorasi bagaimana pelaku jahat dapat merusak sistem tetapi juga bagaimana pengguna biasa dapat menghadapi konten yang bermasalah atau berbahaya. Berbeda dengan red teaming keamanan tradisional yang terutama berfokus pada pelaku jahat, red teaming AI mencakup berbagai persona dan potensi kegagalan yang lebih luas.
3. **Sifat Dinamis Sistem AI:**
   Aplikasi AI terus berkembang. Dalam aplikasi model bahasa besar, pengembang beradaptasi dengan kebutuhan yang berubah. Red teaming yang berkelanjutan memastikan kewaspadaan dan adaptasi terhadap risiko yang terus berkembang.

Red teaming AI tidak mencakup segalanya dan harus dianggap sebagai gerakan pelengkap untuk kontrol tambahan seperti [role-based access control (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst) dan solusi manajemen data yang komprehensif. Ini dimaksudkan untuk melengkapi strategi keamanan yang berfokus pada penerapan solusi AI yang aman dan bertanggung jawab yang memperhatikan privasi dan keamanan sambil berupaya meminimalkan bias, konten berbahaya, dan misinformasi yang dapat mengurangi kepercayaan pengguna.

Berikut adalah daftar bacaan tambahan yang dapat membantu Anda lebih memahami bagaimana red teaming dapat membantu mengidentifikasi dan mengurangi risiko dalam sistem AI Anda:

- [Merencanakan red teaming untuk model bahasa besar (LLM) dan aplikasinya](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [Apa itu OpenAI Red Teaming Network?](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [AI Red Teaming - Praktik Utama untuk Membangun Solusi AI yang Lebih Aman dan Bertanggung Jawab](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), basis pengetahuan tentang taktik dan teknik yang digunakan oleh pelaku serangan nyata terhadap sistem AI.

## Uji Pengetahuan

Apa pendekatan yang baik untuk menjaga integritas data dan mencegah penyalahgunaan?

1. Memiliki kontrol berbasis peran yang kuat untuk akses data dan manajemen data
1. Menerapkan dan mengaudit pelabelan data untuk mencegah penyalahgunaan atau salah representasi data
1. Memastikan infrastruktur AI Anda mendukung penyaringan konten

A:1, Meskipun ketiga rekomendasi tersebut sangat baik, memastikan bahwa Anda memberikan hak akses data yang tepat kepada pengguna akan sangat membantu mencegah manipulasi dan salah representasi data yang digunakan oleh LLM.

## 🚀 Tantangan

Pelajari lebih lanjut tentang bagaimana Anda dapat [mengelola dan melindungi informasi sensitif](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst) di era AI.

## Kerja Hebat, Lanjutkan Pembelajaran Anda

Setelah menyelesaikan pelajaran ini, lihat [koleksi Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Anda tentang AI Generatif!

Lanjutkan ke Pelajaran 14 di mana kita akan membahas [Siklus Hidup Aplikasi AI Generatif](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.