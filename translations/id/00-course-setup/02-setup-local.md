<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T18:15:01+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "id"
}
-->
# Setup Lokal 🖥️

**Gunakan panduan ini jika kamu ingin menjalankan semuanya di laptop sendiri.**  
Ada dua jalur: **(A) Python native + virtual-env** atau **(B) VS Code Dev Container dengan Docker**.  
Pilih yang paling mudah menurutmu—keduanya akan membawa ke materi yang sama.

## 1. Prasyarat

| Alat                | Versi / Catatan                                                                       |
|---------------------|---------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (unduh dari <https://python.org>)                                              |
| **Git**             | Terbaru (sudah ada di Xcode / Git for Windows / package manager Linux)                |
| **VS Code**         | Opsional tapi direkomendasikan <https://code.visualstudio.com>                        |
| **Docker Desktop**  | *Hanya* untuk Opsi B. Instal gratis: <https://docs.docker.com/desktop/>               |

> 💡 **Tip** – Cek alat di terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Opsi A – Python Native (paling cepat)

### Langkah 1  Clone repo ini

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Langkah 2 Buat & aktifkan virtual environment

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompt sekarang harus diawali dengan (.venv)—artinya kamu sudah masuk ke environment.

### Langkah 3 Instal dependensi

```bash
pip install -r requirements.txt
```

Lanjut ke Bagian 3 tentang [API keys](../../../00-course-setup)

## 2. Opsi B – VS Code Dev Container (Docker)

Kami menyiapkan repository dan kursus ini dengan [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) yang punya Universal runtime untuk mendukung pengembangan Python3, .NET, Node.js, dan Java. Konfigurasi terkait ada di file `devcontainer.json` di folder `.devcontainer/` pada root repository ini.

>**Kenapa pilih ini?**
>Lingkungan identik dengan Codespaces; tidak ada perbedaan dependensi.

### Langkah 0 Instal tambahan

Docker Desktop – pastikan ```docker --version``` berjalan.
VS Code Remote – ekstensi Containers (ID: ms-vscode-remote.remote-containers).

### Langkah 1 Buka repo di VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code akan mendeteksi .devcontainer/ dan menampilkan prompt.

### Langkah 2 Buka ulang di container

Klik “Reopen in Container”. Docker akan membangun image (sekitar 3 menit pertama kali).
Saat prompt terminal muncul, kamu sudah berada di dalam container.

## 2. Opsi C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) adalah installer ringan untuk memasang [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, dan beberapa paket.
Conda sendiri adalah package manager yang memudahkan setup dan berpindah antar [**virtual environment**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python dan paket. Juga berguna untuk menginstal paket yang tidak tersedia lewat `pip`.

### Langkah 0  Instal Miniconda

Ikuti [panduan instalasi MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) untuk setup.

```bash
conda --version
```

### Langkah 1 Buat virtual environment

Buat file environment baru (*environment.yml*). Jika kamu mengikuti lewat Codespaces, buat file ini di dalam direktori `.devcontainer`, jadi `.devcontainer/environment.yml`.

### Langkah 2  Isi file environment-mu

Tambahkan potongan berikut ke `environment.yml`-mu

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

### Langkah 3 Buat environment Conda-mu

Jalankan perintah di bawah ini di command line/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Lihat [panduan environment Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika mengalami masalah.

## 2 Opsi D – Jupyter Klasik / Jupyter Lab (di browser)

> **Untuk siapa ini?**  
> Siapa saja yang suka tampilan Jupyter klasik atau ingin menjalankan notebook tanpa VS Code.  

### Langkah 1  Pastikan Jupyter sudah terpasang

Untuk menjalankan Jupyter secara lokal, buka terminal/command line, masuk ke direktori kursus, lalu jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulai Jupyter dan URL untuk mengaksesnya akan muncul di jendela command line.

Setelah mengakses URL tersebut, kamu akan melihat outline kursus dan bisa membuka file `*.ipynb` mana saja. Contohnya, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Tambahkan API Key-mu

Menjaga keamanan API key sangat penting saat membangun aplikasi apapun. Kami sarankan untuk tidak menyimpan API key langsung di kode. Jika detail tersebut dikomit ke repository publik, bisa menimbulkan masalah keamanan dan bahkan biaya tak diinginkan jika disalahgunakan.
Berikut panduan langkah demi langkah membuat file `.env` untuk Python dan menambahkan `GITHUB_TOKEN`:

1. **Masuk ke Direktori Proyekmu**: Buka terminal atau command prompt dan masuk ke root direktori proyek tempat kamu ingin membuat file `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Buat File `.env`**: Gunakan text editor favoritmu untuk membuat file baru bernama `.env`. Jika lewat command line, bisa pakai `touch` (di sistem Unix) atau `echo` (di Windows):

   Sistem berbasis Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit File `.env`**: Buka file `.env` di text editor (misal VS Code, Notepad++, atau editor lain). Tambahkan baris berikut ke file, ganti `your_github_token_here` dengan token GitHub-mu yang sebenarnya:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Simpan File**: Simpan perubahan dan tutup text editor.

5. **Instal `python-dotenv`**: Jika belum, kamu perlu menginstal paket `python-dotenv` untuk memuat variabel environment dari file `.env` ke aplikasi Python-mu. Instal dengan `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Muat Variabel Environment di Script Python-mu**: Di script Python-mu, gunakan paket `python-dotenv` untuk memuat variabel environment dari file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Selesai! Kamu sudah berhasil membuat file `.env`, menambahkan token GitHub, dan memuatnya ke aplikasi Python-mu.

🔐 Jangan pernah commit .env—file ini sudah ada di .gitignore.
Instruksi lengkap tiap provider ada di [`providers.md`](03-providers.md).

## 4. Selanjutnya apa?

| Saya ingin…         | Lanjut ke…                                                                 |
|---------------------|----------------------------------------------------------------------------|
| Mulai Pelajaran 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)        |
| Setup LLM Provider  | [`providers.md`](03-providers.md)                                          |
| Bertemu peserta lain| [Gabung Discord kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Pemecahan Masalah

| Gejala                                    | Solusi                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Tambahkan Python ke PATH atau buka ulang terminal setelah instal |
| `pip` tidak bisa build wheels (Windows)   | `pip install --upgrade pip setuptools wheel` lalu coba lagi.    |
| `ModuleNotFoundError: dotenv`             | Jalankan `pip install -r requirements.txt` (env belum terpasang).|
| Docker build gagal *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → tambah ukuran disk. |
| VS Code terus meminta reopen              | Mungkin dua opsi aktif; pilih salah satu (venv **atau** container)|
| OpenAI 401 / 429 errors                   | Cek nilai `OPENAI_API_KEY` / batas request.                     |
| Error saat pakai Conda                    | Instal library AI Microsoft dengan `conda install -c microsoft azure-ai-ml`|

---

**Disclaimer**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.