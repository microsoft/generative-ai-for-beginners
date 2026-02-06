# Persediaan Tempatan 🖥️

**Gunakan panduan ini jika anda lebih suka menjalankan semuanya di komputer riba anda sendiri.**  
Anda mempunyai dua pilihan: **(A) Python asli + virtual-env** atau **(B) VS Code Dev Container dengan Docker**.  
Pilih mana-mana yang dirasakan lebih mudah—kedua-duanya membawa kepada pelajaran yang sama.

## 1.  Prasyarat

| Alat               | Versi / Nota                                                                        |
|--------------------|------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (dapatkan dari <https://python.org>)                                        |
| **Git**            | Terkini (datang bersama Xcode / Git untuk Windows / pengurus pakej Linux)          |
| **VS Code**        | Pilihan tetapi disyorkan <https://code.visualstudio.com>                           |
| **Docker Desktop** | *Hanya* untuk Pilihan B. Pemasangan percuma: <https://docs.docker.com/desktop/>    |

> 💡 **Petua** – Sahkan alat dalam terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Pilihan A – Python Asli (paling cepat)

### Langkah 1  Klon repositori ini

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Langkah 2 Cipta & aktifkan persekitaran maya

```bash
python -m venv .venv          # buat satu
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompt kini harus bermula dengan (.venv)—itu bermakna anda berada dalam persekitaran tersebut.

### Langkah 3 Pasang kebergantungan

```bash
pip install -r requirements.txt
```

Langkau ke Seksyen 3 mengenai [Kunci API](../../../00-course-setup)

## 2. Pilihan B – VS Code Dev Container (Docker)

Kami menyediakan repositori dan kursus ini dengan [kontena pembangunan](https://containers.dev?WT.mc_id=academic-105485-koreyst) yang mempunyai runtime Universal yang boleh menyokong pembangunan Python3, .NET, Node.js dan Java. Konfigurasi berkaitan ditakrifkan dalam fail `devcontainer.json` yang terletak di folder `.devcontainer/` di akar repositori ini.

>**Kenapa pilih ini?**  
>Persekitaran yang sama dengan Codespaces; tiada pergeseran kebergantungan.

### Langkah 0 Pasang tambahan

Docker Desktop – sahkan ```docker --version``` berfungsi.  
Sambungan VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Langkah 1 Buka repositori dalam VS Code

Fail ▸ Buka Folder…  → generative-ai-for-beginners

VS Code mengesan .devcontainer/ dan memaparkan prompt.

### Langkah 2 Buka semula dalam kontena

Klik “Buka semula dalam Kontena”. Docker membina imej (≈ 3 minit kali pertama).  
Apabila prompt terminal muncul, anda berada dalam kontena.

## 2.  Pilihan C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) adalah pemasang ringan untuk memasang [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, serta beberapa pakej.  
Conda sendiri adalah pengurus pakej, yang memudahkan penyediaan dan pertukaran antara [**persekitaran maya**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python dan pakej yang berbeza. Ia juga berguna untuk memasang pakej yang tidak tersedia melalui `pip`.

### Langkah 0  Pasang Miniconda

Ikuti [panduan pemasangan MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) untuk memasangnya.

```bash
conda --version
```

### Langkah 1 Cipta persekitaran maya

Cipta fail persekitaran baru (*environment.yml*). Jika anda mengikuti menggunakan Codespaces, cipta ini dalam direktori `.devcontainer`, iaitu `.devcontainer/environment.yml`.

### Langkah 2  Isikan fail persekitaran anda

Tambah petikan berikut ke dalam `environment.yml` anda

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

Jalankan arahan di bawah dalam baris arahan/terminal anda

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Laluan sub .devcontainer hanya terpakai kepada tetapan Codespace sahaja
conda activate ai4beg
```

Rujuk [panduan persekitaran Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jika anda menghadapi sebarang masalah.

## 2  Pilihan D – Jupyter Klasik / Jupyter Lab (dalam pelayar anda)

> **Siapa yang sesuai?**  
> Sesiapa yang suka antara muka Jupyter klasik atau mahu menjalankan notebook tanpa VS Code.  

### Langkah 1  Pastikan Jupyter dipasang

Untuk memulakan Jupyter secara tempatan, buka terminal/baris arahan, navigasi ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```

atau

```bash
jupyterhub
```

Ini akan memulakan instans Jupyter dan URL untuk mengaksesnya akan dipaparkan dalam tetingkap baris arahan.

Setelah anda mengakses URL tersebut, anda sepatutnya melihat garis panduan kursus dan boleh menavigasi ke mana-mana fail `*.ipynb`. Contohnya, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Tambah Kunci API Anda

Menjaga kunci API anda selamat dan terjamin adalah penting apabila membina sebarang jenis aplikasi. Kami mengesyorkan supaya tidak menyimpan sebarang kunci API secara langsung dalam kod anda. Melakukan komit ke repositori awam boleh mengakibatkan isu keselamatan dan juga kos yang tidak diingini jika digunakan oleh pihak yang tidak bertanggungjawab.  
Berikut adalah panduan langkah demi langkah tentang cara mencipta fail `.env` untuk Python dan menambah `GITHUB_TOKEN`:

1. **Navigasi ke Direktori Projek Anda**: Buka terminal atau command prompt dan navigasi ke direktori akar projek anda di mana anda ingin mencipta fail `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Cipta Fail `.env`**: Gunakan editor teks pilihan anda untuk mencipta fail baru bernama `.env`. Jika anda menggunakan baris arahan, anda boleh menggunakan `touch` (pada sistem berasaskan Unix) atau `echo` (pada Windows):

   Sistem berasaskan Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edit Fail `.env`**: Buka fail `.env` dalam editor teks (contohnya, VS Code, Notepad++, atau editor lain). Tambah baris berikut ke dalam fail, gantikan `your_github_token_here` dengan token GitHub sebenar anda:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Simpan Fail**: Simpan perubahan dan tutup editor teks.

5. **Pasang `python-dotenv`**: Jika anda belum memasangnya, anda perlu memasang pakej `python-dotenv` untuk memuatkan pembolehubah persekitaran dari fail `.env` ke dalam aplikasi Python anda. Anda boleh memasangnya menggunakan `pip`:

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

Itu sahaja! Anda telah berjaya mencipta fail `.env`, menambah token GitHub anda, dan memuatkannya ke dalam aplikasi Python anda.

🔐 Jangan sekali-kali komit .env—ia sudah ada dalam .gitignore.  
Arahan penuh penyedia terdapat dalam [`providers.md`](03-providers.md).

## 4. Apa seterusnya?

| Saya mahu…          | Pergi ke…                                                               |
|---------------------|-------------------------------------------------------------------------|
| Mula Pelajaran 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Sediakan Penyedia LLM | [`providers.md`](03-providers.md)                                       |
| Berjumpa pelajar lain | [Sertai Discord kami](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Penyelesaian Masalah

| Gejala                                    | Penyelesaian                                                    |
|-------------------------------------------|----------------------------------------------------------------|
| `python not found`                        | Tambah Python ke PATH atau buka semula terminal selepas pemasangan |
| `pip` tidak dapat bina roda (Windows)    | `pip install --upgrade pip setuptools wheel` kemudian cuba lagi. |
| `ModuleNotFoundError: dotenv`             | Jalankan `pip install -r requirements.txt` (persekitaran tidak dipasang). |
| Docker build gagal *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → tingkatkan saiz cakera. |
| VS Code terus meminta buka semula          | Anda mungkin mengaktifkan kedua-dua Pilihan; pilih satu (venv **atau** kontena) |
| Ralat OpenAI 401 / 429                    | Semak nilai `OPENAI_API_KEY` / had kadar permintaan.           |
| Ralat menggunakan Conda                   | Pasang perpustakaan Microsoft AI menggunakan `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->