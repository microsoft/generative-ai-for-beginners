# Memulakan kursus ini

Kami sangat teruja untuk anda memulakan kursus ini dan melihat apa yang anda akan terinspirasi untuk bina dengan AI Generatif!

Untuk memastikan kejayaan anda, halaman ini menggariskan langkah-langkah penetapan, keperluan teknikal, dan di mana untuk mendapatkan bantuan jika perlu.

## Langkah Penetapan

Untuk mula mengambil kursus ini, anda perlu melengkapkan langkah-langkah berikut.

### 1. Fork Repo ini

[Fork keseluruhan repo ini](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ke akaun GitHub anda sendiri untuk dapat mengubah sebarang kod dan melengkapkan cabaran. Anda juga boleh [berikan bintang (🌟) kepada repo ini](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) untuk memudahkan pencarian repo ini dan repo berkaitan.

### 2. Cipta codespace

Untuk mengelakkan sebarang isu pergantungan semasa menjalankan kod, kami mengesyorkan menjalankan kursus ini dalam [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Dalam fork anda: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/ms/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Tambah secret

1. ⚙️ Ikon gear -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Nama OPENAI_API_KEY, tampal kekunci anda, Simpan.

### 3. Apa seterusnya?

| Saya mahu…          | Pergi ke…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Mula Pelajaran 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Bekerja secara luar talian        | [`setup-local.md`](02-setup-local.md)                                   |
| Setup Penyedia LLM | [`providers.md`](03-providers.md)                                        |
| Berjumpa pelajar lain | [Sertai Discord kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Menyelesaikan Masalah


| Gejala                                   | Penyelesaian                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| Pemasangan kontena tersekat > 10 min            | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal tidak bersambung; klik **+** ➜ *bash*                    |
| `401 Unauthorized` dari OpenAI            | `OPENAI_API_KEY` salah / tamat tempoh                              |
| VS Code menunjukkan “Dev container mounting…”   | Segarkan tab penyemak imbas—Codespaces kadang-kadang hilang sambungan   |
| Kernel notebook hilang                   | Menu Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Sistem berasaskan Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Sunting Fail `.env`**: Buka fail `.env` dalam penyunting teks (contohnya, VS Code, Notepad++, atau apa-apa penyunting lain). Tambah baris berikut ke fail tersebut, gantikan `your_github_token_here` dengan token GitHub sebenar anda:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Simpan Fail**: Simpan perubahan dan tutup penyunting teks.

5. **Pasang `python-dotenv`**: Jika belum, anda perlu memasang pakej `python-dotenv` untuk memuatkan pembolehubah persekitaran dari fail `.env` ke aplikasi Python anda. Anda boleh memasangnya menggunakan `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Muatkan Pembolehubah Persekitaran dalam Skrip Python Anda**: Dalam skrip Python anda, gunakan pakej `python-dotenv` untuk memuatkan pembolehubah persekitaran dari fail `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Muatkan pembolehubah persekitaran dari fail .env
   load_dotenv()

   # Akses pembolehubah GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Selesai! Anda telah berjaya mencipta fail `.env`, tambah token GitHub anda, dan memuatkannya ke dalam aplikasi Python anda.

## Cara Menjalankan secara tempatan di komputer anda

Untuk menjalankan kod secara tempatan di komputer anda, anda perlu memasang beberapa versi [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Kemudian untuk menggunakan repositori, anda perlu mengklonnya:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Setelah semuanya siap, anda boleh mula!

## Langkah Pilihan

### Pemasangan Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) adalah pemasang ringan untuk memasang [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, serta beberapa pakej.
Conda sendiri adalah pengurus pakej, yang memudahkan penetapan dan pertukaran antara pelbagai [**persekitaran maya**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) dan pakej Python. Ia juga berguna untuk memasang pakej yang tidak tersedia melalui `pip`.

Anda boleh mengikuti [panduan pemasangan MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) untuk memasangnya.

Dengan Miniconda dipasang, anda perlu mengklon [repositori](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jika anda belum lagi)

Seterusnya, anda perlu mencipta persekitaran maya. Untuk buat ini dengan Conda, teruskan dan cipta fail persekitaran baru (_environment.yml_). Jika anda mengikuti menggunakan Codespaces, cipta ini dalam direktori `.devcontainer`, iaitu `.devcontainer/environment.yml`.

Teruskan dan isi fail persekitaran anda dengan potongan kod di bawah:

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

Jika anda menghadapi ralat menggunakan conda, anda boleh pasang manual Perpustakaan AI Microsoft menggunakan arahan berikut dalam terminal.

```
conda install -c microsoft azure-ai-ml
```

Fail persekitaran menentukan pergantungan yang kita perlukan. `<environment-name>` merujuk kepada nama yang anda ingin gunakan untuk persekitaran Conda anda, dan `<python-version>` ialah versi Python yang anda mahu gunakan, contohnya, `3` ialah versi utama Python terkini.

Setelah itu, anda boleh terus mencipta persekitaran Conda anda dengan menjalankan arahan di bawah dalam baris perintah/terminal anda

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Laluan sub .devcontainer hanya terpakai kepada tetapan Codespace sahaja
conda activate ai4beg
```

Rujuk [panduan persekitaran Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika anda menghadapi sebarang isu.

### Menggunakan Visual Studio Code dengan sambungan sokongan Python

Kami mengesyorkan menggunakan penyunting [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) dengan [sambungan sokongan Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dipasang untuk kursus ini. Ini adalah sekadar cadangan dan bukannya keperluan pasti

> **Nota**: Dengan membuka repositori kursus dalam VS Code, anda mempunyai pilihan untuk menyediakan projek dalam sebuah kontena. Ini kerana adanya direktori [`.devcontainer` khas](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dalam repositori kursus. Lebih lanjut tentang ini kemudian.

> **Nota**: Setelah anda mengklon dan buka direktori dalam VS Code, ia akan secara automatik mencadangkan anda memasang sambungan sokongan Python.

> **Nota**: Jika VS Code mencadangkan anda membuka semula repositori dalam kontena, tolak permintaan ini bagi menggunakan versi Python yang dipasang secara tempatan.

### Menggunakan Jupyter dalam Penyemak Imbas

Anda juga boleh bekerja pada projek ini menggunakan [persekitaran Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) terus dalam penyemak imbas anda. Kedua-dua Jupyter klasik dan [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) menyediakan persekitaran pembangunan yang cukup selesa dengan ciri seperti auto-completion, penonjolan kod, dsb.

Untuk memulakan Jupyter secara tempatan, pergi ke terminal/baris perintah, navigasi ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulakan instans Jupyter dan URL untuk mengaksesnya akan ditunjukkan dalam tetingkap baris perintah.

Setelah anda mengakses URL tersebut, anda sepatutnya dapat melihat garis besar kursus dan boleh melayari mana-mana fail `*.ipynb`. Sebagai contoh, `08-building-search-applications/python/oai-solution.ipynb`.

### Menjalankan dalam kontena

Alternatif kepada penetapan semua perkara di komputer anda atau Codespace ialah menggunakan [kontena](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Folder khas `.devcontainer` dalam repositori kursus membolehkan VS Code menyediakan projek dalam sebuah kontena. Di luar Codespaces, ini memerlukan pemasangan Docker, dan secara terus-terangnya, ia memerlukan sedikit kerja, jadi kami mengesyorkan ini hanya untuk mereka yang berpengalaman bekerja dengan kontena.

Salah satu cara terbaik untuk menjaga kunci API anda selamat apabila menggunakan GitHub Codespaces adalah dengan menggunakan Rahsia Codespace. Sila ikut panduan [pengurusan rahsia Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) untuk maklumat lanjut.

## Pelajaran dan Keperluan Teknikal

Kursus ini mempunyai 6 pelajaran konsep dan 6 pelajaran pengkodan.

Untuk pelajaran pengkodan, kami menggunakan Perkhidmatan Azure OpenAI. Anda memerlukan akses ke perkhidmatan Azure OpenAI dan kunci API untuk menjalankan kod ini. Anda boleh memohon akses dengan [melengkapkan permohonan ini](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Sementara menunggu permohonan anda diproses, setiap pelajaran pengkodan juga termasuk fail `README.md` di mana anda boleh melihat kod dan output.

## Menggunakan Perkhidmatan Azure OpenAI untuk kali pertama

Jika ini kali pertama anda bekerja dengan perkhidmatan Azure OpenAI, sila ikut panduan ini tentang cara [mencipta dan mengerahkan sumber Perkhidmatan Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Menggunakan API OpenAI untuk kali pertama

Jika ini kali pertama anda bekerja dengan API OpenAI, sila ikut panduan bagaimana [mencipta dan menggunakan Antara Muka.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Berjumpa Pelajar Lain

Kami telah mencipta saluran dalam server Discord rasmi [Komuniti AI kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) untuk bertemu pelajar lain. Ini adalah cara yang bagus untuk berhubung dengan usahawan, pembina, pelajar, dan sesiapa sahaja yang mahu meningkatkan kemahiran dalam AI Generatif.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Pasukan projek juga akan berada di server Discord ini untuk membantu pelajar.

## Menyumbang

Kursus ini adalah inisiatif sumber terbuka. Jika anda melihat kawasan yang boleh diperbaiki atau isu, sila cipta [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) atau laporkan [isu GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Pasukan projek akan menjejaki semua sumbangan. Menyumbang kepada sumber terbuka adalah cara yang hebat untuk membina kerjaya anda dalam AI Generatif.

Kebanyakan sumbangan memerlukan anda bersetuju dengan Perjanjian Lesen Penyumbang (CLA) yang menyatakan bahawa anda mempunyai hak dan benar-benar memberikan kami hak untuk menggunakan sumbangan anda. Untuk maklumat lanjut, lawati [CLA, laman web Perjanjian Lesen Penyumbang](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Penting: apabila menterjemah teks dalam repo ini, pastikan anda tidak menggunakan terjemahan mesin. Kami akan mengesahkan terjemahan melalui komuniti, jadi sila hanya sukarela untuk terjemahan dalam bahasa yang anda mahir.

Apabila anda menghantar pull request, bot CLA akan secara automatik menentukan sama ada anda perlu menyediakan CLA dan menghias PR dengan sewajarnya (contoh, label, komen). Ikut sahaja arahan yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali sahaja untuk semua repositori menggunakan CLA kami.

Projek ini telah menerima [Kod Etika Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Untuk maklumat lanjut baca Soalan Lazim Kod Etika atau hubungi [Email opencode](opencode@microsoft.com) untuk sebarang pertanyaan atau komen tambahan.

## Jom Bermula
Sekarang bahawa anda telah menyelesaikan langkah-langkah yang diperlukan untuk menamatkan kursus ini, mari kita mulakan dengan mendapatkan [pengenalan kepada Generative AI dan LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->