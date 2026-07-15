# AGEN

## Gambaran Projek

Repositori ini mengandungi kurikulum 21 pelajaran yang komprehensif yang mengajar asas Generative AI dan pembangunan aplikasi. Kursus ini direka untuk pemula dan merangkumi segala-galanya dari konsep asas hingga membina aplikasi sedia produksi.

**Teknologi Utama:**
- Python 3.9+ dengan perpustakaan: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript dengan Node.js dan perpustakaan: `openai` (Azure OpenAI melalui titik akhir v1 + API Respons), `@azure-rest/ai-inference` (Model Microsoft Foundry)
- Perkhidmatan Azure OpenAI, API OpenAI, dan Model Microsoft Foundry (GitHub Models akan ditutup pada akhir Julai 2026)
- Jupyter Notebooks untuk pembelajaran interaktif
- Dev Containers untuk persekitaran pembangunan yang konsisten

**Struktur Repositori:**
- 21 direktori pelajaran bernombor (00-21) yang mengandungi README, contoh kod, dan tugasan
- Pelbagai pelaksanaan: Python, TypeScript, dan kadang-kadang contoh .NET
- Direktori terjemahan dengan lebih 40 versi bahasa
- Konfigurasi pusat melalui fail `.env` (gunakan `.env.copy` sebagai templat)

## Arahan Persediaan

### Persediaan Awal Repositori

```bash
# Klon repositori
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Salin templat persekitaran
cp .env.copy .env
# Edit .env dengan kunci API dan titik akhir anda
```

### Persediaan Persekitaran Python

```bash
# Buat persekitaran maya
python3 -m venv venv

# Aktifkan persekitaran maya
# Pada macOS/Linux:
source venv/bin/activate
# Pada Windows:
venv\Scripts\activate

# Pasang kebergantungan
pip install -r requirements.txt
```

### Persediaan Node.js/TypeScript

```bash
# Pasang kebergantungan pada tahap root (untuk alat dokumentasi)
npm install

# Untuk contoh TypeScript pelajaran individu, navigasi ke pelajaran tertentu:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Persediaan Dev Container (Disyorkan)

Repositori ini termasuk konfigurasi `.devcontainer` untuk GitHub Codespaces atau VS Code Dev Containers:

1. Buka repositori di GitHub Codespaces atau VS Code dengan sambungan Dev Containers
2. Dev Container akan secara automatik:
   - Pasang kebergantungan Python dari `requirements.txt`
   - Jalankan skrip post-create (`.devcontainer/post-create.sh`)
   - Sediakan kernel Jupyter

## Aliran Kerja Pembangunan

### Pembolehubah Persekitaran

Semua pelajaran yang memerlukan akses API menggunakan pembolehubah persekitaran yang ditakrifkan dalam `.env`:

- `OPENAI_API_KEY` - Untuk API OpenAI
- `AZURE_OPENAI_API_KEY` - Untuk Azure OpenAI dalam Microsoft Foundry (Perkhidmatan Azure OpenAI kini sebahagian daripada Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL titik akhir Azure OpenAI (titik akhir sumber Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Nama pelaksanaan model penyelesaian chat
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nama pelaksanaan model embeding
- `AZURE_OPENAI_API_VERSION` - Versi API (lalai: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Untuk model Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Titik akhir Model Microsoft Foundry (katalog model pelbagai penyedia)
- `AZURE_INFERENCE_CREDENTIAL` - Kunci API Model Microsoft Foundry (menggantikan `GITHUB_TOKEN` yang akan ditutup)

### Menjalankan Contoh Python

```bash
# Navigasi ke direktori pelajaran
cd 06-text-generation-apps/python

# Jalankan skrip Python
python aoai-app.py
```

### Menjalankan Contoh TypeScript

```bash
# Navigasi ke direktori aplikasi TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Bina kod TypeScript
npm run build

# Jalankan aplikasi
npm start
```

### Menjalankan Jupyter Notebooks

```bash
# Mulakan Jupyter di akar repositori
jupyter notebook

# Atau gunakan VS Code dengan sambungan Jupyter
```

### Bekerja dengan Jenis Pelajaran Berbeza

- **Pelajaran "Learn"**: Fokus pada dokumentasi README.md dan konsep
- **Pelajaran "Build"**: Termasuk contoh kod berfungsi dalam Python dan TypeScript
- Setiap pelajaran mempunyai README.md dengan teori, penceritaan kod, dan pautan ke kandungan video

## Garis Panduan Gaya Kod

### Python

- Gunakan `python-dotenv` untuk pengurusan pembolehubah persekitaran
- Import perpustakaan `openai` untuk interaksi API
- Gunakan `pylint` untuk linting (beberapa contoh menggunakan `# pylint: disable=all` untuk kesederhanaan)
- Ikut konvensyen penamaan PEP 8
- Simpan kelayakan API dalam fail `.env`, jangan dalam kod

### TypeScript

- Gunakan pakej `dotenv` untuk pembolehubah persekitaran
- Konfigurasi TypeScript dalam `tsconfig.json` untuk setiap aplikasi
- Gunakan pakej `openai` untuk Azure OpenAI (arah pelanggan di titik akhir `/openai/v1/` dan panggil `client.responses.create`); guna `@azure-rest/ai-inference` untuk Model Microsoft Foundry
- Gunakan `nodemon` untuk pembangunan dengan muat semula automatik
- Bina sebelum menjalankan: `npm run build` kemudian `npm start`

### Konvensyen Am

- Kekalkan contoh kod sederhana dan pendidikan
- Sertakan komen yang menerangkan konsep utama
- Kod setiap pelajaran harus berdikari dan boleh dijalankan
- Gunakan penamaan konsisten: awalan `aoai-` untuk Azure OpenAI, `oai-` untuk API OpenAI, `githubmodels-` untuk Model Microsoft Foundry (awalan warisan dari era GitHub Models)

## Garis Panduan Dokumentasi

### Gaya Markdown

- Semua URL mesti dibungkus dalam format `[text](../../url)` tanpa ruang tambahan
- Pautan relatif mesti bermula dengan `./` atau `../`
- Semua pautan ke domain Microsoft mesti menyertakan ID penjejakan: `?WT.mc_id=academic-105485-koreyst`
- Tiada setempat khusus negara dalam URL (elakkan `/en-us/`)
- Imej disimpan dalam folder `./images` dengan nama yang deskriptif
- Gunakan aksara Inggeris, nombor, dan tanda sengkang dalam nama fail

### Sokongan Terjemahan

- Repositori menyokong lebih 40 bahasa melalui GitHub Actions automatik
- Terjemahan disimpan di direktori `translations/`
- Jangan hantar terjemahan separa
- Terjemahan mesin tidak diterima
- Imej diterjemah disimpan dalam direktori `translated_images/`

## Ujian dan Pengesahan

### Pemeriksaan Pra-hantar

Repositori ini menggunakan GitHub Actions untuk pengesahan. Sebelum menghantar PR:

1. **Periksa Pautan Markdown**:
   ```bash
   # Aliran kerja validate-markdown.yml memeriksa:
   # - Laluan relatif yang rosak
   # - ID penjejakan yang hilang pada laluan
   # - ID penjejakan yang hilang pada URL
   # - URL dengan lokal negara
   # - URL luaran yang rosak
   ```

2. **Ujian Manual**:
   - Uji contoh Python: Aktifkan venv dan jalankan skrip
   - Uji contoh TypeScript: `npm install`, `npm run build`, `npm start`
   - Sahkan pembolehubah persekitaran dikonfigurasi dengan betul
   - Periksa kekunci API berfungsi dengan contoh kod

3. **Contoh Kod**:
   - Pastikan semua kod berjalan tanpa ralat
   - Uji dengan kedua-dua Azure OpenAI dan API OpenAI bila sesuai
   - Sahkan contoh berfungsi dengan Model Microsoft Foundry bila disokong

### Tiada Ujian Automatik

Ini adalah repositori pendidikan yang fokus pada tutorial dan contoh. Tiada ujian unit atau ujian integrasi untuk dijalankan. Pengesahan adalah terutamanya:
- Ujian manual contoh kod
- GitHub Actions untuk pengesahan Markdown
- Semakan komuniti untuk kandungan pendidikan

## Garis Panduan Pull Request

### Sebelum Menghantar

1. Uji perubahan kod dalam Python dan TypeScript bila sesuai
2. Jalankan pengesahan Markdown (dijalankan secara automatik pada PR)
3. Pastikan ID penjejakan hadir pada semua URL Microsoft
4. Semak pautan relatif sah
5. Sahkan imej dirujuk dengan betul

### Format Tajuk PR

- Gunakan tajuk yang deskriptif: `[Pelajaran 06] Betulkan typo contoh Python` atau `Kemas kini README untuk pelajaran 08`
- Rujuk nombor isu bila sesuai: `Betulkan #123`

### Penerangan PR

- Terangkan apa yang diubah dan sebabnya
- Paut ke isu berkaitan
- Untuk perubahan kod, nyatakan contoh yang diuji
- Untuk PR terjemahan, sertakan semua fail untuk terjemahan lengkap

### Keperluan Sumbangan

- Tandatangani CLA Microsoft (automatik pada PR pertama)
- Fork repositori ke akaun anda sebelum membuat perubahan
- Satu PR bagi setiap perubahan logik (jangan gabungkan pembetulan tidak berkaitan)
- Kekalkan PR fokus dan kecil jika boleh

## Aliran Kerja Biasa

### Menambah Contoh Kod Baru

1. Navigasi ke direktori pelajaran yang sesuai
2. Buat contoh dalam subdirektori `python/` atau `typescript/`
3. Ikut konvensyen penamaan: `{provider}-{example-name}.{py|ts|js}`
4. Uji dengan kelayakan API sebenar
5. Dokumenkan sebarang pembolehubah persekitaran baru dalam README pelajaran

### Mengemas Kini Dokumentasi

1. Edit README.md dalam direktori pelajaran
2. Ikut garis panduan Markdown (ID penjejakan, pautan relatif)
3. Kemas kini terjemahan dikendalikan oleh GitHub Actions (jangan sunting secara manual)
4. Uji semua pautan adalah sah

### Bekerja dengan Dev Containers

1. Repositori termasuk `.devcontainer/devcontainer.json`
2. Skrip post-create memasang kebergantungan Python secara automatik
3. Sambungan untuk Python dan Jupyter telah diprapasang
4. Persekitaran berdasarkan `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Penghantaran dan Penerbitan

Ini adalah repositori pembelajaran - tiada proses penghantaran. Kurikulum dimanfaatkan oleh:

1. **Repositori GitHub**: Akses langsung ke kod dan dokumentasi
2. **GitHub Codespaces**: Persekitaran dev segera dengan persediaan prakonfigurasi
3. **Microsoft Learn**: Kandungan mungkin disintesis ke platform pembelajaran rasmi
4. **docsify**: Laman dokumentasi dibina dari Markdown (lihat `docsifytopdf.js` dan `package.json`)

### Membangun Laman Dokumentasi

```bash
# Jana PDF dari dokumentasi (jika perlu)
npm run convert
```

## Penyelesaian Masalah

### Isu Biasa

**Ralat Import Python**:
- Pastikan persekitaran maya diaktifkan
- Jalankan `pip install -r requirements.txt`
- Periksa versi Python adalah 3.9+

**Ralat Pembinaan TypeScript**:
- Jalankan `npm install` dalam direktori aplikasi tertentu
- Periksa versi Node.js serasi
- Kosongkan `node_modules` dan pasang semula jika perlu

**Ralat Pengesahan API**:
- Sahkan fail `.env` wujud dan mempunyai nilai yang betul
- Periksa kekunci API sah dan tidak tamat tempoh
- Pastikan URL titik akhir betul untuk rantau anda

**Pembolehubah Persekitaran Hilang**:
- Salin `.env.copy` ke `.env`
- Isikan semua nilai diperlukan untuk pelajaran yang anda kerjakan
- Mulakan semula aplikasi anda selepas mengemaskini `.env`

## Sumber Tambahan

- [Panduan Persediaan Kursus](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Garis Panduan Menyumbang](./CONTRIBUTING.md)
- [Kod Etika](./CODE_OF_CONDUCT.md)
- [Polisi Keselamatan](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Koleksi Contoh Kod Lanjutan](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Nota Khusus Projek

- Ini adalah **repositori pendidikan** yang tertumpu pada pembelajaran, bukan kod produksi
- Contoh adalah sengaja ringkas dan berfokus pada pengajaran konsep
- Kualiti kod seimbang dengan kejelasan pendidikan
- Setiap pelajaran berdikari dan boleh disiapkan secara bebas
- Repositori menyokong pelbagai penyedia API: Azure OpenAI, OpenAI, Model Microsoft Foundry, dan penyedia luar talian seperti Foundry Local dan Ollama
- Kandungan adalah berbilang bahasa dengan aliran kerja terjemahan automatik
- Komuniti aktif di Discord untuk pertanyaan dan sokongan

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->