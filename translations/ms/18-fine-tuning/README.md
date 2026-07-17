[![Open Source Models](../../../translated_images/ms/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Menalaan Semula LLM Anda

Menggunakan model bahasa besar untuk membina aplikasi AI generatif datang dengan cabaran baru. Isu utama adalah memastikan kualiti respons (ketepatan dan relevan) dalam kandungan yang dijana oleh model untuk permintaan pengguna tertentu. Dalam pelajaran sebelum ini, kita membincangkan teknik seperti kejuruteraan prompt dan penjanaan dipertingkat dengan pengambilan yang cuba menyelesaikan masalah dengan _mengubah input prompt_ kepada model sedia ada.

Dalam pelajaran hari ini, kita membincangkan teknik ketiga, **menalaan semula**, yang cuba menangani cabaran itu dengan _melatih semula model itu sendiri_ dengan data tambahan. Mari kita lihat butirannya.

## Objektif Pembelajaran

Pelajaran ini memperkenalkan konsep menalaan semula untuk model bahasa yang telah dilatih sebelumnya, meneroka faedah dan cabaran pendekatan ini, serta memberikan panduan bila dan bagaimana menggunakan menalaan semula untuk meningkatkan prestasi model AI generatif anda.

Pada akhir pelajaran ini, anda harus dapat menjawab soalan berikut:

- Apa itu menalaan semula untuk model bahasa?
- Bila, dan mengapa, menalaan semula berguna?
- Bagaimana saya boleh menala semula model yang telah dilatih sebelumnya?
- Apakah had menalaan semula?

Sedia? Mari kita mula.

## Panduan Bergambar

Mahu mendapat gambaran besar tentang apa yang akan kita kupas sebelum mula? Lihat panduan bergambar ini yang menggambarkan perjalanan pembelajaran untuk pelajaran ini - dari mempelajari konsep teras dan motivasi untuk menalaan semula, kepada memahami proses dan amalan terbaik untuk melaksanakan tugas menalaan semula. Ini topik yang menarik untuk diterokai, jadi jangan lupa semak halaman [Sumber](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) untuk pautan sokongan tambahan bagi perjalanan pembelajaran kendiri anda!

![Panduan Bergambar Menalaan Semula Model Bahasa](../../../translated_images/ms/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Apa itu menalaan semula untuk model bahasa?

Secara definisi, model bahasa besar adalah _dilatih sebelumnya_ pada sejumlah besar teks yang diperoleh dari pelbagai sumber termasuk internet. Seperti yang telah kita pelajari dalam pelajaran sebelum ini, kita memerlukan teknik seperti _kejuruteraan prompt_ dan _penjanaan dipertingkat dengan pengambilan_ untuk meningkatkan kualiti respons model kepada soalan pengguna ("prompt").

Teknik kejuruteraan prompt yang popular melibatkan memberikan model lebih banyak panduan tentang apa yang diharapkan dalam respons sama ada dengan menyediakan _arahan_ (panduan eksplisit) atau _memberikannya beberapa contoh_ (panduan implisit). Ini dikenali sebagai _pembelajaran beberapa contoh_ tetapi ia mempunyai dua had:

- Had token model boleh mengehadkan jumlah contoh yang anda boleh beri, dan mengehadkan keberkesanan.
- Kos token model boleh menyebabkan mahal untuk menambah contoh pada setiap prompt, dan mengehadkan fleksibiliti.

Menalaan semula ialah amalan biasa dalam sistem pembelajaran mesin di mana kita mengambil model yang dilatih sebelum ini dan melatih semula dengan data baru untuk meningkatkan prestasinya pada tugas khusus. Dalam konteks model bahasa, kita boleh menala semula model yang dilatih sebelumnya _dengan set contoh yang dikurasi untuk tugas atau domain aplikasi tertentu_ untuk mencipta **model khusus** yang mungkin lebih tepat dan relevan untuk tugas atau domain tertentu itu. Manfaat sampingan menalaan semula adalah ia juga boleh mengurangkan jumlah contoh yang diperlukan untuk pembelajaran beberapa contoh - mengurangkan penggunaan token dan kos berkaitan.

## Bila dan mengapa kita harus menala semula model?

Dalam _konteks ini_, apabila kita bercakap tentang menalaan semula, kita merujuk kepada menalaan semula **terarah** di mana latihan semula dilakukan dengan **menambah data baru** yang bukan sebahagian daripada set data latihan asal. Ini berbeza dengan pendekatan menalaan semula tanpa pengawasan di mana model dilatih semula pada data asal, tetapi dengan hiperparameter yang berbeza.

Perkara penting untuk diingat adalah menalaan semula ialah teknik lanjutan yang memerlukan tahap kepakaran tertentu untuk mendapatkan hasil yang diingini. Jika dilakukan dengan tidak betul, ia mungkin tidak memberikan peningkatan yang dijangka, malah boleh merendahkan prestasi model untuk domain sasaran anda.

Jadi, sebelum anda belajar "bagaimana" menala semula model bahasa, anda perlu tahu "mengapa" anda harus mengambil laluan ini, dan "bila" untuk memulakan proses menalaan semula. Mula dengan bertanya kepada diri anda soalan berikut:

- **Kes Penggunaan**: Apakah _kes penggunaan_ anda untuk menalaan semula? Aspek manakah model yang telah dilatih sebelumnya yang anda mahu tingkatkan?
- **Alternatif**: Adakah anda telah mencuba _teknik lain_ untuk mencapai hasil yang diingini? Gunakannya untuk membuat asas perbandingan.
  - Kejuruteraan prompt: Cuba teknik seperti prompt beberapa contoh dengan contoh respons prompt yang relevan. Nilai kualiti respons.
  - Penjanaan Dipertingkat dengan Pengambilan: Cuba tambahkan prompt dengan hasil carian yang diambil dari data anda. Nilai kualiti respons.
- **Kos**: Adakah anda mengenal pasti kos untuk menalaan semula?
  - Kebolehtalaan - adakah model yang dilatih sebelumnya tersedia untuk menalaan semula?
  - Usaha - untuk menyediakan data latihan, menilai & memperhalusi model.
  - Komputer - untuk menjalankan kerja menalaan semula, dan menyebarkan model yang telah ditala semula
  - Data - akses kepada contoh berkualiti mencukupi untuk impak menalaan semula
- **Faedah**: Adakah anda telah mengesahkan faedah menalaan semula?
  - Kualiti - adakah model yang ditala semula mengatasi asas?
  - Kos - adakah ia mengurangkan penggunaan token dengan mempermudah prompt?
  - Kebolehluasan - bolehkah anda menggunakan model asas untuk domain baru?

Dengan menjawab soalan-soalan ini, anda harus dapat memutuskan sama ada menalaan semula adalah pendekatan yang betul untuk kes penggunaan anda. Idealnya, pendekatan ini sah hanya jika faedah melebihi kos. Setelah anda memutuskan untuk meneruskan, tiba masanya untuk berfikir tentang _bagaimana_ anda boleh menala semula model yang dilatih sebelumnya.

Mahu mendapatkan lebih banyak maklumat tentang proses membuat keputusan? Tonton [Memperhalusi atau tidak memperhalusi](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Bagaimana kita boleh menala semula model yang telah dilatih sebelumnya?

Untuk menala semula model yang telah dilatih sebelumnya, anda perlu mempunyai:

- model yang telah dilatih sebelumnya untuk ditala semula
- set data untuk digunakan bagi menalaan semula
- persekitaran latihan untuk menjalankan kerja menalaan semula
- persekitaran penghosan untuk menyebarkan model yang telah ditala semula

## Menalaan Semula di Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ialah tempat anda menala semula, menyebarkan, dan mengurus model khusus di Azure hari ini (ia menggabungkan apa yang dulu dikenali sebagai Azure OpenAI Studio dan Azure AI Studio). Sebelum anda memulakan kerja, adalah baik untuk memahami pilihan yang diberikan Foundry - dan amalan terbaik yang disyorkan oleh platform itu. Di bawah hud, Foundry menggunakan **LoRA (adaptasi pangkat rendah)** untuk menala semula model dengan cekap, yang memastikan latihan lebih pantas dan lebih mampu milik daripada melatih semula setiap berat.

### Langkah 1: Pilih teknik latihan

Foundry menyokong tiga teknik menalaan semula. **Mulakan dengan SFT** - ia merangkumi pelbagai senario paling luas.

| Teknik | Apa yang dilakukan | Bila digunakan |
| --- | --- | --- |
| **Menalaan Semula Terarah (SFT)** | Melatih pada pasangan contoh input/output supaya model belajar menghasilkan respons yang anda mahukan. | Lalai untuk kebanyakan tugas: pengkhususan domain, prestasi tugas, gaya dan nada, mengikuti arahan, dan penyesuaian bahasa. |
| **Pengoptimuman Keutamaan Terus (DPO)** | Belajar daripada pasangan respons _yang dipilih vs. tidak dipilih_ untuk menyelaraskan output dengan keutamaan manusia. | Meningkatkan kualiti respons, keselamatan, dan penjajaran apabila anda mempunyai maklum balas perbandingan. |
| **Penalaan Semula Penguatan (RFT)** | Menggunakan isyarat ganjaran dari _penilai_ untuk mengoptimumkan tingkah laku kompleks dengan pembelajaran penguatan. | Domain objektif, berat pemikiran (matematik, kimia, fizik) dengan jawapan yang jelas betul/salah. Memerlukan lebih kepakaran ML. |

### Langkah 2: Pilih tahap latihan

Foundry membenarkan anda memilih bagaimana dan di mana latihan dijalankan:

- **Standard** - melatih dalam wilayah sumber anda dan menjamin kediaman data. Gunakan bila data mesti kekal dalam wilayah tertentu.
- **Global** - lebih murah dan lebih cepat untuk beratur dengan menggunakan kapasiti di luar wilayah anda (data dan berat disalin ke wilayah latihan). Lalai yang baik apabila kediaman data bukan keperluan.
- **Pembangun** - kos terendah, menggunakan kapasiti menganggur tanpa jaminan latensi/SLA (kerja boleh diberhentikan dan disambung semula). Ideal untuk eksperimen.

### Langkah 3: Pilih model asas

Model yang boleh ditala semula termasuk OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini`, dan `gpt-4.1-nano` (SFT; keluarga 4o/4.1 juga menyokong DPO), model penalaran `o4-mini` dan `gpt-5` (RFT), serta model sumber terbuka seperti `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct`, dan `gpt-oss-20b` (SFT pada sumber Foundry). Sentiasa semak [Senarai model menalaan semula](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) semasa untuk kaedah yang disokong, wilayah, dan ketersediaan.

> Foundry menawarkan dua mod: **tanpa pelayan** (penetapan harga berdasarkan penggunaan, tiada kuota GPU untuk diurus, model OpenAI dan terpilih) dan **komputer terurus** (bawa VM sendiri melalui Azure Machine Learning untuk rangkaian model paling luas). Kebanyakan orang harus bermula dengan tanpa pelayan.

### Amalan terbaik Foundry

- **Asas dahulu.** Ukur model asas dengan kejuruteraan prompt dan RAG _sebelum_ anda menala semula, supaya anda dapat membuktikan peningkatan.
- **Mula kecil, kemudian skala.** Mula dengan 50-100 contoh berkualiti tinggi untuk mengesahkan pendekatan, kemudian bertambah kepada 500+ untuk pengeluaran. Kualiti mengatasi kuantiti - buang contoh berkualiti rendah.
- **Format data dengan betul.** Fail latihan dan pengesahan mesti JSONL, UTF-8 **dengan BOM**, kurang daripada 512 MB, menggunakan format mesej chat-completions. Sentiasa sertakan fail pengesahan supaya anda boleh mengawasi overfitting.
- **Pastikan prompt sistem semasa inferens.** Gunakan mesej sistem yang sama apabila anda memanggil model yang anda gunakan semasa latihan.
- **Nilai checkpoint - jangan terus gunakan yang terakhir.** Foundry menyimpan tiga epoch terakhir sebagai checkpoint boleh diedar; pilih yang paling umum dengan memerhati `train_loss` / `valid_loss` dan ketepatan token.
- **Ukur kos token bersama kualiti** apabila membandingkan model yang ditala semula dengan asas.
- **Iterasi dengan menalaan semula berterusan.** Anda boleh menala semula model yang sudah ditala semula pada data baru (disokong untuk model OpenAI).
- **Perhatikan kos penghosan.** Model khusus yang disebarkan mengenakan bayaran setiap jam, dan penyebaran tidak aktif akan dikeluarkan selepas 15 hari - bersihkan apa yang tidak anda perlukan.

Ikuti panduan secara menyeluruh dalam [Sesuaikan model dengan menalaan semula](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst), dan lihat panduan untuk [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) dan [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) apabila anda bersedia untuk teknik lain.

## Menalaan Semula Dalam Tindakan

Sumber berikut menyediakan tutorial langkah demi langkah yang membimbing anda melalui contoh sebenar pada model yang disokong sekarang dengan dataset yang dikurasi. Untuk menggunakannya, anda perlu mempunyai akaun pada penyedia khusus, bersama akses ke model dan dataset yang berkaitan.

| Penyedia     | Tutorial                                                                                                                                                                       | Penerangan                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Cara menala semula model chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Belajar menala semula model chat OpenAI terkini untuk domain khusus ("pembantu resipi") dengan menyediakan data latihan, menjalankan kerja menalaan semula, dan menggunakan model yang telah ditala semula untuk inferens.                                                                                                                                                                                                                                              |
| Microsoft Foundry | [Sesuaikan model dengan menalaan semula](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Belajar menala semula model yang disokong sekarang seperti `gpt-4.1-mini` **di Azure** dengan Microsoft Foundry: sediakan & muat naik data latihan dan pengesahan, jalankan kerja menalaan semula, kemudian sebarkan & gunakan model baru.                                                                                                                                                                                                                                                                 |

| Hugging Face | [Fine-tuning LLMs with Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Catatan blog ini membimbing anda menyelaraskan halus _open LLM_ (cth: `CodeLlama 7B`) menggunakan perpustakaan [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) dengan [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) terbuka di Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fine-tuning LLMs with AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (atau AutoTrain Advanced) adalah perpustakaan python yang dibangunkan oleh Hugging Face yang membolehkan penyelarasan halus untuk banyak tugasan berbeza termasuk penyelarasan halus LLM. AutoTrain adalah penyelesaian tanpa kod dan penyelarasan halus boleh dilakukan di awan anda sendiri, di Hugging Face Spaces atau secara tempatan. Ia menyokong GUI berasaskan web, CLI dan latihan melalui fail konfigurasi yaml.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Fine-tuning LLMs with Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth adalah rangka kerja sumber terbuka yang menyokong penyelarasan halus LLM dan pembelajaran pengukuhan (RL). Unsloth mempermudah latihan tempatan, penilaian, dan penyebaran dengan [notebook](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) yang sedia digunakan. Ia juga menyokong teks-ke-pertuturan (TTS), BERT dan model multimodal. Untuk memulakan, baca panduan langkah demi langkah mereka [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Tugasan

Pilih salah satu tutorial di atas dan lalui mereka. _Kami mungkin akan menyalin versi tutorial ini dalam Jupyter Notebooks dalam repositori ini sebagai rujukan sahaja. Sila gunakan sumber asal terus untuk mendapatkan versi terkini_.

## Kerja Hebat! Teruskan Pembelajaran Anda.

Selepas menyiapkan pelajaran ini, semak koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif anda!

Tahniah!! Anda telah menyiapkan pelajaran terakhir dari siri v2 untuk kursus ini! Jangan berhenti belajar dan membina. \*\*Semak halaman [SUMBER](RESOURCES.md?WT.mc_id=academic-105485-koreyst) untuk senarai cadangan tambahan khusus untuk topik ini.

Siri pelajaran v1 kami juga telah dikemas kini dengan lebih banyak tugasan dan konsep. Jadi luangkan masa seketika untuk menyegarkan pengetahuan anda - dan sila [kongsi soalan dan maklum balas anda](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) untuk membantu kami memperbaiki pelajaran ini untuk komuniti.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->