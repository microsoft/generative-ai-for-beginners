<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:13:49+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "id"
}
-->
# Memulai dengan kursus ini

Kami sangat antusias Anda memulai kursus ini dan melihat apa yang menginspirasi Anda untuk dibuat dengan Generative AI!

Untuk memastikan kesuksesan Anda, halaman ini menjelaskan langkah-langkah pengaturan, persyaratan teknis, dan tempat mendapatkan bantuan jika diperlukan.

## Langkah Pengaturan

Untuk mulai mengikuti kursus ini, Anda perlu menyelesaikan langkah-langkah berikut.

### 1. Fork Repo ini

[Fork seluruh repo ini](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ke akun GitHub Anda sendiri agar dapat mengubah kode dan menyelesaikan tantangan. Anda juga bisa [memberi bintang (🌟) pada repo ini](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) agar lebih mudah menemukannya dan repo terkait lainnya.

### 2. Buat codespace

Untuk menghindari masalah dependensi saat menjalankan kode, kami menyarankan menjalankan kursus ini di [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Codespace ini dapat dibuat dengan memilih opsi `Code` pada versi fork repo ini dan memilih opsi **Codespaces**.

![Dialog yang menunjukkan tombol untuk membuat codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Menyimpan API Keys Anda

Menjaga keamanan API keys sangat penting saat membangun aplikasi apapun. Kami menyarankan untuk tidak menyimpan API keys langsung di dalam kode Anda. Meng-commit detail tersebut ke repositori publik bisa menimbulkan masalah keamanan dan bahkan biaya tak terduga jika disalahgunakan oleh pihak yang tidak bertanggung jawab.  
Berikut panduan langkah demi langkah cara membuat file `.env` untuk Python dan menambahkan `GITHUB_TOKEN`:

1. **Masuk ke Direktori Proyek Anda**: Buka terminal atau command prompt dan masuk ke direktori root proyek Anda tempat Anda ingin membuat file `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Buat File `.env`**: Gunakan editor teks favorit Anda untuk membuat file baru bernama `.env`. Jika menggunakan command line, Anda bisa menggunakan `touch` (pada sistem berbasis Unix) atau `echo` (pada Windows):

   Sistem berbasis Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit File `.env`**: Buka file `.env` di editor teks (misalnya VS Code, Notepad++, atau editor lain). Tambahkan baris berikut, ganti `your_github_token_here` dengan token GitHub Anda yang sebenarnya:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Simpan File**: Simpan perubahan dan tutup editor teks.

5. **Pasang `python-dotenv`**: Jika belum, Anda perlu memasang paket `python-dotenv` untuk memuat variabel lingkungan dari file `.env` ke aplikasi Python Anda. Anda bisa memasangnya menggunakan `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Muat Variabel Lingkungan di Skrip Python Anda**: Dalam skrip Python, gunakan paket `python-dotenv` untuk memuat variabel lingkungan dari file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Selesai! Anda telah berhasil membuat file `.env`, menambahkan token GitHub, dan memuatnya ke aplikasi Python Anda.

## Cara Menjalankan secara lokal di komputer Anda

Untuk menjalankan kode secara lokal di komputer Anda, Anda perlu memasang versi [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Kemudian, untuk menggunakan repositori, Anda perlu meng-clone-nya:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Setelah semuanya siap, Anda bisa mulai!

## Langkah Opsional

### Memasang Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) adalah installer ringan untuk memasang [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, serta beberapa paket.  
Conda sendiri adalah manajer paket yang memudahkan pengaturan dan pergantian antara berbagai [**virtual environment**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) dan paket Python. Ini juga berguna untuk memasang paket yang tidak tersedia lewat `pip`.

Anda bisa mengikuti [panduan pemasangan MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) untuk mengaturnya.

Setelah Miniconda terpasang, Anda perlu meng-clone [repositori](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jika belum).

Selanjutnya, buat virtual environment. Untuk ini dengan Conda, buat file environment baru (_environment.yml_). Jika mengikuti menggunakan Codespaces, buat di dalam direktori `.devcontainer`, jadi `.devcontainer/environment.yml`.

Isi file environment Anda dengan potongan kode berikut:

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

Jika Anda mengalami error saat menggunakan conda, Anda bisa memasang Microsoft AI Libraries secara manual dengan perintah berikut di terminal.

```
conda install -c microsoft azure-ai-ml
```

File environment ini menentukan dependensi yang dibutuhkan. `<environment-name>` adalah nama yang ingin Anda gunakan untuk environment Conda Anda, dan `<python-version>` adalah versi Python yang ingin Anda gunakan, misalnya `3` adalah versi mayor terbaru Python.

Setelah itu, Anda bisa membuat environment Conda dengan menjalankan perintah berikut di command line/terminal Anda

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Lihat panduan [Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika mengalami masalah.

### Menggunakan Visual Studio Code dengan ekstensi dukungan Python

Kami menyarankan menggunakan editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) dengan [ekstensi dukungan Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) yang terpasang untuk kursus ini. Namun, ini hanya rekomendasi, bukan persyaratan mutlak.

> **Catatan**: Dengan membuka repositori kursus di VS Code, Anda bisa memilih untuk mengatur proyek dalam sebuah container. Ini karena adanya direktori khusus [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) di dalam repositori kursus. Akan dibahas lebih lanjut nanti.

> **Catatan**: Setelah Anda clone dan buka direktori di VS Code, secara otomatis akan menyarankan memasang ekstensi dukungan Python.

> **Catatan**: Jika VS Code menyarankan membuka ulang repositori dalam container, tolak permintaan ini agar menggunakan versi Python yang terpasang secara lokal.

### Menggunakan Jupyter di Browser

Anda juga bisa mengerjakan proyek menggunakan lingkungan [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) langsung di browser Anda. Baik Jupyter klasik maupun [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) menyediakan lingkungan pengembangan yang nyaman dengan fitur seperti auto-completion, penyorotan kode, dan lain-lain.

Untuk memulai Jupyter secara lokal, buka terminal/command line, masuk ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulai instance Jupyter dan URL untuk mengaksesnya akan ditampilkan di jendela command line.

Setelah mengakses URL tersebut, Anda akan melihat garis besar kursus dan bisa membuka file `*.ipynb` mana pun. Misalnya, `08-building-search-applications/python/oai-solution.ipynb`.

### Menjalankan dalam container

Alternatif lain selain mengatur semuanya di komputer atau Codespace adalah menggunakan [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Folder khusus `.devcontainer` di dalam repositori kursus memungkinkan VS Code mengatur proyek dalam container. Di luar Codespaces, ini memerlukan pemasangan Docker, dan jujur saja, ini agak rumit, jadi kami sarankan hanya untuk yang sudah berpengalaman dengan container.

Salah satu cara terbaik menjaga keamanan API keys saat menggunakan GitHub Codespaces adalah dengan menggunakan Codespace Secrets. Silakan ikuti panduan [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) untuk mempelajari lebih lanjut.

## Pelajaran dan Persyaratan Teknis

Kursus ini memiliki 6 pelajaran konsep dan 6 pelajaran coding.

Untuk pelajaran coding, kami menggunakan Azure OpenAI Service. Anda perlu akses ke layanan Azure OpenAI dan API key untuk menjalankan kode ini. Anda bisa mengajukan akses dengan [mengisi aplikasi ini](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Sambil menunggu aplikasi Anda diproses, setiap pelajaran coding juga menyertakan file `README.md` tempat Anda bisa melihat kode dan hasilnya.

## Menggunakan Azure OpenAI Service untuk pertama kali

Jika ini pertama kali Anda menggunakan Azure OpenAI service, silakan ikuti panduan ini tentang cara [membuat dan menerapkan resource Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Menggunakan OpenAI API untuk pertama kali

Jika ini pertama kali Anda menggunakan OpenAI API, silakan ikuti panduan tentang cara [membuat dan menggunakan Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Bertemu dengan Pelajar Lain

Kami telah membuat saluran di server resmi [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) untuk bertemu pelajar lain. Ini adalah cara yang bagus untuk berjejaring dengan pengusaha, pembangun, pelajar, dan siapa saja yang ingin meningkatkan kemampuan di Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tim proyek juga akan hadir di server Discord ini untuk membantu para pelajar.

## Berkontribusi

Kursus ini adalah inisiatif open-source. Jika Anda menemukan area yang bisa diperbaiki atau masalah, silakan buat [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) atau laporkan [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tim proyek akan memantau semua kontribusi. Berkontribusi ke open source adalah cara luar biasa untuk membangun karier Anda di Generative AI.

Sebagian besar kontribusi mengharuskan Anda menyetujui Contributor License Agreement (CLA) yang menyatakan bahwa Anda memiliki hak dan memang memberikan kami hak untuk menggunakan kontribusi Anda. Untuk detail, kunjungi [situs CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Penting: saat menerjemahkan teks di repo ini, pastikan Anda tidak menggunakan terjemahan mesin. Kami akan memverifikasi terjemahan melalui komunitas, jadi harap hanya sukarela menerjemahkan ke bahasa yang Anda kuasai.

Saat Anda mengirim pull request, CLA-bot akan secara otomatis menentukan apakah Anda perlu menyediakan CLA dan menandai PR dengan tepat (misalnya label, komentar). Cukup ikuti instruksi dari bot. Anda hanya perlu melakukan ini sekali untuk semua repositori yang menggunakan CLA kami.

Proyek ini mengadopsi [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Untuk informasi lebih lanjut, baca FAQ Code of Conduct atau hubungi [Email opencode](opencode@microsoft.com) untuk pertanyaan atau komentar tambahan.

## Mari Mulai

Sekarang setelah Anda menyelesaikan langkah-langkah yang diperlukan untuk mengikuti kursus ini, mari mulai dengan mendapatkan [pengantar tentang Generative AI dan LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.