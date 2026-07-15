# Persediaan Tempatan 🖥️

**Gunakan panduan ini jika anda lebih suka menjalankan semuanya di komputer riba anda sendiri.**   
Anda mempunyai dua pilihan: **(A) Python asli + virtual-env** atau **(B) VS Code Dev Container dengan Docker**.  
Pilih yang mana-mana yang anda rasa lebih mudah—kedua-duanya membawa ke pelajaran yang sama.

## 1.  Prasyarat

| Alat               | Versi / Nota                                                                        |
|--------------------|------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (dapatkan dari <https://python.org>)                                        |
| **Git**            | Terkini (datang dengan Xcode / Git untuk Windows / pengurus pakej Linux)           |
| **VS Code**        | Pilihan tetapi disyorkan <https://code.visualstudio.com>                           |
| **Docker Desktop** | *Hanya* untuk Pilihan B. Pasang secara percuma: <https://docs.docker.com/desktop/> |

> 💡 **Petua** – Sahkan alat dalam terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Pilihan A – Python Asli (paling cepat)

### Langkah 1  Klon repo ini

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Langkah 2 Buat & aktifkan persekitaran maya

```bash
python -m venv .venv          # buat satu
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompt kini harus bermula dengan (.venv)—itu bermaksud anda sudah berada dalam env.

### Langkah 3 Pasang kebergantungan

```bash
pip install -r requirements.txt
```

Teruskan ke Seksyen 3 mengenai [kunci API](#3-tambah-kunci-api-anda)

## 2. Pilihan B – VS Code Dev Container (Docker)

Kami menyediakan repositori dan kursus ini dengan [kontena pembangunan](https://containers.dev?WT.mc_id=academic-105485-koreyst) yang mempunyai runtime Universal yang boleh menyokong pembangunan Python3, .NET, Node.js dan Java. Konfigurasi berkaitan ditakrifkan dalam fail `devcontainer.json` yang terletak dalam folder `.devcontainer/` di akar repositori ini.

>**Kenapa pilih ini?**
>Persekitaran yang sama seperti Codespaces; tiada pergeseran kebergantungan.

### Langkah 0 Pasang tambahan

Docker Desktop – sahkan ```docker --version``` berjalan.
VS Code Remote – Extension Containers (ID: ms-vscode-remote.remote-containers).

### Langkah 1 Buka repo di VS Code

Fail ▸ Buka Folder…  → generative-ai-for-beginners

VS Code mengesan .devcontainer/ dan memaparkan prompt.

### Langkah 2 Buka semula dalam kontena

Klik “Buka semula dalam Kontena”. Docker bina imej (≈ 3 minit kali pertama).
Apabila prompt terminal muncul, anda berada dalam kontena.

## 2.  Pilihan C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) adalah pemasang ringan untuk memasang [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, dan beberapa pakej.
Conda sendiri adalah pengurus pakej, yang memudahkan penyediaan dan pertukaran antara [**persekitaran maya**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python dan pakej. Ia juga berguna untuk memasang pakej yang tidak tersedia melalui `pip`.

### Langkah 0  Pasang Miniconda

Ikuti [panduan pemasangan MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) untuk menyediakan.

```bash
conda --version
```

### Langkah 1 Buat persekitaran maya

Buat fail persekitaran baru (*environment.yml*). Jika anda mengikuti menggunakan Codespaces, buat ini dalam direktori `.devcontainer`, iaitu `.devcontainer/environment.yml`.

### Langkah 2  Isi fail persekitaran anda

Tambah potongan berikut ke `environment.yml` anda

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

### Langkah 3 Buat persekitaran Conda anda

Jalankan arahan di bawah dalam baris perintah/terminal anda

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Laluan sub .devcontainer hanya terpakai untuk tetapan Codespace sahaja
conda activate ai4beg
```

Rujuk [panduan persekitaran Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika menghadapi sebarang isu.

## 2  Pilihan D – Jupyter Klasik / Jupyter Lab (dalam pelayar anda)

> **Untuk siapa ini?**  
> Sesiapa yang suka antaramuka Jupyter klasik atau ingin menjalankan notebook tanpa VS Code.  

### Langkah 1  Pastikan Jupyter dipasang

Untuk memulakan Jupyter secara tempatan, pergi ke terminal/command line, navigasi ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulakan instans Jupyter dan URL untuk mengaksesnya akan dipaparkan dalam tetingkap baris perintah.

Setelah mengakses URL, anda sepatutnya dapat melihat garis besar kursus dan boleh menavigasi mana-mana fail `*.ipynb`. Sebagai contoh, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Tambah Kunci API Anda

Menjaga kunci API anda selamat adalah penting ketika membina apa juga jenis aplikasi. Kami mengesyorkan agar tidak menyimpan sebarang kunci API secara langsung dalam kod anda. Menyertakan butiran tersebut dalam repositori awam boleh menyebabkan isu keselamatan dan juga kos tidak diingini jika digunakan oleh pihak jahat.
Berikut adalah panduan langkah demi langkah tentang cara membuat fail `.env` untuk Python dan menambah kelayakan Microsoft Foundry Models anda:

> **Nota:** GitHub Models (dan pembolehubah `GITHUB_TOKEN` nya) akan dihentikan pada akhir Julai 2026. Panduan ini menggunakan [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) sebagai gantinya. Lebih suka bekerja sepenuhnya luar talian? Lihat [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Navigasi ke Direktori Projek Anda**: Buka terminal atau command prompt anda dan pergi ke direktori akar projek anda di mana anda mahu cipta fail `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Cipta Fail `.env`**: Gunakan penyunting teks pilihan anda untuk mencipta fail baru bernama `.env`. Jika menggunakan baris perintah, anda boleh gunakan `touch` (pada sistem Unix) atau `echo` (pada Windows):

   Sistem berasaskan Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Sunting Fail `.env`**: Buka fail `.env` dalam penyunting teks (contoh: VS Code, Notepad++, atau editor lain). Tambah baris berikut dalam fail tersebut, ganti tempat letak dengan endpoint projek Microsoft Foundry dan kunci API sebenar anda:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Simpan Fail**: Simpan perubahan dan tutup editor teks.

5. **Pasang `python-dotenv`**: Jika belum, anda perlu memasang pakej `python-dotenv` untuk memuatkan pemboleh ubah persekitaran dari fail `.env` ke dalam aplikasi Python anda. Anda boleh pasang menggunakan `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Muatkan Pemboleh Ubah Persekitaran dalam Skrip Python Anda**: Dalam skrip Python anda, gunakan pakej `python-dotenv` untuk memuatkan pemboleh ubah persekitaran dari fail `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Muatkan pembolehubah persekitaran daripada fail .env
   load_dotenv()

   # Akses pembolehubah Model Microsoft Foundry
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Itu sahaja! Anda telah berjaya mencipta fail `.env`, menambah kelayakan Microsoft Foundry Models anda, dan memuatkannya ke dalam aplikasi Python anda.

🔐 Jangan sesekali commit .env—ia sudah disenaraikan dalam .gitignore.
Arahan penuh penyedia ada dalam [`providers.md`](03-providers.md).

## 4. Apa seterusnya?

| Saya mahu…          | Pergi ke…                                                               |
|---------------------|------------------------------------------------------------------------|
| Mula Pelajaran 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Sediakan Penyedia LLM | [`providers.md`](03-providers.md)                                      |
| Temui pelajar lain  | [Sertai Discord kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Penyelesaian Masalah

| Gejala                                   | Pembetulan                                                      |
|-----------------------------------------|----------------------------------------------------------------|
| `python tidak ditemui`                   | Tambah Python ke PATH atau buka semula terminal selepas pemasangan|
| `pip` tidak boleh bina roda (Windows)    | `pip install --upgrade pip setuptools wheel` kemudian cuba lagi. |
| `ModuleNotFoundError: dotenv`            | Jalankan `pip install -r requirements.txt` (env belum dipasang).   |
| Docker build gagal *Tiada ruang tinggal*| Docker Desktop ▸ *Tetapan* ▸ *Sumber* → tambahkan saiz cakera.   |
| VS Code asyik minta buka semula          | Anda mungkin aktifkan kedua-dua Pilihan; pilih satu (venv **atau** kontena)|
| Ralat OpenAI 401 / 429                   | Semak nilai `OPENAI_API_KEY` / had kadar permintaan.             |
| Ralat guna Conda                         | Pasang perpustakaan AI Microsoft menggunakan `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->