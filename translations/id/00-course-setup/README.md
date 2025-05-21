<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:32:22+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "id"
}
-->
# Memulai Kursus Ini

Kami sangat bersemangat untuk Anda memulai kursus ini dan melihat apa yang bisa Anda bangun dengan AI Generatif!

Untuk memastikan kesuksesan Anda, halaman ini menjelaskan langkah-langkah pengaturan, persyaratan teknis, dan di mana mendapatkan bantuan jika diperlukan.

## Langkah-langkah Pengaturan

Untuk mulai mengikuti kursus ini, Anda perlu menyelesaikan langkah-langkah berikut.

### 1. Fork Repositori Ini

[Fork seluruh repositori ini](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ke akun GitHub Anda sendiri agar bisa mengubah kode dan menyelesaikan tantangan. Anda juga bisa [memberi bintang (🌟) pada repositori ini](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) untuk menemukan repositori ini dan yang terkait lebih mudah.

### 2. Buat sebuah codespace

Untuk menghindari masalah ketergantungan saat menjalankan kode, kami merekomendasikan menjalankan kursus ini di [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Ini bisa dibuat dengan memilih opsi `Code` pada versi fork repositori Anda dan memilih opsi **Codespaces**.

![Dialog menunjukkan tombol untuk membuat codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Menyimpan Kunci API Anda

Menjaga kunci API Anda tetap aman dan terlindungi adalah penting saat membangun aplikasi apa pun. Kami merekomendasikan untuk tidak menyimpan kunci API secara langsung di dalam kode Anda. Mengkomit detail tersebut ke repositori publik dapat mengakibatkan masalah keamanan dan bahkan biaya yang tidak diinginkan jika digunakan oleh pihak yang tidak bertanggung jawab. Berikut panduan langkah demi langkah tentang cara membuat file `.env` untuk Python dan menambahkan `GITHUB_TOKEN`:

1. **Navigasi ke Direktori Proyek Anda**: Buka terminal atau command prompt Anda dan navigasi ke direktori root proyek Anda di mana Anda ingin membuat file `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Buat File `.env`**: Gunakan editor teks pilihan Anda untuk membuat file baru bernama `.env`. Jika Anda menggunakan command line, Anda bisa menggunakan `touch` (on Unix-based systems) or `echo` (pada Windows):

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

5. **Instal paket `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` untuk memuat variabel lingkungan dari file `.env` ke dalam aplikasi Python Anda. Anda dapat menginstalnya menggunakan `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Memuat Variabel Lingkungan dalam Skrip Python Anda**: Dalam skrip Python Anda, gunakan paket `python-dotenv` untuk memuat variabel lingkungan dari file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Itu dia! Anda telah berhasil membuat file `.env`, menambahkan token GitHub Anda, dan memuatnya ke dalam aplikasi Python Anda.

## Cara Menjalankan Secara Lokal di Komputer Anda

Untuk menjalankan kode secara lokal di komputer Anda, Anda perlu memiliki beberapa versi [Python terinstal](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Untuk kemudian menggunakan repositori, Anda perlu mengkloningnya:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Setelah Anda memeriksa semuanya, Anda bisa mulai!

## Langkah Opsional 

### Menginstal Miniconda 

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) adalah installer ringan untuk menginstal [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, serta beberapa paket.
Conda sendiri adalah pengelola paket, yang memudahkan untuk mengatur dan beralih antara berbagai [**lingkungan virtual**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python dan paket. Ini juga berguna untuk menginstal paket yang tidak tersedia melalui `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Silakan isi file lingkungan Anda dengan cuplikan di bawah ini:

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

Jika Anda mengalami kesalahan menggunakan conda, Anda dapat menginstal secara manual Microsoft AI Libraries menggunakan perintah berikut di terminal.

```
conda install -c microsoft azure-ai-ml
```

File lingkungan menentukan ketergantungan yang kita butuhkan. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` adalah versi utama terbaru dari Python.

Setelah selesai, Anda bisa melanjutkan dan membuat lingkungan Conda Anda dengan menjalankan perintah di bawah ini di command line/terminal Anda

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Lihat panduan [Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika Anda mengalami masalah.

### Menggunakan Visual Studio Code dengan ekstensi dukungan Python

Kami merekomendasikan menggunakan editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) dengan [ekstensi dukungan Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) yang terinstal untuk kursus ini. Namun, ini lebih merupakan rekomendasi dan bukan persyaratan pasti

> **Catatan**: Dengan membuka repositori kursus di VS Code, Anda memiliki opsi untuk mengatur proyek dalam sebuah container. Ini karena [direktori `.devcontainer` khusus](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) yang ditemukan di dalam repositori kursus. Lebih lanjut tentang ini nanti.

> **Catatan**: Setelah Anda mengkloning dan membuka direktori di VS Code, secara otomatis akan menyarankan Anda menginstal ekstensi dukungan Python.

> **Catatan**: Jika VS Code menyarankan Anda untuk membuka kembali repositori dalam container, tolak permintaan ini untuk menggunakan versi Python yang terinstal secara lokal.

### Menggunakan Jupyter di Browser

Anda juga bisa mengerjakan proyek menggunakan [lingkungan Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) langsung di dalam browser Anda. Baik Jupyter klasik maupun [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) menyediakan lingkungan pengembangan yang cukup menyenangkan dengan fitur-fitur seperti auto-completion, penyorotan kode, dll.

Untuk memulai Jupyter secara lokal, buka terminal/command line, navigasi ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulai instance Jupyter dan URL untuk mengaksesnya akan ditampilkan dalam jendela command line.

Setelah Anda mengakses URL tersebut, Anda harus melihat garis besar kursus dan dapat menavigasi ke file `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` di mana Anda dapat melihat kode dan output.

## Menggunakan Layanan Azure OpenAI untuk pertama kalinya

Jika ini adalah pertama kalinya Anda bekerja dengan layanan Azure OpenAI, silakan ikuti panduan ini tentang cara [membuat dan menerapkan sumber daya Layanan Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Menggunakan API OpenAI untuk pertama kalinya

Jika ini adalah pertama kalinya Anda bekerja dengan API OpenAI, silakan ikuti panduan tentang cara [membuat dan menggunakan Antarmuka.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Bertemu dengan Pembelajar Lain

Kami telah membuat saluran di server [AI Community Discord resmi](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) kami untuk bertemu dengan pembelajar lain. Ini adalah cara yang bagus untuk membangun jaringan dengan pengusaha, pembangun, pelajar, dan siapa saja yang berpikiran sama dan ingin meningkatkan keterampilan dalam AI Generatif.

[![Bergabung dengan saluran discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tim proyek juga akan berada di server Discord ini untuk membantu para pembelajar.

## Berkontribusi

Kursus ini adalah inisiatif sumber terbuka. Jika Anda melihat area yang perlu diperbaiki atau masalah, silakan buat [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) atau log [masalah GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tim proyek akan melacak semua kontribusi. Berkontribusi pada sumber terbuka adalah cara yang luar biasa untuk membangun karier Anda dalam AI Generatif.

Sebagian besar kontribusi mengharuskan Anda menyetujui Perjanjian Lisensi Kontributor (CLA) yang menyatakan bahwa Anda memiliki hak dan benar-benar memberikan kami hak untuk menggunakan kontribusi Anda. Untuk detail, kunjungi [situs web CLA, Perjanjian Lisensi Kontributor](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Penting: saat menerjemahkan teks dalam repositori ini, pastikan Anda tidak menggunakan terjemahan mesin. Kami akan memverifikasi terjemahan melalui komunitas, jadi mohon hanya menjadi sukarelawan untuk terjemahan dalam bahasa di mana Anda mahir.

Ketika Anda mengajukan permintaan tarik, CLA-bot akan secara otomatis menentukan apakah Anda perlu menyediakan CLA dan menghias PR dengan tepat (misalnya, label, komentar). Cukup ikuti instruksi yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali di semua repositori yang menggunakan CLA kami.

Proyek ini telah mengadopsi [Kode Etik Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Untuk informasi lebih lanjut baca FAQ Kode Etik atau hubungi [Email opencode](opencode@microsoft.com) dengan pertanyaan atau komentar tambahan.

## Mari Kita Mulai

Sekarang setelah Anda menyelesaikan langkah-langkah yang diperlukan untuk menyelesaikan kursus ini, mari kita mulai dengan mendapatkan [pengantar tentang AI Generatif dan LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai ketepatan, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.