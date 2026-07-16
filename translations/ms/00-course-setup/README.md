# Memulakan Kursus ini

Kami sangat teruja untuk anda memulakan kursus ini dan melihat apa yang anda dapat diilhamkan untuk bina dengan Generative AI!

Untuk memastikan kejayaan anda, halaman ini menyenaraikan langkah-langkah persediaan, keperluan teknikal, dan tempat untuk mendapatkan bantuan jika perlu.

## Langkah Persediaan

Untuk mula mengambil kursus ini, anda perlu melengkapkan langkah-langkah berikut.

### 1. Fork Repo ini

[Fork seluruh repo ini](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ke akaun GitHub anda sendiri supaya anda boleh mengubah sebarang kod dan menyelesaikan cabaran. Anda juga boleh [star (🌟) repo ini](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) untuk memudahkannya dan repo berkaitan dicari.

### 2. Buat codespace

Untuk mengelakkan sebarang masalah bergantung apabila menjalankan kod, kami mengesyorkan menjalankan kursus ini dalam [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Dalam fork anda: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/ms/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Tambah rahsia

1. ⚙️ Ikon gear -> Command Pallete-> Codespaces : Manage user secret -> Tambah rahsia baru.
2. Namakan OPENAI_API_KEY, tampal kunci anda, Simpan.

### 3. Apa seterusnya?

| Saya mahu…            | Pergi ke…                                                                |
|---------------------|-------------------------------------------------------------------------|
| Mula Pelajaran 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Bekerja luar talian  | [`setup-local.md`](02-setup-local.md)                                   |
| Sediakan Penyedia LLM | [`providers.md`](03-providers.md)                                        |
| Berjumpa pelajar lain | [Sertai Discord kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Penyelesaian Masalah


| Simptom                                   | Penyelesaian                                                     |
|-------------------------------------------|-----------------------------------------------------------------|
| Pembinaan Container tersekat > 10 min    | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal tidak melekat; klik **+** ➜ *bash*                    |
| `401 Unauthorized` dari OpenAI            | `OPENAI_API_KEY` salah / tamat tempoh                            |
| VS Code menunjukkan “Dev container mounting…” | Segar semula tab pelayar—Codespaces kadang-kadang hilang sambungan |
| Kernel notebook hilang                     | Menu notebook ➜ **Kernel ▸ Pilih Kernel ▸ Python 3**             |

   Sistem berasaskan Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Sunting Fail `.env`**: Buka fail `.env` dalam editor teks (contoh, VS Code, Notepad++, atau editor lain). Tambah baris berikut ke fail, gantikan tempat letak dengan endpoint dan kunci Microsoft Foundry Models anda yang sebenar (lihat [`providers.md`](03-providers.md) untuk cara mendapatkannya):

   > **Nota:** GitHub Models (dan pembolehubah `GITHUB_TOKEN` nya) akan ditamatkan pada akhir Julai 2026. Gunakan [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) sebagai gantinya.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Simpan Fail**: Simpan perubahan dan tutup editor teks.

5. **Pasang `python-dotenv`**: Jika anda belum memasangnya, anda perlu memasang pakej `python-dotenv` untuk memuatkan pembolehubah persekitaran dari fail `.env` ke dalam aplikasi Python anda. Anda boleh memasangnya menggunakan `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Muatkan Pembolehubah Persekitaran dalam Skrip Python Anda**: Dalam skrip Python anda, gunakan pakej `python-dotenv` untuk memuat pembolehubah persekitaran dari fail `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Muatkan pembolehubah persekitaran dari fail .env
   load_dotenv()

   # Akses pembolehubah Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Itu sahaja! Anda telah berjaya membuat fail `.env`, menambah kelayakan Microsoft Foundry Models anda, dan memuatkannya ke dalam aplikasi Python anda.

## Cara Menjalankan secara tempatan pada komputer anda

Untuk menjalankan kod secara tempatan pada komputer anda, anda perlu memasang [Python versi tertentu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Kemudian untuk menggunakan repositori, anda perlu clone ia:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Setelah anda sudah lengkapkan semuanya, anda boleh mula!

## Langkah Pilihan

### Memasang Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) adalah pemasang ringan untuk memasang [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, serta beberapa pakej.
Conda sendiri adalah pengurus pakej, yang memudahkan penyediaan dan bertukar antara [**persekitaran maya**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python dan pakej yang berbeza. Ia juga berguna untuk memasang pakej yang tidak tersedia melalui `pip`.

Anda boleh ikut [panduan pemasangan MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) untuk memasangnya.

Dengan Miniconda dipasang, anda perlu clone [repositori](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jika belum).

Seterusnya, anda perlu buat persekitaran maya. Untuk ini menggunakan Conda, sila buat fail persekitaran baru (_environment.yml_). Jika anda mengikuti menggunakan Codespaces, buat dalam direktori `.devcontainer`, jadi `.devcontainer/environment.yml`.

Sila isi fail persekitaran anda dengan petikan di bawah:

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

Jika anda mendapati anda mendapat ralat menggunakan conda anda boleh pasang sendiri Microsoft AI Libraries menggunakan arahan berikut dalam terminal.

```
conda install -c microsoft azure-ai-ml
```

Fail persekitaran menentukan kebergantungan yang diperlukan. `<environment-name>` merujuk kepada nama yang anda ingin gunakan untuk persekitaran Conda anda, dan `<python-version>` ialah versi Python yang anda ingin gunakan, contoh, `3` ialah versi utama Python terkini.

Setelah itu, anda boleh buat persekitaran Conda dengan menjalankan arahan di bawah dalam baris arahan/terminal anda

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # sub laluan .devcontainer terpakai hanya kepada persediaan Codespace sahaja
conda activate ai4beg
```

Rujuk [panduan persekitaran Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika anda menghadapi sebarang masalah.

### Menggunakan Visual Studio Code dengan peluasan sokongan Python

Kami mengesyorkan menggunakan editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) dengan [peluasan sokongan Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) yang dipasang untuk kursus ini. Namun, ini adalah lebih kepada cadangan dan bukan keperluan wajib

> **Nota**: Dengan membuka repositori kursus dalam VS Code, anda mempunyai pilihan untuk menyediakan projek dalam container. Ini kerana terdapat direktori khusus [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dalam repositori kursus. Lebih lanjut akan dijelaskan kemudian.

> **Nota**: Setelah clone dan buka direktori dalam VS Code, ia akan segera mencadangkan anda memasang peluasan sokongan Python.

> **Nota**: Jika VS Code mencadangkan anda membuka kembali repositori dalam container, tolak permintaan ini untuk menggunakan versi Python yang dipasang secara tempatan.

### Menggunakan Jupyter dalam Pelayar

Anda juga boleh bekerja pada projek menggunakan [persekitaran Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) terus dalam pelayar anda. Baik Jupyter klasik dan [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) menyediakan persekitaran pembangunan yang selesa dengan ciri seperti auto-completion, penyorotan kod, dan sebagainya.

Untuk memulakan Jupyter secara tempatan, pergi ke terminal/baris arahan, navigasi ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulakan instance Jupyter dan URL untuk mengaksesnya akan dipaparkan dalam tetingkap baris arahan.

Setelah anda akses URL tersebut, anda harus melihat garis panduan kursus dan boleh navigasi ke mana-mana fail `*.ipynb`. Contohnya, `08-building-search-applications/python/oai-solution.ipynb`.

### Menjalankan dalam container

Alternatif untuk menyediakan semuanya di komputer anda atau Codespace adalah menggunakan [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Folder khusus `.devcontainer` dalam repositori kursus membolehkan VS Code menyediakan projek dalam container. Di luar Codespaces, ini memerlukan pemasangan Docker, dan sebenarnya, ia melibatkan sedikit kerja, jadi kami hanya mengesyorkan ini kepada yang berpengalaman dengan container.

Salah satu cara terbaik untuk memastikan kunci API anda selamat bila menggunakan GitHub Codespaces adalah dengan menggunakan Rahsia Codespace. Sila ikut panduan [Pengurusan rahsia Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) untuk ketahui lebih lanjut.


## Pelajaran dan Keperluan Teknikal

Kursus ini mempunyai 6 pelajaran konsep dan 6 pelajaran pengkodan.

Untuk pelajaran pengkodan, kami menggunakan Perkhidmatan Azure OpenAI. Anda perlu mempunyai akses ke perkhidmatan Azure OpenAI dan kunci API untuk menjalankan kod ini. Anda boleh memohon akses dengan [melengkapkan permohonan ini](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Sementara menunggu permohonan anda diproses, setiap pelajaran pengkodan juga disertakan fail `README.md` di mana anda boleh melihat kod dan keluaran.

## Menggunakan Perkhidmatan Azure OpenAI buat pertama kali

Jika ini kali pertama anda bekerja dengan perkhidmatan Azure OpenAI, sila ikut panduan ini tentang cara [membuat dan melancarkan sumber Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Menggunakan OpenAI API buat pertama kali

Jika ini kali pertama anda bekerja dengan OpenAI API, sila ikut panduan tentang cara [membuat dan menggunakan Antara Muka.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Berjumpa Pelajar Lain

Kami telah mencipta saluran di [server Discord Komuniti AI rasmi kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) untuk berjumpa pelajar lain. Ini adalah cara yang bagus untuk berhubung dengan usahawan, pembina, pelajar yang berfikiran sama, dan sesiapa sahaja yang ingin meningkatkan diri dalam Generative AI.

[![Sertai saluran discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Pasukan projek juga akan berada di server Discord ini untuk membantu mana-mana pelajar.

## Menyumbang

Kursus ini adalah inisiatif sumber terbuka. Jika anda nampak kawasan yang boleh diperbaiki atau isu, sila cipta [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) atau log [isu GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Pasukan projek akan mengesan semua sumbangan. Menyumbang ke sumber terbuka adalah cara yang luar biasa untuk membina kerjaya anda dalam Generative AI.

Kebanyakan sumbangan memerlukan anda bersetuju dengan Perjanjian Lesen Penyumbang (CLA) yang menyatakan anda mempunyai hak dan benar-benar memberi kami hak untuk menggunakan sumbangan anda. Untuk butiran, lawati [laman web CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Penting: apabila menterjemah teks dalam repo ini, sila pastikan anda tidak menggunakan terjemahan mesin. Kami akan mengesahkan terjemahan melalui komuniti, jadi sila hanya tawarkan terjemahan dalam bahasa yang anda fasih.

Apabila anda menghantar pull request, bot CLA akan secara automatik menentukan sama ada anda perlu menyediakan CLA dan menghiasi PR dengan sesuai (contoh, label, komen). Ikut sahaja arahan yang diberikan oleh bot. Anda hanya perlu buat ini sekali untuk semua repositori yang menggunakan CLA kami.


Projek ini telah mengguna pakai [Kod Etika Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Untuk maklumat lanjut, baca FAQ Kod Etika atau hubungi [Email opencode](opencode@microsoft.com) untuk sebarang soalan atau komen tambahan.

## Mari Bermula

Kini anda telah menyelesaikan langkah-langkah yang diperlukan untuk menamatkan kursus ini, mari kita mula dengan mendapatkan [pengenalan kepada Generative AI dan LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->