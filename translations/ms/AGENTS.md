# AGENTS.md

## Gambaran Keseluruhan Projek

Repositori ini mengandungi kurikulum komprehensif 21-pelajaran yang mengajar asas Generative AI dan pembangunan aplikasi. Kursus ini direka untuk pemula dan merangkumi segala-galanya dari konsep asas hingga membina aplikasi sedia produksi.

**Teknologi Utama:**
- Python 3.9+ dengan perpustakaan: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript dengan Node.js dan perpustakaan: `openai` (Azure OpenAI melalui titik akhir v1 + API Responses), `@azure-rest/ai-inference` (Model Microsoft Foundry)
- Perkhidmatan Azure OpenAI, API OpenAI, dan Model Microsoft Foundry (Model GitHub akan dihentikan pada akhir Julai 2026)
- Jupyter Notebooks untuk pembelajaran interaktif
- Dev Containers untuk persekitaran pembangunan yang konsisten

**Struktur Repositori:**
- 21 direktori pelajaran bernombor (00-21) mengandungi README, contoh kod, dan tugasan
- Pelbagai implementasi: contoh Python, TypeScript, dan kadang-kadang .NET
- Direktori terjemahan dengan 40+ versi bahasa
- Konfigurasi terpusat melalui fail `.env` (gunakan `.env.copy` sebagai templat)

## Arahan Penyediaan

### Penyediaan Awal Repositori

```bash
# Klon repositori
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Salin templat persekitaran
cp .env.copy .env
# Edit .env dengan kunci API dan titik akhir anda
```

### Penyediaan Persekitaran Python

```bash
# Cipta persekitaran maya
python3 -m venv venv

# Aktifkan persekitaran maya
# Pada macOS/Linux:
source venv/bin/activate
# Pada Windows:
venv\Scripts\activate

# Pasang kebergantungan
pip install -r requirements.txt
```

### Penyediaan Node.js/TypeScript

```bash
# Pasang kebergantungan peringkat root (untuk alat dokumentasi)
npm install

# Untuk contoh TypeScript pelajaran individu, pergi ke pelajaran tertentu:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Penyediaan Dev Container (Disyorkan)

Repositori ini termasuk konfigurasi `.devcontainer` untuk GitHub Codespaces atau VS Code Dev Containers:

1. Buka repositori dalam GitHub Codespaces atau VS Code dengan sambungan Dev Containers
2. Dev Container akan secara automatik:
   - Pasang kebergantungan Python dari `requirements.txt`
   - Jalankan skrip post-create (`.devcontainer/post-create.sh`)
   - Sediakan kernel Jupyter

## Aliran Kerja Pembangunan

### Pembolehubah Persekitaran

Semua pelajaran yang memerlukan akses API menggunakan pembolehubah persekitaran yang ditakrifkan dalam `.env`:

- `OPENAI_API_KEY` - Untuk OpenAI API
- `AZURE_OPENAI_API_KEY` - Untuk Azure OpenAI dalam Microsoft Foundry (Perkhidmatan Azure OpenAI kini sebahagian daripada Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL titik akhir Azure OpenAI (titik akhir sumber Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Nama penyebaran model penyelesaian sembang (default kursus: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nama penyebaran model imbangan (default kursus: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - Versi API (default: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Untuk model Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Titik akhir Model Microsoft Foundry (katalog model pelbagai penyedia)
- `AZURE_INFERENCE_CREDENTIAL` - Kunci API Model Microsoft Foundry (menggantikan `GITHUB_TOKEN` yang akan dihentikan)
- `AZURE_INFERENCE_CHAT_MODEL` - Model tanpa penalaran (contoh `Llama-3.3-70B-Instruct`) digunakan oleh contoh `temperature`, kerana model penalaran tidak menyokong kawalan pensampelan

### Konvensyen Model (penting)

- **Model sembang lalai adalah `gpt-5-mini`** - model **penalaran** terkini yang tidak terdepresiasi. Sejak 2026 model "mini" lama yang menyokong suhu (`gpt-4o-mini`, `gpt-4.1-mini`) sedang *dipencilkan*, jadi kurikulum menggunakan keluarga GPT-5.
- **Model penalaran menolak `temperature` dan `top_p`**, dan menggunakan `max_output_tokens` (API Responses) / `max_completion_tokens` (penyelesaian sembang) menggantikan `max_tokens`. Jangan tambahkan `temperature`/`top_p`/`max_tokens` pada contoh yang memanggil `gpt-5-mini`.
- **Untuk demonstrasi `temperature`**, contoh menggunakan model **Llama** (`Llama-3.3-70B-Instruct`) melalui titik akhir Model Microsoft Foundry (`AZURE_INFERENCE_CHAT_MODEL`). Kawal model penalaran dengan kejuruteraan arahan + kawalan penalaran bukannya tombol pensampelan.
- **Fine-tuning (pelajaran 18)** mengekalkan `gpt-4.1-mini`: GPT-5 hanya menyokong penghalusan pengukuhan (RFT), bukan penghalusan terselia (SFT) yang ditunjukkan di situ.
- Pelajaran 20 (Mistral) dan 21 (Meta) masih menggunakan `temperature`/`max_tokens` kerana mereka mensasarkan model Mistral/Llama yang menyokongnya.

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

# Atau gunakan VS Code dengan peluasan Jupyter
```

### Bekerja dengan Jenis Pelajaran Berbeza

- **Pelajaran "Learn"**: Fokus pada dokumentasi README.md dan konsep
- **Pelajaran "Build"**: Termasuk contoh kod berfungsi dalam Python dan TypeScript
- Setiap pelajaran mempunyai README.md dengan teori, penerangan kod, dan pautan ke kandungan video

## Garis Panduan Gaya Kod

### Python

- Gunakan `python-dotenv` untuk pengurusan pembolehubah persekitaran
- Import perpustakaan `openai` untuk interaksi API
- Gunakan `pylint` untuk linting (sesetengah contoh menggunakan `# pylint: disable=all` untuk kesederhanaan)
- Ikut konvensyen penamaan PEP 8
- Simpan kelayakan API dalam fail `.env`, jangan dalam kod

### TypeScript

- Gunakan pakej `dotenv` untuk pembolehubah persekitaran
- Konfigurasi TypeScript di `tsconfig.json` untuk setiap aplikasi
- Gunakan pakej `openai` untuk Azure OpenAI (arahkan klien ke titik akhir `/openai/v1/` dan panggil `client.responses.create`); gunakan `@azure-rest/ai-inference` untuk Model Microsoft Foundry
- Gunakan `nodemon` untuk pembangunan dengan muat semula automatik
- Bina sebelum menjalankan: `npm run build` kemudian `npm start`

### Konvensyen Umum

- Pastikan contoh kod ringkas dan bersifat pendidikan
- Sertakan komen menerangkan konsep utama
- Kod setiap pelajaran harus berdikari dan boleh dijalankan
- Gunakan penamaan konsisten: awalan `aoai-` untuk Azure OpenAI, `oai-` untuk OpenAI API, `githubmodels-` untuk Model Microsoft Foundry (awalan warisan dari era Model GitHub)

## Garis Panduan Dokumentasi

### Gaya Markdown

- Semua URL mesti dibungkus dalam format `[text](../../url)` tanpa ruang tambahan
- Pautan relatif mesti bermula dengan `./` atau `../`
- Semua pautan ke domain Microsoft mesti memasukkan ID penjejakan: `?WT.mc_id=academic-105485-koreyst`
- Tiada lokal khusus negara dalam URL (elakkan `/en-us/`)
- Imej disimpan dalam folder `./images` dengan nama deskriptif
- Gunakan huruf Inggeris, nombor, dan tanda sengkang dalam nama fail

### Sokongan Terjemahan

- Repositori menyokong 40+ bahasa melalui GitHub Actions automatik
- Terjemahan disimpan dalam direktori `translations/`
- Jangan hantar terjemahan separa
- Terjemahan mesin tidak diterima
- Imej terjemahan disimpan dalam direktori `translated_images/`

## Ujian dan Pengesahan

### Semakan Pra-Penghantaran

Repositori ini menggunakan GitHub Actions untuk pengesahan. Sebelum menghantar PR:

1. **Semak Pautan Markdown**:
   ```bash
   # Aliran kerja validate-markdown.yml memeriksa:
   # - Laluan relatif yang rosak
   # - ID penjejakan hilang pada laluan
   # - ID penjejakan hilang pada URL
   # - URL dengan lokal negara
   # - URL luaran yang rosak
   ```

2. **Ujian Manual**:
   - Uji contoh Python: Aktifkan venv dan jalankan skrip
   - Uji contoh TypeScript: `npm install`, `npm run build`, `npm start`
   - Sahkan pembolehubah persekitaran dikonfigurasi dengan betul
   - Semak kunci API berfungsi dengan contoh kod

3. **Contoh Kod**:
   - Pastikan semua kod berjalan tanpa ralat
   - Uji dengan Azure OpenAI dan OpenAI API bila sesuai
   - Sahkan contoh berfungsi dengan Model Microsoft Foundry jika disokong

### Tiada Ujian Automatik

Ini adalah repositori pendidikan fokus kepada tutorial dan contoh. Tiada ujian unit atau integrasi dijalankan. Pengesahan ialah terutamanya:
- Ujian manual contoh kod
- GitHub Actions untuk pengesahan Markdown
- Semakan komuniti terhadap kandungan pendidikan

## Garis Panduan Pull Request

### Sebelum Menghantar

1. Uji perubahan kod dalam Python dan TypeScript bila sesuai
2. Jalankan pengesahan Markdown (dicetuskan automatik pada PR)
3. Pastikan ID penjejakan ada pada semua URL Microsoft
4. Semak pautan relatif sah
5. Sahkan imej dirujuk dengan betul

### Format Tajuk PR

- Gunakan tajuk deskriptif: `[Lesson 06] Betulkan ralat contoh Python` atau `Kemas kini README untuk pelajaran 08`
- Rujuk nombor isu bila sesuai: `Fixes #123`

### Penerangan PR

- Terangkan apa yang diubah dan kenapa
- Sertakan pautan ke isu berkaitan
- Untuk perubahan kod, nyatakan contoh yang diuji
- Untuk PR terjemahan, sertakan semua fail untuk terjemahan lengkap

### Keperluan Sumbangan

- Tandatangani CLA Microsoft (automatik pada PR pertama)
- Fork repositori ke akaun anda sebelum membuat perubahan
- Satu PR untuk satu perubahan logik (jangan gabungkan pembetulan tidak berkaitan)
- Pastikan PR fokus dan kecil bila boleh

## Aliran Kerja Lazim

### Menambah Contoh Kod Baru

1. Navigasi ke direktori pelajaran yang sesuai
2. Buat contoh dalam subdirektori `python/` atau `typescript/`
3. Ikut konvensyen penamaan: `{provider}-{example-name}.{py|ts|js}`
4. Uji dengan kelayakan API sebenar
5. Dokumentasikan semua pembolehubah persekitaran baru dalam README pelajaran

### Mengemas Kini Dokumentasi

1. Edit README.md dalam direktori pelajaran
2. Ikut garis panduan Markdown (ID penjejakan, pautan relatif)
3. Kemas kini terjemahan dikendalikan oleh GitHub Actions (jangan edit secara manual)
4. Uji semua pautan sah

### Bekerja dengan Dev Containers

1. Repositori termasuk `.devcontainer/devcontainer.json`
2. Skrip post-create memasang kebergantungan Python secara automatik
3. Sambungan untuk Python dan Jupyter telah diprapasang
4. Persekitaran berdasarkan `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Penyebaran dan Penerbitan

Ini repositori pembelajaran - tiada proses penyebaran. Kurikulum ini diakses melalui:

1. **Repositori GitHub**: Akses langsung kod dan dokumentasi
2. **GitHub Codespaces**: Persekitaran pembangunan segera dengan penyediaan diprapasang
3. **Microsoft Learn**: Kandungan mungkin disindikasikan ke platform pembelajaran rasmi
4. **docsify**: Tapak dokumentasi dibina dari Markdown (lihat `docsifytopdf.js` dan `package.json`)

### Membina Tapak Dokumentasi

```bash
# Jana PDF dari dokumentasi (jika perlu)
npm run convert
```

## Penyelesaian Masalah

### Isu Lazim

**Ralat Import Python**:
- Pastikan persekitaran maya diaktifkan
- Jalankan `pip install -r requirements.txt`
- Semak versi Python adalah 3.9+

**Ralat Binaan TypeScript**:
- Jalankan `npm install` dalam direktori aplikasi spesifik
- Semak versi Node.js serasi
- Kosongkan `node_modules` dan pasang semula jika perlu

**Ralat Pengesahan API**:
- Sahkan fail `.env` ada dan nilai betul
- Semak kunci API sah dan belum tamat tempoh
- Pastikan URL titik akhir betul untuk rantau anda

**Pembolehubah Persekitaran Hilang**:
- Salin `.env.copy` ke `.env`
- Isi semua nilai yang diperlukan untuk pelajaran yang sedang dikerjakan
- Mulakan semula aplikasi selepas mengemaskini `.env`

## Sumber Tambahan

- [Panduan Penyediaan Kursus](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Garis Panduan Penyumbang](./CONTRIBUTING.md)
- [Kod Etika](./CODE_OF_CONDUCT.md)
- [Polisi Keselamatan](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Koleksi Contoh Kod Lanjutan](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Nota Khusus Projek

- Ini adalah **repositori pendidikan** fokus kepada pembelajaran, bukan kod produksi
- Contoh sengaja ringkas dan fokus pada pengajaran konsep
- Kualiti kod seimbang dengan kejelasan pendidikan
- Setiap pelajaran berdikari dan boleh diselesaikan secara bebas
- Repositori menyokong pelbagai penyedia API: Azure OpenAI, OpenAI, Model Microsoft Foundry, dan penyedia luar talian seperti Foundry Local dan Ollama
- Kandungan berbilang bahasa dengan aliran kerja terjemahan automatik
- Komuniti aktif di Discord untuk soalan dan sokongan

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->