# Memulai dengan kursus ini

Kami sangat antusias Anda memulai kursus ini dan melihat apa yang menginspirasi Anda untuk membangun dengan Generative AI!

Untuk memastikan keberhasilan Anda, halaman ini menguraikan langkah-langkah pengaturan, persyaratan teknis, dan di mana mendapatkan bantuan jika diperlukan.

## Langkah Pengaturan

Untuk mulai mengikuti kursus ini, Anda perlu menyelesaikan langkah-langkah berikut.

### 1. Fork Repo ini

[Fork seluruh repo ini](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ke akun GitHub Anda sendiri agar dapat mengubah kode dan menyelesaikan tantangan. Anda juga dapat [menandai (🌟) repo ini](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) agar lebih mudah menemukannya dan repo terkait.

### 2. Buat codespace

Untuk menghindari masalah dependensi saat menjalankan kode, kami menyarankan menjalankan kursus ini di [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Dalam fork Anda: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/id/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Tambahkan secret

1. ⚙️ Ikon Gear -> Command Pallete-> Codespaces : Manage user secret -> Tambah secret baru.
2. Nama OPENAI_API_KEY, tempel kunci Anda, Simpan.

### 3. Apa selanjutnya?

| Saya ingin…          | Pergi ke…                                                                  |
|---------------------|---------------------------------------------------------------------------|
| Mulai Pelajaran 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)       |
| Bekerja offline      | [`setup-local.md`](02-setup-local.md)                                     |
| Mengatur Penyedia LLM | [`providers.md`](03-providers.md)                                          |
| Bertemu pelajar lain | [Bergabung dengan Discord kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Pemecahan Masalah


| Gejala                                   | Perbaikan                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| Pembangunan container terhenti > 10 menit | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal tidak terpasang; klik **+** ➜ *bash*                    |
| `401 Unauthorized` dari OpenAI            | `OPENAI_API_KEY` salah / kedaluwarsa                            |
| VS Code menunjukkan “Dev container mounting…” | Segarkan tab browser—Codespaces kadang kehilangan koneksi    |
| Kernel Notebook hilang                    | Menu Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Sistem berbasis Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit File `.env`**: Buka file `.env` di editor teks (misalnya VS Code, Notepad++, atau editor lain). Tambahkan baris berikut ke file, ganti `your_github_token_here` dengan token GitHub Anda yang sebenarnya:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Simpan File**: Simpan perubahan dan tutup editor teks.

5. **Pasang `python-dotenv`**: Jika Anda belum melakukannya, Anda perlu memasang paket `python-dotenv` untuk memuat variabel lingkungan dari file `.env` ke dalam aplikasi Python Anda. Instal menggunakan `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Muat Variabel Lingkungan di Skrip Python Anda**: Dalam skrip Python Anda, gunakan paket `python-dotenv` untuk memuat variabel lingkungan dari file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Muat variabel lingkungan dari file .env
   load_dotenv()

   # Akses variabel GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Selesai! Anda telah berhasil membuat file `.env`, menambahkan token GitHub, dan memuatnya ke dalam aplikasi Python Anda.

## Cara Menjalankan secara lokal di komputer Anda

Untuk menjalankan kode secara lokal di komputer Anda, Anda perlu memiliki beberapa versi [Python terpasang](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Untuk kemudian menggunakan repositori, Anda perlu mengkloningnya:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Setelah semuanya siap, Anda bisa mulai!

## Langkah Opsional

### Memasang Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) adalah pemasang ringan untuk memasang [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, serta beberapa paket.
Conda sendiri adalah manajer paket, yang memudahkan Anda mengatur dan beralih antar [**virtual environment**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) dan paket Python yang berbeda. Ini juga berguna untuk memasang paket yang tidak tersedia melalui `pip`.

Anda dapat mengikuti [panduan pemasangan MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) untuk mengaturnya.

Dengan Miniconda terpasang, Anda perlu mengkloning [repositori](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jika belum melakukannya)

Selanjutnya, Anda perlu membuat lingkungan virtual. Untuk melakukan ini dengan Conda, buatlah file environment baru (_environment.yml_). Jika Anda mengikuti dengan Codespaces, buat ini di dalam direktori `.devcontainer`, sehingga `.devcontainer/environment.yml`.

Isilah file environment Anda dengan potongan di bawah ini:

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

Jika Anda mengalami kesalahan saat menggunakan conda, Anda dapat memasang secara manual Microsoft AI Libraries dengan perintah berikut di terminal.

```
conda install -c microsoft azure-ai-ml
```

File environment menentukan dependensi yang kita butuhkan. `<environment-name>` adalah nama lingkungan Conda yang ingin Anda gunakan, dan `<python-version>` adalah versi Python yang ingin dipakai, misalnya `3` adalah versi utama Python terbaru.

Setelah selesai, Anda bisa membuat lingkungan Conda dengan menjalankan perintah di bawah ini pada command line/terminal Anda

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # sub path .devcontainer berlaku hanya untuk pengaturan Codespace
conda activate ai4beg
```

Lihat [panduan lingkungan Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika menemui masalah.

### Menggunakan Visual Studio Code dengan ekstensi dukungan Python

Kami menyarankan menggunakan editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) dengan [ekstensi dukungan Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) terpasang untuk kursus ini. Namun, ini hanya rekomendasi dan bukan persyaratan mutlak.

> **Catatan**: Dengan membuka repositori kursus di VS Code, Anda dapat mengatur proyek dalam container. Ini karena adanya direktori khusus [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) yang ada di repositori kursus. Akan dijelaskan lebih lanjut nanti.

> **Catatan**: Setelah mengkloning dan membuka direktori di VS Code, secara otomatis akan menyarankan Anda memasang ekstensi dukungan Python.

> **Catatan**: Jika VS Code menyarankan membukanya kembali dalam container, tolak permintaan ini agar menggunakan versi Python yang terpasang secara lokal.

### Menggunakan Jupyter di Browser

Anda juga dapat mengerjakan proyek menggunakan [lingkungan Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) langsung di browser Anda. Baik Jupyter klasik maupun [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) menyediakan lingkungan pengembangan yang nyaman dengan fitur seperti auto-completion, penyorotan kode, dll.

Untuk memulai Jupyter secara lokal, buka terminal/command line, navigasikan ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulai instance Jupyter dan URL untuk mengaksesnya akan ditampilkan dalam jendela command line.

Setelah mengakses URL tersebut, Anda akan melihat garis besar kursus dan dapat menavigasi ke file `*.ipynb` manapun. Sebagai contoh, `08-building-search-applications/python/oai-solution.ipynb`.

### Menjalankan dalam container

Alternatif lain selain menyiapkan semua di komputer atau Codespace Anda adalah menggunakan [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Folder khusus `.devcontainer` dalam repositori kursus memungkinkan VS Code mengatur proyek dalam container. Di luar Codespaces, ini memerlukan pemasangan Docker, dan sebenarnya ini cukup rumit, jadi kami sarankan hanya bagi yang berpengalaman dengan container.

Salah satu cara terbaik menjaga keamanan kunci API saat menggunakan GitHub Codespaces adalah dengan memakai Codespace Secrets. Silakan ikuti panduan [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) untuk mempelajarinya lebih lanjut.


## Pelajaran dan Persyaratan Teknis

Kursus ini memiliki 6 pelajaran konsep dan 6 pelajaran pemrograman.

Untuk pelajaran pemrograman, kami menggunakan Azure OpenAI Service. Anda memerlukan akses ke layanan Azure OpenAI dan kunci API untuk menjalankan kode ini. Anda dapat mendaftar aksesnya dengan [mengisi aplikasi ini](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Sambil menunggu proses aplikasi Anda selesai, setiap pelajaran pemrograman juga menyertakan file `README.md` tempat Anda dapat melihat kode dan hasilnya.

## Menggunakan Azure OpenAI Service untuk pertama kali

Jika ini kali pertama Anda menggunakan layanan Azure OpenAI, ikuti panduan ini tentang cara [membuat dan menerapkan sumber daya Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Menggunakan OpenAI API untuk pertama kali

Jika ini kali pertama Anda menggunakan OpenAI API, ikuti panduan tentang cara [membuat dan menggunakan Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Bertemu Pelajar Lain

Kami telah membuat saluran di server resmi [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) untuk bertemu pelajar lain. Ini adalah cara yang bagus untuk berjejaring dengan pengusaha, pembangun, pelajar, dan siapa saja yang ingin berkembang dalam Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tim proyek juga akan hadir di server Discord ini untuk membantu pelajar.

## Berkontribusi

Kursus ini merupakan inisiatif open-source. Jika Anda menemukan area yang dapat diperbaiki atau masalah, harap buat [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) atau laporkan [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tim proyek akan memantau semua kontribusi. Berkontribusi ke open source adalah cara luar biasa membangun karir Anda dalam Generative AI.

Sebagian besar kontribusi mengharuskan Anda menyetujui Contributor License Agreement (CLA) yang menyatakan bahwa Anda memiliki hak dan benar-benar memberi kami hak untuk menggunakan kontribusi Anda. Untuk detail, kunjungi [situs CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Penting: saat menerjemahkan teks dalam repo ini, pastikan Anda tidak menggunakan terjemahan mesin. Kami akan memverifikasi terjemahan melalui komunitas, jadi tolong sukarela hanya untuk bahasa yang Anda kuasai.

Saat Anda mengirim pull request, CLA-bot akan otomatis menentukan apakah Anda perlu memberikan CLA dan memberi tanda yang sesuai pada PR (misalnya, label, komentar). Cukup ikuti instruksi bot. Anda hanya perlu melakukannya sekali di semua repositori yang menggunakan CLA kami.

Proyek ini mengadopsi [Kode Etik Open Source Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Untuk informasi lebih lanjut baca FAQ Kode Etik atau hubungi [Email opencode](opencode@microsoft.com) untuk pertanyaan atau komentar tambahan.

## Mari Mulai
Sekarang setelah Anda menyelesaikan langkah-langkah yang diperlukan untuk menyelesaikan kursus ini, mari kita mulai dengan mendapatkan [pengantar tentang Generative AI dan LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah penafsiran yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->