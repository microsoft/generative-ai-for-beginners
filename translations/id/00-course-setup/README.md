# Memulai dengan kursus ini

Kami sangat bersemangat Anda memulai kursus ini dan melihat apa yang akan Anda inspirasikan untuk dibangun dengan Generative AI!

Untuk memastikan keberhasilan Anda, halaman ini menjelaskan langkah-langkah pengaturan, persyaratan teknis, dan tempat untuk mendapatkan bantuan jika diperlukan.

## Langkah Pengaturan

Untuk mulai mengikuti kursus ini, Anda perlu menyelesaikan langkah-langkah berikut.

### 1. Fork Repo ini

[Fork seluruh repositori ini](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ke akun GitHub Anda sendiri agar dapat mengubah kode dan menyelesaikan tantangan. Anda juga bisa [menandai (🌟) repo ini](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) agar mudah ditemukan bersama dengan repo terkait lainnya.

### 2. Buat codespace

Untuk menghindari masalah dependensi saat menjalankan kode, kami merekomendasikan menjalankan kursus ini di [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Di fork Anda: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/id/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Tambahkan secret

1. ⚙️ Ikon gear -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Beri nama OPENAI_API_KEY, tempel kunci Anda, Simpan.

### 3. Apa yang berikutnya?

| Saya ingin…          | Pergi ke…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Mulai Pelajaran 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Bekerja offline     | [`setup-local.md`](02-setup-local.md)                                   |
| Menyiapkan Penyedia LLM | [`providers.md`](03-providers.md)                                        |
| Bertemu pelajar lain | [Bergabung di Discord kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Pemecahan Masalah


| Gejala                                   | Solusi                                                          |
|------------------------------------------|-----------------------------------------------------------------|
| Proses build container terhenti > 10 menit | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal tidak terpasang; klik **+** ➜ *bash*                   |
| `401 Unauthorized` dari OpenAI            | `OPENAI_API_KEY` salah / kadaluwarsa                            |
| VS Code menunjukkan “Dev container mounting…” | Segarkan tab browser—Codespaces kadang kehilangan koneksi      |
| Kernel notebook hilang                     | Menu notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Sistem berbasis Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit File `.env`**: Buka file `.env` di editor teks (misalnya, VS Code, Notepad++, atau editor lainnya). Tambahkan baris berikut ke dalam file, ganti placeholder dengan endpoint dan kunci Microsoft Foundry Models Anda yang sebenarnya (lihat [`providers.md`](03-providers.md) untuk cara mendapatkannya):

   > **Catatan:** GitHub Models (dan variabel `GITHUB_TOKEN`-nya) akan dihentikan pada akhir Juli 2026. Gunakan [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) sebagai gantinya.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Simpan File**: Simpan perubahan dan tutup editor teks.

5. **Pasang `python-dotenv`**: Jika belum, Anda perlu memasang paket `python-dotenv` untuk memuat variabel lingkungan dari file `.env` ke aplikasi Python Anda. Anda bisa memasangnya menggunakan `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Muat Variabel Lingkungan di Skrip Python Anda**: Dalam skrip Python Anda, gunakan paket `python-dotenv` untuk memuat variabel lingkungan dari file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Muat variabel lingkungan dari file .env
   load_dotenv()

   # Akses variabel Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Itu saja! Anda telah berhasil membuat file `.env`, menambahkan kredensial Microsoft Foundry Models, dan memuatnya ke aplikasi Python Anda.

## Cara Menjalankan secara lokal di komputer Anda

Untuk menjalankan kode secara lokal di komputer Anda, Anda perlu menginstal beberapa versi [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Untuk kemudian menggunakan repositori, Anda perlu mengkloningnya:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Setelah semuanya diunduh, Anda bisa mulai!

## Langkah Opsional

### Memasang Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) adalah installer ringan untuk memasang [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, serta beberapa paket.
Conda sendiri adalah manajer paket yang memudahkan untuk mengatur dan berganti antara [**virtual environment**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python dan paket-paket. Ini juga berguna untuk memasang paket yang tidak tersedia via `pip`.

Anda dapat mengikuti [panduan pemasangan MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) untuk mengaturnya.

Setelah Miniconda terpasang, Anda perlu mengkloning [repositori](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jika belum).

Selanjutnya, Anda perlu membuat lingkungan virtual. Untuk melakukannya dengan Conda, buat file lingkungan baru (_environment.yml_). Jika mengikuti dengan Codespaces, buat ini di dalam direktori `.devcontainer`, jadi `.devcontainer/environment.yml`.

Silakan isi file lingkungan Anda dengan potongan berikut:

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

Jika Anda mengalami kesalahan saat menggunakan conda, Anda dapat memasang pustaka AI Microsoft secara manual menggunakan perintah berikut di terminal.

```
conda install -c microsoft azure-ai-ml
```

File lingkungan menentukan dependensi yang kita perlukan. `<environment-name>` adalah nama yang ingin Anda gunakan untuk lingkungan Conda Anda, dan `<python-version>` adalah versi Python yang ingin Anda gunakan, misalnya, `3` adalah versi utama Python terbaru.

Setelah itu, Anda dapat membuat lingkungan Conda dengan menjalankan perintah berikut di command line/terminal Anda

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # path .devcontainer hanya berlaku untuk pengaturan Codespace saja
conda activate ai4beg
```

Lihat [panduan lingkungan Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika Anda mengalami masalah.

### Menggunakan Visual Studio Code dengan ekstensi dukungan Python

Kami merekomendasikan menggunakan editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) dengan [ekstensi dukungan Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) yang terpasang untuk kursus ini. Namun, ini hanyalah rekomendasi dan bukan persyaratan mutlak.

> **Catatan**: Dengan membuka repositori kursus di VS Code, Anda dapat mengatur proyek dalam sebuah container. Ini karena adanya direktori [`.devcontainer` khusus](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) di dalam repositori kursus. Akan kami bahas lebih lanjut nanti.

> **Catatan**: Setelah Anda mengkloning dan membuka direktori di VS Code, secara otomatis akan menyarankan Anda memasang ekstensi dukungan Python.

> **Catatan**: Jika VS Code menyarankan Anda membuka kembali repositori dalam container, tolak permintaan ini agar dapat menggunakan Python versi lokal yang sudah terpasang.

### Menggunakan Jupyter dalam Browser

Anda juga dapat mengerjakan proyek menggunakan lingkungan [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) langsung di browser Anda. Baik Jupyter klasik maupun [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) menawarkan lingkungan pengembangan yang nyaman dengan fitur seperti auto-completion, penyorotan kode, dan lain-lain.

Untuk memulai Jupyter secara lokal, buka terminal/command line, masuk ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulai instance Jupyter dan URL untuk mengaksesnya akan ditampilkan di jendela command line.

Setelah Anda mengakses URL tersebut, Anda akan melihat garis besar kursus dan dapat menjelajahi file `*.ipynb`. Misalnya, `08-building-search-applications/python/oai-solution.ipynb`.

### Menjalankan dalam container

Alternatif selain mengatur semuanya di komputer atau Codespace Anda adalah menggunakan [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Folder khusus `.devcontainer` di dalam repositori kursus memungkinkan VS Code untuk mengatur proyek dalam container. Di luar Codespaces, ini membutuhkan pemasangan Docker, dan jujur saja, ini memerlukan sedikit usaha, jadi kami sarankan hanya untuk yang sudah berpengalaman dengan container.

Salah satu cara terbaik untuk menjaga keamanan kunci API Anda saat menggunakan GitHub Codespaces adalah dengan menggunakan Codespace Secrets. Silakan ikuti panduan [pengelolaan secrets di Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) untuk mempelajari lebih lanjut.


## Pelajaran dan Persyaratan Teknis

Kursus ini memiliki 6 pelajaran konsep dan 6 pelajaran pemrograman.

Untuk pelajaran pemrograman, kami menggunakan Azure OpenAI Service. Anda akan memerlukan akses ke layanan Azure OpenAI dan kunci API untuk menjalankan kode ini. Anda bisa mengajukan akses dengan [mengisi aplikasi ini](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Saat menunggu aplikasi Anda diproses, setiap pelajaran pemrograman juga menyertakan file `README.md` di mana Anda bisa melihat kode dan hasilnya.

## Menggunakan Azure OpenAI Service untuk pertama kali

Jika ini pertama kali Anda bekerja dengan layanan Azure OpenAI, silakan ikuti panduan ini tentang cara [membuat dan menerapkan sumber daya Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Menggunakan OpenAI API untuk pertama kali

Jika ini pertama kali Anda bekerja dengan OpenAI API, silakan ikuti panduan tentang cara [membuat dan menggunakan Antarmuka.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Bertemu Pelajar Lain

Kami telah membuat saluran di [server AI Community Discord resmi kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) untuk bertemu pelajar lain. Ini adalah cara yang bagus untuk berjejaring dengan pengusaha, pembangun, pelajar, dan siapa saja yang ingin meningkatkan kemampuan di Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tim proyek juga akan ada di server Discord ini untuk membantu setiap pelajar.

## Berkontribusi

Kursus ini adalah inisiatif open-source. Jika Anda melihat area yang perlu perbaikan atau masalah, silakan buat [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) atau catat [isu GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tim proyek akan melacak semua kontribusi. Berkontribusi ke open source adalah cara luar biasa untuk membangun karir Anda di bidang Generative AI.

Sebagian besar kontribusi memerlukan Anda menyetujui Perjanjian Lisensi Kontributor (CLA) yang menyatakan bahwa Anda memiliki hak dan memang memberikan hak kepada kami untuk menggunakan kontribusi Anda. Untuk detailnya, kunjungi [CLA, situs Perjanjian Lisensi Kontributor](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Penting: saat menerjemahkan teks di repo ini, pastikan Anda tidak menggunakan terjemahan mesin. Kami akan memverifikasi terjemahan melalui komunitas, jadi harap hanya menjadi relawan untuk terjemahan dalam bahasa yang Anda kuasai.

Saat Anda mengirim pull request, bot CLA akan secara otomatis menentukan apakah Anda perlu menyediakan CLA dan menghias PR dengan tepat (misalnya, label, komentar). Cukup ikuti instruksi yang diberikan bot. Anda hanya perlu melakukan ini sekali di semua repositori yang menggunakan CLA kami.


Proyek ini telah mengadopsi [Kode Etik Open Source Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Untuk informasi lebih lanjut baca FAQ Kode Etik atau hubungi [Email opencode](opencode@microsoft.com) jika ada pertanyaan atau komentar tambahan.

## Mari Kita Mulai

Sekarang setelah Anda menyelesaikan langkah-langkah yang diperlukan untuk menyelesaikan kursus ini, mari kita mulai dengan mendapatkan [pengantar tentang Generative AI dan LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->