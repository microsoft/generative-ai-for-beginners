[![Model Sumber Terbuka](../../../translated_images/ms/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Menyempurnakan LLM Anda

Menggunakan model bahasa besar untuk membina aplikasi AI generatif datang dengan cabaran baru. Isu utama adalah memastikan kualiti respons (ketepatan dan kesesuaian) dalam kandungan yang dihasilkan oleh model untuk permintaan pengguna tertentu. Dalam pelajaran sebelumnya, kami membincangkan teknik seperti kejuruteraan arahan dan penjanaan yang dipertingkatkan oleh pemulihan yang cuba menyelesaikan masalah dengan _mengubah input arahan_ kepada model sedia ada.

Dalam pelajaran hari ini, kita akan membincangkan teknik ketiga, **penalaan halus**, yang cuba menangani cabaran tersebut dengan _melatih semula model itu sendiri_ dengan data tambahan. Mari kita selami butirannya.

## Objektif Pembelajaran

Pelajaran ini memperkenalkan konsep penalaan halus untuk model bahasa yang telah dilatih, meneroka manfaat dan cabaran pendekatan ini, serta memberikan panduan bila dan bagaimana menggunakan penalaan halus untuk meningkatkan prestasi model AI generatif anda.

Pada akhir pelajaran ini, anda sepatutnya dapat menjawab soalan berikut:

- Apakah penalaan halus untuk model bahasa?
- Bila dan kenapa penalaan halus berguna?
- Bagaimana saya boleh melakukan penalaan halus pada model yang telah dilatih?
- Apakah batasan penalaan halus?

Sedia? Mari kita mulakan.

## Panduan Bergambar

Ingin mendapatkan gambaran besar apa yang akan kita kupas sebelum bermula? Lihat panduan bergambar ini yang menerangkan perjalanan pembelajaran untuk pelajaran ini - dari mempelajari konsep teras dan motivasi untuk penalaan halus, hingga memahami proses dan amalan terbaik untuk melaksanakan tugasan penalaan halus. Ini adalah topik yang menarik untuk diterokai, jadi jangan lupa untuk menyemak halaman [Sumber](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) untuk pautan tambahan yang menyokong perjalanan pembelajaran kendiri anda!

![Panduan Bergambar untuk Penalaan Halus Model Bahasa](../../../translated_images/ms/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Apakah penalaan halus untuk model bahasa?

Secara definisi, model bahasa besar _telah dilatih terlebih dahulu_ pada jumlah besar teks yang diperoleh dari pelbagai sumber termasuk internet. Seperti yang telah kita pelajari dalam pelajaran sebelum ini, kita perlukan teknik seperti _kejuruteraan arahan_ dan _penjanaan yang dipertingkatkan oleh pemulihan_ untuk meningkatkan kualiti respons model terhadap soalan pengguna ("arahan").

Teknik kejuruteraan arahan yang popular melibatkan memberikan model panduan lebih jelas tentang apa yang dijangka dalam respons sama ada dengan menyediakan _arahan_ (panduan eksplisit) atau _memberikan beberapa contoh_ (panduan implisit). Ini dirujuk sebagai _pembelajaran beberapa contoh_ tetapi ia mempunyai dua batasan:

- Had token model boleh mengehadkan jumlah contoh yang boleh anda berikan, dan mengehadkan keberkesanannya.
- Kos token model boleh menjadikan ia mahal untuk menambah contoh pada setiap arahan, dan mengehadkan fleksibiliti.

Penalaan halus adalah amalan biasa dalam sistem pembelajaran mesin di mana kita mengambil model yang telah dilatih terlebih dahulu dan melatih semula dengan data baru untuk meningkatkan prestasi pada tugasan tertentu. Dalam konteks model bahasa, kita boleh melakukan penalaan halus pada model yang telah dilatih _dengan set contoh yang dibina khusus untuk tugasan atau domain aplikasi tertentu_ untuk mencipta **model khusus** yang mungkin lebih tepat dan relevan untuk tugasan atau domain tersebut. Manfaat sampingan penalaan halus adalah ia juga boleh mengurangkan jumlah contoh yang diperlukan untuk pembelajaran beberapa contoh - mengurangkan penggunaan token dan kos berkaitan.

## Bila dan kenapa harus kita melakukan penalaan halus pada model?

Dalam _konteks ini_, bila kita bercakap tentang penalaan halus, kita merujuk kepada penalaan halus **berpandu** di mana latihan semula dilakukan dengan **menambah data baru** yang bukan sebahagian dari set data latihan asal. Ini berbeza dengan pendekatan penalaan halus tanpa pengawasan di mana model dilatih semula pada data asal, tetapi dengan parameter hiper yang berbeza.

Perkara utama yang perlu diingat ialah penalaan halus adalah teknik lanjutan yang memerlukan tahap kepakaran tertentu untuk mendapatkan hasil yang diingini. Jika dilakukan dengan salah, ia mungkin tidak memberikan penambahbaikan yang diharapkan, malah boleh menurunkan prestasi model untuk domain sasaran anda.

Jadi, sebelum anda belajar "bagaimana" untuk melakukan penalaan halus pada model bahasa, anda perlu tahu "kenapa" anda perlu mengambil jalan ini, dan "bilakah" untuk memulakan proses penalaan halus. Mulakan dengan bertanya pada diri sendiri soalan-soalan ini:

- **Kes Penggunaan**: Apakah _kes penggunaan_ anda untuk penalaan halus? Aspek mana dalam model pra-latih semasa yang anda mahu perbaiki?
- **Alternatif**: Adakah anda sudah mencuba _teknik lain_ untuk mencapai hasil yang diingini? Gunakan mereka untuk mencipta garis asas perbandingan.
  - Kejuruteraan arahan: Cuba teknik seperti arahan beberapa contoh dengan contoh respons arahan yang relevan. Nilai kualiti respons.
  - Penjanaan Dipertingkatkan Pemulihan: Cuba tambah arahan dengan keputusan carian data anda. Nilai kualiti respons.
- **Kos**: Adakah anda sudah mengenal pasti kos untuk penalaan halus?
  - Kebolehtalaan - adakah model pra-latih tersedia untuk penalaan halus?
  - Usaha - untuk menyediakan data latihan, menilai dan memperhalusi model.
  - Pengiraan - untuk menjalankan tugasan penalaan halus, dan menyebarkan model yang telah dipertingkatkan.
  - Data - akses kepada contoh berkualiti yang mencukupi untuk impak penalaan halus.
- **Manfaat**: Adakah anda telah mengesahkan manfaat penalaan halus?
  - Kualiti - adakah model yang ditala halus mengatasi garis asas?
  - Kos - adakah ia mengurangkan penggunaan token dengan memudahkan arahan?
  - Kebolehlanjutan - bolehkah anda menggunakan semula model asas untuk domain baru?

Dengan menjawab soalan ini, anda sepatutnya dapat memutuskan jika penalaan halus adalah pendekatan yang sesuai untuk kes penggunaan anda. Idealnya, pendekatan ini sah hanya jika manfaat melebihi kos. Setelah anda memutuskan untuk meneruskan, tiba masa untuk memikirkan _bagaimana_ anda boleh menala halus model yang telah dilatih.

Mahu mendapatkan lebih banyak pandangan tentang proses membuat keputusan? Tonton [Untuk menala halus atau tidak menala halus](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Bagaimana kita boleh menala halus model yang telah dilatih?

Untuk menala halus model yang telah dilatih, anda perlu mempunyai:

- model yang telah dilatih untuk ditala halus
- set data untuk digunakan dalam penalaan halus
- persekitaran latihan untuk menjalankan tugasan penalaan halus
- persekitaran hos untuk menyebarkan model yang ditala halus

## Penalaan Halus Dalam Tindakan

> **Nota:** `gpt-35-turbo` / `gpt-3.5-turbo`, yang disebut dalam beberapa tutorial di bawah, telah ditamatkan untuk kedua-dua inferens dan penalaan halus. Jika anda memulakan tugasan penalaan halus baru hari ini, sasarkan model yang disokong sekarang - contoh `gpt-4o-mini` atau `gpt-4.1-mini`. Lihat [Senarai model penalaan halus](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) untuk set model yang boleh ditala halus sekarang. Konsep dan langkah dalam tutorial ini masih terpakai.

Sumber berikut menyediakan tutorial langkah demi langkah untuk membimbing anda melalui contoh sebenar menggunakan model terpilih dengan set data yang dibina khusus. Untuk menjalani tutorial ini, anda memerlukan akaun pada penyedia tertentu, bersama akses ke model dan set data yang relevan.

| Penyedia     | Tutorial                                                                                                                                                                       | Penerangan                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Cara menala halus model chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Belajar menala halus `gpt-35-turbo` untuk domain spesifik ("pembantu resipi") dengan menyediakan data latihan, menjalankan tugasan penalaan halus, dan menggunakan model yang telah ditala halus untuk inferens.                                                                                                                                                                                                                                              |
| Azure OpenAI | [Tutorial penalaan halus GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Belajar menala halus model `gpt-35-turbo-0613` **di Azure** dengan mengambil langkah untuk mencipta & memuat naik data latihan, jalankan tugasan penalaan halus. Sebarkan & gunakan model baru.                                                                                                                                                                                                                                                                 |
| Hugging Face | [Penalaan halus LLM dengan Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Pos blog ini membimbing anda menala halus _LLM terbuka_ (contoh: `CodeLlama 7B`) menggunakan perpustakaan [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) dengan [dataset](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) terbuka di Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Penalaan halus LLM dengan AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (atau AutoTrain Advanced) adalah perpustakaan python yang dibangunkan oleh Hugging Face yang membolehkan penalaan halus untuk banyak tugasan berbeza termasuk penalaan halus LLM. AutoTrain adalah penyelesaian tanpa kod dan penalaan halus boleh dilakukan di awan anda sendiri, di Hugging Face Spaces atau secara tempatan. Ia menyokong GUI berasaskan web, CLI, dan latihan melalui fail konfigurasi yaml.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Penalaan halus LLM dengan Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth adalah rangka kerja sumber terbuka yang menyokong penalaan halus LLM dan pembelajaran pengukuhan (RL). Unsloth memudahkan latihan, penilaian, dan penyebaran secara tempatan dengan [notebook](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) yang sedia digunakan. Ia juga menyokong teks ke suara (TTS), model BERT dan multimodal. Untuk bermula, baca panduan langkah demi langkah mereka [Panduan Penalaan Halus LLM](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Tugasan

Pilih salah satu tutorial di atas dan ikuti langkah-langkahnya. _Kami mungkin akan menggandakan versi tutorial ini dalam Jupyter Notebooks di repo ini untuk rujukan sahaja. Sila gunakan sumber asal terus untuk mendapatkan versi terkini_.

## Kerja Hebat! Teruskan Pembelajaran Anda.

Selepas menamatkan pelajaran ini, semak koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif anda!

Tahniah!! Anda telah menamatkan pelajaran terakhir dari siri v2 untuk kursus ini! Jangan berhenti belajar dan membina. \*\*Semak halaman [SUMBER](RESOURCES.md?WT.mc_id=academic-105485-koreyst) untuk senarai cadangan tambahan hanya untuk topik ini.

Siri pelajaran v1 kami juga telah dikemas kini dengan lebih banyak tugasan dan konsep. Jadi luangkan masa untuk menyegarkan kembali pengetahuan anda - dan sila [kongsi soalan dan maklum balas anda](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) untuk membantu kami memperbaiki pelajaran ini untuk komuniti.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->