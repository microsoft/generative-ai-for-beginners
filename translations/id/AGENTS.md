# AGENTS.md

## Gambaran Proyek

Repositori ini berisi kurikulum komprehensif 21 pelajaran yang mengajarkan dasar-dasar Generative AI dan pengembangan aplikasi. Kursus ini dirancang untuk pemula dan mencakup segala hal mulai dari konsep dasar hingga membangun aplikasi siap produksi.

**Teknologi Utama:**
- Python 3.9+ dengan perpustakaan: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript dengan Node.js dan perpustakaan: `openai` (Azure OpenAI melalui endpoint v1 + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API, dan Microsoft Foundry Models (GitHub Models akan berhenti pada akhir Juli 2026)
- Jupyter Notebooks untuk pembelajaran interaktif
- Dev Containers untuk lingkungan pengembangan yang konsisten

**Struktur Repositori:**
- 21 direktori pelajaran bernomor (00-21) berisi README, contoh kode, dan tugas
- Beberapa implementasi: contoh dalam Python, TypeScript, dan terkadang .NET
- Direktori terjemahan dengan lebih dari 40 versi bahasa
- Konfigurasi terpusat melalui file `.env` (gunakan `.env.copy` sebagai template)

## Perintah Setup

### Setup Awal Repositori

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

# Instal dependensi
pip install -r requirements.txt
```

### Setup Node.js/TypeScript

```bash
# Pasang dependensi tingkat root (untuk alat dokumentasi)
npm install

# Untuk contoh TypeScript pelajaran individu, navigasikan ke pelajaran spesifik:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Setup Dev Container (Disarankan)

Repositori ini menyertakan konfigurasi `.devcontainer` untuk GitHub Codespaces atau VS Code Dev Containers:

1. Buka repositori di GitHub Codespaces atau VS Code dengan ekstensi Dev Containers
2. Dev Container akan secara otomatis:
   - Menginstal dependensi Python dari `requirements.txt`
   - Menjalankan skrip post-create (`.devcontainer/post-create.sh`)
   - Menyiapkan kernel Jupyter

## Alur Kerja Pengembangan

### Variabel Lingkungan

Semua pelajaran yang memerlukan akses API menggunakan variabel lingkungan yang didefinisikan dalam `.env`:

- `OPENAI_API_KEY` - Untuk OpenAI API
- `AZURE_OPENAI_API_KEY` - Untuk Azure OpenAI di Microsoft Foundry (Azure OpenAI Service sekarang bagian dari Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL endpoint Azure OpenAI (endpoint sumber daya Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Nama deployment model penyelesaian chat (default kursus: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nama deployment model embeddings (default kursus: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - Versi API (default: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Untuk model Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Endpoint Microsoft Foundry Models (katalog model multi-provider)
- `AZURE_INFERENCE_CREDENTIAL` - Kunci API Microsoft Foundry Models (mengganti `GITHUB_TOKEN` yang akan dihentikan)
- `AZURE_INFERENCE_CHAT_MODEL` - Model non-penalaran (misal `Llama-3.3-70B-Instruct`) yang digunakan oleh contoh `temperature`, karena model penalaran tidak mendukung kontrol sampling

### Konvensi Model (penting)

- **Model chat default adalah `gpt-5-mini`** - model penalaran **terkini dan tidak usang**. Per 2026 model "mini" yang mendukung temperature lebih tua (`gpt-4o-mini`, `gpt-4.1-mini`) sedang *dihentikan*, jadi kurikulum menggunakan keluarga GPT-5.
- **Model penalaran menolak `temperature` dan `top_p`**, dan menggunakan `max_output_tokens` (Responses API) / `max_completion_tokens` (chat completions) bukan `max_tokens`. Jangan tambahkan `temperature`/`top_p`/`max_tokens` pada contoh yang memanggil `gpt-5-mini`.
- **Untuk mendemonstrasikan `temperature`**, contoh menggunakan model **Llama** (`Llama-3.3-70B-Instruct`) melalui endpoint Microsoft Foundry Models (`AZURE_INFERENCE_CHAT_MODEL`). Kendalikan model penalaran dengan rekayasa prompt + kontrol penalaran, bukan knob sampling.
- **Fine-tuning (pelajaran 18)** tetap menggunakan `gpt-4.1-mini`: GPT-5 hanya mendukung reinforcement fine-tuning (RFT), bukan supervised fine-tuning (SFT) yang ditunjukkan di sana.
- Pelajaran 20 (Mistral) dan 21 (Meta) tetap menggunakan `temperature`/`max_tokens` karena mereka menargetkan model Mistral/Llama yang mendukungnya.

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

# Jalankan aplikasinya
npm start
```

### Menjalankan Jupyter Notebooks

```bash
# Mulai Jupyter di akar repositori
jupyter notebook

# Atau gunakan VS Code dengan ekstensi Jupyter
```

### Bekerja dengan Jenis Pelajaran Berbeda

- **Pelajaran "Learn"**: Fokus pada dokumentasi README.md dan konsep
- **Pelajaran "Build"**: Termasuk contoh kode yang berjalan di Python dan TypeScript
- Setiap pelajaran memiliki README.md dengan teori, penjelasan kode, dan tautan ke konten video

## Pedoman Gaya Kode

### Python

- Gunakan `python-dotenv` untuk manajemen variabel lingkungan
- Import perpustakaan `openai` untuk interaksi API
- Gunakan `pylint` untuk linting (beberapa contoh menggunakan `# pylint: disable=all` untuk kesederhanaan)
- Ikuti konvensi penamaan PEP 8
- Simpan kredensial API dalam file `.env`, jangan di dalam kode

### TypeScript

- Gunakan paket `dotenv` untuk variabel lingkungan
- Konfigurasi TypeScript di `tsconfig.json` untuk tiap aplikasi
- Gunakan paket `openai` untuk Azure OpenAI (arahkan klien ke endpoint `/openai/v1/` dan panggil `client.responses.create`); gunakan `@azure-rest/ai-inference` untuk Microsoft Foundry Models
- Gunakan `nodemon` untuk pengembangan dengan auto-reload
- Build sebelum menjalankan: `npm run build` lalu `npm start`

### Konvensi Umum

- Buat contoh kode sederhana dan edukatif
- Sertakan komentar yang menjelaskan konsep utama
- Kode setiap pelajaran harus mandiri dan dapat dijalankan
- Gunakan penamaan konsisten: prefix `aoai-` untuk Azure OpenAI, `oai-` untuk OpenAI API, `githubmodels-` untuk Microsoft Foundry Models (prefix lama dari era GitHub Models tetap dipertahankan)

## Pedoman Dokumentasi

### Gaya Markdown

- Semua URL harus dibungkus dalam format `[text](../../url)` tanpa spasi tambahan
- Link relatif harus dimulai dengan `./` atau `../`
- Semua tautan ke domain Microsoft harus menyertakan ID pelacakan: `?WT.mc_id=academic-105485-koreyst`
- Jangan gunakan lokal khusus negara pada URL (hindari `/en-us/`)
- Gambar disimpan dalam folder `./images` dengan nama deskriptif
- Gunakan karakter bahasa Inggris, angka, dan tanda hubung pada nama file

### Dukungan Terjemahan

- Repositori mendukung 40+ bahasa melalui GitHub Actions otomatis
- Terjemahan disimpan di direktori `translations/`
- Jangan mengirimkan terjemahan parsial
- Terjemahan mesin tidak diterima
- Gambar terjemahan disimpan di direktori `translated_images/`

## Pengujian dan Validasi

### Pemeriksaan Pra-Pengiriman

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
   - Periksa kunci API bekerja dengan contoh kode

3. **Contoh Kode**:
   - Pastikan semua kode berjalan tanpa error
   - Uji dengan Azure OpenAI dan OpenAI API bila berlaku
   - Verifikasi contoh bekerja dengan Microsoft Foundry Models bila didukung

### Tidak Ada Pengujian Otomatis

Ini adalah repositori edukasi fokus pada tutorial dan contoh. Tidak ada unit test atau integrasi test yang dijalankan. Validasi terutama:
- Pengujian manual contoh kode
- GitHub Actions untuk validasi Markdown
- Review komunitas pada konten edukasi

## Pedoman Pull Request

### Sebelum Mengirim

1. Uji perubahan kode di Python dan TypeScript bila berlaku
2. Jalankan validasi Markdown (otomatis dipicu pada PR)
3. Pastikan ID pelacakan ada pada semua URL Microsoft
4. Periksa tautan relatif valid
5. Verifikasi gambar direferensikan dengan benar

### Format Judul PR

- Gunakan judul deskriptif: `[Lesson 06] Perbaiki typo contoh Python` atau `Update README untuk pelajaran 08`
- Cantumkan nomor isu bila berlaku: `Fixes #123`

### Deskripsi PR

- Jelaskan perubahan apa dan kenapa
- Berikan tautan ke isu terkait
- Untuk perubahan kode, sebutkan contoh yang diuji
- Untuk PR terjemahan, sertakan semua file untuk terjemahan lengkap

### Persyaratan Kontribusi

- Tanda tangan Microsoft CLA (otomatis pada PR pertama)
- Fork repositori ke akun Anda sebelum membuat perubahan
- Satu PR per perubahan logis (jangan gabungkan perbaikan tak terkait)
- Jaga PR fokus dan kecil jika memungkinkan

## Alur Kerja Umum

### Menambahkan Contoh Kode Baru

1. Arahkan ke direktori pelajaran yang sesuai
2. Buat contoh di subdirektori `python/` atau `typescript/`
3. Ikuti konvensi penamaan: `{provider}-{example-name}.{py|ts|js}`
4. Uji dengan kredensial API asli
5. Dokumentasikan variabel lingkungan baru pada README pelajaran

### Memperbarui Dokumentasi

1. Edit README.md di direktori pelajaran
2. Ikuti panduan Markdown (ID pelacakan, tautan relatif)
3. Pembaruan terjemahan ditangani oleh GitHub Actions (jangan edit manual)
4. Uji semua tautan valid

### Bekerja dengan Dev Containers

1. Repositori memasukkan `.devcontainer/devcontainer.json`
2. Skrip post-create menginstal dependensi Python otomatis
3. Ekstensi untuk Python dan Jupyter sudah dikonfigurasi
4. Lingkungan berbasis `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deployment dan Penerbitan

Ini adalah repositori pembelajaran - tidak ada proses deployment. Kurikulum digunakan oleh:

1. **Repositori GitHub**: Akses langsung ke kode dan dokumentasi
2. **GitHub Codespaces**: Lingkungan dev instan dengan setup pra-konfigurasi
3. **Microsoft Learn**: Konten dapat didistribusikan ke platform pembelajaran resmi
4. **docsify**: Situs dokumentasi dibangun dari Markdown (lihat `docsifytopdf.js` dan `package.json`)

### Membangun Situs Dokumentasi

```bash
# Menghasilkan PDF dari dokumentasi (jika diperlukan)
npm run convert
```

## Pemecahan Masalah

### Masalah Umum

**Kesalahan Impor Python**:
- Pastikan virtual environment aktif
- Jalankan `pip install -r requirements.txt`
- Periksa versi Python 3.9+

**Kesalahan Build TypeScript**:
- Jalankan `npm install` di direktori aplikasi spesifik
- Periksa versi Node.js kompatibel
- Bersihkan `node_modules` dan instal ulang jika perlu

**Kesalahan Otentikasi API**:
- Pastikan file `.env` ada dan nilai benar
- Periksa kunci API valid dan tidak kadaluarsa
- Pastikan URL endpoint benar untuk wilayah Anda

**Variabel Lingkungan Hilang**:
- Salin `.env.copy` ke `.env`
- Isi semua nilai yang dibutuhkan untuk pelajaran yang dikerjakan
- Mulai ulang aplikasi setelah memperbarui `.env`

## Sumber Daya Tambahan

- [Panduan Setup Kursus](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Panduan Kontribusi](./CONTRIBUTING.md)
- [Kode Etik](./CODE_OF_CONDUCT.md)
- [Kebijakan Keamanan](./SECURITY.md)
- [Discord Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Koleksi Contoh Kode Lanjutan](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Catatan Khusus Proyek

- Ini adalah **repositori edukasi** fokus pada pembelajaran, bukan kode produksi
- Contoh sengaja sederhana dan fokus mengajarkan konsep
- Kualitas kode seimbang dengan kejelasan edukasi
- Setiap pelajaran mandiri dan dapat diselesaikan secara terpisah
- Repositori mendukung banyak penyedia API: Azure OpenAI, OpenAI, Microsoft Foundry Models, dan penyedia offline seperti Foundry Local dan Ollama
- Konten multibahasa dengan alur kerja terjemahan otomatis
- Komunitas aktif di Discord untuk pertanyaan dan dukungan

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->