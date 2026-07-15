# Memilih & Mengonfigurasi Penyedia LLM 🔑

Tugas **mungkin** juga dapat diatur untuk bekerja dengan satu atau beberapa penerapan Large Language Model (LLM) melalui penyedia layanan yang didukung seperti OpenAI, Azure, atau Hugging Face. Mereka menyediakan _hosted endpoint_ (API) yang dapat kita akses secara programatik dengan kredensial yang tepat (kunci API atau token). Dalam kursus ini, kami membahas penyedia berikut:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) dengan beragam model termasuk seri GPT inti.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) untuk model OpenAI dengan fokus pada kesiapan perusahaan
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) untuk satu endpoint dan kunci API untuk mengakses ratusan model dari OpenAI, Meta, Mistral, Cohere, Microsoft, dan lain-lain (menggantikan GitHub Models, yang akan dihentikan pada akhir Juli 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) untuk model open-source dan server inferensi
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) atau [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) jika Anda lebih suka menjalankan model sepenuhnya offline di perangkat Anda sendiri, tanpa langganan cloud yang diperlukan

**Anda perlu menggunakan akun Anda sendiri untuk latihan ini**. Tugas bersifat opsional sehingga Anda bisa memilih untuk mengatur satu, semua - atau tidak sama sekali - penyedia sesuai minat Anda. Berikut beberapa panduan pendaftaran:

| Daftar | Biaya | Kunci API | Playground | Komentar |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Harga](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Berbasis Proyek](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Tanpa Kode, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Banyak Model Tersedia |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Harga](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Harus Mendaftar Terlebih Dahulu](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Harga](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Halaman Ringkasan Proyek](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Playground Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Tier gratis tersedia; satu endpoint + kunci untuk banyak penyedia model |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Harga](https://huggingface.co/pricing) | [Token Akses](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat memiliki model terbatas](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Gratis (dijalankan di perangkat Anda) | Tidak diperlukan | [CLI/SDK Lokal](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Endpoint kompatibel OpenAI sepenuhnya offline |
| | | | | |

Ikuti petunjuk di bawah ini untuk _mengonfigurasi_ repositori ini agar dapat digunakan dengan penyedia berbeda. Tugas yang membutuhkan penyedia tertentu akan berisi salah satu tag ini di nama file mereka:

- `aoai` - membutuhkan endpoint Azure OpenAI, kunci
- `oai` - membutuhkan endpoint OpenAI, kunci
- `hf` - membutuhkan token Hugging Face
- `githubmodels` - membutuhkan endpoint Microsoft Foundry Models, kunci (GitHub Models akan dihentikan pada akhir Juli 2026)

Anda dapat mengonfigurasi satu, tidak sama sekali, atau semua penyedia. Tugas terkait hanya akan memberikan error jika kredensial hilang.

## Buat file `.env`

Kami mengasumsikan Anda sudah membaca panduan di atas dan mendaftar dengan penyedia yang relevan, serta mendapatkan kredensial autentikasi yang diperlukan (API_KEY atau token). Dalam kasus Azure OpenAI, kami juga mengasumsikan Anda memiliki penerapan Azure OpenAI Service (endpoint) yang valid dengan setidaknya satu model GPT yang diterapkan untuk chat completion.

Langkah berikutnya adalah mengonfigurasi **variabel lingkungan lokal** Anda sebagai berikut:

1. Cari di folder root file `.env.copy` yang harus berisi seperti ini:

   ```bash
   # Penyedia OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI di Microsoft Foundry
   ## (Layanan Azure OpenAI sekarang bagian dari Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Default sudah diatur! (versi API GA stabil saat ini)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Model Microsoft Foundry (katalog model multi-penyedia, menggantikan Model GitHub, yang akan pensiun akhir Juli 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Salin file tersebut ke `.env` menggunakan perintah di bawah ini. File ini _gitignore-d_, menjaga rahasia tetap aman.

   ```bash
   cp .env.copy .env
   ```

3. Isi nilai-nilainya (ganti placeholder di sebelah kanan tanda `=`) seperti yang dijelaskan di bagian berikut.

4. (Opsional) Jika Anda menggunakan GitHub Codespaces, Anda memiliki opsi menyimpan variabel lingkungan sebagai _Codespaces secrets_ yang terkait dengan repositori ini. Dalam hal ini, Anda tidak perlu mengatur file .env lokal. **Namun, perhatikan bahwa opsi ini hanya berfungsi jika Anda menggunakan GitHub Codespaces.** Anda tetap perlu mengatur file .env jika menggunakan Docker Desktop.

## Isi file `.env`

Mari kita lihat sekilas nama variabel untuk memahami apa yang mereka wakili:

| Variabel  | Deskripsi  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ini adalah token akses pengguna yang Anda atur di profil Anda |
| OPENAI_API_KEY | Ini adalah kunci otorisasi untuk menggunakan layanan selain endpoint Azure OpenAI |
| AZURE_OPENAI_API_KEY | Ini adalah kunci otorisasi untuk menggunakan layanan tersebut |
| AZURE_OPENAI_ENDPOINT | Ini adalah endpoint yang diterapkan untuk sumber daya Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Ini adalah endpoint penerapan model _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ini adalah endpoint penerapan model _text embeddings_ |
| AZURE_INFERENCE_ENDPOINT | Ini adalah endpoint untuk proyek Microsoft Foundry Anda, dipakai untuk Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Ini adalah kunci API untuk proyek Microsoft Foundry Anda |
| | |

Catatan: Dua variabel Azure OpenAI terakhir mencerminkan model default untuk chat completion (text generation) dan pencarian vektor (embeddings) masing-masing. Instruksi untuk mengaturnya akan didefinisikan dalam tugas terkait.

## Konfigurasi Azure OpenAI: Dari Portal

> **Catatan:** Azure OpenAI Service sekarang bagian dari [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Sumber daya dan penerapan masih muncul di Azure Portal, tetapi manajemen model sehari-hari (penerapan, playground, pemantauan) sekarang dilakukan di portal Foundry daripada "Azure OpenAI Studio" lama yang berdiri sendiri.

Nilai endpoint dan kunci Azure OpenAI akan ditemukan di [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) jadi mari mulai dari sana.

1. Buka [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik opsi **Keys and Endpoint** di sidebar (menu sebelah kiri).
1. Klik **Show Keys** - Anda akan melihat: KEY 1, KEY 2 dan Endpoint.
1. Gunakan nilai KEY 1 untuk AZURE_OPENAI_API_KEY
1. Gunakan nilai Endpoint untuk AZURE_OPENAI_ENDPOINT

Selanjutnya, kita butuh endpoint untuk model spesifik yang telah kita terapkan.

1. Klik opsi **Model deployments** di sidebar (menu kiri) untuk sumber daya Azure OpenAI.
1. Di halaman tujuan, klik **Go to Microsoft Foundry portal** (atau **Manage Deployments**, tergantung tipe sumber daya Anda)

Ini akan membawa Anda ke portal Microsoft Foundry, tempat kita akan menemukan nilai lain sebagaimana dijelaskan di bawah.

## Konfigurasi Azure OpenAI: Dari portal Microsoft Foundry

1. Navigasi ke [portal Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **dari sumber daya Anda** seperti dijelaskan di atas.
1. Klik tab **Deployments** (sidebar, kiri) untuk melihat model yang saat ini diterapkan.
1. Jika model yang Anda inginkan belum diterapkan, gunakan **Deploy model** untuk menerapkannya dari [katalog model](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Anda memerlukan model _text-generation_ - kami rekomendasikan: **gpt-4o-mini**
1. Anda memerlukan model _text-embedding_ - kami rekomendasikan **text-embedding-3-small**

Sekarang perbarui variabel lingkungan untuk mencerminkan _Deployment name_ yang digunakan. Ini biasanya sama dengan nama model kecuali Anda mengubahnya secara eksplisit. Jadi, sebagai contoh, Anda mungkin memiliki:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Jangan lupa simpan file .env saat selesai**. Anda sekarang dapat keluar dari file dan kembali ke petunjuk menjalankan notebook.

## Konfigurasi OpenAI: Dari Profil

Kunci API OpenAI Anda dapat ditemukan di [akun OpenAI Anda](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jika belum punya, Anda dapat mendaftar akun dan membuat kunci API. Setelah mendapat kunci, Anda dapat mengisinya ke variabel `OPENAI_API_KEY` di file `.env`.

## Konfigurasi Hugging Face: Dari Profil

Token Hugging Face Anda dapat ditemukan di profil Anda di bawah [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Jangan posting atau bagikan token ini secara publik. Sebagai gantinya, buat token baru untuk penggunaan proyek ini dan salin ke file `.env` di bawah variabel `HUGGING_FACE_API_KEY`. _Catatan:_ Ini sebenarnya bukan kunci API, tapi digunakan untuk autentikasi sehingga kita mempertahankan nama ini agar konsisten.

## Konfigurasi Microsoft Foundry Models: Dari Portal

> **Catatan:** GitHub Models akan dihentikan pada akhir Juli 2026. Microsoft Foundry Models adalah pengganti langsungnya, menawarkan katalog model gratis untuk dicoba dan pengalaman Azure AI Inference SDK / OpenAI SDK yang sama.

1. Pergi ke [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) dan buat (atau buka) proyek Foundry.
1. Jelajahi [katalog model](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) dan terapkan sebuah model, misalnya `gpt-4o-mini`.
1. Pada halaman **Overview** proyek, salin **endpoint** dan **kunci API**.
1. Gunakan nilai endpoint untuk `AZURE_INFERENCE_ENDPOINT` dan nilai kunci untuk `AZURE_INFERENCE_CREDENTIAL` di file `.env` Anda.

## Penyedia Offline / Lokal

Jika Anda tidak ingin menggunakan langganan cloud sama sekali, Anda dapat menjalankan model open compatible langsung di perangkat Anda sendiri:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - runtime on-device Microsoft. Ia secara otomatis memilih penyedia eksekusi terbaik (NPU, GPU, atau CPU) dan menyediakan endpoint kompatibel OpenAI, jadi Anda bisa menggunakan kembali sebagian besar kode contoh dalam kursus ini dengan sedikit perubahan. Lihat [dokumentasi Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) untuk memulai, atau instal dengan `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - alternatif populer untuk menjalankan model open seperti Llama, Phi, Mistral, dan Gemma secara lokal.


Lihat [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) untuk contoh langsung menggunakan kedua opsi tersebut.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->