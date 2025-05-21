<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T16:01:38+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "ms"
}
-->
# Asas Kejuruteraan Prompt

## Pengenalan
Modul ini merangkumi konsep dan teknik penting untuk mencipta prompt yang berkesan dalam model AI generatif. Cara anda menulis prompt kepada LLM juga penting. Prompt yang disusun dengan teliti dapat mencapai kualiti respons yang lebih baik. Tetapi apakah sebenarnya istilah seperti _prompt_ dan _kejuruteraan prompt_? Dan bagaimana saya boleh memperbaiki input prompt yang saya hantar kepada LLM? Ini adalah soalan yang akan kita cuba jawab dalam bab ini dan yang seterusnya.

_AI Generatif_ mampu mencipta kandungan baharu (contohnya, teks, imej, audio, kod dll.) sebagai respons kepada permintaan pengguna. Ia mencapai ini menggunakan _Model Bahasa Besar_ seperti siri GPT ("Generative Pre-trained Transformer") OpenAI yang dilatih untuk menggunakan bahasa semula jadi dan kod.

Pengguna kini boleh berinteraksi dengan model ini menggunakan paradigma yang biasa seperti sembang, tanpa memerlukan sebarang kepakaran teknikal atau latihan. Model ini adalah _berasaskan prompt_ - pengguna menghantar input teks (prompt) dan mendapat respons AI (penyelesaian). Mereka kemudian boleh "bersembang dengan AI" secara iteratif, dalam perbualan berbilang pusingan, memperhalusi prompt mereka sehingga respons sepadan dengan jangkaan mereka.

"Prompt" kini menjadi _antara muka pengaturcaraan_ utama untuk aplikasi AI generatif, memberitahu model apa yang perlu dilakukan dan mempengaruhi kualiti respons yang dikembalikan. "Kejuruteraan Prompt" adalah bidang kajian yang berkembang pesat yang memberi tumpuan kepada _rekaan dan pengoptimuman_ prompt untuk memberikan respons yang konsisten dan berkualiti pada skala.

## Matlamat Pembelajaran

Dalam pelajaran ini, kita belajar apa itu Kejuruteraan Prompt, mengapa ia penting, dan bagaimana kita boleh merangka prompt yang lebih berkesan untuk model dan objektif aplikasi yang diberikan. Kita akan memahami konsep teras dan amalan terbaik untuk kejuruteraan prompt - dan belajar tentang persekitaran "sandbox" Jupyter Notebooks interaktif di mana kita boleh melihat konsep ini digunakan pada contoh sebenar.

Menjelang akhir pelajaran ini kita akan dapat:

1. Terangkan apa itu kejuruteraan prompt dan mengapa ia penting.
2. Huraikan komponen prompt dan bagaimana ia digunakan.
3. Pelajari amalan terbaik dan teknik untuk kejuruteraan prompt.
4. Gunakan teknik yang dipelajari pada contoh sebenar, menggunakan titik akhir OpenAI.

## Istilah Utama

Kejuruteraan Prompt: Amalan mereka bentuk dan memperhalusi input untuk membimbing model AI ke arah menghasilkan output yang diinginkan.
Tokenisasi: Proses menukar teks kepada unit yang lebih kecil, dipanggil token, yang boleh difahami dan diproses oleh model.
LLM Ditala Arahan: Model Bahasa Besar (LLM) yang telah ditala dengan arahan tertentu untuk meningkatkan ketepatan dan relevan respons mereka.

## Sandbox Pembelajaran

Kejuruteraan prompt pada masa ini lebih kepada seni daripada sains. Cara terbaik untuk meningkatkan intuisi kita untuknya adalah dengan _berlatih lebih banyak_ dan mengamalkan pendekatan cuba-jaya yang menggabungkan kepakaran domain aplikasi dengan teknik yang disyorkan dan pengoptimuman khusus model.

Notebook Jupyter yang disertakan dengan pelajaran ini menyediakan persekitaran _sandbox_ di mana anda boleh mencuba apa yang anda pelajari - semasa anda pergi atau sebagai sebahagian daripada cabaran kod pada akhir. Untuk melaksanakan latihan, anda akan memerlukan:

1. **Kunci API Azure OpenAI** - titik akhir perkhidmatan untuk LLM yang digunakan.
2. **Runtime Python** - di mana Notebook boleh dilaksanakan.
3. **Pembolehubah Env Tempatan** - _lengkapkan langkah [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) sekarang untuk bersedia_.

Notebook ini dilengkapi dengan latihan _pemula_ - tetapi anda digalakkan untuk menambah bahagian _Markdown_ (penerangan) dan _Kod_ (permintaan prompt) anda sendiri untuk mencuba lebih banyak contoh atau idea - dan membina intuisi anda untuk reka bentuk prompt.

## Panduan Bergambar

Ingin mendapatkan gambaran besar tentang apa yang diliputi dalam pelajaran ini sebelum anda menyelam? Lihat panduan bergambar ini, yang memberi anda rasa topik utama yang diliputi dan perkara penting untuk anda fikirkan dalam setiap satu. Peta jalan pelajaran membawa anda daripada memahami konsep dan cabaran teras kepada menangani mereka dengan teknik kejuruteraan prompt yang relevan dan amalan terbaik. Perhatikan bahawa bahagian "Teknik Lanjutan" dalam panduan ini merujuk kepada kandungan yang diliputi dalam bab _seterusnya_ kurikulum ini.

## Misi Permulaan Kami

Sekarang, mari kita bincangkan bagaimana _topik ini_ berkaitan dengan misi permulaan kita untuk [membawa inovasi AI ke pendidikan](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Kami ingin membina aplikasi pembelajaran _peribadi_ berkuasa AI - jadi mari kita fikirkan tentang bagaimana pengguna yang berbeza dari aplikasi kita mungkin "merancang" prompt:

- **Pentadbir** mungkin meminta AI untuk _menganalisis data kurikulum untuk mengenal pasti jurang dalam liputan_. AI boleh meringkaskan hasil atau menggambarkannya dengan kod.
- **Pendidik** mungkin meminta AI untuk _menjana rancangan pelajaran untuk khalayak sasaran dan topik_. AI boleh membina rancangan peribadi dalam format yang ditentukan.
- **Pelajar** mungkin meminta AI untuk _mengajar mereka dalam subjek yang sukar_. AI kini boleh membimbing pelajar dengan pelajaran, petunjuk & contoh yang disesuaikan dengan tahap mereka.

Itu hanyalah permulaan. Lihat [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - perpustakaan prompt sumber terbuka yang dikendalikan oleh pakar pendidikan - untuk mendapatkan gambaran yang lebih luas tentang kemungkinan! _Cuba jalankan beberapa prompt tersebut dalam sandbox atau menggunakan OpenAI Playground untuk melihat apa yang berlaku!_

## Apakah Kejuruteraan Prompt?

Kami memulakan pelajaran ini dengan mentakrifkan **Kejuruteraan Prompt** sebagai proses _mereka bentuk dan mengoptimumkan_ input teks (prompt) untuk memberikan respons yang konsisten dan berkualiti (penyelesaian) untuk objektif aplikasi dan model yang diberikan. Kita boleh menganggap ini sebagai proses 2 langkah:

- _mereka bentuk_ prompt awal untuk model dan objektif yang diberikan
- _memperhalusi_ prompt secara iteratif untuk meningkatkan kualiti respons

Ini semestinya merupakan proses cuba-jaya yang memerlukan intuisi dan usaha pengguna untuk mendapatkan hasil yang optimum. Jadi mengapa ia penting? Untuk menjawab soalan itu, kita perlu memahami tiga konsep:

- _Tokenisasi_ = bagaimana model "melihat" prompt
- _Base LLMs_ = bagaimana model asas "memproses" prompt
- _LLM Ditala Arahan_ = bagaimana model kini boleh melihat "tugas"

### Tokenisasi

LLM melihat prompt sebagai _urutan token_ di mana model yang berbeza (atau versi model) boleh men-tokenkan prompt yang sama dengan cara yang berbeza. Oleh kerana LLM dilatih pada token (dan bukan pada teks mentah), cara prompt ditokenkan mempunyai kesan langsung pada kualiti respons yang dijana.

Untuk mendapatkan intuisi tentang bagaimana tokenisasi berfungsi, cuba alat seperti [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) yang ditunjukkan di bawah. Salin prompt anda - dan lihat bagaimana ia ditukar menjadi token, dengan memberi perhatian kepada bagaimana watak ruang putih dan tanda baca ditangani. Perhatikan bahawa contoh ini menunjukkan LLM yang lebih lama (GPT-3) - jadi mencuba ini dengan model yang lebih baru mungkin menghasilkan hasil yang berbeza.

### Konsep: Model Asas

Sebaik sahaja prompt ditokenkan, fungsi utama ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (atau model Asas) adalah untuk meramalkan token dalam urutan itu. Oleh kerana LLM dilatih pada set data teks yang besar, mereka mempunyai pemahaman yang baik tentang hubungan statistik antara token dan boleh membuat ramalan itu dengan sedikit keyakinan. Perhatikan bahawa mereka tidak memahami _makna_ perkataan dalam prompt atau token; mereka hanya melihat corak yang boleh mereka "lengkapkan" dengan ramalan seterusnya. Mereka boleh terus meramalkan urutan sehingga dihentikan oleh campur tangan pengguna atau beberapa syarat yang telah ditetapkan.

Ingin melihat bagaimana penyelesaian berasaskan prompt berfungsi? Masukkan prompt di atas ke dalam Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) dengan tetapan lalai. Sistem dikonfigurasikan untuk merawat prompt sebagai permintaan maklumat - jadi anda harus melihat penyelesaian yang memuaskan konteks ini.

Tetapi bagaimana jika pengguna ingin melihat sesuatu yang khusus yang memenuhi beberapa kriteria atau objektif tugas? Di sinilah LLM yang _ditala arahan_ muncul dalam gambar.

### Konsep: LLM Ditala Arahan

[LLM Ditala Arahan](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) bermula dengan model asas dan menala halus dengan contoh atau pasangan input/output (contohnya, "mesej" berbilang pusingan) yang boleh mengandungi arahan yang jelas - dan respons daripada AI cuba mengikuti arahan tersebut.

Ini menggunakan teknik seperti Pembelajaran Pengukuhan dengan Maklum Balas Manusia (RLHF) yang boleh melatih model untuk _mengikuti arahan_ dan _belajar daripada maklum balas_ supaya ia menghasilkan respons yang lebih sesuai untuk aplikasi praktikal dan lebih relevan dengan objektif pengguna.

Mari cuba - lawati semula prompt di atas, tetapi sekarang ubah _mesej sistem_ untuk memberikan arahan berikut sebagai konteks:

> _Ringkaskan kandungan yang diberikan kepada anda untuk pelajar darjah dua. Kekalkan hasil kepada satu perenggan dengan 3-5 poin._

Lihat bagaimana hasilnya kini ditala untuk mencerminkan matlamat dan format yang diinginkan? Seorang pendidik kini boleh menggunakan respons ini secara langsung dalam slaid mereka untuk kelas tersebut.

## Mengapa kita memerlukan Kejuruteraan Prompt?

Sekarang kita tahu bagaimana prompt diproses oleh LLM, mari kita bincangkan _mengapa_ kita memerlukan kejuruteraan prompt. Jawapannya terletak pada hakikat bahawa LLM semasa menimbulkan beberapa cabaran yang membuat _penyelesaian yang boleh dipercayai dan konsisten_ lebih sukar untuk dicapai tanpa meletakkan usaha ke dalam pembinaan dan pengoptimuman prompt. Sebagai contoh:

1. **Respons model adalah stokastik.** _Prompt yang sama_ mungkin menghasilkan respons yang berbeza dengan model atau versi model yang berbeza. Dan ia mungkin menghasilkan keputusan yang berbeza dengan _model yang sama_ pada masa yang berbeza. _Teknik kejuruteraan prompt boleh membantu kita meminimumkan variasi ini dengan menyediakan pengawal yang lebih baik_.

2. **Model boleh mengarang respons.** Model dilatih dengan set data yang _besar tetapi terhad_, bermakna mereka kekurangan pengetahuan tentang konsep di luar skop latihan tersebut. Akibatnya, mereka boleh menghasilkan penyelesaian yang tidak tepat, khayalan, atau secara langsung bertentangan dengan fakta yang diketahui. _Teknik kejuruteraan prompt membantu pengguna mengenal pasti dan mengurangkan fabrikasi tersebut contohnya, dengan meminta AI untuk sitasi atau penaakulan_.

3. **Keupayaan model akan berbeza.** Model yang lebih baru atau generasi model akan mempunyai keupayaan yang lebih kaya tetapi juga membawa kelainan unik dan kompromi dalam kos & kerumitan. _Kejuruteraan prompt boleh membantu kita membangunkan amalan terbaik dan aliran kerja yang mengabstrak perbezaan dan menyesuaikan diri dengan keperluan khusus model dengan cara yang berskala dan lancar_.

Mari kita lihat ini dalam tindakan di OpenAI atau Azure OpenAI Playground:

- Gunakan prompt yang sama dengan penyebaran LLM yang berbeza (contohnya, OpenAI, Azure OpenAI, Hugging Face) - adakah anda melihat variasi?
- Gunakan prompt yang sama berulang kali dengan penyebaran LLM yang _sama_ (contohnya, taman permainan Azure OpenAI) - bagaimana variasi ini berbeza?

### Contoh Fabrikasi

Dalam kursus ini, kami menggunakan istilah **"fabrikasi"** untuk merujuk kepada fenomena di mana LLM kadang-kadang menjana maklumat yang tidak tepat secara faktual disebabkan oleh batasan dalam latihan mereka atau kekangan lain. Anda mungkin juga pernah mendengar ini dirujuk sebagai _"halusinasi"_ dalam artikel popular atau kertas penyelidikan. Walau bagaimanapun, kami amat mengesyorkan menggunakan istilah _"fabrikasi"_ supaya kami tidak secara tidak sengaja memperlakukan tingkah laku tersebut dengan sifat seperti manusia kepada hasil yang digerakkan oleh mesin. Ini juga menguatkan garis panduan [AI Bertanggungjawab](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) dari perspektif terminologi, menghapuskan istilah yang mungkin juga dianggap menyinggung perasaan atau tidak inklusif dalam beberapa konteks.

Ingin mendapatkan rasa bagaimana fabrikasi berfungsi? Fikirkan prompt yang mengarahkan AI untuk menghasilkan kandungan untuk topik yang tidak wujud (untuk memastikan ia tidak terdapat dalam set data latihan). Sebagai contoh - saya mencuba prompt ini:

> **Prompt:** menjana rancangan pelajaran mengenai Perang Martian 2076.

Carian web menunjukkan kepada saya bahawa terdapat akaun fiksyen (contohnya, siri televisyen atau buku) mengenai perang Martian - tetapi tiada satu pun pada tahun 2076. Akal juga memberitahu kita bahawa 2076 adalah _di masa depan_ dan oleh itu, tidak boleh dikaitkan dengan peristiwa sebenar.

Jadi apa yang berlaku apabila kita menjalankan prompt ini dengan penyedia LLM yang berbeza?

> **Respons 1**: OpenAI Playground (GPT-35)

> **Respons 2**: Azure OpenAI Playground (GPT-35)

> **Respons 3**: : Hugging Face Chat Playground (LLama-2)

Seperti yang dijangkakan, setiap model (atau versi model) menghasilkan respons yang sedikit berbeza terima kasih kepada tingkah laku stokastik dan variasi keupayaan model. Sebagai contoh, satu model menyasarkan penonton gred 8 manakala yang lain menganggap pelajar sekolah menengah. Tetapi ketiga-tiga model menghasilkan respons yang boleh meyakinkan pengguna yang tidak dimaklumkan bahawa peristiwa itu adalah nyata

Teknik kejuruteraan prompt seperti _metaprompting_ dan _konfigurasi suhu_ mungkin mengurangkan fabrikasi model hingga tahap tertentu. _Senibina_ kejuruteraan prompt baru juga menggabungkan alat dan teknik baru dengan lancar ke dalam aliran prompt, untuk mengurangkan atau mengurangkan beberapa kesan ini.

## Kajian Kes: GitHub Copilot

Mari kita akhiri bahagian ini dengan mendapatkan rasa bagaimana kejuruteraan prompt digunakan dalam penyelesaian dunia sebenar dengan melihat satu Kajian Kes: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot adalah "Pengaturcara Pasangan AI" anda - ia menukar prompt teks kepada penyelesaian kod dan diintegrasikan ke dalam persekitaran pembangunan anda (contohnya, Visual Studio Code) untuk pengalaman pengguna yang lancar. Seperti yang didokumentasikan dalam siri blog di bawah, versi terawal berdasarkan model OpenAI Codex - dengan jurutera dengan cepat menyedari keperluan untuk menala halus model dan membangunkan teknik kejuruteraan prompt yang lebih baik, untuk meningkatkan kualiti kod. Pada bulan Julai, mereka [melancarkan model AI yang dipertingkatkan yang melangkaui Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) untuk cadangan yang lebih cepat.

Baca pos secara berturutan, untuk mengikuti perjalanan pembelajaran mereka.

- **Mei 2023** | [GitHub Copilot semakin memahami kod anda](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mei 2023** | [Di dalam GitHub: Bekerja dengan LLM di belakang GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Cara menulis prompt yang lebih baik untuk GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot melangkaui Codex dengan model AI yang dipertingkatkan](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Panduan Pembangun untuk Kejuruteraan Prompt dan LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Cara membina aplikasi LLM perusahaan: Pelajaran dari GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst
Akhirnya, nilai sebenar templat terletak pada keupayaan untuk mencipta dan menerbitkan _perpustakaan prompt_ untuk domain aplikasi menegak - di mana templat prompt kini _dioptimumkan_ untuk mencerminkan konteks atau contoh khusus aplikasi yang menjadikan respons lebih relevan dan tepat untuk sasaran pengguna. Repositori [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) adalah contoh hebat pendekatan ini, mengumpulkan perpustakaan prompt untuk domain pendidikan dengan penekanan pada objektif utama seperti perancangan pelajaran, reka bentuk kurikulum, bimbingan pelajar dan lain-lain.

## Menyokong Kandungan

Jika kita menganggap pembinaan prompt sebagai mempunyai arahan (tugas) dan sasaran (kandungan utama), maka _kandungan sekunder_ adalah seperti konteks tambahan yang kita berikan untuk **mempengaruhi output dalam beberapa cara**. Ia boleh menjadi penalaan parameter, arahan pemformatan, taksonomi topik dll. yang boleh membantu model _menyesuaikan_ responsnya agar sesuai dengan objektif atau jangkaan pengguna yang diinginkan.

Sebagai contoh: Diberikan katalog kursus dengan metadata yang meluas (nama, penerangan, tahap, tag metadata, pengajar dll.) pada semua kursus yang tersedia dalam kurikulum:

- kita boleh mentakrifkan arahan untuk "meringkaskan katalog kursus untuk Musim Gugur 2023"
- kita boleh menggunakan kandungan utama untuk memberikan beberapa contoh output yang diinginkan
- kita boleh menggunakan kandungan sekunder untuk mengenal pasti 5 "tag" utama yang diminati.

Sekarang, model boleh memberikan ringkasan dalam format yang ditunjukkan oleh beberapa contoh - tetapi jika hasilnya mempunyai pelbagai tag, ia boleh memprioritaskan 5 tag yang dikenal pasti dalam kandungan sekunder.

---

## Amalan Terbaik Prompting

Sekarang kita tahu bagaimana prompt boleh _dibina_, kita boleh mula memikirkan cara untuk _merancang_ mereka agar mencerminkan amalan terbaik. Kita boleh memikirkannya dalam dua bahagian - mempunyai _mindset_ yang betul dan menggunakan _teknik_ yang betul.

### Mindset Kejuruteraan Prompt

Kejuruteraan Prompt adalah proses cuba dan ralat jadi ingat tiga faktor panduan luas:

1. **Pemahaman Domain Penting.** Ketepatan dan relevan respons adalah fungsi daripada _domain_ di mana aplikasi atau pengguna itu beroperasi. Gunakan intuisi dan kepakaran domain anda untuk **menyesuaikan teknik** lebih lanjut. Sebagai contoh, tentukan _personaliti khusus domain_ dalam prompt sistem anda, atau gunakan _templat khusus domain_ dalam prompt pengguna anda. Berikan kandungan sekunder yang mencerminkan konteks khusus domain, atau gunakan _petunjuk dan contoh khusus domain_ untuk membimbing model ke arah corak penggunaan yang biasa.

2. **Pemahaman Model Penting.** Kita tahu model adalah stokastik secara semula jadi. Tetapi pelaksanaan model juga boleh berbeza dari segi set data latihan yang mereka gunakan (pengetahuan pralatih), keupayaan yang mereka sediakan (contohnya, melalui API atau SDK) dan jenis kandungan yang mereka dioptimumkan (contohnya, kod vs. imej vs. teks). Fahami kekuatan dan batasan model yang anda gunakan, dan gunakan pengetahuan itu untuk _memprioritaskan tugas_ atau membina _templat tersuai_ yang dioptimumkan untuk keupayaan model.

3. **Iterasi & Pengesahan Penting.** Model berkembang pesat, dan begitu juga teknik untuk kejuruteraan prompt. Sebagai pakar domain, anda mungkin mempunyai konteks atau kriteria lain untuk aplikasi khusus _anda_, yang mungkin tidak berlaku untuk komuniti yang lebih luas. Gunakan alat & teknik kejuruteraan prompt untuk "memulakan" pembinaan prompt, kemudian ulangi dan sahkan hasilnya menggunakan intuisi dan kepakaran domain anda sendiri. Rekod pandangan anda dan buat **pangkalan pengetahuan** (contohnya, perpustakaan prompt) yang boleh digunakan sebagai asas baru oleh orang lain, untuk iterasi yang lebih cepat pada masa depan.

## Amalan Terbaik

Sekarang mari kita lihat amalan terbaik yang biasa disarankan oleh pengamal [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) dan [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Apa                              | Kenapa                                                                                                                                                                                                                                               |
| :------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Menilai model terbaru.           | Generasi model baru mungkin mempunyai ciri dan kualiti yang lebih baik - tetapi juga mungkin menanggung kos yang lebih tinggi. Nilai mereka untuk impak, kemudian buat keputusan migrasi.                                                              |
| Pisahkan arahan & konteks        | Periksa jika model/pembekal anda mentakrifkan _pemisah_ untuk membezakan arahan, kandungan utama dan sekunder dengan lebih jelas. Ini boleh membantu model memberi berat lebih tepat kepada token.                                                     |
| Bersikap spesifik dan jelas      | Berikan lebih banyak butiran tentang konteks, hasil, panjang, format, gaya dll. yang diinginkan. Ini akan meningkatkan kualiti dan konsistensi respons. Tangkap resipi dalam templat yang boleh digunakan semula.                                      |
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

- Pilih kernel runtime. Jika menggunakan pilihan 1 atau 2, pilih sahaja kernel Python 3.10.x lalai yang disediakan oleh kontena pembangunan.

Anda sudah bersedia untuk menjalankan latihan. Perhatikan bahawa tiada jawapan _betul dan salah_ di sini - hanya meneroka pilihan melalui percubaan dan ralat serta membina intuisi untuk apa yang berkesan untuk model dan domain aplikasi tertentu.

_Oleh kerana itu, tiada segmen Penyelesaian Kod dalam pelajaran ini. Sebaliknya, Notebook akan mempunyai sel Markdown bertajuk "Penyelesaian Saya:" yang menunjukkan satu contoh output untuk rujukan._

## Semakan Pengetahuan

Yang manakah merupakan prompt yang baik mengikut beberapa amalan terbaik yang munasabah?

1. Tunjukkan saya gambar kereta merah
2. Tunjukkan saya gambar kereta merah buatan Volvo dan model XC90 yang diparkir di tepi tebing dengan matahari terbenam
3. Tunjukkan saya gambar kereta merah buatan Volvo dan model XC90

A: 2, ia adalah prompt terbaik kerana ia memberikan butiran tentang "apa" dan pergi ke spesifik (bukan sekadar kereta apa pun tetapi buatan dan model tertentu) dan ia juga menggambarkan keseluruhan suasana. 3 adalah yang terbaik seterusnya kerana ia juga mengandungi banyak penerangan.

## 🚀 Cabaran

Lihat jika anda boleh memanfaatkan teknik "cue" dengan prompt: Lengkapkan ayat "Tunjukkan saya gambar kereta merah buatan Volvo dan ". Apa yang ia balas, dan bagaimana anda akan memperbaikinya?

## Kerja Hebat! Teruskan Pembelajaran Anda

Ingin belajar lebih lanjut tentang pelbagai konsep Kejuruteraan Prompt? Pergi ke [halaman pembelajaran lanjutan](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk mencari sumber hebat lain mengenai topik ini.

Pergi ke Pelajaran 5 di mana kita akan melihat [teknik prompting lanjutan](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Penafian**: 
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.