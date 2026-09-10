# Memilih & Mengkonfigurasi Penyedia LLM 🔑

Tugasan **mungkin** juga disediakan untuk berfungsi dengan satu atau lebih penempatan Model Bahasa Besar (LLM) melalui penyedia perkhidmatan yang disokong seperti OpenAI, Azure atau Hugging Face. Ini menyediakan _titik akhir hos_ (API) yang boleh kita akses secara programatik dengan kelayakan yang betul (kunci API atau token). Dalam kursus ini, kami membincangkan penyedia ini:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) dengan model pelbagai termasuk siri GPT teras.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) untuk model OpenAI dengan kesiapan perusahaan sebagai fokus
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) untuk satu titik akhir dan kunci API bagi mengakses ratusan model dari OpenAI, Meta, Mistral, Cohere, Microsoft dan lain-lain (menggantikan GitHub Models, yang akan bersara pada penghujung Julai 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) untuk model sumber terbuka dan pelayan inferens
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) atau [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) jika anda lebih suka menjalankan model sepenuhnya secara luar talian pada peranti anda sendiri, tanpa langganan awan diperlukan

**Anda perlu menggunakan akaun anda sendiri untuk latihan-latihan ini**. Tugasan adalah pilihan jadi anda boleh memilih untuk menyediakan satu, semua - atau tiada - penyedia berdasarkan minat anda. Beberapa panduan untuk mendaftar:

| Daftar | Kos | Kunci API | Playground | Komen |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Harga](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Berasaskan projek](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Tanpa Kod, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Pelbagai Model Tersedia |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Harga](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Perlu Memohon Awal Untuk Akses](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Harga](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Halaman Gambaran Projek](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Tahap percuma tersedia; satu titik akhir + kunci untuk banyak penyedia model |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Harga](https://huggingface.co/pricing) | [Tokens Akses](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat mempunyai model terhad](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Percuma (berjalan di peranti anda) | Tidak diperlukan | [CLI/SDK Tempatan](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Titik akhir serasi OpenAI sepenuhnya luar talian |
| | | | | |

Ikut arahan di bawah untuk _mengkonfigurasi_ repositori ini untuk digunakan dengan penyedia yang berbeza. Tugasan yang memerlukan penyedia tertentu akan mengandungi salah satu tag ini dalam nama failnya:

- `aoai` - memerlukan titik akhir Azure OpenAI, kunci
- `oai` - memerlukan titik akhir OpenAI, kunci
- `hf` - memerlukan token Hugging Face
- `githubmodels` - memerlukan titik akhir Microsoft Foundry Models, kunci (GitHub Models akan bersara pada penghujung Julai 2026)

Anda boleh mengkonfigurasi satu, tiada, atau semua penyedia. Tugasan yang berkaitan akan gagal jika kelayakan hilang.

## Buat fail `.env`

Kami anggap anda telah membaca panduan di atas dan mendaftar dengan penyedia berkaitan, serta mendapatkan kelayakan pengesahan yang diperlukan (API_KEY atau token). Dalam kes Azure OpenAI, kami anggap anda juga mempunyai penempatan yang sah untuk Perkhidmatan Azure OpenAI (titik akhir) dengan sekurang-kurangnya satu model GPT ditempatkan untuk pelengkap sembang.

Langkah seterusnya ialah mengkonfigurasi **pembolehubah persekitaran tempatan** anda seperti berikut:

1. Cari dalam folder utama fail `.env.copy` yang sepatutnya mengandungi kandungan seperti ini:

   ```bash
   # Penyedia OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI dalam Microsoft Foundry
   ## (Perkhidmatan Azure OpenAI kini sebahagian daripada Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Lalai telah ditetapkan! (versi API GA stabil semasa)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Model Microsoft Foundry (katalog model pelbagai penyedia, menggantikan Model GitHub, yang akan dikemaskan pada akhir Julai 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Salinkan fail itu ke `.env` dengan arahan di bawah. Fail ini _diabaikan oleh git_, memastikan rahsia selamat.

   ```bash
   cp .env.copy .env
   ```

3. Isikan nilai (gantikan pemegang tempat di sebelah kanan `=`) seperti yang diterangkan dalam bahagian seterusnya.

4. (Pilihan) Jika anda menggunakan GitHub Codespaces, anda boleh menyimpan pembolehubah persekitaran sebagai _rahsia Codespaces_ yang dikaitkan dengan repositori ini. Dalam kes itu, anda tidak perlu menyediakan fail .env tempatan. **Walau bagaimanapun, perhatikan bahawa pilihan ini berfungsi hanya jika anda menggunakan GitHub Codespaces.** Anda masih perlu menyediakan fail .env jika menggunakan Docker Desktop.

## Isikan fail `.env`

Mari lihat ringkas nama pembolehubah untuk memahami apa yang mereka wakili:

| Pembolehubah  | Penerangan  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ini adalah token akses pengguna yang anda sediakan dalam profil anda |
| OPENAI_API_KEY | Ini adalah kunci kebenaran untuk menggunakan perkhidmatan bagi titik akhir OpenAI bukan Azure |
| AZURE_OPENAI_API_KEY | Ini adalah kunci kebenaran untuk menggunakan perkhidmatan itu |
| AZURE_OPENAI_ENDPOINT | Ini adalah titik akhir yang ditempatkan untuk sumber Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Ini adalah titik akhir penempatan model _penjanaan teks_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ini adalah titik akhir penempatan model _penanaman teks_ |
| AZURE_INFERENCE_ENDPOINT | Ini adalah titik akhir untuk projek Microsoft Foundry anda, digunakan untuk Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Ini adalah kunci API untuk projek Microsoft Foundry anda |
| | |

Nota: Dua pembolehubah terakhir Azure OpenAI menggambarkan model lalai untuk pelengkap sembang (penjanaan teks) dan carian vektor (penanaman) masing-masing. Arahan untuk menetapkannya akan ditentukan dalam tugasan berkaitan.

## Konfigurasi Azure OpenAI: Dari Portal

> **Nota:** Perkhidmatan Azure OpenAI kini sebahagian daripada [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Sumber dan penempatan masih dipaparkan dalam Azure Portal, tetapi pengurusan model harian (penempatan, playground, pemantauan) kini dilakukan dalam portal Foundry dan bukannya "Azure OpenAI Studio" berdiri sendiri yang lama.

Nilai titik akhir dan kunci Azure OpenAI akan ditemui dalam [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) jadi mari mulakan di situ.

1. Pergi ke [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik pilihan **Keys and Endpoint** dalam bar sisi (menu di kiri).
1. Klik **Show Keys** - anda akan melihat berikut: KEY 1, KEY 2 dan Endpoint.
1. Gunakan nilai KEY 1 untuk AZURE_OPENAI_API_KEY
1. Gunakan nilai Endpoint untuk AZURE_OPENAI_ENDPOINT

Seterusnya, kita perlukan titik akhir untuk model khusus yang telah kita tempatkan.

1. Klik pilihan **Model deployments** dalam bar sisi (menu kiri) untuk sumber Azure OpenAI.
1. Dalam halaman destinasi, klik **Go to Microsoft Foundry portal** (atau **Manage Deployments**, bergantung pada jenis sumber anda)

Ini akan membawa anda ke portal Microsoft Foundry, di mana kita akan mencari nilai lain seperti yang diterangkan di bawah.

## Konfigurasi Azure OpenAI: Dari portal Microsoft Foundry

1. Navigasi ke [portal Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **dari sumber anda** seperti yang diterangkan di atas.
1. Klik tab **Deployments** (bar sisi, kiri) untuk melihat model yang sedang ditempatkan.
1. Jika model yang dikehendaki belum ditempatkan, gunakan **Deploy model** untuk menempatkannya dari [katalog model](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Anda perlu model _penjanaan teks_ - kami cadangkan: **gpt-5-mini**
1. Anda perlu model _penanaman teks_ - kami cadangkan **text-embedding-3-small**

Kini kemaskini pembolehubah persekitaran untuk mencerminkan _Nama Penempatan_ yang digunakan. Ini biasanya sama dengan nama model melainkan anda mengubahnya secara eksplisit. Jadi, sebagai contoh, anda mungkin mempunyai:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Jangan lupa untuk simpan fail .env setelah selesai**. Anda kini boleh keluar dari fail dan kembali ke arahan untuk menjalankan notebook.

## Konfigurasi OpenAI: Dari Profil

Kunci API OpenAI anda boleh didapati dalam [akaun OpenAI anda](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jika anda belum ada, anda boleh mendaftar akaun dan cipta kunci API. Setelah anda ada kunci, anda boleh menggunakannya untuk mengisi pembolehubah `OPENAI_API_KEY` dalam fail `.env`.

## Konfigurasi Hugging Face: Dari Profil

Token Hugging Face anda boleh didapati dalam profil anda di bawah [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Jangan pos atau kongsi ini secara awam. Sebaliknya, cipta token baru untuk penggunaan projek ini dan salin ke dalam fail `.env` di bawah pembolehubah `HUGGING_FACE_API_KEY`. _Nota:_ Ini secara teknikal bukan kunci API tetapi digunakan untuk pengesahan jadi kami mengekalkan konvensyen penamaan itu untuk konsistensi.

## Konfigurasi Microsoft Foundry Models: Dari Portal

> **Nota:** GitHub Models akan bersara pada penghujung Julai 2026. Microsoft Foundry Models adalah pengganti langsung, menawarkan katalog model percuma untuk mencuba dan pengalaman SDK Azure AI Inference / OpenAI SDK yang sama.

1. Pergi ke [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) dan cipta (atau buka) projek Foundry.
1. Layari [katalog model](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) dan tempatkan model, contohnya `gpt-5-mini`.
1. Pada halaman **Overview** projek, salin **endpoint** dan **kunci API**.
1. Gunakan nilai endpoint untuk `AZURE_INFERENCE_ENDPOINT` dan nilai kunci untuk `AZURE_INFERENCE_CREDENTIAL` dalam fail `.env` anda.

## Penyedia Luar Talian / Tempatan

Jika anda lebih suka tidak menggunakan langganan awan sama sekali, anda boleh menjalankan model terbuka yang serasi secara terus pada peranti anda sendiri:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - runtime di peranti dari Microsoft. Ia secara automatik memilih penyedia pelaksanaan terbaik (NPU, GPU, atau CPU) dan mendedahkan titik akhir serasi OpenAI, jadi anda boleh menggunakan semula kebanyakan kod contoh dalam kursus ini dengan perubahan minima. Lihat [dokumentasi Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) untuk bermula, atau pasang dengan `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - alternatif popular untuk menjalankan model terbuka seperti Llama, Phi, Mistral, dan Gemma secara tempatan.


Lihat [Pelajaran 19: Membina dengan SLM](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) untuk contoh praktikal menggunakan kedua-dua pilihan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->