# Peta Jalan Fitur dan Peningkatan yang Ditingkatkan

Dokumen ini menguraikan peningkatan dan perbaikan yang direkomendasikan untuk kurikulum Generative AI for Beginners, berdasarkan tinjauan kode yang komprehensif dan analisis praktik terbaik industri.

## Ringkasan Eksekutif

Basis kode telah dianalisis untuk keamanan, kualitas kode, dan efektivitas pendidikan. Dokumen ini menyediakan rekomendasi untuk perbaikan segera, peningkatan jangka pendek, dan peningkatan di masa depan.

---

## 1. Peningkatan Keamanan (Prioritas: Kritis)

### 1.1 Perbaikan Segera (Selesai)

| Masalah | Berkas Terdampak | Status |
|---------|------------------|--------|
| SECRET_KEY yang dikodekan secara keras | `05-advanced-prompts/python/aoai-solution.py` | Diperbaiki |
| Validasi env yang hilang | Beberapa berkas JS/TS | Diperbaiki |
| Pemanggilan fungsi tidak aman | `11-integrating-with-function-calling/js-githubmodels/app.js` | Diperbaiki |
| Kebocoran penangan berkas | `08-building-search-applications/scripts/` | Diperbaiki |
| Timeout permintaan yang hilang | `09-building-image-applications/python/` | Diperbaiki |

### 1.2 Fitur Keamanan Tambahan yang Direkomendasikan

1. **Contoh Pembatasan Laju**
   - Tambahkan kode contoh yang menunjukkan cara mengimplementasikan pembatasan laju untuk panggilan API
   - Demonstrasikan pola backoff eksponensial

2. **Rotasi API Key**
   - Tambahkan dokumentasi tentang praktik terbaik untuk merotasi API key
   - Sertakan contoh penggunaan Azure Key Vault atau layanan serupa

3. **Integrasi Keamanan Konten**
   - Tambahkan contoh penggunaan Azure Content Safety API
   - Demonstrasikan pola moderasi input/output

---

## 2. Peningkatan Kualitas Kode

### 2.1 Berkas Konfigurasi Ditambahkan

| Berkas | Tujuan |
|--------|---------|
| `.eslintrc.json` | Aturan linting JavaScript/TypeScript |
| `.prettierrc` | Standar format kode |
| `pyproject.toml` | Konfigurasi alat Python (Black, Ruff, mypy) |

### 2.2 Utilitas Bersama Dibuat

Modul `shared/python/` baru dengan:
- `env_utils.py` - Penanganan variabel lingkungan
- `input_validation.py` - Validasi dan sanitasi input
- `api_utils.py` - Pembungkus permintaan API yang aman

### 2.3 Perbaikan Kode yang Direkomendasikan

1. **Cakupan Petunjuk Tipe**
   - Tambahkan petunjuk tipe ke semua berkas Python
   - Aktifkan mode TypeScript ketat di semua proyek TS

2. **Standar Dokumentasi**
   - Tambahkan docstring ke semua fungsi Python
   - Tambahkan komentar JSDoc ke semua fungsi JavaScript/TypeScript

3. **Framework Pengujian**
   - Tambahkan konfigurasi pytest dan contoh pengujian
   - Tambahkan konfigurasi Jest untuk JavaScript/TypeScript

---

## 3. Peningkatan Pendidikan

### 3.1 Topik Pelajaran Baru

1. **Keamanan dalam Aplikasi AI** (Pelajaran 22 yang Diusulkan)
   - Serangan dan pertahanan penyisipan prompt
   - Manajemen API key
   - Moderasi konten
   - Pembatasan laju dan pencegahan penyalahgunaan

2. **Deployment Produksi** (Pelajaran 23 yang Diusulkan)
   - Kontainerisasi dengan Docker
   - Pipeline CI/CD
   - Pemantauan dan pencatatan
   - Manajemen biaya

3. **Teknik RAG Lanjutan** (Pelajaran 24 yang Diusulkan)
   - Pencarian hibrid (kata kunci + semantik)
   - Strategi peringkat ulang
   - RAG multi-modal
   - Metrik evaluasi

### 3.2 Peningkatan Pelajaran yang Ada

| Pelajaran | Peningkatan yang Direkomendasikan |
|-----------|----------------------------------|
| 06 - Text Generation | Tambahkan contoh streaming response |
| 07 - Chat Applications | Tambahkan pola memori percakapan |
| 08 - Search Applications | Tambahkan perbandingan basis data vektor |
| 09 - Image Generation | Tambahkan contoh pengeditan/variasi gambar |
| 11 - Function Calling | Tambahkan pemanggilan fungsi paralel |
| 15 - RAG | Tambahkan perbandingan strategi chunking |
| 17 - AI Agents | Tambahkan orkestrasi multi-agen |

---

## 4. Modernisasi API

### 4.1 Pola API Usang yang Perlu Diperbarui

| Pola Lama | Pola Baru | Berkas Terdampak |
|-----------|-----------|------------------|
| `openai.api_type = "azure"` | Klien `AzureOpenAI()` | Beberapa skrip di `08-building-search-applications/` |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | Beberapa notebook |
| `df.append()` (pandas) | `pd.concat()` | Notebook RAG |

### 4.2 Fitur API Baru yang Perlu Didemonstrasikan

1. **Output Terstruktur** (OpenAI)
   - Mode JSON
   - Pemanggilan fungsi dengan skema ketat

2. **Kemampuan Visio**
   - Analisis gambar dengan GPT-4V
   - Prompt multi-modal

3. **API Asisten**
   - Interpreter kode
   - Pencarian berkas
   - Alat kustom

---

## 5. Peningkatan Infrastruktur

### 5.1 Peningkatan CI/CD

Workflow saat ini menangani validasi markdown. Penambahan yang direkomendasikan:

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

Perbarui `.devcontainer/devcontainer.json`:

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

Pertimbangkan penambahan:
- Notebook Jupyter dengan API key yang sudah terisi (melalui lingkungan)
- Demo Gradio/Streamlit untuk pembelajar visual
- Kuis interaktif untuk penilaian pengetahuan

---

## 7. Dukungan Multi-Bahasa

### 7.1 Cakupan Bahasa Saat Ini

| Teknologi | Pelajaran Tercakup | Status |
|-----------|--------------------|--------|
| Python | Semua | Lengkap |
| TypeScript | 06-09, 11 | Sebagian |
| JavaScript | 06-08, 11 | Sebagian |
| .NET/C# | Beberapa | Sebagian |

### 7.2 Penambahan yang Direkomendasikan

1. **Go** - Berkembang dalam alat AI/ML
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

Tambahkan contoh yang mendemonstrasikan:
- Pemilihan model berdasarkan kompleksitas tugas
- Rekayasa prompt untuk efisiensi token
- Pemrosesan batch untuk operasi masif

---

## 9. Aksesibilitas dan Internasionalisasi

### 9.1 Status Terjemahan Saat Ini

| Bahasa | Status |
|--------|--------|
| Inggris | Lengkap |
| China (Sederhana) | Lengkap |
| Jepang | Lengkap |
| Korea | Lengkap |
| Spanyol | Sebagian |
| Portugis | Sebagian |
| Turki | Sebagian |
| Polandia | Sebagian |

### 9.2 Peningkatan Aksesibilitas

1. Tambahkan teks alternatif ke semua gambar
2. Pastikan contoh kode memiliki highlighting sintaks yang tepat
3. Tambahkan transkrip video untuk semua konten video
4. Pastikan kontras warna memenuhi pedoman WCAG

---

## 10. Prioritas Implementasi

### Fase 1: Segera (Minggu 1-2)
- [x] Perbaiki isu keamanan kritis
- [x] Tambahkan konfigurasi kualitas kode
- [x] Buat utilitas bersama
- [x] Dokumentasikan pedoman keamanan

### Fase 2: Jangka Pendek (Minggu 3-4)
- [ ] Perbarui pola API usang
- [ ] Tambahkan petunjuk tipe ke semua berkas Python
- [ ] Tambahkan workflow CI/CD untuk kualitas kode
- [ ] Buat workflow pemindaian keamanan

### Fase 3: Jangka Menengah (Bulan 2-3)
- [ ] Tambahkan pelajaran keamanan baru
- [ ] Tambahkan pelajaran deployment produksi
- [ ] Perbaiki pengaturan DevContainer
- [ ] Tambahkan demo interaktif

### Fase 4: Jangka Panjang (Bulan 4+)
- [ ] Tambahkan pelajaran RAG lanjutan
- [ ] Perluas cakupan bahasa
- [ ] Tambahkan suite pengujian komprehensif
- [ ] Buat program sertifikasi

---

## Kesimpulan

Peta jalan ini menyediakan pendekatan terstruktur untuk meningkatkan kurikulum Generative AI for Beginners. Dengan menangani masalah keamanan, memodernisasi API, dan menambahkan konten edukasi, kursus ini akan lebih mempersiapkan siswa untuk pengembangan aplikasi AI dunia nyata.

Untuk pertanyaan atau kontribusi, silakan buka isu di repositori GitHub.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk menjaga akurasi, harap diingat bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan jasa penerjemah manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->