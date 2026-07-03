# Asas Kejuruteraan Prompt

[![Asas Kejuruteraan Prompt](../../../translated_images/ms/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Pengenalan
Modul ini merangkumi konsep dan teknik penting untuk mencipta prompt yang berkesan dalam model AI generatif. Cara anda menulis prompt kepada LLM juga penting. Prompt yang dirangka dengan teliti boleh mencapai kualiti respons yang lebih baik. Tetapi apa sebenarnya maksud istilah seperti _prompt_ dan _kejuruteraan prompt_? Dan bagaimana saya boleh memperbaiki _input_ prompt yang saya hantar ke LLM? Ini adalah soalan yang akan kami cuba jawab dalam bab ini dan bab seterusnya.

_AI Generatif_ mampu mencipta kandungan baru (contohnya, teks, imej, audio, kod dan lain-lain) sebagai tindak balas kepada permintaan pengguna. Ia mencapai ini menggunakan _Model Bahasa Besar_ seperti siri GPT OpenAI ("Transformer Pra-latih Generatif") yang dilatih untuk menggunakan bahasa semula jadi dan kod.

Pengguna kini boleh berinteraksi dengan model ini menggunakan paradigma yang biasa seperti chat, tanpa memerlukan kepakaran teknikal atau latihan. Model ini adalah _berasaskan prompt_ - pengguna menghantar teks input (prompt) dan mendapat respons AI (penyempurnaan). Mereka kemudian boleh "berchat dengan AI" secara ulang-alik, dalam perbualan berbilang pusingan, memperhalusi prompt mereka sehingga respons itu memenuhi jangkaan mereka.

"Prompt" kini menjadi _antara muka pengaturcaraan_ utama untuk aplikasi AI generatif, memberitahu model apa yang perlu dibuat dan mempengaruhi kualiti respons yang dikembalikan. "Kejuruteraan Prompt" adalah bidang kajian yang berkembang pesat yang memberi tumpuan kepada _reka bentuk dan pengoptimuman_ prompt untuk memberikan respons yang konsisten dan berkualiti pada skala.

## Matlamat Pembelajaran

Dalam pelajaran ini, kita akan mempelajari apa itu Kejuruteraan Prompt, mengapa ia penting, dan bagaimana kita boleh merangka prompt yang lebih berkesan untuk model dan objektif aplikasi tertentu. Kita akan memahami konsep teras dan amalan terbaik untuk kejuruteraan prompt - serta belajar mengenai persekitaran Jupyter Notebooks "sandbox" interaktif di mana kita dapat melihat konsep ini diaplikasikan kepada contoh sebenar.

Menjelang akhir pelajaran ini, kita akan dapat:

1. Jelaskan apa itu kejuruteraan prompt dan mengapa ia penting.
2. Terangkan komponen prompt dan bagaimana ia digunakan.
3. Pelajari amalan terbaik dan teknik untuk kejuruteraan prompt.
4. Gunakan teknik yang dipelajari kepada contoh sebenar, menggunakan titik akhir OpenAI.

## Istilah Utama

Kejuruteraan Prompt: Amalan mereka bentuk dan memperhalusi input untuk memandu model AI supaya menghasilkan output yang dikehendaki.  
Tokenisasi: Proses menukar teks kepada unit yang lebih kecil, dipanggil token, yang boleh difahami dan diproses oleh model.  
LLM Tune Arahan: Model Bahasa Besar (LLM) yang telah ditala halus dengan arahan khusus untuk meningkatkan ketepatan dan relevansi respons mereka.

## Sandbox Pembelajaran

Kejuruteraan prompt pada masa ini lebih merupakan seni daripada sains. Cara terbaik untuk meningkatkan intuisi kita adalah dengan _berlatih lebih banyak_ dan mengamalkan pendekatan cuba-cuba yang menggabungkan kepakaran domain aplikasi dengan teknik yang disyorkan dan pengoptimuman khusus model.

Jupyter Notebook yang disediakan bersama pelajaran ini menyediakan persekitaran _sandbox_ di mana anda boleh mencuba apa yang anda pelajari - secara langsung atau sebagai sebahagian cabaran kod di akhir pelajaran. Untuk melaksanakan latihan, anda memerlukan:

1. **Kunci API Azure OpenAI** - titik akhir perkhidmatan untuk LLM yang telah dideploy.  
2. **Runtime Python** - untuk menjalankan Notebook tersebut.  
3. **Pembolehubah Persekitaran Tempatan** - _lengkapkan langkah [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) sekarang untuk bersedia_.

Notebook datang dengan latihan _permulaan_ - tetapi anda digalakkan untuk menambah seksyen _Markdown_ (penerangan) dan _Kod_ (permintaan prompt) sendiri untuk mencuba lebih banyak contoh atau idea - dan membina intuisi anda untuk mereka bentuk prompt.

## Panduan Bergambar

Ingin mendapatkan gambaran besar tentang apa yang diliputi dalam pelajaran ini sebelum anda menyelam lebih dalam? Lihat panduan bergambar ini, yang memberikan anda gambaran topik utama yang dibincangkan dan intipati utama untuk anda fikirkan dalam setiap satu. Peta pelajaran membawa anda dari memahami konsep teras dan cabaran kepada menangani mereka dengan teknik kejuruteraan prompt yang berkaitan dan amalan terbaik. Perhatikan bahawa bahagian "Teknik Lanjutan" dalam panduan ini merujuk kepada kandungan yang diliputi dalam bab _seterusnya_ dalam kurikulum ini.

![Panduan Bergambar Kejuruteraan Prompt](../../../translated_images/ms/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Startup Kami

Sekarang, mari kita bincangkan bagaimana _topik ini_ berkaitan dengan misi startup kami untuk [membawa inovasi AI ke pendidikan](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Kami ingin membina aplikasi berkuasa AI untuk _pembelajaran yang diperibadikan_ - jadi mari fikirkan bagaimana pelbagai pengguna aplikasi kami mungkin "mereka bentuk" prompt:

- **Pentadbir** mungkin meminta AI untuk _menganalisis data kurikulum bagi mengenal pasti jurang liputan_. AI boleh meringkaskan keputusan atau memvisualisasikannya dengan kod.  
- **Pendidik** mungkin meminta AI untuk _menghasilkan pelan pelajaran untuk audiens dan topik sasaran_. AI boleh membina pelan diperibadikan dalam format yang ditetapkan.  
- **Pelajar** mungkin meminta AI untuk _menjadi tutor mereka dalam subjek yang sukar_. AI kini boleh membimbing pelajar dengan pelajaran, petunjuk & contoh yang disesuaikan dengan tahap mereka.

Itu baru permulaan. Lihat [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - perpustakaan prompt sumber terbuka yang dikurasi oleh pakar pendidikan - untuk mendapatkan gambaran lebih luas mengenai kemungkinan! _Cuba jalankan beberapa prompt tersebut dalam sandbox atau menggunakan OpenAI Playground untuk melihat apa yang berlaku!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Apa itu Kejuruteraan Prompt?

Kita mula pelajaran ini dengan mentakrifkan **Kejuruteraan Prompt** sebagai proses _mereka bentuk dan mengoptimumkan_ input teks (prompt) untuk memberikan respons yang konsisten dan berkualiti (penyempurnaan) untuk objektif aplikasi dan model tertentu. Kita boleh menganggap ini sebagai proses 2 langkah:

- _mereka bentuk_ prompt awal untuk model dan objektif yang diberikan  
- _memperhalusi_ prompt secara iteratif untuk meningkatkan kualiti respons

Ini semestinya proses cuba-cuba yang memerlukan intuisi dan usaha pengguna untuk mendapatkan keputusan optimum. Jadi mengapa ia penting? Untuk menjawab soalan itu, kita perlu faham tiga konsep:

- _Tokenisasi_ = bagaimana model "melihat" prompt  
- _LLM Asas_ = bagaimana model asas "memproses" prompt  
- _LLM Tune Arahan_ = bagaimana model kini boleh melihat "tugas"

### Tokenisasi

LLM melihat prompt sebagai _urutan token_ di mana model berbeza (atau versi model) boleh membuat tokenisasi prompt yang sama dengan cara berbeza. Oleh kerana LLM dilatih pada token (dan bukan pada teks mentah), cara prompt ditokenkan memberi impak terus kepada kualiti respons yang dijana.

Untuk mendapatkan intuisi tentang bagaimana tokenisasi berfungsi, cuba alat seperti [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) yang ditunjukkan di bawah. Salin prompt anda - dan lihat bagaimana ia ditukar menjadi token, beri perhatian pada bagaimana aksara ruang kosong dan tanda baca diurus. Perhatikan contoh ini menunjukkan LLM lama (GPT-3) - jadi mencuba ini dengan model baru mungkin menghasilkan keputusan berbeza.

![Tokenisasi](../../../translated_images/ms/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Konsep: Model Asas

Apabila prompt ditokenkan, fungsi utama ["LLM Asas"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (atau model asas) adalah untuk meramal token seterusnya dalam urutan itu. Oleh kerana LLM dilatih menggunakan dataset teks yang besar, mereka mempunyai pemahaman hubungan statistik antara token dan boleh membuat ramalan itu dengan yakin. Perlu diingat, mereka tidak memahami _makna_ perkataan dalam prompt atau token; mereka hanya melihat corak yang boleh mereka "lengkapkan" dengan ramalan seterusnya. Mereka boleh terus meramal urutan sehingga diberhentikan oleh campur tangan pengguna atau syarat tertentu yang telah ditetapkan.

Ingin melihat bagaimana penyempurnaan berasaskan prompt berfungsi? Masukkan prompt di atas ke dalam Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) dengan tetapan lalai. Sistem dikonfigurasikan untuk menganggap prompt sebagai permintaan maklumat - jadi anda sepatutnya melihat penyempurnaan yang memuaskan konteks ini.

Tetapi bagaimana jika pengguna mahu melihat sesuatu yang khusus yang memenuhi kriteria atau objektif tugas? Di sinilah LLM _tuned arahan_ masuk dalam gambar.

![Penyempurnaan Chat LLM Asas](../../../translated_images/ms/04-playground-chat-base.65b76fcfde0caa67.webp)

### Konsep: LLM Tune Arahan

[LLM Tune Arahan](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) bermula dengan model asas dan menala halusnya dengan contoh atau pasangan input/output (contohnya, "mesej" berbilang pusingan) yang boleh mengandungi arahan jelas - dan respons dari AI cuba mengikuti arahan itu.

Ini menggunakan teknik seperti Pembelajaran Penguatan dengan Maklum Balas Manusia (RLHF) yang boleh melatih model untuk _mengikut arahan_ dan _belajar dari maklum balas_ supaya ia menghasilkan respons yang lebih sesuai untuk aplikasi praktikal dan lebih relevan kepada objektif pengguna.

Mari cuba - ulang semula prompt di atas, tetapi kini tukar _mesej sistem_ untuk memberikan arahan berikut sebagai konteks:

> _Ringkaskan kandungan yang diberikan untuk murid darjah dua. Kekalkan hasil dalam satu perenggan dengan 3-5 titik peluru._

Lihat bagaimana hasil kini disesuaikan untuk mencerminkan matlamat dan format yang dikehendaki? Seorang pendidik kini boleh terus menggunakan respons ini dalam slaid untuk kelas tersebut.

![Penyempurnaan Chat LLM Tune Arahan](../../../translated_images/ms/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Mengapa kita perlukan Kejuruteraan Prompt?

Sekarang kita tahu bagaimana prompt diproses oleh LLM, mari bincangkan _mengapa_ kita memerlukan kejuruteraan prompt. Jawapannya terletak pada hakikat bahawa LLM semasa menghadapi beberapa cabaran yang menjadikan _penyempurnaan yang boleh dipercayai dan konsisten_ lebih sukar dicapai tanpa usaha dalam pembinaan dan pengoptimuman prompt. Contohnya:

1. **Respons model adalah stokastik.** _Prompt yang sama_ mungkin menghasilkan respons berbeza dengan model atau versi model yang berbeza. Dan ia boleh menghasilkan keputusan berbeza dengan _model yang sama_ pada masa berlainan. _Teknik kejuruteraan prompt boleh membantu kita meminimumkan variasi ini dengan menyediakan panduan yang lebih baik_.

1. **Model boleh mereka cipta respons palsu.** Model dilatih dengan dataset yang _besar tetapi terhad_, bermakna mereka kekurangan pengetahuan tentang konsep di luar skop latihan tersebut. Oleh itu, mereka boleh menghasilkan penyempurnaan yang tidak tepat, khayalan, atau bertentangan terus dengan fakta yang diketahui. _Teknik kejuruteraan prompt membantu pengguna mengenal pasti dan mengurangkan rekaan sebegini contohnya dengan meminta AI menyertakan sumber atau alasan_.

1. **Keupayaan model akan berbeza.** Model baru atau generasi model terbaru akan mempunyai keupayaan yang lebih kaya tetapi juga membawa keunikan dan pertukaran dalam kos & kerumitan. _Kejuruteraan prompt boleh membantu kita membangunkan amalan terbaik dan aliran kerja yang mengabstrakkan perbezaan serta menyesuaikan keperluan spesifik model dengan cara yang berskala dan lancar_.

Mari lihat ini dalam tindakan di OpenAI atau Azure OpenAI Playground:

- Gunakan prompt yang sama dengan pelbagai deployment LLM (contohnya, OpenAI, Azure OpenAI, Hugging Face) - adakah anda melihat variasi?  
- Gunakan prompt yang sama berulang kali dengan deployment LLM yang _sama_ (contohnya, Azure OpenAI playground) - bagaimana variasi ini berbeza?

### Contoh Rekaan

Dalam kursus ini, kami menggunakan istilah **"rekaan"** untuk merujuk fenomena di mana LLM kadangkala menghasilkan maklumat yang salah secara fakta disebabkan kekangan latihan atau had lain. Anda mungkin juga pernah mendengar ini disebut sebagai _"halusinasi"_ dalam artikel popular atau kertas penyelidikan. Walau bagaimanapun, kami sangat mengesyorkan menggunakan istilah _"rekaan"_ supaya kita tidak secara tidak sengaja memberikan sifat seperti manusia kepada tingkah laku yang dijana mesin. Ini juga mengukuhkan panduan [AI Bertanggungjawab](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) dari segi terminologi, mengeluarkan istilah yang mungkin dianggap ofensif atau tidak inklusif dalam beberapa konteks.

Ingin mendapat gambaran bagaimana rekaan berlaku? Fikirkan tentang prompt yang mengarahkan AI untuk menghasilkan kandungan bagi topik yang tidak wujud (untuk memastikan ia tidak terdapat dalam dataset latihan). Sebagai contoh - saya cuba prompt ini:

> **Prompt:** hasilkan pelan pelajaran mengenai Perang Marikh 2076.
Carian web menunjukkan bahawa terdapat akaun fiksyen (contohnya, siri televisyen atau buku) mengenai peperangan Marikh - tetapi tiada pada tahun 2076. Akal fikiran juga memberitahu kita bahawa 2076 adalah _di masa depan_ dan oleh itu, tidak boleh dikaitkan dengan peristiwa sebenar.

Jadi apa yang berlaku apabila kita menjalankan prompt ini dengan pelbagai penyedia LLM?

> **Respons 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/ms/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Respons 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/ms/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Respons 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/ms/04-fabrication-huggingchat.faf82a0a51278956.webp)

Seperti yang dijangka, setiap model (atau versi model) menghasilkan respons yang sedikit berbeza terima kasih kepada tingkah laku stokastik dan variasi keupayaan model. Sebagai contoh, satu model menyasarkan audiens darjah 8 manakala satu lagi menganggap pelajar sekolah menengah. Tetapi ketiga-tiga model menghasilkan respons yang boleh meyakinkan pengguna yang tidak dimaklumkan bahawa peristiwa itu benar.

Teknik kejuruteraan prompt seperti _metaprompting_ dan _konfigurasi suhu_ mungkin mengurangkan fabrikasi model setakat tertentu. _Arkitektur_ kejuruteraan prompt baru juga memasukkan alat dan teknik baru dengan lancar ke dalam aliran prompt, untuk mengurangkan atau mengurangkan beberapa kesan ini.

## Kajian Kes: GitHub Copilot

Mari kita tutup bahagian ini dengan mendapatkan gambaran bagaimana kejuruteraan prompt digunakan dalam penyelesaian dunia sebenar dengan melihat satu Kajian Kes: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot adalah "Pasangan Pengaturcara AI" anda - ia menukar prompt teks kepada pelengkap kod dan diintegrasikan ke dalam persekitaran pembangunan anda (contohnya, Visual Studio Code) untuk pengalaman pengguna yang lancar. Seperti yang didokumentasikan dalam siri blog di bawah, versi awal berdasarkan model OpenAI Codex - dengan jurutera dengan cepat menyedari keperluan untuk melaras model dan membangunkan teknik kejuruteraan prompt yang lebih baik, untuk meningkatkan kualiti kod. Pada bulan Julai, mereka [memperkenalkan model AI yang dipertingkatkan yang melebihi Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) untuk cadangan yang lebih pantas lagi.

Baca pos mengikut urutan, untuk mengikuti perjalanan pembelajaran mereka.

- **Mei 2023** | [GitHub Copilot semakin baik dalam memahami kod anda](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mei 2023** | [Di dalam GitHub: Bekerja dengan LLM di belakang GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Cara menulis prompt yang lebih baik untuk GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot melebihi Codex dengan model AI yang dipertingkatkan](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Panduan Pembangun untuk Kejuruteraan Prompt dan LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Cara membina aplikasi LLM perusahaan: Pengajaran dari GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Anda juga boleh melayari [blog Kejuruteraan](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) mereka untuk lebih banyak pos seperti [yang ini](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) yang menunjukkan bagaimana model dan teknik ini diaplikasikan untuk memacu aplikasi dunia sebenar.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Pembinaan Prompt

Kita telah melihat mengapa kejuruteraan prompt penting - sekarang mari fahami bagaimana prompt dibina supaya kita boleh menilai teknik berbeza untuk reka bentuk prompt yang lebih efektif.

### Prompt Asas

Mari mulakan dengan prompt asas: input teks yang dihantar ke model tanpa konteks lain. Berikut adalah contoh - apabila kita menghantar beberapa perkataan pertama lagu kebangsaan Amerika Syarikat kepada OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) ia serta-merta _melengkapkan_ respons dengan beberapa baris berikut, menggambarkan tingkah laku ramalan asas.

| Prompt (Input)     | Pelengkap (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Ia kedengaran seperti anda sedang memulakan lirik "The Star-Spangled Banner," lagu kebangsaan Amerika Syarikat. Lirik penuhnya adalah ... |

### Prompt Kompleks

Sekarang mari kita tambah konteks dan arahan pada prompt asas itu. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) membolehkan kita membina prompt kompleks sebagai koleksi _mesej_ dengan:

- Pasangan input/output yang mencerminkan input _pengguna_ dan respons _pembantu_.
- Mesej sistem yang menetapkan konteks untuk tingkah laku atau personaliti pembantu.

Permintaan kini dalam bentuk di bawah, di mana _tokenisasi_ dengan berkesan menangkap maklumat berkaitan dari konteks dan perbualan. Kini, menukar konteks sistem boleh memberi impak yang setanding pada kualiti pelengkap, seperti input pengguna yang diberikan.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Prompt Arahan

Dalam contoh di atas, prompt pengguna adalah pertanyaan teks mudah yang boleh ditafsirkan sebagai permintaan maklumat. Dengan prompt _arahan_, kita boleh menggunakan teks itu untuk menentukan tugas dengan lebih terperinci, memberikan panduan yang lebih baik kepada AI. Berikut adalah contoh:

| Prompt (Input)                                                                                                                                                                                                                         | Pelengkap (Output)                                                                                                        | Jenis Arahan        |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Tulis penerangan mengenai Perang Saudara                                                                                                                                                                                               | _mengembalikan perenggan ringkas_                                                                                        | Ringkas             |
| Tulis penerangan mengenai Perang Saudara. Berikan tarikh utama dan peristiwa serta huraikan kepentingannya                                                                                                                                 | _mengembalikan perenggan diikuti oleh senarai tarikh peristiwa utama dengan huraian_                                       | Kompleks            |
| Tulis penerangan mengenai Perang Saudara dalam 1 perenggan. Berikan 3 titik peluru dengan tarikh utama dan kepentingannya. Berikan 3 lagi titik peluru dengan tokoh sejarah utama dan sumbangan mereka. Pulangkan output sebagai fail JSON | _mengembalikan butiran lebih terperinci dalam kotak teks, diformatkan sebagai JSON yang anda boleh salin tampal ke fail dan sahkan jika perlu_ | Kompleks. Berformat. |

## Kandungan Utama

Dalam contoh di atas, prompt masih agak terbuka, membolehkan LLM membuat keputusan bahagian dataset pra-latihannya yang relevan. Dengan corak reka bentuk _kandungan utama_, teks input dibahagikan kepada dua bahagian:

- arahan (tindakan)
- kandungan berkaitan (yang mempengaruhi tindakan)

Berikut adalah contoh di mana arahan adalah "ringkaskan ini dalam 2 ayat".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Pelengkap (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter adalah planet kelima dari Matahari dan yang terbesar dalam Sistem Suria. Ia adalah gergasi gas dengan jisim seribu satu daripada Matahari, tetapi dua setengah kali ganda daripada semua planet lain dalam Sistem Suria digabungkan. Jupiter adalah salah satu objek paling terang yang dapat dilihat dengan mata kasar di langit malam, dan telah diketahui oleh tamadun purba sejak sebelum sejarah direkodkan. Ia dinamakan sempena dewa Rom, Jupiter.[19] Apabila dilihat dari Bumi, Jupiter boleh cukup terang sehingga cahaya pantulannya mewujudkan bayang yang kelihatan,[20] dan secara purata adalah objek semula jadi ketiga paling terang di langit malam selepas Bulan dan Zuhrah. <br/> **Ringkaskan ini dalam 2 ayat pendek** | Jupiter, planet kelima dari Matahari, adalah yang terbesar dalam Sistem Suria dan dikenal pasti sebagai salah satu objek paling terang di langit malam. Dinamakan sempena dewa Rom Jupiter, ia adalah gergasi gas yang jisimnya dua setengah kali ganda daripada semua planet lain dalam Sistem Suria digabungkan. |

Segmen kandungan utama boleh digunakan dengan pelbagai cara untuk menggerakkan arahan yang lebih berkesan:

- **Contoh** - sebagai pengganti memberitahu model apa yang perlu dilakukan dengan arahan eksplisit, berikan contoh apa yang perlu dilakukan dan biarkan ia meneka corak.
- **Petunjuk** - ikut arahan dengan "petunjuk" yang memulakan pelengkap, membimbing model ke arah respons yang lebih relevan.
- **Templat** - ini adalah 'resipi' boleh ulang untuk prompt dengan tempat letak (pembolehubah) yang boleh disesuaikan dengan data untuk kes penggunaan khusus.

Mari terokai ini dalam tindakan.

### Menggunakan Contoh

Ini adalah pendekatan di mana anda menggunakan kandungan utama untuk "memberi makan model" beberapa contoh output yang diingini untuk arahan tertentu, dan membiarkannya meneka corak output yang diingini. Berdasarkan jumlah contoh yang diberikan, kita boleh mempunyai zero-shot prompting, one-shot prompting, few-shot prompting dan lain-lain.

Prompt kini terdiri daripada tiga komponen:

- Penerangan tugas
- Beberapa contoh output yang diingini
- Permulaan contoh baru (yang menjadi penerangan tugas tersirat)

| Jenis Pembelajaran | Prompt (Input)                                                                                                                                        | Pelengkap (Output)         |
| :------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot           | "The Sun is Shining". Terjemah ke dalam Bahasa Sepanyol                                                                                              | "El Sol está brillando".    |
| One-shot            | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot            | Pemain berlari di pangkalan => Bola Sepak <br/> Pemain memukul ace => Tenis <br/> Pemain memukul enam => Kriket <br/> Pemain membuat slam-dunk =>     | Bola Keranjang              |
|                     |                                                                                                                                                       |                             |

Perhatikan bagaimana kita perlu memberi arahan eksplisit ("Terjemah ke Bahasa Sepanyol") dalam zero-shot prompting, tetapi ia dijangka dalam contoh one-shot prompting. Contoh few-shot menunjukkan bagaimana menambah lebih banyak contoh membolehkan model membuat inferens yang lebih tepat tanpa arahan tambahan.

### Petunjuk Prompt

Satu lagi teknik menggunakan kandungan utama adalah memberikan _petunjuk_ dan bukannya contoh. Dalam kes ini, kita memberi model satu dorongan ke arah yang betul dengan _memulakannya_ dengan serpihan yang mencerminkan format respons yang diingini. Model kemudian "mengambil petunjuk" untuk meneruskan dengan cara itu.

| Bilangan Petunjuk | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Pelengkap (Output)                                                                                                                                                                                                                                                                                       |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                 | Jupiter adalah planet kelima dari Matahari dan yang terbesar dalam Sistem Suria. Ia adalah gergasi gas dengan jisim seribu satu daripada Matahari, tetapi dua setengah kali ganda daripada semua planet lain dalam Sistem Suria digabungkan. Jupiter adalah salah satu objek paling terang yang dapat dilihat dengan mata kasar di langit malam, dan telah diketahui oleh tamadun purba sejak sebelum sejarah direkodkan. <br/>**Ringkaskan Ini**                                       | Jupiter adalah planet terbesar dalam Sistem Suria kita dan yang kelima dari Matahari. Ia adalah gergasi gas dengan jisim 1/1000 Matahari, tetapi lebih berat daripada semua planet lain digabungkan. Tamadun purba telah lama mengetahui tentang Jupiter, dan ia mudah dilihat di langit malam. |
| 1              | Musytari adalah planet kelima dari Matahari dan yang terbesar dalam Sistem Suria. Ia adalah gergasi gas dengan jisim satu per seribu daripada Matahari, tetapi dua setengah kali ganda daripada semua planet lain dalam Sistem Suria digabungkan. Musytari adalah salah satu objek paling terang yang dapat dilihat dengan mata kasar di langit malam, dan telah dikenali oleh tamadun kuno sejak sebelum sejarah tercatat. <br/>**Ringkaskan Ini** <br/> Apa yang kita pelajari ialah Musytari | adalah planet kelima dari Matahari dan yang terbesar dalam Sistem Suria. Ia adalah gergasi gas dengan jisim satu per seribu daripada Matahari, tetapi dua setengah kali ganda daripada semua planet lain digabungkan. Ia mudah dilihat dengan mata kasar dan telah dikenali sejak zaman kuno.                        |
| 2              | Musytari adalah planet kelima dari Matahari dan yang terbesar dalam Sistem Suria. Ia adalah gergasi gas dengan jisim satu per seribu daripada Matahari, tetapi dua setengah kali ganda daripada semua planet lain dalam Sistem Suria digabungkan. Musytari adalah salah satu objek paling terang yang dapat dilihat dengan mata kasar di langit malam, dan telah dikenali oleh tamadun kuno sejak sebelum sejarah tercatat. <br/>**Ringkaskan Ini** <br/> 3 Fakta Teratas Yang Kita Pelajari:   | 1. Musytari adalah planet kelima dari Matahari dan yang terbesar dalam Sistem Suria. <br/> 2. Ia adalah gergasi gas dengan jisim satu per seribu daripada Matahari...<br/> 3. Musytari telah kelihatan dengan mata kasar sejak zaman kuno ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt Templates

Templat prompt adalah _resepi yang telah ditetapkan untuk sesuatu prompt_ yang boleh disimpan dan digunakan semula apabila perlu, untuk memberikan pengalaman pengguna yang lebih konsisten secara besar-besaran. Dalam bentuk paling mudah, ia hanyalah koleksi contoh prompt seperti [yang ini dari OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) yang menyediakan komponen prompt interaktif (mesej pengguna dan sistem) serta format permintaan berasaskan API - untuk menyokong penggunaan semula.

Dalam bentuk yang lebih kompleks seperti [contoh ini dari LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) ia mengandungi _tempat letak_ yang boleh digantikan dengan data daripada pelbagai sumber (input pengguna, konteks sistem, sumber data luar dll.) untuk menjana prompt secara dinamik. Ini membolehkan kita mencipta perpustakaan prompt yang boleh digunakan semula untuk menjana pengalaman pengguna yang konsisten **secara berprogram** secara skala besar.

Akhir sekali, nilai sebenar templat terletak pada kebolehan untuk mencipta dan menerbitkan _perpustakaan prompt_ untuk domain aplikasi khusus - di mana templat prompt kini _dioptimumkan_ untuk mencerminkan konteks spesifik aplikasi atau contoh yang menjadikan respon lebih relevan dan tepat untuk audiens pengguna yang disasarkan. Repositori [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) adalah contoh hebat pendekatan ini, mengumpul perpustakaan prompt untuk domain pendidikan dengan penekanan pada objektif utama seperti perancangan pelajaran, reka bentuk kurikulum, bimbingan pelajar dan sebagainya.

## Supporting Content

Jika kita menganggap pembinaan prompt sebagai mempunyai arahan (tugas) dan sasaran (kandungan utama), maka _kandungan sekunder_ adalah seperti konteks tambahan yang kita berikan untuk **mempengaruhi output dengan sesuatu cara**. Ia boleh jadi parameter penalaan, arahan format, taksonomi topik dan sebagainya yang membantu model _menyesuaikan_ jawapannya agar sesuai dengan objektif atau jangkaan pengguna yang dikehendaki.

Contohnya: Diberikan katalog kursus dengan metadata meluas (nama, penerangan, tahap, tanda metadata, pengajar dll.) untuk semua kursus yang ada dalam kurikulum:

- kita boleh mendefinisikan arahan untuk "ringkaskan katalog kursus untuk Musim Gugur 2023"
- kita boleh menggunakan kandungan utama untuk menyediakan beberapa contoh output yang dikehendaki
- kita boleh menggunakan kandungan sekunder untuk mengenal pasti 5 "tag" paling utama.

Kini, model boleh memberikan ringkasan dalam format yang ditunjukkan oleh beberapa contoh - tetapi jika hasil itu mempunyai pelbagai tag, ia boleh mengutamakan 5 tag yang dikenalpasti dalam kandungan sekunder.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #3:
Prompt Engineering Techniques.
What are some basic techniques for prompt engineering?
Illustrate it with some exercises.
-->

## Amalan Terbaik Dalam Prompting

Sekarang kita sudah tahu bagaimana prompt boleh _dibina_, kita boleh mula berfikir tentang bagaimana untuk _mereka bentuk_ ia supaya mencerminkan amalan terbaik. Kita boleh fikirkan ini sebagai dua bahagian - mempunyai _mindset_ yang betul dan menggunakan _teknik_ yang betul.

### Mindset Kejuruteraan Prompt

Kejuruteraan prompt adalah proses cuba-jaya jadi ingat tiga faktor panduan luas ini:

1. **Pemahaman Domain Penting.** Ketepatan dan relevansi jawapan bergantung pada _domain_ di mana aplikasi atau pengguna beroperasi. Gunakan intuisi dan kepakaran domain anda untuk **menyesuaikan teknik** dengan lebih lanjut. Contohnya, tetapkan _personaliti khusus domain_ dalam prompt sistem anda, atau gunakan _templat khusus domain_ dalam prompt pengguna. Berikan kandungan sekunder yang mencerminkan konteks khusus domain, atau gunakan _petanda dan contoh khusus domain_ untuk membimbing model ke arah corak penggunaan yang dikenali.

2. **Pemahaman Model Penting.** Kita tahu model adalah bersifat stokastik secara semula jadi. Tetapi pelaksanaan model juga boleh berbeza dari segi set data latihan yang digunakan (pengetahuan pra-latih), keupayaan yang disediakan (misalnya, melalui API atau SDK) dan jenis kandungan yang dioptimumkan (contohnya, kod vs imej vs teks). Fahami kekuatan dan had model yang anda gunakan, dan gunakan pengetahuan itu untuk _mengutamakan tugasan_ atau bina _templat khusus_ yang dioptimumkan untuk kemampuan model.

3. **Ulangan & Pengesahan Penting.** Model sedang berkembang dengan cepat, begitu juga teknik untuk kejuruteraan prompt. Sebagai pakar domain, anda mungkin mempunyai konteks atau kriteria lain untuk _aplikasi_ anda yang mungkin tidak sesuai untuk komuniti lebih luas. Gunakan alat & teknik kejuruteraan prompt untuk "memulakan" pembinaan prompt, kemudian ulang dan sahkan keputusan menggunakan intuisi dan kepakaran domain anda sendiri. Rekodkan penemuan anda dan cipta **pangkalan pengetahuan** (contohnya, perpustakaan prompt) yang boleh digunakan sebagai asas baru oleh orang lain, untuk ulangan lebih cepat pada masa depan.

## Amalan Terbaik

Mari lihat amalan terbaik biasa yang disyorkan oleh pengamal [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) dan [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Apa                              | Kenapa                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Nilai model terkini.              | Generasi model baru biasanya mempunyai ciri dan kualiti yang lebih baik - tetapi mungkin juga menyebabkan kos lebih tinggi. Nilai impaknya, kemudian buat keputusan migrasi.                                                                       |
| Pisahkan arahan & konteks        | Periksa jika model/pembekal anda mentakrifkan _pembatas_ untuk membezakan arahan, kandungan utama dan sekunder dengan lebih jelas. Ini boleh membantu model memberikan berat yang lebih tepat kepada token.                                          |
| Jadilah spesifik dan jelas        | Berikan lebih banyak butiran tentang konteks yang diingini, hasil, panjang, format, gaya dan sebagainya. Ini akan memperbaiki kualiti dan konsistensi jawapan. Simpan resepi dalam templat yang boleh digunakan semula.                              |
| Jadilah deskriptif, gunakan contoh | Model mungkin memberi respon lebih baik dengan pendekatan "tunjuk dan ceritakan". Mulakan dengan pendekatan `zero-shot` di mana anda memberi arahan (tanpa contoh) kemudian cuba `few-shot` sebagai penambahbaikan, menyediakan beberapa contoh output yang dikehendaki. Gunakan analogi. |
| Gunakan petanda untuk mulakan jawapan | Galakkan ia ke arah hasil yang diingini dengan memberi kata atau frasa pembuka yang boleh digunakan sebagai titik permulaan untuk respon.                                                                                                        |
| Gandakan                        | Kadang-kadang anda perlu mengulangi arahan kepada model. Beri arahan sebelum dan selepas kandungan utama, gunakan arahan dan petanda, dll. Ulang dan sahkan untuk lihat apa yang berkesan.                                                         |
| Susunan Penting                  | Susunan informasi yang anda berikan kepada model mungkin mempengaruhi output, walaupun dalam contoh pembelajaran, terima kasih kepada bias keakraban. Cuba pilihan berbeza untuk lihat apa yang terbaik.                                             |
| Beri model "jalan keluar"         | Beri model satu jenis jawapan _fallback_ yang boleh diberikan jika ia tidak dapat menyiapkan tugasan atas apa jua sebab. Ini boleh mengurangkan peluang model menghasilkan jawapan palsu atau direka-reka.                                            |
|                                  |                                                                                                                                                                                                                                                     |

Seperti amalan terbaik lain, ingat bahawa _pengalaman anda mungkin berbeza_ bergantung pada model, tugasan dan domain. Gunakan ini sebagai titik permulaan, dan ulang supaya anda dapat mengetahui apa yang terbaik untuk anda. Selalu nilai semula proses kejuruteraan prompt anda apabila model dan alat baru tersedia, dengan fokus pada kebolehskalaan proses dan kualiti respons.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Tugasan

Tahniah! Anda telah sampai ke penghujung pelajaran! Kini masa untuk menguji beberapa konsep dan teknik itu dengan contoh sebenar!

Untuk tugasan kita, kita akan menggunakan Jupyter Notebook dengan latihan yang boleh anda siapkan secara interaktif. Anda juga boleh melanjutkan Notebook dengan sel Markdown dan Kod anda sendiri untuk meneroka idea dan teknik secara sendiri.

### Untuk memulakan, buat forking repo, kemudian

- (Disyorkan) Lancarkan GitHub Codespaces
- (Sebagai alternatif) Klon repo ke peranti tempatan dan gunakan dengan Docker Desktop
- (Sebagai alternatif) Buka Notebook dengan persekitaran runtime Notebook pilihan anda.

### Seterusnya, konfigurasikan pembolehubah persekitaran anda

- Salin fail `.env.copy` di akar repo ke `.env` dan isi nilai `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` dan `AZURE_OPENAI_DEPLOYMENT`. Kembali ke [bahagian Learning Sandbox](#sandbox-pembelajaran) untuk belajar caranya.

### Seterusnya, buka Jupyter Notebook

- Pilih kernel runtime. Jika menggunakan pilihan 1 atau 2, hanya pilih kernel Python 3.10.x lalai yang disediakan oleh bekas pembangunan.

Anda sudah siap untuk menjalankan latihan. Perlu diingat bahawa tiada jawapan _betul atau salah_ di sini - hanya meneroka pilihan dengan cuba-jaya dan membangun intuisi untuk apa yang berkesan untuk model dan domain aplikasi tertentu.

_Untuk sebab ini tiada segmen Penyelesaian Kod dalam pelajaran ini. Sebaliknya, Notebook akan mempunyai sel Markdown bertajuk "My Solution:" yang menunjukkan satu contoh output untuk rujukan._

 <!--
LESSON TEMPLATE:
Wrap the section with a summary and resources for self-guided learning.
-->

## Pemeriksaan Pengetahuan

Yang manakah antara berikut adalah prompt yang baik mengikut beberapa amalan terbaik yang munasabah?

1. Tunjukkan saya gambar kereta merah
2. Tunjukkan saya gambar kereta merah buatan Volvo dan model XC90 diparkir di tebing dengan matahari terbenam
3. Tunjukkan saya gambar kereta merah buatan Volvo dan model XC90

A: 2, ia adalah prompt terbaik kerana memberikan butiran tentang "apa" dan masuk ke spesifik (bukan kereta sebarang tetapi buatan dan model tertentu) selain menerangkan suasana keseluruhan. 3 adalah pilihan kedua terbaik kerana juga mengandungi banyak penerangan.

## 🚀 Cabaran

Lihat jika anda boleh menggunakan teknik "petanda" dengan prompt: Lengkapkan ayat "Tunjukkan saya gambar kereta merah buatan Volvo dan ". Apa yang ia balas, dan bagaimana anda akan memperbaikinya?

## Kerja Hebat! Teruskan Pembelajaran Anda

Ingin belajar lebih lanjut tentang pelbagai konsep Kejuruteraan Prompt? Pergi ke [halaman pembelajaran lanjut](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk mencari sumber hebat lain tentang topik ini.

Teruskan ke Pelajaran 5 di mana kami akan melihat [teknik prompting lanjutan](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->