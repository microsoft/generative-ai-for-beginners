<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T13:10:42+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "ms"
}
-->
# Asas Kejuruteraan Prompt

## Pengenalan
Modul ini merangkumi konsep dan teknik penting untuk mencipta prompt yang berkesan dalam model AI generatif. Cara anda menulis prompt kepada LLM juga penting. Prompt yang direka dengan teliti boleh mencapai kualiti respons yang lebih baik. Tetapi apa sebenarnya maksud istilah seperti _prompt_ dan _kejuruteraan prompt_? Dan bagaimana saya boleh meningkatkan input prompt yang saya hantar kepada LLM? Ini adalah soalan yang akan kita cuba jawab dalam bab ini dan yang berikutnya.

_AI Generatif_ mampu mencipta kandungan baru (contohnya, teks, imej, audio, kod, dll.) sebagai tindak balas kepada permintaan pengguna. Ia mencapai ini menggunakan _Model Bahasa Besar_ seperti siri GPT ("Generative Pre-trained Transformer") OpenAI yang dilatih untuk menggunakan bahasa semula jadi dan kod.

Pengguna kini boleh berinteraksi dengan model ini menggunakan paradigma yang biasa seperti chat, tanpa memerlukan kepakaran teknikal atau latihan. Model ini adalah berasaskan _prompt_ - pengguna menghantar input teks (prompt) dan mendapat kembali respons AI (penyelesaian). Mereka kemudian boleh "berbual dengan AI" secara berulang, dalam perbualan pelbagai pusingan, memperhalusi prompt mereka sehingga respons sesuai dengan jangkaan mereka.

"Prompt" kini menjadi _antara muka pengaturcaraan_ utama untuk aplikasi AI generatif, memberitahu model apa yang perlu dilakukan dan mempengaruhi kualiti respons yang dikembalikan. "Kejuruteraan Prompt" adalah bidang pengajian yang berkembang pesat yang memberi tumpuan kepada _rekaan dan pengoptimuman_ prompt untuk memberikan respons yang konsisten dan berkualiti pada skala.

## Matlamat Pembelajaran

Dalam pelajaran ini, kita belajar apa itu Kejuruteraan Prompt, mengapa ia penting, dan bagaimana kita boleh mencipta prompt yang lebih berkesan untuk model dan objektif aplikasi yang diberikan. Kita akan memahami konsep teras dan amalan terbaik untuk kejuruteraan prompt - dan belajar tentang persekitaran "sandbox" Jupyter Notebooks interaktif di mana kita boleh melihat konsep ini diterapkan kepada contoh sebenar.

Pada akhir pelajaran ini kita akan dapat:

1. Menerangkan apa itu kejuruteraan prompt dan mengapa ia penting.
2. Menerangkan komponen prompt dan bagaimana ia digunakan.
3. Mempelajari amalan terbaik dan teknik untuk kejuruteraan prompt.
4. Menerapkan teknik yang dipelajari kepada contoh sebenar, menggunakan endpoint OpenAI.

## Istilah Utama

Kejuruteraan Prompt: Amalan mereka bentuk dan memperhalusi input untuk membimbing model AI ke arah menghasilkan output yang dikehendaki.
Tokenisasi: Proses menukar teks kepada unit yang lebih kecil, dipanggil token, yang boleh difahami dan diproses oleh model.
LLM yang Ditala Arahan: Model Bahasa Besar (LLM) yang telah ditala halus dengan arahan khusus untuk meningkatkan ketepatan dan relevansi respons mereka.

## Sandbox Pembelajaran

Kejuruteraan prompt pada masa ini lebih kepada seni daripada sains. Cara terbaik untuk meningkatkan intuisi kita mengenainya adalah dengan _berlatih lebih_ dan mengamalkan pendekatan percubaan dan kesilapan yang menggabungkan kepakaran domain aplikasi dengan teknik yang disyorkan dan pengoptimuman khusus model.

Notebook Jupyter yang disertakan dengan pelajaran ini menyediakan persekitaran _sandbox_ di mana anda boleh mencuba apa yang anda pelajari - semasa anda pergi atau sebagai sebahagian daripada cabaran kod pada akhir. Untuk melaksanakan latihan, anda akan memerlukan:

1. **Kunci API Azure OpenAI** - endpoint perkhidmatan untuk LLM yang telah dikerahkan.
2. **Runtime Python** - di mana Notebook boleh dilaksanakan.
3. **Pembolehubah Persekitaran Tempatan** - _lengkapkan langkah [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) sekarang untuk bersedia_.

Notebook ini datang dengan latihan _permulaan_ - tetapi anda digalakkan untuk menambah bahagian _Markdown_ (penerangan) dan _Kod_ (permintaan prompt) anda sendiri untuk mencuba lebih banyak contoh atau idea - dan membina intuisi anda untuk reka bentuk prompt.

## Panduan Bergambar

Mahukan gambaran besar tentang apa yang diliputi oleh pelajaran ini sebelum anda menyelam? Lihat panduan bergambar ini, yang memberi anda gambaran tentang topik utama yang diliputi dan hasil utama untuk anda fikirkan dalam setiap satu. Peta jalan pelajaran membawa anda dari memahami konsep teras dan cabaran kepada menangani mereka dengan teknik kejuruteraan prompt yang relevan dan amalan terbaik. Perhatikan bahawa bahagian "Teknik Lanjutan" dalam panduan ini merujuk kepada kandungan yang diliputi dalam bab _seterusnya_ dalam kurikulum ini.

## Startup Kami

Sekarang, mari kita bincangkan bagaimana _topik ini_ berkaitan dengan misi startup kami untuk [membawa inovasi AI kepada pendidikan](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Kami mahu membina aplikasi berkuasa AI untuk _pembelajaran yang diperibadikan_ - jadi mari kita fikirkan tentang bagaimana pengguna yang berbeza dari aplikasi kami mungkin "mereka bentuk" prompt:

- **Pentadbir** mungkin meminta AI untuk _menganalisis data kurikulum untuk mengenal pasti jurang dalam liputan_. AI boleh meringkaskan hasil atau memvisualisasikannya dengan kod.
- **Pendidik** mungkin meminta AI untuk _menghasilkan rancangan pelajaran untuk khalayak sasaran dan topik_. AI boleh membina rancangan yang diperibadikan dalam format yang ditentukan.
- **Pelajar** mungkin meminta AI untuk _membimbing mereka dalam subjek yang sukar_. AI kini boleh membimbing pelajar dengan pelajaran, petunjuk & contoh yang disesuaikan dengan tahap mereka.

Itu hanyalah permulaan. Lihat [Prompts Untuk Pendidikan](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - perpustakaan prompt sumber terbuka yang dikurasi oleh pakar pendidikan - untuk mendapatkan gambaran yang lebih luas tentang kemungkinan! _Cuba jalankan beberapa prompt tersebut dalam sandbox atau menggunakan OpenAI Playground untuk melihat apa yang berlaku!_

## Apakah itu Kejuruteraan Prompt?

Kami memulakan pelajaran ini dengan mendefinisikan **Kejuruteraan Prompt** sebagai proses _mereka bentuk dan mengoptimumkan_ input teks (prompt) untuk memberikan respons yang konsisten dan berkualiti (penyelesaian) untuk objektif aplikasi dan model yang diberikan. Kita boleh menganggap ini sebagai proses 2 langkah:

- _mereka bentuk_ prompt awal untuk model dan objektif yang diberikan
- _memperhalusi_ prompt secara iteratif untuk meningkatkan kualiti respons

Ini semestinya merupakan proses percubaan dan kesilapan yang memerlukan intuisi dan usaha pengguna untuk mendapatkan hasil yang optimum. Jadi mengapa ia penting? Untuk menjawab soalan itu, kita perlu memahami tiga konsep:

- _Tokenisasi_ = bagaimana model "melihat" prompt
- _LLM Asas_ = bagaimana model asas "memproses" prompt
- _LLM yang Ditala Arahan_ = bagaimana model kini boleh melihat "tugas"

### Tokenisasi

LLM melihat prompt sebagai _urutan token_ di mana model yang berbeza (atau versi model) boleh menokenkan prompt yang sama dengan cara yang berbeza. Oleh kerana LLM dilatih pada token (dan bukan pada teks mentah), cara prompt ditokenkan mempunyai kesan langsung terhadap kualiti respons yang dihasilkan.

Untuk mendapatkan intuisi tentang bagaimana tokenisasi berfungsi, cuba alat seperti [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) yang ditunjukkan di bawah. Salin prompt anda - dan lihat bagaimana ia ditukar menjadi token, memberi perhatian kepada bagaimana watak ruang kosong dan tanda baca dikendalikan. Perhatikan bahawa contoh ini menunjukkan LLM yang lebih lama (GPT-3) - jadi mencuba ini dengan model yang lebih baru mungkin menghasilkan hasil yang berbeza.

### Konsep: Model Asas

Setelah prompt ditokenkan, fungsi utama ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (atau model Asas) adalah untuk meramalkan token dalam urutan itu. Oleh kerana LLM dilatih pada set data teks yang besar, mereka mempunyai pemahaman yang baik tentang hubungan statistik antara token dan boleh membuat ramalan itu dengan keyakinan tertentu. Perhatikan bahawa mereka tidak memahami _makna_ perkataan dalam prompt atau token; mereka hanya melihat pola yang boleh mereka "lengkapkan" dengan ramalan seterusnya. Mereka boleh terus meramalkan urutan sehingga dihentikan oleh campur tangan pengguna atau beberapa syarat yang telah ditetapkan.

Mahukan melihat bagaimana penyelesaian berasaskan prompt berfungsi? Masukkan prompt di atas ke dalam Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) dengan tetapan lalai. Sistem dikonfigurasikan untuk merawat prompt sebagai permintaan maklumat - jadi anda harus melihat penyelesaian yang memenuhi konteks ini.

Tetapi bagaimana jika pengguna ingin melihat sesuatu yang spesifik yang memenuhi beberapa kriteria atau objektif tugas? Di sinilah LLM yang _ditala arahan_ muncul.

### Konsep: LLM yang Ditala Arahan

LLM yang [Ditala Arahan](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) bermula dengan model asas dan menala halusnya dengan contoh atau pasangan input/output (contohnya, "mesej" berbilang pusingan) yang boleh mengandungi arahan yang jelas - dan respons daripada AI cuba mengikuti arahan tersebut.

Ini menggunakan teknik seperti Pembelajaran Pengukuhan dengan Maklum Balas Manusia (RLHF) yang boleh melatih model untuk _mengikuti arahan_ dan _belajar daripada maklum balas_ supaya ia menghasilkan respons yang lebih sesuai untuk aplikasi praktikal dan lebih relevan dengan objektif pengguna.

Mari cuba - lawati semula prompt di atas, tetapi kini ubah _mesej sistem_ untuk memberikan arahan berikut sebagai konteks:

> _Ringkaskan kandungan yang anda sediakan untuk pelajar darjah dua. Simpan hasil kepada satu perenggan dengan 3-5 poin peluru._

Lihat bagaimana hasilnya kini disesuaikan untuk mencerminkan matlamat dan format yang diinginkan? Seorang pendidik kini boleh menggunakan respons ini secara langsung dalam slaid mereka untuk kelas tersebut.

## Mengapa kita memerlukan Kejuruteraan Prompt?

Sekarang kita tahu bagaimana prompt diproses oleh LLM, mari kita bincangkan _mengapa_ kita memerlukan kejuruteraan prompt. Jawapannya terletak pada fakta bahawa LLM semasa menghadapi beberapa cabaran yang membuat _penyelesaian yang boleh dipercayai dan konsisten_ lebih sukar dicapai tanpa meletakkan usaha ke dalam pembinaan dan pengoptimuman prompt. Sebagai contoh:

1. **Respons model adalah stokastik.** _Prompt yang sama_ mungkin menghasilkan respons yang berbeza dengan model atau versi model yang berbeza. Dan ia mungkin menghasilkan hasil yang berbeza dengan _model yang sama_ pada masa yang berbeza. _Teknik kejuruteraan prompt boleh membantu kita meminimumkan variasi ini dengan menyediakan panduan yang lebih baik_.

2. **Model boleh membuat respons palsu.** Model dilatih dengan set data yang _besar tetapi terhad_, yang bermaksud mereka kekurangan pengetahuan tentang konsep di luar skop latihan tersebut. Akibatnya, mereka boleh menghasilkan penyelesaian yang tidak tepat, imaginasi, atau bercanggah secara langsung dengan fakta yang diketahui. _Teknik kejuruteraan prompt membantu pengguna mengenal pasti dan mengurangkan fabrikasi tersebut contohnya, dengan meminta AI untuk petikan atau penalaran_.

3. **Keupayaan model akan berbeza.** Model yang lebih baru atau generasi model akan mempunyai keupayaan yang lebih kaya tetapi juga membawa kekurangan unik dan pertukaran dalam kos & kerumitan. _Kejuruteraan prompt boleh membantu kita membangunkan amalan terbaik dan aliran kerja yang mengabstrak perbezaan dan menyesuaikan diri dengan keperluan khusus model dengan cara yang boleh diukur dan lancar_.

Mari kita lihat ini dalam tindakan di OpenAI atau Azure OpenAI Playground:

- Gunakan prompt yang sama dengan penyebaran LLM yang berbeza (contohnya, OpenAI, Azure OpenAI, Hugging Face) - adakah anda melihat variasi?
- Gunakan prompt yang sama berulang kali dengan penyebaran LLM yang _sama_ (contohnya, Azure OpenAI playground) - bagaimana variasi ini berbeza?

### Contoh Fabrikasi

Dalam kursus ini, kami menggunakan istilah **"fabrikasi"** untuk merujuk kepada fenomena di mana LLM kadang-kadang menghasilkan maklumat yang tidak tepat secara faktual disebabkan oleh batasan dalam latihan mereka atau kekangan lain. Anda mungkin juga pernah mendengar ini dirujuk sebagai _"halusinasi"_ dalam artikel popular atau kertas penyelidikan. Walau bagaimanapun, kami sangat mengesyorkan menggunakan _"fabrikasi"_ sebagai istilah supaya kami tidak secara tidak sengaja mengantropomorfisasi tingkah laku dengan mengaitkan sifat manusia kepada hasil yang didorong oleh mesin. Ini juga mengukuhkan garis panduan [AI Bertanggungjawab](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) dari perspektif terminologi, menghapuskan istilah yang mungkin dianggap menyinggung atau tidak inklusif dalam beberapa konteks.

Mahukan mendapatkan gambaran tentang bagaimana fabrikasi berfungsi? Fikirkan tentang prompt yang mengarahkan AI untuk menghasilkan kandungan untuk topik yang tidak wujud (untuk memastikan ia tidak terdapat dalam set data latihan). Sebagai contoh - saya mencuba prompt ini:

> **Prompt:** menghasilkan rancangan pelajaran tentang Perang Martian tahun 2076.

Carian web menunjukkan kepada saya bahawa terdapat akaun fiksyen (contohnya, siri televisyen atau buku) tentang perang Martian - tetapi tiada dalam tahun 2076. Akal juga memberitahu kita bahawa 2076 adalah _masa depan_ dan dengan itu, tidak boleh dikaitkan dengan peristiwa sebenar.

Jadi apa yang berlaku apabila kita menjalankan prompt ini dengan penyedia LLM yang berbeza?

> **Respons 1**: OpenAI Playground (GPT-35)

> **Respons 2**: Azure OpenAI Playground (GPT-35)

> **Respons 3**: : Hugging Face Chat Playground (LLama-2)

Seperti yang dijangkakan, setiap model (atau versi model) menghasilkan respons yang sedikit berbeza terima kasih kepada tingkah laku stokastik dan variasi keupayaan model. Sebagai contoh, satu model mensasarkan penonton darjah 8 sementara yang lain menganggap pelajar sekolah menengah. Tetapi ketiga-tiga model memang menghasilkan respons yang boleh meyakinkan pengguna yang tidak berpengetahuan bahawa peristiwa itu adalah benar

Teknik kejuruteraan prompt seperti _metaprompting_ dan _konfigurasi suhu_ boleh mengurangkan fabrikasi model hingga tahap tertentu. Senibina kejuruteraan prompt yang baru juga menggabungkan alat dan teknik baru dengan lancar ke dalam aliran prompt, untuk mengurangkan atau mengurangkan beberapa kesan ini.

## Kajian Kes: GitHub Copilot

Mari kita tamatkan bahagian ini dengan mendapatkan gambaran tentang bagaimana kejuruteraan prompt digunakan dalam penyelesaian dunia nyata dengan melihat satu Kajian Kes: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot adalah "AI Pair Programmer" anda - ia menukar prompt teks menjadi penyelesaian kod dan diintegrasikan ke dalam persekitaran pembangunan anda (contohnya, Visual Studio Code) untuk pengalaman pengguna yang lancar. Seperti yang didokumentasikan dalam siri blog di bawah, versi terawal adalah berdasarkan model OpenAI Codex - dengan jurutera dengan cepat menyedari keperluan untuk menala halus model dan membangunkan teknik kejuruteraan prompt yang lebih baik, untuk meningkatkan kualiti kod. Pada bulan Julai, mereka [memperkenalkan model AI yang diperbaiki yang melampaui Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) untuk cadangan yang lebih cepat.

Baca catatan dalam urutan, untuk mengikuti perjalanan pembelajaran mereka.

- **Mei 2023** | [GitHub Copilot semakin baik dalam memahami kod anda](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mei 2023** | [Di dalam GitHub: Bekerja dengan LLM di belakang GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Cara menulis prompt yang lebih baik untuk GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot melampaui Codex dengan model AI yang diperbaiki](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Panduan Pembangun untuk Kejuruteraan Prompt dan LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Cara membina aplikasi LLM perusahaan: Pelajaran dari GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-cop
Akhirnya, nilai sebenar templat terletak pada keupayaan untuk mencipta dan menerbitkan _perpustakaan prompt_ untuk domain aplikasi vertikal - di mana templat prompt kini dioptimumkan untuk mencerminkan konteks atau contoh khusus aplikasi yang menjadikan respons lebih relevan dan tepat untuk audiens pengguna yang disasarkan. Repositori [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) adalah contoh yang baik untuk pendekatan ini, mengumpulkan perpustakaan prompt untuk domain pendidikan dengan penekanan pada objektif utama seperti perancangan pelajaran, reka bentuk kurikulum, bimbingan pelajar dan sebagainya.

## Kandungan Sokongan

Jika kita memikirkan pembinaan prompt sebagai mempunyai arahan (tugas) dan sasaran (kandungan utama), maka _kandungan sekunder_ adalah seperti konteks tambahan yang kita sediakan untuk **mempengaruhi output dalam beberapa cara**. Ia boleh menjadi parameter penalaan, arahan pemformatan, taksonomi topik dan sebagainya yang dapat membantu model _menyesuaikan_ responsnya untuk memenuhi objektif atau jangkaan pengguna yang diingini.

Sebagai contoh: Diberikan katalog kursus dengan metadata yang luas (nama, deskripsi, tahap, tag metadata, pengajar dan lain-lain) pada semua kursus yang tersedia dalam kurikulum:

- kita boleh menentukan arahan untuk "meringkaskan katalog kursus untuk Musim Luruh 2023"
- kita boleh menggunakan kandungan utama untuk memberikan beberapa contoh output yang diingini
- kita boleh menggunakan kandungan sekunder untuk mengenal pasti 5 "tag" utama yang menarik.

Sekarang, model boleh memberikan ringkasan dalam format yang ditunjukkan oleh beberapa contoh - tetapi jika hasilnya mempunyai banyak tag, ia boleh memprioritaskan 5 tag yang dikenal pasti dalam kandungan sekunder.

---

## Amalan Terbaik Prompting

Sekarang kita tahu bagaimana prompt boleh _dibina_, kita boleh mula memikirkan bagaimana untuk _merancang_ mereka untuk mencerminkan amalan terbaik. Kita boleh memikirkan ini dalam dua bahagian - mempunyai _pemikiran_ yang betul dan menerapkan _teknik_ yang betul.

### Pemikiran Kejuruteraan Prompt

Kejuruteraan Prompt adalah proses cuba dan ralat jadi ingat tiga faktor panduan utama:

1. **Pemahaman Domain Penting.** Ketepatan dan relevansi respons adalah fungsi dari _domain_ di mana aplikasi atau pengguna itu beroperasi. Gunakan intuisi dan kepakaran domain anda untuk **menyesuaikan teknik** lebih lanjut. Sebagai contoh, definisikan _personaliti khusus domain_ dalam prompt sistem anda, atau gunakan _templat khusus domain_ dalam prompt pengguna anda. Sediakan kandungan sekunder yang mencerminkan konteks khusus domain, atau gunakan _petunjuk dan contoh khusus domain_ untuk membimbing model ke arah corak penggunaan yang biasa.

2. **Pemahaman Model Penting.** Kita tahu model adalah stokastik secara semula jadi. Tetapi pelaksanaan model juga boleh berbeza dari segi dataset latihan yang mereka gunakan (pengetahuan pratetap), keupayaan yang mereka sediakan (contohnya, melalui API atau SDK) dan jenis kandungan yang mereka dioptimumkan (contohnya, kod vs. imej vs. teks). Fahami kekuatan dan batasan model yang anda gunakan, dan gunakan pengetahuan itu untuk _memprioritaskan tugas_ atau membina _templat khusus_ yang dioptimumkan untuk keupayaan model.

3. **Iterasi & Pengesahan Penting.** Model berkembang pesat, begitu juga teknik untuk kejuruteraan prompt. Sebagai pakar domain, anda mungkin mempunyai konteks atau kriteria lain untuk aplikasi khusus anda, yang mungkin tidak berlaku kepada komuniti yang lebih luas. Gunakan alat & teknik kejuruteraan prompt untuk "memulakan" pembinaan prompt, kemudian iterasi dan sahkan hasilnya menggunakan intuisi dan kepakaran domain anda sendiri. Rekodkan pandangan anda dan buat **pangkalan pengetahuan** (contohnya, perpustakaan prompt) yang boleh digunakan sebagai asas baru oleh orang lain, untuk iterasi lebih cepat pada masa depan.

## Amalan Terbaik

Sekarang mari kita lihat amalan terbaik yang biasa disarankan oleh pengamal [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) dan [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Apa                               | Mengapa                                                                                                                                                                                                                                               |
| :-------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Menilai model terkini.            | Generasi model baru cenderung mempunyai ciri dan kualiti yang lebih baik - tetapi mungkin juga menanggung kos yang lebih tinggi. Nilai mereka untuk impak, kemudian buat keputusan migrasi.                                                            |
| Pisahkan arahan & konteks         | Periksa jika model/pembekal anda mendefinisikan _pemisah_ untuk membezakan arahan, kandungan utama dan sekunder dengan lebih jelas. Ini boleh membantu model memberikan berat dengan lebih tepat kepada token.                                        |
| Spesifik dan jelas                | Berikan lebih banyak butiran tentang konteks yang diingini, hasil, panjang, format, gaya dan lain-lain. Ini akan meningkatkan kedua-dua kualiti dan konsistensi respons. Tangkap resipi dalam templat yang boleh digunakan semula.                      |
| Bersifat deskriptif, gunakan contoh | Model mungkin bertindak balas lebih baik kepada pendekatan "tunjuk dan beritahu". Mulakan dengan `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` nilai. Kembali ke [Bahagian Kotak Pasir Pembelajaran](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) untuk belajar bagaimana.

### Seterusnya, buka Jupyter Notebook

- Pilih kernel runtime. Jika menggunakan pilihan 1 atau 2, cukup pilih kernel Python 3.10.x lalai yang disediakan oleh kontena pembangunan.

Anda sudah bersedia untuk menjalankan latihan. Perhatikan bahawa tiada jawapan _betul dan salah_ di sini - hanya meneroka pilihan melalui cuba dan ralat dan membina intuisi untuk apa yang berkesan untuk model dan domain aplikasi tertentu.

_Oleh kerana itu tiada segmen Penyelesaian Kod dalam pelajaran ini. Sebaliknya, Notebook akan mempunyai sel Markdown bertajuk "Penyelesaian Saya:" yang menunjukkan satu contoh output untuk rujukan._

## Pemeriksaan Pengetahuan

Yang manakah berikut adalah prompt yang baik mengikut beberapa amalan terbaik yang munasabah?

1. Tunjukkan saya imej kereta merah
2. Tunjukkan saya imej kereta merah jenama Volvo dan model XC90 diparkir di tepi tebing dengan matahari terbenam
3. Tunjukkan saya imej kereta merah jenama Volvo dan model XC90

A: 2, ia adalah prompt terbaik kerana ia memberikan butiran tentang "apa" dan masuk ke spesifik (bukan hanya sebarang kereta tetapi jenama dan model tertentu) dan ia juga menggambarkan keseluruhan suasana. 3 adalah yang terbaik seterusnya kerana ia juga mengandungi banyak deskripsi.

## 🚀 Cabaran

Lihat jika anda boleh memanfaatkan teknik "cue" dengan prompt: Lengkapkan ayat "Tunjukkan saya imej kereta merah jenama Volvo dan ". Apa yang ia balas, dan bagaimana anda akan memperbaikinya?

## Kerja Hebat! Teruskan Pembelajaran Anda

Mahukan lebih banyak pembelajaran tentang konsep Kejuruteraan Prompt yang berbeza? Pergi ke [halaman pembelajaran lanjutan](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk mencari sumber lain yang hebat tentang topik ini.

Pergi ke Pelajaran 5 di mana kita akan melihat [teknik prompting lanjutan](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.