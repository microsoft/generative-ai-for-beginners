# Memilih & Mengonfigurasi Penyedia LLM 🔑

Tugas **dapat** juga diatur untuk bekerja dengan satu atau lebih penyebaran Large Language Model (LLM) melalui penyedia layanan yang didukung seperti OpenAI, Azure, atau Hugging Face. Mereka menyediakan _hosted endpoint_ (API) yang dapat kita akses secara programatis dengan kredensial yang tepat (kunci API atau token). Dalam kursus ini, kami membahas penyedia berikut:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) dengan berbagai model termasuk seri inti GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) untuk model OpenAI dengan fokus kesiapan perusahaan
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) untuk model open-source dan server inferensi

**Anda perlu menggunakan akun Anda sendiri untuk latihan ini**. Tugas bersifat opsional sehingga Anda dapat memilih untuk mengatur satu, semua - atau tidak sama sekali - penyedia berdasarkan minat Anda. Beberapa panduan untuk pendaftaran:

| Pendaftaran | Biaya | Kunci API | Playground | Komentar |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Harga](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Berbasis Proyek](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Tanpa Kode, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Beberapa Model Tersedia |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Harga](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Harus Mendaftar Terlebih Dahulu Untuk Akses](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Harga](https://huggingface.co/pricing) | [Token Akses](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat memiliki model terbatas](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Ikuti petunjuk di bawah untuk _mengonfigurasi_ repositori ini agar dapat digunakan dengan penyedia yang berbeda. Tugas yang memerlukan penyedia tertentu akan berisi salah satu tag ini dalam nama file mereka:

- `aoai` - memerlukan endpoint Azure OpenAI, kunci
- `oai` - memerlukan endpoint OpenAI, kunci
- `hf` - memerlukan token Hugging Face

Anda dapat mengonfigurasi satu, tidak sama sekali, atau semua penyedia. Tugas terkait akan langsung error jika kredensial hilang.

## Buat file `.env`

Kami mengasumsikan Anda sudah membaca panduan di atas dan mendaftar dengan penyedia terkait, serta memperoleh kredensial autentikasi yang diperlukan (API_KEY atau token). Dalam kasus Azure OpenAI, kami juga mengasumsikan Anda memiliki penyebaran layanan Azure OpenAI (endpoint) yang valid dengan setidaknya satu model GPT yang dideploy untuk chat completion.

Langkah berikutnya adalah mengonfigurasi **variabel lingkungan lokal** Anda sebagai berikut:

1. Cari di folder root file `.env.copy` yang seharusnya berisi seperti ini:

   ```bash
   # Penyedia OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default sudah diatur!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Salin file tersebut ke `.env` menggunakan perintah di bawah ini. File ini _gitignore-d_, menjaga rahasia tetap aman.

   ```bash
   cp .env.copy .env
   ```

3. Isi nilai-nilainya (ganti placeholder di sisi kanan `=`) seperti yang dijelaskan di bagian berikutnya.

4. (Opsional) Jika Anda menggunakan GitHub Codespaces, Anda memiliki opsi untuk menyimpan variabel lingkungan sebagai _Codespaces secrets_ yang terkait dengan repositori ini. Dalam hal ini, Anda tidak perlu mengatur file .env lokal. **Namun, perhatikan bahwa opsi ini hanya berfungsi jika Anda menggunakan GitHub Codespaces.** Anda tetap perlu mengatur file .env jika menggunakan Docker Desktop.

## Isi file `.env`

Mari kita lihat sekilas nama variabel untuk memahami apa yang mereka wakili:

| Variabel  | Deskripsi  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ini adalah token akses pengguna yang Anda atur di profil Anda |
| OPENAI_API_KEY | Ini adalah kunci otorisasi untuk menggunakan layanan pada endpoint non-Azure OpenAI |
| AZURE_OPENAI_API_KEY | Ini adalah kunci otorisasi untuk menggunakan layanan tersebut |
| AZURE_OPENAI_ENDPOINT | Ini adalah endpoint yang dideploy untuk sumber daya Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Ini adalah endpoint penyebaran model _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ini adalah endpoint penyebaran model _text embeddings_ |
| | |

Catatan: Dua variabel Azure OpenAI terakhir mencerminkan model default untuk chat completion (text generation) dan pencarian vektor (embeddings) secara berurutan. Instruksi untuk mengaturnya akan didefinisikan dalam tugas terkait.

## Konfigurasi Azure: Dari Portal

Nilai endpoint dan kunci Azure OpenAI dapat ditemukan di [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) jadi mari mulai dari sana.

1. Buka [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik opsi **Keys and Endpoint** di sidebar (menu di kiri).
1. Klik **Show Keys** - Anda akan melihat: KEY 1, KEY 2 dan Endpoint.
1. Gunakan nilai KEY 1 untuk AZURE_OPENAI_API_KEY
1. Gunakan nilai Endpoint untuk AZURE_OPENAI_ENDPOINT

Selanjutnya, kita perlu endpoint untuk model spesifik yang telah kita deploy.

1. Klik opsi **Model deployments** di sidebar (menu kiri) untuk sumber daya Azure OpenAI.
1. Di halaman tujuan, klik **Manage Deployments**

Ini akan membawa Anda ke situs Azure OpenAI Studio, di mana kita akan menemukan nilai lain seperti yang dijelaskan di bawah.

## Konfigurasi Azure: Dari Studio

1. Navigasi ke [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **dari sumber daya Anda** seperti dijelaskan di atas.
1. Klik tab **Deployments** (sidebar, kiri) untuk melihat model yang sedang dideploy.
1. Jika model yang Anda inginkan belum dideploy, gunakan **Create new deployment** untuk mendeploy-nya.
1. Anda akan membutuhkan model _text-generation_ - kami merekomendasikan: **gpt-35-turbo**
1. Anda akan membutuhkan model _text-embedding_ - kami merekomendasikan **text-embedding-ada-002**

Sekarang perbarui variabel lingkungan untuk mencerminkan _Deployment name_ yang digunakan. Ini biasanya sama dengan nama model kecuali Anda mengubahnya secara eksplisit. Jadi, sebagai contoh, Anda mungkin memiliki:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Jangan lupa simpan file .env setelah selesai**. Anda sekarang dapat keluar dari file dan kembali ke instruksi untuk menjalankan notebook.

## Konfigurasi OpenAI: Dari Profil

Kunci API OpenAI Anda dapat ditemukan di [akun OpenAI Anda](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jika Anda belum memilikinya, Anda dapat mendaftar akun dan membuat kunci API. Setelah Anda memiliki kunci tersebut, Anda dapat menggunakannya untuk mengisi variabel `OPENAI_API_KEY` di file `.env`.

## Konfigurasi Hugging Face: Dari Profil

Token Hugging Face Anda dapat ditemukan di profil Anda di bawah [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Jangan posting atau bagikan ini secara publik. Sebagai gantinya, buat token baru untuk penggunaan proyek ini dan salin ke dalam file `.env` di bawah variabel `HUGGING_FACE_API_KEY`. _Catatan:_ Ini secara teknis bukan kunci API tetapi digunakan untuk autentikasi sehingga kami mempertahankan konvensi penamaan ini untuk konsistensi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->