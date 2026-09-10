# Asas Kejuruteraan Prompt

[![Asas Kejuruteraan Prompt](../../../translated_images/ms/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Pengenalan
Modul ini merangkumi konsep dan teknik penting untuk mencipta prompt yang berkesan dalam model AI generatif. Cara anda menulis prompt kepada LLM juga penting. Prompt yang direka dengan teliti boleh menghasilkan respons yang lebih berkualiti. Tetapi apakah sebenarnya maksud istilah seperti _prompt_ dan _kejuruteraan prompt_? Dan bagaimana saya boleh memperbaiki _input_ prompt yang saya hantar kepada LLM? Ini adalah soalan yang akan kita cuba jawab dalam bab ini dan bab seterusnya.

_AI Generatif_ mampu mencipta kandungan baru (contohnya, teks, imej, audio, kod dan lain-lain) sebagai respons kepada permintaan pengguna. Ia mencapainya dengan menggunakan _Model Bahasa Besar_ seperti siri GPT OpenAI ("Generative Pre-trained Transformer") yang dilatih untuk menggunakan bahasa semula jadi dan kod.

Pengguna kini boleh berinteraksi dengan model ini menggunakan paradigma yang biasa seperti chat, tanpa memerlukan kepakaran teknikal atau latihan. Model-model ini adalah _berasaskan prompt_ - pengguna menghantar input teks (prompt) dan mendapat kembali respons AI (penyempurnaan). Mereka kemudian boleh "berbual dengan AI" secara berterusan, dalam perbualan berbilang pusingan, memperhalusi prompt mereka sehingga respons memenuhi jangkaan mereka.

"Prompt" kini menjadi _antara muka pengaturcaraan_ utama untuk aplikasi AI generatif, memberitahu model apa yang perlu dilakukan dan mempengaruhi kualiti respons yang dikembalikan. "Kejuruteraan Prompt" adalah bidang kajian yang berkembang pesat yang memberi tumpuan kepada _rekabentuk dan pengoptimuman_ prompt untuk menghasilkan respons yang konsisten dan berkualiti secara besar-besaran.

## Matlamat Pembelajaran

Dalam pelajaran ini, kita akan belajar apa itu Kejuruteraan Prompt, mengapa ia penting, dan bagaimana kita boleh menghasilkan prompt yang lebih berkesan untuk model dan objektif aplikasi tertentu. Kita akan memahami konsep teras dan amalan terbaik untuk kejuruteraan prompt - dan belajar mengenai persekitaran "sandbox" interaktif Jupyter Notebooks di mana kita boleh melihat konsep ini diaplikasikan dalam contoh sebenar.

Pada akhir pelajaran ini kita akan dapat:

1. Jelaskan apa itu kejuruteraan prompt dan mengapa ia penting.
2. Huraikan komponen sebuah prompt dan bagaimana ia digunakan.
3. Pelajari amalan terbaik dan teknik untuk kejuruteraan prompt.
4. Terapkan teknik yang dipelajari pada contoh sebenar, menggunakan endpoint OpenAI.

## Istilah Utama

Kejuruteraan Prompt: Amalan mereka bentuk dan memurnikan input untuk membimbing model AI menghasilkan output yang diingini.
Pen-tokenan: Proses menukar teks menjadi unit yang lebih kecil, dipanggil token, yang boleh difahami dan diproses oleh model.
LLM Diselaraskan Arahan: Model Bahasa Besar (LLM) yang telah disesuaikan dengan arahan tertentu untuk meningkatkan ketepatan dan kaitan respons mereka.

## Sandbox Pembelajaran

Kejuruteraan prompt kini lebih merupakan seni daripada sains. Cara terbaik untuk memperbaiki intuisi kita adalah dengan _berlatih lebih banyak_ dan mengamalkan pendekatan cubaan dan ralat yang menggabungkan kepakaran domain aplikasi dengan teknik yang disyorkan dan pengoptimuman model khusus.

Jupyter Notebook yang menyertai pelajaran ini menyediakan persekitaran _sandbox_ di mana anda boleh mencuba apa yang anda pelajari - secara langsung atau sebagai sebahagian daripada cabaran kod di akhir. Untuk melaksanakan latihan, anda memerlukan:

1. **Kunci API Azure OpenAI** - endpoint perkhidmatan untuk LLM yang telah digunakan.
2. **Runtime Python** - di mana Notebook boleh dijalankan.
3. **Pemboleh Ubah Persekitaran Tempatan** - _lengkapkan langkah [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) sekarang untuk bersedia_.

Notebook ini menyediakan latihan _pemula_ - tetapi anda digalakkan untuk menambah bahagian _Markdown_ (keterangan) dan _Kod_ (permintaan prompt) anda sendiri untuk mencuba lebih banyak contoh atau idea - dan membina intuisi anda untuk reka bentuk prompt.

## Panduan Bergambar

Mahu gambaran besar apa yang diliputi pelajaran ini sebelum anda mula? Lihat panduan bergambar ini, yang memberi anda gambaran tentang topik utama yang dibincangkan dan perkara penting untuk difikirkan dalam setiap satu. Peta pelajaran membawa anda dari memahami konsep dan cabaran teras kepada menangani mereka dengan teknik dan amalan terbaik kejuruteraan prompt yang relevan. Perhatikan bahawa bahagian "Teknik Lanjutan" dalam panduan ini merujuk kepada kandungan yang dibincangkan dalam bab _seterusnya_ dalam kurikulum ini.

![Panduan Bergambar Kejuruteraan Prompt](../../../translated_images/ms/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Permulaan Kita

Sekarang, mari bincangkan bagaimana _topik ini_ berkaitan dengan misi permulaan kami untuk [membawa inovasi AI ke pendidikan](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Kami mahu membina aplikasi pembelajaran berkuasa AI yang _dipersonalisasi_ - jadi mari fikirkan bagaimana pengguna berbeza aplikasi kami mungkin "merancang" prompt:

- **Pentadbir** mungkin meminta AI untuk _menganalisis data kurikulum bagi mengenal pasti jurang dalam liputan_. AI boleh meringkaskan hasil atau memvisualisasikannya dengan kod.
- **Pendidik** mungkin meminta AI untuk _menghasilkan rancangan pelajaran untuk sasaran audiens dan topik tertentu_. AI boleh membina rancangan yang dipersonalisasi dalam format yang ditetapkan.
- **Pelajar** mungkin meminta AI untuk _membimbing mereka dalam subjek yang sukar_. AI kini boleh membimbing pelajar dengan pelajaran, petunjuk & contoh yang disesuaikan dengan tahap mereka.

Itu baru permulaan sahaja. Lihatlah [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - perpustakaan prompt sumber terbuka yang dikurasi oleh pakar pendidikan - untuk mendapatkan gambaran lebih luas tentang kemungkinan! _Cuba jalankan beberapa prompt itu dalam sandbox atau menggunakan OpenAI Playground untuk melihat apa yang berlaku!_

<!--
TEMPEL PELAJARAN:
Unit ini harus merangkumi konsep teras #1.
Memperkukuh konsep dengan contoh dan rujukan.

KONSEP #1:
Kejuruteraan Prompt.
Definisikan dan terangkan mengapa ia diperlukan.
-->

## Apa itu Kejuruteraan Prompt?

Kita mulakan pelajaran ini dengan mendefinisikan **Kejuruteraan Prompt** sebagai proses _mereka bentuk dan mengoptimumkan_ input teks (prompt) untuk menghasilkan respons (penyempurnaan) yang konsisten dan berkualiti untuk objektif aplikasi dan model tertentu. Kita boleh fikirkan ini sebagai proses 2 langkah:

- _mereka bentuk_ prompt awal untuk model dan objektif tertentu
- _memurnikan_ prompt secara berulang untuk memperbaiki kualiti respons

Ini sememangnya proses cuba-dan-salah yang memerlukan intuisi dan usaha pengguna untuk mendapatkan hasil optimum. Jadi mengapa ia penting? Untuk menjawab soalan itu, kita perlu faham tiga konsep:

- _Pen-tokenan_ = bagaimana model "melihat" prompt
- _LLM Asas_ = bagaimana model asas "memproses" prompt
- _LLM Diselaraskan Arahan_ = bagaimana model kini boleh melihat "tugas"

### Pen-tokenan

LLM melihat prompt sebagai _urutan token_ di mana model berbeza (atau versi model) boleh men-token-kan prompt yang sama dengan cara yang berbeza. Oleh kerana LLM dilatih menggunakan token (bukan teks kasar), cara prompt ditoken-kan mempunyai kesan langsung terhadap kualiti respons yang dihasilkan.

Untuk mendapatkan intuisi bagaimana pen-tokenan berfungsi, cuba alat seperti [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) yang dipaparkan di bawah. Salin prompt anda - dan lihat bagaimana ia ditukar menjadi token, beri perhatian pada cara ruang putih dan tanda baca dikendalikan. Perhatikan contoh ini menunjukkan LLM yang lebih lama (GPT-3) - jadi mencubanya dengan model yang lebih baru mungkin menghasilkan keputusan yang berbeza.

![Pen-tokenan](../../../translated_images/ms/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Konsep: Model Asas

Setelah prompt ditoken-kan, fungsi utama ["LLM Asas"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (atau model asas) ialah meramalkan token dalam urutan itu. Oleh kerana LLM dilatih menggunakan dataset teks besar, mereka mempunyai pemahaman baik tentang hubungan statistik antara token dan boleh membuat ramalan itu dengan keyakinan tertentu. Perlu diingat mereka tidak memahami _makna_ perkataan dalam prompt atau token; mereka hanya melihat corak yang boleh mereka "lengkapkan" dengan ramalan seterusnya. Mereka boleh terus meramalkan urutan sehingga diberhentikan oleh intervensi pengguna atau kondisi yang telah ditetapkan.

Mahu lihat bagaimana penyempurnaan berasaskan prompt berfungsi? Masukkan prompt di atas ke dalam [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) dengan tetapan lalai. Sistem dikonfigurasikan untuk menganggap prompt sebagai permintaan maklumat - jadi anda harus melihat penyempurnaan yang memenuhi konteks ini.

Tetapi bagaimana jika pengguna mahu melihat sesuatu yang spesifik yang memenuhi kriteria atau objektif tugas? Di sinilah LLM _diselaraskan arahan_ masuk ke gambar.

![Sempurnaan Chat LLM Asas](../../../translated_images/ms/04-playground-chat-base.65b76fcfde0caa67.webp)

### Konsep: LLM Diselaraskan Arahan

Sebuah [LLM Diselaraskan Arahan](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) bermula dengan model asas dan menala semula dengan contoh atau pasangan input/output (contohnya, "mesej" berbilang pusingan) yang mengandungi arahan jelas - dan respons dari AI cuba mengikuti arahan tersebut.

Ini menggunakan teknik seperti Pembelajaran Penguatan dengan Maklum Balas Manusia (RLHF) yang boleh melatih model untuk _mengikuti arahan_ dan _belajar dari maklum balas_ supaya menghasilkan respons yang lebih sesuai untuk aplikasi praktikal dan lebih relevan dengan objektif pengguna.

Mari cuba - tinjau semula prompt tadi, tetapi sekarang ubah _mesej sistem_ untuk memberikan arahan berikut sebagai konteks:

> _Ringkaskan kandungan yang diberikan untuk pelajar darjah dua. Kekalkan keputusan kepada satu perenggan dengan 3-5 titik peluru._

Lihat bagaimana hasilnya kini diselaraskan untuk mencerminkan matlamat dan format yang diingini? Seorang pendidik kini boleh terus menggunakan respons ini dalam slaid mereka untuk kelas tersebut.

![Sempurnaan Chat LLM Diselaraskan Arahan](../../../translated_images/ms/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Mengapa kita memerlukan Kejuruteraan Prompt?

Sekarang kita tahu bagaimana prompt diproses oleh LLM, mari bincangkan _kenapa_ kita memerlukan kejuruteraan prompt. Jawapannya terletak pada hakikat bahawa LLM semasa mempunyai beberapa cabaran yang menjadikan _penyempurnaan boleh dipercayai dan konsisten_ lebih sukar dicapai tanpa usaha membina dan mengoptimumkan prompt. Contohnya:

1. **Respons model adalah stokastik.** _Prompt yang sama_ mungkin menghasilkan respons berbeza dengan model atau versi model yang berbeza. Malah ia mungkin menghasilkan keputusan berbeza dengan _model yang sama_ pada masa berlainan. _Teknik kejuruteraan prompt boleh membantu kita mengurangkan variasi ini dengan menyediakan panduan yang lebih baik_.

1. **Model boleh mengarang respons.** Model dilatih dengan dataset yang _besar tetapi terhad_, bermakna mereka kurang pengetahuan mengenai konsep di luar skop latihan itu. Akibatnya, mereka boleh menghasilkan penyempurnaan yang tidak tepat, rekaan, atau terus bertentangan dengan fakta dikenali. _Teknik kejuruteraan prompt membantu pengguna mengenal pasti dan mengurangkan rekaan tersebut contohnya dengan meminta AI memberikan rujukan atau alasan_.

1. **Keupayaan model berbeza-beza.** Model atau generasi model baru mempunyai keupayaan yang lebih kaya tetapi juga membawa keunikan dan kompromi dalam kos & kerumitan. _Kejuruteraan prompt boleh membantu kita membangunkan amalan terbaik dan aliran kerja yang mengabstrak perbezaan dan menyesuaikan diri dengan keperluan khusus model secara mudah dan boleh skala_.

Mari lihat ini dalam tindakan di OpenAI atau Azure OpenAI Playground:

- Gunakan prompt yang sama dengan pelbagai penyebaran LLM (contoh, OpenAI, Azure OpenAI, Hugging Face) - adakah anda melihat variasi?
- Gunakan prompt yang sama berulang kali dengan penyebaran LLM yang _sama_ (contoh, Azure OpenAI playground) - bagaimana variasi ini berbeza?

### Contoh Rekaan

Dalam kursus ini, kami menggunakan istilah **"rekaan"** untuk merujuk fenomena di mana LLM kadang-kadang menghasilkan maklumat yang salah dari segi fakta disebabkan keterbatasan latihan atau kekangan lain. Anda mungkin juga pernah mendengar ia dirujuk sebagai _"halusinasi"_ dalam artikel popular atau kertas penyelidikan. Walau bagaimanapun, kami sangat mengesyorkan menggunakan istilah _"rekaan"_ supaya kita tidak menyifatkan perilaku ini secara antropomorfik dengan memberi sifat seperti manusia kepada hasil yang dipacu mesin. Ini juga menguatkan [garis panduan AI Bertanggungjawab](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) dari segi terminologi, menghapuskan istilah yang juga mungkin dianggap ofensif atau tidak inklusif dalam beberapa konteks.

Mahu mendapat gambaran bagaimana rekaan berlaku? Fikirkan prompt yang mengarahkan AI untuk menghasilkan kandungan untuk topik yang tidak wujud (untuk memastikan ia tidak dijumpai dalam set data latihan). Contohnya - saya cuba prompt ini:

> **Prompt:** hasilkan rancangan pelajaran tentang Perang Marikh 2076.

Carian web menunjukkan terdapat akaun fiksyen (contohnya, siri televisyen atau buku) mengenai perang Marikh - tetapi tiada pada tahun 2076. Akal sehat juga memberitahu bahawa 2076 adalah _masa depan_ dan oleh itu, tidak boleh dikaitkan dengan peristiwa sebenar.


Jadi apa yang berlaku apabila kita menjalankan arahan ini dengan pembekal LLM yang berbeza?

> **Respons 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/ms/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Respons 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/ms/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Respons 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/ms/04-fabrication-huggingchat.faf82a0a51278956.webp)

Seperti yang dijangkakan, setiap model (atau versi model) menghasilkan respons yang sedikit berbeza disebabkan oleh tingkah laku stokastik dan variasi keupayaan model. Contohnya, satu model mensasarkan audiens darjah 8 manakala yang lain menganggap pengguna pelajar sekolah menengah. Tetapi kesemua tiga model tersebut menghasilkan respons yang boleh meyakinkan pengguna yang tidak dimaklumkan bahawa peristiwa itu adalah benar.

Teknik rekabentuk arahan seperti _metaprompting_ dan _konfigurasi suhu_ boleh mengurangkan fabrikasi model sehingga ke peringkat tertentu. Rekabentuk arahan baharu _arsitektur_ juga menggabungkan alat dan teknik baharu secara lancar ke dalam aliran arahan, untuk mengurangkan atau mengawal sebahagian kesan ini.

## Kajian Kes: GitHub Copilot

Mari kita akhiri bahagian ini dengan mendapatkan gambaran tentang bagaimana rekabentuk arahan digunakan dalam penyelesaian sebenar dengan melihat satu Kajian Kes: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot adalah "Rakan Pengaturcara AI" anda - ia menukar arahan teks kepada pelengkap kod dan diintegrasikan dalam persekitaran pembangunan anda (contohnya, Visual Studio Code) untuk pengalaman pengguna yang lancar. Seperti yang didokumenkan dalam siri blog di bawah, versi awal adalah berdasarkan model OpenAI Codex - dengan jurutera segera menyedari keperluan untuk melaraskan model dan membangunkan teknik rekabentuk arahan yang lebih baik untuk meningkatkan kualiti kod. Pada Julai, mereka [memperkenalkan model AI yang dipertingkatkan yang melangkaui Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) untuk cadangan yang lebih pantas.

Baca pos-pos ini mengikut susunan, untuk mengikuti perjalanan pembelajaran mereka.

- **Mei 2023** | [GitHub Copilot semakin faham kod anda dengan lebih baik](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mei 2023** | [Dalam GitHub: Bekerjasama dengan LLM di sebalik GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Cara menulis arahan yang lebih baik untuk GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot melangkaui Codex dengan model AI yang dipertingkatkan](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Panduan Pembangun untuk Rekabentuk Arahan dan LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Cara membina aplikasi LLM perusahaan: Pengajaran dari GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Anda juga boleh melayari [blog Kejuruteraan](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) mereka untuk lebih banyak pos seperti [yang ini](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) yang menunjukkan bagaimana model dan teknik ini _dikuasakan_ untuk memacu aplikasi dunia nyata.

---

<!--
TEMPEL PELAJARAN:
Unit ini harus merangkumi konsep teras #2.
Memperkuat konsep dengan contoh dan rujukan.

KONSEP #2:
Reka Bentuk Arahan.
Dihuraikan dengan contoh.
-->

## Pembinaan Arahan

Kita telah melihat mengapa rekabentuk arahan itu penting - sekarang mari kita fahami bagaimana arahan _dibina_ supaya kita boleh menilai teknik berbeza untuk reka bentuk arahan yang lebih berkesan.

### Arahan Asas

Mari bermula dengan arahan asas: input teks dihantar ke model tanpa konteks lain. Berikut adalah contoh - apabila kita menghantar beberapa perkataan pertama lagu kebangsaan AS ke OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) ia serta-merta _melengkapkan_ respons dengan baris seterusnya, menggambarkan tingkah laku ramalan asas.

| Arahan (Input)     | Pelengkap (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Ia kedengaran seperti anda memulakan lirik "The Star-Spangled Banner," lagu kebangsaan Amerika Syarikat. Lirik penuh adalah ...              |

### Arahan Kompleks

Sekarang mari kita tambah konteks dan arahan kepada arahan asas itu. [Chat Completion API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) membolehkan kita membina arahan kompleks sebagai koleksi _mesej_ dengan:

- Pasangan input/output yang mencerminkan input _pengguna_ dan respons _pembantu_.
- Mesej sistem menetapkan konteks untuk tingkah laku atau personaliti pembantu.

Permintaan kini dalam bentuk di bawah, di mana _tokenisasi_ secara berkesan menangkap maklumat berkaitan dari konteks dan perbualan. Kini, mengubah konteks sistem boleh memberi impak yang sama terhadap kualiti pelengkap seperti input pengguna yang diberikan.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Arahan Berpanduan

Dalam contoh di atas, arahan pengguna adalah pertanyaan teks mudah yang boleh ditafsirkan sebagai permintaan maklumat. Dengan arahan _berpanduan_, kita boleh menggunakan teks itu untuk memperincikan tugas dengan lebih detail, memberikan panduan lebih baik kepada AI. Berikut adalah contoh:

| Arahan (Input)                                                                                                                                                                                                                         | Pelengkap (Output)                                                                                                        | Jenis Arahan       |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Tulis perihalan tentang Perang Saudara                                                                                                                                                                                                | _mengembalikan perenggan ringkas_                                                                                        | Mudah              |
| Tulis perihalan tentang Perang Saudara. Berikan tarikh dan peristiwa utama serta terangkan kepentingannya                                                                                                                              | _mengembalikan perenggan diikuti oleh senarai tarikh peristiwa utama dengan penerangan_                                   | Kompleks            |
| Tulis perihalan Perang Saudara dalam 1 perenggan. Berikan 3 titik peluru dengan tarikh penting dan kepentingannya. Berikan 3 lagi titik peluru dengan tokoh bersejarah utama dan sumbangan mereka. Pulangkan output sebagai fail JSON                | _mengembalikan maklumat lebih terperinci dalam kotak teks, diformatkan sebagai JSON yang boleh anda salin tampal ke fail dan sahkan bila perlu_ | Kompleks. Diformat. |

## Kandungan Utama

Dalam contoh di atas, arahan masih agak terbuka, membolehkan LLM memutuskan bahagian dataset terlatih sebelumnya yang relevan. Dengan corak reka bentuk _kandungan utama_, teks input dibahagikan kepada dua bahagian:

- satu arahan (tindakan)
- kandungan berkaitan (yang mempengaruhi tindakan)

Berikut adalah contoh di mana arahan adalah "ringkaskan ini dalam 2 ayat".

| Arahan (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Pelengkap (Output)                                                                                                                                                                                                                                                                             |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Musytari adalah planet kelima dari Matahari dan yang terbesar dalam Sistem Suria. Ia adalah gergasi gas dengan jisim satu per seribu jisim Matahari, tetapi dua setengah kali ganda daripada semua planet lain dalam Sistem Suria digabungkan. Musytari adalah antara objek paling terang yang terlihat dengan mata telanjang di langit malam, dan telah diketahui oleh tamadun kuno sejak sebelum sejarah tercatat. Ia dinamakan sempena dewa Rom Musytari.[19] Apabila dilihat dari Bumi, Musytari boleh cukup terang untuk cahaya pantulannya menimbulkan bayang yang kelihatan,[20] dan secara purata merupakan objek semula jadi ketiga paling terang di langit malam selepas Bulan dan Zuhrah. <br/> **Ringkaskan ini dalam 2 ayat pendek** | Musytari, planet kelima dari Matahari, adalah yang terbesar dalam Sistem Suria dan diketahui sebagai salah satu objek paling terang di langit malam. Dinamakan sempena dewa Rom Musytari, ia adalah gergasi gas yang jisimnya dua setengah kali ganda semua planet lain di Sistem Suria digabungkan. |

Segmen kandungan utama boleh digunakan dalam pelbagai cara untuk menghasilkan arahan yang lebih berkesan:

- **Contoh** - bukannya memberitahu model apa yang perlu dibuat dengan arahan jelas, berikan contoh apa yang perlu dibuat dan biarkan ia mengesyaki corak tersebut.
- **Isyarat** - ikut arahan dengan "isyarat" yang mencetus pelengkap, mengawal model ke arah respons yang lebih relevan.
- **Templat** - ini adalah 'resipi' yang boleh diulang untuk arahan dengan ruang letak (pembolehubah) yang boleh disesuaikan dengan data untuk kes penggunaan tertentu.

Mari kita terokai ini dalam tindakan.

### Menggunakan Contoh

Ini adalah pendekatan di mana anda menggunakan kandungan utama untuk "memberi makan model" dengan beberapa contoh output yang diingini untuk arahan tertentu, dan biarkan ia mengesyaki corak output yang diingini. Berdasarkan bilangan contoh yang diberi, kita boleh ada zero-shot, one-shot, few-shot prompting dll.

Arahan kini terdiri daripada tiga komponen:

- Penerangan tugas
- Beberapa contoh output yang diingini
- Permulaan contoh baru (yang menjadi penerangan tugas secara tidak langsung)

| Jenis Pembelajaran | Arahan (Input)                                                                                                                                        | Pelengkap (Output)         |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot          | "The Sun is Shining". Terjemahkan ke Sepanyol                                                                                                      | "El Sol está brillando".    |
| One-shot           | "The Sun is Shining" => "El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                | "Es un día frío y ventoso". |
| Few-shot           | Pemain berlari di base => Besbol <br/> Pemain memukul ace => Tenis <br/> Pemain memukul enam => Kriket <br/> Pemain membuat slam-dunk =>              | Bola Keranjang             |
|                    |                                                                                                                                                       |                             |

Perhatikan bagaimana kita perlu memberikan arahan jelas ("Terjemahkan ke Sepanyol") dalam zero-shot prompting, tetapi ia disyaki dalam contoh one-shot. Contoh few-shot menunjukkan bagaimana menambah lebih banyak contoh membolehkan model membuat inferens yang lebih tepat tanpa arahan tambahan.

### Isyarat Arahan

Teknik lain menggunakan kandungan utama adalah dengan menyediakan _isyarat_ dan bukannya contoh. Dalam kes ini, kita memberi model dorongan ke arah yang betul dengan _mulakan_ dengan petikan yang mencerminkan format respons yang diingini. Model kemudian "mengambil isyarat" untuk meneruskan dalam gaya tersebut.

| Bilangan Isyarat | Arahan (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Pelengkap (Output)                                                                                                                                                                                                                                                                                       |
| :--------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                | Musytari adalah planet kelima dari Matahari dan yang terbesar dalam Sistem Suria. Ia adalah gergasi gas dengan jisim satu per seribu jisim Matahari, tetapi dua setengah kali ganda daripada semua planet lain dalam Sistem Suria digabungkan. Musytari adalah antara objek paling terang yang terlihat dengan mata telanjang di langit malam, dan telah diketahui oleh tamadun kuno sejak sebelum sejarah tercatat. <br/>**Ringkaskan Ini**                              | Musytari adalah planet terbesar dalam Sistem Suria kita dan planet kelima dari Matahari. Ia adalah gergasi gas dengan jisim 1/1000 daripada Matahari, tetapi lebih berat daripada semua planet lain digabungkan. Tamadun kuno telah mengetahui tentang Musytari untuk masa yang lama, dan ia mudah dilihat di langit malam.    |
| 1                | Musytari adalah planet kelima dari Matahari dan yang terbesar dalam Sistem Suria. Ia adalah gergasi gas dengan jisim satu per seribu jisim Matahari, tetapi dua setengah kali ganda daripada semua planet lain dalam Sistem Suria digabungkan. Musytari adalah antara objek paling terang yang terlihat dengan mata telanjang di langit malam, dan telah diketahui oleh tamadun kuno sejak sebelum sejarah tercatat. <br/>**Ringkaskan Ini** <br/> Apa yang kami pelajari ialah Musytari | adalah planet kelima dari Matahari dan yang terbesar dalam Sistem Suria. Ia adalah gergasi gas dengan jisim satu per seribu jisim Matahari, tetapi dua setengah kali ganda daripada semua planet lain digabungkan. Ia mudah dilihat dengan mata telanjang dan telah diketahui sejak zaman kuno.                     |

| 2              | Jupiter adalah planet kelima dari Matahari dan yang terbesar dalam Sistem Suria. Ia adalah gergasi gas dengan jisim satu per seribu jisim Matahari, tetapi dua setengah kali ganda jisim semua planet lain dalam Sistem Suria digabungkan. Jupiter adalah salah satu objek paling terang yang boleh dilihat dengan mata kasar di langit malam, dan telah diketahui oleh tamadun purba sejak sebelum sejarah tercatat. <br/>**Ringkaskan Ini** <br/> 3 Fakta Teratas Yang Kami Pelajari:         | 1. Jupiter adalah planet kelima dari Matahari dan yang terbesar dalam Sistem Suria. <br/> 2. Ia adalah gergasi gas dengan jisim satu per seribu jisim Matahari...<br/> 3. Jupiter telah dapat dilihat dengan mata kasar sejak zaman purba ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Templat Arahan

Templat arahan adalah _resipi telah ditetapkan untuk arahan_ yang boleh disimpan dan digunakan semula apabila diperlukan, untuk memacu pengalaman pengguna yang lebih konsisten secara besar-besaran. Dalam bentuknya yang paling mudah, ia hanyalah satu koleksi contoh arahan seperti [yang ini dari OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) yang menyediakan kedua-dua komponen arahan interaktif (mesej pengguna dan sistem) serta format permintaan yang dipacu oleh API - untuk menyokong penggunaan semula.

Dalam bentuk yang lebih kompleks seperti [contoh ini dari LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), ia mengandungi _ruang letak_ yang boleh digantikan dengan data dari pelbagai sumber (input pengguna, konteks sistem, sumber data luaran dll.) untuk menjana arahan secara dinamik. Ini membolehkan kami mencipta perpustakaan arahan yang boleh digunakan semula yang boleh digunakan untuk memacu pengalaman pengguna yang konsisten **secara berprogram** pada skala besar.

Akhirnya, nilai sebenar templat adalah keupayaan untuk mencipta dan menerbitkan _perpustakaan arahan_ untuk domain aplikasi khusus - di mana templat arahan kini _dioptimumkan_ untuk mencerminkan konteks atau contoh khusus aplikasi yang menjadikan tindak balas lebih relevan dan tepat untuk khalayak pengguna sasaran. Repositori [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) adalah contoh terbaik pendekatan ini, mengumpulkan perpustakaan arahan untuk domain pendidikan dengan penekanan pada objektif utama seperti perancangan pelajaran, reka bentuk kurikulum, bimbingan pelajar dll.

## Kandungan Sokongan

Jika kita memandang pembinaan arahan sebagai mempunyai arahan (tugas) dan sasaran (kandungan utama), maka _kandungan sekunder_ adalah seperti konteks tambahan yang kita berikan untuk **mempengaruhi output dengan cara tertentu**. Ia boleh menjadi parameter penyetelan, arahan pemformatan, taksonomi topik dan sebagainya yang boleh membantu model _menyesuaikan_ tindak balasnya supaya sesuai dengan objektif atau jangkaan pengguna yang diingini.

Contohnya: Diberi katalog kursus dengan metadata yang luas (nama, keterangan, tahap, tag metadata, pengajar dll.) pada semua kursus yang tersedia dalam kurikulum:

- kita boleh mentakrifkan arahan untuk "meringkaskan katalog kursus untuk Musim Luruh 2023"
- kita boleh menggunakan kandungan utama untuk memberikan beberapa contoh output yang diingini
- kita boleh menggunakan kandungan sekunder untuk mengenal pasti 5 "tag" teratas yang diminati.

Kini, model boleh memberikan ringkasan dalam format yang ditunjukkan oleh beberapa contoh - tetapi jika hasil mempunyai pelbagai tag, ia boleh memprioritikan 5 tag yang dikenal pasti dalam kandungan sekunder.

---

<!--
TEMPLAT PELAJARAN:
Unit ini hendaklah merangkumi konsep teras #1.
Memperkukuh konsep dengan contoh dan rujukan.

KONSEP #3:
Teknik Kejuruteraan Arahan.
Apakah beberapa teknik asas untuk kejuruteraan arahan?
Ilustrasikan dengan beberapa latihan.
-->

## Amalan Terbaik Arahan

Sekarang selepas kita mengetahui bagaimana arahan boleh _dibina_, kita boleh mula memikirkan bagaimana untuk _mereka bentuk_ arahan tersebut agar mencerminkan amalan terbaik. Kita boleh memikirkannya dalam dua bahagian - mempunyai _mindset_ yang betul dan menggunakan _teknik_ yang betul.

### Mindset Kejuruteraan Arahan

Kejuruteraan Arahan adalah proses cuba dan gagal, jadi ingat tiga faktor panduan utama:

1. **Pemahaman Domain Penting.** Ketepatan dan relevansi tindak balas adalah fungsi domain di mana aplikasi atau pengguna tersebut beroperasi. Gunakan naluri dan kepakaran domain anda untuk **menyesuaikan teknik** lebih lanjut. Contohnya, mentakrifkan _personaliti khusus domain_ dalam arahan sistem anda, atau menggunakan _templat khusus domain_ dalam arahan pengguna anda. Sediakan kandungan sekunder yang mencerminkan konteks khusus domain, atau gunakan _petunjuk dan contoh khusus domain_ untuk membimbing model ke arah corak penggunaan yang biasa.

2. **Pemahaman Model Penting.** Kita tahu model bersifat stokastik secara semula jadi. Tetapi pelaksanaan model juga boleh berbeza dari segi set data latihan yang mereka gunakan (pengetahuan pra-latih), keupayaan yang mereka sediakan (contohnya, melalui API atau SDK) dan jenis kandungan yang mereka optima untuk (contohnya, kod vs imej vs teks). Fahami kekuatan dan keterbatasan model yang anda gunakan, dan gunakan pengetahuan itu untuk _memprioritaskan tugas_ atau membina _templat tersuai_ yang dioptimumkan untuk keupayaan model.

3. **Iterasi & Pengesahan Penting.** Model sedang berkembang pesat, begitu juga teknik kejuruteraan arahan. Sebagai pakar domain, anda mungkin mempunyai konteks atau kriteria lain untuk aplikasi _anda_ yang mungkin tidak terpakai kepada komuniti yang lebih luas. Gunakan alat & teknik kejuruteraan arahan untuk "memulakan" pembinaan arahan, kemudian iterasi dan sahkan keputusan menggunakan naluri dan kepakaran domain anda sendiri. Rekodkan penemuan anda dan cipta **pangkalan pengetahuan** (contohnya, perpustakaan arahan) yang boleh digunakan sebagai garis dasar baru oleh orang lain, untuk iterasi lebih pantas pada masa akan datang.

## Amalan Terbaik

Sekarang mari lihat amalan terbaik biasa yang disyorkan oleh pengamal [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) dan [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Apa                              | Kenapa                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Nilai model terkini.       | Generasi model baru kemungkinan mempunyai ciri dan kualiti yang lebih baik - tetapi mungkin juga menanggung kos yang lebih tinggi. Nilai mereka untuk impak, kemudian buat keputusan migrasi.                                                                                |
| Pisahkan arahan & konteks   | Semak jika model/pembekal anda menentukan _pemisah_ untuk membezakan arahan, kandungan utama dan sekunder dengan lebih jelas. Ini boleh membantu model memberikan berat token lebih tepat.                                                         |
| Jadilah spesifik dan jelas             | Berikan lebih banyak maklumat tentang konteks, hasil, panjang, format, gaya yang dikehendaki. Ini akan meningkatkan kualiti dan konsistensi tindak balas. Tangkap resipi dalam templat yang boleh digunakan semula.                                                          |
| Jadilah deskriptif, gunakan contoh      | Model mungkin bertindak balas lebih baik dengan pendekatan "tunjuk dan ceritakan". Mula dengan pendekatan `zero-shot` di mana anda memberikan arahan (tetapi tiada contoh) kemudian cuba `few-shot` sebagai penambahbaikan, menyediakan beberapa contoh output yang diingini. Gunakan analogi. |
| Gunakan petunjuk untuk memulakan pelengkap | Dorong ia ke arah hasil yang dikehendaki dengan memberikan beberapa perkataan atau frasa permulaan yang boleh digunakan sebagai titik mula tindak balas.                                                                                                               |
| Gandakan                       | Kadang-kadang anda mungkin perlu mengulangi arahan kepada model. Berikan arahan sebelum dan selepas kandungan utama anda, gunakan arahan dan petunjuk, dsb. Iterasi & sahkan untuk melihat apa yang berkesan.                                                         |
| Susunan Penting                     | Susunan maklumat yang anda berikan kepada model boleh mempengaruhi output, walaupun dalam contoh pembelajaran, disebabkan bias kebaruan. Cuba pilihan berbeza untuk melihat apa yang terbaik.                                                               |
| Berikan model "jalan keluar"           | Berikan model tindak balas pelengkap _fallback_ yang boleh diberikannya jika tidak dapat menyelesaikan tugas untuk apa jua sebab. Ini boleh mengurangkan kemungkinan model menjana tindak balas palsu atau direka-reka.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Seperti mana-mana amalan terbaik, ingat bahawa _hasil anda mungkin berbeza_ berdasarkan model, tugas dan domain. Gunakan ini sebagai titik permulaan, dan buat iterasi untuk mencari apa yang terbaik untuk anda. Sentiasa nilai semula proses kejuruteraan arahan anda apabila model dan alat baru tersedia, dengan fokus pada kebolehsuaian proses dan kualiti tindak balas.

<!--
TEMPLAT PELAJARAN:
Unit ini hendaklah menyediakan cabaran kod jika berkenaan

CABARAN:
Pautan ke Jupyter Notebook dengan hanya komen kod dalam arahan (seksyen kod kosong).

PENYELESAIAN:
Pautan ke salinan Notebook tersebut dengan arahan lengkap dan dijalankan, menunjukkan satu contoh output.
-->

## Tugasan

Tahniah! Anda telah sampai ke akhir pelajaran! Masanya untuk menguji beberapa konsep dan teknik itu dengan contoh sebenar!

Untuk tugasan kita, kita akan menggunakan Jupyter Notebook dengan latihan yang boleh anda lengkapkan secara interaktif. Anda juga boleh melanjutkan Notebook dengan sel Markdown dan Kod anda sendiri untuk meneroka idea dan teknik sendiri.

### Untuk memulakan, forklah repo, kemudian

- (Disyorkan) Lancarkan GitHub Codespaces
- (Sebagai alternatif) Klon repo ke peranti tempatan anda dan gunakan dengan Docker Desktop
- (Sebagai alternatif) Buka Notebook dengan persekitaran runtime Notebook pilihan anda.

### Seterusnya, konfigurasikan pembolehubah persekitaran anda

- Salin fail `.env.copy` di akar repo ke `.env` dan isikan nilai `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` dan `AZURE_OPENAI_DEPLOYMENT`. Kembali ke [bahagian Learning Sandbox](#sandbox-pembelajaran) untuk belajar bagaimana.

### Seterusnya, buka Jupyter Notebook

- Pilih kernel runtime. Jika menggunakan pilihan 1 atau 2, pilih saja kernel Python 3.10.x lalai yang disediakan oleh kontena pembangunan.

Anda sudah bersedia untuk menjalankan latihan. Perhatikan tiada jawapan _betul dan salah_ di sini - hanya meneroka pilihan secara cuba dan gagal dan membina naluri untuk apa yang berkesan untuk model dan domain aplikasi tertentu.

_Oleh itu tiada segmen Penyelesaian Kod dalam pelajaran ini. Sebaliknya, Notebook akan mempunyai sel Markdown bertajuk "Penyelesaian Saya:" yang menunjukkan satu contoh output untuk rujukan._

 <!--
TEMPLAT PELAJARAN:
Bungkus bahagian dengan ringkasan dan sumber untuk pembelajaran kendiri.
-->

## Semakan Pengetahuan

Yang manakah di antara berikut merupakan arahan yang baik mengikut beberapa amalan terbaik yang munasabah?

1. Tunjukkan gambar kereta merah
2. Tunjukkan gambar kereta merah jenama Volvo dan model XC90 yang diparkir di tepi tebing dengan matahari terbenam
3. Tunjukkan gambar kereta merah jenama Volvo dan model XC90

A: 2, ia adalah arahan terbaik kerana memberikan butiran tentang "apa" dan mengulas spesifik (bukan sekadar mana-mana kereta tetapi jenama dan model tertentu) dan juga menerangkan suasana keseluruhan. 3 adalah yang terbaik seterusnya kerana ia juga mengandungi banyak deskripsi.

## 🚀 Cabaran

Cuba lihat jika anda boleh menggunakan teknik "petunjuk" dengan arahan: Selesaikan ayat "Tunjukkan gambar kereta merah jenama Volvo dan ". Apa jawapannya, dan bagaimana anda akan memperbaikinya?

## Kerja Hebat! Teruskan Pembelajaran Anda

Mahu belajar lebih lanjut tentang pelbagai konsep Kejuruteraan Arahan? Pergi ke [halaman pembelajaran berterusan](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk mencari sumber hebat lain mengenai topik ini.

Teruskan ke Pelajaran 5 di mana kita akan melihat [teknik arahan lanjutan](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->