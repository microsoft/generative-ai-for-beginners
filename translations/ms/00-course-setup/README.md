# Memulakan Kursus Ini

Kami sangat teruja untuk anda memulakan kursus ini dan lihat apa yang anda akan terinspirasi untuk bina dengan Generative AI!

Untuk memastikan kejayaan anda, halaman ini menggariskan langkah-langkah persediaan, keperluan teknikal, dan di mana untuk mendapatkan bantuan jika perlu.

## Langkah Persediaan

Untuk mula mengambil kursus ini, anda perlu melengkapkan langkah-langkah berikut.

### 1. Fork Repo Ini

[Fork keseluruhan repo ini](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ke akaun GitHub anda sendiri untuk dapat mengubah mana-mana kod dan melengkapkan cabaran. Anda juga boleh [bintang (🌟) repo ini](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) untuk memudahkan mencarinya dan repo berkaitan.

### 2. Cipta codespace

Untuk mengelakkan sebarang masalah pergantungan semasa menjalankan kod, kami mengesyorkan menjalankan kursus ini di [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Dalam fork anda: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/ms/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Tambah satu rahsia

1. ⚙️ Ikon gear -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Namakan OPENAI_API_KEY, tampal kunci anda, Simpan.

### 3. Apa seterusnya?

| Saya ingin…          | Pergi ke…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Mula Pelajaran 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Kerja secara luar talian         | [`setup-local.md`](02-setup-local.md)                                   |
| Sediakan Penyedia LLM | [`providers.md`](03-providers.md)                                        |
| Berjumpa pelajar lain | [Sertai Discord kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Penyelesaian Masalah


| Simptom                                   | Penyelesaian                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| Pembinaan kontena tersekat > 10 min       | **Codespaces ➜ "Rebuild Container"**                            |
| `python: command not found`               | Terminal tidak disambung; klik **+** ➜ *bash*                    |
| `401 Unauthorized` dari OpenAI            | `OPENAI_API_KEY` salah / tamat tempoh                                |
| VS Code menunjukkan “Dev container mounting…”   | Segarkan tab pelayar—Codespaces kadang-kadang hilang sambungan   |
| Kernel Notebook hilang                   | Menu Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Sistem berasaskan Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit Fail `.env`**: Buka fail `.env` dalam penyunting teks (contoh, VS Code, Notepad++, atau mana-mana penyunting lain). Tambah baris berikut ke fail, gantikan tempat letak dengan titik akhir dan kunci Microsoft Foundry Models anda yang sebenar (rujuk [`providers.md`](03-providers.md) untuk cara mendapatkannya):

   > **Catatan:** GitHub Models (dan pembolehubah `GITHUB_TOKEN`) akan diberhentikan pada akhir Julai 2026. Gunakan [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) sebagai gantinya.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Simpan Fail**: Simpan perubahan dan tutup penyunting teks.

5. **Pasang `python-dotenv`**: Jika anda belum melakukannya, anda perlu memasang pakej `python-dotenv` untuk memuatkan pembolehubah persekitaran dari fail `.env` ke dalam aplikasi Python anda. Anda boleh memasangnya menggunakan `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Muatkan Pembolehubah Persekitaran Dalam Skrip Python Anda**: Dalam skrip Python anda, gunakan pakej `python-dotenv` untuk memuatkan pembolehubah persekitaran dari fail `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Muatkan pembolehubah persekitaran dari fail .env
   load_dotenv()

   # Akses pembolehubah Model Microsoft Foundry
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Itu sahaja! Anda telah berjaya mencipta fail `.env`, menambah kelayakan Microsoft Foundry Models anda, dan memuatkannya ke dalam aplikasi Python anda.

## Cara Jalankan secara tempatan di komputer anda

Untuk menjalankan kod secara tempatan di komputer anda, anda perlu memasang beberapa versi [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Kemudian untuk menggunakan repositori, anda perlu clone ia:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Setelah anda sudah siap, anda boleh mula!

## Langkah Pilihan

### Memasang Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) adalah pemasang ringan untuk memasang [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, serta beberapa pakej.
Conda sendiri adalah pengurus pakej, yang memudahkan penyediaan dan pertukaran antara Python [**persekitaran maya**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) dan pakej. Ia juga berguna untuk memasang pakej yang tidak tersedia melalui `pip`.

Anda boleh mengikuti [panduan pemasangan MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) untuk memasangnya.

Dengan Miniconda dipasang, anda perlu clone [repositori](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jika belum dilakukan)

Seterusnya, anda perlu cipta persekitaran maya. Untuk melakukan ini dengan Conda, teruskan dan cipta fail persekitaran baru (_environment.yml_). Jika anda mengikuti menggunakan Codespaces, cipta fail ini dalam direktori `.devcontainer`, jadi `.devcontainer/environment.yml`.

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

Jika anda menghadapi ralat menggunakan conda anda boleh memasang Perpustakaan AI Microsoft secara manual menggunakan arahan berikut dalam terminal.

```
conda install -c microsoft azure-ai-ml
```

Fail persekitaran menyatakan kebergantungan yang diperlukan. `<environment-name>` merujuk kepada nama yang anda mahu gunakan untuk persekitaran Conda anda, dan `<python-version>` adalah versi Python yang anda ingin gunakan, contohnya, `3` adalah versi utama Python terkini.

Setelah siap, anda boleh cipta persekitaran Conda anda dengan menjalankan arahan di bawah dalam baris perintah/terminal anda

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Sub laluan .devcontainer hanya terpakai untuk tetapan Codespace sahaja
conda activate ai4beg
```

Rujuk kepada [panduan persekitaran Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika anda menemui sebarang masalah.

### Menggunakan Visual Studio Code dengan sambungan sokongan Python

Kami mengesyorkan menggunakan penyunting [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) dengan [sambungan sokongan Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dipasang untuk kursus ini. Walaupun ini hanyalah cadangan dan bukan keperluan pasti.

> **Catatan**: Dengan membuka repositori kursus dalam VS Code, anda ada pilihan untuk menyediakan projek dalam sebuah bekas. Ini kerana adanya direktori khas [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) yang terdapat dalam repositori kursus. Lebih lanjut mengenai ini nanti.

> **Catatan**: Setelah anda clone dan buka direktori dalam VS Code, ia secara automatik akan mencadangkan untuk memasang sambungan sokongan Python.

> **Catatan**: Jika VS Code mencadangkan anda membuka semula repositori dalam bekas, tolak permintaan ini untuk menggunakan versi Python yang dipasang secara tempatan.

### Menggunakan Jupyter dalam Pelayar

Anda juga boleh bekerja pada projek menggunakan persekitaran [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) terus dalam pelayar anda. Kedua-dua Jupyter klasik dan [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) menyediakan persekitaran pembangunan yang menyenangkan dengan ciri seperti auto-selesai, penonjolan kod, dan lain-lain.

Untuk memulakan Jupyter secara tempatan, pergi ke terminal/baris perintah, navigasi ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulakan instans Jupyter dan URL untuk mengaksesnya akan ditunjukkan dalam tetingkap baris perintah.

Setelah anda mengakses URL, anda harus melihat garis panduan kursus dan boleh menavigasi ke mana-mana fail `*.ipynb`. Contohnya, `08-building-search-applications/python/oai-solution.ipynb`.

### Menjalankan dalam bekas

Alternatif untuk menyediakan semuanya pada komputer anda atau Codespace adalah menggunakan [bekas](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Folder khas `.devcontainer` dalam repositori kursus membolehkan VS Code menyediakan projek dalam bekas. Di luar Codespaces, ini memerlukan pemasangan Docker, dan jujurnya, ia sedikit rumit, jadi kami mengesyorkan ini hanya kepada mereka yang berpengalaman dengan bekas.

Salah satu cara terbaik untuk memastikan kunci API anda selamat semasa menggunakan GitHub Codespaces adalah dengan menggunakan Codespace Secrets. Sila ikut panduan [Pengurusan Rahsia Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) untuk mengetahui lebih lanjut.


## Pelajaran dan Keperluan Teknikal

Kursus ini mempunyai pelajaran "Learn" yang menerangkan konsep Generative AI dan pelajaran "Build" dengan contoh kod praktikal dalam kedua-dua **Python** dan **TypeScript** jika boleh.

Untuk pelajaran pengkodan, kami menggunakan Azure OpenAI di Microsoft Foundry. Anda memerlukan langganan Azure dan kunci API. Akses adalah terbuka - tiada permohonan diperlukan - jadi anda boleh [cipta sumber Microsoft Foundry dan menerapkan model](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) untuk mendapatkan titik akhir dan kunci anda.

Setiap pelajaran pengkodan juga termasuk fail `README.md` di mana anda boleh melihat kod dan output tanpa menjalankan apa-apa.

## Menggunakan Perkhidmatan Azure OpenAI buat pertama kali

Jika ini kali pertama anda bekerja dengan perkhidmatan Azure OpenAI, sila ikut panduan ini tentang cara [mencipta dan menerapkan sumber Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Menggunakan API OpenAI buat pertama kali

Jika ini kali pertama anda bekerja dengan API OpenAI, sila ikut panduan tentang cara [mencipta dan menggunakan Antara Muka.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Bertemu Pelajar Lain

Kami telah mencipta saluran dalam [pelayan Discord Komuniti AI rasmi kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) untuk bertemu pelajar lain. Ini adalah cara yang sangat baik untuk berkenalan dengan usahawan, pembina, pelajar, dan sesiapa yang ingin meningkatkan kemahiran dalam Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Pasukan projek juga akan berada di pelayan Discord ini untuk membantu pelajar mana-mana.

## Menyumbang

Kursus ini adalah inisiatif sumber terbuka. Jika anda melihat kawasan yang boleh diperbaiki atau masalah, sila buat [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) atau rekod [isu GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Pasukan projek akan menjejak semua sumbangan. Menyumbang kepada sumber terbuka adalah cara yang hebat untuk membina kerjaya anda dalam Generative AI.

Kebanyakan sumbangan memerlukan anda bersetuju dengan Perjanjian Lesen Penyumbang (CLA) yang menyatakan bahawa anda mempunyai hak dan sebenarnya memberi kami hak untuk menggunakan sumbangan anda. Untuk maklumat lanjut, lawati [CLA, laman web Perjanjian Lesen Penyumbang](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Penting: apabila menterjemah teks dalam repo ini, sila pastikan anda tidak menggunakan terjemahan mesin. Kami akan mengesahkan terjemahan melalui komuniti, jadi sila hanya bantu terjemah dalam bahasa yang anda mahir.


Apabila anda menghantar permintaan tarik, seorang CLA-bot akan secara automatik menentukan sama ada anda perlu menyediakan CLA dan menghias PR dengan sewajarnya (contohnya, label, komen). Ikuti sahaja arahan yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali sahaja untuk semua repositori yang menggunakan CLA kami.

Projek ini telah mengguna pakai [Kod Etika Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Untuk maklumat lanjut, baca Soalan Lazim Kod Etika atau hubungi [Email opencode](opencode@microsoft.com) untuk sebarang soalan atau komen tambahan.

## Mari Kita Mula

Sekarang anda telah melengkapkan langkah yang diperlukan untuk menamatkan kursus ini, mari kita mula dengan mendapatkan [pengenalan kepada Generative AI dan LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->