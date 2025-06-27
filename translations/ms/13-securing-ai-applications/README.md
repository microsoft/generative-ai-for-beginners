<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-06-25T21:31:38+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "ms"
}
-->
# Memastikan Keselamatan Aplikasi AI Generatif Anda

## Pengenalan

Pelajaran ini akan merangkumi:

- Keselamatan dalam konteks sistem AI.
- Risiko dan ancaman biasa kepada sistem AI.
- Kaedah dan pertimbangan untuk memastikan keselamatan sistem AI.

## Matlamat Pembelajaran

Selepas melengkapkan pelajaran ini, anda akan memahami:

- Ancaman dan risiko kepada sistem AI.
- Kaedah dan amalan biasa untuk memastikan keselamatan sistem AI.
- Bagaimana pelaksanaan ujian keselamatan boleh mencegah hasil yang tidak dijangka dan menghakis kepercayaan pengguna.

## Apakah maksud keselamatan dalam konteks AI generatif?

Seiring teknologi Kecerdasan Buatan (AI) dan Pembelajaran Mesin (ML) semakin membentuk kehidupan kita, adalah penting untuk melindungi bukan sahaja data pelanggan tetapi juga sistem AI itu sendiri. AI/ML semakin digunakan dalam menyokong proses pembuatan keputusan bernilai tinggi dalam industri di mana keputusan yang salah mungkin membawa akibat serius.

Berikut adalah perkara utama yang perlu dipertimbangkan:

- **Kesan AI/ML**: AI/ML mempunyai impak yang signifikan dalam kehidupan harian dan oleh itu melindungi mereka telah menjadi penting.
- **Cabaran Keselamatan**: Impak ini memerlukan perhatian yang betul untuk menangani keperluan melindungi produk berasaskan AI daripada serangan canggih, sama ada oleh troll atau kumpulan teratur.
- **Masalah Strategik**: Industri teknologi mesti secara proaktif menangani cabaran strategik untuk memastikan keselamatan pelanggan jangka panjang dan keselamatan data.

Selain itu, model Pembelajaran Mesin sebahagian besarnya tidak dapat membezakan antara input berniat jahat dan data anomali yang tidak berbahaya. Sumber data latihan yang signifikan diperoleh daripada set data awam yang tidak dikurasi dan tidak dimoderasi, yang terbuka kepada sumbangan pihak ketiga. Penyerang tidak perlu mengkompromi set data apabila mereka bebas menyumbang kepada mereka. Lama-kelamaan, data berniat jahat berkeyakinan rendah menjadi data dipercayai berkeyakinan tinggi, jika struktur/format data kekal betul.

Inilah sebabnya mengapa penting untuk memastikan integriti dan perlindungan stor data yang digunakan oleh model anda untuk membuat keputusan.

## Memahami ancaman dan risiko AI

Dari segi AI dan sistem berkaitan, pencemaran data muncul sebagai ancaman keselamatan paling signifikan hari ini. Pencemaran data adalah apabila seseorang sengaja mengubah maklumat yang digunakan untuk melatih AI, menyebabkan ia membuat kesilapan. Ini disebabkan oleh ketiadaan kaedah pengesanan dan mitigasi yang standard, ditambah dengan pergantungan kita pada set data awam yang tidak dipercayai atau tidak dikurasi untuk latihan. Untuk mengekalkan integriti data dan mencegah proses latihan yang cacat, adalah penting untuk mengesan asal usul dan keturunan data anda. Jika tidak, pepatah lama "sampah masuk, sampah keluar" tetap benar, yang membawa kepada prestasi model yang terkompromi.

Berikut adalah contoh bagaimana pencemaran data boleh menjejaskan model anda:

1. **Pembalikan Label**: Dalam tugas klasifikasi binari, musuh sengaja membalikkan label sebahagian kecil data latihan. Sebagai contoh, sampel tidak berbahaya dilabelkan sebagai berniat jahat, menyebabkan model belajar persatuan yang salah.\
   **Contoh**: Penapis spam yang salah mengklasifikasikan e-mel sah sebagai spam kerana label yang dimanipulasi.
2. **Pencemaran Ciri**: Penyerang secara halus mengubah suai ciri dalam data latihan untuk memperkenalkan bias atau mengelirukan model.\
   **Contoh**: Menambah kata kunci yang tidak relevan kepada deskripsi produk untuk memanipulasi sistem cadangan.
3. **Suntikan Data**: Menyuntik data berniat jahat ke dalam set latihan untuk mempengaruhi tingkah laku model.\
   **Contoh**: Memperkenalkan ulasan pengguna palsu untuk mempengaruhi keputusan analisis sentimen.
4. **Serangan Pintu Belakang**: Musuh memasukkan pola tersembunyi (pintu belakang) ke dalam data latihan. Model belajar mengenali pola ini dan bertindak jahat apabila dicetuskan.\
   **Contoh**: Sistem pengecaman wajah yang dilatih dengan imej pintu belakang yang salah mengenal pasti orang tertentu.

MITRE Corporation telah mencipta [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), sebuah pangkalan pengetahuan tentang taktik dan teknik yang digunakan oleh musuh dalam serangan dunia nyata terhadap sistem AI.

> Terdapat peningkatan jumlah kelemahan dalam sistem yang didayakan AI, kerana penggabungan AI meningkatkan permukaan serangan sistem sedia ada melebihi serangan siber tradisional. Kami membangunkan ATLAS untuk meningkatkan kesedaran tentang kelemahan unik dan berkembang ini, kerana komuniti global semakin menggabungkan AI ke dalam pelbagai sistem. ATLAS dimodelkan selepas kerangka MITRE ATT&CK® dan taktik, teknik, dan prosedurnya (TTP) melengkapi yang ada dalam ATT&CK.

Sama seperti kerangka MITRE ATT&CK®, yang digunakan secara meluas dalam keselamatan siber tradisional untuk merancang senario emulasi ancaman lanjutan, ATLAS menyediakan set TTP yang mudah dicari yang dapat membantu untuk lebih memahami dan bersiap sedia untuk mempertahankan diri daripada serangan yang muncul.

Selain itu, Projek Keselamatan Aplikasi Web Terbuka (OWASP) telah mencipta "[Senarai 10 Teratas](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" bagi kelemahan paling kritikal yang ditemui dalam aplikasi yang menggunakan LLM. Senarai ini menyoroti risiko ancaman seperti pencemaran data yang disebutkan di atas bersama dengan yang lain seperti:

- **Suntikan Prompt**: teknik di mana penyerang memanipulasi Model Bahasa Besar (LLM) melalui input yang dirancang dengan teliti, menyebabkan ia berkelakuan di luar tingkah laku yang dimaksudkan.
- **Kelemahan Rantai Bekalan**: Komponen dan perisian yang membentuk aplikasi yang digunakan oleh LLM, seperti modul Python atau set data luaran, boleh dikompromi sendiri yang membawa kepada keputusan yang tidak dijangka, bias yang diperkenalkan dan bahkan kelemahan dalam infrastruktur asas.
- **Ketergantungan Berlebihan**: LLM boleh gagal dan cenderung untuk berhalusinasi, memberikan hasil yang tidak tepat atau tidak selamat. Dalam beberapa keadaan yang didokumentasikan, orang telah mengambil keputusan ini sebagai nilai muka yang membawa kepada akibat negatif dunia nyata yang tidak diingini.

Penasihat Awan Microsoft Rod Trent telah menulis ebook percuma, [Mesti Belajar Keselamatan AI](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), yang mendalami ancaman AI yang muncul ini dan menyediakan panduan luas tentang cara terbaik menangani senario ini.

## Ujian Keselamatan untuk Sistem AI dan LLM

Kecerdasan buatan (AI) sedang mengubah pelbagai domain dan industri, menawarkan kemungkinan dan manfaat baru untuk masyarakat. Walau bagaimanapun, AI juga menimbulkan cabaran dan risiko yang ketara, seperti privasi data, bias, kekurangan penjelasan, dan potensi penyalahgunaan. Oleh itu, adalah penting untuk memastikan bahawa sistem AI selamat dan bertanggungjawab, yang bermaksud bahawa mereka mematuhi piawaian etika dan undang-undang dan boleh dipercayai oleh pengguna dan pemegang kepentingan.

Ujian keselamatan adalah proses menilai keselamatan sistem AI atau LLM, dengan mengenal pasti dan mengeksploitasi kelemahan mereka. Ini boleh dilakukan oleh pembangun, pengguna, atau juruaudit pihak ketiga, bergantung kepada tujuan dan skop ujian. Beberapa kaedah ujian keselamatan yang paling biasa untuk sistem AI dan LLM adalah:

- **Penyucian data**: Ini adalah proses mengeluarkan atau menganonimkan maklumat sensitif atau peribadi dari data latihan atau input sistem AI atau LLM. Penyucian data dapat membantu mencegah kebocoran data dan manipulasi jahat dengan mengurangkan pendedahan data sulit atau peribadi.
- **Ujian Adversarial**: Ini adalah proses menjana dan menggunakan contoh-contoh lawan kepada input atau output sistem AI atau LLM untuk menilai ketahanan dan daya tahannya terhadap serangan lawan. Ujian adversarial dapat membantu mengenal pasti dan mengurangkan kelemahan dan kelemahan sistem AI atau LLM yang mungkin dieksploitasi oleh penyerang.
- **Pengesahan Model**: Ini adalah proses mengesahkan ketepatan dan kelengkapan parameter model atau seni bina sistem AI atau LLM. Pengesahan model dapat membantu mengesan dan mencegah pencurian model dengan memastikan bahawa model dilindungi dan diautentikasi.
- **Pengesahan Output**: Ini adalah proses mengesahkan kualiti dan kebolehpercayaan output sistem AI atau LLM. Pengesahan output dapat membantu mengesan dan membetulkan manipulasi jahat dengan memastikan bahawa output konsisten dan tepat.

OpenAI, peneraju dalam sistem AI, telah menetapkan siri _penilaian keselamatan_ sebagai sebahagian daripada inisiatif rangkaian pasukan merah mereka, yang bertujuan untuk menguji output sistem AI dengan harapan dapat menyumbang kepada keselamatan AI.

> Penilaian boleh terdiri daripada ujian soal jawab mudah hingga simulasi yang lebih kompleks. Sebagai contoh konkrit, berikut adalah penilaian sampel yang dibangunkan oleh OpenAI untuk menilai tingkah laku AI dari beberapa sudut:

#### Persuasi

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Sejauh mana sistem AI boleh memperdaya sistem AI lain untuk mengatakan perkataan rahsia?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Sejauh mana sistem AI boleh meyakinkan sistem AI lain untuk menderma wang?
- [Cadangan Undian](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Sejauh mana sistem AI boleh mempengaruhi sokongan sistem AI lain terhadap cadangan politik?

#### Steganografi (pesanan tersembunyi)

- [Steganografi](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Sejauh mana sistem AI boleh menyampaikan mesej rahsia tanpa ditangkap oleh sistem AI lain?
- [Pemampatan Teks](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Sejauh mana sistem AI boleh memampatkan dan mendekompresi mesej, untuk membolehkan menyembunyikan mesej rahsia?
- [Titik Schelling](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Sejauh mana sistem AI boleh berkoordinasi dengan sistem AI lain, tanpa komunikasi langsung?

### Keselamatan AI

Adalah penting kita berusaha melindungi sistem AI daripada serangan berniat jahat, penyalahgunaan, atau akibat yang tidak diingini. Ini termasuk mengambil langkah untuk memastikan keselamatan, kebolehpercayaan, dan kebolehpercayaan sistem AI, seperti:

- Melindungi data dan algoritma yang digunakan untuk melatih dan menjalankan model AI
- Mencegah akses tanpa izin, manipulasi, atau sabotaj sistem AI
- Mengesan dan mengurangkan bias, diskriminasi, atau isu etika dalam sistem AI
- Memastikan akauntabiliti, ketelusan, dan kebolehjelasan keputusan dan tindakan AI
- Menyelaraskan matlamat dan nilai sistem AI dengan manusia dan masyarakat

Keselamatan AI adalah penting untuk memastikan integriti, ketersediaan, dan kerahsiaan sistem AI dan data. Beberapa cabaran dan peluang keselamatan AI adalah:

- Peluang: Menggabungkan AI dalam strategi keselamatan siber kerana ia boleh memainkan peranan penting dalam mengenal pasti ancaman dan meningkatkan masa tindak balas. AI boleh membantu mengotomatisasi dan meningkatkan pengesanan dan pengurangan serangan siber, seperti phishing, malware, atau ransomware.
- Cabaran: AI juga boleh digunakan oleh musuh untuk melancarkan serangan yang canggih, seperti menjana kandungan palsu atau mengelirukan, menyamar sebagai pengguna, atau mengeksploitasi kelemahan dalam sistem AI. Oleh itu, pembangun AI mempunyai tanggungjawab unik untuk merancang sistem yang teguh dan tahan terhadap penyalahgunaan.

### Perlindungan Data

LLM boleh menimbulkan risiko kepada privasi dan keselamatan data yang mereka gunakan. Sebagai contoh, LLM berpotensi menghafal dan membocorkan maklumat sensitif daripada data latihan mereka, seperti nama peribadi, alamat, kata laluan, atau nombor kad kredit. Mereka juga boleh dimanipulasi atau diserang oleh pelaku jahat yang ingin mengeksploitasi kelemahan atau bias mereka. Oleh itu, adalah penting untuk menyedari risiko ini dan mengambil langkah yang sesuai untuk melindungi data yang digunakan dengan LLM. Terdapat beberapa langkah yang boleh anda ambil untuk melindungi data yang digunakan dengan LLM. Langkah-langkah ini termasuk:

- **Mengehadkan jumlah dan jenis data yang mereka kongsi dengan LLM**: Hanya kongsi data yang diperlukan dan relevan untuk tujuan yang dimaksudkan, dan elakkan berkongsi sebarang data yang sensitif, sulit, atau peribadi. Pengguna juga harus menganonimkan atau menyulitkan data yang mereka kongsi dengan LLM, seperti dengan mengeluarkan atau menyembunyikan sebarang maklumat pengenalan, atau menggunakan saluran komunikasi yang selamat.
- **Mengesahkan data yang dihasilkan oleh LLM**: Sentiasa periksa ketepatan dan kualiti output yang dihasilkan oleh LLM untuk memastikan mereka tidak mengandungi maklumat yang tidak diingini atau tidak sesuai.
- **Melaporkan dan memberi amaran tentang sebarang pelanggaran data atau insiden**: Berwaspada terhadap sebarang aktiviti atau tingkah laku yang mencurigakan atau tidak normal dari LLM, seperti menjana teks yang tidak relevan, tidak tepat, ofensif, atau berbahaya. Ini boleh menjadi petunjuk pelanggaran data atau insiden keselamatan.

Keselamatan data, tadbir urus, dan pematuhan adalah kritikal untuk mana-mana organisasi yang ingin memanfaatkan kuasa data dan AI dalam persekitaran berbilang awan. Melindungi dan mengawal semua data anda adalah usaha yang kompleks dan pelbagai aspek. Anda perlu melindungi dan mengawal jenis data yang berbeza (berstruktur, tidak berstruktur, dan data yang dihasilkan oleh AI) di lokasi yang berbeza di pelbagai awan, dan anda perlu mengambil kira keselamatan data yang sedia ada dan masa depan, tadbir urus, dan peraturan AI. Untuk melindungi data anda, anda perlu mengamalkan beberapa amalan terbaik dan langkah berjaga-jaga, seperti:

- Menggunakan perkhidmatan awan atau platform yang menawarkan perlindungan data dan ciri privasi.
- Menggunakan alat kualiti dan pengesahan data untuk memeriksa data anda untuk kesilapan, ketidakkonsistenan, atau anomali.
- Menggunakan kerangka tadbir urus data dan etika untuk memastikan data anda digunakan dengan cara yang bertanggungjawab dan telus.

### Meniru ancaman dunia nyata - pasukan merah AI

Meniru ancaman dunia nyata kini dianggap sebagai amalan standard dalam membina sistem AI yang berdaya tahan dengan menggunakan alat, taktik, prosedur yang serupa untuk mengenal pasti risiko kepada sistem dan menguji tindak balas pembela.

> Amalan pasukan merah AI telah berkembang untuk mengambil makna yang lebih luas: ia tidak hanya meliputi pemeriksaan untuk kelemahan keselamatan, tetapi juga termasuk pemeriksaan untuk kegagalan sistem lain, seperti penjanaan kandungan yang berpotensi berbahaya. Sistem AI datang dengan risiko baru, dan pasukan merah adalah teras untuk memahami risiko baru tersebut, seperti suntikan prompt dan pengeluaran kandungan yang tidak berasas. - [Pasukan Merah AI Microsoft membina masa depan AI yang lebih selamat](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

Di bawah ini adalah pandangan utama yang telah membentuk program Pasukan Merah AI Microsoft.

1. **Skop Luas Pasukan Merah AI:**
   Pasukan merah AI kini merangkumi kedua-dua keselamatan dan hasil AI Bertanggungjawab (RAI). Secara tradisional, pasukan merah memberi tumpuan kepada aspek keselamatan, menganggap model sebagai vektor (contohnya, mencuri model asas). Walau bagaimanapun, sistem AI memperkenalkan kelemahan keselamatan baru (contohnya, suntikan prompt, pencemaran), memerlukan perhatian khusus. Selain keselamatan, pasukan merah AI juga meneliti isu keadilan (contohnya, stereotaip) dan kandungan berbahaya (contohnya, pengagungan keganasan). Pengenalan awal isu-isu ini membolehkan keutamaan pelaburan pertahanan.
2. **Kegagalan Berniat Jahat dan Tidak Berniat Jahat:**
   Pasukan merah AI mempertimbangkan kegagalan dari perspektif berniat jahat dan tidak berniat jahat. Sebagai contoh, apabila menjalankan pasukan merah Bing baru, kami meneliti bukan sahaja bagaimana musuh berniat jahat boleh menumbangkan sistem tetapi juga bagaimana pengguna biasa boleh menghadapi kandungan yang bermasalah atau berbahaya. Tidak seperti pasukan merah keselamatan tradisional, yang memberi tumpuan terutamanya kepada pelaku berniat jahat, pasukan merah AI mengambil kira pelbagai persona dan potensi kegagalan yang lebih luas.
3. **Sifat Dinamik Sistem AI:**
   Aplikasi AI sentiasa berkembang. Dalam aplikasi model bahasa besar, pembangun menyesuaikan diri dengan

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk mencapai ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau tafsiran yang timbul daripada penggunaan terjemahan ini.