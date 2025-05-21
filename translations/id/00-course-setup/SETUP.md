<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:54:35+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "id"
}
-->
# Siapkan Lingkungan Pengembangan Anda

Kami menyiapkan repositori dan kursus ini dengan [kontainer pengembangan](https://containers.dev?WT.mc_id=academic-105485-koreyst) yang memiliki runtime Universal yang dapat mendukung pengembangan Python3, .NET, Node.js, dan Java. Konfigurasi terkait didefinisikan dalam file `devcontainer.json` yang terletak di folder `.devcontainer/` di root repositori ini.

Untuk mengaktifkan kontainer pengembangan, luncurkan di [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (untuk runtime yang dihosting di cloud) atau di [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (untuk runtime yang dihosting perangkat lokal). Baca [dokumentasi ini](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) untuk lebih detail tentang cara kerja kontainer pengembangan di VS Code.

> [!TIP]  
> Kami merekomendasikan menggunakan GitHub Codespaces untuk memulai dengan cepat dan usaha minimal. Ini menyediakan [kuota penggunaan gratis](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) yang cukup besar untuk akun pribadi. Konfigurasi [timeout](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) untuk menghentikan atau menghapus codespaces yang tidak aktif agar memaksimalkan penggunaan kuota Anda.

## 1. Menjalankan Tugas

Setiap pelajaran akan memiliki tugas _opsional_ yang mungkin disediakan dalam satu atau lebih bahasa pemrograman termasuk: Python, .NET/C#, Java, dan JavaScript/TypeScript. Bagian ini memberikan panduan umum terkait menjalankan tugas tersebut.

### 1.1 Tugas Python

Tugas Python disediakan baik sebagai aplikasi (file `.py`) atau notebook Jupyter (file `.ipynb`).
- Untuk menjalankan notebook, buka di Visual Studio Code lalu klik _Select Kernel_ (di kanan atas) dan pilih opsi Python 3 default yang ditampilkan. Anda sekarang dapat _Run All_ untuk menjalankan notebook.
- Untuk menjalankan aplikasi Python dari command-line, ikuti instruksi spesifik tugas untuk memastikan Anda memilih file yang tepat dan memberikan argumen yang diperlukan.

## 2. Mengkonfigurasi Penyedia

Tugas **mungkin** juga disiapkan untuk bekerja dengan satu atau lebih penyebaran Model Bahasa Besar (LLM) melalui penyedia layanan yang didukung seperti OpenAI, Azure, atau Hugging Face. Ini menyediakan _endpoint yang dihosting_ (API) yang dapat kita akses secara programatis dengan kredensial yang tepat (kunci API atau token). Dalam kursus ini, kami membahas penyedia ini:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) dengan berbagai model termasuk seri inti GPT.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) untuk model OpenAI dengan fokus pada kesiapan perusahaan.
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) untuk model open-source dan server inferensi.

**Anda perlu menggunakan akun Anda sendiri untuk latihan ini**. Tugas bersifat opsional sehingga Anda dapat memilih untuk menyiapkan satu, semua - atau tidak satupun - dari penyedia berdasarkan minat Anda. Beberapa panduan untuk pendaftaran:

| Pendaftaran | Biaya | Kunci API | Playground | Komentar |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Harga](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Berbasis Proyek](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Tanpa Kode, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Tersedia Banyak Model |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Harga](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Harus Mendaftar Terlebih Dahulu Untuk Akses](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Harga](https://huggingface.co/pricing) | [Token Akses](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat memiliki model terbatas](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Ikuti petunjuk di bawah ini untuk _mengkonfigurasi_ repositori ini agar dapat digunakan dengan penyedia yang berbeda. Tugas yang membutuhkan penyedia spesifik akan berisi salah satu tag ini dalam nama file mereka:
- `aoai` - membutuhkan endpoint Azure OpenAI, kunci
- `oai` - membutuhkan endpoint OpenAI, kunci
- `hf` - membutuhkan token Hugging Face

Anda dapat mengkonfigurasi satu, tidak ada, atau semua penyedia. Tugas terkait akan error jika kredensial hilang.

### 2.1. Buat file `.env`

Kami menganggap Anda telah membaca panduan di atas dan mendaftar dengan penyedia yang relevan, dan mendapatkan kredensial autentikasi yang diperlukan (API_KEY atau token). Dalam kasus Azure OpenAI, kami menganggap Anda juga memiliki penyebaran layanan Azure OpenAI yang valid (endpoint) dengan setidaknya satu model GPT yang diterapkan untuk penyelesaian obrolan.

Langkah berikutnya adalah mengkonfigurasi **variabel lingkungan lokal** Anda sebagai berikut:

1. Cari di folder root untuk file `.env.copy` yang seharusnya memiliki konten seperti ini:

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

2. Salin file tersebut ke `.env` menggunakan perintah di bawah ini. File ini _gitignore-d_, menjaga rahasia tetap aman.

   ```bash
   cp .env.copy .env
   ```

3. Isi nilai (ganti placeholder di sisi kanan `=`) seperti yang dijelaskan di bagian berikutnya.

3. (Opsional) Jika Anda menggunakan GitHub Codespaces, Anda memiliki opsi untuk menyimpan variabel lingkungan sebagai _rahasia Codespaces_ yang terkait dengan repositori ini. Dalam kasus itu, Anda tidak perlu mengatur file .env lokal. **Namun, perhatikan bahwa opsi ini hanya berfungsi jika Anda menggunakan GitHub Codespaces.** Anda tetap perlu mengatur file .env jika Anda menggunakan Docker Desktop.

### 2.2. Isi file `.env`

Mari kita lihat sekilas nama variabel untuk memahami apa yang mereka wakili:

| Variabel | Deskripsi |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ini adalah token akses pengguna yang Anda atur di profil Anda |
| OPENAI_API_KEY | Ini adalah kunci otorisasi untuk menggunakan layanan untuk endpoint OpenAI non-Azure |
| AZURE_OPENAI_API_KEY | Ini adalah kunci otorisasi untuk menggunakan layanan tersebut |
| AZURE_OPENAI_ENDPOINT | Ini adalah endpoint yang diterapkan untuk sumber daya Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Ini adalah endpoint penyebaran model _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ini adalah endpoint penyebaran model _text embeddings_ |
| | |

Catatan: Dua variabel Azure OpenAI terakhir mencerminkan model default untuk penyelesaian obrolan (text generation) dan pencarian vektor (embeddings) masing-masing. Instruksi untuk mengaturnya akan didefinisikan dalam tugas yang relevan.

### 2.3 Konfigurasi Azure: Dari Portal

Nilai endpoint dan kunci Azure OpenAI akan ditemukan di [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) jadi mari kita mulai dari sana.

1. Pergi ke [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik opsi **Keys and Endpoint** di sidebar (menu di kiri).
1. Klik **Show Keys** - Anda harus melihat yang berikut ini: KEY 1, KEY 2, dan Endpoint.
1. Gunakan nilai KEY 1 untuk AZURE_OPENAI_API_KEY
1. Gunakan nilai Endpoint untuk AZURE_OPENAI_ENDPOINT

Selanjutnya, kita membutuhkan endpoint untuk model spesifik yang telah kita terapkan.

1. Klik opsi **Model deployments** di sidebar (menu kiri) untuk sumber daya Azure OpenAI.
1. Di halaman tujuan, klik **Manage Deployments**

Ini akan membawa Anda ke situs web Azure OpenAI Studio, di mana kita akan menemukan nilai lainnya seperti yang dijelaskan di bawah ini.

### 2.4 Konfigurasi Azure: Dari Studio

1. Navigasikan ke [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **dari sumber daya Anda** seperti yang dijelaskan di atas.
1. Klik tab **Deployments** (sidebar, kiri) untuk melihat model yang saat ini diterapkan.
1. Jika model yang Anda inginkan belum diterapkan, gunakan **Create new deployment** untuk menerapkannya.
1. Anda akan membutuhkan model _text-generation_ - kami merekomendasikan: **gpt-35-turbo**
1. Anda akan membutuhkan model _text-embedding_ - kami merekomendasikan **text-embedding-ada-002**

Sekarang perbarui variabel lingkungan untuk mencerminkan _Nama Penyebaran_ yang digunakan. Ini biasanya akan sama dengan nama model kecuali Anda mengubahnya secara eksplisit. Jadi, sebagai contoh, Anda mungkin memiliki:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Jangan lupa untuk menyimpan file .env setelah selesai**. Anda sekarang dapat keluar dari file dan kembali ke instruksi untuk menjalankan notebook.

### 2.5 Konfigurasi OpenAI: Dari Profil

Kunci API OpenAI Anda dapat ditemukan di [akun OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) Anda. Jika Anda tidak memilikinya, Anda dapat mendaftar untuk akun dan membuat kunci API. Setelah Anda memiliki kunci, Anda dapat menggunakannya untuk mengisi variabel `OPENAI_API_KEY` dalam file `.env`.

### 2.6 Konfigurasi Hugging Face: Dari Profil

Token Hugging Face Anda dapat ditemukan di profil Anda di bawah [Token Akses](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Jangan posting atau bagikan ini secara publik. Sebaliknya, buat token baru untuk penggunaan proyek ini dan salin itu ke file `.env` di bawah variabel `HUGGING_FACE_API_KEY`. _Catatan:_ Ini secara teknis bukan kunci API tetapi digunakan untuk autentikasi sehingga kami mempertahankan konvensi penamaan tersebut untuk konsistensi.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi penting, disarankan untuk menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.