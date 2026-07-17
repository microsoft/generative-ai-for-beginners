# Memilih & Mengonfigurasi Penyedia LLM 🔑

Tugas **dapat** juga diatur untuk bekerja dengan satu atau lebih penyebaran Large Language Model (LLM) melalui penyedia layanan yang didukung seperti OpenAI, Azure, atau Hugging Face. Penyedia ini menawarkan _endpoint hosting_ (API) yang dapat kita akses secara programatis dengan kredensial yang tepat (kunci API atau token). Dalam kursus ini, kita membahas penyedia berikut:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) dengan beragam model termasuk seri inti GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) untuk model OpenAI dengan fokus kesiapan perusahaan
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) untuk satu endpoint dan kunci API untuk mengakses ratusan model dari OpenAI, Meta, Mistral, Cohere, Microsoft dan lainnya (menggantikan GitHub Models, yang akan pensiun pada akhir Juli 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) untuk model sumber terbuka dan server inferensi
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) atau [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) jika Anda lebih memilih menjalankan model sepenuhnya offline di perangkat Anda sendiri, tanpa perlu langganan cloud

**Anda akan perlu menggunakan akun Anda sendiri untuk latihan ini**. Tugas bersifat opsional jadi Anda bisa memilih untuk mengatur satu, semua - atau tidak sama sekali - penyedia berdasarkan minat Anda. Beberapa panduan pendaftaran:

| Daftar | Biaya | Kunci API | Playground | Komentar |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Harga](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Berbasis proyek](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Tanpa kode, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Tersedia Banyak Model |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Harga](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Permulaan SDK](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Permulaan Studio](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Harus Mendaftar Terlebih Dahulu untuk Akses](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Harga](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Halaman Ringkasan Proyek](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Tersedia tier gratis; satu endpoint + kunci untuk banyak penyedia model |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Harga](https://huggingface.co/pricing) | [Token Akses](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat memiliki model terbatas](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Gratis (berjalan di perangkat Anda) | Tidak diperlukan | [CLI/SDK Lokal](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Endpoint kompatibel OpenAI, sepenuhnya offline |
| | | | | |

Ikuti petunjuk di bawah untuk _mengonfigurasi_ repositori ini untuk digunakan dengan penyedia yang berbeda. Tugas yang memerlukan penyedia tertentu akan memiliki salah satu tag ini di nama file mereka:

- `aoai` - memerlukan endpoint Azure OpenAI, kunci
- `oai` - memerlukan endpoint OpenAI, kunci
- `hf` - memerlukan token Hugging Face
- `githubmodels` - memerlukan endpoint Microsoft Foundry Models, kunci (GitHub Models akan pensiun pada akhir Juli 2026)

Anda bisa mengonfigurasi satu, tidak sama sekali, atau semua penyedia. Tugas terkait akan gagal jika kredensial hilang.

## Membuat file `.env`

Kami mengasumsikan bahwa Anda sudah membaca panduan di atas dan mendaftar dengan penyedia terkait, serta mendapatkan kredensial autentikasi yang diperlukan (API_KEY atau token). Dalam kasus Azure OpenAI, kami mengasumsikan Anda juga memiliki penyebaran layanan Azure OpenAI (endpoint) yang valid dengan setidaknya satu model GPT yang dideploy untuk penyelesaian obrolan.

Langkah selanjutnya adalah mengonfigurasi **variabel lingkungan lokal Anda** sebagai berikut:

1. Cari di folder akar untuk file `.env.copy` yang seharusnya memiliki isi seperti ini:

   ```bash
   # Penyedia OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI di Microsoft Foundry
   ## (Layanan Azure OpenAI sekarang menjadi bagian dari Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Default sudah diatur! (versi API GA stabil saat ini)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Model Microsoft Foundry (katalog model multi-penyedia, menggantikan Model GitHub, yang akan dihentikan akhir Juli 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Salin file tersebut ke `.env` menggunakan perintah berikut. File ini _gitignore-d_, menjaga rahasia tetap aman.

   ```bash
   cp .env.copy .env
   ```

3. Isi nilai-nilainya (ganti placeholder di sisi kanan `=`) seperti yang dijelaskan di bagian berikut.

4. (Opsional) Jika Anda menggunakan GitHub Codespaces, Anda dapat menyimpan variabel lingkungan sebagai _Codespaces secrets_ yang terkait dengan repositori ini. Dalam hal ini, Anda tidak perlu mengatur file .env lokal. **Namun, perhatikan bahwa opsi ini hanya berfungsi jika Anda menggunakan GitHub Codespaces.** Anda tetap perlu mengatur file .env jika menggunakan Docker Desktop.

## Mengisi file `.env`

Mari kita lihat singkat nama variabel untuk memahami apa yang mereka wakili:

| Variabel  | Deskripsi  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ini adalah token akses pengguna yang Anda atur di profil Anda |
| OPENAI_API_KEY | Ini adalah kunci otorisasi untuk menggunakan layanan pada endpoint non-Azure OpenAI |
| AZURE_OPENAI_API_KEY | Ini adalah kunci otorisasi untuk layanan tersebut |
| AZURE_OPENAI_ENDPOINT | Ini adalah endpoint yang disebarkan untuk sumber daya Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Ini adalah endpoint penyebaran model _generasi teks_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ini adalah endpoint penyebaran model _embedding teks_ |
| AZURE_INFERENCE_ENDPOINT | Ini adalah endpoint untuk proyek Microsoft Foundry Anda, digunakan untuk Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Ini adalah kunci API untuk proyek Microsoft Foundry Anda |
| | |

Catatan: Dua variabel Azure OpenAI terakhir mencerminkan model default untuk penyelesaian obrolan (generasi teks) dan pencarian vektor (embedding) secara berurutan. Petunjuk untuk mengaturnya akan didefinisikan di tugas terkait.

## Mengonfigurasi Azure OpenAI: Dari Portal

> **Catatan:** Layanan Azure OpenAI sekarang merupakan bagian dari [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Sumber daya dan penyebaran masih muncul di Portal Azure, tetapi pengelolaan model sehari-hari (penyebaran, playground, pemantauan) sekarang dilakukan di portal Foundry bukan lagi di "Azure OpenAI Studio" yang berdiri sendiri.

Nilai endpoint dan kunci Azure OpenAI dapat ditemukan di [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) jadi mari mulai di sana.

1. Buka [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik opsi **Keys and Endpoint** di bilah sisi (menu kiri).
1. Klik **Show Keys** - Anda akan melihat: KEY 1, KEY 2 dan Endpoint.
1. Gunakan nilai KEY 1 untuk AZURE_OPENAI_API_KEY
1. Gunakan nilai Endpoint untuk AZURE_OPENAI_ENDPOINT

Selanjutnya, kita butuh endpoint untuk model tertentu yang telah kita deploy.

1. Klik opsi **Model deployments** di bilah sisi (menu kiri) untuk sumber daya Azure OpenAI.
1. Di halaman tujuan, klik **Go to Microsoft Foundry portal** (atau **Manage Deployments**, tergantung tipe sumber daya Anda)

Ini akan membawa Anda ke portal Microsoft Foundry, di mana kita akan menemukan nilai lain seperti yang dijelaskan di bawah.

## Mengonfigurasi Azure OpenAI: Dari portal Microsoft Foundry

1. Navigasikan ke [portal Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **dari sumber daya Anda** seperti dijelaskan di atas.
1. Klik tab **Deployments** (bilah sisi, kiri) untuk melihat model yang sedang dideploy.
1. Jika model yang diinginkan belum dideploy, gunakan **Deploy model** untuk mendeploy dari [katalog model](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Anda memerlukan model _text-generation_ - kami rekomendasikan: **gpt-5-mini**
1. Anda memerlukan model _text-embedding_ - kami rekomendasikan **text-embedding-3-small**

Sekarang perbarui variabel lingkungan agar mencerminkan _Deployment name_ yang digunakan. Ini biasanya sama dengan nama model kecuali Anda mengubahnya secara eksplisit. Jadi, sebagai contoh, Anda mungkin memiliki:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Jangan lupa simpan file .env setelah selesai**. Anda sekarang bisa keluar dari file dan kembali ke instruksi menjalankan notebook.

## Mengonfigurasi OpenAI: Dari Profil

Kunci API OpenAI Anda dapat ditemukan di [akun OpenAI Anda](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jika belum punya, Anda bisa mendaftar dan membuat kunci API. Setelah memiliki kunci, gunakan untuk mengisi variabel `OPENAI_API_KEY` di file `.env`.

## Mengonfigurasi Hugging Face: Dari Profil

Token Hugging Face Anda dapat ditemukan di profil Anda di bawah [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Jangan pernah mengunggah atau membagikannya secara publik. Sebaiknya, buat token baru khusus untuk penggunaan proyek ini dan salin ke file `.env` pada variabel `HUGGING_FACE_API_KEY`. _Catatan:_ Ini teknisnya bukan kunci API, tetapi digunakan untuk autentikasi sehingga kami tetap menggunakan konvensi penamaan tersebut demi konsistensi.

## Mengonfigurasi Microsoft Foundry Models: Dari Portal

> **Catatan:** GitHub Models akan pensiun pada akhir Juli 2026. Microsoft Foundry Models adalah penggantinya langsung, menyediakan katalog model gratis untuk dicoba dan pengalaman SDK Azure AI Inference / OpenAI SDK yang sama.

1. Buka [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) dan buat (atau buka) proyek Foundry.
1. Telusuri [katalog model](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) dan deploy model, misalnya `gpt-5-mini`.
1. Pada halaman **Overview** proyek, salin **endpoint** dan **kunci API**.
1. Gunakan nilai endpoint untuk `AZURE_INFERENCE_ENDPOINT` dan nilai kunci untuk `AZURE_INFERENCE_CREDENTIAL` dalam file `.env` Anda.

## Penyedia Offline / Lokal

Jika Anda tidak ingin menggunakan langganan cloud sama sekali, Anda bisa menjalankan model terbuka yang kompatibel langsung di perangkat Anda:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - runtime Microsoft di perangkat. Otomatis memilih penyedia eksekusi terbaik (NPU, GPU, atau CPU) dan menyediakan endpoint kompatibel OpenAI, sehingga Anda dapat menggunakan ulang sebagian besar kode contoh dalam kursus ini dengan perubahan minimal. Lihat [dokumentasi Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) untuk memulai, atau instal dengan `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - alternatif populer untuk menjalankan model terbuka seperti Llama, Phi, Mistral, dan Gemma secara lokal.


Lihat [Pelajaran 19: Membangun dengan SLM](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) untuk contoh langsung yang menggunakan kedua opsi tersebut.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->