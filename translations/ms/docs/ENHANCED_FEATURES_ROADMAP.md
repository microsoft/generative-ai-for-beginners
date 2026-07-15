# Ciri Canggih dan Peta Jalan Penambahbaikan

Dokumen ini menggariskan penambahbaikan dan peningkatan yang disyorkan untuk kurikulum Generative AI for Beginners, berdasarkan ulasan kod menyeluruh dan analisis amalan terbaik industri.

## Ringkasan Eksekutif

Pangkalan kod telah dianalisis dari segi keselamatan, kualiti kod, dan keberkesanan pendidikan. Dokumen ini memberikan cadangan untuk pembaikan segera, penambahbaikan jangka pendek, dan peningkatan masa depan.

---

## 1. Penambahbaikan Keselamatan (Keutamaan: Kritikal)

### 1.1 Pembaikan Segera (Selesai)

| Isu | Fail Terjejas | Status |
|-------|----------------|--------|
| SECRET_KEY yang dikodkan keras | `05-advanced-prompts/python/aoai-solution.py` | Diperbaiki |
| Tiada pengesahan env | Pelbagai fail JS/TS | Diperbaiki |
| Panggilan fungsi tidak selamat | `11-integrating-with-function-calling/js-githubmodels/app.js` | Diperbaiki |
| Kebocoran pemegang fail | `08-building-search-applications/scripts/` | Diperbaiki |
| Tiada had masa permintaan | `09-building-image-applications/python/` | Diperbaiki |

### 1.2 Ciri Keselamatan Tambahan yang Disyorkan

1. **Contoh Had Laju**
   - Tambah kod contoh menunjukkan cara melaksanakan had laju untuk panggilan API
   - Demonstrasi corak pemulaan semula eksponen

2. **Putaran Kunci API**
   - Tambah dokumentasi amalan terbaik untuk putaran kunci API
   - Sertakan contoh menggunakan Azure Key Vault atau perkhidmatan serupa

3. **Integrasi Keselamatan Kandungan**
   - Tambah contoh menggunakan Azure Content Safety API
   - Demonstrasi corak moderasi input/output

---

## 2. Penambahbaikan Kualiti Kod

### 2.1 Fail Konfigurasi Ditambah

| Fail | Tujuan |
|------|---------|
| `.eslintrc.json` | Peraturan lintingan JavaScript/TypeScript |
| `.prettierrc` | Standard format kod |
| `pyproject.toml` | Konfigurasi alatan Python (Black, Ruff, mypy) |

### 2.2 Utiliti Berkongsi Dibuat

Modul baru `shared/python/` dengan:
- `env_utils.py` - Pengendalian pembolehubah persekitaran
- `input_validation.py` - Pengesahan dan sanitasi input
- `api_utils.py` - Pembalut permintaan API yang selamat

### 2.3 Penambahbaikan Kod yang Disyorkan

1. **Liputan Hint Jenis**
   - Tambah hint jenis ke semua fail Python
   - Aktifkan mod TypeScript ketat dalam semua projek TS

2. **Standard Dokumentasi**
   - Tambah docstring ke semua fungsi Python
   - Tambah ulasan JSDoc ke semua fungsi JavaScript/TypeScript

3. **Rangka Kerja Ujian**
   - Tambah konfigurasi pytest dan ujian contoh _(selesai: konfigurasi pytest dalam `pyproject.toml`; ujian contoh untuk utiliti berkongsi dalam [`tests/`](../../../tests) dijalankan dalam CI)_
   - Tambah konfigurasi Jest untuk JavaScript/TypeScript

---

## 3. Penambahbaikan Pendidikan

### 3.1 Topik Pelajaran Baru

1. **Keselamatan dalam Aplikasi AI** (Pelajaran Cadangan 22)
   - Serangan suntikan arahan dan pertahanan
   - Pengurusan kunci API
   - Moderasi kandungan
   - Had laju dan pencegahan penyalahgunaan

2. **Pengeluaran Produksi** (Pelajaran Cadangan 23)
   - Pengkonteineraan dengan Docker
   - Saluran CI/CD
   - Pemantauan dan perekodan log
   - Pengurusan kos

3. **Teknik RAG Lanjutan** (Pelajaran Cadangan 24)
   - Carian hibrid (kata kunci + semantik)
   - Strategi penyusunan semula
   - RAG berbilang modal
   - Metodik penilaian

### 3.2 Penambahbaikan Pelajaran Sedia Ada

| Pelajaran | Penambahbaikan yang Disyorkan |
|--------|------------------------|
| 06 - Penjanaan Teks | Tambah contoh respons penstriman |
| 07 - Aplikasi Sembang | Tambah corak memori perbualan |
| 08 - Aplikasi Carian | Tambah perbandingan pangkalan data vektor |
| 09 - Penjanaan Gambar | Tambah contoh penyuntingan/variasi imej |
| 11 - Panggilan Fungsi | Tambah panggilan fungsi selari |
| 15 - RAG | Tambah perbandingan strategi pemecahan |
| 17 - Ejen AI | Tambah orkestrasi ejen berganda |

---

## 4. Pemodenan API

### 4.1 Corak API Yang Digugurkan (Migrasi Selesai)

Semua contoh **sembang** Python dan TypeScript telah dipindahkan dari Chat Completions API ke **Responses API** (`client.responses.create(...)` → `response.output_text`).

| Corak Lama | Corak Baru | Status |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (sembang) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Selesai |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Selesai |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai` pakej `client.responses.create()` → `response.output_text` | Selesai |
| `df.append()` (pandas) | `pd.concat()` | Selesai |

> **Nota:** Contoh Microsoft Foundry Models yang menggunakan SDK `azure-ai-inference` / `@azure-rest/ai-inference` (`client.complete()`) kekal pada Model Inference API, yang tidak menyokong Responses API. `AzureOpenAI()` sengaja dikekalkan di tempat yang masih sah (embedding dan penjanaan imej).

### 4.2 Ciri API Baru Untuk Demonstrasi

1. **Output Berstruktur** (OpenAI)
   - Mod JSON
   - Panggilan fungsi dengan skema ketat

2. **Keupayaan Visi**
   - Analisis imej dengan GPT-4o (visi)
   - Prompt berbilang modal

3. **Alatan Terbina Dalam Responses API** (menggantikan Assistants API lama)
   - Penterjemah kod
   - Carian fail
   - Carian web dan alatan tersuai

---

## 5. Penambahbaikan Infrastruktur

### 5.1 Penambahbaikan CI/CD

Dilaksanakan dalam [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): linting/formatting Python (Ruff + Black) **dikuatkuasakan** pada modul utiliti `shared/` yang diselenggara dan dijalankan secara **nasihat** merentasi seluruh kurikulum, serta laluan ESLint nasihat untuk JavaScript/TypeScript. Garis dasar ilustrasi adalah:

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

### 5.2 Pengimbasan Keselamatan

Dilaksanakan dalam [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): analisis CodeQL untuk Python dan JavaScript/TypeScript (semasa push, pull request, dan jadual mingguan) serta ulasan kebergantungan pada pull request. Garis dasar ilustrasi adalah:

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

## 6. Penambahbaikan Pengalaman Pembangun

### 6.1 Penambahbaikan DevContainer

Dilaksanakan dalam [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) dan [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): kontena kini membekalkan Pylance, pemformat Black, Ruff, ESLint, Prettier, dan peluasan Copilot, mengaktifkan format-on-save yang dipautkan kepada konfigurasi Black/Prettier repo, dan memasang alatan pembangun (`ruff`, `black`, `mypy`, `pytest`) supaya [alur kerja kualiti kod](../../../.github/workflows/code-quality.yml) dapat dihasilkan semula secara tempatan. Imej asas `mcr.microsoft.com/devcontainers/universal` telah pun membundel Python dan Node, jadi tiada ciri tambahan diperlukan. Garis dasar ilustrasi adalah:

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

### 6.2 Tempat Permainan Interaktif

Pertimbangkan untuk menambah:
- Buku nota Jupyter dengan kunci API telah diisi (melalui persekitaran)
- Demo Gradio/Streamlit untuk pelajar visual
- Kuiz interaktif untuk penilaian pengetahuan

---

## 7. Sokongan Pelbagai Bahasa

### 7.1 Liputan Bahasa Semasa

| Teknologi | Pelajaran Diliputi | Status |
|------------|-----------------|--------|
| Python | Semua | Lengkap |
| TypeScript | 06-09, 11 | Separuh |
| JavaScript | 06-08, 11 | Separuh |
| .NET/C# | Beberapa | Separuh |

### 7.2 Penambahan Disyorkan

1. **Go** - Berkembang dalam alatan AI/ML
2. **Rust** - Aplikasi yang kritikal kepada prestasi
3. **Java/Kotlin** - Aplikasi perusahaan

---

## 8. Pengoptimuman Prestasi

### 8.1 Pengoptimuman Peringkat Kod

1. **Corak Async/Await**
   - Tambah contoh async untuk pemprosesan kelompok
   - Demonstrasi panggilan API serentak

2. **Strategi Caching**
   - Tambah contoh caching embedding
   - Demonstrasi corak caching respons

3. **Pengoptimuman Token**
   - Tambah contoh penggunaan tiktoken
   - Demonstrasi teknik pemampatan prompt

### 8.2 Contoh Pengoptimuman Kos

Tambah contoh menunjukkan:
- Pemilihan model berdasarkan kerumitan tugas
- Kejuruteraan prompt untuk kecekapan token
- Pemprosesan kelompok untuk operasi pukal

---

## 9. Kebolehcapaian dan Pengantarabangsaan

### 9.1 Status Terjemahan Semasa

Semua terjemahan adalah **lengkap** dan dihasilkan secara automatik oleh [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), yang menghasilkan dan mengekalkan lebih 50 versi bahasa kurikulum selari dengan sumber bahasa Inggeris. Kandungan terjemahan berada di bawah `translations/` dan imej diterjemah di bawah `translated_images/`; senarai penuh bahasa yang tersedia diterbitkan di atas README repositori.

| Aspek | Status |
|--------|--------|
| Liputan terjemahan | Lengkap — 50+ bahasa, semua pelajaran |
| Kaedah terjemahan | Automatik melalui [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Disegerakkan dengan sumber Inggeris | Ya — dijana semula secara automatik |

### 9.2 Penambahbaikan Kebolehcapaian

1. Tambah teks alt kepada semua imej
2. Pastikan contoh kod mempunyai penyorotan sintaks yang betul
3. Tambah transkrip video untuk semua kandungan video
4. Pastikan kontras warna memenuhi garis panduan WCAG

---

## 10. Keutamaan Pelaksanaan

### Fasa 1: Segera (Minggu 1-2)
- [x] Betulkan isu keselamatan kritikal
- [x] Tambah konfigurasi kualiti kod
- [x] Buat utiliti berkongsi
- [x] Dokumen panduan keselamatan

### Fasa 2: Jangka Pendek (Minggu 3-4)
- [x] Kemas kini corak API yang digugurkan (Chat Completions → Responses API, Python + TypeScript)
- [ ] Tambah hint jenis ke semua fail Python (selesai untuk modul `shared/` yang diselenggara; contoh pelajaran dikekalkan mudah)
- [x] Tambah alur kerja CI/CD untuk kualiti kod
- [x] Buat alur kerja imbasan keselamatan

### Fasa 3: Jangka Sederhana (Bulan 2-3)
- [ ] Tambah pelajaran keselamatan baru
- [ ] Tambah pelajaran pengeluaran produksi
- [x] Perbaiki persediaan DevContainer
- [ ] Tambah demo interaktif

### Fasa 4: Jangka Panjang (Bulan 4+)
- [ ] Tambah pelajaran RAG lanjutan
- [ ] Kembangkan liputan bahasa
- [ ] Tambah suite ujian menyeluruh
- [ ] Buat program pensijilan

---

## Kesimpulan

Peta jalan ini menyediakan pendekatan berstruktur untuk memperbaiki kurikulum Generative AI for Beginners. Dengan menangani kebimbangan keselamatan, memodenkan API, dan menambah kandungan pendidikan, kursus ini akan menyediakan pelajar dengan lebih baik untuk pembangunan aplikasi AI dunia sebenar.

Untuk sebarang pertanyaan atau sumbangan, sila buka isu di repositori GitHub.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->