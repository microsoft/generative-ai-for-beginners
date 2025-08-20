<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:14:11+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ms"
}
-->
# Memulakan Kursus Ini

Kami sangat teruja anda memulakan kursus ini dan melihat apa yang anda akan terinspirasi untuk bina dengan Generative AI!

Untuk memastikan kejayaan anda, halaman ini menggariskan langkah-langkah persediaan, keperluan teknikal, dan di mana untuk mendapatkan bantuan jika perlu.

## Langkah Persediaan

Untuk mula mengikuti kursus ini, anda perlu melengkapkan langkah-langkah berikut.

### 1. Fork Repo Ini

[Fork keseluruhan repo ini](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ke akaun GitHub anda sendiri supaya anda boleh mengubah sebarang kod dan melengkapkan cabaran. Anda juga boleh [menandakan (🌟) repo ini](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) untuk memudahkan pencarian repo ini dan repo berkaitan.

### 2. Cipta codespace

Untuk mengelakkan sebarang isu pergantungan semasa menjalankan kod, kami mengesyorkan menjalankan kursus ini dalam [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Ini boleh dicipta dengan memilih pilihan `Code` pada versi fork repo ini dan memilih pilihan **Codespaces**.

![Dialog menunjukkan butang untuk mencipta codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Menyimpan Kunci API Anda

Menjaga kunci API anda dengan selamat adalah penting apabila membina sebarang jenis aplikasi. Kami mengesyorkan supaya tidak menyimpan kunci API secara terus dalam kod anda. Melakukan commit maklumat tersebut ke repositori awam boleh menyebabkan isu keselamatan dan juga kos yang tidak diingini jika digunakan oleh pihak yang tidak bertanggungjawab.  
Berikut adalah panduan langkah demi langkah tentang cara mencipta fail `.env` untuk Python dan menambah `GITHUB_TOKEN`:

1. **Pergi ke Direktori Projek Anda**: Buka terminal atau command prompt dan pergi ke direktori root projek anda di mana anda ingin mencipta fail `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Cipta Fail `.env`**: Gunakan editor teks pilihan anda untuk mencipta fail baru bernama `.env`. Jika menggunakan baris arahan, anda boleh gunakan `touch` (pada sistem berasaskan Unix) atau `echo` (pada Windows):

   Sistem berasaskan Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit Fail `.env`**: Buka fail `.env` dalam editor teks (contohnya, VS Code, Notepad++, atau editor lain). Tambah baris berikut ke dalam fail, gantikan `your_github_token_here` dengan token GitHub sebenar anda:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Simpan Fail**: Simpan perubahan dan tutup editor teks.

5. **Pasang `python-dotenv`**: Jika anda belum memasangnya, anda perlu pasang pakej `python-dotenv` untuk memuatkan pembolehubah persekitaran dari fail `.env` ke dalam aplikasi Python anda. Anda boleh pasang menggunakan `pip`:

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

Selesai! Anda telah berjaya mencipta fail `.env`, menambah token GitHub anda, dan memuatkannya ke dalam aplikasi Python anda.

## Cara Menjalankan Secara Tempatan di Komputer Anda

Untuk menjalankan kod secara tempatan di komputer anda, anda perlu memasang versi [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Kemudian, untuk menggunakan repositori, anda perlu clone ia:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Setelah semuanya siap, anda boleh mula!

## Langkah Pilihan

### Memasang Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) adalah pemasang ringan untuk memasang [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, serta beberapa pakej.  
Conda sendiri adalah pengurus pakej yang memudahkan penyediaan dan pertukaran antara [persekitaran maya](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python dan pakej. Ia juga berguna untuk memasang pakej yang tidak tersedia melalui `pip`.

Anda boleh ikut [panduan pemasangan MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) untuk memasangnya.

Setelah Miniconda dipasang, anda perlu clone [repositori](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jika belum).

Seterusnya, anda perlu mencipta persekitaran maya. Untuk melakukan ini dengan Conda, teruskan dan cipta fail persekitaran baru (_environment.yml_). Jika anda mengikuti menggunakan Codespaces, cipta fail ini dalam direktori `.devcontainer`, iaitu `.devcontainer/environment.yml`.

Isikan fail persekitaran anda dengan petikan di bawah:

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

Jika anda menghadapi ralat menggunakan conda, anda boleh pasang secara manual Microsoft AI Libraries menggunakan arahan berikut dalam terminal.

```
conda install -c microsoft azure-ai-ml
```

Fail persekitaran menentukan kebergantungan yang diperlukan. `<environment-name>` merujuk kepada nama yang anda ingin gunakan untuk persekitaran Conda anda, dan `<python-version>` adalah versi Python yang anda ingin gunakan, contohnya, `3` adalah versi utama terkini Python.

Setelah itu, anda boleh terus mencipta persekitaran Conda anda dengan menjalankan arahan di bawah dalam baris arahan/terminal anda

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Rujuk [panduan persekitaran Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika anda menghadapi sebarang masalah.

### Menggunakan Visual Studio Code dengan sambungan sokongan Python

Kami mengesyorkan menggunakan editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) dengan [sambungan sokongan Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) yang dipasang untuk kursus ini. Namun, ini hanyalah cadangan dan bukan keperluan mutlak.

> **Nota**: Dengan membuka repositori kursus dalam VS Code, anda mempunyai pilihan untuk menyediakan projek dalam sebuah container. Ini kerana terdapat direktori [`.devcontainer` khas](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dalam repositori kursus. Kami akan terangkan lebih lanjut kemudian.

> **Nota**: Setelah anda clone dan buka direktori dalam VS Code, ia akan secara automatik mencadangkan anda memasang sambungan sokongan Python.

> **Nota**: Jika VS Code mencadangkan anda membuka semula repositori dalam container, tolak permintaan ini untuk menggunakan versi Python yang dipasang secara tempatan.

### Menggunakan Jupyter dalam Pelayar

Anda juga boleh bekerja pada projek menggunakan persekitaran [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) terus dalam pelayar anda. Kedua-dua Jupyter klasik dan [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) menyediakan persekitaran pembangunan yang mesra dengan ciri seperti auto-completion, penyorotan kod, dan lain-lain.

Untuk memulakan Jupyter secara tempatan, buka terminal/command line, pergi ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulakan instans Jupyter dan URL untuk mengaksesnya akan dipaparkan dalam tetingkap command line.

Setelah anda akses URL tersebut, anda akan melihat garis panduan kursus dan boleh melayari mana-mana fail `*.ipynb`. Contohnya, `08-building-search-applications/python/oai-solution.ipynb`.

### Menjalankan dalam container

Alternatif kepada menyediakan semuanya di komputer atau Codespace anda adalah menggunakan [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Folder `.devcontainer` khas dalam repositori kursus membolehkan VS Code menyediakan projek dalam container. Di luar Codespaces, ini memerlukan pemasangan Docker, dan secara jujurnya, ia memerlukan sedikit usaha, jadi kami mengesyorkan ini hanya untuk mereka yang berpengalaman bekerja dengan container.

Salah satu cara terbaik untuk menjaga kunci API anda selamat semasa menggunakan GitHub Codespaces adalah dengan menggunakan Codespace Secrets. Sila ikut panduan [pengurusan rahsia Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) untuk maklumat lanjut.

## Pelajaran dan Keperluan Teknikal

Kursus ini mempunyai 6 pelajaran konsep dan 6 pelajaran pengkodan.

Untuk pelajaran pengkodan, kami menggunakan Azure OpenAI Service. Anda perlu mempunyai akses ke perkhidmatan Azure OpenAI dan kunci API untuk menjalankan kod ini. Anda boleh memohon akses dengan [melengkapkan permohonan ini](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Sementara menunggu permohonan anda diproses, setiap pelajaran pengkodan juga termasuk fail `README.md` di mana anda boleh melihat kod dan output.

## Menggunakan Azure OpenAI Service buat kali pertama

Jika ini kali pertama anda bekerja dengan perkhidmatan Azure OpenAI, sila ikut panduan ini tentang cara [mencipta dan menyebarkan sumber Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Menggunakan OpenAI API buat kali pertama

Jika ini kali pertama anda bekerja dengan OpenAI API, sila ikut panduan tentang cara [mencipta dan menggunakan Antara Muka.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Berjumpa dengan Pelajar Lain

Kami telah mencipta saluran dalam [server Discord Komuniti AI rasmi](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) kami untuk bertemu pelajar lain. Ini adalah cara yang bagus untuk berhubung dengan usahawan, pembina, pelajar, dan sesiapa sahaja yang ingin meningkatkan kemahiran dalam Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Pasukan projek juga akan berada di server Discord ini untuk membantu mana-mana pelajar.

## Menyumbang

Kursus ini adalah inisiatif sumber terbuka. Jika anda melihat ruang untuk penambahbaikan atau isu, sila cipta [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) atau log [isu GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Pasukan projek akan memantau semua sumbangan. Menyumbang kepada sumber terbuka adalah cara yang hebat untuk membina kerjaya anda dalam Generative AI.

Kebanyakan sumbangan memerlukan anda bersetuju dengan Perjanjian Lesen Penyumbang (CLA) yang menyatakan bahawa anda mempunyai hak dan benar-benar memberi kami hak untuk menggunakan sumbangan anda. Untuk maklumat lanjut, lawati [laman web CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Penting: apabila menterjemah teks dalam repo ini, pastikan anda tidak menggunakan terjemahan mesin. Kami akan mengesahkan terjemahan melalui komuniti, jadi sila hanya sukarela untuk terjemahan dalam bahasa yang anda mahir.

Apabila anda menghantar pull request, bot CLA akan secara automatik menentukan sama ada anda perlu menyediakan CLA dan menghias PR dengan sewajarnya (contohnya, label, komen). Ikut sahaja arahan yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali sahaja untuk semua repositori yang menggunakan CLA kami.

Projek ini telah mengamalkan [Kod Etika Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Untuk maklumat lanjut, baca FAQ Kod Etika atau hubungi [Email opencode](opencode@microsoft.com) untuk sebarang soalan atau komen tambahan.

## Mari Mula

Sekarang anda telah melengkapkan langkah-langkah yang diperlukan untuk menamatkan kursus ini, mari kita mulakan dengan mendapatkan [pengenalan kepada Generative AI dan LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.