# Changelog

Semua perubahan penting pada kurikulum Generative AI untuk Pemula didokumentasikan dalam file ini.

Format ini didasarkan pada [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Karena ini adalah
kurikulum pembelajaran, bukan paket perangkat lunak yang versi, entri dikelompokkan berdasarkan tanggal.

## [2026-07-16] — Validasi Konten + Aset Gambar Pelajaran 09

### Diubah

- **Pelajaran 10 (aplikasi AI low-code):** memperbarui dua tautan `docs.microsoft.com/powerapps/...` Dataverse
  yang sudah tidak berlaku menjadi tautan `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  yang terbaru (telah diverifikasi secara langsung).
- **Pelajaran 17 (agen AI):** memodernisasi contoh model yang sudah usang (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, dan Llama 3.3`) dan nama deployment placeholder dalam contoh Framework Agen
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Root `README.md`:** menambahkan ID pelacakan `?WT.mc_id=academic-105485-koreyst` yang hilang pada tautan
  *Microsoft for Startups*.
- **Aset gambar Pelajaran 09** dibuat ulang dengan model `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, dan
  `images/startup.png` (pasangan contoh editing sebelum/sesudah dibuat melalui panggilan asli
  `client.images.edit` dengan masker yang dihasilkan).

### Diverifikasi

- Mengaudit README untuk pelajaran 01, 03, 05, 12, 14, dan 16 — semuanya terbaru (nama dan tautan Microsoft Foundry
  yang benar); tidak ada perubahan yang diperlukan.
- Melakukan validasi markdown penuh pada semua 41 berkas markdown dalam repositori (kecuali terjemahan) untuk
  jalur dokumen yang usang, lokal Microsoft `/en-us/`, nama produk/model yang ketinggalan zaman, ID pelacakan yang hilang,
  dan tautan/gambar relatif yang rusak. Hanya celah ID pelacakan *Microsoft for Startups* yang
  dapat ditindaklanjuti; semua tanda lainnya dikonfirmasi sebagai positif palsu (tautan terjemahan yang dihasilkan otomatis,
  placeholder yang dikomentari, dan URL struktural pihak ketiga `/en/`).

## [2026-07-15] — Penulisan Ulang Pelajaran 09 (Aplikasi Gambar) untuk Model Gambar GPT

### Diubah

- **Menulis ulang pelajaran 09 "Membangun Aplikasi Pembuatan Gambar"** berdasarkan keluarga model **`gpt-image`**
  yang sekarang (default **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` juga GA), menggantikan
  konten lama DALL·E 2/3. Koreksi utama:
  - Model `gpt-image` mengembalikan gambar sebagai **base64 (`b64_json`)**, bukan URL. Memperbarui semua contoh agar
    menggunakan `base64.b64decode(...)` daripada mengunduh `url` dengan `requests`.
  - Menaikkan versi API gambar menjadi `2025-04-01-preview`.
  - Mengganti bagian "temperature" yang dibuat-buat (model gambar tidak menggunakan `temperature`) dan
    konten **variations** gambar khusus DALL·E-2 dengan bagian **pengeditan gambar** (masker/inpainting).
  - Memperbarui `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, keduanya
    notebook tugas (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), dan notebook .NET `.dib`.

### Dihapus

- Menghapus contoh usang `python/aoai-app-variation.py` dan `python/oai-app-variation.py`
  (`images.create_variation` hanya untuk DALL·E-2 dan tidak didukung oleh `gpt-image`).
- Menghapus 4 aset gambar yang tidak terpakai terkait dengan bagian perbandingan temperature yang dihapus
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Menghilangkan ketergantungan `requests` yang tidak perlu dari contoh Python dan kebutuhan pelajaran.

### Divalidasi

- Menjalankan `aoai-app.py` dari awal hingga akhir terhadap model `gpt-image-1.5` yang telah diterapkan dan memastikan alur decode/save base64 menghasilkan PNG. Notebook dikonfirmasi sebagai JSON yang valid.


## [2026-07-14] — Pembaruan Model Default + Panduan Model Penalaran

### Diubah

- **Model chat default `gpt-4o-mini` → `gpt-5-mini`** di seluruh contoh yang dapat dijalankan dalam kurikulum,
  dokumentasi, dan konfigurasi. Hal ini didorong oleh status siklus hidup model: di Microsoft Foundry,
  `gpt-4o-mini` (pensiun 2026-10-01) dan seluruh keluarga `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, pensiun 2026-10-14) sedang **Dihapus**, sedangkan keluarga **GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) adalah Tersedia Secara Umum** (pensiun 2027-02-06). Diperbarui:
  - `.env.copy`, `00-course-setup/03-providers.md` (rekomendasi penerapan dan perintah deploy `az cognitiveservices`),
    dan README untuk pelajaran 04, 06, 07, dan 15.
  - Contoh Python di pelajaran 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) dan skrip pelajaran 08.
  - Contoh TypeScript / JavaScript di pelajaran 06, 07, dan 11, serta notebook .NET `.dib` untuk
    pelajaran 06 dan 07.
  - Notebook tugas di pelajaran 04, 06, 07, dan 11 (sel kode), juga contoh docstring `shared/python/api_utils.py`.
    
- **Panduan parameter model-penalaran (baru).** `gpt-5-mini` adalah model *penalaran*: ia **tidak**
  mendukung `temperature`/`top_p`, dan menggunakan `max_completion_tokens` (chat completions) /
  `max_output_tokens` (Responses API) menggantikan `max_tokens`. Oleh karena itu:
  - Dihapus `temperature`/`top_p`/`max_tokens` dari sampel yang kini menggunakan default `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, lesson 15 RAG README).
  - Ditambahkan catatan **"Model penalaran tidak menggunakan `temperature`"** pada pelajaran 06, menjelaskan bahwa
    model penalaran dikendalikan dengan **rekayasa prompt + kontrol penalaran** daripada
    kenop sampling, sementara `temperature`/`top_p` tetap berlaku pada model non-penalaran
    (GPT-4.x, Mistral, Llama, Phi, model terbuka).
- **`gpt-5-mini` tidak digunakan untuk tutorial fine-tuning (pelajaran 18).** GPT-5 hanya mendukung
  fine-tuning penguatan (RFT); pelajaran 18 untuk fine-tuning supervisi (SFT) tetap menggunakan
  `gpt-4.1-mini`, yang mendukung SFT/DPO.
- **Demo Temperature menggunakan model Llama.** Untuk tetap mengajarkan `temperature` (yang ditolak oleh model penalaran),
  digunakan model `Llama-3.3-70B-Instruct` melalui endpoint Foundry Models. Ditambahkan variabel baru
  `AZURE_INFERENCE_CHAT_MODEL` ke `.env.copy`; notebook `githubmodels` pelajaran 04/06 dan sampel
  `06` `js-githubmodels` membacanya (fallback ke `Llama-3.3-70B-Instruct`) dan mempertahankan demo
  `temperature`/`top_p`/`max_tokens`.
- **Sampel JS / .NET diperbarui untuk GPT-5.** Dihapus `temperature`/`top_p`/`max_tokens` dari sampel GPT-5
  (`06` aplikasi resep TypeScript, `06` `.dib` .NET - yang juga menaikkan `MaxOutputTokenCount`
  agar output penalaran tidak terpotong). Sampel `06` `js-githubmodels` kini menggunakan Llama untuk mempertahankan demo temperature-nya.
  `.dib` mencatat bahwa `Azure.AI.Inference` + model Llama adalah cara untuk
  mendemonstrasikan `Temperature` di .NET.
- Biarkan `gpt-4o-mini` / `gpt-5-mini` di tempat yang masih akurat: referensi encoding token `tiktoken`,
  daftar ketersediaan katalog model, dan model ucapan pelajaran 02 (`gpt-4o-transcribe`).
- Sampel pelajaran 20 (Mistral) dan 21 (Meta) mempertahankan `temperature`/`max_tokens` karena mereka menargetkan
  model Mistral/Llama, yang mendukung parameter tersebut.

## [2026-07-06] — Penyegaran Modernisasi Konten

Penyegaran luas untuk menjaga kurikulum akurat pada 2026: API modern, nama produk dan
model terkini, panduan penyedia yang diperbarui, dan alat pengalaman pengembang baru.

### Ditambahkan

- Bagian **Microsoft Agent Framework** di pelajaran `17-ai-agents` yang membahas agen chat tunggal,
  pemanggilan alat/fungsi, konfigurasi Azure OpenAI (Microsoft Foundry), dan orkestrasi
  alur kerja multi-agen (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** didokumentasikan sebagai penyedia offline / di perangkat (bersama Ollama) di
  `00-course-setup/03-providers.md` dan pelajaran `19-slm`.
- **Alur kerja continuous integration**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (ditegakkan pada modul `shared/` yang dipelihara,
    advisori di sisa kurikulum), pemeriksaan ESLint, dan job pytest.
  - `.github/workflows/security.yml` — analisis CodeQL (Python + JavaScript/TypeScript) dan
    tinjauan dependensi pada pull request.
- **Suite pengujian** di bawah `tests/` — 41 pengujian pytest yang meliputi modul utilitas bersama.
- **Kemampuan migrasi Azure OpenAI → Responses API** di
  `.github/skills/azure-openai-to-responses/` yang digunakan untuk memandu migrasi API.

### Diubah

- **Chat Completions API → Responses API** di semua sampel chat Python dan TypeScript
  (`client.responses.create(...)` → `response.output_text`), termasuk pelajaran 04, 06, 07, 11,
  15, dan 18, plus README mereka.
- **GitHub Models → Microsoft Foundry Models** di seluruh prose, tautan, dan sampel. GitHub Models
  dihentikan akhir Juli 2026; sampel kini mengarah ke katalog model Microsoft Foundry dan menggunakan
  variabel lingkungan `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md`, dan dokumen penyedia** diperbarui untuk mencerminkan bahwa Azure OpenAI kini bagian
  dari Microsoft Foundry, dan versi API default dinaikkan ke `2024-10-21`.
- **Sampel TypeScript** (pelajaran 06, 07, 08, 11) bermigrasi dari SDK beta `@azure/openai`
  yang usang ke paket `openai` (aplikasi chat memakai Responses API; aplikasi pencarian menggunakan
  klien embeddings).
- **Notebook .NET** (`dotnet/*.dib`) distandarisasi pada `Azure.AI.OpenAI` **2.1.0**: pelajaran 06 dan 07
  menggunakan API `ChatClient`, pelajaran 08 menggunakan `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), dan
  pelajaran 09 menggunakan `ImageClient` (`GenerateImage`) dengan `gpt-image-1`, menggantikan
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` lama dari `1.0.0-beta.9`.
- **Modernisasi nama produk**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (pelajaran 14, 16, 17) dan "Bing" → **Microsoft Copilot** (pelajaran 12), dimana itu merujuk
  produk saat ini.
- **DevContainer** (`.devcontainer/`) kini menyertakan ekstensi Pylance, Black, Ruff, ESLint, Prettier,
  dan Copilot, mengaktifkan format saat simpan, serta menginstal `ruff`, `black`, `mypy`, dan `pytest`
  agar pemeriksaan CI dapat direproduksi secara lokal.
- **Generasi gambar** (pelajaran 09) merekomendasikan `gpt-image-1` untuk Azure (katalog Azure menghapus
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** diperbarui untuk mencerminkan pekerjaan yang telah selesai (migrasi API, CI,
  DevContainer, pengujian) dan fakta terkini (terjemahan diproduksi secara otomatis oleh
  Azure Co-op Translator; API Assistants telah digantikan oleh API Responses).

### Diperbaiki

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` sekarang mengembalikan
  string kosong untuk input yang hanya berisi spasi daripada mengeluarkan kesalahan "terlalu pendek" (konsisten dengan kasus
  `None`). Ditemukan dan dijaga oleh rangkaian pengujian baru.
- **Contoh gambar Lesson 09** — memperbaiki bug nyata: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  dan sebuah variabel yang menimpa modul `openai`.
- **Notebook Lesson 15 RAG** — memperbaiki pengaturan klien, menggantikan `DataFrame.append` yang dihapus
  dengan `pd.concat`, dan memodernisasi penggunaan SDK lama.
- Nama model yang sudah kedaluwarsa / pensiun (`gpt-3.5-turbo`, `gpt-35-turbo`) diganti dengan `gpt-4o-mini`
  pada contoh aktif; keluaran fine-tuning historis di lesson 18 dipertahankan dan diberi anotasi
  daripada ditulis ulang.

### Kadaluwarsa / Catatan

- **Contoh Microsoft Foundry Models** yang menggunakan `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — contoh `githubmodels-*` dan `js-githubmodels` dan lesson 19, 20,
  serta 21 — tetap menggunakan Model Inference API, yang **tidak** mendukung Responses API. Contoh ini
  sengaja dibiarkan pada SDK tersebut.
- `AzureOpenAI()` sengaja dipertahankan jika masih sesuai (embedding dan pembuatan gambar),
  karena alur kerja tersebut bukan bagian dari migrasi Responses API.
- Referensi `text-embedding-ada-002` dipertahankan di mana indeks embedding yang sudah dihitung sebelumnya bergantung pada mereka.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->