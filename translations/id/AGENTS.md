# AGENTS.md

## Gambaran Proyek

Repositori ini berisi kurikulum lengkap dengan 21 pelajaran yang mengajarkan dasar-dasar Generative AI dan pengembangan aplikasi. Kursus ini dirancang untuk pemula dan mencakup segala hal mulai dari konsep dasar hingga membangun aplikasi siap produksi.

**Teknologi Utama:**
- Python 3.9+ dengan pustaka: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript dengan Node.js dan pustaka: `openai` (Azure OpenAI melalui endpoint v1 + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API, dan Microsoft Foundry Models (GitHub Models akan dihentikan akhir Juli 2026)
- Jupyter Notebooks untuk pembelajaran interaktif
- Dev Containers untuk lingkungan pengembangan yang konsisten

**Struktur Repositori:**
- 21 direktori pelajaran bernomor (00-21) berisi README, contoh kode, dan tugas
- Berbagai implementasi: contoh Python, TypeScript, dan kadang .NET
- Direktori terjemahan dengan lebih dari 40 versi bahasa
- Konfigurasi terpusat melalui file `.env` (gunakan `.env.copy` sebagai template)

## Perintah Setup

### Setup Repositori Awal

```bash
# Kloning repositori
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Salin template lingkungan
cp .env.copy .env
# Edit .env dengan kunci API dan endpoint Anda
```

### Setup Lingkungan Python

```bash
# Buat lingkungan virtual
python3 -m venv venv

# Aktifkan lingkungan virtual
# Di macOS/Linux:
source venv/bin/activate
# Di Windows:
venv\Scripts\activate

# Pasang ketergantungan
pip install -r requirements.txt
```

### Setup Node.js/TypeScript

```bash
# Pasang dependensi tingkat root (untuk alat dokumentasi)
npm install

# Untuk contoh TypeScript pelajaran individual, buka pelajaran tertentu:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Setup Dev Container (Direkomendasikan)

Repositori ini menyertakan konfigurasi `.devcontainer` untuk GitHub Codespaces atau VS Code Dev Containers:

1. Buka repositori di GitHub Codespaces atau VS Code dengan ekstensi Dev Containers
2. Dev Container secara otomatis akan:
   - Menginstal dependensi Python dari `requirements.txt`
   - Menjalankan skrip post-create (`.devcontainer/post-create.sh`)
   - Menyiapkan kernel Jupyter

## Alur Kerja Pengembangan

### Variabel Lingkungan

Semua pelajaran yang membutuhkan akses API menggunakan variabel lingkungan yang didefinisikan dalam `.env`:

- `OPENAI_API_KEY` - Untuk OpenAI API
- `AZURE_OPENAI_API_KEY` - Untuk Azure OpenAI di Microsoft Foundry (Azure OpenAI Service kini bagian dari Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL endpoint Azure OpenAI (endpoint resource Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Nama deployment model chat completion
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nama deployment model embeddings
- `AZURE_OPENAI_API_VERSION` - Versi API (default: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Untuk model Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Endpoint Microsoft Foundry Models (katalog model multi-provider)
- `AZURE_INFERENCE_CREDENTIAL` - API key Microsoft Foundry Models (menggantikan `GITHUB_TOKEN` yang akan dihentikan)

### Menjalankan Contoh Python

```bash
# Navigasi ke direktori pelajaran
cd 06-text-generation-apps/python

# Jalankan skrip Python
python aoai-app.py
```

### Menjalankan Contoh TypeScript

```bash
# Arahkan ke direktori aplikasi TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Bangun kode TypeScript
npm run build

# Jalankan aplikasi
npm start
```

### Menjalankan Jupyter Notebooks

```bash
# Mulai Jupyter di root repositori
jupyter notebook

# Atau gunakan VS Code dengan ekstensi Jupyter
```

### Bekerja dengan Jenis Pelajaran Berbeda

- **Pelajaran "Learn"**: Fokus pada dokumentasi README.md dan konsep
- **Pelajaran "Build"**: Termasuk contoh kode yang dapat dijalankan dalam Python dan TypeScript
- Setiap pelajaran memiliki README.md dengan teori, walkthrough kode, dan tautan ke konten video

## Panduan Gaya Kode

### Python

- Gunakan `python-dotenv` untuk pengelolaan variabel lingkungan
- Impor pustaka `openai` untuk interaksi API
- Gunakan `pylint` untuk linting (beberapa contoh menggunakan `# pylint: disable=all` untuk kesederhanaan)
- Ikuti konvensi penamaan PEP 8
- Simpan kredensial API di file `.env`, jangan pernah di dalam kode

### TypeScript

- Gunakan paket `dotenv` untuk variabel lingkungan
- Konfigurasi TypeScript ada di `tsconfig.json` untuk setiap aplikasi
- Gunakan paket `openai` untuk Azure OpenAI (arahkan klien ke endpoint `/openai/v1/` dan panggil `client.responses.create`); gunakan `@azure-rest/ai-inference` untuk Microsoft Foundry Models
- Gunakan `nodemon` untuk pengembangan dengan auto-reload
- Bangun sebelum menjalankan: `npm run build` lalu `npm start`

### Konvensi Umum

- Buat contoh kode sederhana dan edukatif
- Sertakan komentar yang menjelaskan konsep utama
- Kode setiap pelajaran harus mandiri dan dapat dijalankan
- Gunakan penamaan konsisten: prefix `aoai-` untuk Azure OpenAI, `oai-` untuk OpenAI API, `githubmodels-` untuk Microsoft Foundry Models (prefix lama dari era GitHub Models dipertahankan)

## Panduan Dokumentasi

### Gaya Markdown

- Semua URL harus dibungkus dalam format `[text](../../url)` tanpa spasi tambahan
- Tautan relatif harus diawali dengan `./` atau `../`
- Semua tautan ke domain Microsoft harus mencantumkan ID pelacakan: `?WT.mc_id=academic-105485-koreyst`
- Tidak menggunakan lokal spesifik negara dalam URL (hindari `/en-us/`)
- Gambar disimpan di folder `./images` dengan nama deskriptif
- Gunakan karakter bahasa Inggris, angka, dan tanda hubung pada nama file

### Dukungan Terjemahan

- Repositori mendukung lebih dari 40 bahasa melalui GitHub Actions otomatis
- Terjemahan disimpan di direktori `translations/`
- Jangan kirim terjemahan parsial
- Terjemahan mesin tidak diterima
- Gambar terjemahan disimpan di direktori `translated_images/`

## Pengujian dan Validasi

### Pemeriksaan Pra Pengiriman

Repositori ini menggunakan GitHub Actions untuk validasi. Sebelum mengirim PR:

1. **Periksa Tautan Markdown**:
   ```bash
   # Alur kerja validate-markdown.yml memeriksa:
   # - Jalur relatif yang rusak
   # - ID pelacakan yang hilang pada jalur
   # - ID pelacakan yang hilang pada URL
   # - URL dengan lokal negara
   # - URL eksternal yang rusak
   ```

2. **Pengujian Manual**:
   - Uji contoh Python: Aktifkan venv dan jalankan skrip
   - Uji contoh TypeScript: `npm install`, `npm run build`, `npm start`
   - Verifikasi variabel lingkungan dikonfigurasi dengan benar
   - Pastikan API key berfungsi dengan contoh kode

3. **Contoh Kode**:
   - Pastikan semua kode berjalan tanpa error
   - Uji dengan Azure OpenAI dan OpenAI API jika berlaku
   - Verifikasi contoh bekerja dengan Microsoft Foundry Models jika didukung

### Tidak Ada Pengujian Otomatis

Ini adalah repositori edukasi fokus pada tutorial dan contoh. Tidak ada unit test atau integration test untuk dijalankan. Validasi utama:
- Pengujian manual contoh kode
- GitHub Actions untuk validasi Markdown
- Tinjauan komunitas terhadap konten edukasi

## Panduan Pull Request

### Sebelum Mengirim

1. Uji perubahan kode baik di Python maupun TypeScript jika berlaku
2. Jalankan validasi Markdown (langsung dipicu saat PR)
3. Pastikan ID pelacakan ada pada semua URL Microsoft
4. Periksa tautan relatif valid
5. Verifikasi referensi gambar sudah benar

### Format Judul PR

- Gunakan judul deskriptif: `[Lesson 06] Memperbaiki kesalahan contoh Python` atau `Memperbarui README untuk pelajaran 08`
- Cantumkan nomor issue jika ada: `Fixes #123`

### Deskripsi PR

- Jelaskan apa yang diubah dan alasannya
- Tautkan ke isu terkait
- Untuk perubahan kode, sebutkan contoh yang diuji
- Untuk PR terjemahan, sertakan semua file untuk terjemahan lengkap

### Persyaratan Kontribusi

- Tandatangani Microsoft CLA (otomatis saat PR pertama)
- Fork repositori ke akun Anda sebelum mengubah
- Satu PR per perubahan logis (jangan gabungkan perbaikan tidak terkait)
- Usahakan PR fokus dan kecil sebisa mungkin

## Alur Kerja Umum

### Menambah Contoh Kode Baru

1. Arahkan ke direktori pelajaran yang sesuai
2. Buat contoh di subdirektori `python/` atau `typescript/`
3. Ikuti konvensi penamaan: `{provider}-{nama-contoh}.{py|ts|js}`
4. Uji dengan kredensial API yang sebenarnya
5. Dokumentasikan variabel lingkungan baru di README pelajaran

### Memperbarui Dokumentasi

1. Edit README.md di direktori pelajaran
2. Ikuti pedoman Markdown (ID pelacakan, tautan relatif)
3. Pembaruan terjemahan ditangani oleh GitHub Actions (jangan edit manual)
4. Uji semua tautan valid

### Bekerja dengan Dev Containers

1. Repositori menyertakan `.devcontainer/devcontainer.json`
2. Skrip post-create otomatis menginstal dependensi Python
3. Ekstensi Python dan Jupyter sudah dikonfigurasi sebelumnya
4. Lingkungan berbasis `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Penyebaran dan Publikasi

Ini adalah repositori pembelajaran - tidak ada proses penyebaran. Kurikulum diakses melalui:

1. **Repositori GitHub**: Akses langsung ke kode dan dokumentasi
2. **GitHub Codespaces**: Lingkungan pengembangan instan dengan setup pra-konfigurasi
3. **Microsoft Learn**: Konten bisa disindikasi ke platform pembelajaran resmi
4. **docsify**: Situs dokumentasi dibangun dari Markdown (lihat `docsifytopdf.js` dan `package.json`)

### Membangun Situs Dokumentasi

```bash
# Hasilkan PDF dari dokumentasi (jika diperlukan)
npm run convert
```

## Pemecahan Masalah

### Masalah Umum

**Kesalahan Impor Python**:
- Pastikan lingkungan virtual diaktifkan
- Jalankan `pip install -r requirements.txt`
- Periksa versi Python minimal 3.9+

**Kesalahan Build TypeScript**:
- Jalankan `npm install` dalam direktori aplikasi spesifik
- Periksa kompatibilitas versi Node.js
- Hapus `node_modules` dan instal ulang jika perlu

**Kesalahan Otentikasi API**:
- Pastikan file `.env` ada dan berisi nilai yang benar
- Periksa API key valid dan belum kedaluwarsa
- Pastikan URL endpoint tepat sesuai wilayah Anda

**Variabel Lingkungan Hilang**:
- Salin `.env.copy` ke `.env`
- Isi semua nilai yang diperlukan untuk pelajaran yang sedang dikerjakan
- Restart aplikasi setelah memperbarui `.env`

## Sumber Daya Tambahan

- [Panduan Setup Kursus](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Panduan Kontribusi](./CONTRIBUTING.md)
- [Kode Etik](./CODE_OF_CONDUCT.md)
- [Kebijakan Keamanan](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Koleksi Contoh Kode Advanced](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Catatan Khusus Proyek

- Ini adalah **repositori edukasi** yang fokus pada pembelajaran, bukan kode produksi
- Contoh sengaja sederhana dan fokus pada pengajaran konsep
- Kualitas kode diseimbangkan dengan kejelasan edukasi
- Setiap pelajaran mandiri dan bisa diselesaikan secara independen
- Repositori mendukung beberapa penyedia API: Azure OpenAI, OpenAI, Microsoft Foundry Models, dan penyedia offline seperti Foundry Local dan Ollama
- Konten bersifat multibahasa dengan alur kerja terjemahan otomatis
- Komunitas aktif di Discord untuk tanya jawab dan dukungan

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->