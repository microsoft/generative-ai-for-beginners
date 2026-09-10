# Memulai dengan kursus ini

Kami sangat bersemangat Anda memulai kursus ini dan melihat apa yang menginspirasi Anda untuk membangun dengan Generative AI!

Untuk memastikan keberhasilan Anda, halaman ini menjelaskan langkah-langkah persiapan, persyaratan teknis, dan tempat mendapatkan bantuan jika diperlukan.

## Langkah Persiapan

Untuk mulai mengikuti kursus ini, Anda perlu menyelesaikan langkah-langkah berikut.

### 1. Fork Repo ini

[Fork seluruh repo ini](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ke akun GitHub Anda sendiri agar dapat mengubah kode dan menyelesaikan tantangan. Anda juga bisa [menandai (🌟) repo ini](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) agar lebih mudah menemukan repo ini dan yang terkait.

### 2. Buat sebuah codespace

Untuk menghindari masalah dependency saat menjalankan kode, kami menyarankan menjalankan kursus ini di [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Di fork Anda: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/id/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Tambahkan secret

1. ⚙️ Ikon roda gigi -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Nama OPENAI_API_KEY, tempelkan kunci Anda, Simpan.

### 3. Apa selanjutnya?

| Saya ingin…          | Pergi ke…                                                                |
|---------------------|-------------------------------------------------------------------------|
| Mulai Pelajaran 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Bekerja offline     | [`setup-local.md`](02-setup-local.md)                                   |
| Setup Penyedia LLM  | [`providers.md`](03-providers.md)                                        |
| Bertemu pelajar lain| [Gabung Discord kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Pemecahan Masalah


| Gejala                                   | Perbaikan                                                        |
|-----------------------------------------|-----------------------------------------------------------------|
| Build container terhenti > 10 menit    | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`             | Terminal tidak terpasang; klik **+** ➜ *bash*                    |
| `401 Unauthorized` dari OpenAI          | `OPENAI_API_KEY` salah / kadaluarsa                              |
| VS Code menunjukkan “Dev container mounting…” | Segarkan tab browser—Kadang Codespaces kehilangan koneksi     |
| Kernel notebook hilang                  | Menu Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Sistem berbasis Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit File `.env`**: Buka file `.env` di editor teks (misalnya, VS Code, Notepad++, atau editor lain). Tambahkan baris berikut, ganti placeholder dengan endpoint dan kunci Microsoft Foundry Models Anda yang sebenarnya (lihat [`providers.md`](03-providers.md) untuk cara mendapatkan keduanya):

   > **Catatan:** GitHub Models (dan variabel `GITHUB_TOKEN`) akan dihentikan pada akhir Juli 2026. Gunakan [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) sebagai gantinya.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Simpan File**: Simpan perubahan dan tutup editor teks.

5. **Pasang `python-dotenv`**: Jika belum, Anda harus memasang paket `python-dotenv` untuk memuat variabel lingkungan dari file `.env` ke aplikasi Python Anda. Anda bisa memasangnya menggunakan `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Muat Variabel Lingkungan dalam Skrip Python Anda**: Dalam skrip Python Anda, gunakan paket `python-dotenv` untuk memuat variabel lingkungan dari file `.env`:

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

Itu dia! Anda telah berhasil membuat file `.env`, menambahkan kredensial Microsoft Foundry Models Anda, dan memuatnya ke aplikasi Python Anda.

## Cara Menjalankan secara lokal di komputer Anda

Untuk menjalankan kode secara lokal di komputer Anda, Anda perlu memasang beberapa versi [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Untuk menggunakan repositori, Anda perlu meng-clone-nya:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Setelah semuanya terunduh, Anda bisa mulai!

## Langkah Opsional

### Memasang Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) adalah installer ringan untuk memasang [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, serta beberapa paket.
Conda sendiri adalah manajer paket yang memudahkan pengaturan dan perpindahan antara berbagai [environment virtual](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) dan paket Python. Juga berguna untuk memasang paket yang tidak tersedia lewat `pip`.

Anda bisa mengikuti [panduan pemasangan MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) untuk mengaturnya.

Setelah Miniconda terpasang, Anda perlu meng-clone [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jika belum).

Selanjutnya, Anda perlu membuat environment virtual. Untuk ini dengan Conda, buat file environment baru (_environment.yml_). Jika menggunakan Codespaces, buat file ini dalam direktori `.devcontainer`, jadi `.devcontainer/environment.yml`.

Silakan isi file environment Anda dengan potongan kode di bawah:

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

Jika Anda menemukan error saat menggunakan conda, Anda bisa memasang Microsoft AI Libraries secara manual dengan perintah berikut di terminal.

```
conda install -c microsoft azure-ai-ml
```

File environment menentukan dependensi yang diperlukan. `<environment-name>` adalah nama environment Conda yang ingin Anda gunakan, dan `<python-version>` adalah versi Python yang ingin Anda pakai, misalnya, `3` adalah versi utama Python terbaru.

Setelah itu, Anda bisa membuat environment Conda dengan menjalankan perintah di bawah di terminal/command line Anda

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # sub path .devcontainer hanya berlaku untuk pengaturan Codespace saja
conda activate ai4beg
```

Lihat [panduan lingkungan Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika mengalami masalah.

### Menggunakan Visual Studio Code dengan ekstensi dukungan Python

Kami menyarankan menggunakan editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) dengan ekstensi [dukungan Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) yang terpasang untuk kursus ini. Namun, ini hanyalah rekomendasi, bukan persyaratan mutlak.

> **Catatan**: Saat membuka repositori kursus di VS Code, Anda bisa mengatur proyek dalam container. Hal ini karena adanya direktori istimewa [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dalam repositori kursus. Akan dijelaskan lebih lanjut nanti.

> **Catatan**: Setelah Anda clone dan buka direktori di VS Code, biasanya akan otomatis menyarankan memasang ekstensi dukungan Python.

> **Catatan**: Jika VS Code menyarankan membuka ulang repositori dalam container, tolak permintaan ini jika ingin memakai versi Python yang dipasang secara lokal.

### Menggunakan Jupyter di Browser

Anda juga bisa bekerja pada proyek menggunakan lingkungan [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) langsung di browser Anda. Baik Jupyter klasik maupun [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) menyediakan lingkungan pengembangan yang menyenangkan dengan fitur seperti auto-completion, penyorotan kode, dll.

Untuk memulai Jupyter secara lokal, buka terminal/command line, masuk ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulai instance Jupyter dan URL aksesnya akan ditampilkan dalam jendela command line.

Setelah mengakses URL, Anda akan melihat garis besar kursus dan bisa menavigasi ke file `*.ipynb` mana saja. Misalnya, `08-building-search-applications/python/oai-solution.ipynb`.

### Menjalankan dalam container

Alternatif selain mengatur semuanya di komputer atau Codespace Anda adalah menggunakan [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Folder `.devcontainer` khusus dalam repositori kursus memungkinkan VS Code mengatur proyek dalam container. Di luar Codespaces, ini memerlukan instalasi Docker, dan memang cukup rumit, jadi kami hanya menyarankan ini bagi yang berpengalaman dengan container.

Salah satu cara terbaik menjaga keamanan kunci API Anda saat menggunakan GitHub Codespaces adalah memanfaatkan Codespace Secrets. Silakan ikuti panduan [pengelolaan secret di Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) ini untuk mempelajari lebih lanjut.


## Pelajaran dan Persyaratan Teknis

Kursus ini memiliki pelajaran "Belajar" yang menjelaskan konsep Generative AI dan pelajaran "Bangun" dengan contoh kode langsung dalam **Python** dan **TypeScript** jika memungkinkan.

Untuk pelajaran coding, kami menggunakan Azure OpenAI di Microsoft Foundry. Anda butuh langganan Azure dan kunci API. Akses terbuka - tanpa aplikasi, jadi Anda bisa [membuat sumber daya Microsoft Foundry dan menerapkan model](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) untuk mendapatkan endpoint dan kunci.

Setiap pelajaran coding juga menyertakan file `README.md` di mana Anda bisa melihat kode dan output tanpa perlu menjalankan apa pun.

## Menggunakan Azure OpenAI Service untuk pertama kali

Jika ini kali pertama Anda bekerja dengan layanan Azure OpenAI, silakan ikuti panduan ini tentang cara [membuat dan menerapkan sumber daya Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Menggunakan OpenAI API untuk pertama kali

Jika ini kali pertama Anda bekerja dengan OpenAI API, silakan ikuti panduan cara [membuat dan menggunakan Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Bertemu Pelajar Lain

Kami telah membuat saluran di [server Discord komunitas AI resmi](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) untuk bertemu pelajar lain. Ini adalah cara yang bagus untuk berjejaring dengan pengusaha, pembangun, pelajar, dan siapa pun yang ingin meningkatkan kemampuan di Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tim proyek juga akan ada di server Discord ini untuk membantu para pelajar.

## Berkontribusi

Kursus ini adalah inisiatif open-source. Jika Anda melihat area yang bisa diperbaiki atau ada masalah, silakan buat [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) atau laporkan [isu GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tim proyek akan memantau semua kontribusi. Berkontribusi pada open source adalah cara luar biasa membangun karier Anda dalam Generative AI.

Kebanyakan kontribusi mengharuskan Anda menyetujui Contributor License Agreement (CLA) yang menyatakan Anda berhak dan benar-benar memberikan kami hak menggunakan kontribusi Anda. Untuk detail, kunjungi [situs CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Penting: saat menerjemahkan teks di repo ini, pastikan Anda tidak menggunakan terjemahan mesin. Kami akan memverifikasi terjemahan melalui komunitas, jadi harap hanya jadi relawan untuk terjemahan dalam bahasa yang Anda kuasai.


Ketika Anda mengirim pull request, sebuah CLA-bot akan secara otomatis menentukan apakah Anda perlu menyediakan CLA dan menghias PR dengan tepat (misalnya, label, komentar). Cukup ikuti instruksi yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali di semua repositori yang menggunakan CLA kami.

Proyek ini telah mengadopsi [Kode Etik Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Untuk informasi lebih lanjut, baca FAQ Kode Etik atau hubungi [Email opencode](opencode@microsoft.com) untuk pertanyaan atau komentar tambahan.

## Mari kita Mulai

Sekarang setelah Anda menyelesaikan langkah-langkah yang diperlukan untuk menyelesaikan kursus ini, mari kita mulai dengan mendapatkan [pengenalan tentang Generative AI dan LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->