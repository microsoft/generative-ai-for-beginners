<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:55:12+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ms"
}
-->
# Memulakan Kursus ini

Kami sangat teruja untuk anda memulakan kursus ini dan melihat apa yang anda terinspirasi untuk bina dengan AI Generatif!

Untuk memastikan kejayaan anda, halaman ini menerangkan langkah-langkah persediaan, keperluan teknikal, dan di mana untuk mendapatkan bantuan jika diperlukan.

## Langkah Persediaan

Untuk mula mengikuti kursus ini, anda perlu melengkapkan langkah-langkah berikut.

### 1. Fork Repositori ini

[Fork keseluruhan repositori ini](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ke akaun GitHub anda sendiri untuk dapat mengubah mana-mana kod dan melengkapkan cabaran. Anda juga boleh [bintang (🌟) repositori ini](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) untuk memudahkan mencari repositori ini dan yang berkaitan.

### 2. Buat ruang kod

Untuk mengelakkan sebarang isu kebergantungan apabila menjalankan kod, kami mencadangkan menjalankan kursus ini dalam [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Ini boleh dibuat dengan memilih pilihan `Code` pada versi forked repositori ini dan memilih pilihan **Codespaces**.

![Dialog menunjukkan butang untuk membuat ruang kod](../../../00-course-setup/images/who-will-pay.webp)

### 3. Menyimpan Kunci API Anda

Menjaga kunci API anda selamat dan terjamin adalah penting apabila membina sebarang jenis aplikasi. Kami mencadangkan untuk tidak menyimpan sebarang kunci API secara langsung dalam kod anda. Komitmen butiran tersebut ke repositori awam boleh mengakibatkan isu keselamatan dan bahkan kos yang tidak diingini jika digunakan oleh pihak yang tidak bertanggungjawab. Berikut adalah panduan langkah demi langkah tentang cara membuat fail `.env` untuk Python dan menambah `GITHUB_TOKEN`:

1. **Navigasi ke Direktori Projek Anda**: Buka terminal atau command prompt anda dan navigasi ke direktori root projek anda di mana anda ingin membuat fail `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Buat Fail `.env`**: Gunakan editor teks pilihan anda untuk membuat fail baru bernama `.env`. Jika anda menggunakan command line, anda boleh menggunakan `touch` (on Unix-based systems) or `echo` (pada Windows):

   Sistem berasaskan Unix:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Edit Fail `.env`**: Buka fail `.env` dalam editor teks (contohnya, VS Code, Notepad++, atau mana-mana editor lain). Tambahkan baris berikut ke fail, menggantikan `your_github_token_here` dengan token GitHub sebenar anda:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Simpan Fail**: Simpan perubahan dan tutup editor teks.

5. **Pasang pakej `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` untuk memuatkan pembolehubah persekitaran dari fail `.env` ke dalam aplikasi Python anda. Anda boleh memasangnya menggunakan `pip`:

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

Itu sahaja! Anda telah berjaya membuat fail `.env`, menambah token GitHub anda, dan memuatkannya ke dalam aplikasi Python anda.

## Cara Menjalankan Secara Lokal pada Komputer Anda

Untuk menjalankan kod secara lokal pada komputer anda, anda perlu mempunyai beberapa versi [Python dipasang](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Untuk kemudian menggunakan repositori, anda perlu mengklonnya:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Setelah anda mempunyai semuanya diperiksa, anda boleh mula!

## Langkah Pilihan

### Memasang Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) adalah pemasang ringan untuk memasang [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, serta beberapa pakej. Conda sendiri adalah pengurus pakej, yang memudahkan untuk menyiapkan dan bertukar antara [**persekitaran maya**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) dan pakej Python yang berbeza. Ia juga berguna untuk memasang pakej yang tidak tersedia melalui `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Teruskan dan isikan fail persekitaran anda dengan snippet di bawah:

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

Jika anda mendapati anda mendapat ralat menggunakan conda, anda boleh memasang perpustakaan Microsoft AI secara manual menggunakan arahan berikut dalam terminal.

```
conda install -c microsoft azure-ai-ml
```

Fail persekitaran menentukan kebergantungan yang kita perlukan. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` adalah versi utama Python terkini.

Setelah itu selesai, anda boleh teruskan dan buat persekitaran Conda anda dengan menjalankan arahan di bawah dalam baris perintah/terminal anda

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Rujuk kepada [panduan persekitaran Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika anda menghadapi sebarang isu.

### Menggunakan Visual Studio Code dengan sambungan sokongan Python

Kami mencadangkan menggunakan editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) dengan [sambungan sokongan Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) yang dipasang untuk kursus ini. Walau bagaimanapun, ini lebih kepada cadangan dan bukan keperluan mutlak.

> **Nota**: Dengan membuka repositori kursus dalam VS Code, anda mempunyai pilihan untuk menyediakan projek dalam kontena. Ini disebabkan oleh direktori [`.devcontainer` khas](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) yang terdapat dalam repositori kursus. Lebih lanjut mengenai ini nanti.

> **Nota**: Setelah anda mengklon dan membuka direktori dalam VS Code, ia akan secara automatik mencadangkan anda memasang sambungan sokongan Python.

> **Nota**: Jika VS Code mencadangkan anda membuka semula repositori dalam kontena, tolak permintaan ini untuk menggunakan versi Python yang dipasang secara lokal.

### Menggunakan Jupyter dalam Penyemak Imbas

Anda juga boleh bekerja pada projek menggunakan [persekitaran Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) terus dalam penyemak imbas anda. Kedua-dua Jupyter klasik dan [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) menyediakan persekitaran pembangunan yang cukup menyenangkan dengan ciri-ciri seperti auto-lengkap, penyorotan kod, dan lain-lain.

Untuk memulakan Jupyter secara lokal, pergi ke terminal/baris perintah, navigasi ke direktori kursus, dan laksanakan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulakan instance Jupyter dan URL untuk mengaksesnya akan ditunjukkan dalam tetingkap baris perintah.

Setelah anda mengakses URL, anda sepatutnya melihat rangka kursus dan dapat menavigasi ke mana-mana fail `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` di mana anda boleh melihat kod dan output.

## Menggunakan Perkhidmatan Azure OpenAI untuk kali pertama

Jika ini adalah kali pertama anda bekerja dengan perkhidmatan Azure OpenAI, sila ikuti panduan ini tentang cara [membuat dan menggunakan sumber Perkhidmatan Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Menggunakan API OpenAI untuk kali pertama

Jika ini adalah kali pertama anda bekerja dengan API OpenAI, sila ikuti panduan tentang cara [membuat dan menggunakan Antara Muka.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Berkenalan dengan Pelajar Lain

Kami telah mencipta saluran dalam pelayan [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) rasmi kami untuk bertemu dengan pelajar lain. Ini adalah cara yang hebat untuk berhubung dengan usahawan, pembina, pelajar, dan sesiapa sahaja yang ingin meningkatkan kemahiran dalam AI Generatif.

[![Sertai saluran discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Pasukan projek juga akan berada di pelayan Discord ini untuk membantu mana-mana pelajar.

## Menyumbang

Kursus ini adalah inisiatif sumber terbuka. Jika anda melihat kawasan yang boleh diperbaiki atau masalah, sila buat [Permintaan Tarik](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) atau logkan [isu GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Pasukan projek akan menjejaki semua sumbangan. Menyumbang kepada sumber terbuka adalah cara yang hebat untuk membina kerjaya anda dalam AI Generatif.

Kebanyakan sumbangan memerlukan anda bersetuju dengan Perjanjian Lesen Penyumbang (CLA) yang menyatakan bahawa anda mempunyai hak dan benar-benar memberi kami hak untuk menggunakan sumbangan anda. Untuk maklumat lanjut, lawati [laman web CLA, Perjanjian Lesen Penyumbang](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Penting: apabila menterjemah teks dalam repositori ini, sila pastikan anda tidak menggunakan terjemahan mesin. Kami akan mengesahkan terjemahan melalui komuniti, jadi sila hanya menawarkan diri untuk terjemahan dalam bahasa yang anda mahir.

Apabila anda menyerahkan permintaan tarik, bot CLA akan secara automatik menentukan sama ada anda perlu memberikan CLA dan menghias PR dengan sewajarnya (contohnya, label, komen). Hanya ikuti arahan yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali di semua repositori yang menggunakan CLA kami.

Projek ini telah menerima pakai [Kod Etika Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Untuk maklumat lanjut, baca Soalan Lazim Kod Etika atau hubungi [Email opencode](opencode@microsoft.com) dengan sebarang soalan atau komen tambahan.

## Mari Kita Mula

Sekarang bahawa anda telah melengkapkan langkah-langkah yang diperlukan untuk melengkapkan kursus ini, mari kita mula dengan mendapatkan [pengenalan kepada AI Generatif dan LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.