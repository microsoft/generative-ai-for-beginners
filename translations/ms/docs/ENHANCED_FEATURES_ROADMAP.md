# Peta Jalan Ciri dan Penambahbaikan Dipertingkatkan

Dokumen ini menggariskan penambahbaikan dan peningkatan yang disyorkan untuk kurikulum Generative AI untuk Pemula, berdasarkan ulasan kod yang menyeluruh dan analisis amalan terbaik industri.

## Ringkasan Eksekutif

Pangkalan kod telah dianalisis dari segi keselamatan, kualiti kod, dan keberkesanan pendidikan. Dokumen ini menyediakan cadangan untuk pembaikan segera, penambahbaikan jangka dekat, dan penambahbaikan masa depan.

---

## 1. Penambahbaikan Keselamatan (Keutamaan: Kritikal)

### 1.1 Pembaikan Segera (Selesai)

| Isu | Fail Terjejas | Status |
|-------|----------------|--------|
| SECRET_KEY yang dikod keras | `05-advanced-prompts/python/aoai-solution.py` | Diperbaiki |
| Kekurangan pengesahan env | Pelbagai fail JS/TS | Diperbaiki |
| Panggilan fungsi tidak selamat | `11-integrating-with-function-calling/js-githubmodels/app.js` | Diperbaiki |
| Kebocoran pemegang fail | `08-building-search-applications/scripts/` | Diperbaiki |
| Kekurangan timeout permintaan | `09-building-image-applications/python/` | Diperbaiki |

### 1.2 Ciri Keselamatan Tambahan Disyorkan

1. **Contoh Hadkan Kadar**
   - Tambah kod contoh menunjukkan cara melaksanakan had kadar untuk panggilan API
   - Tunjukkan corak backoff eksponen

2. **Pusingan Kunci API**
   - Tambah dokumentasi amalan terbaik untuk memusingkan kunci API
   - Sertakan contoh menggunakan Azure Key Vault atau perkhidmatan serupa

3. **Integrasi Keselamatan Kandungan**
   - Tambah contoh menggunakan Azure Content Safety API
   - Tunjukkan corak moderasi input/output

---

## 2. Penambahbaikan Kualiti Kod

### 2.1 Fail Konfigurasi Ditambah

| Fail | Tujuan |
|------|---------|
| `.eslintrc.json` | Peraturan linting JavaScript/TypeScript |
| `.prettierrc` | Standard pemformatan kod |
| `pyproject.toml` | Konfigurasi alat Python (Black, Ruff, mypy) |

### 2.2 Utiliti Berkongsi Dibuat

Modul `shared/python/` baru dengan:
- `env_utils.py` - Pengendalian pemboleh ubah persekitaran
- `input_validation.py` - Pengesahan dan sanitasi input
- `api_utils.py` - Pembalut permintaan API yang selamat

### 2.3 Penambahbaikan Kod Disyorkan

1. **Liputan Petunjuk Jenis**
   - Tambah petunjuk jenis ke semua fail Python
   - Aktifkan mod strict TypeScript dalam semua projek TS

2. **Standard Dokumentasi**
   - Tambah docstrings ke semua fungsi Python
   - Tambah komen JSDoc ke semua fungsi JavaScript/TypeScript

3. **Rangka Kerja Ujian**
   - Tambah konfigurasi pytest dan ujian contoh
   - Tambah konfigurasi Jest untuk JavaScript/TypeScript

---

## 3. Penambahbaikan Pendidikan

### 3.1 Topik Pelajaran Baru

1. **Keselamatan dalam Aplikasi AI** (Cadangan Pelajaran 22)
   - Serangan dan pertahanan suntikan prompt
   - Pengurusan kunci API
   - Moderasi kandungan
   - Hadkan kadar dan pencegahan penyalahgunaan

2. **Pengeluaran Pengeluaran** (Cadangan Pelajaran 23)
   - Penggunaan kontena dengan Docker
   - Saluran CI/CD
   - Pemantauan dan log
   - Pengurusan kos

3. **Teknik RAG Lanjutan** (Cadangan Pelajaran 24)
   - Carian hibrid (kata kunci + semantik)
   - Strategi pengimbangan semula
   - RAG pelbagai mod
   - Metod evaluasi

### 3.2 Penambahbaikan Pelajaran Sedia Ada

| Pelajaran | Penambahbaikan Disyorkan |
|--------|------------------------|
| 06 - Penjanaan Teks | Tambah contoh respons streaming |
| 07 - Aplikasi Sembang | Tambah corak memori perbualan |
| 08 - Aplikasi Carian | Tambah perbandingan pangkalan data vektor |
| 09 - Penjanaan Imej | Tambah contoh penyuntingan/variasi imej |
| 11 - Panggilan Fungsi | Tambah panggilan fungsi selari |
| 15 - RAG | Tambah perbandingan strategi pemecahan |
| 17 - Ejen AI | Tambah orkestrasi multi-ejen |

---

## 4. Pemodenan API

### 4.1 Corak API Usang yang Perlu Dikemas Kini

| Corak Lama | Corak Baru | Fail Terjejas |
|-------------|-------------|----------------|
| `openai.api_type = "azure"` | Klien `AzureOpenAI()` | Pelbagai skrip dalam `08-building-search-applications/` |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | Pelbagai buku nota |
| `df.append()` (pandas) | `pd.concat()` | Buku nota RAG |

### 4.2 Ciri API Baru untuk Ditunjukkan

1. **Output Berstruktur** (OpenAI)
   - Mod JSON
   - Panggilan fungsi dengan skema ketat

2. **Kebolehan Visi**
   - Analisis imej dengan GPT-4V
   - Prompt pelbagai mod

3. **API Pembantu**
   - Interpreter kod
   - Carian fail
   - Alat khusus

---

## 5. Penambahbaikan Infrastruktur

### 5.1 Penambahbaikan CI/CD

Aliran kerja semasa mengendalikan pengesahan markdown. Tambahan disyorkan:

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

Kemas kini `.devcontainer/devcontainer.json`:

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

Pertimbangkan untuk menambah:
- Nota Jupyter dengan kunci API yang telah diisi (melalui persekitaran)
- Demo Gradio/Streamlit untuk pelajar visual
- Kuiz interaktif untuk penilaian pengetahuan

---

## 7. Sokongan Pelbagai Bahasa

### 7.1 Liputan Bahasa Semasa

| Teknologi | Pelajaran Diliputi | Status |
|------------|-----------------|--------|
| Python | Semua | Lengkap |
| TypeScript | 06-09, 11 | Sebahagian |
| JavaScript | 06-08, 11 | Sebahagian |
| .NET/C# | Beberapa | Sebahagian |

### 7.2 Tambahan Disyorkan

1. **Go** - Berkembang dalam alat AI/ML
2. **Rust** - Aplikasi kritikal prestasi
3. **Java/Kotlin** - Aplikasi enterprise

---

## 8. Pengoptimalan Prestasi

### 8.1 Pengoptimalan Tahap Kod

1. **Corak Async/Await**
   - Tambah contoh async untuk pemprosesan kelompok
   - Tunjukkan panggilan API serentak

2. **Strategi Caching**
   - Tambah contoh caching embedding
   - Tunjukkan corak caching respons

3. **Pengoptimuman Token**
   - Tambah contoh penggunaan tiktoken
   - Tunjukkan teknik pemampatan prompt

### 8.2 Contoh Pengoptimuman Kos

Tambah contoh menunjukkan:
- Pemilihan model berdasarkan kerumitan tugas
- Kejuruteraan prompt untuk kecekapan token
- Pemprosesan kelompok untuk operasi pukal

---

## 9. Kebolehcapaian dan Internasionalisasi

### 9.1 Status Terjemahan Semasa

| Bahasa | Status |
|----------|--------|
| Inggeris | Lengkap |
| Cina (Ringkas) | Lengkap |
| Jepun | Lengkap |
| Korea | Lengkap |
| Sepanyol | Sebahagian |
| Portugis | Sebahagian |
| Turki | Sebahagian |
| Poland | Sebahagian |

### 9.2 Penambahbaikan Kebolehcapaian

1. Tambah teks alt ke semua imej
2. Pastikan contoh kod mempunyai penyorotan sintaks yang betul
3. Tambah transkrip video untuk semua kandungan video
4. Pastikan kontras warna memenuhi garis panduan WCAG

---

## 10. Keutamaan Pelaksanaan

### Fasa 1: Segera (Minggu 1-2)
- [x] Betulkan isu keselamatan kritikal
- [x] Tambah konfigurasi kualiti kod
- [x] Cipta utiliti berkongsi
- [x] Dokumentasikan garis panduan keselamatan

### Fasa 2: Jangka Pendek (Minggu 3-4)
- [ ] Kemas kini corak API usang
- [ ] Tambah petunjuk jenis ke semua fail Python
- [ ] Tambah aliran kerja CI/CD untuk kualiti kod
- [ ] Cipta aliran kerja pengimbasan keselamatan

### Fasa 3: Jangka Sederhana (Bulan 2-3)
- [ ] Tambah pelajaran keselamatan baru
- [ ] Tambah pelajaran pengeluaran pengeluaran
- [ ] Tingkatkan persediaan DevContainer
- [ ] Tambah demo interaktif

### Fasa 4: Jangka Panjang (Bulan 4+)
- [ ] Tambah pelajaran RAG lanjutan
- [ ] Kembangkan liputan bahasa
- [ ] Tambah suite ujian menyeluruh
- [ ] Cipta program pensijilan

---

## Kesimpulan

Peta jalan ini menyediakan pendekatan berstruktur untuk memperbaiki kurikulum Generative AI untuk Pemula. Dengan menangani kebimbangan keselamatan, memodenkan API, dan menambah kandungan pendidikan, kursus ini akan lebih baik menyediakan pelajar untuk pembangunan aplikasi AI dunia sebenar.

Untuk sebarang pertanyaan atau penyumbangan, sila buka isu di repositori GitHub.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi ralat atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber rujukan yang sah. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau penafsiran yang salah yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->