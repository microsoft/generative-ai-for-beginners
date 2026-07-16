# Meneroka dan membandingkan pelbagai LLM

[![Meneroka dan membandingkan pelbagai LLM](../../../translated_images/ms/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Klik imej di atas untuk menonton video pelajaran ini_

Dengan pelajaran sebelumnya, kita telah melihat bagaimana AI Generatif mengubah landskap teknologi, bagaimana Model Bahasa Besar (LLM) berfungsi dan bagaimana perniagaan - seperti permulaan kami - boleh menggunakannya untuk kes penggunaan mereka dan berkembang! Dalam bab ini, kami ingin membanding dan membezakan pelbagai jenis model bahasa besar (LLM) untuk memahami kelebihan dan kekurangannya.

Langkah seterusnya dalam perjalanan permulaan kami adalah meneroka landskap semasa LLM dan memahami yang mana sesuai untuk kes penggunaan kami.

## Pengenalan

Pelajaran ini akan merangkumi:

- Pelbagai jenis LLM dalam landskap semasa.
- Ujian, iterasi, dan perbandingan model berbeza untuk kes penggunaan anda di Azure.
- Cara menggunakan LLM.

## Matlamat Pembelajaran

Setelah menyelesaikan pelajaran ini, anda akan dapat:

- Memilih model yang tepat untuk kes penggunaan anda.
- Memahami cara menguji, mengulangi, dan memperbaiki prestasi model anda.
- Mengetahui bagaimana perniagaan menggunakan model.

## Fahami pelbagai jenis LLM

LLM boleh mempunyai pelbagai pengkelasan berdasarkan seni bina, data latihan, dan kes penggunaan mereka. Memahami perbezaan ini akan membantu permulaan kami memilih model yang sesuai untuk senario, dan memahami cara menguji, mengulangi, dan memperbaiki prestasi.

Terdapat banyak jenis model LLM yang berbeza, pilihan model anda bergantung pada apa yang anda mahu gunakan, data anda, berapa banyak anda sedia bayar dan lain-lain.

Bergantung pada sama ada anda mahu menggunakan model untuk teks, audio, video, penjanaan imej dan sebagainya, anda mungkin memilih jenis model yang berbeza.

- **Pengecaman audio dan pertuturan**. Model gaya Whisper masih berguna sebagai model pengecaman pertuturan tujuan umum, tetapi pilihan pengeluaran kini juga merangkumi model pertuturan-ke-teks yang lebih baru seperti `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, dan varian diarization. Nilai liputan bahasa, diarization, sokongan masa nyata, kelewatan, dan kos untuk senario anda. Ketahui lebih lanjut dalam [dokumentasi pertuturan-ke-teks OpenAI](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Penjanaan imej**. DALL-E dan Midjourney adalah pilihan penjanaan imej yang terkenal, tetapi API imej OpenAI semasa tertumpu pada model GPT Image seperti `gpt-image-2`, sementara Stable Diffusion, Imagen, Flux, dan keluarga model lain juga adalah pilihan biasa. Bandingkan pengikut arahan (prompt adherence), sokongan penyuntingan, kawalan gaya, keperluan keselamatan, dan pelesenan. Ketahui lebih lanjut dalam [panduan penjanaan imej OpenAI](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) dan Bab 9 kurikulum ini.

- **Penjanaan teks**. Model teks kini merangkumi model frontier, model penalaran, model kecil berlatensi rendah, dan model berat terbuka. Contoh semasa termasuk model OpenAI GPT-5.x, model Anthropic Claude 4.x, model Google Gemini 3.x, model Meta Llama 4, dan model Mistral. Jangan pilih hanya berdasarkan tarikh keluaran atau harga; bandingkan kualiti tugas, kelewatan, tingkap konteks, penggunaan alat, kelakuan keselamatan, ketersediaan serantau, dan kos keseluruhan. [Katalog model Microsoft Foundry](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) adalah tempat yang baik untuk membanding model yang tersedia di Azure.

- **Multi-modality**. Ramai model semasa boleh memproses lebih daripada teks. Sesetengah menerima input imej, audio, atau video; ada yang boleh memanggil alat; dan model khusus boleh menjana imej, audio, atau video. Contohnya, model OpenAI semasa menyokong input teks dan imej, model Gemini boleh menyokong input teks, kod, imej, audio, dan video bergantung pada varian, dan Llama 4 Scout dan Maverick adalah model berat terbuka yang secara asli multimodal. Sentiasa periksa setiap kad model untuk modul input dan output yang disokong sebelum membina aliran kerja di sekelilingnya.

Memilih model bermaksud anda mendapat beberapa keupayaan asas, yang mungkin tidak mencukupi. Selalunya anda mempunyai data khusus syarikat yang anda perlu beritahu LLM dengan cara tertentu. Terdapat beberapa pilihan berbeza tentang cara mendekati hal itu, lebih lanjut mengenai itu dalam bahagian berikut.

### Model Asas berbanding LLM

Istilah Model Asas telah [dibuat oleh penyelidik Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) dan didefinisikan sebagai model AI yang memenuhi beberapa kriteria, seperti:

- **Mereka dilatih menggunakan pembelajaran tanpa pengawasan atau pembelajaran kendiri**, bermakna mereka dilatih pada data multimodal tanpa label, dan mereka tidak memerlukan anotasi manusia atau pelabelan data untuk proses latihan mereka.
- **Mereka adalah model yang sangat besar**, berdasarkan rangkaian neural yang sangat dalam yang dilatih pada berbilion parameter.
- **Mereka biasanya bertujuan untuk berfungsi sebagai ‘asas’ untuk model lain**, bermakna mereka boleh digunakan sebagai titik permulaan untuk model lain dibina di atasnya, yang boleh dilakukan dengan penalaan halus.

![Foundation Models versus LLMs](../../../translated_images/ms/FoundationModel.e4859dbb7a825c94.webp)

Sumber imej: [Panduan Penting Model Asas dan Model Bahasa Besar | oleh Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Untuk menerangkan lagi perbezaan ini, mari ambil ChatGPT sebagai contoh sejarah. Versi awal ChatGPT menggunakan GPT-3.5 sebagai model asas. OpenAI kemudian menggunakan data khusus chat dan teknik penyelarasan untuk menghasilkan versi yang ditala yang berprestasi lebih baik dalam senario perbualan, seperti chatbot. Perkhidmatan AI moden sering mengalihkan antara beberapa varian model, jadi nama perkhidmatan dan nama model asas tidak selalu sama.

![Foundation Model](../../../translated_images/ms/Multimodal.2c389c6439e0fc51.webp)

Sumber imej: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Model Berat Terbuka/Sumber Terbuka berbanding Model Proprietari

Satu lagi cara mengklasifikasikan LLM ialah sama ada mereka berat terbuka, sumber terbuka, atau proprietari.

Model sumber terbuka dan berat terbuka membuat artifak model tersedia untuk pemeriksaan, muat turun, atau penyesuaian, tetapi lesen mereka berbeza. Ada yang sepenuhnya sumber terbuka, manakala yang lain adalah model berat terbuka dengan sekatan penggunaan. Mereka berguna apabila perniagaan memerlukan kawalan lebih ke atas penyebaran, lokaliti data, kos, atau penyesuaian. Walau bagaimanapun, pasukan masih perlu meneliti syarat lesen, kos perkhidmatan, penyelenggaraan, kemas kini keselamatan, dan kualiti penilaian sebelum menggunakannya dalam pengeluaran. Contohnya termasuk [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), beberapa [model Mistral](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst), dan banyak model yang dihoskan di [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Model proprietari dimiliki dan dihoskan oleh penyedia. Model ini sering dioptimumkan untuk penggunaan pengeluaran terurus dan boleh menawarkan sokongan kuat, sistem keselamatan, integrasi alat, dan skala. Walau bagaimanapun, pelanggan biasanya tidak boleh memeriksa atau mengubah berat model, dan mereka mesti meneliti terma penyedia untuk privasi, penyimpanan, pematuhan, dan penggunaan yang boleh diterima. Contoh termasuk [model OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst), dan [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Penjanaan embedding berbanding imej berbanding teks dan kod

LLM juga boleh dikategorikan berdasarkan output yang dihasilkan.

Embedding adalah satu set model yang boleh menukar teks menjadi bentuk nombor, dipanggil embedding, iaitu representasi nombor bagi teks input. Embedding memudahkan mesin memahami hubungan antara perkataan atau ayat dan boleh digunakan sebagai input oleh model lain, seperti model klasifikasi, atau model pengelompokan yang mempunyai prestasi lebih baik pada data nombor. Model embedding sering digunakan untuk pembelajaran pemindahan, di mana model dibina untuk tugas gantian yang mempunyai data yang banyak, dan kemudian berat model (embedding) digunakan semula untuk tugas hiliran lain. Contoh kategori ini ialah [embedding OpenAI](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/ms/Embedding.c3708fe988ccf760.webp)

Model penjanaan imej adalah model yang menjana imej. Model ini sering digunakan untuk penyuntingan imej, sintesis imej, dan terjemahan imej. Model penjanaan imej sering dilatih pada set data imej yang besar, seperti [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), dan boleh digunakan untuk menghasilkan imej baru atau mengedit imej sedia ada dengan teknik inpainting, resolusi tinggi, dan pewarnaan. Contohnya termasuk [model GPT Image](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [model Stable Diffusion](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst), dan model Imagen.

![Penjanaan imej](../../../translated_images/ms/Image.349c080266a763fd.webp)

Model penjanaan teks dan kod adalah model yang menjana teks atau kod. Model ini sering digunakan untuk ringkasan teks, terjemahan, dan menjawab soalan. Model penjanaan teks sering dilatih pada set data teks yang besar, seperti [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), dan boleh digunakan untuk menghasilkan teks baru, atau menjawab soalan. Model penjanaan kod, seperti [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), sering dilatih pada set data kod yang besar, seperti GitHub, dan boleh digunakan untuk menjana kod baru, atau membetulkan pepijat dalam kod sedia ada.

![Penjanaan teks dan kod](../../../translated_images/ms/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder berbanding hanya Decoder

Untuk bercakap tentang pelbagai jenis seni bina LLM, mari gunakan analogi.

Bayangkan pengurus anda memberi tugasan menulis kuiz untuk pelajar. Anda mempunyai dua rakan sekerja; seorang mengawasi penciptaan kandungan dan seorang lagi mengawasi semakan.

Pencipta kandungan adalah seperti model hanya decoder: mereka boleh melihat topik, melihat apa yang anda sudah tulis, dan kemudian terus menjana kandungan berdasarkan konteks itu. Mereka sangat bagus menulis kandungan yang menarik dan informatif, tetapi tidak selalu pilihan terbaik apabila tugasan hanya untuk mengklasifikasikan, mendapatkan semula, atau mengekod maklumat. Contoh keluarga model hanya decoder termasuk model GPT dan Llama.

Penilai adalah seperti model hanya Encoder, mereka melihat kursus yang ditulis dan jawapan, perhatikan hubungan antara mereka dan memahami konteks, tetapi mereka tidak pandai menjana kandungan. Contoh model hanya Encoder ialah BERT.

Bayangkan kita juga mempunyai seseorang yang boleh mencipta dan menilai kuiz, ini adalah model Encoder-Decoder. Beberapa contoh ialah BART dan T5.

### Perkhidmatan berbanding Model

Sekarang, mari bercakap tentang perbezaan antara perkhidmatan dan model. Perkhidmatan adalah produk yang ditawarkan oleh Penyedia Perkhidmatan Awan, dan selalunya gabungan model, data, dan komponen lain. Model adalah komponen utama perkhidmatan, dan biasanya model asas, seperti LLM.

Perkhidmatan sering dioptimumkan untuk penggunaan pengeluaran dan selalunya lebih mudah digunakan berbanding model, melalui antara muka pengguna grafik. Walau bagaimanapun, perkhidmatan tidak selalu tersedia secara percuma, dan mungkin memerlukan langganan atau bayaran untuk digunakan, sebagai pertukaran untuk menggunakan peralatan dan sumber pemilik perkhidmatan, mengoptimumkan perbelanjaan dan skala dengan mudah. Contoh perkhidmatan ialah [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), yang menawarkan pelan kadar bayar-semasa-guna, bermakna pengguna dikenakan caj mengikut penggunaan perkhidmatan. Azure OpenAI Service juga menawarkan keselamatan bertaraf perusahaan dan rangka kerja AI bertanggungjawab di atas keupayaan model.

Model adalah artifak rangkaian neural: parameter, berat, seni bina, tokenizer, dan konfigurasi sokongan. Menjalankan model secara lokal atau dalam persekitaran peribadi memerlukan perkakasan yang sesuai, infrastruktur perkhidmatan, pemantauan, dan sama ada lesen sumber terbuka/berat terbuka yang sesuai atau lesen komersial. Model berat terbuka seperti Llama 4 atau model Mistral boleh dihoskan sendiri, tetapi mereka masih memerlukan kuasa pengiraan dan kepakaran operasi.

## Cara menguji dan mengulangi dengan model berbeza untuk memahami prestasi di Azure


Setelah pasukan kami meneroka landskap LLM semasa dan mengenal pasti beberapa calon yang baik untuk senario mereka, langkah seterusnya adalah mengujinya pada data mereka dan pada beban kerja mereka. Ini adalah proses berulang, dilakukan melalui eksperimen dan pengukuran.
Kebanyakan model yang kami sebutkan dalam perenggan sebelumnya (model OpenAI, model berat terbuka seperti Llama 4 dan Mistral, dan model Hugging Face) tersedia dalam [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), dahulunya Azure AI Studio/Azure AI Foundry, adalah platform Azure yang bersatu untuk membina aplikasi dan agen AI. Ia membantu pembangun menguruskan kitar hayat dari eksperimen dan penilaian hingga pelaksanaan, pemantauan, dan tadbir urus. Katalog model dalam Microsoft Foundry membolehkan pengguna untuk:

- Mencari model asas yang diminati dalam katalog, termasuk model yang dijual oleh Azure dan model dari rakan kongsi dan pembekal komuniti. Pengguna boleh menapis mengikut tugas, penyedia, lesen, pilihan pelaksanaan, atau nama.

![Model catalog](../../../translated_images/ms/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Meninjau kad model, termasuk penerangan terperinci tentang penggunaan yang dimaksudkan dan data latihan, contoh kod dan keputusan penilaian pada perpustakaan penilaian dalaman.

![Model card](../../../translated_images/ms/ModelCard.598051692c6e400d.webp)

- Membandingkan penanda aras antara model dan set data yang tersedia dalam industri untuk menilai yang mana memenuhi senario perniagaan, melalui pane [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Model benchmarks](../../../translated_images/ms/ModelBenchmarks.254cb20fbd06c03a.webp)

- Menghaluskan model yang disokong pada data latihan tersuai untuk meningkatkan prestasi model pada beban kerja tertentu, menggunakan kebolehan eksperimen dan penjejakan Microsoft Foundry.

![Model fine-tuning](../../../translated_images/ms/FineTuning.aac48f07142e36fd.webp)

- Melaksanakan model terlatih asal atau versi yang dihaluskan ke titik inferens masa nyata jauh, menggunakan pengiraan terurus atau pilihan pelaksanaan tanpa pelayan, untuk membolehkan aplikasi menggunakannya.

![Model deployment](../../../translated_images/ms/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Tidak semua model dalam katalog kini tersedia untuk penghalusan dan/atau pelaksanaan bayar-semasa-guna. Semak kad model untuk butiran mengenai kebolehan dan had model.

## Memperbaiki keputusan LLM

Kami telah meneroka bersama pasukan startup kami pelbagai jenis LLM dan platform awan (Microsoft Foundry) yang membolehkan kami membandingkan model yang berlainan, menilainya pada data ujian, memperbaiki prestasi, dan melaksanakannya pada titik inferens.

Tetapi bilakah mereka harus mempertimbangkan penghalusan model daripada menggunakan model terlatih siap? Adakah terdapat pendekatan lain untuk meningkatkan prestasi model pada beban kerja tertentu?

Terdapat beberapa pendekatan yang perniagaan boleh gunakan untuk mendapatkan keputusan yang mereka perlukan daripada LLM. Anda boleh memilih jenis model yang berlainan dengan tahap latihan yang berbeza apabila melaksanakan LLM dalam pengeluaran, dengan tahap kerumitan, kos, dan kualiti yang berbeza. Berikut adalah beberapa pendekatan yang berbeza:

- **Kejuruteraan prompt dengan konteks**. Idea adalah untuk menyediakan konteks yang cukup apabila anda prompt untuk memastikan anda mendapat jawapan yang anda perlukan.

- **Generasi Augmented Pengambilan, RAG**. Data anda mungkin wujud dalam pangkalan data atau titik akhir web sebagai contoh, untuk memastikan data ini, atau sebahagian daripadanya, dimasukkan pada masa prompt, anda boleh mengambil data berkaitan dan menjadikannya sebahagian daripada prompt pengguna.

- **Model yang dihaluskan**. Di sini, anda melatih model lebih lanjut pada data anda sendiri yang menyebabkan model menjadi lebih tepat dan responsif terhadap keperluan anda tetapi mungkin mahal.

![LLMs deployment](../../../translated_images/ms/Deploy.18b2d27412ec8c02.webp)

Sumber imej: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Kejuruteraan Prompt dengan Konteks

LLM terlatih siap berfungsi dengan sangat baik pada tugas bahasa semula jadi yang umum, walaupun hanya dengan memanggilnya dengan prompt pendek, seperti ayat untuk dilengkapkan atau soalan – yang dikenali sebagai pembelajaran “zero-shot”.

Walau bagaimanapun, semakin banyak pengguna dapat membingkai pertanyaan mereka, dengan permintaan terperinci dan contoh – Konteks – semakin tepat dan hampir dengan jangkaan pengguna jawapannya. Dalam hal ini, kita bercakap tentang pembelajaran “one-shot” jika prompt hanya mengandungi satu contoh dan “few-shot learning” jika ia mengandungi beberapa contoh.
Kejuruteraan prompt dengan konteks adalah pendekatan yang paling menjimatkan kos untuk memulakan.

### Generasi Augmented Pengambilan (RAG)

LLM mempunyai had bahawa mereka hanya boleh menggunakan data yang telah digunakan semasa latihan mereka untuk menjana jawapan. Ini bermaksud mereka tidak mengetahui apa-apa tentang fakta yang berlaku selepas proses latihan mereka, dan mereka tidak dapat mengakses maklumat bukan awam (seperti data syarikat).
Ini boleh diatasi melalui RAG, teknik yang menambah prompt dengan data luaran dalam bentuk potongan dokumen, mengambil kira had panjang prompt. Ini disokong oleh alat Pangkalan Data Vektor (seperti [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) yang mengambil potongan berguna dari pelbagai sumber data yang telah ditentukan dan menambahkannya ke Konteks prompt.

Teknik ini sangat berguna apabila perniagaan tidak mempunyai cukup data, masa, atau sumber untuk menghaluskan LLM, tetapi masih ingin meningkatkan prestasi pada beban kerja tertentu dan mengurangkan risiko jawapan yang dihalusinasi, lapuk, atau tidak disokong.

### Model yang dihaluskan

Penghalusan adalah proses yang menggunakan pembelajaran pemindahan untuk ‘menyesuaikan’ model kepada tugas huluan atau untuk menyelesaikan masalah tertentu. Berbeza dengan pembelajaran few-shot dan RAG, ia menghasilkan model baru dengan berat dan bias yang dikemas kini. Ia memerlukan set contoh latihan yang terdiri daripada satu input (prompt) dan output yang berkaitan (penyelesaian).
Ini akan menjadi pendekatan yang disukai jika:

- **Menggunakan model khusus tugas yang lebih kecil**. Sesebuah perniagaan ingin menghaluskan model yang lebih kecil untuk tugas sempit daripada berulang kali menggunakan model frontier yang lebih besar, menghasilkan penyelesaian yang lebih menjimatkan kos dan cepat.

- **Mempertimbangkan kelewatan masa**. Kelewatan masa penting untuk kes penggunaan tertentu, jadi tidak mungkin menggunakan prompt yang sangat panjang atau jumlah contoh yang harus dipelajari dari model tidak sesuai dengan had panjang prompt.

- **Menyesuaikan tingkah laku stabil**. Sesebuah perniagaan mempunyai banyak contoh berkualiti tinggi dan ingin model secara konsisten mengikuti corak tugas, format output, nada, atau gaya khusus domain. Jika masalah utamanya adalah fakta terkini atau pengetahuan peribadi yang sering berubah, gunakan RAG dan bukan bergantung hanya pada penghalusan.

### Model terlatih

Melatih LLM dari awal tanpa ragu-ragu adalah pendekatan yang paling sukar dan paling kompleks untuk digunakan, memerlukan sejumlah besar data, sumber mahir, dan kuasa pengkomputeran yang sesuai. Pilihan ini hanya harus dipertimbangkan dalam senario di mana perniagaan mempunyai kes penggunaan khusus domain dan sejumlah besar data berfokus domain.

## Semakan Pengetahuan

Apakah pendekatan yang baik untuk memperbaiki keputusan penyelesaian LLM?

1. Kejuruteraan prompt dengan konteks
1. RAG
1. Model yang dihaluskan

A: Ketiga-tiganya boleh membantu. Mulakan dengan kejuruteraan prompt dan konteks untuk penambahbaikan cepat, dan gunakan RAG apabila model memerlukan fakta terkini atau data perniagaan peribadi. Pilih penghalusan apabila anda mempunyai cukup contoh berkualiti tinggi dan memerlukan model mengikuti corak tugas, format, nada, atau domain secara konsisten.

## 🚀 Cabaran

Baca lebih lanjut tentang bagaimana anda boleh [menggunakan RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) untuk perniagaan anda.

## Kerja Hebat, Teruskan Pembelajaran Anda

Selepas menyelesaikan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif kami](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan AI Generatif anda!

Pergi ke Pelajaran 3 di mana kita akan melihat bagaimana untuk [membina dengan AI Generatif secara Bertanggungjawab](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->