# Peta Jalan Fitur dan Peningkatan yang Ditingkatkan

Dokumen ini menguraikan peningkatan dan perbaikan yang direkomendasikan untuk kurikulum Generative AI for Beginners, berdasarkan tinjauan kode menyeluruh dan analisis praktik terbaik industri.

## Ringkasan Eksekutif

Basis kode telah dianalisis untuk keamanan, kualitas kode, dan efektivitas pendidikan. Dokumen ini memberikan rekomendasi untuk perbaikan segera, peningkatan jangka pendek, dan peningkatan di masa depan.

---

## 1. Peningkatan Keamanan (Prioritas: Kritis)

### 1.1 Perbaikan Segera (Selesai)

| Masalah | Berkas Terdampak | Status |
|-------|----------------|--------|
| SECRET_KEY dikodekan secara hardcoded | `05-advanced-prompts/python/aoai-solution.py` | Sudah diperbaiki |
| Validasi env hilang | Beberapa berkas JS/TS | Sudah diperbaiki |
| Pemanggilan fungsi tidak aman | `11-integrating-with-function-calling/js-githubmodels/app.js` | Sudah diperbaiki |
| Kebocoran handle file | `08-building-search-applications/scripts/` | Sudah diperbaiki |
| Timeout permintaan hilang | `09-building-image-applications/python/` | Sudah diperbaiki |

### 1.2 Fitur Keamanan Tambahan yang Direkomendasikan

1. **Contoh Pembatasan Laju**
   - Tambahkan kode contoh yang menunjukkan cara mengimplementasikan pembatasan laju untuk panggilan API
   - Demonstrasikan pola backoff eksponensial

2. **Rotasi Kunci API**
   - Tambahkan dokumentasi tentang praktik terbaik untuk merotasi kunci API
   - Sertakan contoh penggunaan Azure Key Vault atau layanan serupa

3. **Integrasi Keamanan Konten**
   - Tambahkan contoh menggunakan Azure Content Safety API
   - Demonstrasikan pola moderasi input/output

---

## 2. Peningkatan Kualitas Kode

### 2.1 Berkas Konfigurasi Ditambahkan

| Berkas | Tujuan |
|------|---------|
| `.eslintrc.json` | Aturan linting JavaScript/TypeScript |
| `.prettierrc` | Standar format kode |
| `pyproject.toml` | Konfigurasi tooling Python (Black, Ruff, mypy) |

### 2.2 Utilitas Bersama Dibuat

Modul `shared/python/` baru dengan:
- `env_utils.py` - Penanganan variabel lingkungan
- `input_validation.py` - Validasi dan sanitasi input
- `api_utils.py` - Pembungkus permintaan API yang aman

### 2.3 Peningkatan Kode yang Direkomendasikan

1. **Cakupan Penunjuk Tipe**
   - Tambahkan penunjuk tipe ke semua berkas Python
   - Aktifkan mode TypeScript ketat di semua proyek TS

2. **Standar Dokumentasi**
   - Tambahkan docstrings ke semua fungsi Python
   - Tambahkan komentar JSDoc ke semua fungsi JavaScript/TypeScript

3. **Kerangka Pengujian**
   - Tambahkan konfigurasi pytest dan contoh pengujian _(selesai: konfigurasi pytest di `pyproject.toml`; contoh pengujian untuk utilitas bersama di [`tests/`](../../../tests) dijalankan di CI)_
   - Tambahkan konfigurasi Jest untuk JavaScript/TypeScript

---

## 3. Peningkatan Pendidikan

### 3.1 Topik Pelajaran Baru

1. **Keamanan dalam Aplikasi AI** (Pelajaran Usulan 22)
   - Serangan dan pertahanan injeksi prompt
   - Manajemen kunci API
   - Moderasi konten
   - Pembatasan laju dan pencegahan penyalahgunaan

2. **Penempatan Produksi** (Pelajaran Usulan 23)
   - Kontainerisasi dengan Docker
   - Pipeline CI/CD
   - Pemantauan dan pencatatan
   - Manajemen biaya

3. **Teknik RAG Lanjutan** (Pelajaran Usulan 24)
   - Pencarian hybrid (kata kunci + semantik)
   - Strategi peringkat ulang
   - RAG multi-modal
   - Metrik evaluasi

### 3.2 Peningkatan Pelajaran yang Ada

| Pelajaran | Peningkatan yang Direkomendasikan |
|--------|------------------------|
| 06 - Text Generation | Tambahkan contoh respons streaming |
| 07 - Chat Applications | Tambahkan pola memori percakapan |
| 08 - Search Applications | Tambahkan perbandingan database vektor |
| 09 - Image Generation | Tambahkan contoh pengeditan/variasi gambar |
| 11 - Function Calling | Tambahkan pemanggilan fungsi paralel |
| 15 - RAG | Tambahkan perbandingan strategi pemecahan |
| 17 - AI Agents | Tambahkan orkestrasi multi-agent |

---

## 4. Modernisasi API

### 4.1 Pola API yang Dihapus (Migrasi Selesai)

Semua contoh **chat** Python dan TypeScript telah dimigrasikan dari Chat Completions API ke **Responses API** (`client.responses.create(...)` → `response.output_text`).

| Pola Lama | Pola Baru | Status |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Selesai |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Selesai |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | Paket `openai` `client.responses.create()` → `response.output_text` | Selesai |
| `df.append()` (pandas) | `pd.concat()` | Selesai |

> **Catatan:** Contoh Microsoft Foundry Models yang menggunakan SDK `azure-ai-inference` / `@azure-rest/ai-inference` (`client.complete()`) tetap menggunakan Model Inference API, yang tidak mendukung Responses API. `AzureOpenAI()` sengaja dipertahankan di tempat yang masih valid (embedding dan pembuatan gambar).

### 4.2 Fitur API Baru untuk Ditunjukkan

1. **Output Terstruktur** (OpenAI)
   - Mode JSON
   - Pemanggilan fungsi dengan skema ketat

2. **Kemampuan Visi**
   - Analisis gambar dengan GPT-4o (vision)
   - Prompt multi-modal

3. **Alat Bawaan API Responses** (menggantikan Assistants API lama)
   - Interpreter kode
   - Pencarian berkas
   - Pencarian web dan alat kustom

---

## 5. Peningkatan Infrastruktur

### 5.1 Peningkatan CI/CD

Diimplementasikan di [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): linting/formatting Python (Ruff + Black) **ditegakkan** pada modul utilitas `shared/` yang dipelihara dan berjalan **secara advisori** di seluruh kurikulum, plus lintas lintas ESLint untuk JavaScript/TypeScript. Baseline ilustrasi adalah:

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  python-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install ruff black mypy
      - run: ruff check .
      - run: black --check .

  js-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx eslint .
```

### 5.2 Pemindaian Keamanan

Diimplementasikan di [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): Analisis CodeQL untuk Python dan JavaScript/TypeScript (saat push, pull request, dan jadwal mingguan) serta tinjauan dependensi pada pull request. Baseline ilustrasi adalah:

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3

  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
```

---

## 6. Peningkatan Pengalaman Pengembang

### 6.1 Peningkatan DevContainer

Diimplementasikan di [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) dan [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): kontainer sekarang membawa ekstensi Pylance, formatter Black, Ruff, ESLint, Prettier, dan Copilot, mengaktifkan format-on-save yang terhubung ke konfigurasi Black/Prettier repositori, dan menginstal alat pengembang (`ruff`, `black`, `mypy`, `pytest`) sehingga workflow [code-quality](../../../.github/workflows/code-quality.yml) dapat direproduksi secara lokal. Image dasar `mcr.microsoft.com/devcontainers/universal` sudah mengemas Python dan Node, sehingga tidak memerlukan fitur tambahan. Baseline ilustrasi adalah:

```json
{
  "name": "Generative AI for Beginners",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "github.copilot"
      ],
      "settings": {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "pip install -e .[dev] && npm install"
}
```

### 6.2 Playground Interaktif

Pertimbangkan menambahkan:
- Notebook Jupyter dengan kunci API yang sudah diisi sebelumnya (melalui environment)
- Demo Gradio/Streamlit untuk pembelajar visual
- Kuis interaktif untuk penilaian pengetahuan

---

## 7. Dukungan Multi-Bahasa

### 7.1 Cakupan Bahasa Saat Ini

| Teknologi | Pelajaran Dicakup | Status |
|------------|-----------------|--------|
| Python | Semua | Lengkap |
| TypeScript | 06-09, 11 | Sebagian |
| JavaScript | 06-08, 11 | Sebagian |
| .NET/C# | Beberapa | Sebagian |

### 7.2 Penambahan yang Direkomendasikan

1. **Go** - Berkembang dalam tooling AI/ML
2. **Rust** - Aplikasi yang memerlukan performa tinggi
3. **Java/Kotlin** - Aplikasi enterprise

---

## 8. Optimasi Performa

### 8.1 Optimasi Tingkat Kode

1. **Pola Async/Await**
   - Tambahkan contoh async untuk pemrosesan batch
   - Demonstrasikan panggilan API konkuren

2. **Strategi Caching**
   - Tambahkan contoh caching embedding
   - Demonstrasikan pola caching respons

3. **Optimasi Token**
   - Tambahkan contoh penggunaan tiktoken
   - Demonstrasikan teknik kompresi prompt

### 8.2 Contoh Optimasi Biaya

Tambahkan contoh yang menunjukkan:
- Pemilihan model berdasarkan kompleksitas tugas
- Rekayasa prompt untuk efisiensi token
- Pemrosesan batch untuk operasi besar

---

## 9. Aksesibilitas dan Internasionalisasi

### 9.1 Status Terjemahan Saat Ini

Semua terjemahan **selesai** dan dihasilkan secara otomatis oleh [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), yang menghasilkan dan menjaga lebih dari 50 versi bahasa kurikulum agar tetap sinkron dengan sumber bahasa Inggris. Konten terjemahan berada di bawah `translations/` dan gambar lokal di bawah `translated_images/`; daftar lengkap bahasa yang tersedia diterbitkan di bagian atas README repositori.

| Aspek | Status |
|--------|--------|
| Cakupan terjemahan | Lengkap — 50+ bahasa, semua pelajaran |
| Metode terjemahan | Otomatis melalui [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Disinkronkan dengan sumber bahasa Inggris | Ya — dihasilkan ulang secara otomatis |

### 9.2 Peningkatan Aksesibilitas

1. Tambahkan teks alt pada semua gambar
2. Pastikan contoh kode memiliki penyorotan sintaks yang tepat
3. Tambahkan transkrip video untuk semua konten video
4. Pastikan kontras warna memenuhi pedoman WCAG

---

## 10. Prioritas Implementasi

### Fase 1: Segera (Minggu 1-2)
- [x] Perbaiki masalah keamanan kritis
- [x] Tambahkan konfigurasi kualitas kode
- [x] Buat utilitas bersama
- [x] Dokumentasikan pedoman keamanan

### Fase 2: Jangka Pendek (Minggu 3-4)
- [x] Perbarui pola API yang dihentikan (Chat Completions → Responses API, Python + TypeScript)
- [ ] Tambahkan penunjuk tipe ke semua berkas Python (selesai untuk modul `shared/` yang dipelihara; contoh pelajaran dibuat sederhana)
- [x] Tambahkan workflow CI/CD untuk kualitas kode
- [x] Buat workflow pemindaian keamanan

### Fase 3: Jangka Menengah (Bulan 2-3)
- [ ] Tambahkan pelajaran keamanan baru
- [ ] Tambahkan pelajaran penempatan produksi
- [x] Tingkatkan pengaturan DevContainer
- [ ] Tambahkan demo interaktif

### Fase 4: Jangka Panjang (Bulan 4+)
- [ ] Tambahkan pelajaran RAG lanjutan
- [ ] Perluas cakupan bahasa
- [ ] Tambahkan suite pengujian komprehensif
- [ ] Buat program sertifikasi

---

## Kesimpulan

Peta jalan ini memberikan pendekatan terstruktur untuk meningkatkan kurikulum Generative AI for Beginners. Dengan mengatasi masalah keamanan, memodernisasi API, dan menambahkan konten pendidikan, kursus ini akan lebih mempersiapkan siswa untuk pengembangan aplikasi AI di dunia nyata.

Untuk pertanyaan atau kontribusi, silakan buka issue di repositori GitHub.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->