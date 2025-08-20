<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:34:14+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "ms"
}
-->
# Sediakan Persekitaran Pembangunan Anda

Kami menyediakan repositori dan kursus ini dengan [bekas pembangunan](https://containers.dev?WT.mc_id=academic-105485-koreyst) yang mempunyai runtime Universal yang menyokong pembangunan Python3, .NET, Node.js dan Java. Konfigurasi berkaitan ditakrifkan dalam fail `devcontainer.json` yang terletak di dalam folder `.devcontainer/` di akar repositori ini.

Untuk mengaktifkan bekas pembangunan, lancarkan ia dalam [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (untuk runtime yang dihoskan di awan) atau dalam [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (untuk runtime yang dihoskan pada peranti tempatan). Baca [dokumentasi ini](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) untuk maklumat lanjut tentang cara bekas pembangunan berfungsi dalam VS Code.

> [!TIP]  
> Kami mengesyorkan menggunakan GitHub Codespaces untuk permulaan pantas dengan usaha minimum. Ia menyediakan [kuota penggunaan percuma](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) yang murah hati untuk akaun peribadi. Konfigurasikan [timeout](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) untuk menghentikan atau memadam codespaces yang tidak aktif bagi memaksimumkan penggunaan kuota anda.

## 1. Melaksanakan Tugasan

Setiap pelajaran akan mempunyai tugasan _pilihan_ yang mungkin disediakan dalam satu atau lebih bahasa pengaturcaraan termasuk: Python, .NET/C#, Java dan JavaScript/TypeScript. Bahagian ini memberikan panduan umum berkaitan pelaksanaan tugasan tersebut.

### 1.1 Tugasan Python

Tugasan Python disediakan sama ada sebagai aplikasi (`.py` fail) atau buku nota Jupyter (`.ipynb` fail).  
- Untuk menjalankan buku nota, buka ia dalam Visual Studio Code kemudian klik _Select Kernel_ (di bahagian atas kanan) dan pilih pilihan Python 3 lalai yang dipaparkan. Anda kini boleh _Run All_ untuk melaksanakan buku nota tersebut.  
- Untuk menjalankan aplikasi Python dari baris arahan, ikut arahan khusus tugasan untuk memastikan anda memilih fail yang betul dan menyediakan argumen yang diperlukan.

## 2. Mengkonfigurasi Penyedia

Tugasan **mungkin** juga disediakan untuk berfungsi dengan satu atau lebih penempatan Large Language Model (LLM) melalui penyedia perkhidmatan yang disokong seperti OpenAI, Azure atau Hugging Face. Ini menyediakan _endpoint dihoskan_ (API) yang boleh diakses secara programatik dengan kelayakan yang betul (kunci API atau token). Dalam kursus ini, kami membincangkan penyedia berikut:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) dengan pelbagai model termasuk siri GPT teras.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) untuk model OpenAI dengan fokus kesediaan perusahaan  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) untuk model sumber terbuka dan pelayan inferens

**Anda perlu menggunakan akaun anda sendiri untuk latihan ini**. Tugasan adalah pilihan jadi anda boleh memilih untuk menyediakan satu, semua - atau tiada - penyedia berdasarkan minat anda. Beberapa panduan untuk pendaftaran:

| Pendaftaran | Kos | Kunci API | Playground | Komen |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Harga](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Berdasarkan Projek](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Tanpa Kod, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Pelbagai Model Tersedia |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Harga](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Perlu Memohon Akses Terlebih Dahulu](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Harga](https://huggingface.co/pricing) | [Token Akses](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat mempunyai model terhad](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Ikuti arahan di bawah untuk _mengkonfigurasi_ repositori ini untuk digunakan dengan penyedia yang berbeza. Tugasan yang memerlukan penyedia tertentu akan mengandungi salah satu tag ini dalam nama fail mereka:  
 - `aoai` - memerlukan endpoint Azure OpenAI, kunci  
 - `oai` - memerlukan endpoint OpenAI, kunci  
 - `hf` - memerlukan token Hugging Face

Anda boleh mengkonfigurasi satu, tiada, atau semua penyedia. Tugasan berkaitan akan gagal jika kelayakan tidak disediakan.

###  2.1. Cipta fail `.env`

Kami menganggap anda telah membaca panduan di atas dan mendaftar dengan penyedia yang berkaitan, serta memperoleh kelayakan pengesahan yang diperlukan (API_KEY atau token). Dalam kes Azure OpenAI, kami menganggap anda juga mempunyai penempatan Azure OpenAI Service (endpoint) yang sah dengan sekurang-kurangnya satu model GPT yang dikerahkan untuk penyempurnaan sembang.

Langkah seterusnya adalah untuk mengkonfigurasi **pembolehubah persekitaran tempatan** anda seperti berikut:

1. Cari dalam folder akar fail `.env.copy` yang sepatutnya mengandungi kandungan seperti ini:

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

2. Salin fail tersebut ke `.env` menggunakan arahan di bawah. Fail ini _gitignore-d_, memastikan rahsia selamat.

   ```bash
   cp .env.copy .env
   ```

3. Isikan nilai (gantikan tempat letak pada sebelah kanan `=`) seperti yang diterangkan dalam bahagian seterusnya.

3. (Pilihan) Jika anda menggunakan GitHub Codespaces, anda mempunyai pilihan untuk menyimpan pembolehubah persekitaran sebagai _Codespaces secrets_ yang dikaitkan dengan repositori ini. Dalam kes itu, anda tidak perlu menyediakan fail .env tempatan. **Walau bagaimanapun, ambil perhatian bahawa pilihan ini hanya berfungsi jika anda menggunakan GitHub Codespaces.** Anda masih perlu menyediakan fail .env jika menggunakan Docker Desktop.

### 2.2. Isikan fail `.env`

Mari kita lihat dengan cepat nama pembolehubah untuk memahami apa yang mereka wakili:

| Pembolehubah  | Penerangan  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ini adalah token akses pengguna yang anda tetapkan dalam profil anda |
| OPENAI_API_KEY | Ini adalah kunci kebenaran untuk menggunakan perkhidmatan bagi endpoint OpenAI bukan Azure |
| AZURE_OPENAI_API_KEY | Ini adalah kunci kebenaran untuk menggunakan perkhidmatan tersebut |
| AZURE_OPENAI_ENDPOINT | Ini adalah endpoint yang dikerahkan untuk sumber Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Ini adalah endpoint penempatan model _penjanaan teks_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ini adalah endpoint penempatan model _embedding teks_ |
| | |

Nota: Dua pembolehubah Azure OpenAI terakhir mencerminkan model lalai untuk penyempurnaan sembang (penjanaan teks) dan carian vektor (embedding) masing-masing. Arahan untuk menetapkannya akan diterangkan dalam tugasan berkaitan.

### 2.3 Konfigurasi Azure: Dari Portal

Nilai endpoint dan kunci Azure OpenAI boleh didapati dalam [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) jadi mari kita mulakan di sana.

1. Pergi ke [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
1. Klik pilihan **Keys and Endpoint** di bar sisi (menu di kiri).  
1. Klik **Show Keys** - anda akan melihat: KEY 1, KEY 2 dan Endpoint.  
1. Gunakan nilai KEY 1 untuk AZURE_OPENAI_API_KEY  
1. Gunakan nilai Endpoint untuk AZURE_OPENAI_ENDPOINT  

Seterusnya, kita perlukan endpoint untuk model tertentu yang telah kita kerahkan.

1. Klik pilihan **Model deployments** di bar sisi (menu kiri) untuk sumber Azure OpenAI.  
1. Di halaman destinasi, klik **Manage Deployments**  

Ini akan membawa anda ke laman web Azure OpenAI Studio, di mana kita akan mencari nilai lain seperti yang diterangkan di bawah.

### 2.4 Konfigurasi Azure: Dari Studio

1. Navigasi ke [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **dari sumber anda** seperti yang diterangkan di atas.  
1. Klik tab **Deployments** (bar sisi, kiri) untuk melihat model yang sedang dikerahkan.  
1. Jika model yang anda mahu tidak dikerahkan, gunakan **Create new deployment** untuk mengerahkannya.  
1. Anda memerlukan model _text-generation_ - kami mengesyorkan: **gpt-35-turbo**  
1. Anda memerlukan model _text-embedding_ - kami mengesyorkan **text-embedding-ada-002**  

Kini kemas kini pembolehubah persekitaran untuk mencerminkan _Nama Penempatan_ yang digunakan. Ini biasanya sama dengan nama model melainkan anda menukarnya secara eksplisit. Jadi, sebagai contoh, anda mungkin mempunyai:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Jangan lupa untuk simpan fail .env apabila selesai**. Anda kini boleh keluar dari fail dan kembali ke arahan untuk menjalankan buku nota.

### 2.5 Konfigurasi OpenAI: Dari Profil

Kunci API OpenAI anda boleh didapati dalam [akaun OpenAI anda](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jika anda belum ada, anda boleh mendaftar akaun dan cipta kunci API. Setelah anda mempunyai kunci tersebut, anda boleh menggunakannya untuk mengisi pembolehubah `OPENAI_API_KEY` dalam fail `.env`.

### 2.6 Konfigurasi Hugging Face: Dari Profil

Token Hugging Face anda boleh didapati dalam profil anda di bawah [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Jangan siarkan atau kongsi ini secara terbuka. Sebaliknya, cipta token baru untuk kegunaan projek ini dan salin ke dalam fail `.env` di bawah pembolehubah `HUGGING_FACE_API_KEY`. _Nota:_ Ini secara teknikal bukan kunci API tetapi digunakan untuk pengesahan jadi kami mengekalkan konvensyen penamaan ini untuk konsistensi.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.