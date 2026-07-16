# Pengaturan Lokal 🖥️

**Gunakan panduan ini jika Anda lebih suka menjalankan semuanya di laptop Anda sendiri.**   
Anda memiliki dua pilihan: **(A) Python native + virtual-env** atau **(B) VS Code Dev Container dengan Docker**.  
Pilih yang menurut Anda lebih mudah—keduanya mengarah ke pelajaran yang sama.

## 1. Persyaratan Awal

| Alat               | Versi / Catatan                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (dapatkan dari <https://python.org>)                                        |
| **Git**            | Terbaru (terminasuk dengan Xcode / Git untuk Windows / package manager Linux)      |
| **VS Code**        | Opsional tapi direkomendasikan <https://code.visualstudio.com>                     |
| **Docker Desktop** | *Hanya* untuk Opsi B. Instal gratis: <https://docs.docker.com/desktop/>            |

> 💡 **Tips** – Verifikasi alat di terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Opsi A – Python Native (paling cepat)

### Langkah 1 Clone repo ini

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Langkah 2 Buat & aktifkan lingkungan virtual

```bash
python -m venv .venv          # buat satu
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompt sekarang harus diawali dengan (.venv)—itu artinya Anda sudah berada di dalam lingkungan.

### Langkah 3 Instal dependensi

```bash
pip install -r requirements.txt
```

Langsung ke Bagian 3 tentang [API keys](#3-tambahkan-kunci-api-anda)

## 2. Opsi B – VS Code Dev Container (Docker)

Kami mengatur repositori dan kursus ini dengan [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) yang memiliki runtime Universal yang mendukung pengembangan Python3, .NET, Node.js, dan Java. Konfigurasi terkait didefinisikan dalam file `devcontainer.json` yang terletak di folder `.devcontainer/` pada akar repositori ini.

>**Kenapa memilih ini?**
>Lingkungan identik dengan Codespaces; tidak ada pergeseran dependensi.

### Langkah 0 Instal tambahan

Docker Desktop – pastikan ```docker --version``` berjalan.
VS Code Remote – ekstensi Containers (ID: ms-vscode-remote.remote-containers).

### Langkah 1 Buka repo di VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code mendeteksi .devcontainer/ dan memunculkan prompt.

### Langkah 2 Buka ulang dalam container

Klik “Reopen in Container”. Docker membangun image (≈ 3 menit pertama kali).
Ketika prompt terminal muncul, Anda sudah berada di dalam container.

## 2. Opsi C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) adalah installer ringan untuk memasang [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, serta beberapa paket.
Conda sendiri adalah manajer paket yang memudahkan pengaturan dan perpindahan antar [lingkungan virtual](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) dan paket Python berbeda. Ini juga berguna untuk memasang paket yang tidak tersedia melalui `pip`.

### Langkah 0 Instal Miniconda

Ikuti [panduan instalasi MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) untuk mengaturnya.

```bash
conda --version
```

### Langkah 1 Buat lingkungan virtual

Buat file lingkungan baru (*environment.yml*). Jika Anda mengikuti menggunakan Codespaces, buat di dalam direktori `.devcontainer`, jadi `.devcontainer/environment.yml`.

### Langkah 2 Isikan file lingkungan Anda

Tambahkan potongan berikut ke dalam `environment.yml`

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

### Langkah 3 Buat lingkungan Conda Anda

Jalankan perintah di bawah di command line/terminal Anda

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Sub path .devcontainer hanya berlaku untuk pengaturan Codespace saja
conda activate ai4beg
```

Rujuk ke [panduan lingkungan Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika mengalami masalah.

## 2 Opsi D – Jupyter / Jupyter Lab Klasik (di browser Anda)

> **Untuk siapa ini?**  
> Siapa saja yang menyukai antarmuka Jupyter klasik atau ingin menjalankan notebook tanpa VS Code.  

### Langkah 1 Pastikan Jupyter terpasang

Untuk memulai Jupyter secara lokal, buka terminal/command line, masuk ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulai instance Jupyter dan URL untuk mengaksesnya akan ditampilkan di jendela command line.

Setelah mengakses URL, Anda harus melihat garis besar kursus dan dapat menavigasi ke file `*.ipynb` mana pun. Misalnya, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Tambahkan Kunci API Anda

Menjaga kunci API Anda aman dan terlindungi penting saat membangun aplikasi jenis apa pun. Kami menyarankan agar tidak menyimpan kunci API langsung di kode Anda. Meng-commit detail tersebut ke repositori publik dapat menyebabkan masalah keamanan dan bahkan biaya yang tidak diinginkan jika digunakan oleh pihak yang tidak bertanggung jawab.
Berikut panduan langkah demi langkah cara membuat file `.env` untuk Python dan menambahkan kredensial Microsoft Foundry Models Anda:

> **Catatan:** GitHub Models (dan variabel `GITHUB_TOKEN`-nya) akan dihentikan akhir Juli 2026. Panduan ini menggunakan [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) sebagai gantinya. Ingin bekerja sepenuhnya offline? Lihat [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Pergi ke Direktori Proyek Anda**: Buka terminal atau command prompt dan masuk ke direktori root proyek Anda tempat Anda ingin membuat file `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Buat File `.env`**: Gunakan editor teks pilihan Anda untuk membuat file baru bernama `.env`. Jika menggunakan command line, Anda bisa menggunakan `touch` (pada sistem berbasis Unix) atau `echo` (pada Windows):

   Sistem berbasis Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit File `.env`**: Buka file `.env` di editor teks (misalnya VS Code, Notepad++, atau editor lain). Tambahkan baris berikut ke file, ganti placeholder dengan endpoint proyek Microsoft Foundry dan kunci API Anda yang sebenarnya:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Simpan File**: Simpan perubahan dan tutup editor teks.

5. **Pasang `python-dotenv`**: Jika belum, Anda perlu memasang paket `python-dotenv` untuk memuat variabel lingkungan dari file `.env` ke aplikasi Python Anda. Anda bisa memasangnya dengan `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Muat Variabel Lingkungan di Script Python Anda**: Di script Python Anda, gunakan paket `python-dotenv` untuk memuat variabel lingkungan dari file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Muat variabel lingkungan dari file .env
   load_dotenv()

   # Akses variabel Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Itu saja! Anda telah berhasil membuat file `.env`, menambahkan kredensial Microsoft Foundry Models Anda, dan memuatnya ke aplikasi Python Anda.

🔐 Jangan pernah commit .env—file itu sudah ada di .gitignore.
Instruksi lengkap dari provider tersedia di [`providers.md`](03-providers.md).

## 4. Selanjutnya?

| Saya ingin…          | Pergi ke…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Mulai Pelajaran 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Mengatur Penyedia LLM | [`providers.md`](03-providers.md)                                       |
| Bertemu pelajar lain | [Bergabung dengan Discord kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Pemecahan Masalah

| Gejala                                    | Solusi                                                         |
|------------------------------------------|----------------------------------------------------------------|
| `python not found`                        | Tambahkan Python ke PATH atau buka ulang terminal setelah install |
| `pip` tidak bisa membangun wheels (Windows) | `pip install --upgrade pip setuptools wheel` lalu coba lagi.    |
| `ModuleNotFoundError: dotenv`             | Jalankan `pip install -r requirements.txt` (lingkungan belum terpasang). |
| Build Docker gagal *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → tingkatkan ukuran disk. |
| VS Code terus minta buka ulang              | Anda mungkin mengaktifkan kedua Opsi; pilih salah satu (venv **atau** container) |
| OpenAI 401 / 429 error                    | Periksa nilai `OPENAI_API_KEY` / batas permintaan.             |
| Error pakai Conda                         | Pasang library Microsoft AI dengan `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->