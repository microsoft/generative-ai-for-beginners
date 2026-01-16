<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85b754d4dc980f270f264d17116d9a5f",
  "translation_date": "2025-12-19T16:08:11+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "id"
}
-->
[![Open Source Models](../../../translated_images/id/16-lesson-banner.6b56555e8404fda1.png)](https://youtu.be/CuICgfuHFSg?si=x8SpFRUsIxM9dohN)

## Pendahuluan

Dunia LLM sumber terbuka sangat menarik dan terus berkembang. Pelajaran ini bertujuan untuk memberikan pandangan mendalam tentang model sumber terbuka. Jika Anda mencari informasi tentang bagaimana model proprietary dibandingkan dengan model sumber terbuka, kunjungi pelajaran ["Menjelajahi dan Membandingkan Berbagai LLM" (Exploring and Comparing Different LLMs)](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Pelajaran ini juga akan membahas topik fine-tuning, tetapi penjelasan yang lebih rinci dapat ditemukan di pelajaran ["Fine-Tuning LLMs"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Tujuan Pembelajaran

- Memahami Model sumber terbuka
- Memahami manfaat bekerja dengan Model sumber terbuka
- Menjelajahi model terbuka yang tersedia di Hugging Face dan Azure AI Studio

## Apa itu Model Sumber Terbuka?

Perangkat lunak sumber terbuka telah memainkan peran penting dalam pertumbuhan teknologi di berbagai bidang. Open Source Initiative (OSI) telah mendefinisikan [10 kriteria untuk perangkat lunak](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) agar diklasifikasikan sebagai sumber terbuka. Kode sumber harus dibagikan secara terbuka di bawah lisensi yang disetujui oleh OSI.

Meskipun pengembangan LLM memiliki elemen yang mirip dengan pengembangan perangkat lunak, prosesnya tidak persis sama. Hal ini menimbulkan banyak diskusi di komunitas tentang definisi sumber terbuka dalam konteks LLM. Agar sebuah model sesuai dengan definisi tradisional sumber terbuka, informasi berikut harus tersedia untuk umum:

- Dataset yang digunakan untuk melatih model.
- Bobot model lengkap sebagai bagian dari pelatihan.
- Kode evaluasi.
- Kode fine-tuning.
- Bobot model lengkap dan metrik pelatihan.

Saat ini hanya ada beberapa model yang memenuhi kriteria ini. [Model OLMo yang dibuat oleh Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) adalah salah satu yang masuk kategori ini.

Untuk pelajaran ini, kami akan menyebut model-model tersebut sebagai "model terbuka" karena mungkin tidak memenuhi kriteria di atas pada saat penulisan.

## Manfaat Model Terbuka

**Sangat Dapat Disesuaikan** - Karena model terbuka dirilis dengan informasi pelatihan yang rinci, peneliti dan pengembang dapat memodifikasi bagian dalam model. Ini memungkinkan pembuatan model yang sangat khusus yang di-fine-tune untuk tugas atau bidang studi tertentu. Beberapa contohnya adalah pembuatan kode, operasi matematika, dan biologi.

**Biaya** - Biaya per token untuk menggunakan dan menerapkan model ini lebih rendah dibandingkan model proprietary. Saat membangun aplikasi Generative AI, penting untuk mempertimbangkan kinerja versus harga saat bekerja dengan model ini pada kasus penggunaan Anda.

![Model Cost](../../../translated_images/id/model-price.3f5a3e4d32ae00b4.png)
Sumber: Artificial Analysis

**Fleksibilitas** - Bekerja dengan model terbuka memungkinkan Anda fleksibel dalam menggunakan model yang berbeda atau menggabungkannya. Contohnya adalah [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) di mana pengguna dapat memilih model yang digunakan langsung di antarmuka pengguna:

![Choose Model](../../../translated_images/id/choose-model.f095d15bbac92214.png)

## Menjelajahi Berbagai Model Terbuka

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), yang dikembangkan oleh Meta, adalah model terbuka yang dioptimalkan untuk aplikasi berbasis chat. Ini karena metode fine-tuning-nya, yang mencakup sejumlah besar dialog dan umpan balik manusia. Dengan metode ini, model menghasilkan hasil yang lebih sesuai dengan harapan manusia sehingga memberikan pengalaman pengguna yang lebih baik.

Beberapa contoh versi Llama yang di-fine-tune termasuk [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), yang mengkhususkan diri dalam bahasa Jepang dan [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), yang merupakan versi peningkatan dari model dasar.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) adalah model terbuka dengan fokus kuat pada kinerja tinggi dan efisiensi. Model ini menggunakan pendekatan Mixture-of-Experts yang menggabungkan sekelompok model ahli khusus menjadi satu sistem di mana tergantung pada input, model tertentu dipilih untuk digunakan. Ini membuat komputasi lebih efektif karena model hanya menangani input yang mereka kuasai.

Beberapa contoh versi Mistral yang di-fine-tune termasuk [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), yang fokus pada domain medis dan [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), yang melakukan perhitungan matematika.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) adalah LLM yang dibuat oleh Technology Innovation Institute (**TII**). Falcon-40B dilatih dengan 40 miliar parameter yang telah terbukti berkinerja lebih baik daripada GPT-3 dengan anggaran komputasi yang lebih rendah. Ini karena penggunaan algoritma FlashAttention dan multiquery attention yang memungkinkan pengurangan kebutuhan memori saat inferensi. Dengan waktu inferensi yang lebih singkat ini, Falcon-40B cocok untuk aplikasi chat.

Beberapa contoh versi Falcon yang di-fine-tune adalah [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), asisten yang dibangun di atas model terbuka dan [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), yang memberikan kinerja lebih tinggi daripada model dasar.

## Cara Memilih

Tidak ada jawaban tunggal untuk memilih model terbuka. Tempat yang baik untuk memulai adalah dengan menggunakan fitur filter berdasarkan tugas di Azure AI Studio. Ini akan membantu Anda memahami jenis tugas yang telah dilatih oleh model. Hugging Face juga memelihara LLM Leaderboard yang menunjukkan model dengan kinerja terbaik berdasarkan metrik tertentu.

Saat ingin membandingkan LLM di berbagai tipe, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) adalah sumber daya hebat lainnya:

![Model Quality](../../../translated_images/id/model-quality.aaae1c22e00f7ee1.png)
Sumber: Artificial Analysis

Jika mengerjakan kasus penggunaan spesifik, mencari versi yang di-fine-tune yang fokus pada area yang sama bisa efektif. Mencoba beberapa model terbuka untuk melihat bagaimana kinerjanya sesuai dengan harapan Anda dan pengguna Anda adalah praktik yang baik.

## Langkah Selanjutnya

Bagian terbaik dari model terbuka adalah Anda dapat mulai bekerja dengan mereka dengan cukup cepat. Lihat [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), yang menampilkan koleksi khusus Hugging Face dengan model-model yang kita bahas di sini.

## Pembelajaran tidak berhenti di sini, lanjutkan Perjalanan

Setelah menyelesaikan pelajaran ini, lihat koleksi [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Generative AI Anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->