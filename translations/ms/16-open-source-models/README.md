<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8b2d4bb727c877ebf9edff8623d16b9",
  "translation_date": "2025-09-06T10:21:41+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "ms"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.ms.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Pengenalan

Dunia LLM sumber terbuka sangat menarik dan sentiasa berkembang. Pelajaran ini bertujuan untuk memberikan pandangan mendalam tentang model sumber terbuka. Jika anda mencari maklumat tentang bagaimana model proprietari dibandingkan dengan model sumber terbuka, pergi ke pelajaran ["Meneroka dan Membandingkan LLM Berbeza"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Pelajaran ini juga akan merangkumi topik penalaan halus tetapi penjelasan yang lebih terperinci boleh didapati dalam pelajaran ["Penalaan Halus LLM"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Matlamat Pembelajaran

- Memahami model sumber terbuka
- Memahami manfaat bekerja dengan model sumber terbuka
- Meneroka model sumber terbuka yang tersedia di Hugging Face dan Azure AI Studio

## Apakah Model Sumber Terbuka?

Perisian sumber terbuka telah memainkan peranan penting dalam pertumbuhan teknologi di pelbagai bidang. Open Source Initiative (OSI) telah mendefinisikan [10 kriteria untuk perisian](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) untuk diklasifikasikan sebagai sumber terbuka. Kod sumber mesti dikongsi secara terbuka di bawah lesen yang diluluskan oleh OSI.

Walaupun pembangunan LLM mempunyai elemen yang serupa dengan pembangunan perisian, prosesnya tidak sama sepenuhnya. Ini telah membawa banyak perbincangan dalam komuniti tentang definisi sumber terbuka dalam konteks LLM. Untuk model sejajar dengan definisi tradisional sumber terbuka, maklumat berikut harus tersedia secara umum:

- Dataset yang digunakan untuk melatih model.
- Berat penuh model sebagai sebahagian daripada latihan.
- Kod penilaian.
- Kod penalaan halus.
- Berat penuh model dan metrik latihan.

Pada masa ini, hanya beberapa model yang memenuhi kriteria ini. Model [OLMo yang dicipta oleh Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) adalah salah satu yang sesuai dengan kategori ini.

Untuk pelajaran ini, kita akan merujuk kepada model sebagai "model terbuka" kerana mereka mungkin tidak memenuhi kriteria di atas pada masa penulisan.

## Manfaat Model Terbuka

**Sangat Boleh Disesuaikan** - Oleh kerana model terbuka dikeluarkan dengan maklumat latihan yang terperinci, penyelidik dan pembangun boleh mengubah suai dalaman model. Ini membolehkan penciptaan model yang sangat khusus yang disesuaikan untuk tugas atau bidang kajian tertentu. Beberapa contoh termasuk penjanaan kod, operasi matematik, dan biologi.

**Kos** - Kos per token untuk menggunakan dan menyebarkan model ini lebih rendah daripada model proprietari. Apabila membina aplikasi Generative AI, membandingkan prestasi dengan harga berdasarkan kes penggunaan anda adalah penting.

![Kos Model](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.ms.png)  
Sumber: Artificial Analysis

**Fleksibiliti** - Bekerja dengan model terbuka membolehkan anda fleksibel dalam menggunakan model yang berbeza atau menggabungkannya. Contohnya adalah [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) di mana pengguna boleh memilih model yang digunakan secara langsung dalam antara muka pengguna:

![Pilih Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.ms.png)

## Meneroka Model Terbuka Berbeza

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), yang dibangunkan oleh Meta, adalah model terbuka yang dioptimumkan untuk aplikasi berasaskan sembang. Ini disebabkan oleh kaedah penalaan halusnya, yang melibatkan sejumlah besar dialog dan maklum balas manusia. Dengan kaedah ini, model menghasilkan hasil yang lebih sejajar dengan jangkaan manusia, memberikan pengalaman pengguna yang lebih baik.

Beberapa contoh versi Llama yang telah ditala halus termasuk [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), yang mengkhususkan dalam bahasa Jepun dan [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), yang merupakan versi yang dipertingkatkan daripada model asas.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) adalah model terbuka yang memberi tumpuan kepada prestasi tinggi dan kecekapan. Ia menggunakan pendekatan Mixture-of-Experts yang menggabungkan sekumpulan model pakar khusus ke dalam satu sistem di mana bergantung pada input, model tertentu dipilih untuk digunakan. Ini menjadikan pengiraan lebih berkesan kerana model hanya menangani input yang mereka pakar.

Beberapa contoh versi Mistral yang telah ditala halus termasuk [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), yang memberi tumpuan kepada domain perubatan dan [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), yang melakukan pengiraan matematik.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) adalah LLM yang dicipta oleh Technology Innovation Institute (**TII**). Falcon-40B dilatih pada 40 bilion parameter yang telah terbukti memberikan prestasi lebih baik daripada GPT-3 dengan bajet pengiraan yang lebih rendah. Ini disebabkan oleh penggunaan algoritma FlashAttention dan perhatian multiquery yang membolehkannya mengurangkan keperluan memori semasa masa inferens. Dengan masa inferens yang dikurangkan ini, Falcon-40B sesuai untuk aplikasi sembang.

Beberapa contoh versi Falcon yang telah ditala halus adalah [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), pembantu yang dibina berdasarkan model terbuka dan [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), yang memberikan prestasi lebih tinggi daripada model asas.

## Bagaimana Memilih

Tiada satu jawapan untuk memilih model terbuka. Tempat yang baik untuk bermula adalah dengan menggunakan ciri penapis tugas di Azure AI Studio. Ini akan membantu anda memahami jenis tugas yang telah dilatih oleh model. Hugging Face juga mengekalkan LLM Leaderboard yang menunjukkan model berprestasi terbaik berdasarkan metrik tertentu.

Apabila ingin membandingkan LLM merentasi jenis yang berbeza, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) adalah satu lagi sumber yang hebat:

![Kualiti Model](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.ms.png)  
Sumber: Artificial Analysis

Jika bekerja pada kes penggunaan tertentu, mencari versi yang telah ditala halus yang memberi tumpuan kepada bidang yang sama boleh menjadi berkesan. Bereksperimen dengan pelbagai model terbuka untuk melihat bagaimana mereka berprestasi mengikut jangkaan anda dan pengguna anda adalah satu lagi amalan yang baik.

## Langkah Seterusnya

Bahagian terbaik tentang model terbuka adalah anda boleh mula bekerja dengan mereka dengan cepat. Lihat [Katalog Model Azure AI Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), yang menampilkan koleksi Hugging Face khusus dengan model yang kita bincangkan di sini.

## Pembelajaran tidak berhenti di sini, teruskan Perjalanan

Selepas menyelesaikan pelajaran ini, lihat [koleksi Pembelajaran AI Generatif kami](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan AI Generatif anda!

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.