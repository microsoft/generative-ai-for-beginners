<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3772dcd23a98e2010f53ce8b9c583631",
  "translation_date": "2026-01-18T18:41:52+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "ms"
}
-->
[![Model Sumber Terbuka](../../../../../translated_images/ms/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Penyempurnaan Model Bahasa Besar Anda

Menggunakan model bahasa besar untuk membina aplikasi AI generatif datang dengan cabaran baru. Isu utama ialah memastikan kualiti respons (ketepatan dan kaitan) dalam kandungan yang dijana oleh model untuk permintaan pengguna tertentu. Dalam pelajaran sebelum ini, kami membincangkan teknik seperti kejuruteraan arahan (prompt engineering) dan penjanaan dipertingkatkan pengambilan data (retrieval-augmented generation) yang cuba menyelesaikan masalah dengan _mengubah input arahan_ kepada model sedia ada.

Dalam pelajaran hari ini, kami membincangkan teknik ketiga, **penyempurnaan (fine-tuning)**, yang cuba menangani cabaran tersebut dengan _melatih semula model itu sendiri_ menggunakan data tambahan. Mari kita selami butiran.

## Objektif Pembelajaran

Pelajaran ini memperkenalkan konsep penyempurnaan untuk model bahasa yang telah dilatih sebelumnya, meneroka manfaat dan cabaran pendekatan ini, serta memberikan panduan tentang bila dan bagaimana menggunakan penyempurnaan untuk meningkatkan prestasi model AI generatif anda.

Menjelang akhir pelajaran ini, anda sepatutnya dapat menjawab soalan-soalan berikut:

- Apakah penyempurnaan untuk model bahasa?
- Bila, dan mengapa, penyempurnaan berguna?
- Bagaimana saya boleh menyempurnakan model yang telah dilatih sebelumnya?
- Apakah had penyempurnaan?

Bersedia? Mari kita mulakan.

## Panduan Bergambar

Ingin mendapatkan gambaran besar tentang apa yang akan kita bincangkan sebelum mendalaminya? Lihat panduan bergambar ini yang menerangkan perjalanan pembelajaran untuk pelajaran ini - dari mempelajari konsep utama dan motivasi untuk penyempurnaan, hingga memahami proses dan amalan terbaik untuk melaksanakan tugasan penyempurnaan. Topik ini sangat menarik untuk diterokai, jadi jangan lupa untuk melihat halaman [Sumber](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) untuk pautan tambahan yang menyokong perjalanan pembelajaran kendiri anda!

![Panduan Bergambar Penyempurnaan Model Bahasa](../../../../../translated_images/ms/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Apakah penyempurnaan untuk model bahasa?

Secara definisi, model bahasa besar dilatih terlebih dahulu (_pre-trained_) pada sejumlah besar teks yang diperoleh dari pelbagai sumber termasuk internet. Seperti yang kita pelajari dalam pelajaran sebelum ini, kita memerlukan teknik seperti _kejuruteraan arahan_ dan _penjanaan dipertingkatkan pengambilan data_ untuk meningkatkan kualiti respons model terhadap soalan pengguna ("arahan").

Satu teknik kejuruteraan arahan yang popular melibatkan memberi model lebih panduan tentang apa yang dijangka dalam respons sama ada dengan menyediakan _arahan_ (panduan eksplisit) atau _memberi beberapa contoh_ (panduan implisit). Ini dirujuk sebagai _pembelajaran beberapa contoh_ (few-shot learning) tetapi ia mempunyai dua batasan:

- Had token model boleh mengehadkan jumlah contoh yang boleh diberi, serta keberkesanannya.
- Kos token model boleh menjadikan ia mahal untuk menambah contoh pada setiap arahan, dan mengehadkan fleksibiliti.

Penyempurnaan adalah amalan biasa dalam sistem pembelajaran mesin di mana kita mengambil model yang telah dilatih sebelumnya dan melatih semula model tersebut dengan data baru untuk memperbaiki prestasinya dalam tugasan tertentu. Dalam konteks model bahasa, kita boleh menyempurnakan model pra-latih _dengan set contoh terpilih untuk tugasan atau domain aplikasi tertentu_ untuk mencipta **model tersuai** yang mungkin lebih tepat dan relevan untuk tugasan atau domain tersebut. Manfaat sampingan penyempurnaan ialah ia juga boleh mengurangkan bilangan contoh yang diperlukan untuk pembelajaran beberapa contoh - mengurangkan penggunaan token dan kos berkaitan.

## Bila dan mengapa kita harus menyempurnakan model?

Dalam _konteks ini_, apabila kita bercakap tentang penyempurnaan, kita merujuk kepada penyempurnaan **terarah** di mana latihan semula dijalankan dengan **menambah data baru** yang tidak termasuk dalam dataset latihan asal. Ini berbeza daripada pendekatan penyempurnaan tanpa pengawasan di mana model dilatih semula menggunakan data asal, tetapi dengan hiperparameter yang berbeza.

Perkara utama yang perlu diingat ialah penyempurnaan adalah teknik lanjutan yang memerlukan tahap kepakaran tertentu untuk mencapai hasil yang diingini. Jika dilakukan dengan tidak betul, ia mungkin tidak memberikan peningkatan yang dijangka, malah boleh merosakkan prestasi model untuk domain sasaran anda.

Jadi, sebelum anda belajar "bagaimana" untuk menyempurnakan model bahasa, anda perlu tahu "mengapa" anda perlu memilih laluan ini, dan "bila" hendak memulakan proses penyempurnaan. Mulakan dengan bertanya pada diri anda soalan-soalan ini:

- **Kes Penggunaan**: Apakah _kes penggunaan_ anda untuk penyempurnaan? Aspek manakah model pra-latih semasa yang ingin anda perbaiki?
- **Alternatif**: Adakah anda telah mencuba _teknik lain_ untuk mencapai hasil yang diinginkan? Gunakan teknik itu untuk mencipta asas perbandingan.
  - Kejuruteraan arahan: Cuba teknik seperti few-shot prompting dengan contoh respons arahan yang relevan. Nilai kualiti respons.
  - Penjanaan Dipertingkatkan Pengambilan: Cuba meningkat arahan dengan hasil carian dari data anda. Nilai kualiti respons.
- **Kos**: Adakah anda mengenal pasti kos penyempurnaan?
  - Kebolehlatihan - adakah model pra-latih tersedia untuk penyempurnaan?
  - Usaha - untuk menyediakan data latihan, menilai & memperbaiki model.
  - Komputasi - untuk menjalankan tugasan penyempurnaan, dan menggunakan model yang telah disempurnakan
  - Data - akses kepada contoh berkualiti yang mencukupi untuk impak penyempurnaan
- **Manfaat**: Adakah anda mengesahkan manfaat penyempurnaan?
  - Kualiti - adakah model yang disempurnakan mengatasi asas?
  - Kos - adakah ia mengurangkan penggunaan token dengan mempermudah arahan?
  - Kebolehlanjutan - bolehkah anda menggunakan semula model asas untuk domain baru?

Dengan menjawab soalan-soalan ini, anda sepatutnya dapat memutuskan jika penyempurnaan adalah pendekatan yang tepat untuk kes penggunaan anda. Idealnya, pendekatan ini sah hanya jika manfaat melebihi kos. Setelah anda memutuskan untuk meneruskan, sudah tiba masanya untuk memikirkan _bagaimana_ anda boleh menyempurnakan model pra-latih tersebut.

Ingin mendapatkan lebih banyak pandangan tentang proses membuat keputusan? Tonton [Untuk menyempurnakan atau tidak menyempurnakan](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Bagaimana kita boleh menyempurnakan model pra-latih?

Untuk menyempurnakan model pra-latih, anda perlu mempunyai:

- model pra-latih untuk disempurnakan
- set data untuk digunakan dalam penyempurnaan
- persekitaran latihan untuk menjalankan tugasan penyempurnaan
- persekitaran hosting untuk menggunakan model yang telah disempurnakan

## Penyempurnaan Dalam Tindakan

Sumber berikut menyediakan tutorial langkah demi langkah untuk membimbing anda melalui contoh sebenar menggunakan model terpilih dengan set data terpilih. Untuk mengikuti tutorial ini, anda memerlukan akaun pada penyedia tertentu, bersama-sama akses kepada model dan set data yang relevan.

| Penyedia     | Tutorial                                                                                                                                                                       | Penerangan                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Cara menyempurnakan model chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)               | Belajar menyempurnakan `gpt-35-turbo` untuk domain spesifik ("pembantu resipi") dengan menyediakan data latihan, menjalankan tugasan penyempurnaan, dan menggunakan model yang telah disempurnakan untuk inferens.                                                                                                                                                                                                                   |
| Azure OpenAI | [Tutorial penyempurnaan GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Belajar menyempurnakan model `gpt-35-turbo-0613` **di Azure** dengan langkah-langkah untuk mencipta & memuat naik data latihan, menjalankan tugasan penyempurnaan. Gunakan & gunakan model baru tersebut.                                                                                                                                                                                                                             |
| Hugging Face | [Menyempurnakan LLM dengan Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                            | Pos blog ini membimbing anda menyempurnakan _LLM terbuka_ (contoh: `CodeLlama 7B`) menggunakan perpustakaan [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) dengan set data terbuka pada Hugging Face.                                                                   |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 🤗 AutoTrain | [Menyempurnakan LLM dengan AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                        | AutoTrain (atau AutoTrain Advanced) adalah perpustakaan Python yang dibangunkan oleh Hugging Face yang membolehkan penyempurnaan untuk pelbagai tugasan termasuk penyempurnaan LLM. AutoTrain adalah penyelesaian tanpa kod dan penyempurnaan boleh dilakukan dalam awan anda sendiri, di Hugging Face Spaces atau secara lokal. Ia menyokong GUI berasaskan web, CLI dan latihan melalui fail konfigurasi yaml.                             |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 🦥 Unsloth | [Menyempurnakan LLM dengan Unsloth](https://github.com/unslothai/unsloth)                                                                                                       | Unsloth adalah rangka kerja sumber terbuka yang menyokong penyempurnaan LLM dan pembelajaran penguatan (RL). Unsloth mempermudah latihan lokal, penilaian, dan penggunaan dengan [notebook](https://github.com/unslothai/notebooks) yang sedia untuk digunakan. Ia juga menyokong teks-ke-ucapan (TTS), BERT dan model multimodal. Untuk bermula, baca panduan langkah demi langkah mereka [Panduan Penyempurnaan LLM](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
## Tugasan

Pilih salah satu tutorial di atas dan lalui ia. _Kami mungkin menggandakan versi tutorial ini dalam Jupyter Notebooks dalam repo ini untuk rujukan sahaja. Sila gunakan sumber asal secara terus untuk mendapatkan versi terkini_.

## Kerja Hebat! Teruskan Pembelajaran Anda.

Selepas menamatkan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif anda!

Tahniah!! Anda telah menamatkan pelajaran terakhir dari siri v2 untuk kursus ini! Jangan berhenti belajar dan membina. \*\*Lihat halaman [SUMBER](RESOURCES.md?WT.mc_id=academic-105485-koreyst) untuk senarai cadangan tambahan khusus untuk topik ini.

Siri pelajaran v1 kami juga telah dikemas kini dengan lebih banyak tugasan dan konsep. Luangkan masa seketika untuk menyegarkan pengetahuan anda - dan sila [kongsi soalan dan maklum balas anda](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) untuk membantu kami memperbaiki pelajaran-pelajaran ini bagi komuniti.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau kesilapan tafsiran yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->