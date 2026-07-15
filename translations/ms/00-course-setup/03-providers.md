# Memilih & Mengkonfigurasi Penyedia LLM 🔑

Tugasan **mungkin** juga ditetapkan untuk berfungsi dengan satu atau lebih penghantaran Large Language Model (LLM) melalui penyedia perkhidmatan yang disokong seperti OpenAI, Azure atau Hugging Face. Ini menyediakan _titik akhir hos_ (API) yang boleh kita akses secara programatik dengan kelayakan yang betul (kunci API atau token). Dalam kursus ini, kita membincangkan penyedia ini:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) dengan model pelbagai termasuk siri GPT teras.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) untuk model OpenAI dengan tumpuan kesediaan perniagaan
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) untuk satu titik akhir dan kunci API untuk mengakses ratusan model dari OpenAI, Meta, Mistral, Cohere, Microsoft dan lain-lain (menggantikan GitHub Models, yang akan bersara pada akhir Julai 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) untuk model sumber terbuka dan pelayan inferens
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) atau [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) jika anda lebih suka menjalankan model sepenuhnya luar talian pada peranti anda sendiri, tanpa perlu langganan awan

**Anda perlu menggunakan akaun anda sendiri untuk latihan ini**. Tugasan adalah pilihan supaya anda boleh memilih untuk menyediakan satu, semua - atau tiada - daripada penyedia berdasarkan minat anda. Beberapa panduan untuk mendaftar:

| Daftar | Kos | Kunci API | Playground | Komen |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Harga](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Berasaskan Projek](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Tanpa Kod, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Pelbagai Model Tersedia |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Harga](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Perlu Memohon Awal Untuk Akses](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Harga](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Halaman Tinjauan Projek](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Tiers percuma tersedia; satu titik akhir + kunci untuk banyak penyedia model |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Harga](https://huggingface.co/pricing) | [Token Akses](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat mempunyai model terhad](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Percuma (berjalan pada peranti anda) | Tidak diperlukan | [CLI/SDK Tempatan](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Sepenuhnya luar talian, titik akhir serasi OpenAI |
| | | | | |

Ikuti arahan di bawah untuk _mengkonfigurasi_ repositori ini untuk kegunaan dengan penyedia yang berbeza. Tugasan yang memerlukan penyedia tertentu akan mengandungi satu tag ini dalam nama fail mereka:

- `aoai` - memerlukan titik akhir Azure OpenAI, kunci
- `oai` - memerlukan titik akhir OpenAI, kunci
- `hf` - memerlukan token Hugging Face
- `githubmodels` - memerlukan titik akhir Microsoft Foundry Models, kunci (GitHub Models akan bersara pada akhir Julai 2026)

Anda boleh mengkonfigurasi satu, tiada, atau semua penyedia. Tugasan berkaitan akan gagal jika tiada kelayakan.

## Cipta fail `.env`

Kami mengandaikan anda sudah membaca panduan di atas dan mendaftar dengan penyedia berkaitan, serta memperoleh kelayakan pengesahan yang diperlukan (API_KEY atau token). Dalam kes Azure OpenAI, kami mengandaikan anda juga mempunyai penghantaran sah Azure OpenAI Service (titik akhir) dengan sekurang-kurangnya satu model GPT yang dihantar untuk penyempurnaan chat.

Langkah seterusnya adalah mengkonfigurasi **pembolehubah persekitaran tempatan** anda seperti berikut:

1. Cari dalam folder akar untuk fail `.env.copy` yang sepatutnya mempunyai kandungan seperti ini:

   ```bash
   # Penyedia OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI dalam Microsoft Foundry
   ## (Perkhidmatan Azure OpenAI kini sebahagian daripada Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Lalai telah ditetapkan! (versi API GA stabil semasa)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Model Microsoft Foundry (katalog model berbilang penyedia, menggantikan Model GitHub, yang akan bersara pada akhir Julai 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Salin fail itu ke `.env` menggunakan arahan di bawah. Fail ini _gitignore-d_, memastikan rahsia selamat.

   ```bash
   cp .env.copy .env
   ```

3. Isikan nilai (gantikan pemegang tempat di sebelah kanan `=`) seperti yang diterangkan dalam bahagian seterusnya.

4. (Pilihan) Jika anda menggunakan GitHub Codespaces, anda mempunyai pilihan untuk menyimpan pembolehubah persekitaran sebagai _rahsia Codespaces_ yang dikaitkan dengan repositori ini. Dalam kes itu, anda tidak perlu menyediakan fail .env tempatan. **Namun, perhatikan bahawa pilihan ini hanya berfungsi jika anda menggunakan GitHub Codespaces.** Anda masih perlu menyediakan fail .env jika anda menggunakan Docker Desktop sebaliknya.

## Isi fail `.env`

Mari kita lihat dengan cepat nama pembolehubah untuk memahami apa yang mereka wakili:

| Pembolehubah  | Penerangan  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ini adalah token akses pengguna yang anda sediakan dalam profil anda |
| OPENAI_API_KEY | Ini adalah kunci kebenaran untuk menggunakan perkhidmatan bagi titik akhir OpenAI bukan Azure |
| AZURE_OPENAI_API_KEY | Ini adalah kunci kebenaran untuk menggunakan perkhidmatan itu |
| AZURE_OPENAI_ENDPOINT | Ini adalah titik akhir yang dihantar untuk sumber Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Ini adalah titik penghantaran model _penjanaan teks_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ini adalah titik penghantaran model _pembedded teks_ |
| AZURE_INFERENCE_ENDPOINT | Ini adalah titik akhir untuk projek Microsoft Foundry anda, digunakan bagi Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Ini adalah kunci API untuk projek Microsoft Foundry anda |
| | |

Nota: Dua pembolehubah Azure OpenAI terakhir mencerminkan model lalai untuk penyempurnaan perbualan (penjanaan teks) dan carian vektor (embedding) masing-masing. Arahan untuk menyetelnya akan ditakrifkan dalam tugasan berkaitan.

## Konfigurasi Azure OpenAI: Dari Portal

> **Nota:** Azure OpenAI Service kini sebahagian daripada [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Sumber dan penghantaran masih akan dipaparkan dalam Azure Portal, tetapi pengurusan model harian (penghantaran, playground, pemantauan) kini dilakukan dalam portal Foundry dan bukan "Azure OpenAI Studio" berdiri sendiri yang lama.

Nilai titik akhir dan kunci Azure OpenAI akan didapati di [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) jadi mari kita mulakan dari situ.

1. Pergi ke [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik pilihan **Keys and Endpoint** di bar sisi (menu di kiri).
1. Klik **Show Keys** - anda akan melihat berikut: KEY 1, KEY 2 dan Endpoint.
1. Gunakan nilai KEY 1 untuk AZURE_OPENAI_API_KEY
1. Gunakan nilai Endpoint untuk AZURE_OPENAI_ENDPOINT

Seterusnya, kita memerlukan titik akhir untuk model tertentu yang telah dihantar.

1. Klik pilihan **Model deployments** di bar sisi (menu kiri) untuk sumber Azure OpenAI.
1. Dalam halaman destinasi, klik **Go to Microsoft Foundry portal** (atau **Manage Deployments**, bergantung pada jenis sumber anda)

Ini akan membawa anda ke portal Microsoft Foundry, di mana kita akan menemui nilai lain seperti yang diterangkan di bawah.

## Konfigurasi Azure OpenAI: Dari portal Microsoft Foundry

1. Navigasi ke [portal Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **dari sumber anda** seperti yang diterangkan di atas.
1. Klik tab **Deployments** (bar sisi, kiri) untuk melihat model yang sedang dihantar.
1. Jika model yang dikehendaki belum dihantar, gunakan **Deploy model** untuk menghantarnya dari [katalog model](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Anda akan memerlukan model _penjanaan-teks_ - kami mengesyorkan: **gpt-4o-mini**
1. Anda akan memerlukan model _embedded-teks_ - kami mengesyorkan **text-embedding-3-small**

Kini kemaskini pembolehubah persekitaran untuk mencerminkan _Nama penghantaran_ yang digunakan. Ini biasanya sama dengan nama model kecuali jika anda menukarnya secara eksplisit. Jadi, sebagai contoh, anda mungkin mempunyai:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Jangan lupa untuk menyimpan fail .env selepas selesai**. Anda kini boleh keluar dari fail dan kembali ke arahan untuk menjalankan notebook.

## Konfigurasi OpenAI: Dari Profil

Kunci API OpenAI anda boleh didapati dalam [akaun OpenAI anda](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jika anda belum ada, anda boleh mendaftar akaun dan mencipta kunci API. Setelah mempunyai kunci itu, anda boleh menggunakannya untuk mengisi pembolehubah `OPENAI_API_KEY` dalam fail `.env`.

## Konfigurasi Hugging Face: Dari Profil

Token Hugging Face anda boleh didapati dalam profil anda di bawah [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Jangan siarkan atau kongsi ini secara umum. Sebaliknya, cipta token baru untuk kegunaan projek ini dan salin ke dalam fail `.env` di bawah pembolehubah `HUGGING_FACE_API_KEY`. _Nota:_ Ini secara teknikal bukan kunci API tetapi digunakan untuk pengesahan jadi kami mengekalkan konvensyen penamaan itu bagi konsistensi.

## Konfigurasi Microsoft Foundry Models: Dari Portal

> **Nota:** GitHub Models akan bersara pada akhir Julai 2026. Microsoft Foundry Models adalah pengganti langsung, menawarkan katalog model percubaan percuma yang sama dan pengalaman Azure AI Inference SDK / OpenAI SDK.

1. Pergi ke [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) dan cipta (atau buka) projek Foundry.
1. Layari [katalog model](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) dan hantar model, contohnya `gpt-4o-mini`.
1. Pada halaman **Overview** projek, salin **endpoint** dan **kunci API**.
1. Gunakan nilai endpoint untuk `AZURE_INFERENCE_ENDPOINT` dan nilai kunci untuk `AZURE_INFERENCE_CREDENTIAL` dalam fail `.env` anda.

## Penyedia Luar Talian / Tempatan

Jika anda lebih suka tidak menggunakan langganan awan langsung, anda boleh menjalankan model terbuka yang serasi terus pada peranti anda sendiri:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - runtime di peranti Microsoft. Ia secara automatik memilih penyedia pelaksanaan terbaik (NPU, GPU, atau CPU) dan mendedahkan titik akhir yang serasi OpenAI, jadi anda boleh menggunakan semula kebanyakan kod contoh dalam kursus ini dengan perubahan minimum. Lihat [dokumentasi Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) untuk bermula, atau pasang dengan `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - alternatif popular untuk menjalankan model terbuka seperti Llama, Phi, Mistral, dan Gemma secara tempatan.


Lihat [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) untuk contoh amali menggunakan kedua-dua pilihan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->