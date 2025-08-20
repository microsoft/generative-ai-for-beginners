<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:33:52+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "id"
}
-->
# Siapkan Lingkungan Pengembangan Anda

Kami menyiapkan repositori dan kursus ini dengan [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) yang memiliki runtime Universal yang dapat mendukung pengembangan Python3, .NET, Node.js, dan Java. Konfigurasi terkait didefinisikan dalam file `devcontainer.json` yang terletak di folder `.devcontainer/` di root repositori ini.

Untuk mengaktifkan dev container, jalankan di [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (untuk runtime yang dihosting di cloud) atau di [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (untuk runtime yang dihosting di perangkat lokal). Baca [dokumentasi ini](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) untuk detail lebih lanjut tentang cara kerja dev container di dalam VS Code.

> [!TIP]  
> Kami menyarankan menggunakan GitHub Codespaces untuk memulai dengan cepat dan usaha minimal. Ini menyediakan [kuota penggunaan gratis](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) yang cukup besar untuk akun pribadi. Atur [timeout](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) untuk menghentikan atau menghapus codespaces yang tidak aktif agar kuota Anda dapat digunakan secara maksimal.

## 1. Menjalankan Tugas

Setiap pelajaran akan memiliki tugas _opsional_ yang mungkin disediakan dalam satu atau lebih bahasa pemrograman termasuk: Python, .NET/C#, Java, dan JavaScript/TypeScript. Bagian ini memberikan panduan umum terkait menjalankan tugas-tugas tersebut.

### 1.1 Tugas Python

Tugas Python disediakan baik sebagai aplikasi (`.py` files) atau notebook Jupyter (`.ipynb` files).  
- Untuk menjalankan notebook, buka di Visual Studio Code lalu klik _Select Kernel_ (di kanan atas) dan pilih opsi Python 3 default yang muncul. Sekarang Anda bisa klik _Run All_ untuk menjalankan seluruh notebook.  
- Untuk menjalankan aplikasi Python dari command-line, ikuti instruksi spesifik tugas untuk memastikan Anda memilih file yang tepat dan memberikan argumen yang diperlukan.

## 2. Mengonfigurasi Provider

Tugas **mungkin** juga disiapkan untuk bekerja dengan satu atau lebih deployment Large Language Model (LLM) melalui penyedia layanan yang didukung seperti OpenAI, Azure, atau Hugging Face. Mereka menyediakan _hosted endpoint_ (API) yang dapat kita akses secara programatik dengan kredensial yang tepat (API key atau token). Dalam kursus ini, kami membahas provider berikut:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) dengan berbagai model termasuk seri inti GPT.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) untuk model OpenAI dengan fokus kesiapan enterprise  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) untuk model open-source dan server inferensi

**Anda perlu menggunakan akun Anda sendiri untuk latihan ini**. Tugas bersifat opsional sehingga Anda bisa memilih untuk mengonfigurasi satu, semua, atau tidak sama sekali provider berdasarkan minat Anda. Berikut beberapa panduan pendaftaran:

| Pendaftaran | Biaya | API Key | Playground | Komentar |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Harga](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Berbasis Proyek](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Banyak Model Tersedia |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Harga](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Harus Mendaftar Terlebih Dahulu](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Harga](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat memiliki model terbatas](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Ikuti petunjuk di bawah untuk _mengonfigurasi_ repositori ini agar dapat digunakan dengan berbagai provider. Tugas yang memerlukan provider tertentu akan memiliki salah satu tag ini di nama file mereka:  
 - `aoai` - memerlukan endpoint dan key Azure OpenAI  
 - `oai` - memerlukan endpoint dan key OpenAI  
 - `hf` - memerlukan token Hugging Face

Anda bisa mengonfigurasi satu, tidak sama sekali, atau semua provider. Tugas terkait akan error jika kredensial tidak ditemukan.

###  2.1. Buat file `.env`

Kami mengasumsikan Anda sudah membaca panduan di atas, mendaftar ke provider terkait, dan mendapatkan kredensial autentikasi yang diperlukan (API_KEY atau token). Untuk Azure OpenAI, kami juga mengasumsikan Anda memiliki deployment Azure OpenAI Service (endpoint) yang valid dengan setidaknya satu model GPT yang dideploy untuk chat completion.

Langkah berikutnya adalah mengonfigurasi **variabel lingkungan lokal** Anda sebagai berikut:

1. Cari file `.env.copy` di folder root yang isinya kira-kira seperti ini:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Salin file tersebut menjadi `.env` menggunakan perintah di bawah ini. File ini _gitignore-d_, sehingga rahasia Anda tetap aman.

   ```bash
   cp .env.copy .env
   ```

3. Isi nilai-nilai tersebut (ganti placeholder di sebelah kanan `=`) seperti yang dijelaskan di bagian berikutnya.

3. (Opsional) Jika Anda menggunakan GitHub Codespaces, Anda bisa menyimpan variabel lingkungan sebagai _Codespaces secrets_ yang terkait dengan repositori ini. Dalam kasus ini, Anda tidak perlu membuat file .env lokal. **Namun, opsi ini hanya berlaku jika Anda menggunakan GitHub Codespaces.** Anda tetap harus membuat file .env jika menggunakan Docker Desktop.

### 2.2. Isi file `.env`

Mari kita lihat sekilas nama variabel untuk memahami apa yang mereka wakili:

| Variabel  | Deskripsi  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ini adalah token akses pengguna yang Anda buat di profil Anda |
| OPENAI_API_KEY | Ini adalah kunci otorisasi untuk menggunakan layanan non-Azure OpenAI |
| AZURE_OPENAI_API_KEY | Ini adalah kunci otorisasi untuk menggunakan layanan Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | Ini adalah endpoint yang dideploy untuk resource Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Ini adalah endpoint deployment model _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ini adalah endpoint deployment model _text embeddings_ |
| | |

Catatan: Dua variabel Azure OpenAI terakhir mencerminkan model default untuk chat completion (text generation) dan pencarian vektor (embeddings) secara berurutan. Instruksi pengaturannya akan dijelaskan di tugas terkait.

### 2.3 Konfigurasi Azure: Dari Portal

Nilai endpoint dan key Azure OpenAI dapat ditemukan di [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), jadi mari mulai dari sana.

1. Buka [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
2. Klik opsi **Keys and Endpoint** di sidebar (menu kiri).  
3. Klik **Show Keys** - Anda akan melihat: KEY 1, KEY 2, dan Endpoint.  
4. Gunakan nilai KEY 1 untuk AZURE_OPENAI_API_KEY  
5. Gunakan nilai Endpoint untuk AZURE_OPENAI_ENDPOINT

Selanjutnya, kita perlu mendapatkan endpoint untuk model spesifik yang sudah dideploy.

1. Klik opsi **Model deployments** di sidebar (menu kiri) untuk resource Azure OpenAI.  
2. Di halaman tujuan, klik **Manage Deployments**

Ini akan membawa Anda ke situs Azure OpenAI Studio, di mana kita akan menemukan nilai lain seperti yang dijelaskan berikut ini.

### 2.4 Konfigurasi Azure: Dari Studio

1. Akses [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **dari resource Anda** seperti yang dijelaskan di atas.  
2. Klik tab **Deployments** (sidebar kiri) untuk melihat model yang sudah dideploy.  
3. Jika model yang Anda inginkan belum dideploy, gunakan **Create new deployment** untuk mendeploy-nya.  
4. Anda akan membutuhkan model _text-generation_ - kami rekomendasikan: **gpt-35-turbo**  
5. Anda juga akan membutuhkan model _text-embedding_ - kami rekomendasikan **text-embedding-ada-002**

Sekarang perbarui variabel lingkungan untuk mencerminkan _Deployment name_ yang digunakan. Biasanya ini sama dengan nama model kecuali Anda mengubahnya secara eksplisit. Contohnya, Anda mungkin memiliki:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Jangan lupa simpan file .env setelah selesai**. Anda sekarang bisa keluar dari file dan kembali ke instruksi menjalankan notebook.

### 2.5 Konfigurasi OpenAI: Dari Profil

Kunci API OpenAI Anda dapat ditemukan di [akun OpenAI Anda](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jika belum punya, Anda bisa mendaftar dan membuat API key. Setelah mendapatkan kunci tersebut, gunakan untuk mengisi variabel `OPENAI_API_KEY` di file `.env`.

### 2.6 Konfigurasi Hugging Face: Dari Profil

Token Hugging Face Anda dapat ditemukan di profil Anda di bagian [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Jangan bagikan atau publikasikan token ini secara umum. Sebaiknya buat token baru khusus untuk penggunaan proyek ini dan salin ke file `.env` di variabel `HUGGING_FACE_API_KEY`. _Catatan:_ Secara teknis ini bukan API key, tapi digunakan untuk autentikasi sehingga kami menggunakan nama ini agar konsisten.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.