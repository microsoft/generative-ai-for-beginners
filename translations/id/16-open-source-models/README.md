<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8b2d4bb727c877ebf9edff8623d16b9",
  "translation_date": "2025-09-06T10:21:20+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "id"
}
-->
[![Model Open Source](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.id.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Pendahuluan

Dunia LLM open source sangat menarik dan terus berkembang. Pelajaran ini bertujuan untuk memberikan pandangan mendalam tentang model open source. Jika Anda mencari informasi tentang bagaimana model proprietary dibandingkan dengan model open source, kunjungi pelajaran ["Mengeksplorasi dan Membandingkan Berbagai LLM"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Pelajaran ini juga akan membahas topik fine-tuning, tetapi penjelasan lebih rinci dapat ditemukan di pelajaran ["Fine-Tuning LLMs"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Tujuan Pembelajaran

- Memahami model open source
- Memahami manfaat bekerja dengan model open source
- Mengeksplorasi model open source yang tersedia di Hugging Face dan Azure AI Studio

## Apa itu Model Open Source?

Perangkat lunak open source telah memainkan peran penting dalam perkembangan teknologi di berbagai bidang. Open Source Initiative (OSI) telah mendefinisikan [10 kriteria untuk perangkat lunak](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) agar dapat diklasifikasikan sebagai open source. Kode sumber harus dibagikan secara terbuka di bawah lisensi yang disetujui oleh OSI.

Meskipun pengembangan LLM memiliki elemen yang mirip dengan pengembangan perangkat lunak, prosesnya tidak sepenuhnya sama. Hal ini memunculkan banyak diskusi di komunitas tentang definisi open source dalam konteks LLM. Agar sebuah model sesuai dengan definisi tradisional open source, informasi berikut harus tersedia secara publik:

- Dataset yang digunakan untuk melatih model.
- Bobot model penuh sebagai bagian dari pelatihan.
- Kode evaluasi.
- Kode fine-tuning.
- Bobot model penuh dan metrik pelatihan.

Saat ini hanya ada beberapa model yang memenuhi kriteria ini. [Model OLMo yang dibuat oleh Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) adalah salah satu yang sesuai dengan kategori ini.

Untuk pelajaran ini, kita akan merujuk pada model sebagai "model open" ke depannya karena mungkin tidak sesuai dengan kriteria di atas pada saat penulisan.

## Manfaat Model Open

**Sangat Dapat Disesuaikan** - Karena model open dirilis dengan informasi pelatihan yang rinci, peneliti dan pengembang dapat memodifikasi bagian internal model. Hal ini memungkinkan pembuatan model yang sangat khusus yang disesuaikan untuk tugas atau bidang studi tertentu. Beberapa contohnya adalah generasi kode, operasi matematika, dan biologi.

**Biaya** - Biaya per token untuk menggunakan dan menerapkan model ini lebih rendah dibandingkan dengan model proprietary. Saat membangun aplikasi Generative AI, penting untuk mempertimbangkan kinerja vs harga saat menggunakan model ini untuk kasus penggunaan Anda.

![Biaya Model](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.id.png)  
Sumber: Artificial Analysis

**Fleksibilitas** - Bekerja dengan model open memungkinkan fleksibilitas dalam menggunakan berbagai model atau menggabungkannya. Contohnya adalah [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) di mana pengguna dapat memilih model yang digunakan langsung di antarmuka pengguna:

![Pilih Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.id.png)

## Mengeksplorasi Berbagai Model Open

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), yang dikembangkan oleh Meta, adalah model open yang dioptimalkan untuk aplikasi berbasis chat. Hal ini disebabkan oleh metode fine-tuning-nya, yang melibatkan sejumlah besar dialog dan umpan balik manusia. Dengan metode ini, model menghasilkan hasil yang lebih sesuai dengan ekspektasi manusia, memberikan pengalaman pengguna yang lebih baik.

Beberapa contoh versi fine-tuned dari Llama termasuk [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), yang mengkhususkan diri dalam bahasa Jepang, dan [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), yang merupakan versi yang ditingkatkan dari model dasar.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) adalah model open yang berfokus pada kinerja tinggi dan efisiensi. Model ini menggunakan pendekatan Mixture-of-Experts yang menggabungkan sekelompok model ahli khusus ke dalam satu sistem, di mana tergantung pada input, model tertentu dipilih untuk digunakan. Hal ini membuat komputasi lebih efektif karena model hanya menangani input yang mereka kuasai.

Beberapa contoh versi fine-tuned dari Mistral termasuk [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), yang berfokus pada domain medis, dan [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), yang melakukan perhitungan matematika.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) adalah LLM yang dibuat oleh Technology Innovation Institute (**TII**). Falcon-40B dilatih dengan 40 miliar parameter yang telah terbukti memberikan kinerja lebih baik daripada GPT-3 dengan anggaran komputasi yang lebih rendah. Hal ini disebabkan oleh penggunaan algoritma FlashAttention dan multiquery attention yang memungkinkan pengurangan kebutuhan memori saat waktu inferensi. Dengan waktu inferensi yang lebih rendah, Falcon-40B cocok untuk aplikasi chat.

Beberapa contoh versi fine-tuned dari Falcon adalah [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), asisten yang dibangun di atas model open, dan [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), yang memberikan kinerja lebih tinggi daripada model dasar.

## Cara Memilih

Tidak ada jawaban tunggal untuk memilih model open. Tempat yang baik untuk memulai adalah dengan menggunakan fitur filter berdasarkan tugas di Azure AI Studio. Ini akan membantu Anda memahami jenis tugas yang telah dilatih oleh model. Hugging Face juga memiliki LLM Leaderboard yang menunjukkan model dengan kinerja terbaik berdasarkan metrik tertentu.

Saat ingin membandingkan LLM di berbagai jenis, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) adalah sumber daya yang bagus lainnya:

![Kualitas Model](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.id.png)  
Sumber: Artificial Analysis

Jika bekerja pada kasus penggunaan tertentu, mencari versi fine-tuned yang berfokus pada area yang sama bisa efektif. Bereksperimen dengan beberapa model open untuk melihat bagaimana mereka bekerja sesuai dengan ekspektasi Anda dan pengguna Anda adalah praktik yang baik.

## Langkah Selanjutnya

Bagian terbaik dari model open adalah Anda dapat mulai bekerja dengan mereka dengan cukup cepat. Lihat [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), yang memiliki koleksi Hugging Face khusus dengan model-model yang kita bahas di sini.

## Pembelajaran Tidak Berhenti di Sini, Lanjutkan Perjalanan Anda

Setelah menyelesaikan pelajaran ini, lihat [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan Anda tentang Generative AI!

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.