<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T20:54:14+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ms"
}
-->
# Memulakan Kursus Ini

Kami sangat teruja untuk anda memulakan kursus ini dan melihat apa yang anda terinspirasi untuk bina dengan Generative AI!

Untuk memastikan kejayaan anda, halaman ini menerangkan langkah-langkah persediaan, keperluan teknikal, dan tempat untuk mendapatkan bantuan jika diperlukan.

## Langkah Persediaan

Untuk memulakan kursus ini, anda perlu melengkapkan langkah-langkah berikut.

### 1. Fork Repo Ini

[Fork keseluruhan repo ini](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ke akaun GitHub anda sendiri untuk membolehkan anda mengubah kod dan melengkapkan cabaran. Anda juga boleh [beri bintang (🌟) pada repo ini](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) untuk memudahkan pencarian repo ini dan repo berkaitan.

### 2. Buat Codespace

Untuk mengelakkan sebarang isu kebergantungan semasa menjalankan kod, kami mengesyorkan menjalankan kursus ini dalam [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Dalam fork anda: **Code -> Codespaces -> New on main**

![Dialog menunjukkan butang untuk membuat codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Tambah rahsia

1. ⚙️ Ikon gear -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Namakan OPENAI_API_KEY, tampal kunci anda, Simpan.

### 3. Apa Seterusnya?

| Saya mahu…          | Pergi ke…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Mulakan Pelajaran 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Bekerja secara offline | [`setup-local.md`](02-setup-local.md)                                   |
| Sediakan Penyedia LLM | [`providers.md`](03-providers.md)                                        |
| Bertemu pelajar lain | [Sertai Discord kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Penyelesaian Masalah

| Gejala                                   | Penyelesaian                                                    |
|-------------------------------------------|-----------------------------------------------------------------|
| Pembinaan kontena tersekat > 10 minit     | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal tidak terpasang; klik **+** ➜ *bash*                   |
| `401 Unauthorized` dari OpenAI            | `OPENAI_API_KEY` salah / tamat tempoh                           |
| VS Code menunjukkan “Dev container mounting…” | Segarkan tab pelayar—Codespaces kadang-kadang kehilangan sambungan |
| Kernel notebook hilang                    | Menu notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Sistem berasaskan Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit Fail `.env`**: Buka fail `.env` dalam editor teks (contohnya, VS Code, Notepad++, atau editor lain). Tambahkan baris berikut ke fail, gantikan `your_github_token_here` dengan token GitHub sebenar anda:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Simpan Fail**: Simpan perubahan dan tutup editor teks.

5. **Pasang `python-dotenv`**: Jika anda belum melakukannya, anda perlu memasang pakej `python-dotenv` untuk memuatkan pembolehubah persekitaran dari fail `.env` ke dalam aplikasi Python anda. Anda boleh memasangnya menggunakan `pip`:

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

Untuk menjalankan kod secara lokal di komputer anda, anda perlu mempunyai beberapa versi [Python dipasang](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Untuk menggunakan repositori ini, anda perlu klon:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Setelah semuanya selesai, anda boleh mula!

## Langkah Pilihan

### Memasang Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) adalah pemasang ringan untuk memasang [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, serta beberapa pakej.
Conda sendiri adalah pengurus pakej yang memudahkan penyediaan dan penukaran antara pelbagai [**persekitaran maya**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python dan pakej. Ia juga berguna untuk memasang pakej yang tidak tersedia melalui `pip`.

Anda boleh mengikuti [panduan pemasangan MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) untuk memasangnya.

Dengan Miniconda dipasang, anda perlu klon [repositori](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jika anda belum melakukannya).

Seterusnya, anda perlu mencipta persekitaran maya. Untuk melakukannya dengan Conda, teruskan dan buat fail persekitaran baru (_environment.yml_). Jika anda mengikuti menggunakan Codespaces, buat ini dalam direktori `.devcontainer`, iaitu `.devcontainer/environment.yml`.

Teruskan dan isi fail persekitaran anda dengan petikan di bawah:

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

Jika anda menghadapi masalah menggunakan conda, anda boleh memasang Microsoft AI Libraries secara manual menggunakan arahan berikut dalam terminal.

```
conda install -c microsoft azure-ai-ml
```

Fail persekitaran menentukan kebergantungan yang kita perlukan. `<environment-name>` merujuk kepada nama yang ingin anda gunakan untuk persekitaran Conda anda, dan `<python-version>` adalah versi Python yang ingin anda gunakan, contohnya, `3` adalah versi utama Python terkini.

Setelah selesai, anda boleh teruskan dan mencipta persekitaran Conda anda dengan menjalankan arahan di bawah dalam baris perintah/terminal anda.

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Rujuk kepada [panduan persekitaran Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika anda menghadapi sebarang masalah.

### Menggunakan Visual Studio Code dengan sambungan sokongan Python

Kami mengesyorkan menggunakan editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) dengan sambungan sokongan [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dipasang untuk kursus ini. Walau bagaimanapun, ini lebih kepada cadangan dan bukan keperluan mutlak.

> **Nota**: Dengan membuka repositori kursus dalam VS Code, anda mempunyai pilihan untuk menyediakan projek dalam kontena. Ini kerana direktori [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) khas yang terdapat dalam repositori kursus. Lebih lanjut mengenai ini nanti.

> **Nota**: Setelah anda klon dan buka direktori dalam VS Code, ia akan secara automatik mencadangkan anda memasang sambungan sokongan Python.

> **Nota**: Jika VS Code mencadangkan anda membuka semula repositori dalam kontena, tolak permintaan ini untuk menggunakan versi Python yang dipasang secara lokal.

### Menggunakan Jupyter dalam Pelayar

Anda juga boleh bekerja pada projek menggunakan [persekitaran Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) terus dalam pelayar anda. Kedua-dua Jupyter klasik dan [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) menyediakan persekitaran pembangunan yang menyenangkan dengan ciri-ciri seperti auto-lengkap, penyorotan kod, dan lain-lain.

Untuk memulakan Jupyter secara lokal, pergi ke terminal/baris perintah, navigasi ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulakan instance Jupyter dan URL untuk mengaksesnya akan ditunjukkan dalam tetingkap baris perintah.

Setelah anda mengakses URL, anda seharusnya melihat garis besar kursus dan dapat menavigasi ke mana-mana fail `*.ipynb`. Contohnya, `08-building-search-applications/python/oai-solution.ipynb`.

### Menjalankan dalam Kontena

Alternatif untuk menyediakan semuanya di komputer anda atau Codespace adalah menggunakan [kontena](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Folder `.devcontainer` khas dalam repositori kursus memungkinkan VS Code untuk menyediakan projek dalam kontena. Di luar Codespaces, ini memerlukan pemasangan Docker, dan sejujurnya, ia melibatkan sedikit kerja, jadi kami mengesyorkan ini hanya kepada mereka yang berpengalaman bekerja dengan kontena.

Salah satu cara terbaik untuk menjaga kunci API anda selamat semasa menggunakan GitHub Codespaces adalah dengan menggunakan Codespace Secrets. Sila ikuti panduan [pengurusan rahsia Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) untuk mengetahui lebih lanjut mengenainya.

## Pelajaran dan Keperluan Teknikal

Kursus ini mempunyai 6 pelajaran konsep dan 6 pelajaran pengkodan.

Untuk pelajaran pengkodan, kami menggunakan Azure OpenAI Service. Anda memerlukan akses kepada Azure OpenAI Service dan kunci API untuk menjalankan kod ini. Anda boleh memohon akses dengan [melengkapkan permohonan ini](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Semasa menunggu permohonan anda diproses, setiap pelajaran pengkodan juga termasuk fail `README.md` di mana anda boleh melihat kod dan hasilnya.

## Menggunakan Azure OpenAI Service untuk Kali Pertama

Jika ini kali pertama anda bekerja dengan Azure OpenAI Service, sila ikuti panduan ini tentang cara [mencipta dan melancarkan sumber Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Menggunakan OpenAI API untuk Kali Pertama

Jika ini kali pertama anda bekerja dengan OpenAI API, sila ikuti panduan tentang cara [mencipta dan menggunakan Antaramuka.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Bertemu Pelajar Lain

Kami telah mencipta saluran dalam [pelayan Discord Komuniti AI rasmi](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) kami untuk bertemu pelajar lain. Ini adalah cara yang hebat untuk berhubung dengan usahawan, pembangun, pelajar, dan sesiapa sahaja yang ingin meningkatkan kemahiran dalam Generative AI.

[![Sertai saluran discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Pasukan projek juga akan berada di pelayan Discord ini untuk membantu mana-mana pelajar.

## Menyumbang

Kursus ini adalah inisiatif sumber terbuka. Jika anda melihat kawasan untuk penambahbaikan atau isu, sila buat [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) atau logkan [isu GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Pasukan projek akan menjejaki semua sumbangan. Menyumbang kepada sumber terbuka adalah cara yang hebat untuk membina kerjaya anda dalam Generative AI.

Kebanyakan sumbangan memerlukan anda bersetuju dengan Perjanjian Lesen Penyumbang (CLA) yang menyatakan bahawa anda mempunyai hak dan benar-benar memberikan kami hak untuk menggunakan sumbangan anda. Untuk butiran, lawati [laman web CLA, Perjanjian Lesen Penyumbang](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Penting: apabila menterjemah teks dalam repo ini, sila pastikan anda tidak menggunakan terjemahan mesin. Kami akan mengesahkan terjemahan melalui komuniti, jadi sila hanya sukarela untuk terjemahan dalam bahasa yang anda mahir.

Apabila anda menghantar permintaan tarik, bot CLA akan secara automatik menentukan sama ada anda perlu memberikan CLA dan menghias PR dengan sewajarnya (contohnya, label, komen). Ikuti sahaja arahan yang diberikan oleh bot. Anda hanya perlu melakukannya sekali untuk semua repositori yang menggunakan CLA kami.

Projek ini telah mengadopsi [Kod Etika Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Untuk maklumat lanjut baca FAQ Kod Etika atau hubungi [Email opencode](opencode@microsoft.com) dengan sebarang soalan atau komen tambahan.

## Mari Mulakan
Sekarang setelah anda menyelesaikan langkah-langkah yang diperlukan untuk melengkapkan kursus ini, mari kita mulakan dengan mendapatkan [pengenalan kepada Generative AI dan LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.