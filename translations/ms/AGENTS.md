<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:07:46+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ms"
}
-->
# AGENTS.md

## Gambaran Projek

Repositori ini mengandungi kurikulum 21 pelajaran yang komprehensif untuk mengajar asas AI Generatif dan pembangunan aplikasi. Kursus ini direka untuk pemula dan merangkumi segala-galanya daripada konsep asas hingga membina aplikasi yang sedia untuk pengeluaran.

**Teknologi Utama:**
- Python 3.9+ dengan perpustakaan: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript dengan Node.js dan perpustakaan: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API, dan Model GitHub
- Jupyter Notebooks untuk pembelajaran interaktif
- Dev Containers untuk persekitaran pembangunan yang konsisten

**Struktur Repositori:**
- 21 direktori pelajaran bernombor (00-21) yang mengandungi README, contoh kod, dan tugasan
- Pelbagai implementasi: Python, TypeScript, dan kadangkala contoh .NET
- Direktori terjemahan dengan lebih daripada 40 versi bahasa
- Konfigurasi berpusat melalui fail `.env` (gunakan `.env.copy` sebagai templat)

## Perintah Persediaan

### Persediaan Awal Repositori

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Persediaan Persekitaran Python

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

### Persediaan Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Persediaan Dev Container (Disyorkan)

Repositori ini termasuk konfigurasi `.devcontainer` untuk GitHub Codespaces atau VS Code Dev Containers:

1. Buka repositori dalam GitHub Codespaces atau VS Code dengan sambungan Dev Containers
2. Dev Container akan secara automatik:
   - Memasang kebergantungan Python daripada `requirements.txt`
   - Menjalankan skrip selepas penciptaan (`.devcontainer/post-create.sh`)
   - Menyediakan kernel Jupyter

## Aliran Kerja Pembangunan

### Pembolehubah Persekitaran

Semua pelajaran yang memerlukan akses API menggunakan pembolehubah persekitaran yang ditakrifkan dalam `.env`:

- `OPENAI_API_KEY` - Untuk OpenAI API
- `AZURE_OPENAI_API_KEY` - Untuk Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - URL titik akhir Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` - Nama penyebaran model penyelesaian chat
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nama penyebaran model embeddings
- `AZURE_OPENAI_API_VERSION` - Versi API (lalai: `2024-02-01`)
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

### Bekerja dengan Jenis Pelajaran Berbeza

- **Pelajaran "Learn"**: Fokus pada dokumentasi README.md dan konsep
- **Pelajaran "Build"**: Termasuk contoh kod berfungsi dalam Python dan TypeScript
- Setiap pelajaran mempunyai README.md dengan teori, panduan kod, dan pautan ke kandungan video

## Garis Panduan Gaya Kod

### Python

- Gunakan `python-dotenv` untuk pengurusan pembolehubah persekitaran
- Import perpustakaan `openai` untuk interaksi API
- Gunakan `pylint` untuk linting (beberapa contoh termasuk `# pylint: disable=all` untuk kesederhanaan)
- Ikuti konvensyen penamaan PEP 8
- Simpan kelayakan API dalam fail `.env`, jangan pernah dalam kod

### TypeScript

- Gunakan pakej `dotenv` untuk pembolehubah persekitaran
- Konfigurasi TypeScript dalam `tsconfig.json` untuk setiap aplikasi
- Gunakan `@azure/openai` atau `@azure-rest/ai-inference` untuk perkhidmatan Azure
- Gunakan `nodemon` untuk pembangunan dengan auto-reload
- Bina sebelum menjalankan: `npm run build` kemudian `npm start`

### Konvensyen Umum

- Pastikan contoh kod mudah dan mendidik
- Sertakan komen yang menerangkan konsep utama
- Kod setiap pelajaran harus berdiri sendiri dan boleh dijalankan
- Gunakan penamaan yang konsisten: awalan `aoai-` untuk Azure OpenAI, `oai-` untuk OpenAI API, `githubmodels-` untuk Model GitHub

## Garis Panduan Dokumentasi

### Gaya Markdown

- Semua URL mesti dibungkus dalam format `[teks](../../url)` tanpa ruang tambahan
- Pautan relatif mesti bermula dengan `./` atau `../`
- Semua pautan ke domain Microsoft mesti termasuk ID penjejakan: `?WT.mc_id=academic-105485-koreyst`
- Tiada lokal khusus negara dalam URL (elakkan `/en-us/`)
- Imej disimpan dalam folder `./images` dengan nama yang deskriptif
- Gunakan aksara Inggeris, nombor, dan tanda hubung dalam nama fail

### Sokongan Terjemahan

- Repositori menyokong lebih daripada 40 bahasa melalui GitHub Actions automatik
- Terjemahan disimpan dalam direktori `translations/`
- Jangan serahkan terjemahan separa
- Terjemahan mesin tidak diterima
- Imej terjemahan disimpan dalam direktori `translated_images/`

## Ujian dan Pengesahan

### Semakan Sebelum Penyerahan

Repositori ini menggunakan GitHub Actions untuk pengesahan. Sebelum menyerahkan PR:

1. **Semak Pautan Markdown**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Ujian Manual**:
   - Uji contoh Python: Aktifkan venv dan jalankan skrip
   - Uji contoh TypeScript: `npm install`, `npm run build`, `npm start`
   - Pastikan pembolehubah persekitaran dikonfigurasi dengan betul
   - Semak bahawa kunci API berfungsi dengan contoh kod

3. **Contoh Kod**:
   - Pastikan semua kod berjalan tanpa ralat
   - Uji dengan kedua-dua Azure OpenAI dan OpenAI API apabila berkenaan
   - Pastikan contoh berfungsi dengan Model GitHub di mana disokong

### Tiada Ujian Automatik

Ini adalah repositori pendidikan yang fokus pada tutorial dan contoh. Tiada ujian unit atau ujian integrasi untuk dijalankan. Pengesahan adalah terutamanya:
- Ujian manual contoh kod
- GitHub Actions untuk pengesahan Markdown
- Semakan komuniti kandungan pendidikan

## Garis Panduan Pull Request

### Sebelum Menyerahkan

1. Uji perubahan kod dalam kedua-dua Python dan TypeScript apabila berkenaan
2. Jalankan pengesahan Markdown (dicetuskan secara automatik pada PR)
3. Pastikan ID penjejakan ada pada semua URL Microsoft
4. Semak bahawa pautan relatif adalah sah
5. Pastikan imej dirujuk dengan betul

### Format Tajuk PR

- Gunakan tajuk deskriptif: `[Lesson 06] Betulkan typo contoh Python` atau `Kemas kini README untuk pelajaran 08`
- Rujuk nombor isu apabila berkenaan: `Fixes #123`

### Penerangan PR

- Terangkan apa yang diubah dan mengapa
- Pautkan ke isu berkaitan
- Untuk perubahan kod, nyatakan contoh mana yang diuji
- Untuk PR terjemahan, sertakan semua fail untuk terjemahan lengkap

### Keperluan Sumbangan

- Tandatangani Microsoft CLA (automatik pada PR pertama)
- Fork repositori ke akaun anda sebelum membuat perubahan
- Satu PR untuk setiap perubahan logik (jangan gabungkan pembetulan yang tidak berkaitan)
- Kekalkan PR fokus dan kecil apabila boleh

## Aliran Kerja Biasa

### Menambah Contoh Kod Baru

1. Navigasi ke direktori pelajaran yang sesuai
2. Cipta contoh dalam subdirektori `python/` atau `typescript/`
3. Ikuti konvensyen penamaan: `{provider}-{example-name}.{py|ts|js}`
4. Uji dengan kelayakan API sebenar
5. Dokumentasikan sebarang pembolehubah persekitaran baru dalam README pelajaran

### Mengemas Kini Dokumentasi

1. Edit README.md dalam direktori pelajaran
2. Ikuti garis panduan Markdown (ID penjejakan, pautan relatif)
3. Kemas kini terjemahan dikendalikan oleh GitHub Actions (jangan edit secara manual)
4. Uji semua pautan adalah sah

### Bekerja dengan Dev Containers

1. Repositori termasuk `.devcontainer/devcontainer.json`
2. Skrip selepas penciptaan memasang kebergantungan Python secara automatik
3. Sambungan untuk Python dan Jupyter telah dikonfigurasi
4. Persekitaran berdasarkan `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Penerbitan dan Penyebaran

Ini adalah repositori pembelajaran - tiada proses penyebaran. Kurikulum digunakan oleh:

1. **Repositori GitHub**: Akses langsung kepada kod dan dokumentasi
2. **GitHub Codespaces**: Persekitaran pembangunan segera dengan persediaan yang telah dikonfigurasi
3. **Microsoft Learn**: Kandungan mungkin disindikasikan ke platform pembelajaran rasmi
4. **docsify**: Laman dokumentasi dibina daripada Markdown (lihat `docsifytopdf.js` dan `package.json`)

### Membina Laman Dokumentasi

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Penyelesaian Masalah

### Isu Biasa

**Ralat Import Python**:
- Pastikan persekitaran maya diaktifkan
- Jalankan `pip install -r requirements.txt`
- Semak versi Python adalah 3.9+

**Ralat Pembinaan TypeScript**:
- Jalankan `npm install` dalam direktori aplikasi tertentu
- Semak versi Node.js adalah serasi
- Kosongkan `node_modules` dan pasang semula jika perlu

**Ralat Pengesahan API**:
- Pastikan fail `.env` wujud dan mempunyai nilai yang betul
- Semak kunci API adalah sah dan tidak tamat tempoh
- Pastikan URL titik akhir adalah betul untuk rantau anda

**Pembolehubah Persekitaran Hilang**:
- Salin `.env.copy` ke `.env`
- Isi semua nilai yang diperlukan untuk pelajaran yang sedang anda kerjakan
- Mulakan semula aplikasi anda selepas mengemas kini `.env`

## Sumber Tambahan

- [Panduan Persediaan Kursus](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Garis Panduan Penyumbangan](./CONTRIBUTING.md)
- [Kod Etika](./CODE_OF_CONDUCT.md)
- [Dasar Keselamatan](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Koleksi Contoh Kod Lanjutan](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Nota Khusus Projek

- Ini adalah repositori **pendidikan** yang fokus pada pembelajaran, bukan kod pengeluaran
- Contoh sengaja dibuat mudah dan fokus pada pengajaran konsep
- Kualiti kod seimbang dengan kejelasan pendidikan
- Setiap pelajaran berdiri sendiri dan boleh diselesaikan secara bebas
- Repositori menyokong pelbagai penyedia API: Azure OpenAI, OpenAI, dan Model GitHub
- Kandungan adalah pelbagai bahasa dengan aliran kerja terjemahan automatik
- Komuniti aktif di Discord untuk soalan dan sokongan

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.