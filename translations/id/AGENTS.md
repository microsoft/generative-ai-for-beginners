<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:07:15+00:00",
  "source_file": "AGENTS.md",
  "language_code": "id"
}
-->
# AGENTS.md

## Gambaran Proyek

Repositori ini berisi kurikulum 21 pelajaran yang komprehensif untuk mengajarkan dasar-dasar AI Generatif dan pengembangan aplikasi. Kursus ini dirancang untuk pemula dan mencakup segala hal mulai dari konsep dasar hingga membangun aplikasi siap produksi.

**Teknologi Utama:**
- Python 3.9+ dengan pustaka: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript dengan Node.js dan pustaka: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API, dan Model GitHub
- Jupyter Notebooks untuk pembelajaran interaktif
- Dev Containers untuk lingkungan pengembangan yang konsisten

**Struktur Repositori:**
- 21 direktori pelajaran bernomor (00-21) yang berisi README, contoh kode, dan tugas
- Implementasi beragam: Python, TypeScript, dan kadang-kadang contoh .NET
- Direktori terjemahan dengan lebih dari 40 versi bahasa
- Konfigurasi terpusat melalui file `.env` (gunakan `.env.copy` sebagai template)

## Perintah Setup

### Setup Awal Repositori

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Setup Lingkungan Python

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Setup Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Setup Dev Container (Direkomendasikan)

Repositori ini menyertakan konfigurasi `.devcontainer` untuk GitHub Codespaces atau VS Code Dev Containers:

1. Buka repositori di GitHub Codespaces atau VS Code dengan ekstensi Dev Containers
2. Dev Container akan secara otomatis:
   - Menginstal dependensi Python dari `requirements.txt`
   - Menjalankan skrip post-create (`.devcontainer/post-create.sh`)
   - Menyiapkan kernel Jupyter

## Alur Kerja Pengembangan

### Variabel Lingkungan

Semua pelajaran yang membutuhkan akses API menggunakan variabel lingkungan yang didefinisikan dalam `.env`:

- `OPENAI_API_KEY` - Untuk OpenAI API
- `AZURE_OPENAI_API_KEY` - Untuk Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - URL endpoint Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` - Nama deployment model chat completion
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nama deployment model embeddings
- `AZURE_OPENAI_API_VERSION` - Versi API (default: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Untuk model Hugging Face
- `GITHUB_TOKEN` - Untuk Model GitHub

### Menjalankan Contoh Python

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Menjalankan Contoh TypeScript

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Menjalankan Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Bekerja dengan Jenis Pelajaran yang Berbeda

- **Pelajaran "Learn"**: Fokus pada dokumentasi README.md dan konsep
- **Pelajaran "Build"**: Menyertakan contoh kode yang berfungsi dalam Python dan TypeScript
- Setiap pelajaran memiliki README.md dengan teori, penjelasan kode, dan tautan ke konten video

## Panduan Gaya Kode

### Python

- Gunakan `python-dotenv` untuk manajemen variabel lingkungan
- Impor pustaka `openai` untuk interaksi API
- Gunakan `pylint` untuk linting (beberapa contoh menyertakan `# pylint: disable=all` untuk kesederhanaan)
- Ikuti konvensi penamaan PEP 8
- Simpan kredensial API di file `.env`, jangan di dalam kode

### TypeScript

- Gunakan paket `dotenv` untuk variabel lingkungan
- Konfigurasi TypeScript dalam `tsconfig.json` untuk setiap aplikasi
- Gunakan `@azure/openai` atau `@azure-rest/ai-inference` untuk layanan Azure
- Gunakan `nodemon` untuk pengembangan dengan auto-reload
- Bangun sebelum menjalankan: `npm run build` lalu `npm start`

### Konvensi Umum

- Jaga agar contoh kode tetap sederhana dan edukatif
- Sertakan komentar yang menjelaskan konsep utama
- Kode setiap pelajaran harus mandiri dan dapat dijalankan
- Gunakan penamaan yang konsisten: awalan `aoai-` untuk Azure OpenAI, `oai-` untuk OpenAI API, `githubmodels-` untuk Model GitHub

## Panduan Dokumentasi

### Gaya Markdown

- Semua URL harus dibungkus dalam format `[teks](../../url)` tanpa spasi tambahan
- Tautan relatif harus dimulai dengan `./` atau `../`
- Semua tautan ke domain Microsoft harus menyertakan ID pelacakan: `?WT.mc_id=academic-105485-koreyst`
- Hindari lokal spesifik negara dalam URL (hindari `/en-us/`)
- Gambar disimpan di folder `./images` dengan nama deskriptif
- Gunakan karakter Inggris, angka, dan tanda hubung dalam nama file

### Dukungan Terjemahan

- Repositori mendukung lebih dari 40 bahasa melalui GitHub Actions otomatis
- Terjemahan disimpan di direktori `translations/`
- Jangan kirim terjemahan parsial
- Terjemahan mesin tidak diterima
- Gambar terjemahan disimpan di direktori `translated_images/`

## Pengujian dan Validasi

### Pemeriksaan Sebelum Pengiriman

Repositori ini menggunakan GitHub Actions untuk validasi. Sebelum mengirimkan PR:

1. **Periksa Tautan Markdown**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Pengujian Manual**:
   - Uji contoh Python: Aktifkan venv dan jalankan skrip
   - Uji contoh TypeScript: `npm install`, `npm run build`, `npm start`
   - Verifikasi variabel lingkungan dikonfigurasi dengan benar
   - Periksa bahwa kunci API berfungsi dengan contoh kode

3. **Contoh Kode**:
   - Pastikan semua kode berjalan tanpa kesalahan
   - Uji dengan Azure OpenAI dan OpenAI API jika berlaku
   - Verifikasi contoh berfungsi dengan Model GitHub jika didukung

### Tidak Ada Pengujian Otomatis

Ini adalah repositori edukasi yang berfokus pada tutorial dan contoh. Tidak ada pengujian unit atau integrasi yang dijalankan. Validasi terutama:
- Pengujian manual contoh kode
- GitHub Actions untuk validasi Markdown
- Tinjauan komunitas terhadap konten edukasi

## Panduan Pull Request

### Sebelum Mengirimkan

1. Uji perubahan kode dalam Python dan TypeScript jika berlaku
2. Jalankan validasi Markdown (dipicu otomatis pada PR)
3. Pastikan ID pelacakan ada di semua URL Microsoft
4. Periksa bahwa tautan relatif valid
5. Verifikasi gambar direferensikan dengan benar

### Format Judul PR

- Gunakan judul deskriptif: `[Pelajaran 06] Perbaiki typo contoh Python` atau `Perbarui README untuk pelajaran 08`
- Referensikan nomor isu jika berlaku: `Fixes #123`

### Deskripsi PR

- Jelaskan apa yang diubah dan mengapa
- Tautkan ke isu terkait
- Untuk perubahan kode, spesifikasikan contoh mana yang diuji
- Untuk PR terjemahan, sertakan semua file untuk terjemahan lengkap

### Persyaratan Kontribusi

- Tanda tangani Microsoft CLA (otomatis pada PR pertama)
- Fork repositori ke akun Anda sebelum membuat perubahan
- Satu PR per perubahan logis (jangan gabungkan perbaikan yang tidak terkait)
- Jaga agar PR tetap fokus dan kecil jika memungkinkan

## Alur Kerja Umum

### Menambahkan Contoh Kode Baru

1. Navigasikan ke direktori pelajaran yang sesuai
2. Buat contoh di subdirektori `python/` atau `typescript/`
3. Ikuti konvensi penamaan: `{provider}-{example-name}.{py|ts|js}`
4. Uji dengan kredensial API yang sebenarnya
5. Dokumentasikan variabel lingkungan baru di README pelajaran

### Memperbarui Dokumentasi

1. Edit README.md di direktori pelajaran
2. Ikuti panduan Markdown (ID pelacakan, tautan relatif)
3. Pembaruan terjemahan ditangani oleh GitHub Actions (jangan edit secara manual)
4. Uji semua tautan valid

### Bekerja dengan Dev Containers

1. Repositori menyertakan `.devcontainer/devcontainer.json`
2. Skrip post-create secara otomatis menginstal dependensi Python
3. Ekstensi untuk Python dan Jupyter telah dikonfigurasi sebelumnya
4. Lingkungan berbasis pada `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deployment dan Publikasi

Ini adalah repositori pembelajaran - tidak ada proses deployment. Kurikulum dikonsumsi melalui:

1. **Repositori GitHub**: Akses langsung ke kode dan dokumentasi
2. **GitHub Codespaces**: Lingkungan pengembangan instan dengan setup yang telah dikonfigurasi
3. **Microsoft Learn**: Konten dapat disindikasikan ke platform pembelajaran resmi
4. **docsify**: Situs dokumentasi yang dibangun dari Markdown (lihat `docsifytopdf.js` dan `package.json`)

### Membangun Situs Dokumentasi

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Pemecahan Masalah

### Masalah Umum

**Kesalahan Impor Python**:
- Pastikan lingkungan virtual diaktifkan
- Jalankan `pip install -r requirements.txt`
- Periksa versi Python adalah 3.9+

**Kesalahan Build TypeScript**:
- Jalankan `npm install` di direktori aplikasi tertentu
- Periksa versi Node.js kompatibel
- Hapus `node_modules` dan instal ulang jika diperlukan

**Kesalahan Autentikasi API**:
- Verifikasi file `.env` ada dan memiliki nilai yang benar
- Periksa kunci API valid dan tidak kedaluwarsa
- Pastikan URL endpoint benar untuk wilayah Anda

**Variabel Lingkungan Hilang**:
- Salin `.env.copy` ke `.env`
- Isi semua nilai yang diperlukan untuk pelajaran yang sedang Anda kerjakan
- Restart aplikasi Anda setelah memperbarui `.env`

## Sumber Daya Tambahan

- [Panduan Setup Kursus](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Panduan Kontribusi](./CONTRIBUTING.md)
- [Kode Etik](./CODE_OF_CONDUCT.md)
- [Kebijakan Keamanan](./SECURITY.md)
- [Discord Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Koleksi Contoh Kode Lanjutan](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Catatan Khusus Proyek

- Ini adalah repositori **edukasi** yang berfokus pada pembelajaran, bukan kode produksi
- Contoh sengaja dibuat sederhana dan berfokus pada pengajaran konsep
- Kualitas kode seimbang dengan kejelasan edukasi
- Setiap pelajaran mandiri dan dapat diselesaikan secara independen
- Repositori mendukung beberapa penyedia API: Azure OpenAI, OpenAI, dan Model GitHub
- Konten bersifat multibahasa dengan alur kerja terjemahan otomatis
- Komunitas aktif di Discord untuk pertanyaan dan dukungan

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap disadari bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.