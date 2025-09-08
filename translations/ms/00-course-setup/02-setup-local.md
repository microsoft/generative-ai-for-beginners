<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T18:21:31+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "ms"
}
-->
# Persediaan Tempatan 🖥️

**Guna panduan ini jika anda lebih suka jalankan semuanya di laptop sendiri.**  
Anda ada dua pilihan: **(A) Python asli + virtual-env** atau **(B) VS Code Dev Container dengan Docker**.  
Pilih mana-mana yang anda rasa mudah—kedua-duanya membawa ke pelajaran yang sama.

## 1.  Prasyarat

| Alat                | Versi / Nota                                                                         |
|---------------------|--------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (muat turun dari <https://python.org>)                                        |
| **Git**             | Terkini (datang bersama Xcode / Git for Windows / pengurus pakej Linux)              |
| **VS Code**         | Pilihan tetapi disyorkan <https://code.visualstudio.com>                             |
| **Docker Desktop**  | *Hanya* untuk Pilihan B. Muat turun percuma: <https://docs.docker.com/desktop/>      |

> 💡 **Tip** – Sahkan alat di terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Pilihan A – Python Asli (paling pantas)

### Langkah 1  Klon repo ini

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Langkah 2 Cipta & aktifkan persekitaran maya

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompt kini sepatutnya bermula dengan (.venv)—ini bermakna anda sudah berada dalam env.

### Langkah 3 Pasang keperluan

```bash
pip install -r requirements.txt
```

Terus ke Seksyen 3 tentang [kunci API](../../../00-course-setup)

## 2. Pilihan B – VS Code Dev Container (Docker)

Kami sediakan repositori dan kursus ini dengan [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) yang mempunyai runtime Universal yang menyokong pembangunan Python3, .NET, Node.js dan Java. Konfigurasi berkaitan ditakrifkan dalam fail `devcontainer.json` yang terletak dalam folder `.devcontainer/` di root repositori ini.

>**Kenapa pilih ini?**
>Persekitaran sama seperti Codespaces; tiada isu perbezaan kebergantungan.

### Langkah 0 Pasang keperluan tambahan

Docker Desktop – pastikan ```docker --version``` berfungsi.
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### Langkah 1 Buka repo dalam VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code akan mengesan .devcontainer/ dan memaparkan prompt.

### Langkah 2 Buka semula dalam container

Klik “Reopen in Container”. Docker akan bina imej (± 3 minit kali pertama).
Apabila prompt terminal muncul, anda sudah berada dalam container.

## 2.  Pilihan C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ialah pemasang ringan untuk memasang [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, serta beberapa pakej.
Conda sendiri ialah pengurus pakej, yang memudahkan anda untuk sediakan dan bertukar antara [**persekitaran maya**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python dan pakej. Ia juga berguna untuk memasang pakej yang tidak tersedia melalui `pip`.

### Langkah 0  Pasang Miniconda

Ikuti [panduan pemasangan MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) untuk sediakan.

```bash
conda --version
```

### Langkah 1 Cipta persekitaran maya

Cipta fail persekitaran baru (*environment.yml*). Jika anda mengikuti menggunakan Codespaces, cipta ini dalam direktori `.devcontainer`, iaitu `.devcontainer/environment.yml`.

### Langkah 2  Isikan fail persekitaran anda

Tambah snippet berikut ke dalam `environment.yml` anda

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

### Langkah 3 Cipta persekitaran Conda anda

Jalankan arahan di bawah dalam command line/terminal anda

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Rujuk [panduan persekitaran Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika anda menghadapi sebarang masalah.

## 2  Pilihan D – Jupyter Klasik / Jupyter Lab (dalam pelayar anda)

> **Untuk siapa ini?**  
> Sesiapa yang suka antara muka Jupyter klasik atau mahu jalankan notebook tanpa VS Code.  

### Langkah 1  Pastikan Jupyter telah dipasang

Untuk mulakan Jupyter secara tempatan, buka terminal/command line, navigasi ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulakan Jupyter dan URL untuk mengaksesnya akan dipaparkan dalam tetingkap command line.

Selepas anda akses URL tersebut, anda akan nampak rangka kursus dan boleh navigasi ke mana-mana fail `*.ipynb`. Contohnya, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Tambah Kunci API Anda

Menjaga keselamatan kunci API anda sangat penting apabila membina sebarang aplikasi. Kami syorkan supaya tidak menyimpan kunci API secara langsung dalam kod anda. Jika anda commit butiran tersebut ke repositori awam, ia boleh menyebabkan isu keselamatan dan juga kos yang tidak diingini jika disalah guna.
Berikut adalah panduan langkah demi langkah untuk mencipta fail `.env` untuk Python dan menambah `GITHUB_TOKEN`:

1. **Navigasi ke Direktori Projek Anda**: Buka terminal atau command prompt dan navigasi ke direktori root projek anda di mana anda ingin mencipta fail `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Cipta Fail `.env`**: Guna editor teks pilihan anda untuk mencipta fail baru bernama `.env`. Jika anda menggunakan command line, anda boleh guna `touch` (untuk sistem berasaskan Unix) atau `echo` (untuk Windows):

   Sistem berasaskan Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit Fail `.env`**: Buka fail `.env` dalam editor teks (cth. VS Code, Notepad++, atau mana-mana editor lain). Tambah baris berikut ke dalam fail, gantikan `your_github_token_here` dengan token GitHub sebenar anda:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Simpan Fail**: Simpan perubahan dan tutup editor teks.

5. **Pasang `python-dotenv`**: Jika anda belum pasang, anda perlu pasang pakej `python-dotenv` untuk memuatkan pembolehubah persekitaran dari fail `.env` ke dalam aplikasi Python anda. Anda boleh pasang menggunakan `pip`:

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

🔐 Jangan pernah commit .env—ia sudah ada dalam .gitignore.
Arahan penuh untuk penyedia ada dalam [`providers.md`](03-providers.md).

## 4. Apa seterusnya?

| Saya mahu…           | Pergi ke…                                                                 |
|----------------------|---------------------------------------------------------------------------|
| Mula Pelajaran 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)       |
| Sediakan Penyedia LLM | [`providers.md`](03-providers.md)                                         |
| Berjumpa pelajar lain | [Sertai Discord kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Penyelesaian Masalah

| Simptom                                   | Penyelesaian                                                    |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Tambah Python ke PATH atau buka semula terminal selepas pasang  |
| `pip` tidak dapat bina wheels (Windows)   | `pip install --upgrade pip setuptools wheel` kemudian cuba lagi.|
| `ModuleNotFoundError: dotenv`             | Jalankan `pip install -r requirements.txt` (env belum dipasang).|
| Docker build gagal *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → tambah saiz cakera. |
| VS Code asyik minta buka semula           | Anda mungkin ada dua pilihan aktif; pilih satu (venv **atau** container)|
| Ralat OpenAI 401 / 429                    | Semak nilai `OPENAI_API_KEY` / had kadar permintaan.            |
| Ralat menggunakan Conda                   | Pasang pustaka AI Microsoft dengan `conda install -c microsoft azure-ai-ml`|

---

**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.