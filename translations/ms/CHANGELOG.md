# Perubahan

Semua perubahan penting kepada kurikulum AI Generatif untuk Pemula didokumentasikan dalam fail ini.

Format ini berdasarkan pada [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Oleh kerana ini adalah
kurikulum pembelajaran dan bukannya pakej perisian berpenversion, entri disusun mengikut tarikh.

## [2026-07-16] — Pengesahan Kandungan + Aset Imej Pelajaran 09

### Diubah

- **Pelajaran 10 (aplikasi AI kod rendah):** dikemas kini dua pautan Dataverse `docs.microsoft.com/powerapps/...` yang sudah tidak digunakan
  ke `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro` yang terkini
  (disahkan secara langsung).
- **Pelajaran 17 (agen AI):** memodenkan contoh model lama (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, dan Llama 3.3`) dan nama pelantar simpanan sementara dalam sampel Rangka Kerja Agen
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Root `README.md`:** menambah ID penjejakan `?WT.mc_id=academic-105485-koreyst` yang hilang pada pautan
  *Microsoft for Startups*.
- **Aset imej Pelajaran 09** dijana semula dengan model `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, dan
  `images/startup.png` (pasangan contoh suntingan sebelum/selepas dibuat melalui panggilan nyata
  `client.images.edit` dengan topeng yang dijana).

### Disahkan

- Telah mengaudit README bagi pelajaran 01, 03, 05, 12, 14, dan 16 — semua terkini (penamaan Microsoft Foundry yang betul
  dan pautan); tiada perubahan diperlukan.
- Menjalankan pengesahan markdown penuh ke atas kesemua 41 fail markdown dalam repo (terjemahan tidak termasuk) untuk
  laluan dokumen yang sudah lapuk, lokasi Microsoft `/en-us/`, nama produk/model yang ketinggalan zaman, ID penjejakan yang hilang,
  dan pautan/gambar relatif yang rosak. Hanya jurang ID penjejakan pada *Microsoft for Startups* yang boleh ditindaklanjuti;
  semua bendera lain disahkan sebagai positif palsu (pautan terjemahan auto-jana,
  tempat letak komen, dan URL struktur pihak ketiga `/en/`).

## [2026-07-15] — Penulisan Semula Pelajaran 09 (Aplikasi Imej) untuk Model Imej GPT

### Diubah

- **Menulis semula pelajaran 09 "Membina Aplikasi Penjanaan Imej"** sekitar keluarga model **`gpt-image`**
  terkini (default **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` juga GA), menggantikan
  kandungan lama DALL·E 2/3. Pembetulan utama:
  - Model `gpt-image` mengembalikan imej sebagai **base64 (`b64_json`)**, bukan URL. Mengemas kini semua contoh kepada
    `base64.b64decode(...)` dan bukannya memuat turun `url` dengan `requests`.
  - Menaik taraf versi API imej ke `2025-04-01-preview`.
  - Menggantikan bahagian "temperature" yang direka (model imej tidak mengambil `temperature`) dan kandungan
    **variasi** imej eksklusif DALL·E-2 dengan bahagian **penyuntingan imej** (mask/penghinapan).
  - Mengemas kini `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, kedua-dua
    buku nota tugasan (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), dan buku nota .NET `.dib`.

### Dibuang

- Memadam contoh `python/aoai-app-variation.py` dan `python/oai-app-variation.py` yang sudah lapuk
  (`images.create_variation` hanya untuk DALL·E-2 dan tidak disokong oleh `gpt-image`).
- Memadamkan 4 aset imej yatim yang berkaitan dengan bahagian perbandingan suhu yang dibuang
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Mengeluarkan kebergantungan `requests` yang tidak perlu daripada contoh Python dan keperluan pelajaran.

### Disahkan

- Menjalankan `aoai-app.py` dari mula hingga akhir dengan model `gpt-image-1.5` yang dipasang dan mengesahkan aliran
  dekod/simpan base64 menghasilkan PNG. Buku nota disahkan sebagai JSON sah.

## [2026-07-14] — Kemas Kini Model Lalai + Panduan Model Penalaran

### Diubah

- **Model sembang lalai `gpt-4o-mini` → `gpt-5-mini`** merentasi contoh berjalan dalam kurikulum,
  dokumen, dan konfigurasi. Ini didorong oleh status kitar hayat model: di Microsoft Foundry,
  `gpt-4o-mini` (bersara pada 2026-10-01) dan seluruh keluarga `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, bersara pada 2026-10-14) adalah **Sedang Dihentikan**, manakala keluarga **GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) adalah Secara Amnya Tersedia** (bersara pada 2027-02-06). Dikemaskini:
  - `.env.copy`, `00-course-setup/03-providers.md` (cadangan pengeluaran dan perintah `az cognitiveservices`
    deploy), dan README bagi pelajaran 04, 06, 07, dan 15.
  - Contoh Python dalam pelajaran 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) dan skrip pelajaran 08.
  - Contoh TypeScript / JavaScript dalam pelajaran 06, 07, dan 11, dan buku nota .NET `.dib` untuk
    pelajaran 06 dan 07.
  - Buku nota tugasan dalam pelajaran 04, 06, 07, dan 11 (sel kod), ditambah contoh docstring `shared/python/api_utils.py`.
    
- **Panduan parameter model pemikiran (baru).** `gpt-5-mini` adalah model *pemikiran*: ia **tidak**
  menyokong `temperature`/`top_p`, dan menggunakan `max_completion_tokens` (penyelesaian chat) /
  `max_output_tokens` (API Respons) menggantikan `max_tokens`. Sehubungan itu:
  - Telah mengalih keluar `temperature`/`top_p`/`max_tokens` daripada sampel yang kini lalai kepada `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, pelajaran 15 RAG README).
  - Ditambah nota **"Model penalaran tidak menggunakan `temperature`"** kepada pelajaran 06, menerangkan bahawa
    model penalaran dikawal dengan **rekabentuk prompt + kawalan penalaran** dan bukannya
    suis pensampelan, manakala `temperature`/`top_p` kekal sah untuk model bukan penalaran
    (GPT-4.x, Mistral, Llama, Phi, model terbuka).
- **`gpt-5-mini` tidak digunakan untuk tutorial penalaan halus (pelajaran 18).** GPT-5 hanya menyokong
  penalaan halus pengukuhan (RFT); panduan pelajaran 18 penalaan halus terkawal (SFT) mengekalkan
  `gpt-4.1-mini`, yang menyokong SFT/DPO.
- **Demo suhu menggunakan model Llama.** Untuk terus mengajar `temperature` (yang model penalaran
  tolak), model `Llama-3.3-70B-Instruct` digunakan melalui penghujung Foundry Models. Ditambah pembolehubah
  baru `AZURE_INFERENCE_CHAT_MODEL` ke `.env.copy`; buku nota `githubmodels` pelajaran 04/06 dan
  sampel `06` `js-githubmodels` membacanya (jika tidak menggunakan `Llama-3.3-70B-Instruct`) dan mengekalkan
  demo `temperature`/`top_p`/`max_tokens` mereka.
- **Sampel JS / .NET dikemas kini untuk GPT-5.** Telah mengalih keluar `temperature`/`top_p`/`max_tokens` daripada sampel GPT-5
  (`06` `recipe-app` TypeScript, `06` `.dib` .NET - yang juga menaikkan `MaxOutputTokenCount`
  supaya output penalaran tidak terpotong). Sampel `06` `js-githubmodels` kini menggunakan Llama untuk mengekalkan demo suhunya.
  `.dib` menyatakan bahawa `Azure.AI.Inference` + model Llama adalah cara untuk
  menunjukan `Temperature` dalam .NET.
- Mengekalkan `gpt-4o-mini` / `gpt-5-mini` di tempat yang masih tepat: rujukan pengekodan token `tiktoken`,
  senarai ketersediaan katalog model, dan model pertuturan pelajaran 02 (`gpt-4o-transcribe`).
- Sampel pelajaran 20 (Mistral) dan 21 (Meta) mengekalkan `temperature`/`max_tokens` kerana mereka menyasarkan
  model Mistral/Llama, yang menyokong parameter tersebut.

## [2026-07-06] — Penyegaran Pemodenan Kandungan

Penyegaran besar untuk memastikan kurikulum tepat untuk 2026: API moden, nama produk dan
nama model terkini, panduan pembekal dikemas kini, dan alat pengalaman pembangun baru.

### Ditambah

- Seksyen **Microsoft Agent Framework** dalam pelajaran `17-ai-agents` yang merangkumi ejen chat tunggal,
  alat/panggilan fungsi, konfigurasi Azure OpenAI (Microsoft Foundry), dan orkestrasi aliran kerja multi-ejen
  (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** didokumentasikan sebagai penyedia luar talian / pada peranti (bersama Ollama) dalam
  `00-course-setup/03-providers.md` dan pelajaran `19-slm`.
- **Aliran kerja integrasi berterusan**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (dikuatkuasakan pada modul `shared/` yang dijaga,
    peringatan merentasi silibus yang lain), laluan ESLint peringatan, dan tugasan pytest.
  - `.github/workflows/security.yml` — Analisis CodeQL (Python + JavaScript/TypeScript) dan
    semakan pergantungan pada permintaan tarik.
- **Set ujian** di bawah `tests/` — 41 ujian pytest merangkumi modul utiliti bersama.
- **Kemahiran migrasi API Azure OpenAI → Responses** di bawah
  `.github/skills/azure-openai-to-responses/` yang digunakan untuk membimbing migrasi API.

### Diubah

- **Chat Completions API → Responses API** di semua contoh chat Python dan TypeScript
  (`client.responses.create(...)` → `response.output_text`), termasuk pelajaran 04, 06, 07, 11,
  15, dan 18, beserta README mereka.
- **Model GitHub → Model Microsoft Foundry** dalam prosa, pautan, dan contoh. Model GitHub
  akan bersara pada akhir Julai 2026; contoh kini menunjukkan katalog model Microsoft Foundry dan menggunakan
  pemboleh ubah persekitaran `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md`, dan dokumen penyedia** dikemas kini untuk mencerminkan bahawa Azure OpenAI kini sebahagian
  daripada Microsoft Foundry, dan versi API lalai dinaikkan ke `2024-10-21`.
- **Contoh TypeScript** (pelajaran 06, 07, 08, 11) dipindahkan dari SDK beta `@azure/openai`
  ke pakej `openai` (aplikasi chat menggunakan Responses API; aplikasi carian menggunakan
  klien embeddings).
- **Notebook .NET** (`dotnet/*.dib`) distandardkan pada `Azure.AI.OpenAI` **2.1.0**: pelajaran 06 dan 07
  menggunakan API `ChatClient`, pelajaran 08 menggunakan `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), dan
  pelajaran 09 menggunakan `ImageClient` (`GenerateImage`) dengan `gpt-image-1`, menggantikan
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` lama dari `1.0.0-beta.9`.
- **Perekaan semula nama produk**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (pelajaran 14, 16, 17) dan "Bing" → **Microsoft Copilot** (pelajaran 12), di mana ini merujuk kepada
  produk semasa.
- **DevContainer** (`.devcontainer/`) kini menghantar sambungan Pylance, Black, Ruff, ESLint, Prettier, dan Copilot,
  membolehkan format semasa simpan, dan memasang `ruff`, `black`, `mypy`, dan `pytest` supaya semakan CI
  boleh dihasilkan semula secara tempatan.
- **Penjanaan imej** (pelajaran 09) mengesyorkan `gpt-image-1` untuk Azure (katalog Azure telah membuang
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** telah dikemas kini untuk mencerminkan kerja yang telah disiapkan (migrasi API, CI,
  DevContainer, ujian) dan fakta semasa (terjemahan dihasilkan secara automatik oleh
  Azure Co-op Translator; API Assistants telah digantikan oleh API Responses).

### Diperbaiki

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` kini mengembalikan
  string kosong untuk input hanya ruang putih dan bukannya membangkitkan ralat "terlalu pendek" (selaras dengan
  kes `None`). Ditemui dan dilindungi oleh suite ujian baru.
- **Contoh imej Pelajaran 09** — membetulkan pepijat sebenar: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  dan satu pembolehubah yang menebalkan modul `openai`.
- **Buku nota RAG Pelajaran 15** — membaiki tetapan klien, menggantikan `DataFrame.append`
  yang dipadamkan dengan `pd.concat`, dan mengemaskini penggunaan SDK lama.
- Nama model yang tidak digunakan / digugurkan (`gpt-3.5-turbo`, `gpt-35-turbo`) digantikan dengan `gpt-4o-mini`
  dalam contoh aktif; output penalaan semula sejarah dalam pelajaran 18 dikekalkan dan diberi nota
  dan bukannya ditulis semula.

### Tidak Digunakan / Nota

- **Contoh Model Microsoft Foundry** yang menggunakan SDK `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — contoh dan pelajaran `githubmodels-*` dan `js-githubmodels` dalam pelajaran 19, 20,
  dan 21 — kekal menggunakan Model Inference API, yang **tidak** menyokong API Responses. Ini
  sengaja dibiarkan pada SDK tersebut.
- `AzureOpenAI()` sengaja dikekalkan di tempat yang masih sesuai (embedding dan penjanaan imej),
  kerana aliran kerja tersebut bukan sebahagian daripada migrasi API Responses.
- Rujukan `text-embedding-ada-002` dikekalkan di mana indeks embedding telah dikira sebelumnya bergantung kepadanya.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->