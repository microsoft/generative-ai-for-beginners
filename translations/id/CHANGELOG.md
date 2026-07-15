# Changelog

Semua perubahan penting pada kurikulum Generative AI untuk Pemula didokumentasikan dalam file ini.

Format ini didasarkan pada [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Karena ini adalah
kurikulum pembelajaran, bukan paket perangkat lunak versi tertentu, entri dikelompokkan berdasarkan tanggal.

## [2026-07-06] — Penyegaran Modernisasi Konten

Penyegaran luas untuk menjaga kurikulum tetap akurat untuk tahun 2026: API modern, nama produk dan
model terkini, panduan penyedia terbaru, dan alat baru untuk pengalaman pengembang.

### Ditambahkan

- **Bagian Microsoft Agent Framework** di pelajaran `17-ai-agents` yang mencakup agen obrolan tunggal,
  pemanggilan alat/fungsi, konfigurasi Azure OpenAI (Microsoft Foundry), dan orkestrasi alur kerja multi-agen
  (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** didokumentasikan sebagai penyedia offline / di perangkat (bersama Ollama) di
  `00-course-setup/03-providers.md` dan pelajaran `19-slm`.
- **Alur kerja integrasi berkelanjutan**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (diberlakukan pada modul `shared/` yang dipelihara,
    saran pada seluruh kurikulum), lintasan ESLint sebagai saran, dan pekerjaan pytest.
  - `.github/workflows/security.yml` — Analisis CodeQL (Python + JavaScript/TypeScript) dan
    ulasan dependensi pada pull request.
- **Suite pengujian** di `tests/` — 41 pengujian pytest yang mencakup modul utilitas bersama.
- **Keahlian migrasi Azure OpenAI → Responses API** di
  `.github/skills/azure-openai-to-responses/` yang digunakan untuk memandu migrasi API.

### Diubah

- **Chat Completions API → Responses API** di semua contoh obrolan Python dan TypeScript
  (`client.responses.create(...)` → `response.output_text`), termasuk pelajaran 04, 06, 07, 11,
  15, dan 18, plus README mereka.
- **Model GitHub → Model Microsoft Foundry** di seluruh prosa, tautan, dan contoh. Model GitHub
  dihentikan pada akhir Juli 2026; contoh sekarang merujuk ke katalog model Microsoft Foundry dan menggunakan
  variabel lingkungan `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md`, dan dokumen penyedia** diperbarui untuk mencerminkan bahwa Azure OpenAI sekarang merupakan bagian
  dari Microsoft Foundry, dan versi API default ditingkatkan ke `2024-10-21`.
- **Contoh TypeScript** (pelajaran 06, 07, 08, 11) bermigrasi dari SDK beta `@azure/openai`
  ke paket `openai` (aplikasi obrolan menggunakan Responses API; aplikasi pencarian menggunakan
  klien embeddings).
- **Notebook .NET** (`dotnet/*.dib`) distandarisasi pada `Azure.AI.OpenAI` **2.1.0**: pelajaran 06 dan 07
  menggunakan API `ChatClient`, pelajaran 08 menggunakan `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), dan
  pelajaran 09 menggunakan `ImageClient` (`GenerateImage`) dengan `gpt-image-1`, menggantikan paket lama
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` dari `1.0.0-beta.9`.
- **Modernisasi nama produk**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (pelajaran 14, 16, 17) dan "Bing" → **Microsoft Copilot** (pelajaran 12), jika merujuk ke
  produk saat ini.
- **DevContainer** (`.devcontainer/`) sekarang menyertakan ekstensi Pylance, Black, Ruff, ESLint, Prettier, dan Copilot,
  mengaktifkan format saat simpan, dan menginstal `ruff`, `black`, `mypy`, dan `pytest` agar pemeriksaan CI
  dapat direproduksi secara lokal.
- **Generasi gambar** (pelajaran 09) merekomendasikan `gpt-image-1` untuk Azure (katalog Azure menghentikan
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** diperbarui untuk mencerminkan pekerjaan yang telah selesai (migrasi API, CI,
  DevContainer, pengujian) dan fakta saat ini (terjemahan diproduksi otomatis oleh
  Azure Co-op Translator; API Assistants digantikan oleh Responses API).

### Diperbaiki

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` sekarang mengembalikan
  string kosong untuk input hanya spasi daripada memunculkan error "terlalu pendek" (konsisten dengan
  kasus `None`). Ditemukan dan dilindungi oleh suite pengujian baru.
- **Contoh gambar pelajaran 09** — memperbaiki bug nyata: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  dan variabel yang menimpa modul `openai`.
- **Notebook RAG pelajaran 15** — memperbaiki pengaturan klien, mengganti `DataFrame.append`
  yang dihapus dengan `pd.concat`, dan memodernisasi penggunaan SDK lama.
- Nama model yang usang / dihentikan (`gpt-3.5-turbo`, `gpt-35-turbo`) diganti dengan `gpt-4o-mini`
  di contoh aktif; hasil fine-tuning historis di pelajaran 18 dipertahankan dan diberi catatan
  daripada ditulis ulang.

### Kadaluarsa / Catatan

- Contoh Model Microsoft Foundry yang menggunakan SDK `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — contoh `githubmodels-*` dan `js-githubmodels` serta pelajaran 19, 20,
  dan 21 — tetap menggunakan Model Inference API, yang **tidak** mendukung Responses API. Ini
  sengaja dibiarkan menggunakan SDK tersebut.
- `AzureOpenAI()` sengaja dipertahankan jika masih sesuai (embedding dan generasi gambar),
  karena alur kerja tersebut bukan bagian dari migrasi Responses API.
- Referensi `text-embedding-ada-002` dipertahankan jika indeks embedding yang dihitung sebelumnya bergantung padanya.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->