<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:55:09+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "ms"
}
-->
# Sediakan Persekitaran Pembangunan Anda

Kami menyediakan repositori dan kursus ini dengan [kontena pembangunan](https://containers.dev?WT.mc_id=academic-105485-koreyst) yang mempunyai runtime Universal yang boleh menyokong pembangunan Python3, .NET, Node.js dan Java. Konfigurasi berkaitan ditakrifkan dalam fail `devcontainer.json` yang terletak dalam folder `.devcontainer/` di akar repositori ini.

Untuk mengaktifkan kontena pembangunan, lancarkannya dalam [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (untuk runtime yang dihoskan awan) atau dalam [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (untuk runtime yang dihoskan peranti tempatan). Baca [dokumentasi ini](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) untuk maklumat lanjut tentang cara kontena pembangunan berfungsi dalam VS Code.

> [!TIP]  
> Kami mengesyorkan menggunakan GitHub Codespaces untuk memulakan dengan cepat dengan usaha yang minimum. Ia menyediakan [kuota penggunaan percuma](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) yang murah hati untuk akaun peribadi. Konfigurasikan [masa tamat](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) untuk menghentikan atau memadam codespaces yang tidak aktif untuk memaksimumkan penggunaan kuota anda.

## 1. Melaksanakan Tugasan

Setiap pelajaran akan mempunyai tugasan _pilihan_ yang mungkin disediakan dalam satu atau lebih bahasa pengaturcaraan termasuk: Python, .NET/C#, Java dan JavaScript/TypeScript. Bahagian ini menyediakan panduan umum berkaitan pelaksanaan tugasan tersebut.

### 1.1 Tugasan Python

Tugasan Python disediakan sama ada sebagai aplikasi (fail `.py`) atau Jupyter notebooks (fail `.ipynb`).
- Untuk menjalankan notebook, buka dalam Visual Studio Code kemudian klik _Select Kernel_ (di bahagian atas kanan) dan pilih pilihan Python 3 lalai yang ditunjukkan. Anda kini boleh _Run All_ untuk melaksanakan notebook.
- Untuk menjalankan aplikasi Python dari command-line, ikuti arahan khusus tugasan untuk memastikan anda memilih fail yang betul dan memberikan argumen yang diperlukan.

## 2. Mengkonfigurasi Penyedia

Tugasan **mungkin** juga disediakan untuk berfungsi dengan satu atau lebih Model Bahasa Besar (LLM) melalui penyedia perkhidmatan yang disokong seperti OpenAI, Azure atau Hugging Face. Ini menyediakan _endpoint yang dihoskan_ (API) yang boleh kita akses secara programatik dengan kelayakan yang betul (kunci API atau token). Dalam kursus ini, kita membincangkan penyedia ini:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) dengan model yang pelbagai termasuk siri teras GPT.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) untuk model OpenAI dengan fokus kepada kesediaan perusahaan
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) untuk model sumber terbuka dan pelayan inferens

**Anda perlu menggunakan akaun anda sendiri untuk latihan ini**. Tugasan adalah pilihan jadi anda boleh memilih untuk menyediakan satu, semua - atau tiada - penyedia berdasarkan minat anda. Beberapa panduan untuk pendaftaran:

| Pendaftaran | Kos | Kunci API | Playground | Komen |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Harga](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Berdasarkan Projek](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Pelbagai Model Tersedia |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Harga](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Mesti Mohon Terlebih Dahulu Untuk Akses](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Harga](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat mempunyai model terhad](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Ikuti arahan di bawah untuk _mengkonfigurasi_ repositori ini untuk digunakan dengan penyedia yang berbeza. Tugasan yang memerlukan penyedia tertentu akan mengandungi salah satu tag ini dalam nama fail mereka:
- `aoai` - memerlukan endpoint Azure OpenAI, kunci
- `oai` - memerlukan endpoint OpenAI, kunci
- `hf` - memerlukan token Hugging Face

Anda boleh mengkonfigurasi satu, tiada, atau semua penyedia. Tugasan berkaitan hanya akan memberikan ralat pada kelayakan yang hilang.

### 2.1. Buat fail `.env`

Kami menganggap bahawa anda telah membaca panduan di atas dan mendaftar dengan penyedia yang berkaitan, dan memperoleh kelayakan pengesahan yang diperlukan (API_KEY atau token). Dalam kes Azure OpenAI, kami menganggap anda juga mempunyai penyebaran sah Perkhidmatan Azure OpenAI (endpoint) dengan sekurang-kurangnya satu model GPT yang disebarkan untuk penyelesaian chat.

Langkah seterusnya ialah mengkonfigurasi **pembolehubah persekitaran tempatan** anda seperti berikut:

1. Cari dalam folder akar untuk fail `.env.copy` yang sepatutnya mempunyai kandungan seperti ini:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Salin fail tersebut ke `.env` menggunakan arahan di bawah. Fail ini adalah _gitignore-d_, menjaga rahsia tetap selamat.

   ```bash
   cp .env.copy .env
   ```

3. Isikan nilai-nilai (gantikan placeholder di sebelah kanan `=`) seperti yang diterangkan dalam bahagian seterusnya.

3. (Pilihan) Jika anda menggunakan GitHub Codespaces, anda mempunyai pilihan untuk menyimpan pembolehubah persekitaran sebagai _rahsia Codespaces_ yang dikaitkan dengan repositori ini. Dalam kes itu, anda tidak perlu menyediakan fail .env tempatan. **Walau bagaimanapun, perhatikan bahawa pilihan ini hanya berfungsi jika anda menggunakan GitHub Codespaces.** Anda masih perlu menyediakan fail .env jika anda menggunakan Docker Desktop sebaliknya.

### 2.2. Isi fail `.env`

Mari kita lihat sekilas nama pembolehubah untuk memahami apa yang mereka wakili:

| Pembolehubah  | Penerangan  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ini adalah token akses pengguna yang anda tetapkan dalam profil anda |
| OPENAI_API_KEY | Ini adalah kunci kebenaran untuk menggunakan perkhidmatan untuk endpoint OpenAI bukan Azure |
| AZURE_OPENAI_API_KEY | Ini adalah kunci kebenaran untuk menggunakan perkhidmatan tersebut |
| AZURE_OPENAI_ENDPOINT | Ini adalah endpoint yang disebarkan untuk sumber Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Ini adalah endpoint penyebaran model _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ini adalah endpoint penyebaran model _text embeddings_ |
| | |

Nota: Dua pembolehubah terakhir Azure OpenAI mencerminkan model lalai untuk penyelesaian chat (text generation) dan carian vektor (embeddings) masing-masing. Arahan untuk menetapkannya akan ditakrifkan dalam tugasan yang berkaitan.

### 2.3 Konfigurasi Azure: Dari Portal

Nilai endpoint dan kunci Azure OpenAI akan ditemui dalam [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) jadi mari kita mulakan di sana.

1. Pergi ke [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik pilihan **Keys and Endpoint** dalam bar sisi (menu di kiri).
1. Klik **Show Keys** - anda sepatutnya melihat perkara berikut: KEY 1, KEY 2 dan Endpoint.
1. Gunakan nilai KEY 1 untuk AZURE_OPENAI_API_KEY
1. Gunakan nilai Endpoint untuk AZURE_OPENAI_ENDPOINT

Seterusnya, kita perlukan endpoint untuk model tertentu yang telah kita sebarkan.

1. Klik pilihan **Model deployments** dalam bar sisi (menu kiri) untuk sumber Azure OpenAI.
1. Dalam halaman destinasi, klik **Manage Deployments**

Ini akan membawa anda ke laman web Azure OpenAI Studio, di mana kita akan menemui nilai-nilai lain seperti yang diterangkan di bawah.

### 2.4 Konfigurasi Azure: Dari Studio

1. Navigasi ke [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **dari sumber anda** seperti yang diterangkan di atas.
1. Klik tab **Deployments** (bar sisi, kiri) untuk melihat model yang sedang disebarkan.
1. Jika model yang anda inginkan tidak disebarkan, gunakan **Create new deployment** untuk menyebarkannya.
1. Anda memerlukan model _text-generation_ - kami mengesyorkan: **gpt-35-turbo**
1. Anda memerlukan model _text-embedding_ - kami mengesyorkan **text-embedding-ada-002**

Kini kemas kini pembolehubah persekitaran untuk mencerminkan _Nama Penyebaran_ yang digunakan. Ini biasanya akan sama dengan nama model kecuali anda mengubahnya secara eksplisit. Jadi, sebagai contoh, anda mungkin mempunyai:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Jangan lupa untuk menyimpan fail .env apabila selesai**. Anda kini boleh keluar dari fail dan kembali kepada arahan untuk menjalankan notebook.

### 2.5 Konfigurasi OpenAI: Dari Profil

Kunci API OpenAI anda boleh ditemui dalam [akaun OpenAI anda](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jika anda belum mempunyai satu, anda boleh mendaftar untuk akaun dan membuat kunci API. Setelah anda mempunyai kunci tersebut, anda boleh menggunakannya untuk mengisi pembolehubah `OPENAI_API_KEY` dalam fail `.env`.

### 2.6 Konfigurasi Hugging Face: Dari Profil

Token Hugging Face anda boleh ditemui dalam profil anda di bawah [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Jangan siarkan atau kongsi ini secara terbuka. Sebaliknya, buat token baru untuk penggunaan projek ini dan salin ke dalam fail `.env` di bawah pembolehubah `HUGGING_FACE_API_KEY`. _Nota:_ Ini secara teknikalnya bukan kunci API tetapi digunakan untuk pengesahan jadi kami mengekalkan konvensyen penamaan itu untuk konsistensi.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.