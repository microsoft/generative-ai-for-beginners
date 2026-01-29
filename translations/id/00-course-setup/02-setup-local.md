# Pengaturan Lokal 🖥️

**Gunakan panduan ini jika Anda lebih suka menjalankan semuanya di laptop Anda sendiri.**  
Anda memiliki dua pilihan: **(A) Python native + virtual-env** atau **(B) VS Code Dev Container dengan Docker**.  
Pilih yang terasa lebih mudah—keduanya mengarah ke pelajaran yang sama.

## 1.  Prasyarat

| Alat               | Versi / Catatan                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (dapatkan dari <https://python.org>)                                            |
| **Git**            | Terbaru (termasuk dengan Xcode / Git untuk Windows / manajer paket Linux)             |
| **VS Code**        | Opsional tapi direkomendasikan <https://code.visualstudio.com>                        |
| **Docker Desktop** | *Hanya* untuk Opsi B. Instal gratis: <https://docs.docker.com/desktop/>               |

> 💡 **Tip** – Verifikasi alat di terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Opsi A – Python Native (paling cepat)

### Langkah 1  Clone repo ini

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Langkah 2 Buat & aktifkan virtual environment

```bash
python -m venv .venv          # buat satu
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompt sekarang harus dimulai dengan (.venv)—itu berarti Anda sudah berada di dalam env.

### Langkah 3 Instal dependensi

```bash
pip install -r requirements.txt
```

Langsung ke Bagian 3 tentang [API keys](../../../00-course-setup)

## 2. Opsi B – VS Code Dev Container (Docker)

Kami menyiapkan repositori dan kursus ini dengan [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) yang memiliki runtime Universal yang dapat mendukung pengembangan Python3, .NET, Node.js, dan Java. Konfigurasi terkait didefinisikan dalam file `devcontainer.json` yang terletak di folder `.devcontainer/` di root repositori ini.

>**Mengapa memilih ini?**  
>Lingkungan identik dengan Codespaces; tidak ada pergeseran dependensi.

### Langkah 0 Instal tambahan

Docker Desktop – pastikan ```docker --version``` berfungsi.  
Ekstensi VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Langkah 1 Buka repo di VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code mendeteksi .devcontainer/ dan menampilkan prompt.

### Langkah 2 Buka kembali dalam container

Klik “Reopen in Container”. Docker membangun image (≈ 3 menit pertama kali).  
Saat prompt terminal muncul, Anda sudah berada di dalam container.

## 2.  Opsi C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) adalah installer ringan untuk memasang [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, serta beberapa paket.  
Conda sendiri adalah manajer paket, yang memudahkan pengaturan dan pergantian antara berbagai [**virtual environment**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) dan paket Python. Ini juga berguna untuk memasang paket yang tidak tersedia melalui `pip`.

### Langkah 0  Instal Miniconda

Ikuti [panduan instalasi MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) untuk mengaturnya.

```bash
conda --version
```

### Langkah 1 Buat virtual environment

Buat file environment baru (*environment.yml*). Jika Anda mengikuti menggunakan Codespaces, buat ini di dalam direktori `.devcontainer`, jadi `.devcontainer/environment.yml`.

### Langkah 2  Isi file environment Anda

Tambahkan potongan berikut ke `environment.yml` Anda

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

### Langkah 3 Buat environment Conda Anda

Jalankan perintah di bawah ini di command line/terminal Anda

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # sub path .devcontainer hanya berlaku untuk pengaturan Codespace saja
conda activate ai4beg
```

Lihat [panduan environment Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika Anda mengalami masalah.

## 2  Opsi D – Jupyter Klasik / Jupyter Lab (di browser Anda)

> **Untuk siapa ini?**  
> Siapa saja yang menyukai antarmuka Jupyter klasik atau ingin menjalankan notebook tanpa VS Code.  

### Langkah 1  Pastikan Jupyter terpasang

Untuk memulai Jupyter secara lokal, buka terminal/command line, navigasi ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulai instance Jupyter dan URL untuk mengaksesnya akan ditampilkan di jendela command line.

Setelah Anda mengakses URL tersebut, Anda harus melihat garis besar kursus dan dapat menavigasi ke file `*.ipynb` mana pun. Misalnya, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Tambahkan API Keys Anda

Menjaga API keys Anda tetap aman dan terlindungi penting saat membangun aplikasi apa pun. Kami menyarankan untuk tidak menyimpan API keys langsung di kode Anda. Meng-commit detail tersebut ke repositori publik dapat menyebabkan masalah keamanan dan bahkan biaya yang tidak diinginkan jika digunakan oleh pihak yang tidak bertanggung jawab.  
Berikut panduan langkah demi langkah tentang cara membuat file `.env` untuk Python dan menambahkan `GITHUB_TOKEN`:

1. **Navigasi ke Direktori Proyek Anda**: Buka terminal atau command prompt dan navigasi ke direktori root proyek Anda di mana Anda ingin membuat file `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Buat File `.env`**: Gunakan editor teks favorit Anda untuk membuat file baru bernama `.env`. Jika menggunakan command line, Anda dapat menggunakan `touch` (pada sistem berbasis Unix) atau `echo` (pada Windows):

   Sistem berbasis Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit File `.env`**: Buka file `.env` di editor teks (misalnya, VS Code, Notepad++, atau editor lain). Tambahkan baris berikut ke file, ganti `your_github_token_here` dengan token GitHub Anda yang sebenarnya:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Simpan File**: Simpan perubahan dan tutup editor teks.

5. **Instal `python-dotenv`**: Jika belum, Anda perlu memasang paket `python-dotenv` untuk memuat variabel lingkungan dari file `.env` ke aplikasi Python Anda. Anda dapat memasangnya menggunakan `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Muat Variabel Lingkungan di Skrip Python Anda**: Dalam skrip Python Anda, gunakan paket `python-dotenv` untuk memuat variabel lingkungan dari file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Muat variabel lingkungan dari file .env
   load_dotenv()

   # Akses variabel GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Selesai! Anda telah berhasil membuat file `.env`, menambahkan token GitHub Anda, dan memuatnya ke aplikasi Python Anda.

🔐 Jangan pernah commit .env—file ini sudah ada di .gitignore.  
Instruksi lengkap penyedia ada di [`providers.md`](03-providers.md).

## 4. Apa selanjutnya?

| Saya ingin…          | Pergi ke…                                                               |
|---------------------|-------------------------------------------------------------------------|
| Mulai Pelajaran 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Mengatur Penyedia LLM | [`providers.md`](03-providers.md)                                       |
| Bertemu pelajar lain | [Bergabung dengan Discord kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Pemecahan Masalah

| Gejala                                   | Solusi                                                          |
|-----------------------------------------|-----------------------------------------------------------------|
| `python not found`                      | Tambahkan Python ke PATH atau buka kembali terminal setelah instalasi |
| `pip` tidak bisa membangun wheels (Windows) | `pip install --upgrade pip setuptools wheel` lalu coba lagi.    |
| `ModuleNotFoundError: dotenv`           | Jalankan `pip install -r requirements.txt` (env belum terpasang).|
| Docker build gagal *No space left*      | Docker Desktop ▸ *Settings* ▸ *Resources* → tingkatkan ukuran disk. |
| VS Code terus meminta untuk membuka ulang | Anda mungkin mengaktifkan kedua Opsi; pilih salah satu (venv **atau** container) |
| OpenAI 401 / 429 errors                 | Periksa nilai `OPENAI_API_KEY` / batas permintaan.               |
| Error menggunakan Conda                  | Pasang pustaka Microsoft AI menggunakan `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->