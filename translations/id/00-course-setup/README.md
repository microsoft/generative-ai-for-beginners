<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T18:15:39+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "id"
}
-->
# Memulai Kursus Ini

Kami sangat antusias Anda mulai mengikuti kursus ini dan melihat apa yang akan Anda bangun dengan Generative AI!

Agar Anda sukses, halaman ini menjelaskan langkah-langkah persiapan, kebutuhan teknis, dan di mana Anda bisa mendapatkan bantuan jika diperlukan.

## Langkah-langkah Persiapan

Untuk mulai mengikuti kursus ini, Anda perlu menyelesaikan langkah-langkah berikut.

### 1. Fork Repo Ini

[Fork seluruh repo ini](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ke akun GitHub Anda sendiri agar bisa mengubah kode dan menyelesaikan tantangan. Anda juga bisa [memberi bintang (🌟) pada repo ini](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) agar lebih mudah menemukannya beserta repo terkait lainnya.

### 2. Buat Codespace

Untuk menghindari masalah dependensi saat menjalankan kode, kami menyarankan Anda menjalankan kursus ini di [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Pada fork Anda: **Code -> Codespaces -> New on main**

![Dialog menampilkan tombol untuk membuat codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Tambahkan Secret

1. ⚙️ Ikon gear -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Beri nama OPENAI_API_KEY, tempelkan kunci Anda, lalu Simpan.

### 3.  Selanjutnya Apa?

| Saya ingin…         | Pergi ke…                                                                |
|---------------------|--------------------------------------------------------------------------|
| Mulai Pelajaran 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Bekerja offline     | [`setup-local.md`](02-setup-local.md)                                   |
| Atur LLM Provider   | [`providers.md`](providers.md)                                          |
| Bertemu peserta lain| [Gabung ke Discord kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Pemecahan Masalah


| Gejala                                    | Solusi                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| Build container macet > 10 menit          | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal belum terhubung; klik **+** ➜ *bash*                   |
| `401 Unauthorized` dari OpenAI            | `OPENAI_API_KEY` salah / kadaluarsa                             |
| VS Code menampilkan “Dev container mounting…” | Refresh tab browser—Codespaces kadang kehilangan koneksi    |
| Kernel notebook hilang                    | Menu Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Sistem berbasis Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit File `.env`**: Buka file `.env` di text editor (misal VS Code, Notepad++, atau editor lain). Tambahkan baris berikut ke file, ganti `your_github_token_here` dengan token GitHub Anda yang sebenarnya:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Simpan File**: Simpan perubahan dan tutup text editor.

5. **Install `python-dotenv`**: Jika belum, Anda perlu menginstal paket `python-dotenv` untuk memuat variabel lingkungan dari file `.env` ke aplikasi Python Anda. Anda bisa menginstalnya dengan `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Muat Variabel Lingkungan di Script Python Anda**: Pada script Python Anda, gunakan paket `python-dotenv` untuk memuat variabel lingkungan dari file `.env`:

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

Untuk menjalankan kode secara lokal di komputer Anda, Anda perlu memiliki [Python terinstal](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Setelah itu, untuk menggunakan repository ini, Anda perlu mengkloningnya:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Setelah semuanya siap, Anda bisa langsung mulai!

## Langkah Opsional

### Menginstal Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) adalah installer ringan untuk menginstal [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, serta beberapa paket.
Conda sendiri adalah package manager yang memudahkan Anda mengatur dan berpindah antar [**virtual environment**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python dan paket-paketnya. Conda juga sangat berguna untuk menginstal paket yang tidak tersedia melalui `pip`.

Anda bisa mengikuti [panduan instalasi MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) untuk mengaturnya.

Setelah Miniconda terinstal, Anda perlu mengkloning [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ini (jika belum).

Selanjutnya, Anda perlu membuat virtual environment. Untuk melakukannya dengan Conda, silakan buat file environment baru (_environment.yml_). Jika Anda mengikuti dengan Codespaces, buat file ini di dalam direktori `.devcontainer`, jadi `.devcontainer/environment.yml`.

Isi file environment Anda dengan potongan kode di bawah ini:

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

Jika Anda mengalami error saat menggunakan conda, Anda bisa menginstal Microsoft AI Libraries secara manual dengan perintah berikut di terminal.

```
conda install -c microsoft azure-ai-ml
```

File environment menentukan dependensi yang dibutuhkan. `<environment-name>` adalah nama environment Conda yang Anda inginkan, dan `<python-version>` adalah versi Python yang ingin Anda gunakan, misalnya, `3` adalah versi mayor terbaru Python.

Setelah itu, Anda bisa membuat environment Conda dengan menjalankan perintah berikut di command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Lihat [panduan environment Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika Anda mengalami masalah.

### Menggunakan Visual Studio Code dengan ekstensi dukungan Python

Kami menyarankan menggunakan editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) dengan [ekstensi dukungan Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) terinstal untuk kursus ini. Namun, ini hanya saran dan bukan keharusan.

> **Note**: Dengan membuka repository kursus di VS Code, Anda punya opsi untuk mengatur proyek di dalam container. Ini karena adanya [direktori khusus `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) di dalam repository kursus. Penjelasan lebih lanjut akan dibahas nanti.

> **Note**: Setelah Anda mengkloning dan membuka direktori di VS Code, secara otomatis akan muncul saran untuk menginstal ekstensi dukungan Python.

> **Note**: Jika VS Code menyarankan untuk membuka repository di dalam container, tolak permintaan ini agar Anda bisa menggunakan Python yang terinstal secara lokal.

### Menggunakan Jupyter di Browser

Anda juga bisa mengerjakan proyek ini menggunakan [lingkungan Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) langsung di browser Anda. Baik Jupyter klasik maupun [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) menawarkan lingkungan pengembangan yang nyaman dengan fitur seperti auto-completion, code highlighting, dan lainnya.

Untuk memulai Jupyter secara lokal, buka terminal/command line, navigasikan ke direktori kursus, lalu jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulai instance Jupyter dan URL untuk mengaksesnya akan ditampilkan di jendela command line.

Setelah Anda mengakses URL tersebut, Anda akan melihat outline kursus dan bisa menavigasi ke file `*.ipynb` mana pun. Misalnya, `08-building-search-applications/python/oai-solution.ipynb`.

### Menjalankan di dalam Container

Alternatif dari mengatur semuanya di komputer atau Codespace Anda adalah menggunakan [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Folder khusus `.devcontainer` di dalam repository kursus memungkinkan VS Code mengatur proyek di dalam container. Di luar Codespaces, ini memerlukan instalasi Docker, dan sejujurnya, prosesnya agak rumit, jadi kami hanya menyarankan ini untuk yang sudah berpengalaman dengan container.

Salah satu cara terbaik untuk menjaga keamanan API key Anda saat menggunakan GitHub Codespaces adalah dengan menggunakan Codespace Secrets. Silakan ikuti panduan [manajemen secrets Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) untuk mempelajari lebih lanjut.

## Pelajaran dan Kebutuhan Teknis

Kursus ini terdiri dari 6 pelajaran konsep dan 6 pelajaran coding.

Untuk pelajaran coding, kami menggunakan Azure OpenAI Service. Anda perlu akses ke layanan Azure OpenAI dan API key untuk menjalankan kode ini. Anda bisa mengajukan permohonan akses dengan [mengisi aplikasi ini](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Sambil menunggu aplikasi Anda diproses, setiap pelajaran coding juga menyertakan file `README.md` di mana Anda bisa melihat kode dan hasil outputnya.

## Menggunakan Azure OpenAI Service untuk Pertama Kali

Jika ini adalah pertama kalinya Anda bekerja dengan Azure OpenAI service, silakan ikuti panduan cara [membuat dan mendepoy resource Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Menggunakan OpenAI API untuk Pertama Kali

Jika ini adalah pertama kalinya Anda bekerja dengan OpenAI API, silakan ikuti panduan cara [membuat dan menggunakan Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Bertemu Peserta Lain

Kami telah membuat channel di [server Discord Komunitas AI resmi](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) untuk bertemu peserta lain. Ini adalah cara yang bagus untuk membangun jaringan dengan wirausahawan, builder, pelajar, dan siapa pun yang ingin berkembang di bidang Generative AI.

[![Gabung channel discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tim proyek juga akan hadir di server Discord ini untuk membantu para peserta.

## Berkontribusi

Kursus ini adalah inisiatif open-source. Jika Anda melihat area yang bisa diperbaiki atau menemukan masalah, silakan buat [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) atau laporkan [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tim proyek akan memantau semua kontribusi. Berkontribusi ke open source adalah cara yang luar biasa untuk membangun karier Anda di bidang Generative AI.

Sebagian besar kontribusi mengharuskan Anda menyetujui Contributor License Agreement (CLA) yang menyatakan bahwa Anda memiliki hak dan benar-benar memberikan hak kepada kami untuk menggunakan kontribusi Anda. Untuk detailnya, kunjungi [situs web CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Penting: saat menerjemahkan teks di repo ini, pastikan Anda tidak menggunakan terjemahan mesin. Kami akan memverifikasi terjemahan melalui komunitas, jadi mohon hanya menjadi relawan untuk bahasa yang Anda kuasai.

Saat Anda mengirim pull request, CLA-bot akan secara otomatis menentukan apakah Anda perlu mengisi CLA dan menandai PR sesuai (misal, label, komentar). Cukup ikuti instruksi dari bot. Anda hanya perlu melakukan ini sekali untuk semua repository yang menggunakan CLA kami.

Proyek ini mengadopsi [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Untuk informasi lebih lanjut, baca FAQ Code of Conduct atau hubungi [Email opencode](opencode@microsoft.com) jika ada pertanyaan atau komentar tambahan.

## Ayo Mulai!
Sekarang setelah Anda menyelesaikan langkah-langkah yang diperlukan untuk menyelesaikan kursus ini, mari kita mulai dengan mendapatkan [pengantar tentang Generative AI dan LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Disclaimer**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.