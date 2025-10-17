<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T20:44:32+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "id"
}
-->
# Memulai Kursus Ini

Kami sangat bersemangat untuk Anda memulai kursus ini dan melihat apa yang dapat Anda ciptakan dengan Generative AI!

Untuk memastikan kesuksesan Anda, halaman ini menjelaskan langkah-langkah pengaturan, persyaratan teknis, dan di mana mendapatkan bantuan jika diperlukan.

## Langkah-Langkah Pengaturan

Untuk mulai mengikuti kursus ini, Anda perlu menyelesaikan langkah-langkah berikut.

### 1. Fork Repo Ini

[Fork seluruh repo ini](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ke akun GitHub Anda sendiri agar dapat mengubah kode dan menyelesaikan tantangan. Anda juga dapat [memberi bintang (🌟) pada repo ini](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) untuk mempermudah menemukannya dan repo terkait lainnya.

### 2. Buat Codespace

Untuk menghindari masalah ketergantungan saat menjalankan kode, kami merekomendasikan menjalankan kursus ini di [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Di fork Anda: **Code -> Codespaces -> New on main**

![Dialog menunjukkan tombol untuk membuat codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Tambahkan Secret

1. ⚙️ Ikon Gear -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. Beri nama OPENAI_API_KEY, tempelkan kunci Anda, Simpan.

### 3. Apa Selanjutnya?

| Saya ingin…         | Pergi ke…                                                               |
|---------------------|-------------------------------------------------------------------------|
| Mulai Pelajaran 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Bekerja offline     | [`setup-local.md`](02-setup-local.md)                                   |
| Mengatur Penyedia LLM | [`providers.md`](03-providers.md)                                        |
| Bertemu dengan pelajar lain | [Bergabung dengan Discord kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Pemecahan Masalah

| Gejala                                   | Solusi                                                          |
|------------------------------------------|-----------------------------------------------------------------|
| Pembangunan container macet > 10 menit  | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`              | Terminal tidak terhubung; klik **+** ➜ *bash*                   |
| `401 Unauthorized` dari OpenAI           | `OPENAI_API_KEY` salah / kadaluarsa                             |
| VS Code menunjukkan “Dev container mounting…” | Segarkan tab browser—Codespaces kadang kehilangan koneksi       |
| Kernel notebook hilang                   | Menu notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Sistem berbasis Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit File `.env`**: Buka file `.env` di editor teks (misalnya, VS Code, Notepad++, atau editor lainnya). Tambahkan baris berikut ke file, mengganti `your_github_token_here` dengan token GitHub Anda yang sebenarnya:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Simpan File**: Simpan perubahan dan tutup editor teks.

5. **Instal `python-dotenv`**: Jika Anda belum melakukannya, Anda perlu menginstal paket `python-dotenv` untuk memuat variabel lingkungan dari file `.env` ke aplikasi Python Anda. Anda dapat menginstalnya menggunakan `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Memuat Variabel Lingkungan di Skrip Python Anda**: Dalam skrip Python Anda, gunakan paket `python-dotenv` untuk memuat variabel lingkungan dari file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Selesai! Anda telah berhasil membuat file `.env`, menambahkan token GitHub Anda, dan memuatnya ke aplikasi Python Anda.

## Cara Menjalankan Secara Lokal di Komputer Anda

Untuk menjalankan kode secara lokal di komputer Anda, Anda perlu memiliki beberapa versi [Python terinstal](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Untuk kemudian menggunakan repositori, Anda perlu mengkloningnya:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Setelah semuanya diperiksa, Anda dapat mulai!

## Langkah Opsional

### Menginstal Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) adalah installer ringan untuk menginstal [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, serta beberapa paket.
Conda sendiri adalah pengelola paket yang memudahkan pengaturan dan pengalihan antara berbagai [**lingkungan virtual**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python dan paket. Ini juga berguna untuk menginstal paket yang tidak tersedia melalui `pip`.

Anda dapat mengikuti [panduan instalasi MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) untuk mengaturnya.

Dengan Miniconda terinstal, Anda perlu mengkloning [repositori](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jika Anda belum melakukannya).

Selanjutnya, Anda perlu membuat lingkungan virtual. Untuk melakukannya dengan Conda, buat file lingkungan baru (_environment.yml_). Jika Anda mengikuti menggunakan Codespaces, buat ini di dalam direktori `.devcontainer`, yaitu `.devcontainer/environment.yml`.

Isi file lingkungan Anda dengan cuplikan di bawah ini:

```yml
name: <environment-name>
channels:
  - defaults
  - microsoft
dependencies:
  - python=<python-version>
  - openai
  - python-dotenv
  - pip
  - pip:
      - azure-ai-ml
```

Jika Anda mengalami kesalahan menggunakan conda, Anda dapat menginstal pustaka AI Microsoft secara manual menggunakan perintah berikut di terminal.

```
conda install -c microsoft azure-ai-ml
```

File lingkungan menentukan ketergantungan yang kita butuhkan. `<environment-name>` mengacu pada nama yang ingin Anda gunakan untuk lingkungan Conda Anda, dan `<python-version>` adalah versi Python yang ingin Anda gunakan, misalnya, `3` adalah versi utama terbaru dari Python.

Setelah selesai, Anda dapat membuat lingkungan Conda Anda dengan menjalankan perintah di bawah ini di command line/terminal Anda:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Lihat [panduan lingkungan Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika Anda mengalami masalah.

### Menggunakan Visual Studio Code dengan Ekstensi Dukungan Python

Kami merekomendasikan menggunakan editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) dengan [ekstensi dukungan Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) yang terinstal untuk kursus ini. Namun, ini lebih merupakan rekomendasi dan bukan persyaratan pasti.

> **Catatan**: Dengan membuka repositori kursus di VS Code, Anda memiliki opsi untuk mengatur proyek di dalam container. Ini karena direktori [khusus `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) yang ditemukan di dalam repositori kursus. Lebih lanjut tentang ini nanti.

> **Catatan**: Setelah Anda mengkloning dan membuka direktori di VS Code, secara otomatis akan menyarankan Anda menginstal ekstensi dukungan Python.

> **Catatan**: Jika VS Code menyarankan Anda membuka kembali repositori di dalam container, tolak permintaan ini untuk menggunakan versi Python yang terinstal secara lokal.

### Menggunakan Jupyter di Browser

Anda juga dapat mengerjakan proyek menggunakan [lingkungan Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) langsung di browser Anda. Baik Jupyter klasik maupun [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) menyediakan lingkungan pengembangan yang cukup menyenangkan dengan fitur seperti auto-completion, penyorotan kode, dll.

Untuk memulai Jupyter secara lokal, buka terminal/command line, navigasikan ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulai instance Jupyter dan URL untuk mengaksesnya akan ditampilkan di jendela command line.

Setelah Anda mengakses URL, Anda akan melihat garis besar kursus dan dapat menavigasi ke file `*.ipynb` mana pun. Misalnya, `08-building-search-applications/python/oai-solution.ipynb`.

### Menjalankan di dalam Container

Alternatif untuk mengatur semuanya di komputer Anda atau Codespace adalah menggunakan [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Folder khusus `.devcontainer` di dalam repositori kursus memungkinkan VS Code mengatur proyek di dalam container. Di luar Codespaces, ini akan memerlukan instalasi Docker, dan sejujurnya, ini melibatkan sedikit pekerjaan, jadi kami merekomendasikan ini hanya untuk mereka yang berpengalaman bekerja dengan container.

Salah satu cara terbaik untuk menjaga keamanan kunci API Anda saat menggunakan GitHub Codespaces adalah dengan menggunakan Secrets Codespace. Silakan ikuti [panduan pengelolaan secrets Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) untuk mempelajari lebih lanjut tentang ini.

## Pelajaran dan Persyaratan Teknis

Kursus ini memiliki 6 pelajaran konsep dan 6 pelajaran coding.

Untuk pelajaran coding, kami menggunakan Azure OpenAI Service. Anda akan membutuhkan akses ke layanan Azure OpenAI dan kunci API untuk menjalankan kode ini. Anda dapat mengajukan permohonan akses dengan [mengisi aplikasi ini](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Sambil menunggu aplikasi Anda diproses, setiap pelajaran coding juga menyertakan file `README.md` di mana Anda dapat melihat kode dan hasilnya.

## Menggunakan Azure OpenAI Service untuk Pertama Kali

Jika ini adalah pertama kalinya Anda bekerja dengan layanan Azure OpenAI, silakan ikuti panduan tentang cara [membuat dan menerapkan sumber daya Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Menggunakan OpenAI API untuk Pertama Kali

Jika ini adalah pertama kalinya Anda bekerja dengan OpenAI API, silakan ikuti panduan tentang cara [membuat dan menggunakan Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Bertemu dengan Pelajar Lain

Kami telah membuat saluran di [server Discord Komunitas AI resmi](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) untuk bertemu dengan pelajar lain. Ini adalah cara yang bagus untuk membangun jaringan dengan pengusaha, pembangun, pelajar, dan siapa saja yang ingin meningkatkan kemampuan mereka di Generative AI.

[![Bergabung dengan saluran Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tim proyek juga akan berada di server Discord ini untuk membantu para pelajar.

## Berkontribusi

Kursus ini adalah inisiatif open-source. Jika Anda melihat area yang perlu diperbaiki atau masalah, silakan buat [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) atau log [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tim proyek akan melacak semua kontribusi. Berkontribusi pada open source adalah cara yang luar biasa untuk membangun karier Anda di Generative AI.

Sebagian besar kontribusi mengharuskan Anda menyetujui Contributor License Agreement (CLA) yang menyatakan bahwa Anda memiliki hak dan benar-benar memberikan kami hak untuk menggunakan kontribusi Anda. Untuk detailnya, kunjungi [CLA, situs web Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Penting: saat menerjemahkan teks dalam repo ini, pastikan Anda tidak menggunakan terjemahan mesin. Kami akan memverifikasi terjemahan melalui komunitas, jadi silakan hanya menjadi sukarelawan untuk terjemahan dalam bahasa yang Anda kuasai.

Saat Anda mengirimkan pull request, CLA-bot akan secara otomatis menentukan apakah Anda perlu memberikan CLA dan menghias PR dengan tepat (misalnya, label, komentar). Cukup ikuti instruksi yang diberikan oleh bot. Anda hanya perlu melakukannya sekali di semua repositori yang menggunakan CLA kami.

Proyek ini telah mengadopsi [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Untuk informasi lebih lanjut, baca FAQ Code of Conduct atau hubungi [Email opencode](opencode@microsoft.com) dengan pertanyaan atau komentar tambahan.

## Mari Kita Mulai
Sekarang setelah Anda menyelesaikan langkah-langkah yang diperlukan untuk menyelesaikan kursus ini, mari kita mulai dengan mendapatkan [pengantar tentang Generative AI dan LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.