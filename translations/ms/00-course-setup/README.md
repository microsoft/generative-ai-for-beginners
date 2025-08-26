<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T18:22:12+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ms"
}
-->
# Bermula dengan kursus ini

Kami sangat teruja untuk anda memulakan kursus ini dan melihat apa yang anda akan bina dengan AI Generatif!

Untuk memastikan kejayaan anda, halaman ini menerangkan langkah persediaan, keperluan teknikal, dan di mana untuk mendapatkan bantuan jika perlu.

## Langkah Persediaan

Untuk mula mengikuti kursus ini, anda perlu melengkapkan langkah-langkah berikut.

### 1. Fork Repo ini

[Fork keseluruhan repo ini](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ke akaun GitHub anda sendiri supaya anda boleh mengubah kod dan menyiapkan cabaran. Anda juga boleh [bintang (🌟) repo ini](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) untuk memudahkan anda mencari repo ini dan repo berkaitan lain.

### 2. Cipta codespace

Untuk mengelakkan sebarang isu kebergantungan semasa menjalankan kod, kami mengesyorkan anda menjalankan kursus ini dalam [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Dalam fork anda: **Code -> Codespaces -> New on main**

![Dialog menunjukkan butang untuk mencipta codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Tambah secret

1. ⚙️ Ikon gear -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Namakan OPENAI_API_KEY, tampal kunci anda, Simpan.

### 3.  Apa seterusnya?

| Saya ingin…         | Pergi ke…                                                                |
|---------------------|-------------------------------------------------------------------------|
| Mula Pelajaran 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Bekerja secara luar talian | [`setup-local.md`](02-setup-local.md)                            |
| Sediakan Penyedia LLM | [`providers.md`](providers.md)                                        |
| Bertemu pelajar lain | [Sertai Discord kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Penyelesaian Masalah

| Simptom                                   | Penyelesaian                                                    |
|-------------------------------------------|-----------------------------------------------------------------|
| Pembinaan container tersekat > 10 minit   | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal tidak bersambung; klik **+** ➜ *bash*                  |
| `401 Unauthorized` dari OpenAI            | `OPENAI_API_KEY` salah / tamat tempoh                           |
| VS Code menunjukkan “Dev container mounting…” | Segarkan tab pelayar—Codespaces kadang-kadang terputus sambungan|
| Kernel notebook tiada                     | Menu Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Sistem berasaskan Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit fail `.env`**: Buka fail `.env` dalam editor teks (cth. VS Code, Notepad++, atau mana-mana editor lain). Tambah baris berikut ke fail tersebut, gantikan `your_github_token_here` dengan token GitHub sebenar anda:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Simpan Fail**: Simpan perubahan dan tutup editor teks.

5. **Pasang `python-dotenv`**: Jika anda belum memasangnya, anda perlu memasang pakej `python-dotenv` untuk memuatkan pembolehubah persekitaran dari fail `.env` ke dalam aplikasi Python anda. Anda boleh memasangnya menggunakan `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Muatkan Pembolehubah Persekitaran dalam Skrip Python Anda**: Dalam skrip Python anda, gunakan pakej `python-dotenv` untuk memuatkan pembolehubah persekitaran dari fail `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Itu sahaja! Anda telah berjaya mencipta fail `.env`, menambah token GitHub anda, dan memuatkannya ke dalam aplikasi Python anda.

## Cara Menjalankan Secara Lokal di Komputer Anda

Untuk menjalankan kod secara lokal di komputer anda, anda perlu mempunyai [Python dipasang](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Untuk menggunakan repositori ini, anda perlu klonkan ia:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Setelah semuanya selesai, anda boleh mula!

## Langkah Pilihan

### Memasang Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ialah pemasang ringan untuk memasang [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, serta beberapa pakej.
Conda sendiri ialah pengurus pakej, yang memudahkan anda menyediakan dan bertukar antara [**persekitaran maya**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python dan pakej. Ia juga berguna untuk memasang pakej yang tidak tersedia melalui `pip`.

Anda boleh ikuti [panduan pemasangan MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) untuk memasangnya.

Selepas Miniconda dipasang, anda perlu klonkan [repositori](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ini (jika anda belum lakukannya).

Seterusnya, anda perlu mencipta persekitaran maya. Untuk melakukannya dengan Conda, cipta fail persekitaran baru (_environment.yml_). Jika anda mengikuti menggunakan Codespaces, cipta fail ini dalam direktori `.devcontainer`, iaitu `.devcontainer/environment.yml`.

Isikan fail persekitaran anda dengan kod di bawah:

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

Jika anda menghadapi ralat menggunakan conda, anda boleh pasang Microsoft AI Libraries secara manual menggunakan arahan berikut di terminal.

```
conda install -c microsoft azure-ai-ml
```

Fail persekitaran menentukan kebergantungan yang diperlukan. `<environment-name>` merujuk kepada nama yang anda ingin gunakan untuk persekitaran Conda anda, dan `<python-version>` ialah versi Python yang anda ingin gunakan, contohnya, `3` ialah versi utama Python terkini.

Setelah selesai, anda boleh cipta persekitaran Conda anda dengan menjalankan arahan di bawah dalam command line/terminal anda

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Rujuk [panduan persekitaran Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika anda menghadapi sebarang masalah.

### Menggunakan Visual Studio Code dengan sambungan sokongan Python

Kami mengesyorkan anda menggunakan editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) dengan [sambungan sokongan Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dipasang untuk kursus ini. Namun, ini hanyalah cadangan dan bukan keperluan wajib.

> **Nota**: Dengan membuka repositori kursus dalam VS Code, anda mempunyai pilihan untuk menyediakan projek dalam container. Ini kerana terdapat [direktori khas `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dalam repositori kursus. Akan diterangkan lebih lanjut kemudian.

> **Nota**: Setelah anda klon dan buka direktori dalam VS Code, ia akan secara automatik mencadangkan anda memasang sambungan sokongan Python.

> **Nota**: Jika VS Code mencadangkan anda membuka semula repositori dalam container, tolak permintaan ini untuk menggunakan versi Python yang dipasang secara lokal.

### Menggunakan Jupyter dalam Pelayar

Anda juga boleh bekerja pada projek ini menggunakan [persekitaran Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) terus dalam pelayar anda. Kedua-dua Jupyter klasik dan [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) menyediakan persekitaran pembangunan yang selesa dengan ciri seperti auto-lengkap, penyorotan kod, dan lain-lain.

Untuk memulakan Jupyter secara lokal, buka terminal/command line, navigasi ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulakan Jupyter dan URL untuk mengaksesnya akan dipaparkan dalam tetingkap command line.

Setelah anda akses URL tersebut, anda akan melihat rangka kursus dan boleh navigasi ke mana-mana fail `*.ipynb`. Contohnya, `08-building-search-applications/python/oai-solution.ipynb`.

### Menjalankan dalam container

Alternatif kepada menyediakan semuanya di komputer atau Codespace anda ialah menggunakan [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Folder khas `.devcontainer` dalam repositori kursus membolehkan VS Code menyediakan projek dalam container. Di luar Codespaces, ini memerlukan pemasangan Docker, dan secara jujurnya, ia agak rumit, jadi kami hanya mengesyorkan ini kepada mereka yang berpengalaman dengan container.

Salah satu cara terbaik untuk memastikan kunci API anda selamat semasa menggunakan GitHub Codespaces ialah dengan menggunakan Codespace Secrets. Sila ikuti [panduan pengurusan secrets Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) untuk maklumat lanjut.

## Pelajaran dan Keperluan Teknikal

Kursus ini mempunyai 6 pelajaran konsep dan 6 pelajaran pengekodan.

Untuk pelajaran pengekodan, kami menggunakan Azure OpenAI Service. Anda memerlukan akses ke Azure OpenAI service dan kunci API untuk menjalankan kod ini. Anda boleh memohon akses dengan [mengisi permohonan ini](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Sementara menunggu permohonan anda diproses, setiap pelajaran pengekodan juga disertakan dengan fail `README.md` di mana anda boleh melihat kod dan hasilnya.

## Menggunakan Azure OpenAI Service buat kali pertama

Jika ini kali pertama anda menggunakan Azure OpenAI service, sila ikuti panduan ini tentang cara [mencipta dan melancarkan sumber Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Menggunakan OpenAI API buat kali pertama

Jika ini kali pertama anda menggunakan OpenAI API, sila ikuti panduan tentang cara [mencipta dan menggunakan Antaramuka.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Bertemu Pelajar Lain

Kami telah mencipta saluran dalam [server Discord Komuniti AI rasmi kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) untuk anda bertemu pelajar lain. Ini adalah cara yang baik untuk berhubung dengan usahawan, pembina, pelajar, dan sesiapa sahaja yang ingin meningkatkan kemahiran dalam AI Generatif.

[![Sertai saluran discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Pasukan projek juga akan berada di server Discord ini untuk membantu para pelajar.

## Sumbangan

Kursus ini adalah inisiatif sumber terbuka. Jika anda melihat ruang untuk penambahbaikan atau isu, sila buat [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) atau log [isu GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Pasukan projek akan menjejak semua sumbangan. Menyumbang kepada sumber terbuka adalah cara yang hebat untuk membina kerjaya anda dalam AI Generatif.

Kebanyakan sumbangan memerlukan anda bersetuju dengan Contributor License Agreement (CLA) yang mengisytiharkan bahawa anda mempunyai hak dan benar-benar memberikan kami hak untuk menggunakan sumbangan anda. Untuk maklumat lanjut, lawati [laman web CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Penting: apabila menterjemah teks dalam repo ini, pastikan anda tidak menggunakan terjemahan mesin. Kami akan mengesahkan terjemahan melalui komuniti, jadi sila hanya sukarela untuk terjemahan dalam bahasa yang anda mahir.

Apabila anda menghantar pull request, CLA-bot akan secara automatik menentukan sama ada anda perlu menyediakan CLA dan menandakan PR dengan sewajarnya (cth., label, komen). Ikuti sahaja arahan yang diberikan oleh bot. Anda hanya perlu melakukannya sekali untuk semua repositori yang menggunakan CLA kami.

Projek ini telah menerima pakai [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Untuk maklumat lanjut baca Soalan Lazim Code of Conduct atau hubungi [Email opencode](opencode@microsoft.com) untuk sebarang soalan atau komen tambahan.

## Jom Mulakan
Sekarang setelah anda telah menyelesaikan langkah-langkah yang diperlukan untuk menamatkan kursus ini, mari kita mulakan dengan mendapatkan [pengenalan kepada AI Generatif dan LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.